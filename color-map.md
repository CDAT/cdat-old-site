---
layout: default
title: Color Map 
---
##  Color Map
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

![Graphics_1](media/images/graphics_1)

To view or modify the colormap GUI, depress the "Option" menu to the right of
"VCS Canvas 1". Then move the pointer over the "Colormap Editor..." item and
select.  

![Graphics_9](media/images/graphics_9)

The "Colormap Editor" window will appear. See figure 32. The colormap default
is "rainbow" unless otherwise specified by the user.  

View specified color indices:   
In the "View color indices" input text window, enter one color index value
followed by the <return> key (e.g., 168 <return>). To view multiple random
color indices, enter the color index values separated by commas and the
<return> key (e.g., 168, 233, 184, 39, 255, 16<return>). To view multiple
random ranges of color indices, enter: the first color index, a colon, and the
last color index (e.g., 0:33, 78:90, 167:189, 242, 255,243,247,245<return>).
Be sure to reset the View color indices back to 0:255.  

Change a color index:   
Select the color index 134. Use the "Red" slider, arrow button, or input text
window to change the value to 6. Change the "Green" value to 57, and the
"Blue" value to 70. The color change is immediate on the Colormap GUI.  

Blending colors between two indices:   
The color index 134 should still be highlighted. (If not, then select it.) Now
select color index 184. All color indices between 134 and 184 are highlighted.
Change 184's "Red" value to 75, "Green" value to 5, and "Blue" value to 60.
Now depress the "Edit" menu and select "Blend Colors". The range from 134 to
184 will gradually fade from one color to the other. See figure 33.  

Copy and paste color indices:   
Select color index 134, then 184 to highlight the color range. Now select the
"Copy" menu item found under the "Edit" menu. To paste, select color index 16,
then select the "Paste" menu item found under the "Edit" menu. See figure 34.  

Reverse the colormap:   
To reverse the colormap, select color index 239, then 16. All color indices
between 239 and 16 will be highlighted. Select the "Copy" menu item found
under the "Edit" menu. Now select color index 16, then the "Paste" menu item
found unde the "Edit" menu. The colormap is now reversed. See figure 35.  

Applying your changes:   
To set the colormap changes, depress the "File" menu and select the "Save
(i.e., Apply Changes)" menu option. The plot displayed in the VCS Canvas will
change accordingly. See figure 36.  

Selecting similiar alternative colors:   
Select color index 134, then select the 134 color button located in the lower
right corner of the colormap GUI. The "Select a Similiar Color" GUI will
appear. See figure 37. Change the "RGB Values to:&#160; "R" value 58; "G" value
100; "B" value 70.&#160; The color selection below will change dynamically. Change
the "Number of Columns" and "Number of Rows" values to 10. Select color index
44, then select the "OK" button below. The color index 134 now shows the
alternative color. See figure 38\.  

Selecting a different colormap:   
To select a different colormap, depress the "Options" menu and select the
"Select Colormap" option. The "Select VCS Colormap" GUI will appear. See
figure 39. Select the "ASD" colormap and then the "Apply" button.  

Be sure to reset the colormap back to "rainbow" before moving onto the next
example.

![Colormap_1](media/images/colormap_1)  
Figure 32. Display results from selecting the "Colormap Editor..." menu
option.  

![Colormap_2](media/images/colormap_2)  
Figure 33. Colormap "Blend Colors" display results.  

![Colormap_3](media/images/colormap_3)  
Figure 34. Colormap "Copy and Paste" display results.  

![Colormap_4](media/images/colormap_4)  
Figure 35. Reverse colormap "Copy and Paste" display results.  

![Colormap_5](media/images/colormap_5)  
Figure 36. Colormap "Apply" display results.  

![Colormap_6](media/images/colormap_7)  
Figure 37. Select a similiar color GUI display results.  

![Colormap_8](media/images/colormap_8)  
Figure 38. Select a similiar color replacement display results.  

![Colormap_7](media/images/colormap_6)  
Figure 39. Select colormap GUI display results.  

