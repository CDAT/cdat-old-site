---
layout: default
title: Removing Software 
---

##  Removing (or Cleaning) Software
For building again on a different system, or after downloading a new version,
or just to save disk space, issue the following commands:
    
    cd <CDAT_SRC_DIRECTORY>
    make clean
    
To clean the Makefile and config.log as well
    
    cd <CDAT_SRC_DIRECTORY>
    make distclean

Note:  To rebuild CDAT, always run make clean first and rerun configure. If you wish to rebuild CDAT and restart over, it is best to remove the ` <CDAT_INSTALL_DIRECTORY> ` . 
