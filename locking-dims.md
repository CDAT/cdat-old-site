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

  * [ ![Send this page to somebody](media/mail_icon.gif) ](/cdat/tutorials/vcdat-lite/locking-dims/sendto_form)
  * [ ![Print this page](media/print_icon.gif) ](/this.print\(\))

#  Locking Dimensions in VCDAT

[ ![Table of Contents](media/arrow-up) ](/)

[ ![Previous](media/arrow-left) ](/variable-list)

[ ![Next](media/arrow-right) ](/graphical-methods)

[ Contents ](/)

[ Previous ](/variable-list)

[ Next ](/graphical-methods)

 Goal:  To learn all about locking and unlocking dimentions in VCDAT. 

Another great feature introduced in CDAT 4.3 is the ability to  lock (or pin
down) and unlock any dimension  . This is done by clicking on the little pin
icon at the top of each axis dimension on the left side of the dimensions
navigation sliders.&#160; When you click on the pin, all the settings for this
dimension will be saved as default to use for all other variables that have
this dimension. In this way you can choose a region you want to look at by
selecting the region with the sliders, then pushing the pin in (clicking the
pin) and freezing that dimension. Now no matter what variable you will choose
next or even different file, different variable with this dimension, you will
always see the plot&#160; for your selected, frozen region. With the pin in (the
settings frozen as default) you can still move the sliders and zoom in and
out, change&#160; the region etc., but this will not affect the default setting
that you set when you push the pin in.

Often one needs to look at the zoom of a particular dimension, say only a
window in time, or particular region in (lon, lat) space or particular height
region. You will now have the ability to choose say a height region, lock the
height dimension, and now whenever you plot any variable that has this
dimention, it will be displayed within chosen height region only. If you are
curious to see the full height but do not want to reset the new default, you
can move the sliders without unlocking the height dimensions settings. &#160;If on
the other hand you want to reset the defaults, just unlock the lock and choose
new region, then lock the dim again to keep it as new default. &#160;You will find
it extremelly handy at times. The locks work also on the dimensions/axis order
and are very handy when you need to change the pressure levels to be displayed
from highest to lowest.

Let's see how it works.

Open VCDAT and find the sample file  'clt.nc'  in the  'sample_data' 
directory of your CDAT installation. Open this file and choose the  'clt' 

variable. Let's select a boxfill plot

![plot_1.jpg](media/image_preview)

Let's now move the longitude sliders to span (-180,0), then click on the pin
next to the longitude axis (notice the pin in the different direction then
other pins - it is pinned):

![vcdat_l_9.jpg](media/image_preview)

and select a boxfill plot

![plot_3.jpg](media/image_preview)  
  

Now choose a different file 'geo.1deg.ctl' and select 'orog' orography
variable, and plot boxfill

![plot_4.jpg](media/image_preview)

  
You can see that the plot is over the previously selected region. Let's now
change the region to (0,180)  without touching the pin,  see the resulting
plot:

![plot_5.jpg](media/image_preview)

But now if we will choose a different variable and plot it, the longitude
region will be set to the previously selected (-180,0)

[ ![Table of Contents](media/arrow-up) ](/)

[ ![Previous](media/arrow-left) ](/variable-list)

[ ![Next](media/arrow-right) ](/graphical-methods)
