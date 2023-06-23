import os
import time
import xarray as xr
#observed = xr.open_dataset('Ghana_chirps.nc')
#modelled =xr.open_dataset('pr_GHA-22_MPI-M-MPI-ESM-LR_historical_r1i1p1_GERICS-REMO2015_v1_day_19710101-20051231.nc')
#modelled = modelled.sel(time = slice('1981', '2005'))
#observed = observed.sel(time = slice('1981', '2005'))
#modelled = modelled.rename({'lon':'longitude', 'lat':'latitude'})
#modelled = modelled.rename({'rlon':'lon', 'rlat':'lat'})
#modelled_ = modelled.sel(lon = slice(-3.5,1.5), lat = slice(4.5,12.5))
#observed.to_netcdf('observed_data.nc')
#modelled.to_netcdf('modelled.nc')
