---
layout: default
title:
---

 [ Skip to content. ](/cdat/source/api-reference/browser.gui_formulate.html) |
[ Skip to navigation ](/cdat/source/api-reference/browser.gui_formulate.html)

Search Site

[ Advanced Search&#8230; ](/search_form)

#  [ PCMDI Software Portal ](/)

#####  Sections

  * [ Home ](/)

#####  Personal tools

  * [ Log in ](/login_form)

You are here:  [ Home ](/) -> [ CDAT ](/cdat) -> [ Source Code ](/cdat/source)
-> [ API Reference ](/cdat/source/api-reference) -> Python: module
browser.gui_formulate

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

        * [ Python: module browser.gui_formulate ](/cdat/source/api-reference/browser.gui_formulate.html)

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

  * [ ![Send this page to somebody](media/mail_icon.gif) ](/cdat/source/api-reference/browser.gui_formulate.html/sendto_form)
  * [ ![Print this page](media/print_icon.gif) ](/this.print\(\))

#  Python: module browser.gui_formulate

  
  
 [ browser  ](/browser.html) .gui_formulate 
[ index ](/)  

` #&#160;The&#160;PCMDI&#160;Data&#160;Browser&#160;Formulate&#160;Data&#160;-&#160;&#160;gui_formulate&#160;module  
#  
##############################################################################
#  
#
#  
#&#160;Module:&#160;&#160;&#160;&#160;&#160;&#160;&#160;gui_formulate&#160;module
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
#&#160;Description:&#160;&#160;PCMDI&#160;Software&#160;System&#160;browser&#160;formulate&#160;data.&#160;This&#160;function
#  
#&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;subslices&#160;the&#160;data&#160;and&#160;[&#160;if&#160;need&#160;]&#160;will&#160;take&#160;a&#160;sum,&#160;average
#  
#&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;or&#160;area&#160;weighted&#160;average&#160;of&#160;a&#160;dimension.&#160;Singleton&#160;dimensions
#  
#&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;are&#160;squeezed&#160;out&#160;(or&#160;elminated)&#160;as&#160;a&#160;result.
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

[ cdms.MV ](/cdms.MV.html)  
[ Numeric ](/Numeric.html)  
[ Tkinter ](/Tkinter.html)  
[ cdms ](/cdms.html)  
[ cdtime ](/cdtime.html)  

[ cdutil ](/cdutil.html)  
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

  
 Functions 

` `

 data  (parent, d_name  =None  , var  =None  , new_var  =None  ) 
     ` #---------------------------------------------------------------------------   
#&#160;Modify&#160;the&#160;data&#160;just&#160;before&#160;plotting&#160;or&#160;storing&#160;in&#160;the&#160;"Selected"&#160;list  
#--------------------------------------------------------------------------- `

 re_scale_data  (a, multiplier) 
     ` #---------------------------------------------------------------------------   
#&#160;Modify&#160;the&#160;data&#160;by&#160;scaling&#160;the&#160;incoming&#160;data&#160;by&#160;the&#160;incoming&#160;multiplier.  
#--------------------------------------------------------------------------- `

 zapFirstDimension  (a) 
     ` #---------------------------------------------------------------------------   
#&#160;Modify&#160;the&#160;data&#160;to&#160;remove&#160;only&#160;the&#160;first&#160;single&#160;dimension  
#--------------------------------------------------------------------------- `

  
 Data 

` `

 Pmw  = <Pmw.Pmw_1_2.lib.PmwLoader.PmwLoader instance>

* * *

UCRL-WEB-213937 | [ Privacy & Legal Notice ](/disclaimer.html)

[ webmaster@pcmdi.llnl.gov ](/webmaster@pcmdi.llnl.gov)

[ ![Powered by Plone](media/plone_powered.gif) ](/)

