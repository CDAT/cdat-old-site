---
layout: default
title:
---

 [ Skip to content. ](/cdat/source/api-reference/cdutil.vertical.html) | [ Skip
to navigation ](/cdat/source/api-reference/cdutil.vertical.html)

Search Site

[ Advanced Search&#8230; ](/search_form)

#  [ PCMDI Software Portal ](/)

#####  Sections

  * [ Home ](/)

#####  Personal tools

  * [ Log in ](/login_form)

You are here:  [ Home ](/) -> [ CDAT ](/cdat) -> [ Source Code ](/cdat/source)
-> [ API Reference ](/cdat/source/api-reference) -> Python: module
cdutil.vertical

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

        * [ Python: module cdutil.vertical ](/cdat/source/api-reference/cdutil.vertical.html)

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

  * [ ![Send this page to somebody](media/mail_icon.gif) ](/cdat/source/api-reference/cdutil.vertical.html/sendto_form)
  * [ ![Print this page](media/print_icon.gif) ](/this.print\(\))

#  Python: module cdutil.vertical

  
  
 [ cdutil  ](/cdutil.html) .vertical 
[ index ](/)  

  
 Modules 

` `

[ MV ](/MV.html)  

[ cdms ](/cdms.html)  

[ genutil ](/genutil.html)  

  
 Functions 

` `

 linearInterpolation  (A, I, levels  =[100000, 92500, 85000, 70000, 60000, 50000, 40000, 30000, 25000, 20000, 15000, 10000, 7000, 5000, 3000, 2000, 1000]  , status  =None  ) 
     ` Linear&#160;interpolation   
to&#160;interpolate&#160;a&#160;field&#160;from&#160;some&#160;levels&#160;to&#160;another&#160;set&#160;of&#160;levels  
Value&#160;below&#160;"surface"&#160;are&#160;masked  
  
Input  
A&#160;:&#160;&#160;&#160;&#160;&#160;&#160;array&#160;to&#160;interpolate  
I&#160;:&#160;&#160;&#160;&#160;&#160;&#160;interpolation&#160;field&#160;(usually&#160;Pressure&#160;or&#160;depth)&#160;from&#160;TOP&#160;(level&#160;0)&#160;to
BOTTOM&#160;(last&#160;level)  
levels&#160;:&#160;levels&#160;to&#160;interplate&#160;to&#160;(same&#160;units&#160;as&#160;I),&#160;default&#160;levels
are:[100000,&#160;92500,&#160;85000,&#160;70000,&#160;60000,&#160;50000,&#160;40000,&#160;30000,&#160;25000,&#160;20000,
15000,&#160;10000,&#160;7000,&#160;5000,&#160;3000,&#160;2000,&#160;1000]  
  
I&#160;and&#160;levels&#160;must&#160;have&#160;same&#160;units  
  
Output  
array&#160;on&#160;new&#160;levels&#160;(levels)  
  
Examples:  
A=interpolate(A,I,levels=[100000,&#160;92500,&#160;85000,&#160;70000,&#160;60000,&#160;50000,&#160;40000,
30000,&#160;25000,&#160;20000,&#160;15000,&#160;10000,&#160;7000,&#160;5000,&#160;3000,&#160;2000,&#160;1000]) `

 logLinearInterpolation  (A, P, levels  =[100000, 92500, 85000, 70000, 60000, 50000, 40000, 30000, 25000, 20000, 15000, 10000, 7000, 5000, 3000, 2000, 1000]  , status  =None  ) 
     ` Log-linear&#160;interpolation   
to&#160;convert&#160;a&#160;field&#160;from&#160;sigma&#160;levels&#160;to&#160;pressure&#160;levels  
Value&#160;below&#160;surface&#160;are&#160;masked  
  
Input  
A&#160;:&#160;&#160;&#160;&#160;array&#160;on&#160;sigma&#160;levels  
P&#160;:&#160;&#160;&#160;&#160;pressure&#160;field&#160;from&#160;TOP&#160;(level&#160;0)&#160;to&#160;BOTTOM&#160;(last&#160;level)  
levels&#160;:&#160;pressure&#160;levels&#160;to&#160;interplate&#160;to&#160;(same&#160;units&#160;as&#160;P),&#160;default&#160;levels
are:[100000,&#160;92500,&#160;85000,&#160;70000,&#160;60000,&#160;50000,&#160;40000,&#160;30000,&#160;25000,&#160;20000,
15000,&#160;10000,&#160;7000,&#160;5000,&#160;3000,&#160;2000,&#160;1000]  
  
P&#160;and&#160;levels&#160;must&#160;have&#160;same&#160;units  
  
Output  
array&#160;on&#160;pressure&#160;levels&#160;(levels)  
  
Examples:  
A= [ logLinearInterpolation ](/) (A,P),levels=[100000,&#160;92500,&#160;85000,&#160;70000,
60000,&#160;50000,&#160;40000,&#160;30000,&#160;25000,&#160;20000,&#160;15000,&#160;10000,&#160;7000,&#160;5000,&#160;3000,
2000,&#160;1000]) `

 reconstructPressureFromHybrid  (ps, A, B, Po) 
     ` Reconstruct&#160;the&#160;Pressure&#160;field&#160;on&#160;sigma&#160;levels,&#160;from&#160;the&#160;surface&#160;pressure   
  
Input  
Ps&#160;&#160;&#160;:&#160;Surface&#160;pressure  
A,B,Po:&#160;Hybrid&#160;Convertion&#160;Coefficients,&#160;such&#160;as:&#160;p=B.ps+A.Po  
Ps:&#160;surface&#160;pressure  
B,A&#160;are&#160;1D&#160;:&#160;sigma&#160;levels  
Po&#160;and&#160;Ps&#160;must&#160;have&#160;same&#160;units  
  
Output  
Pressure&#160;field  
Such&#160;as&#160;P=B*Ps+A*Po  
  
Example  
P= [ reconstructPressureFromHybrid ](/) (ps,A,B,Po) `

 sigma2Pressure  = logLinearInterpolation(A, P, levels  =[100000, 92500, 85000, 70000, 60000, 50000, 40000, 30000, 25000, 20000, 15000, 10000, 7000, 5000, 3000, 2000, 1000]  , status  =None  ) 
     ` Log-linear&#160;interpolation   
to&#160;convert&#160;a&#160;field&#160;from&#160;sigma&#160;levels&#160;to&#160;pressure&#160;levels  
Value&#160;below&#160;surface&#160;are&#160;masked  
  
Input  
A&#160;:&#160;&#160;&#160;&#160;array&#160;on&#160;sigma&#160;levels  
P&#160;:&#160;&#160;&#160;&#160;pressure&#160;field&#160;from&#160;TOP&#160;(level&#160;0)&#160;to&#160;BOTTOM&#160;(last&#160;level)  
levels&#160;:&#160;pressure&#160;levels&#160;to&#160;interplate&#160;to&#160;(same&#160;units&#160;as&#160;P),&#160;default&#160;levels
are:[100000,&#160;92500,&#160;85000,&#160;70000,&#160;60000,&#160;50000,&#160;40000,&#160;30000,&#160;25000,&#160;20000,
15000,&#160;10000,&#160;7000,&#160;5000,&#160;3000,&#160;2000,&#160;1000]  
  
P&#160;and&#160;levels&#160;must&#160;have&#160;same&#160;units  
  
Output  
array&#160;on&#160;pressure&#160;levels&#160;(levels)  
  
Examples:  
A= [ logLinearInterpolation ](/) (A,P),levels=[100000,&#160;92500,&#160;85000,&#160;70000,
60000,&#160;50000,&#160;40000,&#160;30000,&#160;25000,&#160;20000,&#160;15000,&#160;10000,&#160;7000,&#160;5000,&#160;3000,
2000,&#160;1000]) `

* * *

UCRL-WEB-213937 | [ Privacy & Legal Notice ](/disclaimer.html)

[ webmaster@pcmdi.llnl.gov ](/webmaster@pcmdi.llnl.gov)

[ ![Powered by Plone](media/plone_powered.gif) ](/)

