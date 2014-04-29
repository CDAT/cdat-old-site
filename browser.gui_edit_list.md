---
layout: default
title:
---

 [ Skip to content. ](/cdat/source/api-reference/browser.gui_edit_list.html) |
[ Skip to navigation ](/cdat/source/api-reference/browser.gui_edit_list.html)

Search Site

[ Advanced Search&#8230; ](/search_form)

#  [ PCMDI Software Portal ](/)

#####  Sections

  * [ Home ](/)

#####  Personal tools

  * [ Log in ](/login_form)

You are here:  [ Home ](/) -> [ CDAT ](/cdat) -> [ Source Code ](/cdat/source)
-> [ API Reference ](/cdat/source/api-reference) -> Python: module
browser.gui_edit_list

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

        * [ Python: module browser.gui_edit_list ](/cdat/source/api-reference/browser.gui_edit_list.html)

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

  * [ ![Send this page to somebody](media/mail_icon.gif) ](/cdat/source/api-reference/browser.gui_edit_list.html/sendto_form)
  * [ ![Print this page](media/print_icon.gif) ](/this.print\(\))

#  Python: module browser.gui_edit_list

  
  
 [ browser  ](/browser.html) .gui_edit_list 
[ index ](/)  

` #&#160;The&#160;PCMDI&#160;Data&#160;Browser&#160;alias&#160;directory&#160;editor&#160;-&#160;&#160;gui_edit_list&#160;module  
#  
##############################################################################
###  
#
#  
#&#160;Module:&#160;&#160;&#160;&#160;&#160;&#160;&#160;gui_edit_list&#160;module
#  
#
#  
#&#160;Copyright:&#160;&#160;&#160;&#160;"See&#160;file&#160;Legal.htm&#160;for&#160;copyright&#160;information."
#  
#
#  
#&#160;Authors:&#160;&#160;&#160;&#160;&#160;&#160;PCMDI&#160;Software&#160;Team
#  
#&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;Lawrence&#160;Livermore&#160;National&#160;Laboratory:
#  
#&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;support@pcmdi.llnl.gov
#  
#
#  
#&#160;Description:&#160;&#160;Sets&#160;and&#160;removes&#160;dimension&#160;named&#160;aliases.&#160;For&#160;example,
#  
#&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;the&#160;time&#160;dimension&#160;name&#160;can&#160;equal&#160;the&#160;following&#160;names:
#  
#&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;'time',&#160;'TIME',&#160;'Time',&#160;'T',&#160;or&#160;'t'.&#160;Also,&#160;adds&#160;to&#160;the
#  
#&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;favorite&#160;directory&#160;list.
#  
#
#  
#&#160;Version:&#160;&#160;&#160;&#160;&#160;&#160;4.0
#  
#
#  
##############################################################################
###  
#  
#---------------------------------------------------------------------  
#&#160;NOTE:&#160;need&#160;to&#160;use&#160;version&#160;of&#160;Python&#160;that&#160;imports&#160;Tkinter&#160;and&#160;Pmw  
#--------------------------------------------------------------------- `

  
 Modules 

` `

[ Tkinter ](/Tkinter.html)  
[ cdat_info ](/cdat_info.html)  
[ cdms ](/cdms.html)  

[ gui_support.gui_color ](/gui_support.gui_color.html)  
[ browser.gui_control ](/browser.gui_control.html)  
[ browser.gui_message ](/browser.gui_message.html)  

[ browser.gui_select_variable ](/browser.gui_select_variable.html)  
[ os ](/os.html)  
[ string ](/string.html)  

[ sys ](/sys.html)  

  
 Classes 

` `

[ create ](/browser.gui_edit_list.html)

  
class  create 

` `

` #---------------------------------------------------------------------  
#  
#&#160;Start&#160;of&#160;Popup&#160;Dialog  
#  
#---------------------------------------------------------------------------  
#&#160;Dimension&#160;Alias&#160;Dialog&#160;Popup  
#---------------------------------------------------------------------------  
`

Methods defined here:  

 __init__  (self, parent, dim_name, event  =None  ) 

 enter_new_alias  (self, dim_name, event  =None  ) 
     ` #---------------------------------------------------------------------------------   
#&#160;Add&#160;new&#160;dimension&#160;alias&#160;name&#160;to&#160;the&#160;dimension&#160;alias&#160;list  
#-----------------------------------------------------------------------------
---- `

 evt_change_alias_entry_color  (self, parent, event) 

 goto_directory  (self, parent) 
     ` #---------------------------------------------------------------------------------   
#&#160;Goto&#160;the&#160;selected&#160;directory  
#-----------------------------------------------------------------------------
---- `

 open_file  (self, parent) 
     ` #---------------------------------------------------------------------------------   
#&#160;Open&#160;the&#160;selected&#160;file  
#-----------------------------------------------------------------------------
---- `

 remove_alias  (self, dim_name) 
     ` #---------------------------------------------------------------------------------   
#&#160;Remove&#160;the&#160;alias&#160;name&#160;from&#160;the&#160;list  
#-----------------------------------------------------------------------------
---- `

  
 Functions 

` `

 check_new_alias_name  (alias_name, dim_name) 
     ` #---------------------------------------------------------------------------------   
#&#160;Return&#160;a&#160;flag&#160;that&#160;indicates&#160;whether&#160;or&#160;not&#160;to&#160;add&#160;to&#160;the  
#&#160;new&#160;alias&#160;list.&#160;A&#160;return&#160;of&#160;0&#160;means&#160;don't&#160;add&#160;to&#160;the&#160;alias  
#&#160;list.&#160;A&#160;return&#160;of&#160;1&#160;means&#160;add&#160;name&#160;to&#160;dimension&#160;alias&#160;list.  
#-----------------------------------------------------------------------------
---- `

 record_bookmarks  (dim_name) 
     ` #---------------------------------------------------------------------------------   
#&#160;Create&#160;New&#160;file&#160;containing&#160;bookmarks&#160;for&#160;favorite&#160;directories  
#-----------------------------------------------------------------------------
---- `

 return_alias_list  (dim_name) 
     ` #---------------------------------------------------------------------------------   
#&#160;Return&#160;the&#160;dimension&#160;alias&#160;list.  
#-----------------------------------------------------------------------------
---- `

 update_vcdat_alias_list  () 
     ` #---------------------------------------------------------------------------------   
#&#160;Update&#160;VCDAT's&#160;alias&#160;list  
#-----------------------------------------------------------------------------
---- `

  
 Data 

` `

 Pmw  = <Pmw.Pmw_1_2.lib.PmwLoader.PmwLoader instance>

* * *

UCRL-WEB-213937 | [ Privacy & Legal Notice ](/disclaimer.html)

[ webmaster@pcmdi.llnl.gov ](/webmaster@pcmdi.llnl.gov)

[ ![Powered by Plone](media/plone_powered.gif) ](/)

