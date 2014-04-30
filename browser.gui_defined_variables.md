---
layout: default
title:
---

##  Python: module browser.gui_defined_variables

    #ThePCMDIDataBrowserDefinedVariablesPanel-gui_defined_variablesmodule  
    ##############################################################################
    #Module:gui_defined_variablesmodule
    #Copyright:"SeefileLegal.htmforcopyrightinformation."
    #Authors:PCMDISoftwareTeam
    #LawrenceLivermoreNationalLaboratory:
    #support@pcmdi.llnl.gov
    #Description:PCMDISoftwareSystembrowserTkinter"DefinedVariables"
    #panelGUI.
    #Version:4.0
    ##############################################################################
    #---------------------------------------------------------------------  
    #NOTE:needtouseversionofPythonthatimportsTkinterandPmw  
    #--------------------------------------------------------------------- 

### Modules 
* [cdms.MV](cdms.MV.html)  
* [Numeric](Numeric.html)  
* [Tkinter](Tkinter.html)  
* [__main__](__main__.html)  
* [cdms](cdms.html)  
* [genutil](genutil.html)  
* [browser.gui_alter_variable](browser.gui_alter_variable.html)  
* [gui_support.gui_color](gui_support.gui_color.html)  
* [browser.gui_control](browser.gui_control.html)  
* [browser.gui_expression](browser.gui_expression.html)  
* [browser.gui_functions](browser.gui_functions.html)  
* [browser.gui_menu](browser.gui_menu.html)  
* [browser.gui_message](browser.gui_message.html)  
* [browser.gui_output](browser.gui_output.html)  
* [browser.gui_reset](browser.gui_reset.html)  
* [browser.gui_user_menus](browser.gui_user_menus.html)  
* [browser.gui_writenetcdf](browser.gui_writenetcdf.html)  
* [os](os.html)  
* [string](string.html)  
* [sys](sys.html)  
* [time](time.html)  
* [tkFileDialog](tkFileDialog.html)  
* [types](types.html)  
* [browser.vcs_function](browser.vcs_function.html)  
  
### Classes 
* [create](browser.gui_defined_variables.html)
* [update_defined](browser.gui_defined_variables.html)
  
class  create 

    #---------------------------------------------------------------------------  
    #  
    #Startofthe"DefinedVariables"panelGUILayout  
    #  
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
    #  
    #Allpanelsarecontainedwithinapanedwidget.Thus,allowingthesizeof  
    #eachsectiontoexpandorconstrict.  
    #  
    #---------------------------------------------------------------------  
    #Beginthecreationof"DefinedVariables"panel  
    #---------------------------------------------------------------------  


###Methods defined here:  

    __init__  (self, parent) 

    alterpaneDV  (self, parent, event  =None  ) 
     ##Functiontoresizethescrolledboxwhenthepanelchanges 

    copy_graphics_method  (self, parent) 
     #######eventtocopythegraphicsmethod 

    copy_template  (self, parent) 
     #######eventtocopytemplate 

    edit_graphics_method  (self, parent) 
     #######eventtoeditthegraphicsmethod 

    edit_template  (self, parent) 
     #######eventtobringupthetemplateeditor 
    
     evt_call_gui_alter_variable  (self, parent, event) 
      #######eventtocallthegui_alter_variablepopup 

    evt_call_gui_writenetcdf  (self, parent, event) 
      #######eventtocallthewritenetCDFpopup 

    evt_change_command_color  (self, parent, event) 
      #######eventtochangethecommandlineexpressioncolor 

    evt_compute_command  (self, parent, event) 
      #######eventtocallthecommandlinecalculatorexpression 

    evt_dispose_defined_variables  (self, parent, event) 
      #######eventtodisposeofunwantedvariables 

    evt_dispose_execute  (self, parent, var_names, result) 

    evt_do_operation  (self, parent, type, event) 

    evt_expression_widget  (self, parent, event) 

    evt_info_on_defined  (self, parent, event) 
      #######eventtoreturninformationonthedefinedvariables 

    evt_log_on_defined  (self, parent, event) 
      #######eventtoreturninformationonthedefinedvariables 

    evt_remove_all_defined  (self, parent, event) 
      #######eventtoremoveallthedefined 

    evt_remove_selected_defined  (self, parent, var_name, event) 
      #######eventtoremovetheselecteddefined 

    evt_select_graphics_method  (self, gm_name, parent) 
      #######eventtoselectthegraphicsmethod 

    evt_selected_defined_variable  (self, parent, event) 

    evt_selected_defined_variable2  (self, parent, event) 

    evt_selected_defined_variable3  (self, parent, control_key  =0  ) 

    evt_selected_trash_variable  (self, parent) 

    evt_set_mode_operation  (self, parent, event) 

    evt_show_defined_variables_tools  (self, parent, event) 
      #######eventtocallthegui_alter_variablepopup 

    evt_show_template_graphics_method  (self, parent, event) 
      #######eventtocallthegui_alter_variablepopup 

    evt_toggle_DV_selection_mode  (self, parent) 
    #-----------------------------------------------------------------   
    #eventfunctionsassociatedwiththe"DefinedVariable"panelbuttons  
    #-----------------------------------------------------------------  
    #  
    #######eventtotoggletheDefinedVariablewindowselectionmode 

    mode_1_operation  (self, parent, type, event) 
    
    mode_2_operation  (self, parent, type, event) 

    redisplay_graphics_method  (self, parent) 
      #######eventtoredisplaythegraphicsmethodlist 

    redisplay_template  (self, parent) 
      #######eventtoredisplaythetemplatelist 

    remove_graphics_method  (self, parent) 
      #######eventtoremovethegraphicsmethod 

    remove_template  (self, parent) 
      #######eventtoremovetemplate 

    rename_graphics_method  (self, parent) 
      #######eventtorenamethegraphicsmethod 

    rename_template  (self, parent) 
      #######eventtorenametemplate 

    return_trash_can_list  (self, parent) 

    script_graphics_method  (self, parent) 
      #######eventtoscriptthegraphicsmethod 

    script_template  (self, parent) 
      #######eventtosavetemplatetoascriptfile 

    select_gm  (self) 
      #######eventtoselectthedesiredgraphicsmethod 

    select_template  (self) 
      #######eventtoselectthedesiredtemplate 

    update_page_layout  (self, parent, remove_list) 
      #######eventtoremovetheselecteddefined 

    class  update_defined 

###Methods defined here:  

    __init__  (parent, *args) 
  
### Functions 

    get_vars  () 
      #Returnalistofallselectedvariablesintheorderin   
      #whichtheywereselected 
  
      selected_updated  (args  =()  ) 
      #-----------------------------------------------------------------------------------   
      #Intheselectedpaneltheuserwillneedtogetallthechangescomingfromthe  
      #[idle]Shellwindow.Thisfunctionwillupdatetheselectedwindowwiththe  
      #neworremovedTransientVariable(i.e.,MV),MA,orNumericarrays.  
      #----------------------------------------------------------------------------------- 

    update_defined_variable_list  (parent) 
### Data 

    Pmw  = <Pmw.Pmw_1_2.lib.PmwLoader.PmwLoader instance>   
    fn  = '/pcmdi/halliday1/PCMDI_GRAPHICS'   
    graphics_method_list  = ['Boxfill', 'Isofill', 'Isoline', 'Meshfill', 'Outfill', 'Outline', 'Scatter', 'Taylordiagram', 'Vector', 'XvsY', 'Xyvsy', 'Yxvsx']   
    trash_store  = '__trashed_on__'   
    trash_str  = '_waiting_for_user_to_dispose_of_via_trash_can' 
