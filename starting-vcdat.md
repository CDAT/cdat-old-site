---
layout: default
title: Starting VCDAT
---

##  Starting VCDAT
Goal:  Be able to launch VCDAT and generate a basic data plot. 

To get VCDAT started, type:
    
          vcdat &  
    
Locate and open the netCDF data file in the following directory: 
`<CDAT_SRC_DIRECTORY>/Packages/dat/clt.nc`

Where the notation <CDAT_SRC_DIRECTORY> indicates the full path name of the
directory where you uncompressed and un-tarred the CDAT source code.  

###Directory: 
In the "Directory" input text window, enter
<CDAT_SRC_DIRECTORY>/Packages/dat or select the file icon just to the left of
the input text window.  

###File:
In the "File or URL" input text window, enter "clt.nc <return>" or
select the arrow button to the right of the input text window and select
"clt.nc".  

###Variable:
In the "Variable" input text window, enter "clt <return>" or
select the arrow button to the right of the input text window and select
"clt".  

###Plot:
Select the orange "Plot" button to plot the "clt" data in standard
Boxfill graphics method form. (See figure 2.)  

Remember:  the hierarchy of plotting is _ 'directory', 'file', 'variable', and then 'plot' _ . (See figure 1.)   

Replace Boxfill graphics method with a different plot option and re-plot.  
Select the "Boxfill" button menu to the right of the "Plot" button and select
"Isofill", then re-select the "Plot" button. (See figure 3.) Repeat this
process for other graphics methods (i.e., 'Graphics Methods' \--> 'Isofill,
Isoline, FilledIsoline', etc.).

![VCDAT](media/images/vcdat-1-thumb)

Figure 1. Full display of VCDAT with default settings.

![Plot_1](media/images/plot_1) 

Figure 2. Standard Boxfill data display.

![Plot_2](media/images/plot_2) 

Figure 3. Standard Isofill (i.e., contour) data display.
