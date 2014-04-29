---
layout: default
title:
---

 [ Skip to content. ](/cdat/source/api-reference/vcs.isofill.html) | [ Skip to
navigation ](/cdat/source/api-reference/vcs.isofill.html)

Search Site

[ Advanced Search&#8230; ](/search_form)

#  [ PCMDI Software Portal ](/)

#####  Sections

  * [ Home ](/)

#####  Personal tools

  * [ Log in ](/login_form)

You are here:  [ Home ](/) -> [ CDAT ](/cdat) -> [ Source Code ](/cdat/source)
-> [ API Reference ](/cdat/source/api-reference) -> Python: module vcs.isofill

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

        * [ Python: module vcs.isofill ](/cdat/source/api-reference/vcs.isofill.html)

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

  * [ ![Send this page to somebody](media/mail_icon.gif) ](/cdat/source/api-reference/vcs.isofill.html/sendto_form)
  * [ ![Print this page](media/print_icon.gif) ](/this.print\(\))

#  Python: module vcs.isofill

  
  
 [ vcs  ](/vcs.html) .isofill 
[ index ](/)  

` #&#160;Isofill&#160;( [ Gfi ](/) )&#160;module `

  
 Modules 

` `

[ vcs.Canvas ](/vcs.Canvas.html)  
[ vcs.VCS_validation_functions ](/vcs.VCS_validation_functions.html)  

[ vcs._vcs ](/vcs._vcs.html)  
[ cdtime ](/cdtime.html)  

[ vcs ](/vcs.html)  

  
 Classes 

` `

[ __builtin__.object ](/__builtin__.html)

    

[ Gfi ](/vcs.isofill.html)

  
class  Gfi  ( [ __builtin__.object ](/__builtin__.html) )

` `

` Class: [ Gfi ](/) #&#160;Isofill  
  
Description&#160;of&#160;Gfb&#160;Class:  
The&#160;Isofill&#160;graphics&#160;method&#160;fills&#160;the&#160;area&#160;between&#160;selected&#160;isolevels  
(levels&#160;of&#160;constant&#160;value)&#160;of&#160;a&#160;two-dimensional&#160;array&#160;with&#160;a  
user-specified&#160;color.&#160;The&#160;example&#160;below&#160;shows&#160;how&#160;to&#160;display&#160;an&#160;isofill  
plot&#160;on&#160;the&#160;VCS&#160;Canvas&#160;and&#160;how&#160;to&#160;create&#160;and&#160;remove&#160;isofill&#160;isolevels.  
  
This&#160;class&#160;is&#160;used&#160;to&#160;define&#160;an&#160;isofill&#160;table&#160;entry&#160;used&#160;in&#160;VCS,&#160;or&#160;it  
can&#160;be&#160;used&#160;to&#160;change&#160;some&#160;or&#160;all&#160;of&#160;the&#160;isofill&#160;attributes&#160;in&#160;an  
existing&#160;isofill&#160;table&#160;entry.  
  
Other&#160;Useful&#160;Functions:  
a=vcs.init()&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#&#160;Constructor  
a.show('isofill')&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#&#160;Show&#160;predefined&#160;isofill&#160;graphics&#160;methods  
a.show('fillarea')&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#&#160;Show&#160;predefined&#160;fillarea&#160;objects  
a.show('template')&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#&#160;Show&#160;predefined&#160;fillarea&#160;objects  
a.setcolormap("AMIP")&#160;&#160;&#160;&#160;&#160;&#160;#&#160;Change&#160;the&#160;VCS&#160;color&#160;map  
a.createtemplate('test')&#160;&#160;&#160;#&#160;Create&#160;a&#160;template  
a.createfillarea('fill')&#160;&#160;&#160;#&#160;Create&#160;a&#160;fillarea  
a.gettemplate('AMIP')&#160;&#160;&#160;&#160;&#160;&#160;#&#160;Get&#160;an&#160;existing&#160;template  
a.getfillarea('def37')&#160;&#160;&#160;&#160;&#160;#&#160;Get&#160;an&#160;existing&#160;fillarea  
a.isofill(s,i,t)&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#&#160;Plot&#160;array&#160;'s'&#160;with&#160;isofill&#160;'i'&#160;and  
template&#160;'t'  
a.update()&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#&#160;Updates&#160;the&#160;VCS&#160;Canvas&#160;at&#160;user's&#160;request  
a.mode=1,&#160;or&#160;0&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#&#160;If&#160;1,&#160;then&#160;automatic&#160;update,&#160;else&#160;if  
0,&#160;then&#160;use&#160;update&#160;function&#160;to  
update&#160;the&#160;VCS&#160;Canvas.  
  
Example&#160;of&#160;Use:  
a=vcs.init()  
To&#160;Create&#160;a&#160;new&#160;instance&#160;of&#160;isofill&#160;use:  
iso=a.createisofill('new','quick')&#160;#&#160;Copies&#160;content&#160;of&#160;'quick'&#160;to&#160;'new'  
iso=a.createisofill('new')&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#&#160;Copies&#160;content&#160;of&#160;'default'&#160;to&#160;'new'  
  
To&#160;Modify&#160;an&#160;existing&#160;isofill&#160;use:  
iso=a.getisofill('AMIP_psl')  
  
iso. [ list ](/) ()&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#&#160;Will&#160;list&#160;all&#160;the&#160;isofill
attribute&#160;values  
iso.projection='linear'  
lon30={-180:'180W',-150:'150W',0:'Eq'}  
iso.xticlabels1=lon30  
iso.xticlabels2=lon30  
iso. [ xticlabels ](/) (lon30,&#160;lon30)&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#&#160;Will&#160;set&#160;them&#160;both  
iso.xmtics1=''  
iso.xmtics2=''  
iso. [ xmtics ](/) (lon30,&#160;lon30)&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#&#160;Will&#160;set&#160;them&#160;both  
iso.yticlabels1=lat10  
iso.yticlabels2=lat10  
iso. [ yticlabels ](/) (lat10,&#160;lat10)&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#&#160;Will&#160;set&#160;them&#160;both  
iso.ymtics1=''  
iso.ymtics2=''  
iso. [ ymtics ](/) (lat10,&#160;lat10)&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#&#160;Will&#160;set&#160;them&#160;both  
iso.datawc_y1=-90.0  
iso.datawc_y2=90.0  
iso.datawc_x1=-180.0  
iso.datawc_x2=180.0  
iso. [ datawc ](/) (-90,&#160;90,&#160;-180,&#160;180)&#160;&#160;&#160;&#160;&#160;&#160;#&#160;Will&#160;set&#160;them&#160;all  
xaxisconvert='linear'  
yaxisconvert='linear'  
iso. [ xyscale ](/) ('linear',&#160;'area_wt')&#160;&#160;&#160;&#160;#&#160;Will&#160;set&#160;them&#160;both  
missing=241&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#&#160;Color&#160;index&#160;value&#160;range&#160;0&#160;to&#160;255  
  
iso.legend=None  
  
There&#160;are&#160;two&#160;possibilities&#160;for&#160;setting&#160;the&#160;isofill&#160;levels:  
A)&#160;Levels&#160;are&#160;all&#160;contiguous&#160;(Examples):  
iso.levels=([0,20,25,30,35,40],)  
iso.levels=([0,20,25,30,35,40,45,50])  
iso.levels=[0,20,25,30,35,40]  
iso.levels=(0.0,20.0,25.0,30.0,35.0,40.0,50.0)  
B)&#160;Levels&#160;are&#160;not&#160;contiguous&#160;(Examples):  
iso.levels=([0,20],[30,40],[50,60])  
iso.levels=([0,20,25,30,35,40],[30,40],[50,60])  
  
There&#160;are&#160;three&#160;possibilities&#160;for&#160;setting&#160;the&#160;fillarea&#160;color&#160;indices&#160;(Ex):  
iso.fillareacolors=([22,33,44,55,66,77])  
iso.fillareacolors=(16,19,33,44)  
iso.fillareacolors=None  
  
There&#160;are&#160;three&#160;possibilities&#160;for&#160;setting&#160;the&#160;fillarea&#160;style&#160;(Ex):  
iso.fillareastyle&#160;=&#160;'solid'  
iso.fillareastyle&#160;=&#160;'hatch'  
iso.fillareastyle&#160;=&#160;'pattern'  
  
There&#160;are&#160;two&#160;ways&#160;to&#160;set&#160;the&#160;fillarea&#160;hatch&#160;or&#160;pattern&#160;indices&#160;(Ex):  
iso.fillareaindices=([1,3,5,6,9,20])  
iso.fillareaindices=(7,1,4,9,6,15)  
See&#160;using&#160;fillarea&#160;objects&#160;below!  
  
Using&#160;the&#160;fillarea&#160;secondary [ object ](/__builtin__.html) (Ex):  
f=createfillarea('fill1')  
To&#160;Create&#160;a&#160;new&#160;instance&#160;of&#160;fillarea&#160;use:  
fill=a.createisofill('new','quick')&#160;#&#160;Copies&#160;'quick'&#160;to&#160;'new'  
fill=a.createisofill('new')&#160;&#160;#&#160;Copies&#160;'default'&#160;to&#160;'new'  
  
To&#160;Modify&#160;an&#160;existing&#160;isofill&#160;use:  
fill=a.getisofill('def37')  
  
iso.fillareaindices=(7,fill,4,9,fill,15)&#160;#&#160;Set&#160;index&#160;using&#160;fillarea  
fill. [ list ](/) ()&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#&#160;list&#160;fillarea&#160;attributes  
fill.style='hatch'&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#&#160;change&#160;style  
fill.color=241&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#&#160;change&#160;color  
fill.index=3&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#&#160;change&#160;style&#160;index  
  
ext_1='n'  
ext_2='y'  
iso. [ exts ](/) ('n',&#160;'y'&#160;)&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#&#160;Will&#160;set&#160;them&#160;both  
`

Methods defined here:  

 __init__  (self, parent, Gfi_name  =None  , Gfi_name_src  ='default'  , createGfi  =0  ) 

 datawc  (self, dsp1  =1e+20  , dsp2  =1e+20  , dsp3  =1e+20  , dsp4  =1e+20  ) 

 exts  (self, ext1  ='n'  , ext2  ='y'  ) 

 list  (self) 

 rename  = renameGfi(self, old_name, new_name) 
     ` ###############################################################################   
#
#  
#&#160;Function:&#160;&#160;&#160;&#160;&#160;renameGfi
#  
#
#  
#&#160;Description&#160;of&#160;Function:
#  
#&#160;&#160;&#160;&#160;&#160;&#160;&#160;Private&#160;function&#160;that&#160;renames&#160;the&#160;name&#160;of&#160;an&#160;existing&#160;isofill
#  
#&#160;&#160;&#160;&#160;&#160;&#160;&#160;graphics&#160;method.
#  
#
#  
#
#  
#&#160;Example&#160;of&#160;Use:
#  
# [ renameGfi ](/) (old_name,&#160;new_name)
#  
#&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;where:&#160;old_name&#160;is&#160;the&#160;current&#160;name&#160;of&#160;isofill&#160;graphics&#160;method
#  
#&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;new_name&#160;is&#160;the&#160;new&#160;name&#160;for&#160;the&#160;isofill&#160;graphics
method#  
#
#  
##############################################################################
# `

 script  (self, script_filename  =None  , mode  =None  ) 
     ` Function:&#160;&#160;&#160;&#160;&#160;script&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#&#160;Calls&#160;_vcs.scriptGfi   
  
Description&#160;of&#160;Function:  
Saves&#160;out&#160;a&#160;isofill&#160;graphics&#160;method&#160;in&#160;Python&#160;or&#160;VCS&#160;script&#160;form&#160;to  
a&#160;designated&#160;file.  
  
Example&#160;of&#160;Use:  
[ script ](/) (scriptfile_name,&#160;mode)  
where:&#160;scriptfile_name&#160;is&#160;the&#160;output&#160;name&#160;of&#160;the&#160;script&#160;file.  
mode&#160;is&#160;either&#160;"w"&#160;for&#160;replace&#160;or&#160;"a"&#160;for&#160;append.  
  
Note:&#160;If&#160;the&#160;the&#160;filename&#160;has&#160;a&#160;".py"&#160;at&#160;the&#160;end,&#160;it&#160;will&#160;produce&#160;a  
Python&#160;script.&#160;If&#160;the&#160;filename&#160;has&#160;a&#160;".scr"&#160;at&#160;the&#160;end,&#160;it&#160;will  
produce&#160;a&#160;VCS&#160;script.&#160;If&#160;neither&#160;extensions&#160;are&#160;give,&#160;then&#160;by  
default&#160;a&#160;Python&#160;script&#160;will&#160;be&#160;produced.  
  
a=vcs.init()  
iso=a.createisofill('temp')  
iso. [ script ](/) ('filename.py')&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#&#160;Append&#160;to&#160;a&#160;Python&#160;file
"filename.py"  
iso. [ script ](/) ('filename.scr')&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#&#160;Append&#160;to&#160;a&#160;VCS&#160;file
"filename.scr"  
iso. [ script ](/) ('filename','w') `

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

 missing 
    

 _ get _  = _getmissing(self) 
    

 _ set _  = _setmissing(self, value) 

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

 __slots__  = ['setmember', 'parent', 'name', 'g_name', 'xaxisconvert', 'yaxisconvert', 'levels', 'fillareacolors', 'fillareastyle', 'fillareaindices', 'ext_1', 'ext_2', 'missing', 'projection', 'xticlabels1', 'xticlabels2', 'yticlabels1', 'yticlabels2', 'xmtics1', 'xmtics2', ...] 

 g_name  = <member 'g_name' of 'Gfi' objects>

 parent  = <member 'parent' of 'Gfi' objects>

 setmember  = <member 'setmember' of 'Gfi' objects>

  
 Functions 

` `

 add_level_ext_1  (self, ext_value) 
     ` ###############################################################################   
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
#&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;where:&#160;self&#160;is&#160;the&#160;class&#160;(e.g., [ Gfi ](/) )
#  
#&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;ext_value&#160;is&#160;either&#160;'n'&#160;to&#160;remove&#160;the&#160;triangle&#160;on&#160;the
#  
#&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;legend&#160;or&#160;'y'&#160;to&#160;show&#160;the&#160;triangle&#160;on&#160;the&#160;triangle
#  
#
#  
##############################################################################
# `

 add_level_ext_2  (self, ext_value) 
     ` ###############################################################################   
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
#&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;where:&#160;self&#160;is&#160;the&#160;class&#160;(e.g., [ Gfi ](/) )
#  
#&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;ext_value&#160;is&#160;either&#160;'n'&#160;to&#160;remove&#160;the&#160;triangle&#160;on&#160;the
#  
#&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;legend&#160;or&#160;'y'&#160;to&#160;show&#160;the&#160;triangle&#160;on&#160;the&#160;triangle
#  
#
#  
##############################################################################
# `

 getGfimember  (self, member) 
     ` ###############################################################################   
#
#  
#&#160;Function:&#160;&#160;&#160;&#160;&#160;getGfimember
#  
#
#  
#&#160;Description&#160;of&#160;Function:
#  
#&#160;&#160;&#160;&#160;&#160;&#160;&#160;Private&#160;function&#160;that&#160;retrieves&#160;the&#160;isofill&#160;members&#160;from&#160;the&#160;C
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
# [ getGfimember ](/) (self,name)
#  
#&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;where:&#160;self&#160;is&#160;the&#160;class&#160;(e.g., [ Gfi ](/) )
#  
#&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;name&#160;is&#160;the&#160;name&#160;of&#160;the&#160;member&#160;that&#160;is&#160;being&#160;found
#  
#
#  
##############################################################################
# `

 getmember  = getGfimember(self, member) 
     ` ###############################################################################   
#
#  
#&#160;Function:&#160;&#160;&#160;&#160;&#160;getGfimember
#  
#
#  
#&#160;Description&#160;of&#160;Function:
#  
#&#160;&#160;&#160;&#160;&#160;&#160;&#160;Private&#160;function&#160;that&#160;retrieves&#160;the&#160;isofill&#160;members&#160;from&#160;the&#160;C
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
# [ getGfimember ](/) (self,name)
#  
#&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;where:&#160;self&#160;is&#160;the&#160;class&#160;(e.g., [ Gfi ](/) )
#  
#&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;name&#160;is&#160;the&#160;name&#160;of&#160;the&#160;member&#160;that&#160;is&#160;being&#160;found
#  
#
#  
##############################################################################
# `

 renameGfi  (self, old_name, new_name) 
     ` ###############################################################################   
#
#  
#&#160;Function:&#160;&#160;&#160;&#160;&#160;renameGfi
#  
#
#  
#&#160;Description&#160;of&#160;Function:
#  
#&#160;&#160;&#160;&#160;&#160;&#160;&#160;Private&#160;function&#160;that&#160;renames&#160;the&#160;name&#160;of&#160;an&#160;existing&#160;isofill
#  
#&#160;&#160;&#160;&#160;&#160;&#160;&#160;graphics&#160;method.
#  
#
#  
#
#  
#&#160;Example&#160;of&#160;Use:
#  
# [ renameGfi ](/) (old_name,&#160;new_name)
#  
#&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;where:&#160;old_name&#160;is&#160;the&#160;current&#160;name&#160;of&#160;isofill&#160;graphics&#160;method
#  
#&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;new_name&#160;is&#160;the&#160;new&#160;name&#160;for&#160;the&#160;isofill&#160;graphics
method#  
#
#  
##############################################################################
# `

 setGfimember  (self, member, value) 
     ` ###############################################################################   
#
#  
#&#160;Function:&#160;&#160;&#160;&#160;&#160;setGfimember
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
# [ setGfimember ](/) (self,name,value)
#  
#&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;where:&#160;self&#160;is&#160;the&#160;class&#160;(e.g., [ Gfi ](/) )
#  
#&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;name&#160;is&#160;the&#160;name&#160;of&#160;the&#160;member&#160;that&#160;is&#160;being&#160;changed
#  
#&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;value&#160;is&#160;the&#160;new&#160;value&#160;of&#160;the&#160;member&#160;(or&#160;attribute)
#  
#
#  
##############################################################################
# `

 setmember  = setGfimember(self, member, value) 
     ` ###############################################################################   
#
#  
#&#160;Function:&#160;&#160;&#160;&#160;&#160;setGfimember
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
# [ setGfimember ](/) (self,name,value)
#  
#&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;where:&#160;self&#160;is&#160;the&#160;class&#160;(e.g., [ Gfi ](/) )
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

