---
layout: default
title: 
---


    * [ Source Code ](/cdat/source)

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

  * [ ![Send this page to somebody](media/mail_icon.gif) ](/cdat/tutorials/f2py-wrapping-fortran-code/part-4-packaging-all-this-into-something-that-can-be-distributed-very-advanced/sendto_form)
  * [ ![Print this page](media/print_icon.gif) ](/this.print\(\))

#  Part 4: Packaging all this into something that can be distributed
(advanced)

This section shows how to package all that we've shown before into something
you can redistribute

Files: [ sf.f90 ](/sf.f90) , [ stream_function_wrapper.py
](/stream_function_wrapper.py) , [ setup.py ](/setup.py) , [ __init__.py
](/myinit.py)

In order to distribute this to others we'd need to organize the thing a bit
better.

First of all we'll assume everything is going to be put in a directory called
"sf" after the name of the package we're creating

In this directory we will separate the fortran code from the python code

we will create 2 sub-directory: Src for the fortran and Lib for the python

In Src we will put the file [ sf.f90 ](/sf.f90) and Lib we will put the file [
stream_function_wrapper.py ](/stream_function_wrapper.py)

Now that this is done we need to create a "setup" file for the python
packaging suite tool, it is called " [ setup.py ](/setup.py) "

This file uses numpy.distutils.core

You can pretty much go throught it w/o really understanding it, just copy
paste,

The basics you need to know are:

files: List of the FORTRAN files needed

extra_link_args : if you need special arguments when building your fortran

libraries: a list of library name that are external and you need to link

library_dirs : a list of additional directories where to look for the
libraries

include_dirs: list of places where to look for include files

name/package_dir: ususally the same name (sf), the one in package_dir/packages
is the one that matters to you

    
    
    import sys
    
    # Gather up all the files we need.
    files = ['Src/sf.f90',]
    
    ## scypy_distutils Script
    from numpy.distutils.core import setup, Extension
    
    extra_link_args=[]
    if sys.platform=='darwin':
        extra_link_args = ['-bundle','-bundle_loader '+sys.prefix+'/bin/python']
        
    ## setup the python module
    setup(name="sf", # name of the package to import later
          ## Build fortran wrappers, uses f2py
          ## directories to search for libraries defined in setup.cfg
          ext_modules = [Extension('streamfunction',
                                   files,
    #                              libraries=[],
    #                              library_dirs=[],
    #   			       include_dirs=['Src'],
                                   extra_link_args=extra_link_args,
                                   ),
                         ],
          
    ##      ## Install these to their own directory
         package_dir={'sf':'Lib'},
         packages = ["sf"],
          
         )
    

Finally in the Lib directory we need to add a file called [ __init__.py
](/myinit.py) that is executed when importing the package. Basivally this
simply expose the function we want to the user

    
    
    ## Figures out which function we expose
    from stream_function_wrapper import zm_msf
    

Now all we need to do is to build and install this package

from the sf directory type:

    
    
    python setup.py build

Now if you are superuser or have write permission to your python distribution
directories you can type

    
    
    python setup.py install

Usually you won't have write permission, no worries, all you need to do is:

    
    
    python setup.py install --prefix=/mydir

Now you have one more thing to do before you can use this package:

in the script that will import the package add the following lines:

    
    
    import sys
