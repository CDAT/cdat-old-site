---
layout: default
title:
---

##  Python: module browser.gui_dimensions

    #ThePCMDIDataBrowserDimensionsPanel-gui_dimensionsmodule  
    ##############################################################################
    #Module:gui_panelCmodule
    #Copyright:"SeefileLegal.htmforcopyrightinformation."
    #Authors:PCMDISoftwareTeam
    #LawrenceLivermoreNationalLaboratory:
    #support@pcmdi.llnl.gov
    #Description:PCMDISoftwareSystembrowserTkinter"Dimensions"panelGUI.
    #Version:3.0
    ##############################################################################
    #---------------------------------------------------------------------  
    #NOTE:needtouseversionofPythonthatimportsTkinterandPmw  
    #--------------------------------------------------------------------- 

### Modules 
* [Tkinter](Tkinter.html)  
* [cdms](cdms.html)  
* [gui_support.gui_color](gui_support.gui_color.html)  
* [browser.gui_control](browser.gui_control.html)  
* [browser.gui_functions](browser.gui_functions.html)  
* [browser.gui_message](browser.gui_message.html)  
* [browser.gui_output](browser.gui_output.html)  
* [os](os.html)  
* [string](string.html)  

 Classes 
* [create](browser.gui_dimensions.html)
* [create_dim_row](browser.gui_dimensions.html)

class  create 

    #---------------------------------------------------------------------  
    #Beginthecreationof"Dimension"panel  
    #---------------------------------------------------------------------  


###Methods defined here:  

     __init__  (self, parent) 
 
    class  create_dim_row 
    #Createonerowofthedimensionclass  


###Methods defined here:  

    __init__  (self, frameit, parent) 

    evt_change_entry_color  (self, parent, num, event) 
    #eventtosetbackgroundcoloroftheentrywindow.Thischangeof   
    #thebackgroundcolorletstheuserknowtheyareineditmodeandmust  
    #selectthe'Enter'keytoregisterchanges. 

    evt_dim_function  (self, parent, event) 
    #Selectthedimensionoperation 

    evt_enter_first_last  (self, parent, event) 
    #eventtosetthefirstandlastdimensionvaluefromtheentrywidget,   
    #eitherincoordinatesorindex 

    evt_first_scl  (self, parent, event) 
    #eventtosetthefirstdimensionvalue,eitherincoordinatesorindex 

    evt_last_scl  (self, parent, event) 
    #eventtosetthelastdimensionvalue,eitherincoordinatesorindex 

    evt_select_command  (self, parent, event) 
    #Selectthedimensioncoordinatesviathecomboboxscrolledlist 

    evt_select_values  (self, parent, event) 
    #Selecttherangeofthecoordinatevalues 

    return_selection  (self, parent) 
    #Returntheselectedcoordinatepoints 

###Functions 

    alterpaneDM  (self, parent, event  =None  ) 
    ##Functiontoresizethescrolledboxwhenthepanelchanges 
  
### Data 

    Pmw  = <Pmw.Pmw_1_2.lib.PmwLoader.PmwLoader instance>
