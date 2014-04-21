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

  * [ ![Send this page to somebody](media/mail_icon.gif) ](/cdat/tutorials/cdatbasics/loops/avg/sendto_form)
  * [ ![Print this page](media/print_icon.gif) ](/this.print\(\))

#  Averaging over multiple files

In this example we will loop over multiple files print compute the average
over all these files

    
    
    import cdms, MV  
    import sys  
      
    # Creates string for path to data  
    pth=sys.prefix+'/sample_data/'  
      
    # Creates list containg path to files  
    files = [ pth+'u_2000.nc',  
              pth+'u_2001.nc',  
              pth+'u_2002.nc',  
    &#160;&#160;&#160;&#160;&#160;&#160;&#160;  ]  
      
    # Now LOOP through the files  
    for file in files:  
        # Open a file  
        f=cdms.open(file)  
      
        # Get the 'u' variable  
    &#160;&#160;&#160; u=f('u')  
      
    &#160;&#160;&#160; if file == files[0]:    # First file  
    &#160;&#160;&#160;     avg=MV.sum(u,0)     # Compute the time sum  
    &#160;&#160;&#160;&#160;&#160;&#160;&#160; n=u.shape[0]        # Number of month in this file  
    &#160;&#160;&#160;   
        else:                   # Another file  
    &#160;&#160;&#160; &#160;&#160;&#160; avg=avg+MV.sum(u,0) # Compute the time sum and add it to our final variable  
            n=n+u.shape[0]  
