---
layout: default
title:
---

 [ Skip to content. ](/cdat/source/api-reference/vcs.scatter.html) | [ Skip to
navigation ](/cdat/source/api-reference/vcs.scatter.html)

Search Site

[ Advanced Search&#8230; ](/search_form)

#  [ PCMDI Software Portal ](/)

#####  Sections

  * [ Home ](/)

#####  Personal tools

  * [ Log in ](/login_form)

You are here:  [ Home ](/) -> [ CDAT ](/cdat) -> [ Source Code ](/cdat/source)
-> [ API Reference ](/cdat/source/api-reference) -> Python: module vcs.scatter

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

        * [ Python: module vcs.scatter ](/cdat/source/api-reference/vcs.scatter.html)

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

  * [ ![Send this page to somebody](media/mail_icon.gif) ](/cdat/source/api-reference/vcs.scatter.html/sendto_form)
  * [ ![Print this page](media/print_icon.gif) ](/this.print\(\))

#  Python: module vcs.scatter

  
  
 [ vcs  ](/vcs.html) .scatter 
[ index ](/)  

` #&#160;Scatter&#160;( [ GSp ](/) )&#160;module `

  
 Modules 

` `

[ vcs.Canvas ](/vcs.Canvas.html)  
[ vcs.VCS_validation_functions ](/vcs.VCS_validation_functions.html)  

[ vcs._vcs ](/vcs._vcs.html)  
[ cdtime ](/cdtime.html)  

[ vcs.queries ](/vcs.queries.html)  

  
 Classes 

` `

[ __builtin__.object ](/__builtin__.html)

    

[ GSp ](/vcs.scatter.html)

  
class  GSp  ( [ __builtin__.object ](/__builtin__.html) )

` `

` Class: [ GSp ](/) #&#160;Scatter  
  
Description&#160;of [ GSp ](/) Class:  
The&#160;Scatter&#160;graphics&#160;method&#160;displays&#160;a&#160;scatter&#160;plot&#160;of&#160;two&#160;4-dimensional&#160;data  
arrays,&#160;e.g.&#160;A(x,y,z,t)&#160;and&#160;B(x,y,z,t).&#160;The&#160;example&#160;below&#160;shows&#160;how&#160;to&#160;change  
the&#160;marker&#160;attributes&#160;of&#160;a&#160;scatter&#160;plot.  
  
This&#160;class&#160;is&#160;used&#160;to&#160;define&#160;an&#160;scatter&#160;table&#160;entry&#160;used&#160;in&#160;VCS,&#160;or&#160;it&#160;can&#160;be  
used&#160;to&#160;change&#160;some&#160;or&#160;all&#160;of&#160;the&#160;scatter&#160;attributes&#160;in&#160;an&#160;existing&#160;scatter  
table&#160;entry.  
  
Other&#160;Useful&#160;Functions:  
a=vcs.init()&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#&#160;Constructor  
a.show('scatter')&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#&#160;Show&#160;predefined&#160;scatter&#160;graphics&#160;methods  
a.show('marker')&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#&#160;Show&#160;predefined&#160;marker&#160;objects  
a.setcolormap("AMIP")&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#&#160;Change&#160;the&#160;VCS&#160;color&#160;map  
a.scatter(s1,&#160;s2,&#160;s,'default')&#160;&#160;#&#160;Plot&#160;data&#160;'s1'&#160;and&#160;'s2'&#160;with&#160;scatter&#160;'s'  
and&#160;'default'&#160;template  
a.update()&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#&#160;Updates&#160;the&#160;VCS&#160;Canvas&#160;at&#160;user's&#160;request  
a.mode=1,&#160;or&#160;0&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#&#160;If&#160;1,&#160;then&#160;automatic&#160;update,&#160;else&#160;if  
0,&#160;then&#160;use&#160;update&#160;function&#160;to  
update&#160;the&#160;VCS&#160;Canvas.  
  
Example&#160;of&#160;Use:  
a=vcs.init()  
To&#160;Create&#160;a&#160;new&#160;instance&#160;of&#160;scatter&#160;use:  
sr=a.createscatter('new','quick')&#160;#&#160;copies&#160;content&#160;of&#160;'quick'&#160;to&#160;'new'  
sr=a.createscatter('new')&#160;#&#160;copies&#160;content&#160;of&#160;'default'&#160;to&#160;'new'  
  
To&#160;Modify&#160;an&#160;existing&#160;scatter&#160;use:  
sr=a.getscatter('AMIP_psl')  
  
sr. [ list ](/) ()&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#&#160;Will&#160;list&#160;all&#160;the&#160;scatter
attribute&#160;values  
sr.projection='linear'&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#&#160;Can&#160;only&#160;be&#160;'linear'  
lon30={-180:'180W',-150:'150W',0:'Eq'}  
sr.xticlabels1=lon30  
sr.xticlabels2=lon30  
sr. [ xticlabels ](/) (lon30,&#160;lon30)&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#&#160;Will&#160;set&#160;them&#160;both  
sr.xmtics1=''  
sr.xmtics2=''  
sr. [ xmtics ](/) (lon30,&#160;lon30)&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#&#160;Will&#160;set&#160;them&#160;both  
sr.yticlabels1=lat10  
sr.yticlabels2=lat10  
sr. [ yticlabels ](/) (lat10,&#160;lat10)&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#&#160;Will&#160;set&#160;them&#160;both  
sr.ymtics1=''  
sr.ymtics2=''  
sr. [ ymtics ](/) (lat10,&#160;lat10)&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#&#160;Will&#160;set&#160;them&#160;both  
sr.datawc_y1=-90.0  
sr.datawc_y2=90.0  
sr.datawc_x1=-180.0  
sr.datawc_x2=180.0  
sr. [ datawc ](/) (-90,&#160;90,&#160;-180,&#160;180)&#160;&#160;&#160;&#160;&#160;&#160;&#160;#&#160;Will&#160;set&#160;them&#160;all  
sr.xaxisconvert='linear'  
sr.yaxisconvert='linear'  
sr. [ xyscale ](/) ('linear',&#160;'area_wt')&#160;&#160;&#160;&#160;&#160;#&#160;Will&#160;set&#160;them&#160;both  
  
Specify&#160;the&#160;marker&#160;type:  
sr.marker=1&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#&#160;Same&#160;as&#160;sr.marker='dot'  
sr.marker=2&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#&#160;Same&#160;as&#160;sr.marker='plus'  
sr.marker=3&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#&#160;Same&#160;as&#160;sr.marker='star'  
sr.marker=4&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#&#160;Same&#160;as&#160;sr.marker='circle'  
sr.marker=5&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#&#160;Same&#160;as&#160;sr.marker='cross'  
sr.marker=6&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#&#160;Same&#160;as&#160;sr.marker='diamond'  
sr.marker=7&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#&#160;Same&#160;as&#160;sr.marker='triangle_up'  
sr.marker=8&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#&#160;Same&#160;as&#160;sr.marker='triangle_down'  
sr.marker=9&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#&#160;Same&#160;as&#160;sr.marker='triangle_left'  
sr.marker=10&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#&#160;Same&#160;as&#160;sr.marker='triangle_right'  
sr.marker=11&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#&#160;Same&#160;as&#160;sr.marker='square'  
sr.marker=12&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#&#160;Same&#160;as&#160;sr.marker='diamond_fill'  
sr.marker=13&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#&#160;Same&#160;as&#160;sr.marker='triangle_up_fill'  
sr.marker=14&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#&#160;Same&#160;as&#160;sr.marker='triangle_down_fill'  
sr.marker=15&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#&#160;Same&#160;as&#160;sr.marker='triangle_left_fill'  
sr.marker=16&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#&#160;Same&#160;as&#160;sr.marker='triangle_right_fill'  
sr.marker=17&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#&#160;Same&#160;as&#160;sr.marker='square_fill'  
sr.marker=None&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#&#160;Draw&#160;no&#160;markers  
  
There&#160;are&#160;four&#160;possibilities&#160;for&#160;setting&#160;the&#160;marker&#160;color&#160;index&#160;(Ex):  
sr.markercolors=22&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#&#160;Same&#160;as&#160;below  
sr.markercolors=(22)&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#&#160;Same&#160;as&#160;below  
sr.markercolors=([22])&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#&#160;Will&#160;set&#160;the&#160;markers&#160;to&#160;a&#160;specific  
#&#160;&#160;&#160;&#160;&#160;&#160;&#160;color&#160;index  
sr.markercolors=None&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#&#160;Color&#160;index&#160;defaults&#160;to&#160;Black  
  
To&#160;set&#160;the&#160;Marker&#160;sizie:  
sr.markersize=5  
sr.markersize=55  
sr.markersize=100  
sr.markersize=300  
sr.markersize=None  
`

Methods defined here:  

 __init__  (self, parent, GSp_name  =None  , GSp_name_src  ='default'  , createGSp  =0  ) 

 datawc  (self, dsp1  =1e+20  , dsp2  =1e+20  , dsp3  =1e+20  , dsp4  =1e+20  ) 

 list  (self) 
     ` #############################################################################   
#&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#  
#&#160;List&#160;out&#160;text&#160;combined&#160;members&#160;(attributes).&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#  
#&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#  
#############################################################################
`

 rename  = renameGSp(self, old_name, new_name) 
     ` ###############################################################################   
#
#  
#&#160;Function:&#160;&#160;&#160;&#160;&#160;renameGSp
#  
#
#  
#&#160;Description&#160;of&#160;Function:
#  
#&#160;&#160;&#160;&#160;&#160;&#160;&#160;Private&#160;function&#160;that&#160;renames&#160;the&#160;name&#160;of&#160;an&#160;existing&#160;scatter
#  
#&#160;&#160;&#160;&#160;&#160;&#160;&#160;graphics&#160;method.
#  
#
#  
#
#  
#&#160;Example&#160;of&#160;Use:
#  
# [ renameGSp ](/) (old_name,&#160;new_name)
#  
#&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;where:&#160;old_name&#160;is&#160;the&#160;current&#160;name&#160;of&#160;scatter&#160;graphics&#160;method
#  
#&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;new_name&#160;is&#160;the&#160;new&#160;name&#160;for&#160;the&#160;scatter&#160;graphics
method#  
#
#  
##############################################################################
# `

 script  (self, script_filename  =None  , mode  =None  ) 
     ` Function:&#160;&#160;&#160;&#160;&#160;script&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#&#160;Calls&#160;_vcs.scriptGSp   
  
Description&#160;of&#160;Function:  
Saves&#160;out&#160;a&#160;scatter&#160;graphics&#160;method&#160;in&#160;Python&#160;or&#160;VCS&#160;script&#160;form&#160;to&#160;a  
designated&#160;file.  
  
Example&#160;of&#160;Use:  
[ script ](/) (scriptfile_name,&#160;mode)  
where:&#160;scriptfile_name&#160;is&#160;the&#160;output&#160;name&#160;of&#160;the&#160;script&#160;file.  
mode&#160;is&#160;either&#160;"w"&#160;for&#160;replace&#160;or&#160;"a"&#160;for&#160;append.  
  
Note:&#160;If&#160;the&#160;the&#160;filename&#160;has&#160;a&#160;".py"&#160;at&#160;the&#160;end,&#160;it&#160;will&#160;produce&#160;a  
Python&#160;script.&#160;If&#160;the&#160;filename&#160;has&#160;a&#160;".scr"&#160;at&#160;the&#160;end,&#160;it&#160;will  
produce&#160;a&#160;VCS&#160;script.&#160;If&#160;neither&#160;extensions&#160;are&#160;give,&#160;then&#160;by  
default&#160;a&#160;Python&#160;script&#160;will&#160;be&#160;produced.  
  
a=vcs.init()  
scr=a.createboxfill('temp')  
scr. [ script ](/) ('filename.py')&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#&#160;Append&#160;to&#160;a&#160;Python&#160;file
"filename.py"  
scr. [ script ](/) ('filename.scr')&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#&#160;Append&#160;to&#160;a&#160;VCS&#160;file
"filename.scr"  
scr. [ script ](/) ('filename','w') `

 xmtics  (self, xmt1  =''  , xmt2  =''  ) 

 xticlabels  (self, xtl1  =''  , xtl2  =''  ) 

 xyscale  (self, xat  =''  , yat  =''  ) 

 ymtics  (self, ymt1  =''  , ymt2  =''  ) 

 yticlabels  (self, ytl1  =''  , ytl2  =''  ) 

* * *

Properties defined here:  

 datawc_calendar 
    

 _ get _  = _getcalendar(self) 
    

 _ set _  = _setcalendar(self, value) 

 datawc_timeunits 
    

 _ get _  = _gettimeunits(self) 
    

 _ set _  = _settimeunits(self, value) 

 datawc_x1 
    

 _ get _  = _getdatawc_x1(self) 
    

 _ set _  = _setdatawc_x1(self, value) 

 datawc_x2 
    

 _ get _  = _getdatawc_x2(self) 
    

 _ set _  = _setdatawc_x2(self, value) 

 datawc_y1 
    

 _ get _  = _getdatawc_y1(self) 
    

 _ set _  = _setdatawc_y1(self, value) 

 datawc_y2 
    

 _ get _  = _getdatawc_y2(self) 
    

 _ set _  = _setdatawc_y2(self, value) 

 marker 
    

 _ get _  = _getmarker(self) 
    

 _ set _  = _setmarker(self, value) 

 markercolor 
    

 _ get _  = _getmarkercolor(self) 
    

 _ set _  = _setmarkercolor(self, value) 

 markersize 
    

 _ get _  = _getmarkersize(self) 
    

 _ set _  = _setmarkersize(self, value) 

 name 
    

 _ get _  = _getname(self) 
    

 _ set _  = _setname(self, value) 

 projection 
    

 _ get _  = _getprojection(self) 
    

 _ set _  = _setprojection(self, value) 

 xaxisconvert 
    

 _ get _  = _getxaxisconvert(self) 
    

 _ set _  = _setxaxisconvert(self, value) 

 xmtics1 
    

 _ get _  = _getxmtics1(self) 
    

 _ set _  = _setxmtics1(self, value) 

 xmtics2 
    

 _ get _  = _getxmtics2(self) 
    

 _ set _  = _setxmtics2(self, value) 

 xticlabels1 
    

 _ get _  = _getxticlabels1(self) 
    

 _ set _  = _setxticlabels1(self, value) 

 xticlabels2 
    

 _ get _  = _getxticlabels2(self) 
    

 _ set _  = _setxticlabels2(self, value) 

 yaxisconvert 
    

 _ get _  = _getyaxisconvert(self) 
    

 _ set _  = _setyaxisconvert(self, value) 

 ymtics1 
    

 _ get _  = _getymtics1(self) 
    

 _ set _  = _setymtics1(self, value) 

 ymtics2 
    

 _ get _  = _getymtics2(self) 
    

 _ set _  = _setymtics2(self, value) 

 yticlabels1 
    

 _ get _  = _getyticlabels1(self) 
    

 _ set _  = _setyticlabels1(self, value) 

 yticlabels2 
    

 _ get _  = _getyticlabels2(self) 
    

 _ set _  = _setyticlabels2(self, value) 

* * *

Data and other attributes defined here:  

 __slots__  = ['setmember', 'parent', 'name', 'g_name', 'yaxisconvert', 'xaxisconvert', 'marker', 'markersize', 'markercolor', 'projection', 'xticlabels1', 'xticlabels2', 'yticlabels1', 'yticlabels2', 'xmtics1', 'xmtics2', 'ymtics1', 'ymtics2', 'datawc_x1', 'datawc_x2', ...] 

 g_name  = <member 'g_name' of 'GSp' objects>

 parent  = <member 'parent' of 'GSp' objects>

 setmember  = <member 'setmember' of 'GSp' objects>

  
 Functions 

` `

 getGSpmember  (self, member) 
     ` ###############################################################################   
#
#  
#&#160;Function:&#160;&#160;&#160;&#160;&#160;getGSpmember
#  
#
#  
#&#160;Description&#160;of&#160;Function:
#  
#&#160;&#160;&#160;&#160;&#160;&#160;&#160;Private&#160;function&#160;that&#160;retrieves&#160;the&#160;scatter&#160;members&#160;from&#160;the&#160;C
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
# [ getGSpmember ](/) (self,name)
#  
#&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;where:&#160;self&#160;is&#160;the&#160;class&#160;(e.g., [ GSp ](/) )
#  
#&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;name&#160;is&#160;the&#160;name&#160;of&#160;the&#160;member&#160;that&#160;is&#160;being&#160;found
#  
#
#  
##############################################################################
# `

 getmember  = getGSpmember(self, member) 
     ` ###############################################################################   
#
#  
#&#160;Function:&#160;&#160;&#160;&#160;&#160;getGSpmember
#  
#
#  
#&#160;Description&#160;of&#160;Function:
#  
#&#160;&#160;&#160;&#160;&#160;&#160;&#160;Private&#160;function&#160;that&#160;retrieves&#160;the&#160;scatter&#160;members&#160;from&#160;the&#160;C
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
# [ getGSpmember ](/) (self,name)
#  
#&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;where:&#160;self&#160;is&#160;the&#160;class&#160;(e.g., [ GSp ](/) )
#  
#&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;name&#160;is&#160;the&#160;name&#160;of&#160;the&#160;member&#160;that&#160;is&#160;being&#160;found
#  
#
#  
##############################################################################
# `

 renameGSp  (self, old_name, new_name) 
     ` ###############################################################################   
#
#  
#&#160;Function:&#160;&#160;&#160;&#160;&#160;renameGSp
#  
#
#  
#&#160;Description&#160;of&#160;Function:
#  
#&#160;&#160;&#160;&#160;&#160;&#160;&#160;Private&#160;function&#160;that&#160;renames&#160;the&#160;name&#160;of&#160;an&#160;existing&#160;scatter
#  
#&#160;&#160;&#160;&#160;&#160;&#160;&#160;graphics&#160;method.
#  
#
#  
#
#  
#&#160;Example&#160;of&#160;Use:
#  
# [ renameGSp ](/) (old_name,&#160;new_name)
#  
#&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;where:&#160;old_name&#160;is&#160;the&#160;current&#160;name&#160;of&#160;scatter&#160;graphics&#160;method
#  
#&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;new_name&#160;is&#160;the&#160;new&#160;name&#160;for&#160;the&#160;scatter&#160;graphics
method#  
#
#  
##############################################################################
# `

 setGSpmember  (self, member, value) 
     ` ###############################################################################   
#
#  
#&#160;Function:&#160;&#160;&#160;&#160;&#160;setGSpmember
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
# [ setGSpmember ](/) (self,name,value)
#  
#&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;where:&#160;self&#160;is&#160;the&#160;class&#160;(e.g., [ GSp ](/) )
#  
#&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;name&#160;is&#160;the&#160;name&#160;of&#160;the&#160;member&#160;that&#160;is&#160;being&#160;changed
#  
#&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;value&#160;is&#160;the&#160;new&#160;value&#160;of&#160;the&#160;member&#160;(or&#160;attribute)
#  
#
#  
##############################################################################
# `

 setmember  = setGSpmember(self, member, value) 
     ` ###############################################################################   
#
#  
#&#160;Function:&#160;&#160;&#160;&#160;&#160;setGSpmember
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
# [ setGSpmember ](/) (self,name,value)
#  
#&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;where:&#160;self&#160;is&#160;the&#160;class&#160;(e.g., [ GSp ](/) )
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

