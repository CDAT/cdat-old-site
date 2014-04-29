---
layout: default
title:
---

 [ Skip to content. ](/cdat/source/api-reference/browser.gui_dimensions.html) |
[ Skip to navigation ](/cdat/source/api-reference/browser.gui_dimensions.html)

Search Site

[ Advanced Search&#8230; ](/search_form)

#  [ PCMDI Software Portal ](/)

#####  Sections

  * [ Home ](/)

#####  Personal tools

  * [ Log in ](/login_form)

You are here:  [ Home ](/) -> [ CDAT ](/cdat) -> [ Source Code ](/cdat/source)
-> [ API Reference ](/cdat/source/api-reference) -> Python: module
browser.gui_dimensions

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

        * [ Python: module browser.gui_dimensions ](/cdat/source/api-reference/browser.gui_dimensions.html)

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

  * [ ![Send this page to somebody](media/mail_icon.gif) ](/cdat/source/api-reference/browser.gui_dimensions.html/sendto_form)
  * [ ![Print this page](media/print_icon.gif) ](/this.print\(\))

#  Python: module browser.gui_dimensions

  
  
 [ browser  ](/browser.html) .gui_dimensions 
[ index ](/)  

` #&#160;The&#160;PCMDI&#160;Data&#160;Browser&#160;Dimensions&#160;Panel&#160;-&#160;&#160;gui_dimensions&#160;module  
#  
##############################################################################
#  
#
#  
#&#160;Module:&#160;&#160;&#160;&#160;&#160;&#160;&#160;gui_panelC&#160;module
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
#&#160;Description:&#160;&#160;PCMDI&#160;Software&#160;System&#160;browser&#160;Tkinter&#160;"Dimensions"&#160;panel&#160;GUI.
#  
#
#  
#&#160;Version:&#160;&#160;&#160;&#160;&#160;&#160;3.0
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
[ cdms ](/cdms.html)  
[ gui_support.gui_color ](/gui_support.gui_color.html)  

[ browser.gui_control ](/browser.gui_control.html)  
[ browser.gui_functions ](/browser.gui_functions.html)  
[ browser.gui_message ](/browser.gui_message.html)  

[ browser.gui_output ](/browser.gui_output.html)  
[ os ](/os.html)  
[ string ](/string.html)  

  
 Classes 

` `

[ create ](/browser.gui_dimensions.html)

[ create_dim_row ](/browser.gui_dimensions.html)

  
class  create 

` `

` #---------------------------------------------------------------------  
#&#160;Begin&#160;the&#160;creation&#160;of&#160;"Dimension"&#160;panel  
#---------------------------------------------------------------------  
`

Methods defined here:  

 __init__  (self, parent) 

  
class  create_dim_row 

` `

` #&#160;Create&#160;one&#160;row&#160;of&#160;the&#160;dimension&#160;class  
`

Methods defined here:  

 __init__  (self, frameit, parent) 

 evt_change_entry_color  (self, parent, num, event) 
     ` #&#160;event&#160;to&#160;set&#160;background&#160;color&#160;of&#160;the&#160;entry&#160;window.&#160;This&#160;change&#160;of   
#&#160;the&#160;background&#160;color&#160;lets&#160;the&#160;user&#160;know&#160;they&#160;are&#160;in&#160;edit&#160;mode&#160;and&#160;must  
#&#160;select&#160;the&#160;'Enter'&#160;key&#160;to&#160;register&#160;changes. `

 evt_dim_function  (self, parent, event) 
     ` #&#160;Select&#160;the&#160;dimension&#160;operation `

 evt_enter_first_last  (self, parent, event) 
     ` #&#160;event&#160;to&#160;set&#160;the&#160;first&#160;and&#160;last&#160;dimension&#160;value&#160;from&#160;the&#160;entry&#160;widget,   
#&#160;either&#160;in&#160;coordinates&#160;or&#160;index `

 evt_first_scl  (self, parent, event) 
     ` #&#160;event&#160;to&#160;set&#160;the&#160;first&#160;dimension&#160;value,&#160;either&#160;in&#160;coordinates&#160;or&#160;index `

 evt_last_scl  (self, parent, event) 
     ` #&#160;event&#160;to&#160;set&#160;the&#160;last&#160;dimension&#160;value,&#160;either&#160;in&#160;coordinates&#160;or&#160;index `

 evt_select_command  (self, parent, event) 
     ` #&#160;Select&#160;the&#160;dimension&#160;coordinates&#160;via&#160;the&#160;combo&#160;box&#160;scrolled&#160;list `

 evt_select_values  (self, parent, event) 
     ` #&#160;Select&#160;the&#160;range&#160;of&#160;the&#160;coordinate&#160;values `

 return_selection  (self, parent) 
     ` #&#160;Return&#160;the&#160;selected&#160;coordinate&#160;points `

  
 Functions 

` `

 alterpaneDM  (self, parent, event  =None  ) 
     ` ##&#160;Function&#160;to&#160;resize&#160;the&#160;scrolled&#160;box&#160;when&#160;the&#160;panel&#160;changes `

  
 Data 

` `

 Pmw  = <Pmw.Pmw_1_2.lib.PmwLoader.PmwLoader instance>

* * *

UCRL-WEB-213937 | [ Privacy & Legal Notice ](/disclaimer.html)

[ webmaster@pcmdi.llnl.gov ](/webmaster@pcmdi.llnl.gov)

[ ![Powered by Plone](media/plone_powered.gif) ](/)

