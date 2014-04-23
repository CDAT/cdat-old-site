---
layout: default
title: Loop 
---
#  Looping through files

In this example we will loop through files and display some of their
information.
    
    import cdms,sys,os  
      
    path=sys.prefix+'/sample_data/'  
      
    # List files in sample_data directory  
    my_files=os.listdir(path)  
      
    # Now loops through values in my_files and assign them  
    # one after the other to file  
      
    for file in my_files:  
        # Deal only with NetCDF files  
        if file[-3:]=='.nc':       
            print 'Dealing with file:',file  
            f=cdms.open(path+file)  
      
            variables=f.listvariables()  
