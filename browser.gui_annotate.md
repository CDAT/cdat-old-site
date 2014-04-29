---
layout: default
title:
---

 [ Skip to content. ](/cdat/source/api-reference/browser.gui_annotate.html) | [
Skip to navigation ](/cdat/source/api-reference/browser.gui_annotate.html)

Search Site

[ Advanced Search&#8230; ](/search_form)

#  [ PCMDI Software Portal ](/)

#####  Sections

  * [ Home ](/)

#####  Personal tools

  * [ Log in ](/login_form)

You are here:  [ Home ](/) -> [ CDAT ](/cdat) -> [ Source Code ](/cdat/source)
-> [ API Reference ](/cdat/source/api-reference) -> Python: module
browser.gui_annotate

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

        * [ Python: module browser.gui_annotate ](/cdat/source/api-reference/browser.gui_annotate.html)

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

  * [ ![Send this page to somebody](media/mail_icon.gif) ](/cdat/source/api-reference/browser.gui_annotate.html/sendto_form)
  * [ ![Print this page](media/print_icon.gif) ](/this.print\(\))

#  Python: module browser.gui_annotate

  
  
 [ browser  ](/browser.html) .gui_annotate 
[ index ](/)  

` #&#160;The&#160;PCMDI&#160;Data&#160;Browser&#160;Plot&#160;Annotation&#160;-&#160;&#160;gui_annotate&#160;module  
#  
##############################################################################
#  
#
#  
#&#160;Module:&#160;&#160;&#160;&#160;&#160;&#160;&#160;gui_annotate&#160;module
#  
#
#  
#&#160;Copyright:&#160;&#160;&#160;&#160;"See&#160;file&#160;Legal.htm&#160;for&#160;copyright&#160;information."
#  
#
#  
#&#160;Authors:&#160;&#160;&#160;&#160;&#160;&#160;PCMDI&#160;Software&#160;Team
#  
#&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;Lawrence&#160;Livermore&#160;National&#160;Laboratory:
#  
#&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;support@pcmdi.llnl.gov
#  
#
#  
#&#160;Description:&#160;&#160;PCMDI&#160;Software&#160;System&#160;browser&#160;VCS&#160;plot&#160;annotation.
#  
#
#  
#&#160;Version:&#160;&#160;&#160;&#160;&#160;&#160;4.0
#  
#
#  
##############################################################################
#  
#  
#---------------------------------------------------------------------  
#&#160;NOTE:&#160;need&#160;to&#160;use&#160;version&#160;of&#160;Python&#160;that&#160;imports&#160;Tkinter&#160;and&#160;Pmw  
#--------------------------------------------------------------------- `

  
 Modules 

` `

[ Numeric ](/Numeric.html)  
[ Tkinter ](/Tkinter.html)  
[ __main__ ](/__main__.html)  
[ cdms ](/cdms.html)  

[ cdtime ](/cdtime.html)  
[ gui_support.gui_color ](/gui_support.gui_color.html)  
[ browser.gui_control ](/browser.gui_control.html)  
[ browser.gui_functions ](/browser.gui_functions.html)  

[ browser.gui_menu ](/browser.gui_menu.html)  
[ browser.gui_set_text_object ](/browser.gui_set_text_object.html)  
[ math ](/math.html)  
[ string ](/string.html)  

[ sys ](/sys.html)  
[ vcs ](/vcs.html)  
[ browser.vcs_function ](/browser.vcs_function.html)  

  
 Classes 

` `

[ Tkinter.Button ](/Tkinter.html) ( [ Tkinter.Widget ](/Tkinter.html) )

    

[ EntryButton ](/browser.gui_annotate.html)

[ create ](/browser.gui_annotate.html)

  
class  EntryButton  ( [ Tkinter.Button ](/Tkinter.html) )

` `

Method resolution order:

     [ EntryButton ](/browser.gui_annotate.html)
     [ Tkinter.Button ](/Tkinter.html)
     [ Tkinter.Widget ](/Tkinter.html)
     [ Tkinter.BaseWidget ](/Tkinter.html)
     [ Tkinter.Misc ](/Tkinter.html)
     [ Tkinter.Pack ](/Tkinter.html)
     [ Tkinter.Place ](/Tkinter.html)
     [ Tkinter.Grid ](/Tkinter.html)

* * *

Methods defined here:  

 __init__  (self, master  =None  , cnf  ={}  , kw) 

* * *

Methods inherited from [ Tkinter.Button ](/Tkinter.html) :  

 flash  (self) 
     ` Flash&#160;the&#160;button.   
  
This&#160;is&#160;accomplished&#160;by&#160;redisplaying  
the&#160;button&#160;several&#160;times,&#160;alternating&#160;between&#160;active&#160;and  
normal&#160;colors.&#160;At&#160;the&#160;end&#160;of&#160;the&#160;flash&#160;the&#160;button&#160;is&#160;left  
in&#160;the&#160;same&#160;normal/active&#160;state&#160;as&#160;when&#160;the&#160;command&#160;was  
invoked.&#160;This&#160;command&#160;is&#160;ignored&#160;if&#160;the&#160;button's&#160;state&#160;is  
disabled. `

 invoke  (self) 
     ` Invoke&#160;the&#160;command&#160;associated&#160;with&#160;the&#160;button.   
  
The&#160;return&#160;value&#160;is&#160;the&#160;return&#160;value&#160;from&#160;the&#160;command,  
or&#160;an&#160;empty&#160;string&#160;if&#160;there&#160;is&#160;no&#160;command&#160;associated&#160;with  
the&#160;button.&#160;This&#160;command&#160;is&#160;ignored&#160;if&#160;the&#160;button's&#160;state  
is&#160;disabled. `

 tkButtonDown  (self, *dummy) 

 tkButtonEnter  (self, *dummy) 

 tkButtonInvoke  (self, *dummy) 

 tkButtonLeave  (self, *dummy) 

 tkButtonUp  (self, *dummy) 

* * *

Methods inherited from [ Tkinter.BaseWidget ](/Tkinter.html) :  

 destroy  (self) 
     ` Destroy&#160;this&#160;and&#160;all&#160;descendants&#160;widgets. `

* * *

Methods inherited from [ Tkinter.Misc ](/Tkinter.html) :  

 __getitem__  = cget(self, key) 
     ` Return&#160;the&#160;resource&#160;value&#160;for&#160;a&#160;KEY&#160;given&#160;as&#160;string. `

 __setitem__  (self, key, value) 

 __str__  (self) 
     ` Return&#160;the&#160;window&#160;path&#160;name&#160;of&#160;this&#160;widget. `

 after  (self, ms, func  =None  , *args) 
     ` Call&#160;function&#160;once&#160;after&#160;given&#160;time.   
  
MS&#160;specifies&#160;the&#160;time&#160;in&#160;milliseconds.&#160;FUNC&#160;gives&#160;the  
function&#160;which&#160;shall&#160;be&#160;called.&#160;Additional&#160;parameters  
are&#160;given&#160;as&#160;parameters&#160;to&#160;the&#160;function&#160;call.&#160;&#160;Return  
identifier&#160;to&#160;cancel&#160;scheduling&#160;with&#160;after_cancel. `

 after_cancel  (self, id) 
     ` Cancel&#160;scheduling&#160;of&#160;function&#160;identified&#160;with&#160;ID.   
  
Identifier&#160;returned&#160;by&#160;after&#160;or&#160;after_idle&#160;must&#160;be  
given&#160;as&#160;first&#160;parameter. `

 after_idle  (self, func, *args) 
     ` Call&#160;FUNC&#160;once&#160;if&#160;the&#160;Tcl&#160;main&#160;loop&#160;has&#160;no&#160;event&#160;to   
process.  
  
Return&#160;an&#160;identifier&#160;to&#160;cancel&#160;the&#160;scheduling&#160;with  
after_cancel. `

 bbox  = grid_bbox(self, column  =None  , row  =None  , col2  =None  , row2  =None  ) 
     ` Return&#160;a&#160;tuple&#160;of&#160;integer&#160;coordinates&#160;for&#160;the&#160;bounding   
box&#160;of&#160;this&#160;widget&#160;controlled&#160;by&#160;the&#160;geometry&#160;manager&#160;grid.  
  
If&#160;COLUMN,&#160;ROW&#160;is&#160;given&#160;the&#160;bounding&#160;box&#160;applies&#160;from  
the&#160;cell&#160;with&#160;row&#160;and&#160;column&#160;0&#160;to&#160;the&#160;specified  
cell.&#160;If&#160;COL2&#160;and&#160;ROW2&#160;are&#160;given&#160;the&#160;bounding&#160;box  
starts&#160;at&#160;that&#160;cell.  
  
The&#160;returned&#160;integers&#160;specify&#160;the&#160;offset&#160;of&#160;the&#160;upper&#160;left  
corner&#160;in&#160;the&#160;master&#160;widget&#160;and&#160;the&#160;width&#160;and&#160;height. `

 bell  (self, displayof  =0  ) 
     ` Ring&#160;a&#160;display's&#160;bell. `

 bind  (self, sequence  =None  , func  =None  , add  =None  ) 
     ` Bind&#160;to&#160;this&#160;widget&#160;at&#160;event&#160;SEQUENCE&#160;a&#160;call&#160;to&#160;function&#160;FUNC.   
  
SEQUENCE&#160;is&#160;a&#160;string&#160;of&#160;concatenated&#160;event  
patterns.&#160;An&#160;event&#160;pattern&#160;is&#160;of&#160;the&#160;form  
<MODIFIER-MODIFIER-TYPE-DETAIL>&#160;where&#160;MODIFIER&#160;is&#160;one  
of&#160;Control,&#160;Mod2,&#160;M2,&#160;Shift,&#160;Mod3,&#160;M3,&#160;Lock,&#160;Mod4,&#160;M4,  
Button1,&#160;B1,&#160;Mod5,&#160;M5&#160;Button2,&#160;B2,&#160;Meta,&#160;M,&#160;Button3,  
B3,&#160;Alt,&#160;Button4,&#160;B4,&#160;Double,&#160;Button5,&#160;B5&#160;Triple,  
Mod1,&#160;M1.&#160;TYPE&#160;is&#160;one&#160;of&#160;Activate,&#160;Enter,&#160;Map,  
ButtonPress, [ Button ](/Tkinter.html) ,&#160;Expose,&#160;Motion,&#160;ButtonRelease  
FocusIn,&#160;MouseWheel,&#160;Circulate,&#160;FocusOut,&#160;Property,  
Colormap,&#160;Gravity&#160;Reparent,&#160;Configure,&#160;KeyPress,&#160;Key,  
Unmap,&#160;Deactivate,&#160;KeyRelease&#160;Visibility,&#160;Destroy,  
Leave&#160;and&#160;DETAIL&#160;is&#160;the&#160;button&#160;number&#160;for&#160;ButtonPress,  
ButtonRelease&#160;and&#160;DETAIL&#160;is&#160;the&#160;Keysym&#160;for&#160;KeyPress&#160;and  
KeyRelease.&#160;Examples&#160;are  
<Control- [ Button ](/Tkinter.html) -1>&#160;for&#160;pressing&#160;Control&#160;and&#160;mouse&#160;button
1&#160;or  
<Alt-A>&#160;for&#160;pressing&#160;A&#160;and&#160;the&#160;Alt&#160;key&#160;(KeyPress&#160;can&#160;be&#160;omitted).  
An&#160;event&#160;pattern&#160;can&#160;also&#160;be&#160;a&#160;virtual&#160;event&#160;of&#160;the&#160;form  
<<AString>>&#160;where&#160;AString&#160;can&#160;be&#160;arbitrary.&#160;This  
event&#160;can&#160;be&#160;generated&#160;by&#160;event_generate.  
If&#160;events&#160;are&#160;concatenated&#160;they&#160;must&#160;appear&#160;shortly  
after&#160;each&#160;other.  
  
FUNC&#160;will&#160;be&#160;called&#160;if&#160;the&#160;event&#160;sequence&#160;occurs&#160;with&#160;an  
instance&#160;of&#160;Event&#160;as&#160;argument.&#160;If&#160;the&#160;return&#160;value&#160;of&#160;FUNC&#160;is  
"break"&#160;no&#160;further&#160;bound&#160;function&#160;is&#160;invoked.  
  
An&#160;additional&#160;boolean&#160;parameter&#160;ADD&#160;specifies&#160;whether&#160;FUNC&#160;will  
be&#160;called&#160;additionally&#160;to&#160;the&#160;other&#160;bound&#160;function&#160;or&#160;whether  
it&#160;will&#160;replace&#160;the&#160;previous&#160;function.  
  
Bind&#160;will&#160;return&#160;an&#160;identifier&#160;to&#160;allow&#160;deletion&#160;of&#160;the&#160;bound&#160;function&#160;with  
unbind&#160;without&#160;memory&#160;leak.  
  
If&#160;FUNC&#160;or&#160;SEQUENCE&#160;is&#160;omitted&#160;the&#160;bound&#160;function&#160;or&#160;list  
of&#160;bound&#160;events&#160;are&#160;returned. `

 bind_all  (self, sequence  =None  , func  =None  , add  =None  ) 
     ` Bind&#160;to&#160;all&#160;widgets&#160;at&#160;an&#160;event&#160;SEQUENCE&#160;a&#160;call&#160;to&#160;function&#160;FUNC.   
An&#160;additional&#160;boolean&#160;parameter&#160;ADD&#160;specifies&#160;whether&#160;FUNC&#160;will  
be&#160;called&#160;additionally&#160;to&#160;the&#160;other&#160;bound&#160;function&#160;or&#160;whether  
it&#160;will&#160;replace&#160;the&#160;previous&#160;function.&#160;See&#160;bind&#160;for&#160;the&#160;return&#160;value. `

 bind_class  (self, className, sequence  =None  , func  =None  , add  =None  ) 
     ` Bind&#160;to&#160;widgets&#160;with&#160;bindtag&#160;CLASSNAME&#160;at&#160;event   
SEQUENCE&#160;a&#160;call&#160;of&#160;function&#160;FUNC.&#160;An&#160;additional  
boolean&#160;parameter&#160;ADD&#160;specifies&#160;whether&#160;FUNC&#160;will&#160;be  
called&#160;additionally&#160;to&#160;the&#160;other&#160;bound&#160;function&#160;or  
whether&#160;it&#160;will&#160;replace&#160;the&#160;previous&#160;function.&#160;See&#160;bind&#160;for  
the&#160;return&#160;value. `

 bindtags  (self, tagList  =None  ) 
     ` Set&#160;or&#160;get&#160;the&#160;list&#160;of&#160;bindtags&#160;for&#160;this&#160;widget.   
  
With&#160;no&#160;argument&#160;return&#160;the&#160;list&#160;of&#160;all&#160;bindtags&#160;associated&#160;with  
this&#160;widget.&#160;With&#160;a&#160;list&#160;of&#160;strings&#160;as&#160;argument&#160;the&#160;bindtags&#160;are  
set&#160;to&#160;this&#160;list.&#160;The&#160;bindtags&#160;determine&#160;in&#160;which&#160;order&#160;events&#160;are  
processed&#160;(see&#160;bind). `

 cget  (self, key) 
     ` Return&#160;the&#160;resource&#160;value&#160;for&#160;a&#160;KEY&#160;given&#160;as&#160;string. `

 clipboard_append  (self, string, kw) 
     ` Append&#160;STRING&#160;to&#160;the&#160;Tk&#160;clipboard.   
  
A&#160;widget&#160;specified&#160;at&#160;the&#160;optional&#160;displayof&#160;keyword  
argument&#160;specifies&#160;the&#160;target&#160;display.&#160;The&#160;clipboard  
can&#160;be&#160;retrieved&#160;with&#160;selection_get. `

 clipboard_clear  (self, kw) 
     ` Clear&#160;the&#160;data&#160;in&#160;the&#160;Tk&#160;clipboard.   
  
A&#160;widget&#160;specified&#160;for&#160;the&#160;optional&#160;displayof&#160;keyword  
argument&#160;specifies&#160;the&#160;target&#160;display. `

 colormodel  (self, value  =None  ) 
     ` Useless.&#160;Not&#160;implemented&#160;in&#160;Tk. `

 columnconfigure  = grid_columnconfigure(self, index, cnf  ={}  , kw) 
     ` Configure&#160;column&#160;INDEX&#160;of&#160;a&#160;grid.   
  
Valid&#160;resources&#160;are&#160;minsize&#160;(minimum&#160;size&#160;of&#160;the&#160;column),  
weight&#160;(how&#160;much&#160;does&#160;additional&#160;space&#160;propagate&#160;to&#160;this&#160;column)  
and&#160;pad&#160;(how&#160;much&#160;space&#160;to&#160;let&#160;additionally). `

 config  = configure(self, cnf  =None  , kw) 
     ` Configure&#160;resources&#160;of&#160;a&#160;widget.   
  
The&#160;values&#160;for&#160;resources&#160;are&#160;specified&#160;as&#160;keyword  
arguments.&#160;To&#160;get&#160;an&#160;overview&#160;about  
the&#160;allowed&#160;keyword&#160;arguments&#160;call&#160;the&#160;method&#160;keys. `

 configure  (self, cnf  =None  , kw) 
     ` Configure&#160;resources&#160;of&#160;a&#160;widget.   
  
The&#160;values&#160;for&#160;resources&#160;are&#160;specified&#160;as&#160;keyword  
arguments.&#160;To&#160;get&#160;an&#160;overview&#160;about  
the&#160;allowed&#160;keyword&#160;arguments&#160;call&#160;the&#160;method&#160;keys. `

 deletecommand  (self, name) 
     ` Internal&#160;function.   
  
Delete&#160;the&#160;Tcl&#160;command&#160;provided&#160;in&#160;NAME. `

 event_add  (self, virtual, *sequences) 
     ` Bind&#160;a&#160;virtual&#160;event&#160;VIRTUAL&#160;(of&#160;the&#160;form&#160;<<Name>>)   
to&#160;an&#160;event&#160;SEQUENCE&#160;such&#160;that&#160;the&#160;virtual&#160;event&#160;is&#160;triggered  
whenever&#160;SEQUENCE&#160;occurs. `

 event_delete  (self, virtual, *sequences) 
     ` Unbind&#160;a&#160;virtual&#160;event&#160;VIRTUAL&#160;from&#160;SEQUENCE. `

 event_generate  (self, sequence, kw) 
     ` Generate&#160;an&#160;event&#160;SEQUENCE.&#160;Additional   
keyword&#160;arguments&#160;specify&#160;parameter&#160;of&#160;the&#160;event  
(e.g.&#160;x,&#160;y,&#160;rootx,&#160;rooty). `

 event_info  (self, virtual  =None  ) 
     ` Return&#160;a&#160;list&#160;of&#160;all&#160;virtual&#160;events&#160;or&#160;the&#160;information   
about&#160;the&#160;SEQUENCE&#160;bound&#160;to&#160;the&#160;virtual&#160;event&#160;VIRTUAL. `

 focus  = focus_set(self) 
     ` Direct&#160;input&#160;focus&#160;to&#160;this&#160;widget.   
  
If&#160;the&#160;application&#160;currently&#160;does&#160;not&#160;have&#160;the&#160;focus  
this&#160;widget&#160;will&#160;get&#160;the&#160;focus&#160;if&#160;the&#160;application&#160;gets  
the&#160;focus&#160;through&#160;the&#160;window&#160;manager. `

 focus_displayof  (self) 
     ` Return&#160;the&#160;widget&#160;which&#160;has&#160;currently&#160;the&#160;focus&#160;on&#160;the   
display&#160;where&#160;this&#160;widget&#160;is&#160;located.  
  
Return&#160;None&#160;if&#160;the&#160;application&#160;does&#160;not&#160;have&#160;the&#160;focus. `

 focus_force  (self) 
     ` Direct&#160;input&#160;focus&#160;to&#160;this&#160;widget&#160;even&#160;if&#160;the   
application&#160;does&#160;not&#160;have&#160;the&#160;focus.&#160;Use&#160;with  
caution! `

 focus_get  (self) 
     ` Return&#160;the&#160;widget&#160;which&#160;has&#160;currently&#160;the&#160;focus&#160;in&#160;the   
application.  
  
Use&#160;focus_displayof&#160;to&#160;allow&#160;working&#160;with&#160;several  
displays.&#160;Return&#160;None&#160;if&#160;application&#160;does&#160;not&#160;have  
the&#160;focus. `

 focus_lastfor  (self) 
     ` Return&#160;the&#160;widget&#160;which&#160;would&#160;have&#160;the&#160;focus&#160;if&#160;top&#160;level   
for&#160;this&#160;widget&#160;gets&#160;the&#160;focus&#160;from&#160;the&#160;window&#160;manager. `

 focus_set  (self) 
     ` Direct&#160;input&#160;focus&#160;to&#160;this&#160;widget.   
  
If&#160;the&#160;application&#160;currently&#160;does&#160;not&#160;have&#160;the&#160;focus  
this&#160;widget&#160;will&#160;get&#160;the&#160;focus&#160;if&#160;the&#160;application&#160;gets  
the&#160;focus&#160;through&#160;the&#160;window&#160;manager. `

 getboolean  (self, s) 
     ` Return&#160;a&#160;boolean&#160;value&#160;for&#160;Tcl&#160;boolean&#160;values&#160;true&#160;and&#160;false&#160;given&#160;as&#160;parameter. `

 getvar  (self, name  ='PY_VAR'  ) 
     ` Return&#160;value&#160;of&#160;Tcl&#160;variable&#160;NAME. `

 grab_current  (self) 
     ` Return&#160;widget&#160;which&#160;has&#160;currently&#160;the&#160;grab&#160;in&#160;this&#160;application   
or&#160;None. `

 grab_release  (self) 
     ` Release&#160;grab&#160;for&#160;this&#160;widget&#160;if&#160;currently&#160;set. `

 grab_set  (self) 
     ` Set&#160;grab&#160;for&#160;this&#160;widget.   
  
A&#160;grab&#160;directs&#160;all&#160;events&#160;to&#160;this&#160;and&#160;descendant  
widgets&#160;in&#160;the&#160;application. `

 grab_set_global  (self) 
     ` Set&#160;global&#160;grab&#160;for&#160;this&#160;widget.   
  
A&#160;global&#160;grab&#160;directs&#160;all&#160;events&#160;to&#160;this&#160;and  
descendant&#160;widgets&#160;on&#160;the&#160;display.&#160;Use&#160;with&#160;caution&#160;\-  
other&#160;applications&#160;do&#160;not&#160;get&#160;events&#160;anymore. `

 grab_status  (self) 
     ` Return&#160;None,&#160;"local"&#160;or&#160;"global"&#160;if&#160;this&#160;widget&#160;has   
no,&#160;a&#160;local&#160;or&#160;a&#160;global&#160;grab. `

 grid_bbox  (self, column  =None  , row  =None  , col2  =None  , row2  =None  ) 
     ` Return&#160;a&#160;tuple&#160;of&#160;integer&#160;coordinates&#160;for&#160;the&#160;bounding   
box&#160;of&#160;this&#160;widget&#160;controlled&#160;by&#160;the&#160;geometry&#160;manager&#160;grid.  
  
If&#160;COLUMN,&#160;ROW&#160;is&#160;given&#160;the&#160;bounding&#160;box&#160;applies&#160;from  
the&#160;cell&#160;with&#160;row&#160;and&#160;column&#160;0&#160;to&#160;the&#160;specified  
cell.&#160;If&#160;COL2&#160;and&#160;ROW2&#160;are&#160;given&#160;the&#160;bounding&#160;box  
starts&#160;at&#160;that&#160;cell.  
  
The&#160;returned&#160;integers&#160;specify&#160;the&#160;offset&#160;of&#160;the&#160;upper&#160;left  
corner&#160;in&#160;the&#160;master&#160;widget&#160;and&#160;the&#160;width&#160;and&#160;height. `

 grid_columnconfigure  (self, index, cnf  ={}  , kw) 
     ` Configure&#160;column&#160;INDEX&#160;of&#160;a&#160;grid.   
  
Valid&#160;resources&#160;are&#160;minsize&#160;(minimum&#160;size&#160;of&#160;the&#160;column),  
weight&#160;(how&#160;much&#160;does&#160;additional&#160;space&#160;propagate&#160;to&#160;this&#160;column)  
and&#160;pad&#160;(how&#160;much&#160;space&#160;to&#160;let&#160;additionally). `

 grid_location  (self, x, y) 
     ` Return&#160;a&#160;tuple&#160;of&#160;column&#160;and&#160;row&#160;which&#160;identify&#160;the&#160;cell   
at&#160;which&#160;the&#160;pixel&#160;at&#160;position&#160;X&#160;and&#160;Y&#160;inside&#160;the&#160;master  
widget&#160;is&#160;located. `

 grid_propagate  (self, flag  =['_noarg_']  ) 
     ` Set&#160;or&#160;get&#160;the&#160;status&#160;for&#160;propagation&#160;of&#160;geometry&#160;information.   
  
A&#160;boolean&#160;argument&#160;specifies&#160;whether&#160;the&#160;geometry&#160;information  
of&#160;the&#160;slaves&#160;will&#160;determine&#160;the&#160;size&#160;of&#160;this&#160;widget.&#160;If&#160;no&#160;argument  
is&#160;given,&#160;the&#160;current&#160;setting&#160;will&#160;be&#160;returned. `

 grid_rowconfigure  (self, index, cnf  ={}  , kw) 
     ` Configure&#160;row&#160;INDEX&#160;of&#160;a&#160;grid.   
  
Valid&#160;resources&#160;are&#160;minsize&#160;(minimum&#160;size&#160;of&#160;the&#160;row),  
weight&#160;(how&#160;much&#160;does&#160;additional&#160;space&#160;propagate&#160;to&#160;this&#160;row)  
and&#160;pad&#160;(how&#160;much&#160;space&#160;to&#160;let&#160;additionally). `

 grid_size  (self) 
     ` Return&#160;a&#160;tuple&#160;of&#160;the&#160;number&#160;of&#160;column&#160;and&#160;rows&#160;in&#160;the&#160;grid. `

 grid_slaves  (self, row  =None  , column  =None  ) 
     ` Return&#160;a&#160;list&#160;of&#160;all&#160;slaves&#160;of&#160;this&#160;widget   
in&#160;its&#160;packing&#160;order. `

 image_names  (self) 
     ` Return&#160;a&#160;list&#160;of&#160;all&#160;existing&#160;image&#160;names. `

 image_types  (self) 
     ` Return&#160;a&#160;list&#160;of&#160;all&#160;available&#160;image&#160;types&#160;(e.g.&#160;phote&#160;bitmap). `

 keys  (self) 
     ` Return&#160;a&#160;list&#160;of&#160;all&#160;resource&#160;names&#160;of&#160;this&#160;widget. `

 lift  = tkraise(self, aboveThis  =None  ) 
     ` Raise&#160;this&#160;widget&#160;in&#160;the&#160;stacking&#160;order. `

 lower  (self, belowThis  =None  ) 
     ` Lower&#160;this&#160;widget&#160;in&#160;the&#160;stacking&#160;order. `

 mainloop  (self, n  =0  ) 
     ` Call&#160;the&#160;mainloop&#160;of&#160;Tk. `

 nametowidget  (self, name) 
     ` Return&#160;the&#160;Tkinter&#160;instance&#160;of&#160;a&#160;widget&#160;identified&#160;by   
its&#160;Tcl&#160;name&#160;NAME. `

 option_add  (self, pattern, value, priority  =None  ) 
     ` Set&#160;a&#160;VALUE&#160;(second&#160;parameter)&#160;for&#160;an&#160;option   
PATTERN&#160;(first&#160;parameter).  
  
An&#160;optional&#160;third&#160;parameter&#160;gives&#160;the&#160;numeric&#160;priority  
(defaults&#160;to&#160;80). `

 option_clear  (self) 
     ` Clear&#160;the&#160;option&#160;database.   
  
It&#160;will&#160;be&#160;reloaded&#160;if&#160;option_add&#160;is&#160;called. `

 option_get  (self, name, className) 
     ` Return&#160;the&#160;value&#160;for&#160;an&#160;option&#160;NAME&#160;for&#160;this&#160;widget   
with&#160;CLASSNAME.  
  
Values&#160;with&#160;higher&#160;priority&#160;override&#160;lower&#160;values. `

 option_readfile  (self, fileName, priority  =None  ) 
     ` Read&#160;file&#160;FILENAME&#160;into&#160;the&#160;option&#160;database.   
  
An&#160;optional&#160;second&#160;parameter&#160;gives&#160;the&#160;numeric  
priority. `

 pack_propagate  (self, flag  =['_noarg_']  ) 
     ` Set&#160;or&#160;get&#160;the&#160;status&#160;for&#160;propagation&#160;of&#160;geometry&#160;information.   
  
A&#160;boolean&#160;argument&#160;specifies&#160;whether&#160;the&#160;geometry&#160;information  
of&#160;the&#160;slaves&#160;will&#160;determine&#160;the&#160;size&#160;of&#160;this&#160;widget.&#160;If&#160;no&#160;argument  
is&#160;given&#160;the&#160;current&#160;setting&#160;will&#160;be&#160;returned. `

 pack_slaves  (self) 
     ` Return&#160;a&#160;list&#160;of&#160;all&#160;slaves&#160;of&#160;this&#160;widget   
in&#160;its&#160;packing&#160;order. `

 place_slaves  (self) 
     ` Return&#160;a&#160;list&#160;of&#160;all&#160;slaves&#160;of&#160;this&#160;widget   
in&#160;its&#160;packing&#160;order. `

 propagate  = pack_propagate(self, flag  =['_noarg_']  ) 
     ` Set&#160;or&#160;get&#160;the&#160;status&#160;for&#160;propagation&#160;of&#160;geometry&#160;information.   
  
A&#160;boolean&#160;argument&#160;specifies&#160;whether&#160;the&#160;geometry&#160;information  
of&#160;the&#160;slaves&#160;will&#160;determine&#160;the&#160;size&#160;of&#160;this&#160;widget.&#160;If&#160;no&#160;argument  
is&#160;given&#160;the&#160;current&#160;setting&#160;will&#160;be&#160;returned. `

 quit  (self) 
     ` Quit&#160;the&#160;Tcl&#160;interpreter.&#160;All&#160;widgets&#160;will&#160;be&#160;destroyed. `

 register  = _register(self, func, subst  =None  , needcleanup  =1  ) 
     ` Return&#160;a&#160;newly&#160;created&#160;Tcl&#160;function.&#160;If&#160;this   
function&#160;is&#160;called,&#160;the&#160;Python&#160;function&#160;FUNC&#160;will  
be&#160;executed.&#160;An&#160;optional&#160;function&#160;SUBST&#160;can  
be&#160;given&#160;which&#160;will&#160;be&#160;executed&#160;before&#160;FUNC. `

 rowconfigure  = grid_rowconfigure(self, index, cnf  ={}  , kw) 
     ` Configure&#160;row&#160;INDEX&#160;of&#160;a&#160;grid.   
  
Valid&#160;resources&#160;are&#160;minsize&#160;(minimum&#160;size&#160;of&#160;the&#160;row),  
weight&#160;(how&#160;much&#160;does&#160;additional&#160;space&#160;propagate&#160;to&#160;this&#160;row)  
and&#160;pad&#160;(how&#160;much&#160;space&#160;to&#160;let&#160;additionally). `

 selection_clear  (self, kw) 
     ` Clear&#160;the&#160;current&#160;X&#160;selection. `

 selection_get  (self, kw) 
     ` Return&#160;the&#160;contents&#160;of&#160;the&#160;current&#160;X&#160;selection.   
  
A&#160;keyword&#160;parameter&#160;selection&#160;specifies&#160;the&#160;name&#160;of  
the&#160;selection&#160;and&#160;defaults&#160;to&#160;PRIMARY.&#160;&#160;A&#160;keyword  
parameter&#160;displayof&#160;specifies&#160;a&#160;widget&#160;on&#160;the&#160;display  
to&#160;use. `

 selection_handle  (self, command, kw) 
     ` Specify&#160;a&#160;function&#160;COMMAND&#160;to&#160;call&#160;if&#160;the&#160;X   
selection&#160;owned&#160;by&#160;this&#160;widget&#160;is&#160;queried&#160;by&#160;another  
application.  
  
This&#160;function&#160;must&#160;return&#160;the&#160;contents&#160;of&#160;the  
selection.&#160;The&#160;function&#160;will&#160;be&#160;called&#160;with&#160;the  
arguments&#160;OFFSET&#160;and&#160;LENGTH&#160;which&#160;allows&#160;the&#160;chunking  
of&#160;very&#160;long&#160;selections.&#160;The&#160;following&#160;keyword  
parameters&#160;can&#160;be&#160;provided:  
selection&#160;-&#160;name&#160;of&#160;the&#160;selection&#160;(default&#160;PRIMARY),  
type&#160;-&#160;type&#160;of&#160;the&#160;selection&#160;(e.g.&#160;STRING,&#160;FILE_NAME). `

 selection_own  (self, kw) 
     ` Become&#160;owner&#160;of&#160;X&#160;selection.   
  
A&#160;keyword&#160;parameter&#160;selection&#160;specifies&#160;the&#160;name&#160;of  
the&#160;selection&#160;(default&#160;PRIMARY). `

 selection_own_get  (self, kw) 
     ` Return&#160;owner&#160;of&#160;X&#160;selection.   
  
The&#160;following&#160;keyword&#160;parameter&#160;can  
be&#160;provided:  
selection&#160;-&#160;name&#160;of&#160;the&#160;selection&#160;(default&#160;PRIMARY),  
type&#160;-&#160;type&#160;of&#160;the&#160;selection&#160;(e.g.&#160;STRING,&#160;FILE_NAME). `

 send  (self, interp, cmd, *args) 
     ` Send&#160;Tcl&#160;command&#160;CMD&#160;to&#160;different&#160;interpreter&#160;INTERP&#160;to&#160;be&#160;executed. `

 setvar  (self, name  ='PY_VAR'  , value  ='1'  ) 
     ` Set&#160;Tcl&#160;variable&#160;NAME&#160;to&#160;VALUE. `

 size  = grid_size(self) 
     ` Return&#160;a&#160;tuple&#160;of&#160;the&#160;number&#160;of&#160;column&#160;and&#160;rows&#160;in&#160;the&#160;grid. `

 slaves  = pack_slaves(self) 
     ` Return&#160;a&#160;list&#160;of&#160;all&#160;slaves&#160;of&#160;this&#160;widget   
in&#160;its&#160;packing&#160;order. `

 tk_bisque  (self) 
     ` Change&#160;the&#160;color&#160;scheme&#160;to&#160;light&#160;brown&#160;as&#160;used&#160;in&#160;Tk&#160;3.6&#160;and&#160;before. `

 tk_focusFollowsMouse  (self) 
     ` The&#160;widget&#160;under&#160;mouse&#160;will&#160;get&#160;automatically&#160;focus.&#160;Can&#160;not   
be&#160;disabled&#160;easily. `

 tk_focusNext  (self) 
     ` Return&#160;the&#160;next&#160;widget&#160;in&#160;the&#160;focus&#160;order&#160;which&#160;follows   
widget&#160;which&#160;has&#160;currently&#160;the&#160;focus.  
  
The&#160;focus&#160;order&#160;first&#160;goes&#160;to&#160;the&#160;next&#160;child,&#160;then&#160;to  
the&#160;children&#160;of&#160;the&#160;child&#160;recursively&#160;and&#160;then&#160;to&#160;the  
next&#160;sibling&#160;which&#160;is&#160;higher&#160;in&#160;the&#160;stacking&#160;order.&#160;&#160;A  
widget&#160;is&#160;omitted&#160;if&#160;it&#160;has&#160;the&#160;takefocus&#160;resource&#160;set  
to&#160;0\. `

 tk_focusPrev  (self) 
     ` Return&#160;previous&#160;widget&#160;in&#160;the&#160;focus&#160;order.&#160;See&#160;tk_focusNext&#160;for&#160;details. `

 tk_menuBar  (self, *args) 
     ` Do&#160;not&#160;use.&#160;Needed&#160;in&#160;Tk&#160;3.6&#160;and&#160;earlier. `

 tk_setPalette  (self, *args, kw) 
     ` Set&#160;a&#160;new&#160;color&#160;scheme&#160;for&#160;all&#160;widget&#160;elements.   
  
A&#160;single&#160;color&#160;as&#160;argument&#160;will&#160;cause&#160;that&#160;all&#160;colors&#160;of&#160;Tk  
widget&#160;elements&#160;are&#160;derived&#160;from&#160;this.  
Alternatively&#160;several&#160;keyword&#160;parameters&#160;and&#160;its&#160;associated  
colors&#160;can&#160;be&#160;given.&#160;The&#160;following&#160;keywords&#160;are&#160;valid:  
activeBackground,&#160;foreground,&#160;selectColor,  
activeForeground,&#160;highlightBackground,&#160;selectBackground,  
background,&#160;highlightColor,&#160;selectForeground,  
disabledForeground,&#160;insertBackground,&#160;troughColor. `

 tk_strictMotif  (self, boolean  =None  ) 
     ` Set&#160;Tcl&#160;internal&#160;variable,&#160;whether&#160;the&#160;look&#160;and&#160;feel   
should&#160;adhere&#160;to&#160;Motif.  
  
A&#160;parameter&#160;of&#160;1&#160;means&#160;adhere&#160;to&#160;Motif&#160;(e.g.&#160;no&#160;color  
change&#160;if&#160;mouse&#160;passes&#160;over&#160;slider).  
Returns&#160;the&#160;set&#160;value. `

 tkraise  (self, aboveThis  =None  ) 
     ` Raise&#160;this&#160;widget&#160;in&#160;the&#160;stacking&#160;order. `

 unbind  (self, sequence, funcid  =None  ) 
     ` Unbind&#160;for&#160;this&#160;widget&#160;for&#160;event&#160;SEQUENCE&#160;&#160;the   
function&#160;identified&#160;with&#160;FUNCID. `

 unbind_all  (self, sequence) 
     ` Unbind&#160;for&#160;all&#160;widgets&#160;for&#160;event&#160;SEQUENCE&#160;all&#160;functions. `

 unbind_class  (self, className, sequence) 
     ` Unbind&#160;for&#160;a&#160;all&#160;widgets&#160;with&#160;bindtag&#160;CLASSNAME&#160;for&#160;event&#160;SEQUENCE   
all&#160;functions. `

 update  (self) 
     ` Enter&#160;event&#160;loop&#160;until&#160;all&#160;pending&#160;events&#160;have&#160;been&#160;processed&#160;by&#160;Tcl. `

 update_idletasks  (self) 
     ` Enter&#160;event&#160;loop&#160;until&#160;all&#160;idle&#160;callbacks&#160;have&#160;been&#160;called.&#160;This   
will&#160;update&#160;the&#160;display&#160;of&#160;windows&#160;but&#160;not&#160;process&#160;events&#160;caused&#160;by  
the&#160;user. `

 wait_variable  (self, name  ='PY_VAR'  ) 
     ` Wait&#160;until&#160;the&#160;variable&#160;is&#160;modified.   
  
A&#160;parameter&#160;of&#160;type&#160;IntVar,&#160;StringVar,&#160;DoubleVar&#160;or  
BooleanVar&#160;must&#160;be&#160;given. `

 wait_visibility  (self, window  =None  ) 
     ` Wait&#160;until&#160;the&#160;visibility&#160;of&#160;a&#160;WIDGET&#160;changes   
(e.g.&#160;it&#160;appears).  
  
If&#160;no&#160;parameter&#160;is&#160;given&#160;self&#160;is&#160;used. `

 wait_window  (self, window  =None  ) 
     ` Wait&#160;until&#160;a&#160;WIDGET&#160;is&#160;destroyed.   
  
If&#160;no&#160;parameter&#160;is&#160;given&#160;self&#160;is&#160;used. `

 waitvar  = wait_variable(self, name  ='PY_VAR'  ) 
     ` Wait&#160;until&#160;the&#160;variable&#160;is&#160;modified.   
  
A&#160;parameter&#160;of&#160;type&#160;IntVar,&#160;StringVar,&#160;DoubleVar&#160;or  
BooleanVar&#160;must&#160;be&#160;given. `

 winfo_atom  (self, name, displayof  =0  ) 
     ` Return&#160;integer&#160;which&#160;represents&#160;atom&#160;NAME. `

 winfo_atomname  (self, id, displayof  =0  ) 
     ` Return&#160;name&#160;of&#160;atom&#160;with&#160;identifier&#160;ID. `

 winfo_cells  (self) 
     ` Return&#160;number&#160;of&#160;cells&#160;in&#160;the&#160;colormap&#160;for&#160;this&#160;widget. `

 winfo_children  (self) 
     ` Return&#160;a&#160;list&#160;of&#160;all&#160;widgets&#160;which&#160;are&#160;children&#160;of&#160;this&#160;widget. `

 winfo_class  (self) 
     ` Return&#160;window&#160;class&#160;name&#160;of&#160;this&#160;widget. `

 winfo_colormapfull  (self) 
     ` Return&#160;true&#160;if&#160;at&#160;the&#160;last&#160;color&#160;request&#160;the&#160;colormap&#160;was&#160;full. `

 winfo_containing  (self, rootX, rootY, displayof  =0  ) 
     ` Return&#160;the&#160;widget&#160;which&#160;is&#160;at&#160;the&#160;root&#160;coordinates&#160;ROOTX,&#160;ROOTY. `

 winfo_depth  (self) 
     ` Return&#160;the&#160;number&#160;of&#160;bits&#160;per&#160;pixel. `

 winfo_exists  (self) 
     ` Return&#160;true&#160;if&#160;this&#160;widget&#160;exists. `

 winfo_fpixels  (self, number) 
     ` Return&#160;the&#160;number&#160;of&#160;pixels&#160;for&#160;the&#160;given&#160;distance&#160;NUMBER   
(e.g.&#160;"3c")&#160;as&#160;float. `

 winfo_geometry  (self) 
     ` Return&#160;geometry&#160;string&#160;for&#160;this&#160;widget&#160;in&#160;the&#160;form&#160;"widthxheight+X+Y". `

 winfo_height  (self) 
     ` Return&#160;height&#160;of&#160;this&#160;widget. `

 winfo_id  (self) 
     ` Return&#160;identifier&#160;ID&#160;for&#160;this&#160;widget. `

 winfo_interps  (self, displayof  =0  ) 
     ` Return&#160;the&#160;name&#160;of&#160;all&#160;Tcl&#160;interpreters&#160;for&#160;this&#160;display. `

 winfo_ismapped  (self) 
     ` Return&#160;true&#160;if&#160;this&#160;widget&#160;is&#160;mapped. `

 winfo_manager  (self) 
     ` Return&#160;the&#160;window&#160;mananger&#160;name&#160;for&#160;this&#160;widget. `

 winfo_name  (self) 
     ` Return&#160;the&#160;name&#160;of&#160;this&#160;widget. `

 winfo_parent  (self) 
     ` Return&#160;the&#160;name&#160;of&#160;the&#160;parent&#160;of&#160;this&#160;widget. `

 winfo_pathname  (self, id, displayof  =0  ) 
     ` Return&#160;the&#160;pathname&#160;of&#160;the&#160;widget&#160;given&#160;by&#160;ID. `

 winfo_pixels  (self, number) 
     ` Rounded&#160;integer&#160;value&#160;of&#160;winfo_fpixels. `

 winfo_pointerx  (self) 
     ` Return&#160;the&#160;x&#160;coordinate&#160;of&#160;the&#160;pointer&#160;on&#160;the&#160;root&#160;window. `

 winfo_pointerxy  (self) 
     ` Return&#160;a&#160;tuple&#160;of&#160;x&#160;and&#160;y&#160;coordinates&#160;of&#160;the&#160;pointer&#160;on&#160;the&#160;root&#160;window. `

 winfo_pointery  (self) 
     ` Return&#160;the&#160;y&#160;coordinate&#160;of&#160;the&#160;pointer&#160;on&#160;the&#160;root&#160;window. `

 winfo_reqheight  (self) 
     ` Return&#160;requested&#160;height&#160;of&#160;this&#160;widget. `

 winfo_reqwidth  (self) 
     ` Return&#160;requested&#160;width&#160;of&#160;this&#160;widget. `

 winfo_rgb  (self, color) 
     ` Return&#160;tuple&#160;of&#160;decimal&#160;values&#160;for&#160;red,&#160;green,&#160;blue&#160;for   
COLOR&#160;in&#160;this&#160;widget. `

 winfo_rootx  (self) 
     ` Return&#160;x&#160;coordinate&#160;of&#160;upper&#160;left&#160;corner&#160;of&#160;this&#160;widget&#160;on&#160;the   
root&#160;window. `

 winfo_rooty  (self) 
     ` Return&#160;y&#160;coordinate&#160;of&#160;upper&#160;left&#160;corner&#160;of&#160;this&#160;widget&#160;on&#160;the   
root&#160;window. `

 winfo_screen  (self) 
     ` Return&#160;the&#160;screen&#160;name&#160;of&#160;this&#160;widget. `

 winfo_screencells  (self) 
     ` Return&#160;the&#160;number&#160;of&#160;the&#160;cells&#160;in&#160;the&#160;colormap&#160;of&#160;the&#160;screen   
of&#160;this&#160;widget. `

 winfo_screendepth  (self) 
     ` Return&#160;the&#160;number&#160;of&#160;bits&#160;per&#160;pixel&#160;of&#160;the&#160;root&#160;window&#160;of&#160;the   
screen&#160;of&#160;this&#160;widget. `

 winfo_screenheight  (self) 
     ` Return&#160;the&#160;number&#160;of&#160;pixels&#160;of&#160;the&#160;height&#160;of&#160;the&#160;screen&#160;of&#160;this&#160;widget   
in&#160;pixel. `

 winfo_screenmmheight  (self) 
     ` Return&#160;the&#160;number&#160;of&#160;pixels&#160;of&#160;the&#160;height&#160;of&#160;the&#160;screen&#160;of   
this&#160;widget&#160;in&#160;mm. `

 winfo_screenmmwidth  (self) 
     ` Return&#160;the&#160;number&#160;of&#160;pixels&#160;of&#160;the&#160;width&#160;of&#160;the&#160;screen&#160;of   
this&#160;widget&#160;in&#160;mm. `

 winfo_screenvisual  (self) 
     ` Return&#160;one&#160;of&#160;the&#160;strings&#160;directcolor,&#160;grayscale,&#160;pseudocolor,   
staticcolor,&#160;staticgray,&#160;or&#160;truecolor&#160;for&#160;the&#160;default  
colormodel&#160;of&#160;this&#160;screen. `

 winfo_screenwidth  (self) 
     ` Return&#160;the&#160;number&#160;of&#160;pixels&#160;of&#160;the&#160;width&#160;of&#160;the&#160;screen&#160;of   
this&#160;widget&#160;in&#160;pixel. `

 winfo_server  (self) 
     ` Return&#160;information&#160;of&#160;the&#160;X-Server&#160;of&#160;the&#160;screen&#160;of&#160;this&#160;widget&#160;in   
the&#160;form&#160;"XmajorRminor&#160;vendor&#160;vendorVersion". `

 winfo_toplevel  (self) 
     ` Return&#160;the&#160;toplevel&#160;widget&#160;of&#160;this&#160;widget. `

 winfo_viewable  (self) 
     ` Return&#160;true&#160;if&#160;the&#160;widget&#160;and&#160;all&#160;its&#160;higher&#160;ancestors&#160;are&#160;mapped. `

 winfo_visual  (self) 
     ` Return&#160;one&#160;of&#160;the&#160;strings&#160;directcolor,&#160;grayscale,&#160;pseudocolor,   
staticcolor,&#160;staticgray,&#160;or&#160;truecolor&#160;for&#160;the  
colormodel&#160;of&#160;this&#160;widget. `

 winfo_visualid  (self) 
     ` Return&#160;the&#160;X&#160;identifier&#160;for&#160;the&#160;visual&#160;for&#160;this&#160;widget. `

 winfo_visualsavailable  (self, includeids  =0  ) 
     ` Return&#160;a&#160;list&#160;of&#160;all&#160;visuals&#160;available&#160;for&#160;the&#160;screen   
of&#160;this&#160;widget.  
  
Each&#160;item&#160;in&#160;the&#160;list&#160;consists&#160;of&#160;a&#160;visual&#160;name&#160;(see&#160;winfo_visual),&#160;a  
depth&#160;and&#160;if&#160;INCLUDEIDS=1&#160;is&#160;given&#160;also&#160;the&#160;X&#160;identifier. `

 winfo_vrootheight  (self) 
     ` Return&#160;the&#160;height&#160;of&#160;the&#160;virtual&#160;root&#160;window&#160;associated&#160;with&#160;this   
widget&#160;in&#160;pixels.&#160;If&#160;there&#160;is&#160;no&#160;virtual&#160;root&#160;window&#160;return&#160;the  
height&#160;of&#160;the&#160;screen. `

 winfo_vrootwidth  (self) 
     ` Return&#160;the&#160;width&#160;of&#160;the&#160;virtual&#160;root&#160;window&#160;associated&#160;with&#160;this   
widget&#160;in&#160;pixel.&#160;If&#160;there&#160;is&#160;no&#160;virtual&#160;root&#160;window&#160;return&#160;the  
width&#160;of&#160;the&#160;screen. `

 winfo_vrootx  (self) 
     ` Return&#160;the&#160;x&#160;offset&#160;of&#160;the&#160;virtual&#160;root&#160;relative&#160;to&#160;the&#160;root   
window&#160;of&#160;the&#160;screen&#160;of&#160;this&#160;widget. `

 winfo_vrooty  (self) 
     ` Return&#160;the&#160;y&#160;offset&#160;of&#160;the&#160;virtual&#160;root&#160;relative&#160;to&#160;the&#160;root   
window&#160;of&#160;the&#160;screen&#160;of&#160;this&#160;widget. `

 winfo_width  (self) 
     ` Return&#160;the&#160;width&#160;of&#160;this&#160;widget. `

 winfo_x  (self) 
     ` Return&#160;the&#160;x&#160;coordinate&#160;of&#160;the&#160;upper&#160;left&#160;corner&#160;of&#160;this&#160;widget   
in&#160;the&#160;parent. `

 winfo_y  (self) 
     ` Return&#160;the&#160;y&#160;coordinate&#160;of&#160;the&#160;upper&#160;left&#160;corner&#160;of&#160;this&#160;widget   
in&#160;the&#160;parent. `

* * *

Data and other attributes inherited from [ Tkinter.Misc ](/Tkinter.html) :  

 getdouble  = <type 'float'>
     ` float(x)&#160;->&#160;floating&#160;point&#160;number   
  
Convert&#160;a&#160;string&#160;or&#160;number&#160;to&#160;a&#160;floating&#160;point&#160;number,&#160;if&#160;possible. `

 getint  = <type 'int'>
     ` int(x[,&#160;base])&#160;->&#160;integer   
  
Convert&#160;a&#160;string&#160;or&#160;number&#160;to&#160;an&#160;integer,&#160;if&#160;possible.&#160;&#160;A&#160;floating&#160;point  
argument&#160;will&#160;be&#160;truncated&#160;towards&#160;zero&#160;(this&#160;does&#160;not&#160;include&#160;a&#160;string  
representation&#160;of&#160;a&#160;floating&#160;point&#160;number!)&#160;&#160;When&#160;converting&#160;a&#160;string,&#160;use  
the&#160;optional&#160;base.&#160;&#160;It&#160;is&#160;an&#160;error&#160;to&#160;supply&#160;a&#160;base&#160;when&#160;converting&#160;a  
non-string.&#160;If&#160;the&#160;argument&#160;is&#160;outside&#160;the&#160;integer&#160;range&#160;a&#160;long&#160;object  
will&#160;be&#160;returned&#160;instead. `

* * *

Methods inherited from [ Tkinter.Pack ](/Tkinter.html) :  

 forget  = pack_forget(self) 
     ` Unmap&#160;this&#160;widget&#160;and&#160;do&#160;not&#160;use&#160;it&#160;for&#160;the&#160;packing&#160;order. `

 info  = pack_info(self) 
     ` Return&#160;information&#160;about&#160;the&#160;packing&#160;options   
for&#160;this&#160;widget. `

 pack  = pack_configure(self, cnf  ={}  , kw) 
     ` Pack&#160;a&#160;widget&#160;in&#160;the&#160;parent&#160;widget.&#160;Use&#160;as&#160;options:   
after=widget&#160;-&#160;pack&#160;it&#160;after&#160;you&#160;have&#160;packed&#160;widget  
anchor=NSEW&#160;(or&#160;subset)&#160;-&#160;position&#160;widget&#160;according&#160;to  
given&#160;direction  
before=widget&#160;-&#160;pack&#160;it&#160;before&#160;you&#160;will&#160;pack&#160;widget  
expand=bool&#160;-&#160;expand&#160;widget&#160;if&#160;parent&#160;size&#160;grows  
fill=NONE&#160;or&#160;X&#160;or&#160;Y&#160;or&#160;BOTH&#160;-&#160;fill&#160;widget&#160;if&#160;widget&#160;grows  
in=master&#160;-&#160;use&#160;master&#160;to&#160;contain&#160;this&#160;widget  
ipadx=amount&#160;-&#160;add&#160;internal&#160;padding&#160;in&#160;x&#160;direction  
ipady=amount&#160;-&#160;add&#160;internal&#160;padding&#160;in&#160;y&#160;direction  
padx=amount&#160;-&#160;add&#160;padding&#160;in&#160;x&#160;direction  
pady=amount&#160;-&#160;add&#160;padding&#160;in&#160;y&#160;direction  
side=TOP&#160;or&#160;BOTTOM&#160;or&#160;LEFT&#160;or&#160;RIGHT&#160;-&#160;&#160;where&#160;to&#160;add&#160;this&#160;widget. `

 pack_configure  (self, cnf  ={}  , kw) 
     ` Pack&#160;a&#160;widget&#160;in&#160;the&#160;parent&#160;widget.&#160;Use&#160;as&#160;options:   
after=widget&#160;-&#160;pack&#160;it&#160;after&#160;you&#160;have&#160;packed&#160;widget  
anchor=NSEW&#160;(or&#160;subset)&#160;-&#160;position&#160;widget&#160;according&#160;to  
given&#160;direction  
before=widget&#160;-&#160;pack&#160;it&#160;before&#160;you&#160;will&#160;pack&#160;widget  
expand=bool&#160;-&#160;expand&#160;widget&#160;if&#160;parent&#160;size&#160;grows  
fill=NONE&#160;or&#160;X&#160;or&#160;Y&#160;or&#160;BOTH&#160;-&#160;fill&#160;widget&#160;if&#160;widget&#160;grows  
in=master&#160;-&#160;use&#160;master&#160;to&#160;contain&#160;this&#160;widget  
ipadx=amount&#160;-&#160;add&#160;internal&#160;padding&#160;in&#160;x&#160;direction  
ipady=amount&#160;-&#160;add&#160;internal&#160;padding&#160;in&#160;y&#160;direction  
padx=amount&#160;-&#160;add&#160;padding&#160;in&#160;x&#160;direction  
pady=amount&#160;-&#160;add&#160;padding&#160;in&#160;y&#160;direction  
side=TOP&#160;or&#160;BOTTOM&#160;or&#160;LEFT&#160;or&#160;RIGHT&#160;-&#160;&#160;where&#160;to&#160;add&#160;this&#160;widget. `

 pack_forget  (self) 
     ` Unmap&#160;this&#160;widget&#160;and&#160;do&#160;not&#160;use&#160;it&#160;for&#160;the&#160;packing&#160;order. `

 pack_info  (self) 
     ` Return&#160;information&#160;about&#160;the&#160;packing&#160;options   
for&#160;this&#160;widget. `

* * *

Methods inherited from [ Tkinter.Place ](/Tkinter.html) :  

 place  = place_configure(self, cnf  ={}  , kw) 
     ` Place&#160;a&#160;widget&#160;in&#160;the&#160;parent&#160;widget.&#160;Use&#160;as&#160;options:   
in=master&#160;-&#160;master&#160;relative&#160;to&#160;which&#160;the&#160;widget&#160;is&#160;placed.  
x=amount&#160;-&#160;locate&#160;anchor&#160;of&#160;this&#160;widget&#160;at&#160;position&#160;x&#160;of&#160;master  
y=amount&#160;-&#160;locate&#160;anchor&#160;of&#160;this&#160;widget&#160;at&#160;position&#160;y&#160;of&#160;master  
relx=amount&#160;-&#160;locate&#160;anchor&#160;of&#160;this&#160;widget&#160;between&#160;0.0&#160;and&#160;1.0  
relative&#160;to&#160;width&#160;of&#160;master&#160;(1.0&#160;is&#160;right&#160;edge)  
rely=amount&#160;-&#160;locate&#160;anchor&#160;of&#160;this&#160;widget&#160;between&#160;0.0&#160;and&#160;1.0  
relative&#160;to&#160;height&#160;of&#160;master&#160;(1.0&#160;is&#160;bottom&#160;edge)  
anchor=NSEW&#160;(or&#160;subset)&#160;-&#160;position&#160;anchor&#160;according&#160;to&#160;given&#160;direction  
width=amount&#160;-&#160;width&#160;of&#160;this&#160;widget&#160;in&#160;pixel  
height=amount&#160;-&#160;height&#160;of&#160;this&#160;widget&#160;in&#160;pixel  
relwidth=amount&#160;-&#160;width&#160;of&#160;this&#160;widget&#160;between&#160;0.0&#160;and&#160;1.0  
relative&#160;to&#160;width&#160;of&#160;master&#160;(1.0&#160;is&#160;the&#160;same&#160;width  
as&#160;the&#160;master)  
relheight=amount&#160;-&#160;height&#160;of&#160;this&#160;widget&#160;between&#160;0.0&#160;and&#160;1.0  
relative&#160;to&#160;height&#160;of&#160;master&#160;(1.0&#160;is&#160;the&#160;same  
height&#160;as&#160;the&#160;master)  
bordermode="inside"&#160;or&#160;"outside"&#160;-&#160;whether&#160;to&#160;take&#160;border&#160;width&#160;of&#160;master
widget  
into&#160;account `

 place_configure  (self, cnf  ={}  , kw) 
     ` Place&#160;a&#160;widget&#160;in&#160;the&#160;parent&#160;widget.&#160;Use&#160;as&#160;options:   
in=master&#160;-&#160;master&#160;relative&#160;to&#160;which&#160;the&#160;widget&#160;is&#160;placed.  
x=amount&#160;-&#160;locate&#160;anchor&#160;of&#160;this&#160;widget&#160;at&#160;position&#160;x&#160;of&#160;master  
y=amount&#160;-&#160;locate&#160;anchor&#160;of&#160;this&#160;widget&#160;at&#160;position&#160;y&#160;of&#160;master  
relx=amount&#160;-&#160;locate&#160;anchor&#160;of&#160;this&#160;widget&#160;between&#160;0.0&#160;and&#160;1.0  
relative&#160;to&#160;width&#160;of&#160;master&#160;(1.0&#160;is&#160;right&#160;edge)  
rely=amount&#160;-&#160;locate&#160;anchor&#160;of&#160;this&#160;widget&#160;between&#160;0.0&#160;and&#160;1.0  
relative&#160;to&#160;height&#160;of&#160;master&#160;(1.0&#160;is&#160;bottom&#160;edge)  
anchor=NSEW&#160;(or&#160;subset)&#160;-&#160;position&#160;anchor&#160;according&#160;to&#160;given&#160;direction  
width=amount&#160;-&#160;width&#160;of&#160;this&#160;widget&#160;in&#160;pixel  
height=amount&#160;-&#160;height&#160;of&#160;this&#160;widget&#160;in&#160;pixel  
relwidth=amount&#160;-&#160;width&#160;of&#160;this&#160;widget&#160;between&#160;0.0&#160;and&#160;1.0  
relative&#160;to&#160;width&#160;of&#160;master&#160;(1.0&#160;is&#160;the&#160;same&#160;width  
as&#160;the&#160;master)  
relheight=amount&#160;-&#160;height&#160;of&#160;this&#160;widget&#160;between&#160;0.0&#160;and&#160;1.0  
relative&#160;to&#160;height&#160;of&#160;master&#160;(1.0&#160;is&#160;the&#160;same  
height&#160;as&#160;the&#160;master)  
bordermode="inside"&#160;or&#160;"outside"&#160;-&#160;whether&#160;to&#160;take&#160;border&#160;width&#160;of&#160;master
widget  
into&#160;account `

 place_forget  (self) 
     ` Unmap&#160;this&#160;widget. `

 place_info  (self) 
     ` Return&#160;information&#160;about&#160;the&#160;placing&#160;options   
for&#160;this&#160;widget. `

* * *

Methods inherited from [ Tkinter.Grid ](/Tkinter.html) :  

 grid  = grid_configure(self, cnf  ={}  , kw) 
     ` Position&#160;a&#160;widget&#160;in&#160;the&#160;parent&#160;widget&#160;in&#160;a&#160;grid.&#160;Use&#160;as&#160;options:   
column=number&#160;-&#160;use&#160;cell&#160;identified&#160;with&#160;given&#160;column&#160;(starting&#160;with&#160;0)  
columnspan=number&#160;-&#160;this&#160;widget&#160;will&#160;span&#160;several&#160;columns  
in=master&#160;-&#160;use&#160;master&#160;to&#160;contain&#160;this&#160;widget  
ipadx=amount&#160;-&#160;add&#160;internal&#160;padding&#160;in&#160;x&#160;direction  
ipady=amount&#160;-&#160;add&#160;internal&#160;padding&#160;in&#160;y&#160;direction  
padx=amount&#160;-&#160;add&#160;padding&#160;in&#160;x&#160;direction  
pady=amount&#160;-&#160;add&#160;padding&#160;in&#160;y&#160;direction  
row=number&#160;-&#160;use&#160;cell&#160;identified&#160;with&#160;given&#160;row&#160;(starting&#160;with&#160;0)  
rowspan=number&#160;-&#160;this&#160;widget&#160;will&#160;span&#160;several&#160;rows  
sticky=NSEW&#160;-&#160;if&#160;cell&#160;is&#160;larger&#160;on&#160;which&#160;sides&#160;will&#160;this  
widget&#160;stick&#160;to&#160;the&#160;cell&#160;boundary `

 grid_configure  (self, cnf  ={}  , kw) 
     ` Position&#160;a&#160;widget&#160;in&#160;the&#160;parent&#160;widget&#160;in&#160;a&#160;grid.&#160;Use&#160;as&#160;options:   
column=number&#160;-&#160;use&#160;cell&#160;identified&#160;with&#160;given&#160;column&#160;(starting&#160;with&#160;0)  
columnspan=number&#160;-&#160;this&#160;widget&#160;will&#160;span&#160;several&#160;columns  
in=master&#160;-&#160;use&#160;master&#160;to&#160;contain&#160;this&#160;widget  
ipadx=amount&#160;-&#160;add&#160;internal&#160;padding&#160;in&#160;x&#160;direction  
ipady=amount&#160;-&#160;add&#160;internal&#160;padding&#160;in&#160;y&#160;direction  
padx=amount&#160;-&#160;add&#160;padding&#160;in&#160;x&#160;direction  
pady=amount&#160;-&#160;add&#160;padding&#160;in&#160;y&#160;direction  
row=number&#160;-&#160;use&#160;cell&#160;identified&#160;with&#160;given&#160;row&#160;(starting&#160;with&#160;0)  
rowspan=number&#160;-&#160;this&#160;widget&#160;will&#160;span&#160;several&#160;rows  
sticky=NSEW&#160;-&#160;if&#160;cell&#160;is&#160;larger&#160;on&#160;which&#160;sides&#160;will&#160;this  
widget&#160;stick&#160;to&#160;the&#160;cell&#160;boundary `

 grid_forget  (self) 
     ` Unmap&#160;this&#160;widget. `

 grid_info  (self) 
     ` Return&#160;information&#160;about&#160;the&#160;options   
for&#160;positioning&#160;this&#160;widget&#160;in&#160;a&#160;grid. `

 grid_remove  (self) 
     ` Unmap&#160;this&#160;widget&#160;but&#160;remember&#160;the&#160;grid&#160;options. `

 location  = grid_location(self, x, y) 
     ` Return&#160;a&#160;tuple&#160;of&#160;column&#160;and&#160;row&#160;which&#160;identify&#160;the&#160;cell   
at&#160;which&#160;the&#160;pixel&#160;at&#160;position&#160;X&#160;and&#160;Y&#160;inside&#160;the&#160;master  
widget&#160;is&#160;located. `

  
class  create 

` `

` #---------------------------------------------------------------------  
#  
#&#160;Start&#160;of&#160;Popup&#160;Dialog  
#  
#---------------------------------------------------------------------------  
#&#160;VCS&#160;Plot&#160;Annotation&#160;Dialog&#160;Popup  
#---------------------------------------------------------------------------  
`

Methods defined here:  

 __init__  (self, parent) 

 annotate_cancel  (self, parent) 

 annotate_clear  (self, parent) 

 annotate_replot  (self, parent) 

 annotate_reset  (self, parent) 

 evt_set_toggle_state  (self, parent, id) 

 execute  (self, parent, result) 

 get_settings  (self, parent) 

 hold_annotate_cancel_settings  (self, parent) 

 hold_annotate_original_settings  (self, parent) 

 master_switch  (self, parent, result) 

 retain_switch  (self, parent, result) 

  
 Functions 

` `

 get_annotation_info  (parent, data_name  =None  ) 
     ` #---------------------------------------------------------------------   
#  
#&#160;Get&#160;the&#160;annotation&#160;infomation&#160;from&#160;the&#160;data&#160;variable  
#  
#--------------------------------------------------------------------------- `

  
 Data 

` `

 Pmw  = <Pmw.Pmw_1_2.lib.PmwLoader.PmwLoader instance>

* * *

UCRL-WEB-213937 | [ Privacy & Legal Notice ](/disclaimer.html)

[ webmaster@pcmdi.llnl.gov ](/webmaster@pcmdi.llnl.gov)

[ ![Powered by Plone](media/plone_powered.gif) ](/)

