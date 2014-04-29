---
layout: default
title:
---

 [ Skip to content. ](/cdat/source/api-reference/cdms.axis.html) | [ Skip to
navigation ](/cdat/source/api-reference/cdms.axis.html)

Search Site

[ Advanced Search&#8230; ](/search_form)

#  [ PCMDI Software Portal ](/)

#####  Sections

  * [ Home ](/)

#####  Personal tools

  * [ Log in ](/login_form)

You are here:  [ Home ](/) -> [ CDAT ](/cdat) -> [ Source Code ](/cdat/source)
-> [ API Reference ](/cdat/source/api-reference) -> Python: module cdms.axis

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

        * [ Python: module cdms.axis ](/cdat/source/api-reference/cdms.axis.html)

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

  * [ ![Send this page to somebody](media/mail_icon.gif) ](/cdat/source/api-reference/cdms.axis.html/sendto_form)
  * [ ![Print this page](media/print_icon.gif) ](/this.print\(\))

#  Python: module cdms.axis

  
  
 [ cdms  ](/cdms.html) .axis 
[ index ](/)  

` CDMS [ Axis ](/) objects `

  
 Modules 

` `

[ MA ](/MA.html)  
[ Numeric ](/Numeric.html)  
[ PropertiedClasses ](/PropertiedClasses.html)  

[ cdms.cdmsNode ](/cdms.cdmsNode.html)  
[ cdms.cdmsobj ](/cdms.cdmsobj.html)  
[ cdtime ](/cdtime.html)  

[ copy ](/copy.html)  
[ cdms.internattr ](/cdms.internattr.html)  
[ regrid ](/regrid.html)  

[ string ](/string.html)  
[ sys ](/sys.html)  
[ types ](/types.html)  

  
 Classes 

` `

[ UserList.UserList ](/UserList.html)

    

[ AliasList ](/cdms.axis.html)

[ cdms.cdmsobj.CdmsObj ](/cdms.cdmsobj.html) ( [
cdms.internattr.InternalAttributesClass ](/cdms.internattr.html) )

    

[ AbstractAxis ](/cdms.axis.html)

    

[ Axis ](/cdms.axis.html)

[ FileAxis ](/cdms.axis.html)

    

[ FileVirtualAxis ](/cdms.axis.html)

[ TransientAxis ](/cdms.axis.html)

    

[ TransientVirtualAxis ](/cdms.axis.html)

  
class  AbstractAxis  ( [ cdms.cdmsobj.CdmsObj ](/cdms.cdmsobj.html) )

` `

Method resolution order:

     [ AbstractAxis ](/cdms.axis.html)
     [ cdms.cdmsobj.CdmsObj ](/cdms.cdmsobj.html)
     [ cdms.internattr.InternalAttributesClass ](/cdms.internattr.html)
     [ PropertiedClasses.Properties.PropertiedClass ](/PropertiedClasses.Properties.html)

* * *

Methods defined here:  

 __getitem__  (self, key) 

 __getslice__  (self, low, high) 

 __init__  (self, parent, node) 

 __len__  (self) 

 __repr__  = [ __str__ ](/) (self) 

 __setitem__  (self, index, value) 

 __setslice__  (self, low, high, value) 

 __str__  (self) 

 asComponentTime  (self, calendar  =None  ) 
     ` Array&#160;version&#160;of&#160;cdtime&#160;tocomp.&#160;Returns&#160;a&#160;list&#160;of&#160;component&#160;times. `

 asDTGTime  (self, calendar  =None  ) 
     ` Array&#160;version&#160;of&#160;cdtime&#160;tocomp.&#160;Returns&#160;a&#160;list&#160;of&#160;component&#160;times&#160;in&#160;DTG&#160;format. `

 asRelativeTime  (self) 
     ` Array&#160;version&#160;of&#160;cdtime&#160;torel.&#160;Returns&#160;a&#160;list&#160;of&#160;component&#160;times. `

 assignValue  (self, data) 

 clone  (self, copyData  =1  ) 
     ` clone&#160;(self,&#160;copyData=1)   
Return&#160;a&#160;copy&#160;of&#160;self&#160;as&#160;a&#160;transient&#160;axis.  
If&#160;copyData&#160;is&#160;1,&#160;make&#160;a&#160;separate&#160;copy&#160;of&#160;the&#160;data. `

 designateCircular  (self, modulo, persistent  =0  ) 

 designateLatitude  (self, persistent  =0  ) 
     ` #&#160;Designate&#160;axis&#160;as&#160;a&#160;latitude&#160;axis.   
#&#160;If&#160;persistent&#160;is&#160;true,&#160;write&#160;metadata&#160;to&#160;the&#160;container. `

 designateLevel  (self, persistent  =0  ) 
     ` #&#160;Designate&#160;axis&#160;as&#160;a&#160;vertical&#160;level&#160;axis   
#&#160;If&#160;persistent&#160;is&#160;true,&#160;write&#160;metadata&#160;to&#160;the&#160;container. `

 designateLongitude  (self, persistent  =0  , modulo  =360.0  ) 
     ` #&#160;Designate&#160;axis&#160;as&#160;a&#160;longitude&#160;axis   
#&#160;If&#160;persistent&#160;is&#160;true,&#160;write&#160;metadata&#160;to&#160;the&#160;container.  
#&#160;If&#160;modulo&#160;is&#160;defined,&#160;set&#160;as&#160;circular `

 designateTime  (self, persistent  =0  , calendar  =4369  ) 
     ` #&#160;Designate&#160;axis&#160;as&#160;a&#160;time&#160;axis,&#160;and&#160;optionally&#160;set&#160;the&#160;calendar   
#&#160;If&#160;persistent&#160;is&#160;true,&#160;write&#160;metadata&#160;to&#160;the&#160;container. `

 genGenericBounds  (self, width  =1.0  ) 
     ` #&#160;Generate&#160;bounds&#160;from&#160;midpoints.&#160;width&#160;is&#160;the&#160;width&#160;of&#160;the&#160;zone&#160;if&#160;the&#160;axis&#160;has&#160;one&#160;value. `

 getBounds  (self) 

 getCalendar  (self) 
     ` #&#160;Return&#160;the&#160;cdtime&#160;calendar:&#160;GregorianCalendar,&#160;NoLeapCalendar,&#160;JulianCalendar,&#160;Calendar360   
#&#160;or&#160;None.&#160;If&#160;the&#160;axis&#160;does&#160;not&#160;have&#160;a&#160;calendar&#160;attribute,&#160;return&#160;the&#160;global  
#&#160;calendar. `

 getData  (self) 

 getExplicitBounds  (self) 
     ` #&#160;Return&#160;None&#160;if&#160;not&#160;explicitly&#160;defined `

 getModulo  (self) 

 getModuloCycle  (self) 

 getValue  (self) 
     ` #&#160;Return&#160;the&#160;entire&#160;array `

 info  (self, flag  =None  , device  =None  ) 
     ` Write&#160;info&#160;about&#160;axis;&#160;include&#160;dimension&#160;values&#160;and&#160;weights&#160;if&#160;flag `

 isCircular  (self) 
     ` #&#160;Return&#160;true&#160;iff&#160;the&#160;axis&#160;wraps&#160;around   
#&#160;An&#160;axis&#160;is&#160;defined&#160;as&#160;circular&#160;if:  
#&#160;(1)&#160;self.  topology  =='circular',&#160;or  
#&#160;(2)&#160;self.  topology  is&#160;undefined,&#160;and&#160;the&#160;axis&#160;is&#160;a&#160;longitude `

 isCircularAxis  (self) 
     ` #&#160;Return&#160;true&#160;iff&#160;the&#160;axis&#160;wraps&#160;around   
#&#160;An&#160;axis&#160;is&#160;defined&#160;as&#160;circular&#160;if:  
#&#160;(1)&#160;self.  topology  =='circular',&#160;or  
#&#160;(2)&#160;self.  topology  is&#160;undefined,&#160;and&#160;the&#160;axis&#160;is&#160;a&#160;longitude `

 isLatitude  (self) 
     ` #&#160;Return&#160;true&#160;iff&#160;the&#160;axis&#160;is&#160;a&#160;latitude&#160;axis `

 isLevel  (self) 
     ` #&#160;Return&#160;true&#160;iff&#160;the&#160;axis&#160;is&#160;a&#160;level&#160;axis `

 isLinear  (self) 

 isLongitude  (self) 
     ` #&#160;Return&#160;true&#160;iff&#160;the&#160;axis&#160;is&#160;a&#160;longitude&#160;axis `

 isTime  (self) 
     ` #&#160;Return&#160;true&#160;iff&#160;the&#160;axis&#160;is&#160;a&#160;time&#160;axis `

 isVirtual  (self) 
     ` Return&#160;true&#160;iff&#160;coordinate&#160;values&#160;are&#160;implicitly&#160;defined. `

 listall  (self, all  =None  ) 
     ` Get&#160;list&#160;of&#160;info&#160;about&#160;this&#160;axis. `

 mapInterval  (self, interval, indicator  ='ccn'  , cycle  =None  ) 
     ` Map&#160;coordinate&#160;interval&#160;to&#160;index&#160;interval.&#160;interval&#160;has&#160;one&#160;of&#160;the&#160;forms:   
  
(x,y)  
(x,y,indicator):&#160;indicator&#160;overrides&#160;keywork&#160;argument  
(x,y,indicator,cycle):&#160;indicator,&#160;cycle&#160;override&#160;keyword&#160;arguments  
None:&#160;indicates&#160;the&#160;full&#160;interval  
  
where&#160;x&#160;and&#160;y&#160;are&#160;the&#160;endpoints&#160;in&#160;coordinate&#160;space.&#160;indicator&#160;is&#160;a  
two-character&#160;string,&#160;where&#160;the&#160;first&#160;character&#160;is&#160;'c'&#160;if&#160;the&#160;interval  
is&#160;closed&#160;on&#160;the&#160;left,&#160;'o'&#160;if&#160;open,&#160;and&#160;the&#160;second&#160;character&#160;has&#160;the  
same&#160;meaning&#160;for&#160;the&#160;right-hand&#160;point.&#160;Set&#160;cycle&#160;to&#160;a&#160;nonzero&#160;value  
to&#160;force&#160;wraparound.  
  
Returns&#160;the&#160;corresponding&#160;index&#160;interval&#160;(i,j),&#160;where&#160;i<j,&#160;indicating  
the&#160;half-open&#160;index&#160;interval&#160;[i,j),&#160;or&#160;None&#160;if&#160;the&#160;intersection&#160;is&#160;empty.  
  
For&#160;an&#160;axis&#160;which&#160;is&#160;circular&#160;(self.  topology  ==&#160;'circular'),&#160;[i,j)  
is&#160;interpreted&#160;as&#160;follows&#160;(where&#160;N&#160;=&#160;len(self)):  
  
(1)&#160;if&#160;j<=N,&#160;the&#160;interval&#160;does&#160;not&#160;wrap&#160;around&#160;the&#160;axis&#160;endpoint  
(2)&#160;if&#160;j>N,&#160;the&#160;interval&#160;wraps&#160;around,&#160;and&#160;is&#160;equivalent&#160;to&#160;the  
two&#160;consecutive&#160;intervals&#160;[i,N),&#160;[0,j-N)  
For&#160;example,&#160;if&#160;the&#160;vector&#160;is&#160;[0,2,4,...,358]&#160;of&#160;length&#160;180,  
and&#160;the&#160;coordinate&#160;interval&#160;is&#160;[-5,5),&#160;the&#160;return&#160;index&#160;interval&#160;is  
[178,183).&#160;This&#160;is&#160;equivalent&#160;to&#160;the&#160;two&#160;intervals&#160;[178,180)&#160;and&#160;[0,3).  
  
Note:&#160;if&#160;the&#160;interval&#160;is&#160;interior&#160;to&#160;the&#160;axis,&#160;but&#160;does&#160;not&#160;span&#160;any  
axis&#160;element,&#160;a&#160;singleton&#160;(i,i+1)&#160;indicating&#160;an&#160;adjacent&#160;index&#160;is&#160;returned. `

 mapIntervalExt  (self, interval, indicator  ='ccn'  , cycle  =None  , epsilon  =None  ) 
     ` Like&#160;mapInterval,&#160;but&#160;returns&#160;(i,j,k)&#160;where&#160;k&#160;is&#160;stride,   
and&#160;(i,j)&#160;is&#160;not&#160;restricted&#160;to&#160;one&#160;cycle. `

 rank  (self) 

 setBounds  (self, bounds) 

 setCalendar  (self, calendar, persistent  =1  ) 
     ` #&#160;Set&#160;the&#160;calendar `

 subAxis  = [ subaxis ](/) (self, i, j, k  =1  ) 

 subaxis  (self, i, j, k  =1  ) 
     ` Create&#160;a&#160;transient&#160;axis&#160;for&#160;the&#160;index&#160;slice&#160;[i:j:k]   
The&#160;stride&#160;k&#160;can&#160;be&#160;positive&#160;or&#160;negative.&#160;Wraparound&#160;is  
supported&#160;for&#160;longitude&#160;dimensions&#160;or&#160;those&#160;with&#160;a&#160;modulus&#160;attribute. `

 toRelativeTime  (self, units, calendar  =None  ) 
     ` Convert&#160;time&#160;axis&#160;values&#160;to&#160;another&#160;unit `

 typecode  (self) 

 validateBounds  (self, bounds) 
     ` #&#160;Check&#160;that&#160;a&#160;boundary&#160;array&#160;is&#160;valid,&#160;raise&#160;exception&#160;if&#160;not.&#160;bounds&#160;is&#160;an&#160;array&#160;of&#160;shape&#160;(n,2) `

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

  
class  AliasList  ( [ UserList.UserList ](/UserList.html) )

` `

Methods defined here:  

 __init__  (self, alist) 

 __setitem__  (self, i, value) 

 append  (self, value) 

 extend  (self, values) 

* * *

Methods inherited from [ UserList.UserList ](/UserList.html) :  

 __add__  (self, other) 

 __cmp__  (self, other) 

 __contains__  (self, item) 

 __delitem__  (self, i) 

 __delslice__  (self, i, j) 

 __eq__  (self, other) 

 __ge__  (self, other) 

 __getitem__  (self, i) 

 __getslice__  (self, i, j) 

 __gt__  (self, other) 

 __iadd__  (self, other) 

 __imul__  (self, n) 

 __le__  (self, other) 

 __len__  (self) 

 __lt__  (self, other) 

 __mul__  (self, n) 

 __ne__  (self, other) 

 __radd__  (self, other) 

 __repr__  (self) 

 __rmul__  = __mul__(self, n) 

 __setslice__  (self, i, j, other) 

 count  (self, item) 

 index  (self, item, *args) 

 insert  (self, i, item) 

 pop  (self, i  =-1  ) 

 remove  (self, item) 

 reverse  (self) 

 sort  (self, *args, kwds) 

  
class  Axis  ( [ AbstractAxis ](/cdms.axis.html) )

` `

` #&#160;One-dimensional&#160;coordinate&#160;axis&#160;in&#160;a&#160;dataset  
`

Method resolution order:

     [ Axis ](/cdms.axis.html)
     [ AbstractAxis ](/cdms.axis.html)
     [ cdms.cdmsobj.CdmsObj ](/cdms.cdmsobj.html)
     [ cdms.internattr.InternalAttributesClass ](/cdms.internattr.html)
     [ PropertiedClasses.Properties.PropertiedClass ](/PropertiedClasses.Properties.html)

* * *

Methods defined here:  

 __getitem__  (self, key) 
     ` #&#160;Handle&#160;slices&#160;of&#160;the&#160;form&#160;x[i],&#160;x[i:j:k],&#160;and&#160;x[...] `

 __getslice__  (self, low, high) 
     ` #&#160;Handle&#160;slices&#160;of&#160;the&#160;form&#160;x[i:j] `

 __init__  (self, parent, axisNode  =None  ) 

 __len__  (self) 

 getBounds  (self) 
     ` #&#160;Return&#160;the&#160;bounds&#160;array,&#160;or&#160;generate&#160;a&#160;default&#160;if&#160;autoBounds&#160;mode&#160;is&#160;on `

 getCalendar  (self) 

 getData  (self) 
     ` #&#160;Get&#160;axis&#160;data `

 getExplicitBounds  (self) 
     ` #&#160;Return&#160;the&#160;bounds&#160;array,&#160;or&#160;None `

 isLinear  (self) 
     ` #&#160;Return&#160;true&#160;iff&#160;the&#160;axis&#160;representation&#160;is&#160;linear `

 typecode  (self) 

* * *

Methods inherited from [ AbstractAxis ](/cdms.axis.html) :  

 __repr__  = __str__(self) 

 __setitem__  (self, index, value) 

 __setslice__  (self, low, high, value) 

 __str__  (self) 

 asComponentTime  (self, calendar  =None  ) 
     ` Array&#160;version&#160;of&#160;cdtime&#160;tocomp.&#160;Returns&#160;a&#160;list&#160;of&#160;component&#160;times. `

 asDTGTime  (self, calendar  =None  ) 
     ` Array&#160;version&#160;of&#160;cdtime&#160;tocomp.&#160;Returns&#160;a&#160;list&#160;of&#160;component&#160;times&#160;in&#160;DTG&#160;format. `

 asRelativeTime  (self) 
     ` Array&#160;version&#160;of&#160;cdtime&#160;torel.&#160;Returns&#160;a&#160;list&#160;of&#160;component&#160;times. `

 assignValue  (self, data) 

 clone  (self, copyData  =1  ) 
     ` clone&#160;(self,&#160;copyData=1)   
Return&#160;a&#160;copy&#160;of&#160;self&#160;as&#160;a&#160;transient&#160;axis.  
If&#160;copyData&#160;is&#160;1,&#160;make&#160;a&#160;separate&#160;copy&#160;of&#160;the&#160;data. `

 designateCircular  (self, modulo, persistent  =0  ) 

 designateLatitude  (self, persistent  =0  ) 
     ` #&#160;Designate&#160;axis&#160;as&#160;a&#160;latitude&#160;axis.   
#&#160;If&#160;persistent&#160;is&#160;true,&#160;write&#160;metadata&#160;to&#160;the&#160;container. `

 designateLevel  (self, persistent  =0  ) 
     ` #&#160;Designate&#160;axis&#160;as&#160;a&#160;vertical&#160;level&#160;axis   
#&#160;If&#160;persistent&#160;is&#160;true,&#160;write&#160;metadata&#160;to&#160;the&#160;container. `

 designateLongitude  (self, persistent  =0  , modulo  =360.0  ) 
     ` #&#160;Designate&#160;axis&#160;as&#160;a&#160;longitude&#160;axis   
#&#160;If&#160;persistent&#160;is&#160;true,&#160;write&#160;metadata&#160;to&#160;the&#160;container.  
#&#160;If&#160;modulo&#160;is&#160;defined,&#160;set&#160;as&#160;circular `

 designateTime  (self, persistent  =0  , calendar  =4369  ) 
     ` #&#160;Designate&#160;axis&#160;as&#160;a&#160;time&#160;axis,&#160;and&#160;optionally&#160;set&#160;the&#160;calendar   
#&#160;If&#160;persistent&#160;is&#160;true,&#160;write&#160;metadata&#160;to&#160;the&#160;container. `

 genGenericBounds  (self, width  =1.0  ) 
     ` #&#160;Generate&#160;bounds&#160;from&#160;midpoints.&#160;width&#160;is&#160;the&#160;width&#160;of&#160;the&#160;zone&#160;if&#160;the&#160;axis&#160;has&#160;one&#160;value. `

 getModulo  (self) 

 getModuloCycle  (self) 

 getValue  (self) 
     ` #&#160;Return&#160;the&#160;entire&#160;array `

 info  (self, flag  =None  , device  =None  ) 
     ` Write&#160;info&#160;about&#160;axis;&#160;include&#160;dimension&#160;values&#160;and&#160;weights&#160;if&#160;flag `

 isCircular  (self) 
     ` #&#160;Return&#160;true&#160;iff&#160;the&#160;axis&#160;wraps&#160;around   
#&#160;An&#160;axis&#160;is&#160;defined&#160;as&#160;circular&#160;if:  
#&#160;(1)&#160;self.  topology  =='circular',&#160;or  
#&#160;(2)&#160;self.  topology  is&#160;undefined,&#160;and&#160;the&#160;axis&#160;is&#160;a&#160;longitude `

 isCircularAxis  (self) 
     ` #&#160;Return&#160;true&#160;iff&#160;the&#160;axis&#160;wraps&#160;around   
#&#160;An&#160;axis&#160;is&#160;defined&#160;as&#160;circular&#160;if:  
#&#160;(1)&#160;self.  topology  =='circular',&#160;or  
#&#160;(2)&#160;self.  topology  is&#160;undefined,&#160;and&#160;the&#160;axis&#160;is&#160;a&#160;longitude `

 isLatitude  (self) 
     ` #&#160;Return&#160;true&#160;iff&#160;the&#160;axis&#160;is&#160;a&#160;latitude&#160;axis `

 isLevel  (self) 
     ` #&#160;Return&#160;true&#160;iff&#160;the&#160;axis&#160;is&#160;a&#160;level&#160;axis `

 isLongitude  (self) 
     ` #&#160;Return&#160;true&#160;iff&#160;the&#160;axis&#160;is&#160;a&#160;longitude&#160;axis `

 isTime  (self) 
     ` #&#160;Return&#160;true&#160;iff&#160;the&#160;axis&#160;is&#160;a&#160;time&#160;axis `

 isVirtual  (self) 
     ` Return&#160;true&#160;iff&#160;coordinate&#160;values&#160;are&#160;implicitly&#160;defined. `

 listall  (self, all  =None  ) 
     ` Get&#160;list&#160;of&#160;info&#160;about&#160;this&#160;axis. `

 mapInterval  (self, interval, indicator  ='ccn'  , cycle  =None  ) 
     ` Map&#160;coordinate&#160;interval&#160;to&#160;index&#160;interval.&#160;interval&#160;has&#160;one&#160;of&#160;the&#160;forms:   
  
(x,y)  
(x,y,indicator):&#160;indicator&#160;overrides&#160;keywork&#160;argument  
(x,y,indicator,cycle):&#160;indicator,&#160;cycle&#160;override&#160;keyword&#160;arguments  
None:&#160;indicates&#160;the&#160;full&#160;interval  
  
where&#160;x&#160;and&#160;y&#160;are&#160;the&#160;endpoints&#160;in&#160;coordinate&#160;space.&#160;indicator&#160;is&#160;a  
two-character&#160;string,&#160;where&#160;the&#160;first&#160;character&#160;is&#160;'c'&#160;if&#160;the&#160;interval  
is&#160;closed&#160;on&#160;the&#160;left,&#160;'o'&#160;if&#160;open,&#160;and&#160;the&#160;second&#160;character&#160;has&#160;the  
same&#160;meaning&#160;for&#160;the&#160;right-hand&#160;point.&#160;Set&#160;cycle&#160;to&#160;a&#160;nonzero&#160;value  
to&#160;force&#160;wraparound.  
  
Returns&#160;the&#160;corresponding&#160;index&#160;interval&#160;(i,j),&#160;where&#160;i<j,&#160;indicating  
the&#160;half-open&#160;index&#160;interval&#160;[i,j),&#160;or&#160;None&#160;if&#160;the&#160;intersection&#160;is&#160;empty.  
  
For&#160;an&#160;axis&#160;which&#160;is&#160;circular&#160;(self.  topology  ==&#160;'circular'),&#160;[i,j)  
is&#160;interpreted&#160;as&#160;follows&#160;(where&#160;N&#160;=&#160;len(self)):  
  
(1)&#160;if&#160;j<=N,&#160;the&#160;interval&#160;does&#160;not&#160;wrap&#160;around&#160;the&#160;axis&#160;endpoint  
(2)&#160;if&#160;j>N,&#160;the&#160;interval&#160;wraps&#160;around,&#160;and&#160;is&#160;equivalent&#160;to&#160;the  
two&#160;consecutive&#160;intervals&#160;[i,N),&#160;[0,j-N)  
For&#160;example,&#160;if&#160;the&#160;vector&#160;is&#160;[0,2,4,...,358]&#160;of&#160;length&#160;180,  
and&#160;the&#160;coordinate&#160;interval&#160;is&#160;[-5,5),&#160;the&#160;return&#160;index&#160;interval&#160;is  
[178,183).&#160;This&#160;is&#160;equivalent&#160;to&#160;the&#160;two&#160;intervals&#160;[178,180)&#160;and&#160;[0,3).  
  
Note:&#160;if&#160;the&#160;interval&#160;is&#160;interior&#160;to&#160;the&#160;axis,&#160;but&#160;does&#160;not&#160;span&#160;any  
axis&#160;element,&#160;a&#160;singleton&#160;(i,i+1)&#160;indicating&#160;an&#160;adjacent&#160;index&#160;is&#160;returned. `

 mapIntervalExt  (self, interval, indicator  ='ccn'  , cycle  =None  , epsilon  =None  ) 
     ` Like&#160;mapInterval,&#160;but&#160;returns&#160;(i,j,k)&#160;where&#160;k&#160;is&#160;stride,   
and&#160;(i,j)&#160;is&#160;not&#160;restricted&#160;to&#160;one&#160;cycle. `

 rank  (self) 

 setBounds  (self, bounds) 

 setCalendar  (self, calendar, persistent  =1  ) 
     ` #&#160;Set&#160;the&#160;calendar `

 subAxis  = subaxis(self, i, j, k  =1  ) 
     ` Create&#160;a&#160;transient&#160;axis&#160;for&#160;the&#160;index&#160;slice&#160;[i:j:k]   
The&#160;stride&#160;k&#160;can&#160;be&#160;positive&#160;or&#160;negative.&#160;Wraparound&#160;is  
supported&#160;for&#160;longitude&#160;dimensions&#160;or&#160;those&#160;with&#160;a&#160;modulus&#160;attribute. `

 subaxis  (self, i, j, k  =1  ) 
     ` Create&#160;a&#160;transient&#160;axis&#160;for&#160;the&#160;index&#160;slice&#160;[i:j:k]   
The&#160;stride&#160;k&#160;can&#160;be&#160;positive&#160;or&#160;negative.&#160;Wraparound&#160;is  
supported&#160;for&#160;longitude&#160;dimensions&#160;or&#160;those&#160;with&#160;a&#160;modulus&#160;attribute. `

 toRelativeTime  (self, units, calendar  =None  ) 
     ` Convert&#160;time&#160;axis&#160;values&#160;to&#160;another&#160;unit `

 validateBounds  (self, bounds) 
     ` #&#160;Check&#160;that&#160;a&#160;boundary&#160;array&#160;is&#160;valid,&#160;raise&#160;exception&#160;if&#160;not.&#160;bounds&#160;is&#160;an&#160;array&#160;of&#160;shape&#160;(n,2) `

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

  
class  FileAxis  ( [ AbstractAxis ](/cdms.axis.html) )

` `

` #&#160;One-dimensional&#160;coordinate&#160;axis&#160;in&#160;a&#160;CdmsFile.  
`

Method resolution order:

     [ FileAxis ](/cdms.axis.html)
     [ AbstractAxis ](/cdms.axis.html)
     [ cdms.cdmsobj.CdmsObj ](/cdms.cdmsobj.html)
     [ cdms.internattr.InternalAttributesClass ](/cdms.internattr.html)
     [ PropertiedClasses.Properties.PropertiedClass ](/PropertiedClasses.Properties.html)

* * *

Methods defined here:  

 __delattr__  (self, name) 
     ` #&#160;delattr&#160;deletes&#160;external&#160;global&#160;attributes&#160;in&#160;the&#160;file `

 __getitem__  (self, key) 
     ` #&#160;Read&#160;data   
#&#160;If&#160;the&#160;axis&#160;has&#160;a&#160;related&#160;Cdunif&#160;variable&#160;object,&#160;just&#160;read&#160;that&#160;variable  
#&#160;otherwise,&#160;cache&#160;the&#160;Cdunif&#160;(read-only)&#160;data&#160;values&#160;in&#160;self.  _data_  .
in&#160;this&#160;case,  
#&#160;the&#160;axis&#160;is&#160;not&#160;extensible,&#160;so&#160;it&#160;is&#160;not&#160;necessary&#160;to&#160;reread&#160;it&#160;each&#160;time. `

 __getslice__  (self, low, high) 

 __init__  (self, parent, axisname, obj  =None  ) 

 __len__  (self) 

 __setattr__  (self, name, value) 
     ` #&#160;setattr&#160;writes&#160;external&#160;attributes&#160;to&#160;the&#160;file `

 __setitem__  (self, index, value) 

 __setslice__  (self, low, high, value) 

 getBounds  (self) 
     ` #&#160;Return&#160;the&#160;bounds&#160;array,&#160;or&#160;generate&#160;a&#160;default&#160;if&#160;autobounds&#160;mode&#160;is&#160;set `

 getCalendar  (self) 

 getData  (self) 

 getExplicitBounds  (self) 
     ` #&#160;Return&#160;the&#160;bounds&#160;array,&#160;or&#160;None `

 isLinear  (self) 

 isVirtual  (self) 
     ` Return&#160;true&#160;iff&#160;coordinate&#160;values&#160;are&#160;implicitly&#160;defined. `

 setBounds  (self, bounds, persistent  =0  , validate  =0  , index  =None  , boundsid  =None  ) 
     ` #&#160;Create&#160;and&#160;write&#160;boundary&#160;data&#160;variable.&#160;An&#160;exception&#160;is&#160;raised   
#&#160;if&#160;the&#160;bounds&#160;are&#160;already&#160;set.&#160;bounds&#160;is&#160;a&#160;Numeric&#160;array.  
#&#160;If&#160;persistent==1,&#160;write&#160;to&#160;file,&#160;else&#160;save&#160;in&#160;self.  _boundsArray_   
#&#160;For&#160;a&#160;persistent&#160;axis,&#160;index=n&#160;writes&#160;the&#160;bounds&#160;starting&#160;at&#160;that  
#&#160;index&#160;in&#160;the&#160;extended&#160;dimension&#160;(default&#160;is&#160;index=0).  
#&#160;If&#160;the&#160;bounds&#160;variable&#160;is&#160;new,&#160;use&#160;the&#160;name&#160;boundsid,&#160;or&#160;'bounds_<varid>'  
#&#160;if&#160;unspecified. `

 typecode  (self) 

* * *

Methods inherited from [ AbstractAxis ](/cdms.axis.html) :  

 __repr__  = __str__(self) 

 __str__  (self) 

 asComponentTime  (self, calendar  =None  ) 
     ` Array&#160;version&#160;of&#160;cdtime&#160;tocomp.&#160;Returns&#160;a&#160;list&#160;of&#160;component&#160;times. `

 asDTGTime  (self, calendar  =None  ) 
     ` Array&#160;version&#160;of&#160;cdtime&#160;tocomp.&#160;Returns&#160;a&#160;list&#160;of&#160;component&#160;times&#160;in&#160;DTG&#160;format. `

 asRelativeTime  (self) 
     ` Array&#160;version&#160;of&#160;cdtime&#160;torel.&#160;Returns&#160;a&#160;list&#160;of&#160;component&#160;times. `

 assignValue  (self, data) 

 clone  (self, copyData  =1  ) 
     ` clone&#160;(self,&#160;copyData=1)   
Return&#160;a&#160;copy&#160;of&#160;self&#160;as&#160;a&#160;transient&#160;axis.  
If&#160;copyData&#160;is&#160;1,&#160;make&#160;a&#160;separate&#160;copy&#160;of&#160;the&#160;data. `

 designateCircular  (self, modulo, persistent  =0  ) 

 designateLatitude  (self, persistent  =0  ) 
     ` #&#160;Designate&#160;axis&#160;as&#160;a&#160;latitude&#160;axis.   
#&#160;If&#160;persistent&#160;is&#160;true,&#160;write&#160;metadata&#160;to&#160;the&#160;container. `

 designateLevel  (self, persistent  =0  ) 
     ` #&#160;Designate&#160;axis&#160;as&#160;a&#160;vertical&#160;level&#160;axis   
#&#160;If&#160;persistent&#160;is&#160;true,&#160;write&#160;metadata&#160;to&#160;the&#160;container. `

 designateLongitude  (self, persistent  =0  , modulo  =360.0  ) 
     ` #&#160;Designate&#160;axis&#160;as&#160;a&#160;longitude&#160;axis   
#&#160;If&#160;persistent&#160;is&#160;true,&#160;write&#160;metadata&#160;to&#160;the&#160;container.  
#&#160;If&#160;modulo&#160;is&#160;defined,&#160;set&#160;as&#160;circular `

 designateTime  (self, persistent  =0  , calendar  =4369  ) 
     ` #&#160;Designate&#160;axis&#160;as&#160;a&#160;time&#160;axis,&#160;and&#160;optionally&#160;set&#160;the&#160;calendar   
#&#160;If&#160;persistent&#160;is&#160;true,&#160;write&#160;metadata&#160;to&#160;the&#160;container. `

 genGenericBounds  (self, width  =1.0  ) 
     ` #&#160;Generate&#160;bounds&#160;from&#160;midpoints.&#160;width&#160;is&#160;the&#160;width&#160;of&#160;the&#160;zone&#160;if&#160;the&#160;axis&#160;has&#160;one&#160;value. `

 getModulo  (self) 

 getModuloCycle  (self) 

 getValue  (self) 
     ` #&#160;Return&#160;the&#160;entire&#160;array `

 info  (self, flag  =None  , device  =None  ) 
     ` Write&#160;info&#160;about&#160;axis;&#160;include&#160;dimension&#160;values&#160;and&#160;weights&#160;if&#160;flag `

 isCircular  (self) 
     ` #&#160;Return&#160;true&#160;iff&#160;the&#160;axis&#160;wraps&#160;around   
#&#160;An&#160;axis&#160;is&#160;defined&#160;as&#160;circular&#160;if:  
#&#160;(1)&#160;self.  topology  =='circular',&#160;or  
#&#160;(2)&#160;self.  topology  is&#160;undefined,&#160;and&#160;the&#160;axis&#160;is&#160;a&#160;longitude `

 isCircularAxis  (self) 
     ` #&#160;Return&#160;true&#160;iff&#160;the&#160;axis&#160;wraps&#160;around   
#&#160;An&#160;axis&#160;is&#160;defined&#160;as&#160;circular&#160;if:  
#&#160;(1)&#160;self.  topology  =='circular',&#160;or  
#&#160;(2)&#160;self.  topology  is&#160;undefined,&#160;and&#160;the&#160;axis&#160;is&#160;a&#160;longitude `

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

 mapInterval  (self, interval, indicator  ='ccn'  , cycle  =None  ) 
     ` Map&#160;coordinate&#160;interval&#160;to&#160;index&#160;interval.&#160;interval&#160;has&#160;one&#160;of&#160;the&#160;forms:   
  
(x,y)  
(x,y,indicator):&#160;indicator&#160;overrides&#160;keywork&#160;argument  
(x,y,indicator,cycle):&#160;indicator,&#160;cycle&#160;override&#160;keyword&#160;arguments  
None:&#160;indicates&#160;the&#160;full&#160;interval  
  
where&#160;x&#160;and&#160;y&#160;are&#160;the&#160;endpoints&#160;in&#160;coordinate&#160;space.&#160;indicator&#160;is&#160;a  
two-character&#160;string,&#160;where&#160;the&#160;first&#160;character&#160;is&#160;'c'&#160;if&#160;the&#160;interval  
is&#160;closed&#160;on&#160;the&#160;left,&#160;'o'&#160;if&#160;open,&#160;and&#160;the&#160;second&#160;character&#160;has&#160;the  
same&#160;meaning&#160;for&#160;the&#160;right-hand&#160;point.&#160;Set&#160;cycle&#160;to&#160;a&#160;nonzero&#160;value  
to&#160;force&#160;wraparound.  
  
Returns&#160;the&#160;corresponding&#160;index&#160;interval&#160;(i,j),&#160;where&#160;i<j,&#160;indicating  
the&#160;half-open&#160;index&#160;interval&#160;[i,j),&#160;or&#160;None&#160;if&#160;the&#160;intersection&#160;is&#160;empty.  
  
For&#160;an&#160;axis&#160;which&#160;is&#160;circular&#160;(self.  topology  ==&#160;'circular'),&#160;[i,j)  
is&#160;interpreted&#160;as&#160;follows&#160;(where&#160;N&#160;=&#160;len(self)):  
  
(1)&#160;if&#160;j<=N,&#160;the&#160;interval&#160;does&#160;not&#160;wrap&#160;around&#160;the&#160;axis&#160;endpoint  
(2)&#160;if&#160;j>N,&#160;the&#160;interval&#160;wraps&#160;around,&#160;and&#160;is&#160;equivalent&#160;to&#160;the  
two&#160;consecutive&#160;intervals&#160;[i,N),&#160;[0,j-N)  
For&#160;example,&#160;if&#160;the&#160;vector&#160;is&#160;[0,2,4,...,358]&#160;of&#160;length&#160;180,  
and&#160;the&#160;coordinate&#160;interval&#160;is&#160;[-5,5),&#160;the&#160;return&#160;index&#160;interval&#160;is  
[178,183).&#160;This&#160;is&#160;equivalent&#160;to&#160;the&#160;two&#160;intervals&#160;[178,180)&#160;and&#160;[0,3).  
  
Note:&#160;if&#160;the&#160;interval&#160;is&#160;interior&#160;to&#160;the&#160;axis,&#160;but&#160;does&#160;not&#160;span&#160;any  
axis&#160;element,&#160;a&#160;singleton&#160;(i,i+1)&#160;indicating&#160;an&#160;adjacent&#160;index&#160;is&#160;returned. `

 mapIntervalExt  (self, interval, indicator  ='ccn'  , cycle  =None  , epsilon  =None  ) 
     ` Like&#160;mapInterval,&#160;but&#160;returns&#160;(i,j,k)&#160;where&#160;k&#160;is&#160;stride,   
and&#160;(i,j)&#160;is&#160;not&#160;restricted&#160;to&#160;one&#160;cycle. `

 rank  (self) 

 setCalendar  (self, calendar, persistent  =1  ) 
     ` #&#160;Set&#160;the&#160;calendar `

 subAxis  = subaxis(self, i, j, k  =1  ) 
     ` Create&#160;a&#160;transient&#160;axis&#160;for&#160;the&#160;index&#160;slice&#160;[i:j:k]   
The&#160;stride&#160;k&#160;can&#160;be&#160;positive&#160;or&#160;negative.&#160;Wraparound&#160;is  
supported&#160;for&#160;longitude&#160;dimensions&#160;or&#160;those&#160;with&#160;a&#160;modulus&#160;attribute. `

 subaxis  (self, i, j, k  =1  ) 
     ` Create&#160;a&#160;transient&#160;axis&#160;for&#160;the&#160;index&#160;slice&#160;[i:j:k]   
The&#160;stride&#160;k&#160;can&#160;be&#160;positive&#160;or&#160;negative.&#160;Wraparound&#160;is  
supported&#160;for&#160;longitude&#160;dimensions&#160;or&#160;those&#160;with&#160;a&#160;modulus&#160;attribute. `

 toRelativeTime  (self, units, calendar  =None  ) 
     ` Convert&#160;time&#160;axis&#160;values&#160;to&#160;another&#160;unit `

 validateBounds  (self, bounds) 
     ` #&#160;Check&#160;that&#160;a&#160;boundary&#160;array&#160;is&#160;valid,&#160;raise&#160;exception&#160;if&#160;not.&#160;bounds&#160;is&#160;an&#160;array&#160;of&#160;shape&#160;(n,2) `

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

 __getattr__  (self, name) 

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

  
class  FileVirtualAxis  ( [ FileAxis ](/cdms.axis.html) )

` `

` An&#160;axis&#160;with&#160;no&#160;explicit&#160;representation&#160;of&#160;data&#160;values&#160;in&#160;the&#160;file.  
It&#160;appears&#160;to&#160;be&#160;a&#160;float&#160;vector&#160;with&#160;values&#160;[0.0,&#160;1.0,&#160;...,&#160;float(axislen-1)]  
This&#160;is&#160;especially&#160;useful&#160;for&#160;the&#160;bound&#160;axis&#160;used&#160;with&#160;boundary&#160;variables.  
For&#160;a&#160;netCDF&#160;file&#160;the&#160;representation&#160;is&#160;a&#160;dimension&#160;with&#160;no&#160;associated  
coordinate&#160;variable.  
`

Method resolution order:

     [ FileVirtualAxis ](/cdms.axis.html)
     [ FileAxis ](/cdms.axis.html)
     [ AbstractAxis ](/cdms.axis.html)
     [ cdms.cdmsobj.CdmsObj ](/cdms.cdmsobj.html)
     [ cdms.internattr.InternalAttributesClass ](/cdms.internattr.html)
     [ PropertiedClasses.Properties.PropertiedClass ](/PropertiedClasses.Properties.html)

* * *

Methods defined here:  

 __init__  (self, parent, axisname, axislen) 

 __len__  (self) 

 getData  (self) 

 isVirtual  (self) 
     ` Return&#160;true&#160;iff&#160;coordinate&#160;values&#160;are&#160;implicitly&#160;defined. `

* * *

Methods inherited from [ FileAxis ](/cdms.axis.html) :  

 __delattr__  (self, name) 
     ` #&#160;delattr&#160;deletes&#160;external&#160;global&#160;attributes&#160;in&#160;the&#160;file `

 __getitem__  (self, key) 
     ` #&#160;Read&#160;data   
#&#160;If&#160;the&#160;axis&#160;has&#160;a&#160;related&#160;Cdunif&#160;variable&#160;object,&#160;just&#160;read&#160;that&#160;variable  
#&#160;otherwise,&#160;cache&#160;the&#160;Cdunif&#160;(read-only)&#160;data&#160;values&#160;in&#160;self.  _data_  .
in&#160;this&#160;case,  
#&#160;the&#160;axis&#160;is&#160;not&#160;extensible,&#160;so&#160;it&#160;is&#160;not&#160;necessary&#160;to&#160;reread&#160;it&#160;each&#160;time. `

 __getslice__  (self, low, high) 

 __setattr__  (self, name, value) 
     ` #&#160;setattr&#160;writes&#160;external&#160;attributes&#160;to&#160;the&#160;file `

 __setitem__  (self, index, value) 

 __setslice__  (self, low, high, value) 

 getBounds  (self) 
     ` #&#160;Return&#160;the&#160;bounds&#160;array,&#160;or&#160;generate&#160;a&#160;default&#160;if&#160;autobounds&#160;mode&#160;is&#160;set `

 getCalendar  (self) 

 getExplicitBounds  (self) 
     ` #&#160;Return&#160;the&#160;bounds&#160;array,&#160;or&#160;None `

 isLinear  (self) 

 setBounds  (self, bounds, persistent  =0  , validate  =0  , index  =None  , boundsid  =None  ) 
     ` #&#160;Create&#160;and&#160;write&#160;boundary&#160;data&#160;variable.&#160;An&#160;exception&#160;is&#160;raised   
#&#160;if&#160;the&#160;bounds&#160;are&#160;already&#160;set.&#160;bounds&#160;is&#160;a&#160;Numeric&#160;array.  
#&#160;If&#160;persistent==1,&#160;write&#160;to&#160;file,&#160;else&#160;save&#160;in&#160;self.  _boundsArray_   
#&#160;For&#160;a&#160;persistent&#160;axis,&#160;index=n&#160;writes&#160;the&#160;bounds&#160;starting&#160;at&#160;that  
#&#160;index&#160;in&#160;the&#160;extended&#160;dimension&#160;(default&#160;is&#160;index=0).  
#&#160;If&#160;the&#160;bounds&#160;variable&#160;is&#160;new,&#160;use&#160;the&#160;name&#160;boundsid,&#160;or&#160;'bounds_<varid>'  
#&#160;if&#160;unspecified. `

 typecode  (self) 

* * *

Methods inherited from [ AbstractAxis ](/cdms.axis.html) :  

 __repr__  = __str__(self) 

 __str__  (self) 

 asComponentTime  (self, calendar  =None  ) 
     ` Array&#160;version&#160;of&#160;cdtime&#160;tocomp.&#160;Returns&#160;a&#160;list&#160;of&#160;component&#160;times. `

 asDTGTime  (self, calendar  =None  ) 
     ` Array&#160;version&#160;of&#160;cdtime&#160;tocomp.&#160;Returns&#160;a&#160;list&#160;of&#160;component&#160;times&#160;in&#160;DTG&#160;format. `

 asRelativeTime  (self) 
     ` Array&#160;version&#160;of&#160;cdtime&#160;torel.&#160;Returns&#160;a&#160;list&#160;of&#160;component&#160;times. `

 assignValue  (self, data) 

 clone  (self, copyData  =1  ) 
     ` clone&#160;(self,&#160;copyData=1)   
Return&#160;a&#160;copy&#160;of&#160;self&#160;as&#160;a&#160;transient&#160;axis.  
If&#160;copyData&#160;is&#160;1,&#160;make&#160;a&#160;separate&#160;copy&#160;of&#160;the&#160;data. `

 designateCircular  (self, modulo, persistent  =0  ) 

 designateLatitude  (self, persistent  =0  ) 
     ` #&#160;Designate&#160;axis&#160;as&#160;a&#160;latitude&#160;axis.   
#&#160;If&#160;persistent&#160;is&#160;true,&#160;write&#160;metadata&#160;to&#160;the&#160;container. `

 designateLevel  (self, persistent  =0  ) 
     ` #&#160;Designate&#160;axis&#160;as&#160;a&#160;vertical&#160;level&#160;axis   
#&#160;If&#160;persistent&#160;is&#160;true,&#160;write&#160;metadata&#160;to&#160;the&#160;container. `

 designateLongitude  (self, persistent  =0  , modulo  =360.0  ) 
     ` #&#160;Designate&#160;axis&#160;as&#160;a&#160;longitude&#160;axis   
#&#160;If&#160;persistent&#160;is&#160;true,&#160;write&#160;metadata&#160;to&#160;the&#160;container.  
#&#160;If&#160;modulo&#160;is&#160;defined,&#160;set&#160;as&#160;circular `

 designateTime  (self, persistent  =0  , calendar  =4369  ) 
     ` #&#160;Designate&#160;axis&#160;as&#160;a&#160;time&#160;axis,&#160;and&#160;optionally&#160;set&#160;the&#160;calendar   
#&#160;If&#160;persistent&#160;is&#160;true,&#160;write&#160;metadata&#160;to&#160;the&#160;container. `

 genGenericBounds  (self, width  =1.0  ) 
     ` #&#160;Generate&#160;bounds&#160;from&#160;midpoints.&#160;width&#160;is&#160;the&#160;width&#160;of&#160;the&#160;zone&#160;if&#160;the&#160;axis&#160;has&#160;one&#160;value. `

 getModulo  (self) 

 getModuloCycle  (self) 

 getValue  (self) 
     ` #&#160;Return&#160;the&#160;entire&#160;array `

 info  (self, flag  =None  , device  =None  ) 
     ` Write&#160;info&#160;about&#160;axis;&#160;include&#160;dimension&#160;values&#160;and&#160;weights&#160;if&#160;flag `

 isCircular  (self) 
     ` #&#160;Return&#160;true&#160;iff&#160;the&#160;axis&#160;wraps&#160;around   
#&#160;An&#160;axis&#160;is&#160;defined&#160;as&#160;circular&#160;if:  
#&#160;(1)&#160;self.  topology  =='circular',&#160;or  
#&#160;(2)&#160;self.  topology  is&#160;undefined,&#160;and&#160;the&#160;axis&#160;is&#160;a&#160;longitude `

 isCircularAxis  (self) 
     ` #&#160;Return&#160;true&#160;iff&#160;the&#160;axis&#160;wraps&#160;around   
#&#160;An&#160;axis&#160;is&#160;defined&#160;as&#160;circular&#160;if:  
#&#160;(1)&#160;self.  topology  =='circular',&#160;or  
#&#160;(2)&#160;self.  topology  is&#160;undefined,&#160;and&#160;the&#160;axis&#160;is&#160;a&#160;longitude `

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

 mapInterval  (self, interval, indicator  ='ccn'  , cycle  =None  ) 
     ` Map&#160;coordinate&#160;interval&#160;to&#160;index&#160;interval.&#160;interval&#160;has&#160;one&#160;of&#160;the&#160;forms:   
  
(x,y)  
(x,y,indicator):&#160;indicator&#160;overrides&#160;keywork&#160;argument  
(x,y,indicator,cycle):&#160;indicator,&#160;cycle&#160;override&#160;keyword&#160;arguments  
None:&#160;indicates&#160;the&#160;full&#160;interval  
  
where&#160;x&#160;and&#160;y&#160;are&#160;the&#160;endpoints&#160;in&#160;coordinate&#160;space.&#160;indicator&#160;is&#160;a  
two-character&#160;string,&#160;where&#160;the&#160;first&#160;character&#160;is&#160;'c'&#160;if&#160;the&#160;interval  
is&#160;closed&#160;on&#160;the&#160;left,&#160;'o'&#160;if&#160;open,&#160;and&#160;the&#160;second&#160;character&#160;has&#160;the  
same&#160;meaning&#160;for&#160;the&#160;right-hand&#160;point.&#160;Set&#160;cycle&#160;to&#160;a&#160;nonzero&#160;value  
to&#160;force&#160;wraparound.  
  
Returns&#160;the&#160;corresponding&#160;index&#160;interval&#160;(i,j),&#160;where&#160;i<j,&#160;indicating  
the&#160;half-open&#160;index&#160;interval&#160;[i,j),&#160;or&#160;None&#160;if&#160;the&#160;intersection&#160;is&#160;empty.  
  
For&#160;an&#160;axis&#160;which&#160;is&#160;circular&#160;(self.  topology  ==&#160;'circular'),&#160;[i,j)  
is&#160;interpreted&#160;as&#160;follows&#160;(where&#160;N&#160;=&#160;len(self)):  
  
(1)&#160;if&#160;j<=N,&#160;the&#160;interval&#160;does&#160;not&#160;wrap&#160;around&#160;the&#160;axis&#160;endpoint  
(2)&#160;if&#160;j>N,&#160;the&#160;interval&#160;wraps&#160;around,&#160;and&#160;is&#160;equivalent&#160;to&#160;the  
two&#160;consecutive&#160;intervals&#160;[i,N),&#160;[0,j-N)  
For&#160;example,&#160;if&#160;the&#160;vector&#160;is&#160;[0,2,4,...,358]&#160;of&#160;length&#160;180,  
and&#160;the&#160;coordinate&#160;interval&#160;is&#160;[-5,5),&#160;the&#160;return&#160;index&#160;interval&#160;is  
[178,183).&#160;This&#160;is&#160;equivalent&#160;to&#160;the&#160;two&#160;intervals&#160;[178,180)&#160;and&#160;[0,3).  
  
Note:&#160;if&#160;the&#160;interval&#160;is&#160;interior&#160;to&#160;the&#160;axis,&#160;but&#160;does&#160;not&#160;span&#160;any  
axis&#160;element,&#160;a&#160;singleton&#160;(i,i+1)&#160;indicating&#160;an&#160;adjacent&#160;index&#160;is&#160;returned. `

 mapIntervalExt  (self, interval, indicator  ='ccn'  , cycle  =None  , epsilon  =None  ) 
     ` Like&#160;mapInterval,&#160;but&#160;returns&#160;(i,j,k)&#160;where&#160;k&#160;is&#160;stride,   
and&#160;(i,j)&#160;is&#160;not&#160;restricted&#160;to&#160;one&#160;cycle. `

 rank  (self) 

 setCalendar  (self, calendar, persistent  =1  ) 
     ` #&#160;Set&#160;the&#160;calendar `

 subAxis  = subaxis(self, i, j, k  =1  ) 
     ` Create&#160;a&#160;transient&#160;axis&#160;for&#160;the&#160;index&#160;slice&#160;[i:j:k]   
The&#160;stride&#160;k&#160;can&#160;be&#160;positive&#160;or&#160;negative.&#160;Wraparound&#160;is  
supported&#160;for&#160;longitude&#160;dimensions&#160;or&#160;those&#160;with&#160;a&#160;modulus&#160;attribute. `

 subaxis  (self, i, j, k  =1  ) 
     ` Create&#160;a&#160;transient&#160;axis&#160;for&#160;the&#160;index&#160;slice&#160;[i:j:k]   
The&#160;stride&#160;k&#160;can&#160;be&#160;positive&#160;or&#160;negative.&#160;Wraparound&#160;is  
supported&#160;for&#160;longitude&#160;dimensions&#160;or&#160;those&#160;with&#160;a&#160;modulus&#160;attribute. `

 toRelativeTime  (self, units, calendar  =None  ) 
     ` Convert&#160;time&#160;axis&#160;values&#160;to&#160;another&#160;unit `

 validateBounds  (self, bounds) 
     ` #&#160;Check&#160;that&#160;a&#160;boundary&#160;array&#160;is&#160;valid,&#160;raise&#160;exception&#160;if&#160;not.&#160;bounds&#160;is&#160;an&#160;array&#160;of&#160;shape&#160;(n,2) `

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

 __getattr__  (self, name) 

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

  
class  TransientAxis  ( [ AbstractAxis ](/cdms.axis.html) )

` `

` #&#160;In-memory&#160;coordinate&#160;axis  
`

Method resolution order:

     [ TransientAxis ](/cdms.axis.html)
     [ AbstractAxis ](/cdms.axis.html)
     [ cdms.cdmsobj.CdmsObj ](/cdms.cdmsobj.html)
     [ cdms.internattr.InternalAttributesClass ](/cdms.internattr.html)
     [ PropertiedClasses.Properties.PropertiedClass ](/PropertiedClasses.Properties.html)

* * *

Methods defined here:  

 __getitem__  (self, key) 

 __getslice__  (self, low, high) 

 __init__  (self, data, bounds  =None  , id  =None  , attributes  =None  , copy  =0  ) 

 __len__  (self) 

 __setitem__  (self, index, value) 

 __setslice__  (self, low, high, value) 

 getBounds  (self) 

 getData  (self) 

 getExplicitBounds  (self) 

 isLinear  (self) 

 setBounds  (self, bounds, persistent  =0  , validate  =0  , index  =None  , boundsid  =None  ) 
     ` #&#160;Set&#160;bounds.&#160;The&#160;persistent&#160;argument&#160;is&#160;for&#160;compatibility&#160;with   
#&#160;persistent&#160;versions,&#160;is&#160;ignored.&#160;Same&#160;for&#160;boundsid&#160;and&#160;index.  
#  
#&#160;mf&#160;20010308&#160;-&#160;add&#160;validate&#160;key&#160;word,&#160;by&#160;default&#160;do&#160;not&#160;validate `

 typecode  (self) 

* * *

Data and other attributes defined here:  

 axis_count  = 0 

* * *

Methods inherited from [ AbstractAxis ](/cdms.axis.html) :  

 __repr__  = __str__(self) 

 __str__  (self) 

 asComponentTime  (self, calendar  =None  ) 
     ` Array&#160;version&#160;of&#160;cdtime&#160;tocomp.&#160;Returns&#160;a&#160;list&#160;of&#160;component&#160;times. `

 asDTGTime  (self, calendar  =None  ) 
     ` Array&#160;version&#160;of&#160;cdtime&#160;tocomp.&#160;Returns&#160;a&#160;list&#160;of&#160;component&#160;times&#160;in&#160;DTG&#160;format. `

 asRelativeTime  (self) 
     ` Array&#160;version&#160;of&#160;cdtime&#160;torel.&#160;Returns&#160;a&#160;list&#160;of&#160;component&#160;times. `

 assignValue  (self, data) 

 clone  (self, copyData  =1  ) 
     ` clone&#160;(self,&#160;copyData=1)   
Return&#160;a&#160;copy&#160;of&#160;self&#160;as&#160;a&#160;transient&#160;axis.  
If&#160;copyData&#160;is&#160;1,&#160;make&#160;a&#160;separate&#160;copy&#160;of&#160;the&#160;data. `

 designateCircular  (self, modulo, persistent  =0  ) 

 designateLatitude  (self, persistent  =0  ) 
     ` #&#160;Designate&#160;axis&#160;as&#160;a&#160;latitude&#160;axis.   
#&#160;If&#160;persistent&#160;is&#160;true,&#160;write&#160;metadata&#160;to&#160;the&#160;container. `

 designateLevel  (self, persistent  =0  ) 
     ` #&#160;Designate&#160;axis&#160;as&#160;a&#160;vertical&#160;level&#160;axis   
#&#160;If&#160;persistent&#160;is&#160;true,&#160;write&#160;metadata&#160;to&#160;the&#160;container. `

 designateLongitude  (self, persistent  =0  , modulo  =360.0  ) 
     ` #&#160;Designate&#160;axis&#160;as&#160;a&#160;longitude&#160;axis   
#&#160;If&#160;persistent&#160;is&#160;true,&#160;write&#160;metadata&#160;to&#160;the&#160;container.  
#&#160;If&#160;modulo&#160;is&#160;defined,&#160;set&#160;as&#160;circular `

 designateTime  (self, persistent  =0  , calendar  =4369  ) 
     ` #&#160;Designate&#160;axis&#160;as&#160;a&#160;time&#160;axis,&#160;and&#160;optionally&#160;set&#160;the&#160;calendar   
#&#160;If&#160;persistent&#160;is&#160;true,&#160;write&#160;metadata&#160;to&#160;the&#160;container. `

 genGenericBounds  (self, width  =1.0  ) 
     ` #&#160;Generate&#160;bounds&#160;from&#160;midpoints.&#160;width&#160;is&#160;the&#160;width&#160;of&#160;the&#160;zone&#160;if&#160;the&#160;axis&#160;has&#160;one&#160;value. `

 getCalendar  (self) 
     ` #&#160;Return&#160;the&#160;cdtime&#160;calendar:&#160;GregorianCalendar,&#160;NoLeapCalendar,&#160;JulianCalendar,&#160;Calendar360   
#&#160;or&#160;None.&#160;If&#160;the&#160;axis&#160;does&#160;not&#160;have&#160;a&#160;calendar&#160;attribute,&#160;return&#160;the&#160;global  
#&#160;calendar. `

 getModulo  (self) 

 getModuloCycle  (self) 

 getValue  (self) 
     ` #&#160;Return&#160;the&#160;entire&#160;array `

 info  (self, flag  =None  , device  =None  ) 
     ` Write&#160;info&#160;about&#160;axis;&#160;include&#160;dimension&#160;values&#160;and&#160;weights&#160;if&#160;flag `

 isCircular  (self) 
     ` #&#160;Return&#160;true&#160;iff&#160;the&#160;axis&#160;wraps&#160;around   
#&#160;An&#160;axis&#160;is&#160;defined&#160;as&#160;circular&#160;if:  
#&#160;(1)&#160;self.  topology  =='circular',&#160;or  
#&#160;(2)&#160;self.  topology  is&#160;undefined,&#160;and&#160;the&#160;axis&#160;is&#160;a&#160;longitude `

 isCircularAxis  (self) 
     ` #&#160;Return&#160;true&#160;iff&#160;the&#160;axis&#160;wraps&#160;around   
#&#160;An&#160;axis&#160;is&#160;defined&#160;as&#160;circular&#160;if:  
#&#160;(1)&#160;self.  topology  =='circular',&#160;or  
#&#160;(2)&#160;self.  topology  is&#160;undefined,&#160;and&#160;the&#160;axis&#160;is&#160;a&#160;longitude `

 isLatitude  (self) 
     ` #&#160;Return&#160;true&#160;iff&#160;the&#160;axis&#160;is&#160;a&#160;latitude&#160;axis `

 isLevel  (self) 
     ` #&#160;Return&#160;true&#160;iff&#160;the&#160;axis&#160;is&#160;a&#160;level&#160;axis `

 isLongitude  (self) 
     ` #&#160;Return&#160;true&#160;iff&#160;the&#160;axis&#160;is&#160;a&#160;longitude&#160;axis `

 isTime  (self) 
     ` #&#160;Return&#160;true&#160;iff&#160;the&#160;axis&#160;is&#160;a&#160;time&#160;axis `

 isVirtual  (self) 
     ` Return&#160;true&#160;iff&#160;coordinate&#160;values&#160;are&#160;implicitly&#160;defined. `

 listall  (self, all  =None  ) 
     ` Get&#160;list&#160;of&#160;info&#160;about&#160;this&#160;axis. `

 mapInterval  (self, interval, indicator  ='ccn'  , cycle  =None  ) 
     ` Map&#160;coordinate&#160;interval&#160;to&#160;index&#160;interval.&#160;interval&#160;has&#160;one&#160;of&#160;the&#160;forms:   
  
(x,y)  
(x,y,indicator):&#160;indicator&#160;overrides&#160;keywork&#160;argument  
(x,y,indicator,cycle):&#160;indicator,&#160;cycle&#160;override&#160;keyword&#160;arguments  
None:&#160;indicates&#160;the&#160;full&#160;interval  
  
where&#160;x&#160;and&#160;y&#160;are&#160;the&#160;endpoints&#160;in&#160;coordinate&#160;space.&#160;indicator&#160;is&#160;a  
two-character&#160;string,&#160;where&#160;the&#160;first&#160;character&#160;is&#160;'c'&#160;if&#160;the&#160;interval  
is&#160;closed&#160;on&#160;the&#160;left,&#160;'o'&#160;if&#160;open,&#160;and&#160;the&#160;second&#160;character&#160;has&#160;the  
same&#160;meaning&#160;for&#160;the&#160;right-hand&#160;point.&#160;Set&#160;cycle&#160;to&#160;a&#160;nonzero&#160;value  
to&#160;force&#160;wraparound.  
  
Returns&#160;the&#160;corresponding&#160;index&#160;interval&#160;(i,j),&#160;where&#160;i<j,&#160;indicating  
the&#160;half-open&#160;index&#160;interval&#160;[i,j),&#160;or&#160;None&#160;if&#160;the&#160;intersection&#160;is&#160;empty.  
  
For&#160;an&#160;axis&#160;which&#160;is&#160;circular&#160;(self.  topology  ==&#160;'circular'),&#160;[i,j)  
is&#160;interpreted&#160;as&#160;follows&#160;(where&#160;N&#160;=&#160;len(self)):  
  
(1)&#160;if&#160;j<=N,&#160;the&#160;interval&#160;does&#160;not&#160;wrap&#160;around&#160;the&#160;axis&#160;endpoint  
(2)&#160;if&#160;j>N,&#160;the&#160;interval&#160;wraps&#160;around,&#160;and&#160;is&#160;equivalent&#160;to&#160;the  
two&#160;consecutive&#160;intervals&#160;[i,N),&#160;[0,j-N)  
For&#160;example,&#160;if&#160;the&#160;vector&#160;is&#160;[0,2,4,...,358]&#160;of&#160;length&#160;180,  
and&#160;the&#160;coordinate&#160;interval&#160;is&#160;[-5,5),&#160;the&#160;return&#160;index&#160;interval&#160;is  
[178,183).&#160;This&#160;is&#160;equivalent&#160;to&#160;the&#160;two&#160;intervals&#160;[178,180)&#160;and&#160;[0,3).  
  
Note:&#160;if&#160;the&#160;interval&#160;is&#160;interior&#160;to&#160;the&#160;axis,&#160;but&#160;does&#160;not&#160;span&#160;any  
axis&#160;element,&#160;a&#160;singleton&#160;(i,i+1)&#160;indicating&#160;an&#160;adjacent&#160;index&#160;is&#160;returned. `

 mapIntervalExt  (self, interval, indicator  ='ccn'  , cycle  =None  , epsilon  =None  ) 
     ` Like&#160;mapInterval,&#160;but&#160;returns&#160;(i,j,k)&#160;where&#160;k&#160;is&#160;stride,   
and&#160;(i,j)&#160;is&#160;not&#160;restricted&#160;to&#160;one&#160;cycle. `

 rank  (self) 

 setCalendar  (self, calendar, persistent  =1  ) 
     ` #&#160;Set&#160;the&#160;calendar `

 subAxis  = subaxis(self, i, j, k  =1  ) 
     ` Create&#160;a&#160;transient&#160;axis&#160;for&#160;the&#160;index&#160;slice&#160;[i:j:k]   
The&#160;stride&#160;k&#160;can&#160;be&#160;positive&#160;or&#160;negative.&#160;Wraparound&#160;is  
supported&#160;for&#160;longitude&#160;dimensions&#160;or&#160;those&#160;with&#160;a&#160;modulus&#160;attribute. `

 subaxis  (self, i, j, k  =1  ) 
     ` Create&#160;a&#160;transient&#160;axis&#160;for&#160;the&#160;index&#160;slice&#160;[i:j:k]   
The&#160;stride&#160;k&#160;can&#160;be&#160;positive&#160;or&#160;negative.&#160;Wraparound&#160;is  
supported&#160;for&#160;longitude&#160;dimensions&#160;or&#160;those&#160;with&#160;a&#160;modulus&#160;attribute. `

 toRelativeTime  (self, units, calendar  =None  ) 
     ` Convert&#160;time&#160;axis&#160;values&#160;to&#160;another&#160;unit `

 validateBounds  (self, bounds) 
     ` #&#160;Check&#160;that&#160;a&#160;boundary&#160;array&#160;is&#160;valid,&#160;raise&#160;exception&#160;if&#160;not.&#160;bounds&#160;is&#160;an&#160;array&#160;of&#160;shape&#160;(n,2) `

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

  
class  TransientVirtualAxis  ( [ TransientAxis ](/cdms.axis.html) )

` `

` An&#160;axis&#160;with&#160;no&#160;explicit&#160;representation&#160;of&#160;data&#160;values.  
It&#160;appears&#160;to&#160;be&#160;a&#160;float&#160;vector&#160;with&#160;values&#160;[0.0,&#160;1.0,&#160;...,&#160;float(axislen-1)]  
`

Method resolution order:

     [ TransientVirtualAxis ](/cdms.axis.html)
     [ TransientAxis ](/cdms.axis.html)
     [ AbstractAxis ](/cdms.axis.html)
     [ cdms.cdmsobj.CdmsObj ](/cdms.cdmsobj.html)
     [ cdms.internattr.InternalAttributesClass ](/cdms.internattr.html)
     [ PropertiedClasses.Properties.PropertiedClass ](/PropertiedClasses.Properties.html)

* * *

Methods defined here:  

 __getitem__  (self, key) 

 __getslice__  (self, low, high) 

 __init__  (self, axisname, axislen) 

 __len__  (self) 

 __repr__  = [ __str__ ](/) (self) 

 __str__  (self) 

 clone  (self, copyData  =1  ) 
     ` clone&#160;(self,&#160;copyData=1)   
Return&#160;a&#160;copy&#160;of&#160;self&#160;as&#160;a&#160;transient&#160;virtual&#160;axis.  
If&#160;copyData&#160;is&#160;1,&#160;make&#160;a&#160;separate&#160;copy&#160;of&#160;the&#160;data. `

 getData  (self) 

 isCircular  (self) 

 isVirtual  (self) 
     ` Return&#160;true&#160;iff&#160;coordinate&#160;values&#160;are&#160;implicitly&#160;defined. `

 setBounds  (self, bounds) 
     ` No&#160;boundaries&#160;on&#160;virtual&#160;axes `

* * *

Methods inherited from [ TransientAxis ](/cdms.axis.html) :  

 __setitem__  (self, index, value) 

 __setslice__  (self, low, high, value) 

 getBounds  (self) 

 getExplicitBounds  (self) 

 isLinear  (self) 

 typecode  (self) 

* * *

Data and other attributes inherited from [ TransientAxis ](/cdms.axis.html) :  

 axis_count  = 0 

* * *

Methods inherited from [ AbstractAxis ](/cdms.axis.html) :  

 asComponentTime  (self, calendar  =None  ) 
     ` Array&#160;version&#160;of&#160;cdtime&#160;tocomp.&#160;Returns&#160;a&#160;list&#160;of&#160;component&#160;times. `

 asDTGTime  (self, calendar  =None  ) 
     ` Array&#160;version&#160;of&#160;cdtime&#160;tocomp.&#160;Returns&#160;a&#160;list&#160;of&#160;component&#160;times&#160;in&#160;DTG&#160;format. `

 asRelativeTime  (self) 
     ` Array&#160;version&#160;of&#160;cdtime&#160;torel.&#160;Returns&#160;a&#160;list&#160;of&#160;component&#160;times. `

 assignValue  (self, data) 

 designateCircular  (self, modulo, persistent  =0  ) 

 designateLatitude  (self, persistent  =0  ) 
     ` #&#160;Designate&#160;axis&#160;as&#160;a&#160;latitude&#160;axis.   
#&#160;If&#160;persistent&#160;is&#160;true,&#160;write&#160;metadata&#160;to&#160;the&#160;container. `

 designateLevel  (self, persistent  =0  ) 
     ` #&#160;Designate&#160;axis&#160;as&#160;a&#160;vertical&#160;level&#160;axis   
#&#160;If&#160;persistent&#160;is&#160;true,&#160;write&#160;metadata&#160;to&#160;the&#160;container. `

 designateLongitude  (self, persistent  =0  , modulo  =360.0  ) 
     ` #&#160;Designate&#160;axis&#160;as&#160;a&#160;longitude&#160;axis   
#&#160;If&#160;persistent&#160;is&#160;true,&#160;write&#160;metadata&#160;to&#160;the&#160;container.  
#&#160;If&#160;modulo&#160;is&#160;defined,&#160;set&#160;as&#160;circular `

 designateTime  (self, persistent  =0  , calendar  =4369  ) 
     ` #&#160;Designate&#160;axis&#160;as&#160;a&#160;time&#160;axis,&#160;and&#160;optionally&#160;set&#160;the&#160;calendar   
#&#160;If&#160;persistent&#160;is&#160;true,&#160;write&#160;metadata&#160;to&#160;the&#160;container. `

 genGenericBounds  (self, width  =1.0  ) 
     ` #&#160;Generate&#160;bounds&#160;from&#160;midpoints.&#160;width&#160;is&#160;the&#160;width&#160;of&#160;the&#160;zone&#160;if&#160;the&#160;axis&#160;has&#160;one&#160;value. `

 getCalendar  (self) 
     ` #&#160;Return&#160;the&#160;cdtime&#160;calendar:&#160;GregorianCalendar,&#160;NoLeapCalendar,&#160;JulianCalendar,&#160;Calendar360   
#&#160;or&#160;None.&#160;If&#160;the&#160;axis&#160;does&#160;not&#160;have&#160;a&#160;calendar&#160;attribute,&#160;return&#160;the&#160;global  
#&#160;calendar. `

 getModulo  (self) 

 getModuloCycle  (self) 

 getValue  (self) 
     ` #&#160;Return&#160;the&#160;entire&#160;array `

 info  (self, flag  =None  , device  =None  ) 
     ` Write&#160;info&#160;about&#160;axis;&#160;include&#160;dimension&#160;values&#160;and&#160;weights&#160;if&#160;flag `

 isCircularAxis  (self) 
     ` #&#160;Return&#160;true&#160;iff&#160;the&#160;axis&#160;wraps&#160;around   
#&#160;An&#160;axis&#160;is&#160;defined&#160;as&#160;circular&#160;if:  
#&#160;(1)&#160;self.  topology  =='circular',&#160;or  
#&#160;(2)&#160;self.  topology  is&#160;undefined,&#160;and&#160;the&#160;axis&#160;is&#160;a&#160;longitude `

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

 mapInterval  (self, interval, indicator  ='ccn'  , cycle  =None  ) 
     ` Map&#160;coordinate&#160;interval&#160;to&#160;index&#160;interval.&#160;interval&#160;has&#160;one&#160;of&#160;the&#160;forms:   
  
(x,y)  
(x,y,indicator):&#160;indicator&#160;overrides&#160;keywork&#160;argument  
(x,y,indicator,cycle):&#160;indicator,&#160;cycle&#160;override&#160;keyword&#160;arguments  
None:&#160;indicates&#160;the&#160;full&#160;interval  
  
where&#160;x&#160;and&#160;y&#160;are&#160;the&#160;endpoints&#160;in&#160;coordinate&#160;space.&#160;indicator&#160;is&#160;a  
two-character&#160;string,&#160;where&#160;the&#160;first&#160;character&#160;is&#160;'c'&#160;if&#160;the&#160;interval  
is&#160;closed&#160;on&#160;the&#160;left,&#160;'o'&#160;if&#160;open,&#160;and&#160;the&#160;second&#160;character&#160;has&#160;the  
same&#160;meaning&#160;for&#160;the&#160;right-hand&#160;point.&#160;Set&#160;cycle&#160;to&#160;a&#160;nonzero&#160;value  
to&#160;force&#160;wraparound.  
  
Returns&#160;the&#160;corresponding&#160;index&#160;interval&#160;(i,j),&#160;where&#160;i<j,&#160;indicating  
the&#160;half-open&#160;index&#160;interval&#160;[i,j),&#160;or&#160;None&#160;if&#160;the&#160;intersection&#160;is&#160;empty.  
  
For&#160;an&#160;axis&#160;which&#160;is&#160;circular&#160;(self.  topology  ==&#160;'circular'),&#160;[i,j)  
is&#160;interpreted&#160;as&#160;follows&#160;(where&#160;N&#160;=&#160;len(self)):  
  
(1)&#160;if&#160;j<=N,&#160;the&#160;interval&#160;does&#160;not&#160;wrap&#160;around&#160;the&#160;axis&#160;endpoint  
(2)&#160;if&#160;j>N,&#160;the&#160;interval&#160;wraps&#160;around,&#160;and&#160;is&#160;equivalent&#160;to&#160;the  
two&#160;consecutive&#160;intervals&#160;[i,N),&#160;[0,j-N)  
For&#160;example,&#160;if&#160;the&#160;vector&#160;is&#160;[0,2,4,...,358]&#160;of&#160;length&#160;180,  
and&#160;the&#160;coordinate&#160;interval&#160;is&#160;[-5,5),&#160;the&#160;return&#160;index&#160;interval&#160;is  
[178,183).&#160;This&#160;is&#160;equivalent&#160;to&#160;the&#160;two&#160;intervals&#160;[178,180)&#160;and&#160;[0,3).  
  
Note:&#160;if&#160;the&#160;interval&#160;is&#160;interior&#160;to&#160;the&#160;axis,&#160;but&#160;does&#160;not&#160;span&#160;any  
axis&#160;element,&#160;a&#160;singleton&#160;(i,i+1)&#160;indicating&#160;an&#160;adjacent&#160;index&#160;is&#160;returned. `

 mapIntervalExt  (self, interval, indicator  ='ccn'  , cycle  =None  , epsilon  =None  ) 
     ` Like&#160;mapInterval,&#160;but&#160;returns&#160;(i,j,k)&#160;where&#160;k&#160;is&#160;stride,   
and&#160;(i,j)&#160;is&#160;not&#160;restricted&#160;to&#160;one&#160;cycle. `

 rank  (self) 

 setCalendar  (self, calendar, persistent  =1  ) 
     ` #&#160;Set&#160;the&#160;calendar `

 subAxis  = subaxis(self, i, j, k  =1  ) 
     ` Create&#160;a&#160;transient&#160;axis&#160;for&#160;the&#160;index&#160;slice&#160;[i:j:k]   
The&#160;stride&#160;k&#160;can&#160;be&#160;positive&#160;or&#160;negative.&#160;Wraparound&#160;is  
supported&#160;for&#160;longitude&#160;dimensions&#160;or&#160;those&#160;with&#160;a&#160;modulus&#160;attribute. `

 subaxis  (self, i, j, k  =1  ) 
     ` Create&#160;a&#160;transient&#160;axis&#160;for&#160;the&#160;index&#160;slice&#160;[i:j:k]   
The&#160;stride&#160;k&#160;can&#160;be&#160;positive&#160;or&#160;negative.&#160;Wraparound&#160;is  
supported&#160;for&#160;longitude&#160;dimensions&#160;or&#160;those&#160;with&#160;a&#160;modulus&#160;attribute. `

 toRelativeTime  (self, units, calendar  =None  ) 
     ` Convert&#160;time&#160;axis&#160;values&#160;to&#160;another&#160;unit `

 validateBounds  (self, bounds) 
     ` #&#160;Check&#160;that&#160;a&#160;boundary&#160;array&#160;is&#160;valid,&#160;raise&#160;exception&#160;if&#160;not.&#160;bounds&#160;is&#160;an&#160;array&#160;of&#160;shape&#160;(n,2) `

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

 allclose  (ax1, ax2, rtol  =1.0000000000000001e-05  , atol  =1e-08  ) 
     ` True&#160;if&#160;all&#160;elements&#160;of&#160;axes&#160;ax1&#160;and&#160;ax2&#160;are&#160;close,   
in&#160;the&#160;sense&#160;of&#160;MA.allclose. `

 axisMatchAxis  (axes, specifications  =None  , omit  =None  , order  =None  ) 
     ` Given&#160;a&#160;list&#160;of&#160;axes&#160;and&#160;a&#160;specification&#160;or&#160;list&#160;of   
specificatons,&#160;and&#160;a&#160;specification&#160;or&#160;list&#160;of&#160;specifications  
of&#160;those&#160;axes&#160;to&#160;omit,&#160;return&#160;a&#160;list&#160;of  
those&#160;axes&#160;in&#160;the&#160;list&#160;that&#160;match&#160;the&#160;specification&#160;but  
do&#160;not&#160;include&#160;in&#160;the&#160;list&#160;any&#160;axes&#160;that&#160;matches&#160;an&#160;omit  
specification.  
  
If&#160;specifications&#160;is&#160;None,&#160;include&#160;all&#160;axes&#160;less&#160;the&#160;omitted&#160;ones.  
  
Individual&#160;specifications&#160;must&#160;be&#160;integer&#160;indices&#160;into&#160;axes&#160;or  
matching&#160;criteria&#160;as&#160;detailed&#160;in&#160;axisMatches.  
  
Axes&#160;are&#160;returned&#160;in&#160;the&#160;order&#160;they&#160;occur&#160;in&#160;the&#160;axes&#160;argument&#160;unless  
order&#160;is&#160;given.  
  
order&#160;can&#160;be&#160;a&#160;string&#160;containing&#160;the&#160;symbols&#160;t,x,y,z,&#160;or&#160;-.  
If&#160;a&#160;-&#160;is&#160;given,&#160;any&#160;elements&#160;of&#160;the&#160;result&#160;not&#160;chosen&#160;otherwise&#160;are  
filled&#160;in&#160;from&#160;left&#160;to&#160;right&#160;with&#160;remaining&#160;candidates. `

 axisMatchIndex  (axes, specifications  =None  , omit  =None  , order  =None  ) 
     ` Given&#160;a&#160;list&#160;of&#160;axes&#160;and&#160;a&#160;specification&#160;or&#160;list&#160;of   
specificatons,&#160;and&#160;a&#160;specification&#160;or&#160;list&#160;of&#160;specifications  
of&#160;those&#160;axes&#160;to&#160;omit,&#160;return&#160;a&#160;list&#160;of&#160;the&#160;indices&#160;of  
those&#160;axes&#160;in&#160;the&#160;list&#160;that&#160;match&#160;the&#160;specification&#160;but  
do&#160;not&#160;include&#160;in&#160;the&#160;list&#160;any&#160;axes&#160;that&#160;matches&#160;an&#160;omit  
specification.  
  
If&#160;specifications&#160;is&#160;None,&#160;include&#160;all&#160;axes&#160;less&#160;the&#160;omitted&#160;ones.  
  
Individual&#160;specifications&#160;must&#160;be&#160;integer&#160;indices&#160;into&#160;axes&#160;or  
matching&#160;criteria&#160;as&#160;detailed&#160;in&#160;axisMatches.  
  
The&#160;indices&#160;of&#160;axes&#160;are&#160;returned&#160;in&#160;the&#160;order&#160;the&#160;axes  
occur&#160;in&#160;the&#160;axes&#160;argument,&#160;unless&#160;order&#160;is&#160;given.  
  
order&#160;can&#160;be&#160;a&#160;string&#160;containing&#160;the&#160;symbols&#160;t,x,y,z,&#160;or&#160;-.  
If&#160;a&#160;-&#160;is&#160;given,&#160;any&#160;elements&#160;of&#160;the&#160;result&#160;not&#160;chosen&#160;otherwise&#160;are  
filled&#160;in&#160;from&#160;left&#160;to&#160;right&#160;with&#160;remaining&#160;candidates. `

 axisMatches  (axis, specification) 
     ` Return&#160;1&#160;or&#160;0&#160;depending&#160;on&#160;whether&#160;axis&#160;matches&#160;the&#160;specification.   
Specification&#160;must&#160;be&#160;one&#160;of:  
1.&#160;a&#160;string&#160;representing&#160;an&#160;axis&#160;id&#160;or&#160;one&#160;of  
the&#160;keywords&#160;time,&#160;latitude&#160;or&#160;lat,&#160;longitude&#160;or&#160;lon,&#160;or  
lev&#160;or&#160;level.  
  
axis&#160;may&#160;be&#160;surrounded&#160;with&#160;parentheses&#160;or&#160;spaces.  
  
We&#160;first&#160;attempt&#160;to&#160;match&#160;the&#160;axis&#160;id&#160;and&#160;the&#160;specification.  
Keywords&#160;try&#160;to&#160;match&#160;using&#160;isTime,&#160;isLatitude,&#160;etc.  
Comparisons&#160;to&#160;keywords&#160;and&#160;axis&#160;ids&#160;is&#160;case-insensitive.  
  
2.&#160;a&#160;function&#160;that&#160;takes&#160;an&#160;axis&#160;as&#160;an&#160;argument&#160;and&#160;returns&#160;a&#160;value.  
if&#160;the&#160;value&#160;returned&#160;is&#160;true,&#160;the&#160;axis&#160;matches.  
  
3.&#160;an&#160;axis&#160;object;&#160;will&#160;match&#160;if&#160;it&#160;is&#160;the&#160;same&#160;object&#160;as&#160;axis. `

 concatenate  (axes, id  =None  , attributes  =None  ) 
     ` Concatenate&#160;the&#160;axes,&#160;return&#160;a&#160;transient&#160;axis. `

 createAxis  (data, bounds  =None  , id  =None  , copy  =0  ) 
     ` #&#160;Create&#160;a&#160;transient&#160;axis `

 createEqualAreaAxis  (nlat) 
     ` #&#160;Generate&#160;an&#160;equal-area&#160;latitude&#160;axis,&#160;north-to-south `

 createGaussianAxis  (nlat) 
     ` #&#160;Generate&#160;a&#160;Gaussian&#160;latitude&#160;axis,&#160;north-to-south `

 createUniformLatitudeAxis  (startLat, nlat, deltaLat) 
     ` #&#160;Generate&#160;a&#160;uniform&#160;latitude&#160;axis `

 createUniformLongitudeAxis  (startLon, nlon, deltaLon) 
     ` #&#160;Generate&#160;a&#160;uniform&#160;longitude&#160;axis `

 getAutoBounds  () 

 isOverlapVector  (vec1, vec2, atol  =1e-08  ) 
     ` Returns&#160;(isoverlap,&#160;index)&#160;where:   
isoverlap&#160;is&#160;true&#160;iff&#160;a&#160;leading&#160;portion&#160;of&#160;vec1&#160;is&#160;a&#160;subset&#160;of&#160;vec2;  
index&#160;is&#160;the&#160;index&#160;such&#160;that&#160;vec1[0]<=vec2[index].&#160;If&#160;index==len(vec2),  
then&#160;vec1[0]>vec2[len(vec2)-1] `

 isSubsetVector  (vec1, vec2, tol) 
     ` #&#160;Return&#160;true&#160;if&#160;vector&#160;vec1&#160;is&#160;a&#160;subset&#160;of&#160;vec2,&#160;within&#160;tolerance&#160;tol.   
#&#160;Return&#160;second&#160;arg&#160;of&#160;index,&#160;if&#160;it&#160;is&#160;a&#160;subset `

 lookupArray  (ar, value) 
     ` Lookup&#160;value&#160;in&#160;array&#160;ar.&#160;Return&#160;index&#160;such&#160;that:   
(a)&#160;ar&#160;is&#160;monotonically&#160;increasing:  
value&#160;<=&#160;ar[index],&#160;index==0..len(ar)-1  
value&#160;>&#160;ar[index],&#160;index==len(ar)  
(b)&#160;ar&#160;is&#160;monotonically&#160;decreasing:  
value&#160;>=&#160;ar[index],&#160;index==0..len(ar)-1  
value&#160;<&#160;ar[index],&#160;index==len(ar) `

 mapLinearExt  (axis, bounds, interval, indicator  ='ccn'  , epsilon  =None  , stride  =1  , wrapped  =0  ) 
     ` Map&#160;coordinate&#160;interval&#160;to&#160;index&#160;interval,&#160;without   
wraparound.&#160;interval&#160;has&#160;the&#160;form&#160;(x,y)&#160;where&#160;x&#160;and&#160;y&#160;are&#160;the  
endpoints&#160;in&#160;coordinate&#160;space.&#160;indicator&#160;is&#160;a&#160;three-character  
string,&#160;where&#160;the&#160;first&#160;character&#160;is&#160;'c'&#160;if&#160;the&#160;interval&#160;is&#160;closed  
on&#160;the&#160;left,&#160;'o'&#160;if&#160;open,&#160;and&#160;the&#160;second&#160;character&#160;has&#160;the&#160;same  
meaning&#160;for&#160;the&#160;right-hand&#160;point.&#160;The&#160;third&#160;character&#160;indicates  
how&#160;the&#160;intersection&#160;of&#160;the&#160;interval&#160;and&#160;axis&#160;is&#160;treated:  
  
'n'&#160;-&#160;the&#160;node&#160;is&#160;in&#160;the&#160;interval  
'b'&#160;-&#160;the&#160;interval&#160;intersects&#160;the&#160;cell&#160;bounds  
's'&#160;-&#160;the&#160;cell&#160;bounds&#160;are&#160;a&#160;subset&#160;of&#160;the&#160;interval  
'e'&#160;-&#160;same&#160;as&#160;'n',&#160;plus&#160;an&#160;extra&#160;node&#160;on&#160;either&#160;side.  
  
Returns&#160;the&#160;corresponding&#160;index&#160;interval&#160;(i,j),&#160;where&#160;i<j,  
indicating&#160;the&#160;half-open&#160;index&#160;interval&#160;[i,j),&#160;or&#160;None&#160;if&#160;the  
intersection&#160;is&#160;empty. `

 mapLinearIntersection  (xind, yind, iind, aMinusEps, aPlusEps, bPlusEps, bMinusEps, boundLeft, nodeSubI, boundRight) 
     ` Return&#160;true&#160;iff&#160;the&#160;coordinate&#160;interval&#160;(a,b)&#160;intersects&#160;the&#160;node   
nodeSubI&#160;or&#160;cell&#160;bounds&#160;[boundLeft,boundRight],&#160;where&#160;the&#160;interval  
(a,b)&#160;is&#160;defined&#160;by:  
  
xind&#160;=&#160;'c'&#160;if&#160;(a,b)&#160;is&#160;closed&#160;on&#160;the&#160;left,&#160;'o'&#160;if&#160;open,  
yind&#160;same&#160;for&#160;right&#160;endpoint  
aMinusEps,aPlusEps&#160;=&#160;a&#160;+/-&#160;epsilon  
bPlusEps,bMinusEps&#160;=&#160;b&#160;+/-&#160;epsilon  
  
and&#160;the&#160;intersection&#160;option&#160;iind&#160;=&#160;'n','b','e','s'&#160;specifies  
whether&#160;the&#160;intersection&#160;is&#160;with&#160;respect&#160;to&#160;the&#160;node&#160;value  
nodeSubI&#160;('n'&#160;or&#160;'e')&#160;or&#160;the&#160;cell&#160;bounds&#160;[boundLeft,boundRight].  
See&#160;mapLinearExt. `

 setAutoBounds  (mode) 
     ` #&#160;Set&#160;autobounds&#160;mode&#160;to&#160;'on'&#160;or&#160;'off'.&#160;If&#160;on,&#160;getBounds&#160;will&#160;automatically   
#&#160;generate&#160;boundary&#160;information&#160;for&#160;an&#160;axis&#160;or&#160;grid,&#160;if&#160;not&#160;explicitly
defined.  
#&#160;If&#160;'off',&#160;and&#160;no&#160;boundary&#160;data&#160;is&#160;explicitly&#160;defined,&#160;the&#160;bounds&#160;will&#160;NOT  
#&#160;be&#160;generated;&#160;getBounds&#160;will&#160;return&#160;None&#160;for&#160;the&#160;boundaries. `

 take  (ax, indices) 
     ` Take&#160;values&#160;indicated&#160;by&#160;indices&#160;list,&#160;return&#160;a&#160;transient&#160;axis. `

  
 Data 

` `

 CdtimeTypes  = (<type 'comptime'>, <type 'reltime'>)   
 FileWasClosed  = 'File was closed for object: '   
 InvalidBoundsArray  = 'Invalid boundary array: '   
 InvalidCalendar  = 'Invalid calendar: '   
 InvalidNCycles  = 'Invalid number of cycles requested for wrapped dimension: '   
 MethodNotImplemented  = 'Method not yet implemented'   
 ReadOnlyAxis  = 'Axis is read-only: '   
 calendarToTag  = {17: '360_day', 4113: 'noleap', 4369: 'proleptic_gregorian', 69905: 'julian', 135441: 'gregorian'}   
 latitude_aliases  = []   
 level_aliases  = ['plev']   
 longitude_aliases  = []   
 std_axis_attributes  = ['name', 'units', 'length', 'values', 'bounds']   
 tagToCalendar  = {'360': 17, '360_day': 17, '365_day': 4113, 'gregorian': 135441, 'julian': 69905, 'noleap': 4113, 'proleptic_gregorian': 4369, 'standard': 4369}   
 time_aliases  = []   
 unspecified  = 'No value specified.' 

* * *

UCRL-WEB-213937 | [ Privacy & Legal Notice ](/disclaimer.html)

[ webmaster@pcmdi.llnl.gov ](/webmaster@pcmdi.llnl.gov)

[ ![Powered by Plone](media/plone_powered.gif) ](/)

