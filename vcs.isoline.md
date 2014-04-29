---
layout: default
title:
---

 [ Skip to content. ](/cdat/source/api-reference/vcs.isoline.html) | [ Skip to
navigation ](/cdat/source/api-reference/vcs.isoline.html)

Search Site

[ Advanced Search&#8230; ](/search_form)

#  [ PCMDI Software Portal ](/)

#####  Sections

  * [ Home ](/)

#####  Personal tools

  * [ Log in ](/login_form)

You are here:  [ Home ](/) -> [ CDAT ](/cdat) -> [ Source Code ](/cdat/source)
-> [ API Reference ](/cdat/source/api-reference) -> Python: module vcs.isoline

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

        * [ Python: module vcs.isoline ](/cdat/source/api-reference/vcs.isoline.html)

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

  * [ ![Send this page to somebody](media/mail_icon.gif) ](/cdat/source/api-reference/vcs.isoline.html/sendto_form)
  * [ ![Print this page](media/print_icon.gif) ](/this.print\(\))

#  Python: module vcs.isoline

  
  
 [ vcs  ](/vcs.html) .isoline 
[ index ](/)  

` #&#160;Isoline&#160;( [ Gi ](/) )&#160;module  
#  
##############################################################################
###  
#
#  
#&#160;Module:&#160;&#160;&#160;&#160;&#160;&#160;&#160;isoline&#160;( [ Gi ](/) )&#160;module
#  
#
#  
#&#160;Copyright:&#160;&#160;&#160;&#160;2000,&#160;Regents&#160;of&#160;the&#160;University&#160;of&#160;California
#  
#&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;This&#160;software&#160;may&#160;not&#160;be&#160;distributed&#160;to&#160;others&#160;without
#  
#&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;permission&#160;of&#160;the&#160;author.
#  
#
#  
#&#160;Author:&#160;&#160;&#160;&#160;&#160;&#160;&#160;PCMDI&#160;Software&#160;Team
#  
#&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;Lawrence&#160;Livermore&#160;NationalLaboratory:
#  
#&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;support@pcmdi.llnl.gov
#  
#
#  
#&#160;Description:&#160;&#160;Python&#160;command&#160;wrapper&#160;for&#160;VCS's&#160;isoline&#160;graphics&#160;method.
#  
#
#  
#&#160;Version:&#160;&#160;&#160;&#160;&#160;&#160;4.0
#  
#
#  
##############################################################################
###  
#  
#  
#  
##############################################################################
###  
#
#  
#&#160;Import:&#160;VCS&#160;C&#160;extension&#160;module.
#  
#
#  
##############################################################################
### `

  
 Modules 

` `

[ vcs.Canvas ](/vcs.Canvas.html)  
[ vcs.VCS_validation_functions ](/vcs.VCS_validation_functions.html)  

[ vcs._vcs ](/vcs._vcs.html)  
[ cdtime ](/cdtime.html)  

[ vcs.queries ](/vcs.queries.html)  
[ vcs ](/vcs.html)  

  
 Classes 

` `

[ __builtin__.object ](/__builtin__.html)

    

[ Gi ](/vcs.isoline.html)

  
class  Gi  ( [ __builtin__.object ](/__builtin__.html) )

` `

` Class: [ Gi ](/) #&#160;Isoline  
  
Description&#160;of [ Gi ](/) Class:  
The&#160;Isoline&#160;graphics&#160;method&#160;draws&#160;lines&#160;of&#160;constant&#160;value&#160;at&#160;specified  
levels&#160;in&#160;order&#160;to&#160;graphically&#160;represent&#160;a&#160;two-dimensional&#160;array.&#160;It  
also&#160;labels&#160;the&#160;values&#160;of&#160;these&#160;isolines&#160;on&#160;the&#160;VCS&#160;Canvas.&#160;The&#160;example  
below&#160;shows&#160;how&#160;to&#160;plot&#160;isolines&#160;of&#160;different&#160;types&#160;at&#160;specified&#160;levels  
and&#160;how&#160;to&#160;create&#160;isoline&#160;labels&#160;having&#160;user-specified&#160;text&#160;and&#160;line&#160;type  
and&#160;color.  
  
This&#160;class&#160;is&#160;used&#160;to&#160;define&#160;an&#160;isoline&#160;table&#160;entry&#160;used&#160;in&#160;VCS,&#160;or&#160;it&#160;can  
be&#160;used&#160;to&#160;change&#160;some&#160;or&#160;all&#160;of&#160;the&#160;isoline&#160;attributes&#160;in&#160;an&#160;existing&#160;isoline  
table&#160;entry.  
  
Other&#160;Useful&#160;Functions:  
a=vcs.init()&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#&#160;Constructor  
a.show('isoline')&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#&#160;Show&#160;predefined&#160;isoline&#160;graphics&#160;methods  
a.show('line')&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#&#160;Show&#160;predefined&#160;VCS&#160;line&#160;objects  
a.setcolormap("AMIP")&#160;&#160;&#160;&#160;&#160;&#160;&#160;#&#160;Change&#160;the&#160;VCS&#160;color&#160;map  
a.isoline(s,a,'default')&#160;&#160;&#160;&#160;#&#160;Plot&#160;data&#160;'s'&#160;with&#160;isoline&#160;'i'&#160;and  
'default'&#160;template  
a.update()&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#&#160;Updates&#160;the&#160;VCS&#160;Canvas&#160;at&#160;user's&#160;request  
a.mode=1,&#160;or&#160;0&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#&#160;If&#160;1,&#160;then&#160;automatic&#160;update,&#160;else&#160;if  
0,&#160;then&#160;use&#160;update&#160;function&#160;to  
update&#160;the&#160;VCS&#160;Canvas.  
  
Example&#160;of&#160;Use:  
a=vcs.init()  
To&#160;Create&#160;a&#160;new&#160;instance&#160;of&#160;isoline&#160;use:  
iso=a.createisoline('new','quick')&#160;#&#160;Copies&#160;content&#160;of&#160;'quick'&#160;to&#160;'new'  
iso=a.createisoline('new')&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#&#160;Copies&#160;content&#160;of&#160;'default'&#160;to&#160;'new'  
  
To&#160;Modify&#160;an&#160;existing&#160;isoline&#160;use:  
iso=a.getisoline('AMIP_psl')  
  
iso. [ list ](/) ()&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#&#160;Will&#160;list&#160;all&#160;the&#160;isoline
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
  
There&#160;are&#160;many&#160;possibilities&#160;ways&#160;to&#160;set&#160;the&#160;isoline&#160;values:  
A)&#160;As&#160;a&#160;list&#160;of&#160;tuples&#160;(Examples):  
iso.level=[(23,32,45,50,76),]  
iso.level=[(22,33,44,55,66)]  
iso.level=[(20,0.0),(30,0),(50,0)]  
iso.level=[(23,32,45,50,76),&#160;(35,&#160;45,&#160;55)]  
B)&#160;As&#160;a&#160;tuple&#160;of&#160;lists&#160;(Examples):  
iso.level=([23,32,45,50,76],)  
iso.level=([22,33,44,55,66])  
iso.level=([23,32,45,50,76],)  
iso.level=([0,20,25,30,35,40],[30,40],[50,60])  
C)&#160;As&#160;a&#160;list&#160;of&#160;lists&#160;(Examples):  
iso.level=[[20,0.0],[30,0],[50,0]]  
D)&#160;As&#160;a&#160;tuple&#160;of&#160;tuples&#160;(Examples):  
iso.level=((20,0.0),(30,0),(50,0),(60,0),(70,0))  
  
Note:&#160;a&#160;combination&#160;of&#160;a&#160;pair&#160;(i.e.,&#160;(30,0)&#160;or&#160;[30,0])&#160;represents  
the&#160;isoline&#160;value&#160;plus&#160;it&#160;increment&#160;value.&#160;Thus,&#160;to&#160;let&#160;VCS  
generate&#160;"default"&#160;isolines&#160;enter&#160;the&#160;following:  
iso.level=[[0,1e20]]&#160;&#160;&#160;&#160;#&#160;Same&#160;as&#160;iso.level=((0,1e20),)  
  
Displaying&#160;isoline&#160;labels:  
iso.label='y'&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#&#160;Same&#160;as&#160;iso.label=1,&#160;will&#160;display&#160;isoline
labels  
iso.label='n'&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#&#160;Same&#160;as&#160;iso.label=0,&#160;will&#160;turn&#160;isoline
labels&#160;off  
  
Specify&#160;the&#160;isoline&#160;line&#160;style&#160;(or&#160;type):  
iso.line=([0,1,2,3,4])&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#&#160;Same&#160;as  
iso.line=(['solid,&#160;'dash',&#160;'dot',&#160;'dash-dot',&#160;'long-dash']),&#160;will  
specify&#160;the&#160;isoline&#160;style  
  
There&#160;are&#160;three&#160;possibilities&#160;for&#160;setting&#160;the&#160;line&#160;color&#160;indices&#160;(Ex):  
iso.linecolors=(22,33,44,55,66,77)&#160;&#160;&#160;&#160;&#160;&#160;#&#160;Same&#160;as  
iso.linecolors=([22,33,44,55,66,77])&#160;&#160;&#160;&#160;#&#160;Will&#160;set&#160;the&#160;isoline&#160;to&#160;a&#160;specific  
#&#160;&#160;&#160;&#160;&#160;color&#160;index  
iso.linecolors=None&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#&#160;Turns&#160;off&#160;the&#160;line&#160;color&#160;index  
  
There&#160;are&#160;three&#160;possibilities&#160;for&#160;setting&#160;the&#160;line&#160;widths&#160;(Ex):  
iso.linewidths=(1,10,3,4,5,6,7,8)&#160;&#160;&#160;&#160;&#160;&#160;&#160;#&#160;Same&#160;as  
iso.linewidths=([1,2,3,4,5,6,7,8])&#160;&#160;&#160;&#160;&#160;&#160;#&#160;Will&#160;set&#160;the&#160;isoline&#160;to&#160;a&#160;specific  
#&#160;&#160;&#160;&#160;&#160;width&#160;size  
iso.linewidths=None&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#&#160;Turns&#160;off&#160;the&#160;line&#160;width&#160;size  
  
There&#160;are&#160;three&#160;ways&#160;to&#160;specify&#160;the&#160;text&#160;or&#160;font&#160;number:  
iso.text=(1,2,3,4,5,6,7,8,9)&#160;&#160;&#160;&#160;#&#160;Font&#160;numbers&#160;are&#160;between&#160;1&#160;and&#160;9  
iso.text=[9,8,7,6,5,4,3,2,1]  
iso.text=([1,3,5,6,9,2])  
iso.text=None&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#&#160;Removes&#160;the&#160;text&#160;settings  
  
There&#160;are&#160;three&#160;possibilities&#160;for&#160;setting&#160;the&#160;text&#160;color&#160;indices&#160;(Ex.):  
iso.textcolors=([22,33,44,55,66,77])  
iso.textcolors=(16,19,33,44)  
iso.textcolors=None&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#&#160;Turns&#160;off&#160;the&#160;text&#160;color&#160;index  
`

Methods defined here:  

 __init__  (self, parent, Gi_name  =None  , Gi_name_src  ='default'  , createGi  =0  ) 

 datawc  (self, dsp1  =1e+20  , dsp2  =1e+20  , dsp3  =1e+20  , dsp4  =1e+20  ) 

 list  (self) 

 rename  = renameGi(self, old_name, new_name) 
     ` #################################################################################   
#
#  
#&#160;Function:&#160;&#160;&#160;&#160;&#160;renameGi
#  
#
#  
#&#160;Description&#160;of&#160;Function:
#  
#&#160;&#160;&#160;&#160;&#160;&#160;&#160;Private&#160;function&#160;that&#160;renames&#160;the&#160;name&#160;of&#160;an&#160;existing&#160;isoline
#  
#&#160;&#160;&#160;&#160;&#160;&#160;&#160;graphics&#160;method.
#  
#
#  
#
#  
#&#160;Example&#160;of&#160;Use:
#  
# [ renameGi ](/) (old_name,&#160;new_name)
#  
#&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;where:&#160;old_name&#160;is&#160;the&#160;current&#160;name&#160;of&#160;isoline&#160;graphics&#160;method
#  
#&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;new_name&#160;is&#160;the&#160;new&#160;name&#160;for&#160;the&#160;isoline&#160;graphics&#160;method
#  
#
#  
##############################################################################
### `

 script  (self, script_filename  =None  , mode  =None  ) 
     ` Function:&#160;&#160;&#160;&#160;&#160;script&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#&#160;Calls&#160;_vcs.scriptGi   
  
Description&#160;of&#160;Function:  
Saves&#160;out&#160;a&#160;isoline&#160;graphics&#160;method&#160;in&#160;Python&#160;and&#160;VCS&#160;script&#160;form&#160;to&#160;a  
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
iso=a.createisoline('temp')  
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

 label 
    

 _ get _  = _getlabel(self) 
    

 _ set _  = _setlabel(self, value) 

 level 
    

 _ get _  = _getlevels(self) 
    

 _ set _  = _setlevels(self, value) 

 levels 
    

 _ get _  = _getlevels(self) 
    

 _ set _  = _setlevels(self, value) 

 line 
    

 _ get _  = _getline(self) 
    

 _ set _  = _setline(self, value) 

 linecolors 
    

 _ get _  = _getlinecolors(self) 
    

 _ set _  = _setlinecolors(self, value) 

 linewidths 
    

 _ get _  = _getlinewidths(self) 
    

 _ set _  = _setlinewidths(self, value) 

 name 
    

 _ get _  = _getname(self) 
    

 _ set _  = _setname(self, value) 

 projection 
    

 _ get _  = _getprojection(self) 
    

 _ set _  = _setprojection(self, value) 

 text 
    

 _ get _  = _gettext(self) 
    

 _ set _  = _settext(self, value) 

 textcolors 
    

 _ get _  = _gettextcolors(self) 
    

 _ set _  = _settextcolors(self, value) 

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

 __slots__  = ['setmember', 'parent', 'name', 'g_name', 'xaxisconvert', 'yaxisconvert', 'levels', 'level', 'label', 'linecolors', 'line', 'linewidths', 'text', 'textcolors', 'projection', 'xticlabels1', 'xticlabels2', 'yticlabels1', 'yticlabels2', 'xmtics1', ...] 

 g_name  = <member 'g_name' of 'Gi' objects>

 parent  = <member 'parent' of 'Gi' objects>

 setmember  = <member 'setmember' of 'Gi' objects>

  
 Functions 

` `

 getGimember  (self, member) 
     ` #################################################################################   
#
#  
#&#160;Function:&#160;&#160;&#160;&#160;&#160;getGimember
#  
#
#  
#&#160;Description&#160;of&#160;Function:
#  
#&#160;&#160;&#160;&#160;&#160;&#160;&#160;Private&#160;function&#160;that&#160;retrieves&#160;the&#160;isoline&#160;members&#160;from&#160;the&#160;C
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
# [ getGimember ](/) (self,name)
#  
#&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;where:&#160;self&#160;is&#160;the&#160;class&#160;(e.g., [ Gi ](/) )
#  
#&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;name&#160;is&#160;the&#160;name&#160;of&#160;the&#160;member&#160;that&#160;is&#160;being&#160;found
#  
#
#  
##############################################################################
### `

 getmember  = getGimember(self, member) 
     ` #################################################################################   
#
#  
#&#160;Function:&#160;&#160;&#160;&#160;&#160;getGimember
#  
#
#  
#&#160;Description&#160;of&#160;Function:
#  
#&#160;&#160;&#160;&#160;&#160;&#160;&#160;Private&#160;function&#160;that&#160;retrieves&#160;the&#160;isoline&#160;members&#160;from&#160;the&#160;C
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
# [ getGimember ](/) (self,name)
#  
#&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;where:&#160;self&#160;is&#160;the&#160;class&#160;(e.g., [ Gi ](/) )
#  
#&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;name&#160;is&#160;the&#160;name&#160;of&#160;the&#160;member&#160;that&#160;is&#160;being&#160;found
#  
#
#  
##############################################################################
### `

 renameGi  (self, old_name, new_name) 
     ` #################################################################################   
#
#  
#&#160;Function:&#160;&#160;&#160;&#160;&#160;renameGi
#  
#
#  
#&#160;Description&#160;of&#160;Function:
#  
#&#160;&#160;&#160;&#160;&#160;&#160;&#160;Private&#160;function&#160;that&#160;renames&#160;the&#160;name&#160;of&#160;an&#160;existing&#160;isoline
#  
#&#160;&#160;&#160;&#160;&#160;&#160;&#160;graphics&#160;method.
#  
#
#  
#
#  
#&#160;Example&#160;of&#160;Use:
#  
# [ renameGi ](/) (old_name,&#160;new_name)
#  
#&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;where:&#160;old_name&#160;is&#160;the&#160;current&#160;name&#160;of&#160;isoline&#160;graphics&#160;method
#  
#&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;new_name&#160;is&#160;the&#160;new&#160;name&#160;for&#160;the&#160;isoline&#160;graphics&#160;method
#  
#
#  
##############################################################################
### `

 setGimember  (self, member, value) 
     ` #################################################################################   
#
#  
#&#160;Function:&#160;&#160;&#160;&#160;&#160;setGimember
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
# [ setGimember ](/) (self,name,value)
#  
#&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;where:&#160;self&#160;is&#160;the&#160;class&#160;(e.g., [ Gi ](/) )
#  
#&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;name&#160;is&#160;the&#160;name&#160;of&#160;the&#160;member&#160;that&#160;is&#160;being&#160;changed
#  
#&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;value&#160;is&#160;the&#160;new&#160;value&#160;of&#160;the&#160;member&#160;(or&#160;attribute)
#  
#
#  
##############################################################################
### `

 setmember  = setGimember(self, member, value) 
     ` #################################################################################   
#
#  
#&#160;Function:&#160;&#160;&#160;&#160;&#160;setGimember
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
# [ setGimember ](/) (self,name,value)
#  
#&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;where:&#160;self&#160;is&#160;the&#160;class&#160;(e.g., [ Gi ](/) )
#  
#&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;name&#160;is&#160;the&#160;name&#160;of&#160;the&#160;member&#160;that&#160;is&#160;being&#160;changed
#  
#&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;value&#160;is&#160;the&#160;new&#160;value&#160;of&#160;the&#160;member&#160;(or&#160;attribute)
#  
#
#  
##############################################################################
### `

* * *

UCRL-WEB-213937 | [ Privacy & Legal Notice ](/disclaimer.html)

[ webmaster@pcmdi.llnl.gov ](/webmaster@pcmdi.llnl.gov)

[ ![Powered by Plone](media/plone_powered.gif) ](/)

