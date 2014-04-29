---
layout: default
title:
---

 [ Skip to content. ](/cdat/source/api-reference/browser.gui_menu.html) | [
Skip to navigation ](/cdat/source/api-reference/browser.gui_menu.html)

Search Site

[ Advanced Search&#8230; ](/search_form)

#  [ PCMDI Software Portal ](/)

#####  Sections

  * [ Home ](/)

#####  Personal tools

  * [ Log in ](/login_form)

You are here:  [ Home ](/) -> [ CDAT ](/cdat) -> [ Source Code ](/cdat/source)
-> [ API Reference ](/cdat/source/api-reference) -> Python: module
browser.gui_menu

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

        * [ Python: module browser.gui_menu ](/cdat/source/api-reference/browser.gui_menu.html)

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

  * [ ![Send this page to somebody](media/mail_icon.gif) ](/cdat/source/api-reference/browser.gui_menu.html/sendto_form)
  * [ ![Print this page](media/print_icon.gif) ](/this.print\(\))

#  Python: module browser.gui_menu

  
  
 [ browser  ](/browser.html) .gui_menu 
[ index ](/)  

` #&#160;The&#160;PCMDI&#160;Data&#160;Browser&#160;Menu&#160;Bar&#160;-&#160;&#160;gui_menu&#160;module  
#  
##############################################################################
#  
#
#  
#&#160;Module:&#160;&#160;&#160;&#160;&#160;&#160;&#160;gui_menu&#160;module
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
#&#160;Description:&#160;&#160;PCMDI&#160;Software&#160;System&#160;browser&#160;Tkinter&#160;Main&#160;Menu&#160;Bar.
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

[ Tkinter ](/Tkinter.html)  
[ __main__ ](/__main__.html)  
[ cdutil ](/cdutil.html)  
[ genutil ](/genutil.html)  
[ browser.gui_about ](/browser.gui_about.html)  
[ browser.gui_ascii ](/browser.gui_ascii.html)  
[ browser.gui_ascii_cols ](/browser.gui_ascii_cols.html)  
[ browser.gui_bounds_question ](/browser.gui_bounds_question.html)  

[ browser.gui_busy ](/browser.gui_busy.html)  
[ gui_support.gui_color ](/gui_support.gui_color.html)  
[ browser.gui_control ](/browser.gui_control.html)  
[ browser.gui_defined_variables ](/browser.gui_defined_variables.html)  
[ browser.gui_edit_list ](/browser.gui_edit_list.html)  
[ browser.gui_extend_menus ](/browser.gui_extend_menus.html)  
[ browser.gui_filters_question ](/browser.gui_filters_question.html)  
[ browser.gui_formulate ](/browser.gui_formulate.html)  

[ browser.gui_functions ](/browser.gui_functions.html)  
[ browser.gui_message ](/browser.gui_message.html)  
[ browser.gui_output ](/browser.gui_output.html)  
[ browser.gui_read_Struct ](/browser.gui_read_Struct.html)  
[ browser.gui_reset ](/browser.gui_reset.html)  
[ browser.gui_saved_settings ](/browser.gui_saved_settings.html)  
[ browser.gui_select_variable ](/browser.gui_select_variable.html)  
[ browser.gui_set_idle_font ](/browser.gui_set_idle_font.html)  

[ browser.gui_statistics_question ](/browser.gui_statistics_question.html)  
[ gui_support ](/gui_support.html)  
[ browser.gui_user_menus ](/browser.gui_user_menus.html)  
[ os ](/os.html)  
[ string ](/string.html)  
[ sys ](/sys.html)  
[ tkFileDialog ](/tkFileDialog.html)  
[ webbrowser ](/webbrowser.html)  

  
 Classes 

` `

[ create ](/browser.gui_menu.html)

[ create_file_menu ](/browser.gui_menu.html)

[ create_help_menu ](/browser.gui_menu.html)

[ create_options_menu ](/browser.gui_menu.html)

[ create_pcmdi_tools_menu ](/browser.gui_menu.html)

[ create_tools_menu ](/browser.gui_menu.html)

[ exit_browser ](/browser.gui_menu.html)

  
class  create 

` `

` #---------------------------------------------------------------------------
-------------  
#&#160;Begin&#160;the&#160;creation&#160;of&#160;the&#160;file&#160;menu&#160;and&#160;its&#160;menu&#160;items  
#-----------------------------------------------------------------------------
-----------  
`

Methods defined here:  

 __init__  (self, parent) 

  
class  create_file_menu 

` `

` #---------------------------------------------------------------------------
-------------  
#&#160;Begin&#160;the&#160;creation&#160;of&#160;the&#160;file&#160;menu&#160;and&#160;its&#160;menu&#160;items  
#-----------------------------------------------------------------------------
-----------  
`

Methods defined here:  

 __init__  (self, main_menu, parent) 

 evt_all_files  (self, parent) 
     ` #######&#160;event&#160;for&#160;seleting&#160;ALL&#160;data&#160;files `

 evt_cdml_files  (self, parent) 
     ` #######&#160;event&#160;for&#160;seleting&#160;CDML&#160;data&#160;files `

 evt_cdms_files  (self, parent) 
     ` #######&#160;event&#160;for&#160;seleting&#160;CDMS&#160;data&#160;files `

 evt_ctl_files  (self, parent) 
     ` #######&#160;event&#160;for&#160;seleting&#160;GrADS&#160;data&#160;files `

 evt_data_files  (self, parent) 
     ` #######&#160;event&#160;for&#160;seleting&#160;the&#160;PCMDI&#160;data&#160;files `

 evt_datasets_files  (self, parent) 
     ` #######&#160;event&#160;for&#160;seleting&#160;the&#160;Database&#160;data&#160;files `

 evt_dic_files  (self, parent) 
     ` #######&#160;event&#160;for&#160;seleting&#160;DRS&#160;data&#160;files `

 evt_find_files  (self, parent) 
     ` #######&#160;event&#160;for&#160;seleting&#160;Pattern&#160;files `

 evt_hdf_files  (self, parent) 

 evt_nc_files  (self, parent) 
     ` #######&#160;event&#160;for&#160;seleting&#160;netCDF&#160;data&#160;files `

 evt_open_file  (self, parent) 
     ` #---------------------------------------------------------------------------   
#&#160;Define&#160;event&#160;function's&#160;for&#160;"File"&#160;menu&#160;items  
#---------------------------------------------------------------------------  
#  
#  
#######&#160;event&#160;that&#160;will&#160;pop&#160;up&#160;the&#160;tkFile&#160;dialog&#160;and&#160;enter&#160;the&#160;directory&#160;and
file&#160;string  
#&#160;&#160;&#160;&#160;&#160;&#160;&#160;in&#160;the&#160;directory&#160;and&#160;file&#160;entry&#160;widgets `

 evt_read_script_file  (self, parent) 
     ` #######&#160;event&#160;to&#160;"Read&#160;Script&#160;File" `

 evt_returned_printers  (self, parent, printer_name) 
     ` #######&#160;event&#160;to&#160;plot&#160;VCS&#160;Canvas&#160;to&#160;desinated&#160;printer `

 evt_save_plot_to_cgm  (self, parent) 
     ` #######&#160;event&#160;to&#160;save&#160;"Plot"&#160;in&#160;a&#160;'CGM'&#160;file `

 evt_save_plot_to_eps  (self, parent) 
     ` #######&#160;event&#160;to&#160;save&#160;"Plot"&#160;in&#160;a&#160;'EPS'&#160;file `

 evt_save_plot_to_gif  (self, parent) 
     ` #######&#160;event&#160;to&#160;save&#160;"Plot"&#160;in&#160;a&#160;'GIF'&#160;file `

 evt_save_plot_to_postscript  (self, parent) 
     ` #######&#160;event&#160;to&#160;save&#160;"Plot"&#160;in&#160;a&#160;'Postscript'&#160;file `

 evt_save_state_of_System  (self, parent) 
     ` #######&#160;event&#160;to&#160;"Save&#160;the&#160;Current&#160;State&#160;of&#160;the&#160;System" `

 evt_save_state_of_VCS  (self, parent) 
     ` #######&#160;event&#160;to&#160;"Save&#160;the&#160;Current&#160;State&#160;of&#160;the&#160;VCS&#160;graphics&#160;System" `

 evt_specify_printer  (self, parent) 
     ` #######&#160;event&#160;to&#160;plot&#160;VCS&#160;Canvas&#160;to&#160;"Specified"&#160;printer `

 evt_xml_files  (self, parent) 
     ` #######&#160;event&#160;for&#160;seleting&#160;XML&#160;data&#160;files `

  
class  create_help_menu 

` `

` #---------------------------------------------------------------------------
-------------  
#&#160;Create&#160;the&#160;Help&#160;menu&#160;and&#160;its&#160;menu&#160;items  
#-----------------------------------------------------------------------------
-----------  
`

Methods defined here:  

 __init__  (self, main_menu, parent) 

 evt_cdat_las_web  (self) 
     ` #######&#160;event&#160;to&#160;bring&#160;up&#160;a&#160;web&#160;browser&#160;that&#160;is&#160;displaying&#160;the&#160;CDAT-LAS&#160;web&#160;page `

 evt_cdat_web  (self) 
     ` #----------------------------------------------------   
#&#160;Class&#160;"Help"&#160;events  
#----------------------------------------------------  
#  
#######&#160;event&#160;to&#160;bring&#160;up&#160;a&#160;web&#160;browser&#160;that&#160;is&#160;displaying&#160;the&#160;CDAT&#160;web&#160;page `

 evt_numpy_web  (self) 
     ` #######&#160;event&#160;to&#160;bring&#160;up&#160;a&#160;web&#160;browser&#160;that&#160;is&#160;displaying&#160;the&#160;Numeric&#160;web&#160;page `

 evt_pcmdi_web  (self) 
     ` #######&#160;event&#160;to&#160;bring&#160;up&#160;a&#160;web&#160;browser&#160;that&#160;is&#160;displaying&#160;the&#160;PCMDI&#160;web&#160;page `

 evt_python_web  (self) 
     ` #######&#160;event&#160;to&#160;bring&#160;up&#160;a&#160;web&#160;browser&#160;that&#160;is&#160;displaying&#160;the&#160;PCMDI&#160;Software&#160;web&#160;page `

  
class  create_options_menu 

` `

` #---------------------------------------------------------------------------
-------------  
#&#160;Create&#160;the&#160;Preferences&#160;menu&#160;and&#160;its&#160;menu&#160;items  
#-----------------------------------------------------------------------------
-----------  
`

Methods defined here:  

 __init__  (self, main_menu, parent, save_region, squeeze_dim_flg, fortran_order_flg, popup_window_settings_flg, view_axes_flg, view_bounds_weights_flg, meridian_flg, convert_to_MV_flg, show_exit_popup_flg) 

 evt_DV_single_selection_mode  (self, parent) 

 evt_color_intensity  (self, parent, color_intensity) 
     ` #----------------------------------------------------   
#&#160;Class&#160;"Preferences"&#160;events  
#----------------------------------------------------  
#  
#######&#160;event&#160;to&#160;set&#160;"Colormap&#160;Maximun&#160;Intensity&#160;Value" `

 evt_convert_to_MV_toggle  (self, parent) 
     ` #######&#160;event&#160;to&#160;set&#160;"Automatic&#160;Conversion&#160;of&#160;Numeric&#160;and&#160;MA&#160;arrays&#160;to&#160;MV" `

 evt_exit_popup_toggle  (self, parent) 
     ` #######&#160;event&#160;to&#160;set&#160;"Show&#160;Popup&#160;Window&#160;for&#160;Existing&#160;VCDAT" `

 evt_fortran_toggle  (self, parent) 
     ` #######&#160;event&#160;to&#160;set&#160;"Fortran&#160;Order" `

 evt_mode_of_operation  (self, parent, operation_mode) 
     ` #######&#160;event&#160;to&#160;set&#160;"Save&#160;Region&#160;Selection" `

 evt_popup_window_toggle  (self, parent) 
     ` #######&#160;event&#160;to&#160;set&#160;"Popup&#160;Window&#160;Defined&#160;Settings" `

 evt_reset_GUI_state  (self, parent) 
     ` #######&#160;event&#160;to&#160;"Reset&#160;GUI&#160;to&#160;its&#160;Initial&#160;State" `

 evt_reset_GUI_swap_space  (self, parent) 
     ` #######&#160;event&#160;to&#160;"Reset&#160;the&#160;GUI's&#160;Swap&#160;Space&#160;Size" `

 evt_save_GUI_settings  (self, parent) 
     ` #######&#160;event&#160;to&#160;"Save&#160;GUI&#160;Settings" `

 evt_save_GUI_state  (self, parent) 
     ` #######&#160;event&#160;to&#160;"Save&#160;GUI's&#160;Initial&#160;State" `

 evt_save_VCS_settings  (self, parent) 
     ` #######&#160;event&#160;to&#160;"Save&#160;VCS&#160;Settings" `

 evt_set_default_colormap  (self, parent) 
     ` #######&#160;event&#160;to&#160;"Reset&#160;the&#160;GUI's&#160;Swap&#160;Space&#160;Size" `

 evt_set_default_graphics_method  (self, parent) 
     ` #######&#160;event&#160;to&#160;"Reset&#160;the&#160;GUI's&#160;Swap&#160;Space&#160;Size" `

 evt_set_default_template  (self, parent) 
     ` #######&#160;event&#160;to&#160;"Reset&#160;the&#160;GUI's&#160;Swap&#160;Space&#160;Size" `

 evt_set_meridian_toggle  (self, parent, number) 
     ` #######&#160;event&#160;to&#160;set&#160;"Meridian&#160;Selection" `

 evt_set_region  (self, parent, region_type) 
     ` #######&#160;event&#160;to&#160;set&#160;"Save&#160;Region&#160;Selection" `

 evt_show_defined_var_tools  (self, parent) 

 evt_show_template_graphics_method_windows  (self, parent) 

 evt_squeeze_dim_toggle  (self, parent) 
     ` #######&#160;event&#160;to&#160;set&#160;"Squeeze&#160;Dimension&#160;Selection" `

 evt_view_axes_toggle  (self, parent) 
     ` #######&#160;event&#160;to&#160;set&#160;"View&#160;Axes&#160;Selection" `

 evt_view_bounds_weights_toggle  (self, parent) 
     ` #######&#160;event&#160;to&#160;set&#160;"View&#160;Bounds&#160;and&#160;Weights&#160;Selection" `

 execute_c_selection  (self, vcs, parent, result) 
     ` #&#160;Set&#160;the&#160;colormap&#160;selection `

  
class  create_pcmdi_tools_menu 

` `

` #---------------------------------------------------------------------------
-------------  
#&#160;Create&#160;the&#160;PCMDI&#160;Tools&#160;menu&#160;and&#160;its&#160;menu&#160;items  
#-----------------------------------------------------------------------------
-----------  
`

Methods defined here:  

 __init__  (self, main_menu, parent) 

 dailyboundsset  (self, parent, fqcy) 

 evt_climatology  (self, parent, fname) 
     ` #----------------------------------------------------   
#&#160;Class&#160;"Climatology"&#160;events  
#---------------------------------------------------- `

 evt_departures  (self, parent, fname) 
     ` #----------------------------------------------------   
#&#160;Class&#160;"Departures"&#160;events  
#---------------------------------------------------- `

 evt_extract  (self, parent, fname) 
     ` #----------------------------------------------------   
#&#160;Class&#160;"Extract"&#160;events  
#---------------------------------------------------- `

 evt_filters  (self, parent, slab, filter_name, fname, varid, options) 

 evt_salstat  (self, parent, fname, axis  =None  ) 
     ` #----------------------------------------------------   
#&#160;Method&#160;"Statistics"&#160;events  
#---------------------------------------------------- `

 evt_sigma  (self, parent, fname) 

 evt_statistics  (self, parent, fname, axis  =None  , weights  =None  , noloop  =0  ) 
     ` #----------------------------------------------------   
#&#160;Method&#160;"Statistics"&#160;events  
#---------------------------------------------------- `

 get_var  (self, parent, fname  =None  ) 
     ` #&#160;Get&#160;the&#160;selected&#160;variable(&#160;s&#160;)&#160;from&#160;a&#160;file&#160;or&#160;defined&#160;in&#160;memory `

 monthlyboundsset  (self, parent) 

 return_unique_name  (self, name) 
     ` #&#160;Return&#160;a&#160;unique&#160;name&#160;to&#160;be&#160;placed&#160;in&#160;the&#160;defined&#160;variable&#160;window `

 yearlyboundsset  (self, parent) 

  
class  create_tools_menu 

` `

` #---------------------------------------------------------------------------
-------------  
#&#160;Create&#160;the&#160;Tools&#160;menu&#160;and&#160;its&#160;menu&#160;items  
#-----------------------------------------------------------------------------
-----------  
`

Methods defined here:  

 __init__  (self, main_menu, parent, record_commands_flg) 

 evt_popup_change_idle_font_pupop  (self, parent) 
     ` #######&#160;event&#160;to&#160;change&#160;idle's&#160;font `

 evt_popup_idle_command_window  (self, parent) 
     ` #######&#160;event&#160;to&#160;popup&#160;the&#160;idle&#160;command&#160;window `

 evt_popup_idle_editor_window  (self, parent) 
     ` #######&#160;event&#160;to&#160;popup&#160;the&#160;idle&#160;editor&#160;window&#160;for&#160;old&#160;file `

 evt_popup_new_idle_editor_window  (self, parent) 
     ` #----------------------------------------------------   
#&#160;Class&#160;"Tools"&#160;events  
#----------------------------------------------------  
#######&#160;event&#160;to&#160;popup&#160;the&#160;idle&#160;editor&#160;window&#160;for&#160;old&#160;file `

 evt_record_toggle  (self, parent) 
     ` #######&#160;event&#160;to&#160;set&#160;record&#160;flag `

 evt_view_GUI_state  (self, parent) 
     ` #######&#160;event&#160;to&#160;"view&#160;GUI&#160;State" `

 evt_view_record  (self, parent) 
     ` #######&#160;event&#160;to&#160;view&#160;recorded&#160;commands `

 evt_view_record_b  (self, parent) 
     ` #######&#160;event&#160;to&#160;view&#160;beginner's&#160;recorded&#160;commands `

 update_defined_for_user  (self, shell, parent, event) 

 withdraw_idle  (self, shell, filename) 

  
class  exit_browser 

` `

` #---------------------------------------------------------------------------
-------------  
#######&#160;event&#160;for&#160;"Exiting"&#160;the&#160;VCDAT&#160;GUI  
#-----------------------------------------------------------------------------
-----------  
`

Methods defined here:  

 __init__  (self, parent) 

 evt_save_VCS_state  (self) 

 evt_save_gui_state  (self) 

 exit_execute  (self, parent, button) 

  
 Data 

` `

 Pmw  = <Pmw.Pmw_1_2.lib.PmwLoader.PmwLoader instance>   
 fn  = '/pcmdi/halliday1/PCMDI_GRAPHICS' 

* * *

UCRL-WEB-213937 | [ Privacy & Legal Notice ](/disclaimer.html)

[ webmaster@pcmdi.llnl.gov ](/webmaster@pcmdi.llnl.gov)

[ ![Powered by Plone](media/plone_powered.gif) ](/)

