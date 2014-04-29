---
layout: default
title:
---

 [ Skip to content. ](/cdat/source/api-reference/vcs.colors.html) | [ Skip to
navigation ](/cdat/source/api-reference/vcs.colors.html)

Search Site

[ Advanced Search&#8230; ](/search_form)

#  [ PCMDI Software Portal ](/)

#####  Sections

  * [ Home ](/)

#####  Personal tools

  * [ Log in ](/login_form)

You are here:  [ Home ](/) -> [ CDAT ](/cdat) -> [ Source Code ](/cdat/source)
-> [ API Reference ](/cdat/source/api-reference) -> Python: module vcs.colors

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

        * [ Python: module vcs.colors ](/cdat/source/api-reference/vcs.colors.html)

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

  * [ ![Send this page to somebody](media/mail_icon.gif) ](/cdat/source/api-reference/vcs.colors.html/sendto_form)
  * [ ![Print this page](media/print_icon.gif) ](/this.print\(\))

#  Python: module vcs.colors

  
  
 [ vcs  ](/vcs.html) .colors 
[ index ](/)  

  
 Functions 

` `

 rgb2str  (r, g  =None  , b  =None  ) 
     ` Input&#160;rgb&#160;values,&#160;return&#160;the&#160;closest&#160;name   
example:  
print [ rgb2str ](/) ([0,0,0])  
>>>&#160;'black' `

 str2rgb  (col) 
     ` Input&#160;a&#160;string&#160;representing&#160;a&#160;color&#160;name&#160;and&#160;it&#160;outputs&#160;the&#160;corresponding&#160;r,g,b&#160;values   
If&#160;the&#160;color&#160;name&#160;is&#160;unknown,&#160;returns&#160;None,None,None  
looks&#160;into&#160;/usr/X11R6/lib/X11/rgb.txt&#160;file  
if&#160;file&#160;does&#160;not&#160;exist&#160;then&#160;looks&#160;into&#160;the&#160;builtin&#160;dictionary  
Examples:  
r,g,b= [ str2rgb ](/) ('pink2')&#160;#&#160;returns:&#160;[238&#160;,&#160;169&#160;,&#160;184&#160;]  
r,g,b= [ str2rgb ](/) ('crapy')&#160;#&#160;returns:&#160;[None,&#160;None,&#160;None]  
Note&#160;r,g,b&#160;values&#160;between&#160;0&#160;and&#160;255 `

  
 Data 

` `

 cols  = {'AliceBlue': [240, 248, 255], 'AntiqueWhite': [250, 235, 215], 'AntiqueWhite1': [255, 239, 219], 'AntiqueWhite2': [238, 223, 204], 'AntiqueWhite3': [205, 192, 176], 'AntiqueWhite4': [139, 131, 120], 'BlanchedAlmond': [255, 235, 205], 'BlueViolet': [138, 43, 226], 'CadetBlue': [95, 158, 160], 'CadetBlue1': [152, 245, 255], ...} 

* * *

UCRL-WEB-213937 | [ Privacy & Legal Notice ](/disclaimer.html)

[ webmaster@pcmdi.llnl.gov ](/webmaster@pcmdi.llnl.gov)

[ ![Powered by Plone](media/plone_powered.gif) ](/)

