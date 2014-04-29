---
layout: default
title:
---

 [ Skip to content. ](/cdat/source/api-reference/browser.tk_cdat.html) | [ Skip
to navigation ](/cdat/source/api-reference/browser.tk_cdat.html)

Search Site

[ Advanced Search&#8230; ](/search_form)

#  [ PCMDI Software Portal ](/)

#####  Sections

  * [ Home ](/)

#####  Personal tools

  * [ Log in ](/login_form)

You are here:  [ Home ](/) -> [ CDAT ](/cdat) -> [ Source Code ](/cdat/source)
-> [ API Reference ](/cdat/source/api-reference) -> Python: module
browser.tk_cdat

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

        * [ Python: module browser.tk_cdat ](/cdat/source/api-reference/browser.tk_cdat.html)

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

  * [ ![Send this page to somebody](media/mail_icon.gif) ](/cdat/source/api-reference/browser.tk_cdat.html/sendto_form)
  * [ ![Print this page](media/print_icon.gif) ](/this.print\(\))

#  Python: module browser.tk_cdat

  
  
 [ browser  ](/browser.html) .tk_cdat 
[ index ](/)  

` #&#160;The&#160;PCMDI's&#160;Visual&#160;Climate&#160;Data&#160;Analysis&#160;Tools&#160;(VCDAT)&#160;-&#160;tk_cdat&#160;module  
#  
##############################################################################
#  
#
#  
#&#160;Module:&#160;&#160;&#160;&#160;&#160;&#160;&#160;tk_cdat&#160;module
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
#&#160;Description:&#160;&#160;CDAT&#160;GUI&#160;command&#160;wrapper&#160;for&#160;PCMDI&#160;Software&#160;System&#160;Browser.
#  
#&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;This&#160;is&#160;the&#160;top&#160;level&#160;Python/Tkinter&#160;file&#160;that&#160;calls&#160;other
#  
#&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;Python/Tkinter&#160;files&#160;to&#160;create&#160;the&#160;CDAT&#160;GUI.
#  
#
# `

  
 Modules 

` `

[ Numeric ](/Numeric.html)  
[ Tkinter ](/Tkinter.html)  
[ __main__ ](/__main__.html)  
[ cdms ](/cdms.html)  
[ cdtime ](/cdtime.html)  
[ getopt ](/getopt.html)  
[ browser.gui_alter_plot ](/browser.gui_alter_plot.html)  

[ gui_support.gui_color ](/gui_support.gui_color.html)  
[ browser.gui_control ](/browser.gui_control.html)  
[ browser.gui_defined_variables ](/browser.gui_defined_variables.html)  
[ browser.gui_dimensions ](/browser.gui_dimensions.html)  
[ browser.gui_extend_menus ](/browser.gui_extend_menus.html)  
[ browser.gui_functions ](/browser.gui_functions.html)  
[ browser.gui_graphics_control ](/browser.gui_graphics_control.html)  

[ browser.gui_menu ](/browser.gui_menu.html)  
[ browser.gui_select_variable ](/browser.gui_select_variable.html)  
[ gui_support ](/gui_support.html)  
[ browser.gui_variable_information ](/browser.gui_variable_information.html)  
[ math ](/math.html)  
[ os ](/os.html)  
[ string ](/string.html)  

[ sys ](/sys.html)  
[ time ](/time.html)  
[ types ](/types.html)  
[ vcs ](/vcs.html)  
[ browser.vcs_function ](/browser.vcs_function.html)  

  
 Classes 

` `

[ TkWaitBar ](/browser.tk_cdat.html)

  
class  TkWaitBar 

` `

Methods defined here:  

 __init__  (self, splash, canvas, bar, width, height, bar_width, bar_height, total) 

 update  (self, count  =None  ) 

  
 Functions 

` `

 closeA  () 
     ` #&#160;IDLE&#160;is&#160;looking&#160;for&#160;a&#160;close&#160;or&#160;exit&#160;on&#160;its&#160;Edit&#160;or&#160;Shell&#160;window.   
#&#160;So,&#160;lets&#160;give&#160;it&#160;what&#160;he&#160;wants.&#160;This&#160;stops&#160;IDLE&#160;from&#160;popping&#160;up&#160;a  
#&#160;Tkinter&#160;root&#160;window&#160;on&#160;the&#160;close&#160;or&#160;exit&#160;of&#160;a&#160;Edit&#160;or&#160;Shell&#160;window. `

 main  () 

  
 Data 

` `

 Pmw  = <Pmw.Pmw_1_2.lib.PmwLoader.PmwLoader instance>   
 Version  = '4.0'   
 fn  = '/pcmdi/halliday1/PCMDI_GRAPHICS'   
 usage_msg  = 'The Visual Climate Data Analysis Tools (VCDAT) v...re, California, 94550, United States of  \n  America.  \n  ' 

* * *

UCRL-WEB-213937 | [ Privacy & Legal Notice ](/disclaimer.html)

[ webmaster@pcmdi.llnl.gov ](/webmaster@pcmdi.llnl.gov)

[ ![Powered by Plone](media/plone_powered.gif) ](/)

