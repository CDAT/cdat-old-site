---
layout: default
title:
---

 [ Skip to content. ](/cdat/source/api-reference/cdms.cdmsNode.html) | [ Skip
to navigation ](/cdat/source/api-reference/cdms.cdmsNode.html)

Search Site

[ Advanced Search&#8230; ](/search_form)

#  [ PCMDI Software Portal ](/)

#####  Sections

  * [ Home ](/)

#####  Personal tools

  * [ Log in ](/login_form)

You are here:  [ Home ](/) -> [ CDAT ](/cdat) -> [ Source Code ](/cdat/source)
-> [ API Reference ](/cdat/source/api-reference) -> Python: module
cdms.cdmsNode

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

        * [ Python: module cdms.cdmsNode ](/cdat/source/api-reference/cdms.cdmsNode.html)

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

  * [ ![Send this page to somebody](media/mail_icon.gif) ](/cdat/source/api-reference/cdms.cdmsNode.html/sendto_form)
  * [ ![Print this page](media/print_icon.gif) ](/this.print\(\))

#  Python: module cdms.cdmsNode

  
  
 [ cdms  ](/cdms.html) .cdmsNode 
[ index ](/)  

` CDMS&#160;node&#160;classes `

  
 Modules 

` `

[ cdms.CDML ](/cdms.CDML.html)  
[ MA ](/MA.html)  

[ Numeric ](/Numeric.html)  
[ cdtime ](/cdtime.html)  

[ re ](/re.html)  
[ string ](/string.html)  

[ sys ](/sys.html)  

  
 Classes 

` `

[ CdmsNode ](/cdms.cdmsNode.html)

    

[ AttrNode ](/cdms.cdmsNode.html)

[ AxisNode ](/cdms.cdmsNode.html)

[ DatasetNode ](/cdms.cdmsNode.html)

[ DocLinkNode ](/cdms.cdmsNode.html)

[ DomElemNode ](/cdms.cdmsNode.html)

[ DomainNode ](/cdms.cdmsNode.html)

[ LinearDataNode ](/cdms.cdmsNode.html)

[ RectGridNode ](/cdms.cdmsNode.html)

[ VariableNode ](/cdms.cdmsNode.html)

[ XLinkNode ](/cdms.cdmsNode.html)

[ cdms.error.CDMSError ](/cdms.error.html) ( [ exceptions.Exception
](/exceptions.html) )

    

[ NotMonotonicError ](/cdms.cdmsNode.html)

  
class  AttrNode  ( [ CdmsNode ](/cdms.cdmsNode.html) )

` `

` #&#160;Attribute&#160;node&#160;-&#160;only&#160;used&#160;as&#160;a&#160;placeholder&#160;during&#160;parse&#160;and&#160;write  
#&#160;&#160;&#160;Attr&#160;nodes&#160;are&#160;not&#160;placed&#160;on&#160;the&#160;tree  
#  
#&#160;Two&#160;ways&#160;to&#160;create&#160;an&#160;Attr&#160;object:  
#&#160;(1)&#160;attr&#160;= [ AttrNode ](/) (name,value)  
#&#160;&#160;&#160;&#160;&#160;datatype&#160;=&#160;sometype&#160;#&#160;optionally,&#160;to&#160;override&#160;intrinsic&#160;type  
#&#160;(2)&#160;attr&#160;= [ AttrNode ](/) (name,None)  
#&#160;&#160;&#160;&#160;&#160;attr. [ setValueFromString ](/) (somestring,sometype)  
`

Methods defined here:  

 __init__  (self, name, value  =None  ) 

 getDatatype  (self) 

 getLength  (self) 

 getValueAsString  (self) 

 mapToExternal  (self) 
     ` #&#160;Note:&#160;mapToExternal&#160;is&#160;not&#160;called&#160;at&#160;init&#160;time,&#160;must&#160;be&#160;called&#160;explicitly   
#&#160;&#160;&#160;if&#160;needed `

 setContentFromString  (self, content) 
     ` #&#160;Set&#160;content   
#&#160;This&#160;may&#160;be&#160;called&#160;multiple&#160;times,&#160;so&#160;append `

 setValueFromString  (self, valString, datatype) 
     ` #&#160;Map&#160;a&#160;string&#160;of&#160;a&#160;given&#160;datatype&#160;to&#160;a&#160;value   
#&#160;&#160;&#160;Returns&#160;ValueError&#160;if&#160;the&#160;conversion&#160;fails `

 write  (self, fd  =None  , tablevel  =0  , format  =1  ) 
     ` #&#160;Write&#160;to&#160;a&#160;file,&#160;with&#160;formatting.   
#&#160;tablevel&#160;is&#160;the&#160;start&#160;number&#160;of&#160;tabs `

* * *

Methods inherited from [ CdmsNode ](/cdms.cdmsNode.html) :  

 add  (self, child) 
     ` #&#160;Add&#160;a&#160;child&#160;node `

 children  (self) 
     ` #&#160;Return&#160;a&#160;list&#160;of&#160;child&#160;nodes `

 getChildAt  (self, index) 
     ` #&#160;Get&#160;the&#160;child&#160;node&#160;at&#160;index&#160;k `

 getChildCount  (self) 
     ` #&#160;Get&#160;the&#160;number&#160;of&#160;children `

 getContent  (self) 
     ` #&#160;Get&#160;content `

 getExternalAttr  (self, name) 
     ` #&#160;Get&#160;an&#160;external&#160;attribute `

 getExternalAttrAsAttr  (self, name) 
     ` #&#160;Get&#160;an&#160;external&#160;attribute,&#160;as&#160;an&#160;Attr&#160;instance `

 getExternalDict  (self) 
     ` #&#160;Get&#160;a&#160;dictionary&#160;of&#160;external&#160;attributes,&#160;of&#160;form&#160;(value,datatype) `

 getIndex  (self, node) 
     ` #&#160;Get&#160;the&#160;index&#160;of&#160;a&#160;node `

 getParent  (self) 
     ` #&#160;Get&#160;the&#160;parent&#160;node `

 isLeaf  (self) 
     ` #&#160;True&#160;iff&#160;node&#160;is&#160;a&#160;leaf&#160;node `

 removeChildAt  (self, index) 
     ` #&#160;Remove&#160;and&#160;return&#160;the&#160;child&#160;at&#160;index&#160;k `

 setExternalAttr  (self, name, value, datatype  =None  ) 
     ` #&#160;Set&#160;an&#160;external&#160;attribute `

 setExternalAttrFromAttr  (self, attr) 
     ` #&#160;Set&#160;an&#160;external&#160;attribute   
#&#160;'attr'&#160;is&#160;an&#160;Attr&#160;object `

 setExternalDict  (self, dict) 
     ` #&#160;Set&#160;the&#160;external&#160;attribute&#160;dictionary.&#160;The&#160;input&#160;dictionary   
#&#160;is&#160;of&#160;the&#160;form&#160;{name:value,...}&#160;where&#160;value&#160;is&#160;a&#160;string. `

 validate  (self, idtable  =None  ) 
     ` #&#160;Validate&#160;attributes `

 write_ldif  (self, parentdn, userAttrs  =[]  , fd  =None  , format  =1  ) 
     ` #&#160;Write&#160;an&#160;LDIF&#160;(LDAP&#160;interchange&#160;format)&#160;entry   
#&#160;parentdn&#160;is&#160;the&#160;parent&#160;LDAP&#160;distinguished&#160;name  
#&#160;userAttrs&#160;is&#160;a&#160;string&#160;or&#160;list&#160;of&#160;strings&#160;of&#160;form&#160;"attr:&#160;value"  
#&#160;A&#160;trailing&#160;newline&#160;is&#160;added&#160;iff&#160;format==1  
#&#160;Note:&#160;unlike&#160;write,&#160;this&#160;does&#160;not&#160;write&#160;children&#160;as&#160;well `

 write_raw  (self, fd  =None  ) 
     ` #&#160;Write&#160;to&#160;a&#160;file&#160;without&#160;formatting. `

  
class  AxisNode  ( [ CdmsNode ](/cdms.cdmsNode.html) )

` `

` #&#160;Coordinate&#160;axis  
`

Methods defined here:  

 __init__  (self, id, length, datatype  ='Long'  , data  =None  ) 
     ` #&#160;If&#160;datatype&#160;is&#160;None,&#160;assume&#160;values&#160;[0,1,..,length-1]   
#&#160;data&#160;is&#160;a&#160;Numeric&#160;array,&#160;if&#160;specified `

 __len__  (self) 

 equal  (self, axis) 
     ` #&#160;Test&#160;if&#160;axis&#160;data&#160;vectors&#160;are&#160;equal `

 extend  (self, axis, isreltime  =0  , allowgaps  =0  ) 
     ` #&#160;Extend&#160;axes.&#160;'isreltime'&#160;is&#160;true&#160;iff   
#&#160;the&#160;axes&#160;are&#160;relative&#160;time&#160;axes  
#&#160;If&#160;allowgaps&#160;is&#160;true,&#160;allow&#160;gaps&#160;when&#160;extending&#160;linear&#160;vectors `

 getContent  (self) 
     ` #&#160;Get&#160;the&#160;content&#160;string:&#160;the&#160;data&#160;values&#160;if&#160;the&#160;representation   
#&#160;is&#160;as&#160;a&#160;vector,&#160;or&#160;ane&#160;empty&#160;string&#160;otherwise `

 getData  (self) 
     ` #&#160;Get&#160;the&#160;data&#160;as&#160;an&#160;array `

 isClose  (self, axis, eps) 
     ` #&#160;Test&#160;if&#160;axis&#160;data&#160;vectors&#160;are&#160;element-wise&#160;close   
#&#160;True&#160;iff&#160;for&#160;each&#160;respective&#160;element&#160;a&#160;and&#160;b,&#160;abs((b-a)/b)<=eps `

 mapToExternal  (self) 
     ` #&#160;Map&#160;to&#160;external&#160;attributes `

 monotonicity  (self) 
     ` #&#160;Test&#160;for&#160;strict&#160;monotonicity.   
#&#160;Returns&#160;CdNotMonotonic,&#160;CdIncreasing,&#160;CdDecreasing,&#160;or&#160;CdSingleton `

 setContentFromString  (self, datastring) 
     ` #&#160;Set&#160;data&#160;from&#160;content&#160;string   
#&#160;The&#160;content&#160;of&#160;an&#160;axis&#160;is&#160;the&#160;data&#160;array. `

 setData  (self, data) 
     ` #&#160;Set&#160;the&#160;data&#160;as&#160;an&#160;array,&#160;check&#160;for&#160;monotonicity `

 setLinearData  (self, linearNode, partition  =None  ) 
     ` #&#160;Set&#160;the&#160;data&#160;as&#160;a&#160;linear&#160;vector   
#&#160;If&#160;the&#160;partition&#160;is&#160;set,&#160;derive&#160;the&#160;vector&#160;length&#160;from&#160;it `

 setPartitionFromString  (self, partstring) 
     ` #&#160;Set&#160;the&#160;partition&#160;from&#160;a&#160;string.&#160;This&#160;does&#160;not   
#&#160;set&#160;the&#160;external&#160;string&#160;representation `

* * *

Methods inherited from [ CdmsNode ](/cdms.cdmsNode.html) :  

 add  (self, child) 
     ` #&#160;Add&#160;a&#160;child&#160;node `

 children  (self) 
     ` #&#160;Return&#160;a&#160;list&#160;of&#160;child&#160;nodes `

 getChildAt  (self, index) 
     ` #&#160;Get&#160;the&#160;child&#160;node&#160;at&#160;index&#160;k `

 getChildCount  (self) 
     ` #&#160;Get&#160;the&#160;number&#160;of&#160;children `

 getExternalAttr  (self, name) 
     ` #&#160;Get&#160;an&#160;external&#160;attribute `

 getExternalAttrAsAttr  (self, name) 
     ` #&#160;Get&#160;an&#160;external&#160;attribute,&#160;as&#160;an&#160;Attr&#160;instance `

 getExternalDict  (self) 
     ` #&#160;Get&#160;a&#160;dictionary&#160;of&#160;external&#160;attributes,&#160;of&#160;form&#160;(value,datatype) `

 getIndex  (self, node) 
     ` #&#160;Get&#160;the&#160;index&#160;of&#160;a&#160;node `

 getParent  (self) 
     ` #&#160;Get&#160;the&#160;parent&#160;node `

 isLeaf  (self) 
     ` #&#160;True&#160;iff&#160;node&#160;is&#160;a&#160;leaf&#160;node `

 removeChildAt  (self, index) 
     ` #&#160;Remove&#160;and&#160;return&#160;the&#160;child&#160;at&#160;index&#160;k `

 setExternalAttr  (self, name, value, datatype  =None  ) 
     ` #&#160;Set&#160;an&#160;external&#160;attribute `

 setExternalAttrFromAttr  (self, attr) 
     ` #&#160;Set&#160;an&#160;external&#160;attribute   
#&#160;'attr'&#160;is&#160;an&#160;Attr&#160;object `

 setExternalDict  (self, dict) 
     ` #&#160;Set&#160;the&#160;external&#160;attribute&#160;dictionary.&#160;The&#160;input&#160;dictionary   
#&#160;is&#160;of&#160;the&#160;form&#160;{name:value,...}&#160;where&#160;value&#160;is&#160;a&#160;string. `

 validate  (self, idtable  =None  ) 
     ` #&#160;Validate&#160;attributes `

 write  (self, fd  =None  , tablevel  =0  , format  =1  ) 
     ` #&#160;Write&#160;to&#160;a&#160;file,&#160;with&#160;formatting.   
#&#160;tablevel&#160;is&#160;the&#160;start&#160;number&#160;of&#160;tabs `

 write_ldif  (self, parentdn, userAttrs  =[]  , fd  =None  , format  =1  ) 
     ` #&#160;Write&#160;an&#160;LDIF&#160;(LDAP&#160;interchange&#160;format)&#160;entry   
#&#160;parentdn&#160;is&#160;the&#160;parent&#160;LDAP&#160;distinguished&#160;name  
#&#160;userAttrs&#160;is&#160;a&#160;string&#160;or&#160;list&#160;of&#160;strings&#160;of&#160;form&#160;"attr:&#160;value"  
#&#160;A&#160;trailing&#160;newline&#160;is&#160;added&#160;iff&#160;format==1  
#&#160;Note:&#160;unlike&#160;write,&#160;this&#160;does&#160;not&#160;write&#160;children&#160;as&#160;well `

 write_raw  (self, fd  =None  ) 
     ` #&#160;Write&#160;to&#160;a&#160;file&#160;without&#160;formatting. `

  
class  CdmsNode 

` `

` #&#160;Named&#160;node  
`

Methods defined here:  

 __init__  (self, tag, id  =None  , parent  =None  ) 

 add  (self, child) 
     ` #&#160;Add&#160;a&#160;child&#160;node `

 children  (self) 
     ` #&#160;Return&#160;a&#160;list&#160;of&#160;child&#160;nodes `

 getChildAt  (self, index) 
     ` #&#160;Get&#160;the&#160;child&#160;node&#160;at&#160;index&#160;k `

 getChildCount  (self) 
     ` #&#160;Get&#160;the&#160;number&#160;of&#160;children `

 getContent  (self) 
     ` #&#160;Get&#160;content `

 getExternalAttr  (self, name) 
     ` #&#160;Get&#160;an&#160;external&#160;attribute `

 getExternalAttrAsAttr  (self, name) 
     ` #&#160;Get&#160;an&#160;external&#160;attribute,&#160;as&#160;an&#160;Attr&#160;instance `

 getExternalDict  (self) 
     ` #&#160;Get&#160;a&#160;dictionary&#160;of&#160;external&#160;attributes,&#160;of&#160;form&#160;(value,datatype) `

 getIndex  (self, node) 
     ` #&#160;Get&#160;the&#160;index&#160;of&#160;a&#160;node `

 getParent  (self) 
     ` #&#160;Get&#160;the&#160;parent&#160;node `

 isLeaf  (self) 
     ` #&#160;True&#160;iff&#160;node&#160;is&#160;a&#160;leaf&#160;node `

 mapToExternal  (self) 
     ` #&#160;Map&#160;to&#160;external&#160;attributes `

 removeChildAt  (self, index) 
     ` #&#160;Remove&#160;and&#160;return&#160;the&#160;child&#160;at&#160;index&#160;k `

 setContentFromString  (self, content) 
     ` #&#160;Set&#160;content&#160;from&#160;a&#160;string.&#160;The&#160;interpretation   
#&#160;of&#160;content&#160;is&#160;class-dependent `

 setExternalAttr  (self, name, value, datatype  =None  ) 
     ` #&#160;Set&#160;an&#160;external&#160;attribute `

 setExternalAttrFromAttr  (self, attr) 
     ` #&#160;Set&#160;an&#160;external&#160;attribute   
#&#160;'attr'&#160;is&#160;an&#160;Attr&#160;object `

 setExternalDict  (self, dict) 
     ` #&#160;Set&#160;the&#160;external&#160;attribute&#160;dictionary.&#160;The&#160;input&#160;dictionary   
#&#160;is&#160;of&#160;the&#160;form&#160;{name:value,...}&#160;where&#160;value&#160;is&#160;a&#160;string. `

 validate  (self, idtable  =None  ) 
     ` #&#160;Validate&#160;attributes `

 write  (self, fd  =None  , tablevel  =0  , format  =1  ) 
     ` #&#160;Write&#160;to&#160;a&#160;file,&#160;with&#160;formatting.   
#&#160;tablevel&#160;is&#160;the&#160;start&#160;number&#160;of&#160;tabs `

 write_ldif  (self, parentdn, userAttrs  =[]  , fd  =None  , format  =1  ) 
     ` #&#160;Write&#160;an&#160;LDIF&#160;(LDAP&#160;interchange&#160;format)&#160;entry   
#&#160;parentdn&#160;is&#160;the&#160;parent&#160;LDAP&#160;distinguished&#160;name  
#&#160;userAttrs&#160;is&#160;a&#160;string&#160;or&#160;list&#160;of&#160;strings&#160;of&#160;form&#160;"attr:&#160;value"  
#&#160;A&#160;trailing&#160;newline&#160;is&#160;added&#160;iff&#160;format==1  
#&#160;Note:&#160;unlike&#160;write,&#160;this&#160;does&#160;not&#160;write&#160;children&#160;as&#160;well `

 write_raw  (self, fd  =None  ) 
     ` #&#160;Write&#160;to&#160;a&#160;file&#160;without&#160;formatting. `

  
class  DatasetNode  ( [ CdmsNode ](/cdms.cdmsNode.html) )

` `

` #&#160;Container&#160;object&#160;for&#160;other&#160;CDMS&#160;objects  
`

Methods defined here:  

 __init__  (self, id) 

 addId  (self, id, child) 
     ` #&#160;Add&#160;a&#160;child&#160;node&#160;with&#160;an&#160;ID `

 dump  (self, path  =None  , format  =1  ) 
     ` #&#160;Dump&#160;to&#160;a&#160;CDML&#160;file.   
#&#160;path&#160;is&#160;the&#160;file&#160;to&#160;dump&#160;to,&#160;or&#160;None&#160;for&#160;standard&#160;output.  
#&#160;if&#160;format&#160;is&#160;true,&#160;write&#160;with&#160;tab,&#160;newline&#160;formatting `

 getChildNamed  (self, id) 
     ` #&#160;Get&#160;a&#160;child&#160;node&#160;from&#160;its&#160;ID `

 getIdDict  (self) 
     ` #&#160;Get&#160;the&#160;ID&#160;table `

 validate  (self, idtable  =None  ) 
     ` #&#160;Validate&#160;the&#160;dataset&#160;and&#160;all&#160;child&#160;nodes `

* * *

Methods inherited from [ CdmsNode ](/cdms.cdmsNode.html) :  

 add  (self, child) 
     ` #&#160;Add&#160;a&#160;child&#160;node `

 children  (self) 
     ` #&#160;Return&#160;a&#160;list&#160;of&#160;child&#160;nodes `

 getChildAt  (self, index) 
     ` #&#160;Get&#160;the&#160;child&#160;node&#160;at&#160;index&#160;k `

 getChildCount  (self) 
     ` #&#160;Get&#160;the&#160;number&#160;of&#160;children `

 getContent  (self) 
     ` #&#160;Get&#160;content `

 getExternalAttr  (self, name) 
     ` #&#160;Get&#160;an&#160;external&#160;attribute `

 getExternalAttrAsAttr  (self, name) 
     ` #&#160;Get&#160;an&#160;external&#160;attribute,&#160;as&#160;an&#160;Attr&#160;instance `

 getExternalDict  (self) 
     ` #&#160;Get&#160;a&#160;dictionary&#160;of&#160;external&#160;attributes,&#160;of&#160;form&#160;(value,datatype) `

 getIndex  (self, node) 
     ` #&#160;Get&#160;the&#160;index&#160;of&#160;a&#160;node `

 getParent  (self) 
     ` #&#160;Get&#160;the&#160;parent&#160;node `

 isLeaf  (self) 
     ` #&#160;True&#160;iff&#160;node&#160;is&#160;a&#160;leaf&#160;node `

 mapToExternal  (self) 
     ` #&#160;Map&#160;to&#160;external&#160;attributes `

 removeChildAt  (self, index) 
     ` #&#160;Remove&#160;and&#160;return&#160;the&#160;child&#160;at&#160;index&#160;k `

 setContentFromString  (self, content) 
     ` #&#160;Set&#160;content&#160;from&#160;a&#160;string.&#160;The&#160;interpretation   
#&#160;of&#160;content&#160;is&#160;class-dependent `

 setExternalAttr  (self, name, value, datatype  =None  ) 
     ` #&#160;Set&#160;an&#160;external&#160;attribute `

 setExternalAttrFromAttr  (self, attr) 
     ` #&#160;Set&#160;an&#160;external&#160;attribute   
#&#160;'attr'&#160;is&#160;an&#160;Attr&#160;object `

 setExternalDict  (self, dict) 
     ` #&#160;Set&#160;the&#160;external&#160;attribute&#160;dictionary.&#160;The&#160;input&#160;dictionary   
#&#160;is&#160;of&#160;the&#160;form&#160;{name:value,...}&#160;where&#160;value&#160;is&#160;a&#160;string. `

 write  (self, fd  =None  , tablevel  =0  , format  =1  ) 
     ` #&#160;Write&#160;to&#160;a&#160;file,&#160;with&#160;formatting.   
#&#160;tablevel&#160;is&#160;the&#160;start&#160;number&#160;of&#160;tabs `

 write_ldif  (self, parentdn, userAttrs  =[]  , fd  =None  , format  =1  ) 
     ` #&#160;Write&#160;an&#160;LDIF&#160;(LDAP&#160;interchange&#160;format)&#160;entry   
#&#160;parentdn&#160;is&#160;the&#160;parent&#160;LDAP&#160;distinguished&#160;name  
#&#160;userAttrs&#160;is&#160;a&#160;string&#160;or&#160;list&#160;of&#160;strings&#160;of&#160;form&#160;"attr:&#160;value"  
#&#160;A&#160;trailing&#160;newline&#160;is&#160;added&#160;iff&#160;format==1  
#&#160;Note:&#160;unlike&#160;write,&#160;this&#160;does&#160;not&#160;write&#160;children&#160;as&#160;well `

 write_raw  (self, fd  =None  ) 
     ` #&#160;Write&#160;to&#160;a&#160;file&#160;without&#160;formatting. `

  
class  DocLinkNode  ( [ CdmsNode ](/cdms.cdmsNode.html) )

` `

` #&#160;Link&#160;to&#160;a&#160;document  
`

Methods defined here:  

 __init__  (self, uri, content  =''  ) 

 mapToExternal  (self) 
     ` #&#160;Map&#160;to&#160;external&#160;attributes `

* * *

Methods inherited from [ CdmsNode ](/cdms.cdmsNode.html) :  

 add  (self, child) 
     ` #&#160;Add&#160;a&#160;child&#160;node `

 children  (self) 
     ` #&#160;Return&#160;a&#160;list&#160;of&#160;child&#160;nodes `

 getChildAt  (self, index) 
     ` #&#160;Get&#160;the&#160;child&#160;node&#160;at&#160;index&#160;k `

 getChildCount  (self) 
     ` #&#160;Get&#160;the&#160;number&#160;of&#160;children `

 getContent  (self) 
     ` #&#160;Get&#160;content `

 getExternalAttr  (self, name) 
     ` #&#160;Get&#160;an&#160;external&#160;attribute `

 getExternalAttrAsAttr  (self, name) 
     ` #&#160;Get&#160;an&#160;external&#160;attribute,&#160;as&#160;an&#160;Attr&#160;instance `

 getExternalDict  (self) 
     ` #&#160;Get&#160;a&#160;dictionary&#160;of&#160;external&#160;attributes,&#160;of&#160;form&#160;(value,datatype) `

 getIndex  (self, node) 
     ` #&#160;Get&#160;the&#160;index&#160;of&#160;a&#160;node `

 getParent  (self) 
     ` #&#160;Get&#160;the&#160;parent&#160;node `

 isLeaf  (self) 
     ` #&#160;True&#160;iff&#160;node&#160;is&#160;a&#160;leaf&#160;node `

 removeChildAt  (self, index) 
     ` #&#160;Remove&#160;and&#160;return&#160;the&#160;child&#160;at&#160;index&#160;k `

 setContentFromString  (self, content) 
     ` #&#160;Set&#160;content&#160;from&#160;a&#160;string.&#160;The&#160;interpretation   
#&#160;of&#160;content&#160;is&#160;class-dependent `

 setExternalAttr  (self, name, value, datatype  =None  ) 
     ` #&#160;Set&#160;an&#160;external&#160;attribute `

 setExternalAttrFromAttr  (self, attr) 
     ` #&#160;Set&#160;an&#160;external&#160;attribute   
#&#160;'attr'&#160;is&#160;an&#160;Attr&#160;object `

 setExternalDict  (self, dict) 
     ` #&#160;Set&#160;the&#160;external&#160;attribute&#160;dictionary.&#160;The&#160;input&#160;dictionary   
#&#160;is&#160;of&#160;the&#160;form&#160;{name:value,...}&#160;where&#160;value&#160;is&#160;a&#160;string. `

 validate  (self, idtable  =None  ) 
     ` #&#160;Validate&#160;attributes `

 write  (self, fd  =None  , tablevel  =0  , format  =1  ) 
     ` #&#160;Write&#160;to&#160;a&#160;file,&#160;with&#160;formatting.   
#&#160;tablevel&#160;is&#160;the&#160;start&#160;number&#160;of&#160;tabs `

 write_ldif  (self, parentdn, userAttrs  =[]  , fd  =None  , format  =1  ) 
     ` #&#160;Write&#160;an&#160;LDIF&#160;(LDAP&#160;interchange&#160;format)&#160;entry   
#&#160;parentdn&#160;is&#160;the&#160;parent&#160;LDAP&#160;distinguished&#160;name  
#&#160;userAttrs&#160;is&#160;a&#160;string&#160;or&#160;list&#160;of&#160;strings&#160;of&#160;form&#160;"attr:&#160;value"  
#&#160;A&#160;trailing&#160;newline&#160;is&#160;added&#160;iff&#160;format==1  
#&#160;Note:&#160;unlike&#160;write,&#160;this&#160;does&#160;not&#160;write&#160;children&#160;as&#160;well `

 write_raw  (self, fd  =None  ) 
     ` #&#160;Write&#160;to&#160;a&#160;file&#160;without&#160;formatting. `

  
class  DomElemNode  ( [ CdmsNode ](/cdms.cdmsNode.html) )

` `

` #&#160;Domain&#160;element  
`

Methods defined here:  

 __init__  (self, name, start  =None  , length  =None  ) 

 getName  (self) 
     ` #&#160;Get&#160;the&#160;name `

 mapToExternal  (self) 
     ` #&#160;Map&#160;to&#160;external&#160;attributes `

 setName  (self, name) 
     ` #&#160;Set&#160;the&#160;name `

 write  (self, fd  =None  , tablevel  =0  , format  =1  ) 
     ` #&#160;Write&#160;to&#160;a&#160;file,&#160;with&#160;formatting.   
#&#160;tablevel&#160;is&#160;the&#160;start&#160;number&#160;of&#160;tabs `

* * *

Methods inherited from [ CdmsNode ](/cdms.cdmsNode.html) :  

 add  (self, child) 
     ` #&#160;Add&#160;a&#160;child&#160;node `

 children  (self) 
     ` #&#160;Return&#160;a&#160;list&#160;of&#160;child&#160;nodes `

 getChildAt  (self, index) 
     ` #&#160;Get&#160;the&#160;child&#160;node&#160;at&#160;index&#160;k `

 getChildCount  (self) 
     ` #&#160;Get&#160;the&#160;number&#160;of&#160;children `

 getContent  (self) 
     ` #&#160;Get&#160;content `

 getExternalAttr  (self, name) 
     ` #&#160;Get&#160;an&#160;external&#160;attribute `

 getExternalAttrAsAttr  (self, name) 
     ` #&#160;Get&#160;an&#160;external&#160;attribute,&#160;as&#160;an&#160;Attr&#160;instance `

 getExternalDict  (self) 
     ` #&#160;Get&#160;a&#160;dictionary&#160;of&#160;external&#160;attributes,&#160;of&#160;form&#160;(value,datatype) `

 getIndex  (self, node) 
     ` #&#160;Get&#160;the&#160;index&#160;of&#160;a&#160;node `

 getParent  (self) 
     ` #&#160;Get&#160;the&#160;parent&#160;node `

 isLeaf  (self) 
     ` #&#160;True&#160;iff&#160;node&#160;is&#160;a&#160;leaf&#160;node `

 removeChildAt  (self, index) 
     ` #&#160;Remove&#160;and&#160;return&#160;the&#160;child&#160;at&#160;index&#160;k `

 setContentFromString  (self, content) 
     ` #&#160;Set&#160;content&#160;from&#160;a&#160;string.&#160;The&#160;interpretation   
#&#160;of&#160;content&#160;is&#160;class-dependent `

 setExternalAttr  (self, name, value, datatype  =None  ) 
     ` #&#160;Set&#160;an&#160;external&#160;attribute `

 setExternalAttrFromAttr  (self, attr) 
     ` #&#160;Set&#160;an&#160;external&#160;attribute   
#&#160;'attr'&#160;is&#160;an&#160;Attr&#160;object `

 setExternalDict  (self, dict) 
     ` #&#160;Set&#160;the&#160;external&#160;attribute&#160;dictionary.&#160;The&#160;input&#160;dictionary   
#&#160;is&#160;of&#160;the&#160;form&#160;{name:value,...}&#160;where&#160;value&#160;is&#160;a&#160;string. `

 validate  (self, idtable  =None  ) 
     ` #&#160;Validate&#160;attributes `

 write_ldif  (self, parentdn, userAttrs  =[]  , fd  =None  , format  =1  ) 
     ` #&#160;Write&#160;an&#160;LDIF&#160;(LDAP&#160;interchange&#160;format)&#160;entry   
#&#160;parentdn&#160;is&#160;the&#160;parent&#160;LDAP&#160;distinguished&#160;name  
#&#160;userAttrs&#160;is&#160;a&#160;string&#160;or&#160;list&#160;of&#160;strings&#160;of&#160;form&#160;"attr:&#160;value"  
#&#160;A&#160;trailing&#160;newline&#160;is&#160;added&#160;iff&#160;format==1  
#&#160;Note:&#160;unlike&#160;write,&#160;this&#160;does&#160;not&#160;write&#160;children&#160;as&#160;well `

 write_raw  (self, fd  =None  ) 
     ` #&#160;Write&#160;to&#160;a&#160;file&#160;without&#160;formatting. `

  
class  DomainNode  ( [ CdmsNode ](/cdms.cdmsNode.html) )

` `

` #&#160;Domain  
`

Methods defined here:  

 __init__  (self) 

* * *

Methods inherited from [ CdmsNode ](/cdms.cdmsNode.html) :  

 add  (self, child) 
     ` #&#160;Add&#160;a&#160;child&#160;node `

 children  (self) 
     ` #&#160;Return&#160;a&#160;list&#160;of&#160;child&#160;nodes `

 getChildAt  (self, index) 
     ` #&#160;Get&#160;the&#160;child&#160;node&#160;at&#160;index&#160;k `

 getChildCount  (self) 
     ` #&#160;Get&#160;the&#160;number&#160;of&#160;children `

 getContent  (self) 
     ` #&#160;Get&#160;content `

 getExternalAttr  (self, name) 
     ` #&#160;Get&#160;an&#160;external&#160;attribute `

 getExternalAttrAsAttr  (self, name) 
     ` #&#160;Get&#160;an&#160;external&#160;attribute,&#160;as&#160;an&#160;Attr&#160;instance `

 getExternalDict  (self) 
     ` #&#160;Get&#160;a&#160;dictionary&#160;of&#160;external&#160;attributes,&#160;of&#160;form&#160;(value,datatype) `

 getIndex  (self, node) 
     ` #&#160;Get&#160;the&#160;index&#160;of&#160;a&#160;node `

 getParent  (self) 
     ` #&#160;Get&#160;the&#160;parent&#160;node `

 isLeaf  (self) 
     ` #&#160;True&#160;iff&#160;node&#160;is&#160;a&#160;leaf&#160;node `

 mapToExternal  (self) 
     ` #&#160;Map&#160;to&#160;external&#160;attributes `

 removeChildAt  (self, index) 
     ` #&#160;Remove&#160;and&#160;return&#160;the&#160;child&#160;at&#160;index&#160;k `

 setContentFromString  (self, content) 
     ` #&#160;Set&#160;content&#160;from&#160;a&#160;string.&#160;The&#160;interpretation   
#&#160;of&#160;content&#160;is&#160;class-dependent `

 setExternalAttr  (self, name, value, datatype  =None  ) 
     ` #&#160;Set&#160;an&#160;external&#160;attribute `

 setExternalAttrFromAttr  (self, attr) 
     ` #&#160;Set&#160;an&#160;external&#160;attribute   
#&#160;'attr'&#160;is&#160;an&#160;Attr&#160;object `

 setExternalDict  (self, dict) 
     ` #&#160;Set&#160;the&#160;external&#160;attribute&#160;dictionary.&#160;The&#160;input&#160;dictionary   
#&#160;is&#160;of&#160;the&#160;form&#160;{name:value,...}&#160;where&#160;value&#160;is&#160;a&#160;string. `

 validate  (self, idtable  =None  ) 
     ` #&#160;Validate&#160;attributes `

 write  (self, fd  =None  , tablevel  =0  , format  =1  ) 
     ` #&#160;Write&#160;to&#160;a&#160;file,&#160;with&#160;formatting.   
#&#160;tablevel&#160;is&#160;the&#160;start&#160;number&#160;of&#160;tabs `

 write_ldif  (self, parentdn, userAttrs  =[]  , fd  =None  , format  =1  ) 
     ` #&#160;Write&#160;an&#160;LDIF&#160;(LDAP&#160;interchange&#160;format)&#160;entry   
#&#160;parentdn&#160;is&#160;the&#160;parent&#160;LDAP&#160;distinguished&#160;name  
#&#160;userAttrs&#160;is&#160;a&#160;string&#160;or&#160;list&#160;of&#160;strings&#160;of&#160;form&#160;"attr:&#160;value"  
#&#160;A&#160;trailing&#160;newline&#160;is&#160;added&#160;iff&#160;format==1  
#&#160;Note:&#160;unlike&#160;write,&#160;this&#160;does&#160;not&#160;write&#160;children&#160;as&#160;well `

 write_raw  (self, fd  =None  ) 
     ` #&#160;Write&#160;to&#160;a&#160;file&#160;without&#160;formatting. `

  
class  LinearDataNode  ( [ CdmsNode ](/cdms.cdmsNode.html) )

` `

` #&#160;Linear&#160;data&#160;element  
`

Methods defined here:  

 __getitem__  (self, index) 
     ` #&#160;Get&#160;an&#160;indexed&#160;value `

 __init__  (self, start, delta, length) 

 __len__  (self) 

 concatenate  (self, linearNode, allowgaps  =0  ) 
     ` #&#160;Concatenate&#160;linear&#160;arrays,&#160;preserving&#160;linearity   
#&#160;If&#160;allowgaps&#160;is&#160;set,&#160;don't&#160;require&#160;that&#160;the&#160;linear&#160;arrays&#160;be&#160;contiguous  
#&#160;Return&#160;a&#160;new&#160;linear&#160;node `

 equal  (self, axis) 
     ` #&#160;Equality&#160;of&#160;linear&#160;vectors `

 equalVector  (self, ar) 
     ` #&#160;Equality&#160;of&#160;linear&#160;vector&#160;and&#160;array `

 isClose  (self, axis, eps) 
     ` #&#160;Closeness&#160;of&#160;linear&#160;vectors `

 isCloseVector  (self, ar, eps) 
     ` #&#160;Closeness&#160;of&#160;linear&#160;vector&#160;and&#160;array `

 mapToExternal  (self) 
     ` #&#160;Map&#160;to&#160;external&#160;attributes `

 monotonicity  (self) 
     ` #&#160;Return&#160;monotonicity:&#160;CdNotMonotonic,&#160;CdIncreasing,&#160;CdDecreasing,&#160;or&#160;CdSingleton `

 toVector  (self, datatype) 
     ` #&#160;Return&#160;a&#160;vector&#160;representation,&#160;given&#160;a&#160;CDMS&#160;datatype `

* * *

Data and other attributes defined here:  

 validDeltaTypes  = [<type 'int'>, <type 'float'>, <type 'list'>] 

 validStartTypes  = [<type 'int'>, <type 'float'>, <type 'comptime'>, <type 'reltime'>] 

* * *

Methods inherited from [ CdmsNode ](/cdms.cdmsNode.html) :  

 add  (self, child) 
     ` #&#160;Add&#160;a&#160;child&#160;node `

 children  (self) 
     ` #&#160;Return&#160;a&#160;list&#160;of&#160;child&#160;nodes `

 getChildAt  (self, index) 
     ` #&#160;Get&#160;the&#160;child&#160;node&#160;at&#160;index&#160;k `

 getChildCount  (self) 
     ` #&#160;Get&#160;the&#160;number&#160;of&#160;children `

 getContent  (self) 
     ` #&#160;Get&#160;content `

 getExternalAttr  (self, name) 
     ` #&#160;Get&#160;an&#160;external&#160;attribute `

 getExternalAttrAsAttr  (self, name) 
     ` #&#160;Get&#160;an&#160;external&#160;attribute,&#160;as&#160;an&#160;Attr&#160;instance `

 getExternalDict  (self) 
     ` #&#160;Get&#160;a&#160;dictionary&#160;of&#160;external&#160;attributes,&#160;of&#160;form&#160;(value,datatype) `

 getIndex  (self, node) 
     ` #&#160;Get&#160;the&#160;index&#160;of&#160;a&#160;node `

 getParent  (self) 
     ` #&#160;Get&#160;the&#160;parent&#160;node `

 isLeaf  (self) 
     ` #&#160;True&#160;iff&#160;node&#160;is&#160;a&#160;leaf&#160;node `

 removeChildAt  (self, index) 
     ` #&#160;Remove&#160;and&#160;return&#160;the&#160;child&#160;at&#160;index&#160;k `

 setContentFromString  (self, content) 
     ` #&#160;Set&#160;content&#160;from&#160;a&#160;string.&#160;The&#160;interpretation   
#&#160;of&#160;content&#160;is&#160;class-dependent `

 setExternalAttr  (self, name, value, datatype  =None  ) 
     ` #&#160;Set&#160;an&#160;external&#160;attribute `

 setExternalAttrFromAttr  (self, attr) 
     ` #&#160;Set&#160;an&#160;external&#160;attribute   
#&#160;'attr'&#160;is&#160;an&#160;Attr&#160;object `

 setExternalDict  (self, dict) 
     ` #&#160;Set&#160;the&#160;external&#160;attribute&#160;dictionary.&#160;The&#160;input&#160;dictionary   
#&#160;is&#160;of&#160;the&#160;form&#160;{name:value,...}&#160;where&#160;value&#160;is&#160;a&#160;string. `

 validate  (self, idtable  =None  ) 
     ` #&#160;Validate&#160;attributes `

 write  (self, fd  =None  , tablevel  =0  , format  =1  ) 
     ` #&#160;Write&#160;to&#160;a&#160;file,&#160;with&#160;formatting.   
#&#160;tablevel&#160;is&#160;the&#160;start&#160;number&#160;of&#160;tabs `

 write_ldif  (self, parentdn, userAttrs  =[]  , fd  =None  , format  =1  ) 
     ` #&#160;Write&#160;an&#160;LDIF&#160;(LDAP&#160;interchange&#160;format)&#160;entry   
#&#160;parentdn&#160;is&#160;the&#160;parent&#160;LDAP&#160;distinguished&#160;name  
#&#160;userAttrs&#160;is&#160;a&#160;string&#160;or&#160;list&#160;of&#160;strings&#160;of&#160;form&#160;"attr:&#160;value"  
#&#160;A&#160;trailing&#160;newline&#160;is&#160;added&#160;iff&#160;format==1  
#&#160;Note:&#160;unlike&#160;write,&#160;this&#160;does&#160;not&#160;write&#160;children&#160;as&#160;well `

 write_raw  (self, fd  =None  ) 
     ` #&#160;Write&#160;to&#160;a&#160;file&#160;without&#160;formatting. `

  
class  NotMonotonicError  ( [ cdms.error.CDMSError ](/cdms.error.html) )

` `

Method resolution order:

     [ NotMonotonicError ](/cdms.cdmsNode.html)
     [ cdms.error.CDMSError ](/cdms.error.html)
     [ exceptions.Exception ](/exceptions.html)

* * *

Methods inherited from [ cdms.error.CDMSError ](/cdms.error.html) :  

 __init__  (self, args  ='Unspecified error from package cdms'  ) 

 __str__  (self) 

* * *

Methods inherited from [ exceptions.Exception ](/exceptions.html) :  

 __getitem__  (...) 

  
class  RectGridNode  ( [ CdmsNode ](/cdms.cdmsNode.html) )

` `

` #&#160;Rectilinear&#160;lat-lon&#160;grid  
`

Methods defined here:  

 __init__  (self, id, latitude, longitude, gridtype  ='unknown'  , order  ='yx'  , mask  =None  ) 
     ` #&#160;Create&#160;a&#160;grid   
#&#160;All&#160;arguments&#160;are&#160;strings `

 mapToExternal  (self) 
     ` #&#160;Map&#160;to&#160;external&#160;attributes `

* * *

Methods inherited from [ CdmsNode ](/cdms.cdmsNode.html) :  

 add  (self, child) 
     ` #&#160;Add&#160;a&#160;child&#160;node `

 children  (self) 
     ` #&#160;Return&#160;a&#160;list&#160;of&#160;child&#160;nodes `

 getChildAt  (self, index) 
     ` #&#160;Get&#160;the&#160;child&#160;node&#160;at&#160;index&#160;k `

 getChildCount  (self) 
     ` #&#160;Get&#160;the&#160;number&#160;of&#160;children `

 getContent  (self) 
     ` #&#160;Get&#160;content `

 getExternalAttr  (self, name) 
     ` #&#160;Get&#160;an&#160;external&#160;attribute `

 getExternalAttrAsAttr  (self, name) 
     ` #&#160;Get&#160;an&#160;external&#160;attribute,&#160;as&#160;an&#160;Attr&#160;instance `

 getExternalDict  (self) 
     ` #&#160;Get&#160;a&#160;dictionary&#160;of&#160;external&#160;attributes,&#160;of&#160;form&#160;(value,datatype) `

 getIndex  (self, node) 
     ` #&#160;Get&#160;the&#160;index&#160;of&#160;a&#160;node `

 getParent  (self) 
     ` #&#160;Get&#160;the&#160;parent&#160;node `

 isLeaf  (self) 
     ` #&#160;True&#160;iff&#160;node&#160;is&#160;a&#160;leaf&#160;node `

 removeChildAt  (self, index) 
     ` #&#160;Remove&#160;and&#160;return&#160;the&#160;child&#160;at&#160;index&#160;k `

 setContentFromString  (self, content) 
     ` #&#160;Set&#160;content&#160;from&#160;a&#160;string.&#160;The&#160;interpretation   
#&#160;of&#160;content&#160;is&#160;class-dependent `

 setExternalAttr  (self, name, value, datatype  =None  ) 
     ` #&#160;Set&#160;an&#160;external&#160;attribute `

 setExternalAttrFromAttr  (self, attr) 
     ` #&#160;Set&#160;an&#160;external&#160;attribute   
#&#160;'attr'&#160;is&#160;an&#160;Attr&#160;object `

 setExternalDict  (self, dict) 
     ` #&#160;Set&#160;the&#160;external&#160;attribute&#160;dictionary.&#160;The&#160;input&#160;dictionary   
#&#160;is&#160;of&#160;the&#160;form&#160;{name:value,...}&#160;where&#160;value&#160;is&#160;a&#160;string. `

 validate  (self, idtable  =None  ) 
     ` #&#160;Validate&#160;attributes `

 write  (self, fd  =None  , tablevel  =0  , format  =1  ) 
     ` #&#160;Write&#160;to&#160;a&#160;file,&#160;with&#160;formatting.   
#&#160;tablevel&#160;is&#160;the&#160;start&#160;number&#160;of&#160;tabs `

 write_ldif  (self, parentdn, userAttrs  =[]  , fd  =None  , format  =1  ) 
     ` #&#160;Write&#160;an&#160;LDIF&#160;(LDAP&#160;interchange&#160;format)&#160;entry   
#&#160;parentdn&#160;is&#160;the&#160;parent&#160;LDAP&#160;distinguished&#160;name  
#&#160;userAttrs&#160;is&#160;a&#160;string&#160;or&#160;list&#160;of&#160;strings&#160;of&#160;form&#160;"attr:&#160;value"  
#&#160;A&#160;trailing&#160;newline&#160;is&#160;added&#160;iff&#160;format==1  
#&#160;Note:&#160;unlike&#160;write,&#160;this&#160;does&#160;not&#160;write&#160;children&#160;as&#160;well `

 write_raw  (self, fd  =None  ) 
     ` #&#160;Write&#160;to&#160;a&#160;file&#160;without&#160;formatting. `

  
class  VariableNode  ( [ CdmsNode ](/cdms.cdmsNode.html) )

` `

` #&#160;Spatio-temporal&#160;variable  
#&#160;Two&#160;ways&#160;to&#160;create&#160;a&#160;variable:  
#&#160;(1)&#160;var&#160;= [ VariableNode ](/) (id,datatype,domain)  
#&#160;(2)&#160;var&#160;= [ VariableNode ](/) (id,datatype)  
#&#160;&#160;&#160;&#160;&#160;var. [ setDomain ](/) (domain)  
`

Methods defined here:  

 __init__  (self, id, datatype, domain) 
     ` #&#160;Create&#160;a&#160;variable.   
#&#160;If&#160;validate&#160;is&#160;true,&#160;validate&#160;immediately `

 getDomain  (self) 
     ` #&#160;Get&#160;the&#160;domain `

 mapToExternal  (self) 
     ` #&#160;Map&#160;to&#160;external&#160;attributes `

 setDomain  (self, domain) 
     ` #&#160;Set&#160;the&#160;domain `

* * *

Methods inherited from [ CdmsNode ](/cdms.cdmsNode.html) :  

 add  (self, child) 
     ` #&#160;Add&#160;a&#160;child&#160;node `

 children  (self) 
     ` #&#160;Return&#160;a&#160;list&#160;of&#160;child&#160;nodes `

 getChildAt  (self, index) 
     ` #&#160;Get&#160;the&#160;child&#160;node&#160;at&#160;index&#160;k `

 getChildCount  (self) 
     ` #&#160;Get&#160;the&#160;number&#160;of&#160;children `

 getContent  (self) 
     ` #&#160;Get&#160;content `

 getExternalAttr  (self, name) 
     ` #&#160;Get&#160;an&#160;external&#160;attribute `

 getExternalAttrAsAttr  (self, name) 
     ` #&#160;Get&#160;an&#160;external&#160;attribute,&#160;as&#160;an&#160;Attr&#160;instance `

 getExternalDict  (self) 
     ` #&#160;Get&#160;a&#160;dictionary&#160;of&#160;external&#160;attributes,&#160;of&#160;form&#160;(value,datatype) `

 getIndex  (self, node) 
     ` #&#160;Get&#160;the&#160;index&#160;of&#160;a&#160;node `

 getParent  (self) 
     ` #&#160;Get&#160;the&#160;parent&#160;node `

 isLeaf  (self) 
     ` #&#160;True&#160;iff&#160;node&#160;is&#160;a&#160;leaf&#160;node `

 removeChildAt  (self, index) 
     ` #&#160;Remove&#160;and&#160;return&#160;the&#160;child&#160;at&#160;index&#160;k `

 setContentFromString  (self, content) 
     ` #&#160;Set&#160;content&#160;from&#160;a&#160;string.&#160;The&#160;interpretation   
#&#160;of&#160;content&#160;is&#160;class-dependent `

 setExternalAttr  (self, name, value, datatype  =None  ) 
     ` #&#160;Set&#160;an&#160;external&#160;attribute `

 setExternalAttrFromAttr  (self, attr) 
     ` #&#160;Set&#160;an&#160;external&#160;attribute   
#&#160;'attr'&#160;is&#160;an&#160;Attr&#160;object `

 setExternalDict  (self, dict) 
     ` #&#160;Set&#160;the&#160;external&#160;attribute&#160;dictionary.&#160;The&#160;input&#160;dictionary   
#&#160;is&#160;of&#160;the&#160;form&#160;{name:value,...}&#160;where&#160;value&#160;is&#160;a&#160;string. `

 validate  (self, idtable  =None  ) 
     ` #&#160;Validate&#160;attributes `

 write  (self, fd  =None  , tablevel  =0  , format  =1  ) 
     ` #&#160;Write&#160;to&#160;a&#160;file,&#160;with&#160;formatting.   
#&#160;tablevel&#160;is&#160;the&#160;start&#160;number&#160;of&#160;tabs `

 write_ldif  (self, parentdn, userAttrs  =[]  , fd  =None  , format  =1  ) 
     ` #&#160;Write&#160;an&#160;LDIF&#160;(LDAP&#160;interchange&#160;format)&#160;entry   
#&#160;parentdn&#160;is&#160;the&#160;parent&#160;LDAP&#160;distinguished&#160;name  
#&#160;userAttrs&#160;is&#160;a&#160;string&#160;or&#160;list&#160;of&#160;strings&#160;of&#160;form&#160;"attr:&#160;value"  
#&#160;A&#160;trailing&#160;newline&#160;is&#160;added&#160;iff&#160;format==1  
#&#160;Note:&#160;unlike&#160;write,&#160;this&#160;does&#160;not&#160;write&#160;children&#160;as&#160;well `

 write_raw  (self, fd  =None  ) 
     ` #&#160;Write&#160;to&#160;a&#160;file&#160;without&#160;formatting. `

  
class  XLinkNode  ( [ CdmsNode ](/cdms.cdmsNode.html) )

` `

` #&#160;Link&#160;to&#160;an&#160;external&#160;element  
`

Methods defined here:  

 __init__  (self, id, uri, contentRole, content  =''  ) 

 mapToExternal  (self) 
     ` #&#160;Map&#160;to&#160;external&#160;attributes `

* * *

Methods inherited from [ CdmsNode ](/cdms.cdmsNode.html) :  

 add  (self, child) 
     ` #&#160;Add&#160;a&#160;child&#160;node `

 children  (self) 
     ` #&#160;Return&#160;a&#160;list&#160;of&#160;child&#160;nodes `

 getChildAt  (self, index) 
     ` #&#160;Get&#160;the&#160;child&#160;node&#160;at&#160;index&#160;k `

 getChildCount  (self) 
     ` #&#160;Get&#160;the&#160;number&#160;of&#160;children `

 getContent  (self) 
     ` #&#160;Get&#160;content `

 getExternalAttr  (self, name) 
     ` #&#160;Get&#160;an&#160;external&#160;attribute `

 getExternalAttrAsAttr  (self, name) 
     ` #&#160;Get&#160;an&#160;external&#160;attribute,&#160;as&#160;an&#160;Attr&#160;instance `

 getExternalDict  (self) 
     ` #&#160;Get&#160;a&#160;dictionary&#160;of&#160;external&#160;attributes,&#160;of&#160;form&#160;(value,datatype) `

 getIndex  (self, node) 
     ` #&#160;Get&#160;the&#160;index&#160;of&#160;a&#160;node `

 getParent  (self) 
     ` #&#160;Get&#160;the&#160;parent&#160;node `

 isLeaf  (self) 
     ` #&#160;True&#160;iff&#160;node&#160;is&#160;a&#160;leaf&#160;node `

 removeChildAt  (self, index) 
     ` #&#160;Remove&#160;and&#160;return&#160;the&#160;child&#160;at&#160;index&#160;k `

 setContentFromString  (self, content) 
     ` #&#160;Set&#160;content&#160;from&#160;a&#160;string.&#160;The&#160;interpretation   
#&#160;of&#160;content&#160;is&#160;class-dependent `

 setExternalAttr  (self, name, value, datatype  =None  ) 
     ` #&#160;Set&#160;an&#160;external&#160;attribute `

 setExternalAttrFromAttr  (self, attr) 
     ` #&#160;Set&#160;an&#160;external&#160;attribute   
#&#160;'attr'&#160;is&#160;an&#160;Attr&#160;object `

 setExternalDict  (self, dict) 
     ` #&#160;Set&#160;the&#160;external&#160;attribute&#160;dictionary.&#160;The&#160;input&#160;dictionary   
#&#160;is&#160;of&#160;the&#160;form&#160;{name:value,...}&#160;where&#160;value&#160;is&#160;a&#160;string. `

 validate  (self, idtable  =None  ) 
     ` #&#160;Validate&#160;attributes `

 write  (self, fd  =None  , tablevel  =0  , format  =1  ) 
     ` #&#160;Write&#160;to&#160;a&#160;file,&#160;with&#160;formatting.   
#&#160;tablevel&#160;is&#160;the&#160;start&#160;number&#160;of&#160;tabs `

 write_ldif  (self, parentdn, userAttrs  =[]  , fd  =None  , format  =1  ) 
     ` #&#160;Write&#160;an&#160;LDIF&#160;(LDAP&#160;interchange&#160;format)&#160;entry   
#&#160;parentdn&#160;is&#160;the&#160;parent&#160;LDAP&#160;distinguished&#160;name  
#&#160;userAttrs&#160;is&#160;a&#160;string&#160;or&#160;list&#160;of&#160;strings&#160;of&#160;form&#160;"attr:&#160;value"  
#&#160;A&#160;trailing&#160;newline&#160;is&#160;added&#160;iff&#160;format==1  
#&#160;Note:&#160;unlike&#160;write,&#160;this&#160;does&#160;not&#160;write&#160;children&#160;as&#160;well `

 write_raw  (self, fd  =None  ) 
     ` #&#160;Write&#160;to&#160;a&#160;file&#160;without&#160;formatting. `

  
 Functions 

` `

 mapIllegalToEntity  (matchobj) 
     ` #&#160;Map&#160;illegal&#160;XML&#160;characters&#160;to&#160;entity&#160;references:   
#&#160;'<'&#160;\-->&#160;&lt;  
#&#160;'>'&#160;\-->&#160;&gt;  
#&#160;'&'&#160;\-->&#160;&amp;  
#&#160;'"'&#160;\-->&#160;&quot;  
#&#160;"'"&#160;\-->&#160;&apos;  
#&#160;all&#160;other&#160;illegal&#160;characters&#160;are&#160;removed&#160;#" `

  
 Data 

` `

 CdAny  = 'Any'   
 CdArray  = 'Array'   
 CdByte  = 'Byte'   
 CdChar  = 'Char'   
 CdDatatypes  = ['Char', 'Byte', 'Short', 'Int', 'Long', 'Float', 'Double', 'String']   
 CdDecreasing  = 1   
 CdDouble  = 'Double'   
 CdFloat  = 'Float'   
 CdFromObject  = 'FromObject'   
 CdGridtypes  = ['unknown', 'gaussian', 'uniform']   
 CdIncreasing  = -1   
 CdInt  = 'Int'   
 CdLinear  = 2   
 CdLong  = 'Long'   
 CdNotMonotonic  = 0   
 CdScalar  = 'Scalar'   
 CdShort  = 'Short'   
 CdSingleton  = 2   
 CdString  = 'String'   
 CdToNumericType  = {'Byte': '1', 'Char': 'c', 'Double': 'd', 'Float': 'f', 'Int': 'i', 'Long': 'l', 'Short': 's'}   
 CdVector  = 1   
 DuplicateIdError  = 'Duplicate identifier: '   
 GaussianGridType  = 'gaussian'   
 InvalidArgumentError  = 'Invalid argument: '   
 InvalidDatatype  = 'Invalid datatype: '   
 InvalidGridtype  = 'Invalid grid type: '   
 InvalidIdError  = 'Invalid identifier: '   
 NotMonotonic  = 'Result array is not monotonic '   
 NumericToCdType  = {'1': 'Byte', 'c': 'Char', 'd': 'Double', 'f': 'Float', 'i': 'Int', 'l': 'Long', 's': 'Short'}   
 StringTypes  = (<type 'str'>, <type 'unicode'>)   
 UniformGridType  = 'uniform'   
 UnknownGridType  = 'unknown' 

* * *

UCRL-WEB-213937 | [ Privacy & Legal Notice ](/disclaimer.html)

[ webmaster@pcmdi.llnl.gov ](/webmaster@pcmdi.llnl.gov)

[ ![Powered by Plone](media/plone_powered.gif) ](/)

