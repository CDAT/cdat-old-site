---
layout: default
title:
---

 [ Skip to content. ](/cdat/source/api-reference/cdms.cdurlparse.html) | [ Skip
to navigation ](/cdat/source/api-reference/cdms.cdurlparse.html)

Search Site

[ Advanced Search&#8230; ](/search_form)

#  [ PCMDI Software Portal ](/)

#####  Sections

  * [ Home ](/)

#####  Personal tools

  * [ Log in ](/login_form)

You are here:  [ Home ](/) -> [ CDAT ](/cdat) -> [ Source Code ](/cdat/source)
-> [ API Reference ](/cdat/source/api-reference) -> Python: module
cdms.cdurlparse

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

        * [ Python: module cdms.cdurlparse ](/cdat/source/api-reference/cdms.cdurlparse.html)

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

  * [ ![Send this page to somebody](media/mail_icon.gif) ](/cdat/source/api-reference/cdms.cdurlparse.html/sendto_form)
  * [ ![Print this page](media/print_icon.gif) ](/this.print\(\))

#  Python: module cdms.cdurlparse

  
  
 [ cdms  ](/cdms.html) .cdurlparse 
[ index ](/)  

` Parse&#160;(absolute&#160;and&#160;relative)&#160;URLs.&#160;&#160;See [ RFC&#160;1808 ](/rfc/rfc1808.txt) :
"Relative&#160;Uniform  
Resource&#160;Locators",&#160;by&#160;R.&#160;Fielding,&#160;UC&#160;Irvine,&#160;June&#160;1995\. `

  
 Modules 

` `

[ string ](/string.html)  

  
 Functions 

` `

 clear_cache  () 
     ` Clear&#160;the&#160;parse&#160;cache. `

 test  () 

 urldefrag  (url) 
     ` Removes&#160;any&#160;existing&#160;fragment&#160;from&#160;URL.   
  
Returns&#160;a&#160;tuple&#160;of&#160;the&#160;defragmented&#160;URL&#160;and&#160;the&#160;fragment.&#160;&#160;If  
the&#160;URL&#160;contained&#160;no&#160;fragments,&#160;the&#160;second&#160;element&#160;is&#160;the  
empty&#160;string. `

 urljoin  (base, url, allow_fragments  =1  ) 
     ` #&#160;Join&#160;a&#160;base&#160;URL&#160;and&#160;a&#160;possibly&#160;relative&#160;URL&#160;to&#160;form&#160;an&#160;absolute   
#&#160;interpretation&#160;of&#160;the&#160;latter. `

 urlparse  (url, scheme  =''  , allow_fragments  =1  ) 
     ` #&#160;Parse&#160;a&#160;URL&#160;into&#160;6&#160;components:   
#&#160;<scheme>://<netloc>/<path>;<params>?<query>#<fragment>  
#&#160;Return&#160;a&#160;6-tuple:&#160;(scheme,&#160;netloc,&#160;path,&#160;params,&#160;query,&#160;fragment).  
#&#160;Note&#160;that&#160;we&#160;don't&#160;break&#160;the&#160;components&#160;up&#160;in&#160;smaller&#160;bits  
#&#160;(e.g.&#160;netloc&#160;is&#160;a&#160;single&#160;string)&#160;and&#160;we&#160;don't&#160;expand&#160;%&#160;escapes. `

 urlunparse  ((scheme, netloc, url, params, query, fragment)) 
     ` #&#160;Put&#160;a&#160;parsed&#160;URL&#160;back&#160;together&#160;again.&#160;&#160;This&#160;may&#160;result&#160;in&#160;a&#160;slightly   
#&#160;different,&#160;but&#160;equivalent&#160;URL,&#160;if&#160;the&#160;URL&#160;that&#160;was&#160;parsed&#160;originally  
#&#160;had&#160;redundant&#160;delimiters,&#160;e.g.&#160;a&#160;?&#160;with&#160;an&#160;empty&#160;query&#160;(the&#160;draft  
#&#160;states&#160;that&#160;these&#160;are&#160;equivalent). `

  
 Data 

` `

 MAX_CACHE_SIZE  = 20   
 non_hierarchical  = ['gopher', 'hdl', 'mailto', 'news', 'telnet', 'wais', 'snews']   
 scheme_chars  = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789+-.'   
 test_input  = '  \n  http://a/b/c/d  \n\n  g:h = <URL:g... http:g?y/./x = <URL:http://a/b/c/g?y/./x> \n  '   
 uses_fragment  = ['ftp', 'hdl', 'http', 'ldap', 'gopher', 'news', 'nntp', 'wais', 'https', 'shttp', 'snews', 'file', 'prospero', '']   
 uses_netloc  = ['ftp', 'http', 'ldap', 'gopher', 'nntp', 'telnet', 'wais', 'file', 'https', 'shttp', 'snews', 'prospero', '']   
 uses_params  = ['ftp', 'hdl', 'prospero', 'http', 'ldap', 'https', 'shttp', '']   
 uses_query  = ['http', 'ldap', 'wais', 'https', 'shttp', 'gopher', '']   
 uses_relative  = ['ftp', 'http', 'ldap', 'gopher', 'nntp', 'wais', 'file', 'https', 'shttp', 'prospero', ''] 

* * *

UCRL-WEB-213937 | [ Privacy & Legal Notice ](/disclaimer.html)

[ webmaster@pcmdi.llnl.gov ](/webmaster@pcmdi.llnl.gov)

[ ![Powered by Plone](media/plone_powered.gif) ](/)

