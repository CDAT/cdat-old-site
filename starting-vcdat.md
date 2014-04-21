---
layout: default
title: 
---

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

  * [ ![Send this page to somebody](media/mail_icon.gif) ](/cdat/tutorials/getting-started/starting-vcdat/sendto_form)
  * [ ![Print this page](media/print_icon.gif) ](/this.print\(\))

#  Starting VCDAT

[ ![Table of Contents](media/arrow-up) ](/)

[ ![Previous](media/arrow-left) ](/what-is-vcdat)

[ ![Next](media/arrow-right) ](/bookmarking)

[ Contents ](/)

[ Previous ](/what-is-vcdat)

[ Next ](/bookmarking)

 Goal:  Be able to launch VCDAT and generate a basic data plot. 

To get VCDAT started, type:

    
    
          vcdat &  
    

Locate and open the netCDF data file in the following directory: `
<CDAT_SRC_DIRECTORY>/Packages/dat/clt.nc `

Where the notation <CDAT_SRC_DIRECTORY> indicates the full path name of the
directory where you uncompressed and un-tarred the CDAT source code.  

_ Directory: _ In the "Directory" input text window, enter
<CDAT_SRC_DIRECTORY>/Packages/dat or&#160; select the file icon just to the left of
the input text window.  

_ File: _ In the "File or URL" input text window, enter "clt.nc <return>" or
select the arrow button to the right of the input text window and select
"clt.nc".  

_ Variable: _ In the "Variable" input text window, enter "clt <return>" or
select the arrow button to the right of the input text window and select
"clt".  

_ Plot: _ Select the orange "Plot" button to plot the "clt" data in standard
Boxfill graphics method form. (See figure 2.)  

 Remember:  the hierarchy of plotting is _ 'directory', 'file', 'variable', and then 'plot' _ . (See figure 1.)   

Replace Boxfill graphics method with a different plot option and re-plot.  
Select the "Boxfill" button menu to the right of the "Plot" button and select
"Isofill", then re-select the "Plot" button. (See figure 3.) Repeat this
process for other graphics methods (i.e., 'Graphics Methods' \--> 'Isofill,
Isoline, FilledIsoline', etc.).

![VCDAT](media/vcdat-1-thumb) Figure 1. Full display of VCDAT with default
settings.

![Plot_1](media/plot_1) Figure 2. Standard Boxfill data display.

![Plot_2](media/plot_2) Figure 3. Standard Isofill (i.e., contour) data
display.

[ ![Table of Contents](media/arrow-up) ](/)

[ ![Previous](media/arrow-left) ](/what-is-vcdat)

[ ![Next](media/arrow-right) ](/bookmarking)
