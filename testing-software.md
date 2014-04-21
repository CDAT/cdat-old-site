---
layout: default
title: 
---


#####  Document Actions

  * [ ![Send this page to somebody](media/mail_icon.gif) ](/cdat/download/installation-guide/testing-software/sendto_form)
  * [ ![Print this page](media/print_icon.gif) ](/this.print\(\))

#  Testing Software

[ ![Table of Contents](media/arrow-up) ](/)

[ ![Previous](media/arrow-left) ](/troubleshooting)

[ ![Next](media/arrow-right) ](/removing-software)

[ Contents ](/)

[ Previous ](/troubleshooting)

[ Next ](/removing-software)

To quickly test CDAT, type the following:

Note: if you used your python to build CDAT then replace
<CDAT_INSTALL_DIRECTORY>/bin/python with the path to your python

    
    
    cd <CDAT_SRC_DIRECTORY>
    <CDAT_INSTALL_DIRECTORY>/bin/python test_cdat.py -a 
    

This will run a basic set of&#160; tests for Packagesand&#160; contributed Packages

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

[ ![Table of Contents](media/arrow-up) ](/)

[ ![Previous](media/arrow-left) ](/troubleshooting)

[ ![Next](media/arrow-right) ](/removing-software)