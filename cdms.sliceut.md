---
layout: default
title:
---

 [ Skip to content. ](/cdat/source/api-reference/cdms.sliceut.html) | [ Skip to
navigation ](/cdat/source/api-reference/cdms.sliceut.html)

Search Site

[ Advanced Search&#8230; ](/search_form)

#  [ PCMDI Software Portal ](/)

#####  Sections

  * [ Home ](/)

#####  Personal tools

  * [ Log in ](/login_form)

You are here:  [ Home ](/) -> [ CDAT ](/cdat) -> [ Source Code ](/cdat/source)
-> [ API Reference ](/cdat/source/api-reference) -> Python: module
cdms.sliceut

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

        * [ Python: module cdms.sliceut ](/cdat/source/api-reference/cdms.sliceut.html)

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

  * [ ![Send this page to somebody](media/mail_icon.gif) ](/cdat/source/api-reference/cdms.sliceut.html/sendto_form)
  * [ ![Print this page](media/print_icon.gif) ](/this.print\(\))

#  Python: module cdms.sliceut

  
  
 [ cdms  ](/cdms.html) .sliceut 
[ index ](/)  

` Utilities&#160;for&#160;manipulating&#160;slices `

  
 Functions 

` `

 lenSlice  (aSlice) 
     ` Return&#160;the&#160;number&#160;of&#160;values&#160;associated&#160;with&#160;a&#160;slice `

 reverseSlice  (s, size) 
     ` For&#160;'reversed'&#160;slices&#160;(slices&#160;with&#160;negative&#160;stride),   
return&#160;an&#160;equivalent&#160;slice&#160;with&#160;positive&#160;step.&#160;For&#160;positive  
strides,&#160;just&#160;return&#160;the&#160;slice&#160;unchanged. `

 sliceIntersect  (aSlice, interval) 

 slicePartition  (aSlice, partition) 

 splitSlice  (s, size) 
     ` For&#160;a&#160;'wraparound'&#160;slice,&#160;return&#160;two&#160;equivalent&#160;slices   
within&#160;the&#160;range&#160;0..size-1. `

 splitSliceExt  (s, size) 
     ` mf&#160;20010330&#160;\--   
For&#160;a&#160;'wraparound'&#160;slice,&#160;return&#160;N&#160;equivalent&#160;slices  
within&#160;the&#160;range&#160;0...(N*size)&#160;N&#160;=&#160;anything `

* * *

UCRL-WEB-213937 | [ Privacy & Legal Notice ](/disclaimer.html)

[ webmaster@pcmdi.llnl.gov ](/webmaster@pcmdi.llnl.gov)

[ ![Powered by Plone](media/plone_powered.gif) ](/)

