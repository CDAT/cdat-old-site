---
layout: default
title:
---

 [ Skip to content. ](/cdat/source/api-
reference/browser.gui_select_variable.html) | [ Skip to navigation
](/cdat/source/api-reference/browser.gui_select_variable.html)

Search Site

[ Advanced Search&#8230; ](/search_form)

#  [ PCMDI Software Portal ](/)

#####  Sections

  * [ Home ](/)

#####  Personal tools

  * [ Log in ](/login_form)

You are here:  [ Home ](/) -> [ CDAT ](/cdat) -> [ Source Code ](/cdat/source)
-> [ API Reference ](/cdat/source/api-reference) -> Python: module
browser.gui_select_variable

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

        * [ Python: module browser.gui_select_variable ](/cdat/source/api-reference/browser.gui_select_variable.html)

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

  * [ ![Send this page to somebody](media/mail_icon.gif) ](/cdat/source/api-reference/browser.gui_select_variable.html/sendto_form)
  * [ ![Print this page](media/print_icon.gif) ](/this.print\(\))

#  Python: module browser.gui_select_variable

  
  
 [ browser  ](/browser.html) .gui_select_variable 
[ index ](/)  

` #&#160;The&#160;PCMDI&#160;Data&#160;Browser&#160;Select&#160;Variable&#160;Panel&#160;-&#160;&#160;gui_select_variable&#160;module  
#  
##############################################################################
###  
#
#  
#&#160;Module:&#160;&#160;&#160;&#160;&#160;&#160;&#160;gui_select_variable&#160;module
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
#&#160;Description:&#160;&#160;PCMDI&#160;Software&#160;System&#160;browser&#160;Tkinter&#160;"Select&#160;Variable"&#160;panel
#  
#&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;GUI.
#  
#
#  
#&#160;Version:&#160;&#160;&#160;&#160;&#160;&#160;3.0
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

[ browser.gui_database ](/browser.gui_database.html)  
[ browser.gui_defined_variables ](/browser.gui_defined_variables.html)  
[ browser.gui_edit_list ](/browser.gui_edit_list.html)  
[ browser.gui_formulate ](/browser.gui_formulate.html)  
[ browser.gui_functions ](/browser.gui_functions.html)  

[ browser.gui_message ](/browser.gui_message.html)  
[ browser.gui_select_variable ](/browser.gui_select_variable.html)  
[ os ](/os.html)  
[ re ](/re.html)  
[ string ](/string.html)  

[ sys ](/sys.html)  
[ tkFileDialog ](/tkFileDialog.html)  
[ types ](/types.html)  

  
 Classes 

` `

[ create ](/browser.gui_select_variable.html)

  
class  create 

` `

` #---------------------------------------------------------------------------  
#  
#&#160;Start&#160;of&#160;the&#160;"Select&#160;Variable"&#160;panel&#160;GUI&#160;Layout  
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
#&#160;Begin&#160;the&#160;creation&#160;of&#160;"Select&#160;Variable"&#160;panel  
#---------------------------------------------------------------------  
`

Methods defined here:  

 __init__  (self, parent) 

  
 Functions 

` `

 evt_backspace  (parent, event) 
     ` #######&#160;event&#160;for&#160;directory&#160;entry&#160;only,&#160;search&#160;for&#160;back&#160;space&#160;entry `

 evt_change_color  (parent, event) 
     ` #-----------------------------------------------------------------   
#&#160;event&#160;functions&#160;associated&#160;with&#160;the&#160;"Select&#160;Variable"&#160;panel  
#----------------------------------------------------------------- `

 evt_cycle_through_directories  (parent, event) 
     ` #######&#160;event&#160;'cycle&#160;through&#160;directories'&#160;for&#160;directory&#160;entry `

 evt_cycle_through_files  (parent, event) 
     ` #######&#160;event&#160;'cycle&#160;through&#160;files'&#160;for&#160;files&#160;entry `

 evt_display_file_info  (parent, event) 
     ` #######&#160;event&#160;'cycle&#160;through&#160;directories'&#160;for&#160;directory&#160;entry `

 evt_enter_directory  (parent, event, who_called  =0  ) 
     ` #######&#160;event&#160;'text&#160;input'&#160;for&#160;directory&#160;or&#160;database&#160;entry `

 evt_enter_file  (parent, event) 
     ` #######&#160;event&#160;for&#160;file&#160;entry `

 evt_enter_variable  (parent, event) 
     ` #######&#160;event&#160;for&#160;variable&#160;entry `

 evt_icon_open_file  (parent, dirfilename  =None  , event  =None  ) 
     ` #######&#160;event&#160;'icon&#160;file&#160;open'&#160;for&#160;directory&#160;and&#160;file&#160;entry `

 evt_popup_database_gui  (self, parent, event) 
     ` #######&#160;event&#160;to&#160;toggle&#160;between&#160;the&#160;'Directory'&#160;or&#160;'Database' `

 evt_tab  (parent, event) 
     ` #######&#160;event&#160;for&#160;directory&#160;entry&#160;only,&#160;search&#160;for&#160;a&#160;tab&#160;entry `

 restore_directory_setting  (self, parent) 
     ` #######&#160;event&#160;in&#160;'Directory&#160;or&#160;Database&#160;settings' `

  
 Data 

` `

 Pmw  = <Pmw.Pmw_1_2.lib.PmwLoader.PmwLoader instance>

* * *

UCRL-WEB-213937 | [ Privacy & Legal Notice ](/disclaimer.html)

[ webmaster@pcmdi.llnl.gov ](/webmaster@pcmdi.llnl.gov)

[ ![Powered by Plone](media/plone_powered.gif) ](/)

