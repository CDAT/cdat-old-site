---
layout: default
title:
---

 [ Skip to content. ](/cdat/source/api-reference/esg.esgMap.html) | [ Skip to
navigation ](/cdat/source/api-reference/esg.esgMap.html)

Search Site

[ Advanced Search&#8230; ](/search_form)

#  [ PCMDI Software Portal ](/)

#####  Sections

  * [ Home ](/)

#####  Personal tools

  * [ Log in ](/login_form)

You are here:  [ Home ](/) -> [ CDAT ](/cdat) -> [ Source Code ](/cdat/source)
-> [ API Reference ](/cdat/source/api-reference) -> Python: module esg.esgMap

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

        * [ Python: module esg.esgMap ](/cdat/source/api-reference/esg.esgMap.html)

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

  * [ ![Send this page to somebody](media/mail_icon.gif) ](/cdat/source/api-reference/esg.esgMap.html/sendto_form)
  * [ ![Print this page](media/print_icon.gif) ](/this.print\(\))

#  Python: module esg.esgMap

  
  
 [ esg  ](/esg.html) .esgMap 
[ index ](/)  

` Mapping&#160;between&#160;ESG,&#160;CDMS,&#160;and&#160;other&#160;schemas. `

  
 Modules 

` `

[ cdms ](/cdms.html)  

[ cdtime ](/cdtime.html)  

[ esg.esg ](/esg.esg.html)  

[ os ](/os.html)  

  
 Functions 

` `

 toEsg  (cddataset, id, paramlistParent, generatedBy, ofType  =None  , isPartOf  =None  , convention  =None  , timeCoverage  =None  , spaceCoverage  =None  , format  =None  , calendar  =None  , taxis  =None  , xaxis  =None  , yaxis  =None  , zaxis  =None  , fileMapper  =None  , mapperArg  =None  ) 
     ` Translate&#160;a&#160;cdms.cdmsNode.DatasetNode&#160;into&#160;an&#160;ESG&#160;Metadata&#160;node.&#160;The&#160;result&#160;node   
contains&#160;a&#160;dataset,&#160;parameterlist,&#160;and&#160;parameters.  
  
cddataset:&#160;&#160;&#160;&#160;&#160;&#160;&#160;input&#160;cdms.cdmsNode.DatasetNode&#160;to&#160;translate  
id:&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;identifier&#160;of&#160;the&#160;resulting&#160;Dataset&#160;node.  
paramlistParent:&#160;string&#160;identifier&#160;of&#160;the&#160;parent&#160;activity&#160;that&#160;owns&#160;the
parameter&#160;list.  
generatedBy:&#160;&#160;&#160;&#160;&#160;string&#160;identifier&#160;of&#160;the&#160;activity&#160;that&#160;generated&#160;the&#160;dataset.  
ofType:&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;string&#160;distinguishing&#160;characteristic&#160;within&#160;an&#160;investigation,
e.g.&#160;"monthly&#160;means"  
isPartOf:&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;Dataset&#160;that&#160;contains&#160;this&#160;dataset,&#160;if&#160;any.  
convention:&#160;&#160;&#160;&#160;&#160;&#160;String&#160;metadata&#160;convention&#160;ID,&#160;e.g.&#160;"CF-1.0"  
timeCoverage:&#160;&#160;&#160;&#160;esg.TimeRegion&#160;instance.&#160;Overrides&#160;taxis.  
spaceCoverage:&#160;&#160;&#160;esg.SpaceRegion&#160;instance.&#160;Overrides&#160;xaxis,&#160;yaxis,&#160;and&#160;zaxis.  
format:&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;esg.Format&#160;instance.  
calendar:&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;CDMS&#160;calendar.  
taxis:&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;name&#160;of&#160;time&#160;axis.  
xaxis:&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;name&#160;of&#160;X&#160;axis.  
yaxis:&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;name&#160;of&#160;Y&#160;axis.  
zaxis:&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;name&#160;of&#160;Z&#160;axis.  
fileMapper:&#160;&#160;&#160;&#160;&#160;&#160;function&#160;mapping&#160;datafile&#160;path&#160;to&#160;logical&#160;fileid&#160;and&#160;name.
fileMapper&#160;has&#160;the&#160;form  
fileid,filename&#160;=&#160;fileMapper(path,&#160;optarg=mapperArg),&#160;where&#160;path&#160;may&#160;be
relative&#160;or&#160;absolute.  
If&#160;None,&#160;don't&#160;translate&#160;filenames.  
mapperArg:&#160;&#160;&#160;&#160;&#160;&#160;&#160;Optional&#160;argument&#160;passed&#160;to&#160;fileMapper `

* * *

UCRL-WEB-213937 | [ Privacy & Legal Notice ](/disclaimer.html)

[ webmaster@pcmdi.llnl.gov ](/webmaster@pcmdi.llnl.gov)

[ ![Powered by Plone](media/plone_powered.gif) ](/)

