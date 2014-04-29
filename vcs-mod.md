---
layout: default
title:
---

##  Python: package vcs
###vcs 
    
    #  VCSVisualizationandControlSystem-(VCS)module                           #
    ###########################################################################
    #                                                                         #
    # Module:vcsmodule                                                        #
    #                                                                         #
    # Authors:  PCMDISoftwareTeam                                             #
    #           support@pcmdi.llnl.gov                                        #
    #           http://esg.llnl.gov/cdat                                      #
    #                                                                         #
    # Description:  PythoncommandwrapperforVCS'sfunctionality.VCSis computer  #
    #               softwarefortheselection,manipulation,anddisplayof         #
    #               scientificdata.Byspecificationofthedesireddata,the        #
    #               graphicsmethod,andthedisplaytemplate,theVCSusergains      #
    #               virtuallycompletecontroloftheappearanceofthedata          #
    #               displayandassociatedtextandanimation.                     #
    #                                                                         #
    ###########################################################################

  
###Package Contents 

* [Canvas](vcs.Canvas.html)  
* [Pboxeslines](vcs.Pboxeslines.html)  
* [Pdata](vcs.Pdata.html)  
* [Pformat](vcs.Pformat.html)  
* [Plegend](vcs.Plegend.html)  
* [Ptext](vcs.Ptext.html)  
* [Pxlabels](vcs.Pxlabels.html)  
* [Pxtickmarks](vcs.Pxtickmarks.html)  
* [Pylabels](vcs.Pylabels.html)  
* [Pytickmarks](vcs.Pytickmarks.html)  
* [VCS_validation_functions](vcs.VCS_validation_functions.html)  
* [vcs](vcs._vcs.html)  
* [animationgui](vcs.animationgui.html)  
* [boxfill](vcs.boxfill.html)  
* [colormap](vcs.colormap.html)  
* [colormapgui](vcs.colormapgui.html)  
* [colors](vcs.colors.html)  
* [continents](vcs.continents.html)  
* [displayplot](vcs.displayplot.html)  
* [error](vcs.error.html)  
* [fillarea](vcs.fillarea.html)  
* [fonteditorgui](vcs.fonteditorgui.html)  
* [graphicsmethodgui](vcs.graphicsmethodgui.html)  
* [gui_template_editor](vcs.gui_template_editor.html)  
* [install_vcs](vcs.install_vcs.html)  
* [isofill](vcs.isofill.html)  
* [isoline](vcs.isoline.html)  
* [line](vcs.line.html)  
* [lineeditorgui](vcs.lineeditorgui.html)  
* [marker](vcs.marker.html)  
* [meshfill](vcs.meshfill.html)  
* [outfill](vcs.outfill.html)  
* [outline](vcs.outline.html)  
* [pagegui](vcs.pagegui.html)  
* [pauser](vcs.pauser.html)  
* [projection](vcs.projection.html)  
* [projectiongui](vcs.projectiongui.html)  
* [queries](vcs.queries.html)  
* [scatter](vcs.scatter.html)  
* [slabapi](vcs.slabapi.html)  
* [taylor](vcs.taylor.html)  
* [template](vcs.template.html)  
* [templateeditorgui](vcs.templateeditorgui.html)  
* [ test  (package)](vcs.test.html)  
* [testtemplate](vcs.testtemplate.html)  
* [textcombined](vcs.textcombined.html)  
* [textorientation](vcs.textorientation.html)  
* [texttable](vcs.texttable.html)  
* [utils](vcs.utils.html)  
* [vcshelp](vcs.vcshelp.html)  
* [vector](vcs.vector.html)  
* [xvsy](vcs.xvsy.html)  
* [xyvsy](vcs.xyvsy.html)  
* [yxvsx](vcs.yxvsx.html)  

  
###Functions 

    init  (mode  =1  , pause_time  =0  , call_from_gui  =0  ) 
      Function:init#Initialize,ConstructaVCSCanvasObject   
  
    DescriptionofFunction:  
      ConstructtheVCSCanasobject.Therecanonlybeatmost8VCS  
      Canvasesopenatanygiventime.  
      
    ExampleofUse:  
    importvcs,cu  
      
    file=cu.open('filename.nc')
    slab=file.getslab('variable')
    a=vcs. [init](/) ()           # Thisexamplesconstructs4VCS Canvas  
    a.plot(slab)                  # Plotslabusingdefaultsettings 
    b=vcs. [init](/) ()           # ConstructVCSobject  
    template=b.gettemplate('AMIP')# Get'example'templateobject  
    b.plot(slab,template)         # Plotslabusingtemplate'AMIP'  
    c=vcs. [init](/) ()           # ConstructnewVCSobject  
    isofill=c.getisofill('quick') # Get'quick'isofillgraphicsmethod  
    c.plot(slab,template,isofill) # Plotslabusingtemplateandisofill objects  
    d=vcs. [init](/) ()           # ConstructnewVCSobject  
    isoline=c.getisoline('quick') # Get'quick'isolinegraphicsmethod  
    c.plot(isoline,slab,template) # Plotslabusingisolineandtemplate
    objects `

  
###Data 

     taylordiagrams  = [<vcs.taylor.Gtd instance>]
