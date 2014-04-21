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

  * [ ![Send this page to somebody](media/mail_icon.gif) ](/cdat/tutorials/cdatbasics/plotting-basics/animate-a-plot/sendto_form)
  * [ ![Print this page](media/print_icon.gif) ](/this.print\(\))

#  Animate a Plot

[ ![Table of Contents](media/arrow-up) ](/)

[ ![Previous](media/arrow-left) ](/plot-keyword-arguments)

[ ![Next](media/arrow-right) ](/modifying-boxfill-plot)

[ Contents ](/)

[ Previous ](/plot-keyword-arguments)

[ Next ](/modifying-boxfill-plot)

 Goal:  Guide you through some basic animation features.   

Before running the tutorial below, type _ "python" _ or _ "cdat" _ at the
command line.&#160; You will see the python prompt appear (i.e., ">>>"). You can
now enter the command lines below.  
  
You can [ _ _  view  _ _ ](/../files/animate-file) or [ _ _  download 
_ _ ](/../files/animate.py) the full source code. To run the source code at
the command line, type: _ "python -i animate.py" _ .

    
    
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
    data = cdmsfile('clt', time=('1980-1-1 0:0:0.0', '1981-12-1 0:0:0.0'), longitude=(-180, 180), latitude = (-90., 90.))  
      
    # Initial VCS:  
    v = vcs.init()  
      
    # Plot data using the default isofill graphics method:  
    v.isofill( data )

![Animate_1](media/animate_1)  

  

    
    
    # Create the images required for animation  
    v.animate.create( thread_it = 0 )
    
    
    # Run the animation using the images created  
    v.animate.run( )  
    

![Animate_2](media/animate_2)  

    
    
    # Stop the animation  
    v.animate.stop( )
    
    
    # Run the animation and pause between frames  
    v.animate.run( )   
    v.animate.pause( 3 )  
    
    
    
    # Zoom in on the animated frames  
    v.animate.zoom( 2 )
    
    
    # Move the animation horizonatally to the up and down  
    v.animate.horizontal( 50 )
    
    
    # Move the animation vertically left and right  
    v.animate.vertical( 50 )
    
    
    # Stop the animation and view frame 5, 10, and 15  
    v.animate.stop( )  
    v.animate.frame( 5 )  
    v.animate.frame( 10 )  
    v.animate.frame( 15 )  
    
    
    
    # Control the animate via the animation GUI  
    v.animate.gui( )

[ ![Table of Contents](media/arrow-up) ](/)

[ ![Previous](media/arrow-left) ](/plot-keyword-arguments)

[ ![Next](media/arrow-right) ](/modifying-boxfill-plot)
