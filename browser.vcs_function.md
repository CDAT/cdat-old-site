---
layout: default
title:
---

##Python: module browser.vcs_function

ThePCMDIDataBrowserVCSPlotFunctions-vcs_functionmodule  

Module:vcs_functionmodule

Copyright:"SeefileLegal.htmforcopyrightinformation."

Authors:PCMDISoftwareTeam

LawrenceLivermoreNationalLaboratory:

support@pcmdi.llnl.gov

Description:PCMDISoftwareSystembrowserVCSplotfunctions.

Version:4.0

NOTE:needtouseversionofPythonthatimportsTkinterandPmw  

Modules 

* [cdms.MV](cdms.MV.html)  
* [Numeric](Numeric.html)  
* [Tkinter](Tkinter.html)  
* [cdms](cdms.html)  
* [cdtime](cdtime.html)  
* [browser.gui_alter_plot](browser.gui_alter_plot.html)  
* [browser.gui_annotate](browser.gui_annotate.html)  
* [browser.gui_control](browser.gui_control.html)  
* [browser.gui_formulate](browser.gui_formulate.html)  
* [browser.gui_functions](browser.gui_functions.html)  
* [browser.gui_menu](browser.gui_menu.html)  
* [browser.gui_message](browser.gui_message.html)  
* [math](math.html)  
* [os](os.html)  
* [string](string.html)  
* [sys](sys.html)  
* [types](types.html)  
* [vcs](vcs.html)  

Functions 

custom_ranges  (min, max, num) 

GenerateBoxDiscreterangesandcolorindices  

dotemplate  (parent, template, id, replot_flg, g_name) 

Resetthetempaltenaeandtemplateattributesifneeeded 

initialize  (root, dosplashscreen, counter_bar) 

InitializetheVCSgrapicspackages  

modify_template  (parent, t, t2, n, n2, x, y, w, h, orientation  ='horizontal'  , legend_top  =1  ) 

ModifythetemplatetofitontheVCSCanvas  

plot  (parent  =None  , slab1  =None  , slab2  =None  , template  =None  , g_name  =None  , g_type  =None  , bg  =0  , id  =1  ) 

PlotthedataviaVCS  

def * [plot]() (parent,g_type,replot_flg,bg,formulate_data=1): 

re_plot  (parent, replot_flg) 

Re-plotthedataviaVCS  

record_plot  (parent, slab1  =None  , slab2  =None  , templ  =None  , gtype  =None  , gname  =None  , plot_kw  ={}  ) 

RecordVCSplotcommand  

set_template  (parent, template_name  =None  ) 

ModifythetemplatetofitontheVCSCanvas  

turn_on_off_1Dplot_annotation  (parent, template_name) 

Turnon/offannotationfor1Dplots  

turn_on_off_plot_annotation  (parent, template_name) 

Turnon/offannotation  

Data 

    Pmw  = <Pmw.Pmw_1_2.lib.PmwLoader.PmwLoader instance>   
    fn  = '/pcmdi/halliday1/PCMDI_GRAPHICS' 

