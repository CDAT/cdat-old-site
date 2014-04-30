---
layout: default
title:
---

##  Python: module browser.gui_edit_list

    #ThePCMDIDataBrowseraliasdirectoryeditor-gui_edit_listmodule  
    ##############################################################################
    #Module:gui_edit_listmodule
    #Copyright:"SeefileLegal.htmforcopyrightinformation."
    #Authors:PCMDISoftwareTeam
    #LawrenceLivermoreNationalLaboratory:
    #support@pcmdi.llnl.gov
    #Description:Setsandremovesdimensionnamedaliases.Forexample,
    #thetimedimensionnamecanequalthefollowingnames:
    #'time','TIME','Time','T',or't'.Also,addstothe
    #favoritedirectorylist.
    #Version:4.0
    ##############################################################################
    #---------------------------------------------------------------------  
    #NOTE:needtouseversionofPythonthatimportsTkinterandPmw  
    #--------------------------------------------------------------------- 

### Modules 
* [Tkinter](Tkinter.html)  
* [cdat_info](cdat_info.html)  
* [cdms](cdms.html)  
* [gui_support.gui_color](gui_support.gui_color.html)  
* [browser.gui_control](browser.gui_control.html)  
* [browser.gui_message](browser.gui_message.html)  
* [browser.gui_select_variable](browser.gui_select_variable.html)  
* [os](os.html)  
* [string](string.html)  
* [sys](sys.html)  

### Classes 
* [create](browser.gui_edit_list.html)

class  create 

    #---------------------------------------------------------------------  
    #  
    #StartofPopupDialog  
    #  
    #---------------------------------------------------------------------------  
    #DimensionAliasDialogPopup  
    #---------------------------------------------------------------------------  


    ###Methods defined here:  
    
    __init__  (self, parent, dim_name, event  =None  ) 
    
    enter_new_alias  (self, dim_name, event  =None  ) 
    #---------------------------------------------------------------------------------   
    #Addnewdimensionaliasnametothedimensionaliaslist  
    #--------------------------------------------------------------------------------- 

    evt_change_alias_entry_color  (self, parent, event) 
    
    goto_directory  (self, parent) 
    #---------------------------------------------------------------------------------   
    #Gototheselecteddirectory  
    #--------------------------------------------------------------------------------- 
  
    open_file  (self, parent) 
    #---------------------------------------------------------------------------------   
    #Opentheselectedfile  
    #--------------------------------------------------------------------------------- 
  
    remove_alias  (self, dim_name) 
    #---------------------------------------------------------------------------------   
    #Removethealiasnamefromthelist  
    #--------------------------------------------------------------------------------- 

### Functions 

    check_new_alias_name  (alias_name, dim_name) 
    #---------------------------------------------------------------------------------   
    #Returnaflagthatindicateswhetherornottoaddtothe  
    #newaliaslist.Areturnof0meansdon'taddtothealias  
    #list.Areturnof1meansaddnametodimensionaliaslist.  
    #--------------------------------------------------------------------------------- 

    record_bookmarks  (dim_name) 
    #---------------------------------------------------------------------------------   
    #CreateNewfilecontainingbookmarksforfavoritedirectories  
    #--------------------------------------------------------------------------------- 
    
    return_alias_list  (dim_name) 
    #---------------------------------------------------------------------------------   
    #Returnthedimensionaliaslist.  
    #--------------------------------------------------------------------------------- 
  
    update_vcdat_alias_list  () 
    #---------------------------------------------------------------------------------   
    #UpdateVCDAT'saliaslist  
    #--------------------------------------------------------------------------------- 

### Data 

    Pmw  = <Pmw.Pmw_1_2.lib.PmwLoader.PmwLoader instance>
