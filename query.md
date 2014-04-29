---
layout: default
title: Querying Files
---

##  Querying Files and Variables

Shows how to query file contents and variables informations

In this example we'll show how to query files and variable  
grey text shows output from cdat  
    
    import cdms,sys  
    f=cdms.open(sys.prefix+'/sample_data/clt.nc')  
      
    # Query "file" attributes  
    f.listglobal()  
    
    ['center', 'comments', 'Conventions', 'model']

    print f.Conventions  

    COARDS

    # Now query the file for variables  
    f.listvariables()  

    ['clt','u','v']
  
    # We can also query for dimensions  
    f.listdimension()  
    
    ['plev', 'latitude1', 'latitude2', 'time1', 'longitude1', 'longitude2', 'longitude', 'time', 'latitude', 'plev1', 'time2']
  
    # To query a variable without actually loading it  
    # in memory first, use a "File Variable" by using []  
    # Here we create the file variable pointing to 'clt'  
    # And query it for all available info  
    V=f['clt']  
    V.info()  

    * Description of Slab clt *  
    id: clt  
    shape: (120, 46, 72)  
    filename: /lgm/cdat/latest/sample_data/clt.nc  
    missing_value: None  
    comments: YONU_AMIP1  
    grid_name: YONU4X5  
    grid_type: gaussian  
    time_statistic: average  
    long_name: Total cloudiness  
    units: %  
    Grid has Python id 0x11dc350.  
    Gridtype: gaussian  
    Grid shape: (46, 72)  
    Order: yx  
     Dimension 1   
    id: time  
    Designated a time axis.  
    units:  months since 1979-1-1 0  
    Length: 120  
    First:  0.0  
    Last:   119.0  
    Python id:  0x11dc5a8  
     Dimension 2   
    id: latitude  
    Designated a latitude axis.  
    units:  degrees_north  
    Length: 46  
    First:  -90.0  
    Last:   90.0  
    Other axis attributes:  
    long_name: Latitude  
    Python id:  0x11dc698  
     Dimension 3   
    id: longitude  
    Designated a longitude axis.  
    units:  degrees_east  
    Length: 72  
    First:  -180.0  
    Last:   175.0  
    Other axis attributes:  
    long_name: Longitude  
    Python id:  0x11dc648  
    * End of description for clt *

    # This was just a print statement, we can actually  
    # query the variable for specifics  
    V.listattributes()  
    
    ['units', 'time_statistic', 'long_name', 'grid_name', 'comments', 'missing_value', 'grid_type']

    V.listdimnames()  
    
    ['time', 'latitude', 'longitude']
  
    # To query a dimension you can either get it  
    # from the file or from the variable  
    time=f['time']  
    time.getAxis(0)  
    time=V.getTime()  
    # Time, Level, Latitude, Longitude can be retrieve  
    # directly independently of where they are in 
    # the variable, using getTime, getLevel, getLatitude,
    # or getLongitude()
