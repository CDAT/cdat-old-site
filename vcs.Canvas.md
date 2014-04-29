---
layout: default
title:
---

 [ Skip to content. ](/cdat/source/api-reference/vcs.Canvas.html) | [ Skip to
navigation ](/cdat/source/api-reference/vcs.Canvas.html)

Search Site

[ Advanced Search&#8230; ](/search_form)

#  [ PCMDI Software Portal ](/)

#####  Sections

  * [ Home ](/)

#####  Personal tools

  * [ Log in ](/login_form)

You are here:  [ Home ](/) -> [ CDAT ](/cdat) -> [ Source Code ](/cdat/source)
-> [ API Reference ](/cdat/source/api-reference) -> Python: module vcs.Canvas

[ Navigation ](/sitemap)

    

  * [ Home ](/)

  * [ PCMDI Home Page ](/)

  * [ News ](/news)

  * [ CDAT ](/cdat)

    * [ Download and Install ](/cdat/download)

    * [ Screenshots ](/cdat/screenshots)

    * [ Contrib Packages ](/cdat/contrib)

    * [ Getting Started ](/cdat/getting_started)

    * [ Tutorials ](/cdat/tutorials)

    * [ Quick Reference ](/cdat/quick_reference)

    * [ FAQ ](/cdat/FAQ)

    * [ Manuals ](/cdat/manuals)

    * [ Tips and Tricks ](/cdat/tips_and_tricks)

    * [ Source Code ](/cdat/source)

      * [ API Reference ](/cdat/source/api-reference)

        * [ Python: module vcs.Canvas ](/cdat/source/api-reference/vcs.Canvas.html)

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

  * [ ![Send this page to somebody](media/mail_icon.gif) ](/cdat/source/api-reference/vcs.Canvas.html/sendto_form)
  * [ ![Print this page](media/print_icon.gif) ](/this.print\(\))

#  Python: module vcs.Canvas

  
  
 [ vcs  ](/vcs.html) .Canvas 
[ index ](/)  

` [ Canvas ](/) :&#160;the&#160;class&#160;representing&#160;a&#160;vcs&#160;drawing&#160;window  
Normally,&#160;created&#160;by&#160;vcs.init()  
Contains&#160;the&#160;method&#160;plot. `

  
 Modules 

` `

[ MA ](/MA.html)  
[ MV ](/MV.html)  
[ Numeric ](/Numeric.html)  
[ RandomArray ](/RandomArray.html)  
[ Tkinter ](/Tkinter.html)  
[ vcs.animationgui ](/vcs.animationgui.html)  
[ vcs.colormapgui ](/vcs.colormapgui.html)  
[ vcs.graphicsmethodgui ](/vcs.graphicsmethodgui.html)  
[ vcs.gui_template_editor ](/vcs.gui_template_editor.html)  
[ vcs.pagegui ](/vcs.pagegui.html)  
[ vcs.projectiongui ](/vcs.projectiongui.html)  
[ vcs._vcs ](/vcs._vcs.html)  

[ vcs.boxfill ](/vcs.boxfill.html)  
[ cdms ](/cdms.html)  
[ cdtime ](/cdtime.html)  
[ cdutil ](/cdutil.html)  
[ vcs.colormap ](/vcs.colormap.html)  
[ vcs.continents ](/vcs.continents.html)  
[ copy ](/copy.html)  
[ vcs.displayplot ](/vcs.displayplot.html)  
[ vcs.fillarea ](/vcs.fillarea.html)  
[ genutil ](/genutil.html)  
[ vcs.isofill ](/vcs.isofill.html)  
[ vcs.isoline ](/vcs.isoline.html)  

[ vcs.line ](/vcs.line.html)  
[ vcs.marker ](/vcs.marker.html)  
[ vcs.meshfill ](/vcs.meshfill.html)  
[ os ](/os.html)  
[ vcs.outfill ](/vcs.outfill.html)  
[ vcs.outline ](/vcs.outline.html)  
[ vcs.projection ](/vcs.projection.html)  
[ vcs.scatter ](/vcs.scatter.html)  
[ signal ](/signal.html)  
[ string ](/string.html)  
[ sys ](/sys.html)  
[ vcs.taylor ](/vcs.taylor.html)  

[ tempfile ](/tempfile.html)  
[ vcs.template ](/vcs.template.html)  
[ vcs.textcombined ](/vcs.textcombined.html)  
[ vcs.textorientation ](/vcs.textorientation.html)  
[ vcs.texttable ](/vcs.texttable.html)  
[ thread ](/thread.html)  
[ types ](/types.html)  
[ vcs ](/vcs.html)  
[ vcs.vector ](/vcs.vector.html)  
[ vcs.xvsy ](/vcs.xvsy.html)  
[ vcs.xyvsy ](/vcs.xyvsy.html)  
[ vcs.yxvsx ](/vcs.yxvsx.html)  

  
 Classes 

` `

[ Canvas ](/vcs.Canvas.html)

[ animate_obj ](/vcs.Canvas.html)

  
class  Canvas 

` `

` Function: [ Canvas ](/) #&#160;Construct&#160;a&#160;VCS [ Canvas ](/) class&#160;Object  
  
Description&#160;of&#160;Function:  
Construct&#160;the&#160;VCS&#160;Canas&#160;object.&#160;There&#160;can&#160;only&#160;be&#160;at&#160;most&#160;8&#160;VCS  
Canvases&#160;open&#160;at&#160;any&#160;given&#160;time.  
  
Example&#160;of&#160;Use:  
a=vcs. [ Canvas ](/) ()&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#&#160;This&#160;examples&#160;constructs&#160;a&#160;VCS [
Canvas ](/)  
`

Methods defined here:  

 BLOCK_X_SERVER  (self, *args) 
     ` #############################################################################   
#&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#  
#&#160;Block&#160;the&#160;X&#160;server.&#160;It&#160;may&#160;NOT&#160;process&#160;do&#160;X11&#160;commands.&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#  
#&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#  
#############################################################################
`

 SCREEN_MODE  (self, *args) 
     ` #############################################################################   
#&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#  
#&#160;Return&#160;the&#160;Screen&#160;mode,&#160;either&#160;data&#160;mode&#160;or&#160;template&#160;editor&#160;mode.&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#  
#&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#  
#############################################################################
`

 UNBLOCK_X_SERVER  (self, *args) 
     ` #############################################################################   
#&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#  
#&#160;Unblock&#160;the&#160;X&#160;server.&#160;It&#160;may&#160;now&#160;proceed&#160;to&#160;do&#160;X11&#160;commands.&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#  
#&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#  
#############################################################################
`

 __init__  (self, mode  =1  , pause_time  =0  , call_from_gui  =0  ) 
     ` #############################################################################   
#&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#  
#&#160;Initialize&#160;the&#160;VCS [ Canvas ](/) and&#160;set&#160;the [ Canvas ](/) mode&#160;to&#160;0.
Because&#160;the&#160;mode&#160;&#160;#  
#&#160;is&#160;set&#160;to&#160;0,&#160;the&#160;user&#160;will&#160;have&#160;to&#160;manually&#160;update&#160;the&#160;VCS [ Canvas ](/) by
#  
#&#160;using&#160;the&#160;"update"&#160;function.&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#  
#&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#  
#############################################################################
`

 __setattr__  (self, name, value) 
     ` #############################################################################   
#&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#  
#&#160;Set&#160;attributes&#160;for&#160;VCS [ Canvas ](/) Class&#160;(i.e.,&#160;set&#160;VCS [ Canvas ](/)
Mode).&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#  
#&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#  
#############################################################################
`

 backing_store  (self, *args) 
     ` Function:&#160;backing_store   
  
Description&#160;of&#160;Function:  
This&#160;function&#160;creates&#160;a&#160;backing&#160;store&#160;pixmap&#160;for&#160;the&#160;VCS [ Canvas ](/) .  
  
Example&#160;of&#160;Use:  
a=vcs.init()  
a. [ backing_store ](/) () `

 boxfill  (self, *args, parms) 
     ` Function:&#160;boxfill&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#&#160;Generate&#160;a&#160;boxfill&#160;plot   
  
Description&#160;of&#160;Function:  
Generate&#160;a&#160;boxfill&#160;plot&#160;given&#160;the&#160;data,&#160;boxfill&#160;graphics&#160;method,&#160;and  
template.&#160;If&#160;no&#160;boxfill&#160;class&#160;object&#160;is&#160;given,&#160;then&#160;the&#160;'default'&#160;boxfill  
graphics&#160;method&#160;is&#160;used.&#160;Similarly,&#160;if&#160;no&#160;template&#160;class&#160;object&#160;is&#160;given,  
then&#160;the&#160;'default'&#160;template&#160;is&#160;used.  
  
Example&#160;of&#160;Use:  
a=vcs.init()  
a. [ show ](/) ('boxfill')&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#&#160;Show&#160;all&#160;the&#160;existing
boxfill&#160;graphics&#160;methods  
box=a. [ getboxfill ](/) ('quick')&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#&#160;Create&#160;instance&#160;of&#160;'quick'  
a. [ boxfill ](/) (array,box)&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#&#160;Plot&#160;array&#160;using&#160;specified&#160;box
and&#160;default  
#&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;template  
templt=a. [ gettemplate ](/) ('AMIP')&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#&#160;Create&#160;an&#160;instance&#160;of&#160;template
'AMIP'  
a. [ clear ](/) ()&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#&#160;Clear&#160;VCS&#160;canvas  
a. [ boxfill ](/) (array,box,template)&#160;&#160;&#160;&#160;&#160;&#160;&#160;#&#160;Plot&#160;array&#160;using&#160;specified&#160;box
and&#160;template  
a. [ boxfill ](/) (box,array,template)&#160;&#160;&#160;&#160;&#160;&#160;&#160;#&#160;Plot&#160;array&#160;using&#160;specified&#160;box
and&#160;template  
a. [ boxfill ](/) (template,array,box)&#160;&#160;&#160;&#160;&#160;&#160;&#160;#&#160;Plot&#160;array&#160;using&#160;specified&#160;box
and&#160;template  
a. [ boxfill ](/) (template,array,box)&#160;&#160;&#160;&#160;&#160;&#160;&#160;#&#160;Plot&#160;array&#160;using&#160;specified&#160;box
and&#160;template  
a. [ boxfill ](/) (array,'AMIP','quick')&#160;&#160;&#160;&#160;&#160;#&#160;Use&#160;'AMIP'&#160;template&#160;and&#160;'quick'
boxfill  
a. [ boxfill ](/) ('AMIP',array,'quick')&#160;&#160;&#160;&#160;&#160;#&#160;Use&#160;'AMIP'&#160;template&#160;and&#160;'quick'
boxfill  
a. [ boxfill ](/) ('AMIP','quick',array)&#160;&#160;&#160;&#160;&#160;#&#160;Use&#160;'AMIP'&#160;template&#160;and&#160;'quick'
boxfill `

 canvasid  (self, *args) 
     ` Function:&#160;canvasid   
  
Description&#160;of&#160;Function:  
Return&#160;VCS [ Canvas ](/) object&#160;ID.&#160;This&#160;ID&#160;number&#160;is&#160;found&#160;at&#160;the&#160;top&#160;of&#160;the
VCS [ Canvas ](/)  
as&#160;part&#160;of&#160;its&#160;title.  
  
Example&#160;of&#160;Use:  
a=vcs.init()  
a. [ open ](/) ()  
id&#160;=&#160;a. [ canvasid ](/) () `

 canvasinfo  (self, *args) 
     ` Function:&#160;canvasinfo   
  
Description&#160;of&#160;Function:  
Obtain&#160;the&#160;current&#160;attributes&#160;of&#160;the&#160;VCS [ Canvas ](/) window.  
  
Example&#160;of&#160;Use:  
a=vcs.init()  
a. [ plot ](/) (array,'default','isofill','quick')  
a. [ canvasinfo ](/) () `

 canvasraised  (self, *args) 
     ` Function:&#160;canvasraised&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#&#160;Raise&#160;the&#160;VCS [ Canvas ](/) to&#160;the&#160;top   
  
Description&#160;of&#160;Function:  
This&#160;function&#160;marks&#160;a&#160;VCS [ Canvas ](/) as&#160;eligible&#160;to&#160;be&#160;displayed&#160;and  
positions&#160;the&#160;window&#160;at&#160;the&#160;top&#160;of&#160;the&#160;stack&#160;of&#160;its&#160;siblings.  
  
Example&#160;of&#160;Use:  
a=vcs.init()  
...  
  
a. [ canvasraised ](/) () `

 cgm  (self, *args) 
     ` Function:&#160;cgm   
  
Description&#160;of&#160;Function:  
To&#160;save&#160;a&#160;graphics&#160;plot&#160;in&#160;CDAT&#160;the&#160;user&#160;can&#160;call&#160;CGM&#160;along&#160;with&#160;the&#160;name&#160;of  
the&#160;output.&#160;This&#160;routine&#160;will&#160;save&#160;the&#160;displayed&#160;image&#160;on&#160;the&#160;VCS&#160;canvas&#160;as  
a&#160;binary&#160;vector&#160;graphics&#160;that&#160;can&#160;be&#160;imported&#160;into&#160;MSWord&#160;or&#160;Framemaker.&#160;CGM  
files&#160;are&#160;in&#160;ISO&#160;standards&#160;output&#160;format.  
  
The&#160;CGM&#160;command&#160;is&#160;used&#160;to&#160;create&#160;or&#160;append&#160;to&#160;a&#160;cgm&#160;file.&#160;There&#160;are&#160;two&#160;modes  
for&#160;saving&#160;a&#160;cgm&#160;file:&#160;`Append'&#160;mode&#160;(a)&#160;appends&#160;cgm&#160;output&#160;to&#160;an&#160;existing&#160;cgm  
file;&#160;`Replace'&#160;(r)&#160;mode&#160;overwrites&#160;an&#160;existing&#160;cgm&#160;file&#160;with&#160;new&#160;cgm&#160;output.  
The&#160;default&#160;mode&#160;is&#160;to&#160;overwrite&#160;an&#160;existing&#160;cgm&#160;file&#160;(i.e.&#160;mode&#160;(r)).  
  
Example&#160;of&#160;Use:  
a=vcs.init()  
a. [ plot ](/) (array,'default','isofill','quick')  
a. [ cgm ](/) (o)  
a. [ cgm ](/) ('example')&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#&#160;by&#160;default&#160;a&#160;cgm&#160;file&#160;will&#160;overwrite&#160;an
existing&#160;file  
a. [ cgm ](/) ('example','a')&#160;&#160;#&#160;'a'&#160;will&#160;instruct&#160;cgm&#160;to&#160;append&#160;to&#160;an
existing&#160;file  
a. [ cgm ](/) ('example','r')&#160;&#160;#&#160;'r'&#160;will&#160;instruct&#160;cgm&#160;to&#160;overwrite&#160;an
existing&#160;file `

 clear  (self, *args) 
     ` Function:&#160;clear   
  
Description&#160;of&#160;Function:  
In&#160;VCS&#160;it&#160;is&#160;necessary&#160;to&#160;clear&#160;all&#160;the&#160;plots&#160;from&#160;a&#160;page.&#160;This&#160;routine  
will&#160;clear&#160;all&#160;the&#160;VCS&#160;displays&#160;on&#160;a&#160;page&#160;(i.e.,&#160;the&#160;VCS [ Canvas ](/)
object).  
  
Example&#160;of&#160;Use:  
a=vcs.init()  
a. [ plot ](/) (array,'default','isofill','quick')  
a. [ clear ](/) () `

 close  (self, *args) 
     ` Function:&#160;close   
  
Description&#160;of&#160;Function:  
Close&#160;the&#160;VCS [ Canvas ](/) .&#160;It&#160;will&#160;not&#160;deallocate&#160;the&#160;VCS [ Canvas ](/)
object.  
To&#160;deallocate&#160;the&#160;VCS [ Canvas ](/) ,&#160;use&#160;the&#160;destroy&#160;method.  
  
Example&#160;of&#160;Use:  
a=vcs.init()  
a. [ plot ](/) (array,'default','isofill','quick')  
a. [ close ](/) () `

 colormapgui  (self, gui_parent  =None  , transient  =0  , max_intensity  =None  ) 
     ` Function:&#160;colormapgui   
  
Description&#160;of&#160;Function:  
Run&#160;the&#160;VCS&#160;colormap&#160;interface.  
  
The&#160;colormapgui&#160;command&#160;is&#160;used&#160;to&#160;bring&#160;up&#160;the&#160;VCS&#160;colormap&#160;interface.&#160;The
interface  
is&#160;used&#160;to&#160;select,&#160;create,&#160;change,&#160;or&#160;remove&#160;colormaps.  
  
Example&#160;of&#160;Use:  
a=vcs.init()  
a. [ colormapgui ](/) ()  
a. [ colormapgui ](/) (max_intensity&#160;=&#160;255) `

 continents  (self, *args, parms) 
     ` Function:&#160;continents&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#&#160;Generate&#160;a&#160;continents&#160;plot   
  
Description&#160;of&#160;Function:  
Generate&#160;a&#160;continents&#160;plot&#160;given&#160;the&#160;data,&#160;continents&#160;graphics&#160;method,&#160;and  
template.&#160;If&#160;no&#160;continents&#160;class&#160;object&#160;is&#160;given,&#160;then&#160;the&#160;'default'
continents  
graphics&#160;method&#160;is&#160;used.&#160;Similarly,&#160;if&#160;no&#160;template&#160;class&#160;object&#160;is&#160;given,  
then&#160;the&#160;'default'&#160;template&#160;is&#160;used.  
  
Example&#160;of&#160;Use:  
a=vcs.init()  
a. [ show ](/) ('continents')&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#&#160;Show&#160;all&#160;the&#160;existing
continents&#160;graphics  
#&#160;methods  
con=a. [ getcontinents ](/) ('quick')&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#&#160;Create&#160;instance&#160;of&#160;'quick'  
a. [ continents ](/) (array,con)&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#&#160;Plot&#160;array&#160;using&#160;specified&#160;con
and&#160;default  
#&#160;&#160;&#160;&#160;&#160;&#160;&#160;template  
a. [ clear ](/) ()&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#&#160;Clear&#160;VCS&#160;canvas  
a. [ continents ](/) (array,con,template)&#160;&#160;&#160;&#160;#&#160;Plot&#160;array&#160;using&#160;specified&#160;con
and&#160;template `

 createboxfill  (self, Gfb_name  =None  , Gfb_name_src  ='default'  ) 
     ` Function:&#160;createboxfill&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#&#160;Construct&#160;a&#160;new&#160;boxfill&#160;graphics&#160;method   
  
Description&#160;of&#160;Function:  
Create&#160;a&#160;new&#160;boxfill&#160;graphics&#160;method&#160;given&#160;the&#160;the&#160;name&#160;and&#160;the&#160;existing  
boxfill&#160;graphics&#160;method&#160;to&#160;copy&#160;the&#160;attributes&#160;from.&#160;If&#160;no&#160;existing  
boxfill&#160;graphics&#160;method&#160;name&#160;is&#160;given,&#160;then&#160;the&#160;default&#160;boxfill&#160;graphics  
method&#160;will&#160;be&#160;used&#160;as&#160;the&#160;graphics&#160;method&#160;to&#160;which&#160;the&#160;attributes&#160;will  
be&#160;copied&#160;from.  
  
If&#160;the&#160;name&#160;provided&#160;already&#160;exists,&#160;then&#160;a&#160;error&#160;will&#160;be&#160;returned.&#160;Graphics  
method&#160;names&#160;must&#160;be&#160;unique.  
  
Example&#160;of&#160;Use:  
a=vcs.init()  
a. [ show ](/) ('boxfill')  
box=a. [ createboxfill ](/) ('example1',)  
a. [ show ](/) ('boxfill')  
box=a. [ createboxfill ](/) ('example2','quick')  
a. [ show ](/) ('boxfill') `

 createcolormap  (self, Cp_name  =None  , Cp_name_src  ='default'  ) 
     ` Function:&#160;createcolormap&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#&#160;Construct&#160;a&#160;new&#160;colormap&#160;secondary&#160;method   
  
Description&#160;of&#160;Function:  
Create&#160;a&#160;new&#160;colormap&#160;secondary&#160;method&#160;given&#160;the&#160;the&#160;name&#160;and&#160;the&#160;existing  
colormap&#160;secondary&#160;method&#160;to&#160;copy&#160;the&#160;attributes&#160;from.&#160;If&#160;no&#160;existing&#160;colormap  
secondary&#160;method&#160;name&#160;is&#160;given,&#160;then&#160;the&#160;default&#160;colormap&#160;secondary&#160;method  
will&#160;be&#160;used&#160;as&#160;the&#160;secondary&#160;method&#160;to&#160;which&#160;the&#160;attributes&#160;will&#160;be  
copied&#160;from.  
  
If&#160;the&#160;name&#160;provided&#160;already&#160;exists,&#160;then&#160;a&#160;error&#160;will&#160;be&#160;returned.  
Secondary&#160;method&#160;names&#160;must&#160;be&#160;unique.  
  
Example&#160;of&#160;Use:  
a=vcs.init()  
cp=a. [ createcolormap ](/) ('example1',)  
a. [ show ](/) ('colormap')  
cp=a. [ createcolormap ](/) ('example2','AMIP')  
a. [ show ](/) ('colormap') `

 createcontinents  (self, Gcon_name  =None  , Gcon_name_src  ='default'  ) 
     ` Function:&#160;createcontinents&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#&#160;Construct&#160;a&#160;new&#160;continents&#160;graphics&#160;method   
  
Description&#160;of&#160;Function:  
Create&#160;a&#160;new&#160;continents&#160;graphics&#160;method&#160;given&#160;the&#160;the&#160;name&#160;and&#160;the&#160;existing  
continents&#160;graphics&#160;method&#160;to&#160;copy&#160;the&#160;attributes&#160;from.&#160;If&#160;no&#160;existing  
continents&#160;graphics&#160;method&#160;name&#160;is&#160;given,&#160;then&#160;the&#160;default&#160;continents&#160;graphics  
method&#160;will&#160;be&#160;used&#160;as&#160;the&#160;graphics&#160;method&#160;to&#160;which&#160;the&#160;attributes&#160;will  
be&#160;copied&#160;from.  
  
If&#160;the&#160;name&#160;provided&#160;already&#160;exists,&#160;then&#160;a&#160;error&#160;will&#160;be&#160;returned.&#160;Graphics  
method&#160;names&#160;must&#160;be&#160;unique.  
  
Example&#160;of&#160;Use:  
a=vcs.init()  
a. [ show ](/) ('continents')  
con=a. [ createcontinents ](/) ('example1',)  
a. [ show ](/) ('continents')  
con=a. [ createcontinents ](/) ('example2','quick')  
a. [ show ](/) ('continents') `

 createfillarea  (self, name  =None  , name_src  ='default'  , style  =None  , index  =None  , color  =None  , priority  =1  , viewport  =None  , worldcoordinate  =None  , x  =None  , y  =None  ) 
     ` Function:&#160;createfillarea&#160;&#160;&#160;&#160;&#160;#&#160;Construct&#160;a&#160;new&#160;fillarea&#160;secondary&#160;method   
  
Description&#160;of&#160;Function:  
Create&#160;a&#160;new&#160;fillarea&#160;secondary&#160;method&#160;given&#160;the&#160;the&#160;name&#160;and&#160;the&#160;existing  
fillarea&#160;secondary&#160;method&#160;to&#160;copy&#160;the&#160;attributes&#160;from.&#160;If&#160;no&#160;existing&#160;fillarea  
secondary&#160;method&#160;name&#160;is&#160;given,&#160;then&#160;the&#160;default&#160;fillarea&#160;secondary&#160;method  
will&#160;be&#160;used&#160;as&#160;the&#160;secondary&#160;method&#160;to&#160;which&#160;the&#160;attributes&#160;will&#160;be  
copied&#160;from.  
  
If&#160;the&#160;name&#160;provided&#160;already&#160;exists,&#160;then&#160;a&#160;error&#160;will&#160;be&#160;returned.  
Secondary&#160;method&#160;names&#160;must&#160;be&#160;unique.  
  
Example&#160;of&#160;Use:  
a=vcs.init()  
a. [ show ](/) ('fillarea')  
fa=a. [ createfillarea ](/) ('example1',)  
a. [ show ](/) ('fillarea')  
fa=a. [ createfillarea ](/) ('example2','black')  
a. [ show ](/) ('fillarea')  
fa2=a. [ createmarker ](/) (name='new',&#160;name_src='red',style=1,&#160;index=1,  
color=242,&#160;priority=1,&#160;viewport=[0,&#160;2.0,&#160;0,&#160;2.0],  
worldcoordinate=[0,100,&#160;0,50]  
x=[0,20,40,60,80,100],  
y=[0,10,20,30,40,50]&#160;)&#160;&#160;&#160;&#160;&#160;&#160;#&#160;Create&#160;instance&#160;of&#160;fill&#160;area&#160;object&#160;'red'  
a. [ fillarea ](/) (fa2)&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#&#160;Plot&#160;using&#160;specified&#160;fill&#160;area
object `

 createisofill  (self, Gfi_name  =None  , Gfi_name_src  ='default'  ) 
     ` Function:&#160;createisofill&#160;&#160;#&#160;Construct&#160;a&#160;new&#160;isofill&#160;graphics&#160;method   
  
Description&#160;of&#160;Function:  
Create&#160;a&#160;new&#160;isofill&#160;graphics&#160;method&#160;given&#160;the&#160;the&#160;name&#160;and&#160;the&#160;existing  
isofill&#160;graphics&#160;method&#160;to&#160;copy&#160;the&#160;attributes&#160;from.&#160;If&#160;no&#160;existing  
isofill&#160;graphics&#160;method&#160;name&#160;is&#160;given,&#160;then&#160;the&#160;default&#160;isofill&#160;graphics  
method&#160;will&#160;be&#160;used&#160;as&#160;the&#160;graphics&#160;method&#160;to&#160;which&#160;the&#160;attributes&#160;will  
be&#160;copied&#160;from.  
  
If&#160;the&#160;name&#160;provided&#160;already&#160;exists,&#160;then&#160;a&#160;error&#160;will&#160;be&#160;returned.&#160;Graphics  
method&#160;names&#160;must&#160;be&#160;unique.  
  
Example&#160;of&#160;Use:  
a=vcs.init()  
a. [ show ](/) ('isofill')  
iso=a. [ createisofill ](/) ('example1',)  
a. [ show ](/) ('isofill')  
iso=a. [ createisofill ](/) ('example2','quick')  
a. [ show ](/) ('isofill') `

 createisoline  (self, Gi_name  =None  , Gi_name_src  ='default'  ) 
     ` Function:&#160;createisoline&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#&#160;Construct&#160;a&#160;new&#160;isoline&#160;graphics&#160;method   
  
Description&#160;of&#160;Function:  
Create&#160;a&#160;new&#160;isoline&#160;graphics&#160;method&#160;given&#160;the&#160;the&#160;name&#160;and&#160;the&#160;existing  
isoline&#160;graphics&#160;method&#160;to&#160;copy&#160;the&#160;attributes&#160;from.&#160;If&#160;no&#160;existing  
isoline&#160;graphics&#160;method&#160;name&#160;is&#160;given,&#160;then&#160;the&#160;default&#160;isoline&#160;graphics  
method&#160;will&#160;be&#160;used&#160;as&#160;the&#160;graphics&#160;method&#160;to&#160;which&#160;the&#160;attributes&#160;will  
be&#160;copied&#160;from.  
  
If&#160;the&#160;name&#160;provided&#160;already&#160;exists,&#160;then&#160;a&#160;error&#160;will&#160;be&#160;returned.&#160;Graphics  
method&#160;names&#160;must&#160;be&#160;unique.  
  
Example&#160;of&#160;Use:  
  
a=vcs.init()  
a. [ show ](/) ('isoline')  
iso=a. [ createisoline ](/) ('example1',)  
a. [ show ](/) ('isoline')  
iso=a. [ createisoline ](/) ('example2','quick')  
a. [ show ](/) ('isoline') `

 createline  (self, name  =None  , name_src  ='default'  , ltype  =None  , width  =None  , color  =None  , priority  =1  , viewport  =None  , worldcoordinate  =None  , x  =None  , y  =None  , projection  ='default'  ) 
     ` Function:&#160;createline&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#&#160;Construct&#160;a&#160;new&#160;line&#160;secondary&#160;method   
  
Description&#160;of&#160;Function:  
Create&#160;a&#160;new&#160;line&#160;secondary&#160;method&#160;given&#160;the&#160;the&#160;name&#160;and&#160;the&#160;existing  
line&#160;secondary&#160;method&#160;to&#160;copy&#160;the&#160;attributes&#160;from.&#160;If&#160;no&#160;existing&#160;line  
secondary&#160;method&#160;name&#160;is&#160;given,&#160;then&#160;the&#160;default&#160;line&#160;secondary&#160;method  
will&#160;be&#160;used&#160;as&#160;the&#160;secondary&#160;method&#160;to&#160;which&#160;the&#160;attributes&#160;will&#160;be  
copied&#160;from.  
  
If&#160;the&#160;name&#160;provided&#160;already&#160;exists,&#160;then&#160;a&#160;error&#160;will&#160;be&#160;returned.  
Secondary&#160;method&#160;names&#160;must&#160;be&#160;unique.  
  
Example&#160;of&#160;Use:  
a=vcs.init()  
a. [ show ](/) ('line')  
ln=a. [ createline ](/) ('example1',)  
a. [ show ](/) ('line')  
ln=a. [ createline ](/) ('example2','black')  
a. [ show ](/) ('line')  
ln2=a. [ createline ](/) (name='new',&#160;name_src='red',ltype='dash',&#160;width=2,  
color=242,&#160;priority=1,&#160;viewport=[0,&#160;2.0,&#160;0,&#160;2.0],  
worldcoordinate=[0,100,&#160;0,50]  
x=[0,20,40,60,80,100],  
y=[0,10,20,30,40,50]&#160;)&#160;&#160;&#160;&#160;&#160;&#160;#&#160;Create&#160;instance&#160;of&#160;line&#160;object&#160;'red'  
a. [ line ](/) (ln2)&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#&#160;Plot&#160;using&#160;specified&#160;line&#160;object `

 createmarker  (self, name  =None  , name_src  ='default'  , mtype  =None  , size  =None  , color  =None  , priority  =1  , viewport  =None  , worldcoordinate  =None  , x  =None  , y  =None  , projection  =None  ) 
     ` Function:&#160;createmarker&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#&#160;Construct&#160;a&#160;new&#160;marker&#160;secondary&#160;method   
  
Description&#160;of&#160;Function:  
Create&#160;a&#160;new&#160;marker&#160;secondary&#160;method&#160;given&#160;the&#160;the&#160;name&#160;and&#160;the&#160;existing  
marker&#160;secondary&#160;method&#160;to&#160;copy&#160;the&#160;attributes&#160;from.&#160;If&#160;no&#160;existing&#160;marker  
secondary&#160;method&#160;name&#160;is&#160;given,&#160;then&#160;the&#160;default&#160;marker&#160;secondary&#160;method  
will&#160;be&#160;used&#160;as&#160;the&#160;secondary&#160;method&#160;to&#160;which&#160;the&#160;attributes&#160;will&#160;be  
copied&#160;from.  
  
If&#160;the&#160;name&#160;provided&#160;already&#160;exists,&#160;then&#160;a&#160;error&#160;will&#160;be&#160;returned.  
Secondary&#160;method&#160;names&#160;must&#160;be&#160;unique.  
  
Example&#160;of&#160;Use:  
a=vcs.init()  
a. [ show ](/) ('marker')  
mrk=a. [ createmarker ](/) ('example1',)  
a. [ show ](/) ('marker')  
mrk=a. [ createmarker ](/) ('example2','black')  
a. [ show ](/) ('boxfill')  
mrk2=a. [ createmarker ](/) (name='new',&#160;name_src='red',mtype='dash',&#160;size=2,  
color=242,&#160;priority=1,&#160;viewport=[0,&#160;2.0,&#160;0,&#160;2.0],  
worldcoordinate=[0,100,&#160;0,50]  
x=[0,20,40,60,80,100],  
y=[0,10,20,30,40,50]&#160;)&#160;&#160;&#160;&#160;&#160;&#160;#&#160;Create&#160;instance&#160;of&#160;marker&#160;object&#160;'red'  
a. [ marker ](/) (mrk2)&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#&#160;Plot&#160;using&#160;specified&#160;marker
object `

 createmeshfill  (self, Gfm_name  =None  , Gfm_name_src  ='default'  ) 
     ` Function:&#160;createmeshfill&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#&#160;Construct&#160;a&#160;new&#160;meshfill&#160;graphics&#160;method   
  
Description&#160;of&#160;Function:  
Create&#160;a&#160;new&#160;meshfill&#160;graphics&#160;method&#160;given&#160;the&#160;the&#160;name&#160;and&#160;the&#160;existing  
meshfill&#160;graphics&#160;method&#160;to&#160;copy&#160;the&#160;attributes&#160;from.&#160;If&#160;no&#160;existing  
meshfill&#160;graphics&#160;method&#160;name&#160;is&#160;given,&#160;then&#160;the&#160;default&#160;meshfill&#160;graphics  
method&#160;will&#160;be&#160;used&#160;as&#160;the&#160;graphics&#160;method&#160;to&#160;which&#160;the&#160;attributes&#160;will  
be&#160;copied&#160;from.  
  
If&#160;the&#160;name&#160;provided&#160;already&#160;exists,&#160;then&#160;a&#160;error&#160;will&#160;be&#160;returned.&#160;Graphics  
method&#160;names&#160;must&#160;be&#160;unique.  
  
Example&#160;of&#160;Use:  
a=vcs.init()  
a. [ show ](/) ('meshfill')  
mesh=a. [ createmeshfill ](/) ('example1',)  
a. [ show ](/) ('meshfill')  
mesh=a. [ createmeshfill ](/) ('example2','quick')  
a. [ show ](/) ('meshfill') `

 createoutfill  (self, Gfo_name  =None  , Gfo_name_src  ='default'  ) 
     ` Function:&#160;createoutfill&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#&#160;Construct&#160;a&#160;new&#160;outfill&#160;graphics&#160;method   
  
Description&#160;of&#160;Function:  
Create&#160;a&#160;new&#160;outfill&#160;graphics&#160;method&#160;given&#160;the&#160;the&#160;name&#160;and&#160;the&#160;existing  
outfill&#160;graphics&#160;method&#160;to&#160;copy&#160;the&#160;attributes&#160;from.&#160;If&#160;no&#160;existing  
outfill&#160;graphics&#160;method&#160;name&#160;is&#160;given,&#160;then&#160;the&#160;default&#160;outfill&#160;graphics  
method&#160;will&#160;be&#160;used&#160;as&#160;the&#160;graphics&#160;method&#160;to&#160;which&#160;the&#160;attributes&#160;will  
be&#160;copied&#160;from.  
  
If&#160;the&#160;name&#160;provided&#160;already&#160;exists,&#160;then&#160;a&#160;error&#160;will&#160;be&#160;returned.&#160;Graphics  
method&#160;names&#160;must&#160;be&#160;unique.  
  
Example&#160;of&#160;Use:  
  
a=vcs.init()  
a. [ show ](/) ('outfill')  
out=a. [ createoutfill ](/) ('example1',)  
a. [ show ](/) ('outfill')  
out=a. [ createoutfill ](/) ('example2','quick')  
a. [ show ](/) ('outfill') `

 createoutline  (self, Go_name  =None  , Go_name_src  ='default'  ) 
     ` Function:&#160;createoutline&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#&#160;Construct&#160;a&#160;new&#160;outline&#160;graphics&#160;method   
  
Description&#160;of&#160;Function:  
Create&#160;a&#160;new&#160;outline&#160;graphics&#160;method&#160;given&#160;the&#160;the&#160;name&#160;and&#160;the&#160;existing  
outline&#160;graphics&#160;method&#160;to&#160;copy&#160;the&#160;attributes&#160;from.&#160;If&#160;no&#160;existing  
outline&#160;graphics&#160;method&#160;name&#160;is&#160;given,&#160;then&#160;the&#160;default&#160;outline&#160;graphics  
method&#160;will&#160;be&#160;used&#160;as&#160;the&#160;graphics&#160;method&#160;to&#160;which&#160;the&#160;attributes&#160;will  
be&#160;copied&#160;from.  
  
If&#160;the&#160;name&#160;provided&#160;already&#160;exists,&#160;then&#160;a&#160;error&#160;will&#160;be&#160;returned.&#160;Graphics  
method&#160;names&#160;must&#160;be&#160;unique.  
  
Example&#160;of&#160;Use:  
  
a=vcs.init()  
a. [ show ](/) ('outline')  
out=a. [ createoutline ](/) ('example1',)  
a. [ show ](/) ('outline')  
out=a. [ createoutline ](/) ('example2','quick')  
a. [ show ](/) ('outline') `

 createprojection  (self, Proj_name  =None  , Proj_name_src  ='default'  ) 
     ` Function:&#160;createprojection&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#&#160;Construct&#160;a&#160;new&#160;projection&#160;method   
  
Description&#160;of&#160;Function:  
Create&#160;a&#160;new&#160;projection&#160;method&#160;given&#160;the&#160;the&#160;name&#160;and&#160;the&#160;existing  
projection&#160;method&#160;to&#160;copy&#160;the&#160;attributes&#160;from.&#160;If&#160;no&#160;existing  
projection&#160;method&#160;name&#160;is&#160;given,&#160;then&#160;the&#160;default&#160;projection  
method&#160;will&#160;be&#160;used&#160;as&#160;the&#160;projection&#160;method&#160;to&#160;which&#160;the&#160;attributes&#160;will  
be&#160;copied&#160;from.  
  
If&#160;the&#160;name&#160;provided&#160;already&#160;exists,&#160;then&#160;a&#160;error&#160;will&#160;be&#160;returned.&#160;Projection  
method&#160;names&#160;must&#160;be&#160;unique.  
  
Example&#160;of&#160;Use:  
a=vcs.init()  
a. [ show ](/) ('projection')  
p=a. [ createprojection ](/) ('example1',)  
a. [ show ](/) ('projection')  
box=a. [ createprojection ](/) ('example2','quick')  
a. [ show ](/) ('projection') `

 createscatter  (self, GSp_name  =None  , GSp_name_src  ='default'  ) 
     ` Function:&#160;createscatter&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#&#160;Construct&#160;a&#160;new&#160;scatter&#160;graphics&#160;method   
  
Description&#160;of&#160;Function:  
Create&#160;a&#160;new&#160;scatter&#160;graphics&#160;method&#160;given&#160;the&#160;the&#160;name&#160;and&#160;the&#160;existing  
scatter&#160;graphics&#160;method&#160;to&#160;copy&#160;the&#160;attributes&#160;from.&#160;If&#160;no&#160;existing  
scatter&#160;graphics&#160;method&#160;name&#160;is&#160;given,&#160;then&#160;the&#160;default&#160;scatter&#160;graphics  
method&#160;will&#160;be&#160;used&#160;as&#160;the&#160;graphics&#160;method&#160;to&#160;which&#160;the&#160;attributes&#160;will  
be&#160;copied&#160;from.  
  
If&#160;the&#160;name&#160;provided&#160;already&#160;exists,&#160;then&#160;a&#160;error&#160;will&#160;be&#160;returned.&#160;Graphics  
method&#160;names&#160;must&#160;be&#160;unique.  
  
Example&#160;of&#160;Use:  
a=vcs.init()  
a. [ show ](/) ('scatter')  
sct=a. [ createscatter ](/) ('example1',)  
a. [ show ](/) ('scatter')  
sct=a. [ createscatter ](/) ('example2','quick')  
a. [ show ](/) ('scatter') `

 createtaylordiagram  (self, Gtd_name  =None  , Gtd_name_src  ='default'  ) 
     ` Function:&#160;createtaylordiagram&#160;&#160;#&#160;Construct&#160;a&#160;new&#160;taylordiagram&#160;graphics&#160;method   
  
Description&#160;of&#160;Function:  
Create&#160;a&#160;new&#160;taylordiagram&#160;graphics&#160;method&#160;given&#160;the&#160;the&#160;name&#160;and&#160;the&#160;existing  
taylordiagram&#160;graphics&#160;method&#160;to&#160;copy&#160;the&#160;attributes&#160;from.&#160;If&#160;no&#160;existing  
taylordiagram&#160;graphics&#160;method&#160;name&#160;is&#160;given,&#160;then&#160;the&#160;default&#160;taylordiagram
graphics  
method&#160;will&#160;be&#160;used&#160;as&#160;the&#160;graphics&#160;method&#160;to&#160;which&#160;the&#160;attributes&#160;will  
be&#160;copied&#160;from.  
  
If&#160;the&#160;name&#160;provided&#160;already&#160;exists,&#160;then&#160;a&#160;error&#160;will&#160;be&#160;returned.&#160;Graphics  
method&#160;names&#160;must&#160;be&#160;unique.  
  
Example&#160;of&#160;Use:  
a=vcs.init()  
a. [ show ](/) ('taylordiagram')  
td=a. [ createtaylordiagram ](/) ('example1',)  
a. [ show ](/) ('taylordiagram')  
td=a. [ createtaylordiagram ](/) ('example2','quick')  
a. [ show ](/) ('taylordiagram') `

 createtemplate  (self, P_name  =None  , P_name_src  ='default'  ) 
     ` Function:&#160;createtemplate&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#&#160;Construct&#160;a&#160;new&#160;template   
  
Description&#160;of&#160;Function:  
Create&#160;a&#160;new&#160;template&#160;given&#160;the&#160;the&#160;name&#160;and&#160;the&#160;existing&#160;template&#160;to&#160;copy  
the&#160;attributes&#160;from.&#160;If&#160;no&#160;existing&#160;template&#160;name&#160;is&#160;given,&#160;then&#160;the&#160;default  
template&#160;will&#160;be&#160;used&#160;as&#160;the&#160;template&#160;to&#160;which&#160;the&#160;attributes&#160;will&#160;be&#160;copied  
from.  
  
If&#160;the&#160;name&#160;provided&#160;already&#160;exists,&#160;then&#160;a&#160;error&#160;will&#160;be&#160;returned.&#160;Template  
names&#160;must&#160;be&#160;unique.  
  
Example&#160;of&#160;Use:  
a=vcs.init()  
a. [ show ](/) ('template')&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#&#160;Show&#160;all&#160;the&#160;existing
templates  
con=a. [ createtemplate ](/) ('example1')&#160;#&#160;create&#160;'example1'&#160;template&#160;from
'default'&#160;template  
a. [ show ](/) ('template')&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#&#160;Show&#160;all&#160;the&#160;existing
templates  
con=a. [ createtemplate ](/) ('example2','quick')&#160;#&#160;create&#160;'example2'&#160;from
'quick'&#160;template  
a. [ listelements ](/) ('template')&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#&#160;Show&#160;all&#160;the&#160;templates&#160;as
a&#160;Python&#160;list `

 createtext  = [ createtextcombined ](/) (self, Tt_name  =None  , Tt_name_src  ='default'  , To_name  =None  , To_name_src  ='default'  , font  =None  , spacing  =None  , expansion  =None  , color  =None  , priority  =1  , viewport  =None  , worldcoordinate  =None  , x  =None  , y  =None  , height  =None  , angle  =None  , path  =None  , halign  =None  , valign  =None  , projection  =None  ) 

 createtextcombined  (self, Tt_name  =None  , Tt_name_src  ='default'  , To_name  =None  , To_name_src  ='default'  , font  =None  , spacing  =None  , expansion  =None  , color  =None  , priority  =1  , viewport  =None  , worldcoordinate  =None  , x  =None  , y  =None  , height  =None  , angle  =None  , path  =None  , halign  =None  , valign  =None  , projection  =None  ) 
     ` Function:&#160;createtext&#160;or&#160;createtextcombined&#160;&#160;#&#160;Construct&#160;a&#160;new&#160;text&#160;combined&#160;secondary&#160;method   
  
Description&#160;of&#160;Function:  
Create&#160;a&#160;new&#160;textcombined&#160;secondary&#160;method&#160;given&#160;the&#160;the&#160;names&#160;and  
the&#160;existing&#160;texttable&#160;and&#160;textorientation&#160;secondary&#160;methods&#160;to&#160;copy  
the&#160;attributes&#160;from.&#160;If&#160;no&#160;existing&#160;texttable&#160;and&#160;textorientation  
secondary&#160;method&#160;names&#160;are&#160;given,&#160;then&#160;the&#160;default&#160;texttable&#160;and  
textorientation&#160;secondary&#160;methods&#160;will&#160;be&#160;used&#160;as&#160;the&#160;secondary&#160;method  
to&#160;which&#160;the&#160;attributes&#160;will&#160;be&#160;copied&#160;from.  
  
If&#160;the&#160;name&#160;provided&#160;already&#160;exists,&#160;then&#160;a&#160;error&#160;will&#160;be&#160;returned.  
Secondary&#160;method&#160;names&#160;must&#160;be&#160;unique.  
  
Example&#160;of&#160;Use:  
a=vcs.init()  
a. [ show ](/) ('texttable')  
a. [ show ](/) ('textorientation')  
tc=a. [ createtextcombined ](/) ('example1','std','example1','7left')  
a. [ show ](/) ('texttable')  
a. [ show ](/) ('textorientation') `

 createtextorientation  (self, To_name  =None  , To_name_src  ='default'  ) 
     ` Function:&#160;createtextorientation&#160;&#160;&#160;#&#160;Construct&#160;a&#160;new&#160;textorientation&#160;secondary&#160;method   
  
Description&#160;of&#160;Function:  
Create&#160;a&#160;new&#160;textorientation&#160;secondary&#160;method&#160;given&#160;the&#160;the&#160;name&#160;and  
the&#160;existing&#160;textorientation&#160;secondary&#160;method&#160;to&#160;copy&#160;the&#160;attributes  
from.&#160;If&#160;no&#160;existing&#160;textorientation&#160;secondary&#160;method&#160;name&#160;is&#160;given,  
then&#160;the&#160;default&#160;textorientation&#160;secondary&#160;method&#160;will&#160;be&#160;used&#160;as&#160;the  
secondary&#160;method&#160;to&#160;which&#160;the&#160;attributes&#160;will&#160;be&#160;copied&#160;from.  
  
If&#160;the&#160;name&#160;provided&#160;already&#160;exists,&#160;then&#160;a&#160;error&#160;will&#160;be&#160;returned.  
Secondary&#160;method&#160;names&#160;must&#160;be&#160;unique.  
  
Example&#160;of&#160;Use:  
a=vcs.init()  
a. [ show ](/) ('textorientation')  
to=a. [ createtextorientation ](/) ('example1',)  
a. [ show ](/) ('textorientation')  
to=a. [ createtextorientation ](/) ('example2','black')  
a. [ show ](/) ('textorientation') `

 createtexttable  (self, name  =None  , name_src  ='default'  , font  =None  , spacing  =None  , expansion  =None  , color  =None  , priority  =1  , viewport  =None  , worldcoordinate  =None  , x  =None  , y  =None  ) 
     ` Function:&#160;createtexttable&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#&#160;Construct&#160;a&#160;new&#160;texttable&#160;secondary&#160;method   
  
Description&#160;of&#160;Function:  
Create&#160;a&#160;new&#160;texttable&#160;secondary&#160;method&#160;given&#160;the&#160;the&#160;name&#160;and&#160;the&#160;existing  
texttable&#160;secondary&#160;method&#160;to&#160;copy&#160;the&#160;attributes&#160;from.&#160;If&#160;no&#160;existing
texttable  
secondary&#160;method&#160;name&#160;is&#160;given,&#160;then&#160;the&#160;default&#160;texttable&#160;secondary&#160;method  
will&#160;be&#160;used&#160;as&#160;the&#160;secondary&#160;method&#160;to&#160;which&#160;the&#160;attributes&#160;will&#160;be  
copied&#160;from.  
  
If&#160;the&#160;name&#160;provided&#160;already&#160;exists,&#160;then&#160;a&#160;error&#160;will&#160;be&#160;returned.  
Secondary&#160;method&#160;names&#160;must&#160;be&#160;unique.  
  
Example&#160;of&#160;Use:  
a=vcs.init()  
a. [ show ](/) ('texttable')  
tt=a. [ createtexttable ](/) ('example1',)  
a. [ show ](/) ('texttable')  
tt=a. [ createtexttable ](/) ('example2','black')  
a. [ show ](/) ('texttable')  
tt=a. [ createtexttable ](/)
(name='new',name_src='red',font=1,spacing=1,expansion=1,  
color=242,&#160;priority=1,&#160;viewport=[0,&#160;2.0,&#160;0,&#160;2.0],  
worldcoordinate=[0,100,&#160;0,50]  
x=[0,20,40,60,80,100],  
y=[0,10,20,30,40,50]&#160;)&#160;&#160;&#160;&#160;&#160;&#160;#&#160;Create&#160;instance&#160;of&#160;texttable&#160;object&#160;'new'  
a.texttable(tt)&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#&#160;Plot&#160;using&#160;specified&#160;texttable&#160;object `

 createvector  (self, Gv_name  =None  , Gv_name_src  ='default'  ) 
     ` Function:&#160;createvector&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#&#160;Construct&#160;a&#160;new&#160;vector&#160;graphics&#160;method   
  
Description&#160;of&#160;Function:  
Create&#160;a&#160;new&#160;vector&#160;graphics&#160;method&#160;given&#160;the&#160;the&#160;name&#160;and&#160;the&#160;existing  
vector&#160;graphics&#160;method&#160;to&#160;copy&#160;the&#160;attributes&#160;from.&#160;If&#160;no&#160;existing  
vector&#160;graphics&#160;method&#160;name&#160;is&#160;given,&#160;then&#160;the&#160;default&#160;vector&#160;graphics  
method&#160;will&#160;be&#160;used&#160;as&#160;the&#160;graphics&#160;method&#160;to&#160;which&#160;the&#160;attributes&#160;will  
be&#160;copied&#160;from.  
  
If&#160;the&#160;name&#160;provided&#160;already&#160;exists,&#160;then&#160;a&#160;error&#160;will&#160;be&#160;returned.&#160;Graphics  
method&#160;names&#160;must&#160;be&#160;unique.  
  
Example&#160;of&#160;Use:  
a=vcs.init()  
a. [ show ](/) ('vector')  
vec=a. [ createvector ](/) ('example1',)  
a. [ show ](/) ('vector')  
vec=a. [ createvector ](/) ('example2','quick')  
a. [ show ](/) ('vector') `

 createxvsy  (self, GXY_name  =None  , GXY_name_src  ='default'  ) 
     ` Function:&#160;createxvsy&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#&#160;Construct&#160;a&#160;new&#160;XvsY&#160;graphics&#160;method   
  
Description&#160;of&#160;Function:  
Create&#160;a&#160;new&#160;XvsY&#160;graphics&#160;method&#160;given&#160;the&#160;the&#160;name&#160;and&#160;the&#160;existing  
XvsY&#160;graphics&#160;method&#160;to&#160;copy&#160;the&#160;attributes&#160;from.&#160;If&#160;no&#160;existing  
XvsY&#160;graphics&#160;method&#160;name&#160;is&#160;given,&#160;then&#160;the&#160;default&#160;XvsY&#160;graphics  
method&#160;will&#160;be&#160;used&#160;as&#160;the&#160;graphics&#160;method&#160;to&#160;which&#160;the&#160;attributes&#160;will  
be&#160;copied&#160;from.  
  
If&#160;the&#160;name&#160;provided&#160;already&#160;exists,&#160;then&#160;a&#160;error&#160;will&#160;be&#160;returned.&#160;Graphics  
method&#160;names&#160;must&#160;be&#160;unique.  
  
Example&#160;of&#160;Use:  
a=vcs.init()  
a. [ show ](/) ('xvsy')  
xy=a. [ createxvsy ](/) ('example1',)  
a. [ show ](/) ('xvsy')  
xy=a. [ createxvsy ](/) ('example2','quick')  
a. [ show ](/) ('xvsy') `

 createxyvsy  (self, GXy_name  =None  , GXy_name_src  ='default'  ) 
     ` Function:&#160;createxyvsy&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#&#160;Construct&#160;a&#160;new&#160;Xyvsy&#160;graphics&#160;method   
  
Description&#160;of&#160;Function:  
Create&#160;a&#160;new&#160;Xyvsy&#160;graphics&#160;method&#160;given&#160;the&#160;the&#160;name&#160;and&#160;the&#160;existing  
Xyvsy&#160;graphics&#160;method&#160;to&#160;copy&#160;the&#160;attributes&#160;from.&#160;If&#160;no&#160;existing  
Xyvsy&#160;graphics&#160;method&#160;name&#160;is&#160;given,&#160;then&#160;the&#160;default&#160;Xyvsy&#160;graphics  
method&#160;will&#160;be&#160;used&#160;as&#160;the&#160;graphics&#160;method&#160;to&#160;which&#160;the&#160;attributes&#160;will  
be&#160;copied&#160;from.  
  
If&#160;the&#160;name&#160;provided&#160;already&#160;exists,&#160;then&#160;a&#160;error&#160;will&#160;be&#160;returned.&#160;Graphics  
method&#160;names&#160;must&#160;be&#160;unique.  
  
Example&#160;of&#160;Use:  
  
a=vcs.init()  
a. [ show ](/) ('xyvsy')  
xyy=a. [ createxyvsy ](/) ('example1',)  
a. [ show ](/) ('xyvsy')  
xyy=a. [ createxyvsy ](/) ('example2','quick')  
a. [ show ](/) ('xyvsy') `

 createyxvsx  (self, GYx_name  =None  , GYx_name_src  ='default'  ) 
     ` Function:&#160;createyxvsx&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#&#160;Construct&#160;a&#160;new&#160;Yxvsx&#160;graphics&#160;method   
  
Description&#160;of&#160;Function:  
Create&#160;a&#160;new&#160;Yxvsx&#160;graphics&#160;method&#160;given&#160;the&#160;the&#160;name&#160;and&#160;the&#160;existing  
Yxvsx&#160;graphics&#160;method&#160;to&#160;copy&#160;the&#160;attributes&#160;from.&#160;If&#160;no&#160;existing  
Yxvsx&#160;graphics&#160;method&#160;name&#160;is&#160;given,&#160;then&#160;the&#160;default&#160;Yxvsx&#160;graphics  
method&#160;will&#160;be&#160;used&#160;as&#160;the&#160;graphics&#160;method&#160;to&#160;which&#160;the&#160;attributes&#160;will  
be&#160;copied&#160;from.  
  
If&#160;the&#160;name&#160;provided&#160;already&#160;exists,&#160;then&#160;a&#160;error&#160;will&#160;be&#160;returned.&#160;Graphics  
method&#160;names&#160;must&#160;be&#160;unique.  
  
Example&#160;of&#160;Use:  
  
a=vcs.init()  
a. [ show ](/) ('yxvsx')  
yxx=a. [ createyxvsx ](/) ('example1',)  
a. [ show ](/) ('yxvsx')  
yxx=a. [ createyxvsx ](/) ('example2','quick')  
a. [ show ](/) ('yxvsx') `

 destroy  (self) 
     ` Function:&#160;destroy   
  
Description&#160;of&#160;Function:  
Destroy&#160;the&#160;VCS [ Canvas ](/) .&#160;It&#160;will&#160;deallocate&#160;the&#160;VCS [ Canvas ](/)
object.  
  
Example&#160;of&#160;Use:  
a=vcs.init()  
a. [ plot ](/) (array,'default','isofill','quick')  
a.destory() `

 drawfillarea  (self, name  =None  , style  =1  , index  =1  , color  =241  , priority  =1  , viewport  =[0.0, 1.0, 0.0, 1.0]  , worldcoordinate  =[0.0, 1.0, 0.0, 1.0]  , x  =None  , y  =None  ) 
     ` Function:&#160;drawfillarea&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#&#160;Generate&#160;and&#160;draw&#160;a&#160;fillarea&#160;plot   
  
Description&#160;of&#160;Function:  
Generate&#160;and&#160;draw&#160;a&#160;fillarea&#160;object&#160;on&#160;the&#160;VCS [ Canvas ](/) .  
  
Example&#160;of&#160;Use:  
a=vcs.init()  
a. [ show ](/) ('fillarea')&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#&#160;Show&#160;all&#160;the&#160;existing
fillarea&#160;objects  
fa=a. [ drawfillarea ](/) (name='red',&#160;mtype='dash',&#160;size=2,  
color=242,&#160;priority=1,&#160;viewport=[0,&#160;2.0,&#160;0,&#160;2.0],  
worldcoordinate=[0,100,&#160;0,50]  
x=[0,20,40,60,80,100],  
y=[0,10,20,30,40,50]&#160;)&#160;&#160;&#160;&#160;&#160;&#160;#&#160;Create&#160;instance&#160;of&#160;fillarea&#160;object&#160;'red'  
a. [ fillarea ](/) (fa)&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#&#160;Plot&#160;using&#160;specified
fillarea&#160;object `

 drawline  (self, name  =None  , ltype  ='solid'  , width  =1  , color  =241  , priority  =1  , viewport  =[0.0, 1.0, 0.0, 1.0]  , worldcoordinate  =[0.0, 1.0, 0.0, 1.0]  , x  =None  , y  =None  , projection  ='default'  ) 
     ` Function:&#160;drawline&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#&#160;Generate&#160;and&#160;draw&#160;a&#160;line&#160;plot   
  
Description&#160;of&#160;Function:  
Generate&#160;and&#160;draw&#160;a&#160;line&#160;object&#160;on&#160;the&#160;VCS [ Canvas ](/) .  
  
Example&#160;of&#160;Use:  
a=vcs.init()  
a. [ show ](/) ('line')&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#&#160;Show&#160;all&#160;the&#160;existing&#160;line
objects  
ln=a. [ drawline ](/) (name='red',&#160;ltype='dash',&#160;width=2,  
color=242,&#160;priority=1,&#160;viewport=[0,&#160;2.0,&#160;0,&#160;2.0],  
worldcoordinate=[0,100,&#160;0,50]  
x=[0,20,40,60,80,100],  
y=[0,10,20,30,40,50]&#160;)&#160;&#160;&#160;&#160;&#160;&#160;#&#160;Create&#160;instance&#160;of&#160;line&#160;object&#160;'red'  
a. [ line ](/) (ln)&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#&#160;Plot&#160;using&#160;specified&#160;line
object `

 drawmarker  (self, name  =None  , mtype  ='solid'  , size  =1  , color  =241  , priority  =1  , viewport  =[0.0, 1.0, 0.0, 1.0]  , worldcoordinate  =[0.0, 1.0, 0.0, 1.0]  , x  =None  , y  =None  ) 
     ` Function:&#160;drawmarker&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#&#160;Generate&#160;and&#160;draw&#160;a&#160;marker&#160;plot   
  
Description&#160;of&#160;Function:  
Generate&#160;and&#160;draw&#160;a&#160;marker&#160;object&#160;on&#160;the&#160;VCS [ Canvas ](/) .  
  
Example&#160;of&#160;Use:  
a=vcs.init()  
a. [ show ](/) ('marker')&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#&#160;Show&#160;all&#160;the&#160;existing&#160;marker
objects  
mrk=a. [ drawmarker ](/) (name='red',&#160;mtype='dash',&#160;size=2,  
color=242,&#160;priority=1,&#160;viewport=[0,&#160;2.0,&#160;0,&#160;2.0],  
worldcoordinate=[0,100,&#160;0,50]  
x=[0,20,40,60,80,100],  
y=[0,10,20,30,40,50]&#160;)&#160;&#160;&#160;&#160;&#160;&#160;#&#160;Create&#160;instance&#160;of&#160;marker&#160;object&#160;'red'  
a. [ marker ](/) (mrk)&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#&#160;Plot&#160;using&#160;specified&#160;marker
object `

 drawtext  = [ drawtextcombined ](/) (self, Tt_name  =None  , To_name  =None  , string  =None  , font  =1  , spacing  =2  , expansion  =100  , color  =241  , height  =14  , angle  =0  , path  ='right'  , halign  ='left'  , valign  ='half'  , priority  =1  , viewport  =[0.0, 1.0, 0.0, 1.0]  , worldcoordinate  =[0.0, 1.0, 0.0, 1.0]  , x  =None  , y  =None  ) 

 drawtextcombined  (self, Tt_name  =None  , To_name  =None  , string  =None  , font  =1  , spacing  =2  , expansion  =100  , color  =241  , height  =14  , angle  =0  , path  ='right'  , halign  ='left'  , valign  ='half'  , priority  =1  , viewport  =[0.0, 1.0, 0.0, 1.0]  , worldcoordinate  =[0.0, 1.0, 0.0, 1.0]  , x  =None  , y  =None  ) 
     ` Function:&#160;drawtexttable&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#&#160;Generate&#160;and&#160;draw&#160;a&#160;texttable&#160;plot   
  
Description&#160;of&#160;Function:  
Generate&#160;and&#160;draw&#160;a&#160;texttable&#160;object&#160;on&#160;the&#160;VCS [ Canvas ](/) .  
  
Example&#160;of&#160;Use:  
a=vcs.init()  
a. [ show ](/) ('texttable')&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#&#160;Show&#160;all&#160;the&#160;existing
texttable&#160;objects  
tt=a.drawtexttable(Tt_name&#160;=&#160;'red',&#160;To_name='7left',&#160;mtype='dash',&#160;size=2,  
color=242,&#160;priority=1,&#160;viewport=[0,&#160;2.0,&#160;0,&#160;2.0],  
worldcoordinate=[0,100,&#160;0,50]  
x=[0,20,40,60,80,100],  
y=[0,10,20,30,40,50]&#160;)&#160;&#160;&#160;&#160;&#160;&#160;#&#160;Create&#160;instance&#160;of&#160;texttable&#160;object&#160;'red'  
a.texttable(tt)&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#&#160;Plot&#160;using&#160;specified&#160;texttable
object `

 eps  (self, *args) 
     ` Function:&#160;Encapsulated&#160;PostScript   
  
Description&#160;of&#160;Function:  
In&#160;some&#160;cases,&#160;the&#160;user&#160;may&#160;want&#160;to&#160;save&#160;the&#160;plot&#160;out&#160;as&#160;an&#160;Encapsulated  
PostScript&#160;image.&#160;This&#160;routine&#160;allows&#160;the&#160;user&#160;to&#160;save&#160;the&#160;VCS&#160;canvas&#160;output  
as&#160;an&#160;Encapsulated&#160;PostScript&#160;file.  
This&#160;file&#160;can&#160;be&#160;converted&#160;to&#160;other&#160;image&#160;formats&#160;with&#160;the&#160;aid&#160;of&#160;xv&#160;and&#160;other  
such&#160;imaging&#160;tools&#160;found&#160;freely&#160;on&#160;the&#160;web.  
  
If&#160;no&#160;path/file&#160;name&#160;is&#160;given&#160;and&#160;no&#160;previously&#160;created&#160;gif&#160;file&#160;has&#160;been  
designated,&#160;then&#160;file  
  
/$HOME/PCMDI_GRAPHICS/default.eps  
  
will&#160;be&#160;used&#160;for&#160;storing&#160;gif&#160;images.&#160;However,&#160;if&#160;a&#160;previously&#160;created&#160;gif  
file&#160;is&#160;designated,&#160;that&#160;file&#160;will&#160;be&#160;used&#160;for&#160;gif&#160;output.  
  
By&#160;default,&#160;the&#160;page&#160;orientation&#160;is&#160;in&#160;Landscape&#160;mode&#160;(l).&#160;To&#160;translate&#160;the
page  
orientation&#160;to&#160;portrait&#160;mode&#160;(p),&#160;enter&#160;'p'&#160;as&#160;the&#160;second&#160;parameter.  
  
The&#160;eps&#160;command&#160;is&#160;used&#160;to&#160;create&#160;or&#160;append&#160;to&#160;a&#160;gif&#160;file.&#160;There&#160;are&#160;two&#160;modes  
for&#160;saving&#160;a&#160;eps&#160;file:&#160;`Append'&#160;mode&#160;(a)&#160;appends&#160;gif&#160;output&#160;to&#160;an&#160;existing&#160;eps  
file;&#160;`Replace'&#160;(r)&#160;mode&#160;overwrites&#160;an&#160;existing&#160;eps&#160;file&#160;with&#160;new&#160;eps&#160;output.  
The&#160;default&#160;mode&#160;is&#160;to&#160;overwrite&#160;an&#160;existing&#160;eps&#160;file&#160;(i.e.&#160;mode&#160;(r)).  
  
Example&#160;of&#160;Use:  
a=vcs.init()  
a. [ plot ](/) (array)  
a. [ eps ](/) ('example')&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#&#160;overwrite&#160;an&#160;existing&#160;eps&#160;file  
a. [ eps ](/) ('example',&#160;'a')&#160;&#160;&#160;&#160;#&#160;append&#160;to&#160;an&#160;existing&#160;eps&#160;file  
a. [ eps ](/) ('example','r')&#160;&#160;&#160;&#160;&#160;#&#160;overwrite&#160;existing&#160;eps&#160;file  
a. [ eps ](/) ('example','r','p')&#160;#&#160;overwrite&#160;eps&#160;image&#160;file&#160;with&#160;new&#160;portrait
orientation&#160;eps `

 fillarea  (self, *args, parms) 
     ` Function:&#160;fillarea&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#&#160;Generate&#160;a&#160;fillarea&#160;plot   
  
Description&#160;of&#160;Function:  
Plot&#160;a&#160;fillarea&#160;segment&#160;on&#160;the&#160;Vcs [ Canvas ](/) .&#160;If&#160;no&#160;fillarea&#160;class  
object&#160;is&#160;given,&#160;then&#160;an&#160;error&#160;will&#160;be&#160;returned.  
  
Example&#160;of&#160;Use:  
a=vcs.init()  
a. [ show ](/) ('fillarea')&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#&#160;Show&#160;all&#160;the&#160;existing&#160;fillarea
objects  
fa=a. [ getfillarea ](/) ('red')&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#&#160;Create&#160;instance&#160;of&#160;'red'  
fa.style=1&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#&#160;Set&#160;the&#160;fillarea&#160;style  
fa.index=4&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#&#160;Set&#160;the&#160;fillarea&#160;index  
fa.color&#160;=&#160;242&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#&#160;Set&#160;the&#160;fillarea&#160;color  
fa.type&#160;=&#160;4&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#&#160;Set&#160;the&#160;fillarea&#160;type  
fa.x=[[0.0,2.0,2.0,0.0,0.0],&#160;[0.5,1.5]]&#160;#&#160;Set&#160;the&#160;x&#160;value&#160;points  
fa.y=[[0.0,0.0,2.0,2.0,0.0],&#160;[1.0,1.0]]&#160;#&#160;Set&#160;the&#160;y&#160;value&#160;points  
a. [ fillarea ](/) (fa)&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#&#160;Plot&#160;using&#160;specified
fillarea&#160;object `

 flush  (self, *args) 
     ` Function:&#160;flush   
  
Description&#160;of&#160;Function:  
The&#160;flush&#160;command&#160;executes&#160;all&#160;buffered&#160;X&#160;events&#160;in&#160;the&#160;que.  
  
Example&#160;of&#160;Use:  
a=vcs.init()  
a. [ plot ](/) (array,'default','isofill','quick')  
a. [ flush ](/) () `

 generate_gm  (self, type, name) 

 geometry  (self, *args) 
     ` Function:&#160;geometry   
  
Description&#160;of&#160;Function:  
The&#160;geometry&#160;command&#160;is&#160;used&#160;to&#160;set&#160;the&#160;size&#160;and&#160;position&#160;of&#160;the&#160;VCS&#160;canvas.  
  
Example&#160;of&#160;Use:  
a=vcs.init()  
a. [ plot ](/) (array,'default','isofill','quick')  
a. [ geometry ](/) (450,337) `

 get_gm  (self, type, name) 

 getboxfill  (self, Gfb_name_src  ='default'  ) 
     ` Function:&#160;getboxfill&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#&#160;Construct&#160;a&#160;new&#160;boxfill&#160;graphics&#160;method   
  
Description&#160;of&#160;Function:  
VCS&#160;contains&#160;a&#160;list&#160;of&#160;graphics&#160;methods.&#160;This&#160;function&#160;will&#160;create&#160;a  
boxfill&#160;class&#160;object&#160;from&#160;an&#160;existing&#160;VCS&#160;boxfill&#160;graphics&#160;method.&#160;If  
no&#160;boxfill&#160;name&#160;is&#160;given,&#160;then&#160;boxfill&#160;'default'&#160;will&#160;be&#160;used.  
  
Note,&#160;VCS&#160;does&#160;not&#160;allow&#160;the&#160;modification&#160;of&#160;`default'&#160;attribute  
sets.&#160;However,&#160;a&#160;`default'&#160;attribute&#160;set&#160;that&#160;has&#160;been&#160;copied&#160;under&#160;a  
different&#160;name&#160;can&#160;be&#160;modified.&#160;(See&#160;the&#160;createboxfill&#160;function.)  
  
Example&#160;of&#160;Use:  
a=vcs.init()  
a. [ show ](/) ('boxfill')&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#&#160;Show&#160;all&#160;the&#160;existing&#160;boxfill
graphics&#160;methods  
box=a. [ getboxfill ](/) ()&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#&#160;box&#160;instance&#160;of&#160;'default'
boxfill&#160;graphics  
#&#160;method  
box2=a. [ getboxfill ](/) ('quick')&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#&#160;box2&#160;instance&#160;of&#160;existing
'quick'&#160;boxfill  
#&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;graphics&#160;method `

 getcolorcell  (self, *args) 
     ` Function:&#160;getcolorcell   
  
Description&#160;of&#160;Function:  
Get&#160;an&#160;individual&#160;color&#160;cell&#160;in&#160;the&#160;active&#160;colormap.&#160;If&#160;default&#160;is  
the&#160;active&#160;colormap,&#160;then&#160;return&#160;an&#160;error&#160;string.  
  
If&#160;the&#160;the&#160;visul&#160;display&#160;is&#160;16-bit,&#160;24-bit,&#160;or&#160;32-bit&#160;TrueColor,&#160;then&#160;a
redrawing  
of&#160;the&#160;VCS [ Canvas ](/) is&#160;made&#160;evertime&#160;the&#160;color&#160;cell&#160;is&#160;changed.  
  
Note,&#160;the&#160;user&#160;can&#160;only&#160;change&#160;color&#160;cells&#160;0&#160;through&#160;239&#160;and&#160;R,G,B  
value&#160;must&#160;range&#160;from&#160;0&#160;to&#160;100.&#160;Where&#160;0&#160;represents&#160;no&#160;color&#160;intensity  
and&#160;100&#160;is&#160;the&#160;greatest&#160;color&#160;intensity.  
  
Example&#160;of&#160;Use:  
a=vcs.init()  
a. [ plot ](/) (array,'default','isofill','quick')  
a. [ setcolormap ](/) ("AMIP")  
a. [ getcolorcell ](/) (11,0,0,0)  
a. [ getcolorcell ](/) (21,100,0,0)  
a. [ getcolorcell ](/) (31,0,100,0)  
a. [ getcolorcell ](/) (41,0,0,100)  
a. [ getcolorcell ](/) (51,100,100,100)  
a. [ getcolorcell ](/) (61,70,70,70) `

 getcolormap  (self, Cp_name_src  ='default'  ) 
     ` Function:&#160;getcolormap&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#&#160;Construct&#160;a&#160;new&#160;colormap&#160;secondary&#160;method   
  
Description&#160;of&#160;Function:  
VCS&#160;contains&#160;a&#160;list&#160;of&#160;secondary&#160;methods.&#160;This&#160;function&#160;will&#160;create&#160;a  
colormap&#160;class&#160;object&#160;from&#160;an&#160;existing&#160;VCS&#160;colormap&#160;secondary&#160;method.&#160;If  
no&#160;colormap&#160;name&#160;is&#160;given,&#160;then&#160;colormap&#160;'default'&#160;will&#160;be&#160;used.  
  
Note,&#160;VCS&#160;does&#160;not&#160;allow&#160;the&#160;modification&#160;of&#160;`default'&#160;attribute&#160;sets.  
However,&#160;a&#160;`default'&#160;attribute&#160;set&#160;that&#160;has&#160;been&#160;copied&#160;under&#160;a  
different&#160;name&#160;can&#160;be&#160;modified.&#160;(See&#160;the&#160;createcolormap&#160;function.)  
  
Example&#160;of&#160;Use:  
a=vcs.init()  
a. [ show ](/) ('colormap')&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#&#160;Show&#160;all&#160;the&#160;existing
colormap&#160;secondary&#160;methods  
cp=a. [ getcolormap ](/) ()&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#&#160;cp&#160;instance&#160;of&#160;'default'
colormap&#160;secondary  
#&#160;&#160;&#160;&#160;&#160;&#160;&#160;method  
cp2=a. [ getcolormap ](/) ('quick')&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#&#160;cp2&#160;instance&#160;of&#160;existing
'quick'&#160;colormap  
#&#160;&#160;&#160;&#160;&#160;&#160;&#160;secondary&#160;method `

 getcolormapname  (self, *args) 
     ` Function:&#160;getcolormapcell   
  
Description&#160;of&#160;Function:  
Get&#160;colormap&#160;name&#160;of&#160;the&#160;active&#160;colormap.  
  
  
Example&#160;of&#160;Use:  
a=vcs.init()  
a. [ plot ](/) (array,'default','isofill','quick')  
a. [ getcolormapname ](/) () `

 getcontinents  (self, Gcon_name_src  ='default'  ) 
     ` Function:&#160;getcontinents&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#&#160;Construct&#160;a&#160;new&#160;continents&#160;graphics&#160;method   
  
Description&#160;of&#160;Function:  
VCS&#160;contains&#160;a&#160;list&#160;of&#160;graphics&#160;methods.&#160;This&#160;function&#160;will&#160;create&#160;a  
continents&#160;class&#160;object&#160;from&#160;an&#160;existing&#160;VCS&#160;continents&#160;graphics&#160;method.&#160;If  
no&#160;continents&#160;name&#160;is&#160;given,&#160;then&#160;continents&#160;'default'&#160;will&#160;be&#160;used.  
  
Note,&#160;VCS&#160;does&#160;not&#160;allow&#160;the&#160;modification&#160;of&#160;`default'&#160;attribute  
sets.&#160;However,&#160;a&#160;`default'&#160;attribute&#160;set&#160;that&#160;has&#160;been&#160;copied&#160;under&#160;a  
different&#160;name&#160;can&#160;be&#160;modified.&#160;(See&#160;the&#160;createcontinents&#160;function.)  
  
Example&#160;of&#160;Use:  
a=vcs.init()  
a. [ show ](/) ('continents')&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#&#160;Show&#160;all&#160;the&#160;existing&#160;continents
graphics  
#&#160;methods  
con=a. [ getcontinents ](/) ()&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#&#160;con&#160;instance&#160;of&#160;'default'
continents&#160;graphics  
#&#160;&#160;&#160;&#160;&#160;&#160;&#160;method  
con2=a. [ getcontinents ](/) ('quick')&#160;&#160;&#160;&#160;&#160;&#160;&#160;#&#160;con2&#160;instance&#160;of&#160;existing
'quick'&#160;continents  
#&#160;&#160;&#160;&#160;&#160;&#160;&#160;graphics&#160;method `

 getcontinentstype  (self, *args) 
     ` Function:&#160;getcontinentstype   
  
Description&#160;of&#160;Function:  
Retrieve&#160;continents&#160;type&#160;from&#160;VCS.&#160;Remember&#160;the&#160;value&#160;can&#160;only&#160;be&#160;between  
0&#160;and&#160;11\.  
  
Example&#160;of&#160;Use:  
a=vcs.init()  
cont_type&#160;=&#160;a. [ getcontinentstype ](/) ()&#160;#&#160;Get&#160;the&#160;continents&#160;type `

 getfillarea  (self, name  ='default'  , style  =None  , index  =None  , color  =None  , priority  =None  , viewport  =None  , worldcoordinate  =None  , x  =None  , y  =None  ) 
     ` Function:&#160;getfillarea&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#&#160;Construct&#160;a&#160;new&#160;fillarea&#160;secondary&#160;method   
  
Description&#160;of&#160;Function:  
VCS&#160;contains&#160;a&#160;list&#160;of&#160;secondary&#160;methods.&#160;This&#160;function&#160;will&#160;create&#160;a  
fillarea&#160;class&#160;object&#160;from&#160;an&#160;existing&#160;VCS&#160;fillarea&#160;secondary&#160;method.&#160;If  
no&#160;fillarea&#160;name&#160;is&#160;given,&#160;then&#160;fillarea&#160;'default'&#160;will&#160;be&#160;used.  
  
Note,&#160;VCS&#160;does&#160;not&#160;allow&#160;the&#160;modification&#160;of&#160;`default'&#160;attribute&#160;sets.  
However,&#160;a&#160;`default'&#160;attribute&#160;set&#160;that&#160;has&#160;been&#160;copied&#160;under&#160;a  
different&#160;name&#160;can&#160;be&#160;modified.&#160;(See&#160;the&#160;createfillarea&#160;function.)  
  
Example&#160;of&#160;Use:  
a=vcs.init()  
a. [ show ](/) ('fillarea')&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#&#160;Show&#160;all&#160;the&#160;existing&#160;fillarea
secondary&#160;methods  
fa=a. [ getfillarea ](/) ()&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#&#160;fa&#160;instance&#160;of&#160;'default'
fillarea&#160;secondary  
#&#160;&#160;&#160;&#160;&#160;&#160;&#160;method  
fa2=a. [ getfillarea ](/) ('quick')&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#&#160;fa2&#160;instance&#160;of&#160;existing&#160;'quick'
fillarea  
#&#160;&#160;&#160;&#160;&#160;&#160;&#160;secondary&#160;method  
fa3=a. [ createmarker ](/) (name='new',&#160;name='red',style=1,&#160;index=1,  
color=242,&#160;priority=1,&#160;viewport=[0,&#160;2.0,&#160;0,&#160;2.0],  
worldcoordinate=[0,100,&#160;0,50]  
x=[0,20,40,60,80,100],  
y=[0,10,20,30,40,50]&#160;)&#160;&#160;&#160;&#160;&#160;&#160;#&#160;Create&#160;instance&#160;of&#160;fill&#160;area&#160;object&#160;'red'  
a. [ fillarea ](/) (fa3)&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#&#160;Plot&#160;using&#160;specified&#160;fill&#160;area
object `

 getisofill  (self, Gfi_name_src  ='default'  ) 
     ` Function:&#160;getisofill&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;Construct&#160;a&#160;new&#160;isofill&#160;graphics&#160;method   
  
Description&#160;of&#160;Function:  
VCS&#160;contains&#160;a&#160;list&#160;of&#160;graphics&#160;methods.&#160;This&#160;function&#160;will&#160;create&#160;a  
isofill&#160;class&#160;object&#160;from&#160;an&#160;existing&#160;VCS&#160;isofill&#160;graphics&#160;method.&#160;If  
no&#160;isofill&#160;name&#160;is&#160;given,&#160;then&#160;isofill&#160;'default'&#160;will&#160;be&#160;used.  
  
Note,&#160;VCS&#160;does&#160;not&#160;allow&#160;the&#160;modification&#160;of&#160;`default'&#160;attribute  
sets.&#160;However,&#160;a&#160;`default'&#160;attribute&#160;set&#160;that&#160;has&#160;been&#160;copied&#160;under&#160;a  
different&#160;name&#160;can&#160;be&#160;modified.&#160;(See&#160;the&#160;createisofill&#160;function.)  
  
Example&#160;of&#160;Use:  
a=vcs.init()  
a. [ show ](/) ('isofill')&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#&#160;Show&#160;all&#160;the&#160;existing&#160;isofill
graphics&#160;methods  
iso=a. [ getisofill ](/) ()&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#&#160;iso&#160;instance&#160;of&#160;'default'
isofill&#160;graphics  
#&#160;&#160;&#160;&#160;&#160;&#160;&#160;method  
iso2=a. [ getisofill ](/) ('quick')&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#&#160;iso2&#160;instance&#160;of&#160;existing
'quick'&#160;isofill  
#&#160;&#160;&#160;&#160;&#160;&#160;&#160;graphics&#160;method `

 getisoline  (self, Gi_name_src  ='default'  ) 
     ` Function:&#160;getisoline&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#&#160;Construct&#160;a&#160;new&#160;isoline&#160;graphics&#160;method   
  
Description&#160;of&#160;Function:  
VCS&#160;contains&#160;a&#160;list&#160;of&#160;graphics&#160;methods.&#160;This&#160;function&#160;will&#160;create&#160;a  
isoline&#160;class&#160;object&#160;from&#160;an&#160;existing&#160;VCS&#160;isoline&#160;graphics&#160;method.&#160;If  
no&#160;isoline&#160;name&#160;is&#160;given,&#160;then&#160;isoline&#160;'default'&#160;will&#160;be&#160;used.  
  
Note,&#160;VCS&#160;does&#160;not&#160;allow&#160;the&#160;modification&#160;of&#160;`default'&#160;attribute  
sets.&#160;However,&#160;a&#160;`default'&#160;attribute&#160;set&#160;that&#160;has&#160;been&#160;copied&#160;under&#160;a  
different&#160;name&#160;can&#160;be&#160;modified.&#160;(See&#160;the&#160;createisoline&#160;function.)  
  
Example&#160;of&#160;Use:  
a=vcs.init()  
a. [ show ](/) ('isoline')&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#&#160;Show&#160;all&#160;the&#160;existing&#160;isoline
graphics&#160;methods  
iso=a. [ getisoline ](/) ()&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#&#160;iso&#160;instance&#160;of&#160;'default'
isoline&#160;graphics  
#&#160;&#160;&#160;&#160;&#160;&#160;&#160;method  
iso2=a. [ getisoline ](/) ('quick')&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#&#160;iso2&#160;instance&#160;of&#160;existing
'quick'&#160;isoline  
#&#160;&#160;&#160;&#160;&#160;&#160;&#160;graphics&#160;method `

 getline  (self, name  ='default'  , ltype  =None  , width  =None  , color  =None  , priority  =None  , viewport  =None  , worldcoordinate  =None  , x  =None  , y  =None  ) 
     ` Function:&#160;getline&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#&#160;Construct&#160;a&#160;new&#160;line&#160;secondary&#160;method   
  
Description&#160;of&#160;Function:  
VCS&#160;contains&#160;a&#160;list&#160;of&#160;secondary&#160;methods.&#160;This&#160;function&#160;will&#160;create&#160;a  
line&#160;class&#160;object&#160;from&#160;an&#160;existing&#160;VCS&#160;line&#160;secondary&#160;method.&#160;If  
no&#160;line&#160;name&#160;is&#160;given,&#160;then&#160;line&#160;'default'&#160;will&#160;be&#160;used.  
  
Note,&#160;VCS&#160;does&#160;not&#160;allow&#160;the&#160;modification&#160;of&#160;`default'&#160;attribute&#160;sets.  
However,&#160;a&#160;`default'&#160;attribute&#160;set&#160;that&#160;has&#160;been&#160;copied&#160;under&#160;a  
different&#160;name&#160;can&#160;be&#160;modified.&#160;(See&#160;the&#160;createline&#160;function.)  
  
Example&#160;of&#160;Use:  
a=vcs.init()  
a. [ show ](/) ('line')&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#&#160;Show&#160;all&#160;the&#160;existing&#160;line
secondary&#160;methods  
ln=a. [ getline ](/) ()&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#&#160;ln&#160;instance&#160;of&#160;'default'&#160;line
secondary  
#&#160;&#160;&#160;&#160;&#160;&#160;&#160;method  
ln2=a. [ getline ](/) ('quick')&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#&#160;ln2&#160;instance&#160;of&#160;existing&#160;'quick'
line  
#&#160;&#160;&#160;&#160;&#160;&#160;&#160;secondary&#160;method  
ln3=a. [ getline ](/) (name='red',&#160;ltype='dash',&#160;width=2,  
color=242,&#160;priority=1,&#160;viewport=[0,&#160;2.0,&#160;0,&#160;2.0],  
worldcoordinate=[0,100,&#160;0,50]  
x=[0,20,40,60,80,100],  
y=[0,10,20,30,40,50]&#160;)&#160;&#160;&#160;&#160;&#160;&#160;#&#160;Create&#160;instance&#160;of&#160;line&#160;object&#160;'red'  
a. [ line ](/) (ln3)&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#&#160;Plot&#160;using&#160;specified&#160;line&#160;object `

 getmarker  (self, name  ='default'  , mtype  =None  , size  =None  , color  =None  , priority  =None  , viewport  =None  , worldcoordinate  =None  , x  =None  , y  =None  ) 
     ` Function:&#160;getmarker&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#&#160;Construct&#160;a&#160;new&#160;marker&#160;secondary&#160;method   
  
Description&#160;of&#160;Function:  
VCS&#160;contains&#160;a&#160;list&#160;of&#160;secondary&#160;methods.&#160;This&#160;function&#160;will&#160;create&#160;a  
marker&#160;class&#160;object&#160;from&#160;an&#160;existing&#160;VCS&#160;marker&#160;secondary&#160;method.&#160;If  
no&#160;marker&#160;name&#160;is&#160;given,&#160;then&#160;marker&#160;'default'&#160;will&#160;be&#160;used.  
  
Note,&#160;VCS&#160;does&#160;not&#160;allow&#160;the&#160;modification&#160;of&#160;`default'&#160;attribute&#160;sets.  
However,&#160;a&#160;`default'&#160;attribute&#160;set&#160;that&#160;has&#160;been&#160;copied&#160;under&#160;a  
different&#160;name&#160;can&#160;be&#160;modified.&#160;(See&#160;the&#160;createmarker&#160;function.)  
  
Example&#160;of&#160;Use:  
a=vcs.init()  
a. [ show ](/) ('marker')&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#&#160;Show&#160;all&#160;the&#160;existing&#160;marker
secondary&#160;methods  
mrk=a. [ getmarker ](/) ()&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#&#160;mrk&#160;instance&#160;of&#160;'default'
marker&#160;secondary  
#&#160;&#160;&#160;&#160;&#160;&#160;&#160;method  
mrk2=a. [ getmarker ](/) ('quick')&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#&#160;mrk2&#160;instance&#160;of&#160;existing
'quick'&#160;marker  
#&#160;&#160;&#160;&#160;&#160;&#160;&#160;secondary&#160;method  
mrk3=a. [ getmarker ](/) (name='red',&#160;mtype='dash',&#160;size=2,  
color=242,&#160;priority=1,&#160;viewport=[0,&#160;2.0,&#160;0,&#160;2.0],  
worldcoordinate=[0,100,&#160;0,50]  
x=[0,20,40,60,80,100],  
y=[0,10,20,30,40,50]&#160;)&#160;&#160;&#160;&#160;&#160;&#160;#&#160;Create&#160;instance&#160;of&#160;marker&#160;object&#160;'red'  
a. [ marker ](/) (mrk3)&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#&#160;Plot&#160;using&#160;specified&#160;marker
object `

 getmeshfill  (self, Gfm_name_src  ='default'  ) 
     ` Function:&#160;getmeshfill&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#&#160;Construct&#160;a&#160;new&#160;meshfill&#160;graphics&#160;method   
  
Description&#160;of&#160;Function:  
VCS&#160;contains&#160;a&#160;list&#160;of&#160;graphics&#160;methods.&#160;This&#160;function&#160;will&#160;create&#160;a  
meshfill&#160;class&#160;object&#160;from&#160;an&#160;existing&#160;VCS&#160;meshfill&#160;graphics&#160;method.&#160;If  
no&#160;meshfill&#160;name&#160;is&#160;given,&#160;then&#160;meshfill&#160;'default'&#160;will&#160;be&#160;used.  
  
Note,&#160;VCS&#160;does&#160;not&#160;allow&#160;the&#160;modification&#160;of&#160;`default'&#160;attribute  
sets.&#160;However,&#160;a&#160;`default'&#160;attribute&#160;set&#160;that&#160;has&#160;been&#160;copied&#160;under&#160;a  
different&#160;name&#160;can&#160;be&#160;modified.&#160;(See&#160;the&#160;createmeshfill&#160;function.)  
  
Example&#160;of&#160;Use:  
a=vcs.init()  
a. [ show ](/) ('meshfill')&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#&#160;Show&#160;all&#160;the&#160;existing&#160;meshfill
graphics&#160;methods  
mesh=a. [ getmeshfill ](/) ()&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#&#160;mesh&#160;instance&#160;of&#160;'default'
meshfill&#160;graphics  
#&#160;method  
mesh2=a. [ getmeshfill ](/) ('quick')&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#&#160;mesh2&#160;instance&#160;of&#160;existing
'quick'&#160;meshfill  
#&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;graphics&#160;method `

 getoutfill  (self, Gfo_name_src  ='default'  ) 
     ` Function:&#160;getoutfill&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#&#160;Construct&#160;a&#160;new&#160;outfill&#160;graphics&#160;method   
  
Description&#160;of&#160;Function:  
VCS&#160;contains&#160;a&#160;list&#160;of&#160;graphics&#160;methods.&#160;This&#160;function&#160;will&#160;create&#160;a  
outfill&#160;class&#160;object&#160;from&#160;an&#160;existing&#160;VCS&#160;outfill&#160;graphics&#160;method.&#160;If  
no&#160;outfill&#160;name&#160;is&#160;given,&#160;then&#160;outfill&#160;'default'&#160;will&#160;be&#160;used.  
  
Note,&#160;VCS&#160;does&#160;not&#160;allow&#160;the&#160;modification&#160;of&#160;`default'&#160;attribute  
sets.&#160;However,&#160;a&#160;`default'&#160;attribute&#160;set&#160;that&#160;has&#160;been&#160;copied&#160;under&#160;a  
different&#160;name&#160;can&#160;be&#160;modified.&#160;(See&#160;the&#160;createoutfill&#160;function.)  
  
Example&#160;of&#160;Use:  
a=vcs.init()  
a. [ show ](/) ('outfill')&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#&#160;Show&#160;all&#160;the&#160;existing&#160;outfill
graphics&#160;methods  
out=a. [ getoutfill ](/) ()&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#&#160;out&#160;instance&#160;of&#160;'default'
outfill&#160;graphics  
#&#160;&#160;&#160;&#160;&#160;&#160;&#160;method  
out2=a. [ getoutfill ](/) ('quick')&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#&#160;out2&#160;instance&#160;of&#160;existing
'quick'&#160;outfill  
#&#160;&#160;&#160;&#160;&#160;&#160;&#160;graphics&#160;method `

 getoutline  (self, Go_name_src  ='default'  ) 
     ` Function:&#160;getoutline&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#&#160;Construct&#160;a&#160;new&#160;outline&#160;graphics&#160;method   
  
Description&#160;of&#160;Function:  
VCS&#160;contains&#160;a&#160;list&#160;of&#160;graphics&#160;methods.&#160;This&#160;function&#160;will&#160;create&#160;a  
outline&#160;class&#160;object&#160;from&#160;an&#160;existing&#160;VCS&#160;outline&#160;graphics&#160;method.&#160;If  
no&#160;outline&#160;name&#160;is&#160;given,&#160;then&#160;outline&#160;'default'&#160;will&#160;be&#160;used.  
  
Note,&#160;VCS&#160;does&#160;not&#160;allow&#160;the&#160;modification&#160;of&#160;`default'&#160;attribute  
sets.&#160;However,&#160;a&#160;`default'&#160;attribute&#160;set&#160;that&#160;has&#160;been&#160;copied&#160;under&#160;a  
different&#160;name&#160;can&#160;be&#160;modified.&#160;(See&#160;the&#160;createoutline&#160;function.)  
  
Example&#160;of&#160;Use:  
a=vcs.init()  
a. [ show ](/) ('outline')&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#&#160;Show&#160;all&#160;the&#160;existing&#160;outline
graphics&#160;methods  
out=a. [ getoutline ](/) ()&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#&#160;out&#160;instance&#160;of&#160;'default'
outline&#160;graphics  
#&#160;&#160;&#160;&#160;&#160;&#160;&#160;method  
out2=a. [ getoutline ](/) ('quick')&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#&#160;out2&#160;instance&#160;of&#160;existing
'quick'&#160;outline  
#&#160;&#160;&#160;&#160;&#160;&#160;&#160;graphics&#160;method `

 getplot  (self, Dp_name_src  ='default'  , template  =None  ) 
     ` Function:&#160;getplot&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#&#160;Get&#160;existing&#160;display&#160;plot   
  
Description&#160;of&#160;Function:  
This&#160;function&#160;will&#160;create&#160;a&#160;display&#160;plot&#160;object&#160;from&#160;an&#160;existing&#160;display  
plot&#160;object&#160;from&#160;an&#160;existing&#160;VCS&#160;plot.&#160;If&#160;no&#160;display&#160;plot&#160;name  
is&#160;given,&#160;then&#160;None&#160;is&#160;returned.  
  
Example&#160;of&#160;Use:  
a=vcs.init()  
a. [ show ](/) ('template')&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#&#160;Show&#160;all&#160;the&#160;existing&#160;templates  
plot1=a. [ getplot ](/) ('dpy_plot_1')&#160;&#160;&#160;&#160;&#160;&#160;&#160;#&#160;plot1&#160;instance&#160;of&#160;'dpy_plot_1'
display&#160;plot `

 getprojection  (self, Proj_name_src  ='default'  ) 
     ` Function:&#160;getprojection&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#&#160;Construct&#160;a&#160;new&#160;projection&#160;method   
  
Description&#160;of&#160;Function:  
VCS&#160;contains&#160;a&#160;list&#160;of&#160;graphics&#160;methods.&#160;This&#160;function&#160;will&#160;create&#160;a  
projection&#160;class&#160;object&#160;from&#160;an&#160;existing&#160;VCS&#160;projection&#160;method.&#160;If  
no&#160;projection&#160;name&#160;is&#160;given,&#160;then&#160;projection&#160;'default'&#160;will&#160;be&#160;used.  
  
Note,&#160;VCS&#160;does&#160;not&#160;allow&#160;the&#160;modification&#160;of&#160;`default'&#160;attribute  
sets.&#160;However,&#160;a&#160;`default'&#160;attribute&#160;set&#160;that&#160;has&#160;been&#160;copied&#160;under&#160;a  
different&#160;name&#160;can&#160;be&#160;modified.&#160;(See&#160;the&#160;createprojection&#160;function.)  
  
Example&#160;of&#160;Use:  
a=vcs.init()  
a. [ show ](/) ('projection')&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#&#160;Show&#160;all&#160;the&#160;existing
projection&#160;methods  
box=a. [ getprojection ](/) ()&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#&#160;box&#160;instance&#160;of&#160;'default'
projection  
#&#160;method  
box2=a. [ getprojection ](/) ('quick')&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#&#160;box2&#160;instance&#160;of&#160;existing
'quick'&#160;projection  
#&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;graphics&#160;method `

 getscatter  (self, GSp_name_src  ='default'  ) 
     ` Function:&#160;getscatter&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#&#160;Construct&#160;a&#160;new&#160;scatter&#160;graphics&#160;method   
  
Description&#160;of&#160;Function:  
VCS&#160;contains&#160;a&#160;list&#160;of&#160;graphics&#160;methods.&#160;This&#160;function&#160;will&#160;create&#160;a  
scatter&#160;class&#160;object&#160;from&#160;an&#160;existing&#160;VCS&#160;scatter&#160;graphics&#160;method.&#160;If  
no&#160;scatter&#160;name&#160;is&#160;given,&#160;then&#160;scatter&#160;'default'&#160;will&#160;be&#160;used.  
  
Note,&#160;VCS&#160;does&#160;not&#160;allow&#160;the&#160;modification&#160;of&#160;`default'&#160;attribute  
sets.&#160;However,&#160;a&#160;`default'&#160;attribute&#160;set&#160;that&#160;has&#160;been&#160;copied&#160;under&#160;a  
different&#160;name&#160;can&#160;be&#160;modified.&#160;(See&#160;the&#160;createscatter&#160;function.)  
  
Example&#160;of&#160;Use:  
a=vcs.init()  
a. [ show ](/) ('scatter')&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#&#160;Show&#160;all&#160;the&#160;existing&#160;scatter
graphics&#160;methods  
sct=a. [ getscatter ](/) ()&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#&#160;sct&#160;instance&#160;of&#160;'default'
scatter&#160;graphics  
#&#160;&#160;&#160;&#160;&#160;&#160;&#160;method  
sct2=a. [ getscatter ](/) ('quick')&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#&#160;sct2&#160;instance&#160;of&#160;existing
'quick'&#160;scatter  
#&#160;&#160;&#160;&#160;&#160;&#160;&#160;graphics&#160;method `

 gettaylordiagram  (self, Gtd_name_src  ='default'  ) 
     ` Function:&#160;gettaylordiagram&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#&#160;Construct&#160;a&#160;new&#160;taylordiagram&#160;graphics&#160;method   
  
Description&#160;of&#160;Function:  
VCS&#160;contains&#160;a&#160;list&#160;of&#160;graphics&#160;methods.&#160;This&#160;function&#160;will&#160;create&#160;a  
taylordiagram&#160;class&#160;object&#160;from&#160;an&#160;existing&#160;VCS&#160;taylordiagram&#160;graphics&#160;method.
If  
no&#160;taylordiagram&#160;name&#160;is&#160;given,&#160;then&#160;taylordiagram&#160;'default'&#160;will&#160;be&#160;used.  
  
Note,&#160;VCS&#160;does&#160;not&#160;allow&#160;the&#160;modification&#160;of&#160;`default'&#160;attribute  
sets.&#160;However,&#160;a&#160;`default'&#160;attribute&#160;set&#160;that&#160;has&#160;been&#160;copied&#160;under&#160;a  
different&#160;name&#160;can&#160;be&#160;modified.&#160;(See&#160;the&#160;createboxfill&#160;function.)  
  
Example&#160;of&#160;Use:  
a=vcs.init()  
a. [ show ](/) ('taylordiagram')&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#&#160;Show&#160;all&#160;the&#160;existing
taylordiagram&#160;graphics&#160;methods  
td=a. [ gettaylordiagram ](/) ()&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#&#160;td&#160;instance&#160;of&#160;'default'
taylordiagram&#160;graphics  
#&#160;method  
td2=a. [ gettaylordiagram ](/) ('default')&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#&#160;td2&#160;instance&#160;of&#160;existing
'default'&#160;taylordiagram  
#&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;graphics&#160;method `

 gettemplate  (self, Pt_name_src  ='default'  ) 
     ` Function:&#160;gettemplate&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#&#160;Construct&#160;a&#160;new&#160;template   
  
Description&#160;of&#160;Function:  
VCS&#160;contains&#160;a&#160;list&#160;of&#160;predefined&#160;templates.&#160;This&#160;function&#160;will&#160;create&#160;a  
template&#160;class&#160;object&#160;from&#160;an&#160;existing&#160;VCS&#160;template.&#160;If&#160;no&#160;template&#160;name  
is&#160;given,&#160;then&#160;template&#160;'default'&#160;will&#160;be&#160;used.  
  
Note,&#160;VCS&#160;does&#160;not&#160;allow&#160;the&#160;modification&#160;of&#160;`default'&#160;attribute  
sets.&#160;However,&#160;a&#160;`default'&#160;attribute&#160;set&#160;that&#160;has&#160;been&#160;copied&#160;under&#160;a  
different&#160;name&#160;can&#160;be&#160;modified.&#160;(See&#160;the&#160;createtemplate&#160;function.)  
  
Example&#160;of&#160;Use:  
a=vcs.init()  
a. [ show ](/) ('template')&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#&#160;Show&#160;all&#160;the&#160;existing&#160;templates  
templt=a. [ gettemplate ](/) ()&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#&#160;templt&#160;instance&#160;of&#160;'default'
template  
templt2=a. [ gettemplate ](/) ('quick')&#160;&#160;&#160;&#160;&#160;&#160;#&#160;templt2&#160;contains&#160;'quick'
template `

 gettext  = [ gettextcombined ](/) (self, Tt_name_src  ='default'  , To_name_src  ='default'  , string  =None  , font  =None  , spacing  =None  , expansion  =None  , color  =None  , priority  =None  , viewport  =None  , worldcoordinate  =None  , x  =None  , y  =None  , height  =None  , angle  =None  , path  =None  , halign  =None  , valign  =None  ) 

 gettextcombined  (self, Tt_name_src  ='default'  , To_name_src  ='default'  , string  =None  , font  =None  , spacing  =None  , expansion  =None  , color  =None  , priority  =None  , viewport  =None  , worldcoordinate  =None  , x  =None  , y  =None  , height  =None  , angle  =None  , path  =None  , halign  =None  , valign  =None  ) 
     ` Function:&#160;gettext&#160;or&#160;gettextcombined&#160;&#160;&#160;#&#160;Construct&#160;a&#160;new&#160;textcombined&#160;secondary&#160;method   
  
Description&#160;of&#160;Function:  
VCS&#160;contains&#160;a&#160;list&#160;of&#160;secondary&#160;methods.&#160;This&#160;function&#160;will&#160;create  
a&#160;textcombined&#160;class&#160;object&#160;from&#160;an&#160;existing&#160;VCS&#160;texttable&#160;secondary  
method&#160;and&#160;an&#160;existing&#160;VCS&#160;textorientation&#160;secondary&#160;method.&#160;If&#160;no  
texttable&#160;or&#160;textorientation&#160;names&#160;are&#160;given,&#160;then&#160;the&#160;'default'&#160;names  
will&#160;be&#160;used&#160;in&#160;both&#160;cases.  
  
Note,&#160;VCS&#160;does&#160;not&#160;allow&#160;the&#160;modification&#160;of&#160;`default'&#160;attribute&#160;sets.  
However,&#160;a&#160;`default'&#160;attribute&#160;set&#160;that&#160;has&#160;been&#160;copied&#160;under&#160;a  
different&#160;name&#160;can&#160;be&#160;modified.&#160;(See&#160;the&#160;createtextcombined&#160;function.)  
  
Example&#160;of&#160;Use:  
a=vcs.init()  
a. [ show ](/) ('texttable')&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#&#160;Show&#160;all&#160;the&#160;existing
texttable&#160;secondary&#160;methods  
a. [ show ](/) ('textorientation')&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#&#160;Show&#160;all&#160;the&#160;existing
textorientation&#160;secondary&#160;methods  
tc=a. [ gettextcombined ](/) ()&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#&#160;Use&#160;'default'&#160;for&#160;texttable
and&#160;textorientation  
tc2=a. [ gettextcombined ](/) ('std','7left')&#160;#&#160;Use&#160;'std'&#160;texttable&#160;and
'7left'&#160;textorientation  
if&#160;istextcombined(tc):&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#&#160;Check&#160;to&#160;see&#160;if&#160;tc&#160;is&#160;a&#160;textcombined  
tc.list()&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#&#160;Print&#160;out&#160;all&#160;its&#160;attriubtes `

 gettextorientation  (self, To_name_src  ='default'  ) 
     ` Function:&#160;gettextorientation&#160;&#160;&#160;&#160;&#160;&#160;&#160;#&#160;Construct&#160;a&#160;new&#160;textorientation&#160;secondary&#160;method   
  
Description&#160;of&#160;Function:  
VCS&#160;contains&#160;a&#160;list&#160;of&#160;secondary&#160;methods.&#160;This&#160;function&#160;will&#160;create  
a&#160;textorientation&#160;class&#160;object&#160;from&#160;an&#160;existing&#160;VCS&#160;textorientation  
secondary&#160;method.&#160;If&#160;no&#160;textorientation&#160;name&#160;is&#160;given,&#160;then  
textorientation&#160;'default'&#160;will&#160;be&#160;used.  
  
Note,&#160;VCS&#160;does&#160;not&#160;allow&#160;the&#160;modification&#160;of&#160;`default'&#160;attribute&#160;sets.  
However,&#160;a&#160;`default'&#160;attribute&#160;set&#160;that&#160;has&#160;been&#160;copied&#160;under&#160;a  
different&#160;name&#160;can&#160;be&#160;modified.&#160;(See&#160;the&#160;createtextorientation&#160;function.)  
  
Example&#160;of&#160;Use:  
a=vcs.init()  
a. [ show ](/) ('textorientation')&#160;&#160;&#160;&#160;#&#160;Show&#160;all&#160;the&#160;existing&#160;textorientation
secondary&#160;methods  
to=a. [ gettextorientation ](/) ()&#160;&#160;&#160;&#160;#&#160;to&#160;instance&#160;of&#160;'default'
textorientation&#160;secondary  
#&#160;&#160;&#160;&#160;&#160;&#160;&#160;method  
to2=a. [ gettextorientation ](/) ('quick')&#160;&#160;#&#160;to2&#160;instance&#160;of&#160;existing&#160;'quick'
textorientation  
#&#160;&#160;&#160;&#160;&#160;&#160;&#160;secondary&#160;method `

 gettexttable  (self, name  ='default'  , font  =None  , spacing  =None  , expansion  =None  , color  =None  , priority  =None  , viewport  =None  , worldcoordinate  =None  , x  =None  , y  =None  ) 
     ` Function:&#160;gettexttable&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#&#160;Construct&#160;a&#160;new&#160;texttable&#160;secondary&#160;method   
  
Description&#160;of&#160;Function:  
VCS&#160;contains&#160;a&#160;list&#160;of&#160;secondary&#160;methods.&#160;This&#160;function&#160;will&#160;create&#160;a  
texttable&#160;class&#160;object&#160;from&#160;an&#160;existing&#160;VCS&#160;texttable&#160;secondary&#160;method.&#160;If  
no&#160;texttable&#160;name&#160;is&#160;given,&#160;then&#160;texttable&#160;'default'&#160;will&#160;be&#160;used.  
  
Note,&#160;VCS&#160;does&#160;not&#160;allow&#160;the&#160;modification&#160;of&#160;`default'&#160;attribute&#160;sets.  
However,&#160;a&#160;`default'&#160;attribute&#160;set&#160;that&#160;has&#160;been&#160;copied&#160;under&#160;a  
different&#160;name&#160;can&#160;be&#160;modified.&#160;(See&#160;the&#160;createtexttable&#160;function.)  
  
Example&#160;of&#160;Use:  
a=vcs.init()  
a. [ show ](/) ('texttable')&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#&#160;Show&#160;all&#160;the&#160;existing&#160;texttable
secondary&#160;methods  
tt=a. [ gettexttable ](/) ()&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#&#160;tt&#160;instance&#160;of&#160;'default'&#160;texttable
secondary  
#&#160;&#160;&#160;&#160;&#160;&#160;&#160;method  
tt2=a. [ gettexttable ](/) ('quick')&#160;&#160;&#160;&#160;&#160;&#160;#&#160;tt2&#160;instance&#160;of&#160;existing&#160;'quick'
texttable  
#&#160;&#160;&#160;&#160;&#160;&#160;&#160;secondary&#160;method  
tt3=a. [ gettexttable ](/) (name='red',&#160;font=1,&#160;spacing=1,expansion=1,  
color=242,&#160;priority=1,&#160;viewport=[0,&#160;2.0,&#160;0,&#160;2.0],  
worldcoordinate=[0,100,&#160;0,50]  
x=[0,20,40,60,80,100],  
y=[0,10,20,30,40,50]&#160;)&#160;&#160;&#160;&#160;&#160;&#160;#&#160;Create&#160;instance&#160;of&#160;texttable&#160;object&#160;'red'  
a.texttable(tt3)&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#&#160;Plot&#160;using&#160;specified&#160;texttable&#160;object
`

 getvector  (self, Gv_name_src  ='default'  ) 
     ` Function:&#160;getvector&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#&#160;Construct&#160;a&#160;new&#160;vector&#160;graphics&#160;method   
  
Description&#160;of&#160;Function:  
VCS&#160;contains&#160;a&#160;list&#160;of&#160;graphics&#160;methods.&#160;This&#160;function&#160;will&#160;create&#160;a  
vector&#160;class&#160;object&#160;from&#160;an&#160;existing&#160;VCS&#160;vector&#160;graphics&#160;method.&#160;If  
no&#160;vector&#160;name&#160;is&#160;given,&#160;then&#160;vector&#160;'default'&#160;will&#160;be&#160;used.  
  
Note,&#160;VCS&#160;does&#160;not&#160;allow&#160;the&#160;modification&#160;of&#160;`default'&#160;attribute  
sets.&#160;However,&#160;a&#160;`default'&#160;attribute&#160;set&#160;that&#160;has&#160;been&#160;copied&#160;under&#160;a  
different&#160;name&#160;can&#160;be&#160;modified.&#160;(See&#160;the&#160;createvector&#160;function.)  
  
Example&#160;of&#160;Use:  
a=vcs.init()  
a. [ show ](/) ('vector')&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#&#160;Show&#160;all&#160;the&#160;existing&#160;vector
graphics&#160;methods  
vec=a. [ getvector ](/) ()&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#&#160;vec&#160;instance&#160;of&#160;'default'&#160;vector
graphics  
#&#160;&#160;&#160;&#160;&#160;&#160;&#160;method  
vec2=a. [ getvector ](/) ('quick')&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#&#160;vec2&#160;instance&#160;of&#160;existing
'quick'&#160;vector  
#&#160;&#160;&#160;&#160;&#160;&#160;&#160;graphics&#160;method `

 getxvsy  (self, GXY_name_src  ='default'  ) 
     ` Function:&#160;getxvsy&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#&#160;Construct&#160;a&#160;new&#160;XvsY&#160;graphics&#160;method   
  
Description&#160;of&#160;Function:  
VCS&#160;contains&#160;a&#160;list&#160;of&#160;graphics&#160;methods.&#160;This&#160;function&#160;will&#160;create&#160;a  
XvsY&#160;class&#160;object&#160;from&#160;an&#160;existing&#160;VCS&#160;XvsY&#160;graphics&#160;method.&#160;If  
no&#160;XvsY&#160;name&#160;is&#160;given,&#160;then&#160;XvsY&#160;'default'&#160;will&#160;be&#160;used.  
  
Note,&#160;VCS&#160;does&#160;not&#160;allow&#160;the&#160;modification&#160;of&#160;`default'&#160;attribute  
sets.&#160;However,&#160;a&#160;`default'&#160;attribute&#160;set&#160;that&#160;has&#160;been&#160;copied&#160;under&#160;a  
different&#160;name&#160;can&#160;be&#160;modified.&#160;(See&#160;the&#160;createxvsy&#160;function.)  
  
Example&#160;of&#160;Use:  
a=vcs.init()  
a. [ show ](/) ('xvsy')&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#&#160;Show&#160;all&#160;the&#160;existing&#160;XvsY
graphics&#160;methods  
xy=a. [ getxvsy ](/) ()&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#&#160;xy&#160;instance&#160;of&#160;'default'&#160;XvsY
graphics  
#&#160;&#160;&#160;&#160;&#160;&#160;&#160;method  
xy2=a. [ getxvsy ](/) ('quick')&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#&#160;xy2&#160;instance&#160;of&#160;existing
'quick'&#160;XvsY  
#&#160;&#160;&#160;&#160;&#160;&#160;&#160;graphics&#160;method `

 getxyvsy  (self, GXy_name_src  ='default'  ) 
     ` Function:&#160;getxyvsy&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#&#160;Construct&#160;a&#160;new&#160;Xyvsy&#160;graphics&#160;method   
  
Description&#160;of&#160;Function:  
VCS&#160;contains&#160;a&#160;list&#160;of&#160;graphics&#160;methods.&#160;This&#160;function&#160;will&#160;create&#160;a  
Xyvsy&#160;class&#160;object&#160;from&#160;an&#160;existing&#160;VCS&#160;Xyvsy&#160;graphics&#160;method.&#160;If  
no&#160;Xyvsy&#160;name&#160;is&#160;given,&#160;then&#160;Xyvsy&#160;'default'&#160;will&#160;be&#160;used.  
  
Note,&#160;VCS&#160;does&#160;not&#160;allow&#160;the&#160;modification&#160;of&#160;`default'&#160;attribute  
sets.&#160;However,&#160;a&#160;`default'&#160;attribute&#160;set&#160;that&#160;has&#160;been&#160;copied&#160;under&#160;a  
different&#160;name&#160;can&#160;be&#160;modified.&#160;(See&#160;the&#160;createxyvsy&#160;function.)  
  
Example&#160;of&#160;Use:  
a=vcs.init()  
a. [ show ](/) ('xyvsy')&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#&#160;Show&#160;all&#160;the&#160;existing&#160;Xyvsy
graphics&#160;methods  
xyy=a. [ getxyvsy ](/) ()&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#&#160;xyy&#160;instance&#160;of&#160;'default'&#160;Xyvsy
graphics  
#&#160;&#160;&#160;&#160;&#160;&#160;&#160;method  
xyy2=a. [ getxyvsy ](/) ('quick')&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#&#160;xyy2&#160;instance&#160;of&#160;existing
'quick'&#160;Xyvsy  
#&#160;&#160;&#160;&#160;&#160;&#160;&#160;graphics&#160;method `

 getyxvsx  (self, GYx_name_src  ='default'  ) 
     ` Function:&#160;getyxvsx&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#&#160;Construct&#160;a&#160;new&#160;Yxvsx&#160;graphics&#160;method   
  
Description&#160;of&#160;Function:  
VCS&#160;contains&#160;a&#160;list&#160;of&#160;graphics&#160;methods.&#160;This&#160;function&#160;will&#160;create&#160;a  
Yxvsx&#160;class&#160;object&#160;from&#160;an&#160;existing&#160;VCS&#160;Yxvsx&#160;graphics&#160;method.&#160;If  
no&#160;Yxvsx&#160;name&#160;is&#160;given,&#160;then&#160;Yxvsx&#160;'default'&#160;will&#160;be&#160;used.  
  
Note,&#160;VCS&#160;does&#160;not&#160;allow&#160;the&#160;modification&#160;of&#160;`default'&#160;attribute  
sets.&#160;However,&#160;a&#160;`default'&#160;attribute&#160;set&#160;that&#160;has&#160;been&#160;copied&#160;under&#160;a  
different&#160;name&#160;can&#160;be&#160;modified.&#160;(See&#160;the&#160;createyxvsx&#160;function.)  
  
Example&#160;of&#160;Use:  
a=vcs.init()  
a. [ show ](/) ('yxvsx')&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#&#160;Show&#160;all&#160;the&#160;existing&#160;Yxvsx
graphics&#160;methods  
yxx=a. [ getyxvsx ](/) ()&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#&#160;yxx&#160;instance&#160;of&#160;'default'&#160;Yxvsx
graphics  
#&#160;&#160;&#160;&#160;&#160;&#160;&#160;method  
yxx2=a. [ getyxvsx ](/) ('quick')&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#&#160;yxx2&#160;instance&#160;of&#160;existing
'quick'&#160;Yxvsx  
#&#160;&#160;&#160;&#160;&#160;&#160;&#160;graphics&#160;method `

 gif  (self, filename  ='noname.gif'  , merge  ='r'  , orientation  ='l'  , geometry  ='792x612'  ) 
     ` Function:&#160;gif   
  
Description&#160;of&#160;Function:  
In&#160;some&#160;cases,&#160;the&#160;user&#160;may&#160;want&#160;to&#160;save&#160;the&#160;plot&#160;out&#160;as&#160;a&#160;gif&#160;image.&#160;This  
routine&#160;allows&#160;the&#160;user&#160;to&#160;save&#160;the&#160;VCS&#160;canvas&#160;output&#160;as&#160;a&#160;SUN&#160;gif&#160;file.  
This&#160;file&#160;can&#160;be&#160;converted&#160;to&#160;other&#160;gif&#160;formats&#160;with&#160;the&#160;aid&#160;of&#160;xv&#160;and&#160;other  
such&#160;imaging&#160;tools&#160;found&#160;freely&#160;on&#160;the&#160;web.  
  
If&#160;no&#160;path/file&#160;name&#160;is&#160;given&#160;and&#160;no&#160;previously&#160;created&#160;gif&#160;file&#160;has&#160;been  
designated,&#160;then&#160;file  
  
/$HOME/PCMDI_GRAPHICS/default.gif  
  
will&#160;be&#160;used&#160;for&#160;storing&#160;gif&#160;images.&#160;However,&#160;if&#160;a&#160;previously&#160;created&#160;gif  
file&#160;is&#160;designated,&#160;that&#160;file&#160;will&#160;be&#160;used&#160;for&#160;gif&#160;output.  
  
By&#160;default,&#160;the&#160;page&#160;orientation&#160;is&#160;in&#160;Landscape&#160;mode&#160;(l).&#160;To&#160;translate&#160;the
page  
orientation&#160;to&#160;portrait&#160;mode&#160;(p),&#160;set&#160;the&#160;orientation&#160;=&#160;'p'.  
  
The&#160;GIF&#160;command&#160;is&#160;used&#160;to&#160;create&#160;or&#160;append&#160;to&#160;a&#160;gif&#160;file.&#160;There&#160;are&#160;two&#160;modes  
for&#160;saving&#160;a&#160;gif&#160;file:&#160;`Append'&#160;mode&#160;(a)&#160;appends&#160;gif&#160;output&#160;to&#160;an&#160;existing&#160;gif  
file;&#160;`Replace'&#160;(r)&#160;mode&#160;overwrites&#160;an&#160;existing&#160;gif&#160;file&#160;with&#160;new&#160;gif&#160;output.  
The&#160;default&#160;mode&#160;is&#160;to&#160;overwrite&#160;an&#160;existing&#160;gif&#160;file&#160;(i.e.&#160;mode&#160;(r)).  
  
Example&#160;of&#160;Use:  
a=vcs.init()  
a. [ plot ](/) (array)  
a. [ gif ](/) (filename='example.gif',&#160;merge='a',&#160;orientation='l',
geometry='800x600')  
a. [ gif ](/) ('example')&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#&#160;overwrite&#160;existing&#160;gif&#160;file&#160;(default&#160;is
merge='r')  
a. [ gif ](/) ('example',merge='r')&#160;&#160;#&#160;overwrite&#160;existing&#160;gif&#160;file  
a. [ gif ](/) ('example',merge='a')&#160;&#160;&#160;&#160;&#160;#&#160;merge&#160;gif&#160;image&#160;into&#160;existing&#160;gif
file  
a. [ gif ](/) ('example',orientation='l')&#160;#&#160;merge&#160;gif&#160;image&#160;into&#160;existing&#160;gif
file&#160;with&#160;landscape&#160;orientation  
a. [ gif ](/) ('example',orientation='p')&#160;#&#160;merge&#160;gif&#160;image&#160;into&#160;existing&#160;gif
file&#160;with&#160;portrait&#160;orientation  
a. [ gif ](/) ('example',geometry='600x500')&#160;#&#160;merge&#160;gif&#160;image&#160;into&#160;existing
gif&#160;file&#160;and&#160;set&#160;the&#160;gif&#160;geometry `

 graphicsmethodgui  (self, gm_type  ='boxfill'  , gm_name  ='default'  , gui_parent  =None  ) 
     ` Function:&#160;graphicsmethodgui   
  
Description&#160;of&#160;Function:  
Run&#160;the&#160;VCS&#160;graphicsmethod&#160;interface.  
  
The&#160;graphicsmethodgui&#160;command&#160;is&#160;used&#160;to&#160;bring&#160;up&#160;the&#160;VCS&#160;graphics&#160;method
interface.  
The&#160;interface&#160;is&#160;used&#160;to&#160;alter&#160;existing&#160;graphics&#160;method&#160;attributes.  
  
Example&#160;of&#160;Use:  
a=vcs.init()  
a. [ graphicsmethodgui ](/) ('boxfill',&#160;'quick') `

 grid  (self, *args) 
     ` Function:&#160;grid   
  
Description&#160;of&#160;Function:  
Set&#160;the&#160;default&#160;plotting&#160;region&#160;for&#160;variables&#160;that&#160;have&#160;more&#160;dimension&#160;values  
than&#160;the&#160;graphics&#160;method.&#160;This&#160;will&#160;also&#160;be&#160;used&#160;for&#160;animating&#160;plots&#160;over&#160;the  
third&#160;and&#160;fourth&#160;dimensions.  
  
  
Example&#160;of&#160;Use:  
a=vcs.init()  
a. [ grid ](/) (12,12,0,71,0,45) `

 gs  (self, filename  ='noname.gs'  , device  ='png256'  , orientation  ='l'  , resolution  ='792x612'  ) 
     ` Function:&#160;gs   
  
Description&#160;of&#160;Function:  
This&#160;routine&#160;allows&#160;the&#160;user&#160;to&#160;save&#160;the&#160;VCS&#160;canvas&#160;in&#160;one&#160;of&#160;the&#160;many  
GhostScript&#160;(gs)&#160;file&#160;types&#160;(also&#160;known&#160;as&#160;devices).&#160;To&#160;view&#160;other  
GhostScript&#160;devices,&#160;issue&#160;the&#160;command&#160;"gs&#160;\--help"&#160;at&#160;the&#160;terminal  
prompt.&#160;Device&#160;names&#160;include:&#160;bmp256,&#160;epswrite,&#160;jpeg,&#160;jpeggray,  
pdfwrite,&#160;png256,&#160;png16m,&#160;sgirgb,&#160;tiffpack,&#160;and&#160;tifflzw.&#160;By&#160;default  
the&#160;device&#160;=&#160;'png256'.  
  
If&#160;no&#160;path/file&#160;name&#160;is&#160;given&#160;and&#160;no&#160;previously&#160;created&#160;gs&#160;file&#160;has&#160;been  
designated,&#160;then&#160;file  
  
/$HOME/PCMDI_GRAPHICS/default.gs  
  
will&#160;be&#160;used&#160;for&#160;storing&#160;gs&#160;images.&#160;However,&#160;if&#160;a&#160;previously&#160;created&#160;gs  
file&#160;exist,&#160;then&#160;this&#160;output&#160;file&#160;will&#160;be&#160;used&#160;for&#160;storage.  
  
By&#160;default,&#160;the&#160;page&#160;orientation&#160;is&#160;in&#160;Landscape&#160;mode&#160;(l).&#160;To&#160;translate  
the&#160;page&#160;orientation&#160;to&#160;portrait&#160;mode&#160;(p),&#160;set&#160;the&#160;parameter&#160;orientation&#160;=
'p'.  
  
The&#160;gs&#160;command&#160;is&#160;used&#160;to&#160;create&#160;a&#160;single&#160;gs&#160;file&#160;at&#160;this&#160;point.&#160;The&#160;user  
can&#160;use&#160;other&#160;tools&#160;to&#160;append&#160;separate&#160;image&#160;files.  
  
Example&#160;of&#160;Use:  
a=vcs.init()  
a. [ plot ](/) (array)  
a. [ gs ](/) ('example')&#160;#defaults:&#160;device='png256',&#160;orientation='l'&#160;and
resolution='792x612'  
a. [ gs ](/) (filename='example.tif',&#160;device='tiffpack',&#160;orientation='l',
resolution='800x600')  
a. [ gs ](/) (filename='example.pdf',&#160;device='pdfwrite',&#160;orientation='l',
resolution='200x200')  
a. [ gs ](/) (filename='example.jpg',&#160;device='jpeg',&#160;orientation='p',
resolution='1000x1000') `

 iscanvasdisplayed  (self, *args) 
     ` Function:&#160;iscanvasdisplayed&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#&#160;Return&#160;1&#160;if&#160;a&#160;VCS [ Canvas ](/) is&#160;displayed   
  
Description&#160;of&#160;Function:  
This&#160;function&#160;returns&#160;a&#160;1&#160;if&#160;a&#160;VCS [ Canvas ](/) is&#160;displayed&#160;or&#160;a&#160;0&#160;if  
no&#160;VCS [ Canvas ](/) is&#160;displayed&#160;on&#160;the&#160;screen.  
  
Example&#160;of&#160;Use:  
a=vcs.init()  
...  
  
a. [ iscanvasdisplayed ](/) () `

 isinfile  (self, GM, file  =None  ) 
     ` Checks&#160;if&#160;a&#160;graphic&#160;method&#160;is&#160;stored&#160;in&#160;a&#160;file   
if&#160;no&#160;file&#160;name&#160;is&#160;passed&#160;then&#160;looks&#160;into&#160;the&#160;initial.attribute&#160;file `

 islandscape  (self) 
     ` Function:&#160;islandscape   
  
Description&#160;of&#160;Function:  
Indicates&#160;if&#160;VCS's&#160;orientation&#160;is&#160;landscape.  
  
Returns&#160;a&#160;1&#160;if&#160;orientation&#160;is&#160;landscape.  
Otherwise,&#160;it&#160;will&#160;return&#160;a&#160;0,&#160;indicating&#160;false&#160;(not&#160;in&#160;landscape&#160;mode).  
  
Example&#160;of&#160;Use:  
a=vcs.init()  
...  
  
if&#160;a. [ islandscape ](/) ():  
a. [ portrait ](/) ()&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#&#160;Set&#160;VCS's&#160;orientation&#160;to&#160;portrait&#160;mode `

 isofill  (self, *args, parms) 
     ` Function:&#160;isofill&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#&#160;Generate&#160;an&#160;isofill&#160;plot   
  
Description&#160;of&#160;Function:  
Generate&#160;a&#160;isofill&#160;plot&#160;given&#160;the&#160;data,&#160;isofill&#160;graphics&#160;method,&#160;and  
template.&#160;If&#160;no&#160;isofill&#160;class&#160;object&#160;is&#160;given,&#160;then&#160;the&#160;'default'&#160;isofill  
graphics&#160;method&#160;is&#160;used.&#160;Similarly,&#160;if&#160;no&#160;template&#160;class&#160;object&#160;is&#160;given,  
then&#160;the&#160;'default'&#160;template&#160;is&#160;used.  
  
Example&#160;of&#160;Use:  
a=vcs.init()  
a. [ show ](/) ('isofill')&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#&#160;Show&#160;all&#160;the&#160;existing&#160;isofill
graphics&#160;methods  
iso=a. [ getisofill ](/) ('quick')&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#&#160;Create&#160;instance&#160;of&#160;'quick'  
a. [ isofill ](/) (array,iso)&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#&#160;Plot&#160;array&#160;using&#160;specified&#160;iso
and&#160;default  
#&#160;&#160;&#160;&#160;&#160;&#160;&#160;template  
a. [ clear ](/) ()&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#&#160;Clear&#160;VCS&#160;canvas  
a. [ isofill ](/) (array,iso,template)&#160;&#160;&#160;&#160;&#160;&#160;&#160;#&#160;Plot&#160;array&#160;using&#160;specified&#160;iso
and&#160;template `

 isoline  (self, *args, parms) 
     ` Function:&#160;isoline&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#&#160;Generate&#160;an&#160;isoline&#160;plot   
  
Description&#160;of&#160;Function:  
Generate&#160;a&#160;isoline&#160;plot&#160;given&#160;the&#160;data,&#160;isoline&#160;graphics&#160;method,&#160;and  
template.&#160;If&#160;no&#160;isoline&#160;class&#160;object&#160;is&#160;given,&#160;then&#160;the&#160;'default'&#160;isoline  
graphics&#160;method&#160;is&#160;used.&#160;Similarly,&#160;if&#160;no&#160;template&#160;class&#160;object&#160;is&#160;given,  
then&#160;the&#160;'default'&#160;template&#160;is&#160;used.  
  
Example&#160;of&#160;Use:  
a=vcs.init()  
a. [ show ](/) ('isoline')&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#&#160;Show&#160;all&#160;the&#160;existing&#160;isoline
graphics&#160;methods  
iso=a. [ getisoline ](/) ('quick')&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#&#160;Create&#160;instance&#160;of&#160;'quick'  
a. [ isoline ](/) (array,iso)&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#&#160;Plot&#160;array&#160;using&#160;specified&#160;iso
and&#160;default  
#&#160;&#160;&#160;&#160;&#160;&#160;&#160;template  
a. [ clear ](/) ()&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#&#160;Clear&#160;VCS&#160;canvas  
a. [ isoline ](/) (array,iso,template)&#160;&#160;&#160;&#160;&#160;&#160;&#160;#&#160;Plot&#160;array&#160;using&#160;specified&#160;iso
and&#160;template `

 isportrait  (self) 
     ` Function:&#160;isportrait   
  
Description&#160;of&#160;Function:  
Indicates&#160;if&#160;VCS's&#160;orientation&#160;is&#160;portrait.  
  
Returns&#160;a&#160;1&#160;if&#160;orientation&#160;is&#160;portrait.  
Otherwise,&#160;it&#160;will&#160;return&#160;a&#160;0,&#160;indicating&#160;false&#160;(not&#160;in&#160;portrait&#160;mode).  
  
Example&#160;of&#160;Use:  
a=vcs.init()  
...  
  
if&#160;a. [ isportrait ](/) ():  
a. [ landscape ](/) ()&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#&#160;Set&#160;VCS's&#160;orientation&#160;to&#160;landscape&#160;mode
`

 landscape  (self, *args) 
     ` Function:&#160;landscape   
  
Description&#160;of&#160;Function:  
Change&#160;the&#160;VCS [ Canvas ](/) orientation&#160;to&#160;Landscape.  
  
Example&#160;of&#160;Use:  
a=vcs.init()  
a. [ plot ](/) (array)  
a. [ landscape ](/) ()&#160;#&#160;Change&#160;the&#160;VCS [ Canvas ](/) orientation&#160;and&#160;set
object&#160;flag&#160;to&#160;landscape `

 line  (self, *args, parms) 
     ` Function:&#160;line&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#&#160;Generate&#160;a&#160;line&#160;plot   
  
Description&#160;of&#160;Function:  
Plot&#160;a&#160;line&#160;segment&#160;on&#160;the&#160;Vcs [ Canvas ](/) .&#160;If&#160;no&#160;line&#160;class  
object&#160;is&#160;given,&#160;then&#160;an&#160;error&#160;will&#160;be&#160;returned.  
  
Example&#160;of&#160;Use:  
a=vcs.init()  
a. [ show ](/) ('line')&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#&#160;Show&#160;all&#160;the&#160;existing&#160;line
objects  
ln=a. [ getline ](/) ('red')&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#&#160;Create&#160;instance&#160;of&#160;'red'  
ln.width=4&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#&#160;Set&#160;the&#160;line&#160;width  
ln.color&#160;=&#160;242&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#&#160;Set&#160;the&#160;line&#160;color  
ln.type&#160;=&#160;4&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#&#160;Set&#160;the&#160;line&#160;type  
ln.x=[[0.0,2.0,2.0,0.0,0.0],&#160;[0.5,1.5]]&#160;#&#160;Set&#160;the&#160;x&#160;value&#160;points  
ln.y=[[0.0,0.0,2.0,2.0,0.0],&#160;[1.0,1.0]]&#160;#&#160;Set&#160;the&#160;y&#160;value&#160;points  
a. [ line ](/) (ln)&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#&#160;Plot&#160;using&#160;specified&#160;line
object `

 listelements  (self, *args) 
     ` Function:&#160;listelements   
  
Description&#160;of&#160;Function:  
Returns&#160;a&#160;Python&#160;list&#160;of&#160;all&#160;the&#160;VCS&#160;class&#160;objects.  
  
The&#160;list&#160;that&#160;will&#160;be&#160;returned:  
['template',&#160;'boxfill',&#160;'continent',&#160;'isofill',&#160;'isoline',&#160;'outfill',
'outline',  
'scatter',&#160;'vector',&#160;'xvsy',&#160;'xyvsy',&#160;'yxvsx',&#160;'colormap',&#160;'fillarea',
'format',  
'line',&#160;'list',&#160;'marker',&#160;'text']  
  
Example&#160;of&#160;Use:  
a=vcs.init()  
a. [ listelements ](/) () `

 marker  (self, *args, parms) 
     ` Function:&#160;marker&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#&#160;Generate&#160;a&#160;marker&#160;plot   
  
Description&#160;of&#160;Function:  
Plot&#160;a&#160;marker&#160;segment&#160;on&#160;the&#160;Vcs [ Canvas ](/) .&#160;If&#160;no&#160;marker&#160;class  
object&#160;is&#160;given,&#160;then&#160;an&#160;error&#160;will&#160;be&#160;returned.  
  
Example&#160;of&#160;Use:  
a=vcs.init()  
a. [ show ](/) ('marker')&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#&#160;Show&#160;all&#160;the&#160;existing&#160;marker
objects  
mrk=a. [ getmarker ](/) ('red')&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#&#160;Create&#160;instance&#160;of&#160;'red'  
mrk.size=4&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#&#160;Set&#160;the&#160;marker&#160;size  
mrk.color&#160;=&#160;242&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#&#160;Set&#160;the&#160;marker&#160;color  
mrk.type&#160;=&#160;4&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#&#160;Set&#160;the&#160;marker&#160;type  
mrk.x=[[0.0,2.0,2.0,0.0,0.0],&#160;[0.5,1.5]]&#160;#&#160;Set&#160;the&#160;x&#160;value&#160;points  
mrk.y=[[0.0,0.0,2.0,2.0,0.0],&#160;[1.0,1.0]]&#160;#&#160;Set&#160;the&#160;y&#160;value&#160;points  
a. [ marker ](/) (mrk)&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#&#160;Plot&#160;using&#160;specified&#160;marker
object `

 match_color  (self, color, colormap  =None  ) 
     ` Function:&#160;cmatch_color&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#&#160;Returns&#160;the&#160;color&#160;in&#160;the&#160;colormap&#160;that&#160;is&#160;closet&#160;from&#160;the&#160;required&#160;color   
Description&#160;of&#160;Function:  
Given&#160;a&#160;color&#160;(defined&#160;as&#160;rgb&#160;values&#160;-0/100&#160;range-&#160;or&#160;a&#160;string&#160;name)&#160;and
optionally&#160;a&#160;colormap&#160;name,  
returns&#160;the&#160;color&#160;number&#160;that&#160;is&#160;closet&#160;from&#160;the&#160;requested&#160;color  
(using&#160;rms&#160;difference&#160;between&#160;rgb&#160;values)  
if&#160;colormap&#160;is&#160;not&#160;map&#160;use&#160;the&#160;currently&#160;used&#160;colormap  
Example&#160;of&#160;use:  
a=vcs.init()  
print&#160;a. [ match_color ](/) ('salmon')  
print&#160;a. [ match_color ](/) ('red')  
print&#160;a. [ match_color ](/) ([0,0,100],'defaullt')&#160;#&#160;closest&#160;color&#160;from&#160;blue `

 meshfill  (self, *args, parms) 
     ` Function:&#160;meshfill&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#&#160;Generate&#160;an&#160;meshfill&#160;plot   
  
Description&#160;of&#160;Function:  
Generate&#160;a&#160;meshfill&#160;plot&#160;given&#160;the&#160;data,&#160;the&#160;mesh,&#160;a&#160;meshfill&#160;graphics&#160;method,
and  
a&#160;template.&#160;If&#160;no&#160;meshfill&#160;class&#160;object&#160;is&#160;given,&#160;then&#160;the&#160;'default'&#160;meshfill  
graphics&#160;method&#160;is&#160;used.&#160;Similarly,&#160;if&#160;no&#160;template&#160;class&#160;object&#160;is&#160;given,  
then&#160;the&#160;'default'&#160;template&#160;is&#160;used.  
  
Format:  
This&#160;function&#160;expects&#160;1D&#160;data&#160;(any&#160;extra&#160;dimension&#160;will&#160;be&#160;used&#160;for&#160;animation)  
In&#160;addition&#160;the&#160;mesh&#160;array&#160;must&#160;be&#160;of&#160;the&#160;same&#160;shape&#160;than&#160;data&#160;with&#160;2
additional&#160;dimension&#160;representing&#160;the&#160;vertices&#160;coordinates&#160;for&#160;the&#160;Y&#160;(0)&#160;and&#160;X
(1)&#160;dimension  
Let's&#160;say&#160;you&#160;want&#160;to&#160;plot&#160;a&#160;spatial&#160;assuming&#160;mesh&#160;containing&#160;10,000&#160;grid
cell,&#160;then&#160;data&#160;must&#160;be&#160;shape&#160;(10000,)&#160;or&#160;(n1,n2,n3,...,10000)&#160;if&#160;additional
dimensions&#160;exist&#160;(ex&#160;time,level),&#160;these&#160;dimension&#160;would&#160;be&#160;used&#160;only&#160;for
animation&#160;and&#160;will&#160;be&#160;ignored&#160;in&#160;the&#160;rest&#160;of&#160;this&#160;example.  
The&#160;shape&#160;of&#160;the&#160;mesh,&#160;assuming&#160;4&#160;vertices&#160;per&#160;grid&#160;cell,&#160;must&#160;be&#160;(1000,2,4),
where&#160;the&#160;array&#160;[:,0,:]&#160;represent&#160;the&#160;Y&#160;coordinates&#160;of&#160;the&#160;vertices&#160;(clockwise
or&#160;counterclockwise)&#160;and&#160;the&#160;array&#160;[:,1:]&#160;represents&#160;the&#160;X&#160;coordinates&#160;of&#160;the
vertices&#160;(the&#160;same&#160;clockwise/counterclockwise&#160;than&#160;the&#160;Y&#160;coordinates)  
In&#160;brief&#160;you'd&#160;have:  
data.shape=(10000,)  
mesh.shape=(10000,2,4)  
  
Example&#160;of&#160;Use:  
a=vcs.init()  
a. [ show ](/) ('meshfill')&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#&#160;Show&#160;all&#160;the&#160;existing&#160;meshfill
graphics&#160;methods  
mesh=a. [ getmeshfill ](/) ()&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#&#160;Create&#160;instance&#160;of&#160;'default'  
a. [ meshfill ](/) (array,mesh)&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#&#160;Plot&#160;array&#160;using&#160;specified
mesh&#160;and&#160;default  
#&#160;&#160;&#160;&#160;&#160;&#160;&#160;template  
a. [ clear ](/) ()&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#&#160;Clear&#160;VCS&#160;canvas  
a. [ meshfill ](/) (array,mesh,mesh_graphic_method,template)&#160;#&#160;Plot&#160;array
using&#160;specified&#160;mesh&#160;mesh&#160;graphic&#160;method&#160;and&#160;template `

 objecthelp  (self, *arg) 
     ` Function:&#160;objecthelp&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#&#160;Print&#160;out&#160;the&#160;object's&#160;doc&#160;string   
  
Description&#160;of&#160;Function:  
Print&#160;out&#160;information&#160;on&#160;the&#160;VCS&#160;object.&#160;See&#160;example&#160;below&#160;on&#160;its&#160;use.  
  
Example&#160;of&#160;Use:  
a=vcs.init()  
  
ln=a. [ getline ](/) ('red')&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#&#160;Get&#160;a&#160;VCS&#160;line&#160;object  
a. [ objecthelp ](/) (ln)&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#&#160;This&#160;will&#160;print&#160;out&#160;information
on&#160;how&#160;to&#160;use&#160;ln `

 open  (self, *args) 
     ` Function:&#160;open   
  
Description&#160;of&#160;Function:  
Open&#160;VCS [ Canvas ](/) object.&#160;This&#160;routine&#160;really&#160;just&#160;manages&#160;the&#160;VCS
canvas.&#160;It&#160;will  
popup&#160;the&#160;VCS [ Canvas ](/) for&#160;viewing.&#160;It&#160;can&#160;be&#160;used&#160;to&#160;display&#160;the&#160;VCS [
Canvas ](/) .  
  
Example&#160;of&#160;Use:  
a=vcs.init()  
a. [ open ](/) () `

 orientation  (self, *args) 
     ` Function:&#160;orientation   
  
Description&#160;of&#160;Function:  
Return&#160;VCS's&#160;orientation.&#160;Will&#160;return&#160;either&#160;Portrait&#160;or&#160;Landscape.  
  
Example&#160;of&#160;Use:  
a=vcs.init()  
a. [ orientation ](/) ()&#160;&#160;&#160;&#160;&#160;&#160;#&#160;Return&#160;either&#160;"landscape"&#160;or&#160;"portrait" `

 outfill  (self, *args, parms) 
     ` Function:&#160;outfill&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#&#160;Generate&#160;an&#160;outfill&#160;plot   
  
Description&#160;of&#160;Function:  
Generate&#160;a&#160;outfill&#160;plot&#160;given&#160;the&#160;data,&#160;outfill&#160;graphics&#160;method,&#160;and  
template.&#160;If&#160;no&#160;outfill&#160;class&#160;object&#160;is&#160;given,&#160;then&#160;the&#160;'default'&#160;outfill  
graphics&#160;method&#160;is&#160;used.&#160;Simerly,&#160;if&#160;no&#160;template&#160;class&#160;object&#160;is&#160;given,  
then&#160;the&#160;'default'&#160;template&#160;is&#160;used.  
  
Example&#160;of&#160;Use:  
a=vcs.init()  
a. [ show ](/) ('outfill')&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#&#160;Show&#160;all&#160;the&#160;existing&#160;outfill
graphics&#160;methods  
out=a. [ getoutfill ](/) ('quick')&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#&#160;Create&#160;instance&#160;of&#160;'quick'  
a. [ outfill ](/) (array,out)&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#&#160;Plot&#160;array&#160;using&#160;specified&#160;out
and&#160;default  
#&#160;&#160;&#160;&#160;&#160;&#160;&#160;template  
a. [ clear ](/) ()&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#&#160;Clear&#160;VCS&#160;canvas  
a. [ outfill ](/) (array,out,template)&#160;&#160;&#160;&#160;&#160;&#160;&#160;#&#160;Plot&#160;array&#160;using&#160;specified&#160;out
and&#160;template `

 outline  (self, *args, parms) 
     ` Function:&#160;outline&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#&#160;Generate&#160;an&#160;outline&#160;plot   
  
Description&#160;of&#160;Function:  
Generate&#160;a&#160;outline&#160;plot&#160;given&#160;the&#160;data,&#160;outline&#160;graphics&#160;method,&#160;and  
template.&#160;If&#160;no&#160;outline&#160;class&#160;object&#160;is&#160;given,&#160;then&#160;the&#160;'default'&#160;outline  
graphics&#160;method&#160;is&#160;used.&#160;Simerly,&#160;if&#160;no&#160;template&#160;class&#160;object&#160;is&#160;given,  
then&#160;the&#160;'default'&#160;template&#160;is&#160;used.  
  
Example&#160;of&#160;Use:  
a=vcs.init()  
a. [ show ](/) ('outline')&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#&#160;Show&#160;all&#160;the&#160;existing&#160;outline
graphics&#160;methods  
out=a. [ getoutline ](/) ('quick')&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#&#160;Create&#160;instance&#160;of&#160;'quick'  
a. [ outline ](/) (array,out)&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#&#160;Plot&#160;array&#160;using&#160;specified&#160;out
and&#160;default  
#&#160;&#160;&#160;&#160;&#160;&#160;&#160;template  
a. [ clear ](/) ()&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#&#160;Clear&#160;VCS&#160;canvas  
a. [ outline ](/) (array,out,template)&#160;&#160;&#160;&#160;&#160;&#160;&#160;#&#160;Plot&#160;array&#160;using&#160;specified&#160;out
and&#160;template `

 page  (self, *args) 
     ` Function:&#160;page   
  
Description&#160;of&#160;Function:  
Change&#160;the&#160;VCS [ Canvas ](/) orientation&#160;to&#160;either&#160;'portrait'&#160;or&#160;'landscape'.  
  
The&#160;orientation&#160;of&#160;the&#160;VCS [ Canvas ](/) and&#160;of&#160;cgm&#160;and&#160;raster&#160;images&#160;is
controlled&#160;by  
the&#160;PAGE&#160;command.&#160;Only&#160;portrait&#160;(y&#160;>&#160;x)&#160;or&#160;landscape&#160;(x&#160;>&#160;y)&#160;orientations&#160;are  
permitted.  
  
Example&#160;of&#160;Use:  
a=vcs.init()  
a. [ plot ](/) (array)  
a. [ page ](/) ()&#160;&#160;&#160;&#160;&#160;&#160;#&#160;Change&#160;the&#160;VCS [ Canvas ](/) orientation&#160;and&#160;set
object&#160;flag&#160;to&#160;portrait `

 pageeditor  (self, gui_parent  =None  , continents  =None  ) 
     ` Function:&#160;pageeditor   
  
Description&#160;of&#160;Function:  
Run&#160;the&#160;VCS&#160;page&#160;editor&#160;GUI.  
  
The&#160;pageeditor&#160;command&#160;is&#160;used&#160;to&#160;bring&#160;up&#160;the&#160;VCS&#160;page&#160;editor&#160;interface.  
The&#160;interface&#160;is&#160;used&#160;to&#160;design&#160;canvases.  
  
Example&#160;of&#160;Use:  
a=vcs.init()  
a.pageieditor() `

 pdf  (self, *args) 
     ` Function:&#160;pdf   
  
Description&#160;of&#160;Function:  
To&#160;save&#160;out&#160;a&#160;postscript&#160;file,  
VCS&#160;will&#160;first&#160;create&#160;a&#160;cgm&#160;file&#160;in&#160;the&#160;user's&#160;PCMDI_GRAPHICS&#160;directory.&#160;Then
it&#160;will  
use&#160;gplot&#160;to&#160;convert&#160;the&#160;cgm&#160;file&#160;to&#160;a&#160;postscript&#160;file&#160;in&#160;the&#160;location&#160;the
user&#160;has  
chosen.&#160;And&#160;then&#160;convert&#160;it&#160;pdf&#160;using&#160;ps2pdf  
  
The&#160;pdf&#160;command&#160;is&#160;used&#160;to&#160;create&#160;a&#160;pdf&#160;file.&#160;Orientation&#160;is&#160;'l'&#160;=&#160;landscape,  
or&#160;'p'&#160;=&#160;portrait.&#160;The&#160;default&#160;is&#160;landscape.  
  
Example&#160;of&#160;Use:  
a=vcs.init()  
a. [ plot ](/) (array)  
a. [ pdf ](/) ('example')&#160;&#160;&#160;&#160;&#160;&#160;#&#160;Creates&#160;a&#160;landscape&#160;pdf&#160;file  
a. [ pdf ](/) ('example','p')&#160;&#160;#&#160;Creates&#160;a&#160;portrait&#160;pdf&#160;file `

 plot  (self, *actual_args, keyargs) 
     ` Function:&#160;plot   
  
Description&#160;of&#160;plot:  
Plot&#160;an&#160;array(s)&#160;of&#160;data&#160;given&#160;a&#160;template&#160;and&#160;graphics&#160;method.&#160;The&#160;VCS
template&#160;is  
used&#160;to&#160;define&#160;where&#160;the&#160;data&#160;and&#160;variable&#160;attributes&#160;will&#160;be&#160;displayed&#160;on&#160;the
VCS  
[ Canvas ](/) .&#160;The&#160;VCS&#160;graphics&#160;method&#160;is&#160;used&#160;to&#160;define&#160;how&#160;the&#160;array(s)
will&#160;be&#160;shown  
on&#160;the&#160;VCS [ Canvas ](/) .  
  
The&#160;form&#160;of&#160;the&#160;call&#160;is:  
[ plot ](/) (array1=None,&#160;array2=None,&#160;template_name=None,
graphics_method=None,  
graphics_name=None,&#160;[key=value&#160;[,&#160;key=value&#160;[,&#160;...]]])  
  
where&#160;array1&#160;and&#160;array2&#160;are&#160;NumPy&#160;arrays.  
  
Plot&#160;keywords:  
ratio&#160;[default&#160;is&#160;none]  
None:&#160;let&#160;the&#160;self.  ratio  attribute&#160;decide  
0,'off':&#160;overwritte&#160;self.  ratio  and&#160;do&#160;nothing&#160;about&#160;the&#160;ratio  
'auto':&#160;computes&#160;an&#160;automatic&#160;ratio  
'3',3:&#160;y&#160;dim&#160;will&#160;be&#160;3&#160;times&#160;bigger&#160;than&#160;x&#160;dim&#160;(restricted&#160;to&#160;original
tempalte.data&#160;area  
Adding&#160;a&#160;'t'&#160;at&#160;the&#160;end&#160;of&#160;the&#160;ratio,&#160;makes&#160;the&#160;tickmarks&#160;and&#160;boxes&#160;move
along.  
  
Variable&#160;attribute&#160;keys:  
comment1&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;=&#160;string&#160;&#160;&#160;#Comment&#160;plotted&#160;above&#160;file_comment  
comment2&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;=&#160;string&#160;&#160;&#160;#Comment&#160;plotted&#160;above&#160;comment1  
comment3&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;=&#160;string&#160;&#160;&#160;#Comment&#160;plotted&#160;above&#160;comment2  
comment4&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;=&#160;string&#160;&#160;&#160;#Comment&#160;plotted&#160;above&#160;comment4  
file_comment&#160;&#160;&#160;&#160;&#160;=&#160;string&#160;&#160;&#160;#Comment&#160;(defaults&#160;to&#160;file.comment)  
hms&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;=&#160;string&#160;(hh:mm:ss)&#160;#Hour,&#160;minute,&#160;second  
long_name&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;=&#160;string&#160;&#160;&#160;#Descriptive&#160;variable&#160;name  
name&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;=&#160;string&#160;&#160;&#160;#Variable&#160;name&#160;(defaults&#160;to&#160;var.id)  
time&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;=&#160;cdtime&#160;&#160;&#160;#instance&#160;(relative&#160;or&#160;absolute),  
cdtime,&#160;reltime&#160;or&#160;abstime&#160;value  
units&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;=&#160;string&#160;&#160;&#160;#Variable&#160;units  
ymd&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;=&#160;string&#160;(yy/mm/dd)&#160;#Year,&#160;month,&#160;day  
  
Dimension&#160;attribute&#160;keys&#160;(dimension&#160;length=n):  
[x|y|z|t|w]array1&#160;=&#160;NumPy&#160;array&#160;of&#160;length&#160;n&#160;&#160;&#160;&#160;#&#160;x&#160;or&#160;y&#160;Dimension&#160;values  
[x|y|z|t|w]array2&#160;=&#160;NumPy&#160;array&#160;of&#160;length&#160;n&#160;&#160;&#160;&#160;#&#160;x&#160;or&#160;y&#160;Dimension&#160;values  
[x|y]bounds&#160;&#160;&#160;&#160;&#160;&#160;&#160;=&#160;NumPy&#160;array&#160;of&#160;shape&#160;(n,2)&#160;#&#160;x&#160;or&#160;y&#160;Dimension&#160;boundaries  
[x|y|z|t|w]name&#160;&#160;&#160;=&#160;string&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#&#160;x&#160;or&#160;y&#160;Dimension&#160;name  
[x|y|z|t|w]units&#160;&#160;=&#160;string&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#&#160;x&#160;or&#160;y&#160;Dimension&#160;units  
[x|y]weights&#160;&#160;&#160;&#160;&#160;&#160;=&#160;NumPy&#160;array&#160;of&#160;length&#160;n&#160;&#160;&#160;&#160;#&#160;x&#160;or&#160;y&#160;Dimension&#160;weights
(used&#160;to  
calculate&#160;area-weighted&#160;mean)  
  
CDMS&#160;object:  
[x|y|z|t|w]axis&#160;&#160;&#160;=&#160;CDMS&#160;axis&#160;object&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#&#160;x&#160;or&#160;y&#160;Axis  
grid&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;=&#160;CDMS&#160;grid&#160;object&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#&#160;Grid&#160;object&#160;(e.g.
grid=var.getGrid()  
variable&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;=&#160;CDMS&#160;variable&#160;object&#160;&#160;&#160;&#160;&#160;&#160;&#160;#&#160;Variable&#160;object  
  
Other:  
[x|y]rev&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;=&#160;0|1&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#&#160;if&#160;==1,&#160;reverse&#160;the&#160;direction
of&#160;the&#160;x  
or&#160;y&#160;axis  
continents&#160;&#160;&#160;&#160;&#160;&#160;&#160;=&#160;0,1,2,3,4,5,6,7,8,9,10,11&#160;&#160;&#160;#&#160;if&#160;>=1,&#160;plot&#160;continental
outlines  
(default:&#160;plot&#160;if&#160;xaxis&#160;is  
longitude,&#160;yaxis&#160;is&#160;latitude&#160;-or-  
xname&#160;is&#160;'longitude'&#160;and&#160;yname&#160;is  
'latitude'  
#&#160;The&#160;continents-type&#160;values&#160;are&#160;integers  
#&#160;ranging&#160;from&#160;0&#160;to&#160;11,&#160;where:  
#&#160;&#160;&#160;&#160;0&#160;signifies&#160;"No&#160;Continents"  
#&#160;&#160;&#160;&#160;1&#160;signifies&#160;"Fine&#160;Continents"  
#&#160;&#160;&#160;&#160;2&#160;signifies&#160;"Coarse&#160;Continents"  
#&#160;&#160;&#160;&#160;3&#160;signifies&#160;"United&#160;States"  
#&#160;&#160;&#160;&#160;4&#160;signifies&#160;"Political&#160;Borders"  
#&#160;&#160;&#160;&#160;5&#160;signifies&#160;"Rivers"  
  
#&#160;Values&#160;6&#160;through&#160;11&#160;signify&#160;the&#160;line&#160;type  
#&#160;defined&#160;by&#160;the&#160;files&#160;data_continent_other7  
#&#160;through&#160;data_continent_other12.  
  
Graphics&#160;Output&#160;in&#160;Background&#160;Mode:  
bg&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;=&#160;0|1&#160;&#160;&#160;#&#160;if&#160;==1,&#160;create&#160;images&#160;in&#160;the&#160;background  
(Don't&#160;display&#160;the&#160;VCS [ Canvas ](/) )  
  
Note:  
More&#160;specific&#160;attributes&#160;take&#160;precedence&#160;over&#160;general&#160;attributes.&#160;In
particular,  
specifie&#160;attributes&#160;override&#160;variable&#160;object&#160;attributes,&#160;dimension&#160;attributes
and  
arrays&#160;override&#160;axis&#160;objects,&#160;which&#160;override&#160;grid&#160;objects,&#160;which&#160;override
variable  
objects.  
  
For&#160;example,&#160;if&#160;both&#160;'file_comment'&#160;and&#160;'variable'&#160;keywords&#160;are&#160;specified,&#160;the
value&#160;of  
'file_comment'&#160;is&#160;used&#160;instead&#160;of&#160;the&#160;file&#160;comment&#160;in&#160;the&#160;parent&#160;of&#160;variable.
Similarly,  
if&#160;both&#160;'xaxis'&#160;and&#160;'grid'&#160;keywords&#160;are&#160;specified,&#160;the&#160;value&#160;of&#160;'xaxis'&#160;takes
precedence  
over&#160;the&#160;x-axis&#160;of&#160;grid.  
  
Example&#160;of&#160;Use:  
x=vcs.init()&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#&#160;x&#160;is&#160;an&#160;instance&#160;of&#160;the&#160;VCS&#160;class&#160;object&#160;(constructor)  
x. [ plot ](/) (array)&#160;&#160;&#160;&#160;&#160;&#160;&#160;#&#160;this&#160;call&#160;will&#160;use&#160;default&#160;settings&#160;for
template&#160;and&#160;boxfill  
x. [ plot ](/) (array,&#160;'AMIP',&#160;'isofill','AMIP_psl')&#160;#&#160;this&#160;is&#160;specifying&#160;the
template&#160;and  
graphics&#160;method  
t=x. [ gettemplate ](/) ('AMIP')&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#&#160;get&#160;a&#160;predefined&#160;the&#160;template&#160;'AMIP'  
vec=x. [ getvector ](/) ('quick')&#160;&#160;&#160;&#160;&#160;&#160;&#160;#&#160;get&#160;a&#160;predefined&#160;the&#160;vector&#160;graphics
method&#160;'quick'  
x. [ plot ](/) (array1,&#160;array2,&#160;t,&#160;vec)&#160;#&#160;plot&#160;the&#160;data&#160;as&#160;a&#160;vector&#160;using&#160;the
'AMIP'&#160;template  
x. [ clear ](/) ()&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#&#160;clear&#160;the&#160;VCS [ Canvas ](/) of&#160;all
plots  
box=x. [ createboxfill ](/) ('new')&#160;&#160;&#160;&#160;&#160;#&#160;create&#160;boxfill&#160;graphics&#160;method&#160;'new'  
x. [ plot ](/) (box,t,array)&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#&#160;plot&#160;array&#160;data&#160;using&#160;box&#160;'new'&#160;and
template&#160;'t' `

 plot_filledcontinents  (self, slab, template_name, g_type, g_name, bg, ratio) 

 portrait  (self, *args) 
     ` Function:&#160;portrait   
  
Description&#160;of&#160;Function:  
Change&#160;the&#160;VCS [ Canvas ](/) orientation&#160;to&#160;Portrait.  
  
Example&#160;of&#160;Use:  
a=vcs.init()  
a. [ plot ](/) (array)  
a. [ portrait ](/) ()&#160;&#160;&#160;&#160;&#160;&#160;#&#160;Change&#160;the&#160;VCS [ Canvas ](/) orientation&#160;and&#160;set
object&#160;flag&#160;to&#160;portrait `

 postscript  (self, *args) 
     ` Function:&#160;postscript   
  
Description&#160;of&#160;Function:  
Postscript&#160;output&#160;is&#160;another&#160;form&#160;of&#160;vector&#160;graphics.&#160;It&#160;is&#160;larger&#160;than&#160;its
CGM&#160;output  
counter&#160;part,&#160;because&#160;it&#160;is&#160;stored&#160;out&#160;in&#160;ASCII&#160;format.&#160;To&#160;save&#160;out&#160;a
postscript&#160;file,  
VCS&#160;will&#160;first&#160;create&#160;a&#160;cgm&#160;file&#160;in&#160;the&#160;user's&#160;PCMDI_GRAPHICS&#160;directory.&#160;Then
it&#160;will  
use&#160;gplot&#160;to&#160;convert&#160;the&#160;cgm&#160;file&#160;to&#160;a&#160;postscript&#160;file&#160;in&#160;the&#160;location&#160;the
user&#160;has  
chosen.  
  
There&#160;are&#160;two&#160;modes&#160;for&#160;saving&#160;a&#160;postscript&#160;file:&#160;`Append'&#160;(a)&#160;mode&#160;appends
postscript  
output&#160;to&#160;an&#160;existing&#160;postscript&#160;file;&#160;and&#160;`Replace'&#160;(r)&#160;mode&#160;overwrites&#160;an
existing  
postscript&#160;file&#160;with&#160;new&#160;postscript&#160;output.&#160;The&#160;default&#160;mode&#160;is&#160;to&#160;overwrite
an&#160;existing  
postscript&#160;file&#160;(i.e.&#160;mode&#160;(r)).  
  
The&#160;POSTSCRIPT&#160;command&#160;is&#160;used&#160;to&#160;create&#160;a&#160;postscript&#160;file.&#160;Orientation&#160;is&#160;'l'
=&#160;landscape,  
or&#160;'p'&#160;=&#160;portrait.&#160;The&#160;default&#160;is&#160;landscape.  
  
Example&#160;of&#160;Use:  
a=vcs.init()  
a. [ plot ](/) (array)  
a. [ postscript ](/) ('example')&#160;&#160;&#160;&#160;&#160;&#160;&#160;#&#160;Overwrite&#160;a&#160;landscape&#160;postscript&#160;file  
a. [ postscript ](/) ('example',&#160;'a')&#160;&#160;#&#160;Append&#160;postscript&#160;to&#160;an&#160;existing&#160;file  
a. [ postscript ](/) ('example',&#160;'r')&#160;&#160;#&#160;Overwrite&#160;an&#160;existing&#160;file  
a. [ postscript ](/) ('example',&#160;'r',&#160;'p')&#160;&#160;#&#160;Overwrite&#160;postscript&#160;file&#160;with&#160;a
portrait&#160;postscript&#160;file `

 printer  (self, *args) 
     ` Function:&#160;printer   
  
Description&#160;of&#160;Function:  
This&#160;function&#160;creates&#160;a&#160;temporary&#160;cgm&#160;file&#160;and&#160;then&#160;sends&#160;it&#160;to&#160;the&#160;specified  
printer.&#160;Once&#160;the&#160;printer&#160;received&#160;the&#160;information,&#160;then&#160;the&#160;temporary&#160;cgm
file  
is&#160;deleted.&#160;The&#160;temporary&#160;cgm&#160;file&#160;is&#160;created&#160;in&#160;the&#160;user's&#160;PCMDI_GRAPHICS
directory.  
  
The&#160;PRINTER&#160;command&#160;is&#160;used&#160;to&#160;send&#160;the&#160;VCS [ Canvas ](/) [ plot ](/) (s)
directly&#160;to&#160;the&#160;printer.  
Orientation&#160;can&#160;be&#160;either:&#160;'l'&#160;=&#160;landscape,&#160;or&#160;'p'&#160;=&#160;portrait.  
  
Note:&#160;VCS&#160;graphical&#160;displays&#160;can&#160;be&#160;printed&#160;only&#160;if&#160;the&#160;user&#160;customizes&#160;a
HARD_COPY  
file&#160;(included&#160;with&#160;the&#160;VCS&#160;software)&#160;for&#160;the&#160;home&#160;system.&#160;The&#160;path&#160;to&#160;the
HARD_COPY  
file&#160;must&#160;be:  
  
/$HOME/PCMDI_GRAPHICS/HARD_COPY  
  
where&#160;/$HOME&#160;denotes&#160;the&#160;user's&#160;home&#160;directory.  
  
  
For&#160;more&#160;information&#160;on&#160;the&#160;HARD_COPY&#160;file,&#160;see&#160;URL:  
  
[ http://www-pcmdi.llnl.gov/software/vcs/vcs_guidetoc.html#1.Setup
](/software/vcs/vcs_guidetoc.html)  
  
Example&#160;of&#160;Use:  
a=vcs.init()  
a. [ plot ](/) (array)  
a. [ printer ](/) ('printer_name')&#160;#&#160;Send [ plot ](/) (s)&#160;to&#160;postscript
printer `

 projectiongui  (self, gui_parent  =None  , projection  ='default'  ) 
     ` Function:&#160;projectiongui   
  
Description&#160;of&#160;Function:  
Run&#160;the&#160;VCS&#160;projection&#160;editor&#160;interface.  
  
The&#160;projectiongui&#160;command&#160;is&#160;used&#160;to&#160;bring&#160;up&#160;the&#160;VCS&#160;projection&#160;interface.
The&#160;interface  
is&#160;used&#160;to&#160;select,&#160;create,&#160;change,&#160;or&#160;remove&#160;projections.  
  
Example&#160;of&#160;Use:  
a=vcs.init()  
a. [ projectiongui ](/) () `

 pstogif  (self, filename, *opt) 
     ` Function:&#160;pstogif   
  
Description&#160;of&#160;Function:  
In&#160;some&#160;cases,&#160;the&#160;user&#160;may&#160;want&#160;to&#160;save&#160;the&#160;plot&#160;out&#160;as&#160;a&#160;gif&#160;image.&#160;This  
routine&#160;allows&#160;the&#160;user&#160;to&#160;convert&#160;a&#160;postscript&#160;file&#160;to&#160;a&#160;gif&#160;file.  
  
Example&#160;of&#160;Use:  
a=vcs.init()  
a. [ plot ](/) (array)  
a. [ pstogif ](/) ('filename.ps')&#160;&#160;&#160;&#160;&#160;&#160;&#160;#&#160;convert&#160;the&#160;postscript&#160;file&#160;to&#160;a&#160;gif
file&#160;(l=landscape)  
a. [ pstogif ](/) ('filename.ps','l')&#160;&#160;&#160;#&#160;convert&#160;the&#160;postscript&#160;file&#160;to&#160;a&#160;gif
file&#160;(l=landscape)  
a. [ pstogif ](/) ('filename.ps','p')&#160;&#160;&#160;#&#160;convert&#160;the&#160;postscript&#160;file&#160;to&#160;a&#160;gif
file&#160;(p=portrait) `

 raster  (self, *args) 
     ` Function:&#160;raster   
  
Description&#160;of&#160;Function:  
In&#160;some&#160;cases,&#160;the&#160;user&#160;may&#160;want&#160;to&#160;save&#160;the&#160;plot&#160;out&#160;as&#160;an&#160;raster&#160;image.&#160;This  
routine&#160;allows&#160;the&#160;user&#160;to&#160;save&#160;the&#160;VCS&#160;canvas&#160;output&#160;as&#160;a&#160;SUN&#160;raster&#160;file.  
This&#160;file&#160;can&#160;be&#160;converted&#160;to&#160;other&#160;raster&#160;formats&#160;with&#160;the&#160;aid&#160;of&#160;xv&#160;and
other  
such&#160;imaging&#160;tools&#160;found&#160;freely&#160;on&#160;the&#160;web.  
  
If&#160;no&#160;path/file&#160;name&#160;is&#160;given&#160;and&#160;no&#160;previously&#160;created&#160;raster&#160;file&#160;has&#160;been  
designated,&#160;then&#160;file  
  
/$HOME/PCMDI_GRAPHICS/default.ras  
  
will&#160;be&#160;used&#160;for&#160;storing&#160;raster&#160;images.&#160;However,&#160;if&#160;a&#160;previously&#160;created
raster  
file&#160;is&#160;designated,&#160;that&#160;file&#160;will&#160;be&#160;used&#160;for&#160;raster&#160;output.  
  
Example&#160;of&#160;Use:  
a=vcs.init()  
a. [ plot ](/) (array)  
a. [ raster ](/) ('example','a')&#160;&#160;&#160;#&#160;append&#160;raster&#160;image&#160;to&#160;existing&#160;file  
a. [ raster ](/) ('example','r')&#160;&#160;&#160;#&#160;overwrite&#160;existing&#160;raster&#160;file `

 removeP  (self, *args) 

 remove_display_name  (self, *args) 
     ` #############################################################################   
#&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#  
#&#160;VCS&#160;utility&#160;wrapper&#160;to&#160;remove&#160;the&#160;display&#160;names.&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#  
#&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#  
#############################################################################
`

 removeobject  (self, obj) 
     ` Function:&#160;remove   
  
Description&#160;of&#160;Function:  
The&#160;user&#160;has&#160;the&#160;ability&#160;to&#160;create&#160;primary&#160;and&#160;secondary&#160;class  
objects.&#160;The&#160;function&#160;allows&#160;the&#160;user&#160;to&#160;remove&#160;these&#160;objects  
from&#160;the&#160;appropriate&#160;class&#160;list.  
  
Note,&#160;To&#160;remove&#160;the&#160;object&#160;completely&#160;from&#160;Python,&#160;remember&#160;to  
use&#160;the&#160;"del"&#160;function.  
  
Also&#160;note,&#160;The&#160;user&#160;is&#160;not&#160;allowed&#160;to&#160;remove&#160;a&#160;"default"&#160;class  
object.  
  
Example&#160;of&#160;Use:  
a=vcs.init()  
line=a. [ getline ](/) ('red')&#160;&#160;&#160;&#160;&#160;&#160;&#160;#&#160;To&#160;Modify&#160;an&#160;existing&#160;line&#160;object  
iso=x. [ createisoline ](/) ('dean')&#160;#&#160;Create&#160;an&#160;instance&#160;of&#160;an&#160;isoline&#160;object  
...  
x.remove(line)&#160;&#160;&#160;&#160;&#160;&#160;#&#160;Removes&#160;line&#160;object&#160;from&#160;VCS&#160;list  
del&#160;line&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#&#160;Destroy&#160;instance&#160;"line",&#160;garbage&#160;collection  
x.remove(iso)&#160;&#160;&#160;&#160;&#160;&#160;&#160;#&#160;Remove&#160;isoline&#160;object&#160;from&#160;VCS&#160;list  
del&#160;iso&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#&#160;Destroy&#160;instance&#160;"iso",&#160;garbage&#160;collection `

 resetgrid  (self, *args) 
     ` Function:&#160;resetgrid   
  
Description&#160;of&#160;Function:  
Set&#160;the&#160;plotting&#160;region&#160;to&#160;default&#160;values.  
  
Example&#160;of&#160;Use:  
Not&#160;Working! `

 return_display_ON_num  (self, *args) 
     ` #############################################################################   
#&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#  
#&#160;VCS&#160;utility&#160;wrapper&#160;to&#160;return&#160;the&#160;number&#160;of&#160;displays&#160;that&#160;are&#160;"ON".&#160;&#160;&#160;&#160;&#160;&#160;&#160;#  
#&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#  
#############################################################################
`

 return_display_names  (self, *args) 
     ` #############################################################################   
#&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#  
#&#160;VCS&#160;utility&#160;wrapper&#160;to&#160;return&#160;the&#160;current&#160;display&#160;names.&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#  
#&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#  
#############################################################################
`

 saveinitialfile  (self) 
     ` Function:&#160;saveinitialfile&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#&#160;Save&#160;initial.attribute&#160;file   
  
Description&#160;of&#160;Function:  
At&#160;start-up,&#160;VCS&#160;reads&#160;a&#160;script&#160;file&#160;named&#160;initial.attributes&#160;that  
defines&#160;the&#160;initial&#160;appearance&#160;of&#160;the&#160;VCS&#160;Interface.&#160;Although&#160;not  
required&#160;to&#160;run&#160;VCS,&#160;this&#160;initial.attributes&#160;file&#160;contains&#160;many  
predefined&#160;settings&#160;to&#160;aid&#160;the&#160;beginning&#160;user&#160;of&#160;VCS.&#160;The&#160;path&#160;to  
the&#160;file&#160;must&#160;be:  
  
/$HOME/PCMDI_GRAPHICS/initial.attributes  
  
The&#160;contents&#160;of&#160;the&#160;initial.attributes&#160;file&#160;can&#160;be&#160;customized&#160;by  
the&#160;user.  
  
Example&#160;of&#160;Use:  
a=vcs.init()  
...  
  
a. [ saveinitialfile ](/) () `

 scatter  (self, *args, parms) 
     ` Function:&#160;scatter&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#&#160;Generate&#160;a&#160;scatter&#160;plot   
  
Description&#160;of&#160;Function:  
Generate&#160;a&#160;scatter&#160;plot&#160;given&#160;the&#160;data,&#160;scatter&#160;graphics&#160;method,&#160;and  
template.&#160;If&#160;no&#160;scatter&#160;class&#160;object&#160;is&#160;given,&#160;then&#160;the&#160;'default'&#160;scatter  
graphics&#160;method&#160;is&#160;used.&#160;Similarly,&#160;if&#160;no&#160;template&#160;class&#160;object&#160;is&#160;given,  
then&#160;the&#160;'default'&#160;template&#160;is&#160;used.  
  
Example&#160;of&#160;Use:  
a=vcs.init()  
a. [ show ](/) ('scatter')&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#&#160;Show&#160;all&#160;the&#160;existing&#160;scatter
graphics&#160;methods  
sct=a. [ getscatter ](/) ('quick')&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#&#160;Create&#160;instance&#160;of&#160;'quick'  
a. [ scatter ](/) (array,sct)&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#&#160;Plot&#160;array&#160;using&#160;specified&#160;sct
and&#160;default  
#&#160;&#160;&#160;&#160;&#160;&#160;&#160;template  
a. [ clear ](/) ()&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#&#160;Clear&#160;VCS&#160;canvas  
a. [ scatter ](/) (array,sct,template)&#160;&#160;&#160;&#160;&#160;&#160;&#160;#&#160;Plot&#160;array&#160;using&#160;specified&#160;sct
and&#160;template `

 scriptobject  (self, obj, script_filename  =None  , mode  =None  ) 
     ` Function:&#160;scriptobject&#160;&#160;&#160;&#160;&#160;&#160;&#160;#&#160;Script&#160;a&#160;single&#160;primary&#160;or&#160;secondary&#160;class&#160;object   
  
Description&#160;of&#160;Function:  
Save&#160;individual&#160;attributes&#160;sets&#160;(i.e.,&#160;individual&#160;primary&#160;class  
objects&#160;and/or&#160;secondary&#160;class&#160;objects).&#160;These&#160;attribute&#160;sets  
are&#160;saved&#160;in&#160;the&#160;user's&#160;current&#160;directory.  
  
Note:&#160;If&#160;the&#160;the&#160;filename&#160;has&#160;a&#160;".py"&#160;at&#160;the&#160;end,&#160;it&#160;will&#160;produce&#160;a  
Python&#160;script.&#160;If&#160;the&#160;filename&#160;has&#160;a&#160;".scr"&#160;at&#160;the&#160;end,&#160;it&#160;will  
produce&#160;a&#160;VCS&#160;script.&#160;If&#160;neither&#160;extensions&#160;are&#160;give,&#160;then&#160;by  
default&#160;a&#160;Python&#160;script&#160;will&#160;be&#160;produced.  
  
Note:&#160;Mode&#160;is&#160;either&#160;"w"&#160;for&#160;replace&#160;or&#160;"a"&#160;for&#160;append.  
  
Note:&#160;VCS&#160;does&#160;not&#160;allow&#160;the&#160;modification&#160;of&#160;`default'&#160;attribute&#160;sets,  
it&#160;will&#160;not&#160;allow&#160;them&#160;to&#160;be&#160;saved&#160;as&#160;individual&#160;script&#160;files.  
However,&#160;a&#160;`default'&#160;attribute&#160;set&#160;that&#160;has&#160;been&#160;copied&#160;under&#160;a  
different&#160;name&#160;can&#160;be&#160;saved&#160;as&#160;a&#160;script&#160;file.  
  
Example&#160;of&#160;Use:  
a=vcs.init()  
l=a. [ getline ](/) ('red')&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#&#160;To&#160;Modify&#160;an&#160;existing&#160;line&#160;object  
i=x. [ createisoline ](/) ('dean')&#160;&#160;#&#160;Create&#160;an&#160;instance&#160;of&#160;default&#160;isoline
object  
...  
x.scriptsingle(l,'line.scr','w')&#160;#&#160;Save&#160;line&#160;object&#160;as&#160;a&#160;VCS&#160;file&#160;'line.scr'  
x.scriptsingle(i,'isoline.py')&#160;&#160;&#160;#&#160;Save&#160;isoline&#160;object&#160;as&#160;a&#160;Python&#160;file
'isoline.py' `

 scriptrun  (self, *args) 
     ` #############################################################################   
#&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#  
#&#160;Import&#160;old&#160;VCS&#160;file&#160;script&#160;commands&#160;into&#160;CDAT.&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#  
#&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#  
#############################################################################
`

 scriptstate  (self, script_name) 
     ` Function:&#160;scriptstate&#160;&#160;&#160;&#160;&#160;&#160;&#160;#&#160;Save&#160;state&#160;of&#160;VCS   
  
Description&#160;of&#160;Function:  
The&#160;VCS&#160;scripting&#160;capability&#160;serves&#160;many&#160;purposes.&#160;It&#160;allows&#160;one&#160;to&#160;save&#160;the  
system&#160;state&#160;for&#160;replay&#160;in&#160;a&#160;later&#160;session;&#160;to&#160;save&#160;primary&#160;and&#160;secondary  
element&#160;attributes&#160;for&#160;use&#160;in&#160;later&#160;visual&#160;presentations;&#160;to&#160;save&#160;a&#160;sequence  
of&#160;interactive&#160;operations&#160;for&#160;replay;&#160;or&#160;to&#160;recover&#160;from&#160;a&#160;system&#160;failure.  
  
Example&#160;of&#160;Use:  
a=vcs.init()  
...  
  
a. [ scriptstate ](/) (script_filename) `

 set  (self, *args) 
     ` Function:&#160;set   
  
Description&#160;of&#160;Function:  
Set&#160;the&#160;default&#160;VCS&#160;primary&#160;class&#160;objects:&#160;template&#160;and&#160;graphics&#160;methods.  
Keep&#160;in&#160;mind&#160;the&#160;template,&#160;determines&#160;the&#160;appearance&#160;of&#160;each&#160;graphics&#160;segment;  
the&#160;graphic&#160;method&#160;specifies&#160;the&#160;display&#160;technique;&#160;and&#160;the&#160;data&#160;defines&#160;what  
is&#160;to&#160;be&#160;displayed.&#160;Note,&#160;the&#160;data&#160;cannot&#160;be&#160;set&#160;with&#160;this&#160;function.  
  
Example&#160;of&#160;Use:  
a=vcs.init()  
a. [ set ](/) ('isofill','quick')&#160;#&#160;Changes&#160;the&#160;default&#160;graphics&#160;method&#160;to
Isofill:&#160;'quick'  
a. [ plot ](/) (array) `

 setcolorcell  (self, *args) 
     ` Function:&#160;setcolorcell   
  
Description&#160;of&#160;Function:  
Set&#160;a&#160;individual&#160;color&#160;cell&#160;in&#160;the&#160;active&#160;colormap.&#160;If&#160;default&#160;is  
the&#160;active&#160;colormap,&#160;then&#160;return&#160;an&#160;error&#160;string.  
  
If&#160;the&#160;the&#160;visul&#160;display&#160;is&#160;16-bit,&#160;24-bit,&#160;or&#160;32-bit&#160;TrueColor,&#160;then&#160;a
redrawing  
of&#160;the&#160;VCS [ Canvas ](/) is&#160;made&#160;evertime&#160;the&#160;color&#160;cell&#160;is&#160;changed.  
  
Note,&#160;the&#160;user&#160;can&#160;only&#160;change&#160;color&#160;cells&#160;0&#160;through&#160;239&#160;and&#160;R,G,B  
value&#160;must&#160;range&#160;from&#160;0&#160;to&#160;100.&#160;Where&#160;0&#160;represents&#160;no&#160;color&#160;intensity  
and&#160;100&#160;is&#160;the&#160;greatest&#160;color&#160;intensity.  
  
Example&#160;of&#160;Use:  
a=vcs.init()  
a. [ plot ](/) (array,'default','isofill','quick')  
a. [ setcolormap ](/) ("AMIP")  
a. [ setcolorcell ](/) (11,0,0,0)  
a. [ setcolorcell ](/) (21,100,0,0)  
a. [ setcolorcell ](/) (31,0,100,0)  
a. [ setcolorcell ](/) (41,0,0,100)  
a. [ setcolorcell ](/) (51,100,100,100)  
a. [ setcolorcell ](/) (61,70,70,70) `

 setcolormap  (self, *args) 
     ` Function:&#160;setcolormap   
  
Description&#160;of&#160;Function:  
It&#160;is&#160;necessary&#160;to&#160;change&#160;the&#160;colormap.&#160;This&#160;routine&#160;will&#160;change&#160;the&#160;VCS  
color&#160;map.  
  
If&#160;the&#160;the&#160;visul&#160;display&#160;is&#160;16-bit,&#160;24-bit,&#160;or&#160;32-bit&#160;TrueColor,&#160;then&#160;a
redrawing  
of&#160;the&#160;VCS [ Canvas ](/) is&#160;made&#160;evertime&#160;the&#160;colormap&#160;is&#160;changed.  
  
Example&#160;of&#160;Use:  
a=vcs.init()  
a. [ plot ](/) (array,'default','isofill','quick')  
a. [ setcolormap ](/) ("AMIP") `

 setcontinentstype  (self, *args) 
     ` Function:&#160;setcontinentstype   
  
Description&#160;of&#160;Function:  
One&#160;has&#160;the&#160;option&#160;of&#160;using&#160;continental&#160;maps&#160;that&#160;are&#160;predefined&#160;or&#160;that  
are&#160;user-defined.&#160;Predefined&#160;continental&#160;maps&#160;are&#160;either&#160;internal&#160;to&#160;VCS  
or&#160;are&#160;specified&#160;by&#160;external&#160;files.&#160;User-defined&#160;continental&#160;maps&#160;are  
specified&#160;by&#160;additional&#160;external&#160;files&#160;that&#160;must&#160;be&#160;read&#160;as&#160;input.  
  
The&#160;continents-type&#160;values&#160;are&#160;integers&#160;ranging&#160;from&#160;0&#160;to&#160;11,&#160;where:  
0&#160;signifies&#160;"No&#160;Continents"  
1&#160;signifies&#160;"Fine&#160;Continents"  
2&#160;signifies&#160;"Coarse&#160;Continents"  
3&#160;signifies&#160;"United&#160;States"&#160;(with&#160;"Fine&#160;Continents")  
4&#160;signifies&#160;"Political&#160;Borders"&#160;(with&#160;"Fine&#160;Continents")  
5&#160;signifies&#160;"Rivers"&#160;(with&#160;"Fine&#160;Continents")  
  
Values&#160;6&#160;through&#160;11&#160;signify&#160;the&#160;line&#160;type&#160;defined&#160;by&#160;the&#160;files  
data_continent_other7&#160;through&#160;data_continent_other12.  
  
Example&#160;of&#160;Use:  
a=vcs.init()  
a. [ setcontinentstype ](/) (3)  
a. [ plot ](/) (array,'default','isofill','quick') `

 show  (self, *args) 
     ` Function:&#160;show   
  
Description&#160;of&#160;Function:  
Show&#160;the&#160;list&#160;of&#160;VCS&#160;primary&#160;and&#160;secondary&#160;class&#160;objects.  
  
Example&#160;of&#160;Use:  
a=vcs.init()  
a. [ show ](/) ('boxfill')  
a. [ show ](/) ('isofill')  
a. [ show ](/) ('line')  
a. [ show ](/) ('marker')  
a. [ show ](/) ('text') `

 showbg  (self, *args) 
     ` Function:&#160;showbg   
  
Description&#160;of&#160;Function:  
This&#160;function&#160;displays&#160;graphics&#160;segments,&#160;which&#160;are&#160;currently&#160;stored&#160;in&#160;the
frame&#160;buffer,  
on&#160;the&#160;VCS [ Canvas ](/) .&#160;That&#160;is,&#160;if&#160;the&#160;plot&#160;function&#160;was&#160;called&#160;with&#160;the
option&#160;bg&#160;=&#160;1&#160;(i.e.,  
background&#160;mode),&#160;then&#160;the&#160;plot&#160;is&#160;produced&#160;in&#160;the&#160;frame&#160;buffer&#160;and&#160;not
visible&#160;to&#160;the  
user.&#160;In&#160;order&#160;to&#160;view&#160;&#160;the&#160;graphics&#160;segments,&#160;this&#160;function&#160;will&#160;copy&#160;the
contents&#160;of  
the&#160;frame&#160;buffer&#160;to&#160;the&#160;VCS [ Canvas ](/) ,&#160;where&#160;the&#160;graphics&#160;can&#160;be&#160;viewed
by&#160;the&#160;user.  
  
Example&#160;of&#160;Use:  
a=vcs.init()  
a. [ plot ](/) (array,&#160;bg=1)  
x. [ showbg ](/) () `

 syncP  (self, *args) 

 taylordiagram  (self, *args, parms) 
     ` Function:&#160;taylordiagram&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#&#160;Generate&#160;an&#160;taylordiagram&#160;plot   
  
Description&#160;of&#160;Function:  
Generate&#160;a&#160;taylordiagram&#160;plot&#160;given&#160;the&#160;data,&#160;taylordiagram&#160;graphics&#160;method,
and  
template.&#160;If&#160;no&#160;taylordiagram&#160;class&#160;object&#160;is&#160;given,&#160;then&#160;the&#160;'default'
taylordiagram  
graphics&#160;method&#160;is&#160;used.&#160;Similarly,&#160;if&#160;no&#160;template&#160;class&#160;object&#160;is&#160;given,  
then&#160;the&#160;'default'&#160;template&#160;is&#160;used.  
  
Example&#160;of&#160;Use:  
a=vcs.init()  
a. [ show ](/) ('taylordiagram')&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#&#160;Show&#160;all&#160;the&#160;existing
taylordiagram&#160;graphics&#160;methods  
td=a. [ gettaylordiagram ](/) ()&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#&#160;Create&#160;instance&#160;of
'default'  
a. [ taylordiagram ](/) (array,td)&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#&#160;Plot&#160;array&#160;using
specified&#160;iso&#160;and&#160;default  
#&#160;&#160;&#160;&#160;&#160;&#160;&#160;template  
a. [ clear ](/) ()&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#&#160;Clear&#160;VCS&#160;canvas  
a. [ taylordiagram ](/) (array,td,template)&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#&#160;Plot&#160;array&#160;using
specified&#160;iso&#160;and&#160;template `

 templateeditor  (self, template_name  ='default'  , template_orig_name  ='default'  , plot  =None  , gui_parent  =None  ) 
     ` #############################################################################   
#&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#  
#&#160;Template&#160;Editor&#160;Graphical&#160;User&#160;Interface&#160;wrapper&#160;for&#160;VCS.&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#  
#&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#  
#############################################################################
`

 text  = [ textcombined ](/) (self, *args, parms) 

 textcombined  (self, *args, parms) 
     ` Function:&#160;text&#160;or&#160;textcombined&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#&#160;Generate&#160;a&#160;textcombined&#160;plot   
  
Description&#160;of&#160;Function:  
Plot&#160;a&#160;textcombined&#160;segment&#160;on&#160;the&#160;Vcs [ Canvas ](/) .&#160;If&#160;no&#160;textcombined
class  
object&#160;is&#160;given,&#160;then&#160;an&#160;error&#160;will&#160;be&#160;returned.  
  
Example&#160;of&#160;Use:  
a=vcs.init()  
a. [ show ](/) ('texttable')&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#&#160;Show&#160;all&#160;the&#160;existing&#160;texttable
objects  
a. [ show ](/) ('textorientation')&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#&#160;Show&#160;all&#160;the&#160;existing
textorientation&#160;objects  
tt=a. [ gettext ](/) ('std','7left')&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#&#160;Create&#160;instance&#160;of&#160;'std'&#160;and
'7left'  
tt.string&#160;=&#160;'Text1'&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#&#160;Show&#160;the&#160;string&#160;"Text1"&#160;on&#160;the&#160;VCS [
Canvas ](/)  
tt.font=2&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#&#160;Set&#160;the&#160;text&#160;size  
tt.color&#160;=&#160;242&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#&#160;Set&#160;the&#160;text&#160;color  
tt.angle&#160;=&#160;45&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#&#160;Set&#160;the&#160;text&#160;angle  
tt.x=[[0.0,2.0,2.0,0.0,0.0],&#160;[0.5,1.5]]&#160;#&#160;Set&#160;the&#160;x&#160;value&#160;points  
tt.y=[[0.0,0.0,2.0,2.0,0.0],&#160;[1.0,1.0]]&#160;#&#160;Set&#160;the&#160;y&#160;value&#160;points  
a. [ text ](/) (tt)&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#&#160;Plot&#160;using&#160;specified&#160;text
object  
  
Optionally&#160;you&#160;can&#160;pass&#160;a&#160;string,&#160;the&#160;coordinates&#160;and&#160;any&#160;keyword  
Example:  
x. [ plot ](/) ('Hi',.5,.5,color=241,angle=45) `

 update  (self, *args) 
     ` Function:&#160;update&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#&#160;Update&#160;the&#160;VCS [ Canvas ](/) .   
  
Description&#160;of&#160;Function:  
If&#160;a&#160;series&#160;of&#160;commands&#160;are&#160;given&#160;to&#160;VCS&#160;and&#160;the [ Canvas ](/) Mode&#160;is  
set&#160;to&#160;manual,&#160;then&#160;use&#160;this&#160;function&#160;to&#160;update&#160;the [ plot ](/) (s)  
manually.  
  
Example&#160;of&#160;Use:  
...  
  
a=vcs.init()  
a. [ plot ](/) (s,'default','boxfill','quick')  
a.mode&#160;=&#160;0&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#&#160;Go&#160;to&#160;manual&#160;mode  
box=x. [ getboxfill ](/) ('quick')  
box.color_1=100  
box.xticlabels('lon30','lon30')  
box.xticlabels('','')  
box.datawc(1e20,1e20,1e20,1e20)  
box.datawc(-45.0,&#160;45.0,&#160;-90.0,&#160;90.0)  
  
a. [ update ](/) ()&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#&#160;Update&#160;the&#160;changes&#160;manually
`

 updateVCSsegments  (self, *args) 
     ` #############################################################################   
#&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#  
#&#160;Touch&#160;all&#160;segements&#160;displayed&#160;on&#160;the&#160;VCS [ Canvas ](/) .
#  
#&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#  
#############################################################################
`

 updateorientation  (self, *args) 
     ` Example&#160;of&#160;Use:   
a=vcs.init()  
x. [ updateorientation ](/) () `

 vector  (self, *args, parms) 
     ` Function:&#160;vector&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#&#160;Generate&#160;a&#160;vector&#160;plot   
  
Description&#160;of&#160;Function:  
Generate&#160;a&#160;vector&#160;plot&#160;given&#160;the&#160;data,&#160;vector&#160;graphics&#160;method,&#160;and  
template.&#160;If&#160;no&#160;vector&#160;class&#160;object&#160;is&#160;given,&#160;then&#160;the&#160;'default'&#160;vector  
graphics&#160;method&#160;is&#160;used.&#160;Similarly,&#160;if&#160;no&#160;template&#160;class&#160;object&#160;is&#160;given,  
then&#160;the&#160;'default'&#160;template&#160;is&#160;used.  
  
Example&#160;of&#160;Use:  
a=vcs.init()  
a. [ show ](/) ('vector')&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#&#160;Show&#160;all&#160;the&#160;existing&#160;vector
graphics&#160;methods  
vec=a. [ getvector ](/) ('quick')&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#&#160;Create&#160;instance&#160;of&#160;'quick'  
a. [ vector ](/) (array,vec)&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#&#160;Plot&#160;array&#160;using&#160;specified&#160;vec
and&#160;default  
#&#160;&#160;&#160;&#160;&#160;&#160;&#160;template  
a. [ clear ](/) ()&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#&#160;Clear&#160;VCS&#160;canvas  
a. [ vector ](/) (array,vec,template)&#160;&#160;&#160;&#160;&#160;&#160;&#160;#&#160;Plot&#160;array&#160;using&#160;specified&#160;vec
and&#160;template `

 xvsy  (self, *args, parms) 
     ` Function:&#160;xvsy&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#&#160;Generate&#160;a&#160;XvsY&#160;plot   
  
Description&#160;of&#160;Function:  
Generate&#160;a&#160;XvsY&#160;plot&#160;given&#160;the&#160;data,&#160;XvsY&#160;graphics&#160;method,&#160;and  
template.&#160;If&#160;no&#160;XvsY&#160;class&#160;object&#160;is&#160;given,&#160;then&#160;the&#160;'default'&#160;XvsY  
graphics&#160;method&#160;is&#160;used.&#160;Similarly,&#160;if&#160;no&#160;template&#160;class&#160;object&#160;is&#160;given,  
then&#160;the&#160;'default'&#160;template&#160;is&#160;used.  
  
Example&#160;of&#160;Use:  
a=vcs.init()  
a. [ show ](/) ('xvsy')&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#&#160;Show&#160;all&#160;the&#160;existing&#160;XvsY
graphics&#160;methods  
xy=a. [ getxvsy ](/) ('quick')&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#&#160;Create&#160;instance&#160;of&#160;'quick'  
a. [ xvsy ](/) (array,xy)&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#&#160;Plot&#160;array&#160;using&#160;specified&#160;xy&#160;and
default  
#&#160;&#160;&#160;&#160;&#160;&#160;&#160;template  
a. [ clear ](/) ()&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#&#160;Clear&#160;VCS&#160;canvas  
a. [ xvsy ](/) (array,xy,template)&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#&#160;Plot&#160;array&#160;using&#160;specified&#160;xy&#160;and
template `

 xyvsy  (self, *args, parms) 
     ` Function:&#160;xyvsy&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#&#160;Generate&#160;a&#160;Xyvsy&#160;plot   
  
Description&#160;of&#160;Function:  
Generate&#160;a&#160;Xyvsy&#160;plot&#160;given&#160;the&#160;data,&#160;Xyvsy&#160;graphics&#160;method,&#160;and  
template.&#160;If&#160;no&#160;Xyvsy&#160;class&#160;object&#160;is&#160;given,&#160;then&#160;the&#160;'default'&#160;Xyvsy  
graphics&#160;method&#160;is&#160;used.&#160;Simerly,&#160;if&#160;no&#160;template&#160;class&#160;object&#160;is&#160;given,  
then&#160;the&#160;'default'&#160;template&#160;is&#160;used.  
  
Example&#160;of&#160;Use:  
a=vcs.init()  
a. [ show ](/) ('xyvsy')&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#&#160;Show&#160;all&#160;the&#160;existing&#160;Xyvsy
graphics&#160;methods  
xyy=a. [ getxyvsy ](/) ('quick')&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#&#160;Create&#160;instance&#160;of&#160;'quick'  
a. [ xyvsy ](/) (array,xyy)&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#&#160;Plot&#160;array&#160;using&#160;specified&#160;xyy
and&#160;default  
#&#160;&#160;&#160;&#160;&#160;&#160;&#160;template  
a. [ clear ](/) ()&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#&#160;Clear&#160;VCS&#160;canvas  
a. [ xyvsy ](/) (array,xyy,template)&#160;&#160;&#160;&#160;&#160;&#160;&#160;#&#160;Plot&#160;array&#160;using&#160;specified&#160;xyy
and&#160;template `

 yxvsx  (self, *args, parms) 
     ` Function:&#160;yxvsx&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#&#160;Generate&#160;a&#160;Yxvsx&#160;plot   
  
Description&#160;of&#160;Function:  
Generate&#160;a&#160;Yxvsx&#160;plot&#160;given&#160;the&#160;data,&#160;Yxvsx&#160;graphics&#160;method,&#160;and  
template.&#160;If&#160;no&#160;Yxvsx&#160;class&#160;object&#160;is&#160;given,&#160;then&#160;the&#160;'default'&#160;Yxvsx  
graphics&#160;method&#160;is&#160;used.&#160;Simerly,&#160;if&#160;no&#160;template&#160;class&#160;object&#160;is&#160;given,  
then&#160;the&#160;'default'&#160;template&#160;is&#160;used.  
  
Example&#160;of&#160;Use:  
a=vcs.init()  
a. [ show ](/) ('yxvsx')&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#&#160;Show&#160;all&#160;the&#160;existing&#160;Yxvsx
graphics&#160;methods  
yxx=a. [ getyxvsx ](/) ('quick')&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#&#160;Create&#160;instance&#160;of&#160;'quick'  
a. [ yxvsx ](/) (array,yxx)&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#&#160;Plot&#160;array&#160;using&#160;specified&#160;yxx
and&#160;default  
#&#160;&#160;&#160;&#160;&#160;&#160;&#160;template  
a. [ clear ](/) ()&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#&#160;Clear&#160;VCS&#160;canvas  
a. [ yxvsx ](/) (array,yxx,template)&#160;&#160;&#160;&#160;&#160;&#160;&#160;#&#160;Plot&#160;array&#160;using&#160;specified&#160;yxx
and&#160;template `

  
class  animate_obj 

` `

` Function:&#160;animate  
  
Description&#160;of&#160;Function:  
Animate&#160;the&#160;contents&#160;of&#160;the&#160;VCS [ Canvas ](/) .&#160;The&#160;animation&#160;can&#160;also&#160;be
controlled&#160;from  
the&#160;animation&#160;GUI.&#160;(See&#160;VCDAT&#160;for&#160;more&#160;details.)  
  
See&#160;the&#160;animation&#160;GUI&#160;documenation&#160;located&#160;at&#160;URL:  
[ http://www-pcmdi.llnl.gov/software/vcs ](/software/vcs)  
  
Example&#160;of&#160;Use:  
a=vcs.init()  
a.plot(array,'default','isofill','quick')  
a.animate()  
`

Methods defined here:  

 __init__  (self, vcs_self) 
     ` ##############################################################################   
#&#160;Initialize&#160;the&#160;animation&#160;flags&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#  
##############################################################################
`

 close  (self) 
     ` ##############################################################################   
#&#160;Close&#160;the&#160;animate&#160;session&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#  
##############################################################################
`

 create  (self, parent  =None  , min  =None  , max  =None  , save_file  =None  , thread_it  =1  ) 
     ` ##############################################################################   
#&#160;Create&#160;the&#160;animation&#160;images.&#160;If&#160;min&#160;or&#160;max&#160;is&#160;None,&#160;then&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#  
#&#160;the&#160;animator&#160;will&#160;find&#160;the&#160;min&#160;and&#160;max&#160;values&#160;from&#160;the&#160;dataset.&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#  
#&#160;If&#160;min&#160;and&#160;max&#160;are&#160;set&#160;to&#160;1e20,&#160;then&#160;no&#160;min&#160;and&#160;max&#160;animation&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#  
#&#160;value&#160;is&#160;used&#160;(i.e.,&#160;each&#160;animation&#160;frame&#160;will&#160;have&#160;different&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#  
#&#160;min&#160;and&#160;max&#160;values.&#160;If&#160;min&#160;and&#160;max&#160;are&#160;set&#160;by&#160;the&#160;user,&#160;then&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#  
#&#160;these&#160;values&#160;are&#160;used&#160;for&#160;the&#160;animation&#160;min&#160;and&#160;max.&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#  
#&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#  
#&#160;If&#160;you&#160;are&#160;running&#160;animation&#160;from&#160;a&#160;program,&#160;set&#160;thread_it&#160;to&#160;0.&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#  
#&#160;This&#160;will&#160;cause&#160;the&#160;Python&#160;program&#160;to&#160;wait&#160;for&#160;the&#160;create&#160;function&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#  
#&#160;to&#160;finish&#160;before&#160;moving&#160;onto&#160;the&#160;next&#160;command&#160;line.&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#  
##############################################################################
`

 creating_animation_flg  (self) 
     ` ##############################################################################   
#&#160;Creating&#160;animation&#160;flag&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#  
##############################################################################
`

 direction  (self, value  =1  ) 
     ` ##############################################################################   
#&#160;Set&#160;the&#160;direction&#160;of&#160;the&#160;animation:&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#  
#&#160;Value&#160;1&#160;->&#160;forward,&#160;2&#160;->&#160;backward&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#  
##############################################################################
`

 frame  (self, value  =1  ) 
     ` ##############################################################################   
#&#160;View&#160;the&#160;specified&#160;animation&#160;frame&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#  
##############################################################################
`

 gui  (self, gui_parent  =None  , transient  =0  ) 
     ` ##############################################################################   
#&#160;Pop&#160;up&#160;the&#160;animation&#160;GUI&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#  
##############################################################################
`

 horizontal  (self, value  =0  ) 
     ` ##############################################################################   
#&#160;Pan&#160;the&#160;zoomed&#160;animation&#160;or&#160;frame&#160;in&#160;the&#160;x&#160;(or&#160;horizontal)&#160;direction&#160;&#160;&#160;&#160;&#160;&#160;&#160;#  
#&#160;Value&#160;ranges&#160;from&#160;-100&#160;to&#160;100&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#  
##############################################################################
`

 load_from_file  (self, parent  =None  , load_file  =None  , thread_it  =1  ) 
     ` ##############################################################################   
#&#160;Load&#160;animation&#160;from&#160;a&#160;stored&#160;Raster&#160;file.&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#  
##############################################################################
`

 mode  (self, value  =1  ) 
     ` ##############################################################################   
#&#160;Mode&#160;sets&#160;the&#160;cycle,&#160;forth&#160;and&#160;back,&#160;or&#160;animate&#160;once&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#  
#&#160;Value:&#160;1&#160;->&#160;cycle,&#160;2&#160;->&#160;animate&#160;once,&#160;and&#160;3&#160;->&#160;forth&#160;and&#160;back&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#  
##############################################################################
`

 number_of_frames  (self) 
     ` ##############################################################################   
#&#160;Return&#160;the&#160;number&#160;of&#160;animate&#160;frames&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#  
##############################################################################
`

 pause  (self, value  =1  ) 
     ` ##############################################################################   
#&#160;Pause&#160;the&#160;animation&#160;loop&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#  
#&#160;Value&#160;ranges&#160;from&#160;0&#160;to&#160;100&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#  
##############################################################################
`

 restore_min_max  (self) 
     ` ##############################################################################   
#&#160;Restore&#160;min&#160;and&#160;max&#160;values&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#  
##############################################################################
`

 run  (self) 
     ` ##############################################################################   
#&#160;Run&#160;or&#160;start&#160;the&#160;animation&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#  
##############################################################################
`

 run_animation_flg  (self) 
     ` ##############################################################################   
#&#160;Run&#160;animation&#160;flag&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#  
##############################################################################
`

 save_original_min_max  (self) 
     ` ##############################################################################   
#&#160;Save&#160;original&#160;min&#160;and&#160;max&#160;values&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#  
##############################################################################
`

 set_animation_min_max  (self, min, max, i) 
     ` ##############################################################################   
#&#160;Set&#160;the&#160;animation&#160;min&#160;and&#160;max&#160;values&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#  
##############################################################################
`

 stop  (self) 
     ` ##############################################################################   
#&#160;Stop&#160;the&#160;animation&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#  
##############################################################################
`

 update_animate_display_list  (self) 
     ` ##############################################################################   
#&#160;Update&#160;the&#160;animation&#160;display&#160;list&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#  
##############################################################################
`

 vertical  (self, value  =0  ) 
     ` ##############################################################################   
#&#160;Pan&#160;the&#160;zoomed&#160;animation&#160;or&#160;frame&#160;in&#160;the&#160;y&#160;(or&#160;vertical)&#160;direction&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#  
#&#160;Value&#160;ranges&#160;from&#160;-100&#160;to&#160;100&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#  
##############################################################################
`

 zoom  (self, value  =1  ) 
     ` ##############################################################################   
#&#160;Zoom&#160;in&#160;on&#160;the&#160;animation&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#  
#&#160;Value&#160;ranges&#160;from&#160;0&#160;to&#160;20&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#  
##############################################################################
`

  
 Functions 

` `

 change_date_time  (tv, number) 
     ` #############################################################################   
#&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#  
#&#160;Primarily&#160;used&#160;for&#160;reseting&#160;the&#160;animation&#160;date&#160;and&#160;time&#160;string.&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#  
#&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#  
#############################################################################
`

 dictionarytovcslist  (dictionary, name) 

 finish_queued_X_server_requests  (self) 
     ` Wait&#160;for&#160;the&#160;X&#160;server&#160;to&#160;execute&#160;all&#160;pending&#160;events.   
  
If&#160;working&#160;with&#160;C&#160;routines,&#160;then&#160;use&#160;BLOCK_X_SERVER  
found&#160;in&#160;the&#160;VCS&#160;module&#160;routine&#160;to&#160;stop&#160;the&#160;X&#160;server  
from&#160;continuing.&#160;Thus,&#160;eliminating&#160;the&#160;asynchronous  
errors. `

  
 Data 

` `

 StringTypes  = (<type 'str'>, <type 'unicode'>)   
 called_initial_attributes_flg  = 0 

* * *

UCRL-WEB-213937 | [ Privacy & Legal Notice ](/disclaimer.html)

[ webmaster@pcmdi.llnl.gov ](/webmaster@pcmdi.llnl.gov)

[ ![Powered by Plone](media/plone_powered.gif) ](/)

