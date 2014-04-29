---
layout: default
title:
---

 [ Skip to content. ](/cdat/source/api-reference/ncml.csParse.html) | [ Skip to
navigation ](/cdat/source/api-reference/ncml.csParse.html)

Search Site

[ Advanced Search&#8230; ](/search_form)

#  [ PCMDI Software Portal ](/)

#####  Sections

  * [ Home ](/)

#####  Personal tools

  * [ Log in ](/login_form)

You are here:  [ Home ](/) -> [ CDAT ](/cdat) -> [ Source Code ](/cdat/source)
-> [ API Reference ](/cdat/source/api-reference) -> Python: module
ncml.csParse

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

        * [ Python: module ncml.csParse ](/cdat/source/api-reference/ncml.csParse.html)

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

  * [ ![Send this page to somebody](media/mail_icon.gif) ](/cdat/source/api-reference/ncml.csParse.html/sendto_form)
  * [ ![Print this page](media/print_icon.gif) ](/this.print\(\))

#  Python: module ncml.csParse

  
  
 [ ncml  ](/ncml.html) .csParse 
[ index ](/)  

` NcML&#160;+&#160;coordinate&#160;extensions&#160;parsing.&#160;See [
http://www.unidata.ucar.edu/schemas/netcdf-cs.xsd ](/schemas/netcdf-cs.xsd) `

  
 Modules 

` `

[ ncml.cs ](/ncml.cs.html)  

[ ncml.ncmlParse ](/ncml.ncmlParse.html)  

[ string ](/string.html)  

  
 Classes 

` `

[ ncml.ncmlParse.ncmlContentHandler ](/ncml.ncmlParse.html) ( [
xml.sax.handler.ContentHandler ](/xml.sax.handler.html) )

    

[ CSContentHandler ](/ncml.csParse.html)

  
class  CSContentHandler  ( [ ncml.ncmlParse.ncmlContentHandler
](/ncml.ncmlParse.html) )

` `

Method resolution order:

     [ CSContentHandler ](/ncml.csParse.html)
     [ ncml.ncmlParse.ncmlContentHandler ](/ncml.ncmlParse.html)
     [ xml.sax.handler.ContentHandler ](/xml.sax.handler.html)

* * *

Methods defined here:  

 __init__  (self) 

 endCoordinateAxis  (self) 

 endCoordinateAxisBoundary  (self) 

 endCoordinateSystem  (self) 

 endCoordinateTransform  (self) 

 endElementNS  (self, name, qname) 

 endNetcdf  (self) 

 endVariable  (self) 

 startCoordinateAxis  (self, attrs) 

 startCoordinateAxisBoundary  (self, attrs) 

 startCoordinateAxisRef  (self, attrs) 

 startCoordinateSystem  (self, attrs) 

 startCoordinateTransform  (self, attrs) 

 startCoordinateTransformRef  (self, attrs) 

 startElementNS  (self, name, qname, attrs) 

 startNetcdf  (self, attrs) 

 startParameter  (self, attrs) 

 startVariable  (self, attrs) 

* * *

Methods inherited from [ ncml.ncmlParse.ncmlContentHandler
](/ncml.ncmlParse.html) :  

 characters  (self, ch) 

 endElement  (self, name) 

 endValues  (self) 

 peek  (self) 

 pop  (self) 

 push  (self, item) 

 setDocumentLocator  (self, locator) 

 startAttribute  (self, attrs) 

 startDimension  (self, attrs) 

 startElement  (self, name, attrs) 

 startValues  (self, attrs) 

* * *

Methods inherited from [ xml.sax.handler.ContentHandler
](/xml.sax.handler.html) :  

 endDocument  (self) 
     ` Receive&#160;notification&#160;of&#160;the&#160;end&#160;of&#160;a&#160;document.   
  
The&#160;SAX&#160;parser&#160;will&#160;invoke&#160;this&#160;method&#160;only&#160;once,&#160;and&#160;it&#160;will  
be&#160;the&#160;last&#160;method&#160;invoked&#160;during&#160;the&#160;parse.&#160;The&#160;parser&#160;shall  
not&#160;invoke&#160;this&#160;method&#160;until&#160;it&#160;has&#160;either&#160;abandoned&#160;parsing  
(because&#160;of&#160;an&#160;unrecoverable&#160;error)&#160;or&#160;reached&#160;the&#160;end&#160;of  
input. `

 endPrefixMapping  (self, prefix) 
     ` End&#160;the&#160;scope&#160;of&#160;a&#160;prefix-URI&#160;mapping.   
  
See&#160;startPrefixMapping&#160;for&#160;details.&#160;This&#160;event&#160;will&#160;always  
occur&#160;after&#160;the&#160;corresponding&#160;endElement&#160;event,&#160;but&#160;the&#160;order  
of&#160;endPrefixMapping&#160;events&#160;is&#160;not&#160;otherwise&#160;guaranteed. `

 ignorableWhitespace  (self, whitespace) 
     ` Receive&#160;notification&#160;of&#160;ignorable&#160;whitespace&#160;in&#160;element&#160;content.   
  
Validating&#160;Parsers&#160;must&#160;use&#160;this&#160;method&#160;to&#160;report&#160;each&#160;chunk  
of&#160;ignorable&#160;whitespace&#160;(see&#160;the&#160;W3C&#160;XML&#160;1.0&#160;recommendation,  
section&#160;2.10):&#160;non-validating&#160;parsers&#160;may&#160;also&#160;use&#160;this&#160;method  
if&#160;they&#160;are&#160;capable&#160;of&#160;parsing&#160;and&#160;using&#160;content&#160;models.  
  
SAX&#160;parsers&#160;may&#160;return&#160;all&#160;contiguous&#160;whitespace&#160;in&#160;a&#160;single  
chunk,&#160;or&#160;they&#160;may&#160;split&#160;it&#160;into&#160;several&#160;chunks;&#160;however,&#160;all  
of&#160;the&#160;characters&#160;in&#160;any&#160;single&#160;event&#160;must&#160;come&#160;from&#160;the&#160;same  
external&#160;entity,&#160;so&#160;that&#160;the&#160;Locator&#160;provides&#160;useful  
information. `

 processingInstruction  (self, target, data) 
     ` Receive&#160;notification&#160;of&#160;a&#160;processing&#160;instruction.   
  
The&#160;Parser&#160;will&#160;invoke&#160;this&#160;method&#160;once&#160;for&#160;each&#160;processing  
instruction&#160;found:&#160;note&#160;that&#160;processing&#160;instructions&#160;may&#160;occur  
before&#160;or&#160;after&#160;the&#160;main&#160;document&#160;element.  
  
A&#160;SAX&#160;parser&#160;should&#160;never&#160;report&#160;an&#160;XML&#160;declaration&#160;(XML&#160;1.0,  
section&#160;2.8)&#160;or&#160;a&#160;text&#160;declaration&#160;(XML&#160;1.0,&#160;section&#160;4.3.1)  
using&#160;this&#160;method. `

 skippedEntity  (self, name) 
     ` Receive&#160;notification&#160;of&#160;a&#160;skipped&#160;entity.   
  
The&#160;Parser&#160;will&#160;invoke&#160;this&#160;method&#160;once&#160;for&#160;each&#160;entity  
skipped.&#160;Non-validating&#160;processors&#160;may&#160;skip&#160;entities&#160;if&#160;they  
have&#160;not&#160;seen&#160;the&#160;declarations&#160;(because,&#160;for&#160;example,&#160;the  
entity&#160;was&#160;declared&#160;in&#160;an&#160;external&#160;DTD&#160;subset).&#160;All&#160;processors  
may&#160;skip&#160;external&#160;entities,&#160;depending&#160;on&#160;the&#160;values&#160;of&#160;the  
[ http://xml.org/sax/features/external-general-entities ](/sax/features
/external-general-entities) and&#160;the  
[ http://xml.org/sax/features/external-parameter-entities ](/sax/features
/external-parameter-entities)  
properties. `

 startDocument  (self) 
     ` Receive&#160;notification&#160;of&#160;the&#160;beginning&#160;of&#160;a&#160;document.   
  
The&#160;SAX&#160;parser&#160;will&#160;invoke&#160;this&#160;method&#160;only&#160;once,&#160;before&#160;any  
other&#160;methods&#160;in&#160;this&#160;interface&#160;or&#160;in&#160;DTDHandler&#160;(except&#160;for  
setDocumentLocator). `

 startPrefixMapping  (self, prefix, uri) 
     ` Begin&#160;the&#160;scope&#160;of&#160;a&#160;prefix-URI&#160;Namespace&#160;mapping.   
  
The&#160;information&#160;from&#160;this&#160;event&#160;is&#160;not&#160;necessary&#160;for&#160;normal  
Namespace&#160;processing:&#160;the&#160;SAX&#160;XML&#160;reader&#160;will&#160;automatically  
replace&#160;prefixes&#160;for&#160;element&#160;and&#160;attribute&#160;names&#160;when&#160;the  
[ http://xml.org/sax/features/namespaces ](/sax/features/namespaces) feature
is&#160;true&#160;(the  
default).  
  
There&#160;are&#160;cases,&#160;however,&#160;when&#160;applications&#160;need&#160;to&#160;use  
prefixes&#160;in&#160;character&#160;data&#160;or&#160;in&#160;attribute&#160;values,&#160;where&#160;they  
cannot&#160;safely&#160;be&#160;expanded&#160;automatically;&#160;the  
start/endPrefixMapping&#160;event&#160;supplies&#160;the&#160;information&#160;to&#160;the  
application&#160;to&#160;expand&#160;prefixes&#160;in&#160;those&#160;contexts&#160;itself,&#160;if  
necessary.  
  
Note&#160;that&#160;start/endPrefixMapping&#160;events&#160;are&#160;not&#160;guaranteed&#160;to  
be&#160;properly&#160;nested&#160;relative&#160;to&#160;each-other:&#160;all  
startPrefixMapping&#160;events&#160;will&#160;occur&#160;before&#160;the&#160;corresponding  
startElement&#160;event,&#160;and&#160;all&#160;endPrefixMapping&#160;events&#160;will&#160;occur  
after&#160;the&#160;corresponding&#160;endElement&#160;event,&#160;but&#160;their&#160;order&#160;is  
not&#160;guaranteed. `

  
 Functions 

` `

 load  (path) 
     ` Create&#160;a&#160;tree&#160;of&#160;NCML&#160;nodes&#160;from&#160;a&#160;file&#160;path.   
Returns&#160;the&#160;parse&#160;tree&#160;root&#160;node. `

  
 Data 

` `

 feature_namespaces  = 'http://xml.org/sax/features/namespaces' 

* * *

UCRL-WEB-213937 | [ Privacy & Legal Notice ](/disclaimer.html)

[ webmaster@pcmdi.llnl.gov ](/webmaster@pcmdi.llnl.gov)

[ ![Powered by Plone](media/plone_powered.gif) ](/)

