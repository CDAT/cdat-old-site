---
layout: default
title:
---

 [ Skip to content. ](/cdat/source/api-
reference/browser.gui_set_graphics_methods.html) | [ Skip to navigation
](/cdat/source/api-reference/browser.gui_set_graphics_methods.html)

Search Site

[ Advanced Search&#8230; ](/search_form)

#  [ PCMDI Software Portal ](/)

#####  Sections

  * [ Home ](/)

#####  Personal tools

  * [ Log in ](/login_form)

You are here:  [ Home ](/) -> [ CDAT ](/cdat) -> [ Source Code ](/cdat/source)
-> [ API Reference ](/cdat/source/api-reference) -> Python: module
browser.gui_set_graphics_methods

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

        * [ Python: module browser.gui_set_graphics_methods ](/cdat/source/api-reference/browser.gui_set_graphics_methods.html)

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

  * [ ![Send this page to somebody](media/mail_icon.gif) ](/cdat/source/api-reference/browser.gui_set_graphics_methods.html/sendto_form)
  * [ ![Print this page](media/print_icon.gif) ](/this.print\(\))

#  Python: module browser.gui_set_graphics_methods

  
  
 [ browser  ](/browser.html) .gui_set_graphics_methods 
[ index ](/)  

` #&#160;The&#160;PCMDI&#160;Data&#160;Browser&#160;Contour&#160;Levels&#160;Popup&#160;-&#160;gui_set_graphics_methods
module  
#  
##############################################################################
#  
#
#  
#&#160;Module:&#160;&#160;&#160;&#160;&#160;&#160;&#160;gui_set_graphics_methods&#160;module
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
#&#160;Description:&#160;&#160;PCMDI&#160;Software&#160;System&#160;browser&#160;to&#160;set&#160;graphics&#160;method
#  
#&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;attributes&#160;popup.
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

[ Numeric ](/Numeric.html)  
[ Tkinter ](/Tkinter.html)  
[ cdms ](/cdms.html)  
[ cdtime ](/cdtime.html)  

[ gui_support.gui_color ](/gui_support.gui_color.html)  
[ browser.gui_control ](/browser.gui_control.html)  
[ browser.gui_functions ](/browser.gui_functions.html)  
[ browser.gui_menu ](/browser.gui_menu.html)  

[ browser.gui_message ](/browser.gui_message.html)  
[ math ](/math.html)  
[ os ](/os.html)  
[ string ](/string.html)  

[ sys ](/sys.html)  
[ types ](/types.html)  
[ vcs ](/vcs.html)  
[ browser.vcs_function ](/browser.vcs_function.html)  

  
 Classes 

` `

[ boxfill_attributes ](/browser.gui_set_graphics_methods.html)

[ continents_attributes ](/browser.gui_set_graphics_methods.html)

[ contour_levels ](/browser.gui_set_graphics_methods.html)

[ meshfill_attributes ](/browser.gui_set_graphics_methods.html)

[ note_book ](/browser.gui_set_graphics_methods.html)

[ oneD_attributes ](/browser.gui_set_graphics_methods.html)

[ outfill_attributes ](/browser.gui_set_graphics_methods.html)

[ outline_attributes ](/browser.gui_set_graphics_methods.html)

[ scatter_attributes ](/browser.gui_set_graphics_methods.html)

[ vector_attributes ](/browser.gui_set_graphics_methods.html)

[ browser.gui_taylor.TDGui ](/browser.gui_taylor.html)

    

[ taylor_attributes ](/browser.gui_set_graphics_methods.html)

  
class  boxfill_attributes 

` `

Methods defined here:  

 __init__  (self, page, parent, re_plot_flag  =1  , gm  =None  ) 

 boxfill_clear  (self) 

 boxfill_replot  (self, parent) 

 evt_boxfill_linear_log  (self, parent, tag) 

 get_settings  (self) 

 reset_boxf_attributes  (self) 

  
class  continents_attributes 

` `

Methods defined here:  

 __init__  (self, page, parent, re_plot_flag  =1  , gm  =None  ) 

 cont_replot  (self, parent) 

 get_settings  (self) 

 persistant_set  (self) 

 reset_cont_attributes  (self) 

  
class  contour_levels 

` `

Methods defined here:  

 __init__  (self, page, parent, re_plot_flag  =1  , gm  =None  , gm_name  =None  ) 

 contour_clear  (self) 

 contour_gen_ranges  (self, parent) 

 contour_replot  (self, parent) 

 evt_contour_linear_log  (self, parent, tag) 

 get_settings  (self) 

 reset_contour_attributes  (self) 

  
class  meshfill_attributes 

` `

Methods defined here:  

 __init__  (self, page, parent, re_plot_flag  =1  , gm  =None  ) 

 get_settings  (self) 

 meshfill_clear  (self) 

 meshfill_replot  (self, parent) 

 reset_meshf_attributes  (self) 

  
class  note_book 

` `

` #---------------------------------------------------------------------  
#  
#&#160;Start&#160;of&#160;Popup&#160;Dialog  
#  
#---------------------------------------------------------------------------  
#&#160;VCS&#160;User&#160;Define&#160;Contour&#160;Levels&#160;Popup  
#---------------------------------------------------------------------------  
`

Methods defined here:  

 __init__  (self, parent) 

 apply  (self, parent, notebook_page, graphics_method) 

 execute  (self, parent, result) 

 hold_gm_original_attr_settings  (self) 

 persistant_set  (self) 

 reset_gms_to_original_settings  (self, parent, notebook_page, graphics_method) 

  
class  oneD_attributes 

` `

Methods defined here:  

 __init__  (self, page, parent, re_plot_flag  =1  , gm  =None  ) 

 get_settings  (self) 

 oneD_clear  (self, parent) 

 oneD_replot  (self, parent) 

 reset_oneD_attributes  (self) 

  
class  outfill_attributes 

` `

Methods defined here:  

 __init__  (self, page, parent, re_plot_flag  =1  , gm  =None  ) 

 get_settings  (self) 

 outf_replot  (self, parent) 

 outfill_clear  (self) 

 reset_outf_attributes  (self) 

  
class  outline_attributes 

` `

Methods defined here:  

 __init__  (self, page, parent, re_plot_flag  =1  , gm  =None  ) 

 get_settings  (self) 

 outl_replot  (self, parent) 

 outline_clear  (self) 

 reset_outl_attributes  (self) 

  
class  scatter_attributes 

` `

Methods defined here:  

 __init__  (self, page, parent, re_plot_flag  =1  , gm  =None  ) 

 get_settings  (self) 

 reset_scat_attributes  (self) 

 scat_replot  (self, parent) 

  
class  taylor_attributes  ( [ browser.gui_taylor.TDGui
](/browser.gui_taylor.html) )

` `

Methods defined here:  

 __init__  (self, page, parent, vcs  =None  , gm_name  ='ASD'  ) 

* * *

Methods inherited from [ browser.gui_taylor.TDGui ](/browser.gui_taylor.html)
:  

 get_settings  (self) 

 gui_addMarker  (self) 

 gui_addMarkerInGui  (self, row) 

 gui_copyMarkers  (self) 

 gui_deleteMarkers  (self) 

 gui_generateInterfaceGui  (self) 

 gui_generateLabelsGui  (self) 

 gui_generateMarkersGui  (self) 

 gui_start  (self) 

 gui_updateMarkers  (self) 

 updateInterface  (self) 

 updatearrow  (self, *args) 

  
class  vector_attributes 

` `

Methods defined here:  

 __init__  (self, page, parent, re_plot_flag  =1  , gm  =None  ) 

 get_settings  (self) 

 reset_vector_attributes  (self) 

 vector_replot  (self, parent) 

  
 Functions 

` `

 return_float_None  (val) 
     ` #---------------------------------------------------------------------   
#  
#&#160;End&#160;set&#160;graphics&#160;methods&#160;popup&#160;dialog  
#  
#--------------------------------------------------------------------- `

 return_int_None  (val) 

 round_number  (N) 

 sign  (N) 

  
 Data 

` `

 Pmw  = <Pmw.Pmw_1_2.lib.PmwLoader.PmwLoader instance>

* * *

UCRL-WEB-213937 | [ Privacy & Legal Notice ](/disclaimer.html)

[ webmaster@pcmdi.llnl.gov ](/webmaster@pcmdi.llnl.gov)

[ ![Powered by Plone](media/plone_powered.gif) ](/)

