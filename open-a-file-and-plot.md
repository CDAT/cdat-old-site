---
layout: default
title: Opening a File 
---

#  Open a File and Plot a Variable
Goal:  Learn how to simply open a netCDF data file, list and extract a variable, and plot a variable using the boxfill, isofill, and isoline graphics methods.   
  
Before running the tutorial below, type _ "python" _ or _ "cdat" _ at the
command line. You will see the python prompt appear (i.e., ">>>"). You can
now enter the command lines below.  
  
You can [download](media/images/python/open_and_plot.py) the full source code. To run the source
code at the command line, type: `python open_and_plot.py`.
    
    # Import modules:  
    # cdms - Climate Data Management system accesses gridded data.  
    # vcs - Visualization and control System 1D and 2D plotting routines.  
    # os - Operation System routines for Mac, DOS, NT, or Posix depending on the   
    #      system you're on.  
    # sys - This module provides access to some objects used or maintained by the  
    #       interpreter and to functions that interact strongly with the interpreter.  
    import cdms, vcs, os, sys  
      
    # Open data file:  
    filepath = os.path.join(sys.prefix, 'sample_data/clt.nc')  
    cdmsfile = cdms.open( filepath )  
    cdmsfile.listvariables()  
    data = cdmsfile('clt')_  
      
    _# Initial VCS:  
    v = vcs.init()  
      
    # Plot data using the default boxfill graphics method:  
    v.plot( data )  

![Simple_plot_1](media/images/simple_plot_1)

    
    # Plot data using the isofill graphics method:  
    v.clear()  
    v.isofill( data )

![Simple_plot_2](media/images/simple_plot_2)

    
    # Plot data using the isoline graphics method:  
    v.clear()  
    v.isoline( data )

![Simple_plot_3](media/images/simple_plot_3)

    
    # Plot data using the boxfill graphics method:  
    v.clear()  
    v.boxfill( data )

![Simple_plot_1](media/images/simple_plot_1)

    
    # Plot a simple overlay plot using the isofill and isoline graphics methods:  
    v.clear()  
    v.isofill( data )  
    v.isoline( data )

![Simple_plot_4](media/images/simple_plot_4)
