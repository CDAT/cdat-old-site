import sys

# Gather up all the files we need.
files = ['Src/sf.f90',]

## scypy_distutils Script
from numpy.distutils.core import setup, Extension

extra_link_args=[]
if sys.platform=='darwin':
    extra_link_args = ['-bundle','-bundle_loader '+sys.prefix+'/bin/python']
    
## setup the python module
setup(name="sf2", # name of the package to import later
      ## Build fortran wrappers, uses f2py
      ## directories to search for libraries defined in setup.cfg
      ext_modules = [Extension('streamfunction',
                               files,
#                              libraries=[],
#                              library_dirs=[],
#   			       include_dirs=['Src'],
                               extra_link_args=extra_link_args,
                               ),
                     ],
      
##      ## Install these to their own directory
     package_dir={'sf':'Lib'},
     packages = ["sf"],
      
     )




