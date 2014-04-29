---
layout: default
title:
---

 [ Skip to content. ](/cdat/source/api-reference/cdms.MV.html) | [ Skip to
navigation ](/cdat/source/api-reference/cdms.MV.html)

Search Site

[ Advanced Search&#8230; ](/search_form)

#  [ PCMDI Software Portal ](/)

#####  Sections

  * [ Home ](/)

#####  Personal tools

  * [ Log in ](/login_form)

You are here:  [ Home ](/) -> [ CDAT ](/cdat) -> [ Source Code ](/cdat/source)
-> [ API Reference ](/cdat/source/api-reference) -> Python: module cdms.MV

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

        * [ Python: module cdms.MV ](/cdat/source/api-reference/cdms.MV.html)

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

  * [ ![Send this page to somebody](media/mail_icon.gif) ](/cdat/source/api-reference/cdms.MV.html/sendto_form)
  * [ ![Print this page](media/print_icon.gif) ](/this.print\(\))

#  Python: module cdms.MV

  
  
 [ cdms  ](/cdms.html) .MV 
[ index ](/)  

` CDMS&#160;Variable&#160;objects,&#160;MaskedArray&#160;interface `

  
 Modules 

` `

[ MA ](/MA.html)  

[ Numeric ](/Numeric.html)  

[ string ](/string.html)  

  
 Classes 

` `

[ var_binary_operation ](/cdms.MV.html)

[ var_unary_operation ](/cdms.MV.html)

  
class  var_binary_operation 

` `

Methods defined here:  

 __call__  (self, a, b) 

 __init__  (self, mafunc) 
     ` [ var_binary_operation ](/) (mafunc)   
mafunc&#160;is&#160;an&#160;MA&#160;masked_binary_function. `

 accumulate  (self, target, axis  =0  ) 

 outer  (self, a, b) 
     ` Return&#160;the&#160;function&#160;applied&#160;to&#160;the&#160;outer&#160;product&#160;of&#160;a&#160;and&#160;b `

 reduce  (self, target, axis  =0  ) 

  
class  var_unary_operation 

` `

Methods defined here:  

 __call__  (self, a) 

 __init__  (self, mafunc) 
     ` [ var_unary_operation ](/) (mafunc)   
mafunc&#160;is&#160;an&#160;MA&#160;masked_unary_function. `

  
 Functions 

` `

 arange  = arrayrange(start, stop  =None  , step  =1  , typecode  =None  , axis  =None  , attributes  =None  , id  =None  ) 
     ` Just&#160;like&#160;range()&#160;except&#160;it&#160;returns&#160;a&#160;variable&#160;whose&#160;type&#160;can&#160;be&#160;specfied   
by&#160;the&#160;keyword&#160;argument&#160;typecode.&#160;The&#160;axis&#160;of&#160;the&#160;result&#160;variable&#160;may&#160;be
specified. `

 argsort  (x, axis  =-1  , fill_value  =None  ) 
     ` Treating&#160;masked&#160;values&#160;as&#160;if&#160;they&#160;have&#160;the&#160;value&#160;fill_value,   
return&#160;sort&#160;indices&#160;for&#160;sorting&#160;along&#160;given&#160;axis.  
if&#160;fill_value&#160;is&#160;None,&#160;use&#160;fill_value(x) `

 arrayrange  (start, stop  =None  , step  =1  , typecode  =None  , axis  =None  , attributes  =None  , id  =None  ) 
     ` Just&#160;like&#160;range()&#160;except&#160;it&#160;returns&#160;a&#160;variable&#160;whose&#160;type&#160;can&#160;be&#160;specfied   
by&#160;the&#160;keyword&#160;argument&#160;typecode.&#160;The&#160;axis&#160;of&#160;the&#160;result&#160;variable&#160;may&#160;be
specified. `

 asarray  (data, typecode  =None  ) 
     ` [ asarray ](/) (data,&#160;typecode=None)&#160;=&#160;array(data,&#160;typecode=None,&#160;copy=0)   
Returns&#160;data&#160;if&#160;typecode&#160;if&#160;data&#160;is&#160;a&#160;MaskedArray&#160;and&#160;typecode&#160;None  
or&#160;the&#160;same. `

 average  (a, axis  =0  , weights  =None  , returned  =0  ) 
     ` [ average ](/) (a,&#160;axis=0,&#160;weights=None)   
Computes&#160;average&#160;along&#160;indicated&#160;axis.  
If&#160;axis&#160;is&#160;None,&#160;average&#160;over&#160;the&#160;entire&#160;array  
Inputs&#160;can&#160;be&#160;integer&#160;or&#160;floating&#160;types;&#160;result&#160;is&#160;of&#160;type&#160;Float.  
  
If&#160;weights&#160;are&#160;given,&#160;result&#160;is [ sum ](/) (a*weights)/( [ sum ](/)
(weights)*1.0)  
weights&#160;must&#160;have&#160;a's&#160;shape&#160;or&#160;be&#160;the&#160;1-d&#160;with&#160;length&#160;the&#160;size  
of&#160;a&#160;in&#160;the&#160;given&#160;axis.  
  
If&#160;returned,&#160;return&#160;a&#160;tuple:&#160;the&#160;result&#160;and&#160;the&#160;sum&#160;of&#160;the&#160;weights  
or&#160;count&#160;of&#160;values.&#160;Results&#160;will&#160;have&#160;the&#160;same&#160;shape.  
  
masked&#160;values&#160;in&#160;the&#160;weights&#160;will&#160;be&#160;set&#160;to&#160;0.0 `

 choose  (indices, t) 
     ` Returns&#160;an&#160;array&#160;shaped&#160;like&#160;indices&#160;containing&#160;elements&#160;chosen   
from&#160;t.  
If&#160;an&#160;element&#160;of&#160;t&#160;is&#160;the&#160;special&#160;element&#160;masked,&#160;any&#160;element  
of&#160;the&#160;result&#160;that&#160;"chooses"&#160;that&#160;element&#160;is&#160;masked.  
  
The&#160;result&#160;has&#160;only&#160;the&#160;default&#160;axes. `

 commonAxes  (a, bdom, omit  =None  ) 
     ` Helper&#160;function&#160;for&#160;commonDomain.&#160;'a'&#160;is&#160;a&#160;variable&#160;or&#160;array,   
'b'&#160;is&#160;an&#160;axislist&#160;or&#160;None. `

 commonDomain  (a, b, omit  =None  ) 
     ` [ commonDomain ](/) (a,b)&#160;tests&#160;that&#160;the&#160;domains&#160;of&#160;variables/arrays&#160;a&#160;and&#160;b&#160;are&#160;equal,   
and&#160;returns&#160;the&#160;common&#160;domain&#160;if&#160;equal,&#160;or&#160;None&#160;if&#160;not&#160;equal.&#160;The&#160;domains&#160;may  
differ&#160;in&#160;that&#160;one&#160;domain&#160;may&#160;have&#160;leading&#160;axes&#160;not&#160;common  
to&#160;the&#160;other;&#160;the&#160;result&#160;domain&#160;will&#160;contain&#160;those&#160;axes.  
If&#160;<omit>&#160;is&#160;specified,&#160;as&#160;an&#160;integer&#160;i,&#160;skip&#160;comparison&#160;of&#160;the&#160;ith&#160;dimension  
and&#160;return&#160;None&#160;for&#160;the&#160;ith&#160;(common)&#160;dimension. `

 commonGrid  (a, b, axes) 
     ` [ commonGrid ](/) (a,b,axes)&#160;tests&#160;if&#160;the&#160;grids&#160;associated&#160;with&#160;variables&#160;a,&#160;b&#160;are&#160;equal,   
and&#160;consistent&#160;with&#160;the&#160;list&#160;of&#160;axes.&#160;If&#160;so,&#160;the&#160;common&#160;grid&#160;is&#160;returned,&#160;else
None  
is&#160;returned.&#160;a&#160;and&#160;b&#160;can&#160;be&#160;Numeric&#160;arrays,&#160;in&#160;which&#160;case&#160;the&#160;result&#160;is&#160;None.  
  
The&#160;common&#160;grid&#160;is&#160;'consistent'&#160;with&#160;axes&#160;if&#160;the&#160;grid&#160;axes&#160;(e.g.,&#160;the&#160;axes&#160;of
latitude&#160;and  
longitude&#160;coordinate&#160;variables)&#160;are&#160;members&#160;of&#160;the&#160;list&#160;'axes'.  
  
If&#160;the&#160;grid(s)&#160;of&#160;a,&#160;b&#160;are&#160;rectilinear,&#160;the&#160;result&#160;is&#160;None,&#160;as&#160;the&#160;grids&#160;are
implicitly  
defined&#160;by&#160;the&#160;axes. `

 commonGrid1  (a, gb, axes) 
     ` Helper&#160;function&#160;for&#160;commonGrid. `

 concatenate  (arrays, axis  =0  , axisid  =None  , axisattributes  =None  ) 
     ` Concatenate&#160;the&#160;arrays&#160;along&#160;the&#160;given&#160;axis.&#160;Give&#160;the&#160;extended&#160;axis&#160;the&#160;id&#160;and   
attributes&#160;provided&#160;-&#160;by&#160;default,&#160;those&#160;of&#160;the&#160;first&#160;array. `

 count  (a, axis  =None  ) 
     ` Count&#160;of&#160;the&#160;non-masked&#160;elements&#160;in&#160;a,&#160;or&#160;along&#160;a&#160;certain&#160;axis. `

 diagonal  (a, offset  =0  , axis1  =0  , axis2  =1  ) 
     ` [ diagonal ](/) (a,&#160;offset=0,&#160;axis1=0,&#160;axis2&#160;=&#160;1)&#160;returns&#160;the&#160;given   
diagonals&#160;defined&#160;by&#160;the&#160;two&#160;dimensions&#160;of&#160;the&#160;array. `

 fromfunction  (f, dimensions) 
     ` Apply&#160;f&#160;to&#160;s&#160;to&#160;create&#160;an&#160;array&#160;as&#160;in&#160;Numeric. `

 fromstring  (s, t) 
     ` Construct&#160;a&#160;masked&#160;array&#160;from&#160;a&#160;string.&#160;Result&#160;will&#160;have&#160;no&#160;mask.   
t&#160;is&#160;a&#160;typecode. `

 isMaskedVariable  (x) 
     ` Is&#160;x&#160;a&#160;masked&#160;variable,&#160;that&#160;is,&#160;an&#160;instance&#160;of&#160;AbstractVariable? `

 left_shift  (a, n) 
     ` Left&#160;shift&#160;n&#160;bits `

 masked_array  (a, mask  =None  , fill_value  =None  , axes  =None  , attributes  =None  , id  =None  ) 
     ` [ masked_array ](/) (a,&#160;mask=None)&#160;=   
array(a,&#160;mask=mask,&#160;copy=0,&#160;fill_value=fill_value)  
Use&#160;fill_value(a)&#160;if&#160;None. `

 masked_equal  (x, value) 
     ` [ masked_equal ](/) (x,&#160;value)&#160;=&#160;x&#160;masked&#160;where&#160;x&#160;==&#160;value   
For&#160;floating&#160;point&#160;consider [ masked_values ](/) (x,&#160;value)&#160;instead. `

 masked_greater  (x, value) 
     ` [ masked_greater ](/) (x,&#160;value)&#160;=&#160;x&#160;masked&#160;where&#160;x&#160;>&#160;value `

 masked_greater_equal  (x, value) 
     ` [ masked_greater_equal ](/) (x,&#160;value)&#160;=&#160;x&#160;masked&#160;where&#160;x&#160;>=&#160;value `

 masked_inside  (x, v1, v2) 
     ` x&#160;with&#160;mask&#160;of&#160;all&#160;values&#160;of&#160;x&#160;that&#160;are&#160;inside&#160;[v1,v2] `

 masked_less  (x, value) 
     ` [ masked_less ](/) (x,&#160;value)&#160;=&#160;x&#160;masked&#160;where&#160;x&#160;<&#160;value `

 masked_less_equal  (x, value) 
     ` [ masked_less_equal ](/) (x,&#160;value)&#160;=&#160;x&#160;masked&#160;where&#160;x&#160;<=&#160;value `

 masked_not_equal  (x, value) 
     ` [ masked_not_equal ](/) (x,&#160;value)&#160;=&#160;x&#160;masked&#160;where&#160;x&#160;!=&#160;value `

 masked_object  (data, value, copy  =1  , savespace  =0  , axes  =None  , attributes  =None  , id  =None  ) 
     ` Create&#160;array&#160;masked&#160;where&#160;exactly&#160;data&#160;equal&#160;to&#160;value `

 masked_outside  (x, v1, v2) 
     ` x&#160;with&#160;mask&#160;of&#160;all&#160;values&#160;of&#160;x&#160;that&#160;are&#160;outside&#160;[v1,v2] `

 masked_values  (data, value, rtol  =1.0000000000000001e-05  , atol  =1e-08  , copy  =1  , savespace  =0  , axes  =None  , attributes  =None  , id  =None  ) 
     ` [ masked_values ](/) (data,&#160;value,&#160;rtol=1.e-5,&#160;atol=1.e-8)   
Create&#160;a&#160;masked&#160;array;&#160;mask&#160;is&#160;None&#160;if&#160;possible.  
May&#160;share&#160;data&#160;values&#160;with&#160;original&#160;array,&#160;but&#160;not&#160;recommended.  
Masked&#160;where&#160;abs(data-value)<=&#160;atol&#160;+&#160;rtol&#160;*&#160;abs(value) `

 masked_where  (condition, x, copy  =1  ) 
     ` Return&#160;x&#160;as&#160;an&#160;array&#160;masked&#160;where&#160;condition&#160;is&#160;true.   
Also&#160;masked&#160;where&#160;x&#160;or&#160;condition&#160;masked. `

 ones  (shape, typecode  ='l'  , savespace  =0  , axes  =None  , attributes  =None  , id  =None  , grid  =None  ) 
     ` [ ones ](/) (n,&#160;typecode=Int,&#160;savespace=0,&#160;axes=None,&#160;attributes=None,&#160;id=None)&#160;=   
an&#160;array&#160;of&#160;all&#160;ones&#160;of&#160;the&#160;given&#160;length&#160;or&#160;shape. `

 outerproduct  (a, b) 
     ` [ outerproduct ](/) (a,b)&#160;=&#160;{a[i]*b[j]},&#160;has&#160;shape&#160;(len(a),len(b)) `

 power  (a, b, third  =None  ) 
     ` ab `

 product  (a, axis  =0  ) 
     ` Product&#160;of&#160;elements&#160;along&#160;axis. `

 repeat  (a, repeats, axis  =0  ) 
     ` repeat&#160;elements&#160;of&#160;a&#160;repeats&#160;times&#160;along&#160;axis   
repeats&#160;is&#160;a&#160;sequence&#160;of&#160;length&#160;a.shape[axis]  
telling&#160;how&#160;many&#160;times&#160;to&#160;repeat&#160;each&#160;element. `

 reshape  (a, newshape, axes  =None  , attributes  =None  , id  =None  , grid  =None  ) 
     ` Copy&#160;of&#160;a&#160;with&#160;a&#160;new&#160;shape. `

 resize  (a, new_shape, axes  =None  , attributes  =None  , id  =None  , grid  =None  ) 
     ` [ resize ](/) (a,&#160;new_shape)&#160;returns&#160;a&#160;new&#160;array&#160;with&#160;the&#160;specified&#160;shape.   
The&#160;original&#160;array's&#160;total&#160;size&#160;can&#160;be&#160;any&#160;size. `

 right_shift  (a, n) 
     ` Right&#160;shift&#160;n&#160;bits `

 set_default_fill_value  (value_type, value) 
     ` Set&#160;the&#160;default&#160;fill&#160;value&#160;for&#160;value_type&#160;to&#160;value.   
value_type&#160;is&#160;a&#160;string:&#160;'real','complex','character','integer',or&#160;'object'.  
value&#160;should&#160;be&#160;a&#160;scalar&#160;or&#160;single-element&#160;array. `

 sort  (a, axis  =-1  ) 
     ` If&#160;x&#160;does&#160;not&#160;have&#160;a&#160;mask,&#160;return&#160;a&#160;masked&#160;array&#160;formed&#160;from&#160;the   
result&#160;of&#160;Numeric. [ sort ](/) (x,&#160;axis).  
Otherwise,&#160;fill&#160;x&#160;with&#160;fill_value.&#160;Sort&#160;it.  
Set&#160;a&#160;mask&#160;where&#160;the&#160;result&#160;is&#160;equal&#160;to&#160;fill_value.  
Note&#160;that&#160;this&#160;may&#160;have&#160;unintended&#160;consequences&#160;if&#160;the&#160;data&#160;contains&#160;the  
fill&#160;value&#160;at&#160;a&#160;non-masked&#160;site.  
  
If&#160;fill_value&#160;is&#160;not&#160;given&#160;the&#160;default&#160;fill&#160;value&#160;for&#160;x's&#160;type&#160;will&#160;be  
used.  
The&#160;sort&#160;axis&#160;is&#160;replaced&#160;with&#160;a&#160;dummy&#160;axis. `

 sum  (a, axis  =0  , fill_value  =0  ) 
     ` Sum&#160;of&#160;elements&#160;along&#160;a&#160;certain&#160;axis. `

 take  (a, indices, axis  =0  ) 
     ` [ take ](/) (a,&#160;indices,&#160;axis=0)&#160;returns&#160;selection&#160;of&#160;items&#160;from&#160;a. `

 transpose  (a, axes  =None  ) 
     ` [ transpose ](/) (a,&#160;axes=None)&#160;reorder&#160;dimensions&#160;per&#160;tuple&#160;axes `

 where  (condition, x, y) 
     ` [ where ](/) (condition,&#160;x,&#160;y)&#160;is&#160;x&#160;where&#160;condition&#160;is&#160;true,&#160;y&#160;otherwise `

 zeros  (shape, typecode  ='l'  , savespace  =0  , axes  =None  , attributes  =None  , id  =None  , grid  =None  ) 
     ` [ zeros ](/) (n,&#160;typecode=Int,&#160;savespace=0,&#160;axes=None,&#160;attributes=None,&#160;id=None)&#160;=   
an&#160;array&#160;of&#160;all&#160;zeros&#160;of&#160;the&#160;given&#160;length&#160;or&#160;shape. `

  
 Data 

` `

 Character  = 'c'   
 Complex  = 'D'   
 Complex0  = 'F'   
 Complex16  = 'F'   
 Complex32  = 'F'   
 Complex64  = 'D'   
 Complex8  = 'F'   
 Float  = 'd'   
 Float0  = 'f'   
 Float16  = 'f'   
 Float32  = 'f'   
 Float64  = 'd'   
 Float8  = 'f'   
 Int  = 'l'   
 Int0  = '1'   
 Int16  = 's'   
 Int32  = 'i'   
 Int8  = '1'   
 PyObject  = 'O'   
 UInt  = 'u'   
 UInt16  = 'w'   
 UInt32  = 'u'   
 UInt8  = 'b'   
 UnsignedInt16  = 'w'   
 UnsignedInt32  = 'u'   
 UnsignedInt8  = 'b'   
 UnsignedInteger  = 'u'   
 absolute  = <cdms.MV.var_unary_operation instance>   
 add  = <cdms.MV.var_binary_operation instance>   
 alltrue  = <cdms.MV.var_unary_operation instance>   
 arccos  = <cdms.MV.var_unary_operation instance>   
 arcsin  = <cdms.MV.var_unary_operation instance>   
 arctan  = <cdms.MV.var_unary_operation instance>   
 arctan2  = <cdms.MV.var_binary_operation instance>   
 around  = <cdms.MV.var_unary_operation instance>   
 bitwise_and  = <cdms.MV.var_binary_operation instance>   
 bitwise_or  = <cdms.MV.var_binary_operation instance>   
 bitwise_xor  = <cdms.MV.var_binary_operation instance>   
 ceil  = <cdms.MV.var_unary_operation instance>   
 conjugate  = <cdms.MV.var_unary_operation instance>   
 cos  = <cdms.MV.var_unary_operation instance>   
 cosh  = <cdms.MV.var_unary_operation instance>   
 divide  = <cdms.MV.var_binary_operation instance>   
 e  = 2.7182818284590451   
 equal  = <cdms.MV.var_binary_operation instance>   
 exp  = <cdms.MV.var_unary_operation instance>   
 fabs  = <cdms.MV.var_unary_operation instance>   
 floor  = <cdms.MV.var_unary_operation instance>   
 fmod  = <cdms.MV.var_binary_operation instance>   
 greater  = <cdms.MV.var_binary_operation instance>   
 greater_equal  = <cdms.MV.var_binary_operation instance>   
 hypot  = <cdms.MV.var_binary_operation instance>   
 less  = <cdms.MV.var_binary_operation instance>   
 less_equal  = <cdms.MV.var_binary_operation instance>   
 log  = <cdms.MV.var_unary_operation instance>   
 log10  = <cdms.MV.var_unary_operation instance>   
 logical_and  = <cdms.MV.var_binary_operation instance>   
 logical_not  = <cdms.MV.var_unary_operation instance>   
 logical_or  = <cdms.MV.var_binary_operation instance>   
 logical_xor  = <cdms.MV.var_binary_operation instance>   
 masked  = array(data = 0, mask = 1, fill_value=[0,])   
 maximum  = <cdms.MV._maximum_operation instance>   
 minimum  = <cdms.MV._minimum_operation instance>   
 multiply  = <cdms.MV.var_binary_operation instance>   
 negative  = <cdms.MV.var_unary_operation instance>   
 nonzero  = <cdms.MV.var_unary_operation instance>   
 not_equal  = <cdms.MV.var_binary_operation instance>   
 pi  = 3.1415926535897931   
 remainder  = <cdms.MV.var_binary_operation instance>   
 sin  = <cdms.MV.var_unary_operation instance>   
 sinh  = <cdms.MV.var_unary_operation instance>   
 sometrue  = <cdms.MV.var_unary_operation instance>   
 sqrt  = <cdms.MV.var_unary_operation instance>   
 subtract  = <cdms.MV.var_binary_operation instance>   
 tan  = <cdms.MV.var_unary_operation instance>   
 tanh  = <cdms.MV.var_unary_operation instance>   
 typecodes  = {'Character': 'c', 'Complex': 'FD', 'Float': 'fd', 'Integer': '1sil', 'UnsignedInteger': 'bwu'} 

* * *

UCRL-WEB-213937 | [ Privacy & Legal Notice ](/disclaimer.html)

[ webmaster@pcmdi.llnl.gov ](/webmaster@pcmdi.llnl.gov)

[ ![Powered by Plone](media/plone_powered.gif) ](/)

