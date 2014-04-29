---
layout: default
title:
---

 [ Skip to content. ](/cdat/source/api-reference/cdms.dataset.html) | [ Skip to
navigation ](/cdat/source/api-reference/cdms.dataset.html)

Search Site

[ Advanced Search&#8230; ](/search_form)

#  [ PCMDI Software Portal ](/)

#####  Sections

  * [ Home ](/)

#####  Personal tools

  * [ Log in ](/login_form)

You are here:  [ Home ](/) -> [ CDAT ](/cdat) -> [ Source Code ](/cdat/source)
-> [ API Reference ](/cdat/source/api-reference) -> Python: module
cdms.dataset

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

        * [ Python: module cdms.dataset ](/cdat/source/api-reference/cdms.dataset.html)

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

  * [ ![Send this page to somebody](media/mail_icon.gif) ](/cdat/source/api-reference/cdms.dataset.html/sendto_form)
  * [ ![Print this page](media/print_icon.gif) ](/this.print\(\))

#  Python: module cdms.dataset

  
  
 [ cdms  ](/cdms.html) .dataset 
[ index ](/)  

` CDMS&#160;dataset&#160;and&#160;file&#160;objects `

  
 Modules 

` `

[ cdms.Cdunif ](/cdms.Cdunif.html)  
[ MA ](/MA.html)  
[ Numeric ](/Numeric.html)  
[ cdms.cache ](/cdms.cache.html)  

[ cdms.cdmsNode ](/cdms.cdmsNode.html)  
[ cdms.cdmsURLopener ](/cdms.cdmsURLopener.html)  
[ cdms.cdmsobj ](/cdms.cdmsobj.html)  
[ cdms.convention ](/cdms.convention.html)  

[ cdms.internattr ](/cdms.internattr.html)  
[ os ](/os.html)  
[ re ](/re.html)  
[ string ](/string.html)  

[ sys ](/sys.html)  
[ urllib ](/urllib.html)  
[ urlparse ](/urlparse.html)  

  
 Classes 

` `

[ cdms.cdmsobj.CdmsObj ](/cdms.cdmsobj.html) ( [
cdms.internattr.InternalAttributesClass ](/cdms.internattr.html) )

    

[ CdmsFile ](/cdms.dataset.html) ( [ cdms.cdmsobj.CdmsObj
](/cdms.cdmsobj.html) , [ cdms.cudsinterface.cuDataset
](/cdms.cudsinterface.html) )

[ Dataset ](/cdms.dataset.html) ( [ cdms.cdmsobj.CdmsObj ](/cdms.cdmsobj.html)
, [ cdms.cudsinterface.cuDataset ](/cdms.cudsinterface.html) )

[ cdms.cudsinterface.cuDataset ](/cdms.cudsinterface.html)

    

[ CdmsFile ](/cdms.dataset.html) ( [ cdms.cdmsobj.CdmsObj
](/cdms.cdmsobj.html) , [ cdms.cudsinterface.cuDataset
](/cdms.cudsinterface.html) )

[ Dataset ](/cdms.dataset.html) ( [ cdms.cdmsobj.CdmsObj ](/cdms.cdmsobj.html)
, [ cdms.cudsinterface.cuDataset ](/cdms.cudsinterface.html) )

[ cdms.error.CDMSError ](/cdms.error.html) ( [ exceptions.Exception
](/exceptions.html) )

    

[ DuplicateAxisError ](/cdms.dataset.html)

  
class  CdmsFile  ( [ cdms.cdmsobj.CdmsObj ](/cdms.cdmsobj.html) , [
cdms.cudsinterface.cuDataset ](/cdms.cudsinterface.html) )

` `

Method resolution order:

     [ CdmsFile ](/cdms.dataset.html)
     [ cdms.cdmsobj.CdmsObj ](/cdms.cdmsobj.html)
     [ cdms.internattr.InternalAttributesClass ](/cdms.internattr.html)
     [ PropertiedClasses.Properties.PropertiedClass ](/PropertiedClasses.Properties.html)
     [ cdms.cudsinterface.cuDataset ](/cdms.cudsinterface.html)

* * *

Methods defined here:  

 __delattr__  (self, name) 
     ` #&#160;delattr&#160;deletes&#160;external&#160;global&#160;attributes&#160;in&#160;the&#160;file `

 __getattr__  (self, name) 
     ` #&#160;getattr&#160;reads&#160;external&#160;global&#160;attributes&#160;from&#160;the&#160;file `

 __init__  (self, path, mode) 

 __repr__  (self) 

 __setattr__  (self, name, value) 
     ` #&#160;setattr&#160;writes&#160;external&#160;global&#160;attributes&#160;to&#160;the&#160;file `

 close  (self) 

 copyAxis  (self, axis, newname  =None  , unlimited  =0  , index  =None  , extbounds  =None  ) 
     ` #&#160;Copy&#160;axis&#160;description&#160;and&#160;data&#160;from&#160;another&#160;axis `

 copyGrid  (self, grid, newname  =None  ) 
     ` #&#160;Copy&#160;grid `

 createAxis  (self, name, ar, unlimited  =0  ) 
     ` #&#160;Create&#160;an&#160;axis   
#&#160;'name'&#160;is&#160;the&#160;string&#160;name&#160;of&#160;the&#160;Axis  
#&#160;'ar'&#160;is&#160;the&#160;1-D&#160;data&#160;array,&#160;or&#160;None&#160;for&#160;an&#160;unlimited&#160;axis  
#&#160;Set&#160;unlimited&#160;to&#160;true&#160;to&#160;designate&#160;the&#160;axis&#160;as&#160;unlimited  
#&#160;Return&#160;an&#160;axis&#160;object. `

 createRectGrid  (self, id, lat, lon, order, type  ='generic'  , mask  =None  ) 
     ` #&#160;Create&#160;an&#160;implicit&#160;rectilinear&#160;grid.&#160;lat,&#160;lon,&#160;and&#160;mask&#160;are&#160;objects.   
#&#160;order&#160;and&#160;type&#160;are&#160;strings `

 createVariable  (self, name, datatype, axesOrGrids, fill_value  =None  ) 
     ` #&#160;Create&#160;a&#160;variable   
#&#160;'name'&#160;is&#160;the&#160;string&#160;name&#160;of&#160;the&#160;Variable  
#&#160;'datatype'&#160;is&#160;a&#160;CDMS&#160;datatype&#160;or&#160;Numeric&#160;typecode  
#&#160;'axesOrGrids'&#160;is&#160;a&#160;list&#160;of&#160;axes,&#160;grids.&#160;(Note:&#160;this&#160;should&#160;be  
#&#160;&#160;&#160;generalized&#160;to&#160;allow&#160;subintervals&#160;of&#160;axes&#160;and/or&#160;grids)  
#&#160;Return&#160;a&#160;variable&#160;object. `

 createVariableCopy  (self, var, id  =None  , attributes  =None  , axes  =None  , extbounds  =None  , extend  =0  , fill_value  =None  , index  =None  , newname  =None  , grid  =None  ) 
     ` Define&#160;a&#160;new&#160;variable,&#160;with&#160;the&#160;same&#160;axes&#160;and&#160;attributes&#160;as&#160;in&#160;<var>.   
This&#160;does&#160;not&#160;copy&#160;the&#160;data&#160;itself.  
Keywords:  
attributes:&#160;A&#160;dictionary&#160;of&#160;attributes.&#160;Default&#160;is&#160;var.attributes.  
axes:&#160;The&#160;list&#160;of&#160;axis&#160;objects.&#160;Default&#160;is&#160;var.getAxisList()  
extbounds:&#160;Bounds&#160;of&#160;the&#160;(portion&#160;of)&#160;the&#160;extended&#160;dimension&#160;being&#160;written.  
id&#160;or&#160;newname:&#160;String&#160;identifier&#160;of&#160;the&#160;new&#160;variable.  
extend:&#160;If&#160;1,&#160;define&#160;the&#160;first&#160;dimension&#160;as&#160;the&#160;unlimited&#160;dimension.&#160;If&#160;0,&#160;do
not&#160;define  
an&#160;unlimited&#160;dimension.&#160;The&#160;default&#160;is&#160;the&#160;define&#160;the&#160;first&#160;dimension&#160;as
unlimited  
only&#160;if&#160;it&#160;is&#160;a&#160;time&#160;dimension.  
-&#160;fill_value&#160;is&#160;the&#160;missing&#160;value&#160;flag.   
-&#160;index&#160;is&#160;the&#160;extended&#160;dimension&#160;index&#160;to&#160;write&#160;to.&#160;The&#160;default&#160;index&#160;is&#160;determined   
by&#160;lookup&#160;relative&#160;to&#160;the&#160;existing&#160;extended&#160;dimension.  
grid&#160;is&#160;the&#160;variable&#160;grid.&#160;If&#160;none,&#160;the&#160;value&#160;of&#160;var. [ getGrid ](/) ()&#160;is
used. `

 createVirtualAxis  (self, name, axislen) 
     ` Create&#160;an&#160;axis&#160;without&#160;any&#160;associated&#160;coordinate&#160;array.&#160;This   
axis&#160;is&#160;read-only.&#160;This&#160;is&#160;useful&#160;for&#160;the&#160;'bound'&#160;axis.  
<name>&#160;is&#160;the&#160;string&#160;name&#160;of&#160;the&#160;axis.  
<axislen>&#160;is&#160;the&#160;integer&#160;length&#160;of&#160;the&#160;axis.  
  
Note:&#160;for&#160;netCDF&#160;output,&#160;this&#160;just&#160;creates&#160;a&#160;dimension&#160;without  
the&#160;associated&#160;coordinate&#160;array.&#160;On&#160;reads&#160;the&#160;axis&#160;will&#160;look&#160;like  
an&#160;axis&#160;of&#160;type&#160;float&#160;with&#160;values&#160;[0.0,&#160;1.0,&#160;...,&#160;float(axislen-1)].  
On&#160;write&#160;attempts&#160;an&#160;exception&#160;is&#160;raised. `

 getAxis  (self, id) 
     ` Get&#160;the&#160;axis&#160;object&#160;with&#160;the&#160;given&#160;id.&#160;Returns&#160;None&#160;if&#160;not&#160;found. `

 getBoundsAxis  (self, n) 
     ` Get&#160;a&#160;bounds&#160;axis&#160;of&#160;length&#160;n.&#160;Create&#160;the&#160;bounds&#160;axis&#160;if&#160;necessary. `

 getGrid  (self, id) 
     ` Get&#160;the&#160;grid&#160;object&#160;with&#160;the&#160;given&#160;id.&#160;Returns&#160;None&#160;if&#160;not&#160;found. `

 getVariable  (self, id) 
     ` Get&#160;the&#160;variable&#160;object&#160;with&#160;the&#160;given&#160;id.&#160;Returns&#160;None&#160;if&#160;not&#160;found. `

 getVariables  (self, spatial  =0  ) 
     ` Get&#160;a&#160;list&#160;of&#160;variable&#160;objects.&#160;If&#160;spatial=1,&#160;only&#160;return&#160;those   
axes&#160;defined&#160;on&#160;latitude&#160;or&#160;longitude,&#160;excluding&#160;weights&#160;and&#160;bounds. `

 matchPattern  (self, pattern, attribute, tag) 
     ` #&#160;Match&#160;a&#160;pattern&#160;in&#160;a&#160;string-valued&#160;attribute.&#160;If&#160;attribute&#160;is&#160;None,   
#&#160;search&#160;all&#160;string&#160;attributes.&#160;If&#160;tag&#160;is&#160;'cdmsFile',&#160;just&#160;check&#160;the&#160;dataset,  
#&#160;else&#160;check&#160;all&#160;nodes&#160;in&#160;the&#160;dataset&#160;of&#160;class&#160;type&#160;matching&#160;the&#160;tag.&#160;If&#160;tag  
#&#160;is&#160;None,&#160;search&#160;the&#160;dataset&#160;and&#160;all&#160;objects&#160;contained&#160;in&#160;it. `

 searchPattern  (self, pattern, attribute, tag) 
     ` #&#160;Search&#160;for&#160;a&#160;pattern&#160;in&#160;a&#160;string-valued&#160;attribute.&#160;If&#160;attribute&#160;is&#160;None,   
#&#160;search&#160;all&#160;string&#160;attributes.&#160;If&#160;tag&#160;is&#160;'cdmsFile',&#160;just&#160;check&#160;the&#160;dataset,  
#&#160;else&#160;check&#160;all&#160;nodes&#160;in&#160;the&#160;dataset&#160;of&#160;class&#160;type&#160;matching&#160;the&#160;tag.&#160;If&#160;tag  
#&#160;is&#160;None,&#160;search&#160;the&#160;dataset&#160;and&#160;all&#160;objects&#160;contained&#160;in&#160;it. `

 searchPredicate  (self, predicate, tag) 
     ` #&#160;Apply&#160;a&#160;predicate,&#160;returning&#160;a&#160;list&#160;of&#160;all&#160;objects&#160;in&#160;the&#160;dataset   
#&#160;for&#160;which&#160;the&#160;predicate&#160;is&#160;true.&#160;The&#160;predicate&#160;is&#160;a&#160;function&#160;which  
#&#160;takes&#160;a&#160;dataset&#160;as&#160;an&#160;argument,&#160;and&#160;returns&#160;true&#160;or&#160;false.&#160;If&#160;the  
#&#160;tag&#160;is&#160;'cdmsFile',&#160;the&#160;predicate&#160;is&#160;applied&#160;to&#160;the&#160;dataset&#160;only.  
#&#160;If&#160;'variable',&#160;'axis',&#160;etc.,&#160;it&#160;is&#160;applied&#160;only&#160;to&#160;that&#160;type&#160;of&#160;object  
#&#160;in&#160;the&#160;dataset.&#160;If&#160;None,&#160;it&#160;is&#160;applied&#160;to&#160;all&#160;objects,&#160;including  
#&#160;the&#160;dataset&#160;itself. `

 sync  (self) 

 write  (self, var, attributes  =None  , axes  =None  , extbounds  =None  , id  =None  , extend  =None  , fill_value  =None  , index  =None  , typecode  =None  ) 
     ` Write&#160;var&#160;to&#160;the&#160;file.&#160;If&#160;the&#160;variable&#160;is&#160;not&#160;yet&#160;defined&#160;in&#160;the&#160;file,   
a&#160;definition&#160;is&#160;created.&#160;By&#160;default,&#160;the&#160;time&#160;dimension&#160;of&#160;the&#160;variable&#160;is
defined&#160;as&#160;the  
'extended&#160;dimension'&#160;of&#160;the&#160;file.&#160;The&#160;function&#160;returns&#160;the&#160;corresponding&#160;file
variable.  
  
Keywords:  
-&#160;attributes&#160;is&#160;the&#160;attribute&#160;dictionary&#160;for&#160;the&#160;variable.&#160;The&#160;default&#160;is&#160;var.attributes.   
-&#160;axes&#160;is&#160;the&#160;list&#160;of&#160;file&#160;axes&#160;comprising&#160;the&#160;domain&#160;of&#160;the&#160;variable.&#160;The&#160;default&#160;is&#160;to   
copy&#160;var.getAxisList().  
-&#160;extbounds&#160;is&#160;the&#160;extended&#160;dimension&#160;bounds.&#160;Defaults&#160;to&#160;var. [ getAxis ](/) (0).getBounds()   
-&#160;id&#160;is&#160;the&#160;variable&#160;name&#160;in&#160;the&#160;file.&#160;Default&#160;is&#160;var.id.   
-&#160;extend=1&#160;causes&#160;the&#160;first&#160;dimension&#160;to&#160;be&#160;'extensible':&#160;iteratively&#160;writeable.   
The&#160;default&#160;is&#160;None,&#160;in&#160;which&#160;case&#160;the&#160;first&#160;dimension&#160;is&#160;extensible&#160;if&#160;it&#160;is
time.  
Set&#160;to&#160;0&#160;to&#160;turn&#160;off&#160;this&#160;behaviour.  
-&#160;fill_value&#160;is&#160;the&#160;missing&#160;value&#160;flag.   
-&#160;index&#160;is&#160;the&#160;extended&#160;dimension&#160;index&#160;to&#160;write&#160;to.&#160;The&#160;default&#160;index&#160;is&#160;determined   
by&#160;lookup&#160;relative&#160;to&#160;the&#160;existing&#160;extended&#160;dimension. `

* * *

Methods inherited from [ cdms.cdmsobj.CdmsObj ](/cdms.cdmsobj.html) :  

 dump  (self, path  =None  , format  =1  ) 
     ` [ dump ](/) (self,path=None,format=1)   
Dump&#160;an&#160;XML&#160;representation&#160;of&#160;this&#160;object&#160;to&#160;a&#160;file.  
'path'&#160;is&#160;the&#160;result&#160;file&#160;name,&#160;None&#160;for&#160;standard&#160;output.  
'format'==1&#160;iff&#160;the&#160;file&#160;is&#160;formatted&#160;with&#160;newlines&#160;for&#160;readability `

 matchone  (self, pattern, attname) 
     ` #&#160;Return&#160;true&#160;iff&#160;the&#160;attribute&#160;with&#160;name&#160;attname&#160;is&#160;a&#160;string   
#&#160;attribute&#160;which&#160;matches&#160;the&#160;compiled&#160;regular&#160;expression&#160;pattern,&#160;or  
#&#160;if&#160;attname&#160;is&#160;None&#160;and&#160;pattern&#160;matches&#160;at&#160;least&#160;one&#160;string  
#&#160;attribute.&#160;Return&#160;false&#160;if&#160;the&#160;attribute&#160;is&#160;not&#160;found&#160;or&#160;is&#160;not&#160;a&#160;string `

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

Methods inherited from [ cdms.cudsinterface.cuDataset
](/cdms.cudsinterface.html) :  

 __call__  (self, id, *args, kwargs) 
     ` Call&#160;a&#160;variable&#160;object&#160;with&#160;the&#160;given&#160;id.&#160;Exception&#160;if&#160;not&#160;found.   
Call&#160;the&#160;variable&#160;with&#160;the&#160;other&#160;arguments. `

 __getitem__  (self, key) 
     ` Implement&#160;f['varname']&#160;for&#160;file/dataset&#160;f. `

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

 listvariables  = listvariable(self) 
     ` Return&#160;a&#160;list&#160;of&#160;the&#160;variables&#160;in&#160;the&#160;file. `

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

  
class  Dataset  ( [ cdms.cdmsobj.CdmsObj ](/cdms.cdmsobj.html) , [
cdms.cudsinterface.cuDataset ](/cdms.cudsinterface.html) )

` `

Method resolution order:

     [ Dataset ](/cdms.dataset.html)
     [ cdms.cdmsobj.CdmsObj ](/cdms.cdmsobj.html)
     [ cdms.internattr.InternalAttributesClass ](/cdms.internattr.html)
     [ PropertiedClasses.Properties.PropertiedClass ](/PropertiedClasses.Properties.html)
     [ cdms.cudsinterface.cuDataset ](/cdms.cudsinterface.html)

* * *

Methods defined here:  

 __init__  (self, uri, mode, datasetNode  =None  , parent  =None  , datapath  =None  ) 

 __repr__  (self) 

 close  (self) 
     ` #&#160;Close&#160;all&#160;files `

 createAxis  (self, name, ar) 
     ` #&#160;Create&#160;an&#160;axis   
#&#160;'name'&#160;is&#160;the&#160;string&#160;name&#160;of&#160;the&#160;Axis  
#&#160;'ar'&#160;is&#160;the&#160;1-D&#160;data&#160;array,&#160;or&#160;None&#160;for&#160;an&#160;unlimited&#160;axis  
#&#160;Return&#160;an&#160;axis&#160;object. `

 createRectGrid  (id, lat, lon, order, type  ='generic'  , mask  =None  ) 
     ` #&#160;Create&#160;an&#160;implicit&#160;rectilinear&#160;grid.&#160;lat,&#160;lon,&#160;and&#160;mask&#160;are&#160;objects.   
#&#160;order&#160;and&#160;type&#160;are&#160;strings `

 createVariable  (self, name, datatype, axisnames) 
     ` #&#160;Create&#160;a&#160;variable   
#&#160;'name'&#160;is&#160;the&#160;string&#160;name&#160;of&#160;the&#160;Variable  
#&#160;'datatype'&#160;is&#160;a&#160;CDMS&#160;datatype  
#&#160;'axisnames'&#160;is&#160;a&#160;list&#160;of&#160;axes&#160;or&#160;grids  
#&#160;Return&#160;a&#160;variable&#160;object. `

 getAxis  (self, id) 
     ` Get&#160;the&#160;axis&#160;object&#160;with&#160;the&#160;given&#160;id.&#160;Returns&#160;None&#160;if&#160;not&#160;found. `

 getConvention  (self) 
     ` Get&#160;the&#160;metadata&#160;convention&#160;associated&#160;with&#160;this&#160;dataset&#160;or&#160;file. `

 getDictionary  (self, tag) 
     ` #&#160;Get&#160;a&#160;dictionary&#160;of&#160;objects&#160;with&#160;the&#160;given&#160;tag `

 getGrid  (self, id) 
     ` Get&#160;the&#160;grid&#160;object&#160;with&#160;the&#160;given&#160;id.&#160;Returns&#160;None&#160;if&#160;not&#160;found. `

 getLogicalCollectionDN  (self, base  =None  ) 
     ` Return&#160;the&#160;logical&#160;collection&#160;distinguished&#160;name&#160;of&#160;this&#160;dataset.   
If&#160;<base>&#160;is&#160;defined,&#160;append&#160;it&#160;to&#160;the&#160;lc&#160;name. `

 getPaths  (self) 
     ` #&#160;Return&#160;a&#160;sorted&#160;list&#160;of&#160;all&#160;data&#160;files&#160;associated&#160;with&#160;the&#160;dataset `

 getVariable  (self, id) 
     ` Get&#160;the&#160;variable&#160;object&#160;with&#160;the&#160;given&#160;id.&#160;Returns&#160;None&#160;if&#160;not&#160;found. `

 getVariables  (self, spatial  =0  ) 
     ` Get&#160;a&#160;list&#160;of&#160;variable&#160;objects.&#160;If&#160;spatial=1,&#160;only&#160;return&#160;those   
axes&#160;defined&#160;on&#160;latitude&#160;or&#160;longitude,&#160;excluding&#160;weights&#160;and&#160;bounds. `

 matchPattern  (self, pattern, attribute, tag) 
     ` #&#160;Match&#160;a&#160;pattern&#160;in&#160;a&#160;string-valued&#160;attribute.&#160;If&#160;attribute&#160;is&#160;None,   
#&#160;search&#160;all&#160;string&#160;attributes.&#160;If&#160;tag&#160;is&#160;'dataset',&#160;just&#160;check&#160;the&#160;dataset,  
#&#160;else&#160;check&#160;all&#160;nodes&#160;in&#160;the&#160;dataset&#160;of&#160;class&#160;type&#160;matching&#160;the&#160;tag.&#160;If&#160;tag  
#&#160;is&#160;None,&#160;search&#160;the&#160;dataset&#160;and&#160;all&#160;objects&#160;contained&#160;in&#160;it. `

 openFile  (self, filename, mode) 
     ` #&#160;Open&#160;a&#160;data&#160;file&#160;associated&#160;with&#160;this&#160;dataset.   
#&#160;<filename>&#160;is&#160;relative&#160;to&#160;the&#160;self.  datapath   
#&#160;<mode>&#160;is&#160;the&#160;open&#160;mode. `

 searchPattern  (self, pattern, attribute, tag) 
     ` #&#160;Search&#160;for&#160;a&#160;pattern&#160;in&#160;a&#160;string-valued&#160;attribute.&#160;If&#160;attribute&#160;is&#160;None,   
#&#160;search&#160;all&#160;string&#160;attributes.&#160;If&#160;tag&#160;is&#160;'dataset',&#160;just&#160;check&#160;the&#160;dataset,  
#&#160;else&#160;check&#160;all&#160;nodes&#160;in&#160;the&#160;dataset&#160;of&#160;class&#160;type&#160;matching&#160;the&#160;tag.&#160;If&#160;tag  
#&#160;is&#160;None,&#160;search&#160;the&#160;dataset&#160;and&#160;all&#160;objects&#160;contained&#160;in&#160;it. `

 searchPredicate  (self, predicate, tag) 
     ` #&#160;Apply&#160;a&#160;predicate,&#160;returning&#160;a&#160;list&#160;of&#160;all&#160;objects&#160;in&#160;the&#160;dataset   
#&#160;for&#160;which&#160;the&#160;predicate&#160;is&#160;true.&#160;The&#160;predicate&#160;is&#160;a&#160;function&#160;which  
#&#160;takes&#160;a&#160;dataset&#160;as&#160;an&#160;argument,&#160;and&#160;returns&#160;true&#160;or&#160;false.&#160;If&#160;the  
#&#160;tag&#160;is&#160;'dataset',&#160;the&#160;predicate&#160;is&#160;applied&#160;to&#160;the&#160;dataset&#160;only.  
#&#160;If&#160;'variable',&#160;'axis',&#160;etc.,&#160;it&#160;is&#160;applied&#160;only&#160;to&#160;that&#160;type&#160;of&#160;object  
#&#160;in&#160;the&#160;dataset.&#160;If&#160;None,&#160;it&#160;is&#160;applied&#160;to&#160;all&#160;objects,&#160;including  
#&#160;the&#160;dataset&#160;itself. `

 sync  (self) 
     ` #&#160;Synchronize&#160;writes&#160;with&#160;data/metadata&#160;files `

* * *

Methods inherited from [ cdms.cdmsobj.CdmsObj ](/cdms.cdmsobj.html) :  

 dump  (self, path  =None  , format  =1  ) 
     ` [ dump ](/) (self,path=None,format=1)   
Dump&#160;an&#160;XML&#160;representation&#160;of&#160;this&#160;object&#160;to&#160;a&#160;file.  
'path'&#160;is&#160;the&#160;result&#160;file&#160;name,&#160;None&#160;for&#160;standard&#160;output.  
'format'==1&#160;iff&#160;the&#160;file&#160;is&#160;formatted&#160;with&#160;newlines&#160;for&#160;readability `

 matchone  (self, pattern, attname) 
     ` #&#160;Return&#160;true&#160;iff&#160;the&#160;attribute&#160;with&#160;name&#160;attname&#160;is&#160;a&#160;string   
#&#160;attribute&#160;which&#160;matches&#160;the&#160;compiled&#160;regular&#160;expression&#160;pattern,&#160;or  
#&#160;if&#160;attname&#160;is&#160;None&#160;and&#160;pattern&#160;matches&#160;at&#160;least&#160;one&#160;string  
#&#160;attribute.&#160;Return&#160;false&#160;if&#160;the&#160;attribute&#160;is&#160;not&#160;found&#160;or&#160;is&#160;not&#160;a&#160;string `

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

Methods inherited from [ cdms.cudsinterface.cuDataset
](/cdms.cudsinterface.html) :  

 __call__  (self, id, *args, kwargs) 
     ` Call&#160;a&#160;variable&#160;object&#160;with&#160;the&#160;given&#160;id.&#160;Exception&#160;if&#160;not&#160;found.   
Call&#160;the&#160;variable&#160;with&#160;the&#160;other&#160;arguments. `

 __getitem__  (self, key) 
     ` Implement&#160;f['varname']&#160;for&#160;file/dataset&#160;f. `

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

 listvariables  = listvariable(self) 
     ` Return&#160;a&#160;list&#160;of&#160;the&#160;variables&#160;in&#160;the&#160;file. `

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

  
class  DuplicateAxisError  ( [ cdms.error.CDMSError ](/cdms.error.html) )

` `

Method resolution order:

     [ DuplicateAxisError ](/cdms.dataset.html)
     [ cdms.error.CDMSError ](/cdms.error.html)
     [ exceptions.Exception ](/exceptions.html)

* * *

Methods inherited from [ cdms.error.CDMSError ](/cdms.error.html) :  

 __init__  (self, args  ='Unspecified error from package cdms'  ) 

 __str__  (self) 

* * *

Methods inherited from [ exceptions.Exception ](/exceptions.html) :  

 __getitem__  (...) 

  
 Functions 

` `

 createDataset  (path, template  =None  ) 
     ` #&#160;Create&#160;a&#160;dataset   
#&#160;'path'&#160;is&#160;the&#160;XML&#160;file&#160;name,&#160;or&#160;netCDF&#160;filename&#160;for&#160;simple&#160;file&#160;create  
#&#160;'template'&#160;is&#160;a&#160;string&#160;template&#160;for&#160;the&#160;datafile(s),&#160;for&#160;dataset&#160;creation `

 load  (path) 
     ` #&#160;Create&#160;a&#160;tree&#160;from&#160;a&#160;file&#160;path.   
#&#160;Returns&#160;the&#160;parse&#160;tree&#160;root&#160;node. `

 loadURI  (uri) 
     ` #&#160;Create&#160;a&#160;tree&#160;from&#160;a&#160;URI   
#&#160;URI&#160;is&#160;of&#160;the&#160;form&#160;scheme://netloc/path;parameters?query#fragment  
#&#160;where&#160;fragment&#160;may&#160;be&#160;an&#160;XPointer.  
#&#160;Returns&#160;the&#160;parse&#160;tree&#160;root&#160;node. `

 openDataset  (uri, mode  ='r'  , template  =None  , dods  =1  ) 
     ` #&#160;Open&#160;an&#160;existing&#160;dataset   
#&#160;'uri'&#160;is&#160;a&#160;Uniform&#160;Resource&#160;Identifier,&#160;referring&#160;to&#160;a&#160;cdunif&#160;file,&#160;XML
file,  
#&#160;&#160;&#160;or&#160;LDAP&#160;URL&#160;of&#160;a&#160;catalog&#160;dataset&#160;entry.  
#&#160;'mode'&#160;is&#160;'r',&#160;'r+',&#160;'a',&#160;or&#160;'w' `

 parseFileMap  (text) 
     ` Parse&#160;a&#160;CDMS&#160;filemap.&#160;having&#160;the&#160;form:   
filemap&#160;:==&#160;[&#160;varmap,&#160;varmap,&#160;...]  
varmap&#160;:==&#160;[&#160;namelist,&#160;slicelist&#160;]  
namelist&#160;:==&#160;[name,&#160;name,&#160;...]  
slicelist&#160;:==&#160;[indexlist,&#160;indexlist,&#160;,,,]  
indexlist&#160;:==&#160;[i,j,k,l,path] `

 parseIndexList  (text) 
     ` Parse&#160;a&#160;string&#160;of&#160;the&#160;form&#160;[i,j,k,l,path]&#160;where   
i,j,k,l&#160;are&#160;indices&#160;or&#160;'-',&#160;and&#160;path&#160;is&#160;a&#160;filename.  
Coerce&#160;the&#160;indices&#160;to&#160;integers,&#160;return&#160;(result,&#160;nconsumed). `

 parseName  (text) 

 parseVarMap  (text) 
     ` Parse&#160;a&#160;string&#160;of&#160;the&#160;form&#160;[&#160;namelist,&#160;slicelist&#160;] `

 parselist  (text, f) 
     ` Parse&#160;a&#160;string&#160;of&#160;the&#160;form&#160;[A,&#160;A,&#160;...].   
f&#160;is&#160;a&#160;function&#160;which&#160;parses&#160;A&#160;and&#160;returns&#160;(A,&#160;nconsumed) `

  
 Data 

` `

 CdDatatypes  = ['Char', 'Byte', 'Short', 'Int', 'Long', 'Float', 'Double', 'String']   
 DuplicateAxis  = 'Axis already defined: '   
 DuplicateGrid  = 'Grid already defined: '   
 DuplicateVariable  = 'Variable already defined: '   
 FileNotFound  = 'File not found: '   
 FileWasClosed  = 'File was closed: '   
 InvalidDomain  = 'Domain elements must be axes or grids'   
 ModeNotSupported  = 'Mode not supported: '   
 SchemeNotSupported  = 'Scheme not supported: ' 

* * *

UCRL-WEB-213937 | [ Privacy & Legal Notice ](/disclaimer.html)

[ webmaster@pcmdi.llnl.gov ](/webmaster@pcmdi.llnl.gov)

[ ![Powered by Plone](media/plone_powered.gif) ](/)

