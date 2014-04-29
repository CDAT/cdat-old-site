---
layout: default
title: Plot Keyword
---

##  Plot Keyword Arguments
Goal:  Guide you through setting keyword "Plot" arguments.   

Before running the tutorial below, type _ "python" _ or _ "cdat" _ at the
command line. You will see the python prompt appear (i.e., ">>>"). You can
now enter the command lines below.  
  
You can [download](media/python/plot_keyword_argument.py) the full source code. To
run the source code at the command line, type: `python plot_keyword_arguments.py`.
    
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

The "plot" keyword arguments play an important role in controlling the output
of the final plot product. In the VCS module, arguments are passed to the
"plot" function by assignment. For example, plot(array1=None, array2=None,
[key=value [, key=value [, ...] ] ])  
where array1 and array2 can be MV, MA, NumPy, Lists, or Dictionary arrays.

The list of "plot" keyword arguments and their discription can be found by
issuing the following command:  

    vcs.help( 'plot' )  

Set the "variable" attribute keyword arguments:    
    
    v.plot(data, 'ASD', name ='name', long_name='varid',  
    hms='hms',units='units', ymd='ymd', file_comment='file_comment',  
    comment1='comment1', comment2='comment2',  
    comment3='comment3',comment4='comment4')

![Keywords_1](media/images/keywords_1)  

Set the "dimension" attribute keyword arguments:   

    v.plot(data, 'ASD', xname ='Xname', yname='Yname',x)

Set the "CDMS" object keyword arguments:   


Set the "Reverse Axis" keyword arguments:   

Set the "Continents" keyword arguments:   

The continents-type values are integers ranging from 0 to 11, where:   

    0 signifies "No Continents"  
    1 signifies "Fine Continents"  
    2 signifies "Coarse Continents"  
    3 signifies "United States"  
    4 signifies "Political Borders"  
    5 signifies "Rivers"  

Values 6 through 11 signify the line type defined by the files
data_continent_other7 through data_continent_other12.   

    v.clear()  
    v.plot(data, continents=0)  
    v.clear()  
    v.plot(data, continents=1)  
    v.clear()  
    v.plot(data, continents=3) # Figure below "United States"  

![Keywords_2](media/images/keywords_2)

Set the "Ratio" keyword argument:   
    
    v.clear( )  
    v.plot( data, ratio=1 ) # Only modify the data image  

![Keywords_3](media/images/keywords_3)

    v.clear( )  
    v.plot( data, ratio='1t' ) # srink border to fit data image

![Keywords_4](media/images/keywords_4)

Set the "Background Mode" keyword argument:   

    v.plot(data, bg=1)  
    v.showbg( )  
    
![Keywords_5](media/images/keywords_5)
