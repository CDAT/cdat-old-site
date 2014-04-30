---
layout: default
title:
---

##  Python: module browser.gui_extend_menus

    #ThePCMDIDataBrowserExtendToplevelMenus-gui_extend_menusmodule  
    ##############################################################################
    #Module:gui_extend_menusmodule
    #Copyright:"SeefileLegal.htmforcopyrightinformation."
    #Authors:PCMDISoftwareTeam
    #LawrenceLivermoreNationalLaboratory:
    #support@pcmdi.llnl.gov
    #Description:PCMDISoftwareSystembrowserExtendToplevelMenus.
    #Version:4.0
    ##############################################################################
    #---------------------------------------------------------------------  
    #NOTE:needtouseversionofPythonthatimportsTkinterandPmw  
    #--------------------------------------------------------------------- 
  
###Modules 
* [Tkinter](Tkinter.html)  
* [__main__](__main__.html)  
* [gui_support.gui_color](gui_support.gui_color.html)  
* [browser.gui_control](browser.gui_control.html)  
* [browser.gui_defined_variables](browser.gui_defined_variables.html)  
* [browser.gui_message](browser.gui_message.html)  
* [browser.gui_saved_settings](browser.gui_saved_settings.html)  
* [browser.gui_select_variable](browser.gui_select_variable.html)  
* [os](os.html)  
* [string](string.html)  
* [sys](sys.html)  
* [tkFileDialog](tkFileDialog.html)  
* [types](types.html)  
  
###Classes 
* [create](browser.gui_extend_menus.html)

class  create 

    #---------------------------------------------------------------------  
    #  
    #StartofPopupDialog  
    #  
    #---------------------------------------------------------------------------  
    #ExtendToplevelMenusDialogPopup  
    #---------------------------------------------------------------------------  

###Methods defined here:  

    __init__  (self, parent) 

    add_function  (self, parent, evt  =None  ) 
    #---------------------------------------------   
    #Addafunctiontoapre-existingmenufromthemainmenubar  
    #--------------------------------------------- 

    add_top_menu  (self, parent, evt  =None  ) 
    #---------------------------------------------   
    #Addanewmenutothemainmenubar  
    #--------------------------------------------- 
  
    browse_files  (self, parent) 
    #---------------------------------------------   
    #OpenatkFileDialogwindowandgetfilenamefromuser  
    #--------------------------------------------- 

    change_description  (self, parent, evt  =None  ) 
    #---------------------------------------------   
    #Changemenudescription  
    #--------------------------------------------- 

    clear_top  (self, parent) 
    #---------------------------------------------   
    #Clear"Menuname"and"Description"fromthe"Createusermenu"window  
    #--------------------------------------------- 

    del_top_menu  (self, parent) 
    #---------------------------------------------   
    #Removeamenufromthemainmenubar  
    #--------------------------------------------- 

    delete_function  (self, parent) 
    #---------------------------------------------   
    #Deleteafunctionfromthemainmenubar  
    #--------------------------------------------- 

    do_nothing  (self, result) 
    #--------------------------------------------------------------   
    #Usethisfunctionto"lock"afield(bind<KeyPress>todo_nothing)  
    #-------------------------------------------------------------- 

    file_or_import  (self, parent, result) 
    #---------------------------------------------   
    #Togglebetweenfileandimportmode.Changetheappearanceof  
    #group2andgroup2aappropriately  
    #--------------------------------------------- 

    get_functions  (self, result  =None  ) 
    #--------------------------------------------------------------   
    #Getfunctionsfromfileorimportandpopulatethefunction  
    #pulldownmenu  
    #-------------------------------------------------------------- 

    import_functions  (self) 
    #---------------------------------------------   
    #Getfunctionsfromanimport  
    #--------------------------------------------- 

    populate_group2  (self, result) 
    #---------------------------------------------   
    #Whenuserselectsamenunamefromthe"Modifyusermenu"window,  
    #populateallappropriatefieldswithcurrentmenuinformation  
    #--------------------------------------------- 

    rename  (self, evt  =None  ) 
    #---------------------------------------------   
    #Renameafunction  
    #--------------------------------------------- 

    select_function  (self, parent) 
    #---------------------------------------------   
    #Changethevalueof"Functionname"fieldtovalueof"Function"  
    #--------------------------------------------- 
    
###Functions 

    find_modules  () 
    #---------------------------------------------------------------------   
    #ReturntheModulesthathavebeenimported  
    #--------------------------------------------------------------------- 

    find_py_files  (parent) 
    #---------------------------------------------------------------------   
    #Findthepyfilesinthedirectory  
    #--------------------------------------------------------------------- 
    
    restore_menus  (parent) 
    #---------------------------------------------------------------------   
    #RestoreMenusintheMainMenuBar  
    #--------------------------------------------------------------------- 

    returned_functions_and_instances  (self) 
    #---------------------------------------------------------------------   
    #ReturntheModule'sfunctionlist  
    #--------------------------------------------------------------------- 

    wrap_balloon_help  (contents, max_width  =None  ) 
    #Makeformattingofhelpballoonseasier 

###Data 

    Pmw  = <Pmw.Pmw_1_2.lib.PmwLoader.PmwLoader instance>   
    fn  = '/pcmdi/halliday1/PCMDI_GRAPHICS'   
    l_menu  = [] 
