---
layout: default
title:
---

 [ Skip to content. ](/cdat/source/api-reference/ncml.ncml.html) | [ Skip to
navigation ](/cdat/source/api-reference/ncml.ncml.html)

Search Site

[ Advanced Search&#8230; ](/search_form)

#  [ PCMDI Software Portal ](/)

#####  Sections

  * [ Home ](/)

#####  Personal tools

  * [ Log in ](/login_form)

You are here:  [ Home ](/) -> [ CDAT ](/cdat) -> [ Source Code ](/cdat/source)
-> [ API Reference ](/cdat/source/api-reference) -> Python: module ncml.ncml

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

        * [ Python: module ncml.ncml ](/cdat/source/api-reference/ncml.ncml.html)

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

  * [ ![Send this page to somebody](media/mail_icon.gif) ](/cdat/source/api-reference/ncml.ncml.html/sendto_form)
  * [ ![Print this page](media/print_icon.gif) ](/this.print\(\))

#  Python: module ncml.ncml

  
  
 [ ncml  ](/ncml.html) .ncml 
[ index ](/)  

` NcML&#160;support.&#160;See [ http://www.vets.ucar.edu/luca/netcdf/ ](/luca/netcdf/) `

  
 Modules 

` `

[ Numeric ](/Numeric.html)  
[ cdms.cdmsNode ](/cdms.cdmsNode.html)  

[ os ](/os.html)  
[ re ](/re.html)  

[ string ](/string.html)  

  
 Classes 

` `

[ exceptions.Exception ](/exceptions.html)

    

[ NCMLError ](/ncml.ncml.html)

[ NCMLNode ](/ncml.ncml.html)

    

[ AttributeNode ](/ncml.ncml.html)

[ DimensionNode ](/ncml.ncml.html)

[ NetcdfNode ](/ncml.ncml.html)

[ ValueNode ](/ncml.ncml.html)

[ VariableNode ](/ncml.ncml.html)

  
class  AttributeNode  ( [ NCMLNode ](/ncml.ncml.html) )

` `

Methods defined here:  

 __init__  (self, name, datatype, value  =None  ) 

 write  (self, fd) 

* * *

Methods inherited from [ NCMLNode ](/ncml.ncml.html) :  

 endwrite  (self, fd, content  =0  ) 

 startwrite  (self, fd) 

  
class  DimensionNode  ( [ NCMLNode ](/ncml.ncml.html) )

` `

Methods defined here:  

 __init__  (self, name, length, isUnlimited  ='false'  ) 

 toCDML  (self, forcedata  =0  ) 
     ` Translate&#160;to&#160;a&#160;CDML&#160;tree.&#160;Returns&#160;a&#160;cdms.cdmsNode.AxisNode. `

 write  (self, fd) 

* * *

Methods inherited from [ NCMLNode ](/ncml.ncml.html) :  

 endwrite  (self, fd, content  =0  ) 

 startwrite  (self, fd) 

  
class  NCMLError  ( [ exceptions.Exception ](/exceptions.html) )

` `

Methods defined here:  

 __init__  (self, args  ='Unspecified error from package ncml'  ) 

 __str__  (self) 

* * *

Methods inherited from [ exceptions.Exception ](/exceptions.html) :  

 __getitem__  (...) 

  
class  NCMLNode 

` `

` Abstract&#160;NCML&#160;node.  
`

Methods defined here:  

 __init__  (self) 

 endwrite  (self, fd, content  =0  ) 

 startwrite  (self, fd) 

 write  (self, fd) 
     ` Output&#160;to&#160;a&#160;file.&#160;fd&#160;is&#160;an&#160;open&#160;file&#160;descriptor. `

  
class  NetcdfNode  ( [ NCMLNode ](/ncml.ncml.html) )

` `

Methods defined here:  

 __init__  (self, id  =None  , uri  =None  ) 

 setAttribute  (self, a) 
     ` Add&#160;an&#160;attribute&#160;node&#160;a. `

 setDimension  (self, d) 
     ` Add&#160;a&#160;dimension&#160;node&#160;d. `

 setVariable  (self, v) 
     ` Add&#160;a&#160;variable&#160;node&#160;v. `

 toCDML  (self, coorddict  =None  , forcedata  =0  ) 
     ` Translate&#160;to&#160;a&#160;CDML&#160;tree.&#160;Returns&#160;a&#160;cdms.cdmsNode.DatasetNode.   
If&#160;coorddict&#160;is&#160;specified,&#160;don't&#160;translate&#160;dimensions&#160;with&#160;names&#160;in&#160;coorddict.
`

 write  (self, fd) 

* * *

Methods inherited from [ NCMLNode ](/ncml.ncml.html) :  

 endwrite  (self, fd, content  =0  ) 

 startwrite  (self, fd) 

  
class  ValueNode  ( [ NCMLNode ](/ncml.ncml.html) )

` `

Methods defined here:  

 __init__  (self, values  =None  , separator  =' '  ) 

 setValues  (self, values) 
     ` Set&#160;values,&#160;a&#160;Numeric&#160;array. `

 write  (self, fd) 

* * *

Methods inherited from [ NCMLNode ](/ncml.ncml.html) :  

 endwrite  (self, fd, content  =0  ) 

 startwrite  (self, fd) 

  
class  VariableNode  ( [ NCMLNode ](/ncml.ncml.html) )

` `

Methods defined here:  

 __init__  (self, name, datatype, shape  =None  ) 

 setAttribute  (self, att) 
     ` Add&#160;an&#160;attribute.&#160;att&#160;is&#160;an [ AttributeNode ](/) `

 setValues  (self, values) 
     ` Set&#160;values,&#160;a [ ValueNode ](/) . `

 toCDML  (self, ncnode, forcedata  =0  ) 
     ` Translate&#160;to&#160;a&#160;CDML&#160;tree.&#160;Returns&#160;a&#160;cdms.cdmsNode. [ VariableNode ](/) or&#160;cdms.cdmsNode.AxisNode. `

 write  (self, fd) 

* * *

Methods inherited from [ NCMLNode ](/ncml.ncml.html) :  

 endwrite  (self, fd, content  =0  ) 

 startwrite  (self, fd) 

  
 Functions 

` `

 scan  (path) 
     ` Scan&#160;a&#160;Cdunif&#160;file,&#160;return&#160;a&#160;tree&#160;of&#160;NCML&#160;objects,&#160;in&#160;the   
form&#160;of&#160;a [ NetcdfNode ](/) . `

  
 Data 

` `

 CdByte  = 'Byte'   
 CdDouble  = 'Double'   
 CdFloat  = 'Float'   
 CdInt  = 'Int'   
 CdLong  = 'Long'   
 CdShort  = 'Short'   
 CdString  = 'String'   
 NCToCdType  = {'boolean': 'Byte', 'byte': 'Byte', 'double': 'Double', 'float': 'Float', 'int': 'Int', 'long': 'Long', 'short': 'Short', 'string': 'String'}   
 NCToNumericType  = {'boolean': '1', 'byte': '1', 'double': 'd', 'float': 'f', 'int': 'i', 'long': 'l', 'short': 's', 'string': 'c'}   
 NumericToNCType  = {'1': 'byte', 'c': 'string', 'd': 'double', 'f': 'float', 'i': 'int', 'l': 'long', 's': 'short'}   
 namespace  = 'http://www.ucar.edu/schemas/netcdf'   
 nsprefix  = 'nc'   
 schemaLocation  = 'http://www.ucar.edu/schemas/netcdf.xsd' 

* * *

UCRL-WEB-213937 | [ Privacy & Legal Notice ](/disclaimer.html)

[ webmaster@pcmdi.llnl.gov ](/webmaster@pcmdi.llnl.gov)

[ ![Powered by Plone](media/plone_powered.gif) ](/)

