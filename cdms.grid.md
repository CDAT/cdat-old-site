---
layout: default
title:
---

 [ Skip to content. ](/cdat/source/api-reference/cdms.grid.html) | [ Skip to
navigation ](/cdat/source/api-reference/cdms.grid.html)

Search Site

[ Advanced Search&#8230; ](/search_form)

#  [ PCMDI Software Portal ](/)

#####  Sections

  * [ Home ](/)

#####  Personal tools

  * [ Log in ](/login_form)

You are here:  [ Home ](/) -> [ CDAT ](/cdat) -> [ Source Code ](/cdat/source)
-> [ API Reference ](/cdat/source/api-reference) -> Python: module cdms.grid

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

        * [ Python: module cdms.grid ](/cdat/source/api-reference/cdms.grid.html)

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

  * [ ![Send this page to somebody](media/mail_icon.gif) ](/cdat/source/api-reference/cdms.grid.html/sendto_form)
  * [ ![Print this page](media/print_icon.gif) ](/this.print\(\))

#  Python: module cdms.grid

  
  
 [ cdms  ](/cdms.html) .grid 
[ index ](/)  

` CDMS&#160;Grid&#160;objects `

  
 Modules 

` `

[ Numeric ](/Numeric.html)  
[ PropertiedClasses ](/PropertiedClasses.html)  
[ cdtime ](/cdtime.html)  

[ copy ](/copy.html)  
[ cdms.internattr ](/cdms.internattr.html)  
[ regrid ](/regrid.html)  

[ string ](/string.html)  
[ sys ](/sys.html)  
[ types ](/types.html)  

  
 Classes 

` `

[ cdms.cdmsobj.CdmsObj ](/cdms.cdmsobj.html) ( [
cdms.internattr.InternalAttributesClass ](/cdms.internattr.html) )

    

[ AbstractGrid ](/cdms.grid.html)

    

[ AbstractRectGrid ](/cdms.grid.html)

    

[ FileRectGrid ](/cdms.grid.html)

[ RectGrid ](/cdms.grid.html)

[ TransientRectGrid ](/cdms.grid.html)

  
class  AbstractGrid  ( [ cdms.cdmsobj.CdmsObj ](/cdms.cdmsobj.html) )

` `

Method resolution order:

     [ AbstractGrid ](/cdms.grid.html)
     [ cdms.cdmsobj.CdmsObj ](/cdms.cdmsobj.html)
     [ cdms.internattr.InternalAttributesClass ](/cdms.internattr.html)
     [ PropertiedClasses.Properties.PropertiedClass ](/PropertiedClasses.Properties.html)

* * *

Methods defined here:  

 __init__  (self, node) 

 __repr__  = [ __str__ ](/) (self) 

 __str__  (self) 

 checkAxes  (self, axes) 
     ` Return&#160;1&#160;iff&#160;self.  getAxisList  and&#160;axes&#160;are&#160;consistent. `

 clone  (self, copyData  =1  ) 
     ` Make&#160;a&#160;copy&#160;of&#160;self. `

 flatAxes  (self) 
     ` Return&#160;(flatlat,&#160;flatlon)&#160;where&#160;flatlat&#160;is&#160;a&#160;raveled&#160;NumPy&#160;array   
having&#160;the&#160;same&#160;length&#160;as&#160;the&#160;number&#160;of&#160;cells&#160;in&#160;the&#160;grid,&#160;similarly  
for&#160;flatlon. `

 getAxisList  (self) 

 hasCoordType  (self, coordType) 
     ` Return&#160;1&#160;iff&#160;self&#160;has&#160;the&#160;coordinate&#160;type. `

 info  (self, flag  =None  , device  =None  ) 
     ` Write&#160;info&#160;about&#160;slab;&#160;include&#160;dimension&#160;values&#160;and&#160;weights&#160;if&#160;flag `

 isClose  (self, g) 
     ` Return&#160;1&#160;if&#160;g&#160;is&#160;'close&#160;enough'&#160;to&#160;self&#160;to&#160;be&#160;considered&#160;equal,&#160;0&#160;if&#160;not. `

 listall  (self, all  =None  ) 

 reconcile  (self, axes) 
     ` Return&#160;a&#160;grid&#160;that&#160;is&#160;consistent&#160;with&#160;the&#160;axes,&#160;or&#160;None. `

 size  (self) 
     ` Return&#160;number&#160;of&#160;cells&#160;in&#160;the&#160;grid `

 subSlice  (self, *specs, keys) 
     ` Get&#160;a&#160;subgrid&#160;based&#160;on&#160;an&#160;argument&#160;list&#160;<specs>&#160;of&#160;slices. `

 writeScrip  (self, cdunifFile) 
     ` Write&#160;a&#160;grid&#160;to&#160;a&#160;SCRIP&#160;file `

 writeToFile  (self, file) 
     ` Write&#160;self&#160;to&#160;a&#160;CdmsFile&#160;file,&#160;returning&#160;CF&#160;coordinates&#160;attribute,&#160;or&#160;None&#160;if&#160;not&#160;applicable `

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

  
class  AbstractRectGrid  ( [ AbstractGrid ](/cdms.grid.html) )

` `

` [ AbstractRectGrid ](/) defines&#160;the&#160;interface&#160;for&#160;rectilinear&#160;grids:  
grids&#160;which&#160;can&#160;be&#160;decomposed&#160;into&#160;1-D&#160;latitude&#160;and&#160;longitude&#160;axes  
`

Method resolution order:

     [ AbstractRectGrid ](/cdms.grid.html)
     [ AbstractGrid ](/cdms.grid.html)
     [ cdms.cdmsobj.CdmsObj ](/cdms.cdmsobj.html)
     [ cdms.internattr.InternalAttributesClass ](/cdms.internattr.html)
     [ PropertiedClasses.Properties.PropertiedClass ](/PropertiedClasses.Properties.html)

* * *

Methods defined here:  

 __init__  (self, node) 

 classify  (self) 
     ` #&#160;Generate&#160;a&#160;best&#160;guess&#160;at&#160;grid&#160;info&#160;for&#160;a&#160;single&#160;grid   
#&#160;Return&#160;a&#160;tuple&#160;(type,nlats,isoffset)&#160;where:  
#&#160;&#160;&#160;type&#160;==&#160;('gaussian'&#160;|&#160;'equalarea'&#160;|&#160;'uniform'&#160;|&#160;'generic')  
#&#160;&#160;&#160;nlats&#160;is&#160;the&#160;number&#160;of&#160;latitudes&#160;of&#160;the&#160;grid:  
#&#160;&#160;&#160;&#160;&#160;if&#160;gaussian,&#160;the&#160;gaussian&#160;nlats&#160;minus&#160;pole&#160;values  
#&#160;&#160;&#160;&#160;&#160;if&#160;equalarea,&#160;the&#160;equalarea&#160;nlats&#160;minus&#160;pole&#160;values  
#&#160;&#160;&#160;isoffset&#160;is&#160;true&#160;iff&#160;this&#160;is&#160;a&#160;BOUNDARY&#160;grid,&#160;hence&#160;the&#160;bounds  
#&#160;&#160;&#160;&#160;&#160;are&#160;the&#160;points&#160;wrt&#160;nlat,&#160;plus&#160;the&#160;poles. `

 classifyInFamily  (self, gridlist) 
     ` #&#160;Generate&#160;a&#160;best&#160;guess&#160;at&#160;grid&#160;info&#160;within&#160;a&#160;family&#160;of&#160;grids&#160;(list&#160;of&#160;grids)   
#&#160;Return&#160;a&#160;tuple&#160;(type,coverage,nlats,isoffset,&#160;basegrid,&#160;latindex)&#160;where:  
#&#160;&#160;&#160;type&#160;==&#160;('gaussian'&#160;|&#160;'equalarea'&#160;|&#160;'uniform'&#160;|&#160;'generic')  
#&#160;&#160;&#160;coverage&#160;==&#160;('global'&#160;|&#160;'regional')  
#&#160;&#160;&#160;nlats&#160;is&#160;the&#160;number&#160;of&#160;latitudes&#160;of&#160;the&#160;FULL&#160;grid:  
#&#160;&#160;&#160;&#160;&#160;if&#160;gaussian,&#160;the&#160;gaussian&#160;nlats&#160;minus&#160;pole&#160;values  
#&#160;&#160;&#160;&#160;&#160;if&#160;equalarea,&#160;the&#160;equalarea&#160;nlats&#160;minus&#160;pole&#160;values  
#&#160;&#160;&#160;&#160;&#160;if&#160;regional,&#160;nlats&#160;for&#160;the&#160;full&#160;grid,&#160;of&#160;which&#160;this&#160;is&#160;a&#160;subset  
#&#160;&#160;&#160;&#160;&#160;if&#160;offset,&#160;nlats&#160;for&#160;which&#160;this&#160;is&#160;the&#160;BOUNDARY&#160;grid  
#&#160;&#160;&#160;isoffset&#160;is&#160;true&#160;iff&#160;this&#160;is&#160;a&#160;BOUNDARY&#160;grid,&#160;hence&#160;the&#160;bounds  
#&#160;&#160;&#160;&#160;&#160;are&#160;the&#160;points&#160;wrt&#160;nlat,&#160;plus&#160;the&#160;poles.  
#&#160;&#160;&#160;basegrid&#160;is&#160;the&#160;full&#160;grid,&#160;if&#160;this&#160;is&#160;regional,&#160;or&#160;None  
#&#160;&#160;&#160;latindex&#160;is&#160;index&#160;into&#160;basegrid&#160;latitude,&#160;or&#160;None `

 flatAxes  (self) 
     ` Return&#160;(flatlat,&#160;flatlon)&#160;where&#160;flatlat&#160;is&#160;a&#160;1D&#160;NumPy&#160;array   
having&#160;the&#160;same&#160;length&#160;as&#160;the&#160;number&#160;of&#160;cells&#160;in&#160;the&#160;grid,&#160;similarly  
for&#160;flatlon. `

 genBounds  (self) 
     ` #&#160;Generate&#160;default&#160;bounds `

 getAxis  (self, naxis) 
     ` #&#160;Get&#160;the&#160;n-th&#160;axis.&#160;naxis&#160;is&#160;0&#160;or&#160;1\. `

 getBounds  (self) 

 getLatitude  (self) 

 getLongitude  (self) 

 getMask  (self) 

 getMesh  (self) 
     ` Generate&#160;a&#160;mesh&#160;array&#160;for&#160;the&#160;meshfill&#160;graphics&#160;method. `

 getOrder  (self) 

 getType  (self) 

 getWeights  (self) 
     ` #&#160;Return&#160;normalized&#160;area&#160;weights,&#160;as&#160;latWeights,&#160;lonWeights:   
#&#160;&#160;&#160;latWeights[i]&#160;=&#160;0.5&#160;*&#160;abs(sin(latBnds[i+1])&#160;-&#160;sin(latBnds[i]))  
#&#160;&#160;&#160;lonWeights[i]&#160;=&#160;abs(lonBnds[i+1]&#160;-&#160;lonBnds[i])/360.0  
#&#160;Assumes&#160;that&#160;both&#160;axes&#160;are&#160;represented&#160;in&#160;degrees. `

 listall  (self, all  =None  ) 

 setMask  (self, mask, permanent  =0  ) 

 setType  (self, gridtype) 

 size  (self) 

 subGrid  (self, latinterval, loninterval) 
     ` #&#160;Create&#160;a&#160;transient&#160;grid&#160;for&#160;the&#160;index&#160;(tuple)&#160;intervals. `

 subGridRegion  (self, latRegion, lonRegion) 
     ` #&#160;Same&#160;as&#160;subGrid,&#160;for&#160;coordinates `

 toCurveGrid  (self, gridid  =None  ) 
     ` Convert&#160;to&#160;a&#160;curvilinear&#160;grid.   
'gridid'&#160;is&#160;the&#160;string&#160;identifier&#160;of&#160;the&#160;resulting&#160;curvilinear&#160;grid&#160;object. `

 toGenericGrid  (self, gridid  =None  ) 

 transpose  (self) 
     ` #&#160;Return&#160;a&#160;transient&#160;grid&#160;which&#160;is&#160;the&#160;transpose&#160;of&#160;this&#160;grid `

 writeScrip  (self, cufile, gridTitle  =None  ) 
     ` Write&#160;a&#160;grid&#160;to&#160;a&#160;SCRIP&#160;file.   
cufile&#160;is&#160;a&#160;Cdunif&#160;file,&#160;NOT&#160;a&#160;CDMS&#160;file.  
gridtitle&#160;is&#160;a&#160;string&#160;identifying&#160;the&#160;grid. `

 writeToFile  (self, file) 

* * *

Data and other attributes defined here:  

 gridtypes  = ['gaussian', 'uniform', 'equalarea', 'generic'] 

* * *

Methods inherited from [ AbstractGrid ](/cdms.grid.html) :  

 __repr__  = __str__(self) 

 __str__  (self) 

 checkAxes  (self, axes) 
     ` Return&#160;1&#160;iff&#160;self.  getAxisList  and&#160;axes&#160;are&#160;consistent. `

 clone  (self, copyData  =1  ) 
     ` Make&#160;a&#160;copy&#160;of&#160;self. `

 getAxisList  (self) 

 hasCoordType  (self, coordType) 
     ` Return&#160;1&#160;iff&#160;self&#160;has&#160;the&#160;coordinate&#160;type. `

 info  (self, flag  =None  , device  =None  ) 
     ` Write&#160;info&#160;about&#160;slab;&#160;include&#160;dimension&#160;values&#160;and&#160;weights&#160;if&#160;flag `

 isClose  (self, g) 
     ` Return&#160;1&#160;if&#160;g&#160;is&#160;'close&#160;enough'&#160;to&#160;self&#160;to&#160;be&#160;considered&#160;equal,&#160;0&#160;if&#160;not. `

 reconcile  (self, axes) 
     ` Return&#160;a&#160;grid&#160;that&#160;is&#160;consistent&#160;with&#160;the&#160;axes,&#160;or&#160;None. `

 subSlice  (self, *specs, keys) 
     ` Get&#160;a&#160;subgrid&#160;based&#160;on&#160;an&#160;argument&#160;list&#160;<specs>&#160;of&#160;slices. `

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

  
class  FileRectGrid  ( [ AbstractRectGrid ](/cdms.grid.html) )

` `

Method resolution order:

     [ FileRectGrid ](/cdms.grid.html)
     [ AbstractRectGrid ](/cdms.grid.html)
     [ AbstractGrid ](/cdms.grid.html)
     [ cdms.cdmsobj.CdmsObj ](/cdms.cdmsobj.html)
     [ cdms.internattr.InternalAttributesClass ](/cdms.internattr.html)
     [ PropertiedClasses.Properties.PropertiedClass ](/PropertiedClasses.Properties.html)

* * *

Methods defined here:  

 __init__  (self, parent, gridname, latobj, lonobj, order, gridtype, maskobj  =None  , tempMask  =None  ) 

 getMask  (self) 
     ` #&#160;Return&#160;the&#160;mask&#160;array&#160;(NOT&#160;the&#160;mask&#160;variable). `

 getMaskVar  (self) 

 setBounds  (self, latBounds, lonBounds, persistent  =0  ) 
     ` #&#160;Set&#160;bounds.&#160;If&#160;persistent==1,&#160;write&#160;to&#160;file,&#160;else&#160;just&#160;shadow&#160;any&#160;file&#160;boundaries. `

 setMask  (self, mask, persistent  =0  ) 
     ` #&#160;Set&#160;the&#160;mask&#160;to&#160;array&#160;'mask'.&#160;If&#160;persistent&#160;==&#160;1,&#160;modify&#160;permanently   
#&#160;in&#160;the&#160;file,&#160;else&#160;set&#160;as&#160;a&#160;temporary&#160;mask. `

* * *

Methods inherited from [ AbstractRectGrid ](/cdms.grid.html) :  

 classify  (self) 
     ` #&#160;Generate&#160;a&#160;best&#160;guess&#160;at&#160;grid&#160;info&#160;for&#160;a&#160;single&#160;grid   
#&#160;Return&#160;a&#160;tuple&#160;(type,nlats,isoffset)&#160;where:  
#&#160;&#160;&#160;type&#160;==&#160;('gaussian'&#160;|&#160;'equalarea'&#160;|&#160;'uniform'&#160;|&#160;'generic')  
#&#160;&#160;&#160;nlats&#160;is&#160;the&#160;number&#160;of&#160;latitudes&#160;of&#160;the&#160;grid:  
#&#160;&#160;&#160;&#160;&#160;if&#160;gaussian,&#160;the&#160;gaussian&#160;nlats&#160;minus&#160;pole&#160;values  
#&#160;&#160;&#160;&#160;&#160;if&#160;equalarea,&#160;the&#160;equalarea&#160;nlats&#160;minus&#160;pole&#160;values  
#&#160;&#160;&#160;isoffset&#160;is&#160;true&#160;iff&#160;this&#160;is&#160;a&#160;BOUNDARY&#160;grid,&#160;hence&#160;the&#160;bounds  
#&#160;&#160;&#160;&#160;&#160;are&#160;the&#160;points&#160;wrt&#160;nlat,&#160;plus&#160;the&#160;poles. `

 classifyInFamily  (self, gridlist) 
     ` #&#160;Generate&#160;a&#160;best&#160;guess&#160;at&#160;grid&#160;info&#160;within&#160;a&#160;family&#160;of&#160;grids&#160;(list&#160;of&#160;grids)   
#&#160;Return&#160;a&#160;tuple&#160;(type,coverage,nlats,isoffset,&#160;basegrid,&#160;latindex)&#160;where:  
#&#160;&#160;&#160;type&#160;==&#160;('gaussian'&#160;|&#160;'equalarea'&#160;|&#160;'uniform'&#160;|&#160;'generic')  
#&#160;&#160;&#160;coverage&#160;==&#160;('global'&#160;|&#160;'regional')  
#&#160;&#160;&#160;nlats&#160;is&#160;the&#160;number&#160;of&#160;latitudes&#160;of&#160;the&#160;FULL&#160;grid:  
#&#160;&#160;&#160;&#160;&#160;if&#160;gaussian,&#160;the&#160;gaussian&#160;nlats&#160;minus&#160;pole&#160;values  
#&#160;&#160;&#160;&#160;&#160;if&#160;equalarea,&#160;the&#160;equalarea&#160;nlats&#160;minus&#160;pole&#160;values  
#&#160;&#160;&#160;&#160;&#160;if&#160;regional,&#160;nlats&#160;for&#160;the&#160;full&#160;grid,&#160;of&#160;which&#160;this&#160;is&#160;a&#160;subset  
#&#160;&#160;&#160;&#160;&#160;if&#160;offset,&#160;nlats&#160;for&#160;which&#160;this&#160;is&#160;the&#160;BOUNDARY&#160;grid  
#&#160;&#160;&#160;isoffset&#160;is&#160;true&#160;iff&#160;this&#160;is&#160;a&#160;BOUNDARY&#160;grid,&#160;hence&#160;the&#160;bounds  
#&#160;&#160;&#160;&#160;&#160;are&#160;the&#160;points&#160;wrt&#160;nlat,&#160;plus&#160;the&#160;poles.  
#&#160;&#160;&#160;basegrid&#160;is&#160;the&#160;full&#160;grid,&#160;if&#160;this&#160;is&#160;regional,&#160;or&#160;None  
#&#160;&#160;&#160;latindex&#160;is&#160;index&#160;into&#160;basegrid&#160;latitude,&#160;or&#160;None `

 flatAxes  (self) 
     ` Return&#160;(flatlat,&#160;flatlon)&#160;where&#160;flatlat&#160;is&#160;a&#160;1D&#160;NumPy&#160;array   
having&#160;the&#160;same&#160;length&#160;as&#160;the&#160;number&#160;of&#160;cells&#160;in&#160;the&#160;grid,&#160;similarly  
for&#160;flatlon. `

 genBounds  (self) 
     ` #&#160;Generate&#160;default&#160;bounds `

 getAxis  (self, naxis) 
     ` #&#160;Get&#160;the&#160;n-th&#160;axis.&#160;naxis&#160;is&#160;0&#160;or&#160;1\. `

 getBounds  (self) 

 getLatitude  (self) 

 getLongitude  (self) 

 getMesh  (self) 
     ` Generate&#160;a&#160;mesh&#160;array&#160;for&#160;the&#160;meshfill&#160;graphics&#160;method. `

 getOrder  (self) 

 getType  (self) 

 getWeights  (self) 
     ` #&#160;Return&#160;normalized&#160;area&#160;weights,&#160;as&#160;latWeights,&#160;lonWeights:   
#&#160;&#160;&#160;latWeights[i]&#160;=&#160;0.5&#160;*&#160;abs(sin(latBnds[i+1])&#160;-&#160;sin(latBnds[i]))  
#&#160;&#160;&#160;lonWeights[i]&#160;=&#160;abs(lonBnds[i+1]&#160;-&#160;lonBnds[i])/360.0  
#&#160;Assumes&#160;that&#160;both&#160;axes&#160;are&#160;represented&#160;in&#160;degrees. `

 listall  (self, all  =None  ) 

 setType  (self, gridtype) 

 size  (self) 

 subGrid  (self, latinterval, loninterval) 
     ` #&#160;Create&#160;a&#160;transient&#160;grid&#160;for&#160;the&#160;index&#160;(tuple)&#160;intervals. `

 subGridRegion  (self, latRegion, lonRegion) 
     ` #&#160;Same&#160;as&#160;subGrid,&#160;for&#160;coordinates `

 toCurveGrid  (self, gridid  =None  ) 
     ` Convert&#160;to&#160;a&#160;curvilinear&#160;grid.   
'gridid'&#160;is&#160;the&#160;string&#160;identifier&#160;of&#160;the&#160;resulting&#160;curvilinear&#160;grid&#160;object. `

 toGenericGrid  (self, gridid  =None  ) 

 transpose  (self) 
     ` #&#160;Return&#160;a&#160;transient&#160;grid&#160;which&#160;is&#160;the&#160;transpose&#160;of&#160;this&#160;grid `

 writeScrip  (self, cufile, gridTitle  =None  ) 
     ` Write&#160;a&#160;grid&#160;to&#160;a&#160;SCRIP&#160;file.   
cufile&#160;is&#160;a&#160;Cdunif&#160;file,&#160;NOT&#160;a&#160;CDMS&#160;file.  
gridtitle&#160;is&#160;a&#160;string&#160;identifying&#160;the&#160;grid. `

 writeToFile  (self, file) 

* * *

Data and other attributes inherited from [ AbstractRectGrid ](/cdms.grid.html)
:  

 gridtypes  = ['gaussian', 'uniform', 'equalarea', 'generic'] 

* * *

Methods inherited from [ AbstractGrid ](/cdms.grid.html) :  

 __repr__  = __str__(self) 

 __str__  (self) 

 checkAxes  (self, axes) 
     ` Return&#160;1&#160;iff&#160;self.  getAxisList  and&#160;axes&#160;are&#160;consistent. `

 clone  (self, copyData  =1  ) 
     ` Make&#160;a&#160;copy&#160;of&#160;self. `

 getAxisList  (self) 

 hasCoordType  (self, coordType) 
     ` Return&#160;1&#160;iff&#160;self&#160;has&#160;the&#160;coordinate&#160;type. `

 info  (self, flag  =None  , device  =None  ) 
     ` Write&#160;info&#160;about&#160;slab;&#160;include&#160;dimension&#160;values&#160;and&#160;weights&#160;if&#160;flag `

 isClose  (self, g) 
     ` Return&#160;1&#160;if&#160;g&#160;is&#160;'close&#160;enough'&#160;to&#160;self&#160;to&#160;be&#160;considered&#160;equal,&#160;0&#160;if&#160;not. `

 reconcile  (self, axes) 
     ` Return&#160;a&#160;grid&#160;that&#160;is&#160;consistent&#160;with&#160;the&#160;axes,&#160;or&#160;None. `

 subSlice  (self, *specs, keys) 
     ` Get&#160;a&#160;subgrid&#160;based&#160;on&#160;an&#160;argument&#160;list&#160;<specs>&#160;of&#160;slices. `

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

  
class  RectGrid  ( [ AbstractRectGrid ](/cdms.grid.html) )

` `

Method resolution order:

     [ RectGrid ](/cdms.grid.html)
     [ AbstractRectGrid ](/cdms.grid.html)
     [ AbstractGrid ](/cdms.grid.html)
     [ cdms.cdmsobj.CdmsObj ](/cdms.cdmsobj.html)
     [ cdms.internattr.InternalAttributesClass ](/cdms.internattr.html)
     [ PropertiedClasses.Properties.PropertiedClass ](/PropertiedClasses.Properties.html)

* * *

Methods defined here:  

 __init__  (self, parent, rectgridNode  =None  ) 

 getMask  (self) 

 getMaskVar  (self) 

 initDomain  (self, axisdict, vardict) 
     ` #&#160;Set&#160;pointers&#160;to&#160;related&#160;structural&#160;elements:&#160;lon,&#160;lat&#160;axes,&#160;order,&#160;mask `

* * *

Methods inherited from [ AbstractRectGrid ](/cdms.grid.html) :  

 classify  (self) 
     ` #&#160;Generate&#160;a&#160;best&#160;guess&#160;at&#160;grid&#160;info&#160;for&#160;a&#160;single&#160;grid   
#&#160;Return&#160;a&#160;tuple&#160;(type,nlats,isoffset)&#160;where:  
#&#160;&#160;&#160;type&#160;==&#160;('gaussian'&#160;|&#160;'equalarea'&#160;|&#160;'uniform'&#160;|&#160;'generic')  
#&#160;&#160;&#160;nlats&#160;is&#160;the&#160;number&#160;of&#160;latitudes&#160;of&#160;the&#160;grid:  
#&#160;&#160;&#160;&#160;&#160;if&#160;gaussian,&#160;the&#160;gaussian&#160;nlats&#160;minus&#160;pole&#160;values  
#&#160;&#160;&#160;&#160;&#160;if&#160;equalarea,&#160;the&#160;equalarea&#160;nlats&#160;minus&#160;pole&#160;values  
#&#160;&#160;&#160;isoffset&#160;is&#160;true&#160;iff&#160;this&#160;is&#160;a&#160;BOUNDARY&#160;grid,&#160;hence&#160;the&#160;bounds  
#&#160;&#160;&#160;&#160;&#160;are&#160;the&#160;points&#160;wrt&#160;nlat,&#160;plus&#160;the&#160;poles. `

 classifyInFamily  (self, gridlist) 
     ` #&#160;Generate&#160;a&#160;best&#160;guess&#160;at&#160;grid&#160;info&#160;within&#160;a&#160;family&#160;of&#160;grids&#160;(list&#160;of&#160;grids)   
#&#160;Return&#160;a&#160;tuple&#160;(type,coverage,nlats,isoffset,&#160;basegrid,&#160;latindex)&#160;where:  
#&#160;&#160;&#160;type&#160;==&#160;('gaussian'&#160;|&#160;'equalarea'&#160;|&#160;'uniform'&#160;|&#160;'generic')  
#&#160;&#160;&#160;coverage&#160;==&#160;('global'&#160;|&#160;'regional')  
#&#160;&#160;&#160;nlats&#160;is&#160;the&#160;number&#160;of&#160;latitudes&#160;of&#160;the&#160;FULL&#160;grid:  
#&#160;&#160;&#160;&#160;&#160;if&#160;gaussian,&#160;the&#160;gaussian&#160;nlats&#160;minus&#160;pole&#160;values  
#&#160;&#160;&#160;&#160;&#160;if&#160;equalarea,&#160;the&#160;equalarea&#160;nlats&#160;minus&#160;pole&#160;values  
#&#160;&#160;&#160;&#160;&#160;if&#160;regional,&#160;nlats&#160;for&#160;the&#160;full&#160;grid,&#160;of&#160;which&#160;this&#160;is&#160;a&#160;subset  
#&#160;&#160;&#160;&#160;&#160;if&#160;offset,&#160;nlats&#160;for&#160;which&#160;this&#160;is&#160;the&#160;BOUNDARY&#160;grid  
#&#160;&#160;&#160;isoffset&#160;is&#160;true&#160;iff&#160;this&#160;is&#160;a&#160;BOUNDARY&#160;grid,&#160;hence&#160;the&#160;bounds  
#&#160;&#160;&#160;&#160;&#160;are&#160;the&#160;points&#160;wrt&#160;nlat,&#160;plus&#160;the&#160;poles.  
#&#160;&#160;&#160;basegrid&#160;is&#160;the&#160;full&#160;grid,&#160;if&#160;this&#160;is&#160;regional,&#160;or&#160;None  
#&#160;&#160;&#160;latindex&#160;is&#160;index&#160;into&#160;basegrid&#160;latitude,&#160;or&#160;None `

 flatAxes  (self) 
     ` Return&#160;(flatlat,&#160;flatlon)&#160;where&#160;flatlat&#160;is&#160;a&#160;1D&#160;NumPy&#160;array   
having&#160;the&#160;same&#160;length&#160;as&#160;the&#160;number&#160;of&#160;cells&#160;in&#160;the&#160;grid,&#160;similarly  
for&#160;flatlon. `

 genBounds  (self) 
     ` #&#160;Generate&#160;default&#160;bounds `

 getAxis  (self, naxis) 
     ` #&#160;Get&#160;the&#160;n-th&#160;axis.&#160;naxis&#160;is&#160;0&#160;or&#160;1\. `

 getBounds  (self) 

 getLatitude  (self) 

 getLongitude  (self) 

 getMesh  (self) 
     ` Generate&#160;a&#160;mesh&#160;array&#160;for&#160;the&#160;meshfill&#160;graphics&#160;method. `

 getOrder  (self) 

 getType  (self) 

 getWeights  (self) 
     ` #&#160;Return&#160;normalized&#160;area&#160;weights,&#160;as&#160;latWeights,&#160;lonWeights:   
#&#160;&#160;&#160;latWeights[i]&#160;=&#160;0.5&#160;*&#160;abs(sin(latBnds[i+1])&#160;-&#160;sin(latBnds[i]))  
#&#160;&#160;&#160;lonWeights[i]&#160;=&#160;abs(lonBnds[i+1]&#160;-&#160;lonBnds[i])/360.0  
#&#160;Assumes&#160;that&#160;both&#160;axes&#160;are&#160;represented&#160;in&#160;degrees. `

 listall  (self, all  =None  ) 

 setMask  (self, mask, permanent  =0  ) 

 setType  (self, gridtype) 

 size  (self) 

 subGrid  (self, latinterval, loninterval) 
     ` #&#160;Create&#160;a&#160;transient&#160;grid&#160;for&#160;the&#160;index&#160;(tuple)&#160;intervals. `

 subGridRegion  (self, latRegion, lonRegion) 
     ` #&#160;Same&#160;as&#160;subGrid,&#160;for&#160;coordinates `

 toCurveGrid  (self, gridid  =None  ) 
     ` Convert&#160;to&#160;a&#160;curvilinear&#160;grid.   
'gridid'&#160;is&#160;the&#160;string&#160;identifier&#160;of&#160;the&#160;resulting&#160;curvilinear&#160;grid&#160;object. `

 toGenericGrid  (self, gridid  =None  ) 

 transpose  (self) 
     ` #&#160;Return&#160;a&#160;transient&#160;grid&#160;which&#160;is&#160;the&#160;transpose&#160;of&#160;this&#160;grid `

 writeScrip  (self, cufile, gridTitle  =None  ) 
     ` Write&#160;a&#160;grid&#160;to&#160;a&#160;SCRIP&#160;file.   
cufile&#160;is&#160;a&#160;Cdunif&#160;file,&#160;NOT&#160;a&#160;CDMS&#160;file.  
gridtitle&#160;is&#160;a&#160;string&#160;identifying&#160;the&#160;grid. `

 writeToFile  (self, file) 

* * *

Data and other attributes inherited from [ AbstractRectGrid ](/cdms.grid.html)
:  

 gridtypes  = ['gaussian', 'uniform', 'equalarea', 'generic'] 

* * *

Methods inherited from [ AbstractGrid ](/cdms.grid.html) :  

 __repr__  = __str__(self) 

 __str__  (self) 

 checkAxes  (self, axes) 
     ` Return&#160;1&#160;iff&#160;self.  getAxisList  and&#160;axes&#160;are&#160;consistent. `

 clone  (self, copyData  =1  ) 
     ` Make&#160;a&#160;copy&#160;of&#160;self. `

 getAxisList  (self) 

 hasCoordType  (self, coordType) 
     ` Return&#160;1&#160;iff&#160;self&#160;has&#160;the&#160;coordinate&#160;type. `

 info  (self, flag  =None  , device  =None  ) 
     ` Write&#160;info&#160;about&#160;slab;&#160;include&#160;dimension&#160;values&#160;and&#160;weights&#160;if&#160;flag `

 isClose  (self, g) 
     ` Return&#160;1&#160;if&#160;g&#160;is&#160;'close&#160;enough'&#160;to&#160;self&#160;to&#160;be&#160;considered&#160;equal,&#160;0&#160;if&#160;not. `

 reconcile  (self, axes) 
     ` Return&#160;a&#160;grid&#160;that&#160;is&#160;consistent&#160;with&#160;the&#160;axes,&#160;or&#160;None. `

 subSlice  (self, *specs, keys) 
     ` Get&#160;a&#160;subgrid&#160;based&#160;on&#160;an&#160;argument&#160;list&#160;<specs>&#160;of&#160;slices. `

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

  
class  TransientRectGrid  ( [ AbstractRectGrid ](/cdms.grid.html) )

` `

` Grids&#160;that&#160;live&#160;in&#160;memory&#160;only.  
`

Method resolution order:

     [ TransientRectGrid ](/cdms.grid.html)
     [ AbstractRectGrid ](/cdms.grid.html)
     [ AbstractGrid ](/cdms.grid.html)
     [ cdms.cdmsobj.CdmsObj ](/cdms.cdmsobj.html)
     [ cdms.internattr.InternalAttributesClass ](/cdms.internattr.html)
     [ PropertiedClasses.Properties.PropertiedClass ](/PropertiedClasses.Properties.html)

* * *

Methods defined here:  

 __init__  (self, latobj, lonobj, order, gridtype, maskarray  =None  ) 

 getMask  (self) 

 setBounds  (self, latBounds, lonBounds) 

 setMask  (self, mask, persistent  =0  ) 
     ` #&#160;Set&#160;the&#160;mask.&#160;The&#160;persistent&#160;argument&#160;is&#160;provided&#160;for&#160;compatibility   
#&#160;with&#160;persistent&#160;versions,&#160;is&#160;ignored. `

* * *

Methods inherited from [ AbstractRectGrid ](/cdms.grid.html) :  

 classify  (self) 
     ` #&#160;Generate&#160;a&#160;best&#160;guess&#160;at&#160;grid&#160;info&#160;for&#160;a&#160;single&#160;grid   
#&#160;Return&#160;a&#160;tuple&#160;(type,nlats,isoffset)&#160;where:  
#&#160;&#160;&#160;type&#160;==&#160;('gaussian'&#160;|&#160;'equalarea'&#160;|&#160;'uniform'&#160;|&#160;'generic')  
#&#160;&#160;&#160;nlats&#160;is&#160;the&#160;number&#160;of&#160;latitudes&#160;of&#160;the&#160;grid:  
#&#160;&#160;&#160;&#160;&#160;if&#160;gaussian,&#160;the&#160;gaussian&#160;nlats&#160;minus&#160;pole&#160;values  
#&#160;&#160;&#160;&#160;&#160;if&#160;equalarea,&#160;the&#160;equalarea&#160;nlats&#160;minus&#160;pole&#160;values  
#&#160;&#160;&#160;isoffset&#160;is&#160;true&#160;iff&#160;this&#160;is&#160;a&#160;BOUNDARY&#160;grid,&#160;hence&#160;the&#160;bounds  
#&#160;&#160;&#160;&#160;&#160;are&#160;the&#160;points&#160;wrt&#160;nlat,&#160;plus&#160;the&#160;poles. `

 classifyInFamily  (self, gridlist) 
     ` #&#160;Generate&#160;a&#160;best&#160;guess&#160;at&#160;grid&#160;info&#160;within&#160;a&#160;family&#160;of&#160;grids&#160;(list&#160;of&#160;grids)   
#&#160;Return&#160;a&#160;tuple&#160;(type,coverage,nlats,isoffset,&#160;basegrid,&#160;latindex)&#160;where:  
#&#160;&#160;&#160;type&#160;==&#160;('gaussian'&#160;|&#160;'equalarea'&#160;|&#160;'uniform'&#160;|&#160;'generic')  
#&#160;&#160;&#160;coverage&#160;==&#160;('global'&#160;|&#160;'regional')  
#&#160;&#160;&#160;nlats&#160;is&#160;the&#160;number&#160;of&#160;latitudes&#160;of&#160;the&#160;FULL&#160;grid:  
#&#160;&#160;&#160;&#160;&#160;if&#160;gaussian,&#160;the&#160;gaussian&#160;nlats&#160;minus&#160;pole&#160;values  
#&#160;&#160;&#160;&#160;&#160;if&#160;equalarea,&#160;the&#160;equalarea&#160;nlats&#160;minus&#160;pole&#160;values  
#&#160;&#160;&#160;&#160;&#160;if&#160;regional,&#160;nlats&#160;for&#160;the&#160;full&#160;grid,&#160;of&#160;which&#160;this&#160;is&#160;a&#160;subset  
#&#160;&#160;&#160;&#160;&#160;if&#160;offset,&#160;nlats&#160;for&#160;which&#160;this&#160;is&#160;the&#160;BOUNDARY&#160;grid  
#&#160;&#160;&#160;isoffset&#160;is&#160;true&#160;iff&#160;this&#160;is&#160;a&#160;BOUNDARY&#160;grid,&#160;hence&#160;the&#160;bounds  
#&#160;&#160;&#160;&#160;&#160;are&#160;the&#160;points&#160;wrt&#160;nlat,&#160;plus&#160;the&#160;poles.  
#&#160;&#160;&#160;basegrid&#160;is&#160;the&#160;full&#160;grid,&#160;if&#160;this&#160;is&#160;regional,&#160;or&#160;None  
#&#160;&#160;&#160;latindex&#160;is&#160;index&#160;into&#160;basegrid&#160;latitude,&#160;or&#160;None `

 flatAxes  (self) 
     ` Return&#160;(flatlat,&#160;flatlon)&#160;where&#160;flatlat&#160;is&#160;a&#160;1D&#160;NumPy&#160;array   
having&#160;the&#160;same&#160;length&#160;as&#160;the&#160;number&#160;of&#160;cells&#160;in&#160;the&#160;grid,&#160;similarly  
for&#160;flatlon. `

 genBounds  (self) 
     ` #&#160;Generate&#160;default&#160;bounds `

 getAxis  (self, naxis) 
     ` #&#160;Get&#160;the&#160;n-th&#160;axis.&#160;naxis&#160;is&#160;0&#160;or&#160;1\. `

 getBounds  (self) 

 getLatitude  (self) 

 getLongitude  (self) 

 getMesh  (self) 
     ` Generate&#160;a&#160;mesh&#160;array&#160;for&#160;the&#160;meshfill&#160;graphics&#160;method. `

 getOrder  (self) 

 getType  (self) 

 getWeights  (self) 
     ` #&#160;Return&#160;normalized&#160;area&#160;weights,&#160;as&#160;latWeights,&#160;lonWeights:   
#&#160;&#160;&#160;latWeights[i]&#160;=&#160;0.5&#160;*&#160;abs(sin(latBnds[i+1])&#160;-&#160;sin(latBnds[i]))  
#&#160;&#160;&#160;lonWeights[i]&#160;=&#160;abs(lonBnds[i+1]&#160;-&#160;lonBnds[i])/360.0  
#&#160;Assumes&#160;that&#160;both&#160;axes&#160;are&#160;represented&#160;in&#160;degrees. `

 listall  (self, all  =None  ) 

 setType  (self, gridtype) 

 size  (self) 

 subGrid  (self, latinterval, loninterval) 
     ` #&#160;Create&#160;a&#160;transient&#160;grid&#160;for&#160;the&#160;index&#160;(tuple)&#160;intervals. `

 subGridRegion  (self, latRegion, lonRegion) 
     ` #&#160;Same&#160;as&#160;subGrid,&#160;for&#160;coordinates `

 toCurveGrid  (self, gridid  =None  ) 
     ` Convert&#160;to&#160;a&#160;curvilinear&#160;grid.   
'gridid'&#160;is&#160;the&#160;string&#160;identifier&#160;of&#160;the&#160;resulting&#160;curvilinear&#160;grid&#160;object. `

 toGenericGrid  (self, gridid  =None  ) 

 transpose  (self) 
     ` #&#160;Return&#160;a&#160;transient&#160;grid&#160;which&#160;is&#160;the&#160;transpose&#160;of&#160;this&#160;grid `

 writeScrip  (self, cufile, gridTitle  =None  ) 
     ` Write&#160;a&#160;grid&#160;to&#160;a&#160;SCRIP&#160;file.   
cufile&#160;is&#160;a&#160;Cdunif&#160;file,&#160;NOT&#160;a&#160;CDMS&#160;file.  
gridtitle&#160;is&#160;a&#160;string&#160;identifying&#160;the&#160;grid. `

 writeToFile  (self, file) 

* * *

Data and other attributes inherited from [ AbstractRectGrid ](/cdms.grid.html)
:  

 gridtypes  = ['gaussian', 'uniform', 'equalarea', 'generic'] 

* * *

Methods inherited from [ AbstractGrid ](/cdms.grid.html) :  

 __repr__  = __str__(self) 

 __str__  (self) 

 checkAxes  (self, axes) 
     ` Return&#160;1&#160;iff&#160;self.  getAxisList  and&#160;axes&#160;are&#160;consistent. `

 clone  (self, copyData  =1  ) 
     ` Make&#160;a&#160;copy&#160;of&#160;self. `

 getAxisList  (self) 

 hasCoordType  (self, coordType) 
     ` Return&#160;1&#160;iff&#160;self&#160;has&#160;the&#160;coordinate&#160;type. `

 info  (self, flag  =None  , device  =None  ) 
     ` Write&#160;info&#160;about&#160;slab;&#160;include&#160;dimension&#160;values&#160;and&#160;weights&#160;if&#160;flag `

 isClose  (self, g) 
     ` Return&#160;1&#160;if&#160;g&#160;is&#160;'close&#160;enough'&#160;to&#160;self&#160;to&#160;be&#160;considered&#160;equal,&#160;0&#160;if&#160;not. `

 reconcile  (self, axes) 
     ` Return&#160;a&#160;grid&#160;that&#160;is&#160;consistent&#160;with&#160;the&#160;axes,&#160;or&#160;None. `

 subSlice  (self, *specs, keys) 
     ` Get&#160;a&#160;subgrid&#160;based&#160;on&#160;an&#160;argument&#160;list&#160;<specs>&#160;of&#160;slices. `

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

  
 Functions 

` `

 createGaussianGrid  (nlats, xorigin  =0.0  , order  ='yx'  ) 
     ` [ createGaussianGrid ](/) (nlats,&#160;xorigin=0.0)   
Create&#160;a&#160;Gaussian&#160;grid,&#160;with&#160;shape&#160;(nlats,&#160;2*nlats).  
'nlats'&#160;is&#160;the&#160;number&#160;of&#160;latitudes.  
'xorigin'&#160;is&#160;the&#160;origin&#160;of&#160;the&#160;longitude&#160;axis.  
'order'&#160;is&#160;either&#160;"yx"&#160;or&#160;"xy" `

 createGenericGrid  (latArray, lonArray, latBounds  =None  , lonBounds  =None  , order  ='yx'  , mask  =None  ) 
     ` #&#160;Generate&#160;a&#160;generic&#160;(untyped)&#160;grid&#160;from&#160;lat,&#160;lon&#160;vectors `

 createGlobalMeanGrid  (grid) 
     ` #&#160;Generate&#160;a&#160;grid&#160;for&#160;calculating&#160;the&#160;global&#160;mean.&#160;The&#160;grid&#160;is&#160;a&#160;single   
#&#160;zone&#160;covering&#160;the&#160;range&#160;of&#160;the&#160;input&#160;grid `

 createRectGrid  (lat, lon, order  ='yx'  , type  ='generic'  , mask  =None  ) 
     ` #&#160;Create&#160;a&#160;transient&#160;rectilinear&#160;grid `

 createUniformGrid  (startLat, nlat, deltaLat, startLon, nlon, deltaLon, order  ='yx'  , mask  =None  ) 
     ` #&#160;Generate&#160;a&#160;uniform&#160;rectilinear&#160;grid `

 createZonalGrid  (grid) 
     ` #&#160;Generate&#160;a&#160;grid&#160;for&#160;zonal&#160;averaging.&#160;The&#160;grid&#160;has&#160;the&#160;same&#160;latitudes   
#&#160;as&#160;the&#160;input&#160;grid,&#160;and&#160;a&#160;single&#160;longitude. `

 defaultRegion  () 
     ` Return&#160;a&#160;specification&#160;for&#160;a&#160;default&#160;(full)&#160;region. `

 setClassifyGrids  (mode) 
     ` #&#160;Set&#160;grid&#160;classifiction&#160;mode.&#160;If&#160;on,&#160;gridtype&#160;is&#160;determined&#160;by&#160;the&#160;grid   
#&#160;classification&#160;method,&#160;regardless&#160;of&#160;the&#160;value&#160;of&#160;grid.getType().  
#&#160;(if&#160;any).&#160;If&#160;'off',&#160;the&#160;value&#160;of&#160;.grid_type&#160;overrides&#160;the&#160;classification. `

 setRegionSpecs  (grid, coordSpec, coordType, resultSpec) 
     ` Modify&#160;a&#160;list&#160;of&#160;coordinate&#160;specifications,&#160;given&#160;a&#160;coordinate&#160;type&#160;and   
a&#160;specification&#160;for&#160;that&#160;coordinate.  
'grid'&#160;is&#160;the&#160;grid&#160;object&#160;to&#160;be&#160;associated&#160;with&#160;the&#160;region.  
'coordSpec'&#160;is&#160;a&#160;coordinate&#160;specification,&#160;having&#160;one&#160;of&#160;the&#160;forms:  
  
x  
(x,y)  
(x,y,'co')  
(x,y,'co',cycle)  
':'  
None  
  
'coordType'&#160;is&#160;one&#160;of&#160;CoordinateTypes  
'resultSpec'&#160;is&#160;a&#160;list&#160;of&#160;4-tuples&#160;of&#160;the&#160;form&#160;(x,y,'co',cycle),&#160;or&#160;None  
if&#160;no&#160;spec&#160;for&#160;the&#160;corresponding&#160;dimension&#160;type.  
  
The&#160;function&#160;sets&#160;the&#160;appropriate&#160;coordinate&#160;in&#160;resultSpec,  
in&#160;the&#160;canonical&#160;form&#160;(x,y,'co',cycle).&#160;A&#160;CDMSError&#160;exception  
is&#160;raised&#160;if&#160;the&#160;entry&#160;in&#160;resultSpec&#160;is&#160;not&#160;None.  
  
Note&#160;that&#160;time&#160;coordinate&#160;types&#160;are&#160;not&#160;permitted. `

 writeScripGrid  (path, grid, gridTitle  =None  ) 
     ` Write&#160;a&#160;grid&#160;to&#160;a&#160;SCRIP&#160;grid&#160;file.   
path&#160;is&#160;the&#160;path&#160;of&#160;the&#160;SCRIP&#160;file&#160;to&#160;be&#160;created.  
grid&#160;is&#160;a&#160;CDMS&#160;grid&#160;object.  
gridTitle&#160;is&#160;a&#160;string&#160;ID&#160;for&#160;the&#160;grid. `

  
 Data 

` `

 CoordTypeToLoc  = {'lat': 1, 'lev': 2, 'lon': 0}   
 CoordinateTypes  = ['lon', 'lat', 'lev', 'time']   
 LatitudeType  = 'lat'   
 LongitudeType  = 'lon'   
 MethodNotImplemented  = 'Method not yet implemented'   
 TimeType  = 'time'   
 VerticalType  = 'lev' 

* * *

UCRL-WEB-213937 | [ Privacy & Legal Notice ](/disclaimer.html)

[ webmaster@pcmdi.llnl.gov ](/webmaster@pcmdi.llnl.gov)

[ ![Powered by Plone](media/plone_powered.gif) ](/)

