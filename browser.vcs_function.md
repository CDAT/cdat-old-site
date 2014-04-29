---
layout: default
title:
---

 [ Skip to content. ](/cdat/source/api-reference/browser.vcs_function.html) | [
Skip to navigation ](/cdat/source/api-reference/browser.vcs_function.html)

Search Site

[ Advanced Search&#8230; ](/search_form)

#  [ PCMDI Software Portal ](/)

#####  Sections

  * [ Home ](/)

#####  Personal tools

  * [ Log in ](/login_form)

You are here:  [ Home ](/) -> [ CDAT ](/cdat) -> [ Source Code ](/cdat/source)
-> [ API Reference ](/cdat/source/api-reference) -> Python: module
browser.vcs_function

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

        * [ Python: module browser.vcs_function ](/cdat/source/api-reference/browser.vcs_function.html)

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

  * [ ![Send this page to somebody](media/mail_icon.gif) ](/cdat/source/api-reference/browser.vcs_function.html/sendto_form)
  * [ ![Print this page](media/print_icon.gif) ](/this.print\(\))

#  Python: module browser.vcs_function

  
  
 [ browser  ](/browser.html) .vcs_function 
[ index ](/)  

` #&#160;The&#160;PCMDI&#160;Data&#160;Browser&#160;VCS&#160;Plot&#160;Functions&#160;-&#160;&#160;vcs_function&#160;module  
#  
##############################################################################
#  
#
#  
#&#160;Module:&#160;&#160;&#160;&#160;&#160;&#160;&#160;vcs_function&#160;module
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
#&#160;Description:&#160;&#160;PCMDI&#160;Software&#160;System&#160;browser&#160;VCS&#160;plot&#160;functions.
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

[ browser.gui_alter_plot ](/browser.gui_alter_plot.html)  
[ browser.gui_annotate ](/browser.gui_annotate.html)  
[ browser.gui_control ](/browser.gui_control.html)  
[ browser.gui_formulate ](/browser.gui_formulate.html)  
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

 custom_ranges  (min, max, num) 
     ` #---------------------------------------------------------------------------   
#&#160;Generate&#160;Box&#160;Discrete&#160;ranges&#160;and&#160;color&#160;indices  
#--------------------------------------------------------------------------- `

 dotemplate  (parent, template, id, replot_flg, g_name) 
     ` Reset&#160;the&#160;tempalte&#160;nae&#160;and&#160;template&#160;attributes&#160;if&#160;neeeded `

 initialize  (root, dosplashscreen, counter_bar) 
     ` #------------------------------------------------------------------------   
#&#160;Initialize&#160;the&#160;VCS&#160;grapics&#160;packages  
#------------------------------------------------------------------------ `

 modify_template  (parent, t, t2, n, n2, x, y, w, h, orientation  ='horizontal'  , legend_top  =1  ) 
     ` #---------------------------------------------------------------------------   
#&#160;Modify&#160;the&#160;template&#160;to&#160;fit&#160;on&#160;the&#160;VCS&#160;Canvas  
#--------------------------------------------------------------------------- `

 plot  (parent  =None  , slab1  =None  , slab2  =None  , template  =None  , g_name  =None  , g_type  =None  , bg  =0  , id  =1  ) 
     ` #---------------------------------------------------------------------------   
#&#160;Plot&#160;the&#160;data&#160;via&#160;VCS  
#---------------------------------------------------------------------------  
#def [ plot ](/) (parent,&#160;g_type,&#160;replot_flg,&#160;bg,&#160;formulate_data&#160;=&#160;1): `

 re_plot  (parent, replot_flg) 
     ` #---------------------------------------------------------------------------   
#&#160;Re-plot&#160;the&#160;data&#160;via&#160;VCS  
#--------------------------------------------------------------------------- `

 record_plot  (parent, slab1  =None  , slab2  =None  , templ  =None  , gtype  =None  , gname  =None  , plot_kw  ={}  ) 
     ` #---------------------------------------------------------------------------   
#&#160;Record&#160;VCS&#160;plot&#160;command  
#--------------------------------------------------------------------------- `

 set_template  (parent, template_name  =None  ) 
     ` #---------------------------------------------------------------------------   
#&#160;Modify&#160;the&#160;template&#160;to&#160;fit&#160;on&#160;the&#160;VCS&#160;Canvas  
#--------------------------------------------------------------------------- `

 turn_on_off_1Dplot_annotation  (parent, template_name) 
     ` #---------------------------------------------------------------------------   
#&#160;Turn&#160;on/off&#160;annotation&#160;for&#160;1D&#160;plots  
#--------------------------------------------------------------------------- `

 turn_on_off_plot_annotation  (parent, template_name) 
     ` #---------------------------------------------------------------------------   
#&#160;Turn&#160;on/off&#160;annotation  
#--------------------------------------------------------------------------- `

  
 Data 

` `

 Pmw  = <Pmw.Pmw_1_2.lib.PmwLoader.PmwLoader instance>   
 fn  = '/pcmdi/halliday1/PCMDI_GRAPHICS' 

* * *

UCRL-WEB-213937 | [ Privacy & Legal Notice ](/disclaimer.html)

[ webmaster@pcmdi.llnl.gov ](/webmaster@pcmdi.llnl.gov)

[ ![Powered by Plone](media/plone_powered.gif) ](/)

