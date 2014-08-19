
# Import regrid2 package for regridder functions
import regrid2, cdms2 , sys, os
import cdutil

# Get the source variable
data_pth = os.path.join(os.path.dirname(sys.argv[0]),"..","data")
fnm = os.path.join(data_pth,"ps_ne120.nc")
fnm_grid = os.path.join(data_pth,"ne120np4_pentagons_100310.nc")
f = cdms2.open(fnm)
dat = f('PS')
f.close()

f = cdms2.open(fnm_grid)
area_in = f("grid_area")
area_in.info()

print "SUM IN WTS:",area_in.sum()

f=cdms2.open(os.path.join(sys.prefix,"sample_data","clt.nc"))
out=f("clt",slice(0,1),squeeze=1)

area_out = cdutil.area_weights(out)*5.112E14
area_out.units = "m**2"
print area_out.sum()


import ESMP
mthd = ESMP.ESMP_REGRIDMETHOD_CONSERVE
diags = {
        "srcGridshape":area_in.shape,
        "dstGridshape":area_out.shape,
        "srcAreaFractions" : area_in,
        "sdstreaFractions" : area_out,
        "regridMethod":mthd,
        "staggerLoc" : "center",
        "periodicity":0,
        "coordSys":"deg",
        "dtype":area_in.dtype,
        }


#    def __init__(self, srcGridshape, dstGridshape, dtype,
#                 regridMethod, staggerLoc, periodicity, coordSys,
#                 srcGridMask = None, hasSrcBounds = False, srcGridAreas = None,
#                 dstGridMask = None, hasDstBounds = False, dstGridAreas = None,
#                 **args):
ER = regrid2.ESMFRegrid(**diags)
s= ER(dat)

print s.hape

