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

  * [ ![Send this page to somebody](media/mail_icon.gif) ](/cdat/tutorials/cdatbasics/cdms-basics/createaxes/sendto_form)
  * [ ![Print this page](media/print_icon.gif) ](/this.print\(\))

#  Creating Axes

Explains how to create axes, and what is important to know about them.

Axes are important in CDAT because they add information about the variable.  
A variable is basically an array with a lot of information associated with
itself.  
Axes are very important as they describe the array's dimensions  
  
There's basically 4 important things on an axes  
    
its  values   
its name or  id  
 its  bounds    
its  units   
  
Let's say in this example that we a dataset representing the amount of rain in
a day.  
Also we'll say that the data are only collected if it actually rained  
  
Here are the mini dataset will be using  
  
Date ---- Value  
Jan 3&#160;&#160;&#160;&#160;&#160;&#160;&#160; 2 cm  
Jan 5&#160;&#160;&#160;&#160;&#160;&#160; 15 cm  
Jan 17&#160;&#160;&#160;&#160;&#160; 3.5 cm  
Jan 23&#160;&#160;&#160;&#160;&#160; 4 cm  
  

    
    
    # Let's import the necessary modules  
    import cdms,MV  
      
    # Let's create the variable first  
    rain = MV.array([2.,15.,3.5,4.])  
    rain.id    = 'pr'  
    rain.units = 'cm'  
      
    # Now we need to create the associated "time" axis, let's use days' since 2005 as units  
    # First the axis itslef with its values  
    # values can be passed as a list, an array or a variable  
    time = cdms.createAxis([2,4,16,22]) # Remember Jan 1st, is 0 days since Jan 1st!  
    # Now let's name it  
    time.id = 'time'  
    # Let's give it some units  
    time.units = 'days since 2005-1-1'  
      
    # Another very important attribute are the bounds, indeed we need to know the "extend" of each value  
    # Here we will assume that the data span a full day everytime, but they could as well spend a few hours   
    # of these days only  
      
    bounds = MV.array ([[2.,3.],  
    		    [4.,5.],  
    		    [16.,17.],  
    		    [22.,23.] ])  
      
    time.setBounds(bounds)  
      
    # Now we have to link the variable dimension to this axes object  
      
    rain.setAxis(0,time)  
      
    rain.info()  
    
    
    
    * Description of Slab pr *  
    id: pr  
    shape: (4,)  
    filename:  
    missing_value: None  
    comments:  
    grid_name: N/A  
    grid_type: N/A  
    time_statistic:  
    long_name:  
    units:  
    No grid present.  
     Dimension 1   
       id: time  
       Designated a time axis.  
