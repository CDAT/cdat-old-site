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

  * [ ![Send this page to somebody](media/mail_icon.gif) ](/cdat/tutorials/cdatbasics/plotting-basics/open-a-file-and-plot/sendto_form)
  * [ ![Print this page](media/print_icon.gif) ](/this.print\(\))

#  Open a File and Plot a Variable

[ ![Table of Contents](media/arrow-up) ](/)

[ ![Previous](media/arrow-left) ](/what-is-vcs)

[ ![Next](media/arrow-right) ](/derived-data)

[ Contents ](/)

[ Previous ](/what-is-vcs)

[ Next ](/derived-data)

 Goal:  Learn how to simply open a netCDF data file, list and extract a variable, and plot a variable using the boxfill, isofill, and isoline graphics methods.   
  
Before running the tutorial below, type _ "python" _ or _ "cdat" _ at the
command line.&#160; You will see the python prompt appear (i.e., ">>>"). You can
now enter the command lines below.  
  
You can [ _ _  view  _ _ ](/../files/open-and-plot) or [ _ _  download
 _ _ ](/../files/open_and_plot.py) the full source code.&#160; To run the source
code at the command line, type: _ "python open_and_plot.py". _  
  

    
    
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
    

![Simple_plot_1](media/simple_plot_1)

_ _

    
    
    # Plot data using the isofill graphics method:  
    v.clear()  
    v.isofill( data )

![Simple_plot_2](media/simple_plot_2)

_ _

    
    
    # Plot data using the isoline graphics method:  
    v.clear()  
    v.isoline( data )

![Simple_plot_3](media/simple_plot_3)

_ _

    
    
    # Plot data using the boxfill graphics method:  
    v.clear()  
    v.boxfill( data )

![Simple_plot_1](media/simple_plot_1)

_ _

    
    
    # Plot a simple overlay plot using the isofill and isoline graphics methods:  
    v.clear()  
    v.isofill( data )  
    v.isoline( data )

![Simple_plot_4](media/simple_plot_4)

[ ![Table of Contents](media/arrow-up) ](/)

[ ![Previous](media/arrow-left) ](/what-is-vcs)

[ ![Next](media/arrow-right) ](/derived-data)
