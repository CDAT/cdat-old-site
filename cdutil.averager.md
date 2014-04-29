---
layout: default
title:
---

 [ Skip to content. ](/cdat/source/api-reference/cdutil.averager.html) | [ Skip
to navigation ](/cdat/source/api-reference/cdutil.averager.html)

Search Site

[ Advanced Search&#8230; ](/search_form)

#  [ PCMDI Software Portal ](/)

#####  Sections

  * [ Home ](/)

#####  Personal tools

  * [ Log in ](/login_form)

You are here:  [ Home ](/) -> [ CDAT ](/cdat) -> [ Source Code ](/cdat/source)
-> [ API Reference ](/cdat/source/api-reference) -> Python: function averager

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

        * [ Python: function averager ](/cdat/source/api-reference/cdutil.averager.html)

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

  * [ ![Send this page to somebody](media/mail_icon.gif) ](/cdat/source/api-reference/cdutil.averager.html/sendto_form)
  * [ ![Print this page](media/print_icon.gif) ](/this.print\(\))

#  Python: function averager

 cdutil.averager  = averager(V, axis  =None  , weights  =None  , action  ='average'  , returned  =0  , weight  =None  , combinewts  =None  ) 
     ` Documentation&#160;for&#160;averager():   
\-----------------------------  
The&#160;averager()&#160;function&#160;provides&#160;a&#160;convenient&#160;way&#160;of&#160;averaging&#160;your&#160;data
giving  
you&#160;control&#160;over&#160;the&#160;order&#160;of&#160;operations&#160;(i.e&#160;which&#160;dimensions&#160;are&#160;averaged  
over&#160;first)&#160;and&#160;also&#160;the&#160;weighting&#160;for&#160;the&#160;different&#160;axes.&#160;You&#160;can&#160;pass&#160;your  
own&#160;array&#160;of&#160;weights&#160;for&#160;each&#160;dimension&#160;or&#160;use&#160;the&#160;default&#160;(grid)&#160;weights&#160;or  
specify&#160;equal&#160;weighting.  
  
  
Author:&#160;Krishna&#160;AchutaRao&#160;:&#160;achutarao1@llnl.gov  
  
Returns:  
\-------  
The&#160;average&#160;over&#160;the&#160;specified&#160;dimensions.  
Usage:  
\------  
from&#160;cdutil&#160;import&#160;averager  
averager(&#160;V,&#160;axis='axisoptions',&#160;weights=weightoptions,&#160;action='average',  
returned='0')  
  
Where&#160;V&#160;is&#160;an&#160;array.&#160;It&#160;can&#160;be&#160;an&#160;array&#160;of&#160;Numeric,&#160;MA&#160;or&#160;MV&#160;type.&#160;In&#160;each
case  
the&#160;function&#160;returns&#160;an&#160;array&#160;(except&#160;when&#160;it&#160;results&#160;in&#160;a&#160;scalar)&#160;of&#160;the&#160;same  
type&#160;as&#160;V.&#160;See&#160;examples&#160;for&#160;more&#160;details.  
  
Optional&#160;Arguments:  
\-------------------  
axis=axisoptions  
Restrictions:&#160;axisoptions&#160;has&#160;to&#160;be&#160;a&#160;string  
Default&#160;:&#160;first&#160;dimension&#160;in&#160;the&#160;data&#160;you&#160;pass&#160;to&#160;the&#160;function.  
  
You&#160;can&#160;pass&#160;axis='tyx',&#160;or&#160;'123',&#160;or&#160;'x&#160;(plev)'&#160;etc.&#160;&#160;the&#160;same&#160;way&#160;as  
in&#160;order=&#160;options&#160;for&#160;variable&#160;operations&#160;EXCEPT&#160;that  
'...'(i.e&#160;Ellipses)&#160;are&#160;not&#160;allowed.&#160;In&#160;the&#160;case&#160;that&#160;V&#160;is&#160;a&#160;Numeric&#160;or  
MA&#160;array,&#160;axis&#160;names&#160;have&#160;no&#160;meaning&#160;and&#160;only&#160;axis&#160;indexes&#160;are&#160;valid.  
  
  
weights=weightoptions  
Default&#160;:  
'weighted'&#160;for&#160;Transient&#160;Variables&#160;(MVs)  
'unweighted'&#160;for&#160;MA&#160;or&#160;Numeric&#160;arrays.  
  
Note&#160;that&#160;depending&#160;on&#160;the&#160;array&#160;being&#160;operated&#160;on&#160;by&#160;averager,&#160;the  
default&#160;weights&#160;change!  
  
Weight&#160;options&#160;are&#160;one&#160;of&#160;'weighted',&#160;'unweighted',&#160;&#160;an&#160;array&#160;of&#160;weights&#160;for  
each&#160;dimension&#160;or&#160;a&#160;MaskedVariable&#160;of&#160;the&#160;same&#160;shape&#160;as&#160;the&#160;data&#160;x.  
  
-&#160;'weighted'&#160;means&#160;use&#160;the&#160;grid&#160;information&#160;to&#160;generate&#160;weights&#160;for   
that&#160;dimension.  
  
-&#160;'unweighted'&#160;means&#160;use&#160;equal&#160;weights&#160;for&#160;all&#160;the&#160;grid&#160;points&#160;in&#160;that&#160;axis.   
  
-&#160;Also&#160;an&#160;array&#160;of&#160;weights&#160;(of&#160;the&#160;same&#160;shape&#160;as&#160;the&#160;dimension&#160;being   
averaged&#160;over&#160;or&#160;same&#160;shape&#160;as&#160;V)&#160;can&#160;be&#160;passed.  
  
Additional&#160;Notes&#160;on&#160;'weighted'&#160;option:&#160;The&#160;weights&#160;are&#160;generated  
using&#160;the&#160;bounds&#160;for&#160;the&#160;specified&#160;axis.&#160;For&#160;latitude&#160;and&#160;Longitude,  
the&#160;weights&#160;are&#160;calculated&#160;using&#160;the&#160;area&#160;(see&#160;the&#160;cdms&#160;manual  
grid.getWeights()&#160;for&#160;more&#160;details)&#160;whereas&#160;for&#160;the&#160;other&#160;axes  
weights&#160;are&#160;the&#160;difference&#160;between&#160;the&#160;bounds&#160;(when&#160;the&#160;bounds&#160;are  
available).&#160;If&#160;the&#160;bounds&#160;are&#160;stored&#160;in&#160;the&#160;file&#160;being&#160;read&#160;in,&#160;then  
those&#160;values&#160;are&#160;used.&#160;Otherwise,&#160;bounds&#160;are&#160;generated&#160;as&#160;long&#160;as  
cdms.setAutoBounds('on')&#160;is&#160;set.&#160;If&#160;cdms.setAutoBounds()&#160;is&#160;set&#160;to  
'off',&#160;then&#160;an&#160;Error&#160;is&#160;raised.  
  
action='average'&#160;or&#160;'sum'  
Default&#160;:&#160;'average'  
  
You&#160;can&#160;either&#160;return&#160;the&#160;weighted&#160;average&#160;or&#160;the&#160;weighted&#160;sum&#160;of&#160;the  
data&#160;by&#160;specifying&#160;the&#160;keyword&#160;argument&#160;action=  
  
returned&#160;=&#160;0&#160;or&#160;1  
Default:&#160;0  
  
-&#160;0&#160;implies&#160;sum&#160;of&#160;weights&#160;are&#160;not&#160;returned&#160;after&#160;averaging&#160;operation.   
-&#160;1&#160;implies&#160;the&#160;sum&#160;of&#160;weights&#160;after&#160;the&#160;average&#160;operation&#160;is&#160;returned.   
  
combinewts&#160;=&#160;None,&#160;0&#160;or&#160;1  
Default:&#160;None&#160;-&#160;same&#160;as&#160;0  
-&#160;0&#160;implies&#160;weights&#160;passed&#160;for&#160;individual&#160;axes&#160;are&#160;not&#160;combined&#160;into&#160;one   
weight&#160;array&#160;for&#160;the&#160;full&#160;variable&#160;V&#160;before&#160;performing&#160;operation.  
-&#160;1&#160;implies&#160;weights&#160;passed&#160;for&#160;individual&#160;axes&#160;are&#160;combined&#160;into&#160;one   
weight&#160;array&#160;for&#160;the&#160;full&#160;variable&#160;before&#160;performing&#160;average&#160;or&#160;sum  
operations.&#160;One-dimensional&#160;weight&#160;arrays&#160;or&#160;key&#160;words&#160;of&#160;'weighted'&#160;or  
'unweighted'&#160;must&#160;be&#160;passed&#160;for&#160;the&#160;axes&#160;over&#160;which&#160;the&#160;operation&#160;is  
to&#160;be&#160;performed.&#160;Additionally,&#160;weights&#160;for&#160;axes&#160;that&#160;are&#160;not&#160;being  
averaged&#160;or&#160;summed&#160;may&#160;also&#160;bepassed&#160;in&#160;the&#160;order&#160;in&#160;which&#160;they&#160;appear.  
If&#160;the&#160;weights&#160;for&#160;the&#160;other&#160;axes&#160;are&#160;not&#160;passed,&#160;they&#160;&#160;are&#160;assumed&#160;to  
be&#160;equally&#160;weighted.  
  
Examples:  
\---------  
>>>&#160;f&#160;=&#160;cdms.open('data_file_name')  
>>>&#160;averager(f('variable_name'),&#160;axis='1')  
#&#160;extracts&#160;the&#160;variable&#160;'variable_name'&#160;from&#160;f&#160;and&#160;averages&#160;over&#160;the  
#&#160;dimension&#160;whose&#160;position&#160;is&#160;1.&#160;Since&#160;no&#160;other&#160;options&#160;are&#160;specified,  
#&#160;defaults&#160;kick&#160;in&#160;i.e&#160;weight='weighted'&#160;and&#160;returned=0  
  
>>>&#160;averager(V,&#160;axis='xy',&#160;weights=['weighted','unweighted'])  
or  
>>>&#160;averager(V,&#160;axis='t',&#160;weights='unweighted')  
or  
>>>&#160;averager(V,&#160;axis='x')  
#&#160;Default&#160;weights&#160;option&#160;of&#160;'weighted'&#160;is&#160;implemented  
or  
>>>&#160;averager(V,&#160;axis='x',&#160;weights=mywts)  
#&#160;where&#160;mywts&#160;is&#160;an&#160;array&#160;of&#160;shape&#160;(len(xaxis))&#160;or&#160;shape(V)  
or  
>>>&#160;averager(V,&#160;axis='(lon)y',&#160;weights=[myxwts,&#160;myywts])  
#&#160;where&#160;myxwts&#160;is&#160;of&#160;shape&#160;len(xaxis)&#160;and&#160;myywts&#160;is&#160;of&#160;shape&#160;len(yaxis)  
or  
>>>&#160;averager(V,&#160;axis='xy',&#160;weights=V_wts)  
#&#160;where&#160;V_wts&#160;is&#160;a&#160;Masked&#160;Variable&#160;of&#160;shape&#160;V  
or  
>>>&#160;averager(V,&#160;axis='x',&#160;weights='unweighted',&#160;action='sum')  
#&#160;will&#160;return&#160;the&#160;equally&#160;weighted&#160;sum&#160;over&#160;the&#160;x&#160;dimension  
or  
>>>&#160;ywt&#160;=&#160;area_weights(y)  
>>>&#160;fractional_area&#160;=&#160;averager(ywt,&#160;axis='xy',  
weights=['unweighted',&#160;'unweighted'],&#160;action='sum')  
#&#160;is&#160;a&#160;good&#160;way&#160;to&#160;compute&#160;the&#160;area&#160;fraction&#160;that&#160;the  
#&#160;data&#160;y&#160;that&#160;is&#160;non-missing  
  
Note:  
\-----  
When&#160;averaging&#160;data&#160;with&#160;missing&#160;values,&#160;extra&#160;care&#160;needs&#160;to&#160;be&#160;taken.  
It&#160;is&#160;recommended&#160;that&#160;you&#160;use&#160;the&#160;default&#160;weights='weighted'&#160;option.  
This&#160;uses&#160;cdutil.area_weights(V)&#160;to&#160;get&#160;the&#160;correct&#160;weights&#160;to  
pass&#160;to&#160;the&#160;averager.  
>>>&#160;averager(V,&#160;axis='xy',&#160;weights='weighted')  
  
The&#160;above&#160;is&#160;equivalent&#160;to:  
>>>&#160;V_wts&#160;=&#160;cdutil.area_weights(V)  
>>>&#160;result&#160;=&#160;averager(V,&#160;axis='xy',&#160;weights=V_wts)  
or  
>>>&#160;result&#160;=&#160;averager(V,&#160;axis='xy',&#160;weights=cdutil.area_weights(V))  
  
However,&#160;the&#160;area_weights&#160;function&#160;requires&#160;that&#160;the&#160;axis&#160;bounds&#160;are  
stored&#160;or&#160;can&#160;be&#160;calculated&#160;(see&#160;documentation&#160;of&#160;area_weights&#160;for&#160;more  
details).&#160;In&#160;the&#160;case&#160;that&#160;such&#160;weights&#160;are&#160;not&#160;stored&#160;with&#160;the&#160;axis  
specifications&#160;(or&#160;the&#160;user&#160;desires&#160;to&#160;specify&#160;weights&#160;from&#160;another  
source),&#160;the&#160;use&#160;of&#160;combinewts&#160;option&#160;can&#160;produce&#160;the&#160;same&#160;results.  
In&#160;short,&#160;the&#160;following&#160;two&#160;are&#160;equivalent:  
>>>&#160;xavg_1&#160;=&#160;averager(X,&#160;axis&#160;=&#160;'xy',&#160;weights&#160;=&#160;area_weights(X))  
>>>&#160;xavg_2&#160;=&#160;averager(X,&#160;axis&#160;=&#160;'xy',&#160;weights&#160;=&#160;['weighted',&#160;'weighted',
'weighted'],&#160;combinewts=1)  
  
Where&#160;X&#160;is&#160;a&#160;function&#160;of&#160;x,&#160;y&#160;and&#160;a&#160;third&#160;dimension&#160;such&#160;as&#160;time&#160;or&#160;level.  
  
In&#160;general,&#160;the&#160;above&#160;can&#160;be&#160;substituted&#160;with&#160;arrays&#160;of&#160;weights&#160;where  
the&#160;'weighted'&#160;keyword&#160;appears. `

* * *

UCRL-WEB-213937 | [ Privacy & Legal Notice ](/disclaimer.html)

[ webmaster@pcmdi.llnl.gov ](/webmaster@pcmdi.llnl.gov)

[ ![Powered by Plone](media/plone_powered.gif) ](/)

