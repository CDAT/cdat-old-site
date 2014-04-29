---
layout: default
title:
---

 [ Skip to content. ](/cdat/source/api-reference/regrid.horizontal.html) | [
Skip to navigation ](/cdat/source/api-reference/regrid.horizontal.html)

Search Site

[ Advanced Search&#8230; ](/search_form)

#  [ PCMDI Software Portal ](/)

#####  Sections

  * [ Home ](/)

#####  Personal tools

  * [ Log in ](/login_form)

You are here:  [ Home ](/) -> [ CDAT ](/cdat) -> [ Source Code ](/cdat/source)
-> [ API Reference ](/cdat/source/api-reference) -> Python: module
regrid.horizontal

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

        * [ Python: module regrid.horizontal ](/cdat/source/api-reference/regrid.horizontal.html)

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

  * [ ![Send this page to somebody](media/mail_icon.gif) ](/cdat/source/api-reference/regrid.horizontal.html/sendto_form)
  * [ ![Print this page](media/print_icon.gif) ](/this.print\(\))

#  Python: module regrid.horizontal

  
  
 [ regrid  ](/regrid.html) .horizontal 
[ index ](/)  

  
 Modules 

` `

[ MA ](/MA.html)  
[ Numeric ](/Numeric.html)  

[ regrid._regrid ](/regrid._regrid.html)  
[ copy ](/copy.html)  

[ string ](/string.html)  

  
 Classes 

` `

[ Regridder ](/regrid.horizontal.html)

  
class  Regridder 

` `

` #&#160;Create&#160;a&#160;regridder.&#160;ingrid&#160;and&#160;outgrid&#160;are&#160;CDMS&#160;AbstractGrid&#160;objects.  
`

Methods defined here:  

 __call__  (self, ar, missing  =None  , order  =None  , mask  =None  , returnTuple  =0  ) 
     ` #&#160;Call&#160;the&#160;regridder&#160;function.   
#&#160;ar&#160;is&#160;the&#160;input&#160;array.  
#&#160;order&#160;is&#160;of&#160;the&#160;form&#160;"tzyx",&#160;"tyx",&#160;etc.  
#&#160;missing&#160;is&#160;the&#160;missing&#160;data&#160;value,&#160;if&#160;any.  
#&#160;mask&#160;is&#160;either&#160;2-D&#160;or&#160;the&#160;same&#160;shape&#160;as&#160;ar.  
#&#160;If&#160;returnTuple&#160;is&#160;true,&#160;return&#160;the&#160;tuple&#160;(outArray,&#160;outWeights)&#160;where  
#&#160;outWeights&#160;is&#160;the&#160;fraction&#160;of&#160;each&#160;zone&#160;of&#160;the&#160;output&#160;grid&#160;which&#160;overlaps
non-missing  
#&#160;zones&#160;of&#160;the&#160;input&#160;grid;&#160;it&#160;has&#160;the&#160;same&#160;shape&#160;as&#160;the&#160;output&#160;array. `

 __init__  (self, ingrid, outgrid) 

  
 Functions 

` `

 extractBounds  (bounds) 
     ` #&#160;Map&#160;(n,2)&#160;boundary&#160;arrays&#160;to&#160;individual&#160;boundary&#160;arrays.&#160;Returns&#160;(lowerBounds,&#160;upperBounds) `

 input_mask  (ain, type, mask, missing  =None  ) 
     ` #-------------------------------------------------------------------   
#  
#&#160;&#160;&#160;&#160;&#160;purpose:&#160;set&#160;up&#160;the&#160;input&#160;mask&#160;including&#160;missing&#160;from&#160;ain  
#  
#&#160;&#160;&#160;&#160;&#160;usage:  
#  
#&#160;&#160;&#160;&#160;&#160;passed&#160;:  
#  
#&#160;&#160;&#160;&#160;&#160;returned:  
#  
#  
#------------------------------------------------------------------------ `

* * *

UCRL-WEB-213937 | [ Privacy & Legal Notice ](/disclaimer.html)

[ webmaster@pcmdi.llnl.gov ](/webmaster@pcmdi.llnl.gov)

[ ![Powered by Plone](media/plone_powered.gif) ](/)

