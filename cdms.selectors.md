---
layout: default
title:
---

 [ Skip to content. ](/cdat/source/api-reference/cdms.selectors.html) | [ Skip
to navigation ](/cdat/source/api-reference/cdms.selectors.html)

Search Site

[ Advanced Search&#8230; ](/search_form)

#  [ PCMDI Software Portal ](/)

#####  Sections

  * [ Home ](/)

#####  Personal tools

  * [ Log in ](/login_form)

You are here:  [ Home ](/) -> [ CDAT ](/cdat) -> [ Source Code ](/cdat/source)
-> [ API Reference ](/cdat/source/api-reference) -> Python: module
cdms.selectors

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

        * [ Python: module cdms.selectors ](/cdat/source/api-reference/cdms.selectors.html)

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

  * [ ![Send this page to somebody](media/mail_icon.gif) ](/cdat/source/api-reference/cdms.selectors.html/sendto_form)
  * [ ![Print this page](media/print_icon.gif) ](/this.print\(\))

#  Python: module cdms.selectors

  
  
 [ cdms  ](/cdms.html) .selectors 
[ index ](/)  

` Classes&#160;to&#160;support&#160;easy&#160;selection&#160;of&#160;climate&#160;data `

  
 Modules 

` `

[ MA ](/MA.html)  

[ cdtime ](/cdtime.html)  

[ string ](/string.html)  

[ types ](/types.html)  

  
 Classes 

` `

[ cdms.error.CDMSError ](/cdms.error.html) ( [ exceptions.Exception
](/exceptions.html) )

    

[ SelectorError ](/cdms.selectors.html)

[ Selector ](/cdms.selectors.html)

[ SelectorComponent ](/cdms.selectors.html)

    

[ axisComponent ](/cdms.selectors.html)

    

[ coordinateComponent ](/cdms.selectors.html)

[ indexComponent ](/cdms.selectors.html)

[ indexedComponent ](/cdms.selectors.html)

[ positionalComponent ](/cdms.selectors.html)

[ requiredComponent ](/cdms.selectors.html)

  
class  Selector 

` `

` [ Selector ](/) class  
`

Methods defined here:  

 __and__  (self, other) 
     ` Implements&#160;the&#160;&&#160;operator,&#160;which&#160;returns   
[ clone ](/) ()&#160;refined&#160;by&#160;other `

 __call__  (self, *args, kwargs) 
     ` Return&#160;a&#160;new&#160;selector&#160;consisting&#160;of&#160;this&#160;one&#160;refined&#160;by&#160;the&#160;given&#160;arguments.   
Arguments&#160;are&#160;as&#160;per&#160;the&#160;constructor&#160;or&#160;method&#160;refine. `

 __init__  (self, *args, kwargs) 
     ` Positional&#160;args&#160;are&#160;SelectorComponents&#160;or&#160;Selectors   
Keyword&#160;args&#160;and&#160;their&#160;value&#160;are&#160;passed&#160;to&#160;kwselect&#160;to&#160;create  
selectors.&#160;All&#160;the&#160;selector&#160;components&#160;are&#160;put&#160;into&#160;the  
components&#160;list&#160;of&#160;this [ Selector ](/) ,&#160;along&#160;with&#160;all&#160;the&#160;components  
of&#160;any [ Selector ](/) arguments. `

 __repr__  (self) 

 clone  (self) 
     ` Makes&#160;a&#160;copy&#160;of&#160;this [ Selector ](/) . `

 components  (self) 
     ` List&#160;of&#160;selector&#160;components,&#160;each&#160;an&#160;instance&#160;of [ SelectorComponent ](/) . `

 refine  (self, *args, kwargs) 
     ` Add&#160;components&#160;to&#160;this&#160;selector&#160;using&#160;the&#160;same&#160;syntax&#160;as&#160;the   
constructor.&#160;Ignores&#160;non-keyword&#160;arguments&#160;that&#160;are&#160;not  
SelectorComponents&#160;or&#160;Selectors. `

 select  (self, variable, *args, kwargs) 
     ` Extract&#160;the&#160;selection&#160;from&#160;a&#160;variable.   
  
May&#160;specify&#160;additional&#160;refinement&#160;via&#160;extra&#160;arguments&#160;and  
keyword&#160;specifiers&#160;as&#160;in&#160;the&#160;constructor&#160;or&#160;method&#160;'refine'.  
  
Options&#160;modify&#160;the&#160;result&#160;of&#160;the&#160;selection.&#160;The&#160;options&#160;and  
their&#160;default&#160;values&#160;are:  
\--&#160;raw&#160;=&#160;0:&#160;if&#160;1,&#160;return&#160;an&#160;MA&#160;only  
\--&#160;squeeze&#160;=&#160;0:&#160;&#160;If&#160;1,&#160;eliminate&#160;any&#160;dimensions&#160;of&#160;length&#160;1  
from&#160;the&#160;result.  
\--&#160;order&#160;=&#160;None:&#160;If&#160;given,&#160;is&#160;a&#160;string&#160;such&#160;as  
variable.getOrder()  
returns.&#160;Result&#160;is&#160;permuted&#160;into&#160;this&#160;order.  
\--&#160;grid&#160;=&#160;None:&#160;&#160;If&#160;given,&#160;is&#160;a&#160;grid&#160;object;&#160;result&#160;is  
regridded&#160;onto&#160;this&#160;grid.  
Each&#160;of&#160;the&#160;components&#160;contributes&#160;arguments&#160;suitable&#160;for&#160;the  
subRegion&#160;call&#160;in&#160;class&#160;cdms.AbstractVariable.&#160;If&#160;a&#160;component  
is&#160;to&#160;modify&#160;the&#160;same&#160;axis&#160;as&#160;a&#160;previous&#160;component,&#160;its&#160;application  
is&#160;postponed.&#160;subRegion&#160;is&#160;called&#160;and&#160;the&#160;result&#160;is&#160;then&#160;fed  
to&#160;each&#160;of&#160;the&#160;components'&#160;"post"&#160;method.&#160;This&#160;returns&#160;a  
possibly&#160;modified&#160;result,&#160;which&#160;becomes&#160;the&#160;input&#160;to&#160;the&#160;next  
component's&#160;post&#160;method.  
  
This&#160;procedure&#160;is&#160;repeated&#160;until&#160;no&#160;more&#160;components&#160;are&#160;postponed.  
Then&#160;the&#160;options&#160;are&#160;applied&#160;to&#160;the&#160;result&#160;in&#160;the&#160;order  
listed&#160;above,&#160;and&#160;the&#160;result&#160;is&#160;returned.  
  
Execption [ SelectorError ](/) is&#160;thrown&#160;if&#160;the&#160;selection&#160;is  
impossible.  
  
The&#160;result&#160;is&#160;a&#160;TransientVariable&#160;and&#160;id(variable)&#160;<>&#160;id(result)  
even&#160;if&#160;there&#160;are&#160;no&#160;components. `

 unmodified_select  (self, variable, raw  =0  , squeeze  =0  , order  =None  , grid  =None  ) 
     ` Select&#160;using&#160;this&#160;selector&#160;without&#160;further&#160;modification `

  
class  SelectorComponent 

` `

` Base&#160;class&#160;representing&#160;selection&#160;for&#160;a&#160;given&#160;set&#160;of&#160;axes.  
`

Methods defined here:  

 post  (self, fetched, slab, axes, specifications, confined_by, aux, axismap) 
     ` Post-process&#160;fetched&#160;if&#160;desired,&#160;return&#160;new&#160;value.   
Arguments&#160;slab,&#160;axes,&#160;specifications,&#160;confined_by,&#160;and&#160;aux&#160;are  
pre-subRegion&#160;call.  
  
axismap&#160;gives&#160;the&#160;indices&#160;of&#160;fetched's&#160;axes&#160;in&#160;axes&#160;and&#160;should  
be&#160;modified&#160;as&#160;required&#160;by&#160;this&#160;method.&#160;&#160;Set&#160;axismap[i]&#160;to&#160;None&#160;to  
indicate&#160;that&#160;you&#160;have&#160;eliminated&#160;an&#160;axis. `

 specify  (self, slab, axes, specifications, confined_by, aux) 
     ` Refine&#160;the&#160;specification&#160;suitable&#160;for&#160;slab.subRegion   
Set&#160;confined_by&#160;to&#160;yourself&#160;for&#160;each&#160;axis&#160;you&#160;confine.  
If&#160;you&#160;would&#160;normally&#160;confine&#160;an&#160;axis&#160;to&#160;':',&#160;don't,  
unless&#160;you&#160;*require*&#160;that&#160;axis&#160;not&#160;be&#160;confined&#160;by&#160;other  
components.  
  
Returning:  
Return&#160;1&#160;if&#160;you&#160;wish&#160;to&#160;skip&#160;your&#160;turn.&#160;You'll&#160;be&#160;called  
later&#160;with&#160;the&#160;results&#160;of&#160;the&#160;other&#160;selectors.  
  
Raise&#160;a [ SelectorError ](/) exception&#160;if&#160;you&#160;can't&#160;do&#160;your&#160;job.  
  
Otherwise,&#160;return&#160;0,&#160;even&#160;if&#160;slab&#160;had&#160;no&#160;axes&#160;you&#160;wish  
to&#160;confine.  
  
Store&#160;any&#160;info&#160;you&#160;want&#160;in&#160;dictionary&#160;aux[id(self)] `

 specifyGrid  (self, var, grid, specs) 
     ` Refine&#160;the&#160;specification&#160;suitable&#160;for&#160;grid.intersect().   
  
'var'&#160;is&#160;a&#160;variable.  
'grid'&#160;is&#160;the&#160;grid&#160;associated&#160;with&#160;the&#160;variable.  
'specs'&#160;is&#160;the&#160;result&#160;set&#160;of&#160;specifications,&#160;of&#160;the&#160;form&#160;defined&#160;in&#160;the&#160;grid
module.  
  
Return:  
0&#160;if&#160;self&#160;confines&#160;the&#160;grid.  
1&#160;if&#160;self&#160;is&#160;not&#160;associated&#160;with&#160;coordinate&#160;regions,&#160;or&#160;does&#160;not&#160;confine&#160;the
grid.  
  
Note:&#160;This&#160;function&#160;should&#160;return&#160;0&#160;only&#160;if&#160;self&#160;is&#160;a&#160;component&#160;that&#160;confines  
nonrectilinear&#160;grids.&#160;See&#160;class [ coordinateComponent ](/) . `

  
class  SelectorError  ( [ cdms.error.CDMSError ](/cdms.error.html) )

` `

` The&#160;exception&#160;type&#160;for&#160;errors&#160;in&#160;the&#160;selector&#160;packages  
`

Method resolution order:

     [ SelectorError ](/cdms.selectors.html)
     [ cdms.error.CDMSError ](/cdms.error.html)
     [ exceptions.Exception ](/exceptions.html)

* * *

Methods defined here:  

 __init__  (self, args) 

* * *

Methods inherited from [ cdms.error.CDMSError ](/cdms.error.html) :  

 __str__  (self) 

* * *

Methods inherited from [ exceptions.Exception ](/exceptions.html) :  

 __getitem__  (...) 

  
class  axisComponent  ( [ SelectorComponent ](/cdms.selectors.html) )

` `

` A [ SelectorComponent ](/) that&#160;confines&#160;exactly&#160;one&#160;axis&#160;or&#160;coordinate
dimension&#160;(e.g.&#160;latitude).  
`

Methods defined here:  

 __init__  (self, id, spec) 

 __repr__  (self) 

 specify  (self, slab, axes, specifications, confined_by, aux) 
     ` Do&#160;specification&#160;for&#160;axis&#160;self.  id  ;&#160;skip&#160;if&#160;axis&#160;not&#160;present. `

* * *

Methods inherited from [ SelectorComponent ](/cdms.selectors.html) :  

 post  (self, fetched, slab, axes, specifications, confined_by, aux, axismap) 
     ` Post-process&#160;fetched&#160;if&#160;desired,&#160;return&#160;new&#160;value.   
Arguments&#160;slab,&#160;axes,&#160;specifications,&#160;confined_by,&#160;and&#160;aux&#160;are  
pre-subRegion&#160;call.  
  
axismap&#160;gives&#160;the&#160;indices&#160;of&#160;fetched's&#160;axes&#160;in&#160;axes&#160;and&#160;should  
be&#160;modified&#160;as&#160;required&#160;by&#160;this&#160;method.&#160;&#160;Set&#160;axismap[i]&#160;to&#160;None&#160;to  
indicate&#160;that&#160;you&#160;have&#160;eliminated&#160;an&#160;axis. `

 specifyGrid  (self, var, grid, specs) 
     ` Refine&#160;the&#160;specification&#160;suitable&#160;for&#160;grid.intersect().   
  
'var'&#160;is&#160;a&#160;variable.  
'grid'&#160;is&#160;the&#160;grid&#160;associated&#160;with&#160;the&#160;variable.  
'specs'&#160;is&#160;the&#160;result&#160;set&#160;of&#160;specifications,&#160;of&#160;the&#160;form&#160;defined&#160;in&#160;the&#160;grid
module.  
  
Return:  
0&#160;if&#160;self&#160;confines&#160;the&#160;grid.  
1&#160;if&#160;self&#160;is&#160;not&#160;associated&#160;with&#160;coordinate&#160;regions,&#160;or&#160;does&#160;not&#160;confine&#160;the
grid.  
  
Note:&#160;This&#160;function&#160;should&#160;return&#160;0&#160;only&#160;if&#160;self&#160;is&#160;a&#160;component&#160;that&#160;confines  
nonrectilinear&#160;grids.&#160;See&#160;class [ coordinateComponent ](/) . `

  
class  coordinateComponent  ( [ axisComponent ](/cdms.selectors.html) )

` `

` A [ SelectorComponent ](/) that&#160;confines&#160;exactly&#160;one&#160;coordinate&#160;dimension
(e.g.,&#160;latitude)  
`

Method resolution order:

     [ coordinateComponent ](/cdms.selectors.html)
     [ axisComponent ](/cdms.selectors.html)
     [ SelectorComponent ](/cdms.selectors.html)

* * *

Methods defined here:  

 __init__  (self, id, spec) 

 specifyGrid  (self, var, grid, specs) 
     ` Determine&#160;if&#160;this&#160;component&#160;confines&#160;the&#160;grid,&#160;and&#160;if&#160;so&#160;set&#160;the&#160;specs&#160;and&#160;return&#160;1 `

* * *

Methods inherited from [ axisComponent ](/cdms.selectors.html) :  

 __repr__  (self) 

 specify  (self, slab, axes, specifications, confined_by, aux) 
     ` Do&#160;specification&#160;for&#160;axis&#160;self.  id  ;&#160;skip&#160;if&#160;axis&#160;not&#160;present. `

* * *

Methods inherited from [ SelectorComponent ](/cdms.selectors.html) :  

 post  (self, fetched, slab, axes, specifications, confined_by, aux, axismap) 
     ` Post-process&#160;fetched&#160;if&#160;desired,&#160;return&#160;new&#160;value.   
Arguments&#160;slab,&#160;axes,&#160;specifications,&#160;confined_by,&#160;and&#160;aux&#160;are  
pre-subRegion&#160;call.  
  
axismap&#160;gives&#160;the&#160;indices&#160;of&#160;fetched's&#160;axes&#160;in&#160;axes&#160;and&#160;should  
be&#160;modified&#160;as&#160;required&#160;by&#160;this&#160;method.&#160;&#160;Set&#160;axismap[i]&#160;to&#160;None&#160;to  
indicate&#160;that&#160;you&#160;have&#160;eliminated&#160;an&#160;axis. `

  
class  indexComponent  ( [ axisComponent ](/cdms.selectors.html) )

` `

` An [ axisComponent ](/) that&#160;confines&#160;exactly&#160;one&#160;axis&#160;by  
specifying&#160;indices.  
`

Method resolution order:

     [ indexComponent ](/cdms.selectors.html)
     [ axisComponent ](/cdms.selectors.html)
     [ SelectorComponent ](/cdms.selectors.html)

* * *

Methods defined here:  

 __init__  (self, id, start  =None  , stop  =None  , stride  =None  ) 

* * *

Methods inherited from [ axisComponent ](/cdms.selectors.html) :  

 __repr__  (self) 

 specify  (self, slab, axes, specifications, confined_by, aux) 
     ` Do&#160;specification&#160;for&#160;axis&#160;self.  id  ;&#160;skip&#160;if&#160;axis&#160;not&#160;present. `

* * *

Methods inherited from [ SelectorComponent ](/cdms.selectors.html) :  

 post  (self, fetched, slab, axes, specifications, confined_by, aux, axismap) 
     ` Post-process&#160;fetched&#160;if&#160;desired,&#160;return&#160;new&#160;value.   
Arguments&#160;slab,&#160;axes,&#160;specifications,&#160;confined_by,&#160;and&#160;aux&#160;are  
pre-subRegion&#160;call.  
  
axismap&#160;gives&#160;the&#160;indices&#160;of&#160;fetched's&#160;axes&#160;in&#160;axes&#160;and&#160;should  
be&#160;modified&#160;as&#160;required&#160;by&#160;this&#160;method.&#160;&#160;Set&#160;axismap[i]&#160;to&#160;None&#160;to  
indicate&#160;that&#160;you&#160;have&#160;eliminated&#160;an&#160;axis. `

 specifyGrid  (self, var, grid, specs) 
     ` Refine&#160;the&#160;specification&#160;suitable&#160;for&#160;grid.intersect().   
  
'var'&#160;is&#160;a&#160;variable.  
'grid'&#160;is&#160;the&#160;grid&#160;associated&#160;with&#160;the&#160;variable.  
'specs'&#160;is&#160;the&#160;result&#160;set&#160;of&#160;specifications,&#160;of&#160;the&#160;form&#160;defined&#160;in&#160;the&#160;grid
module.  
  
Return:  
0&#160;if&#160;self&#160;confines&#160;the&#160;grid.  
1&#160;if&#160;self&#160;is&#160;not&#160;associated&#160;with&#160;coordinate&#160;regions,&#160;or&#160;does&#160;not&#160;confine&#160;the
grid.  
  
Note:&#160;This&#160;function&#160;should&#160;return&#160;0&#160;only&#160;if&#160;self&#160;is&#160;a&#160;component&#160;that&#160;confines  
nonrectilinear&#160;grids.&#160;See&#160;class [ coordinateComponent ](/) . `

  
class  indexedComponent  ( [ SelectorComponent ](/cdms.selectors.html) )

` `

` A [ SelectorComponent ](/) that&#160;confines&#160;exactly&#160;one&#160;axis  
whose&#160;index&#160;is&#160;given.  
`

Methods defined here:  

 __init__  (self, index, value) 

 specify  (self, slab, axes, specifications, confined_by, aux) 
     ` Do&#160;the&#160;specification&#160;for&#160;axis&#160;whose&#160;index&#160;is&#160;self.  index  . `

* * *

Methods inherited from [ SelectorComponent ](/cdms.selectors.html) :  

 post  (self, fetched, slab, axes, specifications, confined_by, aux, axismap) 
     ` Post-process&#160;fetched&#160;if&#160;desired,&#160;return&#160;new&#160;value.   
Arguments&#160;slab,&#160;axes,&#160;specifications,&#160;confined_by,&#160;and&#160;aux&#160;are  
pre-subRegion&#160;call.  
  
axismap&#160;gives&#160;the&#160;indices&#160;of&#160;fetched's&#160;axes&#160;in&#160;axes&#160;and&#160;should  
be&#160;modified&#160;as&#160;required&#160;by&#160;this&#160;method.&#160;&#160;Set&#160;axismap[i]&#160;to&#160;None&#160;to  
indicate&#160;that&#160;you&#160;have&#160;eliminated&#160;an&#160;axis. `

 specifyGrid  (self, var, grid, specs) 
     ` Refine&#160;the&#160;specification&#160;suitable&#160;for&#160;grid.intersect().   
  
'var'&#160;is&#160;a&#160;variable.  
'grid'&#160;is&#160;the&#160;grid&#160;associated&#160;with&#160;the&#160;variable.  
'specs'&#160;is&#160;the&#160;result&#160;set&#160;of&#160;specifications,&#160;of&#160;the&#160;form&#160;defined&#160;in&#160;the&#160;grid
module.  
  
Return:  
0&#160;if&#160;self&#160;confines&#160;the&#160;grid.  
1&#160;if&#160;self&#160;is&#160;not&#160;associated&#160;with&#160;coordinate&#160;regions,&#160;or&#160;does&#160;not&#160;confine&#160;the
grid.  
  
Note:&#160;This&#160;function&#160;should&#160;return&#160;0&#160;only&#160;if&#160;self&#160;is&#160;a&#160;component&#160;that&#160;confines  
nonrectilinear&#160;grids.&#160;See&#160;class [ coordinateComponent ](/) . `

  
class  positionalComponent  ( [ SelectorComponent ](/cdms.selectors.html)
)

` `

` A [ SelectorComponent ](/) that&#160;confines&#160;the&#160;next&#160;axis&#160;available.  
`

Methods defined here:  

 __init__  (self, v) 

 __repr__  (self) 

 specify  (self, slab, axes, specifications, confined_by, aux) 
     ` Find&#160;the&#160;next&#160;unconfined&#160;axis&#160;and&#160;confine&#160;it. `

* * *

Methods inherited from [ SelectorComponent ](/cdms.selectors.html) :  

 post  (self, fetched, slab, axes, specifications, confined_by, aux, axismap) 
     ` Post-process&#160;fetched&#160;if&#160;desired,&#160;return&#160;new&#160;value.   
Arguments&#160;slab,&#160;axes,&#160;specifications,&#160;confined_by,&#160;and&#160;aux&#160;are  
pre-subRegion&#160;call.  
  
axismap&#160;gives&#160;the&#160;indices&#160;of&#160;fetched's&#160;axes&#160;in&#160;axes&#160;and&#160;should  
be&#160;modified&#160;as&#160;required&#160;by&#160;this&#160;method.&#160;&#160;Set&#160;axismap[i]&#160;to&#160;None&#160;to  
indicate&#160;that&#160;you&#160;have&#160;eliminated&#160;an&#160;axis. `

 specifyGrid  (self, var, grid, specs) 
     ` Refine&#160;the&#160;specification&#160;suitable&#160;for&#160;grid.intersect().   
  
'var'&#160;is&#160;a&#160;variable.  
'grid'&#160;is&#160;the&#160;grid&#160;associated&#160;with&#160;the&#160;variable.  
'specs'&#160;is&#160;the&#160;result&#160;set&#160;of&#160;specifications,&#160;of&#160;the&#160;form&#160;defined&#160;in&#160;the&#160;grid
module.  
  
Return:  
0&#160;if&#160;self&#160;confines&#160;the&#160;grid.  
1&#160;if&#160;self&#160;is&#160;not&#160;associated&#160;with&#160;coordinate&#160;regions,&#160;or&#160;does&#160;not&#160;confine&#160;the
grid.  
  
Note:&#160;This&#160;function&#160;should&#160;return&#160;0&#160;only&#160;if&#160;self&#160;is&#160;a&#160;component&#160;that&#160;confines  
nonrectilinear&#160;grids.&#160;See&#160;class [ coordinateComponent ](/) . `

  
class  requiredComponent  ( [ SelectorComponent ](/cdms.selectors.html) )

` `

` Checks&#160;to&#160;see&#160;that&#160;a&#160;specific&#160;id&#160;axis&#160;must&#160;be&#160;present.  
`

Methods defined here:  

 __init__  (self, ids) 
     ` Checks&#160;to&#160;see&#160;that&#160;a&#160;specific&#160;axis&#160;or&#160;axes&#160;must&#160;be&#160;present.   
Initialize&#160;with&#160;a&#160;sequence&#160;of&#160;ids. `

 specify  (self, slab, axes, specifications, confined_by, aux) 
     ` Doesn't&#160;confine&#160;but&#160;checks&#160;for&#160;existance. `

* * *

Methods inherited from [ SelectorComponent ](/cdms.selectors.html) :  

 post  (self, fetched, slab, axes, specifications, confined_by, aux, axismap) 
     ` Post-process&#160;fetched&#160;if&#160;desired,&#160;return&#160;new&#160;value.   
Arguments&#160;slab,&#160;axes,&#160;specifications,&#160;confined_by,&#160;and&#160;aux&#160;are  
pre-subRegion&#160;call.  
  
axismap&#160;gives&#160;the&#160;indices&#160;of&#160;fetched's&#160;axes&#160;in&#160;axes&#160;and&#160;should  
be&#160;modified&#160;as&#160;required&#160;by&#160;this&#160;method.&#160;&#160;Set&#160;axismap[i]&#160;to&#160;None&#160;to  
indicate&#160;that&#160;you&#160;have&#160;eliminated&#160;an&#160;axis. `

 specifyGrid  (self, var, grid, specs) 
     ` Refine&#160;the&#160;specification&#160;suitable&#160;for&#160;grid.intersect().   
  
'var'&#160;is&#160;a&#160;variable.  
'grid'&#160;is&#160;the&#160;grid&#160;associated&#160;with&#160;the&#160;variable.  
'specs'&#160;is&#160;the&#160;result&#160;set&#160;of&#160;specifications,&#160;of&#160;the&#160;form&#160;defined&#160;in&#160;the&#160;grid
module.  
  
Return:  
0&#160;if&#160;self&#160;confines&#160;the&#160;grid.  
1&#160;if&#160;self&#160;is&#160;not&#160;associated&#160;with&#160;coordinate&#160;regions,&#160;or&#160;does&#160;not&#160;confine&#160;the
grid.  
  
Note:&#160;This&#160;function&#160;should&#160;return&#160;0&#160;only&#160;if&#160;self&#160;is&#160;a&#160;component&#160;that&#160;confines  
nonrectilinear&#160;grids.&#160;See&#160;class [ coordinateComponent ](/) . `

  
 Functions 

` `

 kwselect  (k, value) 
     ` Turn&#160;a&#160;keyword/value&#160;pair&#160;into&#160;a [ SelectorComponent ](/)   
The&#160;words&#160;latitude,&#160;longitude,&#160;time,&#160;and&#160;level&#160;are  
used&#160;to&#160;pass&#160;value&#160;to&#160;the&#160;routine&#160;of&#160;the&#160;same&#160;name.  
Otherise,&#160;axis&#160;is&#160;called&#160;using&#160;k&#160;as&#160;the&#160;id. `

 latitude  (*value) 
     ` Creates&#160;default&#160;selector&#160;corresponding&#160;to&#160;keyword&#160;latitude&#160;=&#160;value `

 latitudeslice  (start  =None  , stop  =None  , stride  =None  ) 

 level  (*value) 
     ` Creates&#160;default&#160;selector&#160;corresponding&#160;to&#160;keyword&#160;level&#160;=&#160;value `

 levelslice  (start  =None  , stop  =None  , stride  =None  ) 

 longitude  (*value) 
     ` Creates&#160;default&#160;selector&#160;corresponding&#160;to&#160;keyword&#160;longitude&#160;=&#160;value `

 longitudeslice  (start  =None  , stop  =None  , stride  =None  ) 

 required  (values) 
     ` Creates&#160;a&#160;selector&#160;that&#160;requires&#160;a&#160;certain&#160;axis&#160;to&#160;be&#160;present. `

 setslice  (id, start  =None  , stop  =None  , stride  =None  ) 

 time  (*value) 
     ` Creates&#160;a&#160;default&#160;selector&#160;corresponding&#160;to&#160;keyword&#160;time=value `

 timeslice  (start  =None  , stop  =None  , stride  =None  ) 

  
 Data 

` `

 LatitudeType  = 'lat'   
 LongitudeType  = 'lon'   
 TimeType  = 'time'   
 VerticalType  = 'lev'   
 all  = Selector() 

* * *

UCRL-WEB-213937 | [ Privacy & Legal Notice ](/disclaimer.html)

[ webmaster@pcmdi.llnl.gov ](/webmaster@pcmdi.llnl.gov)

[ ![Powered by Plone](media/plone_powered.gif) ](/)

