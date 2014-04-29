---
layout: default
title:
---

 [ Skip to content. ](/cdat/source/api-reference/cdms.cdxmllib.html) | [ Skip
to navigation ](/cdat/source/api-reference/cdms.cdxmllib.html)

Search Site

[ Advanced Search&#8230; ](/search_form)

#  [ PCMDI Software Portal ](/)

#####  Sections

  * [ Home ](/)

#####  Personal tools

  * [ Log in ](/login_form)

You are here:  [ Home ](/) -> [ CDAT ](/cdat) -> [ Source Code ](/cdat/source)
-> [ API Reference ](/cdat/source/api-reference) -> Python: module
cdms.cdxmllib

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

        * [ Python: module cdms.cdxmllib ](/cdat/source/api-reference/cdms.cdxmllib.html)

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

  * [ ![Send this page to somebody](media/mail_icon.gif) ](/cdat/source/api-reference/cdms.cdxmllib.html/sendto_form)
  * [ ![Print this page](media/print_icon.gif) ](/this.print\(\))

#  Python: module cdms.cdxmllib

  
  
 [ cdms  ](/cdms.html) .cdxmllib 
[ index ](/)  

` A&#160;parser&#160;for&#160;XML,&#160;using&#160;the&#160;derived&#160;class&#160;as&#160;static&#160;DTD. `

  
 Modules 

` `

[ re ](/re.html)  

[ string ](/string.html)  

  
 Classes 

` `

[ XMLParser ](/cdms.cdxmllib.html)

    

[ TestXMLParser ](/cdms.cdxmllib.html)

[ exceptions.RuntimeError ](/exceptions.html) ( [ exceptions.StandardError
](/exceptions.html) )

    

[ Error ](/cdms.cdxmllib.html)

  
class  Error  ( [ exceptions.RuntimeError ](/exceptions.html) )

` `

Method resolution order:

     [ Error ](/cdms.cdxmllib.html)
     [ exceptions.RuntimeError ](/exceptions.html)
     [ exceptions.StandardError ](/exceptions.html)
     [ exceptions.Exception ](/exceptions.html)

* * *

Methods inherited from [ exceptions.Exception ](/exceptions.html) :  

 __getitem__  (...) 

 __init__  (...) 

 __str__  (...) 

  
class  TestXMLParser  ( [ XMLParser ](/cdms.cdxmllib.html) )

` `

Methods defined here:  

 __init__  (self, kw) 

 close  (self) 

 flush  (self) 

 handle_cdata  (self, data) 

 handle_comment  (self, data) 

 handle_data  (self, data) 

 handle_doctype  (self, tag, pubid, syslit, data) 

 handle_proc  (self, name, data) 

 handle_xml  (self, encoding, standalone) 

 syntax_error  (self, message) 

 unknown_charref  (self, ref) 

 unknown_endtag  (self, tag) 

 unknown_entityref  (self, ref) 

 unknown_starttag  (self, tag, attrs) 

* * *

Methods inherited from [ XMLParser ](/cdms.cdxmllib.html) :  

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

 handle_endtag  (self, tag, method) 
     ` #&#160;Overridable&#160;\--&#160;handle&#160;end&#160;tag `

 handle_starttag  (self, tag, method, attrs) 
     ` #&#160;Overridable&#160;\--&#160;handle&#160;start&#160;tag `

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

 translate_references  (self, data, all  =1  ) 
     ` #&#160;Interface&#160;\--&#160;translate&#160;references `

* * *

Data and other attributes inherited from [ XMLParser ](/cdms.cdxmllib.html) :  

 attributes  = {} 

 elements  = {} 

 entitydefs  = {'amp': '&#38;', 'apos': '&#39;', 'gt': '&#62;', 'lt': '&#60;', 'quot': '&#34;'} 

  
class  XMLParser 

` `

Methods defined here:  

 __init__  (self, kw) 
     ` #&#160;Interface&#160;\--&#160;initialize&#160;and&#160;reset&#160;this&#160;instance `

 close  (self) 
     ` #&#160;Interface&#160;\--&#160;handle&#160;the&#160;remaining&#160;data `

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

 handle_cdata  (self, data) 
     ` #&#160;Example&#160;\--&#160;handle&#160;cdata,&#160;could&#160;be&#160;overridden `

 handle_charref  (self, name) 
     ` #&#160;Example&#160;\--&#160;handle&#160;character&#160;reference,&#160;no&#160;need&#160;to&#160;override `

 handle_comment  (self, data) 
     ` #&#160;Example&#160;\--&#160;handle&#160;comment,&#160;could&#160;be&#160;overridden `

 handle_data  (self, data) 
     ` #&#160;Example&#160;\--&#160;handle&#160;data,&#160;should&#160;be&#160;overridden `

 handle_doctype  (self, tag, pubid, syslit, data) 
     ` #&#160;Overridable&#160;\--&#160;handle&#160;DOCTYPE `

 handle_endtag  (self, tag, method) 
     ` #&#160;Overridable&#160;\--&#160;handle&#160;end&#160;tag `

 handle_proc  (self, name, data) 
     ` #&#160;Example&#160;\--&#160;handle&#160;processing&#160;instructions,&#160;could&#160;be&#160;overridden `

 handle_starttag  (self, tag, method, attrs) 
     ` #&#160;Overridable&#160;\--&#160;handle&#160;start&#160;tag `

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

 unknown_charref  (self, ref) 

 unknown_endtag  (self, tag) 

 unknown_entityref  (self, name) 

 unknown_starttag  (self, tag, attrs) 
     ` #&#160;To&#160;be&#160;overridden&#160;\--&#160;handlers&#160;for&#160;unknown&#160;objects `

* * *

Data and other attributes defined here:  

 attributes  = {} 

 elements  = {} 

 entitydefs  = {'amp': '&#38;', 'apos': '&#39;', 'gt': '&#62;', 'lt': '&#60;', 'quot': '&#34;'} 

  
 Functions 

` `

 test  (args  =None  ) 

  
 Data 

` `

 amp  = <_sre.SRE_Pattern object>   
 attrfind  = <_sre.SRE_Pattern object>   
 attrtrans  = '  \x00\x01\x02\x03\x04\x05\x06\x07\x08  \x0b\x0c  \x0e\x0f\x10\x11\x12\x13\x14\x15\x16\x17\x18\x19\x1a\x1b\x1c\x1d\x1e\x1f  !"#$%& \'  ()*+,-./...  \xcf\xd0\xd1\xd2\xd3\xd4\xd5\xd6\xd7\xd8\xd9\xda\xdb\xdc\xdd\xde\xdf\xe0\xe1\xe2\xe3\xe4\xe5\xe6\xe7\xe8\xe9\xea\xeb\xec\xed\xee\xef\xf0\xf1\xf2\xf3\xf4\xf5\xf6\xf7\xf8\xf9\xfa\xfb\xfc\xfd\xfe\xff  '   
 cdataclose  = <_sre.SRE_Pattern object>   
 cdataopen  = <_sre.SRE_Pattern object>   
 charref  = <_sre.SRE_Pattern object>   
 commentclose  = <_sre.SRE_Pattern object>   
 commentopen  = <_sre.SRE_Pattern object>   
 doctype  = <_sre.SRE_Pattern object>   
 doubledash  = <_sre.SRE_Pattern object>   
 endbracket  = <_sre.SRE_Pattern object>   
 endbracketfind  = <_sre.SRE_Pattern object>   
 endtagopen  = <_sre.SRE_Pattern object>   
 entityref  = <_sre.SRE_Pattern object>   
 illegal  = <_sre.SRE_Pattern object>   
 interesting  = <_sre.SRE_Pattern object>   
 ncname  = <_sre.SRE_Pattern object>   
 newline  = <_sre.SRE_Pattern object>   
 procclose  = <_sre.SRE_Pattern object>   
 procopen  = <_sre.SRE_Pattern object>   
 qname  = <_sre.SRE_Pattern object>   
 ref  = <_sre.SRE_Pattern object>   
 space  = <_sre.SRE_Pattern object>   
 starttagend  = <_sre.SRE_Pattern object>   
 starttagmatch  = <_sre.SRE_Pattern object>   
 starttagopen  = <_sre.SRE_Pattern object>   
 tagfind  = <_sre.SRE_Pattern object>   
 version  = '0.3'   
 xmldecl  = <_sre.SRE_Pattern object>   
 xmlns  = <_sre.SRE_Pattern object>

* * *

UCRL-WEB-213937 | [ Privacy & Legal Notice ](/disclaimer.html)

[ webmaster@pcmdi.llnl.gov ](/webmaster@pcmdi.llnl.gov)

[ ![Powered by Plone](media/plone_powered.gif) ](/)

