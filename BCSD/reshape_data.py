import xarray as xr

observed = xr.open_dataset('/home/kenz/Documents/bcsd-final/data2/Ghana_chirps.nc')
modelled =xr.open_dataset('/home/kenz/Documents/bcsd-final/data2/mo.nc')

modelled = modelled.sel(time = slice('1981', '2005'))
observed = observed.sel(time = slice('1981', '2005'))

#modelled = modelled.rename({'rlon':'longitude', 'rlat':'latitude'})
modelled = modelled.sel(lon = slice(1.5,3.5), lat = slice(4.5,12.5))

modelled.to_netcdf('../../bcsd-final/data2/modelled.nc')
observed.to_netcdf('../../bcsd-final/data2/observed_data.nc')

