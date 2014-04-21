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

  * [ ![Send this page to somebody](media/mail_icon.gif) ](/cdat/tutorials/getting-started/color-map/sendto_form)
  * [ ![Print this page](media/print_icon.gif) ](/this.print\(\))

#  Color Map

[ ![Table of Contents](media/arrow-up) ](/)

[ ![Previous](media/arrow-left) ](/alter-plot)

[ ![Next](media/arrow-right) ](/animation)

[ Contents ](/)

[ Previous ](/alter-plot)

[ Next ](/animation)

 Goal:  To introduce you to the VCS colormap and the Colormap GUI. 

Reselect the "clt" Variable in the "Variable" selection window. This will
reinitialize the "Dimension Manipulation Panel". Select the orange "Plot"
button to display the "clt" data set. Make sure the graphics method selected
is "Boxfill".

There can only be one active colormap at any given instance, and there is
always an active colormap. A colormap contains 240 user definable colors and
16 immutable colors. The color mixtures are defined in terms of percentages of
red, green, and blue colors (0 to 100% for each). The immutable colors are, in
order: 240-white, 241-black, 242-red, 243-green, 244-blue, 245-yellow,
246-cyan, 247-magenta, 248-orange, 249-brown, 250-violet, 251-olive green,
252-grey, 253-light green, 254-light red, and 255-light blue.  

![Graphics_1](media/graphics_1)

To view or modify the colormap GUI, depress the "Option" menu to the right of
"VCS Canvas 1". Then move the pointer over the "Colormap Editor..." item and
select.  

![Graphics_9](media/graphics_9)

The "Colormap Editor" window will appear. See figure 32. The colormap default
is "rainbow" unless otherwise specified by the user.  

 _ View specified color indices: _    
In the "View color indices" input text window, enter one color index value
followed by the <return> key (e.g., 168 <return>). To view multiple random
color indices, enter the color index values separated by commas and the
<return> key (e.g., 168, 233, 184, 39, 255, 16<return>). To view multiple
random ranges of color indices, enter: the first color index, a colon, and the
last color index (e.g., 0:33, 78:90, 167:189, 242, 255,243,247,245<return>).
Be sure to reset the View color indices back to 0:255.  

 _ Change a color index: _    
Select the color index 134. Use the "Red" slider, arrow button, or input text
window to change the value to 6. Change the "Green" value to 57, and the
"Blue" value to 70. The color change is immediate on the Colormap GUI.  

 _ Blending colors between two indices: _    
The color index 134 should still be highlighted. (If not, then select it.) Now
select color index 184. All color indices between 134 and 184 are highlighted.
Change 184's "Red" value to 75, "Green" value to 5, and "Blue" value to 60.
Now depress the "Edit" menu and select "Blend Colors". The range from 134 to
184 will gradually fade from one color to the other. See figure 33.  

 _ Copy and paste color indices: _    
Select color index 134, then 184 to highlight the color range. Now select the
"Copy" menu item found under the "Edit" menu. To paste, select color index 16,
then select the "Paste" menu item found under the "Edit" menu. See figure 34.  

 _ Reverse the colormap: _    
To reverse the colormap, select color index 239, then 16. All color indices
between 239 and 16 will be highlighted. Select the "Copy" menu item found
under the "Edit" menu. Now select color index 16, then the "Paste" menu item
found unde the "Edit" menu. The colormap is now reversed. See figure 35.  

 _ Applying your changes: _    
To set the colormap changes, depress the "File" menu and select the "Save
(i.e., Apply Changes)" menu option. The plot displayed in the VCS Canvas will
change accordingly. See figure 36.  

 _ Selecting similiar alternative colors: _    
Select color index 134, then select the 134 color button located in the lower
right corner of the colormap GUI. The "Select a Similiar Color" GUI will
appear. See figure 37. Change the "RGB Values to:&#160; "R" value 58; "G" value
100; "B" value 70.&#160; The color selection below will change dynamically. Change
the "Number of Columns" and "Number of Rows" values to 10. Select color index
44, then select the "OK" button below. The color index 134 now shows the
alternative color. See figure 38\.  

 _ Selecting a different colormap: _    
To select a different colormap, depress the "Options" menu and select the
"Select Colormap" option. The "Select VCS Colormap" GUI will appear. See
figure 39. Select the "ASD" colormap and then the "Apply" button.  

Be sure to reset the colormap back to "rainbow" before moving onto the next
example.

![Colormap_1](media/colormap_1)  
Figure 32. Display results from selecting the "Colormap Editor..." menu
option.  

![Colormap_2](media/colormap_2)  
Figure 33. Colormap "Blend Colors" display results.  

![Colormap_3](media/colormap_3)  
Figure 34. Colormap "Copy and Paste" display results.  

![Colormap_4](media/colormap_4)  
Figure 35. Reverse colormap "Copy and Paste" display results.  

![Colormap_5](media/colormap_5)  
Figure 36. Colormap "Apply" display results.  

![Colormap_6](media/colormap_7)  
Figure 37. Select a similiar color GUI display results.  

![Colormap_8](media/colormap_8)  
Figure 38. Select a similiar color replacement display results.  

![Colormap_7](media/colormap_6)  
Figure 39. Select colormap GUI display results.  

  

[ ![Table of Contents](media/arrow-up) ](/)

[ ![Previous](media/arrow-left) ](/alter-plot)

[ ![Next](media/arrow-right) ](/animation)
