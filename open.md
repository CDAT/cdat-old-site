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

  * [ ![Send this page to somebody](media/mail_icon.gif) ](/cdat/tutorials/cdatbasics/cdms-basics/open/sendto_form)
  * [ ![Print this page](media/print_icon.gif) ](/this.print\(\))

#  Opening Files, Reading-in Data

Explains how to open a file a read-in variables.

CDMS is an easy to use interface to read in data from multiple binary formats,
such as NetCDF, HDF, Grads/GRIB (with a control file), PP, DRS (special build
need), ...

CDMS is also an OpenDAP client, you can access OpenDAP served data by typing
the URL instead of the file name

In this example we will open a file contained in your cdat distribution under
the sample_data directory and read the variable named 'clt' contained in it.

    
    
    # Import the cdms module and the sys module
    import cdms,sys
    
    # Construct the string containing the path to the data_file
    file_name=sys.prefix+'/sample_data/clt.nc'
    
    # open the file with the cdms interface
    file=cdms.open(file_name)
    
