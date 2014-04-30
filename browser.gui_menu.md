---
layout: default
title:
---

Python: module browser.gui_menu

ThePCMDIDataBrowserMenuBar-gui_menumodule  

Module:gui_menumodule

Copyright:"SeefileLegal.htmforcopyrightinformation."

Authors:PCMDISoftwareTeam

LawrenceLivermoreNationalLaboratory:

support@pcmdi.llnl.gov

Description:PCMDISoftwareSystembrowserTkinterMainMenuBar.

Version:4.0

---------------------------------------------------------------------  
NOTE:needtouseversionofPythonthatimportsTkinterandPmw  
--------------------------------------------------------------------- 

Modules 
* [Tkinter](Tkinter.html)  
* [__main__](__main__.html)  
* [cdutil](cdutil.html)  
* [genutil](genutil.html)  
* [browser.gui_about](browser.gui_about.html)  
* [browser.gui_ascii](browser.gui_ascii.html)  
* [browser.gui_ascii_cols](browser.gui_ascii_cols.html)  
* [browser.gui_bounds_question](browser.gui_bounds_question.html)  
* [browser.gui_busy](browser.gui_busy.html)  
* [gui_support.gui_color](gui_support.gui_color.html)  
* [browser.gui_control](browser.gui_control.html)  
* [browser.gui_defined_variables](browser.gui_defined_variables.html)  
* [browser.gui_edit_list](browser.gui_edit_list.html)  
* [browser.gui_extend_menus](browser.gui_extend_menus.html)  
* [browser.gui_filters_question](browser.gui_filters_question.html)  
* [browser.gui_formulate](browser.gui_formulate.html)  
* [browser.gui_functions](browser.gui_functions.html)  
* [browser.gui_message](browser.gui_message.html)  
* [browser.gui_output](browser.gui_output.html)  
* [browser.gui_read_Struct](browser.gui_read_Struct.html)  
* [browser.gui_reset](browser.gui_reset.html)  
* [browser.gui_saved_settings](browser.gui_saved_settings.html)  
* [browser.gui_select_variable](browser.gui_select_variable.html)  
* [browser.gui_set_idle_font](browser.gui_set_idle_font.html)  
* [browser.gui_statistics_question](browser.gui_statistics_question.html)  
* [gui_support](gui_support.html)  
* [browser.gui_user_menus](browser.gui_user_menus.html)  
* [os](os.html)  
* [string](string.html)  
* [sys](sys.html)  
* [tkFileDialog](tkFileDialog.html)  
* [webbrowser](webbrowser.html)  

Classes 
* [create](browser.gui_menu.html)
* [create_file_menu](browser.gui_menu.html)
* [create_help_menu](browser.gui_menu.html)
* [create_options_menu](browser.gui_menu.html)
* [create_pcmdi_tools_menu](browser.gui_menu.html)
* [create_tools_menu](browser.gui_menu.html)
* [exit_browser](browser.gui_menu.html)

class  create 

---------------------------------------------------------------------------
Beginthecreationofthefilemenuanditsmenuitems  
-----------------------------------------------------------------------------

Methods defined here:  

__init__  (self, parent) 

class  create_file_menu 

---------------------------------------------------------------------------
Beginthecreationofthefilemenuanditsmenuitems  
-----------------------------------------------------------------------------

Methods defined here:  

__init__  (self, main_menu, parent) 

evt_all_files  (self, parent) 
eventforseletingALLdatafiles 

evt_cdml_files  (self, parent) 
eventforseletingCDMLdatafiles 

evt_cdms_files  (self, parent) 
eventforseletingCDMSdatafiles 

evt_ctl_files  (self, parent) 
eventforseletingGrADSdatafiles 

evt_data_files  (self, parent) 
eventforseletingthePCMDIdatafiles 

evt_datasets_files  (self, parent) 
eventforseletingtheDatabasedatafiles 

evt_dic_files  (self, parent) 
eventforseletingDRSdatafiles 

evt_find_files  (self, parent) 
eventforseletingPatternfiles 

evt_hdf_files  (self, parent) 

evt_nc_files  (self, parent) 
eventforseletingnetCDFdatafiles 

evt_open_file  (self, parent) 

---------------------------------------------------------------------------   
Defineeventfunction'sfor"File"menuitems  
---------------------------------------------------------------------------  

eventthatwillpopupthetkFiledialogandenterthedirectoryand
filestring  
inthedirectoryandfileentrywidgets 

evt_read_script_file  (self, parent) 
eventto"ReadScriptFile" 

evt_returned_printers  (self, parent, printer_name) 
eventtoplotVCSCanvastodesinatedprinter 

evt_save_plot_to_cgm  (self, parent) 
eventtosave"Plot"ina'CGM'file 

evt_save_plot_to_eps  (self, parent) 
eventtosave"Plot"ina'EPS'file 

evt_save_plot_to_gif  (self, parent) 
eventtosave"Plot"ina'GIF'file 

evt_save_plot_to_postscript  (self, parent) 
eventtosave"Plot"ina'Postscript'file 

evt_save_state_of_System  (self, parent) 
eventto"SavetheCurrentStateoftheSystem" 

evt_save_state_of_VCS  (self, parent) 
eventto"SavetheCurrentStateoftheVCSgraphicsSystem" 

evt_specify_printer  (self, parent) 
eventtoplotVCSCanvasto"Specified"printer 

evt_xml_files  (self, parent) 
eventforseletingXMLdatafiles 

class  create_help_menu 

---------------------------------------------------------------------------
CreatetheHelpmenuanditsmenuitems  
-----------------------------------------------------------------------------

Methods defined here:  

__init__  (self, main_menu, parent) 

evt_cdat_las_web  (self) 
eventtobringupawebbrowserthatisdisplayingtheCDAT-LASwebpage 

evt_cdat_web  (self) 

----------------------------------------------------   
Class"Help"events  
----------------------------------------------------  

eventtobringupawebbrowserthatisdisplayingtheCDATwebpage 

evt_numpy_web  (self) 
eventtobringupawebbrowserthatisdisplayingtheNumericwebpage 

evt_pcmdi_web  (self) 
eventtobringupawebbrowserthatisdisplayingthePCMDIwebpage 

evt_python_web  (self) 
eventtobringupawebbrowserthatisdisplayingthePCMDISoftwarewebpage 

class  create_options_menu 

---------------------------------------------------------------------------
CreatethePreferencesmenuanditsmenuitems  
-----------------------------------------------------------------------------

Methods defined here:  

__init__  (self, main_menu, parent, save_region, squeeze_dim_flg, fortran_order_flg, popup_window_settings_flg, view_axes_flg, view_bounds_weights_flg, meridian_flg, convert_to_MV_flg, show_exit_popup_flg) 

evt_DV_single_selection_mode  (self, parent) 

evt_color_intensity  (self, parent, color_intensity) 

----------------------------------------------------   
Class"Preferences"events  
----------------------------------------------------  

eventtoset"ColormapMaximunIntensityValue" 

evt_convert_to_MV_toggle  (self, parent) 
eventtoset"AutomaticConversionofNumericandMAarraystoMV" 

evt_exit_popup_toggle  (self, parent) 
eventtoset"ShowPopupWindowforExistingVCDAT" 

evt_fortran_toggle  (self, parent) 
eventtoset"FortranOrder" 

evt_mode_of_operation  (self, parent, operation_mode) 
eventtoset"SaveRegionSelection" 

evt_popup_window_toggle  (self, parent) 
eventtoset"PopupWindowDefinedSettings" 

evt_reset_GUI_state  (self, parent) 
eventto"ResetGUItoitsInitialState" 

evt_reset_GUI_swap_space  (self, parent) 
eventto"ResettheGUI'sSwapSpaceSize" 

evt_save_GUI_settings  (self, parent) 
eventto"SaveGUISettings" 

evt_save_GUI_state  (self, parent) 
eventto"SaveGUI'sInitialState" 

evt_save_VCS_settings  (self, parent) 
eventto"SaveVCSSettings" 

evt_set_default_colormap  (self, parent) 
eventto"ResettheGUI'sSwapSpaceSize" 

evt_set_default_graphics_method  (self, parent) 
eventto"ResettheGUI'sSwapSpaceSize" 

evt_set_default_template  (self, parent) 
eventto"ResettheGUI'sSwapSpaceSize" 

evt_set_meridian_toggle  (self, parent, number) 
eventtoset"MeridianSelection" 

evt_set_region  (self, parent, region_type) 
eventtoset"SaveRegionSelection" 

evt_show_defined_var_tools  (self, parent) 
evt_show_template_graphics_method_windows  (self, parent) 

evt_squeeze_dim_toggle  (self, parent) 
eventtoset"SqueezeDimensionSelection" 

evt_view_axes_toggle  (self, parent) 
eventtoset"ViewAxesSelection" 

evt_view_bounds_weights_toggle  (self, parent) 
eventtoset"ViewBoundsandWeightsSelection" 

execute_c_selection  (self, vcs, parent, result) 
Setthecolormapselection 

class  create_pcmdi_tools_menu 

---------------------------------------------------------------------------
CreatethePCMDIToolsmenuanditsmenuitems  
-----------------------------------------------------------------------------

Methods defined here:  

__init__  (self, main_menu, parent) 

dailyboundsset  (self, parent, fqcy) 

evt_climatology  (self, parent, fname) 

----------------------------------------------------   
Class"Climatology"events  
---------------------------------------------------- 

evt_departures  (self, parent, fname) 

----------------------------------------------------   
Class"Departures"events  
---------------------------------------------------- 

evt_extract  (self, parent, fname) 
----------------------------------------------------   
Class"Extract"events  
---------------------------------------------------- 

evt_filters  (self, parent, slab, filter_name, fname, varid, options) 

evt_salstat  (self, parent, fname, axis  =None  ) 
----------------------------------------------------   
Method"Statistics"events  
---------------------------------------------------- 

evt_sigma  (self, parent, fname) 

evt_statistics  (self, parent, fname, axis  =None  , weights  =None  , noloop  =0  ) 
----------------------------------------------------   
Method"Statistics"events  
---------------------------------------------------- 

get_var  (self, parent, fname  =None  ) 
Gettheselectedvariable(s)fromafileordefinedinmemory 

monthlyboundsset  (self, parent) 

return_unique_name  (self, name) 
Returnauniquenametobeplacedinthedefinedvariablewindow 

yearlyboundsset  (self, parent) 


class  create_tools_menu 

---------------------------------------------------------------------------
CreatetheToolsmenuanditsmenuitems  
-----------------------------------------------------------------------------

Methods defined here:  

__init__  (self, main_menu, parent, record_commands_flg) 

evt_popup_change_idle_font_pupop  (self, parent) 
eventtochangeidle'sfont 

evt_popup_idle_command_window  (self, parent) 
eventtopopuptheidlecommandwindow 

evt_popup_idle_editor_window  (self, parent) 
eventtopopuptheidleeditorwindowforoldfile 

evt_popup_new_idle_editor_window  (self, parent) 
----------------------------------------------------   
Class"Tools"events  
----------------------------------------------------  
eventtopopuptheidleeditorwindowforoldfile 

evt_record_toggle  (self, parent) 
eventtosetrecordflag 

evt_view_GUI_state  (self, parent) 
eventto"viewGUIState" 

evt_view_record  (self, parent) 
eventtoviewrecordedcommands 

evt_view_record_b  (self, parent) 
eventtoviewbeginner'srecordedcommands 

update_defined_for_user  (self, shell, parent, event) 

withdraw_idle  (self, shell, filename) 


class  exit_browser 


---------------------------------------------------------------------------
eventfor"Exiting"theVCDATGUI  
-----------------------------------------------------------------------------


Methods defined here:  

__init__  (self, parent) 

evt_save_VCS_state  (self) 

evt_save_gui_state  (self) 

exit_execute  (self, parent, button) 


Data 

Pmw  = <Pmw.Pmw_1_2.lib.PmwLoader.PmwLoader instance>   
fn  = '/pcmdi/halliday1/PCMDI_GRAPHICS' 

