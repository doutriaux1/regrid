from distutils.core import setup
import numpy
from numpy.distutils.core import setup, Extension
import glob,subprocess

p = subprocess.Popen(("git","describe","--tags"),stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
try:
  descr = p.stdout.readlines()[0].strip()
  Version = "-".join(descr.split("-")[:-2])
  if Version=="":
    Version = descr
except:
  Version = "0.1"
  descr = Version

p = subprocess.Popen(("git","log","-n1","--pretty=short"),stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
try:
  commit = p.stdout.readlines()[0].split()[1]
except:
  commit = ""
f = open("src/python/version.py","w")
print >>f, "__version__ = '%s'" % Version
print >>f, "__git_tag_describe__ = '%s'" % descr
print >>f, "__git_sha1__ = '%s'" % commit
f.close()

setup (name         = "acme_regridder",
       version      = descr,
       author       = "Charles Doutriaux",
       description  = "regridder for acme purposes",
       url          = "http://github.com/doutriaux1/regrid",
       packages     = ['acme_regridder',],
       package_dir  = {'acme_regridder': 'src/python',
                       },
       scripts      = ["scripts/acme_regrid.py","scripts/acme_regrid"],
       #data_files   = [('share',('pth_to_file1','pth_to_file2',)),
       #                ]
       include_dirs = [numpy.lib.utils.get_include()],
              ext_modules = [
           Extension('acme_regridder._regrid',
                     ['src/C/_regridmodule.c',],
                     library_dirs = [],
                     libraries = [],
                     define_macros = [],
                     extra_compile_args = ["-fopenmp",],
                     extra_link_args = [],
                     ),
           ]
      )

