---
layout: default
title:
---

 [ Skip to content. ](/cdat/source/api-reference/cdms.cdmsobj.html) | [ Skip to
navigation ](/cdat/source/api-reference/cdms.cdmsobj.html)

Search Site

[ Advanced Search&#8230; ](/search_form)

#  [ PCMDI Software Portal ](/)

#####  Sections

  * [ Home ](/)

#####  Personal tools

  * [ Log in ](/login_form)

You are here:  [ Home ](/) -> [ CDAT ](/cdat) -> [ Source Code ](/cdat/source)
-> [ API Reference ](/cdat/source/api-reference) -> Python: module
cdms.cdmsobj

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

        * [ Python: module cdms.cdmsobj ](/cdat/source/api-reference/cdms.cdmsobj.html)

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

  * [ ![Send this page to somebody](media/mail_icon.gif) ](/cdat/source/api-reference/cdms.cdmsobj.html/sendto_form)
  * [ ![Print this page](media/print_icon.gif) ](/this.print\(\))

#  Python: module cdms.cdmsobj

  
  
 [ cdms  ](/cdms.html) .cdmsobj 
[ index ](/)  

` CDMS&#160;module-level&#160;functions&#160;and&#160;definitions `

  
 Modules 

` `

[ cdms.cdmsNode ](/cdms.cdmsNode.html)  
[ cdtime ](/cdtime.html)  
[ glob ](/glob.html)  

[ cdms.internattr ](/cdms.internattr.html)  
[ os ](/os.html)  
[ re ](/re.html)  

[ string ](/string.html)  
[ sys ](/sys.html)  
[ types ](/types.html)  

  
 Classes 

` `

[ cdms.internattr.InternalAttributesClass ](/cdms.internattr.html) ( [
PropertiedClasses.Properties.PropertiedClass
](/PropertiedClasses.Properties.html) )

    

[ CdmsObj ](/cdms.cdmsobj.html)

  
class  CdmsObj  ( [ cdms.internattr.InternalAttributesClass
](/cdms.internattr.html) )

` `

` #&#160;Generic&#160;CDMS&#160;object&#160;has&#160;a&#160;tree&#160;node,&#160;attributes  
`

Method resolution order:

     [ CdmsObj ](/cdms.cdmsobj.html)
     [ cdms.internattr.InternalAttributesClass ](/cdms.internattr.html)
     [ PropertiedClasses.Properties.PropertiedClass ](/PropertiedClasses.Properties.html)

* * *

Methods defined here:  

 __init__  (self, node  =None  ) 

 dump  (self, path  =None  , format  =1  ) 
     ` [ dump ](/) (self,path=None,format=1)   
Dump&#160;an&#160;XML&#160;representation&#160;of&#160;this&#160;object&#160;to&#160;a&#160;file.  
'path'&#160;is&#160;the&#160;result&#160;file&#160;name,&#160;None&#160;for&#160;standard&#160;output.  
'format'==1&#160;iff&#160;the&#160;file&#160;is&#160;formatted&#160;with&#160;newlines&#160;for&#160;readability `

 matchPattern  (self, pattern, attribute, tag) 
     ` #&#160;Match&#160;a&#160;pattern&#160;in&#160;a&#160;string-valued&#160;attribute.&#160;If&#160;attribute&#160;is&#160;None,   
#&#160;search&#160;all&#160;string&#160;attributes.&#160;If&#160;tag&#160;is&#160;not&#160;None,&#160;it&#160;must&#160;match&#160;the&#160;internal
node&#160;tag. `

 matchone  (self, pattern, attname) 
     ` #&#160;Return&#160;true&#160;iff&#160;the&#160;attribute&#160;with&#160;name&#160;attname&#160;is&#160;a&#160;string   
#&#160;attribute&#160;which&#160;matches&#160;the&#160;compiled&#160;regular&#160;expression&#160;pattern,&#160;or  
#&#160;if&#160;attname&#160;is&#160;None&#160;and&#160;pattern&#160;matches&#160;at&#160;least&#160;one&#160;string  
#&#160;attribute.&#160;Return&#160;false&#160;if&#160;the&#160;attribute&#160;is&#160;not&#160;found&#160;or&#160;is&#160;not&#160;a&#160;string `

 searchPattern  (self, pattern, attribute, tag) 
     ` #&#160;Search&#160;for&#160;a&#160;pattern&#160;in&#160;a&#160;string-valued&#160;attribute.&#160;If&#160;attribute&#160;is&#160;None,   
#&#160;search&#160;all&#160;string&#160;attributes.&#160;If&#160;tag&#160;is&#160;not&#160;None,&#160;it&#160;must&#160;match&#160;the&#160;internal
node&#160;tag. `

 searchPredicate  (self, predicate, tag) 
     ` #&#160;Apply&#160;a&#160;truth-valued&#160;predicate.&#160;Return&#160;a&#160;list&#160;containing&#160;a&#160;single&#160;instance:&#160;[self]   
#&#160;if&#160;the&#160;predicate&#160;is&#160;true&#160;and&#160;either&#160;tag&#160;is&#160;None&#160;or&#160;matches&#160;the&#160;object&#160;node
tag.  
#&#160;If&#160;the&#160;predicate&#160;returns&#160;false,&#160;return&#160;an&#160;empty&#160;list `

 searchone  (self, pattern, attname) 
     ` Return&#160;true&#160;iff&#160;the&#160;attribute&#160;with&#160;name&#160;attname&#160;is&#160;a&#160;string   
attribute&#160;which&#160;contains&#160;the&#160;compiled&#160;regular&#160;expression&#160;pattern,&#160;or  
if&#160;attname&#160;is&#160;None&#160;and&#160;pattern&#160;matches&#160;at&#160;least&#160;one&#160;string  
attribute.&#160;Return&#160;false&#160;if&#160;the&#160;attribute&#160;is&#160;not&#160;found&#160;or&#160;is&#160;not  
a&#160;string. `

* * *

Methods inherited from [ cdms.internattr.InternalAttributesClass
](/cdms.internattr.html) :  

 is_internal_attribute  (self, name) 
     ` [ is_internal_attribute ](/) (name)&#160;is&#160;true&#160;if&#160;name&#160;is&#160;internal. `

 replace_external_attributes  (self, newAttributes) 
     ` [ replace_external_attributes ](/) (newAttributes)   
Replace&#160;the&#160;external&#160;attributes&#160;with&#160;dictionary&#160;newAttributes. `

* * *

Methods inherited from [ PropertiedClasses.Properties.PropertiedClass
](/PropertiedClasses.Properties.html) :  

 __delattr__  (self, name) 

 __getattr__  (self, name) 

 __setattr__  (self, name, value) 

 get_property_d  (self, name) 
     ` Return&#160;the&#160;'del'&#160;property&#160;handler&#160;for&#160;name&#160;that&#160;self&#160;uses.   
Returns&#160;None&#160;if&#160;no&#160;handler. `

 get_property_g  (self, name) 
     ` Return&#160;the&#160;'get'&#160;property&#160;handler&#160;for&#160;name&#160;that&#160;self&#160;uses.   
Returns&#160;None&#160;if&#160;no&#160;handler. `

 get_property_s  (self, name) 
     ` Return&#160;the&#160;'set'&#160;property&#160;handler&#160;for&#160;name&#160;that&#160;self&#160;uses.   
Returns&#160;None&#160;if&#160;no&#160;handler. `

 set_property  (self, name, actg  =None  , acts  =None  , actd  =None  , nowrite  =None  , nodelete  =None  ) 
     ` Set&#160;attribute&#160;handlers&#160;for&#160;&#160;name&#160;to&#160;methods&#160;actg,&#160;acts,&#160;actd   
None&#160;means&#160;no&#160;change&#160;for&#160;that&#160;action.  
nowrite&#160;=&#160;1&#160;prevents&#160;setting&#160;this&#160;attribute.  
nowrite&#160;defaults&#160;to&#160;0\.  
nodelete&#160;=&#160;1&#160;prevents&#160;deleting&#160;this&#160;attribute.  
nodelete&#160;defaults&#160;to&#160;1&#160;unless&#160;actd&#160;given.  
if&#160;nowrite&#160;and&#160;nodelete&#160;is&#160;None:&#160;nodelete&#160;=&#160;1 `

  
 Functions 

` `

 generateTime  (matchobj, timespecs) 
     ` #&#160;Generate&#160;a&#160;component&#160;time&#160;from&#160;a&#160;matchobj&#160;and&#160;list&#160;of&#160;specs `

 getPathFromTemplate  (template, matchnames) 
     ` #&#160;Generate&#160;a&#160;file&#160;path,&#160;given&#160;a&#160;template&#160;and&#160;matchname&#160;list.   
#&#160;matchnames&#160;is&#160;a&#160;list&#160;[varname,time,etime,level,elevel],&#160;where  
#&#160;any&#160;or&#160;all&#160;elems&#160;may&#160;be&#160;None `

 getTimeAsString  (spec, time) 
     ` #&#160;Get&#160;a&#160;string&#160;time&#160;component&#160;from&#160;a&#160;spec&#160;and&#160;a&#160;component&#160;time `

 matchPattern  (objlist, pattern, attribute  =None  , tag  =None  ) 

 matchingFiles  (direc, template) 
     ` #&#160;Find&#160;all&#160;files&#160;in&#160;'direc'&#160;which&#160;match&#160;'template'.   
#&#160;template&#160;is&#160;a&#160;relative&#160;path,&#160;and&#160;may&#160;contain&#160;specifiers  
#&#160;in&#160;directory&#160;names.&#160;Returns&#160;a&#160;list&#160;[(f,m),..,(f,m)]&#160;where  
#&#160;f&#160;is&#160;a&#160;matching&#160;file&#160;name,&#160;and&#160;m&#160;is&#160;a&#160;list&#160;[var,time,etime,level,elevel]  
#&#160;of&#160;matching&#160;values&#160;in&#160;f.&#160;Any&#160;or&#160;all&#160;elems&#160;of&#160;the&#160;list&#160;may&#160;be&#160;None. `

 retglob  (matchobj) 

 searchPattern  (objlist, pattern, attribute  =None  , tag  =None  ) 

 searchPredicate  (objlist, predicate, tag  =None  ) 

 setDebugMode  (mode) 
     ` #&#160;Set&#160;debug&#160;mode,&#160;to&#160;'on'&#160;or&#160;'off' `

 templateToRegex  (template) 
     ` #&#160;Map&#160;a&#160;template&#160;to&#160;a&#160;regular&#160;expression   
#&#160;Returns&#160;(regex,dimtypes),&#160;where&#160;regex&#160;is&#160;the&#160;regular&#160;expression  
#&#160;corresponding&#160;to&#160;template,&#160;and&#160;dimtypes&#160;is&#160;a&#160;dictionary  
#&#160;such&#160;that&#160;dimtypes[dimtype]&#160;=&#160;specStrings  
#&#160;where&#160;specStrings&#160;is&#160;the&#160;specifier&#160;associated&#160;with&#160;the&#160;dimension&#160;type,  
#&#160;or&#160;for&#160;time,&#160;the&#160;list&#160;of&#160;specifiers&#160;in&#160;the&#160;order&#160;(yr,mo,dy,hr,mi,se)  
#&#160;where&#160;each&#160;element&#160;is&#160;the&#160;specifier&#160;for&#160;that&#160;time&#160;element `

  
 Data 

` `

 AbsoluteTemplate  = 'Template must be a relative path: '   
 CdArray  = 'Array'   
 CdByte  = 'Byte'   
 CdChar  = 'Char'   
 CdDouble  = 'Double'   
 CdFloat  = 'Float'   
 CdFromObject  = 'FromObject'   
 CdInt  = 'Int'   
 CdLong  = 'Long'   
 CdScalar  = 'Scalar'   
 CdShort  = 'Short'   
 CdString  = 'String'   
 Unlimited  = 1 

* * *

UCRL-WEB-213937 | [ Privacy & Legal Notice ](/disclaimer.html)

[ webmaster@pcmdi.llnl.gov ](/webmaster@pcmdi.llnl.gov)

[ ![Powered by Plone](media/plone_powered.gif) ](/)

