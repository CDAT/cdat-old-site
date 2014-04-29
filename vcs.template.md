---
layout: default
title:
---

 [ Skip to content. ](/cdat/source/api-reference/vcs.template.html) | [ Skip to
navigation ](/cdat/source/api-reference/vcs.template.html)

Search Site

[ Advanced Search&#8230; ](/search_form)

#  [ PCMDI Software Portal ](/)

#####  Sections

  * [ Home ](/)

#####  Personal tools

  * [ Log in ](/login_form)

You are here:  [ Home ](/) -> [ CDAT ](/cdat) -> [ Source Code ](/cdat/source)
-> [ API Reference ](/cdat/source/api-reference) -> Python: module
vcs.template

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

        * [ Python: module vcs.template ](/cdat/source/api-reference/vcs.template.html)

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

  * [ ![Send this page to somebody](media/mail_icon.gif) ](/cdat/source/api-reference/vcs.template.html/sendto_form)
  * [ ![Print this page](media/print_icon.gif) ](/this.print\(\))

#  Python: module vcs.template

  
  
 [ vcs  ](/vcs.html) .template 
[ index ](/)  

` #&#160;Template&#160;( [ P ](/) )&#160;module `

  
 Modules 

` `

[ Numeric ](/Numeric.html)  
[ RandomArray ](/RandomArray.html)  

[ vcs._vcs ](/vcs._vcs.html)  
[ copy ](/copy.html)  

[ vcs.queries ](/vcs.queries.html)  
[ vcs ](/vcs.html)  

  
 Classes 

` `

[ P ](/vcs.template.html)

  
class  P 

` `

` Class: [ P ](/) #&#160;Template  
  
Description&#160;of [ P ](/) Class:  
The&#160;template&#160;primary&#160;method&#160;( [ P ](/) )&#160;determines&#160;the&#160;location&#160;of&#160;each
picture  
segment,&#160;the&#160;space&#160;to&#160;be&#160;allocated&#160;to&#160;it,&#160;and&#160;related&#160;properties&#160;relevant  
to&#160;its&#160;display.  
  
Other&#160;Useful&#160;Functions:  
a.show('template')&#160;&#160;&#160;&#160;&#160;&#160;&#160;#&#160;Show&#160;predefined&#160;templates  
a.show('texttable')&#160;&#160;&#160;&#160;&#160;&#160;#&#160;Show&#160;predefined&#160;text&#160;table&#160;methods  
a.show('textorientation')&#160;&#160;&#160;#&#160;Show&#160;predefined&#160;text&#160;orientation&#160;methods  
a.show('line')&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#&#160;Show&#160;predefined&#160;line&#160;methods  
a.listelements('template')&#160;#&#160;Show&#160;templates&#160;as&#160;a&#160;Python&#160;list  
a.update()&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#&#160;Updates&#160;the&#160;VCS&#160;Canvas&#160;at&#160;user's&#160;request  
a.mode=1,&#160;or&#160;0&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#&#160;If&#160;1,&#160;then&#160;automatic&#160;update,&#160;else&#160;if  
0,&#160;then&#160;use&#160;the&#160;update&#160;function&#160;to  
update&#160;the&#160;VCS&#160;Canvas.  
  
Example&#160;of&#160;Use:  
a=vcs.init()  
To&#160;Create&#160;a&#160;new&#160;instance&#160;of&#160;boxfill&#160;use:  
box=a.createboxfill('new','quick')&#160;#&#160;Copies&#160;content&#160;of&#160;'quick'&#160;to&#160;'new'  
box=a.createboxfill('new')&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#&#160;Copies&#160;content&#160;of&#160;'default'&#160;to&#160;'new'  
  
To&#160;Modify&#160;an&#160;existing&#160;boxfill&#160;use:  
box=a.getboxfill('AMIP_psl')  
  
To&#160;Create&#160;a&#160;new&#160;instance&#160;of&#160;template&#160;use:  
tpl=a.createtemplate('new','AMIP')&#160;&#160;#&#160;Copies&#160;content&#160;of&#160;'AMIP'&#160;to&#160;'new'  
tpl=a.createtemplate('new')&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#&#160;Copies&#160;content&#160;of&#160;'default'&#160;to&#160;'new'  
  
To&#160;Modify&#160;an&#160;existing&#160;template&#160;use:  
tpl=a.gettemplate('AMIP')  
`

Methods defined here:  

 __init__  (self, parent, Pic_name  =None  , Pic_name_src  ='default'  , createP  =0  ) 
     ` ###########################################################################   
#&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#  
#&#160;Initialize&#160;the&#160;template&#160;attributes.&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#  
#&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#  
########################################################################### `

 __setattr__  (self, name, value) 

 drawColorBar  (self, colors, levels, legend  =None  , ext_1  ='n'  , ext_2  ='n'  , x  =None  , bg  =0  , priority  =None  ) 
     ` This&#160;function,&#160;draws&#160;the&#160;colorbar,&#160;it&#160;needs:   
colors&#160;:&#160;The&#160;colors&#160;to&#160;be&#160;plotted  
levels&#160;:&#160;The&#160;levels&#160;that&#160;each&#160;color&#160;represent  
legend&#160;:&#160;To&#160;overwrite,&#160;saying&#160;just&#160;draw&#160;box&#160;at&#160;certain&#160;values&#160;and&#160;display&#160;some
specific&#160;text&#160;instead&#160;of&#160;the&#160;value  
ext_1&#160;and&#160;ext_2:&#160;to&#160;draw&#160;the&#160;arrows  
x&#160;:&#160;the&#160;canvas&#160;where&#160;to&#160;plot&#160;it  
bg:&#160;background&#160;mode&#160;? `

 drawTicks  (self, slab, gm, x, axis, number, vp, wc, bg  =0  ) 
     ` Draws&#160;the&#160;ticks&#160;for&#160;the&#160;axis&#160;x&#160;number&#160;number   
using&#160;the&#160;label&#160;passed&#160;by&#160;the&#160;graphic&#160;&#160;method  
vp&#160;and&#160;wc&#160;are&#160;from&#160;the&#160;actual&#160;canvas,&#160;they&#160;have&#160;been&#160;reset&#160;when&#160;they&#160;get
here... `

 list  (self, single  =None  ) 
     ` ###########################################################################   
#&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#  
#&#160;List&#160;out&#160;template&#160;text&#160;members&#160;(attributes).&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#  
#&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#  
########################################################################### `

 move  (self, p, axis) 
     ` move&#160;a&#160;template&#160;by&#160;p%&#160;along&#160;the&#160;axis&#160;'x'&#160;or&#160;'y'   
positive&#160;values&#160;of&#160;p&#160;mean&#160;movement&#160;toward&#160;right/top  
negative&#160;values&#160;of&#160;p&#160;mean&#160;movement&#160;toward&#160;left/bottom  
The&#160;reference&#160;point&#160;is&#160;t.data.x1/y1  
usage  
t. [ move ](/) (p,axis)  
example:  
t. [ move ](/) (.2,'x')&#160;#&#160;move&#160;everything&#160;right&#160;by&#160;20%  
t. [ move ](/) (.2,'y')&#160;#&#160;move&#160;everything&#160;down&#160;by&#160;20% `

 moveto  (self, x, y) 
     ` move&#160;a&#160;template&#160;along&#160;the&#160;axis&#160;'x'&#160;or&#160;'y'&#160;to&#160;p   
The&#160;reference&#160;point&#160;is&#160;t.data.x/y1  
usage  
t. [ moveto ](/) (x,y)  
example:  
t. [ moveto ](/) (.2,.2)&#160;#&#160;move&#160;everything&#160;so&#160;that&#160;data.x1=.2and&#160;data.y1=.2 `

 plot  (self, slab, gm, bg  =0  , min  =None  , max  =None  ) 
     ` This&#160;plots&#160;the&#160;template&#160;stuff&#160;on&#160;the&#160;Canvas,&#160;it&#160;needs&#160;a&#160;slab&#160;and&#160;a&#160;graphic&#160;method `

 ratio  (self, Rwished, Rout  =None  , box_and_ticks  =0  ) 
     ` Computes&#160;ratio&#160;to&#160;shrink&#160;the&#160;data&#160;area&#160;of&#160;a&#160;template&#160;to&#160;have&#160;an&#160;y/x&#160;ratio&#160;of&#160;Rwished   
has&#160;the&#160;least&#160;possible&#160;deformation&#160;in&#160;linear&#160;projection  
  
Version:&#160;1.1  
  
Necessary&#160;arguments:  
Rwished:&#160;Ratio&#160;y/x&#160;wished  
Optional&#160;arguments:  
Rout:&#160;Ratio&#160;of&#160;output&#160;(default&#160;is&#160;US&#160;Letter=11./8.5)  
Also&#160;you&#160;can&#160;pass&#160;a&#160;string:&#160;"A4","US&#160;LETTER",&#160;"X"/"SCREEN",&#160;the&#160;latest&#160;uses
the&#160;window&#160;information  
box_and_ticks:&#160;Also&#160;redefine&#160;box&#160;and&#160;ticks&#160;to&#160;the&#160;new&#160;region  
Returned:  
vcs&#160;template&#160;object  
  
Usage&#160;example:  
##&#160;y&#160;is&#160;twice&#160;x  
t. [ ratio ](/) (2) `

 ratio_linear_projection  (self, lon1, lon2, lat1, lat2, Rwished  =None  , Rout  =None  , box_and_ticks  =0  ) 
     ` Computes&#160;ratio&#160;to&#160;shrink&#160;the&#160;data&#160;area&#160;of&#160;a&#160;template&#160;in&#160;order&#160;that&#160;the&#160;overall&#160;area   
has&#160;the&#160;least&#160;possible&#160;deformation&#160;in&#160;linear&#160;projection  
  
Version:&#160;1.1  
Notes:&#160;Thanks&#160;to&#160;Karl&#160;Taylor&#160;for&#160;the&#160;equation&#160;of&#160;"optimal"&#160;ratio  
  
Necessary&#160;arguments:  
lon1,&#160;lon2:&#160;in&#160;degrees_east&#160;&#160;:&#160;Longitude&#160;spanned&#160;by&#160;plot  
lat1,&#160;lat2:&#160;in&#160;degrees_north&#160;:&#160;Latitude&#160;&#160;spanned&#160;by&#160;plot  
Optional&#160;arguments:  
Rwished:&#160;Ratio&#160;y/x&#160;wished,&#160;None=automagic  
Rout:&#160;Ratio&#160;of&#160;output&#160;(default&#160;is&#160;US&#160;Letter=11./8.5)  
Also&#160;you&#160;can&#160;pass&#160;a&#160;string:&#160;"A4","US&#160;LETTER",&#160;"X"/"SCREEN",&#160;the&#160;latest&#160;uses
the&#160;window&#160;information  
box_and_ticks:&#160;Also&#160;redefine&#160;box&#160;and&#160;ticks&#160;to&#160;the&#160;new&#160;region  
Returned:  
vcs&#160;template&#160;object  
  
Usage&#160;example:  
##&#160;USA  
t. [ ratio_linear_projection ](/) (-135,-50,20,50) `

 reset  (self, sub_name, v1, v2, ov1  =None  , ov2  =None  ) 
     ` this&#160;function&#160;reset&#160;all&#160;the&#160;attribute&#160;who&#160;have&#160;a&#160;sub&#160;attribute&#160;named&#160;name1&#160;or&#160;name2&#160;or&#160;name   
also&#160;respect&#160;how&#160;far&#160;from&#160;original&#160;position&#160;you&#160;are  
i.e&#160;you&#160;move&#160;to&#160;x1,x2&#160;from&#160;old_x1,&#160;old_x2  
if&#160;your&#160;current&#160;x1&#160;value&#160;is&#160;not&#160;==&#160;to&#160;old_x1_value,&#160;then&#160;respect&#160;how&#160;far&#160;from
it&#160;you&#160;&#160;were  
usage:  
[ reset ](/) (sub_name,v1,v2,ov1=None,ov2=None)  
Example:  
t. [ reset ](/) ('x',x1,x2,t.data.x1,t.data.x2)  
#where&#160;t&#160;is&#160;a&#160;vcs&#160;template&#160;object `

 scale  (self, scale, axis  ='xy'  , font  =-1  ) 
     ` scale&#160;a&#160;template&#160;along&#160;the&#160;axis&#160;'x'&#160;or&#160;'y'&#160;by&#160;scale   
positive&#160;values&#160;of&#160;p&#160;mean&#160;increase  
negative&#160;values&#160;of&#160;p&#160;mean&#160;decrease  
The&#160;reference&#160;point&#160;is&#160;t.data.x/y1  
usage  
t. [ scale ](/) (scale,axis='xy',font=-1)  
scale:&#160;any&#160;number  
axis&#160;can&#160;be&#160;'x','y'&#160;or&#160;'xy'&#160;(which&#160;means&#160;both)  
font&#160;can&#160;be&#160;1/0/-1  
0:&#160;means&#160;do&#160;not&#160;scale&#160;the&#160;fonts  
1:&#160;means&#160;scale&#160;the&#160;fonts  
-1:&#160;means&#160;do&#160;not&#160;scale&#160;the&#160;fonts&#160;unless&#160;axis='xy'   
Example:  
x=vcs.init()  
t=x.createtemplate('a_template')  
t. [ scale ](/) (.5)&#160;&#160;#&#160;halves&#160;the&#160;template&#160;size  
t. [ scale ](/) (1.2)&#160;#&#160;upsize&#160;everything&#160;to&#160;20%&#160;more&#160;than&#160;the&#160;original&#160;size  
t. [ scale ](/) (2,'x')&#160;#&#160;double&#160;the&#160;x&#160;axis  
  
reference&#160;is&#160;t.data.x1/y1 `

 scalefont  (self, scale) 
     ` Scales&#160;the&#160;tempate&#160;font&#160;by&#160;scale   
Usage:  
[ scalefont ](/) (scale)  
  
Example:  
x=vcs.init()  
t=x.createtemplate('a_template')  
t. [ scalefont ](/) (.5)&#160;#&#160;reduces&#160;the&#160;fonts&#160;size&#160;by&#160;2 `

 script  (self, script_filename  =None  , mode  =None  ) 
     ` Function:&#160;&#160;&#160;&#160;&#160;script&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#&#160;Calls&#160;_vcs.scriptP   
  
Description&#160;of&#160;Function:  
Saves&#160;out&#160;a&#160;template&#160;object&#160;in&#160;VCS&#160;or&#160;Python&#160;script&#160;form&#160;to&#160;a&#160;designated  
file.  
  
Example&#160;of&#160;Use:  
[ script ](/) (scriptfile_name,&#160;mode)  
where:&#160;scriptfile_name&#160;is&#160;the&#160;output&#160;name&#160;of&#160;the&#160;script&#160;file.  
mode&#160;is&#160;either&#160;"w"&#160;for&#160;replace&#160;or&#160;"a"&#160;for&#160;append.  
  
Note:&#160;If&#160;the&#160;the&#160;filename&#160;has&#160;a&#160;".py"&#160;at&#160;the&#160;end,&#160;it&#160;will&#160;produce&#160;a  
Python&#160;script.&#160;If&#160;the&#160;filename&#160;has&#160;a&#160;".scr"&#160;at&#160;the&#160;end,&#160;it&#160;will  
produce&#160;a&#160;VCS&#160;script.&#160;If&#160;neither&#160;extensions&#160;are&#160;give,&#160;then&#160;by  
default&#160;a&#160;Python&#160;script&#160;will&#160;be&#160;produced.  
  
a=vcs.init()  
templt=a.createtemplate('temp')&#160;&#160;&#160;#&#160;create&#160;a&#160;template&#160;object  
templt. [ script ](/) ('filename.py')&#160;&#160;&#160;&#160;&#160;&#160;#&#160;Append&#160;to&#160;a&#160;Python&#160;file
"filename.py"  
templt. [ script ](/) ('filename.scr')&#160;&#160;&#160;&#160;&#160;#&#160;Append&#160;to&#160;a&#160;VCS&#160;file
"filename.scr"  
templt. [ script ](/) ('filename','w')&#160;&#160;&#160;&#160;&#160;#&#160;Create&#160;or&#160;overwrite&#160;to&#160;a&#160;Python
file&#160;"filename.py" `

  
 Functions 

` `

 getPmember  (self, member) 
     ` ###############################################################################   
#
#  
#&#160;Function:&#160;&#160;&#160;&#160;&#160;getPmember
#  
#
#  
#&#160;Description&#160;of&#160;Function:
#  
#&#160;&#160;&#160;&#160;&#160;&#160;&#160;Private&#160;function&#160;that&#160;retrieves&#160;the&#160;template&#160;members&#160;from&#160;the&#160;C
#  
#&#160;&#160;&#160;&#160;&#160;&#160;&#160;structure&#160;and&#160;passes&#160;it&#160;back&#160;to&#160;Python.
#  
#
#  
#
#  
#&#160;Example&#160;of&#160;Use:
#  
#&#160;&#160;&#160;&#160;&#160;&#160;return_value&#160;=
#  
# [ getPmember ](/) (self,name)
#  
#&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;where:&#160;self&#160;is&#160;the&#160;class&#160;(e.g., [ P ](/) )
#  
#&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;name&#160;is&#160;the&#160;name&#160;of&#160;the&#160;member&#160;that&#160;is&#160;being&#160;found
#  
#
#  
##############################################################################
# `

 renameP  (self, old_name, new_name) 
     ` ###############################################################################   
#
#  
#&#160;Function:&#160;&#160;&#160;&#160;&#160;renameP
#  
#
#  
#&#160;Description&#160;of&#160;Function:
#  
#&#160;&#160;&#160;&#160;&#160;&#160;&#160;Private&#160;function&#160;that&#160;renames&#160;the&#160;name&#160;of&#160;an&#160;existing&#160;template
#  
#&#160;&#160;&#160;&#160;&#160;&#160;&#160;graphics&#160;method.
#  
#
#  
#
#  
#&#160;Example&#160;of&#160;Use:
#  
# [ renameP ](/) (old_name,&#160;new_name)
#  
#&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;where:&#160;old_name&#160;is&#160;the&#160;current&#160;name&#160;of&#160;template&#160;graphics
method#  
#&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;new_name&#160;is&#160;the&#160;new&#160;name&#160;for&#160;the&#160;template&#160;graphics
method  
#
#  
##############################################################################
# `

 setPmember  (self, member, value) 
     ` ###############################################################################   
#
#  
#&#160;Function:&#160;&#160;&#160;&#160;&#160;setPmember
#  
#
#  
#&#160;Description&#160;of&#160;Function:
#  
#&#160;&#160;&#160;&#160;&#160;&#160;&#160;Private&#160;function&#160;to&#160;update&#160;the&#160;VCS&#160;canvas&#160;plot.&#160;If&#160;the&#160;canvas&#160;mode&#160;is
#  
#&#160;&#160;&#160;&#160;&#160;&#160;&#160;set&#160;to&#160;0,&#160;then&#160;this&#160;function&#160;does&#160;nothing.
#  
#
#  
#
#  
#&#160;Example&#160;of&#160;Use:
#  
# [ setPmember ](/) (self,name,value)
#  
#&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;where:&#160;self&#160;is&#160;the&#160;class&#160;(e.g., [ P ](/) )
#  
#&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;name&#160;is&#160;the&#160;name&#160;of&#160;the&#160;member&#160;that&#160;is&#160;being&#160;changed
#  
#&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;value&#160;is&#160;the&#160;new&#160;value&#160;of&#160;the&#160;member&#160;(or&#160;attribute)
#  
#
#  
##############################################################################
# `

  
 Data 

` `

 StringTypes  = (<type 'str'>, <type 'unicode'>) 

* * *

UCRL-WEB-213937 | [ Privacy & Legal Notice ](/disclaimer.html)

[ webmaster@pcmdi.llnl.gov ](/webmaster@pcmdi.llnl.gov)

[ ![Powered by Plone](media/plone_powered.gif) ](/)

