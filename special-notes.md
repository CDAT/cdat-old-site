---
layout: default
title: Special Notes 
---

##  Special Notes on Specific Packages
###  OPeNDAP (a.k.a., DODS)
CDAT is automatically built with OPeNDAP (a.k.a., DODS) support on Linux and
Mac OS X 10.3.x platforms. You must provide the binaries for the DODS
libraries on all other platforms. (Make sure they've been compiled with the
same compiler used to build CDAT.) To build with OPeNDAP client support, use
the ` \--with-opendap=/my_dods_dir ` command option. (We recommend the use of
the ` \--force ` option as well).

If you do not want OPeNDAP support (e.g., for Linux and Mac OS X platforms)
add the ` \--disable-opendap ` option to the build command line.

###  SCRIP interpolation
CDAT Version 4 includes support for the SCRIP interpolation package developed
at Los Alamos National Laboratory. SCRIP interpolates gridded data, and can be
used with nonrectangular grids introduced in CDAT V4.

Because this package is standalone and is written in Fortran 90, it is not
built by default.

Note: CDAT has a built-in regridder for rectangular grids. If you need the
richer functionality of SCRIP, this package is included in `
<CDAT_SRC_DIRECTORY>/exsrc/src ` directory. See the SCRIP user guide for
installation instructions.

###  R Statistical Package
The R statistical package takes an extremely long time to build, but it builds
smoothly on Linux and Mac OS X 10.3.x platforms. Because of the time R takes
to build, we've decided to remove it from the build process.

If you already have R built on your system, and wish to only build the Rpy
contrib package, then make sure your ` LD_LIBRARY_PATH ` includes the path to
your R distribution, and then run the following build line command:

    cd <CDAT_SRC_DIRECTORY>
    <CDAT_INSTALL_DIRECTORY>/bin/python install.py --enable-r

###  Scientific Python
If OPeNDAP (a.k.a., DODS) is enabled, then SP will be built&#160; with DODS
support.
