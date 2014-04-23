---
layout: default
title: Fortran Part 2
---

##  Part 2: Basic wrapping and calling

In this section we show how to quickly wrap and call the fortran subroutine
described in part 1

Get the fortran subroutine [here](media/fortran/sf.f90)

Get the sample data: [va_djf.nc ](media/fortran/va_djf.nc) and [ps.nc](media/fortran/ps.nc)

The easiest way to wrap this using f2py is to run the following comand
    
    f2py -c -m streamfunction sf.f90

You should get something similar to the following on your screen:

    running build
    running config_cc
    unifing config_cc, config, build_clib, build_ext, build commands --compiler options
    running config_fc
    unifing config_fc, config, build_clib, build_ext, build commands --fcompiler options
    running build_src
    building extension "streamfunction" sources
    f2py options: []
    f2py:> /tmp/tmpwrCzXz/src.linux-i686-2.5/streamfunctionmodule.c
    creating /tmp/tmpwrCzXz
    creating /tmp/tmpwrCzXz/src.linux-i686-2.5
    Reading fortran codes...
            Reading file 'sf.f90' (format:free)
    Post-processing...
            Block: streamfunction
                            Block: ccmp_zm_mspi
    Post-processing (stage 2)...
    Building modules...
            Building module "streamfunction"...
                    Constructing wrapper function "ccmp_zm_mspi"...
                      zm_mpsi = ccmp_zm_mspi(v,lat,p,ps,msg,[nlon,nlat,nlev])
            Wrote C/API module "streamfunction" to file "/tmp/tmpwrCzXz/src.linux-i686-2.5/streamfunctionmodule.c"
      adding '/tmp/tmpwrCzXz/src.linux-i686-2.5/fortranobject.c' to sources.
      adding '/tmp/tmpwrCzXz/src.linux-i686-2.5' to include_dirs.
    copying /lgm/cdat/latest/lib/python2.5/site-packages/numpy/f2py/src/fortranobject.c -> /tmp/tmpwrCzXz/src.linux-i686-2.5
    copying /lgm/cdat/latest/lib/python2.5/site-packages/numpy/f2py/src/fortranobject.h -> /tmp/tmpwrCzXz/src.linux-i686-2.5
    running build_ext
    customize UnixCCompiler
    customize UnixCCompiler using build_ext
    customize GnuFCompiler
    Could not locate executable g77
    Could not locate executable f77
    customize IntelFCompiler
    Could not locate executable ifort
    Could not locate executable ifc
    customize LaheyFCompiler
    Could not locate executable lf95
    customize PGroupFCompiler
    Could not locate executable pgf90
    Could not locate executable pgf77
    customize AbsoftFCompiler
    Could not locate executable f90
    customize NAGFCompiler
    Could not locate executable f95
    customize VastFCompiler
    customize GnuFCompiler
    customize CompaqFCompiler
    Could not locate executable fort
    customize IntelItaniumFCompiler
    Could not locate executable efort
    Could not locate executable efc
    customize IntelEM64TFCompiler
    customize Gnu95FCompiler
    Found executable /usr/local/bin/gfortran
    customize Gnu95FCompiler
    customize Gnu95FCompiler using build_ext
    building 'streamfunction' extension
    compiling C sources
    C compiler: gcc -fno-strict-aliasing -DNDEBUG -O -fPIC
    
    creating /tmp/tmpwrCzXz/tmp
    creating /tmp/tmpwrCzXz/tmp/tmpwrCzXz
    creating /tmp/tmpwrCzXz/tmp/tmpwrCzXz/src.linux-i686-2.5
    compile options: '-I/tmp/tmpwrCzXz/src.linux-i686-2.5 -I/lgm/cdat/latest/lib/python2.5/site-packages/numpy/core/include -I/lgm/cdat/latest/include/python2.5 -c'
    gcc: /tmp/tmpwrCzXz/src.linux-i686-2.5/fortranobject.c
    gcc: /tmp/tmpwrCzXz/src.linux-i686-2.5/streamfunctionmodule.c
    compiling Fortran sources
    Fortran f77 compiler: /usr/local/bin/gfortran -Wall -ffixed-form -fno-second-underscore -fPIC -O3 -funroll-loops -march=pentium4 -mmmx -msse2 -msse -fomit-frame-pointer -malign-double
    Fortran f90 compiler: /usr/local/bin/gfortran -Wall -fno-second-underscore -fPIC -O3 -funroll-loops -march=pentium4 -mmmx -msse2 -msse -fomit-frame-pointer -malign-double
    Fortran fix compiler: /usr/local/bin/gfortran -Wall -ffixed-form -fno-second-underscore -Wall -fno-second-underscore -fPIC -O3 -funroll-loops -march=pentium4 -mmmx -msse2 -msse -fomit-frame-pointer -malign-double
    compile options: '-I/tmp/tmpwrCzXz/src.linux-i686-2.5 -I/lgm/cdat/latest/lib/python2.5/site-packages/numpy/core/include -I/lgm/cdat/latest/include/python2.5 -c'
    gfortran:f90: sf.f90
    sf.f90:107.56:
    
      INTEGER                                           :: k
                                                           1
    Warning: Unused variable k declared at (1)
    sf.f90: In function 'ccmp_zm_mspi':
    sf.f90:106: warning: 'flag' may be used uninitialized in this function
    /usr/local/bin/gfortran -Wall -Wall -shared /tmp/tmpwrCzXz/tmp/tmpwrCzXz/src.linux-i686-2.5/streamfunctionmodule.o /tmp/tmpwrCzXz/tmp/tmpwrCzXz/src.linux-i686-2.5/fortranobject.o /tmp/tmpwrCzXz/sf.o -lgfortran -o ./streamfunction.so
    Removing build directory /tmp/tmpwrCzXz
    
Most importantly you should now have a file called:

`streamfunction.so`

This file can be loaded in Python

Let's take a look at it, from the directory where the file resides run python,
import the file/module

    python
    Python 2.5.1 (r251:54863, Jan  2 2008, 11:40:37)
    [GCC 4.2.1] on linux2
    Type "help", "copyright", "credits" or "license" for more information.
    Loaded 5.0 settings
    
    >>> import streamfunction

We can look at the module contents:
    
    >>> dir(streamfunction)
    ['__doc__', '__file__', '__name__', '__version__', 'ccmp_zm_mspi']

Not surprisingly it only contains the  ccmp_zm_mspi  subroutine

Let's take a look at it, f2py nicely documented its call for us:
    
    >>> print streamfunction.ccmp_zm_mspi.__doc__
    ccmp_zm_mspi - Function signature:
      zm_mpsi = ccmp_zm_mspi(v,lat,p,ps,msg,[nlon,nlat,nlev])
    Required arguments:
      v : input rank-3 array('f') with bounds (nlon,nlat,nlev)
      lat : input rank-1 array('f') with bounds (nlat)
      p : input rank-1 array('f') with bounds (nlev)
      ps : input rank-2 array('f') with bounds (nlon,nlat)
      msg : input float
    Optional arguments:
      nlon := shape(v,0) input int
      nlat := shape(v,1) input int
      nlev := shape(v,2) input int
    Return objects:
      zm_mpsi : rank-2 array('f') with bounds (nlat,nlev)

Ok, at this stage it is important to note a few things.

1- f2py separated input and output arguments, the later ones are now returned
(zm_mpsi)

2- f2py detected that some input arguments can be deducted from the other
input arguments, in this case the arrays dimensions

This is important for 2 reason:

a- You do not need to pass these, f2py will figure it out on its own

b- If you decide to pass them anyway, they have been shifted to the end of the
call, remember in the fortran call nlon, nlat and nlev were the first
arguments to pass, now they do not need to be passed but must be passed last.  

OK let's use our sample dataset and call this function

    import streamfunction
    import cdms2
    # Open data file 1
    f=cdms2.open('[va_djf.nc](/va_djf.nc)')
    # reads in data, makes sure order is right and levels are top to bottom
    v=f('v',level=(0,1E10),order='xyz') # right order, p starts at 0 (top)
    f.close()
    # now get the latitude and level axes
    lat=v.getLatitude()
    p=v.getLevel()
    # does the same with second file
    fp=cdms2.open('[ps.nc](/ps.nc)')
    ps=fp('ps',order='xy') # right order
    fp.close()
    msg=1.e20
    
    zm_mpsi=streamfunction.ccmp_zm_mspi(v.filled(),lat[:],p[:],ps.filled(),msg)

Let's point out a few important things

1- When reading the data we made sure they'd be ordered according to what the
fortran wants (lon,lat,lev)

2-

a- When passing or variable to the fortran we convert them to numpy object,
indeed only understand pure array, it does not know about masked values or
axis or attributes.

b- Axes object had to be converted as well to pure array , that's why we used
[:] when passing them, it returns their values only as an array

3- When converting MV/MA to numpy pure arrays we used the .filled() attribute,
