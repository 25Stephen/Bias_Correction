#!/bin/bash

cd data2
ghana='ghana_rainfall_1981_2015.nc'
chirps='chirps_dgh_1981_2015.nc'
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

python ../merra_prism_e.py $ghana_upscaled chirps_filled.nc pr precip chirps_bc.nc

cdo griddes ghana_rainfall_1981_2015.nc > ghana_grid
cdo remapbil,ghana_grid chirps_bc.nc chirps_bc_interp.nc
cdo remapbil,ghana_grid ghana_upscaled.nc ghana_reinterpolated.nc


cdo ydayavg ghana_reinterpolated.nc ghana_interpolated_ydayavg.nc
cdo ydayavg ghana_rainfall_1981_2015.nc ghana_ydayavg.nc
cdo div ghana_ydayavg.nc ghana_interpolated_ydayavg.nc sf.nc


cdo setmisstonn sf.nc scale_factors.nc

#python ../spatial_s.py chirps_bc_interp.nc scale_factors.nc final_bcsd.nc


exit
