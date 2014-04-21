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

  * [ ![Send this page to somebody](media/mail_icon.gif) ](/cdat/tutorials/cdatbasics/files/concatenetcdf/sendto_form)
  * [ ![Print this page](media/print_icon.gif) ](/this.print\(\))

#  Concatenating NetCDF files

In this example we will concatenate data split between 3 files into one

    
    
    import cdms  
      
    path=sys.prefix+'/sample_data/'  
      
    files = [ path+'u_2000.nc',  
              path+'u_2001.nc',  
              path+'u_2002.nc',  
    &#160;&#160;&#160; &#160;&#160;   ]  
      
    # First let's open the output file for writing (and possibly erase existing file)  
    fout=cdms.open('u_concatenated.nc','w')  
      
    for file in files:  
    &#160;&#160;&#160; f=cdms.open(file)  