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

  * [ ![Send this page to somebody](media/mail_icon.gif) ](/cdat/tutorials/cdatbasics/variablesandaxes/createvarscratch/sendto_form)
  * [ ![Print this page](media/print_icon.gif) ](/this.print\(\))

#  Creating a Variable From Scratch - Part 1

In this tutorial we show how to create a variable from some data and set some
attributes on it.

    
    
    import cdms, MV  
      
    # Let's start by creating data by hand, but you could achieve this via a script,   
    # reading data from a file, etc..  
      
    my_data=[  
    	 [1,2,3],  
    	 [4,5,6],  
    	 [7,8,9],  
    	 [10,11,12],  
    	]  
      
    # It is really easy to convert this 2 dimensional list into an array   
    # that CDAT will be able to process further for statistical analysis or simply to disply it  
      
    my_array=MV.array(my_data)  
    print my_array.shape  
      
    # Done, that was easy, wasn't it ?  
    # Now we can fine tune this array, since it has been created with default values  
      
    # First its name  
    my_array.id='My Array'  
      
    # Second it's type, since everytihng in the list was integer it is of type integer  
    # But we can change this  
    my_array=my_array.astype('f')   
      
    # Here we changed the typecode to&#160; 'f' which is float   
    # Accessible values are 'f': float, 'd': double, 'i': int , 'l': long  
      
    # Ok now we are adding "descriptive" attributes that would be useful to remember  
    my_array.history='first i created a list and then converted to MV and changed name and type'  
      
    # At this point we should also change the axis but this is for another tutorials  
