---
layout: default
title: 
---

#####  Document Actions

  * [ ![Send this page to somebody](media/mail_icon.gif) ](/cdat/download/download/sendto_form)
  * [ ![Print this page](media/print_icon.gif) ](/this.print\(\))

#  Obtaining and Installing CDAT

#  CDAT is no longer supported as is, it has been superseded by UV-CDAT

  

###  For UV-CDAT install instructions see: [ UV-CDAT install site ](/install/)

  

###  For UV-CDAT see: [ UV-CDAT site ](/)

  

###  The following are the old instruction for CDAT 5.2 which is no longer
supported

  

####  Download Stable Releases

  * CDAT is no longer available via tarball, instead it is distributed via "subversion". 
  * Subversion can be obtained at: http://subversion.tigris.org/ 
  * Current version is: 
    * CDAT Version 5.2 (September 14h, 2009)   

      *             svn export http://www-pcmdi.llnl.gov/svn/repository/cdat/tags/5.2 cdat-5.2-src
            

      * Once you got the sources you can install CDAT as follow: 
      *             # Now you need to build cdat, terms in between [] are optional
            ./configure --prefix=CDAT_BUILD [--with-externals=CDAT_EXTERNALS] [--with-python=MY_PYTHON] [--with-opendap]
            # use ./configure --help for a list of all options!
            
            # Clean previous build, just in case
            make clean
            # And finally make and build cdat
            make
            # You can now start CDAT with the command
            CDAT_BUILD/bin/cdat
            

      * In addition 5.2 comes a few UNSUPPORTED binary tarball, these (and a tarball of the sources) can be found at: 
      * [ http://sourceforge.net/projects/cdat/files/Releases/5.2 ](/projects/cdat/files/Releases/5.2)
      * For more info on these binaries see [ this ](/installation-guide/copy_of_express-install) .   

###  Download Bleeding-Edge Source Code via Subversion

  * If you're brave or a developper you may want to access our development branch, this includes our latest version BUT may content unstable code. 
  * to do so follow these instruction: 
    * Create a directory to store your sources: CDAT_SRC, and choose a location where to build cdat: CDAT_BUILD 
    * Optionally you may decide on a directory where to install the externals libraries and programs needed by cdat CDAT_EXTERNALS (default is CDAT_BUILD/Externals) 
    * You can also use your own python if you want (it will still build packages in CDAT_BUILD, so you need to have write access to this location): MY_PYTHON   

    
    
    cd CDAT_SRC
    # The first time do:
    svn co http://www-pcmdi.llnl.gov/svn/repository/cdat/trunk .
    # Thereafter, to simply obtain the changes since your last time simply do
    svn update
    # Now you need to build cdat, terms in between [] are optional
    ./configure --prefix=CDAT_BUILD [--with-externals=CDAT_EXTERNALS] [--with-python=MY_PYTHON] [--with-opendap]
    # use ./configure --help for a list of all options!
    
    # Clean previous build, just in csae
    make clean
    # And finally make and build cdat
    make
    

Wait a while... You should now have a fully working cdat, if you run into any
problem please contact us and send us the logs located under the logs
directory

##  Old Versions:
