---
layout: default
title: 
---


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

  * [ ![Send this page to somebody](media/mail_icon.gif) ](/cdat/tutorials/cdatbasics/cdms-basics/query/sendto_form)
  * [ ![Print this page](media/print_icon.gif) ](/this.print\(\))

#  Querying Files and Variables

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
    &#160;id: time  
    &#160;Designated a time axis.  
    &#160;units:  months since 1979-1-1 0  
    &#160;Length: 120  
    &#160;First:  0.0  
    &#160;Last:   119.0  
    &#160;Python id:  0x11dc5a8  
     Dimension 2   
    &#160;id: latitude  
    &#160;Designated a latitude axis.  
    &#160;units:  degrees_north  
    &#160;Length: 46  
    &#160;First:  -90.0  
    &#160;Last:   90.0  
    &#160;Other axis attributes:  
    &#160;long_name: Latitude  
    &#160;Python id:  0x11dc698  
     Dimension 3   
    &#160;id: longitude  
    &#160;Designated a longitude axis.  
    &#160;units:  degrees_east  
    &#160;Length: 72  
    &#160;First:  -180.0  
    &#160;Last:   175.0  
    &#160;Other axis attributes:  
    &#160;long_name: Longitude  
    &#160;Python id:  0x11dc648  
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
