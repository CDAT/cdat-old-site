---
layout: default
title:
---

 [ Skip to content. ](/cdat/source/api-reference/vcs.gui_template_editor.html)
| [ Skip to navigation ](/cdat/source/api-
reference/vcs.gui_template_editor.html)

Search Site

[ Advanced Search&#8230; ](/search_form)

#  [ PCMDI Software Portal ](/)

#####  Sections

  * [ Home ](/)

#####  Personal tools

  * [ Log in ](/login_form)

You are here:  [ Home ](/) -> [ CDAT ](/cdat) -> [ Source Code ](/cdat/source)
-> [ API Reference ](/cdat/source/api-reference) -> Python: module
vcs.gui_template_editor

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

        * [ Python: module vcs.gui_template_editor ](/cdat/source/api-reference/vcs.gui_template_editor.html)

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

  * [ ![Send this page to somebody](media/mail_icon.gif) ](/cdat/source/api-reference/vcs.gui_template_editor.html/sendto_form)
  * [ ![Print this page](media/print_icon.gif) ](/this.print\(\))

#  Python: module vcs.gui_template_editor

  
  
 [ vcs  ](/vcs.html) .gui_template_editor 
[ index ](/)  

` #&#160;Template&#160;Editor&#160;GUI&#160;Module `

  
 Modules 

` `

[ vcs.Canvas ](/vcs.Canvas.html)  
[ MA ](/MA.html)  
[ Numeric ](/Numeric.html)  
[ Tkinter ](/Tkinter.html)  
[ vcs._vcs ](/vcs._vcs.html)  

[ cdms ](/cdms.html)  
[ vcs.fonteditorgui ](/vcs.fonteditorgui.html)  
[ browser.gui_busy ](/browser.gui_busy.html)  
[ gui_support.gui_color ](/gui_support.gui_color.html)  
[ browser.gui_control ](/browser.gui_control.html)  

[ browser.gui_message ](/browser.gui_message.html)  
[ gui_support ](/gui_support.html)  
[ vcs.lineeditorgui ](/vcs.lineeditorgui.html)  
[ os ](/os.html)  
[ string ](/string.html)  

[ sys ](/sys.html)  
[ tkFileDialog ](/tkFileDialog.html)  
[ vcs ](/vcs.html)  

  
 Classes 

` `

[ Template_Editor ](/vcs.gui_template_editor.html)

[ busy ](/vcs.gui_template_editor.html)

[ create_attribute ](/vcs.gui_template_editor.html)

[ template_state ](/vcs.gui_template_editor.html)

  
class  Template_Editor 

` `

Methods defined here:  

 __init__  (self, gui_parent  =None  , canvas  =None  , plot  =None  , template_name  ='quick'  , template_orig_name  ='quick'  , graphics_method  ='isofill'  , graphics_method_name  ='default'  ) 

 copy_template  (self) 

 create_axis  (self, page) 

 create_borders_and_lines  (self, page) 

 create_data_and_legend  (self, page) 

 create_labels  (self, page) 
     ` #-----------------------------------------------------   
#&#160;Populate&#160;the&#160;'Labels'&#160;tab  
#----------------------------------------------------- `

 create_menu_bar  (self) 

 create_new  (self) 

 do_nothing  (self, event) 
     ` #----------------------------------------------------------   
#&#160;Don't&#160;do&#160;anything.  
#---------------------------------------------------------- `

 evt_change_color  (self, master, obj, event) 
     ` #----------------------------------------------------------   
#&#160;Change&#160;the&#160;color&#160;of&#160;the&#160;text&#160;window&#160;when&#160;inputing&#160;text.  
#---------------------------------------------------------- `

 evt_create_new  (self, result) 

 execute  (self, result, template_name  =None  ) 
     ` #&#160;Main&#160;command&#160;control&#160;function.&#160;&#160;Figure&#160;out&#160;what&#160;to&#160;do&#160;with&#160;the   
#&#160;&#160;request&#160;(ie.&#160;Save,&#160;Cancel,&#160;etc.) `

 execute2  (self, name, result) 
     ` #----------------------------------------------------------   
#&#160;Handle&#160;the&#160;closing&#160;of&#160;the&#160;"Properties"&#160;button  
#---------------------------------------------------------- `

 exit  (self) 

 get_template  (self) 
     ` #----------------------------------------------------------   
#&#160;Create&#160;a&#160;copy&#160;of&#160;the&#160;template&#160;and&#160;then&#160;tell&#160;the&#160;canvas&#160;to&#160;use  
#&#160;&#160;the&#160;template&#160;copy&#160;to&#160;display&#160;the&#160;plot.&#160;(This&#160;way&#160;we're&#160;not  
#&#160;&#160;actually&#160;modifying&#160;the&#160;real&#160;template&#160;in&#160;case&#160;we&#160;want&#160;to  
#&#160;&#160;revert&#160;or&#160;do&#160;a&#160;"Save&#160;As".)  
#---------------------------------------------------------- `

 open_new  (self) 

 priority_change  (self, name, evt  =None  ) 

 refresh_data  (self) 

 refresh_toggle  (self, attr_name, toggle_val) 

 reinitialize_editor  (self) 

 remove_temp_templates  (self) 

 replot  (self) 

 restore_plots_on_canvas  (self) 

 sample_data  (self) 

 save  (self, template_name  =None  ) 
     ` #&#160;Prompt&#160;user&#160;to&#160;save&#160;changes&#160;if&#160;they&#160;are&#160;trying&#160;to&#160;close&#160;the&#160;template   
#&#160;&#160;editor&#160;and&#160;changes&#160;have&#160;been&#160;made. `

 saveas  (self) 

 savefile  (self) 

 savescript  (self) 

 savesession  (self) 
     ` #&#160;Verify&#160;template&#160;being&#160;saved&#160;and&#160;give&#160;users&#160;one&#160;more&#160;chance&#160;to   
#&#160;&#160;cancel&#160;their&#160;save&#160;request. `

 scale  (self) 

 select_all  (self) 

 set_value  (self, attribute, result) 
     ` #----------------------------------------------------------   
#&#160;Change&#160;the&#160;value&#160;of&#160;a&#160;particular&#160;attribute&#160;in&#160;the  
#&#160;&#160;template&#160;so&#160;that&#160;it&#160;reflects&#160;the&#160;state&#160;of&#160;the&#160;GUI.  
#&#160;&#160;This&#160;is&#160;more&#160;for&#160;the&#160;pull&#160;down&#160;menu&#160;options&#160;such&#160;as  
#&#160;&#160;text&#160;orientation,&#160;text&#160;table,&#160;etc.  
#---------------------------------------------------------- `

 show_canvas  (self) 

 show_properties  (self, parent, master) 
     ` #--------------------------------------------------------------   
#&#160;Open&#160;properties&#160;button&#160;for&#160;selected&#160;attribute  
#-------------------------------------------------------------- `

 unselect_all  (self) 

 update_value  (self, item, name, evt  =None  ) 
     ` #----------------------------------------------------------   
#&#160;Update&#160;the&#160;new&#160;value&#160;for&#160;the&#160;template&#160;in&#160;use.&#160;&#160;This&#160;is&#160;normally&#160;called  
#&#160;&#160;from&#160;a&#160;bound&#160;object&#160;when&#160;someone&#160;changes&#160;focus&#160;to&#160;another&#160;window&#160;or  
#&#160;&#160;hits&#160;'Enter'.  
#---------------------------------------------------------- `

  
class  busy 

` `

` #----------------------------------------------------------  
#&#160;Create&#160;a&#160;Dummy&#160;class  
#----------------------------------------------------------  
`

  
class  create_attribute 

` `

` #----------------------------------------------------------  
#&#160;This&#160;creates&#160;a&#160;template&#160;object&#160;and&#160;packs&#160;it&#160;into&#160;the&#160;current  
#&#160;&#160;master&#160;widget.  
#----------------------------------------------------------  
`

Methods defined here:  

 __init__  (self, name  =None  , parent  =None  , master  =None  , x1  =None  , x2  =None  , y1  =None  , y2  =None  , row  =0  ) 

  
class  template_state 

` `

` #&#160;Dictionary&#160;of&#160;checkbutton&#160;values.&#160;&#160;This&#160;is&#160;for&#160;use  
#&#160;&#160;&#160;in&#160;keeping&#160;track&#160;of&#160;which&#160;values&#160;are&#160;turned&#160;on&#160;and&#160;off  
`

Methods defined here:  

 __init__  (self) 

  
 Functions 

` `

 change_field_mode  (self, mode) 

 create  (gui_parent  =None  , canvas  =None  , plot  =None  , template_name  =''  , template_orig_name  =''  ) 
     ` #--------------------------------------------------------------   
#&#160;Call&#160;mainloop()&#160;if&#160;called&#160;from&#160;the&#160;command&#160;line  
#--------------------------------------------------------------  
#&#160;Create/Popup&#160;template&#160;editor&#160;for&#160;VCS. `

 format_number  (value, digits  =4  ) 
     ` #--------------------------------------------------------------   
#&#160;Format&#160;printed&#160;number&#160;so&#160;it&#160;is&#160;only&#160;has&#160;'x'&#160;digits&#160;after&#160;the  
#&#160;&#160;decimal  
#-------------------------------------------------------------- `

 spacer  (interior, height  =1  , width  =1  ) 
     ` #--------------------------------------------------------------   
#&#160;Create&#160;an&#160;invisible&#160;spacer&#160;to&#160;get&#160;around&#160;padx&#160;and&#160;pady  
#&#160;&#160;putting&#160;spaces&#160;on&#160;both&#160;sides  
#-------------------------------------------------------------- `

 toggle_on_off  (self, parent) 
     ` #--------------------------------------------------------------   
#&#160;When&#160;an&#160;attribute&#160;is&#160;selected&#160;to&#160;be&#160;displayed,&#160;highlight&#160;the  
#&#160;&#160;label&#160;name,&#160;activate&#160;the&#160;coordinate&#160;entryfields&#160;and&#160;activate  
#&#160;&#160;the&#160;properties&#160;button.&#160;When&#160;it&#160;is&#160;unselected,&#160;do&#160;the&#160;reverse.  
#-------------------------------------------------------------- `

  
 Data 

` `

 Pmw  = <Pmw.Pmw_1_2.lib.PmwLoader.PmwLoader instance>   
 hot_color  = 'green' 

* * *

UCRL-WEB-213937 | [ Privacy & Legal Notice ](/disclaimer.html)

[ webmaster@pcmdi.llnl.gov ](/webmaster@pcmdi.llnl.gov)

[ ![Powered by Plone](media/plone_powered.gif) ](/)

