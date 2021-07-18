# program to plot the max pr day 
import os
from netCDF4 import Dataset as NetCDFFile
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
import numpy as np 
os.system('mkdir -p plots')
dir_2_nc="/p/tmp/fallah/out_era5_masked/"
k = 0
for year in range(1979,2020):
    # read the model data: 
    nc = NetCDFFile(dir_2_nc+'file'+str(year)+'.nc')
    lats = nc.variables['latitude'][:]
    lons = nc.variables['longitude'][:]
    mask = nc.variables['pr'][:]
    nc.close()
    # remove negative
    masks = mask.data.astype(float)
    masks[masks<0]=np.nan
    max_value = np.nanmax(masks)
    max_index = np.where(masks == max_value)
    fig = plt.figure('1')
    fig.set_size_inches(16, 8)
    date = np.linspace(1979,2020,14965)
    plt.bar(date[(k*365) + max_index[0]],max_value*1000,color='lightgrey', alpha=.5)
    plt.scatter(date[(k*365)+max_index[0]],max_value*1000, s= 40, color='r')

    plt.xlim([1978,2020])
    plt.ylim([0,140])

    plt.xlabel('year', fontsize=20)
    plt.ylabel('maximum precipitation [mm/day]', fontsize=20)
    if year == 1979 :
        plt.savefig("plots/year"+str(year)+"_time_series.png", bbox_inches = 'tight',
                pad_inches = 0, transparent=False);
    else:
        plt.savefig("plots/year"+str(year)+"_time_series.png", bbox_inches = 'tight',
                pad_inches = 0, transparent=True);


    plt.close()

    # plot the maps : 
    fig = plt.figure('1')
    fig.set_size_inches(8, 10)
    my_map = Basemap(projection='cyl', 
                    llcrnrlat=47, llcrnrlon=5,
                    urcrnrlat=55, urcrnrlon=15,
                    resolution='l', area_thresh=1.0)
    #my_map = Basemap(projection='mill',llcrnrlat=47,urcrnrlat=55,\
    #            llcrnrlon=5,urcrnrlon=15,resolution='c')
    if year == 1979 :
        my_map.fillcontinents(color='wheat', zorder=-1)
    
    my_map.drawcountries(linewidth=2)
    my_map.drawcoastlines()
    lons_m, lats_m = my_map(lons, lats)

    # plot
    index1 = max_index[1][0]
    index2 = max_index[2][0]

    my_map.scatter(lons_m[index2], lats_m[index1] ,s=200, color='red', zorder=1, alpha=1)
    parallels = np.arange(-90.,90,2.5)
    # labels = [left,right,top,bottom]
    my_map.drawparallels(parallels,labels=[False,True,True,False], fontsize=20)
    meridians = np.arange(0.,360.,2.5)
    my_map.drawmeridians(meridians,labels=[True,False,False,True], fontsize=20)
    plt.savefig("plots/year"+str(year)+".png", bbox_inches = 'tight',
        pad_inches = 0, transparent=True);
    plt.close()
    k += 1
