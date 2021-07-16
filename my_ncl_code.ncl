load "shapefile_utils.ncl"  ;-- load additional lib
        
shp_name  = "CCC_adm0.shp" ;-- shapefile name
mask_name = "CCC_adm0_mask_array_0.1x0.1deg_global.nc"   ;-- output mask file name
        
       
;-- Open grid file and read the variable
f = addfile("topo_0.1x0.1deg_global.nc","r")
v     = f->topo
v@lat = f->lat
v@lon = f->lon
        
;-- resources for the shapefile_mask_data function
opt = True
opt@return_mask = True    ;-- this forces the return of a 0s and 1s mask array
opt@delta_kilometers = 300
          
;-- create the mask based on the given shapefile; add coordinates
mask_array         =  shapefile_mask_data(v, shp_name, opt)
mask_array!0       = "lat"
mask_array!1       = "lon"
mask_array&lat     =  f->lat
mask_array&lon     =  f->lon
mask_array@comment = "Mask shapefile: CCC_adm/CCC_adm0.shp"
        
;-- set value 0 to missing value
mask_array = where(mask_array .eq. 1, mask_array, mask_array@_FillValue)
        
;-- delete, create, and write mask array to new file
system("rm -f " + mask_name)
fout = addfile(mask_name,"c")
fout->mask_array = mask_array