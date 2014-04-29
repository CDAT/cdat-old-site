---
layout: default
title:
---

 [ Skip to content. ](/cdat/source/api-reference/browser.gui_control.html) | [
Skip to navigation ](/cdat/source/api-reference/browser.gui_control.html)

Search Site

[ Advanced Search&#8230; ](/search_form)

#  [ PCMDI Software Portal ](/)

#####  Sections

  * [ Home ](/)

#####  Personal tools

  * [ Log in ](/login_form)

You are here:  [ Home ](/) -> [ CDAT ](/cdat) -> [ Source Code ](/cdat/source)
-> [ API Reference ](/cdat/source/api-reference) -> Python: module
browser.gui_control

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

        * [ Python: module browser.gui_control ](/cdat/source/api-reference/browser.gui_control.html)

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

  * [ ![Send this page to somebody](media/mail_icon.gif) ](/cdat/source/api-reference/browser.gui_control.html/sendto_form)
  * [ ![Print this page](media/print_icon.gif) ](/this.print\(\))

#  Python: module browser.gui_control

  
  
 [ browser  ](/browser.html) .gui_control 
[ index ](/)  

` #&#160;The&#160;PCMDI&#160;Data&#160;Browser&#160;controls&#160;-&#160;&#160;gui_control&#160;module  
#  
##############################################################################
#  
#
#  
#&#160;Module:&#160;&#160;&#160;&#160;&#160;&#160;&#160;gui_control&#160;module
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
#&#160;Description:&#160;&#160;PCMDI&#160;Software&#160;System&#160;browser&#160;interface&#160;controls.
#  
#
#  
#&#160;Version:&#160;&#160;&#160;&#160;&#160;&#160;4.0
#  
#
#  
##############################################################################
# `

  
 Modules 

` `

[ cdms ](/cdms.html)  
[ cdtime ](/cdtime.html)  

[ os ](/os.html)  
[ string ](/string.html)  

[ time ](/time.html)  
[ types ](/types.html)  

  
 Classes 

` `

[ Command ](/browser.gui_control.html)

  
class  Command 

` `

` #---------------------------------------------------------------------------
------  
#&#160;Event&#160;handling&#160;function&#160;that&#160;will&#160;allow&#160;the&#160;passing&#160;of&#160;arguments  
#-----------------------------------------------------------------------------
----  
`

Methods defined here:  

 __call__  (self, *args, kw) 

 __init__  (self, func, *args, kw) 

  
 Functions 

` `

 record_command  (parent, command_str, do_beginner  =0  ) 
     ` #---------------------------------------------------------------------------------   
#&#160;Record&#160;command&#160;in&#160;the&#160;command&#160;file  
#  
#&#160;0&#160;-&#160;Only&#160;do&#160;advanced&#160;scripting  
#&#160;1&#160;-&#160;Do&#160;both&#160;advanced&#160;and&#160;beginner&#160;scripting  
#&#160;2&#160;-&#160;Only&#160;do&#160;beginner&#160;scripting  
#-----------------------------------------------------------------------------
---- `

 start_recording_commands  (parent) 
     ` #---------------------------------------------------------------------------------   
#&#160;Start&#160;recording&#160;command&#160;file  
#-----------------------------------------------------------------------------
---- `

 start_tracking_directory_file_variable_log  (parent) 
     ` #---------------------------------------------------------------------------------   
#&#160;Start&#160;tracking&#160;directories,&#160;files,&#160;and&#160;variables&#160;requested&#160;by&#160;the&#160;user.  
#&#160;If&#160;the&#160;"TrackUser"&#160;directory&#160;doesn't&#160;exist&#160;in&#160;the&#160;"$HOME/PCMDI_GRAPHICS  
#&#160;directory,&#160;then&#160;create&#160;it.  
#-----------------------------------------------------------------------------
---- `

 track_user  (parent, command_str) 

  
 Data 

` `

 calendar_list  = {'clim': 4096, 'climleap': 4352, 'd360': 17, 'gregorian': 4369, 'julian': 69905, 'no_calendar': 135441, 'noleap': 4113, 'proleptic_gregorian': 4369}   
 datachlst  = ["a alter the variable's attributes", 'n save variable to netCDF file', 'r remove the selected data variable', 'R remove [all] the variables in the data list']   
 datafilechlst  = ['Data Files', '*.nc Files', '*.ctl Files', '*.cdms Files', '*.dic Files', '*.hdf Files', '*.xml Files', '*.cdml Files', 'All Files', 'Find Pattern', 'Datasets']   
 datatypes  = [('Search for Data files', '*.nc *.ctl *.cdms *.dic *.hdf *.xml *.cdml'), ('Search for netCDF files', '*.nc'), ('Search for GrADS files', '*.ctl'), ('Search for CDMS files', '*.cdms'), ('Search for DRS files', '*.dic'), ('Search for CDMS files', '*.hdf'), ('Search for XML files', '*.xml'), ('Search for XML files', '*.cdml'), ('All files', '*')]   
 db  = None   
 db_connections  = []   
 dbdchlst  = ['Directory', 'Database']   
 defined_frame_scale  = 1.75   
 dim_axis  = ['X', 'Y', 'Z', 'T', 'W', 'U', 'V', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', ...]   
 dim_button_max  = 150   
 dim_button_min  = 50   
 dim_button_ratio  = 0.80000000000000004   
 dim_scale_ratio  = 2.0   
 dimchlst  = ['def (default) user defines axis subset by selecting first and last points', 'sum user wants summation of selected axis points', 'avg user wants average of selected axis points', 'wgt user wants weighted average of selected axis points', 'awt user wants altered weighted average of selected axis points', 'gtm user wants geometrical mean of selected axis points', 'std user wants standard deviation over selected axis points']   
 dimchlst2  = ['def (default) user defines axis subset by selecting first and last points', 'sum user wants summation of selected axis points', 'avg user wants average of selected axis points', 'awt user wants altered weighted average of selected axis points', 'gtm user wants geometrical mean of selected axis points', 'std user wants standard deviation over selected axis points']   
 dimname_width  = 10   
 directory_or_database  = 'directory'   
 dirimpchlst  = ['File', 'Import']   
 do_not_show_in_list  = ['__builtins__', '__doc__', '__main__', '__name__', 'Pmw', 'Tkinter', 'browser', 'gui_alter_plot', 'gui_color', 'gui_control', 'gui_defined_variables', 'gui_dimensions', 'gui_functions', 'gui_graphics_control', 'gui_menu', 'gui_select_variable', 'gui_variable_information', 'types', 'os', 'string', ...]   
 dvholder  = '-- '   
 dvsize  = 3   
 favorite_directories  = []   
 favorite_files  = []   
 favorite_files_index  = None   
 favorite_index  = None   
 filetypes  = [('Python and text files', '*.py *.pyw *.txt', 'TEXT'), ('All text files', '*', 'TEXT'), ('All files', '*')]   
 gmchlst  = ['Boxfill', 'BoxDiscrete', 'BoxedIsoline', 'FilledIsoline', 'Isofill', 'Isoline', 'Meshfill', 'Outfill', 'Outline', 'Scatter', 'Taylordiagram', 'Vector', 'XvsY', 'Xyvsy', 'Yxvsx']   
 gui_font  = ('helvetica', 12)   
 have_cdms_database  = 0   
 i  = 17   
 idle_font_height  = '10'   
 idle_font_name  = 'courier'   
 idle_font_size  = '12'   
 idle_font_width  = '80'   
 latitude_alias  = ['latitude']   
 level_alias  = ['level', 'plev', 'plev']   
 listbox_width  = 16   
 longitude_alias  = ['longitude']   
 max_help_width  = 50   
 mbutton_font  = ('helvetica', 12)   
 menu_font  = ('helvetica', 12)   
 mini_defined_template_gm_width  = 135   
 ndim  = 26   
 potchlst  = ['VCS Canvas 1', 'VCS Canvas 2', 'VCS Canvas 3', 'VCS Canvas 4', 'Background Canvas', 'Clear VCS Canvas 1', 'Close VCS Canvas 1']   
 scl_width  = 10   
 search_function_type_list  = [<type 'function'>, <type 'instance'>, <type 'builtin_function_or_method'>]   
 time_alias  = ['time'] 

* * *

UCRL-WEB-213937 | [ Privacy & Legal Notice ](/disclaimer.html)

[ webmaster@pcmdi.llnl.gov ](/webmaster@pcmdi.llnl.gov)

[ ![Powered by Plone](media/plone_powered.gif) ](/)

