---
layout: default
title: 
---
#  Simple X-Y Line Plot
Goal:  Guide you through a simple X-Y line plot.   

Before running the tutorial below, type _ "python" _ or _ "cdat" _ at the
command line. You will see the python prompt appear (i.e., ">>>"). You can
now enter the command lines below.  
  
You can [download](media/python/simple_x_y_line_plot.py) the full source code. To run the
source code at the command line, type: `python simple_x_y_line_plot.py`.
    
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
      
    # Extract a 3 dimensional data set and get a subset of the time dimension  
    data = cdmsfile('clt', longitude=(-180, 180), latitude = (-50., -50.))  
      
    # Initial VCS:  
    v = vcs.init()  
      
    # Plot data using the default Yxvsx graphics method:  
    #  
    # Here is an example of using the Yxvsx graphics method  
    # that makes an X-Y plot (where the y-axis is a function  
    # of the x-axis).  
    #_  
    _v.yxvsx( data, long_name ='Simple X-Y Plot' )

![1D_Plot_1](media/images/1D_plot_1)  

    # Plot data using the default Xyvsy graphics method:  
    #  
    # Here is an example of using the Xyvsy graphics method  
    # that makes an X-Y plot (where the x-axis is a function  
    # of the y-axis).  
    #  
    v.clear()  
    v.xyvsy( data, long_name ='Simple X-Y Plot' )

![1D_Plot_2](media/images/1D_plot_2)  
