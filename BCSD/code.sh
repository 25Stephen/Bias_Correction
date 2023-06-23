#!/bin/bash

cd data2
cdo remapcon,r1440x720 pr_GHA-22_MPI-M-MPI-ESM-LR_historical_r1i1p1_GERICS-REMO2015_v1_day_19710101-20051231.nc mo.nc #### reshape data to 0.25x0.25

#python ../reshape_data.py

#cdo -mulc,86400. modelled.nc modelled_data.nc  ##covert to mm/day


#obser='observed_data.nc'
#modelled='modelled_data.nc'

#rm modelled.nc

#ghana_upscaled='ghana_upscaled.nc'
#chirps_filled='chirps_filled.nc'

#cdo griddes $obser > obser_grid




#cdo setmissval,nan $ghana temp_miss.nc
#cdo fillmiss temp_miss.nc tmp.nc
#cdo setmissval,-9999 tmp.nc tmp_filled.nc

#########################################################################


#cdo remapbil,obser_grid modelled.nc $ghana_upscaled
##cdo remapbil,chirps_grid -gridboxmean,3,3 tmp_filled.nc $ghana_upscaled
#cdo fillmiss $modelled $chirps_filled
#tmp_filled.nc

#python ../merra_prism_e.py $ghana_upscaled chirps_filled.nc var1 precip chirps_bc.nc
#
#cdo griddes observed_data.nc > ghana_grid
#cdo remapbil,ghana_grid chirps_bc.nc chirps_bc_interp.nc
#cdo remapbil,ghana_grid ghana_upscaled.nc ghana_reinterpolated.nc
#
#
#cdo ydayavg ghana_reinterpolated.nc ghana_interpolated_ydayavg.nc
#cdo ydayavg ghana_rainfall_1981_2015.nc ghana_ydayavg.nc
#cdo div ghana_ydayavg.nc ghana_interpolated_ydayavg.nc sf.nc
#
#
#cdo setmisstonn sf.nc scale_factors.nc
#
#python ../spatial_s.py chirps_bc_interp.nc scale_factors.nc final_bcsd.nc
#
#
exit
