import cdms2,numpy,sys,argparse

p=argparse.ArgumentParser()
p.add_argument("--input",help="File to make smaller",default="ne120_to_t85.wgts.nc")
p.add_argument("--output",help = "output file name, default append_small to input file name",default=None)
p.add_argument("--nodouble",help = "converts double to float",action="store_true")


p = p.parse_args(sys.argv[1:])

if p.output is None:
    fnmout = p.input[:-3]+"_small.nc"
else:
    fnmout=p.output

f=cdms2.open(p.input)

fo = cdms2.open(fnmout,"w")

for v in f.variables.keys():
    V = f(v)
    if V.dtype == numpy.float and p.nodouble:
        fo.write(V,dtype=numpy.float32)
    else:
        fo.write(V)
fo.close()

