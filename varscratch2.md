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

  * [ ![Send this page to somebody](media/mail_icon.gif) ](/cdat/tutorials/cdatbasics/variablesandaxes/varscratch2/sendto_form)
  * [ ![Print this page](media/print_icon.gif) ](/this.print\(\))

#  Creating a Variable From Scratch - Part 2

In this tutorial we show how to create axes to "decorate" a variable.

    
    
    import cdms, MV, Numeric  
      
    # First let's create a variable, type flaot, named 'myvar'  
    var = MV.array([[1,2,3], [4,5,6],[7,8,9], [10,11,12] ],typecode='f', id='myvar')  
      
    # Now let's assume this is lat/lon variable  
    # Storing the number of lat/lon  
    nlat,nlon=var.shape  
      
    # Step 1, creating the longitude axis  
    # First let's create the values  
    # First longitude located at 0  
    lons = Numeric.arange(0,360,360./nlon,'f')   
    print lons          # [&#160;&#160; 0., 120., 240.,]  
      
    # Now create the axis  
    lons=cdms.createAxis(lons)  
      
    # And decorate it  
    lons.id = 'longitude'  
    lons.units = 'degrees_east'  
      
    # Just to make sure we will describe this axis as a longitude one  
    lons.designateLongitude()  
      
    # Now let's do the same for the latitudes  
    # First latitude located at 180./nlat/2. from south pole  
    lats = Numeric.arange(-90,90,180./nlat,'f') + 90./nlat   
    print lats           # [-67.5,-22.5, 22.5, 67.5,]  
      
    # Now create the axis  
    lats=cdms.createAxis(lats)  
      
    # And decorate it  
    lats.id = 'latitude'  
    lats.units = 'degrees_north'  
      
    # Just to make sure we will describe this axis as a latitude one  
    lats.designateLatitude()  
      
    # Now let's apply these to the variable  
    # We can do it one at a time:  
    var.setAxis(0,lats)  
    var.setAxis(1,lons)  
      
    # Or all at once:  
    var.setAxisList((lats,lons))  
