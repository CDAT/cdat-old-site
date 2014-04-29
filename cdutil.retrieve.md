---
layout: default
title:
---

 [ Skip to content. ](/cdat/source/api-reference/cdutil.retrieve.html) | [ Skip
to navigation ](/cdat/source/api-reference/cdutil.retrieve.html)

Search Site

[ Advanced Search&#8230; ](/search_form)

#  [ PCMDI Software Portal ](/)

#####  Sections

  * [ Home ](/)

#####  Personal tools

  * [ Log in ](/login_form)

You are here:  [ Home ](/) -> [ CDAT ](/cdat) -> [ Source Code ](/cdat/source)
-> [ API Reference ](/cdat/source/api-reference) -> Python: module
cdutil.retrieve

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

        * [ Python: module cdutil.retrieve ](/cdat/source/api-reference/cdutil.retrieve.html)

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

  * [ ![Send this page to somebody](media/mail_icon.gif) ](/cdat/source/api-reference/cdutil.retrieve.html/sendto_form)
  * [ ![Print this page](media/print_icon.gif) ](/this.print\(\))

#  Python: module cdutil.retrieve

  
  
 [ cdutil  ](/cdutil.html) .retrieve 
[ index ](/)  

  
 Modules 

` `

[ MA ](/MA.html)  
[ MV ](/MV.html)  
[ Numeric ](/Numeric.html)  

[ cdutil.ValidationFunctions ](/cdutil.ValidationFunctions.html)  
[ cdms ](/cdms.html)  
[ cdtime ](/cdtime.html)  

[ exceptions ](/exceptions.html)  
[ genutil ](/genutil.html)  
[ regrid ](/regrid.html)  

[ string ](/string.html)  
[ types ](/types.html)  

  
 Classes 

` `

[ __builtin__.object ](/__builtin__.html)

    

[ GridAxis ](/cdutil.retrieve.html)

[ VariableConditioner ](/cdutil.retrieve.html)

[ VariablesMatcher ](/cdutil.retrieve.html)

[ WeightedGridMaker ](/cdutil.retrieve.html)

[ WeightsMaker ](/cdutil.retrieve.html)

[ exceptions.Exception ](/exceptions.html)

    

[ WeightsMakerError ](/cdutil.retrieve.html)

    

[ WeightedGridMakerError ](/cdutil.retrieve.html)

    

[ VariableConditionerError ](/cdutil.retrieve.html)

    

[ VariablesMatcherError ](/cdutil.retrieve.html)

  
class  GridAxis  ( [ __builtin__.object ](/__builtin__.html) )

` `

Methods defined here:  

 __init__  (self) 

 __str__  (self) 

* * *

Properties defined here:  

 delta 
    

 _ get _  = _get_delta(self) 
    

 _ set _  = _set_delta(self, value) 

 first 
    

 _ get _  = _get_first(self) 
    

 _ set _  = _set_first(self, value) 

 n 
    

 _ get _  = _get_n(self) 
    

 _ set _  = _set_n(self, value) 

 type 
    

 _ get _  = _get_type(self) 
    

 _ set _  = _set_type(self, value) 

* * *

Data and other attributes defined here:  

 __slots__  = ['first', 'n', 'delta', 'type', '_first', '_n', '_delta', '_type'] 

  
class  VariableConditioner  ( [ __builtin__.object ](/__builtin__.html) )

` `

Methods defined here:  

 __call__  = [ get ](/) (self, returnTuple  =1  ) 

 __init__  (self, source, var  =None  , weightsMaker  =None  , weightedGridMaker  =None  , offset  =0.0  , slope  =1.0  , cdmsArguments  =None  , cdmsKeywords  =None  , id  =None  , preprocess  =None  , preprocessKeywords  ={}  , comments  =''  ) 

 __str__  (self) 

 get  (self, returnTuple  =1  ) 

* * *

Properties defined here:  

 data 
    

 _ get _  = _get_data(self) 
    

 _ set _  = _set_data(self, value) 

 file 
    

 _ get _  = _get_file(self) 
    

 _ set _  = _set_file(self, value) 

 id 
    

 _ get _  = _get_id(self) 
    

 _ set _  = _set_id(self, value) 

 offset 
    

 _ get _  = _get_offset(self) 
    

 _ set _  = _set_offset(self, value) 

 slope 
    

 _ get _  = _get_slope(self) 
    

 _ set _  = _set_slope(self, value) 

 var 
    

 _ get _  = _get_var(self) 
    

 _ set _  = _set_var(self, value) 

 weightedGridMaker 
    

 _ get _  = _get_weightedGridMaker(self) 
    

 _ set _  = _set_weightedGridMaker(self, value) 

* * *

Data and other attributes defined here:  

 __slots__  = ['source', 'var', 'data', 'file', 'weightsMaker', 'weightedGridMaker', 'slope', 'offset', 'cdmsArguments', 'cdmsKeywords', 'id', 'preprocessKeywords', 'preprocess', 'comments', '_var', '_id', '_slope', '_offset', '_file', '_data', ...] 

 cdmsArguments  = <member 'cdmsArguments' of 'VariableConditioner' objects>

 cdmsKeywords  = <member 'cdmsKeywords' of 'VariableConditioner' objects>

 comments  = <member 'comments' of 'VariableConditioner' objects>

 preprocess  = <member 'preprocess' of 'VariableConditioner' objects>

 preprocessKeywords  = <member 'preprocessKeywords' of 'VariableConditioner' objects>

 source  = <member 'source' of 'VariableConditioner' objects>

 weightsMaker  = <member 'weightsMaker' of 'VariableConditioner' objects>

  
class  VariableConditionerError  ( [ WeightedGridMakerError
](/cdutil.retrieve.html) )

` `

Method resolution order:

     [ VariableConditionerError ](/cdutil.retrieve.html)
     [ WeightedGridMakerError ](/cdutil.retrieve.html)
     [ WeightsMakerError ](/cdutil.retrieve.html)
     [ exceptions.Exception ](/exceptions.html)

* * *

Methods inherited from [ WeightsMakerError ](/cdutil.retrieve.html) :  

 __init__  (self, args) 

* * *

Methods inherited from [ exceptions.Exception ](/exceptions.html) :  

 __getitem__  (...) 

 __str__  (...) 

  
class  VariablesMatcher  ( [ __builtin__.object ](/__builtin__.html) )

` `

Methods defined here:  

 __call__  = [ get ](/) (self, returnTuple  =1  ) 

 __init__  (self, variableConditioner1  =None  , variableConditioner2  =None  , externalVariableConditioner  =None  , weightedGridMaker  =None  , cdmsArguments  =[]  , cdmsKeywords  ={}  ) 

 __str__  (self) 

 get  (self, returnTuple  =1  ) 

* * *

Data and other attributes defined here:  

 __dict__  = <dictproxy object>
     ` dictionary&#160;for&#160;instance&#160;variables&#160;(if&#160;defined) `

 __weakref__  = <attribute '__weakref__' of 'VariablesMatcher' objects>
     ` list&#160;of&#160;weak&#160;references&#160;to&#160;the [ object ](/__builtin__.html) (if&#160;defined) `

  
class  VariablesMatcherError  ( [ VariableConditionerError
](/cdutil.retrieve.html) )

` `

Method resolution order:

     [ VariablesMatcherError ](/cdutil.retrieve.html)
     [ VariableConditionerError ](/cdutil.retrieve.html)
     [ WeightedGridMakerError ](/cdutil.retrieve.html)
     [ WeightsMakerError ](/cdutil.retrieve.html)
     [ exceptions.Exception ](/exceptions.html)

* * *

Methods inherited from [ WeightsMakerError ](/cdutil.retrieve.html) :  

 __init__  (self, args) 

* * *

Methods inherited from [ exceptions.Exception ](/exceptions.html) :  

 __getitem__  (...) 

 __str__  (...) 

  
class  WeightedGridMaker  ( [ __builtin__.object ](/__builtin__.html) )

` `

Methods defined here:  

 __call__  = [ get ](/) (self) 

 __init__  (self, source  =None  , var  =None  , nlat  =None  , flat  =None  , dellat  =None  , grid_type  ='uniform'  , nlon  =None  , flon  =None  , dellon  =None  , weightsMaker  =None  ) 

 __str__  (self) 

 get  (self) 

* * *

Properties defined here:  

 file 
    

 _ get _  = _get_file(self) 
    

 _ set _  = _set_file(self, value) 

 grid 
    

 _ get _  = _get_grid(self) 
    

 _ set _  = _set_grid(self, value) 

 var 
    

 _ get _  = _get_var(self) 
    

 _ set _  = _set_var(self, value) 

* * *

Data and other attributes defined here:  

 __slots__  = ['grid', 'var', 'file', 'longitude', 'latitude', 'weightsMaker', '_var', '_file', '_grid'] 

 latitude  = <member 'latitude' of 'WeightedGridMaker' objects>

 longitude  = <member 'longitude' of 'WeightedGridMaker' objects>

 weightsMaker  = <member 'weightsMaker' of 'WeightedGridMaker' objects>

  
class  WeightedGridMakerError  ( [ WeightsMakerError
](/cdutil.retrieve.html) )

` `

Method resolution order:

     [ WeightedGridMakerError ](/cdutil.retrieve.html)
     [ WeightsMakerError ](/cdutil.retrieve.html)
     [ exceptions.Exception ](/exceptions.html)

* * *

Methods inherited from [ WeightsMakerError ](/cdutil.retrieve.html) :  

 __init__  (self, args) 

* * *

Methods inherited from [ exceptions.Exception ](/exceptions.html) :  

 __getitem__  (...) 

 __str__  (...) 

  
class  WeightsMaker  ( [ __builtin__.object ](/__builtin__.html) )

` `

Methods defined here:  

 __call__  = [ get ](/) (self, input  =None  ) 

 __init__  (self, source  =None  , var  =None  , values  =None  , actions  =[<cdms.MV.var_binary_operation instance>]  , combiningActions  =[<cdms.MV.var_binary_operation instance>]  ) 

 __str__  (self) 
     ` #&#160;Representation&#160;of&#160;Mask [ object ](/__builtin__.html) `

 get  (self, input  =None  ) 

* * *

Properties defined here:  

 var 
    

 _ get _  = _get_var(self) 
    

 _ set _  = _set_var(self, value) 

* * *

Data and other attributes defined here:  

 __slots__  = ['mask', 'var', 'values', 'actions', 'file', 'combiningActions', 'data', '_var'] 

 actions  = <member 'actions' of 'WeightsMaker' objects>

 combiningActions  = <member 'combiningActions' of 'WeightsMaker' objects>

 data  = <member 'data' of 'WeightsMaker' objects>

 file  = <member 'file' of 'WeightsMaker' objects>

 mask  = <member 'mask' of 'WeightsMaker' objects>

 values  = <member 'values' of 'WeightsMaker' objects>

  
class  WeightsMakerError  ( [ exceptions.Exception ](/exceptions.html) )

` `

Methods defined here:  

 __init__  (self, args) 

* * *

Methods inherited from [ exceptions.Exception ](/exceptions.html) :  

 __getitem__  (...) 

 __str__  (...) 

* * *

UCRL-WEB-213937 | [ Privacy & Legal Notice ](/disclaimer.html)

[ webmaster@pcmdi.llnl.gov ](/webmaster@pcmdi.llnl.gov)

[ ![Powered by Plone](media/plone_powered.gif) ](/)

