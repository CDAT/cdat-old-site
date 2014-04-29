---
layout: default
title:
---

 [ Skip to content. ](/cdat/source/api-reference/vcs.taylor.html) | [ Skip to
navigation ](/cdat/source/api-reference/vcs.taylor.html)

Search Site

[ Advanced Search&#8230; ](/search_form)

#  [ PCMDI Software Portal ](/)

#####  Sections

  * [ Home ](/)

#####  Personal tools

  * [ Log in ](/login_form)

You are here:  [ Home ](/) -> [ CDAT ](/cdat) -> [ Source Code ](/cdat/source)
-> [ API Reference ](/cdat/source/api-reference) -> Python: module vcs.taylor

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

        * [ Python: module vcs.taylor ](/cdat/source/api-reference/vcs.taylor.html)

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

  * [ ![Send this page to somebody](media/mail_icon.gif) ](/cdat/source/api-reference/vcs.taylor.html/sendto_form)
  * [ ![Print this page](media/print_icon.gif) ](/this.print\(\))

#  Python: module vcs.taylor

  
  
 [ vcs  ](/vcs.html) .taylor 
[ index ](/)  

  
 Modules 

` `

[ MA ](/MA.html)  
[ cdms.MV ](/cdms.MV.html)  
[ Numeric ](/Numeric.html)  

[ RandomArray ](/RandomArray.html)  
[ cdms ](/cdms.html)  
[ vcs.colors ](/vcs.colors.html)  

[ string ](/string.html)  
[ sys ](/sys.html)  
[ types ](/types.html)  

[ vcs ](/vcs.html)  

  
 Classes 

` `

[ Gtd ](/vcs.taylor.html)

[ TDMarker ](/vcs.taylor.html)

  
class  Gtd 

` `

Methods defined here:  

 __init__  (self) 

 __setattr__  (self, name, value) 

 addMarker  (self, status  ='on'  , line  =None  , id  =''  , id_size  =None  , id_color  =None  , id_font  =None  , symbol  =None  , color  =None  , size  =None  , xoffset  =0.0  , yoffset  =0.0  , line_color  =None  , line_size  =None  , line_type  =None  ) 

 color2vcs  (self, canvas, col) 

 defaultSkillFunction  (self, s, R) 
     ` Default&#160;skillfunction `

 draw  (self, canvas, data) 

 drawFrame  (self, canvas, data) 

 drawSkill  (self, canvas, values, function  =None  ) 
     ` Draw&#160;a&#160;skill&#160;score,&#160;default&#160;skill&#160;score&#160;provide&#160;in&#160;defaultSkill   
from&#160;Karl&#160;taylor,&#160;see&#160;PCMDI&#160;report&#160;series&#160;55 `

 drawarrow  (self, canvas, xloc, yloc, x1, y1, x2, y2, color) 

 init  (self) 

 list  (self) 

 matchVcsColor  (self, canvas, r, g, b) 

 plot  (self, data, template  ='default'  , skill  =None  , bg  =0  , canvas  =None  ) 
     ` plots `

 script  (self, file, option  ='a'  ) 

 setattr__  (self, name, value) 

  
class  TDMarker 

` `

Methods defined here:  

 __init__  (self, parent) 

 __len__  (self) 

 __setattr__  (self, name, value) 

 addMarker  (self, status  ='on'  , line  =None  , id  =''  , id_size  =None  , id_color  =None  , id_font  =None  , symbol  =None  , color  =None  , size  =None  , xoffset  =0.0  , yoffset  =0.0  , line_color  =None  , line_size  =None  , line_type  =None  ) 

 equalize  (self) 
     ` Make&#160;sure&#160;that&#160;we&#160;have&#160;the&#160;same&#160;amount&#160;of&#160;everything   
usage [ equalize ](/) ()  
Also&#160;updates&#160;self.  number  `

 insert  (self, i) 

 list  (self) 

 pop  (self, i) 

* * *

UCRL-WEB-213937 | [ Privacy & Legal Notice ](/disclaimer.html)

[ webmaster@pcmdi.llnl.gov ](/webmaster@pcmdi.llnl.gov)

[ ![Powered by Plone](media/plone_powered.gif) ](/)

