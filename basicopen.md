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

  * [ ![Send this page to somebody](media/mail_icon.gif) ](/cdat/tutorials/cdatbasics/files/basicopen/sendto_form)
  * [ ![Print this page](media/print_icon.gif) ](/this.print\(\))

#  Opening a file and looking at its content

In this example we will open a file with cdms and query its content

    
    
    import cdms, sys  
      
    file=sys.prefix+'/sample_data/clt.nc'  
      
    # Open the file via cdms  
    f=cdms.open(file)  
      
    # Now we are going to query the file  
    # Get the names of the variables in the file  
    variables = f.listvariables()  
      
    print variables        # ['clt', 'u', 'v']  
      
    # Get the names of the dimensions present in files  
    dims = f.listdimension()  
      
    # Get the global (file) attributes  
    glob = f.listglobal()  
    print glob             # ['center', 'comments', 'Conventions', 'model']  
      
    # Get attributes attached to a variable (here clt)  
