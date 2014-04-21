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

  * [ ![Send this page to somebody](media/mail_icon.gif) ](/cdat/tutorials/getting-started/dimension-subsetting/sendto_form)
  * [ ![Print this page](media/print_icon.gif) ](/this.print\(\))

#  Dimension Subsetting

[ ![Table of Contents](media/arrow-up) ](/)

[ ![Previous](media/arrow-left) ](/bookmarking)

[ ![Next](media/arrow-right) ](/dimension-manipulation)

[ Contents ](/)

[ Previous ](/bookmarking)

[ Next ](/dimension-manipulation)

 Goal:  To introduce you to dimension subsetting, node striding, and, reversing. 

![Dimension](media/dimension)

There are three ways to subset a dimension:

  *  Method 1:  Edit the "longitude" dimension's coordinate value entry window. In the window, replace text with "-90:90 by 5". Then press the 'Enter' key to register the change. 

![Dimension 1](media/dimensions_1)

 Remember:  the text string represents "first : last by stride". 

  *  Method 2:  Select the arrow button to the right of the "latitude" entry window. Select the -70 value in the item list to get the first or single value. Repeat the process and select 70. This will complete the range for the "latitude" dimension (i.e., "-70 : 70 by 1") . See images below.   

![Dimensions 2](media/dimensions_2) ![Dimensions 3](media/dimensions_3)
![Dimensions 4](media/dimensions_4)

  *  Method 3:  For the time dimension, move the top slider to "1982-1-1 0:0" to set the first value and the bottom slider to "1984-12-1 0:0" to set the last value. The first values under the sliders represent the first value (i.e., 1982-1-1 0:0) and the second value under the sliders represent the second or last value (i.e., 1984-12-1 0:0). These values are dynamically updated as the sliders move.   

![Dimensions_5](media/dimensions_5)

Select the orange "Plot" button above to see results. The plotted results can
be seen in figure 6.

 Try Reversing the Dimension Order:  To reverse the order of the "longitude" dimension, move the top slider to the right and stop at the value of 90 and the bottom slider to the left and stop at the value of -90 . Notice the change in the values under the sliders.   

![Dimensions_8](media/dimensions_8)  

Select the orange "Plot" button above to see results. The plotted results can
be seen in figure 7.  
  

![Dimensions_6](media/dimensions_6)  
Figure 6. Subsetted display results.  

![Dimensions_7](media/dimensions_7)  
Figure 7. Reversed "longitutde" display results.  

[ ![Table of Contents](media/arrow-up) ](/)

[ ![Previous](media/arrow-left) ](/bookmarking)

[ ![Next](media/arrow-right) ](/dimension-manipulation)
