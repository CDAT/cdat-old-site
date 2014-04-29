---
layout: default
title:
---

 [ Skip to content. ](/cdat/source/api-reference/vcs.animationgui.html) | [
Skip to navigation ](/cdat/source/api-reference/vcs.animationgui.html)

Search Site

[ Advanced Search&#8230; ](/search_form)

#  [ PCMDI Software Portal ](/)

#####  Sections

  * [ Home ](/)

#####  Personal tools

  * [ Log in ](/login_form)

You are here:  [ Home ](/) -> [ CDAT ](/cdat) -> [ Source Code ](/cdat/source)
-> [ API Reference ](/cdat/source/api-reference) -> Python: module
vcs.animationgui

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

        * [ Python: module vcs.animationgui ](/cdat/source/api-reference/vcs.animationgui.html)

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

  * [ ![Send this page to somebody](media/mail_icon.gif) ](/cdat/source/api-reference/vcs.animationgui.html/sendto_form)
  * [ ![Print this page](media/print_icon.gif) ](/this.print\(\))

#  Python: module vcs.animationgui

  
  
 [ vcs  ](/vcs.html) .animationgui 
[ index ](/)  

` #&#160;The&#160;VCS&#160;Animation&#160;GUI&#160;controls&#160;-&#160;&#160;animationgui&#160;module  
#  
##############################################################################
###  
#
#  
#&#160;Module:&#160;&#160;&#160;&#160;&#160;&#160;&#160;animationgui&#160;module
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
#&#160;Description:&#160;&#160;PCMDI's&#160;VCS&#160;animation&#160;GUI&#160;browser&#160;and&#160;editor.
#  
#
#  
#&#160;Version:&#160;&#160;&#160;&#160;&#160;&#160;4.0
#  
#
#  
##############################################################################
### `

  
 Modules 

` `

[ Tkinter ](/Tkinter.html)  
[ gui_support ](/gui_support.html)  

[ os ](/os.html)  
[ string ](/string.html)  

[ sys ](/sys.html)  
[ tkFileDialog ](/tkFileDialog.html)  

  
 Classes 

` `

[ A_Command ](/vcs.animationgui.html)

[ AnimationGui ](/vcs.animationgui.html)

[ create_animation_options_menu ](/vcs.animationgui.html)

  
class  A_Command 

` `

` #---------------------------------------------------------------------------
------  
#-----------------------------------------------------------------------------
----  
#  
#&#160;Event&#160;handling&#160;function&#160;that&#160;will&#160;allow&#160;the&#160;passing&#160;of&#160;arguments  
#  
#-----------------------------------------------------------------------------
----  
#-----------------------------------------------------------------------------
----  
`

Methods defined here:  

 __call__  (self, *args, kw) 

 __init__  (self, func, *args, kw) 

  
class  AnimationGui 

` `

` #---------------------------------------------------------------------------
-------------  
#-----------------------------------------------------------------------------
-----------  
#  
#&#160;Create&#160;the&#160;Tkinter/Pmw&#160;Animation&#160;editor&#160;interface  
#  
#-----------------------------------------------------------------------------
-----------  
#-----------------------------------------------------------------------------
-----------  
`

Methods defined here:  

 __init__  (self, animation, gui_parent  =None  , transient  =0  ) 

 create_file_menu  (self, main_menu, gui_parent) 

 create_help_menu  (self, parent, main_menu) 

 destroy_close_animation  (self, gui_parent  =None  ) 

 evt_about_dialog  (self, parent) 

 execute  (self, parent, event) 

  
class  create_animation_options_menu 

` `

` #---------------------------------------------------------------------------
-------------  
#-----------------------------------------------------------------------------
-----------  
#  
#&#160;Create&#160;the&#160;Animation&#160;Options&#160;menu&#160;and&#160;its&#160;menu&#160;items  
#  
#-----------------------------------------------------------------------------
-----------  
#-----------------------------------------------------------------------------
-----------  
`

Methods defined here:  

 __init__  (self, eself, main_menu, parent, animation) 

 evt_set_direction  (self, animation, parent, number) 
     ` #######&#160;event&#160;to&#160;set&#160;the&#160;animation&#160;direction `

 evt_set_min_max  (self, eself, parent, animation) 
     ` #######&#160;event&#160;to&#160;set&#160;the&#160;animation&#160;direction `

 evt_set_mode  (self, animation, parent, number) 
     ` #######&#160;event&#160;to&#160;set&#160;the&#160;animation&#160;mode `

 mmexecute  (self, eself, parent, result) 
     ` #######&#160;event&#160;to&#160;destory&#160;the&#160;set&#160;min&#160;and&#160;max&#160;dialog&#160;panel `

 set_toggle_flg  (self, animation) 
     ` #######&#160;event&#160;to&#160;set&#160;radio&#160;button `

  
 Functions 

` `

 create  (animation_obj, parent  =None  , transient  =0  ) 
     ` #####################################################################################   
#&#160;Create/Popup&#160;animation&#160;GUI&#160;editor&#160;for&#160;VCS
#  
##############################################################################
####### `

 create_animation_control_buttons  (self, parent, gui_parent, animation) 
     ` #----------------------------------------------------------------------------------------   
#-----------------------------------------------------------------------------
-----------  
#  
#&#160;Create&#160;the&#160;animation&#160;control&#160;buttons  
#  
#-----------------------------------------------------------------------------
-----------  
#-----------------------------------------------------------------------------
----------- `

 create_animation_file_controls  (self, parent, gui_parent, animation) 
     ` #----------------------------------------------------------------------------------------   
#-----------------------------------------------------------------------------
-----------  
#  
#&#160;Create&#160;the&#160;animation&#160;file&#160;controls  
#  
#-----------------------------------------------------------------------------
-----------  
#-----------------------------------------------------------------------------
----------- `

 create_control_animation_frame  (self, parent, animation) 
     ` #----------------------------------------------------------------------------------------   
#-----------------------------------------------------------------------------
-----------  
#  
#&#160;Create&#160;the&#160;Animation&#160;"Control&#160;animation&#160;frames"&#160;section  
#  
#-----------------------------------------------------------------------------
-----------  
#-----------------------------------------------------------------------------
----------- `

 create_control_images  (self, parent, gui_parent, animation) 
     ` #####################################################################################   
#&#160;Create&#160;the&#160;images&#160;on&#160;the&#160;VCS&#160;Canvas&#160;for&#160;play&#160;back
#  
##############################################################################
####### `

 create_zoom_and_pan_animation_frame  (self, parent, animation) 
     ` #----------------------------------------------------------------------------------------   
#-----------------------------------------------------------------------------
-----------  
#  
#&#160;Create&#160;the&#160;Animation&#160;"Zoom&#160;and&#160;pan&#160;animation&#160;frames"&#160;section  
#  
#-----------------------------------------------------------------------------
-----------  
#-----------------------------------------------------------------------------
----------- `

 evt_change_hor_cmb  (self, event) 
     ` #####################################################################################   
#&#160;Call&#160;horizontal&#160;widget&#160;event&#160;function&#160;below&#160;to&#160;pan&#160;animation&#160;in&#160;the&#160;x
direction&#160;&#160;&#160;#  
##############################################################################
####### `

 evt_change_hor_scl  (self, animation, event) 
     ` #####################################################################################   
#&#160;Pan&#160;image&#160;frames&#160;in&#160;the&#160;x&#160;direction
#  
##############################################################################
####### `

 evt_change_load_color  (self, parent, event) 

 evt_change_save_color  (self, parent, event) 

 evt_change_ver_cmb  (self, event) 
     ` #####################################################################################   
#&#160;Call&#160;vertical&#160;widget&#160;event&#160;function&#160;below&#160;to&#160;pan&#160;animation&#160;in&#160;the&#160;y
direction&#160;&#160;&#160;&#160;&#160;#  
##############################################################################
####### `

 evt_change_ver_scl  (self, animation, event) 
     ` #####################################################################################   
#&#160;Pan&#160;image&#160;frames&#160;in&#160;the&#160;y&#160;direction
#  
##############################################################################
####### `

 evt_cntrl_nxt_cnt  (self) 
     ` #####################################################################################   
#&#160;Call&#160;the&#160;Scale&#160;widget&#160;event&#160;function&#160;below&#160;to&#160;show&#160;the&#160;appropriate&#160;frame
#  
##############################################################################
####### `

 evt_cntrl_nxt_scl  (self, animation, event) 
     ` #####################################################################################   
#&#160;Show&#160;the&#160;appropriate&#160;frame&#160;requested&#160;by&#160;the&#160;user
#  
##############################################################################
####### `

 evt_cntrl_slw_cnt  (self) 
     ` #####################################################################################   
#&#160;Call&#160;the&#160;Scale&#160;widget&#160;event&#160;function&#160;below&#160;to&#160;pause&#160;the&#160;speed&#160;of&#160;the
animation&#160;&#160;&#160;&#160;#  
##############################################################################
####### `

 evt_cntrl_slw_scl  (self, animation, event) 
     ` #####################################################################################   
#&#160;Slow&#160;the&#160;animate&#160;speed
#  
##############################################################################
####### `

 evt_enter_load_file  (self, parent, gui_parent, animation, who_called, event) 

 evt_enter_save_file  (self, parent, animation, who_called, event) 

 evt_zoom_image_cmb  (self, event) 
     ` #####################################################################################   
#&#160;Call&#160;the&#160;Zoom&#160;widget&#160;event&#160;function&#160;below&#160;to&#160;zoom&#160;in&#160;on&#160;the&#160;animation
#  
##############################################################################
####### `

 evt_zoom_image_scl  (self, animation, event) 
     ` #####################################################################################   
#&#160;Zoom&#160;in&#160;on&#160;the&#160;animation&#160;frame(s)
#  
##############################################################################
####### `

  
 Data 

` `

 Pmw  = <Pmw.Pmw_1_2.lib.PmwLoader.PmwLoader instance>   
 imagefiletypes  = [('Raster files', '*.ras'), ('All files', '*')] 

* * *

UCRL-WEB-213937 | [ Privacy & Legal Notice ](/disclaimer.html)

[ webmaster@pcmdi.llnl.gov ](/webmaster@pcmdi.llnl.gov)

[ ![Powered by Plone](media/plone_powered.gif) ](/)

