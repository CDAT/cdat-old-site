---
layout: default
title:
---

 [ Skip to content. ](/cdat/source/api-reference/cdms.database.html) | [ Skip
to navigation ](/cdat/source/api-reference/cdms.database.html)

Search Site

[ Advanced Search&#8230; ](/search_form)

#  [ PCMDI Software Portal ](/)

#####  Sections

  * [ Home ](/)

#####  Personal tools

  * [ Log in ](/login_form)

You are here:  [ Home ](/) -> [ CDAT ](/cdat) -> [ Source Code ](/cdat/source)
-> [ API Reference ](/cdat/source/api-reference) -> Python: module
cdms.database

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

        * [ Python: module cdms.database ](/cdat/source/api-reference/cdms.database.html)

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

  * [ ![Send this page to somebody](media/mail_icon.gif) ](/cdat/source/api-reference/cdms.database.html/sendto_form)
  * [ ![Print this page](media/print_icon.gif) ](/this.print\(\))

#  Python: module cdms.database

  
  
 [ cdms  ](/cdms.html) .database 
[ index ](/)  

` CDMS&#160;database&#160;objects `

  
 Modules 

` `

[ cdms.cdmsobj ](/cdms.cdmsobj.html)  
[ cdms.cdurlparse ](/cdms.cdurlparse.html)  
[ copy ](/copy.html)  

[ cdms.internattr ](/cdms.internattr.html)  
[ os ](/os.html)  
[ re ](/re.html)  

[ string ](/string.html)  
[ sys ](/sys.html)  
[ types ](/types.html)  

  
 Classes 

` `

[ cdms.cdmsobj.CdmsObj ](/cdms.cdmsobj.html) ( [
cdms.internattr.InternalAttributesClass ](/cdms.internattr.html) )

    

[ AbstractDatabase ](/cdms.database.html)

    

[ LDAPDatabase ](/cdms.database.html)

[ AbstractResultEntry ](/cdms.database.html)

    

[ LDAPResultEntry ](/cdms.database.html)

[ AbstractSearchResult ](/cdms.database.html)

    

[ LDAPSearchResult ](/cdms.database.html)

  
class  AbstractDatabase  ( [ cdms.cdmsobj.CdmsObj ](/cdms.cdmsobj.html) )

` `

` [ AbstractDatabase ](/) defines&#160;the&#160;common&#160;database&#160;interface.&#160;Concrete
database&#160;classes&#160;are  
derived&#160;from&#160;this&#160;class.  
`

Method resolution order:

     [ AbstractDatabase ](/cdms.database.html)
     [ cdms.cdmsobj.CdmsObj ](/cdms.cdmsobj.html)
     [ cdms.internattr.InternalAttributesClass ](/cdms.internattr.html)
     [ PropertiedClasses.Properties.PropertiedClass ](/PropertiedClasses.Properties.html)

* * *

Methods defined here:  

 __init__  (self, uri, path) 

 __repr__  (self) 

 cachecdml  (self, name, cdml) 

 close  (self) 

 disableCache  (self) 

 enableCache  (self) 

 getDataset  (self, name) 

 getObjFromDataset  (self, name) 

 openDataset  (self, dsetid, mode  ='r'  ) 

 searchFilter  (self, filter, classtag  =None  , relbase  =None  , scope  =2  , attnames  =[]  ) 

 useRequestManager  (self, lcBaseDN, useReplica  =1  , userid  ='anonymous'  ) 

 usingRequestManager  (self) 

* * *

Methods inherited from [ cdms.cdmsobj.CdmsObj ](/cdms.cdmsobj.html) :  

 dump  (self, path  =None  , format  =1  ) 
     ` [ dump ](/) (self,path=None,format=1)   
Dump&#160;an&#160;XML&#160;representation&#160;of&#160;this&#160;object&#160;to&#160;a&#160;file.  
'path'&#160;is&#160;the&#160;result&#160;file&#160;name,&#160;None&#160;for&#160;standard&#160;output.  
'format'==1&#160;iff&#160;the&#160;file&#160;is&#160;formatted&#160;with&#160;newlines&#160;for&#160;readability `

 matchPattern  (self, pattern, attribute, tag) 
     ` #&#160;Match&#160;a&#160;pattern&#160;in&#160;a&#160;string-valued&#160;attribute.&#160;If&#160;attribute&#160;is&#160;None,   
#&#160;search&#160;all&#160;string&#160;attributes.&#160;If&#160;tag&#160;is&#160;not&#160;None,&#160;it&#160;must&#160;match&#160;the&#160;internal
node&#160;tag. `

 matchone  (self, pattern, attname) 
     ` #&#160;Return&#160;true&#160;iff&#160;the&#160;attribute&#160;with&#160;name&#160;attname&#160;is&#160;a&#160;string   
#&#160;attribute&#160;which&#160;matches&#160;the&#160;compiled&#160;regular&#160;expression&#160;pattern,&#160;or  
#&#160;if&#160;attname&#160;is&#160;None&#160;and&#160;pattern&#160;matches&#160;at&#160;least&#160;one&#160;string  
#&#160;attribute.&#160;Return&#160;false&#160;if&#160;the&#160;attribute&#160;is&#160;not&#160;found&#160;or&#160;is&#160;not&#160;a&#160;string `

 searchPattern  (self, pattern, attribute, tag) 
     ` #&#160;Search&#160;for&#160;a&#160;pattern&#160;in&#160;a&#160;string-valued&#160;attribute.&#160;If&#160;attribute&#160;is&#160;None,   
#&#160;search&#160;all&#160;string&#160;attributes.&#160;If&#160;tag&#160;is&#160;not&#160;None,&#160;it&#160;must&#160;match&#160;the&#160;internal
node&#160;tag. `

 searchPredicate  (self, predicate, tag) 
     ` #&#160;Apply&#160;a&#160;truth-valued&#160;predicate.&#160;Return&#160;a&#160;list&#160;containing&#160;a&#160;single&#160;instance:&#160;[self]   
#&#160;if&#160;the&#160;predicate&#160;is&#160;true&#160;and&#160;either&#160;tag&#160;is&#160;None&#160;or&#160;matches&#160;the&#160;object&#160;node
tag.  
#&#160;If&#160;the&#160;predicate&#160;returns&#160;false,&#160;return&#160;an&#160;empty&#160;list `

 searchone  (self, pattern, attname) 
     ` Return&#160;true&#160;iff&#160;the&#160;attribute&#160;with&#160;name&#160;attname&#160;is&#160;a&#160;string   
attribute&#160;which&#160;contains&#160;the&#160;compiled&#160;regular&#160;expression&#160;pattern,&#160;or  
if&#160;attname&#160;is&#160;None&#160;and&#160;pattern&#160;matches&#160;at&#160;least&#160;one&#160;string  
attribute.&#160;Return&#160;false&#160;if&#160;the&#160;attribute&#160;is&#160;not&#160;found&#160;or&#160;is&#160;not  
a&#160;string. `

* * *

Methods inherited from [ cdms.internattr.InternalAttributesClass
](/cdms.internattr.html) :  

 is_internal_attribute  (self, name) 
     ` [ is_internal_attribute ](/) (name)&#160;is&#160;true&#160;if&#160;name&#160;is&#160;internal. `

 replace_external_attributes  (self, newAttributes) 
     ` [ replace_external_attributes ](/) (newAttributes)   
Replace&#160;the&#160;external&#160;attributes&#160;with&#160;dictionary&#160;newAttributes. `

* * *

Methods inherited from [ PropertiedClasses.Properties.PropertiedClass
](/PropertiedClasses.Properties.html) :  

 __delattr__  (self, name) 

 __getattr__  (self, name) 

 __setattr__  (self, name, value) 

 get_property_d  (self, name) 
     ` Return&#160;the&#160;'del'&#160;property&#160;handler&#160;for&#160;name&#160;that&#160;self&#160;uses.   
Returns&#160;None&#160;if&#160;no&#160;handler. `

 get_property_g  (self, name) 
     ` Return&#160;the&#160;'get'&#160;property&#160;handler&#160;for&#160;name&#160;that&#160;self&#160;uses.   
Returns&#160;None&#160;if&#160;no&#160;handler. `

 get_property_s  (self, name) 
     ` Return&#160;the&#160;'set'&#160;property&#160;handler&#160;for&#160;name&#160;that&#160;self&#160;uses.   
Returns&#160;None&#160;if&#160;no&#160;handler. `

 set_property  (self, name, actg  =None  , acts  =None  , actd  =None  , nowrite  =None  , nodelete  =None  ) 
     ` Set&#160;attribute&#160;handlers&#160;for&#160;&#160;name&#160;to&#160;methods&#160;actg,&#160;acts,&#160;actd   
None&#160;means&#160;no&#160;change&#160;for&#160;that&#160;action.  
nowrite&#160;=&#160;1&#160;prevents&#160;setting&#160;this&#160;attribute.  
nowrite&#160;defaults&#160;to&#160;0\.  
nodelete&#160;=&#160;1&#160;prevents&#160;deleting&#160;this&#160;attribute.  
nodelete&#160;defaults&#160;to&#160;1&#160;unless&#160;actd&#160;given.  
if&#160;nowrite&#160;and&#160;nodelete&#160;is&#160;None:&#160;nodelete&#160;=&#160;1 `

  
class  AbstractResultEntry 

` `

Methods defined here:  

 __init__  (self, db) 

 getObject  (self) 
     ` Method:   
  
[ getObject ](/) ()  
  
Description:  
  
Get&#160;the&#160;CDMS&#160;object&#160;associated&#160;with&#160;this&#160;entry.  
  
Returns:  
  
Instance&#160;of&#160;a&#160;CDMS&#160;object. `

  
class  AbstractSearchResult 

` `

Methods defined here:  

 __getitem__  (self, key) 

 __len__  (self) 

 searchPredicate  (self, predicate, tag  =None  ) 

  
class  LDAPDatabase  ( [ AbstractDatabase ](/cdms.database.html) )

` `

` #&#160;Database&#160;implemented&#160;via&#160;LDAP&#160;(Lightweight&#160;Directory&#160;Access&#160;Protocol)  
`

Method resolution order:

     [ LDAPDatabase ](/cdms.database.html)
     [ AbstractDatabase ](/cdms.database.html)
     [ cdms.cdmsobj.CdmsObj ](/cdms.cdmsobj.html)
     [ cdms.internattr.InternalAttributesClass ](/cdms.internattr.html)
     [ PropertiedClasses.Properties.PropertiedClass ](/PropertiedClasses.Properties.html)

* * *

Methods defined here:  

 __del__  (self) 

 __init__  (self, uri, db) 

 cachecdml  (self, name, cdml, datapath) 

 close  (self) 
     ` Method:   
  
[ close ](/) ()  
  
Description:  
  
Close&#160;a&#160;database&#160;connection.  
  
Returns:  
  
None `

 getDataset  (self, dn) 

 getObjFromDataset  (self, dn) 

 listDatasets  (self) 
     ` Return&#160;a&#160;list&#160;of&#160;the&#160;dataset&#160;IDs&#160;in&#160;this&#160;database. `

 normalizedn  (self, dn) 

 open  = [ openDataset ](/) (self, dsetid, mode  ='r'  ) 

 openDataset  (self, dsetid, mode  ='r'  ) 
     ` Method:   
  
[ openDataset ](/) (dsetid,&#160;mode='r')  
  
Description:  
  
Open&#160;a&#160;dataset.  
  
Arguments:  
  
dsetid:&#160;string&#160;dataset&#160;identifier  
mode:&#160;open&#160;mode&#160;('r'&#160;-&#160;read-only,&#160;'r+'&#160;-&#160;read-write,&#160;'w'&#160;-&#160;create)  
  
Returns:  
  
Dataset&#160;instance.  
  
Example:  
  
dset&#160;=&#160;db. [ openDataset ](/) ('ncep_reanalysis_mo') `

 searchFilter  (self, filter  =None  , tag  =None  , relbase  =None  , scope  =2  , attnames  =None  , timeout  =None  ) 
     ` Method:   
  
[ searchFilter ](/) (filter=None,&#160;tag=None,&#160;relbase=None,&#160;scope=Subtree,
attnames=None,&#160;timeout=None)  
  
Description:  
  
Search&#160;a&#160;CDMS&#160;database.  
  
Arguments:  
  
filter:&#160;string&#160;search&#160;filter  
Simple&#160;filters&#160;have&#160;the&#160;form&#160;"tag&#160;=&#160;value".&#160;Simple&#160;filters&#160;can&#160;be&#160;combined
using  
logical&#160;operators&#160;'&',&#160;'|',&#160;'!'&#160;in&#160;prefix&#160;notation.&#160;For&#160;example,  
the&#160;filter&#160;'(&(objectclass=variable)(id=cli))'&#160;finds&#160;all&#160;variables&#160;named&#160;cli.  
  
More&#160;formally:  
  
filter&#160;&#160;&#160;&#160;&#160;::=&#160;"("&#160;filtercomp&#160;")"  
filtercomp&#160;::=&#160;"&"&#160;filterlist&#160;|&#160;#&#160;and  
"|"&#160;filterlist&#160;|&#160;#&#160;or  
"!"&#160;filterlist&#160;|&#160;#&#160;not  
simple  
filterlist&#160;::=&#160;filter&#160;|&#160;filter&#160;filterlist  
simple&#160;&#160;&#160;&#160;&#160;::=&#160;tag&#160;op&#160;value  
op&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;::=&#160;"="&#160;|&#160;&#160;&#160;&#160;&#160;&#160;#&#160;equality  
"~="&#160;|&#160;&#160;&#160;&#160;&#160;#&#160;approximate&#160;equality  
"<="&#160;|&#160;&#160;&#160;&#160;&#160;#&#160;lexicographically&#160;less&#160;than&#160;or&#160;equal&#160;to  
">="&#160;&#160;&#160;&#160;&#160;&#160;&#160;#&#160;lexicographically&#160;greater&#160;than&#160;or&#160;equal&#160;to  
value&#160;&#160;&#160;&#160;&#160;&#160;::=&#160;string,&#160;may&#160;include&#160;'*'&#160;as&#160;a&#160;wild&#160;card  
  
tag:&#160;string&#160;class&#160;tag&#160;("dataset"&#160;|&#160;"variable"&#160;|&#160;"database"&#160;|&#160;"axis"&#160;|&#160;"grid").  
Restricts&#160;the&#160;search&#160;to&#160;a&#160;class&#160;of&#160;objects  
relbase:&#160;string&#160;search&#160;base,&#160;relative&#160;to&#160;the&#160;database&#160;path  
scope:&#160;search&#160;scope&#160;(Subtree&#160;|&#160;Onelevel&#160;|&#160;Base).&#160;Subtree&#160;searches&#160;the&#160;base
object&#160;and&#160;its&#160;descendants.  
Onelevel&#160;searches&#160;the&#160;base&#160;object&#160;and&#160;its&#160;immediate&#160;descendants.&#160;Base&#160;searches
the&#160;base&#160;object&#160;alone.  
Default&#160;is&#160;Subtree.  
attnames:&#160;list&#160;of&#160;attribute&#160;names.&#160;Restricts&#160;the&#160;attributes&#160;returned.  
timeout:&#160;integer&#160;number&#160;of&#160;seconds&#160;before&#160;timeout.  
  
Returns:  
  
SearchResult&#160;instance.&#160;Entries&#160;can&#160;be&#160;accessed&#160;sequentially.&#160;For&#160;each&#160;entry,
entry.name&#160;is&#160;the  
name&#160;of&#160;the&#160;entry,&#160;entry.attributes&#160;is&#160;a&#160;dictionary&#160;of&#160;the&#160;attributes&#160;returned
by&#160;the&#160;search,  
entry.getObject()&#160;returns&#160;the&#160;CDMS&#160;object&#160;associated&#160;with&#160;the&#160;entry:  
  
for&#160;entry&#160;in&#160;result:  
print&#160;entry.name,&#160;entry.attributes["id"]  
  
Entries&#160;can&#160;be&#160;refined&#160;with [ searchPredicate ](/) ().  
  
Example:  
  
(1)&#160;Find&#160;all&#160;variables&#160;named&#160;"cli":  
  
result&#160;=&#160;db. [ searchFilter ](/) (filter="id=cli",tag="variable")  
  
(2)&#160;Find&#160;all&#160;objects&#160;in&#160;dataset&#160;"ncep_reanalysis_mo":  
  
result&#160;=&#160;db. [ searchFilter ](/) (relbase="dataset=ncep_reanalysis_mo"),
scope=cdms.Onelevel) `

 setExternalDict  (self, ldapattrs) 
     ` #&#160;Set&#160;the&#160;database&#160;attributes&#160;from&#160;an&#160;LDAP&#160;search&#160;result.   
#&#160;ldapattrs&#160;is&#160;a&#160;dictionary,&#160;keyed&#160;on&#160;attribute&#160;name.  
#&#160;Values&#160;are&#160;lists&#160;of&#160;attribute&#160;values. `

* * *

Methods inherited from [ AbstractDatabase ](/cdms.database.html) :  

 __repr__  (self) 

 disableCache  (self) 

 enableCache  (self) 

 useRequestManager  (self, lcBaseDN, useReplica  =1  , userid  ='anonymous'  ) 

 usingRequestManager  (self) 

* * *

Methods inherited from [ cdms.cdmsobj.CdmsObj ](/cdms.cdmsobj.html) :  

 dump  (self, path  =None  , format  =1  ) 
     ` [ dump ](/) (self,path=None,format=1)   
Dump&#160;an&#160;XML&#160;representation&#160;of&#160;this&#160;object&#160;to&#160;a&#160;file.  
'path'&#160;is&#160;the&#160;result&#160;file&#160;name,&#160;None&#160;for&#160;standard&#160;output.  
'format'==1&#160;iff&#160;the&#160;file&#160;is&#160;formatted&#160;with&#160;newlines&#160;for&#160;readability `

 matchPattern  (self, pattern, attribute, tag) 
     ` #&#160;Match&#160;a&#160;pattern&#160;in&#160;a&#160;string-valued&#160;attribute.&#160;If&#160;attribute&#160;is&#160;None,   
#&#160;search&#160;all&#160;string&#160;attributes.&#160;If&#160;tag&#160;is&#160;not&#160;None,&#160;it&#160;must&#160;match&#160;the&#160;internal
node&#160;tag. `

 matchone  (self, pattern, attname) 
     ` #&#160;Return&#160;true&#160;iff&#160;the&#160;attribute&#160;with&#160;name&#160;attname&#160;is&#160;a&#160;string   
#&#160;attribute&#160;which&#160;matches&#160;the&#160;compiled&#160;regular&#160;expression&#160;pattern,&#160;or  
#&#160;if&#160;attname&#160;is&#160;None&#160;and&#160;pattern&#160;matches&#160;at&#160;least&#160;one&#160;string  
#&#160;attribute.&#160;Return&#160;false&#160;if&#160;the&#160;attribute&#160;is&#160;not&#160;found&#160;or&#160;is&#160;not&#160;a&#160;string `

 searchPattern  (self, pattern, attribute, tag) 
     ` #&#160;Search&#160;for&#160;a&#160;pattern&#160;in&#160;a&#160;string-valued&#160;attribute.&#160;If&#160;attribute&#160;is&#160;None,   
#&#160;search&#160;all&#160;string&#160;attributes.&#160;If&#160;tag&#160;is&#160;not&#160;None,&#160;it&#160;must&#160;match&#160;the&#160;internal
node&#160;tag. `

 searchPredicate  (self, predicate, tag) 
     ` #&#160;Apply&#160;a&#160;truth-valued&#160;predicate.&#160;Return&#160;a&#160;list&#160;containing&#160;a&#160;single&#160;instance:&#160;[self]   
#&#160;if&#160;the&#160;predicate&#160;is&#160;true&#160;and&#160;either&#160;tag&#160;is&#160;None&#160;or&#160;matches&#160;the&#160;object&#160;node
tag.  
#&#160;If&#160;the&#160;predicate&#160;returns&#160;false,&#160;return&#160;an&#160;empty&#160;list `

 searchone  (self, pattern, attname) 
     ` Return&#160;true&#160;iff&#160;the&#160;attribute&#160;with&#160;name&#160;attname&#160;is&#160;a&#160;string   
attribute&#160;which&#160;contains&#160;the&#160;compiled&#160;regular&#160;expression&#160;pattern,&#160;or  
if&#160;attname&#160;is&#160;None&#160;and&#160;pattern&#160;matches&#160;at&#160;least&#160;one&#160;string  
attribute.&#160;Return&#160;false&#160;if&#160;the&#160;attribute&#160;is&#160;not&#160;found&#160;or&#160;is&#160;not  
a&#160;string. `

* * *

Methods inherited from [ cdms.internattr.InternalAttributesClass
](/cdms.internattr.html) :  

 is_internal_attribute  (self, name) 
     ` [ is_internal_attribute ](/) (name)&#160;is&#160;true&#160;if&#160;name&#160;is&#160;internal. `

 replace_external_attributes  (self, newAttributes) 
     ` [ replace_external_attributes ](/) (newAttributes)   
Replace&#160;the&#160;external&#160;attributes&#160;with&#160;dictionary&#160;newAttributes. `

* * *

Methods inherited from [ PropertiedClasses.Properties.PropertiedClass
](/PropertiedClasses.Properties.html) :  

 __delattr__  (self, name) 

 __getattr__  (self, name) 

 __setattr__  (self, name, value) 

 get_property_d  (self, name) 
     ` Return&#160;the&#160;'del'&#160;property&#160;handler&#160;for&#160;name&#160;that&#160;self&#160;uses.   
Returns&#160;None&#160;if&#160;no&#160;handler. `

 get_property_g  (self, name) 
     ` Return&#160;the&#160;'get'&#160;property&#160;handler&#160;for&#160;name&#160;that&#160;self&#160;uses.   
Returns&#160;None&#160;if&#160;no&#160;handler. `

 get_property_s  (self, name) 
     ` Return&#160;the&#160;'set'&#160;property&#160;handler&#160;for&#160;name&#160;that&#160;self&#160;uses.   
Returns&#160;None&#160;if&#160;no&#160;handler. `

 set_property  (self, name, actg  =None  , acts  =None  , actd  =None  , nowrite  =None  , nodelete  =None  ) 
     ` Set&#160;attribute&#160;handlers&#160;for&#160;&#160;name&#160;to&#160;methods&#160;actg,&#160;acts,&#160;actd   
None&#160;means&#160;no&#160;change&#160;for&#160;that&#160;action.  
nowrite&#160;=&#160;1&#160;prevents&#160;setting&#160;this&#160;attribute.  
nowrite&#160;defaults&#160;to&#160;0\.  
nodelete&#160;=&#160;1&#160;prevents&#160;deleting&#160;this&#160;attribute.  
nodelete&#160;defaults&#160;to&#160;1&#160;unless&#160;actd&#160;given.  
if&#160;nowrite&#160;and&#160;nodelete&#160;is&#160;None:&#160;nodelete&#160;=&#160;1 `

  
class  LDAPResultEntry  ( [ AbstractResultEntry ](/cdms.database.html) )

` `

Methods defined here:  

 __init__  (self, db, dn, attributes) 

* * *

Methods inherited from [ AbstractResultEntry ](/cdms.database.html) :  

 getObject  (self) 
     ` Method:   
  
[ getObject ](/) ()  
  
Description:  
  
Get&#160;the&#160;CDMS&#160;object&#160;associated&#160;with&#160;this&#160;entry.  
  
Returns:  
  
Instance&#160;of&#160;a&#160;CDMS&#160;object. `

  
class  LDAPSearchResult  ( [ AbstractSearchResult ](/cdms.database.html) )

` `

Methods defined here:  

 __getitem__  (self, key) 

 __init__  (self, db, LDAPresult) 

 __len__  (self) 

 searchPredicate  (self, predicate, tag  =None  ) 
     ` Method:   
  
[ searchPredicate ](/) (predicate,&#160;tag=None)  
  
Description:  
  
Refine&#160;a&#160;search&#160;result,&#160;with&#160;a&#160;predicate&#160;search.  
  
Arguments:  
  
predicate:&#160;Function&#160;name&#160;or&#160;lambda&#160;function.&#160;The&#160;function&#160;takes&#160;a&#160;single&#160;CDMS
object,  
and&#160;returns&#160;true&#160;(1)&#160;if&#160;the&#160;object&#160;satisfies&#160;the&#160;predicate,&#160;0&#160;if&#160;not.  
tag:&#160;Restrict&#160;the&#160;search&#160;to&#160;objects&#160;in&#160;one&#160;class.  
  
Returns:  
  
SearchResult&#160;instance.&#160;Entries&#160;can&#160;be&#160;accessed&#160;sequentially.&#160;For&#160;each&#160;entry,
entry.name&#160;is&#160;the  
name&#160;of&#160;the&#160;entry,&#160;entry.attributes&#160;is&#160;a&#160;dictionary&#160;of&#160;the&#160;attributes&#160;returned
by&#160;the&#160;search,  
entry.getObject()&#160;returns&#160;the&#160;CDMS&#160;object&#160;associated&#160;with&#160;the&#160;entry:  
  
for&#160;entry&#160;in&#160;result:  
print&#160;entry.name,&#160;entry.attributes["id"]  
  
Entries&#160;can&#160;be&#160;refined&#160;with [ searchPredicate ](/) ().  
  
Example:  
  
(1)&#160;Find&#160;all&#160;variables&#160;on&#160;a&#160;73x96&#160;grid  
  
newresult&#160;=&#160;result. [ searchPredicate ](/) (lambda&#160;obj:
obj.getGrid().shape==(73,96),"variable") `

  
 Functions 

` `

 connect  (uri  =None  , user  =''  , password  =''  ) 
     ` Method:   
  
[ connect ](/) (uri=None,&#160;user="",&#160;password="")  
  
Description:  
  
Open&#160;a&#160;CDMS&#160;database&#160;connection.  
  
Arguments:  
  
uri:&#160;Universal&#160;Resource&#160;Identifier.&#160;If&#160;unspecified,&#160;defaults&#160;to&#160;the
environment&#160;variable&#160;CDMSROOT.  
user:&#160;user&#160;id  
password:&#160;password  
  
Returns:  
  
Database&#160;instance.  
  
Example:  
  
db&#160;=&#160;cdms. [ connect ](/)
("ldap://dbhost.llnl.gov/database=CDMS,ou=PCMDI,o=LLNL,c=US") `

 loadString  (text, uri, parent  =None  , datapath  =None  ) 
     ` Create&#160;a&#160;dataset&#160;from&#160;a&#160;text&#160;string.&#160;<text>&#160;is&#160;the&#160;string&#160;in&#160;CDML&#160;format.   
<uri>&#160;is&#160;the&#160;URL&#160;of&#160;the&#160;dataset&#160;in&#160;a&#160;catalog&#160;or&#160;file.  
<parent>&#160;is&#160;the&#160;containing&#160;database&#160;object,&#160;if&#160;any.  
<datapath>&#160;is&#160;the&#160;location&#160;of&#160;data&#160;files&#160;relative&#160;to&#160;the&#160;parent&#160;database&#160;URL.
`

  
 Data 

` `

 AuthenticationError  = 'Error authenticating to database'   
 Base  = 0   
 CannotOpenDataset  = 'Cannot open dataset'   
 ConnectError  = 'Error connecting to database'   
 DatabaseNotFound  = 'Database not found'   
 InvalidEntryName  = 'Invalid entry name'   
 MethodNotImplemented  = 'Method not yet implemented'   
 Onelevel  = 1   
 PermissionError  = 'No permission to access'   
 SchemeNotSupported  = 'Scheme not supported'   
 Subtree  = 2 

* * *

UCRL-WEB-213937 | [ Privacy & Legal Notice ](/disclaimer.html)

[ webmaster@pcmdi.llnl.gov ](/webmaster@pcmdi.llnl.gov)

[ ![Powered by Plone](media/plone_powered.gif) ](/)

