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

  * [ ![Send this page to somebody](media/mail_icon.gif) ](/cdat/tutorials/cdatbasics/loops/concatenate/sendto_form)
  * [ ![Print this page](media/print_icon.gif) ](/this.print\(\))

#  Concatenating Data

In this example we will loop through files containing each a year of data. We
will then concatenate the data either along the time dimension (to compute the
time average) or along a new dimension in order to compute statitistic between
years (standard deviation, etc..)

    
    
    import cdms, MV, genutil  
    import sys  
      
    pth=sys.prefix+'/sample_data/'  
      
    files = [ pth+'u_2000.nc',  
              pth+'u_2001.nc',  
              pth+'u_2002.nc',  
             ]  
      
    for file in files:  
        f=cdms.open(file)  
    &#160;&#160;&#160; u=f('u')  
      
    &#160;&#160;&#160; if file == files[0]:          # First file  
    &#160;&#160;&#160;     sh=list(u.shape)          # Create a list with the shape of the data  
    &#160;&#160;&#160;&#160;&#160;&#160;&#160; sh.insert(0,1)            # Insert value 1 in front of the list  
    &#160;&#160;&#160; &#160;&#160;&#160; accumulation = u  
    &#160;&#160;&#160;&#160;&#160;&#160;&#160; newdim = MV.reshape(u,sh) # Create a new 1D dimension  
      
    &#160;&#160;&#160; else:	  
            # add u at the end of accumaltion on dimension 0          
            accumulation = MV.concatenate((accumulation,u))  
    &#160;&#160;&#160;&#160;&#160;&#160;&#160; tmp = MV.reshape(u,sh)                # Create a new 1D dimension  
    &#160;&#160;&#160;&#160;&#160;&#160;&#160; newdim = MV.concatenate((newdim,tmp)) # Add u to the newdim over the new dimension  
      
    &#160;&#160;&#160; f.close()  
          
      
    print accumulation.shape   # All time added over the same dimension  
    print newdim.shape         # Has a new dimension for years  
      
