
import regrid2, cdms2 , sys, os
# Get the source variable
data_pth = os.path.join(os.path.dirname(sys.argv[0]),"..","data")

data_pth = os.path.join(sys.prefix,"sample_data")

fnm = os.path.join(data_pth,"sampleCurveGrid4.nc")
fnm2  = os.path.join(data_pth,"clt.nc")

f=cdms2.open(fnm)
s=f("sample")

f2=cdms2.open(fnm2)
s2=f2("clt")

diag = {}

s3=s.regrid(s2.getGrid(),diag=diag)

print s3.shape
print diag
