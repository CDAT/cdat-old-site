---
layout: default
title:
---

 [ Skip to content. ](/cdat/source/api-reference/ncml.cs.html) | [ Skip to
navigation ](/cdat/source/api-reference/ncml.cs.html)

Search Site

[ Advanced Search&#8230; ](/search_form)

#  [ PCMDI Software Portal ](/)

#####  Sections

  * [ Home ](/)

#####  Personal tools

  * [ Log in ](/login_form)

You are here:  [ Home ](/) -> [ CDAT ](/cdat) -> [ Source Code ](/cdat/source)
-> [ API Reference ](/cdat/source/api-reference) -> Python: module ncml.cs

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

        * [ Python: module ncml.cs ](/cdat/source/api-reference/ncml.cs.html)

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

  * [ ![Send this page to somebody](media/mail_icon.gif) ](/cdat/source/api-reference/ncml.cs.html/sendto_form)
  * [ ![Print this page](media/print_icon.gif) ](/this.print\(\))

#  Python: module ncml.cs

  
  
 [ ncml  ](/ncml.html) .cs 
[ index ](/)  

` NcML&#160;+&#160;coordinate&#160;extensions&#160;support.&#160;See [
http://www.unidata.ucar.edu/schemas/netcdf-cs.xsd ](/schemas/netcdf-cs.xsd) `

  
 Modules 

` `

[ ncml.ncml ](/ncml.ncml.html)  

[ string ](/string.html)  

  
 Classes 

` `

[ ncml.ncml.NCMLNode ](/ncml.ncml.html)

    

[ CoordinateSystemNode ](/ncml.cs.html)

[ CoordinateTransformNode ](/ncml.cs.html)

[ ncml.ncml.NetcdfNode ](/ncml.ncml.html) ( [ ncml.ncml.NCMLNode
](/ncml.ncml.html) )

    

[ NetcdfNode ](/ncml.cs.html)

[ ncml.ncml.VariableNode ](/ncml.ncml.html) ( [ ncml.ncml.NCMLNode
](/ncml.ncml.html) )

    

[ CoordinateAxisBoundaryNode ](/ncml.cs.html)

[ CoordinateAxisNode ](/ncml.cs.html)

[ VariableNode ](/ncml.cs.html)

  
class  CoordinateAxisBoundaryNode  ( [ ncml.ncml.VariableNode
](/ncml.ncml.html) )

` `

Method resolution order:

     [ CoordinateAxisBoundaryNode ](/ncml.cs.html)
     [ ncml.ncml.VariableNode ](/ncml.ncml.html)
     [ ncml.ncml.NCMLNode ](/ncml.ncml.html)

* * *

Methods defined here:  

 __init__  (self, name, datatype, shape  =None  ) 

* * *

Methods inherited from [ ncml.ncml.VariableNode ](/ncml.ncml.html) :  

 setAttribute  (self, att) 
     ` Add&#160;an&#160;attribute.&#160;att&#160;is&#160;an&#160;AttributeNode `

 setValues  (self, values) 
     ` Set&#160;values,&#160;a&#160;ValueNode. `

 toCDML  (self, ncnode, forcedata  =0  ) 
     ` Translate&#160;to&#160;a&#160;CDML&#160;tree.&#160;Returns&#160;a&#160;cdms.cdmsNode. [ VariableNode ](/) or&#160;cdms.cdmsNode.AxisNode. `

 write  (self, fd) 

* * *

Methods inherited from [ ncml.ncml.NCMLNode ](/ncml.ncml.html) :  

 endwrite  (self, fd, content  =0  ) 

 startwrite  (self, fd) 

  
class  CoordinateAxisNode  ( [ ncml.ncml.VariableNode ](/ncml.ncml.html) )

` `

Method resolution order:

     [ CoordinateAxisNode ](/ncml.cs.html)
     [ ncml.ncml.VariableNode ](/ncml.ncml.html)
     [ ncml.ncml.NCMLNode ](/ncml.ncml.html)

* * *

Methods defined here:  

 __init__  (self, name, datatype, units, shape  =None  , axisType  =None  , positive  =None  , boundaryRef  =None  ) 

 toCDML  (self, ncnode, forcedata  =0  ) 
     ` Translate&#160;to&#160;a&#160;CDML&#160;tree.&#160;Returns&#160;a&#160;cdms.cdmsNode.AxisNode.   
If&#160;forcedata=1,&#160;values&#160;are&#160;set&#160;to&#160;[0.,&#160;1.,&#160;...]&#160;even&#160;if&#160;not&#160;explicitly
defined. `

 write  (self, fd) 

* * *

Methods inherited from [ ncml.ncml.VariableNode ](/ncml.ncml.html) :  

 setAttribute  (self, att) 
     ` Add&#160;an&#160;attribute.&#160;att&#160;is&#160;an&#160;AttributeNode `

 setValues  (self, values) 
     ` Set&#160;values,&#160;a&#160;ValueNode. `

* * *

Methods inherited from [ ncml.ncml.NCMLNode ](/ncml.ncml.html) :  

 endwrite  (self, fd, content  =0  ) 

 startwrite  (self, fd) 

  
class  CoordinateSystemNode  ( [ ncml.ncml.NCMLNode ](/ncml.ncml.html) )

` `

Methods defined here:  

 __init__  (self, name) 

 addCoordinateAxis  (self, a) 

 addCoordinateTransform  (self, t) 

 write  (self, fd) 

* * *

Methods inherited from [ ncml.ncml.NCMLNode ](/ncml.ncml.html) :  

 endwrite  (self, fd, content  =0  ) 

 startwrite  (self, fd) 

  
class  CoordinateTransformNode  ( [ ncml.ncml.NCMLNode ](/ncml.ncml.html)
)

` `

Methods defined here:  

 __init__  (self, name, authority, transformType  =None  ) 

 setAttribute  (self, p) 

 write  (self, fd) 

* * *

Methods inherited from [ ncml.ncml.NCMLNode ](/ncml.ncml.html) :  

 endwrite  (self, fd, content  =0  ) 

 startwrite  (self, fd) 

  
class  NetcdfNode  ( [ ncml.ncml.NetcdfNode ](/ncml.ncml.html) )

` `

Method resolution order:

     [ NetcdfNode ](/ncml.cs.html)
     [ ncml.ncml.NetcdfNode ](/ncml.ncml.html)
     [ ncml.ncml.NCMLNode ](/ncml.ncml.html)

* * *

Methods defined here:  

 __init__  (self, id  =None  , uri  =None  ) 

 setCoordinateAxis  (self, c) 
     ` Add&#160;a&#160;coordinate&#160;axis&#160;node. `

 setCoordinateSystem  (self, c) 
     ` Add&#160;a&#160;coordinate&#160;system&#160;node. `

 setCoordinateTransform  (self, c) 
     ` Add&#160;a&#160;coordinate&#160;transform. `

 toCDML  (self, forcedata  =0  ) 
     ` Translate&#160;to&#160;a&#160;CDML&#160;tree.&#160;Returns&#160;a&#160;cdms.cdmsNode.DatasetNode. `

 write  (self, fd) 

* * *

Methods inherited from [ ncml.ncml.NetcdfNode ](/ncml.ncml.html) :  

 setAttribute  (self, a) 
     ` Add&#160;an&#160;attribute&#160;node&#160;a. `

 setDimension  (self, d) 
     ` Add&#160;a&#160;dimension&#160;node&#160;d. `

 setVariable  (self, v) 
     ` Add&#160;a&#160;variable&#160;node&#160;v. `

* * *

Methods inherited from [ ncml.ncml.NCMLNode ](/ncml.ncml.html) :  

 endwrite  (self, fd, content  =0  ) 

 startwrite  (self, fd) 

  
class  VariableNode  ( [ ncml.ncml.VariableNode ](/ncml.ncml.html) )

` `

Method resolution order:

     [ VariableNode ](/ncml.cs.html)
     [ ncml.ncml.VariableNode ](/ncml.ncml.html)
     [ ncml.ncml.NCMLNode ](/ncml.ncml.html)

* * *

Methods defined here:  

 __init__  (self, name, datatype, shape  =None  , coordinateSystems  =None  ) 

 toCDML  (self, ncnode) 
     ` Translate&#160;to&#160;a&#160;CDML&#160;tree.&#160;Returns&#160;a&#160;cdms.cdmsNode. [ VariableNode ](/) or&#160;cdms.cdmsNode.AxisNode. `

 write  (self, fd) 

* * *

Methods inherited from [ ncml.ncml.VariableNode ](/ncml.ncml.html) :  

 setAttribute  (self, att) 
     ` Add&#160;an&#160;attribute.&#160;att&#160;is&#160;an&#160;AttributeNode `

 setValues  (self, values) 
     ` Set&#160;values,&#160;a&#160;ValueNode. `

* * *

Methods inherited from [ ncml.ncml.NCMLNode ](/ncml.ncml.html) :  

 endwrite  (self, fd, content  =0  ) 

 startwrite  (self, fd) 

  
 Functions 

` `

 scan  (path) 
     ` Scan&#160;a&#160;Cdunif&#160;file,&#160;return&#160;a&#160;tree&#160;of&#160;NCML&#160;objects,&#160;in&#160;the   
form&#160;of&#160;a [ NetcdfNode ](/) . `

  
 Data 

` `

 CdString  = 'String'   
 cdToCsAxisType  = {'t': 'Time', 'x': 'Lon', 'y': 'Lat', 'z': 'Height'}   
 schemaLocation  = 'http://www.ucar.edu/schemas/netcdf-cs.xsd' 

* * *

UCRL-WEB-213937 | [ Privacy & Legal Notice ](/disclaimer.html)

[ webmaster@pcmdi.llnl.gov ](/webmaster@pcmdi.llnl.gov)

[ ![Powered by Plone](media/plone_powered.gif) ](/)

