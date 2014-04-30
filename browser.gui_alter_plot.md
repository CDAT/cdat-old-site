---
layout: default
title: Browser gui_alter_plot
---

##  Python: module browser.gui_alter_plot
  
    ##############################################################################
    #Module:gui_alter_plotnotebookmodule
    #Copyright:"SeefileLegal.htmforcopyrightinformation."
    #Authors:PCMDISoftwareTeam
    #LawrenceLivermoreNationalLaboratory:
    #support@pcmdi.llnl.gov
    #Description:GUIpopupdialogtoaltertheappearanceoftheVCSplot
    #Version:4.0
    ##############################################################################
    #---------------------------------------------------------------------  
    #NOTE:needtouseversionofPythonthatimportsTkinterandPmw  
    #--------------------------------------------------------------------- 

  
### Modules 
* [Numeric](Numeric.html)  
* [Tkinter](Tkinter.html)  
* [gui_support.gui_color](gui_support.gui_color.html)  
* [browser.gui_control](browser.gui_control.html)  
* [os](os.html)  
* [string](string.html)  
* [sys](sys.html)  
* [types](types.html)  
* [browser.vcs_function](browser.vcs_function.html)  

  
### Classes 
[note_book](browser.gui_alter_plot.html)
  
    class  note_book 

    #-------------------------------------------------------------------------------  
    #PopuptoalterthevisualappearanceoftheVCSplot.  
    #-------------------------------------------------------------------------------  


    Methods defined here:  

    __init__  (self, parent) 
    apply  (self, parent) 
    cbn10_cb  (self) 
    cbn11_cb  (self) 
    cbn12_cb  (self) 
    cbn13_cb  (self) 
    cbn14_cb  (self) 
    cbn15_cb  (self) 
    cbn16_cb  (self) 
    cbn17_cb  (self) 
    cbn18_cb  (self) 
    cbn19_cb  (self) 
    cbn1_cb  (self) 
    cbn20_cb  (self) 
    cbn21_cb  (self) 
    cbn22_cb  (self) 
    cbn2_cb  (self) 
    cbn3_cb  (self) 
    cbn4_cb  (self) 
    cbn5_cb  (self) 
    cbn6_cb  (self) 
    cbn7_cb  (self) 
    cbn8_cb  (self) 

    major_log_axis,minor_log_axis= * [generate_log_values]() ()   
    
    try:  
    self.  eny1  .setentry(major_log_axis)  
    self.  eny2  .setentry(minor_log_axis)  
    except:  
    pass  
    self.  parent  .graphics_method.xticlabels1=major_log_axis  
    self.  parent  .graphics_method.xticlabels2=major_log_axis  
    self.  parent  .graphics_method.xmtics1=minor_log_axis  
    self.  parent  .graphics_method.xmtics2=minor_log_axis 

    cbn9_cb  (self) 
    major_sine_axis,minor_sine_axis= * [generate_sine_values]() ()   

    try:  
    self.  eny1  .setentry(major_sine_axis)  
    self.  eny2  .setentry(minor_sine_axis)  
    except:  
    pass  
    self.  parent  .graphics_method.xticlabels1=major_sine_axis  
    self.  parent  .graphics_method.xticlabels2=major_sine_axis  
    self.  parent  .graphics_method.xmtics1=minor_sine_axis  
    self.  parent  .graphics_method.xmtics2=minor_sine_axis 

    cbnAwt1_cb  (self) 
    cbnAwt2_cb  (self) 
    cbnLn1_cb  (self) 
    cbnLn2_cb  (self) 
    cbnstat_off_cb  (self) 
    cbnstat_on_cb  (self) 
    execute  (self, parent, result) 
    get_legend_settings  (self) 
    get_plot_settings  (self) 
    get_template_settings  (self) 
    get_x_settings  (self) 
    get_x_y_axis_entries  (self) 
    get_y_settings  (self) 
    hold_alter_original_attr_settings  (self, parent) 
    reset_alter_to_original_settings  (self, parent) 
    set_default_xlabels  (self) 
    set_default_ylabels  (self) 
 
### Functions 

    generate_log_values  () 
    #Generatelog10dictionaryvalues 
    
    generate_sine_values  () 
    #Generatesinedictionaryvalues 
    
    generate_x_axis  (parent, graphics_method, replot_flg) 
    #----------------------------------------------------------------------------   
    #Setthegraphicsmethodsx-axisaccordingtothe"alterplot"popupcontrols  
    #----------------------------------------------------------------------------
    
    
    generate_y_axis  (parent, graphics_method, replot_flg) 
    #----------------------------------------------------------------------------   
    #Setthegraphicsmethodsy-axisaccordingtothe"alterplot"popupcontrols  
    #----------------------------------------------------------------------------


    initialize  (parent) 
    #-------------------------------------------------------------------------------   
    #Initializethealterplot'sdefaultsettings  
    #------------------------------------------------------------------------------- 

     settings  (parent, replot_flg, g_name, template_name) 
      #ifgraphics_method.yaxisconvert=='log10':   
    #major_log_axis={}  
    #minor_log_axis={}  
    #a=10000.0  
    #b=a/10.0  
    #forjinrange(8):  
    #foriinrange(a/b):  
    #log_num=Numeric.log10(a-(i*b))  
    #minor_log_axis[log_num]=str(a-(i*b))  
    #if(log_num-int(log_num))==0:  
    #major_log_axis[log_num]=str(a-(i*b))  
    #a=b  
    #b=a/10.0  
    ##  
    #graphics_method.yticlabels1=major_log_axis  
    #graphics_method.ymtics1=minor_log_axis  
    #graphics_method.yticlabels2=major_log_axis  
    #graphics_method.ymtics2=minor_log_axis  
    #elifreplot_flg!=3:  
    #graphics_method.yticlabels1='*'  
    #graphics_method.ymtics1='*'  
    #graphics_method.yticlabels2='*'  
    #graphics_method.ymtics2='*'  
    #else:  
    #major_str=parent.alter_notebook.eny3.get()  
    #minor_str=parent.alter_notebook.eny4.get()  
    #graphics_method.yticlabels1='*'  
    #if(major_str!='*')and(major_str!=''):  
    #s=eval(major_str)  
    #graphics_method.yticlabels1=s  
    #graphics_method.ymtics1=''  
    #if(minor_str!='*')and(minor_str!=''):  
    #s=eval(minor_str)  
    #graphics_method.ymtics1=s  
    #graphics_method.yticlabels2='*'  
    #graphics_method.ymtics2=''  
    #  
    #  
    #----------------------------------------------------------------------------  
    #Setthegraphicsmethodsaccordingtothe"alterplot"popupcontrols  
    #----------------------------------------------------------------------------


    write_legend_page  (self, page) 
    #----------------------------------------------------------------------   
    #Writethe"Legend"pagetothenotebook  
    #---------------------------------------------------------------------- 

    write_shape_page  (self, page) 
    #----------------------------------------------------------------------   
    #Writethe"Shape"pageofthenotebook  
    #---------------------------------------------------------------------- 

    write_template_page  (self, page) 
    #----------------------------------------------------------------------   
    #Writethe"Template"pageofthenotebook.  
    #---------------------------------------------------------------------- 

    write_x_axis_page  (self, page) 
    #----------------------------------------------------------------------   
    #Writethe"X-Axis"pageofthenotebook.  
    #---------------------------------------------------------------------- 

    write_y_axis_page  (self, page) 
    #----------------------------------------------------------------------   
    #Writethe"Y-Axis"pagetothenotebook  
    #---------------------------------------------------------------------- 

### Data 

    Pmw  = <Pmw.Pmw_1_2.lib.PmwLoader.PmwLoader instance>   
    fn  = '/pcmdi/halliday1/PCMDI_GRAPHICS'   
    global_xmtics  = '*'   
    global_xticlabels  = '*'   
    global_ymtics  = '*'   
    global_yticlabels  = '*' 
