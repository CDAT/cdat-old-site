---
layout: default
title:
---

 [ Skip to content. ](/cdat/source/api-reference/vcs.lineeditorgui.html) | [
Skip to navigation ](/cdat/source/api-reference/vcs.lineeditorgui.html)

Search Site

[ Advanced Search&#8230; ](/search_form)

#  [ PCMDI Software Portal ](/)

#####  Sections

  * [ Home ](/)

#####  Personal tools

  * [ Log in ](/login_form)

You are here:  [ Home ](/) -> [ CDAT ](/cdat) -> [ Source Code ](/cdat/source)
-> [ API Reference ](/cdat/source/api-reference) -> Python: module
vcs.lineeditorgui

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

        * [ Python: module vcs.lineeditorgui ](/cdat/source/api-reference/vcs.lineeditorgui.html)

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

  * [ ![Send this page to somebody](media/mail_icon.gif) ](/cdat/source/api-reference/vcs.lineeditorgui.html/sendto_form)
  * [ ![Print this page](media/print_icon.gif) ](/this.print\(\))

#  Python: module vcs.lineeditorgui

  
  
 [ vcs  ](/vcs.html) .lineeditorgui 
[ index ](/)  

` ##&#160;The&#160;line&#160;GUI&#160;editor `

  
 Modules 

` `

[ Tkinter ](/Tkinter.html)  
[ browser ](/browser.html)  

[ copy ](/copy.html)  
[ gui_support ](/gui_support.html)  

[ os ](/os.html)  
[ string ](/string.html)  

[ tkFileDialog ](/tkFileDialog.html)  
[ vcs ](/vcs.html)  

  
 Classes 

` `

[ LineGUI ](/vcs.lineeditorgui.html)

  
class  LineGUI 

` `

Methods defined here:  

 __init__  (self, canvas  =None  , gui_parent  =None  , dialog_parent  =None  , master  =None  , name  ='default'  , Parent  =None  ) 

 cancel  (self) 

 evt_open_file  (self) 
     ` #&#160;Open&#160;VCS&#160;file `

 evt_save_as  (self) 

 evt_save_line_as  (self) 
     ` #&#160;Save&#160;VCS&#160;projection&#160;as&#160;a&#160;new&#160;name `

 evt_save_to_file  (self) 
     ` #&#160;Save&#160;VCS&#160;Color&#160;map&#160;to&#160;a&#160;file `

 exit  (self) 

 loadline  (self, result) 

 rename_line  (self, result) 
     ` #&#160;Save,&#160;copy,&#160;and&#160;write&#160;colormap&#160;to&#160;a&#160;file `

 reset  (self) 

 save_vals  (self) 

 setgui  (self) 

 setline  (self, *crap) 

  
 Functions 

` `

 create  (gui_parent  =None  , line  ='default'  , canvas  =None  , parent  =None  ) 
     ` #&#160;Create/Popup&#160;projection&#160;GUI&#160;for&#160;VCS. `

  
 Data 

` `

 Pmw  = <Pmw.Pmw_1_2.lib.PmwLoader.PmwLoader instance>

* * *

UCRL-WEB-213937 | [ Privacy & Legal Notice ](/disclaimer.html)

[ webmaster@pcmdi.llnl.gov ](/webmaster@pcmdi.llnl.gov)

[ ![Powered by Plone](media/plone_powered.gif) ](/)

