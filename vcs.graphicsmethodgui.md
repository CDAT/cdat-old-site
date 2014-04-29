---
layout: default
title:
---

 [ Skip to content. ](/cdat/source/api-reference/vcs.graphicsmethodgui.html) |
[ Skip to navigation ](/cdat/source/api-reference/vcs.graphicsmethodgui.html)

Search Site

[ Advanced Search&#8230; ](/search_form)

#  [ PCMDI Software Portal ](/)

#####  Sections

  * [ Home ](/)

#####  Personal tools

  * [ Log in ](/login_form)

You are here:  [ Home ](/) -> [ CDAT ](/cdat) -> [ Source Code ](/cdat/source)
-> [ API Reference ](/cdat/source/api-reference) -> Python: module
vcs.graphicsmethodgui

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

        * [ Python: module vcs.graphicsmethodgui ](/cdat/source/api-reference/vcs.graphicsmethodgui.html)

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

  * [ ![Send this page to somebody](media/mail_icon.gif) ](/cdat/source/api-reference/vcs.graphicsmethodgui.html/sendto_form)
  * [ ![Print this page](media/print_icon.gif) ](/this.print\(\))

#  Python: module vcs.graphicsmethodgui

  
  
 [ vcs  ](/vcs.html) .graphicsmethodgui 
[ index ](/)  

` #&#160;The&#160;VCS&#160;Graphics&#160;Method&#160;GUI&#160;controls&#160;-&#160;&#160;graphicsmethodgui&#160;module  
#  
##############################################################################
#  
#
#  
#&#160;Module:&#160;&#160;&#160;&#160;&#160;&#160;&#160;graphicsmethodgui&#160;module
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
#&#160;Description:&#160;&#160;PCMDI's&#160;VCS&#160;GUI&#160;graphics&#160;method&#160;editor.&#160;Tkinter&#160;version.
#  
#
#  
#&#160;Version:&#160;&#160;&#160;&#160;&#160;&#160;4.0
#  
#
#  
##############################################################################
# `

  
 Modules 

` `

[ Tkinter ](/Tkinter.html)  
[ browser ](/browser.html)  
[ gui_support.gui_color ](/gui_support.gui_color.html)  

[ browser.gui_control ](/browser.gui_control.html)  
[ browser.gui_message ](/browser.gui_message.html)  
[ gui_support ](/gui_support.html)  

[ os ](/os.html)  
[ vcs.projectiongui ](/vcs.projectiongui.html)  
[ string ](/string.html)  

[ sys ](/sys.html)  
[ tkFileDialog ](/tkFileDialog.html)  
[ vcs ](/vcs.html)  

  
 Classes 

` `

[ G_Command ](/vcs.graphicsmethodgui.html)

[ GraphicsMethodGui ](/vcs.graphicsmethodgui.html)

[ create_graphicsmethod_help_menu ](/vcs.graphicsmethodgui.html)

[ hold ](/vcs.graphicsmethodgui.html)

[ pa_attributes ](/vcs.graphicsmethodgui.html)

[ wc_attributes ](/vcs.graphicsmethodgui.html)

[ x_attributes ](/vcs.graphicsmethodgui.html)

[ y_attributes ](/vcs.graphicsmethodgui.html)

  
class  G_Command 

` `

` #---------------------------------------------------------------------------
------  
#&#160;Event&#160;handling&#160;function&#160;that&#160;will&#160;allow&#160;the&#160;passing&#160;of&#160;arguments  
#-----------------------------------------------------------------------------
----  
`

Methods defined here:  

 __call__  (self, *args, kw) 

 __init__  (self, func, *args, kw) 

  
class  GraphicsMethodGui 

` `

Methods defined here:  

 __init__  (self, vcs  =None  , gm_type  ='boxfill'  , gm_name  ='default'  , gui_parent  =None  ) 

 apply  (self, gui_parent) 

 dismiss  (self) 

 execute  (self, gui_parent, result) 

 gm_clear  (self, gui_parent) 

 gm_reset  (self, gui_parent) 

 hold_gm_original_settings  (self, gui_parent) 

  
class  create_graphicsmethod_help_menu 

` `

` #---------------------------------------------------------------------------
-------------  
#&#160;Create&#160;the&#160;graphicsmethod&#160;Help&#160;menu&#160;and&#160;its&#160;menu&#160;items  
#-----------------------------------------------------------------------------
-----------  
`

Methods defined here:  

 __init__  (self, main_menu, eself, parent) 

 evt_about_dialog  (self, eself, parent) 
     ` #&#160;Create&#160;about&#160;grapnics&#160;method&#160;dialog. `

  
class  hold 

` `

  
class  pa_attributes 

` `

Methods defined here:  

 __init__  (self, page, parent, gm, gm_type, canvas, gui_parent) 

 clear  (self) 

 evt_projection  (self, canvas, gui_parent) 

 reset  (self) 

 set  (self, *crapargs) 

  
class  wc_attributes 

` `

Methods defined here:  

 __init__  (self, page, parent, gm) 

 clear  (self) 

 reset  (self) 

 set  (self) 

  
class  x_attributes 

` `

` #---------------------------------------------------------------------------
-------------  
#&#160;Create&#160;the&#160;general&#160;graphics&#160;method&#160;attributes  
#-----------------------------------------------------------------------------
-----------  
`

Methods defined here:  

 __init__  (self, page, parent, gm, vcs) 

 clear  (self) 

 reset  (self) 

 set  (self) 

  
class  y_attributes 

` `

Methods defined here:  

 __init__  (self, page, parent, gm, vcs) 

 clear  (self) 

 reset  (self) 

 set  (self) 

  
 Functions 

` `

 create  (canvas  =None  , gm_type  ='boxfill'  , gm_name  ='default'  , gui_parent  =None  ) 
     ` #&#160;Create/Popup&#160;graphics&#160;method&#160;gui&#160;editor&#160;for&#160;VCS. `

 create_graphicsmethod_file_menu  (main_menu, eself, gui_parent) 
     ` #----------------------------------------------------------------------------------------   
#&#160;Create&#160;the&#160;graphicsmethod&#160;File&#160;menu&#160;and&#160;its&#160;menu&#160;items  
#-----------------------------------------------------------------------------
----------- `

 evt_edit_graphics_methods  (eself, gui_parent) 

 evt_new_graphics_methods  (eself, gui_parent) 

 evt_rename_graphics_methods  (eself, gui_parent) 

 evt_savescript_graphics_methods  (eself, gui_parent) 

 evt_which_edit_graphics_method  (eself, dialog, event) 

 evt_which_graphics_method  (dialog, event) 

 execute_load_selection  (eself, gui_parent, result) 

 execute_new_selection  (eself, gui_parent, hold, result) 

 execute_rename_selection  (eself, gui_parent, hold, result) 

  
 Data 

` `

 Pmw  = <Pmw.Pmw_1_2.lib.PmwLoader.PmwLoader instance>   
 gmchlst  = ['Boxfill', 'Isofill', 'Isoline', 'Outfill', 'Outline', 'Xyvsy', 'Meshfill', 'Yxvsx', 'XvsY', 'Vector', 'Scatter', 'Taylordiagram'] 

* * *

UCRL-WEB-213937 | [ Privacy & Legal Notice ](/disclaimer.html)

[ webmaster@pcmdi.llnl.gov ](/webmaster@pcmdi.llnl.gov)

[ ![Powered by Plone](media/plone_powered.gif) ](/)

