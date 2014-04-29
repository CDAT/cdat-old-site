---
layout: default
title:
---

 [ Skip to content. ](/cdat/source/api-reference/browser.gui_extend_menus.html)
| [ Skip to navigation ](/cdat/source/api-
reference/browser.gui_extend_menus.html)

Search Site

[ Advanced Search&#8230; ](/search_form)

#  [ PCMDI Software Portal ](/)

#####  Sections

  * [ Home ](/)

#####  Personal tools

  * [ Log in ](/login_form)

You are here:  [ Home ](/) -> [ CDAT ](/cdat) -> [ Source Code ](/cdat/source)
-> [ API Reference ](/cdat/source/api-reference) -> Python: module
browser.gui_extend_menus

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

        * [ Python: module browser.gui_extend_menus ](/cdat/source/api-reference/browser.gui_extend_menus.html)

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

  * [ ![Send this page to somebody](media/mail_icon.gif) ](/cdat/source/api-reference/browser.gui_extend_menus.html/sendto_form)
  * [ ![Print this page](media/print_icon.gif) ](/this.print\(\))

#  Python: module browser.gui_extend_menus

  
  
 [ browser  ](/browser.html) .gui_extend_menus 
[ index ](/)  

` #&#160;The&#160;PCMDI&#160;Data&#160;Browser&#160;Extend&#160;Toplevel&#160;Menus&#160;-&#160;&#160;gui_extend_menus&#160;module  
#  
##############################################################################
###  
#
#  
#&#160;Module:&#160;&#160;&#160;&#160;&#160;&#160;&#160;gui_extend_menus&#160;module
#  
#
#  
#&#160;Copyright:&#160;&#160;&#160;&#160;"See&#160;file&#160;Legal.htm&#160;for&#160;copyright&#160;information."
#  
#
#  
#&#160;Authors:&#160;&#160;&#160;&#160;&#160;&#160;PCMDI&#160;Software&#160;Team
#  
#&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;Lawrence&#160;Livermore&#160;National&#160;Laboratory:
#  
#&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;support@pcmdi.llnl.gov
#  
#
#  
#&#160;Description:&#160;&#160;PCMDI&#160;Software&#160;System&#160;browser&#160;Extend&#160;Toplevel&#160;Menus.
#  
#
#  
#&#160;Version:&#160;&#160;&#160;&#160;&#160;&#160;4.0
#  
#
#  
##############################################################################
###  
#  
#---------------------------------------------------------------------  
#&#160;NOTE:&#160;need&#160;to&#160;use&#160;version&#160;of&#160;Python&#160;that&#160;imports&#160;Tkinter&#160;and&#160;Pmw  
#--------------------------------------------------------------------- `

  
 Modules 

` `

[ Tkinter ](/Tkinter.html)  
[ __main__ ](/__main__.html)  
[ gui_support.gui_color ](/gui_support.gui_color.html)  
[ browser.gui_control ](/browser.gui_control.html)  

[ browser.gui_defined_variables ](/browser.gui_defined_variables.html)  
[ browser.gui_message ](/browser.gui_message.html)  
[ browser.gui_saved_settings ](/browser.gui_saved_settings.html)  
[ browser.gui_select_variable ](/browser.gui_select_variable.html)  

[ os ](/os.html)  
[ string ](/string.html)  
[ sys ](/sys.html)  
[ tkFileDialog ](/tkFileDialog.html)  

[ types ](/types.html)  

  
 Classes 

` `

[ create ](/browser.gui_extend_menus.html)

  
class  create 

` `

` #---------------------------------------------------------------------  
#  
#&#160;Start&#160;of&#160;Popup&#160;Dialog  
#  
#---------------------------------------------------------------------------  
#&#160;Extend&#160;Toplevel&#160;Menus&#160;Dialog&#160;Popup  
#---------------------------------------------------------------------------  
`

Methods defined here:  

 __init__  (self, parent) 

 add_function  (self, parent, evt  =None  ) 
     ` #---------------------------------------------   
#&#160;Add&#160;a&#160;function&#160;to&#160;a&#160;pre-existing&#160;menu&#160;from&#160;the&#160;main&#160;menu&#160;bar  
#--------------------------------------------- `

 add_top_menu  (self, parent, evt  =None  ) 
     ` #---------------------------------------------   
#&#160;Add&#160;a&#160;new&#160;menu&#160;to&#160;the&#160;main&#160;menu&#160;bar  
#--------------------------------------------- `

 browse_files  (self, parent) 
     ` #---------------------------------------------   
#&#160;Open&#160;a&#160;tkFileDialog&#160;window&#160;and&#160;get&#160;filename&#160;from&#160;user  
#--------------------------------------------- `

 change_description  (self, parent, evt  =None  ) 
     ` #---------------------------------------------   
#&#160;Change&#160;menu&#160;description  
#--------------------------------------------- `

 clear_top  (self, parent) 
     ` #---------------------------------------------   
#&#160;Clear&#160;"Menu&#160;name"&#160;and&#160;"Description"&#160;from&#160;the&#160;"Create&#160;user&#160;menu"&#160;window  
#--------------------------------------------- `

 del_top_menu  (self, parent) 
     ` #---------------------------------------------   
#&#160;Remove&#160;a&#160;menu&#160;from&#160;the&#160;main&#160;menu&#160;bar  
#--------------------------------------------- `

 delete_function  (self, parent) 
     ` #---------------------------------------------   
#&#160;Delete&#160;a&#160;function&#160;from&#160;the&#160;main&#160;menu&#160;bar  
#--------------------------------------------- `

 do_nothing  (self, result) 
     ` #--------------------------------------------------------------   
#&#160;Use&#160;this&#160;function&#160;to&#160;"lock"&#160;a&#160;field&#160;(bind&#160;<KeyPress>&#160;to&#160;do_nothing)  
#-------------------------------------------------------------- `

 file_or_import  (self, parent, result) 
     ` #---------------------------------------------   
#&#160;Toggle&#160;between&#160;file&#160;and&#160;import&#160;mode.&#160;&#160;Change&#160;the&#160;appearance&#160;of  
#&#160;&#160;group2&#160;and&#160;group2a&#160;appropriately  
#--------------------------------------------- `

 get_functions  (self, result  =None  ) 
     ` #--------------------------------------------------------------   
#&#160;Get&#160;functions&#160;from&#160;file&#160;or&#160;import&#160;and&#160;populate&#160;the&#160;function  
#&#160;&#160;pull&#160;down&#160;menu  
#-------------------------------------------------------------- `

 import_functions  (self) 
     ` #---------------------------------------------   
#&#160;Get&#160;functions&#160;from&#160;an&#160;import  
#--------------------------------------------- `

 populate_group2  (self, result) 
     ` #---------------------------------------------   
#&#160;When&#160;user&#160;selects&#160;a&#160;menu&#160;name&#160;from&#160;the&#160;"Modify&#160;user&#160;menu"&#160;window,  
#&#160;&#160;populate&#160;all&#160;appropriate&#160;fields&#160;with&#160;current&#160;menu&#160;information  
#--------------------------------------------- `

 rename  (self, evt  =None  ) 
     ` #---------------------------------------------   
#&#160;Rename&#160;a&#160;function  
#--------------------------------------------- `

 select_function  (self, parent) 
     ` #---------------------------------------------   
#&#160;Change&#160;the&#160;value&#160;of&#160;"Function&#160;name"&#160;field&#160;to&#160;value&#160;of&#160;"Function"  
#--------------------------------------------- `

  
 Functions 

` `

 find_modules  () 
     ` #---------------------------------------------------------------------   
#&#160;Return&#160;the&#160;Modules&#160;that&#160;have&#160;been&#160;imported  
#--------------------------------------------------------------------- `

 find_py_files  (parent) 
     ` #---------------------------------------------------------------------   
#&#160;Find&#160;the&#160;py&#160;files&#160;in&#160;the&#160;directory  
#--------------------------------------------------------------------- `

 restore_menus  (parent) 
     ` #---------------------------------------------------------------------   
#&#160;Restore&#160;Menus&#160;in&#160;the&#160;Main&#160;Menu&#160;Bar  
#--------------------------------------------------------------------- `

 returned_functions_and_instances  (self) 
     ` #---------------------------------------------------------------------   
#&#160;Return&#160;the&#160;Module's&#160;function&#160;list  
#--------------------------------------------------------------------- `

 wrap_balloon_help  (contents, max_width  =None  ) 
     ` #&#160;Make&#160;formatting&#160;of&#160;help&#160;balloons&#160;easier `

  
 Data 

` `

 Pmw  = <Pmw.Pmw_1_2.lib.PmwLoader.PmwLoader instance>   
 fn  = '/pcmdi/halliday1/PCMDI_GRAPHICS'   
 l_menu  = [] 

* * *

UCRL-WEB-213937 | [ Privacy & Legal Notice ](/disclaimer.html)

[ webmaster@pcmdi.llnl.gov ](/webmaster@pcmdi.llnl.gov)

[ ![Powered by Plone](media/plone_powered.gif) ](/)

