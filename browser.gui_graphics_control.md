---
layout: default
title:
---

 [ Skip to content. ](/cdat/source/api-
reference/browser.gui_graphics_control.html) | [ Skip to navigation
](/cdat/source/api-reference/browser.gui_graphics_control.html)

Search Site

[ Advanced Search&#8230; ](/search_form)

#  [ PCMDI Software Portal ](/)

#####  Sections

  * [ Home ](/)

#####  Personal tools

  * [ Log in ](/login_form)

You are here:  [ Home ](/) -> [ CDAT ](/cdat) -> [ Source Code ](/cdat/source)
-> [ API Reference ](/cdat/source/api-reference) -> Python: module
browser.gui_graphics_control

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

        * [ Python: module browser.gui_graphics_control ](/cdat/source/api-reference/browser.gui_graphics_control.html)

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

  * [ ![Send this page to somebody](media/mail_icon.gif) ](/cdat/source/api-reference/browser.gui_graphics_control.html/sendto_form)
  * [ ![Print this page](media/print_icon.gif) ](/this.print\(\))

#  Python: module browser.gui_graphics_control

  
  
 [ browser  ](/browser.html) .gui_graphics_control 
[ index ](/)  

` #&#160;The&#160;PCMDI&#160;Data&#160;Browser&#160;Graphics&#160;Control&#160;Panel&#160;-&#160;&#160;gui_graphics_control
module  
#  
##############################################################################
#  
#
#  
#&#160;Module:&#160;&#160;&#160;&#160;&#160;&#160;&#160;gui_graphics_control&#160;module
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
#&#160;Description:&#160;&#160;PCMDI&#160;Software&#160;System&#160;browser&#160;Tkinter&#160;"Graphics&#160;Control"
#  
#&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;panel&#160;&#160;GUI.
#  
#
#  
#&#160;Version:&#160;&#160;&#160;&#160;&#160;&#160;4.0
#  
#
#  
##############################################################################
#  
#  
#---------------------------------------------------------------------  
#&#160;NOTE:&#160;need&#160;to&#160;use&#160;version&#160;of&#160;Python&#160;that&#160;imports&#160;Tkinter&#160;and&#160;Pmw  
#--------------------------------------------------------------------- `

  
 Modules 

` `

[ Tkinter ](/Tkinter.html)  
[ __main__ ](/__main__.html)  
[ browser.gui_alter_plot ](/browser.gui_alter_plot.html)  
[ browser.gui_annotate ](/browser.gui_annotate.html)  
[ browser.gui_busy ](/browser.gui_busy.html)  
[ browser.gui_canvas_geometry ](/browser.gui_canvas_geometry.html)  

[ gui_support.gui_color ](/gui_support.gui_color.html)  
[ browser.gui_control ](/browser.gui_control.html)  
[ browser.gui_defined_variables ](/browser.gui_defined_variables.html)  
[ browser.gui_formulate ](/browser.gui_formulate.html)  
[ browser.gui_functions ](/browser.gui_functions.html)  
[ browser.gui_message ](/browser.gui_message.html)  

[ browser.gui_output ](/browser.gui_output.html)  
[ browser.gui_set_graphics_methods ](/browser.gui_set_graphics_methods.html)  
[ browser.gui_set_min_max_scale ](/browser.gui_set_min_max_scale.html)  
[ gui_support ](/gui_support.html)  
[ os ](/os.html)  
[ string ](/string.html)  

[ sys ](/sys.html)  
[ vcs ](/vcs.html)  
[ browser.vcs_function ](/browser.vcs_function.html)  

  
 Classes 

` `

[ create ](/browser.gui_graphics_control.html)

  
class  create 

` `

` #---------------------------------------------------------------------------  
#  
#&#160;Start&#160;of&#160;the&#160;"Graphics&#160;Control"&#160;panel&#160;GUI&#160;Layout  
#  
#---------------------------------------------------------------------------  
#&#160;Start&#160;the&#160;Tkinter/Pmw&#160;GUI&#160;layout.&#160;The&#160;layout&#160;is&#160;listed&#160;from&#160;top&#160;to&#160;bottom.  
#&#160;Starting&#160;with:&#160;the&#160;menu&#160;bar;&#160;followed&#160;by&#160;the&#160;"Select&#160;Variable"&#160;panel,&#160;which  
#&#160;allows&#160;the&#160;user&#160;to&#160;select&#160;data&#160;from&#160;a&#160;directory&#160;or&#160;a&#160;database;&#160;followed&#160;by  
#&#160;the&#160;"Graphics&#160;Control"&#160;panel,&#160;which&#160;allows&#160;the&#160;user&#160;to&#160;plot&#160;the&#160;selected&#160;or  
#&#160;defined&#160;variables;&#160;followed&#160;by&#160;the&#160;"Dimension"&#160;panel,&#160;which&#160;allows&#160;the&#160;user
to  
#&#160;select&#160;subsets&#160;of&#160;the&#160;selected&#160;variable&#160;before&#160;plotting&#160;or&#160;storing&#160;into
memory;  
#&#160;followed&#160;by&#160;the&#160;"Defined&#160;Variables"&#160;panel,&#160;which&#160;allows&#160;the&#160;user&#160;to&#160;modify
the  
#&#160;variables&#160;that&#160;are&#160;stored&#160;in&#160;memory;&#160;and&#160;finally&#160;followed&#160;by&#160;the&#160;"Variable  
#&#160;Information"&#160;scroll&#160;window,&#160;which&#160;displays&#160;variable&#160;information.  
#  
#&#160;All&#160;panels&#160;are&#160;contained&#160;within&#160;a&#160;paned&#160;widget.&#160;Thus,&#160;allowing&#160;the&#160;size&#160;of  
#&#160;each&#160;section&#160;to&#160;expand&#160;or&#160;constrict.  
#  
#---------------------------------------------------------------------  
#&#160;Begin&#160;the&#160;creation&#160;of&#160;"Graphics&#160;Control"&#160;panel  
#---------------------------------------------------------------------  
`

Methods defined here:  

 __init__  (self, parent) 

 call_do_plot  (self, parent, gm_type  ='Boxfill'  , var_name  =None  , new_form  =0  ) 
     ` #######&#160;call&#160;do&#160;plot   
#&#160;This&#160;function&#160;can&#160;be&#160;called&#160;twice.&#160;Once&#160;for&#160;the&#160;inital&#160;graphics&#160;method&#160;and
second&#160;for&#160;an  
#&#160;overlay&#160;isoline. `

 call_multiple_plot  (self, parent, gm_type  ='Boxfill'  , var_name  =None  , new_form  =0  ) 
     ` #######&#160;call&#160;multiple&#160;plot   
#&#160;This&#160;function&#160;can&#160;be&#160;called&#160;twice.&#160;Once&#160;for&#160;the&#160;inital&#160;graphics&#160;method&#160;and
second&#160;for&#160;an  
#&#160;overlay&#160;isoline. `

 evt_animate  (self, parent) 
     ` #######&#160;event&#160;to&#160;'Animate'&#160;the&#160;VCS&#160;Canvas `

 evt_clear_display  (self, parent) 
     ` #######&#160;event&#160;to&#160;'VCS&#160;Clear&#160;Display' `

 evt_close_canvas  (self, parent) 
     ` #######&#160;event&#160;to&#160;'Close&#160;VCS&#160;Canvas' `

 evt_colormap  (self, parent) 
     ` #######&#160;event&#160;to&#160;pop&#160;up&#160;the&#160;VCS&#160;'Colormap' `

 evt_continents_toggle  (self, parent, number) 
     ` #######&#160;event&#160;to&#160;set&#160;continents&#160;flag&#160;type `

 evt_define  (self, parent, var_name  =None  ) 
     ` #######&#160;event&#160;to&#160;define&#160;a&#160;variable `

 evt_gmeditor  (self, parent) 

 evt_isoline_labels_toggle  (self, parent) 
     ` #######&#160;event&#160;to&#160;set&#160;isoline&#160;labels&#160;flag `

 evt_number_of_plots_on_canvas  (self, parent, number) 
     ` #######&#160;event&#160;to&#160;set&#160;the&#160;nubmer&#160;plots&#160;on&#160;a&#160;VCS&#160;Canvas `

 evt_overlay_toggle  (self, parent) 
     ` #######&#160;event&#160;to&#160;set&#160;overlay&#160;flag `

 evt_page_orientation  (self, parent, orientation) 
     ` #######&#160;event&#160;to&#160;set&#160;page&#160;orientation `

 evt_pageeditor  (self, parent) 

 evt_plot  (self, parent) 
     ` #######&#160;event&#160;to&#160;plot   
#&#160;This&#160;is&#160;called&#160;because&#160;there&#160;is&#160;a&#160;need&#160;for&#160;an&#160;intermediate&#160;step&#160;to&#160;check
whether  
#&#160;an&#160;overlay&#160;is&#160;needed&#160;(i.e.,&#160;FilledIsoline&#160;or&#160;BoxedIsoline).&#160;If&#160;an&#160;overlay&#160;is
needed,  
#&#160;Then&#160;call&#160;"call_do_plot"&#160;twice;&#160;once&#160;for&#160;isofill&#160;or&#160;boxfill;&#160;and&#160;again&#160;for
the&#160;isoline  
#&#160;overlay. `

 evt_set_plot_projection  (self, parent, number) 
     ` #######&#160;event&#160;to&#160;set&#160;the&#160;plot&#160;projection `

 evt_templateeditor  (self, parent) 

 evt_which_graphics_method  (self, parent, event) 
     ` #######&#160;event&#160;to&#160;check&#160;which&#160;graphics&#160;method&#160;is&#160;in&#160;use `

 evt_which_vcs_canvas  (self, parent, event) 
     ` #######&#160;event&#160;to&#160;check&#160;which&#160;VCS&#160;Canvas&#160;is&#160;in&#160;use `

 remove_variable_from_defined_variable_list  (self, parent, remove_variable) 

 turn_off_all_plots  (self, parent) 

 turn_on_listed_plots  (self, parent, on_list) 

 which_plot_is_on  (self, parent) 

  
 Functions 

` `

 remove_graphics_methods  (parent) 

  
 Data 

` `

 Pmw  = <Pmw.Pmw_1_2.lib.PmwLoader.PmwLoader instance>   
 fn  = '/pcmdi/halliday1/PCMDI_GRAPHICS' 

* * *

UCRL-WEB-213937 | [ Privacy & Legal Notice ](/disclaimer.html)

[ webmaster@pcmdi.llnl.gov ](/webmaster@pcmdi.llnl.gov)

[ ![Powered by Plone](media/plone_powered.gif) ](/)

