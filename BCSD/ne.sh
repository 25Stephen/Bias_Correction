#!/bin/bash


cd data2
ghana='observed_data.nc'
chirps='modelled_data.nc'
ghana_upscaled='ghana_upscaled.nc'
chirps_filled='chirps_filled.nc'


cdo griddes $chirps > chirps_grid

cdo setmissval,nan $ghana temp_miss.nc
cdo fillmiss temp_miss.nc tmp.nc
cdo setmissval,-9999 tmp.nc tmp_filled.nc
cdo remapbil,chirps_grid tmp_filled.nc $ghana_upscaled
#cdo remapbil,chirps_grid -gridboxmean,3,3 tmp_filled.nc $ghana_upscaled
cdo fillmiss $chirps $chirps_filled
#tmp_filled.nc

python ../merra_prism_e.py $ghana_upscaled chirps_filled.nc precip pr chirps_bc.nc


cdo griddes observed_data.nc > ghana_grid

## ncatted -O -a units,lat,c,c,"degrees north" -a units,lon,c,c,"degrees east" mygrid.nc
## ncatted -O -a units,lat,c,c,"degrees north" -a units,lon,c,c,"degrees east" frac.nc
## cdo -remapbil,mygrid.nc frac.nc fracout.nc
cdo selvar,bias_corrected chirps_bc.nc chirps_b
cdo remapbil,ghana_grid chirps_b.nc chirps_bc_interp.nc
cdo remapbil,ghana_grid ghana_upscaled.nc ghana_reinterpolated.nc


cdo ydayavg ghana_reinterpolated.nc ghana_interpolated_ydayavg.nc
cdo ydayavg observed_data.nc ghana_ydayavg.nc
cdo div ghana_ydayavg.nc ghana_interpolated_ydayavg.nc sf.nc

cdo setmisstonn sf.nc scale_factors.nc

python ../spatial_s.py chirps_bc_interp.nc scale_factors.nc final_bcsd.nc

cd /home/kenz/Documents/bcsd-final/data2/ 
rm temp_miss.nc tmp.nc tmp_filled.nc chirps_filled.nc chirps_grid ghana_grid ghana_upscaled.nc chirps_bc_interp.nc ghana_interpolated_ydayavg.nc scale_factors sf.nc ghana_reinterpolated.nc ghana_ydayavg.nc 

exit
