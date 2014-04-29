---
layout: default
title:
---

 [ Skip to content. ](/cdat/source/api-reference/cdms.bindex.html) | [ Skip to
navigation ](/cdat/source/api-reference/cdms.bindex.html)

Search Site

[ Advanced Search&#8230; ](/search_form)

#  [ PCMDI Software Portal ](/)

#####  Sections

  * [ Home ](/)

#####  Personal tools

  * [ Log in ](/login_form)

You are here:  [ Home ](/) -> [ CDAT ](/cdat) -> [ Source Code ](/cdat/source)
-> [ API Reference ](/cdat/source/api-reference) -> Python: module cdms.bindex

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

        * [ Python: module cdms.bindex ](/cdat/source/api-reference/cdms.bindex.html)

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

  * [ ![Send this page to somebody](media/mail_icon.gif) ](/cdat/source/api-reference/cdms.bindex.html/sendto_form)
  * [ ![Print this page](media/print_icon.gif) ](/this.print\(\))

#  Python: module cdms.bindex

  
  
 [ cdms  ](/cdms.html) .bindex 
[ index ](/)  

` Bin&#160;index&#160;for&#160;non-rectilinear&#160;grids `

  
 Modules 

` `

[ Numeric ](/Numeric.html)  

[ cdms._bindex ](/cdms._bindex.html)  

  
 Functions 

` `

 bindexHorizontalGrid  (latlin, lonlin) 
     ` Create&#160;a&#160;bin&#160;index&#160;for&#160;a&#160;horizontal&#160;grid.   
'latlin'&#160;is&#160;the&#160;raveled&#160;latitude&#160;values.  
'lonlin'&#160;is&#160;the&#160;raveled&#160;longitude&#160;values.  
  
Returns&#160;the&#160;index. `

 intersectHorizontalGrid  (latspecs, lonspecs, latlin, lonlin, index) 
     ` Intersect&#160;a&#160;horizontal&#160;grid&#160;with&#160;a&#160;lat-lon&#160;region.   
  
'latspecs'&#160;and&#160;'lonspecs'&#160;are&#160;the&#160;latitude/longitude&#160;specs  
as&#160;defined&#160;in&#160;the&#160;grid&#160;module.  
'latlin'&#160;and&#160;'lonlin'&#160;are&#160;the&#160;raveled&#160;latitude/longitude&#160;arrays.  
'index'&#160;is&#160;the&#160;bin&#160;index&#160;as&#160;returned&#160;from&#160;bindex.  
  
Returns&#160;an&#160;array&#160;of&#160;indices,&#160;in&#160;latlin/lonlin,&#160;of&#160;the&#160;points&#160;in  
the&#160;intersection. `

* * *

UCRL-WEB-213937 | [ Privacy & Legal Notice ](/disclaimer.html)

[ webmaster@pcmdi.llnl.gov ](/webmaster@pcmdi.llnl.gov)

[ ![Powered by Plone](media/plone_powered.gif) ](/)

