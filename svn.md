---
layout: default
title: SVN 
---

##  PCMDI Source Code Repository
CDAT is an open-source project. So how do you see the source? And never
download by hand again?  
  
Our normal release cycle releases a set of sources at a stable point. However,
you might want to get an update between releases because someone has made an
improvement you would like to use. You can now do this yourself. Be aware that
while we make every attempt to only commit source that is correct and working,
and that we develop in separate "branches" to help ensure this, this direct
access is inherently less stable than using our official releases.  

####  Instructions for accessing the repository:
* Install a Subversion client program. On Unix/Linux systems, the ` svn ` command-line client program may already be installed. 
* See the [ Subversion website ](/) for full downloads and documentation.   
* To download the main CDAT development branch into a local working directory called cdat, type:   
    
        svn checkout http://www-pcmdi.llnl.gov/svn/repository/cdat/trunk cdat

* If the checkout is successful, you should see output indicating that the files were downloaded: 
    
        [halliday1@ananke]$ svn checkout http://www-pcmdi.llnl.gov/svn/repository/cdat/trunk cdat  
        A    cdat/CDAT_demo  
        A    cdat/CDAT_demo/index.py  
        A    cdat/MacOSXInstructions.html  
        A    cdat/tarballit.sh  
        A    cdat/Changes_3.3_to_4.pdf  
        A    cdat/installation_gui.py  
        A    cdat/pysrc  
        A    cdat/pysrc/clean_script  
        A    cdat/pysrc/src  
      
        ...lots more output

* Use the ` svn info ` command for more information about your current working directory. 
* Use the ` svn update ` command any time you would like to update your copy of CDAT with the latest changes. 
* Use the ` svn status --show-updates ` command if you want to see which files have been updated in the repository since your last update.   
