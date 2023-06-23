#!/bin/bash

path1=~/media/kenz/1B8D1A637BBA134B/bcsd-final   # path to  observed data
path2=~/media/kenz/1B8D1A637BBA134B/bcsd-final   # path to future data
path3=~/media/kenz/1B8D1A637BBA134B/bcsd-final   # path to historical modelled data


input1=${path1}/Ghana_ERA5_dTn_1981_2020.nc
input2=${path2}/Ghana_ERA5_dTx_1981_2020.nc
input3=${path3}/tasmax_GHA-22_MOHC-HadGEM2-ES_rcp26_r1i1p1_ICTP-RegCM4-7_v0_day_20060101-20991230.nc

input4=${path3}/tasmax_GHA-22_MOHC-HadGEM2-ES_rcp85_r1i1p1_ICTP-RegCM4-7_v0_day_20060101-20991230.nc

cdo ensmean $input1 $input2 o.nc
cdo -sellonlatbox,-1.5,1.5,5,12 -remapbil,$input4$ o.nc obs.nc

rm o.nc

python3 bias.py obs.nc $input3 $input4 bc_data.nc


