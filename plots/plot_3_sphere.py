import numpy
import regrid2, cdms2 , sys, os
# Get the source variable
data_pth = os.path.join(os.path.dirname(sys.argv[0]),"..","data")
fnm = os.path.join(data_pth,"ps_ne120.nc")
fnm_grid = os.path.join(data_pth,"ne120np4_pentagons_100310.nc")

f=cdms2.open(fnm)
fg=cdms2.open(fnm_grid)
print "FILE VARS:", f.variables.keys()
print "GRD FILE VARS:", fg.variables.keys()

ps = f["PS"]#(slice(200000,300000))
ps=ps().filled()
print "INPUT SHP:",ps.shape

blon = fg("grid_corner_lon")
blat = fg("grid_corner_lat")
imsk = fg("grid_imask")
print "MASK SHAPE",imsk.shape,imsk.max(),imsk.min()
print "BOUNDS LON SHP:",blon.shape

mesh = numpy.array((blat,blon))
mesh=numpy.transpose(mesh,(1,0,2))
print mesh.shape
#mesh=mesh[200000:300000]

print "PRINT MESH SHAPE:",mesh.shape
print "MESH DOMAIN:"
print mesh[:,0].max(),mesh[:,0].min()
print mesh[:,1].max(),mesh[:,1].min()



import vcs

x=vcs.init()
m=x.createmeshfill()
m.datawc_x1=-120+360.
m.datawc_x2=-50+360.
m.datawc_y1=25
m.datawc_y2=50
m.wrap=[0,360.]
x.plot(ps,mesh,m)
x.png("mesh")
raw_input("Press enter")
