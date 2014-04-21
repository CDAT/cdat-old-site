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

  * [ ![Send this page to somebody](media/mail_icon.gif) ](/cdat/tutorials/cdatbasics/plotting-basics/simple-x-y-line-plot/sendto_form)
  * [ ![Print this page](media/print_icon.gif) ](/this.print\(\))

#  Simple X-Y Line Plot

[ ![Table of Contents](media/arrow-up) ](/)

[ ![Previous](media/arrow-left) ](/page-orientation-and-output)

[ ![Next](media/arrow-right) ](/plot-keyword-arguments)

[ Contents ](/)

[ Previous ](/page-orientation-and-output)

[ Next ](/plot-keyword-arguments)

 Goal:  Guide you through a simple X-Y line plot.   

Before running the tutorial below, type _ "python" _ or _ "cdat" _ at the
command line.&#160; You will see the python prompt appear (i.e., ">>>"). You can
now enter the command lines below.  
  
You can [ _ _  view  _ _ ](/../files/simple-1D-plot) or [ _ _  download
 _ _ ](/../files/simple_x_y_line_plot.py) the full source code. To run the
source code at the command line, type: _ "python simple_x_y_line_plot.py" _ .  

    
    
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

  

![1D_Plot_1](media/1D_plot_1)  

    
    
    # Plot data using the default Xyvsy graphics method:  
    #  
    # Here is an example of using the Xyvsy graphics method  
    # that makes an X-Y plot (where the x-axis is a function  
    # of the y-axis).  
    #  
    v.clear()  
    v.xyvsy( data, long_name ='Simple X-Y Plot' )

![1D_Plot_2](media/1D_plot_2)  

[ ![Table of Contents](media/arrow-up) ](/)

[ ![Previous](media/arrow-left) ](/page-orientation-and-output)

[ ![Next](media/arrow-right) ](/plot-keyword-arguments)
