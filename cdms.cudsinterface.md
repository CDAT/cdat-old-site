---
layout: default
title:
---

 [ Skip to content. ](/cdat/source/api-reference/cdms.cudsinterface.html) | [
Skip to navigation ](/cdat/source/api-reference/cdms.cudsinterface.html)

Search Site

[ Advanced Search&#8230; ](/search_form)

#  [ PCMDI Software Portal ](/)

#####  Sections

  * [ Home ](/)

#####  Personal tools

  * [ Log in ](/login_form)

You are here:  [ Home ](/) -> [ CDAT ](/cdat) -> [ Source Code ](/cdat/source)
-> [ API Reference ](/cdat/source/api-reference) -> Python: module
cdms.cudsinterface

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

        * [ Python: module cdms.cudsinterface ](/cdat/source/api-reference/cdms.cudsinterface.html)

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

  * [ ![Send this page to somebody](media/mail_icon.gif) ](/cdat/source/api-reference/cdms.cudsinterface.html/sendto_form)
  * [ ![Print this page](media/print_icon.gif) ](/this.print\(\))

#  Python: module cdms.cudsinterface

  
  
 [ cdms  ](/cdms.html) .cudsinterface 
[ index ](/)  

` Emulation&#160;of&#160;old&#160;cu&#160;package `

  
 Modules 

` `

[ MA ](/MA.html)  

[ string ](/string.html)  

[ sys ](/sys.html)  

[ types ](/types.html)  

  
 Classes 

` `

[ cuDataset ](/cdms.cudsinterface.html)

  
class  cuDataset 

` `

` A&#160;mixin&#160;class&#160;to&#160;support&#160;the&#160;old&#160;cu&#160;interface  
`

Methods defined here:  

 __call__  (self, id, *args, kwargs) 
     ` Call&#160;a&#160;variable&#160;object&#160;with&#160;the&#160;given&#160;id.&#160;Exception&#160;if&#160;not&#160;found.   
Call&#160;the&#160;variable&#160;with&#160;the&#160;other&#160;arguments. `

 __getitem__  (self, key) 
     ` Implement&#160;f['varname']&#160;for&#160;file/dataset&#160;f. `

 __init__  (self) 

 cleardefault  (self) 
     ` Clear&#160;the&#160;default&#160;variable&#160;name. `

 default_variable  (self, vname) 
     ` Set&#160;the&#160;default&#160;variable&#160;name. `

 dimensionarray  (self, dname, vname  =None  ) 
     ` Values&#160;of&#160;the&#160;dimension&#160;named&#160;dname. `

 dimensionobject  (self, dname, vname  =None  ) 
     ` CDMS&#160;axis&#160;object&#160;for&#160;the&#160;dimension&#160;named&#160;dname. `

 getattribute  (self, vname, attribute) 
     ` Get&#160;the&#160;value&#160;of&#160;attribute&#160;for&#160;variable&#160;vname `

 getdimensionunits  (self, dname, vname  =None  ) 
     ` Get&#160;the&#160;units&#160;for&#160;the&#160;given&#160;dimension. `

 getglobal  (self, attribute) 
     ` Get&#160;the&#160;value&#160;of&#160;the&#160;global&#160;attribute. `

 getslab  (self, vname, *args, keys) 
     ` [ getslab ](/) ('name',&#160;arg1,&#160;arg2,&#160;....)&#160;returns&#160;a&#160;cdms&#160;variable   
containing&#160;the&#160;data.  
  
Arguments&#160;for&#160;each&#160;dimension&#160;can&#160;be:  
(1)&#160;:&#160;or&#160;None&#160;\--&#160;selected&#160;entire&#160;dimension  
(2)&#160;Ellipsis&#160;\--&#160;select&#160;entire&#160;dimensions&#160;between&#160;the&#160;ones&#160;given.  
(3)&#160;a&#160;pair&#160;of&#160;successive&#160;arguments&#160;giving&#160;an&#160;interval&#160;in  
world&#160;coordinates.  
(4)&#160;a&#160;cdms-style&#160;tuple&#160;of&#160;world&#160;coordinates&#160;e.g.&#160;(start,&#160;stop,&#160;'cc') `

 listall  (self, vname  =None  , all  =None  ) 
     ` Get&#160;info&#160;about&#160;data&#160;from&#160;the&#160;file. `

 listattribute  (self, vname  =None  ) 
     ` Get&#160;attributes&#160;of&#160;data&#160;from&#160;the&#160;file. `

 listdimension  (self, vname  =None  ) 
     ` Return&#160;a&#160;list&#160;of&#160;the&#160;dimension&#160;names&#160;associated&#160;with&#160;a&#160;variable.   
If&#160;no&#160;argument,&#160;return&#160;the&#160;file.axes.keys() `

 listglobal  (self) 
     ` Returns&#160;a&#160;list&#160;of&#160;the&#160;global&#160;attributes&#160;in&#160;the&#160;file. `

 listvariable  (self) 
     ` Return&#160;a&#160;list&#160;of&#160;the&#160;variables&#160;in&#160;the&#160;file. `

 listvariables  = [ listvariable ](/) (self) 

 readScripGrid  (self, whichGrid  ='destination'  , checkGrid  =1  ) 
     ` Read&#160;a&#160;SCRIP&#160;curvilinear&#160;or&#160;generic&#160;grid&#160;from&#160;the&#160;dataset.   
The&#160;dataset&#160;can&#160;be&#160;a&#160;SCRIP&#160;grid&#160;file&#160;or&#160;mapping&#160;file.&#160;If&#160;a&#160;mapping&#160;file,  
'whichGrid'&#160;chooses&#160;the&#160;grid&#160;to&#160;read,&#160;either&#160;"source"&#160;or&#160;"destination".  
If&#160;'checkGrid'&#160;is&#160;1&#160;(default),&#160;the&#160;grid&#160;cells&#160;are&#160;checked&#160;for&#160;convexity,  
and&#160;'repaired'&#160;if&#160;necessary.  
Returns&#160;the&#160;grid&#160;object. `

 showall  (self, vname  =None  , all  =None  , device  =None  ) 
     ` Show&#160;a&#160;full&#160;description&#160;of&#160;the&#160;variable. `

 showattribute  (self, vname  =None  , device  =None  ) 
     ` Show&#160;the&#160;attributes&#160;of&#160;vname. `

 showdimension  (self, vname  =None  , device  =None  ) 
     ` Show&#160;the&#160;dimension&#160;names&#160;associated&#160;with&#160;a&#160;variable. `

 showglobal  (self, device  =None  ) 
     ` Show&#160;the&#160;global&#160;attributes&#160;in&#160;the&#160;file. `

 showvariable  (self, device  =None  ) 
     ` Show&#160;the&#160;variables&#160;in&#160;the&#160;file. `

* * *

UCRL-WEB-213937 | [ Privacy & Legal Notice ](/disclaimer.html)

[ webmaster@pcmdi.llnl.gov ](/webmaster@pcmdi.llnl.gov)

[ ![Powered by Plone](media/plone_powered.gif) ](/)

