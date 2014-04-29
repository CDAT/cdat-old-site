---
layout: default
title:
---

 [ Skip to content. ](/cdat/source/api-reference/vcs.utils.html) | [ Skip to
navigation ](/cdat/source/api-reference/vcs.utils.html)

Search Site

[ Advanced Search&#8230; ](/search_form)

#  [ PCMDI Software Portal ](/)

#####  Sections

  * [ Home ](/)

#####  Personal tools

  * [ Log in ](/login_form)

You are here:  [ Home ](/) -> [ CDAT ](/cdat) -> [ Source Code ](/cdat/source)
-> [ API Reference ](/cdat/source/api-reference) -> Python: module vcs.utils

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

        * [ Python: module vcs.utils ](/cdat/source/api-reference/vcs.utils.html)

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

  * [ ![Send this page to somebody](media/mail_icon.gif) ](/cdat/source/api-reference/vcs.utils.html/sendto_form)
  * [ ![Print this page](media/print_icon.gif) ](/this.print\(\))

#  Python: module vcs.utils

  
  
 [ vcs  ](/vcs.html) .utils 
[ index ](/)  

  
 Modules 

` `

[ cdtime ](/cdtime.html)  

  
 Classes 

` `

[ exceptions.Exception ](/exceptions.html)

    

[ VCSUtilsError ](/vcs.utils.html)

  
class  VCSUtilsError  ( [ exceptions.Exception ](/exceptions.html) )

` `

Methods defined here:  

 __init__  (self, args  =None  ) 
     ` Create&#160;an&#160;exception `

 __repr__  = [ __str__ ](/) (self) 

 __str__  (self) 
     ` Calculate&#160;the&#160;string&#160;representation `

* * *

Methods inherited from [ exceptions.Exception ](/exceptions.html) :  

 __getitem__  (...) 

  
 Functions 

` `

 generate_time_labels  (d1, d2, units, calendar  =135441  ) 
     ` [ generate_time_labels ](/) (self,d1,d2,units,calendar=cdtime.DefaultCalendar)   
returns&#160;a&#160;dictionary&#160;of&#160;time&#160;labels&#160;for&#160;an&#160;interval&#160;of&#160;time,&#160;in&#160;a&#160;user&#160;defined
units&#160;system  
d1&#160;and&#160;d2&#160;must&#160;be&#160;cdtime&#160;object,&#160;if&#160;not&#160;they&#160;will&#160;be&#160;assumed&#160;to&#160;be&#160;in&#160;"units"  
  
Example:  
lbls&#160;= [ generate_time_labels ](/) (cdtime.reltime(0,'months&#160;since&#160;2000'),  
cdtime.reltime(12,'months&#160;since&#160;2000'),  
'days&#160;since&#160;1800',  
)  
This&#160;generated&#160;a&#160;dictionary&#160;of&#160;nice&#160;time&#160;labels&#160;for&#160;the&#160;year&#160;2000&#160;in&#160;units&#160;of
'days&#160;since&#160;1800'  
  
lbls&#160;= [ generate_time_labels ](/) (cdtime.reltime(0,'months&#160;since&#160;2000'),  
cdtime.comptime(2001),  
'days&#160;since&#160;1800',  
)  
This&#160;generated&#160;a&#160;dictionary&#160;of&#160;nice&#160;time&#160;labels&#160;for&#160;the&#160;year&#160;2000&#160;in&#160;units&#160;of
'days&#160;since&#160;1800'  
  
lbls&#160;= [ generate_time_labels ](/) (0,  
12,  
'months&#160;since&#160;2000',  
)  
This&#160;generated&#160;a&#160;dictionary&#160;of&#160;nice&#160;time&#160;labels&#160;for&#160;the&#160;year&#160;2000&#160;in&#160;units&#160;of
'months&#160;since&#160;2000' `

 getcolors  (levs, colors  =[16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, ...]  , split  =1  , white  =240  ) 
     ` Function&#160;: [ getcolors ](/) (levs,colors=range(16,240),split=1,white=240)   
  
Description&#160;of&#160;Function:  
For&#160;isofill/boxfill&#160;purposes  
Given&#160;a&#160;list&#160;of&#160;levels&#160;this&#160;function&#160;returns&#160;the&#160;colors&#160;that&#160;would&#160;best&#160;spread
a&#160;list&#160;of&#160;"user-defined"&#160;colors&#160;(default&#160;is&#160;16&#160;to&#160;239&#160;,&#160;i.e&#160;224&#160;colors),
always&#160;using&#160;the&#160;first&#160;and&#160;last&#160;color.&#160;Optionally&#160;the&#160;color&#160;range&#160;can&#160;be&#160;split
into&#160;2&#160;equal&#160;domain&#160;to&#160;represent&#160;<0&#160;and&#160;>0&#160;values.  
If&#160;the&#160;colors&#160;are&#160;split&#160;an&#160;interval&#160;goes&#160;from&#160;<0&#160;to&#160;>0&#160;then&#160;this&#160;is&#160;assigned
the&#160;"white"&#160;color  
Usage:  
levs&#160;:&#160;levels&#160;defining&#160;the&#160;color&#160;ranges  
colors&#160;(default=&#160;range(16,240)&#160;)&#160;:&#160;A&#160;list/tuple&#160;of&#160;the&#160;of&#160;colors&#160;you&#160;wish&#160;to
use  
split&#160;#&#160;parameter&#160;to&#160;split&#160;the&#160;colors&#160;between&#160;2&#160;equal&#160;domain:  
one&#160;for&#160;positive&#160;values&#160;and&#160;one&#160;for&#160;&#160;negative&#160;values  
0&#160;:&#160;no&#160;split  
1&#160;:&#160;split&#160;if&#160;the&#160;levels&#160;go&#160;from&#160;<0&#160;to&#160;>0  
2&#160;:&#160;split&#160;even&#160;if&#160;all&#160;the&#160;values&#160;are&#160;positive&#160;or&#160;negative  
white&#160;(=240)&#160;#&#160;If&#160;split&#160;is&#160;on&#160;and&#160;an&#160;interval&#160;goes&#160;from&#160;<0&#160;to&#160;>0&#160;this&#160;color
number&#160;will&#160;be&#160;used&#160;within&#160;this&#160;interval&#160;(240&#160;is&#160;white&#160;in&#160;the&#160;default&#160;VCS
palette&#160;color)  
  
Examples&#160;of&#160;Use:  
>>>&#160;a=[0.0,&#160;2.0,&#160;4.0,&#160;6.0,&#160;8.0,&#160;10.0,&#160;12.0,&#160;14.0,&#160;16.0,&#160;18.0,&#160;20.0]  
>>>&#160;vcs.getcolors&#160;(a)  
[16,&#160;41,&#160;66,&#160;90,&#160;115,&#160;140,&#160;165,&#160;189,&#160;214,&#160;239]  
>>>&#160;vcs.getcolors&#160;(a,colors=range(16,200))  
[16,&#160;36,&#160;57,&#160;77,&#160;97,&#160;118,&#160;138,&#160;158,&#160;179,&#160;199]  
>>>&#160;vcs. [ getcolors ](/) (a,colors=[16,25,15,56,35,234,12,11,19,32,132,17])  
[16,&#160;25,&#160;15,&#160;35,&#160;234,&#160;12,&#160;11,&#160;32,&#160;132,&#160;17]  
>>>&#160;a=[-6.0,&#160;-2.0,&#160;2.0,&#160;6.0,&#160;10.0,&#160;14.0,&#160;18.0,&#160;22.0,&#160;26.0]  
>>>&#160;vcs.getcolors&#160;(a,white=241)  
[72,&#160;241,&#160;128,&#160;150,&#160;172,&#160;195,&#160;217,&#160;239]  
>>>&#160;vcs.getcolors&#160;(a,white=241,split=0)  
[16,&#160;48,&#160;80,&#160;112,&#160;143,&#160;175,&#160;207,&#160;239] `

 minmax  (*data) 
     ` Function&#160;:&#160;minmax   
Description&#160;of&#160;Function  
Return&#160;the&#160;minimum&#160;and&#160;maximum&#160;of&#160;a&#160;serie&#160;of&#160;array/list/tuples&#160;(or&#160;combination
of&#160;these)  
Values&#160;those&#160;absolute&#160;value&#160;are&#160;greater&#160;than&#160;1.E20,&#160;are&#160;masked  
You&#160;can&#160;combined&#160;list/tuples/...&#160;pretty&#160;much&#160;any&#160;combination&#160;is&#160;allowed  
  
Examples&#160;of&#160;Use  
>>>&#160;s=range(7)  
>>>&#160;vcs. [ minmax ](/) (s)  
(0.0,&#160;6.0)  
>>>&#160;vcs. [ minmax ](/) ([s,s])  
(0.0,&#160;6.0)  
>>>&#160;vcs. [ minmax ](/) ([[s,s*2],4.,[6.,7.,s]],[5.,-7.,8,(6.,1.)])  
(-7.0,&#160;8.0) `

 mkevenlevels  (n1, n2, nlev  =10  ) 
     ` Function&#160;:&#160;mkevenlevels   
  
Description&#160;of&#160;Function:  
Return&#160;a&#160;serie&#160;of&#160;evenly&#160;spaced&#160;levels&#160;going&#160;from&#160;n1&#160;to&#160;n2  
by&#160;default&#160;10&#160;intervals&#160;will&#160;be&#160;produced  
  
Examples&#160;of&#160;use:  
>>>&#160;vcs. [ mkevenlevels ](/) (0,100)  
[0.0,&#160;10.0,&#160;20.0,&#160;30.0,&#160;40.0,&#160;50.0,&#160;60.0,&#160;70.0,&#160;80.0,&#160;90.0,&#160;100.0]  
>>>&#160;vcs. [ mkevenlevels ](/) (0,100,nlev=5)  
[0.0,&#160;20.0,&#160;40.0,&#160;60.0,&#160;80.0,&#160;100.0]  
>>>&#160;vcs. [ mkevenlevels ](/) (100,0,nlev=5)  
[100.0,&#160;80.0,&#160;60.0,&#160;40.0,&#160;20.0,&#160;0.0] `

 mklabels  (vals, output  ='dict'  ) 
     ` Function&#160;:&#160;mklabels   
  
Description&#160;of&#160;Function:  
This&#160;function&#160;gets&#160;levels&#160;and&#160;output&#160;strings&#160;for&#160;nice&#160;display&#160;of&#160;the&#160;levels
values,&#160;returns&#160;a&#160;dictionary&#160;unless&#160;output="list"&#160;specified  
  
Examples&#160;of&#160;use:  
>>>&#160;a=vcs. [ mkscale ](/) (2,20,zero=2)  
>>>&#160;vcs.mklabels&#160;(a)  
{20.0:&#160;'20',&#160;18.0:&#160;'18',&#160;16.0:&#160;'16',&#160;14.0:&#160;'14',&#160;12.0:&#160;'12',&#160;10.0:&#160;'10',&#160;8.0:
'8',&#160;6.0:&#160;'6',&#160;4.0:&#160;'4',&#160;2.0:&#160;'2',&#160;0.0:&#160;'0'}  
>>>&#160;vcs.mklabels&#160;(&#160;[5,.005])  
{0.0050000000000000001:&#160;'0.005',&#160;5.0:&#160;'5.000'}  
>>>&#160;vcs.mklabels&#160;(&#160;[.00002,.00005])  
{2.0000000000000002e-05:&#160;'2E-5',&#160;5.0000000000000002e-05:&#160;'5E-5'}  
>>>&#160;vcs.mklabels&#160;(&#160;[.00002,.00005],output='list')  
['2E-5',&#160;'5E-5'] `

 mkscale  (n1, n2, nc  =12  , zero  =1  ) 
     ` Function:&#160;mkscale   
  
Description&#160;of&#160;function:  
This&#160;function&#160;return&#160;a&#160;nice&#160;scale&#160;given&#160;a&#160;min&#160;and&#160;a&#160;max  
  
option:  
nc&#160;#&#160;Maximum&#160;number&#160;of&#160;intervals&#160;(default=12)  
zero&#160;#&#160;Not&#160;all&#160;implemented&#160;yet&#160;so&#160;set&#160;to&#160;1&#160;but&#160;values&#160;will&#160;be:  
-1:&#160;zero&#160;MUST&#160;NOT&#160;be&#160;a&#160;contour   
0:&#160;let&#160;the&#160;function&#160;decide&#160;#&#160;NOT&#160;IMPLEMENTED  
1:&#160;zero&#160;CAN&#160;be&#160;a&#160;contour&#160;&#160;(default)  
2:&#160;zero&#160;MUST&#160;be&#160;a&#160;contour  
Examples&#160;of&#160;Use:  
>>>&#160;vcs. [ mkscale ](/) (0,100)  
[0.0,&#160;10.0,&#160;20.0,&#160;30.0,&#160;40.0,&#160;50.0,&#160;60.0,&#160;70.0,&#160;80.0,&#160;90.0,&#160;100.0]  
>>>&#160;vcs. [ mkscale ](/) (0,100,nc=5)  
[0.0,&#160;20.0,&#160;40.0,&#160;60.0,&#160;80.0,&#160;100.0]  
>>>&#160;vcs. [ mkscale ](/) (-10,100,nc=5)  
[-25.0,&#160;0.0,&#160;25.0,&#160;50.0,&#160;75.0,&#160;100.0]  
>>>&#160;vcs. [ mkscale ](/) (-10,100,nc=5,zero=-1)  
[-20.0,&#160;20.0,&#160;60.0,&#160;100.0]  
>>>&#160;vcs. [ mkscale ](/) (2,20)  
[2.0,&#160;4.0,&#160;6.0,&#160;8.0,&#160;10.0,&#160;12.0,&#160;14.0,&#160;16.0,&#160;18.0,&#160;20.0]  
>>>&#160;vcs. [ mkscale ](/) (2,20,zero=2)  
[0.0,&#160;2.0,&#160;4.0,&#160;6.0,&#160;8.0,&#160;10.0,&#160;12.0,&#160;14.0,&#160;16.0,&#160;18.0,&#160;20.0] `

* * *

UCRL-WEB-213937 | [ Privacy & Legal Notice ](/disclaimer.html)

[ webmaster@pcmdi.llnl.gov ](/webmaster@pcmdi.llnl.gov)

[ ![Powered by Plone](media/plone_powered.gif) ](/)

