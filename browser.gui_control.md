---
layout: default
title:
---

#  Python: module browser.gui_control

    #ThePCMDIDataBrowsercontrols-gui_controlmodule  
    ##############################################################################
    #Module:gui_controlmodule
    #Copyright:"SeefileLegal.htmforcopyrightinformation."
    #Authors:PCMDISoftwareTeam
    #LawrenceLivermoreNationalLaboratory:
    #support@pcmdi.llnl.gov
    #Description:PCMDISoftwareSystembrowserinterfacecontrols.
    #Version:4.0
    ##############################################################################
  
### Modules 
* [cdms](cdms.html)  
* [cdtime](cdtime.html)  
* [os](os.html)  
* [string](string.html)  
* [time](time.html)  
* [types](types.html)  
  
### Classes 
[Command](browser.gui_control.html)

    #---------------------------------------------------------------------------
    #Eventhandlingfunctionthatwillallowthepassingofarguments  
    #-----------------------------------------------------------------------------

###Methods defined here:  

    __call__  (self, *args, kw) 
    __init__  (self, func, *args, kw) 

###Functions 

    record_command  (parent, command_str, do_beginner  =0  ) 

    #---------------------------------------------------------------------------------   
    #Recordcommandinthecommandfile  
    #0-Onlydoadvancedscripting  
    #1-Dobothadvancedandbeginnerscripting  
    #2-Onlydobeginnerscripting  
    #--------------------------------------------------------------------------------- 
    
    start_recording_commands  (parent) 

    #---------------------------------------------------------------------------------   
    #Startrecordingcommandfile  
    #--------------------------------------------------------------------------------- 

    start_tracking_directory_file_variable_log  (parent) 
    #---------------------------------------------------------------------------------   
    #Starttrackingdirectories,files,andvariablesrequestedbytheuser.  
    #Ifthe"TrackUser"directorydoesn'texistinthe"$HOME/PCMDI_GRAPHICS  
    #directory,thencreateit.  
    #--------------------------------------------------------------------------------- 

    track_user  (parent, command_str) 

### Data 

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

