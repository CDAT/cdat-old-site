---
layout: default
title:
---

 [ Skip to content. ](/cdat/source/api-reference/cdms.avariable.html) | [ Skip
to navigation ](/cdat/source/api-reference/cdms.avariable.html)

Search Site

[ Advanced Search&#8230; ](/search_form)

#  [ PCMDI Software Portal ](/)

#####  Sections

  * [ Home ](/)

#####  Personal tools

  * [ Log in ](/login_form)

You are here:  [ Home ](/) -> [ CDAT ](/cdat) -> [ Source Code ](/cdat/source)
-> [ API Reference ](/cdat/source/api-reference) -> Python: module
cdms.avariable

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

        * [ Python: module cdms.avariable ](/cdat/source/api-reference/cdms.avariable.html)

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

  * [ ![Send this page to somebody](media/mail_icon.gif) ](/cdat/source/api-reference/cdms.avariable.html/sendto_form)
  * [ ![Print this page](media/print_icon.gif) ](/this.print\(\))

#  Python: module cdms.avariable

  
  
 [ cdms  ](/cdms.html) .avariable 
[ index ](/)  

` CDMS&#160;Variable&#160;objects,&#160;abstract&#160;interface `

  
 Modules 

` `

[ MA ](/MA.html)  
[ cdms.MV ](/cdms.MV.html)  
[ Numeric ](/Numeric.html)  

[ PropertiedClasses ](/PropertiedClasses.html)  
[ cdms.cdmsNode ](/cdms.cdmsNode.html)  
[ copy ](/copy.html)  

[ cdms.internattr ](/cdms.internattr.html)  
[ re ](/re.html)  
[ cdms.selectors ](/cdms.selectors.html)  

[ string ](/string.html)  
[ types ](/types.html)  

  
 Classes 

` `

[ cdms.cdmsobj.CdmsObj ](/cdms.cdmsobj.html) ( [
cdms.internattr.InternalAttributesClass ](/cdms.internattr.html) )

    

[ AbstractVariable ](/cdms.avariable.html) ( [ cdms.cdmsobj.CdmsObj
](/cdms.cdmsobj.html) , [ cdms.slabinterface.Slab ](/cdms.slabinterface.html)
)

[ cdms.slabinterface.Slab ](/cdms.slabinterface.html)

    

[ AbstractVariable ](/cdms.avariable.html) ( [ cdms.cdmsobj.CdmsObj
](/cdms.cdmsobj.html) , [ cdms.slabinterface.Slab ](/cdms.slabinterface.html)
)

  
class  AbstractVariable  ( [ cdms.cdmsobj.CdmsObj ](/cdms.cdmsobj.html) ,
[ cdms.slabinterface.Slab ](/cdms.slabinterface.html) )

` `

Method resolution order:

     [ AbstractVariable ](/cdms.avariable.html)
     [ cdms.cdmsobj.CdmsObj ](/cdms.cdmsobj.html)
     [ cdms.internattr.InternalAttributesClass ](/cdms.internattr.html)
     [ PropertiedClasses.Properties.PropertiedClass ](/PropertiedClasses.Properties.html)
     [ cdms.slabinterface.Slab ](/cdms.slabinterface.html)

* * *

Methods defined here:  

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

 __init__  (self, parent  =None  , variableNode  =None  ) 
     ` Not&#160;to&#160;be&#160;called&#160;by&#160;users.   
variableNode&#160;is&#160;the&#160;variable&#160;tree&#160;node,&#160;if&#160;any.  
parent&#160;is&#160;the&#160;containing&#160;dataset&#160;instance. `

 __isub__  (self, other) 
     ` Subtract&#160;other&#160;from&#160;self&#160;in&#160;place. `

 __le__  (self, other) 

 __lshift__  (self, n) 

 __lt__  (self, other) 

 __mul__  (self, other) 

 __ne__  (self, other) 

 __neg__  (self) 

 __pow__  (self, other, third  =None  ) 

 __radd__  = [ __add__ ](/) (self, other) 

 __rdiv__  (self, other) 

 __rmul__  = [ __mul__ ](/) (self, other) 

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

 expertSlice  (self, slicelist) 

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

 getAxis  (self, n) 
     ` Get&#160;the&#160;n-th&#160;axis `

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

 getDomain  (self) 
     ` Get&#160;the&#160;list&#160;of&#160;axes `

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

 getValue  (self, squeeze  =1  ) 
     ` Return&#160;the&#160;entire&#160;set&#160;of&#160;values. `

 isAbstractCoordinate  (self) 

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

 select  = [ __call__ ](/) (self, *args, kwargs) 

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

 subSlice  (self, *specs, keys) 

 typecode  (self) 

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

 info  (self, flag  =None  , device  =None  ) 
     ` Write&#160;info&#160;about&#160;slab;&#160;include&#160;dimension&#160;values&#160;and&#160;weights&#160;if&#160;flag `

 listall  (self, all  =None  ) 
     ` Get&#160;list&#160;of&#160;info&#160;about&#160;this&#160;slab. `

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

  
 Functions 

` `

 order2index  (axes, order) 
     ` Find&#160;the&#160;index&#160;permutation&#160;of&#160;axes&#160;to&#160;match&#160;order.   
The&#160;argument&#160;order&#160;is&#160;a&#160;string.  
Order&#160;elements&#160;can&#160;be:  
Letters&#160;t,&#160;x,&#160;y,&#160;z&#160;meaning&#160;time,&#160;longitude,&#160;latitude,&#160;level  
Numbers&#160;0-9&#160;representing&#160;position&#160;in&#160;axes  
The&#160;letter&#160;-&#160;meaning&#160;insert&#160;the&#160;next&#160;available&#160;axis&#160;here.  
The&#160;ellipsis&#160;...&#160;meaning&#160;fill&#160;these&#160;positions&#160;with&#160;any  
remaining&#160;axes.  
(name)&#160;meaning&#160;an&#160;axis&#160;whose&#160;id&#160;is&#160;name `

 orderparse  (order) 
     ` Parse&#160;an&#160;order&#160;string.&#160;Returns&#160;a&#160;list&#160;of&#160;axes&#160;specifiers.   
Order&#160;elements&#160;can&#160;be:  
Letters&#160;t,&#160;x,&#160;y,&#160;z&#160;meaning&#160;time,&#160;longitude,&#160;latitude,&#160;level  
Numbers&#160;0-9&#160;representing&#160;position&#160;in&#160;axes  
The&#160;letter&#160;-&#160;meaning&#160;insert&#160;the&#160;next&#160;available&#160;axis&#160;here.  
The&#160;ellipsis&#160;...&#160;meaning&#160;fill&#160;these&#160;positions&#160;with&#160;any  
remaining&#160;axes.  
(name)&#160;meaning&#160;an&#160;axis&#160;whose&#160;id&#160;is&#160;name `

  
 Data 

` `

 CF1  = <cdms.convention.CFConvention instance>   
 CdtimeTypes  = (<type 'comptime'>, <type 'reltime'>)   
 InvalidRegion  = 'Invalid region: '   
 NotImplemented  = 'Child of AbstractVariable failed to implement: '   
 OutOfRange  = 'Coordinate interval is out of range or intersection has no data: '   
 unspecified  = 'No value specified.' 

* * *

UCRL-WEB-213937 | [ Privacy & Legal Notice ](/disclaimer.html)

[ webmaster@pcmdi.llnl.gov ](/webmaster@pcmdi.llnl.gov)

[ ![Powered by Plone](media/plone_powered.gif) ](/)

