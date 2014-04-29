---
layout: default
title:
---

 [ Skip to content. ](/cdat/source/api-reference/cdms.convention.html) | [ Skip
to navigation ](/cdat/source/api-reference/cdms.convention.html)

Search Site

[ Advanced Search&#8230; ](/search_form)

#  [ PCMDI Software Portal ](/)

#####  Sections

  * [ Home ](/)

#####  Personal tools

  * [ Log in ](/login_form)

You are here:  [ Home ](/) -> [ CDAT ](/cdat) -> [ Source Code ](/cdat/source)
-> [ API Reference ](/cdat/source/api-reference) -> Python: module
cdms.convention

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

        * [ Python: module cdms.convention ](/cdat/source/api-reference/cdms.convention.html)

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

  * [ ![Send this page to somebody](media/mail_icon.gif) ](/cdat/source/api-reference/cdms.convention.html/sendto_form)
  * [ ![Print this page](media/print_icon.gif) ](/this.print\(\))

#  Python: module cdms.convention

  
  
 [ cdms  ](/cdms.html) .convention 
[ index ](/)  

` metadata&#160;conventions `

  
 Modules 

` `

[ string ](/string.html)  

  
 Classes 

` `

[ UserList.UserList ](/UserList.html)

    

[ AliasList ](/cdms.convention.html)

[ AbstractConvention ](/cdms.convention.html)

    

[ NUGConvention ](/cdms.convention.html)

    

[ COARDSConvention ](/cdms.convention.html)

    

[ CFConvention ](/cdms.convention.html)

  
class  AbstractConvention 

` `

Methods defined here:  

 axisIsLatitude  (self, axis) 

 axisIsLongitude  (self, axis) 

 getAxisAuxIds  (self, vardict, axiskeys) 

 getAxisIds  (self, vardict) 

 getDsetnodeAuxAxisIds  (self, dsetnode) 

 getVarLatId  (self, var, vardict  =None  ) 

 getVarLonId  (self, var, vardict  =None  ) 

  
class  AliasList  ( [ UserList.UserList ](/UserList.html) )

` `

Methods defined here:  

 __init__  (self, alist) 

 __setitem__  (self, i, value) 

 append  (self, value) 

* * *

Methods inherited from [ UserList.UserList ](/UserList.html) :  

 __add__  (self, other) 

 __cmp__  (self, other) 

 __contains__  (self, item) 

 __delitem__  (self, i) 

 __delslice__  (self, i, j) 

 __eq__  (self, other) 

 __ge__  (self, other) 

 __getitem__  (self, i) 

 __getslice__  (self, i, j) 

 __gt__  (self, other) 

 __iadd__  (self, other) 

 __imul__  (self, n) 

 __le__  (self, other) 

 __len__  (self) 

 __lt__  (self, other) 

 __mul__  (self, n) 

 __ne__  (self, other) 

 __radd__  (self, other) 

 __repr__  (self) 

 __rmul__  = __mul__(self, n) 

 __setslice__  (self, i, j, other) 

 count  (self, item) 

 extend  (self, other) 

 index  (self, item, *args) 

 insert  (self, i, item) 

 pop  (self, i  =-1  ) 

 remove  (self, item) 

 reverse  (self) 

 sort  (self, *args, kwds) 

  
class  CFConvention  ( [ COARDSConvention ](/cdms.convention.html) )

` `

Method resolution order:

     [ CFConvention ](/cdms.convention.html)
     [ COARDSConvention ](/cdms.convention.html)
     [ NUGConvention ](/cdms.convention.html)
     [ AbstractConvention ](/cdms.convention.html)

* * *

Methods defined here:  

 __init__  (self, version) 

 axisIsLatitude  (self, axis) 

 axisIsLongitude  (self, axis) 

 getAxisAuxIds  (self, vardict, axiskeys) 
     ` Get&#160;Axis2D&#160;and&#160;AuxAxis1D&#160;IDs `

 getDsetnodeAuxAxisIds  (self, dsetnode) 
     ` Get&#160;auxiliary&#160;axis&#160;IDs&#160;from&#160;a&#160;dataset&#160;node `

 getVarLatId  (self, var, vardict) 

 getVarLonId  (self, var, vardict) 

 getVariableBounds  (self, dset, var) 
     ` Get&#160;the&#160;bounds&#160;variable&#160;for&#160;the&#160;variable,&#160;from&#160;a&#160;dataset&#160;or&#160;file. `

* * *

Data and other attributes defined here:  

 current  = 'CF-1.0' 

* * *

Methods inherited from [ NUGConvention ](/cdms.convention.html) :  

 getAxisIds  (self, vardict) 
     ` Get&#160;1-D&#160;coordinate&#160;axis&#160;IDs. `

  
class  COARDSConvention  ( [ NUGConvention ](/cdms.convention.html) )

` `

Method resolution order:

     [ COARDSConvention ](/cdms.convention.html)
     [ NUGConvention ](/cdms.convention.html)
     [ AbstractConvention ](/cdms.convention.html)

* * *

Methods defined here:  

 __init__  (self, version  =None  ) 

* * *

Methods inherited from [ NUGConvention ](/cdms.convention.html) :  

 getAxisAuxIds  (self, vardict, axiskeys) 

 getAxisIds  (self, vardict) 
     ` Get&#160;1-D&#160;coordinate&#160;axis&#160;IDs. `

* * *

Methods inherited from [ AbstractConvention ](/cdms.convention.html) :  

 axisIsLatitude  (self, axis) 

 axisIsLongitude  (self, axis) 

 getDsetnodeAuxAxisIds  (self, dsetnode) 

 getVarLatId  (self, var, vardict  =None  ) 

 getVarLonId  (self, var, vardict  =None  ) 

  
class  NUGConvention  ( [ AbstractConvention ](/cdms.convention.html) )

` `

Methods defined here:  

 __init__  (self, version  =None  ) 

 getAxisAuxIds  (self, vardict, axiskeys) 

 getAxisIds  (self, vardict) 
     ` Get&#160;1-D&#160;coordinate&#160;axis&#160;IDs. `

* * *

Methods inherited from [ AbstractConvention ](/cdms.convention.html) :  

 axisIsLatitude  (self, axis) 

 axisIsLongitude  (self, axis) 

 getDsetnodeAuxAxisIds  (self, dsetnode) 

 getVarLatId  (self, var, vardict  =None  ) 

 getVarLonId  (self, var, vardict  =None  ) 

  
 Functions 

` `

 getDatasetConvention  (dset) 
     ` Return&#160;an&#160;appropriate&#160;convention&#160;object.&#160;dset&#160;is&#160;a&#160;file&#160;or&#160;dataset&#160;object `

  
 Data 

` `

 CF1  = <cdms.convention.CFConvention instance>   
 COARDS  = <cdms.convention.COARDSConvention instance>   
 MethodNotImplemented  = 'Method not yet implemented'   
 NUG  = <cdms.convention.NUGConvention instance>   
 latitude_aliases  = []   
 level_aliases  = ['plev']   
 longitude_aliases  = []   
 time_aliases  = [] 

* * *

UCRL-WEB-213937 | [ Privacy & Legal Notice ](/disclaimer.html)

[ webmaster@pcmdi.llnl.gov ](/webmaster@pcmdi.llnl.gov)

[ ![Powered by Plone](media/plone_powered.gif) ](/)

