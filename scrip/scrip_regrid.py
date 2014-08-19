# Import regrid2 package for regridder functions
import regrid2, cdms2 
import regrid2, cdms2 , sys, os
# Get the source variable
data_pth = os.path.join(os.path.dirname(sys.argv[0]),"..","data")
fnm = os.path.join(data_pth,"ps_ne120.nc")
fnm_grid = os.path.join(data_pth,"ne120np4_pentagons_100310.nc")
fweights = os.path.join(data_pth,"ne120_to_t85.wgts.nc")
print fweights
f = cdms2.open(fnm)
dat = f('PS')
f.close()

f=cdms2.open("crap.nc","w")
f.write(dat)
f.close()
# Read the regridder from the remapper file
remapf = cdms2.open(fweights)
regridf = regrid2.readRegridder(remapf)
remapf.close()

print dir(regridf)
s = regridf(dat)
print s.shape

# Regrid the source va
