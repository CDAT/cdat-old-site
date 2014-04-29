---
layout: default
title:
---

 [ Skip to content. ](/cdat/source/api-reference/vcs.pagegui.html) | [ Skip to
navigation ](/cdat/source/api-reference/vcs.pagegui.html)

Search Site

[ Advanced Search&#8230; ](/search_form)

#  [ PCMDI Software Portal ](/)

#####  Sections

  * [ Home ](/)

#####  Personal tools

  * [ Log in ](/login_form)

You are here:  [ Home ](/) -> [ CDAT ](/cdat) -> [ Source Code ](/cdat/source)
-> [ API Reference ](/cdat/source/api-reference) -> Python: module vcs.pagegui

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

        * [ Python: module vcs.pagegui ](/cdat/source/api-reference/vcs.pagegui.html)

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

  * [ ![Send this page to somebody](media/mail_icon.gif) ](/cdat/source/api-reference/vcs.pagegui.html/sendto_form)
  * [ ![Print this page](media/print_icon.gif) ](/this.print\(\))

#  Python: module vcs.pagegui

  
  
 [ vcs  ](/vcs.html) .pagegui 
[ index ](/)  

` #&#160;The&#160;VCS&#160;Page&#160;Layout&#160;GUI&#160;controls&#160;-&#160;&#160;pagegui&#160;module  
#  
##############################################################################
###  
#
#  
#&#160;Module:&#160;&#160;&#160;&#160;&#160;&#160;&#160;pagegui&#160;module
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
#&#160;Description:&#160;&#160;PCMDI's&#160;VCS&#160;page&#160;description&#160;GUI&#160;browser&#160;and&#160;editor.
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

[ cdms.MV ](/cdms.MV.html)  
[ Numeric ](/Numeric.html)  
[ Tkinter ](/Tkinter.html)  
[ __main__ ](/__main__.html)  

[ cdms ](/cdms.html)  
[ gui_support.gui_color ](/gui_support.gui_color.html)  
[ browser.gui_defined_variables ](/browser.gui_defined_variables.html)  
[ browser.gui_message ](/browser.gui_message.html)  

[ browser.gui_output ](/browser.gui_output.html)  
[ gui_support ](/gui_support.html)  
[ os ](/os.html)  
[ string ](/string.html)  

[ sys ](/sys.html)  
[ tkFileDialog ](/tkFileDialog.html)  
[ types ](/types.html)  

  
 Classes 

` `

[ Form ](/vcs.pagegui.html)

[ P_Command ](/vcs.pagegui.html)

[ PageDescriptionEditor ](/vcs.pagegui.html)

[ create_page_description_panel ](/vcs.pagegui.html)

[ create_pd_options_menu ](/vcs.pagegui.html)

[ show_bin ](/vcs.pagegui.html)

  
class  Form 

` `

` #----------------------------------------------------------------------  
#----------------------------------------------------------------------  
#  
#&#160;Show&#160;the&#160;VCS&#160;"Page&#160;Layout"&#160;.  
#  
#----------------------------------------------------------------------  
#----------------------------------------------------------------------  
#Create&#160;dummy&#160;form&#160;class  
`

  
class  P_Command 

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

  
class  PageDescriptionEditor 

` `

` #---------------------------------------------------------------------------
------  
#-----------------------------------------------------------------------------
-----------  
#  
#&#160;Create&#160;the&#160;Tkinter/Pmw&#160;Page&#160;Layout&#160;editor&#160;interface  
#  
#-----------------------------------------------------------------------------
-----------  
#-----------------------------------------------------------------------------
-----------  
`

Methods defined here:  

 __init__  (self, canvas  =None  , gui_parent  =None  , continents  =None  ) 

 create_file_menu  (self, main_menu) 

 create_help_menu  (self, main_menu) 

 evt_about_dialog  (self) 

  
class  create_page_description_panel 

` `

` #&#160;Create&#160;page&#160;description&#160;panel's&#160;forms&#160;list  
`

Methods defined here:  

 __init__  (self, eself, parent) 

 create_form  (self, template  ='default'  , graphics_method  ='Boxfill'  , graphics_name  ='default'  , data1  =None  , data2  =None  , data3  =None  , id  =1  , vcs  =None  ) 
     ` #&#160;Create&#160;page&#160;description&#160;form `

 do_plot  (self, id) 

 evt_change_priority  (self, id) 

 evt_remove_form  (self, id) 

 evt_replace_data  (self, pe, id, event) 

 evt_replace_gm  (self, pe, id, event) 

 evt_replace_template  (self, pe, id, event) 

 evt_status_button  (self, id) 

  
class  create_pd_options_menu 

` `

` #&#160;Create&#160;the&#160;page&#160;description&#160;Options&#160;menu&#160;and&#160;its&#160;menu&#160;items  
#  
#-----------------------------------------------------------------------------
-----------  
#-----------------------------------------------------------------------------
-----------  
`

Methods defined here:  

 __init__  (self, eself, main_menu) 

 evt_create_new_pd_form  (self, eself) 

 evt_remove_pd_form  (self, eself) 

  
class  show_bin 

` `

` #----------------------------------------------------------------------  
#----------------------------------------------------------------------  
#  
#&#160;Show&#160;the&#160;VCS&#160;"Templates"&#160;.  
#  
#----------------------------------------------------------------------  
#----------------------------------------------------------------------  
`

Methods defined here:  

 __init__  (self, group_bins, dialog) 

 data  (self, vcs) 

 edit_graphics_method  (self, vcs) 

 edit_template  (self, vcs) 

 evt_select_graphics_method  (self, gm_name, vcs) 

 graphics_method  (self, vcs, gm_name) 

 select_data  (self) 

 select_gm  (self) 

 select_template  (self) 

 template  (self, vcs) 

 update_data_list  (self) 

  
 Functions 

` `

 create  (canvas  =None  , gui_parent  =None  ) 
     ` #####################################################################################   
#&#160;Create/Popup&#160;page&#160;description&#160;GUI&#160;editor&#160;for&#160;VCS
#  
##############################################################################
####### `

 return_defined_data_list  () 
     ` #&#160;Find&#160;the&#160;data&#160;that&#160;is&#160;defined `

  
 Data 

` `

 Pmw  = <Pmw.Pmw_1_2.lib.PmwLoader.PmwLoader instance>   
 graphics_method_list  = ['Boxfill', 'Isofill', 'Isoline', 'Outfill', 'Outline', 'Vector', 'Scatter', 'XvsY', 'Xyvsy', 'Yxvsx', 'Continents'] 

* * *

UCRL-WEB-213937 | [ Privacy & Legal Notice ](/disclaimer.html)

[ webmaster@pcmdi.llnl.gov ](/webmaster@pcmdi.llnl.gov)

[ ![Powered by Plone](media/plone_powered.gif) ](/)

