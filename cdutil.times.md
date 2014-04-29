---
layout: default
title:
---

 [ Skip to content. ](/cdat/source/api-reference/cdutil.times.html) | [ Skip to
navigation ](/cdat/source/api-reference/cdutil.times.html)

Search Site

[ Advanced Search&#8230; ](/search_form)

#  [ PCMDI Software Portal ](/)

#####  Sections

  * [ Home ](/)

#####  Personal tools

  * [ Log in ](/login_form)

You are here:  [ Home ](/) -> [ CDAT ](/cdat) -> [ Source Code ](/cdat/source)
-> [ API Reference ](/cdat/source/api-reference) -> Python: module
cdutil.times

[ Navigation ](/sitemap)

    

  * [ Home ](/)

  * [ PCMDI Home Page ](/)

  * [ News ](/news)

  * [ CDAT ](/cdat)

    * [ Download and Install ](/cdat/download)

    * [ Screenshots ](/cdat/screenshots)

    * [ Contrib Packages ](/cdat/contrib)

    * [ Getting Started ](/cdat/getting_started)

    * [ Tutorials ](/cdat/tutorials)

    * [ Quick Reference ](/cdat/quick_reference)

    * [ FAQ ](/cdat/FAQ)

    * [ Manuals ](/cdat/manuals)

    * [ Tips and Tricks ](/cdat/tips_and_tricks)

    * [ Source Code ](/cdat/source)

      * [ API Reference ](/cdat/source/api-reference)

        * [ Python: module cdutil.times ](/cdat/source/api-reference/cdutil.times.html)

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

  * [ ![Send this page to somebody](media/mail_icon.gif) ](/cdat/source/api-reference/cdutil.times.html/sendto_form)
  * [ ![Print this page](media/print_icon.gif) ](/this.print\(\))

#  Python: module cdutil.times

  
  
 [ cdutil  ](/cdutil.html) .times 
[ index ](/)  

  
 Modules 

` `

[ MA ](/MA.html)  
[ cdms.MV ](/cdms.MV.html)  

[ Numeric ](/Numeric.html)  
[ cdms ](/cdms.html)  

[ cdtime ](/cdtime.html)  
[ string ](/string.html)  

[ sys ](/sys.html)  
[ types ](/types.html)  

  
 Classes 

` `

[ TimeSlicer ](/cdutil.times.html)

    

[ ASeason ](/cdutil.times.html)

    

[ Seasons ](/cdutil.times.html)

  
class  ASeason  ( [ TimeSlicer ](/cdutil.times.html) )

` `

Methods defined here:  

 __init__  (self) 

* * *

Methods inherited from [ TimeSlicer ](/cdutil.times.html) :  

 average  (self, slab, slices, bounds, norm, criteriaarg  =None  , statusbar  =None  ) 
     ` Return&#160;the&#160;average&#160;of&#160;the&#160;result&#160;of&#160;slicer   
Input:  
slab&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;:&#160;the&#160;slab&#160;on&#160;which&#160;to&#160;operate  
slices&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;:&#160;the&#160;slices&#160;for&#160;each&#160;part  
bounds&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;:&#160;the&#160;length&#160;of&#160;each&#160;slice  
norm&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;:&#160;the&#160;actual&#160;length&#160;of&#160;each&#160;"season"  
criteriaarg&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;:&#160;arguments&#160;for&#160;criteria&#160;thing  
Output:  
out&#160;:&#160;the&#160;average&#160;of&#160;slab,&#160;masked&#160;by&#160;criteria `

 departures  (self, slab, slicerarg  =None  , criteriaarg  =None  , ref  =None  , statusbar  =None  ) 

 get  (self, slab, slicerarg  =None  , criteriaarg  =None  , statusbar  =None  ) 

 statusbar1  (self, i, n, statusbar) 

 statusbar2  (self, statusbar) 

  
class  Seasons  ( [ ASeason ](/cdutil.times.html) )

` `

Method resolution order:

     [ Seasons ](/cdutil.times.html)
     [ ASeason ](/cdutil.times.html)
     [ TimeSlicer ](/cdutil.times.html)

* * *

Methods defined here:  

 __init__  (self, *seasons) 

 climatology  (self, slab, criteriaarg  =None  , criteriaargclim  =None  , statusbar  =None  ) 
     ` Compute&#160;the&#160;climatology&#160;from&#160;a&#160;slab   
Input:  
slab  
criteriaarg&#160;&#160;&#160;&#160;&#160;:&#160;the&#160;argument&#160;for&#160;criteria&#160;function&#160;when&#160;slicing&#160;the&#160;season
(and&#160;clim)  
criteriaargclim&#160;:&#160;the&#160;argument&#160;for&#160;criteria&#160;function&#160;when&#160;averaging&#160;the
seasons&#160;together  
if&#160;different&#160;from&#160;criteriarg  
Output:  
The&#160;Average&#160;of&#160;the&#160;seasons&#160;in&#160;the&#160;order&#160;passed&#160;when&#160;constructing&#160;it  
i.e&#160;if&#160;DJF&#160;and&#160;JJA&#160;are&#160;asked,&#160;the&#160;output&#160;will&#160;have&#160;the&#160;average&#160;DJF&#160;first,&#160;then
the&#160;average&#160;JJA  
2&#160;criteria&#160;can&#160;be&#160;passed&#160;one&#160;for&#160;the&#160;slicing&#160;part&#160;and&#160;one&#160;for&#160;the&#160;climatology
part `

 departures  (self, slab, slicerarg  =None  , criteriaarg  =None  , ref  =None  , statusbar  =None  ) 
     ` Return&#160;the&#160;departures&#160;for&#160;the&#160;list&#160;of&#160;season&#160;you&#160;specified,&#160;returned&#160;in&#160;chronological&#160;order   
i.e.&#160;if&#160;you&#160;asked&#160;for&#160;DJF&#160;and&#160;JJA&#160;and&#160;the&#160;first&#160;season&#160;of&#160;your&#160;dataset&#160;is&#160;JJA
you&#160;will&#160;have&#160;a&#160;JJA&#160;first&#160;!!!!  
Check&#160;your&#160;time&#160;axis&#160;coordinate&#160;!!!  
To&#160;pass&#160;a&#160;specific&#160;array&#160;from&#160;which&#160;to&#160;compute&#160;departures,&#160;please&#160;pass&#160;1&#160;per
season&#160;(or&#160;None&#160;if&#160;we&#160;should&#160;compute&#160;it)  
for&#160;info&#160;one&#160;default&#160;departures&#160;see:&#160;departures2.__doc__ `

 get  (self, slab, slicerarg  =None  , criteriaarg  =None  , statusbar  =None  ) 
     ` Get&#160;the&#160;seasons&#160;asked&#160;for&#160;and&#160;return&#160;them&#160;in&#160;chronological&#160;order   
i.e.&#160;if&#160;you&#160;asked&#160;for&#160;DJF&#160;and&#160;JJA&#160;and&#160;the&#160;first&#160;season&#160;of&#160;your&#160;dataset&#160;is&#160;JJA
you&#160;will&#160;have&#160;a&#160;JJA&#160;first&#160;!!!!  
Check&#160;your&#160;time&#160;axis&#160;coordinate&#160;!!!  
slicerarg&#160;will&#160;be&#160;ignored  
it&#160;is&#160;recomended&#160;to&#160;use&#160;Season(slab,criteria=mycriteriaarguments)&#160;syntax  
rather&#160;than&#160;Season(slab,None,None,mycriteriaarguments)  
Now&#160;for&#160;the&#160;original&#160;doc&#160;of&#160;the&#160;get&#160;function&#160;see&#160;get2__doc__: `

* * *

Methods inherited from [ TimeSlicer ](/cdutil.times.html) :  

 average  (self, slab, slices, bounds, norm, criteriaarg  =None  , statusbar  =None  ) 
     ` Return&#160;the&#160;average&#160;of&#160;the&#160;result&#160;of&#160;slicer   
Input:  
slab&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;:&#160;the&#160;slab&#160;on&#160;which&#160;to&#160;operate  
slices&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;:&#160;the&#160;slices&#160;for&#160;each&#160;part  
bounds&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;:&#160;the&#160;length&#160;of&#160;each&#160;slice  
norm&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;:&#160;the&#160;actual&#160;length&#160;of&#160;each&#160;"season"  
criteriaarg&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;:&#160;arguments&#160;for&#160;criteria&#160;thing  
Output:  
out&#160;:&#160;the&#160;average&#160;of&#160;slab,&#160;masked&#160;by&#160;criteria `

 statusbar1  (self, i, n, statusbar) 

 statusbar2  (self, statusbar) 

  
class  TimeSlicer 

` `

` Author&#160;:&#160;Charles&#160;Doutriaux:&#160;doutriaux1@llnl.gov  
Date:&#160;April&#160;2001  
Returns&#160;masked&#160;average&#160;of&#160;specific&#160;time&#160;slices  
"slicer"&#160;determine&#160;which&#160;slices&#160;of&#160;the&#160;Transient&#160;Variable&#160;(TV)&#160;are&#160;processed  
"criteria"&#160;gets&#160;TV&#160;(with&#160;time&#160;dimension)&#160;and&#160;returns&#160;a&#160;"timeless"&#160;mask,&#160;used
to&#160;mask&#160;the&#160;averaged&#160;slices  
  
"slicer"  
Input:  
-&#160;Time&#160;Axis   
-&#160;User&#160;argument&#160;(can&#160;be&#160;anything)&#160;(in&#160;a&#160;list&#160;if&#160;more&#160;than&#160;one&#160;argument)   
Output:  
indices&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;:&#160;the&#160;indices&#160;for&#160;each&#160;season:  
[[i1,i2,...,il],  
[j1,j2,...,jm],  
...,  
[k1,k2,...kn]]  
bounds&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;:&#160;the&#160;bounds&#160;covered&#160;by&#160;each&#160;slice&#160;for&#160;each&#160;season:  
[[[i1b1,i1b2],[i2b1,i2b2],...,[ilb1,ilb2]],  
[[[j1b1,j1b2],[j2b1,j2b2],...,[jmb1,jmb2]],  
...,  
[[k1b1,k1b2],[k2b1,k2b2],...,[knb1,knb2]]]  
norm&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;:&#160;the&#160;actual&#160;length&#160;of&#160;each&#160;"season",&#160;and&#160;its&#160;start  
[[Li,Si],  
[Lj,Sj],  
...,  
[Lk,Sk]]  
"criteria"  
Input:  
-&#160;slab&#160;:&#160;a&#160;slab   
-&#160;mask:&#160;&#160;the&#160;actual&#160;percentage&#160;of&#160;data&#160;in&#160;each&#160;subset&#160;used&#160;to&#160;produce&#160;the&#160;slab   
the&#160;bounds&#160;of&#160;its&#160;first&#160;(time)&#160;dimension&#160;must&#160;be&#160;correct  
they&#160;will&#160;be&#160;used&#160;by&#160;centroid  
-&#160;spread:&#160;the&#160;begining&#160;and&#160;end&#160;time&#160;of&#160;the&#160;slice&#160;processed   
-&#160;User&#160;argument&#160;(can&#160;be&#160;anything)   
Output:  
-&#160;the&#160;slab,&#160;masked   
  
Once&#160;constructed&#160;the&#160;object,&#160;beside&#160;"slicer"&#160;and&#160;"criteria"&#160;has&#160;3&#160;functions:  
  
"get"&#160;:&#160;which&#160;returns&#160;the&#160;slices&#160;wanted,&#160;appropriately&#160;masked  
Input:  
slab&#160;:&#160;the&#160;slab&#160;on&#160;which&#160;to&#160;operate  
sliceruserargument&#160;&#160;:&#160;anything&#160;your&#160;slicer&#160;function&#160;needs,&#160;default&#160;is&#160;None  
criteriauserargument:&#160;anything&#160;your&#160;criteria&#160;function&#160;needs,&#160;default&#160;is&#160;None  
Output:  
out&#160;&#160;:&#160;averaged&#160;and&#160;masked&#160;slices&#160;of&#160;slab  
  
"departures"&#160;:&#160;which&#160;returns&#160;the&#160;departures&#160;of&#160;slab&#160;from&#160;the&#160;result&#160;of&#160;get  
Input:  
slab&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;:&#160;slab&#160;from&#160;which&#160;the&#160;we&#160;want&#160;to&#160;get&#160;the&#160;departure  
sliceruserargument&#160;&#160;:&#160;anything&#160;your&#160;slicer&#160;function&#160;needs,&#160;default&#160;is&#160;None  
criteriauserargument:&#160;anything&#160;your&#160;criteria&#160;function&#160;needs,&#160;default&#160;is&#160;None  
(ref):&#160;optional&#160;&#160;&#160;&#160;&#160;:&#160;result&#160;from&#160;get&#160;or&#160;equivalent&#160;precomputed  
  
Output:  
out&#160;:&#160;departure&#160;of&#160;slab&#160;from&#160;ref  
  
"average"&#160;:&#160;which&#160;return&#160;the&#160;average&#160;of&#160;the&#160;result&#160;of&#160;get  
Input:  
slab&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;:&#160;the&#160;slab&#160;on&#160;which&#160;to&#160;operate  
slices&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;:&#160;the&#160;slices&#160;for&#160;each&#160;part  
bounds&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;:&#160;the&#160;length&#160;of&#160;each&#160;slice  
norm&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;:&#160;the&#160;actual&#160;length&#160;of&#160;each&#160;"season"  
criteriaarg&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;:&#160;arguments&#160;for&#160;criteria&#160;thing  
Output:  
out&#160;:&#160;the&#160;average&#160;of&#160;slab,&#160;masked&#160;by&#160;criteria  
  
Example&#160;of&#160;construction:  
TS= [ TimeSlicer ](/) (slicerfunc,criteriafunc)  
myres=TS(myslab,[[slicerarg,[criteriaarg]])  
myresdeparture=TS(myslab,[[slicerarg,[criteriaarg,ref]]]  
`

Methods defined here:  

 __init__  (self, slicerfunction  =None  , criteriafunction  =None  ) 

 average  (self, slab, slices, bounds, norm, criteriaarg  =None  , statusbar  =None  ) 
     ` Return&#160;the&#160;average&#160;of&#160;the&#160;result&#160;of&#160;slicer   
Input:  
slab&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;:&#160;the&#160;slab&#160;on&#160;which&#160;to&#160;operate  
slices&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;:&#160;the&#160;slices&#160;for&#160;each&#160;part  
bounds&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;:&#160;the&#160;length&#160;of&#160;each&#160;slice  
norm&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;:&#160;the&#160;actual&#160;length&#160;of&#160;each&#160;"season"  
criteriaarg&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;:&#160;arguments&#160;for&#160;criteria&#160;thing  
Output:  
out&#160;:&#160;the&#160;average&#160;of&#160;slab,&#160;masked&#160;by&#160;criteria `

 departures  (self, slab, slicerarg  =None  , criteriaarg  =None  , ref  =None  , statusbar  =None  ) 

 get  (self, slab, slicerarg  =None  , criteriaarg  =None  , statusbar  =None  ) 

 statusbar1  (self, i, n, statusbar) 

 statusbar2  (self, statusbar) 

  
 Functions 

` `

 centroid  (msk, bounds, coords  =None  ) 
     ` Computes&#160;the&#160;centroid&#160;of&#160;a&#160;bunch&#160;of&#160;point   
Authors:&#160;Charles&#160;Doutriaux/Karl&#160;Taylor  
Date:&#160;April&#160;2001  
Input:  
s:&#160;a&#160;slab  
bounds&#160;:&#160;the&#160;bounds&#160;of&#160;the&#160;overall&#160;thing  
coords&#160;:&#160;the&#160;coordinate&#160;spanned&#160;by&#160;each&#160;subset  
Output:  
centroid:&#160;a&#160;slab&#160;representing&#160;the&#160;centroid,&#160;values&#160;are&#160;between&#160;0&#160;(data&#160;evenly
distributed&#160;evenly&#160;across&#160;the&#160;center)&#160;and&#160;+/-1&#160;(data&#160;not&#160;evenly&#160;distributed)  
centroid&#160;is&#160;1D&#160;less&#160;than&#160;s `

 cyclicalcentroid  (s, bounds, coords  =None  ) 
     ` returns&#160;the&#160;centroid,&#160;but&#160;this&#160;assumes&#160;cyclical&#160;axis,&#160;therefore&#160;spread&#160;the&#160;points&#160;around&#160;a&#160;circle,&#160;before&#160;computing&#160;the&#160;centroid   
Usage:  
cyclecentroid= [ cyclicalcentroid ](/) (s,bounds)  
Input:  
s:&#160;a&#160;slab  
bounds&#160;:&#160;the&#160;bounds&#160;of&#160;the&#160;overall&#160;thing  
coords&#160;:&#160;the&#160;coordinate&#160;spanned&#160;by&#160;each&#160;subset  
Output:  
cyclecentroid&#160;:&#160;slab&#160;is&#160;same&#160;shape&#160;than&#160;s&#160;but&#160;without&#160;the&#160;1st&#160;dim `

 dayBasedSlicer  (tim, arg  =None  ) 
     ` slicer&#160;function&#160;for&#160;the [ TimeSlicer ](/) class   
select&#160;days  
Author&#160;:&#160;Charles&#160;Doutriaux,&#160;doutriaux1@llnl.gov  
Original&#160;Date:&#160;June,&#160;2003  
Last&#160;Modified:&#160;...  
Input:  
-&#160;tim:&#160;time&#160;axis   
-&#160;arg:&#160;character&#160;string&#160;representing&#160;the&#160;desired&#160;day/days&#160;or&#160;day&#160;number(s)&#160;(jan&#160;1st,&#160;is&#160;day&#160;0,&#160;feb&#160;29th&#160;is&#160;day&#160;59.5...)   
day&#160;are&#160;represented&#160;as&#160;"Jan-01"&#160;"January-01"&#160;"jan-1",&#160;"1-january",&#160;case&#160;does
not&#160;matter  
days&#160;can&#160;be&#160;represented&#160;by&#160;2&#160;number&#160;but&#160;then&#160;month&#160;is&#160;assumed&#160;to&#160;be&#160;first&#160;!
e.g&#160;"01-25"&#160;=&#160;"jan-25"  
you&#160;can&#160;mix&#160;definitions  
Output:  
\- `

 generalCriteria  (slab, mask, spread, arg) 
     ` Default&#160;Conditions:   
50%&#160;of&#160;the&#160;data  
AND  
Centroid&#160;<&#160;x&#160;(in&#160;absolute&#160;value),&#160;centroid&#160;is&#160;always&#160;between&#160;0&#160;(perfect&#160;and&#160;1,
none&#160;perfect)  
by&#160;default&#160;centroid&#160;is&#160;not&#160;used  
  
Author:&#160;Charles&#160;Doutriaux,&#160;doutriaux1@llnl.gov  
  
Usage:  
[ generalCriteria ](/) (slab,sliced,slices,arg)  
slab&#160;:&#160;the&#160;original&#160;slab  
mask:&#160;&#160;the&#160;actual&#160;percentage&#160;of&#160;data&#160;in&#160;each&#160;subset&#160;used&#160;to&#160;produce&#160;the&#160;slab  
the&#160;bounds&#160;of&#160;its&#160;first&#160;(time)&#160;dimension&#160;must&#160;be&#160;correct  
they&#160;will&#160;be&#160;used&#160;by&#160;centroid  
spread:&#160;the&#160;begining&#160;and&#160;end&#160;time&#160;of&#160;the&#160;slice&#160;processed  
arg:  
First&#160;represent&#160;the&#160;%&#160;of&#160;value&#160;present&#160;to&#160;retain&#160;a&#160;slice  
Second&#160;represent&#160;the&#160;value&#160;of&#160;the&#160;centroid&#160;(between&#160;0:&#160;perfect&#160;and&#160;1:&#160;bad  
If&#160;you&#160;do&#160;not&#160;want&#160;to&#160;use&#160;one&#160;these&#160;criteria&#160;pass&#160;None  
if&#160;you&#160;would&#160;rather&#160;use&#160;a&#160;cyclicalcnetroid&#160;pass:&#160;"cyclical"&#160;as&#160;an&#160;Xtra
argument `

 getMonthIndex  (my_str) 
     ` Given&#160;a&#160;string&#160;representing&#160;a&#160;month&#160;or&#160;a&#160;season&#160;(common&#160;abrev)   
Returns&#160;the&#160;ordered&#160;indices&#160;of&#160;the&#160;month  
Author:&#160;Krishna&#160;Achutarao  
Date:&#160;April&#160;2001 `

 getMonthString  (my_list) 
     ` Given&#160;a&#160;list&#160;of&#160;month&#160;creates&#160;the&#160;string&#160;representing&#160;the&#160;sequence `

 isMonthly  (s) 
     ` This&#160;function&#160;test&#160;if&#160;the&#160;data&#160;are&#160;monthly&#160;data&#160;from&#160;the&#160;time&#160;axis `

 mergeTime  (ds, statusbar  =1  ) 
     ` Merge&#160;chronologically&#160;a&#160;bunch&#160;of&#160;slab   
Version&#160;1.0  
Author:&#160;Charles&#160;Doutriaux,&#160;doutriaux1@llnl.gov  
Usage:  
mymerged= [ mergeTime ](/) (ds)  
where:  
ds&#160;is&#160;a&#160;list&#160;or&#160;an&#160;array&#160;of&#160;slabs&#160;to&#160;merge,&#160;each&#160;slab&#160;MUST&#160;be&#160;in&#160;chronological
order  
Output:  
a&#160;slab&#160;merging&#160;all&#160;the&#160;slab&#160;of&#160;ds  
order&#160;is&#160;the&#160;order&#160;of&#160;the&#160;first&#160;slab `

 monthBasedSlicer  (tim, arg  =None  ) 
     ` slicer&#160;function&#160;for&#160;the [ TimeSlicer ](/) class   
select&#160;months  
Author&#160;:&#160;Charles&#160;Doutriaux,&#160;doutriaux1@llnl.gov  
Original&#160;Date:&#160;April&#160;2001  
Last&#160;Modified:&#160;October,&#160;2001  
Input:  
-&#160;tim:&#160;time&#160;axis   
-&#160;arg:&#160;character&#160;string&#160;representing&#160;the&#160;desired&#160;month/season&#160;or&#160;integer(s)   
also&#160;you&#160;can&#160;pass&#160;a&#160;list&#160;of&#160;the&#160;months&#160;you&#160;want&#160;(string&#160;or&#160;integer)  
you&#160;can&#160;mix&#160;integer&#160;and&#160;strings  
Output:  
\- `

 setAxisTimeBoundsDaily  (axis, frequency  =1  ) 
     ` Sets&#160;the&#160;bounds&#160;correctly&#160;for&#160;the&#160;time&#160;axis&#160;(beginning&#160;to&#160;end&#160;of&#160;day)   
Usage:  
tim=s.getTime()  
cdutil.times. [ setAxisTimeBoundsMonthly ](/) (tim,frequency=1)  
e.g.&#160;for&#160;twice-daily&#160;data&#160;use&#160;frequency=2  
for&#160;6&#160;hourly&#160;data&#160;use&#160;frequency=4  
for&#160;&#160;&#160;hourly&#160;data&#160;use&#160;frequency=24  
Origin&#160;of&#160;day&#160;is&#160;always&#160;midnight `

 setAxisTimeBoundsMonthly  (axis, stored  =0  ) 
     ` Sets&#160;the&#160;bounds&#160;correctly&#160;for&#160;the&#160;time&#160;axis&#160;(beginning&#160;to&#160;end&#160;of&#160;month)   
Set&#160;stored&#160;to&#160;1&#160;to&#160;indicate&#160;that&#160;your&#160;data&#160;are&#160;stored&#160;at&#160;the&#160;end&#160;of&#160;the&#160;month  
Usage:  
tim=s.getTime()  
cdutil.times. [ setAxisTimeBoundsMonthly ](/) (tim,stored=0) `

 setAxisTimeBoundsYearly  (axis) 
     ` Sets&#160;the&#160;bounds&#160;correctly&#160;for&#160;the&#160;time&#160;axis&#160;(beginning&#160;to&#160;end&#160;of&#160;year)   
Usage:  
tim=s.getTime()  
cdutil.times. [ setAxisTimeBoundsYearly ](/) (tim) `

 setSlabTimeBoundsDaily  (slab, frequency  =1  ) 
     ` Sets&#160;the&#160;bounds&#160;correctly&#160;for&#160;the&#160;time&#160;axis&#160;(beginning&#160;to&#160;end&#160;of&#160;day)   
for&#160;'frequency'-daily&#160;data  
Usage:  
cdutil.times. [ setSlabTimeBoundsDaily ](/) (slab,frequency=1)  
e.g.&#160;for&#160;twice-daily&#160;data&#160;use&#160;frequency=2  
for&#160;6&#160;hourly&#160;data&#160;use&#160;frequency=4  
for&#160;&#160;&#160;hourly&#160;data&#160;use&#160;frequency=24  
Origin&#160;of&#160;day&#160;is&#160;always&#160;midnight `

 setSlabTimeBoundsMonthly  (slab, stored  =0  ) 
     ` Sets&#160;the&#160;bounds&#160;correctly&#160;for&#160;the&#160;time&#160;axis&#160;for&#160;monthly&#160;data&#160;stored   
without&#160;bounds.  
Set&#160;stored&#160;to&#160;1&#160;to&#160;indicate&#160;that&#160;your&#160;data&#160;are&#160;stored&#160;at&#160;the&#160;end&#160;of&#160;the&#160;month  
Usage:  
cdutil.times. [ setSlabTimeBoundsMonthly ](/) (slab,stored=0) `

 setSlabTimeBoundsYearly  (slab) 
     ` Sets&#160;the&#160;bounds&#160;correctly&#160;for&#160;the&#160;time&#160;axis&#160;for&#160;yearly&#160;data   
Usage:  
cdutil.times. [ setSlabTimeBoundsYearly ](/) (slab) `

 setTimeBoundsDaily  (obj, frequency  =1  ) 
     ` Sets&#160;the&#160;bounds&#160;correctly&#160;for&#160;the&#160;time&#160;axis&#160;(beginning&#160;to&#160;end&#160;of&#160;day)   
for&#160;'frequency'-daily&#160;data  
Usage:  
cdutil.times. [ setSlabTimeBoundsDaily ](/) (slab,frequency=1)  
or  
cdutil.times. [ setSlabTimeBoundsDaily ](/) (time_axis,frequency=1)  
e.g.&#160;for&#160;twice-daily&#160;data&#160;use&#160;frequency=2  
for&#160;6&#160;hourly&#160;data&#160;use&#160;frequency=4  
for&#160;&#160;&#160;hourly&#160;data&#160;use&#160;frequency=24  
Origin&#160;of&#160;day&#160;is&#160;always&#160;midnight `

 setTimeBoundsMonthly  (obj, stored  =0  ) 
     ` Sets&#160;the&#160;bounds&#160;correctly&#160;for&#160;the&#160;time&#160;axis&#160;(beginning&#160;to&#160;end&#160;of&#160;month)   
Set&#160;stored&#160;to&#160;1&#160;to&#160;indicate&#160;that&#160;your&#160;data&#160;are&#160;stored&#160;at&#160;the&#160;end&#160;of&#160;the&#160;month  
Usage:  
tim=s.getTime()  
cdutil.times. [ setAxisTimeBoundsMonthly ](/) (s,stored=0)  
or  
cdutil.times. [ setAxisTimeBoundsMonthly ](/) (tim,stored=0) `

 setTimeBoundsYearly  (obj) 
     ` Sets&#160;the&#160;bounds&#160;correctly&#160;for&#160;the&#160;time&#160;axis&#160;for&#160;yearly&#160;data   
Usage:  
cdutil.times. [ setSlabTimeBoundsYearly ](/) (slab)  
or  
cdutil.times. [ setSlabTimeBoundsYearly ](/) (time_axis) `

 switchCalendars  (t1, u1, c1, u2, c2  =None  ) 
     ` converts&#160;a&#160;relative&#160;time&#160;from&#160;one&#160;calendar&#160;to&#160;another,&#160;assuming&#160;that&#160;they&#160;are&#160;in&#160;different&#160;calendar   
Usage:&#160;cvreltime(t1,c1,u2,c2)  
where&#160;t1&#160;is&#160;cdtime&#160;reltime&#160;object&#160;or&#160;a&#160;value&#160;(then&#160;u1&#160;is&#160;needed)  
c1,c2&#160;are&#160;cdtime&#160;calendars  
u1,&#160;u2&#160;the&#160;units&#160;in&#160;the&#160;final&#160;calendar `

 weekday  (a, calendar  =None  ) 

  
 Data 

` `

 ANNUALCYCLE  = <cdutil.times.Seasons instance>   
 APR  = <cdutil.times.Seasons instance>   
 AUG  = <cdutil.times.Seasons instance>   
 DEC  = <cdutil.times.Seasons instance>   
 DJF  = <cdutil.times.Seasons instance>   
 FEB  = <cdutil.times.Seasons instance>   
 JAN  = <cdutil.times.Seasons instance>   
 JJA  = <cdutil.times.Seasons instance>   
 JUL  = <cdutil.times.Seasons instance>   
 JUN  = <cdutil.times.Seasons instance>   
 MAM  = <cdutil.times.Seasons instance>   
 MAR  = <cdutil.times.Seasons instance>   
 MAY  = <cdutil.times.Seasons instance>   
 NOV  = <cdutil.times.Seasons instance>   
 OCT  = <cdutil.times.Seasons instance>   
 SEASONALCYCLE  = <cdutil.times.Seasons instance>   
 SEP  = <cdutil.times.Seasons instance>   
 SON  = <cdutil.times.Seasons instance>   
 YEAR  = <cdutil.times.Seasons instance>

* * *

UCRL-WEB-213937 | [ Privacy & Legal Notice ](/disclaimer.html)

[ webmaster@pcmdi.llnl.gov ](/webmaster@pcmdi.llnl.gov)

[ ![Powered by Plone](media/plone_powered.gif) ](/)

