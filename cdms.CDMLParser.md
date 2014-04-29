---
layout: default
title:
---

 [ Skip to content. ](/cdat/source/api-reference/cdms.CDMLParser.html) | [ Skip
to navigation ](/cdat/source/api-reference/cdms.CDMLParser.html)

Search Site

[ Advanced Search&#8230; ](/search_form)

#  [ PCMDI Software Portal ](/)

#####  Sections

  * [ Home ](/)

#####  Personal tools

  * [ Log in ](/login_form)

You are here:  [ Home ](/) -> [ CDAT ](/cdat) -> [ Source Code ](/cdat/source)
-> [ API Reference ](/cdat/source/api-reference) -> Python: module
cdms.CDMLParser

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

        * [ Python: module cdms.CDMLParser ](/cdat/source/api-reference/cdms.CDMLParser.html)

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

  * [ ![Send this page to somebody](media/mail_icon.gif) ](/cdat/source/api-reference/cdms.CDMLParser.html/sendto_form)
  * [ ![Print this page](media/print_icon.gif) ](/this.print\(\))

#  Python: module cdms.CDMLParser

  
  
 [ cdms  ](/cdms.html) .CDMLParser 
[ index ](/)  

` Parse&#160;a&#160;CDML/XML&#160;file `

  
 Modules 

` `

[ cdms.CDML ](/cdms.CDML.html)  

[ cdms.cdmsNode ](/cdms.cdmsNode.html)  

[ re ](/re.html)  

[ string ](/string.html)  

  
 Classes 

` `

[ cdms.cdxmllib.XMLParser ](/cdms.cdxmllib.html)

    

[ CDMLParser ](/cdms.CDMLParser.html)

  
class  CDMLParser  ( [ cdms.cdxmllib.XMLParser ](/cdms.cdxmllib.html) )

` `

Methods defined here:  

 __init__  (self, verbose  =0  ) 

 cdml_syntax_error  (self, lineno, message) 

 close  (self) 

 end_attr  (self) 
     ` #&#160;Now&#160;the&#160;value&#160;if&#160;any&#160;as&#160;stored&#160;in&#160;self.  content  `

 end_axis  (self) 

 end_cdml  (self) 

 end_component  (self) 

 end_compoundAxis  (self) 

 end_data  (self) 

 end_dataset  (self) 

 end_doclink  (self) 

 end_domElem  (self) 

 end_domain  (self) 

 end_linear  (self) 

 end_rectGrid  (self) 

 end_variable  (self) 

 end_xlink  (self) 

 getCurrentNode  (self) 
     ` #&#160;Get&#160;the&#160;current&#160;parent&#160;node `

 getRoot  (self) 
     ` #&#160;Get&#160;the&#160;root&#160;node `

 handle_cdata  (self, data) 

 handle_data  (self, data) 
     ` #&#160;Handle&#160;content   
#&#160;discard&#160;data&#160;which&#160;is&#160;just&#160;whitespace,  
#&#160;and&#160;strip&#160;other&#160;data `

 handle_proc  (self, name, data) 

 handle_special  (self, data) 

 handle_starttag  (self, tag, method, attrs) 

 popCurrentNode  (self) 
     ` #&#160;Pop&#160;the&#160;current&#160;node&#160;off&#160;the&#160;stack `

 pushCurrentNode  (self, node) 
     ` #&#160;Push&#160;current&#160;node&#160;on&#160;the&#160;stack `

 start_attr  (self, attrs) 

 start_axis  (self, attrs) 

 start_cdml  (self, attrs) 
     ` #------------------------------------------------------------------------ `

 start_component  (self, attrs) 

 start_compoundAxis  (self, attrs) 
     ` #------------------------------------------------------------------------ `

 start_data  (self, attrs) 
     ` #------------------------------------------------------------------------ `

 start_dataset  (self, attrs) 

 start_doclink  (self, attrs) 

 start_domElem  (self, attrs) 

 start_domain  (self, attrs) 
     ` #------------------------------------------------------------------------ `

 start_linear  (self, attrs) 

 start_rectGrid  (self, attrs) 

 start_variable  (self, attrs) 

 start_xlink  (self, attrs) 

 unknown_charref  (self, ref) 

 unknown_endtag  (self, tag) 

 unknown_entityref  (self, ref) 

 unknown_starttag  (self, tag, attrs) 

* * *

Methods inherited from [ cdms.cdxmllib.XMLParser ](/cdms.cdxmllib.html) :  

 feed  (self, data) 
     ` #&#160;Interface&#160;\--&#160;feed&#160;some&#160;data&#160;to&#160;the&#160;parser.&#160;&#160;Call&#160;this&#160;as   
#&#160;often&#160;as&#160;you&#160;want,&#160;with&#160;as&#160;little&#160;or&#160;as&#160;much&#160;text&#160;as&#160;you  
#&#160;want&#160;(may&#160;include&#160;'\n').&#160;&#160;(This&#160;just&#160;saves&#160;the&#160;text,&#160;all&#160;the  
#&#160;processing&#160;is&#160;done&#160;by [ goahead ](/) ().) `

 finish_endtag  (self, tag) 
     ` #&#160;Internal&#160;\--&#160;finish&#160;processing&#160;of&#160;end&#160;tag `

 finish_starttag  (self, tagname, attrdict, method) 
     ` #&#160;Internal&#160;\--&#160;finish&#160;processing&#160;of&#160;start&#160;tag `

 getnamespace  (self) 
     ` #&#160;Interface&#160;-&#160;return&#160;a&#160;dictionary&#160;of&#160;all&#160;namespaces&#160;currently&#160;valid `

 goahead  (self, end) 
     ` #&#160;Internal&#160;\--&#160;handle&#160;data&#160;as&#160;far&#160;as&#160;reasonable.&#160;&#160;May&#160;leave&#160;state   
#&#160;and&#160;data&#160;to&#160;be&#160;processed&#160;by&#160;a&#160;subsequent&#160;call.&#160;&#160;If&#160;'end'&#160;is  
#&#160;true,&#160;force&#160;handling&#160;all&#160;data&#160;as&#160;if&#160;followed&#160;by&#160;EOF&#160;marker. `

 handle_charref  (self, name) 
     ` #&#160;Example&#160;\--&#160;handle&#160;character&#160;reference,&#160;no&#160;need&#160;to&#160;override `

 handle_comment  (self, data) 
     ` #&#160;Example&#160;\--&#160;handle&#160;comment,&#160;could&#160;be&#160;overridden `

 handle_doctype  (self, tag, pubid, syslit, data) 
     ` #&#160;Overridable&#160;\--&#160;handle&#160;DOCTYPE `

 handle_endtag  (self, tag, method) 
     ` #&#160;Overridable&#160;\--&#160;handle&#160;end&#160;tag `

 handle_xml  (self, encoding, standalone) 
     ` #&#160;Overridable&#160;\--&#160;handle&#160;xml&#160;processing&#160;instruction `

 parse_attributes  (self, tag, i, j) 
     ` #&#160;Internal&#160;\--&#160;parse&#160;attributes&#160;between&#160;i&#160;and&#160;j `

 parse_cdata  (self, i) 
     ` #&#160;Internal&#160;\--&#160;handle&#160;CDATA&#160;tag,&#160;return&#160;length&#160;or&#160;-1&#160;if&#160;not&#160;terminated `

 parse_comment  (self, i) 
     ` #&#160;Internal&#160;\--&#160;parse&#160;comment,&#160;return&#160;length&#160;or&#160;-1&#160;if&#160;not&#160;terminated `

 parse_doctype  (self, res) 
     ` #&#160;Internal&#160;\--&#160;handle&#160;DOCTYPE&#160;tag,&#160;return&#160;length&#160;or&#160;-1&#160;if&#160;not&#160;terminated `

 parse_endtag  (self, i) 
     ` #&#160;Internal&#160;\--&#160;parse&#160;endtag `

 parse_proc  (self, i) 
     ` #&#160;Internal&#160;\--&#160;handle&#160;a&#160;processing&#160;instruction&#160;tag `

 parse_starttag  (self, i) 
     ` #&#160;Internal&#160;\--&#160;handle&#160;starttag,&#160;return&#160;length&#160;or&#160;-1&#160;if&#160;not&#160;terminated `

 reset  (self) 
     ` #&#160;Interface&#160;\--&#160;reset&#160;this&#160;instance.&#160;&#160;Loses&#160;all&#160;unprocessed&#160;data `

 setliteral  (self, *args) 
     ` #&#160;For&#160;derived&#160;classes&#160;only&#160;\--&#160;enter&#160;literal&#160;mode&#160;(CDATA) `

 setnomoretags  (self) 
     ` #&#160;For&#160;derived&#160;classes&#160;only&#160;\--&#160;enter&#160;literal&#160;mode&#160;(CDATA)&#160;till&#160;EOF `

 syntax_error  (self, message) 
     ` #&#160;Example&#160;\--&#160;handle&#160;relatively&#160;harmless&#160;syntax&#160;errors,&#160;could&#160;be&#160;overridden `

 translate_references  (self, data, all  =1  ) 
     ` #&#160;Interface&#160;\--&#160;translate&#160;references `

* * *

Data and other attributes inherited from [ cdms.cdxmllib.XMLParser
](/cdms.cdxmllib.html) :  

 attributes  = {} 

 elements  = {} 

 entitydefs  = {'amp': '&#38;', 'apos': '&#39;', 'gt': '&#62;', 'lt': '&#60;', 'quot': '&#34;'} 

  
 Data 

` `

 InvalidAttribute  = 'Invalid attribute' 

* * *

UCRL-WEB-213937 | [ Privacy & Legal Notice ](/disclaimer.html)

[ webmaster@pcmdi.llnl.gov ](/webmaster@pcmdi.llnl.gov)

[ ![Powered by Plone](media/plone_powered.gif) ](/)

