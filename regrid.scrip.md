---
layout: default
title:
---

 [ Skip to content. ](/cdat/source/api-reference/regrid.scrip.html) | [ Skip to
navigation ](/cdat/source/api-reference/regrid.scrip.html)

Search Site

[ Advanced Search&#8230; ](/search_form)

#  [ PCMDI Software Portal ](/)

#####  Sections

  * [ Home ](/)

#####  Personal tools

  * [ Log in ](/login_form)

You are here:  [ Home ](/) -> [ CDAT ](/cdat) -> [ Source Code ](/cdat/source)
-> [ API Reference ](/cdat/source/api-reference) -> Python: module
regrid.scrip

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

        * [ Python: module regrid.scrip ](/cdat/source/api-reference/regrid.scrip.html)

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

  * [ ![Send this page to somebody](media/mail_icon.gif) ](/cdat/source/api-reference/regrid.scrip.html/sendto_form)
  * [ ![Print this page](media/print_icon.gif) ](/this.print\(\))

#  Python: module regrid.scrip

  
  
 [ regrid  ](/regrid.html) .scrip 
[ index ](/)  

  
 Modules 

` `

[ regrid._scrip ](/regrid._scrip.html)  

  
 Classes 

` `

[ ScripRegridder ](/regrid.scrip.html)

    

[ BicubicRegridder ](/regrid.scrip.html)

[ BilinearRegridder ](/regrid.scrip.html)

[ ConservativeRegridder ](/regrid.scrip.html)

[ DistwgtRegridder ](/regrid.scrip.html)

  
class  BicubicRegridder  ( [ ScripRegridder ](/regrid.scrip.html) )

` `

` Bicubic&#160;regrid.  
`

Methods defined here:  

 __call__  (self, input, gradLat, gradLon, gradLatlon) 
     ` gradLat&#160;=&#160;df/di   
gradLon&#160;=&#160;df/dj  
gradLatlon&#160;=&#160;d(df)/(di)(dj) `

 __init__  (self, outputGrid, remapMatrix, sourceAddress, destAddress, inputGrid  =None  , sourceFrac  =None  , destFrac  =None  ) 

* * *

Methods inherited from [ ScripRegridder ](/regrid.scrip.html) :  

 getDestinationFraction  (self) 

 getInputGrid  (self) 

 getOutputGrid  (self) 

 getSourceFraction  (self) 

  
class  BilinearRegridder  ( [ ScripRegridder ](/regrid.scrip.html) )

` `

Methods defined here:  

 __init__  (self, outputGrid, remapMatrix, sourceAddress, destAddress, inputGrid  =None  , sourceFrac  =None  , destFrac  =None  ) 

 regrid  (self, input) 

* * *

Methods inherited from [ ScripRegridder ](/regrid.scrip.html) :  

 __call__  (self, input) 

 getDestinationFraction  (self) 

 getInputGrid  (self) 

 getOutputGrid  (self) 

 getSourceFraction  (self) 

  
class  ConservativeRegridder  ( [ ScripRegridder ](/regrid.scrip.html) )

` `

` First-order&#160;conservative&#160;regrid.&#160;By&#160;default,&#160;the&#160;normalize&#160;option
="fracarea",&#160;and&#160;array&#160;'normal'  
is&#160;not&#160;specified.&#160;If&#160;'normal'&#160;is&#160;specified,&#160;it&#160;should&#160;be&#160;a&#160;one-dimensional
array&#160;of&#160;the&#160;same&#160;length  
as&#160;the&#160;output&#160;grid&#160;size,&#160;with&#160;values:  
1.0&#160;for&#160;normalize="fracarea",  
grid_frac&#160;for&#160;normalize="destarea",&#160;or  
grid_frac*grid_area&#160;for&#160;normalize="none".  
sourceArea&#160;is&#160;the&#160;area&#160;of&#160;the&#160;source&#160;grid&#160;cells  
destArea&#160;is&#160;the&#160;area&#160;of&#160;the&#160;destination&#160;grid&#160;cells  
`

Methods defined here:  

 __init__  (self, outputGrid, remapMatrix, sourceAddress, destAddress, inputGrid  =None  , sourceFrac  =None  , destFrac  =None  , normalize  ='fracarea'  , normal  =None  , sourceArea  =None  , destArea  =None  ) 

 getDestinationArea  (self) 

 getSourceArea  (self) 

 regrid  (self, input) 

* * *

Methods inherited from [ ScripRegridder ](/regrid.scrip.html) :  

 __call__  (self, input) 

 getDestinationFraction  (self) 

 getInputGrid  (self) 

 getOutputGrid  (self) 

 getSourceFraction  (self) 

  
class  DistwgtRegridder  ( [ ScripRegridder ](/regrid.scrip.html) )

` `

Methods defined here:  

 __init__  (self, outputGrid, remapMatrix, sourceAddress, destAddress, inputGrid  =None  , sourceFrac  =None  , destFrac  =None  ) 

 regrid  (self, input) 

* * *

Methods inherited from [ ScripRegridder ](/regrid.scrip.html) :  

 __call__  (self, input) 

 getDestinationFraction  (self) 

 getInputGrid  (self) 

 getOutputGrid  (self) 

 getSourceFraction  (self) 

  
class  ScripRegridder 

` `

Methods defined here:  

 __call__  (self, input) 

 __init__  (self, outputGrid, remapMatrix, sourceAddress, destAddress, inputGrid  =None  , sourceFrac  =None  , destFrac  =None  ) 

 getDestinationFraction  (self) 

 getInputGrid  (self) 

 getOutputGrid  (self) 

 getSourceFraction  (self) 

  
 Functions 

` `

 readRegridder  (fileobj, mapMethod  =None  , checkGrid  =1  ) 
     ` Read&#160;a&#160;regridder&#160;from&#160;an&#160;open&#160;fileobj.   
mapMethod&#160;is&#160;one&#160;of&#160;"conservative",&#160;"bilinear",&#160;"bicubic",&#160;or&#160;"distwgt".&#160;If
unspecified,&#160;it&#160;defaults&#160;to&#160;the&#160;method&#160;defined&#160;in&#160;the&#160;file.  
If&#160;'checkGrid'&#160;is&#160;1&#160;(default),&#160;the&#160;grid&#160;cells&#160;are&#160;checked&#160;for&#160;convexity,  
and&#160;'repaired'&#160;if&#160;necessary. `

* * *

UCRL-WEB-213937 | [ Privacy & Legal Notice ](/disclaimer.html)

[ webmaster@pcmdi.llnl.gov ](/webmaster@pcmdi.llnl.gov)

[ ![Powered by Plone](media/plone_powered.gif) ](/)

