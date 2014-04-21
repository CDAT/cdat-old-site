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

  * [ ![Send this page to somebody](media/mail_icon.gif) ](/cdat/tutorials/cdatbasics/plotting-basics/modifying-isoline-plot/sendto_form)
  * [ ![Print this page](media/print_icon.gif) ](/this.print\(\))

#  Creating and Modifying an Isoline Graphics Method

[ ![Table of Contents](media/arrow-up) ](/)

[ ![Previous](media/arrow-left) ](/modifying-isofill-plot)

[ ![Next](media/arrow-right) ](/simple-overlay-plot)

[ Contents ](/)

[ Previous ](/modifying-isofill-plot)

[ Next ](/simple-overlay-plot)

 Goal:  Guide you through creating and setting isoline graphics method attributes.   

Before running the tutorial below, type _ "python" _ or _ "cdat" _ at the
command line.&#160; You will see the python prompt appear (i.e., ">>>"). You can
now enter the command lines below.  
  
You can [ _ _  view  _ _ ](/../files/isoline_file) or [ _ _  download 
_ _ ](/../files/isoline_file.py) the full source code. To run the source code
at the command line, type: _ "python isoline_file.py" _ .

    
    
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
    data = cdmsfile('clt', longitude=(-180, 180), latitude = (-90., 90.))  
      
    # Initial VCS:  
    v = vcs.init()
    
    
    # Show the list of persistent isoline graphics methods.  
    v.show('isoline')  
      
    
    
    
    Isoline Names List*  
    (   1):                 ASD        P_and_height             default  
    (   4):                 map               polar               quick  
    End Isoline Names List*

  
  

Get a isoline graphics method object and plot:  

    
    
    # Assign the variable "df_asd" to the persistent 'ASD' isoline graphics methods.  
    df_asd = v.getisoline( 'ASD' )  
      
    # Plot the data using the above isoline graphics method.  
    v.plot( data, df_asd )  
    

![Isoline_1](media/isoline_1)  

List the 'ASD' isoline graphics method attributes by issuing the following
command:  

    
    
    # List the 'ASD' isoline graphics methods attributes.  
    df_asd.list()  
    
    
    
    ---------Isoline (Gi) member (attribute) listings ---------  
    Canvas Mode = 1  
    graphics method = Gi  
    name = ASD  
    projection = linear  
    xticlabels1 = *  
    xticlabels2 = *  
    xmtics1 =   
    xmtics2 =   
    yticlabels1 = *  
    yticlabels2 = *  
    ymtics1 =    
    ymtics2 =    
    datawc_x1 = 1.00000002004e+20  
    datawc_y1 =  1.00000002004e+20  
    datawc_x2 =  1.00000002004e+20  
    datawc_y2 =  1.00000002004e+20  
    datawc_timeunits =  days since 2000  
    datawc_calendar =  135441  
    xaxisconvert =  linear  
    yaxisconvert =  linear  
    label =  n  
    line =  ['solid']  
    linecolors =  [241]  
    linewidths =  [1.0]  
    text =  None  
    textcolors =  None  
    level =  [[0.0, 1.0000000200408773e+20] ]

  
  
Change 'ASD' isoline graphics methods attributes by entering the appropriate
command lines:  

    
    
    # change the isofill levels and line type and color  
    df_asd.levels = ( [20,0], [30,0], [40,0], [50,0], [60,0])  
    df_asd.levels = ( [0,20],[20,40],[50,60])  
    df_asd.levels = ( [20,0], [30,0], [40,0], [50,0], [60,0])  
    df_asd.levels = (30,50,70)  
    df_asd.line=[0, 2, 0]  
    df_asd.linecolors=(16,100,200)  
    

![Isoline_2](media/isoline_2)  

    
    
    # view the level labels  
    df_asd.label='y'  
    

![Isoline_3](media/isoline_3)  

    
    
    # set the label font and text color  
    df_asd.text=(1, 5, 9)  
    df_asd.textcolors=(16,100,200)  
    

![Isoline_4](media/isoline_4)  

    
    
    # Create a persistent isoline graphics methods from an existing isoline graphics method.  
    cf_new = v.createisoline( 'new', 'ASD' ) # create new from ASD  
    cf_new2 = v.createisoline( 'new2','quick' )# create new2 from quick  
    cf_new.list()                        # list its attributes  
    v.show('isoline')                    # show isoline list with new and new2  
    v.removeobject( cf_new )             # remove new from isoline list  
    v.show('isoline')                    # show isoline list without new

[ ![Table of Contents](media/arrow-up) ](/)

[ ![Previous](media/arrow-left) ](/modifying-isofill-plot)

[ ![Next](media/arrow-right) ](/simple-overlay-plot)
