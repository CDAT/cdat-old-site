---
layout: default
title:
---

 [ Skip to content. ](/cdat/source/api-
reference/browser.gui_variable_information.html) | [ Skip to navigation
](/cdat/source/api-reference/browser.gui_variable_information.html)

Search Site

[ Advanced Search&#8230; ](/search_form)

#  [ PCMDI Software Portal ](/)

#####  Sections

  * [ Home ](/)

#####  Personal tools

  * [ Log in ](/login_form)

You are here:  [ Home ](/) -> [ CDAT ](/cdat) -> [ Source Code ](/cdat/source)
-> [ API Reference ](/cdat/source/api-reference) -> Python: module
browser.gui_variable_information

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

        * [ Python: module browser.gui_variable_information ](/cdat/source/api-reference/browser.gui_variable_information.html)

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

  * [ ![Send this page to somebody](media/mail_icon.gif) ](/cdat/source/api-reference/browser.gui_variable_information.html/sendto_form)
  * [ ![Print this page](media/print_icon.gif) ](/this.print\(\))

#  Python: module browser.gui_variable_information

  
  
 [ browser  ](/browser.html) .gui_variable_information 
[ index ](/)  

` #&#160;The&#160;PCMDI&#160;Data&#160;Browser&#160;Variable&#160;Information&#160;Panel&#160;-
gui_variable_information&#160;module  
#  
##############################################################################
#  
#
#  
#&#160;Module:&#160;&#160;&#160;&#160;&#160;&#160;&#160;gui_variable_information&#160;module
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
#&#160;Description:&#160;&#160;PCMDI&#160;Software&#160;System&#160;browser&#160;Tkinter&#160;"Variable&#160;Information"
#  
#&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;panel&#160;GUI.
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
[ __main__ ](/__main__.html)  
[ browser.gui_busy ](/browser.gui_busy.html)  
[ gui_support.gui_color ](/gui_support.gui_color.html)  

[ browser.gui_control ](/browser.gui_control.html)  
[ browser.gui_defined_variables ](/browser.gui_defined_variables.html)  
[ browser.gui_formulate ](/browser.gui_formulate.html)  
[ browser.gui_message ](/browser.gui_message.html)  

[ os ](/os.html)  
[ string ](/string.html)  
[ sys ](/sys.html)  
[ types ](/types.html)  

[ browser.vcs_function ](/browser.vcs_function.html)  

  
 Classes 

` `

[ Form ](/browser.gui_variable_information.html)

[ create ](/browser.gui_variable_information.html)

[ create_page_description_panel ](/browser.gui_variable_information.html)

  
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

  
class  create 

` `

` #---------------------------------------------------------------------------  
#  
#&#160;Start&#160;of&#160;the&#160;"Variable&#160;Information"&#160;panel&#160;GUI&#160;Layout  
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
#&#160;Begin&#160;the&#160;creation&#160;of&#160;"Variable&#160;Information"&#160;&#160;panel  
#---------------------------------------------------------------------  
`

Methods defined here:  

 __init__  (self, parent) 

  
class  create_page_description_panel 

` `

` #&#160;Create&#160;page&#160;description&#160;panel's&#160;forms&#160;list  
`

Methods defined here:  

 __init__  (self, parent) 

 create_form  (self, parent, data1  =None  , data2  =None  , data3  =None  , id  =1  , vcs  =None  ) 
     ` #&#160;Create&#160;page&#160;description&#160;form `

 do_plot  (self, id) 

 evt_change_priority  (self, id, parent) 

 evt_create_new_pl_form  (self, parent) 
     ` #&#160;Create&#160;a&#160;new&#160;page&#160;layout&#160;form `

 evt_form_priority_change_color  (self, id, parent, event) 

 evt_remove_form  (self, id, parent, event) 

 evt_replace_data  (self, pe, id, data_entry, parent, event) 

 evt_replace_gm  (self, pe, id, parent, event) 

 evt_replace_template  (self, pe, id, parent, event) 

 evt_status_button  (self, id, parent, event) 

  
 Data 

` `

 Pmw  = <Pmw.Pmw_1_2.lib.PmwLoader.PmwLoader instance>

* * *

UCRL-WEB-213937 | [ Privacy & Legal Notice ](/disclaimer.html)

[ webmaster@pcmdi.llnl.gov ](/webmaster@pcmdi.llnl.gov)

[ ![Powered by Plone](media/plone_powered.gif) ](/)

