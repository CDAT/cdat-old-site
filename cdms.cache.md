---
layout: default
title:
---

 [ Skip to content. ](/cdat/source/api-reference/cdms.cache.html) | [ Skip to
navigation ](/cdat/source/api-reference/cdms.cache.html)

Search Site

[ Advanced Search&#8230; ](/search_form)

#  [ PCMDI Software Portal ](/)

#####  Sections

  * [ Home ](/)

#####  Personal tools

  * [ Log in ](/login_form)

You are here:  [ Home ](/) -> [ CDAT ](/cdat) -> [ Source Code ](/cdat/source)
-> [ API Reference ](/cdat/source/api-reference) -> Python: module cdms.cache

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

        * [ Python: module cdms.cache ](/cdat/source/api-reference/cdms.cache.html)

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

  * [ ![Send this page to somebody](media/mail_icon.gif) ](/cdat/source/api-reference/cdms.cache.html/sendto_form)
  * [ ![Print this page](media/print_icon.gif) ](/this.print\(\))

#  Python: module cdms.cache

  
  
 [ cdms  ](/cdms.html) .cache 
[ index ](/)  

` CDMS&#160;cache&#160;management&#160;and&#160;file&#160;movement&#160;objects `

  
 Modules 

` `

[ cdms.cdmsobj ](/cdms.cdmsobj.html)  
[ cdms.cdurllib ](/cdms.cdurllib.html)  
[ errno ](/errno.html)  

[ os ](/os.html)  
[ shelve ](/shelve.html)  
[ sys ](/sys.html)  

[ tempfile ](/tempfile.html)  
[ time ](/time.html)  
[ urlparse ](/urlparse.html)  

  
 Classes 

` `

[ Cache ](/cdms.cache.html)

  
class  Cache 

` `

` #&#160;A&#160;simple&#160;data&#160;cache  
`

Methods defined here:  

 __init__  (self) 

 clean  (self) 
     ` Clean&#160;pending&#160;read&#160;notifications. `

 copyFile  (self, fromURL, filekey, lcpath  =None  , userid  =None  , useReplica  =None  ) 
     ` Copy&#160;the&#160;file&#160;<fromURL>&#160;into&#160;the&#160;cache.&#160;Return&#160;the&#160;result&#160;path.   
  
For&#160;request&#160;manager&#160;transfers,&#160;lcpath&#160;is&#160;the&#160;logical&#160;collection&#160;path,  
<userid>&#160;is&#160;the&#160;string&#160;user&#160;ID,&#160;<useReplica>&#160;is&#160;true&#160;iff&#160;the&#160;request&#160;manager
should  
search&#160;the&#160;replica&#160;catalog&#160;for&#160;the&#160;actual&#160;file&#160;to&#160;transfer. `

 delete  (self) 
     ` Delete&#160;the&#160;cache. `

 deleteEntry  (self, filekey) 
     ` Delete&#160;a&#160;cache&#160;index&#160;entry. `

 get  (self, filekey) 
     ` Get&#160;the&#160;path&#160;associated&#160;with&#160;<filekey>,&#160;or&#160;None&#160;if&#160;not&#160;present. `

 getFile  (self, fromURL, filekey, naptime  =5  , maxtries  =60  , lcpath  =None  , userid  =None  , useReplica  =None  ) 
     ` Get&#160;the&#160;file&#160;with&#160;<fileURL>.&#160;If&#160;the&#160;file&#160;is&#160;in&#160;the&#160;cache,&#160;read&#160;it.   
If&#160;another&#160;process&#160;is&#160;transferring&#160;it&#160;into&#160;the&#160;cache,&#160;wait&#160;for&#160;the  
transfer&#160;to&#160;complete.&#160;<naptime>&#160;is&#160;the&#160;number&#160;of&#160;seconds&#160;between  
retries,&#160;<maxtries>&#160;is&#160;the&#160;maximum&#160;number&#160;of&#160;retries.  
Otherwise,&#160;copy&#160;it&#160;from&#160;the&#160;remote&#160;file.  
  
<filekey>&#160;is&#160;the&#160;cache&#160;index&#160;key.&#160;A&#160;good&#160;choice&#160;is&#160;(datasetDN,&#160;filename)  
where&#160;datasetDN&#160;is&#160;the&#160;distinguished&#160;name&#160;of&#160;the&#160;dataset,&#160;and&#160;filename  
is&#160;the&#160;name&#160;of&#160;the&#160;file&#160;within&#160;the&#160;dataset.  
  
For&#160;request&#160;manager&#160;transfers,&#160;<lcpath>&#160;is&#160;the&#160;logical&#160;collection&#160;path,  
<userid>&#160;is&#160;the&#160;user&#160;string&#160;ID,&#160;<useReplica>&#160;is&#160;true&#160;iff&#160;the&#160;request&#160;manager
should  
search&#160;the&#160;replica&#160;catalog&#160;for&#160;the&#160;actual&#160;file&#160;to&#160;transfer.  
  
Returns&#160;the&#160;path&#160;of&#160;a&#160;file&#160;in&#160;the&#160;cache.  
  
Note:&#160;The&#160;function&#160;does&#160;not&#160;guarantee&#160;that&#160;the&#160;file&#160;is&#160;still&#160;in&#160;the&#160;cache  
by&#160;the&#160;time&#160;it&#160;returns. `

 put  (self, filekey, path) 
     ` cache[filekey]&#160;=&#160;path `

* * *

Data and other attributes defined here:  

 indexpath  = None 

  
 Functions 

` `

 copyFile  (fromURL, toURL, callback  =None  , lcpath  =None  , userid  =None  , useReplica  =1  ) 
     ` Copy&#160;file&#160;<fromURL>&#160;to&#160;local&#160;file&#160;<toURL>.&#160;For&#160;FTP&#160;transfers,&#160;if&#160;cache._useWindow&#160;is&#160;true,   
display&#160;a&#160;progress&#160;dialog,&#160;otherwise&#160;just&#160;print&#160;progress&#160;messages.  
  
For&#160;request&#160;manager&#160;transfers,&#160;<lcpath>&#160;is&#160;the&#160;logical&#160;collection
distinguished&#160;name,  
<userid>&#160;is&#160;the&#160;string&#160;user&#160;ID,&#160;<useReplica>&#160;is&#160;true&#160;iff&#160;the&#160;request&#160;manager
should  
search&#160;the&#160;replica&#160;catalog&#160;for&#160;the&#160;actual&#160;file&#160;to&#160;transfer. `

 lock  (filename) 
     ` Acquire&#160;a&#160;file-based&#160;lock&#160;with&#160;the&#160;given&#160;name.   
Usage: [ lock ](/) (filename)  
If&#160;the&#160;function&#160;returns,&#160;the&#160;lock&#160;was&#160;acquired&#160;successfully.  
Note:&#160;This&#160;function&#160;is&#160;UNIX-specific.  
Note:&#160;It&#160;is&#160;important&#160;to&#160;delete&#160;the&#160;lock&#160;via [ unlock ](/) ()&#160;if&#160;the&#160;process  
is&#160;interrupted,&#160;otherwise&#160;subsequent&#160;locks&#160;will&#160;fail. `

 lockpath  (filename) 
     ` Generate&#160;the&#160;pathname&#160;of&#160;a&#160;lock.&#160;Creates&#160;the&#160;directory&#160;containing&#160;the&#160;lock   
if&#160;necessary.  
Usage: [ lockpath ](/) (filename) `

 unlock  (filename) 
     ` Delete&#160;a&#160;file-based&#160;lock&#160;with&#160;the&#160;given&#160;name.   
Usage: [ unlock ](/) (filename)  
If&#160;the&#160;function&#160;returns,&#160;the&#160;lock&#160;was&#160;successfully&#160;deleted.  
Note:&#160;This&#160;function&#160;is&#160;UNIX-specific. `

 useGlobusTransfer  () 
     ` Specify&#160;that&#160;file&#160;transfers&#160;should&#160;use&#160;the&#160;Globus&#160;storage&#160;API&#160;(SC-API).&#160;See&#160;usePythonTransfer. `

 usePythonTransfer  () 
     ` Specify&#160;that&#160;file&#160;transfers&#160;should&#160;use&#160;the&#160;Python&#160;libraries&#160;urllib,&#160;ftplib.&#160;See&#160;useGlobusTransfer. `

 useRequestManagerTransfer  () 

 useTTY  () 
     ` Informational&#160;messages&#160;such&#160;as&#160;FTP&#160;status&#160;should&#160;be&#160;sent&#160;to&#160;the&#160;terminal.&#160;See&#160;useWindow. `

 useWindow  () 
     ` Specify&#160;that&#160;dialog&#160;windows&#160;should&#160;be&#160;used&#160;if&#160;possible.&#160;Do&#160;not&#160;call&#160;this&#160;directly,&#160;use   
gui.setProgressParent&#160;instead.&#160;See&#160;useTTY. `

  
 Data 

` `

 GlobusNotSupported  = 'Globus interface not supported'   
 LockError  = 'Lock error:'   
 MethodNotImplemented  = 'Method not yet implemented'   
 RequestManagerNotSupported  = 'Request manager interface not supported (module reqm not found)'   
 SchemeNotSupported  = 'Scheme not supported: '   
 TimeOutError  = 'Wait for read completion timed out:' 

* * *

UCRL-WEB-213937 | [ Privacy & Legal Notice ](/disclaimer.html)

[ webmaster@pcmdi.llnl.gov ](/webmaster@pcmdi.llnl.gov)

[ ![Powered by Plone](media/plone_powered.gif) ](/)

