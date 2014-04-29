---
layout: default
title:
---

 [ Skip to content. ](/cdat/source/api-reference/browser.gui_functions.html) |
[ Skip to navigation ](/cdat/source/api-reference/browser.gui_functions.html)

Search Site

[ Advanced Search&#8230; ](/search_form)

#  [ PCMDI Software Portal ](/)

#####  Sections

  * [ Home ](/)

#####  Personal tools

  * [ Log in ](/login_form)

You are here:  [ Home ](/) -> [ CDAT ](/cdat) -> [ Source Code ](/cdat/source)
-> [ API Reference ](/cdat/source/api-reference) -> Python: module
browser.gui_functions

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

        * [ Python: module browser.gui_functions ](/cdat/source/api-reference/browser.gui_functions.html)

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

  * [ ![Send this page to somebody](media/mail_icon.gif) ](/cdat/source/api-reference/browser.gui_functions.html/sendto_form)
  * [ ![Print this page](media/print_icon.gif) ](/this.print\(\))

#  Python: module browser.gui_functions

  
  
 [ browser  ](/browser.html) .gui_functions 
[ index ](/)  

` #&#160;The&#160;PCMDI&#160;Data&#160;Browser&#160;Miscellaneous&#160;Functions&#160;-&#160;&#160;gui_functions&#160;module  
#  
##############################################################################
#  
#
#  
#&#160;Module:&#160;&#160;&#160;&#160;&#160;&#160;&#160;gui_functions&#160;module
#  
#
#  
#&#160;Copyright:&#160;&#160;&#160;&#160;"See&#160;file&#160;Legal.htm&#160;for&#160;copyright&#160;information."
#  
#
#  
#&#160;Authors:&#160;&#160;&#160;&#160;&#160;&#160;PCMDI&#160;Software&#160;Team
#  
#&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;Lawrence&#160;Livermore&#160;NationalLaboratory:
#  
#&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;support@pcmdi.llnl.gov
#  
#
#  
#&#160;Description:&#160;&#160;PCMDI&#160;Software&#160;System&#160;Browser&#160;miscellaneous&#160;GUI&#160;functions.
#  
#
#  
#&#160;Version:&#160;&#160;&#160;&#160;&#160;&#160;4.0
#  
#
#  
##############################################################################
#  
#  
#---------------------------------------------------------------------  
#&#160;NOTE:&#160;need&#160;to&#160;use&#160;version&#160;of&#160;Python&#160;that&#160;imports&#160;Tkinter&#160;and&#160;Pmw  
#--------------------------------------------------------------------- `

  
 Modules 

` `

[ Numeric ](/Numeric.html)  
[ Tkinter ](/Tkinter.html)  
[ __main__ ](/__main__.html)  
[ cdms ](/cdms.html)  
[ cdtime ](/cdtime.html)  
[ copy ](/copy.html)  

[ copy_reg ](/copy_reg.html)  
[ gui_support.gui_color ](/gui_support.gui_color.html)  
[ browser.gui_control ](/browser.gui_control.html)  
[ browser.gui_defined_variables ](/browser.gui_defined_variables.html)  
[ browser.gui_message ](/browser.gui_message.html)  
[ browser.gui_reset ](/browser.gui_reset.html)  

[ math ](/math.html)  
[ multiarray ](/multiarray.html)  
[ os ](/os.html)  
[ vcs.pagegui ](/vcs.pagegui.html)  
[ pickle ](/pickle.html)  
[ string ](/string.html)  

[ sys ](/sys.html)  
[ types ](/types.html)  
[ vcs ](/vcs.html)  

  
 Classes 

` `

[ generate_labels_list ](/browser.gui_functions.html)

[ replace_axis_values ](/browser.gui_functions.html)

  
class  generate_labels_list 

` `

Methods defined here:  

 __init__  (self, parent, dim_index, axis) 

 generatelist  (self, button) 

  
class  replace_axis_values 

` `

Methods defined here:  

 __init__  (self, parent, dim_index, replace_type  =None  ) 

 evt_replace_axis_values  (self, parent, dim_index, replace_type, result) 

  
 Functions 

` `

 arange  (...) 
     ` [ arange ](/) (start,&#160;stop=None,&#160;step=1,&#160;typecode=None)   
  
Just&#160;like&#160;range()&#160;except&#160;it&#160;returns&#160;an&#160;array&#160;whose&#160;type&#160;can&#160;be  
specified&#160;by&#160;the&#160;keyword&#160;argument&#160;typecode. `

 array  (...) 
     ` [ array ](/) (sequence,&#160;typecode=None,&#160;copy=1,&#160;savespace=0)&#160;will&#160;return&#160;a&#160;new&#160;array&#160;formed&#160;from&#160;the&#160;given&#160;(potentially&#160;nested)&#160;sequence&#160;with&#160;type&#160;given&#160;by&#160;typecode.&#160;&#160;If&#160;no&#160;typecode&#160;is&#160;given,&#160;then&#160;the&#160;type&#160;will&#160;be&#160;determined&#160;as&#160;the&#160;minimum&#160;type&#160;required&#160;to&#160;hold&#160;the&#160;objects&#160;in&#160;sequence.&#160;&#160;If&#160;copy&#160;is&#160;zero&#160;and&#160;sequence&#160;is&#160;already&#160;an&#160;array,&#160;a&#160;reference&#160;will&#160;be&#160;returned.&#160;&#160;If&#160;savespace&#160;is&#160;nonzero,&#160;the&#160;new&#160;array&#160;will&#160;maintain&#160;its&#160;precision&#160;in&#160;operations. `

 arrayrange  = arange(...) 
     ` [ arange ](/) (start,&#160;stop=None,&#160;step=1,&#160;typecode=None)   
  
Just&#160;like&#160;range()&#160;except&#160;it&#160;returns&#160;an&#160;array&#160;whose&#160;type&#160;can&#160;be  
specified&#160;by&#160;the&#160;keyword&#160;argument&#160;typecode. `

 choose  (...) 
     ` [ choose ](/) (a,&#160;(b1,b2,...)) `

 cross_correlate  (...) 
     ` [ cross_correlate ](/) (a,v,&#160;mode=0) `

 evt_menu_index  (parent, dim_index, called_from) 

 evt_menu_raw  (parent, dim_index) 

 evt_transpose_dimensions  (index, dim_name, t_index, t_dim_name, parent) 
     ` #-----------------------------------------------------------------------------------   
#&#160;Transpose&#160;two&#160;dimensions  
#-----------------------------------------------------------------------------
------ `

 fromstring  (...) 
     ` [ fromstring ](/) (string,&#160;typecode='l',&#160;count=-1)&#160;returns&#160;a&#160;new&#160;1d&#160;array&#160;initialized&#160;from&#160;the&#160;raw&#160;binary&#160;data&#160;in&#160;string.&#160;&#160;If&#160;count&#160;is&#160;positive,&#160;the&#160;new&#160;array&#160;will&#160;have&#160;count&#160;elements,&#160;otherwise&#160;it's&#160;size&#160;is&#160;determined&#160;by&#160;the&#160;size&#160;of&#160;string. `

 get_available_printers  () 
     ` #------------------------------------------------------------------------   
#&#160;Return&#160;the&#160;list&#160;of&#160;available&#160;printers.&#160;Printer&#160;names&#160;should&#160;be&#160;located  
#&#160;in&#160;the&#160;user's&#160;$HOME/PCMDI_GRAPHICS/HARD_COPY&#160;file  
#------------------------------------------------------------------------ `

 get_axis_values  (parent, dim_index) 

 get_axis_weight_values  (parent, dim_index) 

 get_dimension_selections  (Csrl, Cpts) 
     ` #-----------------------------------------------------------------------------------   
#&#160;Select&#160;the&#160;first&#160;and&#160;last&#160;dimension&#160;values&#160;\--&#160;Will&#160;also&#160;highlight&#160;the
dimension's  
#&#160;new&#160;range  
#-----------------------------------------------------------------------------
------ `

 reshape  (...) 
     ` [ reshape ](/) (a,&#160;(d1,&#160;d2,&#160;...,&#160;dn)).&#160;&#160;Change&#160;the&#160;shape&#160;of&#160;a&#160;to&#160;be&#160;an&#160;n-dimensional&#160;array&#160;with&#160;dimensions&#160;given&#160;by&#160;d1...dn.&#160;&#160;Note:&#160;the&#160;size&#160;specified&#160;for&#160;the&#160;new&#160;array&#160;must&#160;be&#160;exactly&#160;equal&#160;to&#160;the&#160;size&#160;of&#160;the&#160;&#160;old&#160;one&#160;or&#160;an&#160;error&#160;will&#160;occur. `

 return_axis_size  (parent, dim_index) 

 return_latitude_region_values  (region) 

 return_longitude_region_values  (region) 

 searchsorted  = binarysearch(...) 
     ` binarysearch(a,v) `

 set_lat_lon  (parent, R0, R1) 

 set_region_index_values  (parent, dim_name, region, dim_index) 

 take  (...) 
     ` [ take ](/) (a,&#160;indices,&#160;axis=0).&#160;&#160;Selects&#160;the&#160;elements&#160;in&#160;indices&#160;from&#160;array&#160;a&#160;along&#160;the&#160;given&#160;axis. `

 zeros  (...) 
     ` [ zeros ](/) ((d1,...,dn),typecode='l',savespace=0)&#160;will&#160;return&#160;a&#160;new&#160;array&#160;of&#160;shape&#160;(d1,...,dn)&#160;and&#160;type&#160;typecode&#160;with&#160;all&#160;it's&#160;entries&#160;initialized&#160;to&#160;zero.&#160;&#160;If&#160;savespace&#160;is&#160;nonzero&#160;the&#160;array&#160;will&#160;be&#160;a&#160;spacesaver&#160;array. `

  
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
 LittleEndian  = True   
 NewAxis  = None   
 Pmw  = <Pmw.Pmw_1_2.lib.PmwLoader.PmwLoader instance>   
 PyObject  = 'O'   
 UInt  = 'u'   
 UInt16  = 'w'   
 UInt32  = 'u'   
 UInt8  = 'b'   
 UnsignedInt16  = 'w'   
 UnsignedInt32  = 'u'   
 UnsignedInt8  = 'b'   
 UnsignedInteger  = 'u'   
 absolute  = <ufunc 'absolute'>   
 add  = <ufunc 'add'>   
 arccos  = <ufunc 'arccos'>   
 arccosh  = <ufunc 'arccosh'>   
 arcsin  = <ufunc 'arcsin'>   
 arcsinh  = <ufunc 'arcsinh'>   
 arctan  = <ufunc 'arctan'>   
 arctan2  = <ufunc 'arctan2'>   
 arctanh  = <ufunc 'arctanh'>   
 bitwise_and  = <ufunc 'bitwise_and'>   
 bitwise_or  = <ufunc 'bitwise_or'>   
 bitwise_xor  = <ufunc 'bitwise_xor'>   
 ceil  = <ufunc 'ceil'>   
 conjugate  = <ufunc 'conjugate'>   
 cos  = <ufunc 'cos'>   
 cosh  = <ufunc 'cosh'>   
 divide  = <ufunc 'divide'>   
 divide_safe  = <ufunc 'divide_safe'>   
 e  = 2.7182818284590451   
 equal  = <ufunc 'equal'>   
 exp  = <ufunc 'exp'>   
 fabs  = <ufunc 'fabs'>   
 floor  = <ufunc 'floor'>   
 floor_divide  = <ufunc 'floor_divide'>   
 fmod  = <ufunc 'fmod'>   
 greater  = <ufunc 'greater'>   
 greater_equal  = <ufunc 'greater_equal'>   
 hypot  = <ufunc 'hypot'>   
 invert  = <ufunc 'invert'>   
 left_shift  = <ufunc 'left_shift'>   
 less  = <ufunc 'less'>   
 less_equal  = <ufunc 'less_equal'>   
 log  = <ufunc 'log'>   
 log10  = <ufunc 'log10'>   
 logical_and  = <ufunc 'logical_and'>   
 logical_not  = <ufunc 'logical_not'>   
 logical_or  = <ufunc 'logical_or'>   
 logical_xor  = <ufunc 'logical_xor'>   
 maximum  = <ufunc 'maximum'>   
 minimum  = <ufunc 'minimum'>   
 multiply  = <ufunc 'multiply'>   
 negative  = <ufunc 'negative'>   
 not_equal  = <ufunc 'not_equal'>   
 pi  = 3.1415926535897931   
 power  = <ufunc 'power'>   
 remainder  = <ufunc 'remainder'>   
 right_shift  = <ufunc 'right_shift'>   
 sin  = <ufunc 'sin'>   
 sinh  = <ufunc 'sinh'>   
 sqrt  = <ufunc 'sqrt'>   
 subtract  = <ufunc 'subtract'>   
 tan  = <ufunc 'tan'>   
 tanh  = <ufunc 'tanh'>   
 true_divide  = <ufunc 'true_divide'>   
 typecodes  = {'Character': 'c', 'Complex': 'FD', 'Float': 'fd', 'Integer': '1sil', 'UnsignedInteger': 'bwu'} 

* * *

UCRL-WEB-213937 | [ Privacy & Legal Notice ](/disclaimer.html)

[ webmaster@pcmdi.llnl.gov ](/webmaster@pcmdi.llnl.gov)

[ ![Powered by Plone](media/plone_powered.gif) ](/)

