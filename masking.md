---
layout: default
title: 
---

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

  * [ ![Send this page to somebody](media/mail_icon.gif) ](/cdat/tutorials/advanced_cdat/masking.html/sendto_form)
  * [ ![Print this page](media/print_icon.gif) ](/this.print\(\))

#  Part II. Masking Technique

[ ![Table of Contents](media/arrow-up) ](/index.html)

[ ![Previous](media/arrow-left) ](/regridding.html)

[ ![Next](media/arrow-right) ](/annualcycle.html)

[ Contents ](/index.html)

[ Previous ](/regridding.html)

[ Next ](/annualcycle.html)

 Goal:  The goal for this tutorial is to show how to create sea/land mask and apply those masks to sea/land data creating masked data.   

The strategy:  

> 3) read the data with fraction land caverage from which the land/sea mask
will be created. Regrid the fraction to the 5-deg grid, create land and sea
masks.  

>

> 4) create sst/tas variables masked with ocean/land maskes .  

_  
 3)  read the data with fraction land caverage _   

    
    
    # extract a land/sea mask and regrid it to our desired 5 degree grid  
    # (these data are percent land coverage [0-100])  
    file4 = os.path.join(sys.prefix, 'sample_data/geo.1deg.ctl')  
    c = cdms.open(file4)   
    fraction=c('sftlf',squeeze=1)  
    c.close()   
    # plot the fraction field  
    y=vcs.init()  
    y.setcolormap('default')  
    y.plot(fraction)

  
  
![](media/regrid_fraction.jpg)  
  
Regrid the fraction to the 5-deg grid, create land and sea masks.  

    
    
    # get grid for regridding   
    grid3=fraction.getGrid()   
    # etup regrid function   
    regridfunc=Regridder(grid3,grid1)  
    # regrid mask values   
    fraction=regridfunc(fraction)   
        
    # create land and sea masks.  
    # 50% or more coverage in a box is defined as land   
    # and less than or equal to 50% coverage is ocean.  
    # All other values in the arrays are zeros.  
    land=Numeric.where(Numeric.greater(fraction.filled(),50.),1.,0.)  
    ocean=Numeric.where(Numeric.less_equal(fraction.filled(),50.),1.,0)

_  4)  create sst/tas variables masked with ocean/land maskes . _  

    
    
    masked_sst=Numeric.multiply(sst_new.filled(),ocean)  
    masked_tas=Numeric.multiply(tas_new.filled(),land)

Plot 'masked_sst' and 'masked_tas'  

    
    
    x=clear()   
    x.plot(masked_sst) 

![regr4.jpg](media/regr4.jpg)  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  

    
    
    y=clear()   
    y.plot(masked_tas)

![regr5.jpg](media/regr5.jpg)  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
next: [ ](/annualcycle.html) [ Part III. Creating annual cycle and calculating
anomalies. ](/annualcycle.html)

[ ![Table of Contents](media/arrow-up) ](/index.html)

[ ![Previous](media/arrow-left) ](/regridding.html)

[ ![Next](media/arrow-right) ](/annualcycle.html)
