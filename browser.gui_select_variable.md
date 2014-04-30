---
layout: default
title:
---

##Python: module browser.gui_select_variable

ThePCMDIDataBrowserSelectVariablePanel-gui_select_variablemodule  

Module:gui_select_variablemodule

Copyright:"SeefileLegal.htmforcopyrightinformation."

Authors:PCMDISoftwareTeam

LawrenceLivermoreNationalLaboratory:

support@pcmdi.llnl.gov

Description:PCMDISoftwareSystembrowserTkinter"SelectVariable"panel

GUI.

Version:3.0

NOTE:needtouseversionofPythonthatimportsTkinterandPmw  

Modules 

* [Tkinter](Tkinter.html)  
* [cdat_info](cdat_info.html)  
* [cdms](cdms.html)  
* [gui_support.gui_color](gui_support.gui_color.html)  
* [browser.gui_control](browser.gui_control.html)  
* [browser.gui_database](browser.gui_database.html)  
* [browser.gui_defined_variables](browser.gui_defined_variables.html)  
* [browser.gui_edit_list](browser.gui_edit_list.html)  
* [browser.gui_formulate](browser.gui_formulate.html)  
* [browser.gui_functions](browser.gui_functions.html)  
* [browser.gui_message](browser.gui_message.html)  
* [browser.gui_select_variable](browser.gui_select_variable.html)  
* [os](os.html)  
* [re](re.html)  
* [string](string.html)  
* [sys](sys.html)  
* [tkFileDialog](tkFileDialog.html)  
* [types](types.html)  

Classes 

* [create](browser.gui_select_variable.html)

class  create 

Startofthe"SelectVariable"panelGUILayout  

StarttheTkinter/PmwGUIlayout.Thelayoutislistedfromtoptobottom.  
Startingwith:themenubar;followedbythe"SelectVariable"panel,which  
allowstheusertoselectdatafromadirectoryoradatabase;followedby  
the"GraphicsControl"panel,whichallowstheusertoplottheselectedor  
definedvariables;followedbythe"Dimension"panel,whichallowstheuser
to  
selectsubsetsoftheselectedvariablebeforeplottingorstoringinto
memory;  
followedbythe"DefinedVariables"panel,whichallowstheusertomodify
the  
variablesthatarestoredinmemory;andfinallyfollowedbythe"Variable  
Information"scrollwindow,whichdisplaysvariableinformation.  

Allpanelsarecontainedwithinapanedwidget.Thus,allowingthesizeof  
eachsectiontoexpandorconstrict.  

Beginthecreationof"SelectVariable"panel  

Methods defined here:  

__init__  (self, parent) 

Functions 

evt_backspace  (parent, event) 
eventfordirectoryentryonly,searchforbackspaceentry 

evt_change_color  (parent, event) 

eventfunctionsassociatedwiththe"SelectVariable"panel  

evt_cycle_through_directories  (parent, event) 
event'cyclethroughdirectories'fordirectoryentry 

evt_cycle_through_files  (parent, event) 
event'cyclethroughfiles'forfilesentry 

evt_display_file_info  (parent, event) 
event'cyclethroughdirectories'fordirectoryentry 

evt_enter_directory  (parent, event, who_called  =0  ) 
event'textinput'fordirectoryordatabaseentry 

evt_enter_file  (parent, event) 
eventforfileentry 

evt_enter_variable  (parent, event) 
eventforvariableentry 

evt_icon_open_file  (parent, dirfilename  =None  , event  =None  ) 
event'iconfileopen'fordirectoryandfileentry 

evt_popup_database_gui  (self, parent, event) 
eventtotogglebetweenthe'Directory'or'Database' 

evt_tab  (parent, event) 
eventfordirectoryentryonly,searchforatabentry 

restore_directory_setting  (self, parent) 
eventin'DirectoryorDatabasesettings' 

Data 

Pmw  = <Pmw.Pmw_1_2.lib.PmwLoader.PmwLoader instance>

