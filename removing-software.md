---
layout: default
title: 
---


#####  Document Actions

  * [ ![Send this page to somebody](media/mail_icon.gif) ](/cdat/download/installation-guide/removing-software/sendto_form)
  * [ ![Print this page](media/print_icon.gif) ](/this.print\(\))

#  Removing (or Cleaning) Software

[ ![Table of Contents](media/arrow-up) ](/)

[ ![Previous](media/arrow-left) ](/testing-software)

[ ![Next](media/arrow-right) ](/contrib)

[ Contents ](/)

[ Previous ](/testing-software)

[ Next ](/contrib)

For building again on a different system, or after downloading a new version,
or just to save disk space, issue the following commands:

    
    
    cd <CDAT_SRC_DIRECTORY>
    make clean
    

To clean the Makefile and config.log as well

    
    
    cd <CDAT_SRC_DIRECTORY>
    make distclean
    

 Note:  To rebuild CDAT, always run make clean first and rerun configure. If you wish to rebuild CDAT and restart over, it is best to remove the ` <CDAT_INSTALL_DIRECTORY> ` . 

[ ![Table of Contents](media/arrow-up) ](/)

[ ![Previous](media/arrow-left) ](/testing-software)

[ ![Next](media/arrow-right) ](/contrib)
