---
layout: default
title:
---

 [ Skip to content. ](/cdat/source/api-
reference/vcs.VCS_validation_functions.html) | [ Skip to navigation
](/cdat/source/api-reference/vcs.VCS_validation_functions.html)

Search Site

[ Advanced Search&#8230; ](/search_form)

#  [ PCMDI Software Portal ](/)

#####  Sections

  * [ Home ](/)

#####  Personal tools

  * [ Log in ](/login_form)

You are here:  [ Home ](/) -> [ CDAT ](/cdat) -> [ Source Code ](/cdat/source)
-> [ API Reference ](/cdat/source/api-reference) -> Python: module
vcs.VCS_validation_functions

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

        * [ Python: module vcs.VCS_validation_functions ](/cdat/source/api-reference/vcs.VCS_validation_functions.html)

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

  * [ ![Send this page to somebody](media/mail_icon.gif) ](/cdat/source/api-reference/vcs.VCS_validation_functions.html/sendto_form)
  * [ ![Print this page](media/print_icon.gif) ](/this.print\(\))

#  Python: module vcs.VCS_validation_functions

  
  
 [ vcs  ](/vcs.html) .VCS_validation_functions 
[ index ](/)  

  
 Modules 

` `

[ vcs._vcs ](/vcs._vcs.html)  

[ cdtime ](/cdtime.html)  

[ vcs.queries ](/vcs.queries.html)  

[ vcs ](/vcs.html)  

  
 Classes 

` `

[ exceptions.Exception ](/exceptions.html)

    

[ PPE ](/vcs.VCS_validation_functions.html)

  
class  PPE  ( [ exceptions.Exception ](/exceptions.html) )

` `

Methods defined here:  

 __init__  (self, parameter, type) 

 __str__  (self) 

* * *

Methods inherited from [ exceptions.Exception ](/exceptions.html) :  

 __getitem__  (...) 

  
 Functions 

` `

 DMS2deg  (val) 
     ` converts&#160;DDDMMMSSS&#160;to&#160;degrees `

 checkAxisConvert  (self, name, value) 

 checkBoxfillType  (self, name, value) 

 checkCalendar  (self, name, value) 

 checkColor  (self, name, value) 

 checkColorList  (self, name, value) 

 checkDatawc  (self, name, value) 

 checkExt  (self, name, value) 

 checkFillAreaStyle  (self, name, value) 
     ` ## [ checkName ](/) (self,name,value)   
##&#160;&#160;&#160;&#160;&#160;&#160;if&#160;not&#160;isinstance(value,str):  
##&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;raise&#160;ValueError,'The&#160;fillarea&#160;attribute&#160;must&#160;be&#160;a&#160;string'  
##&#160;&#160;&#160;&#160;&#160;&#160;if&#160;not&#160;value.lower()&#160;in&#160;['solid','hatch','pattern']:  
##&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;raise&#160;ValueError,&#160;'The&#160;fillarea&#160;attribute&#160;must&#160;be&#160;either&#160;solid,
hatch,&#160;or&#160;pattern.'  
##&#160;&#160;&#160;&#160;&#160;&#160;return&#160;value `

 checkInStringsListInt  (self, name, value, values) 
     ` checks&#160;the&#160;line&#160;type `

 checkIndex  (self, name, value) 

 checkIndicesList  (self, name, value) 

 checkInt  (self, name, value, minvalue  =None  , maxvalue  =None  ) 

 checkIntFloat  (self, name, value) 

 checkIsofill  (self, name, value) 

 checkIsoline  (self, name, value) 

 checkIsolineLevels  (self, name, value) 

 checkLegend  (self, name, value) 

 checkLine  (self, name, value) 

 checkLineType  (self, name, value) 

 checkLinesList  (self, name, value) 

 checkListOfNumbers  (self, name, value, minvalue  =None  , maxvalue  =None  , minelements  =None  , maxelements  =None  ) 

 checkListTuple  (self, name, value) 

 checkMarker  (self, name, value) 

 checkName  (self, name, value) 

 checkNumber  (self, name, value, minvalue  =None  , maxvalue  =None  ) 

 checkOnOff  (self, name, value, return_string  =0  ) 

 checkProjParameters  (self, name, value) 

 checkProjType  (self, name, value) 
     ` set&#160;the&#160;projection&#160;type `

 checkProjection  (self, name, value) 

 checkStringDictionary  (self, name, value) 

 checkTextsList  (self, name, value) 

 checkTimeUnits  (self, name, value) 

 checkVectorAlignment  (self, name, value) 

 checkVectorType  (self, name, value) 

 checkWrap  (self, name, value) 

 checkYesNo  (self, name, value) 

 checkname  (self, name, value) 

 deg2DMS  (val) 
     ` converts&#160;degrees&#160;to&#160;DDDMMMSSS.ss&#160;format `

 getProjType  (self) 
     ` get&#160;the&#160;projection&#160;type `

 isListorTuple  (value) 

 isNumber  (value, min  =None  , max  =None  ) 
     ` Checks&#160;if&#160;value&#160;is&#160;a&#160;Number,&#160;optionaly&#160;can&#160;check&#160;if&#160;min<value<max `

 setProjParameter  (self, name, value) 
     ` Set&#160;an&#160;individual&#160;paramater&#160;for&#160;a&#160;projection `

* * *

UCRL-WEB-213937 | [ Privacy & Legal Notice ](/disclaimer.html)

[ webmaster@pcmdi.llnl.gov ](/webmaster@pcmdi.llnl.gov)

[ ![Powered by Plone](media/plone_powered.gif) ](/)

