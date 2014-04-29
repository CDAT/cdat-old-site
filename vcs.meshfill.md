---
layout: default
title:
---

 [ Skip to content. ](/cdat/source/api-reference/vcs.meshfill.html) | [ Skip to
navigation ](/cdat/source/api-reference/vcs.meshfill.html)

Search Site

[ Advanced Search&#8230; ](/search_form)

#  [ PCMDI Software Portal ](/)

#####  Sections

  * [ Home ](/)

#####  Personal tools

  * [ Log in ](/login_form)

You are here:  [ Home ](/) -> [ CDAT ](/cdat) -> [ Source Code ](/cdat/source)
-> [ API Reference ](/cdat/source/api-reference) -> Python: module
vcs.meshfill

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

        * [ Python: module vcs.meshfill ](/cdat/source/api-reference/vcs.meshfill.html)

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

  * [ ![Send this page to somebody](media/mail_icon.gif) ](/cdat/source/api-reference/vcs.meshfill.html/sendto_form)
  * [ ![Print this page](media/print_icon.gif) ](/this.print\(\))

#  Python: module vcs.meshfill

  
  
 [ vcs  ](/vcs.html) .meshfill 
[ index ](/)  

` #&#160;Meshfill&#160;( [ Gfm ](/) )&#160;module `

  
 Modules 

` `

[ vcs.Canvas ](/vcs.Canvas.html)  

[ vcs.VCS_validation_functions ](/vcs.VCS_validation_functions.html)  

[ vcs._vcs ](/vcs._vcs.html)  

  
 Classes 

` `

[ __builtin__.object ](/__builtin__.html)

    

[ Gfm ](/vcs.meshfill.html)

  
class  Gfm  ( [ __builtin__.object ](/__builtin__.html) )

` `

` Class: [ Gfm ](/) #&#160;Meshfill  
  
Description&#160;of [ Gfm ](/) Class:  
The&#160;meshfill&#160;graphics&#160;method&#160;( [ Gfm ](/) )&#160;displays&#160;a&#160;two-dimensional&#160;data
array  
by&#160;surrounding&#160;each&#160;data&#160;value&#160;by&#160;a&#160;colored&#160;grid&#160;mesh.  
  
This&#160;class&#160;is&#160;used&#160;to&#160;define&#160;a&#160;meshfill&#160;table&#160;entry&#160;used&#160;in&#160;VCS,&#160;or&#160;it  
can&#160;be&#160;used&#160;to&#160;change&#160;some&#160;or&#160;all&#160;of&#160;the&#160;attributes&#160;in&#160;an&#160;existing  
meshfill&#160;table&#160;entry  
.  
Other&#160;Useful&#160;Functions:  
a=vcs.init()&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#&#160;Constructor  
a.show('meshfill')&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#&#160;Show&#160;predefined&#160;meshfill&#160;graphics&#160;methods  
a.setcolormap("AMIP")&#160;&#160;&#160;&#160;#&#160;Change&#160;the&#160;VCS&#160;color&#160;map  
a.meshfill(s,b,'default')&#160;#&#160;Plot&#160;data&#160;'s'&#160;with&#160;meshfill&#160;'b'&#160;and  
'default'&#160;template  
a.update()&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#&#160;Updates&#160;the&#160;VCS&#160;Canvas&#160;at&#160;user's&#160;request  
a.mode=1,&#160;or&#160;0&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#&#160;If&#160;1,&#160;then&#160;automatic&#160;update,&#160;else&#160;if  
0,&#160;then&#160;use&#160;the&#160;update&#160;function&#160;to  
update&#160;the&#160;VCS&#160;Canvas.  
  
Example&#160;of&#160;Use:  
a=vcs.init()  
To&#160;Create&#160;a&#160;new&#160;instance&#160;of&#160;meshfill&#160;use:  
mesh=a.createmeshfill('new','quick')&#160;#&#160;Copies&#160;content&#160;of&#160;'quick'&#160;to&#160;'new'  
mesh=a.createmeshfill('new')&#160;&#160;&#160;&#160;&#160;&#160;&#160;#&#160;Copies&#160;content&#160;of&#160;'default'&#160;to&#160;'new'  
  
To&#160;Modify&#160;an&#160;existing&#160;meshfill&#160;use:  
mesh=a.getmeshfill('AMIP_psl')  
  
mesh. [ list ](/) ()&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#&#160;Will&#160;list&#160;all&#160;the&#160;meshfill
attribute&#160;values  
mesh.projection='linear'  
lon30={-180:'180W',-150:'150W',0:'Eq'}  
mesh.xticlabels1=lon30  
mesh.xticlabels2=lon30  
mesh. [ xticlabels ](/) (lon30,&#160;lon30)&#160;&#160;&#160;&#160;&#160;&#160;&#160;#&#160;Will&#160;set&#160;them&#160;both  
mesh.xmtics1=''  
mesh.xmtics2=''  
mesh. [ xmtics ](/) (lon30,&#160;lon30)&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#&#160;Will&#160;set&#160;them&#160;both  
mesh.yticlabels1=lat10  
mesh.yticlabels2=lat10  
mesh. [ yticlabels ](/) (lat10,&#160;lat10)&#160;&#160;&#160;&#160;&#160;&#160;&#160;#&#160;Will&#160;set&#160;them&#160;both  
mesh.ymtics1=''  
mesh.ymtics2=''  
mesh. [ ymtics ](/) (lat10,&#160;lat10)&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#&#160;Will&#160;set&#160;them&#160;both  
mesh.datawc_y1=-90.0  
mesh.datawc_y2=90.0  
mesh.datawc_x1=-180.0  
mesh.datawc_x2=180.0  
mesh. [ datawc ](/) (-90,&#160;90,&#160;-180,&#160;180)&#160;&#160;&#160;&#160;&#160;#&#160;Will&#160;set&#160;them&#160;all  
There&#160;are&#160;two&#160;possibilities&#160;for&#160;setting&#160;the&#160;meshfill&#160;levels:  
A)&#160;Levels&#160;are&#160;all&#160;contiguous&#160;(Examples):  
mesh.levels=([0,20,25,30,35,40],)  
mesh.levels=([0,20,25,30,35,40,45,50])  
mesh.levels=[0,20,25,30,35,40]  
mesh.levels=(0.0,20.0,25.0,30.0,35.0,40.0,50.0)  
B)&#160;Levels&#160;are&#160;not&#160;contiguous&#160;(Examples):  
mesh.levels=([0,20],[30,40],[50,60])  
mesh.levels=([0,20,25,30,35,40],[30,40],[50,60])  
  
There&#160;are&#160;three&#160;possibilities&#160;for&#160;setting&#160;the&#160;fillarea&#160;color&#160;indices&#160;(Ex):  
mesh.fillareacolors=([22,33,44,55,66,77])  
mesh.fillareacolors=(16,19,33,44)  
mesh.fillareacolors=None  
  
There&#160;are&#160;three&#160;possibilities&#160;for&#160;setting&#160;the&#160;fillarea&#160;style&#160;(Ex):  
mesh.fillareastyle&#160;=&#160;'solid'  
mesh.fillareastyle&#160;=&#160;'hatch'  
mesh.fillareastyle&#160;=&#160;'pattern'  
  
There&#160;are&#160;two&#160;ways&#160;to&#160;set&#160;the&#160;fillarea&#160;hatch&#160;or&#160;pattern&#160;indices&#160;(Ex):  
mesh.fillareaindices=([1,3,5,6,9,20])  
mesh.fillareaindices=(7,1,4,9,6,15)  
See&#160;using&#160;fillarea&#160;objects&#160;below!  
  
Using&#160;the&#160;fillarea&#160;secondary [ object ](/__builtin__.html) (Ex):  
f=createfillarea('fill1')  
To&#160;Create&#160;a&#160;new&#160;instance&#160;of&#160;fillarea&#160;use:  
fill=a.createfillarea('new','quick')&#160;#&#160;Copies&#160;'quick'&#160;to&#160;'new'  
fill=a.createfillarea('new')&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#&#160;Copies&#160;'default'&#160;to&#160;'new'  
  
To&#160;Modify&#160;an&#160;existing&#160;fillarea&#160;use:  
fill=a.getmfillarea('def37')  
  
mesh.fillareaindices=(7,fill,4,9,fill,15)&#160;#&#160;Set&#160;index&#160;using&#160;fillarea  
fill. [ list ](/) ()&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#&#160;list&#160;fillarea&#160;attributes  
fill.style='hatch'&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#&#160;change&#160;style  
fill.color=241&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#&#160;change&#160;color  
fill.index=3&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#&#160;change&#160;style&#160;index  
  
ext_1='n'  
ext_2='y'  
mesh. [ exts ](/) ('n',&#160;'y'&#160;)&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#&#160;Will&#160;set&#160;them&#160;both  
missing=241&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#&#160;Color&#160;index&#160;value&#160;range&#160;0&#160;to&#160;255  
`

Methods defined here:  

 __init__  (self, parent, Gfm_name  =None  , Gfm_name_src  ='default'  , createGfm  =0  ) 

 colors  (self, color1  =16  , color2  =239  ) 

 datawc  (self, dsp1  =1e+20  , dsp2  =1e+20  , dsp3  =1e+20  , dsp4  =1e+20  ) 

 exts  (self, ext1  ='n'  , ext2  ='y'  ) 

 list  (self) 
     ` #############################################################################   
#&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#  
#&#160;List&#160;out&#160;meshfill&#160;graphics&#160;method&#160;members&#160;(attributes).&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#  
#&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#  
#############################################################################
`

 rename  = renameGfm(self, old_name, new_name) 
     ` #################################################################################   
#
#  
#&#160;Function:&#160;&#160;&#160;&#160;&#160;renameGfm
#  
#
#  
#&#160;Description&#160;of&#160;Function:
#  
#&#160;&#160;&#160;&#160;&#160;&#160;&#160;Private&#160;function&#160;that&#160;renames&#160;the&#160;name&#160;of&#160;an&#160;existing&#160;meshfill
#  
#&#160;&#160;&#160;&#160;&#160;&#160;&#160;graphics&#160;method.
#  
#
#  
#
#  
#&#160;Example&#160;of&#160;Use:
#  
# [ renameGfm ](/) (old_name,&#160;new_name)
#  
#&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;where:&#160;old_name&#160;is&#160;the&#160;current&#160;name&#160;of&#160;meshfill&#160;graphics&#160;method
#  
#&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;new_name&#160;is&#160;the&#160;new&#160;name&#160;for&#160;the&#160;meshfill&#160;graphics
method&#160;&#160;#  
#
#  
##############################################################################
## `

 script  (self, script_filename  =None  , mode  =None  ) 
     ` Function:&#160;&#160;&#160;&#160;&#160;script&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#&#160;Calls&#160;_vcs.scriptGfm   
  
Description&#160;of&#160;Function:  
Saves&#160;out&#160;a&#160;meshfill&#160;graphics&#160;method&#160;in&#160;Python&#160;or&#160;VCS&#160;script&#160;form&#160;to&#160;a  
designated&#160;file.  
  
Example&#160;of&#160;Use:  
[ script ](/) (scriptfile_name,&#160;mode)  
where:&#160;scriptfile_name&#160;is&#160;the&#160;output&#160;name&#160;of&#160;the&#160;script&#160;file.  
mode&#160;is&#160;either&#160;'w'&#160;for&#160;replace&#160;or&#160;'a'&#160;for&#160;append.  
  
Note:&#160;If&#160;the&#160;the&#160;filename&#160;has&#160;a&#160;'.py'&#160;at&#160;the&#160;end,&#160;it&#160;will&#160;produce&#160;a  
Python&#160;script.&#160;If&#160;the&#160;filename&#160;has&#160;a&#160;'.scr'&#160;at&#160;the&#160;end,&#160;it&#160;will  
produce&#160;a&#160;VCS&#160;script.&#160;If&#160;neither&#160;extensions&#160;are&#160;give,&#160;then&#160;by  
default&#160;a&#160;Python&#160;script&#160;will&#160;be&#160;produced.  
  
a=vcs.init()  
mesh=a.createmeshfill('temp')  
mesh. [ script ](/) ('filename.py')&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#&#160;Append&#160;to&#160;a&#160;Python&#160;file
'filename.py'  
mesh. [ script ](/) ('filename.scr')&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#&#160;Append&#160;to&#160;a&#160;VCS&#160;file
'filename.scr'  
mesh. [ script ](/) ('filename','w') `

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

 ext_1 
    

 _ get _  = _getext_1(self) 
    

 _ set _  = _setext_1(self, value) 

 ext_2 
    

 _ get _  = _getext_2(self) 
    

 _ set _  = _setext_2(self, value) 

 fillareacolors 
    

 _ get _  = _getfillareacolors(self) 
    

 _ set _  = _setfillareacolors(self, value) 

 fillareaindices 
    

 _ get _  = _getfillareaindices(self) 
    

 _ set _  = _setfillareaindices(self, value) 

 fillareastyle 
    

 _ get _  = _getfillareastyle(self) 
    

 _ set _  = _setfillareastyle(self, value) 

 legend 
    

 _ get _  = _getlegend(self) 
    

 _ set _  = _setlegend(self, value) 

 levels 
    

 _ get _  = _getlevels(self) 
    

 _ set _  = _setlevels(self, value) 

 mesh 
    

 _ get _  = _getmesh(self) 
    

 _ set _  = _setmesh(self, value) 

 missing 
    

 _ get _  = _getmissing(self) 
    

 _ set _  = _setmissing(self, value) 

 name 
    

 _ get _  = _getname(self) 
    

 _ set _  = _setname(self, value) 

 projection 
    

 _ get _  = _getprojection(self) 
    

 _ set _  = _setprojection(self, value) 

 wrap 
    

 _ get _  = _getwrap(self) 
    

 _ set _  = _setwrap(self, value) 

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

 __slots__  = ['setmember', 'parent', 'name', 'g_name', 'xaxisconvert', 'yaxisconvert', 'levels', 'fillareacolors', 'fillareastyle', 'fillareaindices', 'ext_1', 'ext_2', 'missing', 'projection', 'xticlabels1', 'xticlabels2', 'yticlabels1', 'yticlabels2', 'xmtics1', 'xmtics2', ...] 

 g_name  = <member 'g_name' of 'Gfm' objects>

 parent  = <member 'parent' of 'Gfm' objects>

 setmember  = <member 'setmember' of 'Gfm' objects>

  
 Functions 

` `

 add_level_ext_1  (self, ext_value) 
     ` #################################################################################   
#
#  
#&#160;Function:&#160;&#160;&#160;&#160;&#160;add_level_ext_1
#  
#
#  
#&#160;Description&#160;of&#160;Function:
#  
#&#160;&#160;&#160;&#160;&#160;&#160;&#160;Private&#160;function&#160;that&#160;adds&#160;the&#160;extension&#160;triangle&#160;to&#160;the&#160;left&#160;of&#160;the
#  
#&#160;&#160;&#160;&#160;&#160;&#160;&#160;legend&#160;on&#160;the&#160;plot
#  
#
#  
#
#  
#&#160;Example&#160;of&#160;Use:
#  
# [ add_level_ext_1 ](/) (self,&#160;ext_value)
#  
#&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;where:&#160;self&#160;is&#160;the&#160;class&#160;(e.g.,&#160;Gfi)
#  
#&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;ext_value&#160;is&#160;either&#160;'n'&#160;to&#160;remove&#160;the&#160;triangle&#160;on&#160;the
#  
#&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;legend&#160;or&#160;'y'&#160;to&#160;show&#160;the&#160;triangle&#160;on&#160;the&#160;triangle
#  
#
#  
##############################################################################
### `

 add_level_ext_2  (self, ext_value) 
     ` #################################################################################   
#
#  
#&#160;Function:&#160;&#160;&#160;&#160;&#160;add_level_ext_2
#  
#
#  
#&#160;Description&#160;of&#160;Function:
#  
#&#160;&#160;&#160;&#160;&#160;&#160;&#160;Private&#160;function&#160;that&#160;adds&#160;the&#160;extension&#160;triangle&#160;to&#160;the&#160;right&#160;of&#160;the
#  
#&#160;&#160;&#160;&#160;&#160;&#160;&#160;legend&#160;on&#160;the&#160;plot
#  
#
#  
#
#  
#&#160;Example&#160;of&#160;Use:
#  
# [ add_level_ext_2 ](/) (self,&#160;ext_value)
#  
#&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;where:&#160;self&#160;is&#160;the&#160;class&#160;(e.g.,&#160;Gfi)
#  
#&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;ext_value&#160;is&#160;either&#160;'n'&#160;to&#160;remove&#160;the&#160;triangle&#160;on&#160;the
#  
#&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;legend&#160;or&#160;'y'&#160;to&#160;show&#160;the&#160;triangle&#160;on&#160;the&#160;triangle
#  
#
#  
##############################################################################
### `

 getGfmmember  (self, member) 

 getmember  = getGfmmember(self, member) 

 renameGfm  (self, old_name, new_name) 
     ` #################################################################################   
#
#  
#&#160;Function:&#160;&#160;&#160;&#160;&#160;renameGfm
#  
#
#  
#&#160;Description&#160;of&#160;Function:
#  
#&#160;&#160;&#160;&#160;&#160;&#160;&#160;Private&#160;function&#160;that&#160;renames&#160;the&#160;name&#160;of&#160;an&#160;existing&#160;meshfill
#  
#&#160;&#160;&#160;&#160;&#160;&#160;&#160;graphics&#160;method.
#  
#
#  
#
#  
#&#160;Example&#160;of&#160;Use:
#  
# [ renameGfm ](/) (old_name,&#160;new_name)
#  
#&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;where:&#160;old_name&#160;is&#160;the&#160;current&#160;name&#160;of&#160;meshfill&#160;graphics&#160;method
#  
#&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;new_name&#160;is&#160;the&#160;new&#160;name&#160;for&#160;the&#160;meshfill&#160;graphics
method&#160;&#160;#  
#
#  
##############################################################################
## `

 setGfmmember  (self, member, value) 
     ` ###############################################################################   
#
#  
#&#160;Function:&#160;&#160;&#160;&#160;&#160;setGfmmember
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
# [ setGfmmember ](/) (self,name,value)
#  
#&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;where:&#160;self&#160;is&#160;the&#160;class&#160;(e.g., [ Gfm ](/) )
#  
#&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;name&#160;is&#160;the&#160;name&#160;of&#160;the&#160;member&#160;that&#160;is&#160;being&#160;changed
#  
#&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;value&#160;is&#160;the&#160;new&#160;value&#160;of&#160;the&#160;member&#160;(or&#160;attribute)
#  
#
#  
##############################################################################
# `

 setmember  = setGfmmember(self, member, value) 
     ` ###############################################################################   
#
#  
#&#160;Function:&#160;&#160;&#160;&#160;&#160;setGfmmember
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
# [ setGfmmember ](/) (self,name,value)
#  
#&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;where:&#160;self&#160;is&#160;the&#160;class&#160;(e.g., [ Gfm ](/) )
#  
#&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;name&#160;is&#160;the&#160;name&#160;of&#160;the&#160;member&#160;that&#160;is&#160;being&#160;changed
#  
#&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;value&#160;is&#160;the&#160;new&#160;value&#160;of&#160;the&#160;member&#160;(or&#160;attribute)
#  
#
#  
##############################################################################
# `

* * *

UCRL-WEB-213937 | [ Privacy & Legal Notice ](/disclaimer.html)

[ webmaster@pcmdi.llnl.gov ](/webmaster@pcmdi.llnl.gov)

[ ![Powered by Plone](media/plone_powered.gif) ](/)

