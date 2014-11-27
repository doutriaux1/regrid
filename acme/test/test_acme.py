import acme_regridder,os
import cdms2
import acme_regridder._regrid
import numpy
value = 0

cdms2.setNetcdfShuffleFlag(value) ## where value is either 0 or 1
cdms2.setNetcdfDeflateFlag(value) ## where value is either 0 or 1
cdms2.setNetcdfDeflateLevelFlag(value) ## where value is a integer between 0 and 9 included

f=cdms2.open("../data/ne120_to_t85.wgts.nc")
S=f("S")
row=f("row")
col=f("col")
frac_b=f("frac_b")
mask_b=f("mask_b")

f2 = cdms2.open("../data/ps_ne120.nc")
ps = f2("PS")
print ps.shape,ps.dtype
print S.shape,S.dtype
print frac_b.shape,frac_b.dtype
print mask_b.shape,mask_b.dtype
print row.shape,row.dtype
print col.shape,col.dtype
## First make up a bigger array for testing purposes
axes = ps.getAxisList()
ps=ps.filled()
sh = list(ps.shape)
sh.insert(0,1)
ps.shape = sh

if not os.path.exists("crap.nc"):
  for i in range(7):
    ps=numpy.concatenate((ps,ps),axis=0)
  print "NEW PS SHAPE:",ps.shape
  for i in range(4):
    ps=numpy.concatenate((ps,ps),axis=1)
  print "NEW PS SHAPE:",ps.shape
  f=cdms2.open("crap.nc","w")
  f.write(ps,id="PS")
else:
  f=cdms2.open("crap.nc")
  ps=f("PS").filled()
  #ps=ps.astype("l")
print "PS SHAPE:",ps.shape


import time
print "REGRIDDING"
t1=time.time()
out = acme_regridder._regrid.apply_weights(ps,S.filled(),row.filled(),col.filled(),frac_b.filled())
t2=time.time()
print "time:",t2-t1
print out.shape
f=cdms2.open("out.nc","w")
f.write(out,id="PS",dtype=ps.dtype)
f.close()
fok = "ok_%s.nc" % ps.dtype
if os.path.exists(fok):
    f=cdms2.open(fok)
    ok=f("ok")
    f.close()
    d = out-ok
    print "MIN,MAX:",d.min(),d.max()
else:
    f=cdms2.open(fok,"w")
    f.write(out,id="ok",dtype=ps.dtype)
    f.close()


