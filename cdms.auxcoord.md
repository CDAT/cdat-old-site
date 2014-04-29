---
layout: default
title:
---

 [ Skip to content. ](/cdat/source/api-reference/cdms.auxcoord.html) | [ Skip
to navigation ](/cdat/source/api-reference/cdms.auxcoord.html)

Search Site

[ Advanced Search&#8230; ](/search_form)

#  [ PCMDI Software Portal ](/)

#####  Sections

  * [ Home ](/)

#####  Personal tools

  * [ Log in ](/login_form)

You are here:  [ Home ](/) -> [ CDAT ](/cdat) -> [ Source Code ](/cdat/source)
-> [ API Reference ](/cdat/source/api-reference) -> Python: module
cdms.auxcoord

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

        * [ Python: module cdms.auxcoord ](/cdat/source/api-reference/cdms.auxcoord.html)

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

  * [ ![Send this page to somebody](media/mail_icon.gif) ](/cdat/source/api-reference/cdms.auxcoord.html/sendto_form)
  * [ ![Print this page](media/print_icon.gif) ](/this.print\(\))

#  Python: module cdms.auxcoord

  
  
 [ cdms  ](/cdms.html) .auxcoord 
[ index ](/)  

` CDMS&#160;1-D&#160;auxiliary&#160;coordinates.  
  
Note:&#160;In&#160;contrast&#160;to&#160;Axis&#160;objects&#160;(concrete&#160;classes&#160;subclassed&#160;from
AbstractAxis),&#160;auxiliary&#160;coordinate&#160;variables&#160;are&#160;not&#160;monotonic&#160;in&#160;value,&#160;and
do&#160;not&#160;share&#160;a&#160;name&#160;with&#160;the&#160;dimension. `

  
 Modules 

` `

[ cdms.internattr ](/cdms.internattr.html)  

  
 Classes 

` `

[ cdms.coord.AbstractCoordinateAxis ](/cdms.coord.html) ( [
cdms.cdmsobj.CdmsObj ](/cdms.cdmsobj.html) )

    

[ AbstractAuxAxis1D ](/cdms.auxcoord.html)

    

[ DatasetAuxAxis1D ](/cdms.auxcoord.html) ( [ AbstractAuxAxis1D
](/cdms.auxcoord.html) , [ cdms.variable.DatasetVariable
](/cdms.variable.html) )

[ FileAuxAxis1D ](/cdms.auxcoord.html) ( [ AbstractAuxAxis1D
](/cdms.auxcoord.html) , [ cdms.fvariable.FileVariable ](/cdms.fvariable.html)
)

[ TransientAuxAxis1D ](/cdms.auxcoord.html) ( [ AbstractAuxAxis1D
](/cdms.auxcoord.html) , [ cdms.tvariable.TransientVariable
](/cdms.tvariable.html) )

  
class  AbstractAuxAxis1D  ( [ cdms.coord.AbstractCoordinateAxis
](/cdms.coord.html) )

` `

Method resolution order:

     [ AbstractAuxAxis1D ](/cdms.auxcoord.html)
     [ cdms.coord.AbstractCoordinateAxis ](/cdms.coord.html)
     [ cdms.cdmsobj.CdmsObj ](/cdms.cdmsobj.html)
     [ cdms.internattr.InternalAttributesClass ](/cdms.internattr.html)
     [ PropertiedClasses.Properties.PropertiedClass ](/PropertiedClasses.Properties.html)

* * *

Methods defined here:  

 __init__  (self, parent  =None  , variableNode  =None  , bounds  =None  ) 

 clone  (self, copyData  =1  ) 
     ` clone&#160;(self,&#160;copyData=1)   
Return&#160;a&#160;copy&#160;of&#160;self&#160;as&#160;a&#160;transient&#160;axis.  
If&#160;copyData&#160;is&#160;1,&#160;make&#160;a&#160;separate&#160;copy&#160;of&#160;the&#160;data. `

 setBounds  (self, bounds) 

 subSlice  (self, *specs, keys) 

* * *

Methods inherited from [ cdms.coord.AbstractCoordinateAxis ](/cdms.coord.html)
:  

 designateLatitude  (self, persistent  =0  ) 
     ` #&#160;Designate&#160;axis&#160;as&#160;a&#160;latitude&#160;axis.   
#&#160;If&#160;persistent&#160;is&#160;true,&#160;write&#160;metadata&#160;to&#160;the&#160;container. `

 designateLevel  (self, persistent  =0  ) 
     ` #&#160;Designate&#160;axis&#160;as&#160;a&#160;vertical&#160;level&#160;axis   
#&#160;If&#160;persistent&#160;is&#160;true,&#160;write&#160;metadata&#160;to&#160;the&#160;container. `

 designateLongitude  (self, persistent  =0  ) 
     ` #&#160;Designate&#160;axis&#160;as&#160;a&#160;longitude&#160;axis   
#&#160;If&#160;persistent&#160;is&#160;true,&#160;write&#160;metadata&#160;to&#160;the&#160;container. `

 designateTime  (self, persistent  =0  , calendar  =4369  ) 
     ` #&#160;Designate&#160;axis&#160;as&#160;a&#160;time&#160;axis,&#160;and&#160;optionally&#160;set&#160;the&#160;calendar   
#&#160;If&#160;persistent&#160;is&#160;true,&#160;write&#160;metadata&#160;to&#160;the&#160;container. `

 getBounds  (self) 

 getCalendar  (self) 
     ` #&#160;Return&#160;the&#160;cdtime&#160;calendar:&#160;GregorianCalendar,&#160;NoLeapCalendar,&#160;JulianCalendar,&#160;Calendar360   
#&#160;or&#160;None.&#160;If&#160;the&#160;axis&#160;does&#160;not&#160;have&#160;a&#160;calendar&#160;attribute,&#160;return&#160;the&#160;global  
#&#160;calendar. `

 getData  (self) 

 getExplicitBounds  (self) 
     ` #&#160;Return&#160;None&#160;if&#160;not&#160;explicitly&#160;defined `

 info  (self, flag  =None  , device  =None  ) 
     ` Write&#160;info&#160;about&#160;axis;&#160;include&#160;dimension&#160;values&#160;and&#160;weights&#160;if&#160;flag `

 isAbstractCoordinate  (self) 

 isLatitude  (self) 
     ` #&#160;Return&#160;true&#160;iff&#160;the&#160;axis&#160;is&#160;a&#160;latitude&#160;axis `

 isLevel  (self) 
     ` #&#160;Return&#160;true&#160;iff&#160;the&#160;axis&#160;is&#160;a&#160;level&#160;axis `

 isLongitude  (self) 
     ` #&#160;Return&#160;true&#160;iff&#160;the&#160;axis&#160;is&#160;a&#160;longitude&#160;axis `

 isTime  (self) 
     ` #&#160;Return&#160;true&#160;iff&#160;the&#160;axis&#160;is&#160;a&#160;time&#160;axis `

 listall  (self, all  =None  ) 
     ` Get&#160;list&#160;of&#160;info&#160;about&#160;this&#160;axis. `

 setCalendar  (self, calendar, persistent  =1  ) 
     ` #&#160;Set&#160;the&#160;calendar `

 size  (self, axis  =None  ) 
     ` Number&#160;of&#160;elements&#160;in&#160;array,&#160;or&#160;in&#160;a&#160;particular&#160;axis. `

 writeToFile  (self, file) 

* * *

Data and other attributes inherited from [ cdms.coord.AbstractCoordinateAxis
](/cdms.coord.html) :  

 axis_count  = 0 

* * *

Methods inherited from [ cdms.cdmsobj.CdmsObj ](/cdms.cdmsobj.html) :  

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

  
class  DatasetAuxAxis1D  ( [ AbstractAuxAxis1D ](/cdms.auxcoord.html) , [
cdms.variable.DatasetVariable ](/cdms.variable.html) )

` `

Method resolution order:

     [ DatasetAuxAxis1D ](/cdms.auxcoord.html)
     [ AbstractAuxAxis1D ](/cdms.auxcoord.html)
     [ cdms.coord.AbstractCoordinateAxis ](/cdms.coord.html)
     [ cdms.cdmsobj.CdmsObj ](/cdms.cdmsobj.html)
     [ cdms.internattr.InternalAttributesClass ](/cdms.internattr.html)
     [ PropertiedClasses.Properties.PropertiedClass ](/PropertiedClasses.Properties.html)
     [ cdms.variable.DatasetVariable ](/cdms.variable.html)
     [ cdms.avariable.AbstractVariable ](/cdms.avariable.html)
     [ cdms.slabinterface.Slab ](/cdms.slabinterface.html)

* * *

Methods defined here:  

 __init__  (self, parent, id  =None  , variableNode  =None  , bounds  =None  ) 
     ` #&#160;Note:&#160;node&#160;is&#160;a&#160;VariableNode `

 __repr__  (self) 

* * *

Methods inherited from [ AbstractAuxAxis1D ](/cdms.auxcoord.html) :  

 clone  (self, copyData  =1  ) 
     ` clone&#160;(self,&#160;copyData=1)   
Return&#160;a&#160;copy&#160;of&#160;self&#160;as&#160;a&#160;transient&#160;axis.  
If&#160;copyData&#160;is&#160;1,&#160;make&#160;a&#160;separate&#160;copy&#160;of&#160;the&#160;data. `

 setBounds  (self, bounds) 

 subSlice  (self, *specs, keys) 

* * *

Methods inherited from [ cdms.coord.AbstractCoordinateAxis ](/cdms.coord.html)
:  

 designateLatitude  (self, persistent  =0  ) 
     ` #&#160;Designate&#160;axis&#160;as&#160;a&#160;latitude&#160;axis.   
#&#160;If&#160;persistent&#160;is&#160;true,&#160;write&#160;metadata&#160;to&#160;the&#160;container. `

 designateLevel  (self, persistent  =0  ) 
     ` #&#160;Designate&#160;axis&#160;as&#160;a&#160;vertical&#160;level&#160;axis   
#&#160;If&#160;persistent&#160;is&#160;true,&#160;write&#160;metadata&#160;to&#160;the&#160;container. `

 designateLongitude  (self, persistent  =0  ) 
     ` #&#160;Designate&#160;axis&#160;as&#160;a&#160;longitude&#160;axis   
#&#160;If&#160;persistent&#160;is&#160;true,&#160;write&#160;metadata&#160;to&#160;the&#160;container. `

 designateTime  (self, persistent  =0  , calendar  =4369  ) 
     ` #&#160;Designate&#160;axis&#160;as&#160;a&#160;time&#160;axis,&#160;and&#160;optionally&#160;set&#160;the&#160;calendar   
#&#160;If&#160;persistent&#160;is&#160;true,&#160;write&#160;metadata&#160;to&#160;the&#160;container. `

 getBounds  (self) 

 getCalendar  (self) 
     ` #&#160;Return&#160;the&#160;cdtime&#160;calendar:&#160;GregorianCalendar,&#160;NoLeapCalendar,&#160;JulianCalendar,&#160;Calendar360   
#&#160;or&#160;None.&#160;If&#160;the&#160;axis&#160;does&#160;not&#160;have&#160;a&#160;calendar&#160;attribute,&#160;return&#160;the&#160;global  
#&#160;calendar. `

 getData  (self) 

 getExplicitBounds  (self) 
     ` #&#160;Return&#160;None&#160;if&#160;not&#160;explicitly&#160;defined `

 info  (self, flag  =None  , device  =None  ) 
     ` Write&#160;info&#160;about&#160;axis;&#160;include&#160;dimension&#160;values&#160;and&#160;weights&#160;if&#160;flag `

 isAbstractCoordinate  (self) 

 isLatitude  (self) 
     ` #&#160;Return&#160;true&#160;iff&#160;the&#160;axis&#160;is&#160;a&#160;latitude&#160;axis `

 isLevel  (self) 
     ` #&#160;Return&#160;true&#160;iff&#160;the&#160;axis&#160;is&#160;a&#160;level&#160;axis `

 isLongitude  (self) 
     ` #&#160;Return&#160;true&#160;iff&#160;the&#160;axis&#160;is&#160;a&#160;longitude&#160;axis `

 isTime  (self) 
     ` #&#160;Return&#160;true&#160;iff&#160;the&#160;axis&#160;is&#160;a&#160;time&#160;axis `

 listall  (self, all  =None  ) 
     ` Get&#160;list&#160;of&#160;info&#160;about&#160;this&#160;axis. `

 setCalendar  (self, calendar, persistent  =1  ) 
     ` #&#160;Set&#160;the&#160;calendar `

 size  (self, axis  =None  ) 
     ` Number&#160;of&#160;elements&#160;in&#160;array,&#160;or&#160;in&#160;a&#160;particular&#160;axis. `

 writeToFile  (self, file) 

* * *

Data and other attributes inherited from [ cdms.coord.AbstractCoordinateAxis
](/cdms.coord.html) :  

 axis_count  = 0 

* * *

Methods inherited from [ cdms.cdmsobj.CdmsObj ](/cdms.cdmsobj.html) :  

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

* * *

Methods inherited from [ cdms.variable.DatasetVariable ](/cdms.variable.html)
:  

 __getitem__  (self, key) 

 __getslice__  (self, low, high) 

 __len__  (self) 
     ` Length&#160;of&#160;first&#160;dimension `

 __setitem__  (self, index, value) 

 __setslice__  (self, low, high, value) 

 expertPaths  (self, slist) 
     ` [ expertPaths ](/) (self,&#160;slicelist)   
takes&#160;a&#160;list&#160;of&#160;slices,  
returns&#160;a&#160;3-tuple:&#160;(npart,&#160;dimensionlist,&#160;partitionSlices)&#160;where:  
npart&#160;is&#160;the&#160;number&#160;of&#160;partitioned&#160;dimensions:&#160;0,&#160;1,&#160;or&#160;2;  
dimensionlist&#160;is&#160;a&#160;tuple&#160;of&#160;length&#160;npart,&#160;having&#160;the&#160;dimension  
numbers&#160;of&#160;the&#160;partitioned&#160;dimensions;  
partitionSlices&#160;is&#160;the&#160;list&#160;of&#160;file-specific&#160;(filename,&#160;slice)  
corresponding&#160;to&#160;the&#160;paths&#160;and&#160;slices&#160;within&#160;the&#160;files&#160;to&#160;be&#160;read.  
The&#160;exact&#160;form&#160;of&#160;partitionSlices&#160;depends&#160;on&#160;the&#160;value&#160;of&#160;npart:  
npart&#160;&#160;&#160;&#160;&#160;partitionSlices  
0&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;(filename,slicelist)  
1&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;[(filename,slicelist),...,(filename,slicelist)]  
2&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;[[(filename,slicelist),...,(filename,slicelist)]  
[(filename,slicelist),...,(filename,slicelist)]  
...  
[(filename,slicelist),...,(filename,slicelist)]]  
  
Note:  
-&#160;A&#160;filename&#160;of&#160;None&#160;indicates&#160;that&#160;no&#160;file&#160;was&#160;found&#160;with&#160;data   
corresponding&#160;to&#160;the&#160;slicelist.  
-&#160;If&#160;partitionSlices&#160;is&#160;None,&#160;the&#160;slicelist&#160;does&#160;not&#160;intersect&#160;the&#160;domain.   
-&#160;An&#160;empty&#160;partitionSlices&#160;[]&#160;means&#160;that&#160;the&#160;variable&#160;is&#160;zero-dimensional. `

 expertSlice  (self, initslist) 

 genMatch  (self, axis, interval, matchnames) 
     ` Helper&#160;function&#160;for&#160;expertPaths.   
axis&#160;is&#160;a&#160;partitioned&#160;axis,&#160;either&#160;time&#160;or&#160;vertical&#160;level.  
interval&#160;is&#160;an&#160;index&#160;interval&#160;(istart,&#160;iend).  
matchnames&#160;is&#160;a&#160;partially&#160;filled&#160;list&#160;[id,&#160;timestart,&#160;timeend,&#160;levstart,
levend]  
If&#160;a&#160;filemap&#160;is&#160;used,&#160;matchnames&#160;has&#160;indices,&#160;otherwise&#160;has&#160;coordinates.  
  
Function&#160;modifies&#160;matchnames&#160;based&#160;on&#160;axis&#160;and&#160;interval,  
returns&#160;the&#160;modified&#160;matchnames&#160;tuple. `

 getAxis  (self, n) 

 getDomain  (self) 

 getFilePath  (self, matchnames, template) 
     ` Lookup&#160;or&#160;generate&#160;the&#160;file&#160;path,&#160;depending&#160;on&#160;whether&#160;a&#160;filemap   
or&#160;template&#160;is&#160;present. `

 getPaths  (self, *specs, keys) 
     ` #&#160;Get&#160;the&#160;paths&#160;associated&#160;with&#160;the&#160;interval&#160;region&#160;specified   
#&#160;by&#160;'intervals'.&#160;This&#160;incorporates&#160;most&#160;of&#160;the&#160;logic&#160;of&#160;__getitem__,  
#&#160;without&#160;actually&#160;reading&#160;the&#160;data.  
#  
#&#160;'specs'&#160;is&#160;a&#160;list&#160;of&#160;interval&#160;range&#160;specifications&#160;as&#160;defined  
#&#160;for&#160;getSlice.  
#  
#&#160;The&#160;function&#160;returns&#160;a&#160;list&#160;of&#160;tuples&#160;of&#160;the&#160;form&#160;(path,slicelist),  
#&#160;where&#160;path&#160;is&#160;the&#160;path&#160;of&#160;a&#160;file,&#160;and&#160;slicetuple&#160;is&#160;a&#160;tuple&#160;of  
#&#160;slices,&#160;of&#160;the&#160;same&#160;length&#160;as&#160;the&#160;rank&#160;of&#160;the&#160;variable,&#160;representing&#160;the  
#&#160;region&#160;of&#160;the&#160;variable&#160;which&#160;is&#160;contained&#160;in&#160;the&#160;file.&#160;The&#160;following  
#&#160;would&#160;retrieve&#160;the&#160;data&#160;for&#160;that&#160;file:  
#  
#&#160;&#160;&#160;f&#160;=&#160;Cdunif.CdunifFile(path,'r')  
#&#160;&#160;&#160;var&#160;=&#160;f.variables[self.  name_in_file  ]  
#&#160;&#160;&#160;data&#160;=&#160;apply(var.getitem,slicelist) `

 getShape  (self) 

 getTemplate  (self) 
     ` #&#160;Get&#160;the&#160;template `

 getValue  (self, squeeze  =1  ) 
     ` Return&#160;the&#160;entire&#160;set&#160;of&#160;values. `

 initDomain  (self, axisdict, griddict) 
     ` Must&#160;be&#160;called&#160;by&#160;whoever&#160;made&#160;this&#160;Variable&#160;to&#160;set&#160;up&#160;axes,&#160;grids. `

 typecode  (self) 

* * *

Methods inherited from [ cdms.avariable.AbstractVariable
](/cdms.avariable.html) :  

 __abs__  (self) 

 __add__  (self, other) 

 __array__  (self, t  =None  ) 

 __call__  (self, *args, kwargs) 
     ` Selection&#160;of&#160;a&#160;subregion&#160;using&#160;selectors `

 __div__  (self, other) 

 __eq__  (self, other) 

 __ge__  (self, other) 

 __gt__  (self, other) 

 __iadd__  (self, other) 
     ` Add&#160;other&#160;to&#160;self&#160;in&#160;place. `

 __idiv__  (self, other) 
     ` Divide&#160;self&#160;by&#160;other&#160;in&#160;place. `

 __imul__  (self, other) 
     ` Multiply&#160;self&#160;by&#160;other&#160;in&#160;place. `

 __isub__  (self, other) 
     ` Subtract&#160;other&#160;from&#160;self&#160;in&#160;place. `

 __le__  (self, other) 

 __lshift__  (self, n) 

 __lt__  (self, other) 

 __mul__  (self, other) 

 __ne__  (self, other) 

 __neg__  (self) 

 __pow__  (self, other, third  =None  ) 

 __radd__  = __add__(self, other) 

 __rdiv__  (self, other) 

 __rmul__  = __mul__(self, other) 

 __rshift__  (self, n) 

 __rsub__  (self, other) 

 __sqrt__  (self) 

 __sub__  (self, other) 

 assignValue  (self, data) 

 astype  (self, tc) 
     ` return&#160;self&#160;as&#160;array&#160;of&#160;given&#160;type. `

 crossSectionRegrid  (self, newLevel, newLatitude, missing  =None  , order  =None  , method  ='log'  ) 
     ` Return&#160;the&#160;variable&#160;regridded&#160;to&#160;new&#160;pressure&#160;levels&#160;and&#160;latitudes.   
The&#160;variable&#160;should&#160;be&#160;a&#160;function&#160;of&#160;lat,&#160;level,&#160;and&#160;(optionally)&#160;time.  
<newLevel>&#160;is&#160;an&#160;axis&#160;of&#160;the&#160;result&#160;pressure&#160;levels.  
<newLatitude>&#160;is&#160;an&#160;axis&#160;of&#160;latitude&#160;values.  
<method>&#160;is&#160;optional,&#160;either&#160;"log"&#160;to&#160;interpolate&#160;in&#160;the&#160;log&#160;of&#160;pressure
(default),  
or&#160;"linear"&#160;for&#160;linear&#160;interpolation.  
<missing>&#160;and&#160;<order>&#160;are&#160;as&#160;for&#160;regrid.CrossSectionRegridder. `

 decode  (self, ar) 
     ` Decode&#160;compressed&#160;data.&#160;ar&#160;is&#160;a&#160;masked&#160;array,&#160;scalar,&#160;or&#160;MA.masked `

 generateGridkey  (self, convention, vardict) 
     ` [ generateGridkey ](/) ():&#160;Determine&#160;if&#160;the&#160;variable&#160;is&#160;gridded,   
and&#160;generate&#160;((latname,&#160;lonname,&#160;order,&#160;maskname,&#160;class),&#160;lat,&#160;lon)&#160;if
gridded,  
or&#160;(None,&#160;None,&#160;None)&#160;if&#160;not&#160;gridded.&#160;vardict&#160;is&#160;the&#160;variable&#160;dictionary&#160;of
the&#160;parent `

 generateRectGridkey  (self, lat, lon) 
     ` [ generateRectGridkey ](/) ():&#160;Determine&#160;if&#160;the&#160;variable&#160;is&#160;gridded,&#160;rectilinear,   
and&#160;generate&#160;(latname,&#160;lonname,&#160;order,&#160;maskname,&#160;class)&#160;if&#160;gridded,  
or&#160;None&#160;if&#160;not&#160;gridded `

 getAxisIds  (self) 
     ` Get&#160;a&#160;list&#160;of&#160;axis&#160;identifiers `

 getAxisIndex  (self, axis_spec) 
     ` Return&#160;the&#160;index&#160;of&#160;the&#160;axis&#160;specificed&#160;by&#160;axis_spec.   
Argument&#160;axis_spec&#160;and&#160;be&#160;as&#160;for&#160;axisMatches  
Return&#160;-1&#160;if&#160;no&#160;match. `

 getAxisList  (self, axes  =None  , omit  =None  , order  =None  ) 
     ` Get&#160;the&#160;list&#160;of&#160;axis&#160;objects;   
If&#160;axes&#160;is&#160;not&#160;None,&#160;include&#160;only&#160;certain&#160;axes.  
If&#160;omit&#160;is&#160;not&#160;None,&#160;omit&#160;those&#160;specified&#160;by&#160;omit.  
Arguments&#160;omit&#160;or&#160;axes&#160;&#160;may&#160;be&#160;as&#160;specified&#160;in&#160;axisMatchAxis  
order&#160;is&#160;an&#160;optional&#160;string&#160;determining&#160;the&#160;output&#160;order `

 getAxisListIndex  (self, axes  =None  , omit  =None  , order  =None  ) 
     ` Return&#160;a&#160;list&#160;of&#160;indices&#160;of&#160;axis&#160;objects;   
If&#160;axes&#160;is&#160;not&#160;None,&#160;include&#160;only&#160;certain&#160;axes.  
less&#160;the&#160;ones&#160;specified&#160;in&#160;omit.&#160;If&#160;axes&#160;is&#160;None,  
use&#160;all&#160;axes&#160;of&#160;this&#160;variable.  
Other&#160;specificiations&#160;are&#160;as&#160;for&#160;axisMatchIndex. `

 getConvention  (self) 
     ` Get&#160;the&#160;metadata&#160;convention&#160;associated&#160;with&#160;this&#160;object. `

 getGrid  (self) 
     ` #&#160;Return&#160;the&#160;grid `

 getGridIndices  (self) 
     ` Return&#160;a&#160;tuple&#160;of&#160;indices&#160;corresponding&#160;to&#160;the&#160;variable&#160;grid. `

 getLatitude  (self) 
     ` Get&#160;the&#160;first&#160;latitude&#160;dimension,&#160;or&#160;None&#160;if&#160;not&#160;found. `

 getLevel  (self) 
     ` Get&#160;the&#160;first&#160;vertical&#160;level&#160;dimension&#160;in&#160;the&#160;domain,   
or&#160;None&#160;if&#160;not&#160;found. `

 getLongitude  (self) 
     ` Get&#160;the&#160;first&#160;latitude&#160;dimension,&#160;or&#160;None&#160;if&#160;not&#160;found. `

 getMissing  (self, asarray  =0  ) 
     ` Return&#160;the&#160;missing&#160;value&#160;as&#160;a&#160;scalar,&#160;or&#160;as   
a&#160;Numeric&#160;array&#160;if&#160;asarray==1 `

 getOrder  (self, ids  =0  ) 
     ` [ getOrder ](/) (ids=0)&#160;returns&#160;the&#160;order&#160;string,&#160;such&#160;as&#160;tzyx.   
  
if&#160;ids&#160;==&#160;0&#160;(the&#160;default)&#160;for&#160;an&#160;axis&#160;that&#160;is&#160;not&#160;t,z,x,y  
the&#160;order&#160;string&#160;will&#160;contain&#160;a&#160;'-'&#160;in&#160;that&#160;location.  
The&#160;result&#160;string&#160;will&#160;be&#160;of&#160;the&#160;same&#160;length&#160;as&#160;the&#160;number  
of&#160;axes.&#160;This&#160;makes&#160;it&#160;easy&#160;to&#160;loop&#160;over&#160;the&#160;dimensions.  
  
if&#160;ids&#160;==&#160;1&#160;those&#160;axes&#160;will&#160;be&#160;represented&#160;in&#160;the&#160;order  
string&#160;as&#160;(id)&#160;where&#160;id&#160;is&#160;that&#160;axis'&#160;id.&#160;The&#160;result&#160;will  
be&#160;suitable&#160;for&#160;passing&#160;to&#160;order2index&#160;to&#160;get&#160;the  
corresponding&#160;axes,&#160;and&#160;to&#160;orderparse&#160;for&#160;dividing&#160;up&#160;into  
components. `

 getRegion  (self, *specs, keys) 
     ` getRegion   
Read&#160;a&#160;region&#160;of&#160;data.&#160;A&#160;region&#160;is&#160;an&#160;n-dimensional  
rectangular&#160;region&#160;specified&#160;in&#160;coordinate&#160;space.  
'slices'&#160;is&#160;an&#160;argument&#160;list,&#160;each&#160;item&#160;of&#160;which&#160;has&#160;one&#160;of&#160;the&#160;following
forms:  
-&#160;x,&#160;where&#160;x&#160;is&#160;a&#160;scalar   
Map&#160;the&#160;scalar&#160;to&#160;the&#160;index&#160;of&#160;the&#160;closest&#160;coordinate&#160;value  
-&#160;(x,y)   
Map&#160;the&#160;half-open&#160;coordinate&#160;interval&#160;[x,y)&#160;to&#160;index&#160;interval  
-&#160;(x,y,'cc')   
Map&#160;the&#160;closed&#160;interval&#160;[x,y]&#160;to&#160;index&#160;interval.&#160;Other&#160;options&#160;are&#160;'oo'
(open),  
'oc'&#160;(open&#160;on&#160;the&#160;left),&#160;and&#160;'co'&#160;(open&#160;on&#160;the&#160;right,&#160;the&#160;default).  
-&#160;(x,y,'co',cycle)   
Map&#160;the&#160;coordinate&#160;interval&#160;with&#160;wraparound.&#160;If&#160;no&#160;cycle&#160;is&#160;specified,
wraparound  
will&#160;occur&#160;iff&#160;axis.isCircular()&#160;is&#160;true.  
NOTE:&#160;Only&#160;one&#160;dimension&#160;may&#160;be&#160;wrapped.  
-&#160;Ellipsis   
Represents&#160;the&#160;full&#160;range&#160;of&#160;all&#160;dimensions&#160;bracketed&#160;by&#160;non-Ellipsis&#160;items.  
-&#160;':'&#160;or&#160;None   
Represents&#160;the&#160;full&#160;range&#160;of&#160;one&#160;dimension.  
  
For&#160;example,&#160;suppose&#160;the&#160;variable&#160;domain&#160;is&#160;(time,level,lat,lon).&#160;Then  
  
[ getRegion ](/) ((10,20),850,Ellipsis,(-180,180))  
  
retrieves:  
-&#160;all&#160;times&#160;t&#160;such&#160;that&#160;10.<=t<20\.   
-&#160;level&#160;850   
-&#160;all&#160;values&#160;of&#160;all&#160;dimensions&#160;between&#160;level&#160;and&#160;lon&#160;(namely,&#160;lat)   
-&#160;longitudes&#160;x&#160;such&#160;that&#160;-180<=x<180.&#160;This&#160;will&#160;be&#160;wrapped&#160;unless   
lon.topology=='linear' `

 getSlice  (self, *specs, keys) 
     ` x.getSlice&#160;takes&#160;arguments&#160;of&#160;the&#160;following&#160;forms&#160;and&#160;produces   
a&#160;return&#160;array.&#160;The&#160;keyword&#160;argument&#160;squeeze&#160;determines&#160;whether  
or&#160;not&#160;the&#160;shape&#160;of&#160;the&#160;returned&#160;array&#160;contains&#160;dimensions&#160;whose  
length&#160;is&#160;1;&#160;by&#160;default&#160;this&#160;argument&#160;is&#160;1,&#160;and&#160;such&#160;dimensions  
are&#160;'squeezed&#160;out'.  
There&#160;can&#160;be&#160;zero&#160;or&#160;more&#160;positional&#160;arguments,&#160;each&#160;of&#160;the&#160;form:  
(a)&#160;a&#160;single&#160;integer&#160;n,&#160;meaning&#160;slice(n,&#160;n+1)  
(b)&#160;an&#160;instance&#160;of&#160;the&#160;slice&#160;class  
(c)&#160;a&#160;tuple,&#160;which&#160;will&#160;be&#160;used&#160;as&#160;arguments&#160;to&#160;create&#160;a&#160;slice  
(d)&#160;None&#160;or&#160;':',&#160;which&#160;means&#160;a&#160;slice&#160;covering&#160;that&#160;entire&#160;dimension  
(e)&#160;Ellipsis&#160;(...),&#160;which&#160;means&#160;to&#160;fill&#160;the&#160;slice&#160;list&#160;with&#160;':'  
leaving&#160;only&#160;enough&#160;room&#160;at&#160;the&#160;end&#160;for&#160;the&#160;remaining  
positional&#160;arguments  
There&#160;can&#160;be&#160;keyword&#160;arguments&#160;of&#160;the&#160;form&#160;key&#160;=&#160;value,&#160;where  
key&#160;can&#160;be&#160;one&#160;of&#160;the&#160;names&#160;'time',&#160;'level',&#160;'latitude',&#160;or  
'longitude'.&#160;The&#160;corresponding&#160;value&#160;can&#160;be&#160;any&#160;of&#160;(a)-(d)&#160;above.  
  
There&#160;must&#160;be&#160;no&#160;conflict&#160;between&#160;the&#160;positional&#160;arguments&#160;and  
the&#160;keywords.  
  
In&#160;(a)-(c)&#160;negative&#160;numbers&#160;are&#160;treated&#160;as&#160;offsets&#160;from&#160;the&#160;end  
of&#160;that&#160;dimension,&#160;as&#160;in&#160;normal&#160;Python&#160;indexing. `

 getTime  (self) 
     ` Get&#160;the&#160;first&#160;time&#160;dimension,&#160;or&#160;None&#160;if&#160;not&#160;found `

 isEncoded  (self) 
     ` True&#160;iff&#160;self&#160;is&#160;represented&#160;as&#160;packed&#160;data. `

 pressureRegrid  (self, newLevel, missing  =None  , order  =None  , method  ='log'  ) 
     ` Return&#160;the&#160;variable&#160;regridded&#160;to&#160;new&#160;pressure&#160;levels.   
The&#160;variable&#160;should&#160;be&#160;a&#160;function&#160;of&#160;lat,&#160;lon,&#160;pressure,&#160;and&#160;(optionally)
time.  
<newLevel>&#160;is&#160;an&#160;axis&#160;of&#160;the&#160;result&#160;pressure&#160;levels.  
<method>&#160;is&#160;optional,&#160;either&#160;"log"&#160;to&#160;interpolate&#160;in&#160;the&#160;log&#160;of&#160;pressure
(default),  
or&#160;"linear"&#160;for&#160;linear&#160;interpolation.  
<missing>&#160;and&#160;<order>&#160;are&#160;as&#160;for&#160;regrid.PressureRegridder. `

 rank  (self) 

 reg_specs2slices  (self, initspeclist, force  =None  ) 

 regrid  (self, togrid, missing  =None  , order  =None  , mask  =None  ) 
     ` return&#160;self&#160;regridded&#160;to&#160;the&#160;new&#160;grid.&#160;Keyword&#160;arguments   
are&#160;as&#160;for&#160;regrid.Regridder. `

 reorder  (self, order) 
     ` return&#160;self&#160;reordered&#160;per&#160;the&#160;specification&#160;order `

 select  = __call__(self, *args, kwargs) 
     ` Selection&#160;of&#160;a&#160;subregion&#160;using&#160;selectors `

 setGrid  (self, grid) 
     ` #&#160;Set&#160;the&#160;variable&#160;grid `

 setMissing  (self, value) 
     ` Set&#160;the&#160;missing&#160;value,&#160;which&#160;may&#160;be&#160;a&#160;scalar,   
a&#160;single-valued&#160;Numeric&#160;array,&#160;or&#160;None.&#160;The&#160;value&#160;is  
cast&#160;to&#160;the&#160;same&#160;type&#160;as&#160;the&#160;variable. `

 specs2slices  (self, speclist, force  =None  ) 
     ` Create&#160;an&#160;equivalent&#160;list&#160;of&#160;slices&#160;from&#160;an&#160;index&#160;specification   
An&#160;index&#160;specification&#160;is&#160;a&#160;list&#160;of&#160;acceptable&#160;items,&#160;which&#160;are  
\--&#160;an&#160;integer  
\--&#160;a&#160;slice&#160;instance&#160;(slice(start,&#160;stop,&#160;stride))  
\--&#160;the&#160;object&#160;"unspecified"  
\--&#160;the&#160;object&#160;None  
\--&#160;a&#160;colon  
The&#160;size&#160;of&#160;the&#160;speclist&#160;must&#160;be [ rank ](/) () `

 subRegion  (self, *specs, keys) 

* * *

Methods inherited from [ cdms.slabinterface.Slab ](/cdms.slabinterface.html) :  

 createattribute  (self, name, value) 
     ` Create&#160;an&#160;attribute&#160;and&#160;set&#160;its&#160;name&#160;to&#160;value. `

 deleteattribute  (self, name) 
     ` Delete&#160;the&#160;named&#160;attribute. `

 getattribute  (self, name) 
     ` Get&#160;the&#160;attribute&#160;name. `

 getdimattribute  (self, dim, field) 
     ` Get&#160;the&#160;attribute&#160;named&#160;field&#160;from&#160;the&#160;dim'th&#160;dimension.   
For&#160;bounds&#160;returns&#160;the&#160;old&#160;cu&#160;one-dimensional&#160;version. `

 listattributes  (self) 
     ` Return&#160;a&#160;list&#160;of&#160;attribute&#160;names. `

 listdimattributes  (self, dim) 
     ` List&#160;the&#160;legal&#160;axis&#160;field&#160;names. `

 listdimnames  (self) 
     ` Return&#160;a&#160;list&#160;of&#160;the&#160;names&#160;of&#160;the&#160;dimensions. `

 setattribute  (self, name, value) 
     ` Set&#160;the&#160;attribute&#160;name&#160;to&#160;value. `

 showdim  (self) 
     ` Show&#160;the&#160;dimension&#160;attributes&#160;and&#160;values. `

* * *

Data and other attributes inherited from [ cdms.slabinterface.Slab
](/cdms.slabinterface.html) :  

 std_slab_atts  = ['filename', 'missing_value', 'comments', 'grid_name', 'grid_type', 'time_statistic', 'long_name', 'units'] 

  
class  FileAuxAxis1D  ( [ AbstractAuxAxis1D ](/cdms.auxcoord.html) , [
cdms.fvariable.FileVariable ](/cdms.fvariable.html) )

` `

Method resolution order:

     [ FileAuxAxis1D ](/cdms.auxcoord.html)
     [ AbstractAuxAxis1D ](/cdms.auxcoord.html)
     [ cdms.coord.AbstractCoordinateAxis ](/cdms.coord.html)
     [ cdms.cdmsobj.CdmsObj ](/cdms.cdmsobj.html)
     [ cdms.internattr.InternalAttributesClass ](/cdms.internattr.html)
     [ PropertiedClasses.Properties.PropertiedClass ](/PropertiedClasses.Properties.html)
     [ cdms.fvariable.FileVariable ](/cdms.fvariable.html)
     [ cdms.variable.DatasetVariable ](/cdms.variable.html)
     [ cdms.avariable.AbstractVariable ](/cdms.avariable.html)
     [ cdms.slabinterface.Slab ](/cdms.slabinterface.html)

* * *

Methods defined here:  

 __init__  (self, parent, id, obj  =None  , bounds  =None  ) 

 __repr__  (self) 

* * *

Methods inherited from [ AbstractAuxAxis1D ](/cdms.auxcoord.html) :  

 clone  (self, copyData  =1  ) 
     ` clone&#160;(self,&#160;copyData=1)   
Return&#160;a&#160;copy&#160;of&#160;self&#160;as&#160;a&#160;transient&#160;axis.  
If&#160;copyData&#160;is&#160;1,&#160;make&#160;a&#160;separate&#160;copy&#160;of&#160;the&#160;data. `

 setBounds  (self, bounds) 

 subSlice  (self, *specs, keys) 

* * *

Methods inherited from [ cdms.coord.AbstractCoordinateAxis ](/cdms.coord.html)
:  

 designateLatitude  (self, persistent  =0  ) 
     ` #&#160;Designate&#160;axis&#160;as&#160;a&#160;latitude&#160;axis.   
#&#160;If&#160;persistent&#160;is&#160;true,&#160;write&#160;metadata&#160;to&#160;the&#160;container. `

 designateLevel  (self, persistent  =0  ) 
     ` #&#160;Designate&#160;axis&#160;as&#160;a&#160;vertical&#160;level&#160;axis   
#&#160;If&#160;persistent&#160;is&#160;true,&#160;write&#160;metadata&#160;to&#160;the&#160;container. `

 designateLongitude  (self, persistent  =0  ) 
     ` #&#160;Designate&#160;axis&#160;as&#160;a&#160;longitude&#160;axis   
#&#160;If&#160;persistent&#160;is&#160;true,&#160;write&#160;metadata&#160;to&#160;the&#160;container. `

 designateTime  (self, persistent  =0  , calendar  =4369  ) 
     ` #&#160;Designate&#160;axis&#160;as&#160;a&#160;time&#160;axis,&#160;and&#160;optionally&#160;set&#160;the&#160;calendar   
#&#160;If&#160;persistent&#160;is&#160;true,&#160;write&#160;metadata&#160;to&#160;the&#160;container. `

 getBounds  (self) 

 getCalendar  (self) 
     ` #&#160;Return&#160;the&#160;cdtime&#160;calendar:&#160;GregorianCalendar,&#160;NoLeapCalendar,&#160;JulianCalendar,&#160;Calendar360   
#&#160;or&#160;None.&#160;If&#160;the&#160;axis&#160;does&#160;not&#160;have&#160;a&#160;calendar&#160;attribute,&#160;return&#160;the&#160;global  
#&#160;calendar. `

 getData  (self) 

 getExplicitBounds  (self) 
     ` #&#160;Return&#160;None&#160;if&#160;not&#160;explicitly&#160;defined `

 info  (self, flag  =None  , device  =None  ) 
     ` Write&#160;info&#160;about&#160;axis;&#160;include&#160;dimension&#160;values&#160;and&#160;weights&#160;if&#160;flag `

 isAbstractCoordinate  (self) 

 isLatitude  (self) 
     ` #&#160;Return&#160;true&#160;iff&#160;the&#160;axis&#160;is&#160;a&#160;latitude&#160;axis `

 isLevel  (self) 
     ` #&#160;Return&#160;true&#160;iff&#160;the&#160;axis&#160;is&#160;a&#160;level&#160;axis `

 isLongitude  (self) 
     ` #&#160;Return&#160;true&#160;iff&#160;the&#160;axis&#160;is&#160;a&#160;longitude&#160;axis `

 isTime  (self) 
     ` #&#160;Return&#160;true&#160;iff&#160;the&#160;axis&#160;is&#160;a&#160;time&#160;axis `

 listall  (self, all  =None  ) 
     ` Get&#160;list&#160;of&#160;info&#160;about&#160;this&#160;axis. `

 setCalendar  (self, calendar, persistent  =1  ) 
     ` #&#160;Set&#160;the&#160;calendar `

 size  (self, axis  =None  ) 
     ` Number&#160;of&#160;elements&#160;in&#160;array,&#160;or&#160;in&#160;a&#160;particular&#160;axis. `

 writeToFile  (self, file) 

* * *

Data and other attributes inherited from [ cdms.coord.AbstractCoordinateAxis
](/cdms.coord.html) :  

 axis_count  = 0 

* * *

Methods inherited from [ cdms.cdmsobj.CdmsObj ](/cdms.cdmsobj.html) :  

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

* * *

Methods inherited from [ cdms.fvariable.FileVariable ](/cdms.fvariable.html) :  

 __len__  (self) 
     ` Length&#160;of&#160;first&#160;dimension. `

 __setitem__  (self, index, value) 

 __setslice__  (self, low, high, value) 

 assignValue  (self, data) 

 expertSlice  (self, initslicelist) 

 getValue  (self, squeeze  =1  ) 
     ` Return&#160;the&#160;entire&#160;set&#160;of&#160;values. `

 initDomain  (self, axisdict) 
     ` Called&#160;by&#160;whoever&#160;made&#160;me. `

 typecode  (self) 

* * *

Methods inherited from [ cdms.variable.DatasetVariable ](/cdms.variable.html)
:  

 __getitem__  (self, key) 

 __getslice__  (self, low, high) 

 expertPaths  (self, slist) 
     ` [ expertPaths ](/) (self,&#160;slicelist)   
takes&#160;a&#160;list&#160;of&#160;slices,  
returns&#160;a&#160;3-tuple:&#160;(npart,&#160;dimensionlist,&#160;partitionSlices)&#160;where:  
npart&#160;is&#160;the&#160;number&#160;of&#160;partitioned&#160;dimensions:&#160;0,&#160;1,&#160;or&#160;2;  
dimensionlist&#160;is&#160;a&#160;tuple&#160;of&#160;length&#160;npart,&#160;having&#160;the&#160;dimension  
numbers&#160;of&#160;the&#160;partitioned&#160;dimensions;  
partitionSlices&#160;is&#160;the&#160;list&#160;of&#160;file-specific&#160;(filename,&#160;slice)  
corresponding&#160;to&#160;the&#160;paths&#160;and&#160;slices&#160;within&#160;the&#160;files&#160;to&#160;be&#160;read.  
The&#160;exact&#160;form&#160;of&#160;partitionSlices&#160;depends&#160;on&#160;the&#160;value&#160;of&#160;npart:  
npart&#160;&#160;&#160;&#160;&#160;partitionSlices  
0&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;(filename,slicelist)  
1&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;[(filename,slicelist),...,(filename,slicelist)]  
2&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;[[(filename,slicelist),...,(filename,slicelist)]  
[(filename,slicelist),...,(filename,slicelist)]  
...  
[(filename,slicelist),...,(filename,slicelist)]]  
  
Note:  
-&#160;A&#160;filename&#160;of&#160;None&#160;indicates&#160;that&#160;no&#160;file&#160;was&#160;found&#160;with&#160;data   
corresponding&#160;to&#160;the&#160;slicelist.  
-&#160;If&#160;partitionSlices&#160;is&#160;None,&#160;the&#160;slicelist&#160;does&#160;not&#160;intersect&#160;the&#160;domain.   
-&#160;An&#160;empty&#160;partitionSlices&#160;[]&#160;means&#160;that&#160;the&#160;variable&#160;is&#160;zero-dimensional. `

 genMatch  (self, axis, interval, matchnames) 
     ` Helper&#160;function&#160;for&#160;expertPaths.   
axis&#160;is&#160;a&#160;partitioned&#160;axis,&#160;either&#160;time&#160;or&#160;vertical&#160;level.  
interval&#160;is&#160;an&#160;index&#160;interval&#160;(istart,&#160;iend).  
matchnames&#160;is&#160;a&#160;partially&#160;filled&#160;list&#160;[id,&#160;timestart,&#160;timeend,&#160;levstart,
levend]  
If&#160;a&#160;filemap&#160;is&#160;used,&#160;matchnames&#160;has&#160;indices,&#160;otherwise&#160;has&#160;coordinates.  
  
Function&#160;modifies&#160;matchnames&#160;based&#160;on&#160;axis&#160;and&#160;interval,  
returns&#160;the&#160;modified&#160;matchnames&#160;tuple. `

 getAxis  (self, n) 

 getDomain  (self) 

 getFilePath  (self, matchnames, template) 
     ` Lookup&#160;or&#160;generate&#160;the&#160;file&#160;path,&#160;depending&#160;on&#160;whether&#160;a&#160;filemap   
or&#160;template&#160;is&#160;present. `

 getPaths  (self, *specs, keys) 
     ` #&#160;Get&#160;the&#160;paths&#160;associated&#160;with&#160;the&#160;interval&#160;region&#160;specified   
#&#160;by&#160;'intervals'.&#160;This&#160;incorporates&#160;most&#160;of&#160;the&#160;logic&#160;of&#160;__getitem__,  
#&#160;without&#160;actually&#160;reading&#160;the&#160;data.  
#  
#&#160;'specs'&#160;is&#160;a&#160;list&#160;of&#160;interval&#160;range&#160;specifications&#160;as&#160;defined  
#&#160;for&#160;getSlice.  
#  
#&#160;The&#160;function&#160;returns&#160;a&#160;list&#160;of&#160;tuples&#160;of&#160;the&#160;form&#160;(path,slicelist),  
#&#160;where&#160;path&#160;is&#160;the&#160;path&#160;of&#160;a&#160;file,&#160;and&#160;slicetuple&#160;is&#160;a&#160;tuple&#160;of  
#&#160;slices,&#160;of&#160;the&#160;same&#160;length&#160;as&#160;the&#160;rank&#160;of&#160;the&#160;variable,&#160;representing&#160;the  
#&#160;region&#160;of&#160;the&#160;variable&#160;which&#160;is&#160;contained&#160;in&#160;the&#160;file.&#160;The&#160;following  
#&#160;would&#160;retrieve&#160;the&#160;data&#160;for&#160;that&#160;file:  
#  
#&#160;&#160;&#160;f&#160;=&#160;Cdunif.CdunifFile(path,'r')  
#&#160;&#160;&#160;var&#160;=&#160;f.variables[self.  name_in_file  ]  
#&#160;&#160;&#160;data&#160;=&#160;apply(var.getitem,slicelist) `

 getShape  (self) 

 getTemplate  (self) 
     ` #&#160;Get&#160;the&#160;template `

* * *

Methods inherited from [ cdms.avariable.AbstractVariable
](/cdms.avariable.html) :  

 __abs__  (self) 

 __add__  (self, other) 

 __array__  (self, t  =None  ) 

 __call__  (self, *args, kwargs) 
     ` Selection&#160;of&#160;a&#160;subregion&#160;using&#160;selectors `

 __div__  (self, other) 

 __eq__  (self, other) 

 __ge__  (self, other) 

 __gt__  (self, other) 

 __iadd__  (self, other) 
     ` Add&#160;other&#160;to&#160;self&#160;in&#160;place. `

 __idiv__  (self, other) 
     ` Divide&#160;self&#160;by&#160;other&#160;in&#160;place. `

 __imul__  (self, other) 
     ` Multiply&#160;self&#160;by&#160;other&#160;in&#160;place. `

 __isub__  (self, other) 
     ` Subtract&#160;other&#160;from&#160;self&#160;in&#160;place. `

 __le__  (self, other) 

 __lshift__  (self, n) 

 __lt__  (self, other) 

 __mul__  (self, other) 

 __ne__  (self, other) 

 __neg__  (self) 

 __pow__  (self, other, third  =None  ) 

 __radd__  = __add__(self, other) 

 __rdiv__  (self, other) 

 __rmul__  = __mul__(self, other) 

 __rshift__  (self, n) 

 __rsub__  (self, other) 

 __sqrt__  (self) 

 __sub__  (self, other) 

 astype  (self, tc) 
     ` return&#160;self&#160;as&#160;array&#160;of&#160;given&#160;type. `

 crossSectionRegrid  (self, newLevel, newLatitude, missing  =None  , order  =None  , method  ='log'  ) 
     ` Return&#160;the&#160;variable&#160;regridded&#160;to&#160;new&#160;pressure&#160;levels&#160;and&#160;latitudes.   
The&#160;variable&#160;should&#160;be&#160;a&#160;function&#160;of&#160;lat,&#160;level,&#160;and&#160;(optionally)&#160;time.  
<newLevel>&#160;is&#160;an&#160;axis&#160;of&#160;the&#160;result&#160;pressure&#160;levels.  
<newLatitude>&#160;is&#160;an&#160;axis&#160;of&#160;latitude&#160;values.  
<method>&#160;is&#160;optional,&#160;either&#160;"log"&#160;to&#160;interpolate&#160;in&#160;the&#160;log&#160;of&#160;pressure
(default),  
or&#160;"linear"&#160;for&#160;linear&#160;interpolation.  
<missing>&#160;and&#160;<order>&#160;are&#160;as&#160;for&#160;regrid.CrossSectionRegridder. `

 decode  (self, ar) 
     ` Decode&#160;compressed&#160;data.&#160;ar&#160;is&#160;a&#160;masked&#160;array,&#160;scalar,&#160;or&#160;MA.masked `

 generateGridkey  (self, convention, vardict) 
     ` [ generateGridkey ](/) ():&#160;Determine&#160;if&#160;the&#160;variable&#160;is&#160;gridded,   
and&#160;generate&#160;((latname,&#160;lonname,&#160;order,&#160;maskname,&#160;class),&#160;lat,&#160;lon)&#160;if
gridded,  
or&#160;(None,&#160;None,&#160;None)&#160;if&#160;not&#160;gridded.&#160;vardict&#160;is&#160;the&#160;variable&#160;dictionary&#160;of
the&#160;parent `

 generateRectGridkey  (self, lat, lon) 
     ` [ generateRectGridkey ](/) ():&#160;Determine&#160;if&#160;the&#160;variable&#160;is&#160;gridded,&#160;rectilinear,   
and&#160;generate&#160;(latname,&#160;lonname,&#160;order,&#160;maskname,&#160;class)&#160;if&#160;gridded,  
or&#160;None&#160;if&#160;not&#160;gridded `

 getAxisIds  (self) 
     ` Get&#160;a&#160;list&#160;of&#160;axis&#160;identifiers `

 getAxisIndex  (self, axis_spec) 
     ` Return&#160;the&#160;index&#160;of&#160;the&#160;axis&#160;specificed&#160;by&#160;axis_spec.   
Argument&#160;axis_spec&#160;and&#160;be&#160;as&#160;for&#160;axisMatches  
Return&#160;-1&#160;if&#160;no&#160;match. `

 getAxisList  (self, axes  =None  , omit  =None  , order  =None  ) 
     ` Get&#160;the&#160;list&#160;of&#160;axis&#160;objects;   
If&#160;axes&#160;is&#160;not&#160;None,&#160;include&#160;only&#160;certain&#160;axes.  
If&#160;omit&#160;is&#160;not&#160;None,&#160;omit&#160;those&#160;specified&#160;by&#160;omit.  
Arguments&#160;omit&#160;or&#160;axes&#160;&#160;may&#160;be&#160;as&#160;specified&#160;in&#160;axisMatchAxis  
order&#160;is&#160;an&#160;optional&#160;string&#160;determining&#160;the&#160;output&#160;order `

 getAxisListIndex  (self, axes  =None  , omit  =None  , order  =None  ) 
     ` Return&#160;a&#160;list&#160;of&#160;indices&#160;of&#160;axis&#160;objects;   
If&#160;axes&#160;is&#160;not&#160;None,&#160;include&#160;only&#160;certain&#160;axes.  
less&#160;the&#160;ones&#160;specified&#160;in&#160;omit.&#160;If&#160;axes&#160;is&#160;None,  
use&#160;all&#160;axes&#160;of&#160;this&#160;variable.  
Other&#160;specificiations&#160;are&#160;as&#160;for&#160;axisMatchIndex. `

 getConvention  (self) 
     ` Get&#160;the&#160;metadata&#160;convention&#160;associated&#160;with&#160;this&#160;object. `

 getGrid  (self) 
     ` #&#160;Return&#160;the&#160;grid `

 getGridIndices  (self) 
     ` Return&#160;a&#160;tuple&#160;of&#160;indices&#160;corresponding&#160;to&#160;the&#160;variable&#160;grid. `

 getLatitude  (self) 
     ` Get&#160;the&#160;first&#160;latitude&#160;dimension,&#160;or&#160;None&#160;if&#160;not&#160;found. `

 getLevel  (self) 
     ` Get&#160;the&#160;first&#160;vertical&#160;level&#160;dimension&#160;in&#160;the&#160;domain,   
or&#160;None&#160;if&#160;not&#160;found. `

 getLongitude  (self) 
     ` Get&#160;the&#160;first&#160;latitude&#160;dimension,&#160;or&#160;None&#160;if&#160;not&#160;found. `

 getMissing  (self, asarray  =0  ) 
     ` Return&#160;the&#160;missing&#160;value&#160;as&#160;a&#160;scalar,&#160;or&#160;as   
a&#160;Numeric&#160;array&#160;if&#160;asarray==1 `

 getOrder  (self, ids  =0  ) 
     ` [ getOrder ](/) (ids=0)&#160;returns&#160;the&#160;order&#160;string,&#160;such&#160;as&#160;tzyx.   
  
if&#160;ids&#160;==&#160;0&#160;(the&#160;default)&#160;for&#160;an&#160;axis&#160;that&#160;is&#160;not&#160;t,z,x,y  
the&#160;order&#160;string&#160;will&#160;contain&#160;a&#160;'-'&#160;in&#160;that&#160;location.  
The&#160;result&#160;string&#160;will&#160;be&#160;of&#160;the&#160;same&#160;length&#160;as&#160;the&#160;number  
of&#160;axes.&#160;This&#160;makes&#160;it&#160;easy&#160;to&#160;loop&#160;over&#160;the&#160;dimensions.  
  
if&#160;ids&#160;==&#160;1&#160;those&#160;axes&#160;will&#160;be&#160;represented&#160;in&#160;the&#160;order  
string&#160;as&#160;(id)&#160;where&#160;id&#160;is&#160;that&#160;axis'&#160;id.&#160;The&#160;result&#160;will  
be&#160;suitable&#160;for&#160;passing&#160;to&#160;order2index&#160;to&#160;get&#160;the  
corresponding&#160;axes,&#160;and&#160;to&#160;orderparse&#160;for&#160;dividing&#160;up&#160;into  
components. `

 getRegion  (self, *specs, keys) 
     ` getRegion   
Read&#160;a&#160;region&#160;of&#160;data.&#160;A&#160;region&#160;is&#160;an&#160;n-dimensional  
rectangular&#160;region&#160;specified&#160;in&#160;coordinate&#160;space.  
'slices'&#160;is&#160;an&#160;argument&#160;list,&#160;each&#160;item&#160;of&#160;which&#160;has&#160;one&#160;of&#160;the&#160;following
forms:  
-&#160;x,&#160;where&#160;x&#160;is&#160;a&#160;scalar   
Map&#160;the&#160;scalar&#160;to&#160;the&#160;index&#160;of&#160;the&#160;closest&#160;coordinate&#160;value  
-&#160;(x,y)   
Map&#160;the&#160;half-open&#160;coordinate&#160;interval&#160;[x,y)&#160;to&#160;index&#160;interval  
-&#160;(x,y,'cc')   
Map&#160;the&#160;closed&#160;interval&#160;[x,y]&#160;to&#160;index&#160;interval.&#160;Other&#160;options&#160;are&#160;'oo'
(open),  
'oc'&#160;(open&#160;on&#160;the&#160;left),&#160;and&#160;'co'&#160;(open&#160;on&#160;the&#160;right,&#160;the&#160;default).  
-&#160;(x,y,'co',cycle)   
Map&#160;the&#160;coordinate&#160;interval&#160;with&#160;wraparound.&#160;If&#160;no&#160;cycle&#160;is&#160;specified,
wraparound  
will&#160;occur&#160;iff&#160;axis.isCircular()&#160;is&#160;true.  
NOTE:&#160;Only&#160;one&#160;dimension&#160;may&#160;be&#160;wrapped.  
-&#160;Ellipsis   
Represents&#160;the&#160;full&#160;range&#160;of&#160;all&#160;dimensions&#160;bracketed&#160;by&#160;non-Ellipsis&#160;items.  
-&#160;':'&#160;or&#160;None   
Represents&#160;the&#160;full&#160;range&#160;of&#160;one&#160;dimension.  
  
For&#160;example,&#160;suppose&#160;the&#160;variable&#160;domain&#160;is&#160;(time,level,lat,lon).&#160;Then  
  
[ getRegion ](/) ((10,20),850,Ellipsis,(-180,180))  
  
retrieves:  
-&#160;all&#160;times&#160;t&#160;such&#160;that&#160;10.<=t<20\.   
-&#160;level&#160;850   
-&#160;all&#160;values&#160;of&#160;all&#160;dimensions&#160;between&#160;level&#160;and&#160;lon&#160;(namely,&#160;lat)   
-&#160;longitudes&#160;x&#160;such&#160;that&#160;-180<=x<180.&#160;This&#160;will&#160;be&#160;wrapped&#160;unless   
lon.topology=='linear' `

 getSlice  (self, *specs, keys) 
     ` x.getSlice&#160;takes&#160;arguments&#160;of&#160;the&#160;following&#160;forms&#160;and&#160;produces   
a&#160;return&#160;array.&#160;The&#160;keyword&#160;argument&#160;squeeze&#160;determines&#160;whether  
or&#160;not&#160;the&#160;shape&#160;of&#160;the&#160;returned&#160;array&#160;contains&#160;dimensions&#160;whose  
length&#160;is&#160;1;&#160;by&#160;default&#160;this&#160;argument&#160;is&#160;1,&#160;and&#160;such&#160;dimensions  
are&#160;'squeezed&#160;out'.  
There&#160;can&#160;be&#160;zero&#160;or&#160;more&#160;positional&#160;arguments,&#160;each&#160;of&#160;the&#160;form:  
(a)&#160;a&#160;single&#160;integer&#160;n,&#160;meaning&#160;slice(n,&#160;n+1)  
(b)&#160;an&#160;instance&#160;of&#160;the&#160;slice&#160;class  
(c)&#160;a&#160;tuple,&#160;which&#160;will&#160;be&#160;used&#160;as&#160;arguments&#160;to&#160;create&#160;a&#160;slice  
(d)&#160;None&#160;or&#160;':',&#160;which&#160;means&#160;a&#160;slice&#160;covering&#160;that&#160;entire&#160;dimension  
(e)&#160;Ellipsis&#160;(...),&#160;which&#160;means&#160;to&#160;fill&#160;the&#160;slice&#160;list&#160;with&#160;':'  
leaving&#160;only&#160;enough&#160;room&#160;at&#160;the&#160;end&#160;for&#160;the&#160;remaining  
positional&#160;arguments  
There&#160;can&#160;be&#160;keyword&#160;arguments&#160;of&#160;the&#160;form&#160;key&#160;=&#160;value,&#160;where  
key&#160;can&#160;be&#160;one&#160;of&#160;the&#160;names&#160;'time',&#160;'level',&#160;'latitude',&#160;or  
'longitude'.&#160;The&#160;corresponding&#160;value&#160;can&#160;be&#160;any&#160;of&#160;(a)-(d)&#160;above.  
  
There&#160;must&#160;be&#160;no&#160;conflict&#160;between&#160;the&#160;positional&#160;arguments&#160;and  
the&#160;keywords.  
  
In&#160;(a)-(c)&#160;negative&#160;numbers&#160;are&#160;treated&#160;as&#160;offsets&#160;from&#160;the&#160;end  
of&#160;that&#160;dimension,&#160;as&#160;in&#160;normal&#160;Python&#160;indexing. `

 getTime  (self) 
     ` Get&#160;the&#160;first&#160;time&#160;dimension,&#160;or&#160;None&#160;if&#160;not&#160;found `

 isEncoded  (self) 
     ` True&#160;iff&#160;self&#160;is&#160;represented&#160;as&#160;packed&#160;data. `

 pressureRegrid  (self, newLevel, missing  =None  , order  =None  , method  ='log'  ) 
     ` Return&#160;the&#160;variable&#160;regridded&#160;to&#160;new&#160;pressure&#160;levels.   
The&#160;variable&#160;should&#160;be&#160;a&#160;function&#160;of&#160;lat,&#160;lon,&#160;pressure,&#160;and&#160;(optionally)
time.  
<newLevel>&#160;is&#160;an&#160;axis&#160;of&#160;the&#160;result&#160;pressure&#160;levels.  
<method>&#160;is&#160;optional,&#160;either&#160;"log"&#160;to&#160;interpolate&#160;in&#160;the&#160;log&#160;of&#160;pressure
(default),  
or&#160;"linear"&#160;for&#160;linear&#160;interpolation.  
<missing>&#160;and&#160;<order>&#160;are&#160;as&#160;for&#160;regrid.PressureRegridder. `

 rank  (self) 

 reg_specs2slices  (self, initspeclist, force  =None  ) 

 regrid  (self, togrid, missing  =None  , order  =None  , mask  =None  ) 
     ` return&#160;self&#160;regridded&#160;to&#160;the&#160;new&#160;grid.&#160;Keyword&#160;arguments   
are&#160;as&#160;for&#160;regrid.Regridder. `

 reorder  (self, order) 
     ` return&#160;self&#160;reordered&#160;per&#160;the&#160;specification&#160;order `

 select  = __call__(self, *args, kwargs) 
     ` Selection&#160;of&#160;a&#160;subregion&#160;using&#160;selectors `

 setGrid  (self, grid) 
     ` #&#160;Set&#160;the&#160;variable&#160;grid `

 setMissing  (self, value) 
     ` Set&#160;the&#160;missing&#160;value,&#160;which&#160;may&#160;be&#160;a&#160;scalar,   
a&#160;single-valued&#160;Numeric&#160;array,&#160;or&#160;None.&#160;The&#160;value&#160;is  
cast&#160;to&#160;the&#160;same&#160;type&#160;as&#160;the&#160;variable. `

 specs2slices  (self, speclist, force  =None  ) 
     ` Create&#160;an&#160;equivalent&#160;list&#160;of&#160;slices&#160;from&#160;an&#160;index&#160;specification   
An&#160;index&#160;specification&#160;is&#160;a&#160;list&#160;of&#160;acceptable&#160;items,&#160;which&#160;are  
\--&#160;an&#160;integer  
\--&#160;a&#160;slice&#160;instance&#160;(slice(start,&#160;stop,&#160;stride))  
\--&#160;the&#160;object&#160;"unspecified"  
\--&#160;the&#160;object&#160;None  
\--&#160;a&#160;colon  
The&#160;size&#160;of&#160;the&#160;speclist&#160;must&#160;be [ rank ](/) () `

 subRegion  (self, *specs, keys) 

* * *

Methods inherited from [ cdms.slabinterface.Slab ](/cdms.slabinterface.html) :  

 createattribute  (self, name, value) 
     ` Create&#160;an&#160;attribute&#160;and&#160;set&#160;its&#160;name&#160;to&#160;value. `

 deleteattribute  (self, name) 
     ` Delete&#160;the&#160;named&#160;attribute. `

 getattribute  (self, name) 
     ` Get&#160;the&#160;attribute&#160;name. `

 getdimattribute  (self, dim, field) 
     ` Get&#160;the&#160;attribute&#160;named&#160;field&#160;from&#160;the&#160;dim'th&#160;dimension.   
For&#160;bounds&#160;returns&#160;the&#160;old&#160;cu&#160;one-dimensional&#160;version. `

 listattributes  (self) 
     ` Return&#160;a&#160;list&#160;of&#160;attribute&#160;names. `

 listdimattributes  (self, dim) 
     ` List&#160;the&#160;legal&#160;axis&#160;field&#160;names. `

 listdimnames  (self) 
     ` Return&#160;a&#160;list&#160;of&#160;the&#160;names&#160;of&#160;the&#160;dimensions. `

 setattribute  (self, name, value) 
     ` Set&#160;the&#160;attribute&#160;name&#160;to&#160;value. `

 showdim  (self) 
     ` Show&#160;the&#160;dimension&#160;attributes&#160;and&#160;values. `

* * *

Data and other attributes inherited from [ cdms.slabinterface.Slab
](/cdms.slabinterface.html) :  

 std_slab_atts  = ['filename', 'missing_value', 'comments', 'grid_name', 'grid_type', 'time_statistic', 'long_name', 'units'] 

  
class  TransientAuxAxis1D  ( [ AbstractAuxAxis1D ](/cdms.auxcoord.html) ,
[ cdms.tvariable.TransientVariable ](/cdms.tvariable.html) )

` `

Method resolution order:

     [ TransientAuxAxis1D ](/cdms.auxcoord.html)
     [ AbstractAuxAxis1D ](/cdms.auxcoord.html)
     [ cdms.coord.AbstractCoordinateAxis ](/cdms.coord.html)
     [ cdms.tvariable.TransientVariable ](/cdms.tvariable.html)
     [ cdms.avariable.AbstractVariable ](/cdms.avariable.html)
     [ cdms.cdmsobj.CdmsObj ](/cdms.cdmsobj.html)
     [ cdms.internattr.InternalAttributesClass ](/cdms.internattr.html)
     [ PropertiedClasses.Properties.PropertiedClass ](/PropertiedClasses.Properties.html)
     [ cdms.slabinterface.Slab ](/cdms.slabinterface.html)
     [ MA.MA.MaskedArray ](/MA.MA.html)
     [ __builtin__.object ](/__builtin__.html)

* * *

Methods defined here:  

 __init__  (self, data, typecode  =None  , copy  =0  , savespace  =0  , mask  =None  , fill_value  =None  , axes  =None  , attributes  =None  , id  =None  , copyaxes  =1  , bounds  =None  ) 
     ` Create&#160;a&#160;transient,&#160;auxiliary&#160;1-D&#160;axis.   
All&#160;arguments&#160;are&#160;as&#160;for [ TransientVariable ](/cdms.tvariable.html) .  
'bounds'&#160;is&#160;the&#160;bounds&#160;array,&#160;having&#160;shape&#160;(m,nvert)&#160;where&#160;data.shape&#160;is&#160;(m,)
and  
nvert&#160;is&#160;the&#160;max&#160;number&#160;of&#160;vertices&#160;per&#160;cell. `

* * *

Methods inherited from [ AbstractAuxAxis1D ](/cdms.auxcoord.html) :  

 clone  (self, copyData  =1  ) 
     ` clone&#160;(self,&#160;copyData=1)   
Return&#160;a&#160;copy&#160;of&#160;self&#160;as&#160;a&#160;transient&#160;axis.  
If&#160;copyData&#160;is&#160;1,&#160;make&#160;a&#160;separate&#160;copy&#160;of&#160;the&#160;data. `

 setBounds  (self, bounds) 

 subSlice  (self, *specs, keys) 

* * *

Methods inherited from [ cdms.coord.AbstractCoordinateAxis ](/cdms.coord.html)
:  

 designateLatitude  (self, persistent  =0  ) 
     ` #&#160;Designate&#160;axis&#160;as&#160;a&#160;latitude&#160;axis.   
#&#160;If&#160;persistent&#160;is&#160;true,&#160;write&#160;metadata&#160;to&#160;the&#160;container. `

 designateLevel  (self, persistent  =0  ) 
     ` #&#160;Designate&#160;axis&#160;as&#160;a&#160;vertical&#160;level&#160;axis   
#&#160;If&#160;persistent&#160;is&#160;true,&#160;write&#160;metadata&#160;to&#160;the&#160;container. `

 designateLongitude  (self, persistent  =0  ) 
     ` #&#160;Designate&#160;axis&#160;as&#160;a&#160;longitude&#160;axis   
#&#160;If&#160;persistent&#160;is&#160;true,&#160;write&#160;metadata&#160;to&#160;the&#160;container. `

 designateTime  (self, persistent  =0  , calendar  =4369  ) 
     ` #&#160;Designate&#160;axis&#160;as&#160;a&#160;time&#160;axis,&#160;and&#160;optionally&#160;set&#160;the&#160;calendar   
#&#160;If&#160;persistent&#160;is&#160;true,&#160;write&#160;metadata&#160;to&#160;the&#160;container. `

 getBounds  (self) 

 getCalendar  (self) 
     ` #&#160;Return&#160;the&#160;cdtime&#160;calendar:&#160;GregorianCalendar,&#160;NoLeapCalendar,&#160;JulianCalendar,&#160;Calendar360   
#&#160;or&#160;None.&#160;If&#160;the&#160;axis&#160;does&#160;not&#160;have&#160;a&#160;calendar&#160;attribute,&#160;return&#160;the&#160;global  
#&#160;calendar. `

 getData  (self) 

 getExplicitBounds  (self) 
     ` #&#160;Return&#160;None&#160;if&#160;not&#160;explicitly&#160;defined `

 info  (self, flag  =None  , device  =None  ) 
     ` Write&#160;info&#160;about&#160;axis;&#160;include&#160;dimension&#160;values&#160;and&#160;weights&#160;if&#160;flag `

 isAbstractCoordinate  (self) 

 isLatitude  (self) 
     ` #&#160;Return&#160;true&#160;iff&#160;the&#160;axis&#160;is&#160;a&#160;latitude&#160;axis `

 isLevel  (self) 
     ` #&#160;Return&#160;true&#160;iff&#160;the&#160;axis&#160;is&#160;a&#160;level&#160;axis `

 isLongitude  (self) 
     ` #&#160;Return&#160;true&#160;iff&#160;the&#160;axis&#160;is&#160;a&#160;longitude&#160;axis `

 isTime  (self) 
     ` #&#160;Return&#160;true&#160;iff&#160;the&#160;axis&#160;is&#160;a&#160;time&#160;axis `

 listall  (self, all  =None  ) 
     ` Get&#160;list&#160;of&#160;info&#160;about&#160;this&#160;axis. `

 setCalendar  (self, calendar, persistent  =1  ) 
     ` #&#160;Set&#160;the&#160;calendar `

 size  (self, axis  =None  ) 
     ` Number&#160;of&#160;elements&#160;in&#160;array,&#160;or&#160;in&#160;a&#160;particular&#160;axis. `

 writeToFile  (self, file) 

* * *

Data and other attributes inherited from [ cdms.coord.AbstractCoordinateAxis
](/cdms.coord.html) :  

 axis_count  = 0 

* * *

Methods inherited from [ cdms.tvariable.TransientVariable
](/cdms.tvariable.html) :  

 __len__  (self) 
     ` Length&#160;of&#160;first&#160;dimension `

 __repr__  (self) 

 __str__  (self) 

 assignValue  (self, data) 

 astype  (self, tc) 
     ` return&#160;self&#160;as&#160;array&#160;of&#160;given&#160;type. `

 copyAxis  (self, n, axis) 
     ` Set&#160;n&#160;axis&#160;of&#160;self&#160;to&#160;a&#160;copy&#160;of&#160;axis.&#160;(0-based&#160;index)   
Invalidates&#160;grid. `

 copyDomain  (self, other) 
     ` Set&#160;the&#160;axes&#160;and&#160;grid&#160;by&#160;copying&#160;variable&#160;other. `

 copydimension  (self, idim, other, jdim) 
     ` Set&#160;idim&#160;dimension&#160;of&#160;self&#160;to&#160;variable&#160;other's&#160;jdim'th   
This&#160;is&#160;for&#160;old&#160;cu&#160;compatibility.&#160;Use&#160;copyAxis&#160;for&#160;new&#160;code. `

 expertSlice  (self, slicelist) 

 getAxis  (self, n) 

 getDomain  (self) 

 getGrid  (self) 

 getValue  (self, squeeze  =1  ) 

 initDomain  (self, axes, copyaxes  =1  ) 

 isEncoded  (self) 
     ` Transient&#160;variables&#160;are&#160;not&#160;encoded `

 setAxis  (self, n, axis, savegrid  =0  ) 
     ` Set&#160;n&#160;axis&#160;of&#160;self&#160;to&#160;a&#160;copy&#160;of&#160;axis.&#160;(0-based&#160;index) `

 setAxisList  (self, axislist) 
     ` Set&#160;the&#160;axes&#160;to&#160;axislist. `

 setMaskFromGridMask  (self, mask, gridindices) 
     ` Set&#160;the&#160;mask&#160;for&#160;self,&#160;given&#160;a&#160;grid&#160;mask&#160;and&#160;the&#160;variable&#160;domain   
indices&#160;corresponding&#160;to&#160;the&#160;grid&#160;dimensions. `

 setMissing  (self, value) 
     ` Set&#160;missing&#160;value&#160;attribute&#160;and&#160;fill&#160;value `

 set_fill_value  (self, value) 
     ` Set&#160;missing&#160;value&#160;attribute&#160;and&#160;fill&#160;value `

 setdimattribute  (self, dim, field, value) 
     ` Set&#160;the&#160;attribute&#160;named&#160;field&#160;from&#160;the&#160;dim'th&#160;dimension. `

 typecode  (self) 

* * *

Data and other attributes inherited from [ cdms.tvariable.TransientVariable
](/cdms.tvariable.html) :  

 count  = 0 

* * *

Methods inherited from [ cdms.avariable.AbstractVariable
](/cdms.avariable.html) :  

 __abs__  (self) 

 __add__  (self, other) 

 __array__  (self, t  =None  ) 

 __call__  (self, *args, kwargs) 
     ` Selection&#160;of&#160;a&#160;subregion&#160;using&#160;selectors `

 __div__  (self, other) 

 __eq__  (self, other) 

 __ge__  (self, other) 

 __getitem__  (self, key) 

 __getslice__  (self, low, high) 

 __gt__  (self, other) 

 __iadd__  (self, other) 
     ` Add&#160;other&#160;to&#160;self&#160;in&#160;place. `

 __idiv__  (self, other) 
     ` Divide&#160;self&#160;by&#160;other&#160;in&#160;place. `

 __imul__  (self, other) 
     ` Multiply&#160;self&#160;by&#160;other&#160;in&#160;place. `

 __isub__  (self, other) 
     ` Subtract&#160;other&#160;from&#160;self&#160;in&#160;place. `

 __le__  (self, other) 

 __lshift__  (self, n) 

 __lt__  (self, other) 

 __mul__  (self, other) 

 __ne__  (self, other) 

 __neg__  (self) 

 __pow__  (self, other, third  =None  ) 

 __radd__  = __add__(self, other) 

 __rdiv__  (self, other) 

 __rmul__  = __mul__(self, other) 

 __rshift__  (self, n) 

 __rsub__  (self, other) 

 __sqrt__  (self) 

 __sub__  (self, other) 

 crossSectionRegrid  (self, newLevel, newLatitude, missing  =None  , order  =None  , method  ='log'  ) 
     ` Return&#160;the&#160;variable&#160;regridded&#160;to&#160;new&#160;pressure&#160;levels&#160;and&#160;latitudes.   
The&#160;variable&#160;should&#160;be&#160;a&#160;function&#160;of&#160;lat,&#160;level,&#160;and&#160;(optionally)&#160;time.  
<newLevel>&#160;is&#160;an&#160;axis&#160;of&#160;the&#160;result&#160;pressure&#160;levels.  
<newLatitude>&#160;is&#160;an&#160;axis&#160;of&#160;latitude&#160;values.  
<method>&#160;is&#160;optional,&#160;either&#160;"log"&#160;to&#160;interpolate&#160;in&#160;the&#160;log&#160;of&#160;pressure
(default),  
or&#160;"linear"&#160;for&#160;linear&#160;interpolation.  
<missing>&#160;and&#160;<order>&#160;are&#160;as&#160;for&#160;regrid.CrossSectionRegridder. `

 decode  (self, ar) 
     ` Decode&#160;compressed&#160;data.&#160;ar&#160;is&#160;a&#160;masked&#160;array,&#160;scalar,&#160;or&#160;MA.masked `

 generateGridkey  (self, convention, vardict) 
     ` [ generateGridkey ](/) ():&#160;Determine&#160;if&#160;the&#160;variable&#160;is&#160;gridded,   
and&#160;generate&#160;((latname,&#160;lonname,&#160;order,&#160;maskname,&#160;class),&#160;lat,&#160;lon)&#160;if
gridded,  
or&#160;(None,&#160;None,&#160;None)&#160;if&#160;not&#160;gridded.&#160;vardict&#160;is&#160;the&#160;variable&#160;dictionary&#160;of
the&#160;parent `

 generateRectGridkey  (self, lat, lon) 
     ` [ generateRectGridkey ](/) ():&#160;Determine&#160;if&#160;the&#160;variable&#160;is&#160;gridded,&#160;rectilinear,   
and&#160;generate&#160;(latname,&#160;lonname,&#160;order,&#160;maskname,&#160;class)&#160;if&#160;gridded,  
or&#160;None&#160;if&#160;not&#160;gridded `

 getAxisIds  (self) 
     ` Get&#160;a&#160;list&#160;of&#160;axis&#160;identifiers `

 getAxisIndex  (self, axis_spec) 
     ` Return&#160;the&#160;index&#160;of&#160;the&#160;axis&#160;specificed&#160;by&#160;axis_spec.   
Argument&#160;axis_spec&#160;and&#160;be&#160;as&#160;for&#160;axisMatches  
Return&#160;-1&#160;if&#160;no&#160;match. `

 getAxisList  (self, axes  =None  , omit  =None  , order  =None  ) 
     ` Get&#160;the&#160;list&#160;of&#160;axis&#160;objects;   
If&#160;axes&#160;is&#160;not&#160;None,&#160;include&#160;only&#160;certain&#160;axes.  
If&#160;omit&#160;is&#160;not&#160;None,&#160;omit&#160;those&#160;specified&#160;by&#160;omit.  
Arguments&#160;omit&#160;or&#160;axes&#160;&#160;may&#160;be&#160;as&#160;specified&#160;in&#160;axisMatchAxis  
order&#160;is&#160;an&#160;optional&#160;string&#160;determining&#160;the&#160;output&#160;order `

 getAxisListIndex  (self, axes  =None  , omit  =None  , order  =None  ) 
     ` Return&#160;a&#160;list&#160;of&#160;indices&#160;of&#160;axis&#160;objects;   
If&#160;axes&#160;is&#160;not&#160;None,&#160;include&#160;only&#160;certain&#160;axes.  
less&#160;the&#160;ones&#160;specified&#160;in&#160;omit.&#160;If&#160;axes&#160;is&#160;None,  
use&#160;all&#160;axes&#160;of&#160;this&#160;variable.  
Other&#160;specificiations&#160;are&#160;as&#160;for&#160;axisMatchIndex. `

 getConvention  (self) 
     ` Get&#160;the&#160;metadata&#160;convention&#160;associated&#160;with&#160;this&#160;object. `

 getGridIndices  (self) 
     ` Return&#160;a&#160;tuple&#160;of&#160;indices&#160;corresponding&#160;to&#160;the&#160;variable&#160;grid. `

 getLatitude  (self) 
     ` Get&#160;the&#160;first&#160;latitude&#160;dimension,&#160;or&#160;None&#160;if&#160;not&#160;found. `

 getLevel  (self) 
     ` Get&#160;the&#160;first&#160;vertical&#160;level&#160;dimension&#160;in&#160;the&#160;domain,   
or&#160;None&#160;if&#160;not&#160;found. `

 getLongitude  (self) 
     ` Get&#160;the&#160;first&#160;latitude&#160;dimension,&#160;or&#160;None&#160;if&#160;not&#160;found. `

 getMissing  (self, asarray  =0  ) 
     ` Return&#160;the&#160;missing&#160;value&#160;as&#160;a&#160;scalar,&#160;or&#160;as   
a&#160;Numeric&#160;array&#160;if&#160;asarray==1 `

 getOrder  (self, ids  =0  ) 
     ` [ getOrder ](/) (ids=0)&#160;returns&#160;the&#160;order&#160;string,&#160;such&#160;as&#160;tzyx.   
  
if&#160;ids&#160;==&#160;0&#160;(the&#160;default)&#160;for&#160;an&#160;axis&#160;that&#160;is&#160;not&#160;t,z,x,y  
the&#160;order&#160;string&#160;will&#160;contain&#160;a&#160;'-'&#160;in&#160;that&#160;location.  
The&#160;result&#160;string&#160;will&#160;be&#160;of&#160;the&#160;same&#160;length&#160;as&#160;the&#160;number  
of&#160;axes.&#160;This&#160;makes&#160;it&#160;easy&#160;to&#160;loop&#160;over&#160;the&#160;dimensions.  
  
if&#160;ids&#160;==&#160;1&#160;those&#160;axes&#160;will&#160;be&#160;represented&#160;in&#160;the&#160;order  
string&#160;as&#160;(id)&#160;where&#160;id&#160;is&#160;that&#160;axis'&#160;id.&#160;The&#160;result&#160;will  
be&#160;suitable&#160;for&#160;passing&#160;to&#160;order2index&#160;to&#160;get&#160;the  
corresponding&#160;axes,&#160;and&#160;to&#160;orderparse&#160;for&#160;dividing&#160;up&#160;into  
components. `

 getRegion  (self, *specs, keys) 
     ` getRegion   
Read&#160;a&#160;region&#160;of&#160;data.&#160;A&#160;region&#160;is&#160;an&#160;n-dimensional  
rectangular&#160;region&#160;specified&#160;in&#160;coordinate&#160;space.  
'slices'&#160;is&#160;an&#160;argument&#160;list,&#160;each&#160;item&#160;of&#160;which&#160;has&#160;one&#160;of&#160;the&#160;following
forms:  
-&#160;x,&#160;where&#160;x&#160;is&#160;a&#160;scalar   
Map&#160;the&#160;scalar&#160;to&#160;the&#160;index&#160;of&#160;the&#160;closest&#160;coordinate&#160;value  
-&#160;(x,y)   
Map&#160;the&#160;half-open&#160;coordinate&#160;interval&#160;[x,y)&#160;to&#160;index&#160;interval  
-&#160;(x,y,'cc')   
Map&#160;the&#160;closed&#160;interval&#160;[x,y]&#160;to&#160;index&#160;interval.&#160;Other&#160;options&#160;are&#160;'oo'
(open),  
'oc'&#160;(open&#160;on&#160;the&#160;left),&#160;and&#160;'co'&#160;(open&#160;on&#160;the&#160;right,&#160;the&#160;default).  
-&#160;(x,y,'co',cycle)   
Map&#160;the&#160;coordinate&#160;interval&#160;with&#160;wraparound.&#160;If&#160;no&#160;cycle&#160;is&#160;specified,
wraparound  
will&#160;occur&#160;iff&#160;axis.isCircular()&#160;is&#160;true.  
NOTE:&#160;Only&#160;one&#160;dimension&#160;may&#160;be&#160;wrapped.  
-&#160;Ellipsis   
Represents&#160;the&#160;full&#160;range&#160;of&#160;all&#160;dimensions&#160;bracketed&#160;by&#160;non-Ellipsis&#160;items.  
-&#160;':'&#160;or&#160;None   
Represents&#160;the&#160;full&#160;range&#160;of&#160;one&#160;dimension.  
  
For&#160;example,&#160;suppose&#160;the&#160;variable&#160;domain&#160;is&#160;(time,level,lat,lon).&#160;Then  
  
[ getRegion ](/) ((10,20),850,Ellipsis,(-180,180))  
  
retrieves:  
-&#160;all&#160;times&#160;t&#160;such&#160;that&#160;10.<=t<20\.   
-&#160;level&#160;850   
-&#160;all&#160;values&#160;of&#160;all&#160;dimensions&#160;between&#160;level&#160;and&#160;lon&#160;(namely,&#160;lat)   
-&#160;longitudes&#160;x&#160;such&#160;that&#160;-180<=x<180.&#160;This&#160;will&#160;be&#160;wrapped&#160;unless   
lon.topology=='linear' `

 getSlice  (self, *specs, keys) 
     ` x.getSlice&#160;takes&#160;arguments&#160;of&#160;the&#160;following&#160;forms&#160;and&#160;produces   
a&#160;return&#160;array.&#160;The&#160;keyword&#160;argument&#160;squeeze&#160;determines&#160;whether  
or&#160;not&#160;the&#160;shape&#160;of&#160;the&#160;returned&#160;array&#160;contains&#160;dimensions&#160;whose  
length&#160;is&#160;1;&#160;by&#160;default&#160;this&#160;argument&#160;is&#160;1,&#160;and&#160;such&#160;dimensions  
are&#160;'squeezed&#160;out'.  
There&#160;can&#160;be&#160;zero&#160;or&#160;more&#160;positional&#160;arguments,&#160;each&#160;of&#160;the&#160;form:  
(a)&#160;a&#160;single&#160;integer&#160;n,&#160;meaning&#160;slice(n,&#160;n+1)  
(b)&#160;an&#160;instance&#160;of&#160;the&#160;slice&#160;class  
(c)&#160;a&#160;tuple,&#160;which&#160;will&#160;be&#160;used&#160;as&#160;arguments&#160;to&#160;create&#160;a&#160;slice  
(d)&#160;None&#160;or&#160;':',&#160;which&#160;means&#160;a&#160;slice&#160;covering&#160;that&#160;entire&#160;dimension  
(e)&#160;Ellipsis&#160;(...),&#160;which&#160;means&#160;to&#160;fill&#160;the&#160;slice&#160;list&#160;with&#160;':'  
leaving&#160;only&#160;enough&#160;room&#160;at&#160;the&#160;end&#160;for&#160;the&#160;remaining  
positional&#160;arguments  
There&#160;can&#160;be&#160;keyword&#160;arguments&#160;of&#160;the&#160;form&#160;key&#160;=&#160;value,&#160;where  
key&#160;can&#160;be&#160;one&#160;of&#160;the&#160;names&#160;'time',&#160;'level',&#160;'latitude',&#160;or  
'longitude'.&#160;The&#160;corresponding&#160;value&#160;can&#160;be&#160;any&#160;of&#160;(a)-(d)&#160;above.  
  
There&#160;must&#160;be&#160;no&#160;conflict&#160;between&#160;the&#160;positional&#160;arguments&#160;and  
the&#160;keywords.  
  
In&#160;(a)-(c)&#160;negative&#160;numbers&#160;are&#160;treated&#160;as&#160;offsets&#160;from&#160;the&#160;end  
of&#160;that&#160;dimension,&#160;as&#160;in&#160;normal&#160;Python&#160;indexing. `

 getTime  (self) 
     ` Get&#160;the&#160;first&#160;time&#160;dimension,&#160;or&#160;None&#160;if&#160;not&#160;found `

 pressureRegrid  (self, newLevel, missing  =None  , order  =None  , method  ='log'  ) 
     ` Return&#160;the&#160;variable&#160;regridded&#160;to&#160;new&#160;pressure&#160;levels.   
The&#160;variable&#160;should&#160;be&#160;a&#160;function&#160;of&#160;lat,&#160;lon,&#160;pressure,&#160;and&#160;(optionally)
time.  
<newLevel>&#160;is&#160;an&#160;axis&#160;of&#160;the&#160;result&#160;pressure&#160;levels.  
<method>&#160;is&#160;optional,&#160;either&#160;"log"&#160;to&#160;interpolate&#160;in&#160;the&#160;log&#160;of&#160;pressure
(default),  
or&#160;"linear"&#160;for&#160;linear&#160;interpolation.  
<missing>&#160;and&#160;<order>&#160;are&#160;as&#160;for&#160;regrid.PressureRegridder. `

 rank  (self) 

 reg_specs2slices  (self, initspeclist, force  =None  ) 

 regrid  (self, togrid, missing  =None  , order  =None  , mask  =None  ) 
     ` return&#160;self&#160;regridded&#160;to&#160;the&#160;new&#160;grid.&#160;Keyword&#160;arguments   
are&#160;as&#160;for&#160;regrid.Regridder. `

 reorder  (self, order) 
     ` return&#160;self&#160;reordered&#160;per&#160;the&#160;specification&#160;order `

 select  = __call__(self, *args, kwargs) 
     ` Selection&#160;of&#160;a&#160;subregion&#160;using&#160;selectors `

 setGrid  (self, grid) 
     ` #&#160;Set&#160;the&#160;variable&#160;grid `

 specs2slices  (self, speclist, force  =None  ) 
     ` Create&#160;an&#160;equivalent&#160;list&#160;of&#160;slices&#160;from&#160;an&#160;index&#160;specification   
An&#160;index&#160;specification&#160;is&#160;a&#160;list&#160;of&#160;acceptable&#160;items,&#160;which&#160;are  
\--&#160;an&#160;integer  
\--&#160;a&#160;slice&#160;instance&#160;(slice(start,&#160;stop,&#160;stride))  
\--&#160;the&#160;object&#160;"unspecified"  
\--&#160;the&#160;object&#160;None  
\--&#160;a&#160;colon  
The&#160;size&#160;of&#160;the&#160;speclist&#160;must&#160;be [ rank ](/) () `

 subRegion  (self, *specs, keys) 

* * *

Methods inherited from [ cdms.cdmsobj.CdmsObj ](/cdms.cdmsobj.html) :  

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

* * *

Methods inherited from [ cdms.slabinterface.Slab ](/cdms.slabinterface.html) :  

 createattribute  (self, name, value) 
     ` Create&#160;an&#160;attribute&#160;and&#160;set&#160;its&#160;name&#160;to&#160;value. `

 deleteattribute  (self, name) 
     ` Delete&#160;the&#160;named&#160;attribute. `

 getattribute  (self, name) 
     ` Get&#160;the&#160;attribute&#160;name. `

 getdimattribute  (self, dim, field) 
     ` Get&#160;the&#160;attribute&#160;named&#160;field&#160;from&#160;the&#160;dim'th&#160;dimension.   
For&#160;bounds&#160;returns&#160;the&#160;old&#160;cu&#160;one-dimensional&#160;version. `

 listattributes  (self) 
     ` Return&#160;a&#160;list&#160;of&#160;attribute&#160;names. `

 listdimattributes  (self, dim) 
     ` List&#160;the&#160;legal&#160;axis&#160;field&#160;names. `

 listdimnames  (self) 
     ` Return&#160;a&#160;list&#160;of&#160;the&#160;names&#160;of&#160;the&#160;dimensions. `

 setattribute  (self, name, value) 
     ` Set&#160;the&#160;attribute&#160;name&#160;to&#160;value. `

 showdim  (self) 
     ` Show&#160;the&#160;dimension&#160;attributes&#160;and&#160;values. `

* * *

Data and other attributes inherited from [ cdms.slabinterface.Slab
](/cdms.slabinterface.html) :  

 std_slab_atts  = ['filename', 'missing_value', 'comments', 'grid_name', 'grid_type', 'time_statistic', 'long_name', 'units'] 

* * *

Methods inherited from [ MA.MA.MaskedArray ](/MA.MA.html) :  

 __and__  (self, other) 
     ` Return&#160;bitwise_and `

 __float__  (self) 
     ` Convert&#160;self&#160;to&#160;float. `

 __floordiv__  (self, other) 
     ` Return&#160;divide(self,&#160;other) `

 __int__  (self) 
     ` Convert&#160;self&#160;to&#160;int. `

 __mod__  (self, other) 
     ` Return&#160;remainder(self,&#160;other) `

 __or__  (self, other) 
     ` Return&#160;bitwise_or `

 __pos__  (self) 
     ` Return&#160;array(self) `

 __rand__  = __and__(self, other) 
     ` Return&#160;bitwise_and `

 __rfloordiv__  (self, other) 
     ` Return&#160;divide(other,&#160;self) `

 __rmod__  (self, other) 
     ` Return&#160;remainder(other,&#160;self) `

 __ror__  = __or__(self, other) 
     ` Return&#160;bitwise_or `

 __rtruediv__  (self, other) 
     ` Return&#160;divide(other,&#160;self) `

 __rxor__  = __xor__(self, other) 
     ` Return&#160;bitwise_xor `

 __setitem__  (self, index, value) 
     ` Set&#160;item&#160;described&#160;by&#160;index.&#160;If&#160;value&#160;is&#160;masked,&#160;mask&#160;those&#160;locations. `

 __setslice__  (self, i, j, value) 
     ` Set&#160;slice&#160;i:j;&#160;if&#160;value&#160;is&#160;masked,&#160;mask&#160;those&#160;locations. `

 __truediv__  (self, other) 
     ` Return&#160;divide(self,&#160;other) `

 __xor__  (self, other) 
     ` Return&#160;bitwise_xor `

 byte_swapped  (self) 
     ` Returns&#160;the&#160;raw&#160;data&#160;field,&#160;byte_swapped.&#160;Included&#160;for&#160;consistency   
with&#160;Numeric&#160;but&#160;doesn't&#160;make&#160;sense&#160;in&#160;this&#160;context. `

 compressed  (self) 
     ` A&#160;1-D&#160;array&#160;of&#160;all&#160;the&#160;non-masked&#160;data. `

 dot  (self, other) 
     ` s. [ dot ](/) (other)&#160;=&#160;innerproduct(s,&#160;other) `

 fill_value  (self) 
     ` Get&#160;the&#160;current&#160;fill&#160;value. `

 filled  (self, fill_value  =None  ) 
     ` A&#160;Numeric&#160;array&#160;with&#160;masked&#160;values&#160;filled.&#160;If&#160;fill_value&#160;is&#160;None,   
use [ fill_value ](/) ().  
  
If&#160;mask&#160;is&#160;None,&#160;copy&#160;data&#160;only&#160;if&#160;not&#160;contiguous.  
Result&#160;is&#160;always&#160;a&#160;contiguous,&#160;Numeric&#160;array. `

 ids  (self) 
     ` Return&#160;the&#160;ids&#160;of&#160;the&#160;data&#160;and&#160;mask&#160;areas `

 iscontiguous  (self) 
     ` Is&#160;the&#160;data&#160;contiguous? `

 itemsize  (self) 
     ` Item&#160;size&#160;of&#160;each&#160;data&#160;item. `

 mask  (self) 
     ` Return&#160;the&#160;data&#160;mask,&#160;or&#160;None.&#160;Result&#160;contiguous. `

 outer  (self, other) 
     ` s. [ outer ](/) (other)&#160;=&#160;outerproduct(s,&#160;other) `

 put  (self, values) 
     ` Set&#160;the&#160;non-masked&#160;entries&#160;of&#160;self&#160;to [ filled ](/) (values).   
No&#160;change&#160;to&#160;mask `

 putmask  (self, values) 
     ` Set&#160;the&#160;masked&#160;entries&#160;of&#160;self&#160;to [ filled ](/) (values).   
Mask&#160;changed&#160;to&#160;None. `

 raw_data  (self) 
     ` The&#160;raw&#160;data;&#160;portions&#160;may&#160;be&#160;meaningless.   
May&#160;be&#160;noncontiguous.&#160;Expert&#160;use&#160;only. `

 raw_mask  (self) 
     ` The&#160;raw&#160;mask;&#160;portions&#160;may&#160;be&#160;meaningless.   
May&#160;be&#160;noncontiguous.&#160;Expert&#160;use&#160;only. `

 savespace  (self, value) 
     ` Set&#160;the&#160;spacesaver&#160;attribute&#160;to&#160;value `

 spacesaver  (self) 
     ` [ spacesaver ](/) ()&#160;queries&#160;the&#160;spacesaver&#160;attribute. `

 tolist  (self, fill_value  =None  ) 
     ` Convert&#160;to&#160;list `

 tostring  (self, fill_value  =None  ) 
     ` Convert&#160;to&#160;string `

 unmask  (self) 
     ` Replace&#160;the&#160;mask&#160;by&#160;None&#160;if&#160;possible. `

 unshare_mask  (self) 
     ` If&#160;currently&#160;sharing&#160;mask,&#160;make&#160;a&#160;copy. `

* * *

Properties inherited from [ MA.MA.MaskedArray ](/MA.MA.html) :  

 flat 
     ` Access&#160;array&#160;in&#160;flat&#160;form. `
    

 _ get _  = _get_flat(self) 
     ` Calculate&#160;the&#160;flat&#160;value. `
    

 _ set _  = _set_flat(self, value) 
     ` x.flat&#160;=&#160;value `

 imag 
     ` Access&#160;the&#160;imaginary&#160;part&#160;of&#160;the&#160;array `
    

 _ get _  = _get_imaginary(self) 
     ` Get&#160;the&#160;imaginary&#160;part&#160;of&#160;a&#160;complex&#160;array. `
    

 _ set _  = _set_imaginary(self, value) 
     ` x.imaginary&#160;=&#160;value `

 imaginary 
     ` Access&#160;the&#160;imaginary&#160;part&#160;of&#160;the&#160;array `
    

 _ get _  = _get_imaginary(self) 
     ` Get&#160;the&#160;imaginary&#160;part&#160;of&#160;a&#160;complex&#160;array. `
    

 _ set _  = _set_imaginary(self, value) 
     ` x.imaginary&#160;=&#160;value `

 real 
     ` Access&#160;the&#160;real&#160;part&#160;of&#160;the&#160;array `
    

 _ get _  = _get_real(self) 
     ` Get&#160;the&#160;real&#160;part&#160;of&#160;a&#160;complex&#160;array. `
    

 _ set _  = _set_real(self, value) 
     ` x.real&#160;=&#160;value `

 shape 
     ` tuple&#160;giving&#160;the&#160;shape&#160;of&#160;the&#160;array `
    

 _ get _  = _get_shape(self) 
     ` Return&#160;the&#160;current&#160;shape. `
    

 _ set _  = _set_shape(self, newshape) 
     ` Set&#160;the&#160;array's&#160;shape. `

* * *

Data and other attributes inherited from [ MA.MA.MaskedArray ](/MA.MA.html) :  

 __dict__  = <dictproxy object>
     ` dictionary&#160;for&#160;instance&#160;variables&#160;(if&#160;defined) `

 __weakref__  = <attribute '__weakref__' of 'MaskedArray' objects>
     ` list&#160;of&#160;weak&#160;references&#160;to&#160;the&#160;object&#160;(if&#160;defined) `

 handler_cache_key  = 'MA.MaskedArray' 

* * *

UCRL-WEB-213937 | [ Privacy & Legal Notice ](/disclaimer.html)

[ webmaster@pcmdi.llnl.gov ](/webmaster@pcmdi.llnl.gov)

[ ![Powered by Plone](media/plone_powered.gif) ](/)

