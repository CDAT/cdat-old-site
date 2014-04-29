---
layout: default
title:
---

 [ Skip to content. ](/cdat/source/api-
reference/browser.gui_defined_variables.html) | [ Skip to navigation
](/cdat/source/api-reference/browser.gui_defined_variables.html)

Search Site

[ Advanced Search&#8230; ](/search_form)

#  [ PCMDI Software Portal ](/)

#####  Sections

  * [ Home ](/)

#####  Personal tools

  * [ Log in ](/login_form)

You are here:  [ Home ](/) -> [ CDAT ](/cdat) -> [ Source Code ](/cdat/source)
-> [ API Reference ](/cdat/source/api-reference) -> Python: module
browser.gui_defined_variables

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

        * [ Python: module browser.gui_defined_variables ](/cdat/source/api-reference/browser.gui_defined_variables.html)

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

  * [ ![Send this page to somebody](media/mail_icon.gif) ](/cdat/source/api-reference/browser.gui_defined_variables.html/sendto_form)
  * [ ![Print this page](media/print_icon.gif) ](/this.print\(\))

#  Python: module browser.gui_defined_variables

  
  
 [ browser  ](/browser.html) .gui_defined_variables 
[ index ](/)  

` #&#160;The&#160;PCMDI&#160;Data&#160;Browser&#160;Defined&#160;Variables&#160;Panel&#160;-&#160;&#160;gui_defined_variables
module  
#  
##############################################################################
#  
#
#  
#&#160;Module:&#160;&#160;&#160;&#160;&#160;&#160;&#160;gui_defined_variables&#160;module
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
#&#160;Description:&#160;&#160;PCMDI&#160;Software&#160;System&#160;browser&#160;Tkinter&#160;"Defined&#160;Variables"
#  
#&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;panel&#160;GUI.
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

[ cdms.MV ](/cdms.MV.html)  
[ Numeric ](/Numeric.html)  
[ Tkinter ](/Tkinter.html)  
[ __main__ ](/__main__.html)  
[ cdms ](/cdms.html)  
[ genutil ](/genutil.html)  

[ browser.gui_alter_variable ](/browser.gui_alter_variable.html)  
[ gui_support.gui_color ](/gui_support.gui_color.html)  
[ browser.gui_control ](/browser.gui_control.html)  
[ browser.gui_expression ](/browser.gui_expression.html)  
[ browser.gui_functions ](/browser.gui_functions.html)  
[ browser.gui_menu ](/browser.gui_menu.html)  

[ browser.gui_message ](/browser.gui_message.html)  
[ browser.gui_output ](/browser.gui_output.html)  
[ browser.gui_reset ](/browser.gui_reset.html)  
[ browser.gui_user_menus ](/browser.gui_user_menus.html)  
[ browser.gui_writenetcdf ](/browser.gui_writenetcdf.html)  
[ os ](/os.html)  

[ string ](/string.html)  
[ sys ](/sys.html)  
[ time ](/time.html)  
[ tkFileDialog ](/tkFileDialog.html)  
[ types ](/types.html)  
[ browser.vcs_function ](/browser.vcs_function.html)  

  
 Classes 

` `

[ create ](/browser.gui_defined_variables.html)

[ update_defined ](/browser.gui_defined_variables.html)

  
class  create 

` `

` #---------------------------------------------------------------------------  
#  
#&#160;Start&#160;of&#160;the&#160;"Defined&#160;Variables"&#160;panel&#160;GUI&#160;Layout  
#  
#---------------------------------------------------------------------------  
#&#160;Start&#160;the&#160;Tkinter/Pmw&#160;GUI&#160;layout.&#160;The&#160;layout&#160;is&#160;listed&#160;from&#160;top&#160;to&#160;bottom.  
#&#160;Starting&#160;with:&#160;the&#160;menu&#160;bar;&#160;followed&#160;by&#160;the&#160;"Select&#160;Variable"&#160;panel,&#160;which  
#&#160;allows&#160;the&#160;user&#160;to&#160;select&#160;data&#160;from&#160;a&#160;directory&#160;or&#160;a&#160;database;&#160;followed&#160;by  
#&#160;the&#160;"Graphics&#160;Control"&#160;panel,&#160;which&#160;allows&#160;the&#160;user&#160;to&#160;plot&#160;the&#160;selected&#160;or  
#&#160;defined&#160;variables;&#160;followed&#160;by&#160;the&#160;"Dimension"&#160;panel,&#160;which&#160;allows&#160;the&#160;user
to  
#&#160;select&#160;subsets&#160;of&#160;the&#160;selected&#160;variable&#160;before&#160;plotting&#160;or&#160;storing&#160;into
memory;  
#&#160;followed&#160;by&#160;the&#160;"Defined&#160;Variables"&#160;panel,&#160;which&#160;allows&#160;the&#160;user&#160;to&#160;modify
the  
#&#160;variables&#160;that&#160;are&#160;stored&#160;in&#160;memory;&#160;and&#160;finally&#160;followed&#160;by&#160;the&#160;"Variable  
#&#160;Information"&#160;scroll&#160;window,&#160;which&#160;displays&#160;variable&#160;information.  
#  
#&#160;All&#160;panels&#160;are&#160;contained&#160;within&#160;a&#160;paned&#160;widget.&#160;Thus,&#160;allowing&#160;the&#160;size&#160;of  
#&#160;each&#160;section&#160;to&#160;expand&#160;or&#160;constrict.  
#  
#---------------------------------------------------------------------  
#&#160;Begin&#160;the&#160;creation&#160;of&#160;"Defined&#160;Variables"&#160;panel  
#---------------------------------------------------------------------  
`

Methods defined here:  

 __init__  (self, parent) 

 alterpaneDV  (self, parent, event  =None  ) 
     ` ##&#160;Function&#160;to&#160;resize&#160;the&#160;scrolled&#160;box&#160;when&#160;the&#160;panel&#160;changes `

 copy_graphics_method  (self, parent) 
     ` #######&#160;event&#160;to&#160;copy&#160;the&#160;graphics&#160;method `

 copy_template  (self, parent) 
     ` #######&#160;event&#160;to&#160;copy&#160;template `

 edit_graphics_method  (self, parent) 
     ` #######&#160;event&#160;to&#160;edit&#160;the&#160;graphics&#160;method `

 edit_template  (self, parent) 
     ` #######&#160;event&#160;to&#160;bring&#160;up&#160;the&#160;template&#160;editor `

 evt_call_gui_alter_variable  (self, parent, event) 
     ` #######&#160;event&#160;to&#160;call&#160;the&#160;gui_alter_variable&#160;popup `

 evt_call_gui_writenetcdf  (self, parent, event) 
     ` #######&#160;event&#160;to&#160;call&#160;the&#160;writenetCDF&#160;popup `

 evt_change_command_color  (self, parent, event) 
     ` #######&#160;event&#160;to&#160;change&#160;the&#160;command&#160;line&#160;expression&#160;color `

 evt_compute_command  (self, parent, event) 
     ` #######&#160;event&#160;to&#160;call&#160;the&#160;command&#160;line&#160;calculator&#160;expression `

 evt_dispose_defined_variables  (self, parent, event) 
     ` #######&#160;event&#160;to&#160;dispose&#160;of&#160;unwanted&#160;variables `

 evt_dispose_execute  (self, parent, var_names, result) 

 evt_do_operation  (self, parent, type, event) 

 evt_expression_widget  (self, parent, event) 

 evt_info_on_defined  (self, parent, event) 
     ` #######&#160;event&#160;to&#160;return&#160;information&#160;on&#160;the&#160;defined&#160;variables `

 evt_log_on_defined  (self, parent, event) 
     ` #######&#160;event&#160;to&#160;return&#160;information&#160;on&#160;the&#160;defined&#160;variables `

 evt_remove_all_defined  (self, parent, event) 
     ` #######&#160;event&#160;to&#160;remove&#160;all&#160;the&#160;defined `

 evt_remove_selected_defined  (self, parent, var_name, event) 
     ` #######&#160;event&#160;to&#160;remove&#160;the&#160;selected&#160;defined `

 evt_select_graphics_method  (self, gm_name, parent) 
     ` #######&#160;event&#160;to&#160;select&#160;the&#160;graphics&#160;method `

 evt_selected_defined_variable  (self, parent, event) 

 evt_selected_defined_variable2  (self, parent, event) 

 evt_selected_defined_variable3  (self, parent, control_key  =0  ) 

 evt_selected_trash_variable  (self, parent) 

 evt_set_mode_operation  (self, parent, event) 

 evt_show_defined_variables_tools  (self, parent, event) 
     ` #######&#160;event&#160;to&#160;call&#160;the&#160;gui_alter_variable&#160;popup `

 evt_show_template_graphics_method  (self, parent, event) 
     ` #######&#160;event&#160;to&#160;call&#160;the&#160;gui_alter_variable&#160;popup `

 evt_toggle_DV_selection_mode  (self, parent) 
     ` #-----------------------------------------------------------------   
#&#160;event&#160;functions&#160;associated&#160;with&#160;the&#160;"Defined&#160;Variable"&#160;panel&#160;buttons  
#-----------------------------------------------------------------  
#  
#######&#160;event&#160;to&#160;toggle&#160;the&#160;Defined&#160;Variable&#160;window&#160;selection&#160;mode `

 mode_1_operation  (self, parent, type, event) 

 mode_2_operation  (self, parent, type, event) 

 redisplay_graphics_method  (self, parent) 
     ` #######&#160;event&#160;to&#160;redisplay&#160;the&#160;graphics&#160;method&#160;list `

 redisplay_template  (self, parent) 
     ` #######&#160;event&#160;to&#160;redisplay&#160;the&#160;template&#160;list `

 remove_graphics_method  (self, parent) 
     ` #######&#160;event&#160;to&#160;remove&#160;the&#160;graphics&#160;method `

 remove_template  (self, parent) 
     ` #######&#160;event&#160;to&#160;remove&#160;template `

 rename_graphics_method  (self, parent) 
     ` #######&#160;event&#160;to&#160;rename&#160;the&#160;graphics&#160;method `

 rename_template  (self, parent) 
     ` #######&#160;event&#160;to&#160;rename&#160;template `

 return_trash_can_list  (self, parent) 

 script_graphics_method  (self, parent) 
     ` #######&#160;event&#160;to&#160;script&#160;the&#160;graphics&#160;method `

 script_template  (self, parent) 
     ` #######&#160;event&#160;to&#160;save&#160;template&#160;to&#160;a&#160;script&#160;file `

 select_gm  (self) 
     ` #######&#160;event&#160;to&#160;select&#160;the&#160;desired&#160;graphics&#160;method `

 select_template  (self) 
     ` #######&#160;event&#160;to&#160;select&#160;the&#160;desired&#160;template `

 update_page_layout  (self, parent, remove_list) 
     ` #######&#160;event&#160;to&#160;remove&#160;the&#160;selected&#160;defined `

  
class  update_defined 

` `

Methods defined here:  

 __init__  (parent, *args) 

  
 Functions 

` `

 get_vars  () 
     ` #&#160;Return&#160;a&#160;list&#160;of&#160;all&#160;selected&#160;variables&#160;in&#160;the&#160;order&#160;in   
#&#160;&#160;which&#160;they&#160;were&#160;selected `

 selected_updated  (args  =()  ) 
     ` #-----------------------------------------------------------------------------------   
#&#160;In&#160;the&#160;selected&#160;panel&#160;the&#160;user&#160;will&#160;need&#160;to&#160;get&#160;all&#160;the&#160;changes&#160;coming&#160;from
the  
#&#160;[&#160;idle&#160;]&#160;Shell&#160;window.&#160;This&#160;function&#160;will&#160;update&#160;the&#160;selected&#160;window&#160;with
the  
#&#160;new&#160;or&#160;removed&#160;TransientVariable&#160;(i.e.,&#160;MV),&#160;MA,&#160;or&#160;Numeric&#160;arrays.  
#-----------------------------------------------------------------------------
------ `

 update_defined_variable_list  (parent) 

  
 Data 

` `

 Pmw  = <Pmw.Pmw_1_2.lib.PmwLoader.PmwLoader instance>   
 fn  = '/pcmdi/halliday1/PCMDI_GRAPHICS'   
 graphics_method_list  = ['Boxfill', 'Isofill', 'Isoline', 'Meshfill', 'Outfill', 'Outline', 'Scatter', 'Taylordiagram', 'Vector', 'XvsY', 'Xyvsy', 'Yxvsx']   
 trash_store  = '__trashed_on__'   
 trash_str  = '_waiting_for_user_to_dispose_of_via_trash_can' 

* * *

UCRL-WEB-213937 | [ Privacy & Legal Notice ](/disclaimer.html)

[ webmaster@pcmdi.llnl.gov ](/webmaster@pcmdi.llnl.gov)

[ ![Powered by Plone](media/plone_powered.gif) ](/)

