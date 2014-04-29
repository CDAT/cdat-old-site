---
layout: default
title:
---

 [ Skip to content. ](/cdat/source/api-reference/cdms.cdmsURLopener.html) | [
Skip to navigation ](/cdat/source/api-reference/cdms.cdmsURLopener.html)

Search Site

[ Advanced Search&#8230; ](/search_form)

#  [ PCMDI Software Portal ](/)

#####  Sections

  * [ Home ](/)

#####  Personal tools

  * [ Log in ](/login_form)

You are here:  [ Home ](/) -> [ CDAT ](/cdat) -> [ Source Code ](/cdat/source)
-> [ API Reference ](/cdat/source/api-reference) -> Python: module
cdms.cdmsURLopener

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

        * [ Python: module cdms.cdmsURLopener ](/cdat/source/api-reference/cdms.cdmsURLopener.html)

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

  * [ ![Send this page to somebody](media/mail_icon.gif) ](/cdat/source/api-reference/cdms.cdmsURLopener.html/sendto_form)
  * [ ![Print this page](media/print_icon.gif) ](/this.print\(\))

#  Python: module cdms.cdmsURLopener

  
  
 [ cdms  ](/cdms.html) .cdmsURLopener 
[ index ](/)  

` Overrides&#160;urllib&#160;error&#160;handling `

  
 Modules 

` `

[ urllib ](/urllib.html)  

  
 Classes 

` `

[ urllib.FancyURLopener ](/urllib.html) ( [ urllib.URLopener ](/urllib.html) )

    

[ CDMSURLopener ](/cdms.cdmsURLopener.html)

  
class  CDMSURLopener  ( [ urllib.FancyURLopener ](/urllib.html) )

` `

Method resolution order:

     [ CDMSURLopener ](/cdms.cdmsURLopener.html)
     [ urllib.FancyURLopener ](/urllib.html)
     [ urllib.URLopener ](/urllib.html)

* * *

Methods defined here:  

 http_error_default  (self, url, fp, errcode, errmsg, headers) 
     ` #&#160;Override [ FancyURLopener ](/urllib.html) error&#160;handling&#160;-&#160;raise&#160;an&#160;exception   
#&#160;Can&#160;also&#160;define&#160;function&#160;http_error_DDD&#160;where&#160;DDD&#160;is&#160;the&#160;3-digit&#160;error&#160;code,  
#&#160;to&#160;handle&#160;specific&#160;errors. `

* * *

Methods inherited from [ urllib.FancyURLopener ](/urllib.html) :  

 __init__  (self, *args, kwargs) 

 get_user_passwd  (self, host, realm, clear_cache  =0  ) 

 http_error_301  (self, url, fp, errcode, errmsg, headers, data  =None  ) 
     ` Error&#160;301&#160;\--&#160;also&#160;relocated&#160;(permanently). `

 http_error_302  (self, url, fp, errcode, errmsg, headers, data  =None  ) 
     ` Error&#160;302&#160;\--&#160;relocated&#160;(temporarily). `

 http_error_303  (self, url, fp, errcode, errmsg, headers, data  =None  ) 
     ` Error&#160;303&#160;\--&#160;also&#160;relocated&#160;(essentially&#160;identical&#160;to&#160;302). `

 http_error_307  (self, url, fp, errcode, errmsg, headers, data  =None  ) 
     ` Error&#160;307&#160;\--&#160;relocated,&#160;but&#160;turn&#160;POST&#160;into&#160;error. `

 http_error_401  (self, url, fp, errcode, errmsg, headers, data  =None  ) 
     ` Error&#160;401&#160;\--&#160;authentication&#160;required.   
See&#160;this&#160;URL&#160;for&#160;a&#160;description&#160;of&#160;the&#160;basic&#160;authentication&#160;scheme:  
[ http://www.ics.uci.edu/pub/ietf/http/draft-ietf-http-v10-spec-00.txt
](/pub/ietf/http/draft-ietf-http-v10-spec-00.txt) `

 prompt_user_passwd  (self, host, realm) 
     ` Override&#160;this&#160;in&#160;a&#160;GUI&#160;environment! `

 redirect_internal  (self, url, fp, errcode, errmsg, headers, data) 

 retry_http_basic_auth  (self, url, realm, data  =None  ) 

 retry_https_basic_auth  (self, url, realm, data  =None  ) 

* * *

Methods inherited from [ urllib.URLopener ](/urllib.html) :  

 __del__  (self) 

 addheader  (self, *args) 
     ` Add&#160;a&#160;header&#160;to&#160;be&#160;used&#160;by&#160;the&#160;HTTP&#160;interface&#160;only   
e.g.&#160;u. [ addheader ](/) ('Accept',&#160;'sound/basic') `

 cleanup  (self) 

 close  (self) 

 http_error  (self, url, fp, errcode, errmsg, headers, data  =None  ) 
     ` Handle&#160;http&#160;errors.   
Derived&#160;class&#160;can&#160;override&#160;this,&#160;or&#160;provide&#160;specific&#160;handlers  
named&#160;http_error_DDD&#160;where&#160;DDD&#160;is&#160;the&#160;3-digit&#160;error&#160;code. `

 open  (self, fullurl, data  =None  ) 
     ` Use&#160;URLopener(). [ open ](/) (file)&#160;instead&#160;of [ open ](/) (file,&#160;'r'). `

 open_data  (self, url, data  =None  ) 
     ` Use&#160;"data"&#160;URL. `

 open_file  (self, url) 
     ` Use&#160;local&#160;file&#160;or&#160;FTP&#160;depending&#160;on&#160;form&#160;of&#160;URL. `

 open_ftp  (self, url) 
     ` Use&#160;FTP&#160;protocol. `

 open_gopher  (self, url) 
     ` Use&#160;Gopher&#160;protocol. `

 open_http  (self, url, data  =None  ) 
     ` Use&#160;HTTP&#160;protocol. `

 open_https  (self, url, data  =None  ) 
     ` Use&#160;HTTPS&#160;protocol. `

 open_local_file  (self, url) 
     ` Use&#160;local&#160;file. `

 open_unknown  (self, fullurl, data  =None  ) 
     ` Overridable&#160;interface&#160;to&#160;open&#160;unknown&#160;URL&#160;type. `

 open_unknown_proxy  (self, proxy, fullurl, data  =None  ) 
     ` Overridable&#160;interface&#160;to&#160;open&#160;unknown&#160;URL&#160;type. `

 retrieve  (self, url, filename  =None  , reporthook  =None  , data  =None  ) 
     ` [ retrieve ](/) (url)&#160;returns&#160;(filename,&#160;headers)&#160;for&#160;a&#160;local&#160;object   
or&#160;(tempfilename,&#160;headers)&#160;for&#160;a&#160;remote&#160;object. `

* * *

Data and other attributes inherited from [ urllib.URLopener ](/urllib.html) :  

 version  = 'Python-urllib/1.16' 

* * *

UCRL-WEB-213937 | [ Privacy & Legal Notice ](/disclaimer.html)

[ webmaster@pcmdi.llnl.gov ](/webmaster@pcmdi.llnl.gov)

[ ![Powered by Plone](media/plone_powered.gif) ](/)

