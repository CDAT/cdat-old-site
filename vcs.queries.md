---
layout: default
title:
---

 [ Skip to content. ](/cdat/source/api-reference/vcs.queries.html) | [ Skip to
navigation ](/cdat/source/api-reference/vcs.queries.html)

Search Site

[ Advanced Search&#8230; ](/search_form)

#  [ PCMDI Software Portal ](/)

#####  Sections

  * [ Home ](/)

#####  Personal tools

  * [ Log in ](/login_form)

You are here:  [ Home ](/) -> [ CDAT ](/cdat) -> [ Source Code ](/cdat/source)
-> [ API Reference ](/cdat/source/api-reference) -> Python: module vcs.queries

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

        * [ Python: module vcs.queries ](/cdat/source/api-reference/vcs.queries.html)

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

  * [ ![Send this page to somebody](media/mail_icon.gif) ](/cdat/source/api-reference/vcs.queries.html/sendto_form)
  * [ ![Print this page](media/print_icon.gif) ](/this.print\(\))

#  Python: module vcs.queries

  
  
 [ vcs  ](/vcs.html) .queries 
[ index ](/)  

` ############################################################################
###############  
#
#  
#&#160;Functions&#160;which&#160;get&#160;information&#160;about&#160;vcs&#160;graphics&#160;objects&#160;such&#160;as&#160;graphics
methods.&#160;&#160;&#160;&#160;#  
#
#  
##############################################################################
############# `

  
 Modules 

` `

[ vcs.boxfill ](/vcs.boxfill.html)  
[ vcs.continents ](/vcs.continents.html)  
[ vcs.displayplot ](/vcs.displayplot.html)  
[ vcs.fillarea ](/vcs.fillarea.html)  
[ vcs.isofill ](/vcs.isofill.html)  
[ vcs.isoline ](/vcs.isoline.html)  

[ vcs.line ](/vcs.line.html)  
[ vcs.marker ](/vcs.marker.html)  
[ vcs.meshfill ](/vcs.meshfill.html)  
[ vcs.outfill ](/vcs.outfill.html)  
[ vcs.outline ](/vcs.outline.html)  
[ vcs.projection ](/vcs.projection.html)  

[ vcs.scatter ](/vcs.scatter.html)  
[ vcs.taylor ](/vcs.taylor.html)  
[ vcs.template ](/vcs.template.html)  
[ vcs.textcombined ](/vcs.textcombined.html)  
[ vcs.textorientation ](/vcs.textorientation.html)  
[ vcs.texttable ](/vcs.texttable.html)  

[ vcs.vector ](/vcs.vector.html)  
[ vcs.xvsy ](/vcs.xvsy.html)  
[ vcs.xyvsy ](/vcs.xyvsy.html)  
[ vcs.yxvsx ](/vcs.yxvsx.html)  

  
 Functions 

` `

 graphicsmethodlist  () 
     ` Function:&#160;graphicsmethodlist   
  
Description&#160;of&#160;Function:  
Will&#160;return&#160;a&#160;list&#160;of&#160;available&#160;grapics&#160;methods&#160;(i.e.,&#160;boxfill,&#160;isofill,
isoline,&#160;outf  
ill,  
outline,&#160;continents,&#160;scatter,&#160;vector,&#160;xvsy,&#160;xyvsy,&#160;yxvsx,&#160;taylordiagram&#160;).  
  
Example&#160;of&#160;Use:  
a=vcs.init()  
gm_list=a. [ graphicsmethodlist ](/) ()&#160;&#160;#&#160;Return&#160;graphics&#160;method&#160;list `

 graphicsmethodtype  (gobj) 
     ` Function:&#160;graphicsmethodtype   
  
Description&#160;of&#160;Function:  
Will&#160;return&#160;the&#160;grapics&#160;method's&#160;type:&#160;boxfill,&#160;isofill,&#160;isoline,&#160;outfill,  
outline,&#160;continents,&#160;scatter,&#160;vector,&#160;xvsy,&#160;xyvsy,&#160;or&#160;yxvsx,&#160;taylordiagram.  
  
Returns&#160;a&#160;None&#160;if&#160;the&#160;object&#160;is&#160;not&#160;a&#160;graphics&#160;method.  
  
Example&#160;of&#160;Use:  
a=vcs.init()  
box=a.getboxfill('quick')&#160;&#160;#&#160;Get&#160;an&#160;existing&#160;boxfill&#160;graphics&#160;method&#160;in&#160;VCS  
iso=a.getisofill('quick')&#160;&#160;#&#160;Get&#160;an&#160;existing&#160;isofill&#160;graphics&#160;method&#160;in&#160;VCS  
ln=a.getline('quick')&#160;&#160;&#160;&#160;&#160;&#160;#&#160;Get&#160;an&#160;existing&#160;line&#160;element&#160;in&#160;VCS  
...  
  
print&#160;vcs. [ graphicsmethodtype ](/) (box)&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#&#160;Will&#160;print&#160;'boxfill'  
print&#160;vcs. [ graphicsmethodtype ](/) (iso)&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#&#160;Will&#160;print&#160;'isofill'  
print&#160;vcs. [ graphicsmethodtype ](/) (ln)&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#&#160;Will&#160;print&#160;None,&#160;because
ln&#160;is&#160;not&#160;a  
#&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;graphics&#160;method `

 isboxfill  (obj) 
     ` Function:&#160;isboxfill   
  
Description&#160;of&#160;Function:  
Check&#160;to&#160;see&#160;if&#160;this&#160;object&#160;is&#160;a&#160;VCS&#160;primary&#160;boxfill&#160;graphics&#160;method.  
  
Example&#160;of&#160;Use:  
a=vcs.init()  
box=a.getboxfill("quick")&#160;&#160;#&#160;To&#160;Modify&#160;an&#160;existing&#160;boxfill&#160;object  
...  
  
if&#160;queries. [ isboxfill ](/) (box):  
box.list() `

 iscolormap  (obj) 
     ` Function:&#160;iscolormap   
  
Description&#160;of&#160;Function:  
Check&#160;to&#160;see&#160;if&#160;this&#160;object&#160;is&#160;a&#160;VCS&#160;secondary&#160;colormap.  
  
Example&#160;of&#160;Use:  
a=vcs.init()  
ln=a.getcolormap("quick")&#160;&#160;#&#160;To&#160;Modify&#160;an&#160;existing&#160;colormap&#160;object  
...  
  
if&#160;a. [ iscolormap ](/) (ln):  
ln.list() `

 iscontinents  (obj) 
     ` Function:&#160;iscontinents   
  
Description&#160;of&#160;Function:  
Check&#160;to&#160;see&#160;if&#160;this&#160;object&#160;is&#160;a&#160;VCS&#160;primary&#160;continents&#160;graphics&#160;method.  
  
Example&#160;of&#160;Use:  
a=vcs.init()  
con=a.getcontinents("quick")&#160;&#160;#&#160;To&#160;Modify&#160;an&#160;existing&#160;continents&#160;object  
...  
  
if&#160;queries. [ iscontinents ](/) (con):  
con.list() `

 isfillarea  (obj) 
     ` Function:&#160;isfillarea   
  
Description&#160;of&#160;Function:  
Check&#160;to&#160;see&#160;if&#160;this&#160;object&#160;is&#160;a&#160;VCS&#160;secondary&#160;fillarea.  
  
Example&#160;of&#160;Use:  
a=vcs.init()  
fa=a.getfillarea("def37")&#160;&#160;#&#160;To&#160;Modify&#160;an&#160;existing&#160;fillarea&#160;object  
...  
  
if&#160;queries. [ isfillarea ](/) (fa):  
fa.list() `

 isgraphicsmethod  (gobj) 
     ` Function:&#160;isgraphicsmethod   
  
Description&#160;of&#160;Function:  
Indicates&#160;if&#160;the&#160;entered&#160;argument&#160;is&#160;one&#160;of&#160;the&#160;following&#160;graphics  
methods:&#160;boxfill,&#160;isofill,&#160;isoline,&#160;outfill,&#160;outline,&#160;continents,  
scatter,&#160;vector,&#160;xvsy,&#160;xyvsy,&#160;yxvsx.  
  
Returns&#160;a&#160;1,&#160;which&#160;indicates&#160;true,&#160;if&#160;the&#160;argment&#160;is&#160;one&#160;of&#160;the&#160;above.  
Otherwise,&#160;it&#160;will&#160;return&#160;a&#160;0,&#160;indicating&#160;false.  
  
Example&#160;of&#160;Use:  
a=vcs.init()  
box=a.getboxfill('quick')&#160;&#160;#&#160;To&#160;Modify&#160;an&#160;existing&#160;boxfill&#160;use:  
...  
  
if&#160;vcs. [ isgraphicsmethod ](/) (box):  
box.list() `

 isisofill  (obj) 
     ` Function:&#160;isisofill   
  
Description&#160;of&#160;Function:  
Check&#160;to&#160;see&#160;if&#160;this&#160;object&#160;is&#160;a&#160;VCS&#160;primary&#160;isofill&#160;graphics&#160;method.  
  
Example&#160;of&#160;Use:  
a=vcs.init()  
iso=a.getisofill("quick")&#160;&#160;#&#160;To&#160;Modify&#160;an&#160;existing&#160;isofill&#160;object  
...  
  
if&#160;queries. [ isisofill ](/) (iso):  
iso.list() `

 isisoline  (obj) 
     ` Function:&#160;isisoline   
  
Description&#160;of&#160;Function:  
Check&#160;to&#160;see&#160;if&#160;this&#160;object&#160;is&#160;a&#160;VCS&#160;primary&#160;isoline&#160;graphics&#160;method.  
  
Example&#160;of&#160;Use:  
a=vcs.init()  
iso=a.getisoline("quick")&#160;&#160;#&#160;To&#160;Modify&#160;an&#160;existing&#160;isoline&#160;object  
...  
  
if&#160;queries. [ isisoline ](/) (iso):  
iso.list() `

 isline  (obj) 
     ` Function:&#160;isline   
  
Description&#160;of&#160;Function:  
Check&#160;to&#160;see&#160;if&#160;this&#160;object&#160;is&#160;a&#160;VCS&#160;secondary&#160;line.  
  
Example&#160;of&#160;Use:  
a=vcs.init()  
ln=a.getline("red")&#160;&#160;#&#160;To&#160;Modify&#160;an&#160;existing&#160;line&#160;object  
...  
  
if&#160;queries. [ isline ](/) (ln):  
ln.list() `

 ismarker  (obj) 
     ` Function:&#160;ismarker   
  
Description&#160;of&#160;Function:  
Check&#160;to&#160;see&#160;if&#160;this&#160;object&#160;is&#160;a&#160;VCS&#160;secondary&#160;marker.  
  
Example&#160;of&#160;Use:  
a=vcs.init()  
mk=a.getmarker("red")&#160;&#160;#&#160;To&#160;Modify&#160;an&#160;existing&#160;marker&#160;object  
...  
  
if&#160;queries. [ ismarker ](/) (mk):  
mk.list() `

 ismeshfill  (obj) 
     ` Function:&#160;ismeshfill   
  
Description&#160;of&#160;Function:  
Check&#160;to&#160;see&#160;if&#160;this&#160;object&#160;is&#160;a&#160;VCS&#160;primary&#160;meshfill&#160;graphics&#160;method.  
  
Example&#160;of&#160;Use:  
a=vcs.init()  
mesh=a.getmeshfill("quick")&#160;&#160;#&#160;To&#160;Modify&#160;an&#160;existing&#160;taylor&#160;object  
...  
  
if&#160;queries. [ ismeshfill ](/) (mesh):  
mesh.list() `

 isoutfill  (obj) 
     ` Function:&#160;isoutfill   
  
Description&#160;of&#160;Function:  
Check&#160;to&#160;see&#160;if&#160;this&#160;object&#160;is&#160;a&#160;VCS&#160;primary&#160;outfill&#160;graphics&#160;method.  
  
Example&#160;of&#160;Use:  
a=vcs.init()  
out=a.getoutfill("quick")&#160;&#160;#&#160;To&#160;Modify&#160;an&#160;existing&#160;outfill&#160;object  
...  
  
if&#160;queries. [ isoutfill ](/) (out):  
out.list() `

 isoutline  (obj) 
     ` Function:&#160;isoutline   
  
Description&#160;of&#160;Function:  
Check&#160;to&#160;see&#160;if&#160;this&#160;object&#160;is&#160;a&#160;VCS&#160;primary&#160;outline&#160;graphics&#160;method.  
  
Example&#160;of&#160;Use:  
a=vcs.init()  
out=a.getoutline("quick")&#160;&#160;#&#160;To&#160;Modify&#160;an&#160;existing&#160;outline&#160;object  
...  
  
if&#160;queries. [ isoutline ](/) (out):  
out.list() `

 isplot  (pobj) 
     ` Function:&#160;isplot   
  
Description&#160;of&#160;Function:  
Indicates&#160;if&#160;the&#160;entered&#160;argument&#160;a&#160;display&#160;plot.  
  
Returns&#160;a&#160;1&#160;if&#160;the&#160;argment&#160;true.  
Otherwise,&#160;it&#160;will&#160;return&#160;a&#160;0,&#160;indicating&#160;false.  
  
Example&#160;of&#160;Use:  
a=vcs.init()  
...  
a.show('plot')&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#&#160;show&#160;all&#160;the&#160;plot&#160;objects&#160;on&#160;the&#160;VCS
Canvas  
p1=a.getplot('dpy_plot_1')&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#&#160;Get&#160;an&#160;existing&#160;plot&#160;object&#160;named
'dpy_plot_1'  
p2=a.plot(s)&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#&#160;Create&#160;a&#160;new&#160;display&#160;plot&#160;object  
...  
  
if&#160;a. [ isplot ](/) (p1):  
p1.list()&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#&#160;If&#160;it&#160;is&#160;a&#160;plot&#160;then&#160;list&#160;its&#160;members `

 isprojection  (obj) 
     ` Function:&#160;isprojection   
  
Description&#160;of&#160;Function:  
Check&#160;to&#160;see&#160;if&#160;this&#160;object&#160;is&#160;a&#160;VCS&#160;secondary&#160;projection&#160;graphic&#160;object&#160;.  
  
Example&#160;of&#160;Use:  
a=vcs.init()  
p=a.getprojection("default")&#160;&#160;#&#160;To&#160;Modify&#160;an&#160;existing&#160;taylor&#160;object  
...  
  
if&#160;queries. [ isprojection ](/) (p):  
p.list() `

 isscatter  (obj) 
     ` Function:&#160;isscatter   
  
Description&#160;of&#160;Function:  
Check&#160;to&#160;see&#160;if&#160;this&#160;object&#160;is&#160;a&#160;VCS&#160;primary&#160;scatter&#160;graphics&#160;method.  
  
Example&#160;of&#160;Use:  
a=vcs.init()  
scr=a.getscatter("quick")&#160;&#160;#&#160;To&#160;Modify&#160;an&#160;existing&#160;scatter&#160;object  
...  
  
if&#160;queries. [ isscatter ](/) (scr):  
scr.list() `

 issecondaryobject  (sobj) 
     ` Function:&#160;issecondaryobject   
  
Description&#160;of&#160;Function:  
  
In&#160;addition,&#160;detailed&#160;specification&#160;of&#160;the&#160;primary&#160;elements'&#160;(or  
primary&#160;class&#160;elements'),&#160;attributes&#160;is&#160;provided&#160;by&#160;eight&#160;secondary  
elements&#160;or&#160;(secondary&#160;class&#160;elements):  
  
1.)&#160;colormap:&#160;specification&#160;of&#160;combinations&#160;of&#160;256&#160;available  
colors  
2.)&#160;fill&#160;area:&#160;style,&#160;style&#160;index,&#160;and&#160;color&#160;index  
3.)&#160;format:&#160;specifications&#160;for&#160;converting&#160;numbers&#160;to&#160;display  
strings  
4.)&#160;line:&#160;line&#160;type,&#160;width,&#160;and&#160;color&#160;index  
5.)&#160;list:&#160;a&#160;sequence&#160;of&#160;pairs&#160;of&#160;numerical&#160;and&#160;character&#160;values  
6.)&#160;marker:&#160;marker&#160;type,&#160;size,&#160;and&#160;color&#160;index  
7.)&#160;text&#160;table:&#160;text&#160;font&#160;type,&#160;character&#160;spacing,&#160;expansion,&#160;and  
color&#160;index  
8.)&#160;text&#160;orientation:&#160;character&#160;height,&#160;angle,&#160;path,&#160;and  
horizontal/vertical&#160;alignment  
9.)&#160;projections  
  
  
Example&#160;of&#160;Use:  
a=vcs.init()  
line=a.getline('red')&#160;&#160;#&#160;To&#160;Modify&#160;an&#160;existing&#160;line&#160;object  
...  
  
if&#160;queries. [ issecondaryobject ](/) (line):  
box.list() `

 istaylordiagram  (obj) 
     ` Function:&#160;istaylordiagram   
  
Description&#160;of&#160;Function:  
Check&#160;to&#160;see&#160;if&#160;this&#160;object&#160;is&#160;a&#160;VCS&#160;primary&#160;taylordiagram&#160;graphics&#160;method.  
  
Example&#160;of&#160;Use:  
a=vcs.init()  
td=a.gettaylordiagram("default")&#160;&#160;#&#160;To&#160;get&#160;an&#160;existing&#160;taylor&#160;object  
...  
  
if&#160;queries. [ istaylordiagram ](/) (td):  
td.list() `

 istemplate  (gobj) 
     ` Function:&#160;istemplate   
  
Description&#160;of&#160;Function:  
Indicates&#160;if&#160;the&#160;entered&#160;argument&#160;a&#160;template.  
  
Returns&#160;a&#160;1&#160;if&#160;the&#160;argment&#160;true.  
Otherwise,&#160;it&#160;will&#160;return&#160;a&#160;0,&#160;indicating&#160;false.  
  
Example&#160;of&#160;Use:  
a=vcs.init()  
templt=a.gettemplate('quick')&#160;&#160;#&#160;Modify&#160;an&#160;existing&#160;template&#160;named&#160;'quick'  
...  
  
if&#160;vcs. [ istemplate ](/) (templt):  
templt.list()&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#&#160;If&#160;it&#160;is&#160;a&#160;template&#160;then&#160;list&#160;its&#160;members `

 istext  = istextcombined(obj) 
     ` Function:&#160;istextcombined   
  
Description&#160;of&#160;Function:  
Check&#160;to&#160;see&#160;if&#160;this&#160;object&#160;is&#160;a&#160;VCS&#160;secondary&#160;text&#160;combined.  
  
Example&#160;of&#160;Use:  
a=vcs.init()  
tc=a.gettextcombined("std",&#160;"7left")&#160;&#160;#&#160;To&#160;Modify&#160;existing&#160;text&#160;table&#160;and
orientation&#160;objects  
...  
  
if [ istextcombined ](/) (tc):  
tc.list()  
if [ istexttable ](/) (tc):  
tc.list()  
if [ istextorientation ](/) (tc):  
tc.list() `

 istextcombined  (obj) 
     ` Function:&#160;istextcombined   
  
Description&#160;of&#160;Function:  
Check&#160;to&#160;see&#160;if&#160;this&#160;object&#160;is&#160;a&#160;VCS&#160;secondary&#160;text&#160;combined.  
  
Example&#160;of&#160;Use:  
a=vcs.init()  
tc=a.gettextcombined("std",&#160;"7left")&#160;&#160;#&#160;To&#160;Modify&#160;existing&#160;text&#160;table&#160;and
orientation&#160;objects  
...  
  
if [ istextcombined ](/) (tc):  
tc.list()  
if [ istexttable ](/) (tc):  
tc.list()  
if [ istextorientation ](/) (tc):  
tc.list() `

 istextorientation  (obj) 
     ` Function:&#160;istextorientation   
  
Description&#160;of&#160;Function:  
Check&#160;to&#160;see&#160;if&#160;this&#160;object&#160;is&#160;a&#160;VCS&#160;secondary&#160;text&#160;orientation.  
  
Example&#160;of&#160;Use:  
a=vcs.init()  
to=a.gettextorientation("7left")&#160;&#160;#&#160;To&#160;Modify&#160;an&#160;existing&#160;text&#160;orientation
object  
...  
  
if&#160;queries. [ istextorientation ](/) (to):  
to.list() `

 istexttable  (obj) 
     ` Function:&#160;istexttable   
  
Description&#160;of&#160;Function:  
Check&#160;to&#160;see&#160;if&#160;this&#160;object&#160;is&#160;a&#160;VCS&#160;secondary&#160;text&#160;table.  
  
Example&#160;of&#160;Use:  
a=vcs.init()  
tt=a.gettexttable("std")&#160;&#160;#&#160;To&#160;Modify&#160;an&#160;existing&#160;text&#160;table&#160;object  
...  
  
if&#160;queries. [ istexttable ](/) (tt):  
tt.list() `

 isvector  (obj) 
     ` Function:&#160;isvector   
  
Description&#160;of&#160;Function:  
Check&#160;to&#160;see&#160;if&#160;this&#160;object&#160;is&#160;a&#160;VCS&#160;primary&#160;vector&#160;graphics&#160;method.  
  
Example&#160;of&#160;Use:  
a=vcs.init()  
vec=a.getvector("quick")&#160;&#160;#&#160;To&#160;Modify&#160;an&#160;existing&#160;vector&#160;object  
...  
  
if&#160;queries. [ isvector ](/) (vec):  
vec.list() `

 isxvsy  (obj) 
     ` Function:&#160;isxvsy   
  
Description&#160;of&#160;Function:  
Check&#160;to&#160;see&#160;if&#160;this&#160;object&#160;is&#160;a&#160;VCS&#160;primary&#160;xvsy&#160;graphics&#160;method.  
  
Example&#160;of&#160;Use:  
a=vcs.init()  
xy=a.getxvsy("quick")&#160;&#160;#&#160;To&#160;Modify&#160;an&#160;existing&#160;xvsy&#160;object  
...  
  
if&#160;queries. [ isxvsy ](/) (xy):  
xy.list() `

 isxyvsy  (obj) 
     ` Function:&#160;isxyvsy   
  
Description&#160;of&#160;Function:  
Check&#160;to&#160;see&#160;if&#160;this&#160;object&#160;is&#160;a&#160;VCS&#160;primary&#160;Xyvsy&#160;graphics&#160;method.  
  
Example&#160;of&#160;Use:  
a=vcs.init()  
xyy=a.getxyvsy("quick")&#160;&#160;#&#160;To&#160;Modify&#160;an&#160;existing&#160;Xyvsy&#160;object  
...  
  
if&#160;queries. [ isxyvsy ](/) (xyy):  
xyy.list() `

 isyxvsx  (obj) 
     ` Function:&#160;isyxvsx   
  
Description&#160;of&#160;Function:  
Check&#160;to&#160;see&#160;if&#160;this&#160;object&#160;is&#160;a&#160;VCS&#160;primary&#160;yxvsx&#160;graphics&#160;method.  
  
Example&#160;of&#160;Use:  
a=vcs.init()  
yxx=a.getyxvsx("quick")&#160;&#160;#&#160;To&#160;Modify&#160;an&#160;existing&#160;yxvsx&#160;object  
...  
  
if&#160;queries. [ isyxvsx ](/) (yxx):  
yxx.list() `

* * *

UCRL-WEB-213937 | [ Privacy & Legal Notice ](/disclaimer.html)

[ webmaster@pcmdi.llnl.gov ](/webmaster@pcmdi.llnl.gov)

[ ![Powered by Plone](media/plone_powered.gif) ](/)

