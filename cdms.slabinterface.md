---
layout: default
title:
---

 [ Skip to content. ](/cdat/source/api-reference/cdms.slabinterface.html) | [
Skip to navigation ](/cdat/source/api-reference/cdms.slabinterface.html)

Search Site

[ Advanced Search&#8230; ](/search_form)

#  [ PCMDI Software Portal ](/)

#####  Sections

  * [ Home ](/)

#####  Personal tools

  * [ Log in ](/login_form)

You are here:  [ Home ](/) -> [ CDAT ](/cdat) -> [ Source Code ](/cdat/source)
-> [ API Reference ](/cdat/source/api-reference) -> Python: module
cdms.slabinterface

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

        * [ Python: module cdms.slabinterface ](/cdat/source/api-reference/cdms.slabinterface.html)

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

  * [ ![Send this page to somebody](media/mail_icon.gif) ](/cdat/source/api-reference/cdms.slabinterface.html/sendto_form)
  * [ ![Print this page](media/print_icon.gif) ](/this.print\(\))

#  Python: module cdms.slabinterface

  
  
 [ cdms  ](/cdms.html) .slabinterface 
[ index ](/)  

` Read&#160;part&#160;of&#160;the&#160;old&#160;cu&#160;slab&#160;interface&#160;implemented&#160;over&#160;CDMS `

  
 Modules 

` `

[ MA ](/MA.html)  
[ Numeric ](/Numeric.html)  

[ cdms ](/cdms.html)  
[ string ](/string.html)  

[ sys ](/sys.html)  
[ types ](/types.html)  

  
 Classes 

` `

[ Slab ](/cdms.slabinterface.html)

  
class  Slab 

` `

` [ Slab ](/) is&#160;the&#160;cu&#160;api  
This&#160;is&#160;an&#160;abstract&#160;class&#160;to&#160;inherit&#160;in&#160;AbstractVariable  
About&#160;axes:  
weight&#160;and&#160;bounds&#160;attributes&#160;always&#160;set&#160;but&#160;may&#160;be&#160;None  
if&#160;bounds&#160;are&#160;None,&#160;getdimattribute&#160;returns&#160;result&#160;of&#160;querying&#160;the  
axis.  
`

Methods defined here:  

 __init__  (self) 

 createattribute  (self, name, value) 
     ` Create&#160;an&#160;attribute&#160;and&#160;set&#160;its&#160;name&#160;to&#160;value. `

 deleteattribute  (self, name) 
     ` Delete&#160;the&#160;named&#160;attribute. `

 getattribute  (self, name) 
     ` Get&#160;the&#160;attribute&#160;name. `

 getdimattribute  (self, dim, field) 
     ` Get&#160;the&#160;attribute&#160;named&#160;field&#160;from&#160;the&#160;dim'th&#160;dimension.   
For&#160;bounds&#160;returns&#160;the&#160;old&#160;cu&#160;one-dimensional&#160;version. `

 info  (self, flag  =None  , device  =None  ) 
     ` Write&#160;info&#160;about&#160;slab;&#160;include&#160;dimension&#160;values&#160;and&#160;weights&#160;if&#160;flag `

 listall  (self, all  =None  ) 
     ` Get&#160;list&#160;of&#160;info&#160;about&#160;this&#160;slab. `

 listattributes  (self) 
     ` Return&#160;a&#160;list&#160;of&#160;attribute&#160;names. `

 listdimattributes  (self, dim) 
     ` List&#160;the&#160;legal&#160;axis&#160;field&#160;names. `

 listdimnames  (self) 
     ` Return&#160;a&#160;list&#160;of&#160;the&#160;names&#160;of&#160;the&#160;dimensions. `

 setattribute  (self, name, value) 
     ` Set&#160;the&#160;attribute&#160;name&#160;to&#160;value. `

 showdim  (self) 
     ` Show&#160;the&#160;dimension&#160;attributes&#160;and&#160;values. `

* * *

Data and other attributes defined here:  

 std_slab_atts  = ['filename', 'missing_value', 'comments', 'grid_name', 'grid_type', 'time_statistic', 'long_name', 'units'] 

  
 Functions 

` `

 cdms_bounds2cu_bounds  (b) 
     ` Bounds&#160;are&#160;&#160;len(v)&#160;by&#160;2&#160;in&#160;cdms&#160;but&#160;len(v)+1&#160;in&#160;cu `

  
 Data 

` `

 std_axis_attributes  = ['name', 'units', 'length', 'values', 'bounds'] 

* * *

UCRL-WEB-213937 | [ Privacy & Legal Notice ](/disclaimer.html)

[ webmaster@pcmdi.llnl.gov ](/webmaster@pcmdi.llnl.gov)

[ ![Powered by Plone](media/plone_powered.gif) ](/)

