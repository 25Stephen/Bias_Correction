from __future__ import annotations
from xclim import sdba
import cftime
import matplotlib.pyplot as plt
import nc_time_axis
import numpy as np
import xarray as xr
import warnings
warnings.filterwarnings('ignore')


# var = str(input('tasmax or precip, '))
var = 'tasmax'

ds = xr.open_dataset('out.nc')
ds = ds.rename({'mx2t':'tasmax'})

w = []
for i in ds.lat.values:
    w.append(i[1])
    
ds = ds.drop_vars('y').drop_vars('x')
ds.coords['y']=w
ds.coords['x']=ds.lon.values[1]
ds = ds[var].drop_vars('lon').drop_vars('lat')
ds = ds.rename({'x':'lon', 'y':'lat'})

# ds = xr.open_dataset('Ghana_ERA5_dTx_1981_2020.nc')
# ds = ds.rename({'mx2t':'tasmax', 'longitude':'lon', 'latitude':'lat'})
# ds_t = (ds_tn + ds_tn)/2
rcp26 = xr.open_dataset('tasmax_GHA-22_MOHC-HadGEM2-ES_rcp26_r1i1p1_ICTP-RegCM4-7_v0_day_20060101-20991230.nc')
rcp85 = xr.open_dataset('tasmax_GHA-22_MOHC-HadGEM2-ES_rcp85_r1i1p1_ICTP-RegCM4-7_v0_day_20060101-20991230.nc')
hist = xr.open_dataset('tasmax_GHA-22_MOHC-HadGEM2-ES_historical_r1i1p1_ICTP-RegCM4-7_v0_day_19710101-20041230.nc')

# var = 'tasmax'
v = []
for i in hist.lat.values:
    v.append(i[1])
    
def pro_data(data):
    hist = data.drop_vars('y').drop_vars('x')
    # ds_rcp = ds_rcp.drop_vars('lon').drop_vars('lat')
    hist.coords['y']=v
    hist.coords['x']=hist.lon.values[1]
    hist = hist[var].drop_vars('lon').drop_vars('lat')
    hist = hist.rename({'x':'lon', 'y':'lat'})
    return(hist)

rcp26=pro_data(rcp26)
rcp85=pro_data(rcp85)

hist=pro_data(hist)

#set extent
wesn = [-3, 1.5, 5, 12]
   
if var == 'precip':
    ds_meas_flt = ds.sel(time=~((ds.time.dt.dayofyear == 366)))[var]
else:
    ds_meas_flt = ds.sel(time=~((ds.time.dt.dayofyear == 366)))+273.13

#Filter data
#############################################################################################################
ds_meas_flt = ds_meas_flt.sel(lon = slice(wesn[0], wesn[1]), lat = slice(wesn[2], wesn[3]))

# ds_meas_flt = ds_meas_flt.convert_calendar('360_day', align_on = 'date' , use_cftime=True)

ds_hist_flt = hist.sel(lon = slice(wesn[0], wesn[1]), lat = slice(wesn[2], wesn[3]))
# ds_hist_flt = ds_hist_flt.convert_calendar('proleptic_gregorian',align_on='year')

# ds_hist_flt = ds_hist.sel(time=~((ds_hist.time.dt.month == 2) & (ds_hist.time.dt.day == 29)))
ds_rcp_flt_26 = rcp26.sel(lon = slice(wesn[0], wesn[1]), lat = slice(wesn[2], wesn[3]))
# ds_rcp_flt_26 = ds_rcp_flt_26.convert_calendar('proleptic_gregorian',align_on='year')

ds_rcp_flt_85 = rcp85.sel(lon = slice(wesn[0], wesn[1]), lat = slice(wesn[2], wesn[3]))

#Allign time
############################################################################################################

################### Here we have the fuctions used for computations ##############################3

###This funtion coverts the data into a standard date time
def _cfnoleap_to_datetime(da):
    da_std = da.convert_calendar("standard", use_cftime=True, align_on='year')
    datetimeindex = da_std.indexes['time'].to_datetimeindex()
    ds = da#.to_dataset()
    ds['time_dt']= ('time', datetimeindex)
    ds = ds.swap_dims({'time': 'time_dt'})
    assert len(da.time) == len(ds.time_dt)
    return ds


# if var == 'precip':
#     ds_hist_dt = _cfnoleap_to_datetime(ds_hist_flt)*86400
#     ds_rcp_dt = _cfnoleap_to_datetime(ds_rcp_flt)*86400
# else:
#     ds_hist_dt = _cfnoleap_to_datetime(ds_hist_flt)
#     ds_rcp_dt = _cfnoleap_to_datetime(ds_rcp_flt)
if var == 'precip':
    ds_hist_dt = _cfnoleap_to_datetime(ds_hist_flt)*86400
    ds_rcp_dt_26 = _cfnoleap_to_datetime(ds_rcp_flt_26)*86400
    ds_rcp_dt_85 = _cfnoleap_to_datetime(ds_rcp_flt_85)*86400

else:
    ds_hist_dt = _cfnoleap_to_datetime(ds_hist_flt)
    ds_rcp_dt_26 = _cfnoleap_to_datetime(ds_rcp_flt_26)
    ds_rcp_dt_85 = _cfnoleap_to_datetime(ds_rcp_flt_85)
##################################################################################################################

# ############################# Preprocess the dataset to suit the model ####################################

ref = ds_meas_flt
ref.attrs['units']='K'
    
rcp26 = ds_rcp_dt_26.drop_vars('time').rename({'time_dt':'time'})
rcp26.attrs['units']='K'

rcp85 = ds_rcp_dt_85.drop_vars('time').rename({'time_dt':'time'}).sel(time=slice('2023','2100'))
rcp85.attrs['units']='K'

hist_mod = ds_hist_dt.drop_vars('time').rename({'time_dt':'time'})
hist_mod.attrs['units']='K'

hist_r_add=rcp26.sel(time=slice('2022'))
hist_mod = xr.combine_by_coords([hist_r_add,hist_mod])[var]

rcp26=rcp26.sel(time=slice('2023','2100'))

QM = sdba.EmpiricalQuantileMapping.train(
    ref, hist_mod, nquantiles=15, group="time", kind="+"
)
scen = QM.adjust(rcp26, extrapolation="constant", interp="nearest")

rcp26_data = QM.adjust(rcp26, extrapolation="constant", interp="nearest")

rcp85_data = QM.adjust(rcp85, extrapolation="constant", interp="nearest")

