# Import regrid2 package for regridder functions
import regrid2, cdms2 
import regrid2, cdms2 , sys, os
import numpy
# Get the source variable
data_pth = os.path.join(os.path.dirname(sys.argv[0]),"..","data")
fnm = os.path.join(data_pth,"ps_ne120.nc")
fnm_grid = os.path.join(data_pth,"ne120np4_pentagons_100310.nc")
fweights = os.path.join(data_pth,"ne120_to_t85.wgts.nc")
print fweights
f = cdms2.open(fnm)
dat = f('PS')
f.close()

# Read the regridder from the remapper file
remapf = cdms2.open(fweights)
#regridf = regrid2.readRegridder(remapf)

#print dir(regridf)
#s = regridf(dat)
#print s.shape

class WeightFileRegridder:
  def __init__(self,weightFile):
    if isinstance(weightFile,str):
      if not os.path.exists(weightFile):
        raise Exception("WeightFile %s does not exists" % weightFile)
      wFile=cdms2.open(weightFile)
    else:
      wFile = weightFile
    print wFile.variables
    self.S=wFile("S").filled()
    self.row=wFile("row").filled()-1
    self.col=wFile("col").filled()-1
    self.frac_b=wFile("frac_b").filled()
    self.n_s=self.S.shape[0]
    self.n_b=self.frac_b.shape[0]
    self.method = wFile.map_method
    if isinstance(weightFile,str):
        wFile.close()

  def regrid(self, input):
    input = input.filled().ravel()
    dest_field=numpy.zeros((self.n_b,))
    print "nb:",self.n_b
    print "ns:",self.n_s
    print "row:",self.row.shape,self.row.min(),self.row.max()
    print "col:",self.col.shape,self.col.min(),self.col.max()
    print "input",input.shape
    for i in range(self.n_s):
        dest_field[self.row[i]]=dest_field[self.row[i]]+self.S[i]*input[self.col[i]]
    return dest_field

regdr = WeightFileRegridder(remapf)

print regdr.regrid(dat)
remapf.close()
