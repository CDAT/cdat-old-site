---
layout: default
title:
---

##  Python: module browser.gui_graphics_control

    #ThePCMDIDataBrowserGraphicsControlPanel-gui_graphics_controlmodule  
    ##############################################################################
    #Module:gui_graphics_controlmodule
    #Copyright:"SeefileLegal.htmforcopyrightinformation."
    #Authors:PCMDISoftwareTeam
    #LawrenceLivermoreNationalLaboratory:
    #support@pcmdi.llnl.gov
    #Description:PCMDISoftwareSystembrowserTkinter"GraphicsControl"
    #panelGUI.
    #Version:4.0
    ##############################################################################
    #---------------------------------------------------------------------  
    #NOTE:needtouseversionofPythonthatimportsTkinterandPmw  
    #--------------------------------------------------------------------- 

  
###Modules 
* [Tkinter](Tkinter.html)  
* [__main__](__main__.html)  
* [browser.gui_alter_plot](browser.gui_alter_plot.html)  
* [browser.gui_annotate](browser.gui_annotate.html)  
* [browser.gui_busy](browser.gui_busy.html)  
* [browser.gui_canvas_geometry](browser.gui_canvas_geometry.html)  
* [gui_support.gui_color](gui_support.gui_color.html)  
* [browser.gui_control](browser.gui_control.html)  
* [browser.gui_defined_variables](browser.gui_defined_variables.html)  
* [browser.gui_formulate](browser.gui_formulate.html)  
* [browser.gui_functions](browser.gui_functions.html)  
* [browser.gui_message](browser.gui_message.html)  
* [browser.gui_output](browser.gui_output.html)  
* [browser.gui_set_graphics_methods](browser.gui_set_graphics_methods.html)  
* [browser.gui_set_min_max_scale](browser.gui_set_min_max_scale.html)  
* [gui_support](gui_support.html)  
* [os](os.html)  
* [string](string.html)  
* [sys](sys.html)  
* [vcs](vcs.html)  
* [browser.vcs_function](browser.vcs_function.html)  
  
###Classes 
* [create](browser.gui_graphics_control.html)
  
class  create 

    #---------------------------------------------------------------------------  
    #Startofthe"GraphicsControl"panelGUILayout  
    #---------------------------------------------------------------------------  
    #StarttheTkinter/PmwGUIlayout.Thelayoutislistedfromtoptobottom.  
    #Startingwith:themenubar;followedbythe"SelectVariable"panel,which  
    #allowstheusertoselectdatafromadirectoryoradatabase;followedby  
    #the"GraphicsControl"panel,whichallowstheusertoplottheselectedor  
    #definedvariables;followedbythe"Dimension"panel,whichallowstheuserto  
    #selectsubsetsoftheselectedvariablebeforeplottingorstoringintomemory;  
    #followedbythe"DefinedVariables"panel,whichallowstheusertomodifythe  
    #variablesthatarestoredinmemory;andfinallyfollowedbythe"Variable  
    #Information"scrollwindow,whichdisplaysvariableinformation.  
    #Allpanelsarecontainedwithinapanedwidget.Thus,allowingthesizeof  
    #eachsectiontoexpandorconstrict.  
    #---------------------------------------------------------------------  
    #Beginthecreationof"GraphicsControl"panel  
    #---------------------------------------------------------------------  


###Methods defined here:  

    __init__  (self, parent) 

    call_do_plot  (self, parent, gm_type  ='Boxfill'  , var_name  =None  , new_form  =0  ) 
    #######calldoplot   
    #Thisfunctioncanbecalledtwice.Oncefortheinitalgraphicsmethodand
    secondforan  
    #overlayisoline. 

    call_multiple_plot  (self, parent, gm_type  ='Boxfill'  , var_name  =None  , new_form  =0  ) 
    #######callmultipleplot   
    #Thisfunctioncanbecalledtwice.Oncefortheinitalgraphicsmethodand
    secondforan  
    #overlayisoline. 

    evt_animate  (self, parent) 
    #######eventto'Animate'theVCSCanvas 

    evt_clear_display  (self, parent) 
    #######eventto'VCSClearDisplay' 

    evt_close_canvas  (self, parent) 
    #######eventto'CloseVCSCanvas' 

    evt_colormap  (self, parent) 
    #######eventtopopuptheVCS'Colormap' 

    evt_continents_toggle  (self, parent, number) 
    #######eventtosetcontinentsflagtype 

    evt_define  (self, parent, var_name  =None  ) 
    #######eventtodefineavariable 

    evt_gmeditor  (self, parent) 

    evt_isoline_labels_toggle  (self, parent) 
    #######eventtosetisolinelabelsflag 

    evt_number_of_plots_on_canvas  (self, parent, number) 
    #######eventtosetthenubmerplotsonaVCSCanvas 

    evt_overlay_toggle  (self, parent) 
    #######eventtosetoverlayflag 

    evt_page_orientation  (self, parent, orientation) 
    #######eventtosetpageorientation 

    evt_pageeditor  (self, parent) 

    evt_pageeditorplot  (self, parent) 
    #######eventtoplot   
    #Thisiscalledbecausethereisaneedforanintermediatesteptocheckwhether  
    #anoverlayisneeded(i.e.,FilledIsolineorBoxedIsoline).Ifanoverlayisneeded,  
    #Thencall"call_do_plot"twice;onceforisofillorboxfill;andagainfortheisoline  
    #overlay. 

    evt_set_plot_projection  (self, parent, number) 
    #######eventtosettheplotprojection 

    evt_templateeditor  (self, parent) 

    evt_which_graphics_method  (self, parent, event) 
    #######eventtocheckwhichgraphicsmethodisinuse 

    evt_which_vcs_canvas  (self, parent, event) 
    #######eventtocheckwhichVCSCanvasisinuse 

    remove_variable_from_defined_variable_list  (self, parent, remove_variable) 
    
    turn_off_all_plots  (self, parent) 

    turn_on_listed_plots  (self, parent, on_list) 

    which_plot_is_on  (self, parent) 
  
###Functions 

    remove_graphics_methods  (parent) 

###Data 

    Pmw  = <Pmw.Pmw_1_2.lib.PmwLoader.PmwLoader instance>   
    fn  = '/pcmdi/halliday1/PCMDI_GRAPHICS' 
