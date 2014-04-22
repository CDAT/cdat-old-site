---
layout: default
title: Express Install 
---

##  Express Install
Explanation to install CDAT on your system. And a few platform specific notes.

###  Express Installation
Check for platform-specific instructions in the "In Depth" section, and set
the environment variable CC if needed.

Note:  On some platforms the CC environment variable must be set before building. 

`<CDAT_INSTALL_DIRECTORY>` indicates  the full path  name of the
directory into which CDAT is to be installed and the notation 
`<CDAT_SRC_DIRECTORY>` indicates  the full path  name of the directory
where you uncompressed and un-tarred the CDAT source code.

The `<CDAT_EXTERNALS>` directory is a directory where you would like to
install software that CDAT needs but is not developped by the CDAT team. These
are usually needed by ANY version of CDAT. So it might be a good idea to build
them once only somewhere outside of the `<CDAT_INSTALL_DIRECTORY>` so you can
reuse for the next version w/o rebuilding them. By default it is set to
`<CDAT_INSTALL_DIRECTORY>` Externals.

`<MY_PYTHON>` referes to the location of your Python if you wish to use your
own python (beware it ight not work&#160; if it is too old or doesn't have some
features needed by CDAT)

cd to the directory where svn put your version:

    # Terms in between [] are optional
    ./configure --prefix=CDAT_INSTALL_DIRECTORY [--with-externals=CDAT_EXTERNALS] [--with-python=MY_PYTHON] [--with-opendap]
    # use ./configure --help for a list of all options!
    
    # Clean previous build, just in csae
    make clean
    # And finally make and build cdat
    make

Wait a bit and that should do it.

###  CDMS Only Express Installation Instructions
Check for platform-specific instructions above and set the environment
variable CC if needed.

To install a minimal configuration supporting CDMS only:
    
    cd <CDAT_SRC_DIRECTORY>
    ./configure --prefix=<CDAT_INSTALL_DIRECTORY> --enable-cdms-only [options]
