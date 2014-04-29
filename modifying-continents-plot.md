---
layout: default
title: Modifying Continents Plot 
---

##  Creating and Modifying a Continents Graphics Method
Goal:  Guide you through choosing defined continents.   

Before running the tutorial below, type _ "python" _ or _ "cdat" _ at the
command line. You will see the python prompt appear (i.e., ">>>"). You can
now enter the command lines below.  

You can [download](media/python/continents_file.py) the full source code. To run the source
code at the command line, type: `"python continents_file.py"`.

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

The VCS module contains a list of persistent continents graphics method
objects. To view this list issue the "show" command.  
    
    # Show the list of persistent continents graphics methods.  
    v.show('continents')  
    
    *Continents Names List*  
    (   1):                 ASD                def1             default  
      
    *End Continents Names List*

Get a continents graphics method object and plot:  
    
    # Assign the variable "ct_asd" to the persistent 'ASD' continents graphics methods.  
    ct_asd = v.getcontinents( 'ASD' )  
      
    # Plot only the the above continents graphics method.  
    v.plot( ct_asd )

![Continents_1](media/images/continents_1)  

List the 'ASD' continents graphics method attributes by issuing the following
command:  
    
    # List the 'ASD' boxfill graphics methods attributes.  
    ct_asd.list()  
    
    ----------Continents (Gcon) member (attribute) listings ----------  
    Canvas Mode = 1  
    graphics method = Gcon  
    name = ASD  
    projection = linear  
    xticlabels1 = lon30  
    xticlabels2 = lon30  
    xmtics1 =   
    xmtics2 =   
    yticlabels1 = lat20  
    yticlabels2 = lat20  
    ymtics1 =    
    ymtics2 =    
    datawc_x1 = 1.00000002004e+20  
    datawc_y1 =  1.00000002004e+20  
    datawc_x2 =  1.00000002004e+20  
    datawc_y2 =  1.00000002004e+20  
    line =  solid  
    linecolor =  None  
    linewidth =  None  
    type =  1
  
# Change 'ASD' continents graphics methods attributes by entering the
following commands.  
ct_asd.line = 2 # set the line type  
ct_asd.linecolor = 242 # set the line color  
ct_asd.linewidth = 3 # set the line width  
ct_asd.type = 3 # change the continents type to the 'Fine Continents'  

![Continents_2](media/images/continents_2)  

Overlay continents:  

    # Clear the VCS canvas and plot data using the boxfill graphics method.   
    # Also use the predefined template 'ASD' and plot with no continents.  
    v.clear()  
    v.plot( data, 'ASD', continents=0 )  
      
    # Now overlay the 'ASD' continents using the 'ASD_dud' template.  
    # The 'ASD_dud' template omits all text and only plots the data.   
    v.plot( ct_asd, 'ASD_dud' )  
      
    # Change the continents attributes for better viewing  
    ct_asd.line = 0            # change to solid line  
    ct_asd.linecolor = 241     # change the line color to black  
    ct_asd.linewidth = 2       # change the line width to 2  
    ct_asd.type = 5		   # change the continents type to the 'United States'  

![Continents_3](media/images/continents_3)  
Modifying the default continents:  
    
    # Clear the VCS canvas and plot data using the boxfill graphics method.   
    # Also use the predefined template 'ASD' and plot with no continents.  
    v.clear()  
    v.plot( data, continents=4 )  
      
    # Now get the line 'continents' object.  
    lc = v.getline('continents')   
    lc.list()  
    
    ----------Line (Tl) member (attribute) listings ----------  
    Canvas Mode = 1  
    secondary method = Tl  
    name = continents  
    type = ['solid']  
    width = [2.0]  
    color = [241]  
    priority = 1  
    viewport = [0.0, 1.0, 0.0, 1.0]  
    worldcoordinate = [0.0, 1.0, 0.0, 1.0]  
    x = None  
    y = None  
    projection = default

# Change line attribute values  
    lc.color=250  
    lc.width=2  
  
    v.clear()  
    v.plot( data, continents=4 )  

![Continents_4](media/images/continents_4)  
