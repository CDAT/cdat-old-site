---
layout: default
title: 
---

      * [ f2py - Wrapping Fortran Code ](/cdat/tutorials/f2py-wrapping-fortran-code)

    * [ Quick Reference ](/cdat/quick_reference)

    * [ FAQ ](/cdat/FAQ)

    * [ Manuals ](/cdat/manuals)

    * [ Tips and Tricks ](/cdat/tips_and_tricks)

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

  * [ ![Send this page to somebody](media/mail_icon.gif) ](/cdat/tutorials/cdatbasics/plotting-basics/plotting-primitives/sendto_form)
  * [ ![Print this page](media/print_icon.gif) ](/this.print\(\))

#  Plotting Primitives

[ ![Table of Contents](media/arrow-up) ](/)

[ ![Previous](media/arrow-left) ](/save-plot-output)

[ ![Next](media/arrow-right) ](/creating-and-modifying-templates)

[ Contents ](/)

[ Previous ](/save-plot-output)

[ Next ](/creating-and-modifying-templates)

 Goal:  Guide you through plotting using graphics primitives.   

Before running the tutorial below, type _ "python" _ or _ "cdat" _ at the
command line.&#160; You will see the python prompt appear (i.e., ">>>"). You can
now enter the command lines below.  

You can [ _ _  view  _ _ ](/../files/primitive_file) or [ _ _  download
 _ _ ](/../files/primitive_file.py) the full source code. To run the source
code at the command line, type: _ "python primitive_file.py" _ .  

    
    
    # Import the modules needed for the tuturial  
    # vcs - Visualization and control System 1D and 2D plotting routines.  
    import vcs  
      
    # Initial VCS:  
    v = vcs.init()

There are four drawing primitives:

  1. Text 
  2. Lines 
  3. Markers 
  4. Fillareas 
All graphics primitives have a viewport and world coordinate associated with
them. If the graphics primitive's viewport and world coordinate values are not
set, the global v.viewport() (e.g., [0,1,0,1]) and v.world() (e.g., [0,1,0,1]
coodinate values will be used.

    
    
    # Import the modules needed for the tuturial  
    import vcs, sys  
      
    # Initial VCS:  
    v = vcs.init()  
      
    # Create and draw a "Text" on the VCS Canvas.  
    tex = v.createtext('nTtex','std','nToex','7left')  
    tex.height = 20  
    tex.x=[0.1, 0.1, 0.1]  
    tex.y=[0.97, 0.93, 0.89]  
    tex.string=['Example of drawing VCS low-level primitives.',  
      'Also, an example of using the viewport to clip graphics.',  
      'Here the viewport is the default [0,1,0,1], see markers below']  
    v.plot(tex)  
      
    print ""  
    print "Press the Return key to see the next set of primitives."  
    sys.stdin.readline()  
      
    # create marker in a shape of a dot to mark where the x coordinates   
    # of this viewport are  
    mk=v.createmarker('new')  
    mk.x=[0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9]  
    mk.y=[0.84,0.84,0.84,0.84,0.84,0.84,0.84,0.84,0.84]  
    mk.color=244  
    mk.size=7  
    mk.type='dot'  
    v.plot(mk)  
      
    # create ne text object, with default settings  
    # this text object will annotate the markers  
    t1 = v.createtext('new1')  
    t1.x=[0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9]  
    t1.y=[0.82,0.82,0.82,0.82,0.82,0.82,0.82,0.82,0.82]  
    t1.string=['x=0.1','0.2','0.3','0.4','0.5','0.6','0.7','0.8','0.9']  
    t1.height = 15  
    v.plot(t1)

![primitive1.png](media/primitive1.png)

    
    
    # Let the world coordinate values remain the default  
    # setting (i.e.,[0, 1, 0, 1]), but change the global viewport.  
    v.viewport=[0.3,0.7,0.3,0.7]  
      
    # Create the line, fill area, and text objects  
    ln=v.createline('new')  
    fa=v.createfillarea('new')  
    t=v.createtext('newTt','std','newTo','7left')  
      
    # Draw a box around the entire VCS Canvas viewport. It will   
    # use the global viewport setting above and use the default  
    # world coordinate values.  
    # Remember the default values for vp and wc are:  
    #            viewport         = [0.0, 1.0, 0.0, 1.0]  
    #            worldcoordinate  = [0.0, 1.0, 0.0, 1.0]  
    ln.x=[0, 1, 1, 0, 0]            # x line positions  
    ln.y=[0, 0, 1, 1, 0]            # y line positions  
    ln.width=4                      # test width  
    ln.color = 242                  # test color  
    ln.type = 4                     # test line type  
    v.plot(ln)                      # plot lines  
    print "Press the Return key to see the next set of primitives."  
    sys.stdin.readline()  
      
    # create another text object for the new vieport title  
    t3 = v.createtext('new3')  
    t3.x=[0.08]  
    t3.y=[0.91]  
    t3.color = 242  
    t3.string=['Here the vieport was changed to [0.2, 0.8, 0.1, 0.7]']  
    t3.height = 18  
    v.plot(t3)  
      
    # create another marker object, similar to previous one,  
    # place at the same coordinates   
    # notice where those x coordinates are in the new viewport  
    mk1=v.createmarker('new1')  
    mk1.x=[0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9]  
    mk1.y=[0.84,0.84,0.84,0.84,0.84,0.84,0.84,0.84,0.84]  
    mk1.color=242  
    mk1.size=6  
    mk1.type='dot'  
    v.plot(mk1)  
      
    # create new text object to annotate above markers  
    t2 = v.createtext('new2')  
    t2.x=[0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9]  
    t2.y=[0.81,0.81,0.81,0.81,0.81,0.81,0.81,0.81,0.81]  
    t2.string=['x=0.1','0.2','0.3','0.4','0.5','0.6','0.7','0.8','0.9']  
    t2.height = 13  
    t2.color = 242  
    v.plot(t2)

![primitive2.png](media/primitive2.png)  

    
    
    # Draw text on the screen. Use global vp and default wc.  
    t.x = [0.2, 0.5]               # x text positions  
    t.y = [0.7, 0.6]                # y text positions  
    t.string=['PCMDI', 'CDAT']      # text strings  
    t.color=243                     # text color  
    t.height = 50                   # text size  
    v.plot(t)                       # plot text  
    print "Press the Return key to see the next set of primitives."  
    sys.stdin.readline()  
      
    # Draw fill area on screen. Use global vp and default wc.  
    fa.x=[[0.0,0.5,0.5,0.0],[0.5,1.0,0.75] ]# x fill area positions  
    fa.y=[[0.0,0.0,0.5,0.5],[0.5,0.5,0.0] ]# x fill area positions  
      
    fa.color=[241,245]      # fill area color  
    fa.style='hatch'        # fill area style  
    fa.index=3              # fill area index  
    v.plot(fa)              # plot fill area   
    print "Press the Return key to end."  
    sys.stdin.readline()  
    

![primitive3.png](media/primitive3.png)

[ ![Table of Contents](media/arrow-up) ](/)

[ ![Previous](media/arrow-left) ](/save-plot-output)

[ ![Next](media/arrow-right) ](/creating-and-modifying-templates)
