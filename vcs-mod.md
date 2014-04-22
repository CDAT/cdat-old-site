---
layout: default
title:
---

#  Python: package vcs

  
  
 vcs 
[ index ](/)  

` #&#160;VCS&#160;Visualization&#160;and&#160;Control&#160;System&#160;-&#160;(VCS)&#160;module  
#  
##############################################################################
###  
#
#  
#&#160;Module:&#160;&#160;&#160;&#160;&#160;&#160;&#160;vcs&#160;module
#  
#
#  
#&#160;Authors:&#160;&#160;&#160;&#160;&#160;&#160;PCMDI&#160;Software&#160;Team
#  
#&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;support@pcmdi.llnl.gov
#  
# [ http://esg.llnl.gov/cdat ](/cdat) #  
#
#  
#&#160;Description:&#160;&#160;Python&#160;command&#160;wrapper&#160;for&#160;VCS's&#160;functionality.&#160;VCS&#160;is
computer&#160;#  
#&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;software&#160;for&#160;the&#160;selection,&#160;manipulation,&#160;and&#160;display&#160;of
#  
#&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;scientific&#160;data.&#160;By&#160;specification&#160;of&#160;the&#160;desired&#160;data,&#160;the
#  
#&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;graphics&#160;method,&#160;and&#160;the&#160;display&#160;template,&#160;the&#160;VCS&#160;user&#160;gains
#  
#&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;virtually&#160;complete&#160;control&#160;of&#160;the&#160;appearance&#160;of&#160;the&#160;data
#  
#&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;display&#160;and&#160;associated&#160;text&#160;and&#160;animation.
#  
#
#  
##############################################################################
### `

  
 Package Contents 

` `

[ Canvas ](/vcs.Canvas.html)  
[ Pboxeslines ](/vcs.Pboxeslines.html)  
[ Pdata ](/vcs.Pdata.html)  
[ Pformat ](/vcs.Pformat.html)  
[ Plegend ](/vcs.Plegend.html)  
[ Ptext ](/vcs.Ptext.html)  
[ Pxlabels ](/vcs.Pxlabels.html)  
[ Pxtickmarks ](/vcs.Pxtickmarks.html)  
[ Pylabels ](/vcs.Pylabels.html)  
[ Pytickmarks ](/vcs.Pytickmarks.html)  
[ VCS_validation_functions ](/vcs.VCS_validation_functions.html)  
[ _vcs ](/vcs._vcs.html)  
[ animationgui ](/vcs.animationgui.html)  
[ boxfill ](/vcs.boxfill.html)  

[ colormap ](/vcs.colormap.html)  
[ colormapgui ](/vcs.colormapgui.html)  
[ colors ](/vcs.colors.html)  
[ continents ](/vcs.continents.html)  
[ displayplot ](/vcs.displayplot.html)  
[ error ](/vcs.error.html)  
[ fillarea ](/vcs.fillarea.html)  
[ fonteditorgui ](/vcs.fonteditorgui.html)  
[ graphicsmethodgui ](/vcs.graphicsmethodgui.html)  
[ gui_template_editor ](/vcs.gui_template_editor.html)  
[ install_vcs ](/vcs.install_vcs.html)  
[ isofill ](/vcs.isofill.html)  
[ isoline ](/vcs.isoline.html)  
[ line ](/vcs.line.html)  

[ lineeditorgui ](/vcs.lineeditorgui.html)  
[ marker ](/vcs.marker.html)  
[ meshfill ](/vcs.meshfill.html)  
[ outfill ](/vcs.outfill.html)  
[ outline ](/vcs.outline.html)  
[ pagegui ](/vcs.pagegui.html)  
[ pauser ](/vcs.pauser.html)  
[ projection ](/vcs.projection.html)  
[ projectiongui ](/vcs.projectiongui.html)  
[ queries ](/vcs.queries.html)  
[ scatter ](/vcs.scatter.html)  
[ slabapi ](/vcs.slabapi.html)  
[ taylor ](/vcs.taylor.html)  
[ template ](/vcs.template.html)  

[ templateeditorgui ](/vcs.templateeditorgui.html)  
[  test  (package) ](/vcs.test.html)  
[ testtemplate ](/vcs.testtemplate.html)  
[ textcombined ](/vcs.textcombined.html)  
[ textorientation ](/vcs.textorientation.html)  
[ texttable ](/vcs.texttable.html)  
[ utils ](/vcs.utils.html)  
[ vcshelp ](/vcs.vcshelp.html)  
[ vector ](/vcs.vector.html)  
[ xvsy ](/vcs.xvsy.html)  
[ xyvsy ](/vcs.xyvsy.html)  
[ yxvsx ](/vcs.yxvsx.html)  

  
 Functions 

` `

 init  (mode  =1  , pause_time  =0  , call_from_gui  =0  ) 
     ` Function:&#160;init&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#&#160;Initialize,&#160;Construct&#160;a&#160;VCS&#160;Canvas&#160;Object   
  
Description&#160;of&#160;Function:  
Construct&#160;the&#160;VCS&#160;Canas&#160;object.&#160;There&#160;can&#160;only&#160;be&#160;at&#160;most&#160;8&#160;VCS  
Canvases&#160;open&#160;at&#160;any&#160;given&#160;time.  
  
Example&#160;of&#160;Use:  
import&#160;vcs,cu  
  
file=cu.open('filename.nc')  
slab=file.getslab('variable')  
a=vcs. [ init ](/) ()&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#&#160;This&#160;examples&#160;constructs&#160;4&#160;VCS
Canvas  
a.plot(slab)&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#&#160;Plot&#160;slab&#160;using&#160;default&#160;settings  
b=vcs. [ init ](/) ()&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#&#160;Construct&#160;VCS&#160;object  
template=b.gettemplate('AMIP')&#160;&#160;&#160;&#160;&#160;&#160;#&#160;Get&#160;'example'&#160;template&#160;object  
b.plot(slab,template)&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#&#160;Plot&#160;slab&#160;using&#160;template&#160;'AMIP'  
c=vcs. [ init ](/) ()&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#&#160;Construct&#160;new&#160;VCS&#160;object  
isofill=c.getisofill('quick')&#160;&#160;&#160;&#160;&#160;&#160;&#160;#&#160;Get&#160;'quick'&#160;isofill&#160;graphics&#160;method  
c.plot(slab,template,isofill)&#160;&#160;&#160;&#160;&#160;&#160;&#160;#&#160;Plot&#160;slab&#160;using&#160;template&#160;and&#160;isofill
objects  
d=vcs. [ init ](/) ()&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#&#160;Construct&#160;new&#160;VCS&#160;object  
isoline=c.getisoline('quick')&#160;&#160;&#160;&#160;&#160;&#160;&#160;#&#160;Get&#160;'quick'&#160;isoline&#160;graphics&#160;method  
c.plot(isoline,slab,template)&#160;&#160;&#160;&#160;&#160;&#160;&#160;#&#160;Plot&#160;slab&#160;using&#160;isoline&#160;and&#160;template
objects `

  
 Data 

` `

 taylordiagrams  = [<vcs.taylor.Gtd instance>] 

* * *

UCRL-WEB-213937 | [ Privacy & Legal Notice ](/disclaimer.html)

[ webmaster@pcmdi.llnl.gov ](/webmaster@pcmdi.llnl.gov)

[ ![Powered by Plone](media/imgaes/plone_powered.gif) ](/)

