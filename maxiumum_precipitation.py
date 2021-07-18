# program to plot maxiumum precipitation per day with location
import os
from netCDF4 import Dataset as NetCDFFile
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
import numpy as np 
country="DEU"
out="/p/tmp/fallah/out_era5_masked/"
cmd = "mkdir -p "+out
os.system(cmd)

#sample = "/p/tmp/fallah/pr_1hr_ECMWF-ERA5_observation_2019010100-2019123123.nc"
for year in range(1979,2020):
    
    if year == 2019:
        sample = "/p/tmp/fallah/pr_1hr_ECMWF-ERA5_observation_2019010100-2019123123.nc"
        cmd = "cdo -O -b F32 mul "+country+"_adm0_mask_array_era5_global.nc -daysum -selname,pr "+\
            sample+" "+out+"file"+str(year)+".nc"
        os.system(cmd)

    elif year == 1979 :
        sample= "/p/projects/climate_data_central/reanalysis/ERA5/pr/pr_1hr_ECMWF-ERA5_observation_1979010107-1979123123.nc"
        print(year)
        cmd = "cdo -O -b F32 mul "+country+"_adm0_mask_array_era5_global.nc -daysum -selname,pr "+\
            sample+" "+out+"file"+str(year)+".nc"
        os.system(cmd)
    else:
        sample = "/p/projects/climate_data_central/reanalysis/ERA5/pr/pr_1hr_ECMWF-ERA5_observation_"+\
            str(year)+"010100-"+str(year)+"123123.nc"
        cmd = "cdo -O -b F32 mul "+country+"_adm0_mask_array_era5_global.nc -daysum -selname,pr "+\
            sample+" "+out+"file"+str(year)+".nc"
        os.system(cmd)



