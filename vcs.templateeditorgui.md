---
layout: default
title:
---

 [ Skip to content. ](/cdat/source/api-reference/vcs.templateeditorgui.html) |
[ Skip to navigation ](/cdat/source/api-reference/vcs.templateeditorgui.html)

Search Site

[ Advanced Search&#8230; ](/search_form)

#  [ PCMDI Software Portal ](/)

#####  Sections

  * [ Home ](/)

#####  Personal tools

  * [ Log in ](/login_form)

You are here:  [ Home ](/) -> [ CDAT ](/cdat) -> [ Source Code ](/cdat/source)
-> [ API Reference ](/cdat/source/api-reference) -> Python: module
vcs.templateeditorgui

[ Navigation ](/sitemap)

    

  * [ Home ](/)

  * [ PCMDI Home Page ](/)

  * [ News ](/news)

  * [ CDAT ](/cdat)

    * [ Download and Install ](/cdat/download)

    * [ Screenshots ](/cdat/screenshots)

    * [ Contrib Packages ](/cdat/contrib)

    * [ Getting Started ](/cdat/getting_started)

    * [ Tutorials ](/cdat/tutorials)

    * [ Quick Reference ](/cdat/quick_reference)

    * [ FAQ ](/cdat/FAQ)

    * [ Manuals ](/cdat/manuals)

    * [ Tips and Tricks ](/cdat/tips_and_tricks)

    * [ Source Code ](/cdat/source)

      * [ API Reference ](/cdat/source/api-reference)

        * [ Python: module vcs.templateeditorgui ](/cdat/source/api-reference/vcs.templateeditorgui.html)

    * [ Contact Us ](/cdat/contact-us)

    * [ Documents ](/cdat/docs)

    * [ Support ](/cdat/support)

  * [ CMOR ](/cmor)

  * [ IPCC AR4 Model Data Portal ](/esg_data_portal)

  * [ About Us ](/about)

  * [ Newsletter ](/Newsletter)

[ News ](/news)

     [ ![](media/newsitem_icon.gif) CDAT Newsletter, June 2007  2007-06-26  ](/Newsletter/Vol3/index_d.html)
     [ ![](media/newsitem_icon.gif) CDAT 4.1.2 Released  2006-06-07  ](/cdat_4_1_2)
     [ ![](media/newsitem_icon.gif) CDAT 4.0 Released  2005-11-21  ](/cdat_4_0)
     [ ![](media/newsitem_icon.gif) PCMDI Software Portal Released  2005-09-28  ](/software_portal_release)
     [ ![](media/newsitem_icon.gif) CDAT 4.0 Beta Released  2005-09-28  ](/cdat_4_0_beta)
     [ More news&#8230; ](/news)

#####  Document Actions

  * [ ![Send this page to somebody](media/mail_icon.gif) ](/cdat/source/api-reference/vcs.templateeditorgui.html/sendto_form)
  * [ ![Print this page](media/print_icon.gif) ](/this.print\(\))

#  Python: module vcs.templateeditorgui

  
  
 [ vcs  ](/vcs.html) .templateeditorgui 
[ index ](/)  

` #&#160;The&#160;VCS&#160;Template&#160;GUI&#160;controls&#160;-&#160;&#160;templateeditorgui&#160;module  
#  
##############################################################################
###  
#
#  
#&#160;Module:&#160;&#160;&#160;&#160;&#160;&#160;&#160;templateeditorgui&#160;module
#  
#
#  
#&#160;Copyright:&#160;&#160;&#160;&#160;"See&#160;file&#160;Legal.htm&#160;for&#160;copyright&#160;information."
#  
#
#  
#&#160;Authors:&#160;&#160;&#160;&#160;&#160;&#160;PCMDI&#160;Software&#160;Team
#  
#&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;Lawrence&#160;Livermore&#160;NationalLaboratory:
#  
#&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;support@pcmdi.llnl.gov
#  
#
#  
#&#160;Description:&#160;&#160;PCMDI's&#160;VCS&#160;GUI&#160;template&#160;editor.
#  
#
#  
#
#  
##############################################################################
### `

  
 Modules 

` `

[ vcs.Canvas ](/vcs.Canvas.html)  
[ MA ](/MA.html)  
[ vcs.Pboxeslines ](/vcs.Pboxeslines.html)  
[ vcs.Pdata ](/vcs.Pdata.html)  
[ vcs.Pformat ](/vcs.Pformat.html)  

[ vcs.Plegend ](/vcs.Plegend.html)  
[ vcs.Ptext ](/vcs.Ptext.html)  
[ vcs.Pxlabels ](/vcs.Pxlabels.html)  
[ vcs.Pxtickmarks ](/vcs.Pxtickmarks.html)  
[ vcs.Pylabels ](/vcs.Pylabels.html)  

[ vcs.Pytickmarks ](/vcs.Pytickmarks.html)  
[ Tkinter ](/Tkinter.html)  
[ cdms ](/cdms.html)  
[ gui_support ](/gui_support.html)  
[ os ](/os.html)  

[ string ](/string.html)  
[ sys ](/sys.html)  

  
 Classes 

` `

[ _Pmw.Pmw_1_2.lib.PmwGroup.Group ](/_Pmw.Pmw_1_2.lib.PmwGroup.html) ( [
_Pmw.Pmw_1_2.lib.PmwBase.MegaWidget ](/_Pmw.Pmw_1_2.lib.PmwBase.html) )

    

[ TemplateAttributeEditor ](/vcs.templateeditorgui.html)

[ _Pmw.Pmw_1_2.lib.PmwLabeledWidget.LabeledWidget
](/_Pmw.Pmw_1_2.lib.PmwLabeledWidget.html) ( [
_Pmw.Pmw_1_2.lib.PmwBase.MegaWidget ](/_Pmw.Pmw_1_2.lib.PmwBase.html) )

    

[ SingleEditor ](/vcs.templateeditorgui.html)

    

[ CounterEditor ](/vcs.templateeditorgui.html)

[ FloatEditor ](/vcs.templateeditorgui.html)

[ SelectionEditor ](/vcs.templateeditorgui.html)

[ TemplateEditor ](/vcs.templateeditorgui.html)

  
class  CounterEditor  ( [ SingleEditor ](/vcs.templateeditorgui.html) )

` `

Method resolution order:

     [ CounterEditor ](/vcs.templateeditorgui.html)
     [ SingleEditor ](/vcs.templateeditorgui.html)
     [ _Pmw.Pmw_1_2.lib.PmwLabeledWidget.LabeledWidget ](/_Pmw.Pmw_1_2.lib.PmwLabeledWidget.html)
     [ _Pmw.Pmw_1_2.lib.PmwBase.MegaWidget ](/_Pmw.Pmw_1_2.lib.PmwBase.html)
     [ _Pmw.Pmw_1_2.lib.PmwBase.MegaArchetype ](/_Pmw.Pmw_1_2.lib.PmwBase.html)

* * *

Methods defined here:  

 __init__  (self, parent, name, editor) 

 changed  (self) 

 color_field  (self, color) 

 get  (self) 
     ` Return&#160;value `

 set  (self, value) 

* * *

Methods inherited from [ SingleEditor ](/vcs.templateeditorgui.html) :  

 apply  (self) 

 apply_to  (self, ta) 

 is_changed  (self) 

 is_changed_from_original  (self) 

 revert  (self) 

* * *

Methods inherited from [ _Pmw.Pmw_1_2.lib.PmwLabeledWidget.LabeledWidget
](/_Pmw.Pmw_1_2.lib.PmwLabeledWidget.html) :  

 interior  (self) 

* * *

Methods inherited from [ _Pmw.Pmw_1_2.lib.PmwBase.MegaWidget
](/_Pmw.Pmw_1_2.lib.PmwBase.html) :  

 after  (this, *args, kw) 

 after_cancel  (this, *args, kw) 

 after_idle  (this, *args, kw) 

 bbox  (this, *args, kw) 

 bell  (this, *args, kw) 

 bind  (this, *args, kw) 

 bind_all  (this, *args, kw) 

 bind_class  (this, *args, kw) 

 bindtags  (this, *args, kw) 

 clipboard_append  (this, *args, kw) 

 clipboard_clear  (this, *args, kw) 

 colormodel  (this, *args, kw) 

 columnconfigure  (this, *args, kw) 

 config  (this, *args, kw) 

 deletecommand  (this, *args, kw) 

 event_add  (this, *args, kw) 

 event_delete  (this, *args, kw) 

 event_generate  (this, *args, kw) 

 event_info  (this, *args, kw) 

 focus  (this, *args, kw) 

 focus_displayof  (this, *args, kw) 

 focus_force  (this, *args, kw) 

 focus_get  (this, *args, kw) 

 focus_lastfor  (this, *args, kw) 

 focus_set  (this, *args, kw) 

 forget  (this, *args, kw) 

 getboolean  (this, *args, kw) 

 getvar  (this, *args, kw) 

 grab_current  (this, *args, kw) 

 grab_release  (this, *args, kw) 

 grab_set  (this, *args, kw) 

 grab_set_global  (this, *args, kw) 

 grab_status  (this, *args, kw) 

 grid  (this, *args, kw) 

 grid_bbox  (this, *args, kw) 

 grid_columnconfigure  (this, *args, kw) 

 grid_configure  (this, *args, kw) 

 grid_forget  (this, *args, kw) 

 grid_info  (this, *args, kw) 

 grid_location  (this, *args, kw) 

 grid_propagate  (this, *args, kw) 

 grid_remove  (this, *args, kw) 

 grid_rowconfigure  (this, *args, kw) 

 grid_size  (this, *args, kw) 

 grid_slaves  (this, *args, kw) 

 image_names  (this, *args, kw) 

 image_types  (this, *args, kw) 

 info  (this, *args, kw) 

 keys  (this, *args, kw) 

 lift  (this, *args, kw) 

 lower  (this, *args, kw) 

 mainloop  (this, *args, kw) 

 nametowidget  (this, *args, kw) 

 option_add  (this, *args, kw) 

 option_clear  (this, *args, kw) 

 option_get  (this, *args, kw) 

 option_readfile  (this, *args, kw) 

 pack  (this, *args, kw) 

 pack_configure  (this, *args, kw) 

 pack_forget  (this, *args, kw) 

 pack_info  (this, *args, kw) 

 pack_propagate  (this, *args, kw) 

 pack_slaves  (this, *args, kw) 

 place  (this, *args, kw) 

 place_configure  (this, *args, kw) 

 place_forget  (this, *args, kw) 

 place_info  (this, *args, kw) 

 place_slaves  (this, *args, kw) 

 propagate  (this, *args, kw) 

 quit  (this, *args, kw) 

 register  (this, *args, kw) 

 rowconfigure  (this, *args, kw) 

 selection_clear  (this, *args, kw) 

 selection_get  (this, *args, kw) 

 selection_handle  (this, *args, kw) 

 selection_own  (this, *args, kw) 

 selection_own_get  (this, *args, kw) 

 send  (this, *args, kw) 

 setvar  (this, *args, kw) 

 size  (this, *args, kw) 

 slaves  (this, *args, kw) 

 tk_bisque  (this, *args, kw) 

 tk_focusFollowsMouse  (this, *args, kw) 

 tk_focusNext  (this, *args, kw) 

 tk_focusPrev  (this, *args, kw) 

 tk_menuBar  (this, *args, kw) 

 tk_setPalette  (this, *args, kw) 

 tk_strictMotif  (this, *args, kw) 

 tkraise  (this, *args, kw) 

 unbind  (this, *args, kw) 

 unbind_all  (this, *args, kw) 

 unbind_class  (this, *args, kw) 

 update  (this, *args, kw) 

 update_idletasks  (this, *args, kw) 

 wait_variable  (this, *args, kw) 

 wait_visibility  (this, *args, kw) 

 wait_window  (this, *args, kw) 

 waitvar  (this, *args, kw) 

 winfo_atom  (this, *args, kw) 

 winfo_atomname  (this, *args, kw) 

 winfo_cells  (this, *args, kw) 

 winfo_children  (this, *args, kw) 

 winfo_class  (this, *args, kw) 

 winfo_colormapfull  (this, *args, kw) 

 winfo_containing  (this, *args, kw) 

 winfo_depth  (this, *args, kw) 

 winfo_exists  (this, *args, kw) 

 winfo_fpixels  (this, *args, kw) 

 winfo_geometry  (this, *args, kw) 

 winfo_height  (this, *args, kw) 

 winfo_id  (this, *args, kw) 

 winfo_interps  (this, *args, kw) 

 winfo_ismapped  (this, *args, kw) 

 winfo_manager  (this, *args, kw) 

 winfo_name  (this, *args, kw) 

 winfo_parent  (this, *args, kw) 

 winfo_pathname  (this, *args, kw) 

 winfo_pixels  (this, *args, kw) 

 winfo_pointerx  (this, *args, kw) 

 winfo_pointerxy  (this, *args, kw) 

 winfo_pointery  (this, *args, kw) 

 winfo_reqheight  (this, *args, kw) 

 winfo_reqwidth  (this, *args, kw) 

 winfo_rgb  (this, *args, kw) 

 winfo_rootx  (this, *args, kw) 

 winfo_rooty  (this, *args, kw) 

 winfo_screen  (this, *args, kw) 

 winfo_screencells  (this, *args, kw) 

 winfo_screendepth  (this, *args, kw) 

 winfo_screenheight  (this, *args, kw) 

 winfo_screenmmheight  (this, *args, kw) 

 winfo_screenmmwidth  (this, *args, kw) 

 winfo_screenvisual  (this, *args, kw) 

 winfo_screenwidth  (this, *args, kw) 

 winfo_server  (this, *args, kw) 

 winfo_toplevel  (this, *args, kw) 

 winfo_viewable  (this, *args, kw) 

 winfo_visual  (this, *args, kw) 

 winfo_visualid  (this, *args, kw) 

 winfo_visualsavailable  (this, *args, kw) 

 winfo_vrootheight  (this, *args, kw) 

 winfo_vrootwidth  (this, *args, kw) 

 winfo_vrootx  (this, *args, kw) 

 winfo_vrooty  (this, *args, kw) 

 winfo_width  (this, *args, kw) 

 winfo_x  (this, *args, kw) 

 winfo_y  (this, *args, kw) 

* * *

Methods inherited from [ _Pmw.Pmw_1_2.lib.PmwBase.MegaArchetype
](/_Pmw.Pmw_1_2.lib.PmwBase.html) :  

 __getitem__  = cget(self, option) 

 __setitem__  (self, key, value) 

 __str__  (self) 

 addoptions  (self, optionDefs) 

 cget  (self, option) 

 component  (self, name) 

 componentaliases  (self) 

 componentgroup  (self, name) 

 components  (self) 

 configure  (self, option  =None  , kw) 

 createcomponent  (self, componentName, componentAliases, componentGroup, widgetClass, *widgetArgs, kw) 

 createlabel  (self, parent, childCols  =1  , childRows  =1  ) 

 defineoptions  (self, keywords, optionDefs, dynamicGroups  =()  ) 

 destroy  (self) 

 destroycomponent  (self, name) 

 hulldestroyed  (self) 

 initialiseoptions  (self, dummy  =None  ) 

 isinitoption  (self, option) 

 options  (self) 

  
class  FloatEditor  ( [ SingleEditor ](/vcs.templateeditorgui.html) )

` `

Method resolution order:

     [ FloatEditor ](/vcs.templateeditorgui.html)
     [ SingleEditor ](/vcs.templateeditorgui.html)
     [ _Pmw.Pmw_1_2.lib.PmwLabeledWidget.LabeledWidget ](/_Pmw.Pmw_1_2.lib.PmwLabeledWidget.html)
     [ _Pmw.Pmw_1_2.lib.PmwBase.MegaWidget ](/_Pmw.Pmw_1_2.lib.PmwBase.html)
     [ _Pmw.Pmw_1_2.lib.PmwBase.MegaArchetype ](/_Pmw.Pmw_1_2.lib.PmwBase.html)

* * *

Methods defined here:  

 __init__  (self, parent, name, editor) 

 changed  (self) 

 color_field  (self, color) 

 colorize  (self, value) 

 format  (self, value) 

 get  (self) 
     ` Return&#160;value `

 is_changed  (self) 

 is_changed_from_original  (self) 

 set  (self, value) 

* * *

Methods inherited from [ SingleEditor ](/vcs.templateeditorgui.html) :  

 apply  (self) 

 apply_to  (self, ta) 

 revert  (self) 

* * *

Methods inherited from [ _Pmw.Pmw_1_2.lib.PmwLabeledWidget.LabeledWidget
](/_Pmw.Pmw_1_2.lib.PmwLabeledWidget.html) :  

 interior  (self) 

* * *

Methods inherited from [ _Pmw.Pmw_1_2.lib.PmwBase.MegaWidget
](/_Pmw.Pmw_1_2.lib.PmwBase.html) :  

 after  (this, *args, kw) 

 after_cancel  (this, *args, kw) 

 after_idle  (this, *args, kw) 

 bbox  (this, *args, kw) 

 bell  (this, *args, kw) 

 bind  (this, *args, kw) 

 bind_all  (this, *args, kw) 

 bind_class  (this, *args, kw) 

 bindtags  (this, *args, kw) 

 clipboard_append  (this, *args, kw) 

 clipboard_clear  (this, *args, kw) 

 colormodel  (this, *args, kw) 

 columnconfigure  (this, *args, kw) 

 config  (this, *args, kw) 

 deletecommand  (this, *args, kw) 

 event_add  (this, *args, kw) 

 event_delete  (this, *args, kw) 

 event_generate  (this, *args, kw) 

 event_info  (this, *args, kw) 

 focus  (this, *args, kw) 

 focus_displayof  (this, *args, kw) 

 focus_force  (this, *args, kw) 

 focus_get  (this, *args, kw) 

 focus_lastfor  (this, *args, kw) 

 focus_set  (this, *args, kw) 

 forget  (this, *args, kw) 

 getboolean  (this, *args, kw) 

 getvar  (this, *args, kw) 

 grab_current  (this, *args, kw) 

 grab_release  (this, *args, kw) 

 grab_set  (this, *args, kw) 

 grab_set_global  (this, *args, kw) 

 grab_status  (this, *args, kw) 

 grid  (this, *args, kw) 

 grid_bbox  (this, *args, kw) 

 grid_columnconfigure  (this, *args, kw) 

 grid_configure  (this, *args, kw) 

 grid_forget  (this, *args, kw) 

 grid_info  (this, *args, kw) 

 grid_location  (this, *args, kw) 

 grid_propagate  (this, *args, kw) 

 grid_remove  (this, *args, kw) 

 grid_rowconfigure  (this, *args, kw) 

 grid_size  (this, *args, kw) 

 grid_slaves  (this, *args, kw) 

 image_names  (this, *args, kw) 

 image_types  (this, *args, kw) 

 info  (this, *args, kw) 

 keys  (this, *args, kw) 

 lift  (this, *args, kw) 

 lower  (this, *args, kw) 

 mainloop  (this, *args, kw) 

 nametowidget  (this, *args, kw) 

 option_add  (this, *args, kw) 

 option_clear  (this, *args, kw) 

 option_get  (this, *args, kw) 

 option_readfile  (this, *args, kw) 

 pack  (this, *args, kw) 

 pack_configure  (this, *args, kw) 

 pack_forget  (this, *args, kw) 

 pack_info  (this, *args, kw) 

 pack_propagate  (this, *args, kw) 

 pack_slaves  (this, *args, kw) 

 place  (this, *args, kw) 

 place_configure  (this, *args, kw) 

 place_forget  (this, *args, kw) 

 place_info  (this, *args, kw) 

 place_slaves  (this, *args, kw) 

 propagate  (this, *args, kw) 

 quit  (this, *args, kw) 

 register  (this, *args, kw) 

 rowconfigure  (this, *args, kw) 

 selection_clear  (this, *args, kw) 

 selection_get  (this, *args, kw) 

 selection_handle  (this, *args, kw) 

 selection_own  (this, *args, kw) 

 selection_own_get  (this, *args, kw) 

 send  (this, *args, kw) 

 setvar  (this, *args, kw) 

 size  (this, *args, kw) 

 slaves  (this, *args, kw) 

 tk_bisque  (this, *args, kw) 

 tk_focusFollowsMouse  (this, *args, kw) 

 tk_focusNext  (this, *args, kw) 

 tk_focusPrev  (this, *args, kw) 

 tk_menuBar  (this, *args, kw) 

 tk_setPalette  (this, *args, kw) 

 tk_strictMotif  (this, *args, kw) 

 tkraise  (this, *args, kw) 

 unbind  (this, *args, kw) 

 unbind_all  (this, *args, kw) 

 unbind_class  (this, *args, kw) 

 update  (this, *args, kw) 

 update_idletasks  (this, *args, kw) 

 wait_variable  (this, *args, kw) 

 wait_visibility  (this, *args, kw) 

 wait_window  (this, *args, kw) 

 waitvar  (this, *args, kw) 

 winfo_atom  (this, *args, kw) 

 winfo_atomname  (this, *args, kw) 

 winfo_cells  (this, *args, kw) 

 winfo_children  (this, *args, kw) 

 winfo_class  (this, *args, kw) 

 winfo_colormapfull  (this, *args, kw) 

 winfo_containing  (this, *args, kw) 

 winfo_depth  (this, *args, kw) 

 winfo_exists  (this, *args, kw) 

 winfo_fpixels  (this, *args, kw) 

 winfo_geometry  (this, *args, kw) 

 winfo_height  (this, *args, kw) 

 winfo_id  (this, *args, kw) 

 winfo_interps  (this, *args, kw) 

 winfo_ismapped  (this, *args, kw) 

 winfo_manager  (this, *args, kw) 

 winfo_name  (this, *args, kw) 

 winfo_parent  (this, *args, kw) 

 winfo_pathname  (this, *args, kw) 

 winfo_pixels  (this, *args, kw) 

 winfo_pointerx  (this, *args, kw) 

 winfo_pointerxy  (this, *args, kw) 

 winfo_pointery  (this, *args, kw) 

 winfo_reqheight  (this, *args, kw) 

 winfo_reqwidth  (this, *args, kw) 

 winfo_rgb  (this, *args, kw) 

 winfo_rootx  (this, *args, kw) 

 winfo_rooty  (this, *args, kw) 

 winfo_screen  (this, *args, kw) 

 winfo_screencells  (this, *args, kw) 

 winfo_screendepth  (this, *args, kw) 

 winfo_screenheight  (this, *args, kw) 

 winfo_screenmmheight  (this, *args, kw) 

 winfo_screenmmwidth  (this, *args, kw) 

 winfo_screenvisual  (this, *args, kw) 

 winfo_screenwidth  (this, *args, kw) 

 winfo_server  (this, *args, kw) 

 winfo_toplevel  (this, *args, kw) 

 winfo_viewable  (this, *args, kw) 

 winfo_visual  (this, *args, kw) 

 winfo_visualid  (this, *args, kw) 

 winfo_visualsavailable  (this, *args, kw) 

 winfo_vrootheight  (this, *args, kw) 

 winfo_vrootwidth  (this, *args, kw) 

 winfo_vrootx  (this, *args, kw) 

 winfo_vrooty  (this, *args, kw) 

 winfo_width  (this, *args, kw) 

 winfo_x  (this, *args, kw) 

 winfo_y  (this, *args, kw) 

* * *

Methods inherited from [ _Pmw.Pmw_1_2.lib.PmwBase.MegaArchetype
](/_Pmw.Pmw_1_2.lib.PmwBase.html) :  

 __getitem__  = cget(self, option) 

 __setitem__  (self, key, value) 

 __str__  (self) 

 addoptions  (self, optionDefs) 

 cget  (self, option) 

 component  (self, name) 

 componentaliases  (self) 

 componentgroup  (self, name) 

 components  (self) 

 configure  (self, option  =None  , kw) 

 createcomponent  (self, componentName, componentAliases, componentGroup, widgetClass, *widgetArgs, kw) 

 createlabel  (self, parent, childCols  =1  , childRows  =1  ) 

 defineoptions  (self, keywords, optionDefs, dynamicGroups  =()  ) 

 destroy  (self) 

 destroycomponent  (self, name) 

 hulldestroyed  (self) 

 initialiseoptions  (self, dummy  =None  ) 

 isinitoption  (self, option) 

 options  (self) 

  
class  SelectionEditor  ( [ SingleEditor ](/vcs.templateeditorgui.html) )

` `

Method resolution order:

     [ SelectionEditor ](/vcs.templateeditorgui.html)
     [ SingleEditor ](/vcs.templateeditorgui.html)
     [ _Pmw.Pmw_1_2.lib.PmwLabeledWidget.LabeledWidget ](/_Pmw.Pmw_1_2.lib.PmwLabeledWidget.html)
     [ _Pmw.Pmw_1_2.lib.PmwBase.MegaWidget ](/_Pmw.Pmw_1_2.lib.PmwBase.html)
     [ _Pmw.Pmw_1_2.lib.PmwBase.MegaArchetype ](/_Pmw.Pmw_1_2.lib.PmwBase.html)

* * *

Methods defined here:  

 __init__  (self, parent, name, editor) 

 changed  (self, value) 

 color_field  (self, color) 

 get  (self) 
     ` Return&#160;value `

 set  (self, value) 

* * *

Methods inherited from [ SingleEditor ](/vcs.templateeditorgui.html) :  

 apply  (self) 

 apply_to  (self, ta) 

 is_changed  (self) 

 is_changed_from_original  (self) 

 revert  (self) 

* * *

Methods inherited from [ _Pmw.Pmw_1_2.lib.PmwLabeledWidget.LabeledWidget
](/_Pmw.Pmw_1_2.lib.PmwLabeledWidget.html) :  

 interior  (self) 

* * *

Methods inherited from [ _Pmw.Pmw_1_2.lib.PmwBase.MegaWidget
](/_Pmw.Pmw_1_2.lib.PmwBase.html) :  

 after  (this, *args, kw) 

 after_cancel  (this, *args, kw) 

 after_idle  (this, *args, kw) 

 bbox  (this, *args, kw) 

 bell  (this, *args, kw) 

 bind  (this, *args, kw) 

 bind_all  (this, *args, kw) 

 bind_class  (this, *args, kw) 

 bindtags  (this, *args, kw) 

 clipboard_append  (this, *args, kw) 

 clipboard_clear  (this, *args, kw) 

 colormodel  (this, *args, kw) 

 columnconfigure  (this, *args, kw) 

 config  (this, *args, kw) 

 deletecommand  (this, *args, kw) 

 event_add  (this, *args, kw) 

 event_delete  (this, *args, kw) 

 event_generate  (this, *args, kw) 

 event_info  (this, *args, kw) 

 focus  (this, *args, kw) 

 focus_displayof  (this, *args, kw) 

 focus_force  (this, *args, kw) 

 focus_get  (this, *args, kw) 

 focus_lastfor  (this, *args, kw) 

 focus_set  (this, *args, kw) 

 forget  (this, *args, kw) 

 getboolean  (this, *args, kw) 

 getvar  (this, *args, kw) 

 grab_current  (this, *args, kw) 

 grab_release  (this, *args, kw) 

 grab_set  (this, *args, kw) 

 grab_set_global  (this, *args, kw) 

 grab_status  (this, *args, kw) 

 grid  (this, *args, kw) 

 grid_bbox  (this, *args, kw) 

 grid_columnconfigure  (this, *args, kw) 

 grid_configure  (this, *args, kw) 

 grid_forget  (this, *args, kw) 

 grid_info  (this, *args, kw) 

 grid_location  (this, *args, kw) 

 grid_propagate  (this, *args, kw) 

 grid_remove  (this, *args, kw) 

 grid_rowconfigure  (this, *args, kw) 

 grid_size  (this, *args, kw) 

 grid_slaves  (this, *args, kw) 

 image_names  (this, *args, kw) 

 image_types  (this, *args, kw) 

 info  (this, *args, kw) 

 keys  (this, *args, kw) 

 lift  (this, *args, kw) 

 lower  (this, *args, kw) 

 mainloop  (this, *args, kw) 

 nametowidget  (this, *args, kw) 

 option_add  (this, *args, kw) 

 option_clear  (this, *args, kw) 

 option_get  (this, *args, kw) 

 option_readfile  (this, *args, kw) 

 pack  (this, *args, kw) 

 pack_configure  (this, *args, kw) 

 pack_forget  (this, *args, kw) 

 pack_info  (this, *args, kw) 

 pack_propagate  (this, *args, kw) 

 pack_slaves  (this, *args, kw) 

 place  (this, *args, kw) 

 place_configure  (this, *args, kw) 

 place_forget  (this, *args, kw) 

 place_info  (this, *args, kw) 

 place_slaves  (this, *args, kw) 

 propagate  (this, *args, kw) 

 quit  (this, *args, kw) 

 register  (this, *args, kw) 

 rowconfigure  (this, *args, kw) 

 selection_clear  (this, *args, kw) 

 selection_get  (this, *args, kw) 

 selection_handle  (this, *args, kw) 

 selection_own  (this, *args, kw) 

 selection_own_get  (this, *args, kw) 

 send  (this, *args, kw) 

 setvar  (this, *args, kw) 

 size  (this, *args, kw) 

 slaves  (this, *args, kw) 

 tk_bisque  (this, *args, kw) 

 tk_focusFollowsMouse  (this, *args, kw) 

 tk_focusNext  (this, *args, kw) 

 tk_focusPrev  (this, *args, kw) 

 tk_menuBar  (this, *args, kw) 

 tk_setPalette  (this, *args, kw) 

 tk_strictMotif  (this, *args, kw) 

 tkraise  (this, *args, kw) 

 unbind  (this, *args, kw) 

 unbind_all  (this, *args, kw) 

 unbind_class  (this, *args, kw) 

 update  (this, *args, kw) 

 update_idletasks  (this, *args, kw) 

 wait_variable  (this, *args, kw) 

 wait_visibility  (this, *args, kw) 

 wait_window  (this, *args, kw) 

 waitvar  (this, *args, kw) 

 winfo_atom  (this, *args, kw) 

 winfo_atomname  (this, *args, kw) 

 winfo_cells  (this, *args, kw) 

 winfo_children  (this, *args, kw) 

 winfo_class  (this, *args, kw) 

 winfo_colormapfull  (this, *args, kw) 

 winfo_containing  (this, *args, kw) 

 winfo_depth  (this, *args, kw) 

 winfo_exists  (this, *args, kw) 

 winfo_fpixels  (this, *args, kw) 

 winfo_geometry  (this, *args, kw) 

 winfo_height  (this, *args, kw) 

 winfo_id  (this, *args, kw) 

 winfo_interps  (this, *args, kw) 

 winfo_ismapped  (this, *args, kw) 

 winfo_manager  (this, *args, kw) 

 winfo_name  (this, *args, kw) 

 winfo_parent  (this, *args, kw) 

 winfo_pathname  (this, *args, kw) 

 winfo_pixels  (this, *args, kw) 

 winfo_pointerx  (this, *args, kw) 

 winfo_pointerxy  (this, *args, kw) 

 winfo_pointery  (this, *args, kw) 

 winfo_reqheight  (this, *args, kw) 

 winfo_reqwidth  (this, *args, kw) 

 winfo_rgb  (this, *args, kw) 

 winfo_rootx  (this, *args, kw) 

 winfo_rooty  (this, *args, kw) 

 winfo_screen  (this, *args, kw) 

 winfo_screencells  (this, *args, kw) 

 winfo_screendepth  (this, *args, kw) 

 winfo_screenheight  (this, *args, kw) 

 winfo_screenmmheight  (this, *args, kw) 

 winfo_screenmmwidth  (this, *args, kw) 

 winfo_screenvisual  (this, *args, kw) 

 winfo_screenwidth  (this, *args, kw) 

 winfo_server  (this, *args, kw) 

 winfo_toplevel  (this, *args, kw) 

 winfo_viewable  (this, *args, kw) 

 winfo_visual  (this, *args, kw) 

 winfo_visualid  (this, *args, kw) 

 winfo_visualsavailable  (this, *args, kw) 

 winfo_vrootheight  (this, *args, kw) 

 winfo_vrootwidth  (this, *args, kw) 

 winfo_vrootx  (this, *args, kw) 

 winfo_vrooty  (this, *args, kw) 

 winfo_width  (this, *args, kw) 

 winfo_x  (this, *args, kw) 

 winfo_y  (this, *args, kw) 

* * *

Methods inherited from [ _Pmw.Pmw_1_2.lib.PmwBase.MegaArchetype
](/_Pmw.Pmw_1_2.lib.PmwBase.html) :  

 __getitem__  = cget(self, option) 

 __setitem__  (self, key, value) 

 __str__  (self) 

 addoptions  (self, optionDefs) 

 cget  (self, option) 

 component  (self, name) 

 componentaliases  (self) 

 componentgroup  (self, name) 

 components  (self) 

 configure  (self, option  =None  , kw) 

 createcomponent  (self, componentName, componentAliases, componentGroup, widgetClass, *widgetArgs, kw) 

 createlabel  (self, parent, childCols  =1  , childRows  =1  ) 

 defineoptions  (self, keywords, optionDefs, dynamicGroups  =()  ) 

 destroy  (self) 

 destroycomponent  (self, name) 

 hulldestroyed  (self) 

 initialiseoptions  (self, dummy  =None  ) 

 isinitoption  (self, option) 

 options  (self) 

  
class  SingleEditor  ( [ _Pmw.Pmw_1_2.lib.PmwLabeledWidget.LabeledWidget
](/_Pmw.Pmw_1_2.lib.PmwLabeledWidget.html) )

` `

` An&#160;editor&#160;for&#160;a&#160;single&#160;quantity.  
`

Method resolution order:

     [ SingleEditor ](/vcs.templateeditorgui.html)
     [ _Pmw.Pmw_1_2.lib.PmwLabeledWidget.LabeledWidget ](/_Pmw.Pmw_1_2.lib.PmwLabeledWidget.html)
     [ _Pmw.Pmw_1_2.lib.PmwBase.MegaWidget ](/_Pmw.Pmw_1_2.lib.PmwBase.html)
     [ _Pmw.Pmw_1_2.lib.PmwBase.MegaArchetype ](/_Pmw.Pmw_1_2.lib.PmwBase.html)

* * *

Methods defined here:  

 __init__  (self, parent, name, editor) 

 apply  (self) 

 apply_to  (self, ta) 

 color_field  (self, color) 

 is_changed  (self) 

 is_changed_from_original  (self) 

 revert  (self) 

* * *

Methods inherited from [ _Pmw.Pmw_1_2.lib.PmwLabeledWidget.LabeledWidget
](/_Pmw.Pmw_1_2.lib.PmwLabeledWidget.html) :  

 interior  (self) 

* * *

Methods inherited from [ _Pmw.Pmw_1_2.lib.PmwBase.MegaWidget
](/_Pmw.Pmw_1_2.lib.PmwBase.html) :  

 after  (this, *args, kw) 

 after_cancel  (this, *args, kw) 

 after_idle  (this, *args, kw) 

 bbox  (this, *args, kw) 

 bell  (this, *args, kw) 

 bind  (this, *args, kw) 

 bind_all  (this, *args, kw) 

 bind_class  (this, *args, kw) 

 bindtags  (this, *args, kw) 

 clipboard_append  (this, *args, kw) 

 clipboard_clear  (this, *args, kw) 

 colormodel  (this, *args, kw) 

 columnconfigure  (this, *args, kw) 

 config  (this, *args, kw) 

 deletecommand  (this, *args, kw) 

 event_add  (this, *args, kw) 

 event_delete  (this, *args, kw) 

 event_generate  (this, *args, kw) 

 event_info  (this, *args, kw) 

 focus  (this, *args, kw) 

 focus_displayof  (this, *args, kw) 

 focus_force  (this, *args, kw) 

 focus_get  (this, *args, kw) 

 focus_lastfor  (this, *args, kw) 

 focus_set  (this, *args, kw) 

 forget  (this, *args, kw) 

 getboolean  (this, *args, kw) 

 getvar  (this, *args, kw) 

 grab_current  (this, *args, kw) 

 grab_release  (this, *args, kw) 

 grab_set  (this, *args, kw) 

 grab_set_global  (this, *args, kw) 

 grab_status  (this, *args, kw) 

 grid  (this, *args, kw) 

 grid_bbox  (this, *args, kw) 

 grid_columnconfigure  (this, *args, kw) 

 grid_configure  (this, *args, kw) 

 grid_forget  (this, *args, kw) 

 grid_info  (this, *args, kw) 

 grid_location  (this, *args, kw) 

 grid_propagate  (this, *args, kw) 

 grid_remove  (this, *args, kw) 

 grid_rowconfigure  (this, *args, kw) 

 grid_size  (this, *args, kw) 

 grid_slaves  (this, *args, kw) 

 image_names  (this, *args, kw) 

 image_types  (this, *args, kw) 

 info  (this, *args, kw) 

 keys  (this, *args, kw) 

 lift  (this, *args, kw) 

 lower  (this, *args, kw) 

 mainloop  (this, *args, kw) 

 nametowidget  (this, *args, kw) 

 option_add  (this, *args, kw) 

 option_clear  (this, *args, kw) 

 option_get  (this, *args, kw) 

 option_readfile  (this, *args, kw) 

 pack  (this, *args, kw) 

 pack_configure  (this, *args, kw) 

 pack_forget  (this, *args, kw) 

 pack_info  (this, *args, kw) 

 pack_propagate  (this, *args, kw) 

 pack_slaves  (this, *args, kw) 

 place  (this, *args, kw) 

 place_configure  (this, *args, kw) 

 place_forget  (this, *args, kw) 

 place_info  (this, *args, kw) 

 place_slaves  (this, *args, kw) 

 propagate  (this, *args, kw) 

 quit  (this, *args, kw) 

 register  (this, *args, kw) 

 rowconfigure  (this, *args, kw) 

 selection_clear  (this, *args, kw) 

 selection_get  (this, *args, kw) 

 selection_handle  (this, *args, kw) 

 selection_own  (this, *args, kw) 

 selection_own_get  (this, *args, kw) 

 send  (this, *args, kw) 

 setvar  (this, *args, kw) 

 size  (this, *args, kw) 

 slaves  (this, *args, kw) 

 tk_bisque  (this, *args, kw) 

 tk_focusFollowsMouse  (this, *args, kw) 

 tk_focusNext  (this, *args, kw) 

 tk_focusPrev  (this, *args, kw) 

 tk_menuBar  (this, *args, kw) 

 tk_setPalette  (this, *args, kw) 

 tk_strictMotif  (this, *args, kw) 

 tkraise  (this, *args, kw) 

 unbind  (this, *args, kw) 

 unbind_all  (this, *args, kw) 

 unbind_class  (this, *args, kw) 

 update  (this, *args, kw) 

 update_idletasks  (this, *args, kw) 

 wait_variable  (this, *args, kw) 

 wait_visibility  (this, *args, kw) 

 wait_window  (this, *args, kw) 

 waitvar  (this, *args, kw) 

 winfo_atom  (this, *args, kw) 

 winfo_atomname  (this, *args, kw) 

 winfo_cells  (this, *args, kw) 

 winfo_children  (this, *args, kw) 

 winfo_class  (this, *args, kw) 

 winfo_colormapfull  (this, *args, kw) 

 winfo_containing  (this, *args, kw) 

 winfo_depth  (this, *args, kw) 

 winfo_exists  (this, *args, kw) 

 winfo_fpixels  (this, *args, kw) 

 winfo_geometry  (this, *args, kw) 

 winfo_height  (this, *args, kw) 

 winfo_id  (this, *args, kw) 

 winfo_interps  (this, *args, kw) 

 winfo_ismapped  (this, *args, kw) 

 winfo_manager  (this, *args, kw) 

 winfo_name  (this, *args, kw) 

 winfo_parent  (this, *args, kw) 

 winfo_pathname  (this, *args, kw) 

 winfo_pixels  (this, *args, kw) 

 winfo_pointerx  (this, *args, kw) 

 winfo_pointerxy  (this, *args, kw) 

 winfo_pointery  (this, *args, kw) 

 winfo_reqheight  (this, *args, kw) 

 winfo_reqwidth  (this, *args, kw) 

 winfo_rgb  (this, *args, kw) 

 winfo_rootx  (this, *args, kw) 

 winfo_rooty  (this, *args, kw) 

 winfo_screen  (this, *args, kw) 

 winfo_screencells  (this, *args, kw) 

 winfo_screendepth  (this, *args, kw) 

 winfo_screenheight  (this, *args, kw) 

 winfo_screenmmheight  (this, *args, kw) 

 winfo_screenmmwidth  (this, *args, kw) 

 winfo_screenvisual  (this, *args, kw) 

 winfo_screenwidth  (this, *args, kw) 

 winfo_server  (this, *args, kw) 

 winfo_toplevel  (this, *args, kw) 

 winfo_viewable  (this, *args, kw) 

 winfo_visual  (this, *args, kw) 

 winfo_visualid  (this, *args, kw) 

 winfo_visualsavailable  (this, *args, kw) 

 winfo_vrootheight  (this, *args, kw) 

 winfo_vrootwidth  (this, *args, kw) 

 winfo_vrootx  (this, *args, kw) 

 winfo_vrooty  (this, *args, kw) 

 winfo_width  (this, *args, kw) 

 winfo_x  (this, *args, kw) 

 winfo_y  (this, *args, kw) 

* * *

Methods inherited from [ _Pmw.Pmw_1_2.lib.PmwBase.MegaArchetype
](/_Pmw.Pmw_1_2.lib.PmwBase.html) :  

 __getitem__  = cget(self, option) 

 __setitem__  (self, key, value) 

 __str__  (self) 

 addoptions  (self, optionDefs) 

 cget  (self, option) 

 component  (self, name) 

 componentaliases  (self) 

 componentgroup  (self, name) 

 components  (self) 

 configure  (self, option  =None  , kw) 

 createcomponent  (self, componentName, componentAliases, componentGroup, widgetClass, *widgetArgs, kw) 

 createlabel  (self, parent, childCols  =1  , childRows  =1  ) 

 defineoptions  (self, keywords, optionDefs, dynamicGroups  =()  ) 

 destroy  (self) 

 destroycomponent  (self, name) 

 hulldestroyed  (self) 

 initialiseoptions  (self, dummy  =None  ) 

 isinitoption  (self, option) 

 options  (self) 

  
class  TemplateAttributeEditor  ( [ _Pmw.Pmw_1_2.lib.PmwGroup.Group
](/_Pmw.Pmw_1_2.lib.PmwGroup.html) )

` `

` An&#160;entry&#160;widget&#160;for&#160;an&#160;attribute&#160;of&#160;the&#160;template.  
`

Method resolution order:

     [ TemplateAttributeEditor ](/vcs.templateeditorgui.html)
     [ _Pmw.Pmw_1_2.lib.PmwGroup.Group ](/_Pmw.Pmw_1_2.lib.PmwGroup.html)
     [ _Pmw.Pmw_1_2.lib.PmwBase.MegaWidget ](/_Pmw.Pmw_1_2.lib.PmwBase.html)
     [ _Pmw.Pmw_1_2.lib.PmwBase.MegaArchetype ](/_Pmw.Pmw_1_2.lib.PmwBase.html)

* * *

Methods defined here:  

 __init__  (self, parent, template_editor, v, members) 

 apply  (self) 
     ` Save&#160;the&#160;value&#160;from&#160;the&#160;display&#160;into&#160;the&#160;template. `

 apply_to  (self, t) 
     ` Save&#160;the&#160;value&#160;from&#160;the&#160;display&#160;into&#160;the&#160;template&#160;t. `

 is_changed  (self) 
     ` Are&#160;any&#160;of&#160;the&#160;entries&#160;of&#160;this&#160;attribute&#160;changed? `

 is_changed_from_original  (self) 
     ` Are&#160;any&#160;of&#160;the&#160;entries&#160;of&#160;this&#160;attribute&#160;changed? `

 priority_check  (self) 

 revert  (self) 
     ` Set&#160;everything&#160;back&#160;to&#160;the&#160;original&#160;value. `

* * *

Methods inherited from [ _Pmw.Pmw_1_2.lib.PmwGroup.Group
](/_Pmw.Pmw_1_2.lib.PmwGroup.html) :  

 collapse  (self) 

 expand  (self) 

 interior  (self) 

 toggle  (self) 

* * *

Methods inherited from [ _Pmw.Pmw_1_2.lib.PmwBase.MegaWidget
](/_Pmw.Pmw_1_2.lib.PmwBase.html) :  

 after  (this, *args, kw) 

 after_cancel  (this, *args, kw) 

 after_idle  (this, *args, kw) 

 bbox  (this, *args, kw) 

 bell  (this, *args, kw) 

 bind  (this, *args, kw) 

 bind_all  (this, *args, kw) 

 bind_class  (this, *args, kw) 

 bindtags  (this, *args, kw) 

 clipboard_append  (this, *args, kw) 

 clipboard_clear  (this, *args, kw) 

 colormodel  (this, *args, kw) 

 columnconfigure  (this, *args, kw) 

 config  (this, *args, kw) 

 deletecommand  (this, *args, kw) 

 event_add  (this, *args, kw) 

 event_delete  (this, *args, kw) 

 event_generate  (this, *args, kw) 

 event_info  (this, *args, kw) 

 focus  (this, *args, kw) 

 focus_displayof  (this, *args, kw) 

 focus_force  (this, *args, kw) 

 focus_get  (this, *args, kw) 

 focus_lastfor  (this, *args, kw) 

 focus_set  (this, *args, kw) 

 forget  (this, *args, kw) 

 getboolean  (this, *args, kw) 

 getvar  (this, *args, kw) 

 grab_current  (this, *args, kw) 

 grab_release  (this, *args, kw) 

 grab_set  (this, *args, kw) 

 grab_set_global  (this, *args, kw) 

 grab_status  (this, *args, kw) 

 grid  (this, *args, kw) 

 grid_bbox  (this, *args, kw) 

 grid_columnconfigure  (this, *args, kw) 

 grid_configure  (this, *args, kw) 

 grid_forget  (this, *args, kw) 

 grid_info  (this, *args, kw) 

 grid_location  (this, *args, kw) 

 grid_propagate  (this, *args, kw) 

 grid_remove  (this, *args, kw) 

 grid_rowconfigure  (this, *args, kw) 

 grid_size  (this, *args, kw) 

 grid_slaves  (this, *args, kw) 

 image_names  (this, *args, kw) 

 image_types  (this, *args, kw) 

 info  (this, *args, kw) 

 keys  (this, *args, kw) 

 lift  (this, *args, kw) 

 lower  (this, *args, kw) 

 mainloop  (this, *args, kw) 

 nametowidget  (this, *args, kw) 

 option_add  (this, *args, kw) 

 option_clear  (this, *args, kw) 

 option_get  (this, *args, kw) 

 option_readfile  (this, *args, kw) 

 pack  (this, *args, kw) 

 pack_configure  (this, *args, kw) 

 pack_forget  (this, *args, kw) 

 pack_info  (this, *args, kw) 

 pack_propagate  (this, *args, kw) 

 pack_slaves  (this, *args, kw) 

 place  (this, *args, kw) 

 place_configure  (this, *args, kw) 

 place_forget  (this, *args, kw) 

 place_info  (this, *args, kw) 

 place_slaves  (this, *args, kw) 

 propagate  (this, *args, kw) 

 quit  (this, *args, kw) 

 register  (this, *args, kw) 

 rowconfigure  (this, *args, kw) 

 selection_clear  (this, *args, kw) 

 selection_get  (this, *args, kw) 

 selection_handle  (this, *args, kw) 

 selection_own  (this, *args, kw) 

 selection_own_get  (this, *args, kw) 

 send  (this, *args, kw) 

 setvar  (this, *args, kw) 

 size  (this, *args, kw) 

 slaves  (this, *args, kw) 

 tk_bisque  (this, *args, kw) 

 tk_focusFollowsMouse  (this, *args, kw) 

 tk_focusNext  (this, *args, kw) 

 tk_focusPrev  (this, *args, kw) 

 tk_menuBar  (this, *args, kw) 

 tk_setPalette  (this, *args, kw) 

 tk_strictMotif  (this, *args, kw) 

 tkraise  (this, *args, kw) 

 unbind  (this, *args, kw) 

 unbind_all  (this, *args, kw) 

 unbind_class  (this, *args, kw) 

 update  (this, *args, kw) 

 update_idletasks  (this, *args, kw) 

 wait_variable  (this, *args, kw) 

 wait_visibility  (this, *args, kw) 

 wait_window  (this, *args, kw) 

 waitvar  (this, *args, kw) 

 winfo_atom  (this, *args, kw) 

 winfo_atomname  (this, *args, kw) 

 winfo_cells  (this, *args, kw) 

 winfo_children  (this, *args, kw) 

 winfo_class  (this, *args, kw) 

 winfo_colormapfull  (this, *args, kw) 

 winfo_containing  (this, *args, kw) 

 winfo_depth  (this, *args, kw) 

 winfo_exists  (this, *args, kw) 

 winfo_fpixels  (this, *args, kw) 

 winfo_geometry  (this, *args, kw) 

 winfo_height  (this, *args, kw) 

 winfo_id  (this, *args, kw) 

 winfo_interps  (this, *args, kw) 

 winfo_ismapped  (this, *args, kw) 

 winfo_manager  (this, *args, kw) 

 winfo_name  (this, *args, kw) 

 winfo_parent  (this, *args, kw) 

 winfo_pathname  (this, *args, kw) 

 winfo_pixels  (this, *args, kw) 

 winfo_pointerx  (this, *args, kw) 

 winfo_pointerxy  (this, *args, kw) 

 winfo_pointery  (this, *args, kw) 

 winfo_reqheight  (this, *args, kw) 

 winfo_reqwidth  (this, *args, kw) 

 winfo_rgb  (this, *args, kw) 

 winfo_rootx  (this, *args, kw) 

 winfo_rooty  (this, *args, kw) 

 winfo_screen  (this, *args, kw) 

 winfo_screencells  (this, *args, kw) 

 winfo_screendepth  (this, *args, kw) 

 winfo_screenheight  (this, *args, kw) 

 winfo_screenmmheight  (this, *args, kw) 

 winfo_screenmmwidth  (this, *args, kw) 

 winfo_screenvisual  (this, *args, kw) 

 winfo_screenwidth  (this, *args, kw) 

 winfo_server  (this, *args, kw) 

 winfo_toplevel  (this, *args, kw) 

 winfo_viewable  (this, *args, kw) 

 winfo_visual  (this, *args, kw) 

 winfo_visualid  (this, *args, kw) 

 winfo_visualsavailable  (this, *args, kw) 

 winfo_vrootheight  (this, *args, kw) 

 winfo_vrootwidth  (this, *args, kw) 

 winfo_vrootx  (this, *args, kw) 

 winfo_vrooty  (this, *args, kw) 

 winfo_width  (this, *args, kw) 

 winfo_x  (this, *args, kw) 

 winfo_y  (this, *args, kw) 

* * *

Methods inherited from [ _Pmw.Pmw_1_2.lib.PmwBase.MegaArchetype
](/_Pmw.Pmw_1_2.lib.PmwBase.html) :  

 __getitem__  = cget(self, option) 

 __setitem__  (self, key, value) 

 __str__  (self) 

 addoptions  (self, optionDefs) 

 cget  (self, option) 

 component  (self, name) 

 componentaliases  (self) 

 componentgroup  (self, name) 

 components  (self) 

 configure  (self, option  =None  , kw) 

 createcomponent  (self, componentName, componentAliases, componentGroup, widgetClass, *widgetArgs, kw) 

 createlabel  (self, parent, childCols  =1  , childRows  =1  ) 

 defineoptions  (self, keywords, optionDefs, dynamicGroups  =()  ) 

 destroy  (self) 

 destroycomponent  (self, name) 

 hulldestroyed  (self) 

 initialiseoptions  (self, dummy  =None  ) 

 isinitoption  (self, option) 

 options  (self) 

  
class  TemplateEditor 

` `

` Template&#160;editor&#160;gui.  
`

Methods defined here:  

 __init__  (self, canvas  =None  , template_name  =''  , gui_parent  =None  , gm  ='isofill'  , gm_name  ='default'  ) 

 apply  (self) 

 ask_save  (self) 
     ` Ask&#160;user&#160;if&#160;he&#160;wants&#160;to&#160;save&#160;changes,&#160;if&#160;necessary. `

 ask_save_execute  (self, name) 

 button_dispatch  (self, name) 

 close  (self) 

 create_dialogs  (self) 
     ` Create&#160;the&#160;dialogs&#160;to&#160;be&#160;raised&#160;and&#160;lowered&#160;as&#160;required. `

 create_filemenu  (self, main_menu, canvas) 

 create_help_menu  (self, main_menu) 

 create_page  (self, name) 

 editor_page  (self, name, list2d) 

 evt_about_dialog  (self) 

 evt_command_summary  (self) 

 exit_editor  (self) 
     ` Invoked&#160;for&#160;exit&#160;and&#160;the&#160;cancel&#160;button `

 is_changed  (self) 
     ` Has&#160;a&#160;modification&#160;been&#160;made? `

 is_changed_from_original  (self) 
     ` Has&#160;a&#160;modification&#160;been&#160;made&#160;from&#160;the&#160;original? `

 is_opened  (self) 
     ` Is&#160;this&#160;editor&#160;open&#160;now? `

 makepages  (self, name) 
     ` This&#160;is&#160;called&#160;the&#160;first&#160;time&#160;a&#160;given&#160;page&#160;is&#160;selected. `

 new_window  (self, template_name  =''  ) 

 ok  (self) 

 open  (self) 

 process_template_choice  (self, result) 

 refresh_data  (self, attr_name, mem_name, value) 

 revert  (self) 

 save  (self) 
     ` Apply&#160;to&#160;template.&#160;Returns&#160;1&#160;if&#160;save&#160;was&#160;legal. `

 saveas  (self) 

 savesession  (self) 

 set_title  (self) 

 show  (self) 
     ` Show&#160;the&#160;current&#160;situation&#160;on&#160;the&#160;canvas `

 update_template_selector_list  (self) 

* * *

Data and other attributes defined here:  

 balloon_text  = 'This is the VCS template editor. It can edit the...at they were after the template  \n  was last opened.  \n  ' 

 command_summary  = 'Open: Work on a new template; close the curren...o (3)  \n  Session Save sets (1), (2), and (4) to (1)  \n  ' 

  
 Functions 

` `

 create  (canvas  =None  , template_name  =''  , gui_parent  =None  ) 
     ` #&#160;Create/Popup&#160;template&#160;editor&#160;for&#160;VCS. `

  
 Data 

` `

 Pmw  = <Pmw.Pmw_1_2.lib.PmwLoader.PmwLoader instance>   
 attribute_explanations  = {'box1': 'One of four available boxes you can draw', 'box2': 'One of four available boxes you can draw', 'box3': 'One of four available boxes you can draw', 'box4': 'One of four available boxes you can draw', 'comment1': 'One of four available comment lines.', 'comment2': 'One of four available comment lines.', 'comment3': 'One of four available comment lines.', 'comment4': 'One of four available comment lines.', 'crdate': 'Data creation date', 'crtime': 'Data creation time', ...}   
 attribute_labels  = {'source': 'file_comment', 'title': 'long_name'}   
 entry_editors  = {'format': <class vcs.templateeditorgui.SelectionEditor>, 'line': <class vcs.templateeditorgui.SelectionEditor>, 'priority': <class vcs.templateeditorgui.CounterEditor>, 'textorientation': <class vcs.templateeditorgui.SelectionEditor>, 'texttable': <class vcs.templateeditorgui.SelectionEditor>, 'x': <class vcs.templateeditorgui.FloatEditor>, 'x1': <class vcs.templateeditorgui.FloatEditor>, 'x2': <class vcs.templateeditorgui.FloatEditor>, 'y': <class vcs.templateeditorgui.FloatEditor>, 'y1': <class vcs.templateeditorgui.FloatEditor>, ...}   
 entry_labels  = {'format': 'Format', 'line': 'Line', 'priority': 'Priority', 'textorientation': 'Orientation', 'texttable': 'Properties', 'x': 'X', 'x1': 'X1', 'x2': 'X2', 'y': 'Y', 'y1': 'Y1', ...} 

* * *

UCRL-WEB-213937 | [ Privacy & Legal Notice ](/disclaimer.html)

[ webmaster@pcmdi.llnl.gov ](/webmaster@pcmdi.llnl.gov)

[ ![Powered by Plone](media/plone_powered.gif) ](/)

