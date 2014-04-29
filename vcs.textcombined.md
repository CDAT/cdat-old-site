---
layout: default
title:
---

 [ Skip to content. ](/cdat/source/api-reference/vcs.textcombined.html) | [
Skip to navigation ](/cdat/source/api-reference/vcs.textcombined.html)

Search Site

[ Advanced Search&#8230; ](/search_form)

#  [ PCMDI Software Portal ](/)

#####  Sections

  * [ Home ](/)

#####  Personal tools

  * [ Log in ](/login_form)

You are here:  [ Home ](/) -> [ CDAT ](/cdat) -> [ Source Code ](/cdat/source)
-> [ API Reference ](/cdat/source/api-reference) -> Python: module
vcs.textcombined

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

        * [ Python: module vcs.textcombined ](/cdat/source/api-reference/vcs.textcombined.html)

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

  * [ ![Send this page to somebody](media/mail_icon.gif) ](/cdat/source/api-reference/vcs.textcombined.html/sendto_form)
  * [ ![Print this page](media/print_icon.gif) ](/this.print\(\))

#  Python: module vcs.textcombined

  
  
 [ vcs  ](/vcs.html) .textcombined 
[ index ](/)  

` #&#160;Text&#160;Combined&#160;( [ Tc ](/) )&#160;module `

  
 Modules 

` `

[ vcs.Canvas ](/vcs.Canvas.html)  

[ Numeric ](/Numeric.html)  

[ vcs.VCS_validation_functions ](/vcs.VCS_validation_functions.html)  

  
 Classes 

` `

[ vcs.textorientation.To ](/vcs.textorientation.html)

    

[ Tc ](/vcs.textcombined.html) ( [ vcs.texttable.Tt ](/vcs.texttable.html) , [
vcs.textorientation.To ](/vcs.textorientation.html) )

[ vcs.texttable.Tt ](/vcs.texttable.html)

    

[ Tc ](/vcs.textcombined.html) ( [ vcs.texttable.Tt ](/vcs.texttable.html) , [
vcs.textorientation.To ](/vcs.textorientation.html) )

  
class  Tc  ( [ vcs.texttable.Tt ](/vcs.texttable.html) , [
vcs.textorientation.To ](/vcs.textorientation.html) )

` `

` Class: [ Tc ](/) #&#160;Text&#160;Combined  
  
Description&#160;of [ Tc ](/) Class:  
The&#160;( [ Tc ](/) )&#160;Text&#160;Combined&#160;class&#160;will&#160;combine&#160;a&#160;text&#160;table&#160;class&#160;and&#160;a
text&#160;orientation  
class&#160;together.&#160;From&#160;combining&#160;the&#160;two&#160;classess,&#160;the&#160;user&#160;will&#160;be&#160;able&#160;to&#160;set  
attributes&#160;for&#160;both&#160;classes&#160;(i.e.,&#160;define&#160;the&#160;font,&#160;spacing,&#160;expansion,&#160;color  
index,&#160;height,&#160;angle,&#160;path,&#160;vertical&#160;alignment,&#160;and&#160;horizontal&#160;alignment).  
  
This&#160;class&#160;is&#160;used&#160;to&#160;define&#160;and&#160;list&#160;a&#160;combined&#160;text&#160;table&#160;and&#160;text
orientation  
entry&#160;used&#160;in&#160;VCS.  
  
Other&#160;Useful&#160;Functions:  
a=vcs.init()&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#&#160;Constructor  
a.show('texttable')&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#&#160;Show&#160;predefined&#160;text&#160;table&#160;objects  
a.show('textorientation')&#160;&#160;#&#160;Show&#160;predefined&#160;text&#160;orientation&#160;objects  
a.update()&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#&#160;Updates&#160;the&#160;VCS&#160;Canvas&#160;at&#160;user's&#160;request  
a.mode=1,&#160;or&#160;0&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#&#160;If&#160;1,&#160;then&#160;automatic&#160;update,&#160;else&#160;if  
0,&#160;then&#160;use&#160;update&#160;function&#160;to  
update&#160;the&#160;VCS&#160;Canvas.  
Example&#160;of&#160;Use:  
a=vcs.init()  
[ To ](/vcs.textorientation.html) Create&#160;a&#160;new&#160;instance&#160;of&#160;text&#160;table&#160;use:  
tc=a.createtextcombined('new_tt','std','new_to','7left')&#160;&#160;#&#160;Copies&#160;content&#160;of  
#&#160;'std'&#160;to&#160;'new_tt'&#160;and&#160;'7left'&#160;to&#160;'new_to'  
  
[ To ](/vcs.textorientation.html) Modify&#160;an&#160;existing&#160;texttable&#160;use:  
tc=a.gettextcombined('std','7left')  
  
tc. [ list ](/) ()&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#&#160;Will&#160;list&#160;all&#160;the&#160;textcombined
attribute&#160;values  
#&#160;(i.e.,&#160;texttable&#160;and&#160;textorientation&#160;attributes  
Specify&#160;the&#160;text&#160;font&#160;type:  
tc.font=1&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#&#160;The&#160;font&#160;value&#160;must&#160;be&#160;in&#160;the&#160;range&#160;1&#160;to
9  
  
Specify&#160;the&#160;text&#160;spacing:  
tc.spacing=2&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#&#160;The&#160;spacing&#160;value&#160;must&#160;be&#160;in&#160;the&#160;range
-50&#160;to&#160;50  
  
Specify&#160;the&#160;text&#160;expansion:  
tc.expansion=100&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#&#160;The&#160;expansion&#160;value&#160;ranges&#160;from&#160;50&#160;to&#160;150  
  
Specify&#160;the&#160;text&#160;color:  
tc.color=241&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#&#160;The&#160;text&#160;color&#160;value&#160;ranges&#160;from&#160;1&#160;to&#160;257  
  
Specify&#160;the&#160;graphics&#160;text&#160;priority&#160;on&#160;the&#160;VCS&#160;Canvas:  
tt.priority&#160;=&#160;1  
  
Specify&#160;the&#160;viewport&#160;and&#160;world&#160;coordinate:  
tt.viewport=[0,&#160;1.0,&#160;0,1.0]&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#&#160;FloatType&#160;[0,1]x[0,1]  
tt.worldcoordinate=[0,1.0,0,1.0]&#160;&#160;&#160;#&#160;FloatType&#160;[#,#]x[#,#]  
  
Specify&#160;the&#160;location&#160;of&#160;the&#160;text:  
tt.x=[[0,.1,.2],&#160;[.3,.4,.5]]&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#&#160;List&#160;of&#160;FloatTypes  
tt.y=[[.5,.4,.3],&#160;[.2,.1,0]]&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#&#160;List&#160;of&#160;FloatTypes  
  
Specify&#160;the&#160;text&#160;height:  
tc.height=20&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#&#160;The&#160;height&#160;value&#160;must&#160;be&#160;an&#160;integer  
  
Specify&#160;the&#160;text&#160;angle:  
tc.angle=0&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#&#160;The&#160;angle&#160;value&#160;ranges&#160;from&#160;0&#160;to&#160;360  
  
Specify&#160;the&#160;text&#160;path:  
tc.path='right'&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#&#160;Same&#160;as&#160;tc.path=0  
tc.path='left'&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#&#160;Same&#160;as&#160;tc.path=1  
tc.path='up'&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#&#160;Same&#160;as&#160;tc.path=2  
tc.path='down'&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#&#160;Same&#160;as&#160;tc.path=3  
  
Specify&#160;the&#160;text&#160;horizontal&#160;alignment:  
tc.halign='right'&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#&#160;Same&#160;as&#160;tc.halign=0  
tc.halign='center'&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#&#160;Same&#160;as&#160;tc.halign=1  
tc.halign='right'&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#&#160;Same&#160;as&#160;tc.halign=2  
  
Specify&#160;the&#160;text&#160;vertical&#160;alignment:  
tc.valign='tcp'&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#&#160;Same&#160;as&#160;tcvalign=0  
tc.valign='cap'&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#&#160;Same&#160;as&#160;tcvalign=1  
tc.valign='half'&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#&#160;Same&#160;as&#160;tcvalign=2  
tc.valign='base'&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#&#160;Same&#160;as&#160;tcvalign=3  
tc.valign='bottom'&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#&#160;Same&#160;as&#160;tcvalign=4  
`

Method resolution order:

     [ Tc ](/vcs.textcombined.html)
     [ vcs.texttable.Tt ](/vcs.texttable.html)
     [ vcs.textorientation.To ](/vcs.textorientation.html)

* * *

Methods defined here:  

 __init__  (self, parent, Tt_name  =None  , Tt_name_src  ='default'  , To_name  =None  , To_name_src  ='default'  , createTc  =0  ) 
     ` #############################################################################   
#&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#  
#&#160;Initialize&#160;the&#160;text&#160;combine&#160;attributes.&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#  
#&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#  
#############################################################################
`

 __setattr__  (self, name, value) 
     ` #############################################################################   
#&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#  
#&#160;Set&#160;text&#160;table&#160;and&#160;text&#160;orientation&#160;attributes.&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#  
#&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#  
#############################################################################
`

 list  (self) 
     ` #############################################################################   
#&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#  
#&#160;List&#160;out&#160;text&#160;combined&#160;members&#160;(attributes).&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#  
#&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#  
#############################################################################
`

 script  (self, script_filename  =None  , mode  =None  ) 
     ` Function:&#160;&#160;&#160;&#160;&#160;script&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#&#160;Calls&#160;_vcs.scripTo   
  
Description&#160;of&#160;Function:  
Saves&#160;out&#160;a&#160;text&#160;table&#160;and&#160;text&#160;orientation&#160;graphics&#160;method&#160;in&#160;Python&#160;or  
VCS&#160;script&#160;form&#160;to&#160;a&#160;designated&#160;file.  
  
Example&#160;of&#160;Use:  
[ script ](/) (scriptfile_name,mode)  
where:&#160;scriptfile_name&#160;is&#160;the&#160;output&#160;name&#160;of&#160;the&#160;script&#160;file.  
mode&#160;is&#160;either&#160;"w"&#160;for&#160;replace&#160;or&#160;"a"&#160;for&#160;append.  
  
Note:&#160;If&#160;the&#160;the&#160;filename&#160;has&#160;a&#160;".py"&#160;at&#160;the&#160;end,&#160;it&#160;will&#160;produce&#160;a  
Python&#160;script.&#160;If&#160;the&#160;filename&#160;has&#160;a&#160;".scr"&#160;at&#160;the&#160;end,&#160;it&#160;will  
produce&#160;a&#160;VCS&#160;script.&#160;If&#160;neither&#160;extensions&#160;are&#160;give,&#160;then&#160;by  
default&#160;a&#160;Python&#160;script&#160;will&#160;be&#160;produced.  
  
a=vcs.init()  
tc=a.createtextcombined('new_tt','std','new_to','7left')  
tc. [ script ](/) ('filename.py')&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#&#160;Append&#160;to&#160;a&#160;Python&#160;file
"filename.py"  
tc. [ script ](/) ('filename.scr')&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#&#160;Append&#160;to&#160;a&#160;VCS&#160;file
"filename.scr"  
tc. [ script ](/) ('filename','w')&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;#&#160;Create&#160;or&#160;overwrite&#160;to&#160;a&#160;Python
file&#160;"filename.py" `

  
 Data 

` `

 StringTypes  = (<type 'str'>, <type 'unicode'>) 

* * *

UCRL-WEB-213937 | [ Privacy & Legal Notice ](/disclaimer.html)

[ webmaster@pcmdi.llnl.gov ](/webmaster@pcmdi.llnl.gov)

[ ![Powered by Plone](media/plone_powered.gif) ](/)

