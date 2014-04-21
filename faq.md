---
layout: default
title: 
---


##  INSTALL

  *  Which Operating Systems are supported ? 
    * The list of supported platforms is [ here ](/../download/installation-guide/software-platforms) . 
  *  What are the system requirements ? 
    * Xlib 
    * ~60Mb of disk space, double that for temporary files during installation 
    * 64Mb of memory, but as always the more the merrier 
  *  Where do I&#160;get CDAT&#160;? 
    * Go to the [ Sourceforge CDAT Project Page ](/projects/cdat) . 
  *  Can I obtain the developpement (beta)&#160;version ? 
    * Yes, the sourceforge web page contains the latest stable version, but you can access the latest "experimental"&#160;version&#160; by following the instructions listed [ here ](/cdat/p4.html) . 
  *  Why do you distribute sources only ? 
    * We have had trouble getting binary distributions to work due to the complexity of this product. 
  *  What do I do if I have trouble building? 
    * If building CDAT on a Mac OS X 10.4.x and the netpbm lib doesn't build. Then disable netpbm for the build by tpying: " \--disable-netpbm". For example: "./express_install --disable-netpbm". 
    * If the cdms library doesn't build, or builds but you cannot import cdms, then try to disable the OPeNDAP library: "--disable-opendap". For example: "./express_install --disable-opendap". 
    * Make sure you read all of the README.txt file, including the "Notes". 
    * Take special note of the section near the top that describes settings required for your platform. 
    * Send email to cdat-discussion.sf.net, pasting in the log file from the component whose build failed. 

##  DOCUMENTATION

  *  I don't know python, does it matter ? 
    * CDAT is based on python, but the VCDAT GUI can help you to learn python and use CDAT without any knowledge of python. VCDAT can produce python scripts that reflect your session. 
    * Some good references for python can be found on the [ python web site ](/) , notably: 
      * [ Python for Newbies ](/doc/Newbies.html) \-- The very thing if you are new to Python-based codes. 
      * [ Python Documentation ](/doc/) \-- tutorial, library reference, .. 
  *  Where is the documentation ? 
    * [ Here ](/../)

##  GRAPHICS

  *  No postcript/encapsulated postscript/gif are produced; CDAT asks for gplot. Where can i find it ? 
    * You probably didn't build gplot, see the README.txt file in the top directory of your build directory. 
  *  Are X11R6 and Tcl/Tk bundled with CDAT? 
    * CDAT does  not  come with its own X11R6. On most platforms, X11R6 is located at: ` /usr/X11R6 ` . The CDAT GUI and graphics packages (Tcl/Tk, VCS, Xmgrace, etc) must have X11R6. Therefore, if X11R6 is not in the standard location, then you will need to set your ` LD_LIBRARY_PATH ` to point to the libraries. On some platforms, X11R6 does  *  not  *   come with the developer libraries (i.e., *.a files). If you cd to /usr/X11R6/lib and don't see the *.a files, then you need to install the *.a files into this directory. 
    * By default, CDAT builds Python with Tcl/Tk. Optionally, you can build your own Python without Tcl/Tk and build the rest of CDAT in expert mode. This can be accomplished by using the --disable-tkbuild flag while building CDAT. In either case, Python must have Tcl/Tk in order to run Tkinter, and Pmw. It is not recommended that you use --disable-tkbuild unless you know that you want to use the standard Tcl/Tk on that system (e.g., on the Mac OS platform, you can use Tcl/TK Aqua). 
  *  I have Ferret colormaps that I liked can I still use them in CDAT? 
    * CDAT comes a script that can convert Ferret colormaps to VCS, see the [ corresponding page ](/../tips_and_tricks/plot-color-and-colormap-tips/converting-ferret-colormaps-to-vcs-colormaps) in [ Tips and Tricks section ](/../tips_and_tricks/index.html) where you can find additional information about [ Colors and Colormaps ](/../tips_and_tricks/plot-color-and-colormap-tips/index) .   

##  DIAGNOSTICS

*  How do I calculate the stream function and velocity potential of the wind? 
    
    
    &#160;>>> import sphere

Doing that step will tell you if you have installed Spherepack and other
contributed packages

* Step 1. Get winds u and v and their grid vectors, longitude values (lonvals)and latitude values (latvals), from somewhere.This example uses 2D fields for simplicity. The fields must be global without missing values. Hint: latvals = u.getLatitude()[:] and lonvals = u.getLongitude()[:] 
* Step 2. Make an instance of the Sphere class, x, as 
    
    
    >>> x = sphere.Sphere(lonvals, latvals)

* Step 3. Compute the streamfunction, sf, and the velocity potential, vp, using 
    
    
    >>> sf, vp = x.sfvp(u, v)

If you do not have the contrib packages installed...... please install them by
reading the installation instructions.There is more extensive documentation of
the sphere module which I am attaching with this e-mail.

##  GENERAL

  *  I found a bug, how do i let you know ? 
    * The [ bug page ](/tracker/) is here, please check first that your bug isn't already checked in 
