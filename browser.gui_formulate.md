---
layout: default
title:
---

#  Python: module browser.gui_formulate

    #ThePCMDIDataBrowserFormulateData-gui_formulatemodule  
    ##############################################################################
    #Module:gui_formulatemodule
    #Copyright:"SeefileLegal.htmforcopyrightinformation."
    #Authors:PCMDISoftwareTeam
    #LawrenceLivermoreNationalLaboratory:
    #support@pcmdi.llnl.gov
    #Description:PCMDISoftwareSystembrowserformulatedata.Thisfunction
    #subslicesthedataand[ifneed]willtakeasum,average
    #orareaweightedaverageofadimension.Singletondimensions
    #aresqueezedout(orelminated)asaresult.
    #Version:4.0
    ##############################################################################
    #---------------------------------------------------------------------  
    #NOTE:needtouseversionofPythonthatimportsTkinterandPmw  
    #--------------------------------------------------------------------- 

###Modules 
* [cdms.MV](cdms.MV.html)  
* [Numeric](Numeric.html)  
* [Tkinter](Tkinter.html)  
* [cdms](cdms.html)  
* [cdtime](cdtime.html)  
* [cdutil](cdutil.html)  
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
  
###Functions 

    data  (parent, d_name  =None  , var  =None  , new_var  =None  ) 
    #---------------------------------------------------------------------------   
    #Modifythedatajustbeforeplottingorstoringinthe"Selected"list  
    #--------------------------------------------------------------------------- 
  
    re_scale_data  (a, multiplier) 
    #---------------------------------------------------------------------------   
    #Modifythedatabyscalingtheincomingdatabytheincomingmultiplier.  
    #--------------------------------------------------------------------------- 

    zapFirstDimension  (a) 
    #---------------------------------------------------------------------------   
    #Modifythedatatoremoveonlythefirstsingledimension  
    #--------------------------------------------------------------------------- 

### Data 

    Pmw  = <Pmw.Pmw_1_2.lib.PmwLoader.PmwLoader instance>
