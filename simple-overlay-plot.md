---
layout: default
title: Simple Overlay Plot
---

##  Simple Overlay Plot

Goal:  Guide you through creating simple overlay plots.   

Before running the tutorial below, type _ "python" _ or _ "cdat" _ at the
command line. You will see the python prompt appear (i.e., ">>>"). You can
now enter the command lines below.  

You can [download](media/python/overlay_file.py) the full source code. To run the source code
at the command line, type: `python overlay_file.py`.

    # Import the modules needed for the tuturial  
    # cdms - Climate Data Management system accesses gridded data.  
    # vcs - Visualization and control System 1D and 2D plotting routines.  
    # cdutil - Climate utilitizes that contains miscellaneous routines for   
    #          manipulating variables.  
    # time - This module provides various functions to mainpulate time values.  
    # os - Operation System routines for Mac, DOS, NT, or Posix depending on   
    #      the system you're on.  
    # sys - This module provides access to some objects used or maintained by   
    #       the interpreter and to functions that interact strongly with the interpreter.  
    import vcs, cdms, cdutil, time, os, sys  
      
    # Open data file:  
    filepath = os.path.join(sys.prefix, 'sample_data/clt.nc')  
    cdmsfile = cdms.open( filepath )  
      
    # Extract 3 dimensional data sets and get a subset of the time dimension  
    data = cdmsfile( 'clt')  
    data1 = cdmsfile('u', longitude=(-180, -50), latitude = (10., 72))  
    data2 = cdmsfile('v', longitude=(-180, -50), latitude = (10., 72))  
    data3 = cdmsfile('clt',   
    longitude=(-180, -50), latitude = (10., 70))  
      
    # Set the longitude and latitude axes of the "v" variable  
    # to that of the "u" variable.  
    data2.setAxis(2, data1.getAxis(2))  
    data2.setAxis(3, data1.getAxis(3))  
      
    # Initial VCS:  
    v = vcs.init()

Overlay the same data using the isofill and isoline graphics methods:  
    
    # 1st plot the data with the isofill graphics method.  
    v.isofill( data )  
      
    # 2nd overlay the data with the isoline graphics method.  
    v.isoline( data )  

![Overlay_1](media/images/overlay_1)  
Overlay boxfill data with vector data.  
    
    # Clear the VCS Canvas  
    v.clear( )  
      
    # Plot the variable clt with the boxfill graphics method,   
    # then the u and v vector as an overlay. Because it   
    # is an overlay we do not want to plot any text or   
    # continents. To only plot data, use the "default_dud"   
    # template.  
    v.boxfill( data3 )  
    v.vector( data1, data2, 'default_dud', continents=0 )  

![Overlay_2](media/images/overlay_2)  
