---
layout: default
title: API gui_support
---

#  Python: package gui_support
## Package Contents 
* [gui_color](gui_support.gui_color.html)
* [gui_support_version](gui_support.gui_support_version.html)

##Classes 
[VcsDialog](gui_support.html)
  
###class  VcsDialog
####Methods defined here:

    __init__(self, kw) 
    destroy(self) 
    execute(self, name) 
    position_over(self, gui_parent) 
      #Positionthisdialogoverthegui_parent
    position_popup(self, popup, transient  =1  ) 
      #Positionadialogoverthisone.

##Functions 
    add_balloon_help(menu, menu_title) 
      #Addaballoonhelptoggletomenu.
    balloon_state() 
      #Returnthestateoftheglobalballoonsetting.
    buildDate() 
      #Returnsthedatepythonwasbuilt,andthedateCDATwasbuilt
    root() 
      #Returntheroot
    root_exists() 
      #Doestherootwindowexistyet?
    set_root(root) 
      #Settherootexternally.
    toggle_balloon_state() 
      #Settheballoonhelpflag.
    version() 
      #Returntheversionnumberfromthecdatversionscript

##Data 

    Pmw  = <Pmw.Pmw_1_2.lib.PmwLoader.PmwLoader instance>   
    balloon  = None   
    balloons_off  = 'none'   
    balloons_on  = 'balloon'   
    fn  = '/pcmdi/halliday1/PCMDI_GRAPHICS' 
