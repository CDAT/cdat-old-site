---
layout: default
title:
---


##Python: module browser.gui_set_graphics_methods

ThePCMDIDataBrowserContourLevelsPopup-gui_set_graphics_methodsmodule  

Module:gui_set_graphics_methodsmodule

Copyright:"SeefileLegal.htmforcopyrightinformation."

Authors:PCMDISoftwareTeam

LawrenceLivermoreNationalLaboratory:

support@pcmdi.llnl.gov

Description:PCMDISoftwareSystembrowsertosetgraphicsmethod

attributespopup.

Version:4.0

NOTE:needtouseversionofPythonthatimportsTkinterandPmw  

Modules 

* [Numeric](Numeric.html)  
* [Tkinter](Tkinter.html)  
* [cdms](cdms.html)  
* [cdtime](cdtime.html)  
* [gui_support.gui_color](gui_support.gui_color.html)  
* [browser.gui_control](browser.gui_control.html)  
* [browser.gui_functions](browser.gui_functions.html)  
* [browser.gui_menu](browser.gui_menu.html)  
* [browser.gui_message](browser.gui_message.html)  
* [math](math.html)  
* [os](os.html)  
* [string](string.html)  
* [sys](sys.html)  
* [types](types.html)  
* [vcs](vcs.html)  
* [browser.vcs_function](browser.vcs_function.html)  

Classes 

* [boxfill_attributes](browser.gui_set_graphics_methods.html)
* [continents_attributes](browser.gui_set_graphics_methods.html)
* [contour_levels](browser.gui_set_graphics_methods.html)
* [meshfill_attributes](browser.gui_set_graphics_methods.html)
* [note_book](browser.gui_set_graphics_methods.html)
* [oneD_attributes](browser.gui_set_graphics_methods.html)
* [outfill_attributes](browser.gui_set_graphics_methods.html)
* [outline_attributes](browser.gui_set_graphics_methods.html)
* [scatter_attributes](browser.gui_set_graphics_methods.html)
* [vector_attributes](browser.gui_set_graphics_methods.html)
* [browser.gui_taylor.TDGui](browser.gui_taylor.html)
* [taylor_attributes](browser.gui_set_graphics_methods.html)

class  boxfill_attributes 

Methods defined here:  

__init__  (self, page, parent, re_plot_flag  =1  , gm  =None  ) 

boxfill_clear  (self) 

boxfill_replot  (self, parent) 

evt_boxfill_linear_log  (self, parent, tag) 

get_settings  (self) 

reset_boxf_attributes  (self) 

class  continents_attributes 

Methods defined here:  

__init__  (self, page, parent, re_plot_flag  =1  , gm  =None  ) 

cont_replot  (self, parent) 

get_settings  (self) 

persistant_set  (self) 

reset_cont_attributes  (self) 

class  contour_levels 

Methods defined here:  

__init__  (self, page, parent, re_plot_flag  =1  , gm  =None  , gm_name  =None  ) 

contour_clear  (self) 

contour_gen_ranges  (self, parent) 

contour_replot  (self, parent) 

evt_contour_linear_log  (self, parent, tag) 

get_settings  (self) 

reset_contour_attributes  (self) 

class  meshfill_attributes 

Methods defined here:  

__init__  (self, page, parent, re_plot_flag  =1  , gm  =None  ) 

get_settings  (self) 

meshfill_clear  (self) 

meshfill_replot  (self, parent) 

reset_meshf_attributes  (self) 

class  note_book 

StartofPopupDialog  

VCSUserDefineContourLevelsPopup  

Methods defined here:  

__init__  (self, parent) 

apply  (self, parent, notebook_page, graphics_method) 

execute  (self, parent, result) 

hold_gm_original_attr_settings  (self) 

persistant_set  (self) 

reset_gms_to_original_settings  (self, parent, notebook_page, graphics_method) 

class  oneD_attributes 

Methods defined here:  

__init__  (self, page, parent, re_plot_flag  =1  , gm  =None  ) 

get_settings  (self) 

oneD_clear  (self, parent) 

oneD_replot  (self, parent) 

reset_oneD_attributes  (self) 

class  outfill_attributes 

Methods defined here:  

__init__  (self, page, parent, re_plot_flag  =1  , gm  =None  ) 

get_settings  (self) 

outf_replot  (self, parent) 

outfill_clear  (self) 

reset_outf_attributes  (self) 

class  outline_attributes 

Methods defined here:  

__init__  (self, page, parent, re_plot_flag  =1  , gm  =None  ) 

get_settings  (self) 

outl_replot  (self, parent) 

outline_clear  (self) 

reset_outl_attributes  (self) 

class  scatter_attributes 

Methods defined here:  

__init__  (self, page, parent, re_plot_flag  =1  , gm  =None  ) 

get_settings  (self) 

reset_scat_attributes  (self) 

scat_replot  (self, parent) 

class  taylor_attributes  ( * [browser.gui_taylor.TDGui](/browser.gui_taylor.html) )

Methods defined here:  

__init__  (self, page, parent, vcs  =None  , gm_name  ='ASD'  ) 

Methods inherited from * [browser.gui_taylor.TDGui](browser.gui_taylor.html)

get_settings  (self) 

gui_addMarker  (self) 

gui_addMarkerInGui  (self, row) 

gui_copyMarkers  (self) 

gui_deleteMarkers  (self) 

gui_generateInterfaceGui  (self) 

gui_generateLabelsGui  (self) 

gui_generateMarkersGui  (self) 

gui_start  (self) 

gui_updateMarkers  (self) 

updateInterface  (self) 

updatearrow  (self, *args) 

class  vector_attributes 

Methods defined here:  

__init__  (self, page, parent, re_plot_flag  =1  , gm  =None  ) 

get_settings  (self) 

reset_vector_attributes  (self) 

vector_replot  (self, parent) 

Functions 

return_float_None  (val) 

Endsetgraphicsmethodspopupdialog  

return_int_None  (val) 

round_number  (N) 

sign  (N) 

Data 

Pmw  = <Pmw.Pmw_1_2.lib.PmwLoader.PmwLoader instance>
