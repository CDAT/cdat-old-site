---
layout: default
title: Testing Software
---

#  Testing Software
To quickly test CDAT, type the following:

Note: if you used your python to build CDAT then replace `<CDAT_INSTALL_DIRECTORY>/bin/python` with the path to your python
    
    cd <CDAT_SRC_DIRECTORY>
    <CDAT_INSTALL_DIRECTORY>/bin/python test_cdat.py -a 
    
This will run a basic set of tests for Packagesand contributed Packages

By default it uploads your machine name to help us to know which kind of
systems cdat is built on

to stay anoymous and only upload your system info use:
    
    cd <CDAT_SRC_DIRECTORY>
    <CDAT_INSTALL_DIRECTORY>/bin/python test_cdat.py -a --upload=1

If you do not wish to upload any information then run:
    
    cd <CDAT_SRC_DIRECTORY>
    <CDAT_INSTALL_DIRECTORY>/bin/python test_cdat.py -a --upload=0

For more info on the test suite run:
    
    cd <CDAT_SRC_DIRECTORY>
    <CDAT_INSTALL_DIRECTORY>/bin/python test_cdat.py --help
