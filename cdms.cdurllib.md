---
layout: default
title:
---

 [ Skip to content. ](/cdat/source/api-reference/cdms.cdurllib.html) | [ Skip
to navigation ](/cdat/source/api-reference/cdms.cdurllib.html)

Search Site

[ Advanced Search&#8230; ](/search_form)

#  [ PCMDI Software Portal ](/)

#####  Sections

  * [ Home ](/)

#####  Personal tools

  * [ Log in ](/login_form)

You are here:  [ Home ](/) -> [ CDAT ](/cdat) -> [ Source Code ](/cdat/source)
-> [ API Reference ](/cdat/source/api-reference) -> Python: module
cdms.cdurllib

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

        * [ Python: module cdms.cdurllib ](/cdat/source/api-reference/cdms.cdurllib.html)

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

  * [ ![Send this page to somebody](media/mail_icon.gif) ](/cdat/source/api-reference/cdms.cdurllib.html/sendto_form)
  * [ ![Print this page](media/print_icon.gif) ](/this.print\(\))

#  Python: module cdms.cdurllib

  
  
 [ cdms  ](/cdms.html) .cdurllib 
[ index ](/)  

` Customized [ URLopener ](/urllib.html) `

  
 Modules 

` `

[ getpass ](/getpass.html)  
[ socket ](/socket.html)  

[ string ](/string.html)  
[ sys ](/sys.html)  

[ urllib ](/urllib.html)  

  
 Classes 

` `

[ urllib.URLopener ](/urllib.html)

    

[ CDURLopener ](/cdms.cdurllib.html)

  
class  CDURLopener  ( [ urllib.URLopener ](/urllib.html) )

` `

Methods defined here:  

 __init__  (self, proxies  =None  ) 

 open_ftp  (self, url) 
     ` #&#160;Use&#160;FTP&#160;protocol `

 retrieve  (self, url, filename  =None  , reporthook  =None  , blocksize  =262144  ) 

 setUserObject  (self, userObject) 
     ` #&#160;Attach&#160;an&#160;object&#160;to&#160;be&#160;returned&#160;with&#160;callbacks `

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

 http_error_default  (self, url, fp, errcode, errmsg, headers) 
     ` Default&#160;error&#160;handler:&#160;close&#160;the&#160;connection&#160;and&#160;raise&#160;IOError. `

 open  (self, fullurl, data  =None  ) 
     ` Use [ URLopener ](/urllib.html) (). [ open ](/) (file)&#160;instead&#160;of [ open ](/) (file,&#160;'r'). `

 open_data  (self, url, data  =None  ) 
     ` Use&#160;"data"&#160;URL. `

 open_file  (self, url) 
     ` Use&#160;local&#160;file&#160;or&#160;FTP&#160;depending&#160;on&#160;form&#160;of&#160;URL. `

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

* * *

Data and other attributes inherited from [ urllib.URLopener ](/urllib.html) :  

 version  = 'Python-urllib/1.16' 

  
 Functions 

` `

 sampleReportHook  (blocknum, blocksize, size, userObj) 

  
 Data 

` `

 MAXFTPCACHE  = 10 

* * *

UCRL-WEB-213937 | [ Privacy & Legal Notice ](/disclaimer.html)

[ webmaster@pcmdi.llnl.gov ](/webmaster@pcmdi.llnl.gov)

[ ![Powered by Plone](media/plone_powered.gif) ](/)

