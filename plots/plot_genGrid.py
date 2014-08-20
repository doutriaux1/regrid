import numpy
import regrid2, cdms2 , sys, os
# Get the source variable
import vcs
f=cdms2.open(os.path.join(sys.prefix,"sample_data","sampleGenGrid3.nc"))
s=f("sample")
mesh =s.getGrid().getMesh()

x=vcs.init()
m=x.createmeshfill()
m.datawc_x1=-120+360.
m.datawc_x2=-50+360.
m.datawc_y1=25
m.datawc_y2=50
m.wrap=[0,360.]
x.plot(s,mesh,m)
x.png("mesh")
raw_input("Press enter")
