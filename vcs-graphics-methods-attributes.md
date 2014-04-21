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

  * [ ![Send this page to somebody](media/mail_icon.gif) ](/cdat/tutorials/getting-started/vcs-graphics-methods-attributes/sendto_form)
  * [ ![Print this page](media/print_icon.gif) ](/this.print\(\))

#  VCS Boxfill Graphics Methods Attributes

[ ![Table of Contents](media/arrow-up) ](/)

[ ![Previous](media/arrow-left) ](/data-plot-extremes)

[ ![Next](media/arrow-right) ](/multiple-plots)

[ Contents ](/)

[ Previous ](/data-plot-extremes)

[ Next ](/multiple-plots)

 Goal:  To introduce you to VCS Boxfill graphics methods (GM) and setting its attributes. 

Reselect the "clt" Variable in the "Variable" selection window. This will
reinitialize the "Dimension Manipulation Panel". Select the orange "Plot"
button to display the "clt" data set. Make sure the graphics method selected
is "Boxfill".  

A graphics method defines how the array data will be graphically represented
on the VCS Canvas.  

![Graphics_1](media/graphics_1)  
  
To modify graphics method attributes, depress the "Option" menu to the right
of "VCS Canvas 1". Then move the pointer over the "Set Graphics Methods
Attributes&#8230;" item and select.  

![Graphics_9](media/graphics_9)

  
The "Graphics Method Attribute Settings" window will appear. See figure 20.
The "Boxfill" graphics method tab is selected by default.  

To view and change the graphics method attribute, select the appropriate
graphics method tab at the top of the GUI (e.g., "Boxfill", "Continents",
"Contour", etc.). If "Boxfill" is not selected, then select the "Boxfill" tab.  

_ Log10 Boxfill: _  
There are three Boxfill types. Change the "Boxfill type" to "log10", then
change "Color 1" value to 55 and "Color 2" value to 200. Select the "Preview"
button at the bottom of the page. See figure 21. Note, the color index values
ranges from 0 to 255. Color index values 240 through 255 are immutable color
indexes. For more information on color indexes and the color map, please see
the color map section.

_ Custom Boxfill: _  
Select "custom" for the "Boxfill type". (You may need to scroll the GUI scroll
bar located at the bottom to the right in order to see the "custom" toggle
button.) From the original boxfill plot, we know that the data ranges from 0
to 100. Scroll the GUI down until you see the "Custom Settings" section. In
the "Ranges" section, enter: 10, 20, 35.4, 50, 60, 90. In the "Colors" section
enter: 242, 243, 244, 245, 248. Now select the "Preview" button. See figure
22.  

In the "General Settings" section, enter the "Missing" color index value 240.
The color index 240 is white. Scroll the window down to the "Custom Settings".
For the "Minimum Value" section enter: 20. For the "Maximun Value" section
enter: 80. For the "Number of Intervals section enter: 10. Now select the
"Generate Ranges" button and the "Ranges" and "Colors" values will be
automatically generated for you. Select the "Preview" button below to view the
changes. See figure 23.  

_ Linear Boxfill: _  
Select the "Reset" button at the bottom of the GUI. This action will redisplay
the plot with its original default settings. In the "General Settings"
section, for the "Legend Labels" enter: (20:'twenty', 40:'forty', 60:'sixty',
80:'eighty'). In the "Linear and Log Settings" section enter 20 for "Level 1",
80 for "Level 2", 100 for "Color 1", and 200 for "Color 2". Now select the
"Preview" button. See figure 24.  

Before exiting the GUI, select the "Cancel button. Do not save the settings.  

![Graphics_method_1](media/graphics_method_1)

Figure 20.&#160; Display results from selecting the "Set Graphics Method
Attributes..." menu option.  

![Graphics_method_2](media/graphics_method_2)  
Figure 21. "log10" display results.  

![Graphics_method_3](media/graphics_method_3)  
Figure 22. "custom" display results.  

![Graphics_method_5](media/graphics_method_5)  
Figure 23. "custom" display results with automatic generation of ranges and
colors.  

![Graphics_method_5](media/graphics_method_4)  
Figure 24. "linear" display results with "legend Labels" changes.  

[ ![Table of Contents](media/arrow-up) ](/)

[ ![Previous](media/arrow-left) ](/data-plot-extremes)

[ ![Next](media/arrow-right) ](/multiple-plots)
