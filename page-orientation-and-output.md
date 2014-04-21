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

  * [ ![Send this page to somebody](media/mail_icon.gif) ](/cdat/tutorials/cdatbasics/plotting-basics/page-orientation-and-output/sendto_form)
  * [ ![Print this page](media/print_icon.gif) ](/this.print\(\))

#  Page Orientation and Output

[ ![Table of Contents](media/arrow-up) ](/)

[ ![Previous](media/arrow-left) ](/derived-data)

[ ![Next](media/arrow-right) ](/simple-x-y-line-plot)

[ Contents ](/)

[ Previous ](/derived-data)

[ Next ](/simple-x-y-line-plot)

 Goal:  Setting the VCS Canvas page orientation and generating output files.   
  

Before running the tutorial below, type _ "python" _ or _ "cdat" _ at the
command line.&#160; You will see the python prompt appear (i.e., ">>>"). You can
now enter the command lines below.  
  
You can [ _ _  view  _ _ ](/../files/orientation-and-output) or [ _ _ 
download  _ _ ](/../files/orientation_and_output.py) the full source code.
To run the source code at the command line, type: _ "python
orientation_and_output.py". _  
  

    
    
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
      
    # Extract a 3 dimensional data set  
    data = cdmsfile('clt')  
      
    # Initial VCS:  
    v = vcs.init()  
      
    # Opening a VCS Canvas - not necessary to do this   
    # before issuing the plot command!  
    v.open()  
      
    # A quick plot of the data  
    v.plot( data )  
    

![Orientation_1](media/orientation_1)

    
    
    # Changing plot orientation to "Portrait"   
    v.portrait()

![Orientation_2](media/orientation_2)

    
    
    # To change the orientation back to "Landscape"  
    v.landscape()

![Orientation_1](media/orientation_1)  

    
    
    ##############################################################  
    #                                                            #  
    # Saving "Landscape" orientation graphics to file            #  
    # "Landscape" is the default output orientation.             #  
    #                                                            #  
    ##############################################################  
      
    # Append to a postscript file  
    v.postscript('test.ps')  
      
    # Overwrite the existing postscript file  
    v.postscript('test.ps')  
      
    # GIF format - append landscape orientation gif image   
    v.gif('test.gif', merge='a', orientation='l', geometry='800x600')  
      
    # CGM format - append to an existing cgm file  
    v.cgm('test.cgm', 'a')  
      
    # Encapsulated Postscript - overwrite an existing eps file  
    v.eps('test.eps', 'r')  
      
    # PDF format  
    v.pdf('test.pdf')  
      
    ###########################################################################  
    # GhostScript (gs) format -                                               #  
    # This routine allows the user to save the VCS canvas in one of the many  #  
    # GhostScript (gs) file types (also known as devices). To view other      #  
    # GhostScript devices, issue the command "gs --help" at the terminal      #   
    # prompt.                                                                 #  
    ###########################################################################  
    v.gs('example')  # defaults: device='png256', orientation='l' and resolution='792x612'  
    v.gs(filename='example.tif', device='tiffpack', orientation='l', resolution='800x600')  
    v.gs(filename='example.pdf', device='pdfwrite', orientation='l', resolution='200x200')  
    
    
    
    # Changing plot orientation to "Portrait"   
    v.portrait()

![Orientation_2](media/orientation_2)

    
    
    ##############################################################  
    #                                                            #  
    # Saving "Portrait" orientation graphics to file            #  
    #                                                            #  
    ##############################################################  
      
    # Append postscript output to an existing file  
    v.postscript('test.ps','a','p')  
      
    # Overwrite existing postscript file with a new postscript file  
    v.postscript('test.ps','r','p')  
      
    # GIF format - overwrite gif image(s) output with portriat gif image  
    v.gif('test.gif', merge='r', orientation='p', geometry='800x600')  
      
    # CGM format - overwrite existing cgm file  
    v.cgm('test.cgm', 'r')  
      
    # Encapsulated Postscript - append portait output to an existing eps file.  
    v.eps('test.eps', 'a', 'p')  
      
    # PDF format  
    v.pdf ('test.pdf', 'p')  
      
    ###########################################################################  
    # GhostScript (gs) format -                                               #  
    # This routine allows the user to save the VCS canvas in one of the many  #  
    # GhostScript (gs) file types (also known as devices). To view other      #  
    # GhostScript devices, issue the command "gs --help" at the terminal      #   
    # prompt.                                                                 #  
    ###########################################################################  
    v.gs(filename='example.jpg', device='jpeg', orientation='p', resolution='1000x1000')  
    

  

[ ![Table of Contents](media/arrow-up) ](/)

[ ![Previous](media/arrow-left) ](/derived-data)

[ ![Next](media/arrow-right) ](/simple-x-y-line-plot)
