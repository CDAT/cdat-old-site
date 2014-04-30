---
layout: default
title:
---

##Python: module browser.gui_variable_information

ThePCMDIDataBrowserVariableInformationPanel-gui_variable_informationmodule  

Module:gui_variable_informationmodule

Copyright:"SeefileLegal.htmforcopyrightinformation."

Authors:PCMDISoftwareTeam

LawrenceLivermoreNationalLaboratory:

support@pcmdi.llnl.gov

Description:PCMDISoftwareSystembrowserTkinter"VariableInformation"

panelGUI.

Version:3.0

NOTE:needtouseversionofPythonthatimportsTkinterandPmw  

Modules 

* [Tkinter](Tkinter.html)  
* [__main__](__main__.html)  
* [browser.gui_busy](browser.gui_busy.html)  
* [gui_support.gui_color](gui_support.gui_color.html)  
* [browser.gui_control](browser.gui_control.html)  
* [browser.gui_defined_variables](browser.gui_defined_variables.html)  
* [browser.gui_formulate](browser.gui_formulate.html)  
* [browser.gui_message](browser.gui_message.html)  
* [os](os.html)  
* [string](string.html)  
* [sys](sys.html)  
* [types](types.html)  
* [browser.vcs_function](browser.vcs_function.html)  

Classes 

* [Form](browser.gui_variable_information.html)
* [create](browser.gui_variable_information.html)
* [create_page_description_panel](browser.gui_variable_information.html)

class  Form 

ShowtheVCS"PageLayout".  

Createdummyformclass  

class  create 

Startofthe"VariableInformation"panelGUILayout  

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

Beginthecreationof"VariableInformation"panel  

Methods defined here:  

__init__  (self, parent) 

class  create_page_description_panel 

Createpagedescriptionpanel'sformslist  

Methods defined here:  

__init__  (self, parent) 

create_form  (self, parent, data1  =None  , data2  =None  , data3  =None  , id  =1  , vcs  =None  ) 
Createpagedescriptionform 

do_plot  (self, id) 

evt_change_priority  (self, id, parent) 

evt_create_new_pl_form  (self, parent) 
Createanewpagelayoutform 

evt_form_priority_change_color  (self, id, parent, event) 

evt_remove_form  (self, id, parent, event) 

evt_replace_data  (self, pe, id, data_entry, parent, event) 

evt_replace_gm  (self, pe, id, parent, event) 

evt_replace_template  (self, pe, id, parent, event) 

evt_status_button  (self, id, parent, event) 

Data 

Pmw  = <Pmw.Pmw_1_2.lib.PmwLoader.PmwLoader instance>
