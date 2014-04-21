---
layout: default
title: 
---


      * [ f2py - Wrapping Fortran Code ](/cdat/tutorials/f2py-wrapping-fortran-code)

    * [ Quick Reference ](/cdat/quick_reference)

    * [ FAQ ](/cdat/FAQ)

    * [ Manuals ](/cdat/manuals)

    * [ Tips and Tricks ](/cdat/tips_and_tricks)

    * [ Source Code ](/cdat/source)

    * [ Contact Us ](/cdat/contact-us)

    * [ Documents ](/cdat/docs)

    * [ Support ](/cdat/support)

  * [ CMOR ](/cmor)

  * [ IPCC AR4 Model Data Portal ](/esg_data_portal)

  * [ About Us ](/about)

  * [ Newsletter ](/Newsletter)

[ News ](/news)

     [ ![](media/newsitem_icon.gif) CDAT Newsletter, June 2007  2007-06-26  ](/Newsletter/Vol3/index_d.html)
     [ ![](media/newsitem_icon.gif) CDAT 4.1.2 Released  2006-06-07  ](/cdat_4_1_2)
     [ ![](media/newsitem_icon.gif) CDAT 4.0 Released  2005-11-21  ](/cdat_4_0)
     [ ![](media/newsitem_icon.gif) PCMDI Software Portal Released  2005-09-28  ](/software_portal_release)
     [ ![](media/newsitem_icon.gif) CDAT 4.0 Beta Released  2005-09-28  ](/cdat_4_0_beta)
     [ More news&#8230; ](/news)

#####  Document Actions

  * [ ![Send this page to somebody](media/mail_icon.gif) ](/cdat/tutorials/cdatbasics/plotting-basics/derived-data/sendto_form)
  * [ ![Print this page](media/print_icon.gif) ](/this.print\(\))

#  Plot Extracted and Derived Data

[ ![Table of Contents](media/arrow-up) ](/)

[ ![Previous](media/arrow-left) ](/open-a-file-and-plot)

[ ![Next](media/arrow-right) ](/page-orientation-and-output)

[ Contents ](/)

[ Previous ](/open-a-file-and-plot)

[ Next ](/page-orientation-and-output)

 Goal:  Guide you through some basic features of extracting and scripting derived data.   

Before running the tutorial below, type _ "python" _ or _ "cdat" _ at the
command line.&#160; You will see the python prompt appear (i.e., ">>>"). You can
now enter the command lines below.  
  
You can now enter the command lines below.  
  
You can [ _ _  view  _ _ ](/../files/extract-derive-and-plot) or [ _ _ 
download  _ _ ](/../files/extract_and_plot.py) the full source code. To run
the source code at the command line, type: _ "python extract_and_plot.py". _

    
    
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
    filepath = os.path.join(sys.prefix, 'sample_data/ts_da.nc')  
    cdmsfile = cdms.open( filepath )  
      
    # Extract a 3 dimensional data set  
    data = cdmsfile('ts')  
      
    # From viewing the dataset's attributes, we see that  
    # it is "Surface Air Temperature" and its units are   
    # represented in kelvin (K)._ _  
    data.info()  
      
    # Initial VCS:  
    v = vcs.init()  
      
    # Plot data using the default boxfill graphics method:  
    v.plot( data )  
    

![Derived_1](media/derived_1)

    
    
    # Select one time step, and average over the longitude   
    # axis resulting in a zonal mean  
    dl=cdutil.averager(data(time=7665, squeeze=1), axis='x')  
      
    # Set the variable's ID to 't_z'.   
    dl.id = 't_z'  
      
    # Clear the VCS Canvas and plot the 1D dataset.  
    v.clear()  
    v.plot( dl )  
    

![Derived_2](media/derived_2)  

    
    
    # Subtract 273.16 to produce temperature in degrees C  
    dc = data - 273.16  
    dc.id = 'ts'  
    dc.long_name = 'Surface (2m) Air Temperature [C]'  
    v.clear()  
    v.plot( dc )  
    

![Derived_3](media/derived_3)  

    
    
    # Extract a 4 dimensional dataset  
    filepath = os.path.join(sys.prefix, 'sample_data/ta_ncep_87-6-88-4.nc')  
    cdmsfile = cdms.open( filepath )  
    data = cdmsfile('ta')  
      
    # Average over time and longitude to get a variable   
    # with latitude and level axes  
    d2 = cdutil.averager(data, axis='tx')  
    d2.id = 't_zh'  
      
    # Plot results  
    v.clear()  
    v.plot( d2 )  
    

![Derived_4](media/derived_4)  

    
    
    # Extract data from a specific level  
    dp = cdmsfile('ta', longitude=(180, -180), latitude = (90., -90.), level =(200., 200.), squeeze=1)  
      
    # Plot results  
    v.clear()  
    v.plot( dp )  
    

![Derived_5](media/derived_5)

[ ![Table of Contents](media/arrow-up) ](/)

[ ![Previous](media/arrow-left) ](/open-a-file-and-plot)

[ ![Next](media/arrow-right) ](/page-orientation-and-output)
