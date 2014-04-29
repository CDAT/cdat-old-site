---
layout: default
title:
---

 [ Skip to content. ](/cdat/source/api-reference/cdutil.region.html) | [ Skip
to navigation ](/cdat/source/api-reference/cdutil.region.html)

Search Site

[ Advanced Search&#8230; ](/search_form)

#  [ PCMDI Software Portal ](/)

#####  Sections

  * [ Home ](/)

#####  Personal tools

  * [ Log in ](/login_form)

You are here:  [ Home ](/) -> [ CDAT ](/cdat) -> [ Source Code ](/cdat/source)
-> [ API Reference ](/cdat/source/api-reference) -> Python: module
cdutil.region

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

        * [ Python: module cdutil.region ](/cdat/source/api-reference/cdutil.region.html)

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

  * [ ![Send this page to somebody](media/mail_icon.gif) ](/cdat/source/api-reference/cdutil.region.html/sendto_form)
  * [ ![Print this page](media/print_icon.gif) ](/this.print\(\))

#  Python: module cdutil.region

  
  
 [ cdutil  ](/cdutil.html) .region 
[ index ](/)  

  
 Classes 

` `

[ cdms.selectors.SelectorComponent ](/cdms.selectors.html)

    

[ DomainComponent ](/cdutil.region.html)

  
class  DomainComponent  ( [ cdms.selectors.SelectorComponent
](/cdms.selectors.html) )

` `

` gets&#160;a&#160;domain,&#160;and&#160;by&#160;default&#160;adjusts&#160;the&#160;bounds&#160;to&#160;the&#160;domain  
or&#160;if&#160;exact&#160;is&#160;set&#160;to&#160;0&#160;or&#160;None&#160;gets&#160;all&#160;the&#160;domain&#160;that&#160;has  
parts&#160;of&#160;the&#160;domain&#160;requested,&#160;also&#160;post&#160;processing&#160;allows&#160;you&#160;to&#160;apply&#160;a&#160;mask  
dimension&#160;names&#160;can&#160;be&#160;passed&#160;as&#160;keywords,  
but&#160;if&#160;no&#160;name&#160;is&#160;passed&#160;arguments&#160;are&#160;taken&#160;in&#160;order&#160;and&#160;applied&#160;to&#160;the
corresponding&#160;axis  
Overwritting&#160;an&#160;axis&#160;(2&#160;keywords&#160;or&#160;keyword&#160;+&#160;argument)&#160;is&#160;not&#160;allowed  
Example&#160;of&#160;use:  
NH=cdms.selectors.Selector( [ domain ](/) (latitude=(0.,90.)))  
`

Methods defined here:  

 __init__  (self, *args, kargs) 
     ` initialise&#160;some&#160;value&#160;such&#160;as&#160;tolerances&#160;for&#160;equality `

 __str__  (self) 

 post  (self, fetched, slab, axes, specifications, confined_by, aux, axismap) 
     ` Post&#160;processing&#160;retouches&#160;the&#160;bounds&#160;and&#160;later&#160;will&#160;deal&#160;with&#160;the&#160;mask `

 same  (self, data, value) 
     ` Check&#160;if&#160;data&#160;is&#160;basically&#160;the&#160;same&#160;than&#160;value `

 specify  (self, slab, axes, specification, confined_by, aux) 
     ` First&#160;part:&#160;confine&#160;the&#160;slab&#160;within&#160;a&#160;Domain&#160;wide&#160;enough&#160;to&#160;do&#160;the&#160;exact&#160;in&#160;post `

* * *

Methods inherited from [ cdms.selectors.SelectorComponent
](/cdms.selectors.html) :  

 specifyGrid  (self, var, grid, specs) 
     ` Refine&#160;the&#160;specification&#160;suitable&#160;for&#160;grid.intersect().   
  
'var'&#160;is&#160;a&#160;variable.  
'grid'&#160;is&#160;the&#160;grid&#160;associated&#160;with&#160;the&#160;variable.  
'specs'&#160;is&#160;the&#160;result&#160;set&#160;of&#160;specifications,&#160;of&#160;the&#160;form&#160;defined&#160;in&#160;the&#160;grid
module.  
  
Return:  
0&#160;if&#160;self&#160;confines&#160;the&#160;grid.  
1&#160;if&#160;self&#160;is&#160;not&#160;associated&#160;with&#160;coordinate&#160;regions,&#160;or&#160;does&#160;not&#160;confine&#160;the
grid.  
  
Note:&#160;This&#160;function&#160;should&#160;return&#160;0&#160;only&#160;if&#160;self&#160;is&#160;a&#160;component&#160;that&#160;confines  
nonrectilinear&#160;grids.&#160;See&#160;class&#160;coordinateComponent. `

  
 Functions 

` `

 domain  (*args, kargs) 
     ` construct&#160;the&#160;selector `

  
 Data 

` `

 AAZ  = Selector(<cdutil.region.DomainComponent instance at 0x402a810c>)   
 AZ  = Selector(<cdutil.region.DomainComponent instance at 0x402a834c>)   
 AntarcticZone  = Selector(<cdutil.region.DomainComponent instance at 0x402a810c>)   
 ArcticZone  = Selector(<cdutil.region.DomainComponent instance at 0x402a834c>)   
 NH  = Selector(<cdutil.region.DomainComponent instance at 0x402a6a4c>)   
 NPZ  = Selector(<cdutil.region.DomainComponent instance at 0x402a834c>)   
 NorthernHemisphere  = Selector(<cdutil.region.DomainComponent instance at 0x402a6a4c>)   
 SH  = Selector(<cdutil.region.DomainComponent instance at 0x402a6c8c>)   
 SPZ  = Selector(<cdutil.region.DomainComponent instance at 0x402a810c>)   
 SouthernHemisphere  = Selector(<cdutil.region.DomainComponent instance at 0x402a6c8c>)   
 Tropics  = Selector(<cdutil.region.DomainComponent instance at 0x402a822c>) 

* * *

UCRL-WEB-213937 | [ Privacy & Legal Notice ](/disclaimer.html)

[ webmaster@pcmdi.llnl.gov ](/webmaster@pcmdi.llnl.gov)

[ ![Powered by Plone](media/plone_powered.gif) ](/)

