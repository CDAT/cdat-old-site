---
layout: default
title:
---

 [ Skip to content. ](/cdat/source/api-reference/cdms.hgrid.html) | [ Skip to
navigation ](/cdat/source/api-reference/cdms.hgrid.html)

Search Site

[ Advanced Search&#8230; ](/search_form)

#  [ PCMDI Software Portal ](/)

#####  Sections

  * [ Home ](/)

#####  Personal tools

  * [ Log in ](/login_form)

You are here:  [ Home ](/) -> [ CDAT ](/cdat) -> [ Source Code ](/cdat/source)
-> [ API Reference ](/cdat/source/api-reference) -> Python: module cdms.hgrid

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

        * [ Python: module cdms.hgrid ](/cdat/source/api-reference/cdms.hgrid.html)

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

  * [ ![Send this page to somebody](media/mail_icon.gif) ](/cdat/source/api-reference/cdms.hgrid.html/sendto_form)
  * [ ![Print this page](media/print_icon.gif) ](/this.print\(\))

#  Python: module cdms.hgrid

  
  
 [ cdms  ](/cdms.html) .hgrid 
[ index ](/)  

` CDMS&#160;HorizontalGrid&#160;objects `

  
 Modules 

` `

[ MA ](/MA.html)  

[ Numeric ](/Numeric.html)  

[ PropertiedClasses ](/PropertiedClasses.html)  

[ cdms.bindex ](/cdms.bindex.html)  

  
 Classes 

` `

[ cdms.grid.AbstractGrid ](/cdms.grid.html) ( [ cdms.cdmsobj.CdmsObj
](/cdms.cdmsobj.html) )

    

[ AbstractHorizontalGrid ](/cdms.hgrid.html)

    

[ AbstractCurveGrid ](/cdms.hgrid.html)

    

[ DatasetCurveGrid ](/cdms.hgrid.html)

[ FileCurveGrid ](/cdms.hgrid.html)

[ TransientCurveGrid ](/cdms.hgrid.html)

  
class  AbstractCurveGrid  ( [ AbstractHorizontalGrid ](/cdms.hgrid.html) )

` `

Method resolution order:

     [ AbstractCurveGrid ](/cdms.hgrid.html)
     [ AbstractHorizontalGrid ](/cdms.hgrid.html)
     [ cdms.grid.AbstractGrid ](/cdms.grid.html)
     [ cdms.cdmsobj.CdmsObj ](/cdms.cdmsobj.html)
     [ cdms.internattr.InternalAttributesClass ](/cdms.internattr.html)
     [ PropertiedClasses.Properties.PropertiedClass ](/PropertiedClasses.Properties.html)

* * *

Methods defined here:  

 __init__  (self, latAxis, lonAxis, id  =None  , maskvar  =None  , tempmask  =None  , node  =None  ) 
     ` Create&#160;a&#160;curvilinear&#160;grid. `

 __repr__  (self) 

 __str__  = [ __repr__ ](/) (self) 

 checkAxes  (self, axes) 
     ` Return&#160;1&#160;iff&#160;every&#160;element&#160;of [ getAxisList ](/) ()&#160;is&#160;in&#160;the&#160;list&#160;'axes'. `

 clone  (self, copyData  =1  ) 

 flatAxes  (self) 
     ` Return&#160;(flatlat,&#160;flatlon)&#160;where&#160;flatlat&#160;is&#160;a&#160;1D&#160;NumPy&#160;array   
having&#160;the&#160;same&#160;length&#160;as&#160;the&#160;number&#160;of&#160;cells&#160;in&#160;the&#160;grid,&#160;similarly  
for&#160;flatlon. `

 genBounds  (self) 
     ` #&#160;Don't&#160;try&#160;to&#160;generate&#160;bounds&#160;for&#160;curvilinear&#160;grids `

 getAxis  (self, naxis) 
     ` #&#160;Get&#160;the&#160;n-th&#160;index&#160;axis.&#160;naxis&#160;is&#160;0&#160;or&#160;1\. `

 getAxisList  (self) 

 getGridSlices  (self, domainlist, newaxislist, slicelist) 
     ` Determine&#160;which&#160;slices&#160;in&#160;slicelist&#160;correspond&#160;to&#160;the&#160;lat/lon&#160;elements   
of&#160;the&#160;grid.  
domainlist&#160;is&#160;a&#160;list&#160;of&#160;axes&#160;of&#160;a&#160;variable.  
newaxislist&#160;is&#160;a&#160;list&#160;of&#160;result&#160;axes&#160;after&#160;the&#160;slicelist&#160;is&#160;applied&#160;to
domainlist.  
slicelist&#160;is&#160;a&#160;list&#160;of&#160;slices.  
  
All&#160;lists&#160;are&#160;of&#160;equal&#160;length.  
  
Return&#160;value&#160;is&#160;(newslicelist,&#160;gridaxislist)&#160;where  
newslicelist&#160;is&#160;the&#160;elements&#160;of&#160;slicelist&#160;that&#160;correspond&#160;to&#160;the&#160;grid,&#160;in&#160;the  
preferred&#160;order&#160;of&#160;the&#160;grid.  
gridaxislist&#160;is&#160;the&#160;elements&#160;of&#160;newaxislist&#160;that&#160;correspond&#160;to&#160;the&#160;grid,&#160;in
the  
preferred&#160;order&#160;of&#160;the&#160;grid. `

 getIndex  (self) 
     ` Get&#160;the&#160;grid&#160;index `

 getMask  (self) 
     ` Get&#160;the&#160;mask&#160;array,&#160;if&#160;any,&#160;otherwise&#160;None&#160;is&#160;returned. `

 getMesh  (self, transpose  =None  ) 
     ` Generate&#160;a&#160;mesh&#160;array&#160;for&#160;the&#160;meshfill&#160;graphics&#160;method.   
If&#160;transpose&#160;is&#160;defined&#160;to&#160;a&#160;tuple,&#160;say&#160;(1,0),&#160;first&#160;transpose  
latbounds&#160;and&#160;lonbounds&#160;according&#160;to&#160;the&#160;tuple,&#160;(1,0,2)&#160;in&#160;this&#160;case. `

 intersect  (self, spec) 
     ` Intersect&#160;with&#160;the&#160;region&#160;specification.   
  
'spec'&#160;is&#160;a&#160;region&#160;specification&#160;of&#160;the&#160;form&#160;defined&#160;in&#160;the&#160;grid&#160;module.  
  
Returns&#160;(mask,&#160;indexspecs)&#160;where  
'mask'&#160;is&#160;the&#160;mask&#160;of&#160;the&#160;result&#160;grid&#160;AFTER&#160;self&#160;and&#160;region&#160;spec&#160;are
interested.  
'indexspecs'&#160;is&#160;a&#160;list&#160;of&#160;index&#160;specifications&#160;suitable&#160;for&#160;slicing&#160;a  
variable&#160;with&#160;the&#160;given&#160;grid. `

 isClose  (self, g) 
     ` Return&#160;1&#160;iff&#160;g&#160;is&#160;a&#160;grid&#160;of&#160;the&#160;same&#160;type&#160;and&#160;shape.&#160;A&#160;real&#160;element-by-element   
comparison&#160;would&#160;be&#160;too&#160;expensive&#160;here. `

 reconcile  (self, axes) 
     ` Return&#160;a&#160;grid&#160;that&#160;is&#160;consistent&#160;with&#160;the&#160;axes,&#160;or&#160;None.   
For&#160;curvilinear&#160;grids&#160;this&#160;means&#160;that&#160;the&#160;grid-related&#160;axes&#160;are  
contained&#160;in&#160;the&#160;'axes'&#160;list. `

 size  (self) 

 subSlice  (self, *specs, keys) 
     ` Get&#160;a&#160;transient&#160;subgrid&#160;based&#160;on&#160;an&#160;argument&#160;list&#160;<specs>&#160;of&#160;slices. `

 toCurveGrid  (self, gridid  =None  ) 

 toGenericGrid  (self, gridid  =None  ) 

 writeScrip  (self, cufile, gridTitle  =None  ) 
     ` Write&#160;a&#160;grid&#160;to&#160;a&#160;SCRIP&#160;file.   
cufile&#160;is&#160;a&#160;Cdunif&#160;file,&#160;NOT&#160;a&#160;CDMS&#160;file.  
gridtitle&#160;is&#160;a&#160;string&#160;identifying&#160;the&#160;grid. `

 writeToFile  (self, file) 

* * *

Methods inherited from [ AbstractHorizontalGrid ](/cdms.hgrid.html) :  

 checkConvex  (self) 
     ` Check&#160;that&#160;each&#160;cell&#160;of&#160;the&#160;grid&#160;is&#160;convex&#160;in&#160;lon-lat&#160;space,&#160;with&#160;nodes&#160;defined&#160;counter-clockwise.   
Return&#160;a&#160;1D&#160;Numeric&#160;array&#160;of&#160;cells&#160;that&#160;fail&#160;the&#160;cross-product&#160;test. `

 fixCutCells  (self, nonConvexCells, threshold  =270.0  ) 
     ` For&#160;any&#160;mapping&#160;from&#160;a&#160;spherical&#160;to&#160;a&#160;planar&#160;surface,&#160;there&#160;is&#160;a&#160;linear&#160;cut.   
Grid&#160;cells&#160;that&#160;span&#160;the&#160;cut&#160;may&#160;appear&#160;to&#160;be&#160;nonconvex,&#160;which&#160;causes  
problems&#160;with&#160;meshfill&#160;graphics.&#160;This&#160;routine&#160;attempts&#160;to&#160;'repair'&#160;the&#160;cut
cell  
boundaries&#160;so&#160;that&#160;meshfill&#160;recognizes&#160;they&#160;are&#160;convex.  
  
nonConvexCells:&#160;1D&#160;Numeric&#160;array&#160;of&#160;indices&#160;of&#160;nonconvex&#160;cells,&#160;as&#160;returned
from  
checkConvex.  
threshold:&#160;positive&#160;floating-point&#160;value&#160;in&#160;degrees.  
If&#160;the&#160;difference&#160;in&#160;longitude&#160;values&#160;of  
consecutive&#160;boundaries&#160;nodes&#160;exceeds&#160;the&#160;threshold,&#160;the&#160;cell&#160;is&#160;considered  
a&#160;cut&#160;cell.  
  
On&#160;return,&#160;the&#160;grid&#160;boundaries&#160;are&#160;modified.  
Return&#160;value&#160;is&#160;a&#160;1D&#160;array&#160;of&#160;indices&#160;of&#160;cells&#160;that&#160;cannot&#160;be&#160;repaired. `

 getBounds  (self) 
     ` Get&#160;the&#160;grid&#160;cell&#160;boundaries,&#160;as&#160;a&#160;tuple&#160;(latitudeBounds,&#160;longitudeBounds) `

 getLatitude  (self) 
     ` Get&#160;the&#160;latitude&#160;coordinates. `

 getLongitude  (self) 
     ` Get&#160;the&#160;longitude&#160;coordinates. `

 getWeightsArray  (self) 
     ` Return&#160;normalized&#160;area&#160;weights,&#160;as&#160;an&#160;array&#160;of&#160;the&#160;same   
shape&#160;as&#160;the&#160;grid. `

 hasCoordType  (self, coordType) 

 listall  (self, all  =None  ) 

 setMask  (self, mask, permanent  =0  ) 

 subGridRegion  (self, latRegion, lonRegion) 

* * *

Methods inherited from [ cdms.grid.AbstractGrid ](/cdms.grid.html) :  

 info  (self, flag  =None  , device  =None  ) 
     ` Write&#160;info&#160;about&#160;slab;&#160;include&#160;dimension&#160;values&#160;and&#160;weights&#160;if&#160;flag `

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

  
class  AbstractHorizontalGrid  ( [ cdms.grid.AbstractGrid
](/cdms.grid.html) )

` `

Method resolution order:

     [ AbstractHorizontalGrid ](/cdms.hgrid.html)
     [ cdms.grid.AbstractGrid ](/cdms.grid.html)
     [ cdms.cdmsobj.CdmsObj ](/cdms.cdmsobj.html)
     [ cdms.internattr.InternalAttributesClass ](/cdms.internattr.html)
     [ PropertiedClasses.Properties.PropertiedClass ](/PropertiedClasses.Properties.html)

* * *

Methods defined here:  

 __init__  (self, latAxis, lonAxis, id  =None  , maskvar  =None  , tempmask  =None  , node  =None  ) 
     ` Create&#160;a&#160;horizontal&#160;grid. `

 checkConvex  (self) 
     ` Check&#160;that&#160;each&#160;cell&#160;of&#160;the&#160;grid&#160;is&#160;convex&#160;in&#160;lon-lat&#160;space,&#160;with&#160;nodes&#160;defined&#160;counter-clockwise.   
Return&#160;a&#160;1D&#160;Numeric&#160;array&#160;of&#160;cells&#160;that&#160;fail&#160;the&#160;cross-product&#160;test. `

 fixCutCells  (self, nonConvexCells, threshold  =270.0  ) 
     ` For&#160;any&#160;mapping&#160;from&#160;a&#160;spherical&#160;to&#160;a&#160;planar&#160;surface,&#160;there&#160;is&#160;a&#160;linear&#160;cut.   
Grid&#160;cells&#160;that&#160;span&#160;the&#160;cut&#160;may&#160;appear&#160;to&#160;be&#160;nonconvex,&#160;which&#160;causes  
problems&#160;with&#160;meshfill&#160;graphics.&#160;This&#160;routine&#160;attempts&#160;to&#160;'repair'&#160;the&#160;cut
cell  
boundaries&#160;so&#160;that&#160;meshfill&#160;recognizes&#160;they&#160;are&#160;convex.  
  
nonConvexCells:&#160;1D&#160;Numeric&#160;array&#160;of&#160;indices&#160;of&#160;nonconvex&#160;cells,&#160;as&#160;returned
from  
checkConvex.  
threshold:&#160;positive&#160;floating-point&#160;value&#160;in&#160;degrees.  
If&#160;the&#160;difference&#160;in&#160;longitude&#160;values&#160;of  
consecutive&#160;boundaries&#160;nodes&#160;exceeds&#160;the&#160;threshold,&#160;the&#160;cell&#160;is&#160;considered  
a&#160;cut&#160;cell.  
  
On&#160;return,&#160;the&#160;grid&#160;boundaries&#160;are&#160;modified.  
Return&#160;value&#160;is&#160;a&#160;1D&#160;array&#160;of&#160;indices&#160;of&#160;cells&#160;that&#160;cannot&#160;be&#160;repaired. `

 genBounds  (self) 
     ` #&#160;Generate&#160;default&#160;bounds `

 getAxis  (self, naxis) 
     ` #&#160;Get&#160;the&#160;n-th&#160;axis.&#160;naxis&#160;is&#160;0&#160;or&#160;1\. `

 getBounds  (self) 
     ` Get&#160;the&#160;grid&#160;cell&#160;boundaries,&#160;as&#160;a&#160;tuple&#160;(latitudeBounds,&#160;longitudeBounds) `

 getLatitude  (self) 
     ` Get&#160;the&#160;latitude&#160;coordinates. `

 getLongitude  (self) 
     ` Get&#160;the&#160;longitude&#160;coordinates. `

 getMask  (self) 
     ` Get&#160;the&#160;mask&#160;array,&#160;if&#160;any,&#160;otherwise&#160;None&#160;is&#160;returned. `

 getMesh  (self) 
     ` Get&#160;the&#160;mesh&#160;array&#160;used&#160;by&#160;the&#160;meshfill&#160;plot. `

 getWeightsArray  (self) 
     ` Return&#160;normalized&#160;area&#160;weights,&#160;as&#160;an&#160;array&#160;of&#160;the&#160;same   
shape&#160;as&#160;the&#160;grid. `

 hasCoordType  (self, coordType) 

 listall  (self, all  =None  ) 

 setMask  (self, mask, permanent  =0  ) 

 subGridRegion  (self, latRegion, lonRegion) 

* * *

Methods inherited from [ cdms.grid.AbstractGrid ](/cdms.grid.html) :  

 __repr__  = __str__(self) 

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

 info  (self, flag  =None  , device  =None  ) 
     ` Write&#160;info&#160;about&#160;slab;&#160;include&#160;dimension&#160;values&#160;and&#160;weights&#160;if&#160;flag `

 isClose  (self, g) 
     ` Return&#160;1&#160;if&#160;g&#160;is&#160;'close&#160;enough'&#160;to&#160;self&#160;to&#160;be&#160;considered&#160;equal,&#160;0&#160;if&#160;not. `

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

  
class  DatasetCurveGrid  ( [ AbstractCurveGrid ](/cdms.hgrid.html) )

` `

Method resolution order:

     [ DatasetCurveGrid ](/cdms.hgrid.html)
     [ AbstractCurveGrid ](/cdms.hgrid.html)
     [ AbstractHorizontalGrid ](/cdms.hgrid.html)
     [ cdms.grid.AbstractGrid ](/cdms.grid.html)
     [ cdms.cdmsobj.CdmsObj ](/cdms.cdmsobj.html)
     [ cdms.internattr.InternalAttributesClass ](/cdms.internattr.html)
     [ PropertiedClasses.Properties.PropertiedClass ](/PropertiedClasses.Properties.html)

* * *

Methods defined here:  

 __init__  (self, latAxis, lonAxis, id, parent  =None  , maskvar  =None  , tempmask  =None  , node  =None  ) 
     ` Create&#160;a&#160;file&#160;curvilinear&#160;grid. `

 __repr__  (self) 

* * *

Methods inherited from [ AbstractCurveGrid ](/cdms.hgrid.html) :  

 __str__  = __repr__(self) 

 checkAxes  (self, axes) 
     ` Return&#160;1&#160;iff&#160;every&#160;element&#160;of [ getAxisList ](/) ()&#160;is&#160;in&#160;the&#160;list&#160;'axes'. `

 clone  (self, copyData  =1  ) 

 flatAxes  (self) 
     ` Return&#160;(flatlat,&#160;flatlon)&#160;where&#160;flatlat&#160;is&#160;a&#160;1D&#160;NumPy&#160;array   
having&#160;the&#160;same&#160;length&#160;as&#160;the&#160;number&#160;of&#160;cells&#160;in&#160;the&#160;grid,&#160;similarly  
for&#160;flatlon. `

 genBounds  (self) 
     ` #&#160;Don't&#160;try&#160;to&#160;generate&#160;bounds&#160;for&#160;curvilinear&#160;grids `

 getAxis  (self, naxis) 
     ` #&#160;Get&#160;the&#160;n-th&#160;index&#160;axis.&#160;naxis&#160;is&#160;0&#160;or&#160;1\. `

 getAxisList  (self) 

 getGridSlices  (self, domainlist, newaxislist, slicelist) 
     ` Determine&#160;which&#160;slices&#160;in&#160;slicelist&#160;correspond&#160;to&#160;the&#160;lat/lon&#160;elements   
of&#160;the&#160;grid.  
domainlist&#160;is&#160;a&#160;list&#160;of&#160;axes&#160;of&#160;a&#160;variable.  
newaxislist&#160;is&#160;a&#160;list&#160;of&#160;result&#160;axes&#160;after&#160;the&#160;slicelist&#160;is&#160;applied&#160;to
domainlist.  
slicelist&#160;is&#160;a&#160;list&#160;of&#160;slices.  
  
All&#160;lists&#160;are&#160;of&#160;equal&#160;length.  
  
Return&#160;value&#160;is&#160;(newslicelist,&#160;gridaxislist)&#160;where  
newslicelist&#160;is&#160;the&#160;elements&#160;of&#160;slicelist&#160;that&#160;correspond&#160;to&#160;the&#160;grid,&#160;in&#160;the  
preferred&#160;order&#160;of&#160;the&#160;grid.  
gridaxislist&#160;is&#160;the&#160;elements&#160;of&#160;newaxislist&#160;that&#160;correspond&#160;to&#160;the&#160;grid,&#160;in
the  
preferred&#160;order&#160;of&#160;the&#160;grid. `

 getIndex  (self) 
     ` Get&#160;the&#160;grid&#160;index `

 getMask  (self) 
     ` Get&#160;the&#160;mask&#160;array,&#160;if&#160;any,&#160;otherwise&#160;None&#160;is&#160;returned. `

 getMesh  (self, transpose  =None  ) 
     ` Generate&#160;a&#160;mesh&#160;array&#160;for&#160;the&#160;meshfill&#160;graphics&#160;method.   
If&#160;transpose&#160;is&#160;defined&#160;to&#160;a&#160;tuple,&#160;say&#160;(1,0),&#160;first&#160;transpose  
latbounds&#160;and&#160;lonbounds&#160;according&#160;to&#160;the&#160;tuple,&#160;(1,0,2)&#160;in&#160;this&#160;case. `

 intersect  (self, spec) 
     ` Intersect&#160;with&#160;the&#160;region&#160;specification.   
  
'spec'&#160;is&#160;a&#160;region&#160;specification&#160;of&#160;the&#160;form&#160;defined&#160;in&#160;the&#160;grid&#160;module.  
  
Returns&#160;(mask,&#160;indexspecs)&#160;where  
'mask'&#160;is&#160;the&#160;mask&#160;of&#160;the&#160;result&#160;grid&#160;AFTER&#160;self&#160;and&#160;region&#160;spec&#160;are
interested.  
'indexspecs'&#160;is&#160;a&#160;list&#160;of&#160;index&#160;specifications&#160;suitable&#160;for&#160;slicing&#160;a  
variable&#160;with&#160;the&#160;given&#160;grid. `

 isClose  (self, g) 
     ` Return&#160;1&#160;iff&#160;g&#160;is&#160;a&#160;grid&#160;of&#160;the&#160;same&#160;type&#160;and&#160;shape.&#160;A&#160;real&#160;element-by-element   
comparison&#160;would&#160;be&#160;too&#160;expensive&#160;here. `

 reconcile  (self, axes) 
     ` Return&#160;a&#160;grid&#160;that&#160;is&#160;consistent&#160;with&#160;the&#160;axes,&#160;or&#160;None.   
For&#160;curvilinear&#160;grids&#160;this&#160;means&#160;that&#160;the&#160;grid-related&#160;axes&#160;are  
contained&#160;in&#160;the&#160;'axes'&#160;list. `

 size  (self) 

 subSlice  (self, *specs, keys) 
     ` Get&#160;a&#160;transient&#160;subgrid&#160;based&#160;on&#160;an&#160;argument&#160;list&#160;<specs>&#160;of&#160;slices. `

 toCurveGrid  (self, gridid  =None  ) 

 toGenericGrid  (self, gridid  =None  ) 

 writeScrip  (self, cufile, gridTitle  =None  ) 
     ` Write&#160;a&#160;grid&#160;to&#160;a&#160;SCRIP&#160;file.   
cufile&#160;is&#160;a&#160;Cdunif&#160;file,&#160;NOT&#160;a&#160;CDMS&#160;file.  
gridtitle&#160;is&#160;a&#160;string&#160;identifying&#160;the&#160;grid. `

 writeToFile  (self, file) 

* * *

Methods inherited from [ AbstractHorizontalGrid ](/cdms.hgrid.html) :  

 checkConvex  (self) 
     ` Check&#160;that&#160;each&#160;cell&#160;of&#160;the&#160;grid&#160;is&#160;convex&#160;in&#160;lon-lat&#160;space,&#160;with&#160;nodes&#160;defined&#160;counter-clockwise.   
Return&#160;a&#160;1D&#160;Numeric&#160;array&#160;of&#160;cells&#160;that&#160;fail&#160;the&#160;cross-product&#160;test. `

 fixCutCells  (self, nonConvexCells, threshold  =270.0  ) 
     ` For&#160;any&#160;mapping&#160;from&#160;a&#160;spherical&#160;to&#160;a&#160;planar&#160;surface,&#160;there&#160;is&#160;a&#160;linear&#160;cut.   
Grid&#160;cells&#160;that&#160;span&#160;the&#160;cut&#160;may&#160;appear&#160;to&#160;be&#160;nonconvex,&#160;which&#160;causes  
problems&#160;with&#160;meshfill&#160;graphics.&#160;This&#160;routine&#160;attempts&#160;to&#160;'repair'&#160;the&#160;cut
cell  
boundaries&#160;so&#160;that&#160;meshfill&#160;recognizes&#160;they&#160;are&#160;convex.  
  
nonConvexCells:&#160;1D&#160;Numeric&#160;array&#160;of&#160;indices&#160;of&#160;nonconvex&#160;cells,&#160;as&#160;returned
from  
checkConvex.  
threshold:&#160;positive&#160;floating-point&#160;value&#160;in&#160;degrees.  
If&#160;the&#160;difference&#160;in&#160;longitude&#160;values&#160;of  
consecutive&#160;boundaries&#160;nodes&#160;exceeds&#160;the&#160;threshold,&#160;the&#160;cell&#160;is&#160;considered  
a&#160;cut&#160;cell.  
  
On&#160;return,&#160;the&#160;grid&#160;boundaries&#160;are&#160;modified.  
Return&#160;value&#160;is&#160;a&#160;1D&#160;array&#160;of&#160;indices&#160;of&#160;cells&#160;that&#160;cannot&#160;be&#160;repaired. `

 getBounds  (self) 
     ` Get&#160;the&#160;grid&#160;cell&#160;boundaries,&#160;as&#160;a&#160;tuple&#160;(latitudeBounds,&#160;longitudeBounds) `

 getLatitude  (self) 
     ` Get&#160;the&#160;latitude&#160;coordinates. `

 getLongitude  (self) 
     ` Get&#160;the&#160;longitude&#160;coordinates. `

 getWeightsArray  (self) 
     ` Return&#160;normalized&#160;area&#160;weights,&#160;as&#160;an&#160;array&#160;of&#160;the&#160;same   
shape&#160;as&#160;the&#160;grid. `

 hasCoordType  (self, coordType) 

 listall  (self, all  =None  ) 

 setMask  (self, mask, permanent  =0  ) 

 subGridRegion  (self, latRegion, lonRegion) 

* * *

Methods inherited from [ cdms.grid.AbstractGrid ](/cdms.grid.html) :  

 info  (self, flag  =None  , device  =None  ) 
     ` Write&#160;info&#160;about&#160;slab;&#160;include&#160;dimension&#160;values&#160;and&#160;weights&#160;if&#160;flag `

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

  
class  FileCurveGrid  ( [ AbstractCurveGrid ](/cdms.hgrid.html) )

` `

Method resolution order:

     [ FileCurveGrid ](/cdms.hgrid.html)
     [ AbstractCurveGrid ](/cdms.hgrid.html)
     [ AbstractHorizontalGrid ](/cdms.hgrid.html)
     [ cdms.grid.AbstractGrid ](/cdms.grid.html)
     [ cdms.cdmsobj.CdmsObj ](/cdms.cdmsobj.html)
     [ cdms.internattr.InternalAttributesClass ](/cdms.internattr.html)
     [ PropertiedClasses.Properties.PropertiedClass ](/PropertiedClasses.Properties.html)

* * *

Methods defined here:  

 __init__  (self, latAxis, lonAxis, id, parent  =None  , maskvar  =None  , tempmask  =None  , node  =None  ) 
     ` Create&#160;a&#160;file&#160;curvilinear&#160;grid. `

 __repr__  (self) 

* * *

Methods inherited from [ AbstractCurveGrid ](/cdms.hgrid.html) :  

 __str__  = __repr__(self) 

 checkAxes  (self, axes) 
     ` Return&#160;1&#160;iff&#160;every&#160;element&#160;of [ getAxisList ](/) ()&#160;is&#160;in&#160;the&#160;list&#160;'axes'. `

 clone  (self, copyData  =1  ) 

 flatAxes  (self) 
     ` Return&#160;(flatlat,&#160;flatlon)&#160;where&#160;flatlat&#160;is&#160;a&#160;1D&#160;NumPy&#160;array   
having&#160;the&#160;same&#160;length&#160;as&#160;the&#160;number&#160;of&#160;cells&#160;in&#160;the&#160;grid,&#160;similarly  
for&#160;flatlon. `

 genBounds  (self) 
     ` #&#160;Don't&#160;try&#160;to&#160;generate&#160;bounds&#160;for&#160;curvilinear&#160;grids `

 getAxis  (self, naxis) 
     ` #&#160;Get&#160;the&#160;n-th&#160;index&#160;axis.&#160;naxis&#160;is&#160;0&#160;or&#160;1\. `

 getAxisList  (self) 

 getGridSlices  (self, domainlist, newaxislist, slicelist) 
     ` Determine&#160;which&#160;slices&#160;in&#160;slicelist&#160;correspond&#160;to&#160;the&#160;lat/lon&#160;elements   
of&#160;the&#160;grid.  
domainlist&#160;is&#160;a&#160;list&#160;of&#160;axes&#160;of&#160;a&#160;variable.  
newaxislist&#160;is&#160;a&#160;list&#160;of&#160;result&#160;axes&#160;after&#160;the&#160;slicelist&#160;is&#160;applied&#160;to
domainlist.  
slicelist&#160;is&#160;a&#160;list&#160;of&#160;slices.  
  
All&#160;lists&#160;are&#160;of&#160;equal&#160;length.  
  
Return&#160;value&#160;is&#160;(newslicelist,&#160;gridaxislist)&#160;where  
newslicelist&#160;is&#160;the&#160;elements&#160;of&#160;slicelist&#160;that&#160;correspond&#160;to&#160;the&#160;grid,&#160;in&#160;the  
preferred&#160;order&#160;of&#160;the&#160;grid.  
gridaxislist&#160;is&#160;the&#160;elements&#160;of&#160;newaxislist&#160;that&#160;correspond&#160;to&#160;the&#160;grid,&#160;in
the  
preferred&#160;order&#160;of&#160;the&#160;grid. `

 getIndex  (self) 
     ` Get&#160;the&#160;grid&#160;index `

 getMask  (self) 
     ` Get&#160;the&#160;mask&#160;array,&#160;if&#160;any,&#160;otherwise&#160;None&#160;is&#160;returned. `

 getMesh  (self, transpose  =None  ) 
     ` Generate&#160;a&#160;mesh&#160;array&#160;for&#160;the&#160;meshfill&#160;graphics&#160;method.   
If&#160;transpose&#160;is&#160;defined&#160;to&#160;a&#160;tuple,&#160;say&#160;(1,0),&#160;first&#160;transpose  
latbounds&#160;and&#160;lonbounds&#160;according&#160;to&#160;the&#160;tuple,&#160;(1,0,2)&#160;in&#160;this&#160;case. `

 intersect  (self, spec) 
     ` Intersect&#160;with&#160;the&#160;region&#160;specification.   
  
'spec'&#160;is&#160;a&#160;region&#160;specification&#160;of&#160;the&#160;form&#160;defined&#160;in&#160;the&#160;grid&#160;module.  
  
Returns&#160;(mask,&#160;indexspecs)&#160;where  
'mask'&#160;is&#160;the&#160;mask&#160;of&#160;the&#160;result&#160;grid&#160;AFTER&#160;self&#160;and&#160;region&#160;spec&#160;are
interested.  
'indexspecs'&#160;is&#160;a&#160;list&#160;of&#160;index&#160;specifications&#160;suitable&#160;for&#160;slicing&#160;a  
variable&#160;with&#160;the&#160;given&#160;grid. `

 isClose  (self, g) 
     ` Return&#160;1&#160;iff&#160;g&#160;is&#160;a&#160;grid&#160;of&#160;the&#160;same&#160;type&#160;and&#160;shape.&#160;A&#160;real&#160;element-by-element   
comparison&#160;would&#160;be&#160;too&#160;expensive&#160;here. `

 reconcile  (self, axes) 
     ` Return&#160;a&#160;grid&#160;that&#160;is&#160;consistent&#160;with&#160;the&#160;axes,&#160;or&#160;None.   
For&#160;curvilinear&#160;grids&#160;this&#160;means&#160;that&#160;the&#160;grid-related&#160;axes&#160;are  
contained&#160;in&#160;the&#160;'axes'&#160;list. `

 size  (self) 

 subSlice  (self, *specs, keys) 
     ` Get&#160;a&#160;transient&#160;subgrid&#160;based&#160;on&#160;an&#160;argument&#160;list&#160;<specs>&#160;of&#160;slices. `

 toCurveGrid  (self, gridid  =None  ) 

 toGenericGrid  (self, gridid  =None  ) 

 writeScrip  (self, cufile, gridTitle  =None  ) 
     ` Write&#160;a&#160;grid&#160;to&#160;a&#160;SCRIP&#160;file.   
cufile&#160;is&#160;a&#160;Cdunif&#160;file,&#160;NOT&#160;a&#160;CDMS&#160;file.  
gridtitle&#160;is&#160;a&#160;string&#160;identifying&#160;the&#160;grid. `

 writeToFile  (self, file) 

* * *

Methods inherited from [ AbstractHorizontalGrid ](/cdms.hgrid.html) :  

 checkConvex  (self) 
     ` Check&#160;that&#160;each&#160;cell&#160;of&#160;the&#160;grid&#160;is&#160;convex&#160;in&#160;lon-lat&#160;space,&#160;with&#160;nodes&#160;defined&#160;counter-clockwise.   
Return&#160;a&#160;1D&#160;Numeric&#160;array&#160;of&#160;cells&#160;that&#160;fail&#160;the&#160;cross-product&#160;test. `

 fixCutCells  (self, nonConvexCells, threshold  =270.0  ) 
     ` For&#160;any&#160;mapping&#160;from&#160;a&#160;spherical&#160;to&#160;a&#160;planar&#160;surface,&#160;there&#160;is&#160;a&#160;linear&#160;cut.   
Grid&#160;cells&#160;that&#160;span&#160;the&#160;cut&#160;may&#160;appear&#160;to&#160;be&#160;nonconvex,&#160;which&#160;causes  
problems&#160;with&#160;meshfill&#160;graphics.&#160;This&#160;routine&#160;attempts&#160;to&#160;'repair'&#160;the&#160;cut
cell  
boundaries&#160;so&#160;that&#160;meshfill&#160;recognizes&#160;they&#160;are&#160;convex.  
  
nonConvexCells:&#160;1D&#160;Numeric&#160;array&#160;of&#160;indices&#160;of&#160;nonconvex&#160;cells,&#160;as&#160;returned
from  
checkConvex.  
threshold:&#160;positive&#160;floating-point&#160;value&#160;in&#160;degrees.  
If&#160;the&#160;difference&#160;in&#160;longitude&#160;values&#160;of  
consecutive&#160;boundaries&#160;nodes&#160;exceeds&#160;the&#160;threshold,&#160;the&#160;cell&#160;is&#160;considered  
a&#160;cut&#160;cell.  
  
On&#160;return,&#160;the&#160;grid&#160;boundaries&#160;are&#160;modified.  
Return&#160;value&#160;is&#160;a&#160;1D&#160;array&#160;of&#160;indices&#160;of&#160;cells&#160;that&#160;cannot&#160;be&#160;repaired. `

 getBounds  (self) 
     ` Get&#160;the&#160;grid&#160;cell&#160;boundaries,&#160;as&#160;a&#160;tuple&#160;(latitudeBounds,&#160;longitudeBounds) `

 getLatitude  (self) 
     ` Get&#160;the&#160;latitude&#160;coordinates. `

 getLongitude  (self) 
     ` Get&#160;the&#160;longitude&#160;coordinates. `

 getWeightsArray  (self) 
     ` Return&#160;normalized&#160;area&#160;weights,&#160;as&#160;an&#160;array&#160;of&#160;the&#160;same   
shape&#160;as&#160;the&#160;grid. `

 hasCoordType  (self, coordType) 

 listall  (self, all  =None  ) 

 setMask  (self, mask, permanent  =0  ) 

 subGridRegion  (self, latRegion, lonRegion) 

* * *

Methods inherited from [ cdms.grid.AbstractGrid ](/cdms.grid.html) :  

 info  (self, flag  =None  , device  =None  ) 
     ` Write&#160;info&#160;about&#160;slab;&#160;include&#160;dimension&#160;values&#160;and&#160;weights&#160;if&#160;flag `

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

  
class  TransientCurveGrid  ( [ AbstractCurveGrid ](/cdms.hgrid.html) )

` `

Method resolution order:

     [ TransientCurveGrid ](/cdms.hgrid.html)
     [ AbstractCurveGrid ](/cdms.hgrid.html)
     [ AbstractHorizontalGrid ](/cdms.hgrid.html)
     [ cdms.grid.AbstractGrid ](/cdms.grid.html)
     [ cdms.cdmsobj.CdmsObj ](/cdms.cdmsobj.html)
     [ cdms.internattr.InternalAttributesClass ](/cdms.internattr.html)
     [ PropertiedClasses.Properties.PropertiedClass ](/PropertiedClasses.Properties.html)

* * *

Methods defined here:  

 __init__  (self, latAxis, lonAxis, id  =None  , maskvar  =None  , tempmask  =None  ) 
     ` Create&#160;a&#160;file&#160;curvilinear&#160;grid. `

 __repr__  (self) 

 toCurveGrid  (self, gridid  =None  ) 

* * *

Data and other attributes defined here:  

 grid_count  = 0 

* * *

Methods inherited from [ AbstractCurveGrid ](/cdms.hgrid.html) :  

 __str__  = __repr__(self) 

 checkAxes  (self, axes) 
     ` Return&#160;1&#160;iff&#160;every&#160;element&#160;of [ getAxisList ](/) ()&#160;is&#160;in&#160;the&#160;list&#160;'axes'. `

 clone  (self, copyData  =1  ) 

 flatAxes  (self) 
     ` Return&#160;(flatlat,&#160;flatlon)&#160;where&#160;flatlat&#160;is&#160;a&#160;1D&#160;NumPy&#160;array   
having&#160;the&#160;same&#160;length&#160;as&#160;the&#160;number&#160;of&#160;cells&#160;in&#160;the&#160;grid,&#160;similarly  
for&#160;flatlon. `

 genBounds  (self) 
     ` #&#160;Don't&#160;try&#160;to&#160;generate&#160;bounds&#160;for&#160;curvilinear&#160;grids `

 getAxis  (self, naxis) 
     ` #&#160;Get&#160;the&#160;n-th&#160;index&#160;axis.&#160;naxis&#160;is&#160;0&#160;or&#160;1\. `

 getAxisList  (self) 

 getGridSlices  (self, domainlist, newaxislist, slicelist) 
     ` Determine&#160;which&#160;slices&#160;in&#160;slicelist&#160;correspond&#160;to&#160;the&#160;lat/lon&#160;elements   
of&#160;the&#160;grid.  
domainlist&#160;is&#160;a&#160;list&#160;of&#160;axes&#160;of&#160;a&#160;variable.  
newaxislist&#160;is&#160;a&#160;list&#160;of&#160;result&#160;axes&#160;after&#160;the&#160;slicelist&#160;is&#160;applied&#160;to
domainlist.  
slicelist&#160;is&#160;a&#160;list&#160;of&#160;slices.  
  
All&#160;lists&#160;are&#160;of&#160;equal&#160;length.  
  
Return&#160;value&#160;is&#160;(newslicelist,&#160;gridaxislist)&#160;where  
newslicelist&#160;is&#160;the&#160;elements&#160;of&#160;slicelist&#160;that&#160;correspond&#160;to&#160;the&#160;grid,&#160;in&#160;the  
preferred&#160;order&#160;of&#160;the&#160;grid.  
gridaxislist&#160;is&#160;the&#160;elements&#160;of&#160;newaxislist&#160;that&#160;correspond&#160;to&#160;the&#160;grid,&#160;in
the  
preferred&#160;order&#160;of&#160;the&#160;grid. `

 getIndex  (self) 
     ` Get&#160;the&#160;grid&#160;index `

 getMask  (self) 
     ` Get&#160;the&#160;mask&#160;array,&#160;if&#160;any,&#160;otherwise&#160;None&#160;is&#160;returned. `

 getMesh  (self, transpose  =None  ) 
     ` Generate&#160;a&#160;mesh&#160;array&#160;for&#160;the&#160;meshfill&#160;graphics&#160;method.   
If&#160;transpose&#160;is&#160;defined&#160;to&#160;a&#160;tuple,&#160;say&#160;(1,0),&#160;first&#160;transpose  
latbounds&#160;and&#160;lonbounds&#160;according&#160;to&#160;the&#160;tuple,&#160;(1,0,2)&#160;in&#160;this&#160;case. `

 intersect  (self, spec) 
     ` Intersect&#160;with&#160;the&#160;region&#160;specification.   
  
'spec'&#160;is&#160;a&#160;region&#160;specification&#160;of&#160;the&#160;form&#160;defined&#160;in&#160;the&#160;grid&#160;module.  
  
Returns&#160;(mask,&#160;indexspecs)&#160;where  
'mask'&#160;is&#160;the&#160;mask&#160;of&#160;the&#160;result&#160;grid&#160;AFTER&#160;self&#160;and&#160;region&#160;spec&#160;are
interested.  
'indexspecs'&#160;is&#160;a&#160;list&#160;of&#160;index&#160;specifications&#160;suitable&#160;for&#160;slicing&#160;a  
variable&#160;with&#160;the&#160;given&#160;grid. `

 isClose  (self, g) 
     ` Return&#160;1&#160;iff&#160;g&#160;is&#160;a&#160;grid&#160;of&#160;the&#160;same&#160;type&#160;and&#160;shape.&#160;A&#160;real&#160;element-by-element   
comparison&#160;would&#160;be&#160;too&#160;expensive&#160;here. `

 reconcile  (self, axes) 
     ` Return&#160;a&#160;grid&#160;that&#160;is&#160;consistent&#160;with&#160;the&#160;axes,&#160;or&#160;None.   
For&#160;curvilinear&#160;grids&#160;this&#160;means&#160;that&#160;the&#160;grid-related&#160;axes&#160;are  
contained&#160;in&#160;the&#160;'axes'&#160;list. `

 size  (self) 

 subSlice  (self, *specs, keys) 
     ` Get&#160;a&#160;transient&#160;subgrid&#160;based&#160;on&#160;an&#160;argument&#160;list&#160;<specs>&#160;of&#160;slices. `

 toGenericGrid  (self, gridid  =None  ) 

 writeScrip  (self, cufile, gridTitle  =None  ) 
     ` Write&#160;a&#160;grid&#160;to&#160;a&#160;SCRIP&#160;file.   
cufile&#160;is&#160;a&#160;Cdunif&#160;file,&#160;NOT&#160;a&#160;CDMS&#160;file.  
gridtitle&#160;is&#160;a&#160;string&#160;identifying&#160;the&#160;grid. `

 writeToFile  (self, file) 

* * *

Methods inherited from [ AbstractHorizontalGrid ](/cdms.hgrid.html) :  

 checkConvex  (self) 
     ` Check&#160;that&#160;each&#160;cell&#160;of&#160;the&#160;grid&#160;is&#160;convex&#160;in&#160;lon-lat&#160;space,&#160;with&#160;nodes&#160;defined&#160;counter-clockwise.   
Return&#160;a&#160;1D&#160;Numeric&#160;array&#160;of&#160;cells&#160;that&#160;fail&#160;the&#160;cross-product&#160;test. `

 fixCutCells  (self, nonConvexCells, threshold  =270.0  ) 
     ` For&#160;any&#160;mapping&#160;from&#160;a&#160;spherical&#160;to&#160;a&#160;planar&#160;surface,&#160;there&#160;is&#160;a&#160;linear&#160;cut.   
Grid&#160;cells&#160;that&#160;span&#160;the&#160;cut&#160;may&#160;appear&#160;to&#160;be&#160;nonconvex,&#160;which&#160;causes  
problems&#160;with&#160;meshfill&#160;graphics.&#160;This&#160;routine&#160;attempts&#160;to&#160;'repair'&#160;the&#160;cut
cell  
boundaries&#160;so&#160;that&#160;meshfill&#160;recognizes&#160;they&#160;are&#160;convex.  
  
nonConvexCells:&#160;1D&#160;Numeric&#160;array&#160;of&#160;indices&#160;of&#160;nonconvex&#160;cells,&#160;as&#160;returned
from  
checkConvex.  
threshold:&#160;positive&#160;floating-point&#160;value&#160;in&#160;degrees.  
If&#160;the&#160;difference&#160;in&#160;longitude&#160;values&#160;of  
consecutive&#160;boundaries&#160;nodes&#160;exceeds&#160;the&#160;threshold,&#160;the&#160;cell&#160;is&#160;considered  
a&#160;cut&#160;cell.  
  
On&#160;return,&#160;the&#160;grid&#160;boundaries&#160;are&#160;modified.  
Return&#160;value&#160;is&#160;a&#160;1D&#160;array&#160;of&#160;indices&#160;of&#160;cells&#160;that&#160;cannot&#160;be&#160;repaired. `

 getBounds  (self) 
     ` Get&#160;the&#160;grid&#160;cell&#160;boundaries,&#160;as&#160;a&#160;tuple&#160;(latitudeBounds,&#160;longitudeBounds) `

 getLatitude  (self) 
     ` Get&#160;the&#160;latitude&#160;coordinates. `

 getLongitude  (self) 
     ` Get&#160;the&#160;longitude&#160;coordinates. `

 getWeightsArray  (self) 
     ` Return&#160;normalized&#160;area&#160;weights,&#160;as&#160;an&#160;array&#160;of&#160;the&#160;same   
shape&#160;as&#160;the&#160;grid. `

 hasCoordType  (self, coordType) 

 listall  (self, all  =None  ) 

 setMask  (self, mask, permanent  =0  ) 

 subGridRegion  (self, latRegion, lonRegion) 

* * *

Methods inherited from [ cdms.grid.AbstractGrid ](/cdms.grid.html) :  

 info  (self, flag  =None  , device  =None  ) 
     ` Write&#160;info&#160;about&#160;slab;&#160;include&#160;dimension&#160;values&#160;and&#160;weights&#160;if&#160;flag `

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

 readScripCurveGrid  (fileobj, dims, whichType, whichGrid) 
     ` Read&#160;a&#160;'native'&#160;SCRIP&#160;grid&#160;file,&#160;returning&#160;a&#160;transient&#160;curvilinear&#160;grid.   
fileobj&#160;is&#160;an&#160;open&#160;CDMS&#160;dataset&#160;or&#160;file&#160;object.  
dims&#160;is&#160;the&#160;grid&#160;shape.  
whichType&#160;is&#160;the&#160;type&#160;of&#160;file,&#160;either&#160;"grid"&#160;or&#160;"mapping"  
if&#160;whichType&#160;is&#160;"mapping",&#160;whichGrid&#160;is&#160;the&#160;choice&#160;of&#160;grid,&#160;either&#160;"source"&#160;or
"destination" `

  
 Data 

` `

 CoordTypeToLoc  = {'lat': 1, 'lev': 2, 'lon': 0}   
 LatitudeType  = 'lat'   
 LongitudeType  = 'lon'   
 MethodNotImplemented  = 'Method not yet implemented'   
 TimeType  = 'time'   
 VerticalType  = 'lev' 

* * *

UCRL-WEB-213937 | [ Privacy & Legal Notice ](/disclaimer.html)

[ webmaster@pcmdi.llnl.gov ](/webmaster@pcmdi.llnl.gov)

[ ![Powered by Plone](media/plone_powered.gif) ](/)

