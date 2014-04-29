---
layout: default
title:
---

 [ Skip to content. ](/cdat/source/api-reference/xmgrace.xmgrace.html) | [ Skip
to navigation ](/cdat/source/api-reference/xmgrace.xmgrace.html)

Search Site

[ Advanced Search&#8230; ](/search_form)

#  [ PCMDI Software Portal ](/)

#####  Sections

  * [ Home ](/)

#####  Personal tools

  * [ Log in ](/login_form)

You are here:  [ Home ](/) -> [ CDAT ](/cdat) -> [ Source Code ](/cdat/source)
-> [ API Reference ](/cdat/source/api-reference) -> Python: module
xmgrace.xmgrace

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

        * [ Python: module xmgrace.xmgrace ](/cdat/source/api-reference/xmgrace.xmgrace.html)

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

  * [ ![Send this page to somebody](media/mail_icon.gif) ](/cdat/source/api-reference/xmgrace.xmgrace.html/sendto_form)
  * [ ![Print this page](media/print_icon.gif) ](/this.print\(\))

#  Python: module xmgrace.xmgrace

  
  
 [ xmgrace  ](/xmgrace.html) .xmgrace 
[ index ](/)  

  
 Modules 

` `

[ xmgrace.ValidationFunctions ](/xmgrace.ValidationFunctions.html)  
[ atexit ](/atexit.html)  

[ genutil.colors ](/genutil.colors.html)  
[ os ](/os.html)  

[ signal ](/signal.html)  
[ time ](/time.html)  

[ types ](/types.html)  

  
 Classes 

` `

[ __builtin__.object ](/__builtin__.html)

    

[ BOX_ELLIPSE ](/xmgrace.xmgrace.html)

[ COLOR ](/xmgrace.xmgrace.html)

[ DSET ](/xmgrace.xmgrace.html)

[ FILL ](/xmgrace.xmgrace.html)

[ FONT ](/xmgrace.xmgrace.html)

[ GRAPH ](/xmgrace.xmgrace.html)

[ LINE ](/xmgrace.xmgrace.html)

[ REGION ](/xmgrace.xmgrace.html)

[ STRING ](/xmgrace.xmgrace.html)

[ init ](/xmgrace.xmgrace.html)

  
class  BOX_ELLIPSE  ( [ __builtin__.object ](/__builtin__.html) )

` `

Methods defined here:  

 __init__  (self, parent, x1, y1, x2, y2, color, lwidth, lstyl, fillcolor, fillpattern, graph  =0  ) 

 list  (self) 

* * *

Properties defined here:  

 color 
    

 _ get _  = _getcolor(self) 
    

 _ set _  = _setcolor(self, value) 

 coord 
    

 _ get _  = _getcoord(self) 
    

 _ set _  = _setcoord(self, value) 

 linestyle 
    

 _ get _  = _getlinestyle(self) 
    

 _ set _  = _setlinestyle(self, value) 

 linewidth 
    

 _ get _  = _getlinewidth(self) 
    

 _ set _  = _setlinewidth(self, value) 

 loctype 
    

 _ get _  = _getloctype(self) 
    

 _ set _  = _setloctype(self, value) 

 status 
    

 _ get _  = _getstatus(self) 
    

 _ set _  = _setstatus(self, value) 

 x1 
    

 _ get _  = _getx1(self) 
    

 _ set _  = _setx1(self, value) 

 x2 
    

 _ get _  = _getx2(self) 
    

 _ set _  = _setx2(self, value) 

 y1 
    

 _ get _  = _gety1(self) 
    

 _ set _  = _sety1(self, value) 

 y2 
    

 _ get _  = _gety2(self) 
    

 _ set _  = _sety2(self, value) 

* * *

Data and other attributes defined here:  

 __slots__  = ['status', 'loctype', 'color', 'linewidth', 'linestyle', 'x1', 'x2', 'y1', 'y2', 'coord', 'fill', 'parent', 'graph', '_status', '_loctype', '_color', '_linewidth', '_linestyle', '_x1', '_x2', ...] 

 fill  = <member 'fill' of 'BOX_ELLIPSE' objects>

 graph  = <member 'graph' of 'BOX_ELLIPSE' objects>

 parent  = <member 'parent' of 'BOX_ELLIPSE' objects>

  
class  COLOR  ( [ __builtin__.object ](/__builtin__.html) )

` `

Methods defined here:  

 __init__  (self, name  ='Black'  , rgb  =None  , id  =16  ) 

 change  (self, nm) 

 list  (self) 
     ` list&#160;the&#160;attributes `

* * *

Properties defined here:  

 id 
    

 _ get _  = _getid(self) 
    

 _ set _  = _setid(self, value) 

 name 
    

 _ get _  = _getname(self) 
    

 _ set _  = _setname(self, value) 

 rgb 
    

 _ get _  = _getrgb(self) 
    

 _ set _  = _setrgb(self, value) 

* * *

Data and other attributes defined here:  

 __slots__  = ['name', 'rgb', 'id', '_name', '_rgb', '_id'] 

  
class  DSET  ( [ __builtin__.object ](/__builtin__.html) )

` `

Methods defined here:  

 __init__  (self, parent, color, graph) 

 list  (self) 
     ` #&#160;end&#160;of&#160;__init__ `

* * *

Properties defined here:  

 comment 
    

 _ get _  = _getcomment(self) 
    

 _ set _  = _setcomment(self, value) 

 dropline 
    

 _ get _  = _getdropline(self) 
    

 _ set _  = _setdropline(self, value) 

 graph 
    

 _ get _  = _getgraph(self) 
    

 _ set _  = _setgraph(self, value) 

 hidden 
    

 _ get _  = _gethidden(self) 
    

 _ set _  = _sethidden(self, value) 

 legend 
    

 _ get _  = _getlegend(self) 
    

 _ set _  = _setlegend(self, value) 

 type 
    

 _ get _  = _gettype(self) 
    

 _ set _  = _settype(self, value) 

* * *

Data and other attributes defined here:  

 __slots__  = ['graph', 'hidden', 'type', 'dropline', 'comment', 'legend', 'symbol', 'line', 'baseline', 'fill', 'avalue', 'errorbar', 'id', 'parent', '_graph', '_hidden', '_type', '_dropline', '_comment', '_legend'] 

 avalue  = <member 'avalue' of 'DSET' objects>

 baseline  = <member 'baseline' of 'DSET' objects>

 errorbar  = <member 'errorbar' of 'DSET' objects>

 fill  = <member 'fill' of 'DSET' objects>

 id  = <member 'id' of 'DSET' objects>

 line  = <member 'line' of 'DSET' objects>

 parent  = <member 'parent' of 'DSET' objects>

 symbol  = <member 'symbol' of 'DSET' objects>

  
class  FILL  ( [ __builtin__.object ](/__builtin__.html) )

` `

Methods defined here:  

 __init__  (self, parent, fillcolor, fillpattern) 

 list  (self) 

* * *

Properties defined here:  

 color 
    

 _ get _  = _getcolor(self) 
    

 _ set _  = _setcolor(self, value) 

 pattern 
    

 _ get _  = _getpattern(self) 
    

 _ set _  = _setpattern(self, value) 

* * *

Data and other attributes defined here:  

 __slots__  = ['_color', '_pattern', 'parent', 'color', 'pattern'] 

 parent  = <member 'parent' of 'FILL' objects>

  
class  FONT  ( [ __builtin__.object ](/__builtin__.html) )

` `

Methods defined here:  

 __init__  (self, name) 

* * *

Properties defined here:  

 name 
    

 _ get _  = _getname(self) 
    

 _ set _  = _setname(self, value) 

* * *

Data and other attributes defined here:  

 __dict__  = <dictproxy object>
     ` dictionary&#160;for&#160;instance&#160;variables&#160;(if&#160;defined) `

 __slots___  = ['name', '_name'] 

 __weakref__  = <attribute '__weakref__' of 'FONT' objects>
     ` list&#160;of&#160;weak&#160;references&#160;to&#160;the [ object ](/__builtin__.html) (if&#160;defined) `

  
class  GRAPH  ( [ __builtin__.object ](/__builtin__.html) )

` `

Methods defined here:  

 __init__  (self, parent, ymin  =0.0  , ymax  =1.0  , xmin  =0.0  , xmax  =1.0  ) 

 list  (self) 
     ` #end&#160;of&#160;__init__ `

* * *

Properties defined here:  

 bar_hgap 
    

 _ get _  = _getbar_hgap(self) 
    

 _ set _  = _setbar_hgap(self, value) 

 hidden 
    

 _ get _  = _gethidden(self) 
    

 _ set _  = _sethidden(self, value) 

 nset 
    

 _ get _  = _getnset(self) 
    

 _ set _  = _setnset(self, value) 

 stack_world 
    

 _ get _  = _getstack_world(self) 
    

 _ set _  = _setstack_world(self, value) 

 stacked 
    

 _ get _  = _getstacked(self) 
    

 _ set _  = _setstacked(self, value) 

 status 
    

 _ get _  = _getstatus(self) 
    

 _ set _  = _setstatus(self, value) 

 stitle 
    

 _ get _  = _getstitle(self) 
    

 _ set _  = _setstitle(self, value) 

 title 
    

 _ get _  = _gettitle(self) 
    

 _ set _  = _settitle(self, value) 

 type 
    

 _ get _  = _gettype(self) 
    

 _ set _  = _settype(self, value) 

 vxmax 
    

 _ get _  = _getvxmax(self) 
    

 _ set _  = _setvxmax(self, value) 

 vxmin 
    

 _ get _  = _getvxmin(self) 
    

 _ set _  = _setvxmin(self, value) 

 vymax 
    

 _ get _  = _getvymax(self) 
    

 _ set _  = _setvymax(self, value) 

 vymin 
    

 _ get _  = _getvymin(self) 
    

 _ set _  = _setvymin(self, value) 

 xmax 
    

 _ get _  = _getxmax(self) 
    

 _ set _  = _setxmax(self, value) 

 xmin 
    

 _ get _  = _getxmin(self) 
    

 _ set _  = _setxmin(self, value) 

 ymax 
    

 _ get _  = _getymax(self) 
    

 _ set _  = _setymax(self, value) 

 ymin 
    

 _ get _  = _getymin(self) 
    

 _ set _  = _setymin(self, value) 

 znorm 
    

 _ get _  = _getznorm(self) 
    

 _ set _  = _setznorm(self, value) 

* * *

Data and other attributes defined here:  

 Set  = <member 'Set' of 'GRAPH' objects>

 __slots__  = ['vxmin', 'vxmax', 'vymin', 'vymax', 'status', 'hidden', 'type', 'stacked', 'stack_world', 'bar_hgap', 'znorm', 'title', 'stitle', 'stit', 'tit', 'fixedpoint', 'xaxis', 'yaxis', 'altxaxis', 'altyaxis', ...] 

 altxaxis  = <member 'altxaxis' of 'GRAPH' objects>

 altyaxis  = <member 'altyaxis' of 'GRAPH' objects>

 fixedpoint  = <member 'fixedpoint' of 'GRAPH' objects>

 frame  = <member 'frame' of 'GRAPH' objects>

 legend  = <member 'legend' of 'GRAPH' objects>

 stit  = <member 'stit' of 'GRAPH' objects>

 tit  = <member 'tit' of 'GRAPH' objects>

 xaxis  = <member 'xaxis' of 'GRAPH' objects>

 yaxis  = <member 'yaxis' of 'GRAPH' objects>

  
class  LINE  ( [ __builtin__.object ](/__builtin__.html) )

` `

Methods defined here:  

 __init__  (self, parent, x1, y1, x2, y2, color, lwidth, lstyl, pos, atyp, algth, alyo, graph  =0  ) 

 list  (self) 

* * *

Properties defined here:  

 color 
    

 _ get _  = _getcolor(self) 
    

 _ set _  = _setcolor(self, value) 

 coord 
    

 _ get _  = _getcoord(self) 
    

 _ set _  = _setcoord(self, value) 

 linestyle 
    

 _ get _  = _getlinestyle(self) 
    

 _ set _  = _setlinestyle(self, value) 

 linewidth 
    

 _ get _  = _getlinewidth(self) 
    

 _ set _  = _setlinewidth(self, value) 

 loctype 
    

 _ get _  = _getloctype(self) 
    

 _ set _  = _setloctype(self, value) 

 status 
    

 _ get _  = _getstatus(self) 
    

 _ set _  = _setstatus(self, value) 

 x1 
    

 _ get _  = _getx1(self) 
    

 _ set _  = _setx1(self, value) 

 x2 
    

 _ get _  = _getx2(self) 
    

 _ set _  = _setx2(self, value) 

 y1 
    

 _ get _  = _gety1(self) 
    

 _ set _  = _sety1(self, value) 

 y2 
    

 _ get _  = _gety2(self) 
    

 _ set _  = _sety2(self, value) 

* * *

Data and other attributes defined here:  

 __slots__  = ['status', 'loctype', 'color', 'linewidth', 'linestyle', 'x1', 'x2', 'y1', 'y2', 'coord', 'parent', 'arrow', 'graph', '_status', '_loctype', '_color', '_linewidth', '_linestyle', '_x1', '_x2', ...] 

 arrow  = <member 'arrow' of 'LINE' objects>

 graph  = <member 'graph' of 'LINE' objects>

 parent  = <member 'parent' of 'LINE' objects>

  
class  REGION  ( [ __builtin__.object ](/__builtin__.html) )

` `

` [ REGION ](/) CLASS  
`

Methods defined here:  

 __init__  (self, parent) 
     ` Default&#160;values `

 list  (self) 
     ` list&#160;the&#160;attributes `

* * *

Properties defined here:  

 color 
    

 _ get _  = _getcolor(self) 
    

 _ set _  = _setcolor(self, value) 

 line 
    

 _ get _  = _getline(self) 
    

 _ set _  = _setline(self, value) 

 linestyle 
    

 _ get _  = _getlinestyle(self) 
    

 _ set _  = _setlinestyle(self, value) 

 linewidth 
    

 _ get _  = _getlinewidth(self) 
    

 _ set _  = _setlinewidth(self, value) 

 link 
    

 _ get _  = _getlink(self) 
    

 _ set _  = _setlink(self, value) 

 status 
    

 _ get _  = _getstatus(self) 
    

 _ set _  = _setstatus(self, value) 

 type 
    

 _ get _  = _gettype(self) 
    

 _ set _  = _settype(self, value) 

 xy 
    

 _ get _  = _getxy(self) 
    

 _ set _  = _setxy(self, value) 

* * *

Data and other attributes defined here:  

 __slots__  = ['status', 'type', 'linestyle', 'linewidth', 'color', 'xy', 'line', 'link', 'parent', '_status', '_type', '_linestyle', '_linewidth', '_color', '_xy', '_line', '_link'] 

 parent  = <member 'parent' of 'REGION' objects>

  
class  STRING  ( [ __builtin__.object ](/__builtin__.html) )

` `

Methods defined here:  

 __init__  (self, parent, x, y, text, color, char_size, font, rot, just, graph  =0  ) 

 list  (self) 

* * *

Properties defined here:  

 char_size 
    

 _ get _  = _getchar_size(self) 
    

 _ set _  = _setchar_size(self, value) 

 color 
    

 _ get _  = _getcolor(self) 
    

 _ set _  = _setcolor(self, value) 

 font 
    

 _ get _  = _getfont(self) 
    

 _ set _  = _setfont(self, value) 

 just 
    

 _ get _  = _getjust(self) 
    

 _ set _  = _setjust(self, value) 

 loctype 
    

 _ get _  = _getloctype(self) 
    

 _ set _  = _setloctype(self, value) 

 rot 
    

 _ get _  = _getrot(self) 
    

 _ set _  = _setrot(self, value) 

 status 
    

 _ get _  = _getstatus(self) 
    

 _ set _  = _setstatus(self, value) 

 text 
    

 _ get _  = _gettext(self) 
    

 _ set _  = _settext(self, value) 

 x 
    

 _ get _  = _getx(self) 
    

 _ set _  = _setx(self, value) 

 xy 
    

 _ get _  = _getxy(self) 
    

 _ set _  = _setxy(self, value) 

 y 
    

 _ get _  = _gety(self) 
    

 _ set _  = _sety(self, value) 

* * *

Data and other attributes defined here:  

 __slots__  = ['status', 'loctype', 'color', 'font', 'just', 'rot', 'x', 'y', 'xy', 'char_size', 'text', 'parent', 'graph', '_status', '_loctype', '_color', '_font', '_just', '_rot', '_x', ...] 

 graph  = <member 'graph' of 'STRING' objects>

 parent  = <member 'parent' of 'STRING' objects>

  
class  init  ( [ __builtin__.object ](/__builtin__.html) )

` `

Methods defined here:  

 __call__  (self, cmd) 

 __del__  (self) 
     ` If&#160;you&#160;want&#160;to&#160;force&#160;xmgrace&#160;to&#160;stay&#160;up   
change&#160;close_cmd&#160;to&#160;'close' `

 __init__  (self, xmgrace_args  =''  , pipe_file  =None  , new_pipe  =1  , clean_on_exit  =True  , color  =1  , font  =0  , linewidth  =1.0  , pattern  =1  , char_size  =1  ) 

 __str__  (self) 

 add_box  (self, x1, y1, x2, y2, color  =-1  , lwidth  =-1  , lstyl  =-1  , fillcolor  =-1  , fillpattern  =-1  ) 

 add_color  (self, name, rgb  =None  , id  =None  ) 

 add_ellipse  (self, x1, y1, x2, y2, color  =-1  , lwidth  =-1  , lstyl  =-1  , fillcolor  =-1  , fillpattern  =-1  ) 

 add_font  (self, name) 

 add_graph  (self, ymin  =0.0  , ymax  =1.0  , xmin  =0.0  , xmax  =1.0  ) 

 add_line  (self, x1, y1, x2, y2, color  =-1  , lwidth  =-1  , lstyl  =-1  , position  =0  , atyp  =0  , algth  =2  , alyo  =[1.0, 1.0]  ) 

 add_r  (self) 

 add_set  (self, graph  =0  , color  =None  ) 

 add_string  (self, x, y, text, color  =-1  , char_size  =-1  , font  =-1  , rot  =0  , just  =14  ) 

 clean_exit  (self) 

 close  (self) 

 col  (self, c) 

 command  (self, cmd) 
     ` Issue&#160;a&#160;command&#160;to&#160;grace&#160;followed&#160;by&#160;a&#160;newline.   
  
Unless&#160;the&#160;constructor&#160;was&#160;called&#160;with&#160;bufsize=0,&#160;this  
interface&#160;is&#160;buffered,&#160;and&#160;command&#160;execution&#160;may&#160;be&#160;delayed.  
To&#160;flush&#160;the&#160;buffer,&#160;either&#160;call [ flush ](/) ()&#160;or&#160;send&#160;the  
command&#160;via&#160;self(cmd). `

 copy  (self, S0, S1, G0  =0  , G1  =0  ) 
     ` copy&#160;sets&#160;definitions&#160;and&#160;possibly&#160;set&#160;if&#160;presents,&#160;destination&#160;must&#160;exist `

 creategraph  (self, ymin  =0.0  , ymax  =1.0  , xmin  =0.0  , xmax  =1.0  ) 

 eps  (self, fnm, color  ='color'  , level  ='level2'  , bbox  ='tight'  , docdata  ='8bit'  , dpi  =300  ) 

 exit  (self) 
     ` Cause&#160;xmgrace&#160;to&#160;exit.   
  
Ask&#160;xmgrace&#160;to&#160;exit&#160;(i.e.,&#160;for&#160;the&#160;program&#160;to&#160;shut&#160;down).&#160;&#160;If  
it&#160;isn't&#160;listening,&#160;try&#160;to&#160;kill&#160;the&#160;process&#160;with&#160;a&#160;SIGTERM. `

 flush  (self) 
     ` Flush&#160;any&#160;pending&#160;commands&#160;to&#160;grace. `

 is_open  (self) 
     ` Return&#160;1&#160;iff&#160;the&#160;pipe&#160;is&#160;not&#160;known&#160;to&#160;have&#160;been&#160;closed. `

 jpeg  (self, fnm, color  ='color'  , optimize  ='off'  , quality  =75  , smoothing  =0  , baseline  ='off'  , progressive  ='on'  , dct  ='islow'  , dpi  =72  ) 

 landscape  (self) 

 list  (self) 

 list_font  (self) 

 make_parameter  (self) 

 metafile  (self, fnm, dpi  =72  ) 

 mif  (self, fnm, dpi  =72  ) 

 move  (self, S0, S1, G0  =0  , G1  =0  ) 
     ` move&#160;sets&#160;definitions&#160;and&#160;possibly&#160;set&#160;if&#160;presents,&#160;destination&#160;must&#160;exist `

 orientation  (self) 

 output  (self, fnm, out  ='PostScript'  ) 

 pdf  (self, fnm, pdf  ='1.3'  , compression  =4  , dpi  =72  ) 

 plot  (self, dat, xs  =None  , G  =None  , S  =None  ) 

 png  (self, fnm, interlaced  ='off'  , transparent  ='on'  , compression  =4  , dpi  =72  ) 

 pnm  (self, fnm, format  ='ppm'  , rawbit  ='on'  , dpi  =72  ) 

 portrait  (self) 

 postscript  (self, fnm, color  ='color'  , level  ='level2'  , docdata  ='8bit'  , xoffset  =0  , yoffset  =0  , mediafeed  ='auto'  , hwresolution  ='off'  , dpi  =300  ) 

 ps  (self, *args, kw) 

 read_parameter  (self, parameterfile) 

 redraw  (self) 

 svg  (self, fnm, dpi  =72  ) 

 swap  (self, S0, S1, G0  =0  , G1  =0  ) 
     ` Swap&#160;2&#160;sets&#160;definitions&#160;and&#160;possibly&#160;sets&#160;if&#160;presents `

 update  (self) 

 whichsets  (self, *args) 

* * *

Properties defined here:  

 background_color 
    

 _ get _  = _getbackground_color(self) 
    

 _ set _  = _setbackground_color(self, value) 

 char_size 
    

 _ get _  = _getchar_size(self) 
    

 _ set _  = _setchar_size(self, value) 

 color 
    

 _ get _  = _getcolor(self) 
    

 _ set _  = _setcolor(self, value) 

 font 
    

 _ get _  = _getfont(self) 
    

 _ set _  = _setfont(self, value) 

 linestyle 
    

 _ get _  = _getlinestyle(self) 
    

 _ set _  = _setlinestyle(self, value) 

 linewidth 
    

 _ get _  = _getlinewidth(self) 
    

 _ set _  = _setlinewidth(self, value) 

 link_page 
    

 _ get _  = _getlink_page(self) 
    

 _ set _  = _setlink_page(self, value) 

 pattern 
    

 _ get _  = _getpattern(self) 
    

 _ set _  = _setpattern(self, value) 

 pyversion 
    

 _ get _  = _getversion(self) 

 sformat 
    

 _ get _  = _getsformat(self) 
    

 _ set _  = _setsformat(self, value) 

 stitle 
    

 _ get _  = _getstitle(self) 
    

 _ set _  = _setstitle(self, value) 

 symbol_size 
    

 _ get _  = _getsymbol_size(self) 
    

 _ set _  = _setsymbol_size(self, value) 

 title 
    

 _ get _  = _gettitle(self) 
    

 _ set _  = _settitle(self, value) 

 version 
    

 _ get _  = _getversion(self) 

* * *

Data and other attributes defined here:  

 Box  = <member 'Box' of 'init' objects>

 Color  = <member 'Color' of 'init' objects>

 Ellipse  = <member 'Ellipse' of 'init' objects>

 Font  = <member 'Font' of 'init' objects>

 Graph  = <member 'Graph' of 'init' objects>

 Line  = <member 'Line' of 'init' objects>

 R  = <member 'R' of 'init' objects>

 Set  = <member 'Set' of 'init' objects>

 String  = <member 'String' of 'init' objects>

 __slots__  = ['title', 'stitle', 'link_page', 'linewidth', 'linestyle', 'color', 'pattern', 'font', 'char_size', 'symbol_size', 'sformat', 'background_color', 'nset', 'ngraph', 'nline', 'nbox', 'nr', 'nellipse', 'pid', 'ininit', ...] 

 date  = <member 'date' of 'init' objects>

 ininit  = <member 'ininit' of 'init' objects>

 nbox  = <member 'nbox' of 'init' objects>

 ncolor  = <member 'ncolor' of 'init' objects>

 nellipse  = <member 'nellipse' of 'init' objects>

 new_pipe  = <member 'new_pipe' of 'init' objects>

 nfont  = <member 'nfont' of 'init' objects>

 ngraph  = <member 'ngraph' of 'init' objects>

 nline  = <member 'nline' of 'init' objects>

 nr  = <member 'nr' of 'init' objects>

 nset  = <member 'nset' of 'init' objects>

 nstring  = <member 'nstring' of 'init' objects>

 page  = <member 'page' of 'init' objects>

 parent  = <member 'parent' of 'init' objects>

 pid  = <member 'pid' of 'init' objects>

 pipe  = <member 'pipe' of 'init' objects>

 pipe_file  = <member 'pipe_file' of 'init' objects>

 timestamp  = <member 'timestamp' of 'init' objects>

* * *

UCRL-WEB-213937 | [ Privacy & Legal Notice ](/disclaimer.html)

[ webmaster@pcmdi.llnl.gov ](/webmaster@pcmdi.llnl.gov)

[ ![Powered by Plone](media/plone_powered.gif) ](/)

