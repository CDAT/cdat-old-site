---
layout: default
title:
---

 [ Skip to content. ](/cdat/source/api-reference/esg.esg.html) | [ Skip to
navigation ](/cdat/source/api-reference/esg.esg.html)

Search Site

[ Advanced Search&#8230; ](/search_form)

#  [ PCMDI Software Portal ](/)

#####  Sections

  * [ Home ](/)

#####  Personal tools

  * [ Log in ](/login_form)

You are here:  [ Home ](/) -> [ CDAT ](/cdat) -> [ Source Code ](/cdat/source)
-> [ API Reference ](/cdat/source/api-reference) -> Python: module esg.esg

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

        * [ Python: module esg.esg ](/cdat/source/api-reference/esg.esg.html)

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

  * [ ![Send this page to somebody](media/mail_icon.gif) ](/cdat/source/api-reference/esg.esg.html/sendto_form)
  * [ ![Print this page](media/print_icon.gif) ](/this.print\(\))

#  Python: module esg.esg

  
  
 [ esg  ](/esg.html) .esg 
[ index ](/)  

` ESG&#160;markup&#160;support.&#160;See [ http://www.earthsystemgrid.org ](/) `

  
 Modules 

` `

[ cdtime ](/cdtime.html)  

[ re ](/re.html)  

[ string ](/string.html)  

  
 Classes 

` `

[ Contact ](/esg.esg.html)

[ ESGNode ](/esg.esg.html)

    

[ Activity ](/esg.esg.html)

    

[ Campaign ](/esg.esg.html)

[ Ensemble ](/esg.esg.html)

[ Investigation ](/esg.esg.html)

    

[ Analysis ](/esg.esg.html)

[ Experiment ](/esg.esg.html)

[ Observation ](/esg.esg.html)

[ Simulation ](/esg.esg.html)

[ Project ](/esg.esg.html)

[ Dataset ](/esg.esg.html)

[ File ](/esg.esg.html)

[ Institution ](/esg.esg.html)

[ Metadata ](/esg.esg.html)

[ Parameter ](/esg.esg.html)

[ ParameterList ](/esg.esg.html)

[ Person ](/esg.esg.html)

[ Service ](/esg.esg.html)

[ Format ](/esg.esg.html)

[ Mapping ](/esg.esg.html)

[ ObjRef ](/esg.esg.html)

    

[ Participant ](/esg.esg.html)

[ Qualified ](/esg.esg.html)

    

[ Date ](/esg.esg.html)

[ SimulationInput ](/esg.esg.html)

[ Reference ](/esg.esg.html)

[ SpaceRegion ](/esg.esg.html)

[ TimeRegion ](/esg.esg.html)

[ exceptions.Exception ](/exceptions.html)

    

[ ESGError ](/esg.esg.html)

  
class  Activity  ( [ ESGNode ](/esg.esg.html) )

` `

Methods defined here:  

 __init__  (self, id, name  =None  , description  =None  , rights  =None  , isPartOf  =None  , isDerivedFrom  =None  ) 

 addDate  (self, date) 

 addDerived  (seld, derived) 

 addNote  (self, note) 

 addParticipant  (self, participant) 

 addReference  (self, reference) 

 write  (self, fd) 

* * *

Methods inherited from [ ESGNode ](/esg.esg.html) :  

 endwrite  (self, fd) 

 startwrite  (self, fd, nl  =1  , noname  =0  ) 

  
class  Analysis  ( [ Investigation ](/esg.esg.html) )

` `

Method resolution order:

     [ Analysis ](/esg.esg.html)
     [ Investigation ](/esg.esg.html)
     [ Activity ](/esg.esg.html)
     [ ESGNode ](/esg.esg.html)

* * *

Methods defined here:  

 __init__  (self, id, name  =None  , description  =None  , rights  =None  , parent  =None  ) 

 write  (self, fd) 

* * *

Methods inherited from [ Activity ](/esg.esg.html) :  

 addDate  (self, date) 

 addDerived  (seld, derived) 

 addNote  (self, note) 

 addParticipant  (self, participant) 

 addReference  (self, reference) 

* * *

Methods inherited from [ ESGNode ](/esg.esg.html) :  

 endwrite  (self, fd) 

 startwrite  (self, fd, nl  =1  , noname  =0  ) 

  
class  Campaign  ( [ Activity ](/esg.esg.html) )

` `

Method resolution order:

     [ Campaign ](/esg.esg.html)
     [ Activity ](/esg.esg.html)
     [ ESGNode ](/esg.esg.html)

* * *

Methods defined here:  

 __init__  (self, id, name  =None  , description  =None  , rights  =None  ) 

 write  (self, fd) 

* * *

Methods inherited from [ Activity ](/esg.esg.html) :  

 addDate  (self, date) 

 addDerived  (seld, derived) 

 addNote  (self, note) 

 addParticipant  (self, participant) 

 addReference  (self, reference) 

* * *

Methods inherited from [ ESGNode ](/esg.esg.html) :  

 endwrite  (self, fd) 

 startwrite  (self, fd, nl  =1  , noname  =0  ) 

  
class  Contact 

` `

Methods defined here:  

 __init__  (self, street  =None  , city  =None  , state  =None  , region  =None  , province  =None  , postcode  =None  , country  =None  , email  =None  , telephone  =None  , fax  =None  , url  =None  ) 

 write  (self, fd) 

  
class  Dataset  ( [ ESGNode ](/esg.esg.html) )

` `

Methods defined here:  

 __init__  (self, id, generatedBy  =None  , ofType  =None  , isPartOf  =None  , convention  =None  , timeCoverage  =None  , spaceCoverage  =None  , format  =None  , name  =None  ) 
     ` Create&#160;a [ Dataset ](/) .   
  
id:&#160;Unique&#160;string&#160;identifier  
generatedBy: [ Investigation ](/) that&#160;generated&#160;the&#160;dataset.  
ofType:&#160;String&#160;distinguishing&#160;characteristic&#160;within&#160;an&#160;investigation,&#160;e.g.
"monthly&#160;means"  
isPartOf: [ Dataset ](/) that&#160;contains&#160;this&#160;dataset,&#160;if&#160;any.  
convention:&#160;String&#160;metadata&#160;convention&#160;ID,&#160;e.g.&#160;"CF-1.0"  
timeCoverage:&#160;instance&#160;of [ TimeRegion ](/)  
spaceCoverage:&#160;instance&#160;of [ SpaceRegion ](/) `

 addDate  (self, date) 
     ` Set&#160;an&#160;event&#160;date.   
  
ofType:&#160;String&#160;type&#160;of&#160;event,&#160;e.g.,&#160;"start"&#160;or&#160;"stop".  
datetime:&#160;String&#160;of&#160;form&#160;"yyyy-mm-dd&#160;hh:mi:ss" `

 addParameterList  (self, qlist) 
     ` Add&#160;a&#160;parameter&#160;list.   
  
qlist:&#160;idref&#160;of&#160;a&#160;parameter&#160;list. `

 setSpaceCoverage  (self, sc) 

 setTimeCoverage  (self, tc) 

 write  (self, fd) 

* * *

Methods inherited from [ ESGNode ](/esg.esg.html) :  

 endwrite  (self, fd) 

 startwrite  (self, fd, nl  =1  , noname  =0  ) 

  
class  Date  ( [ Qualified ](/esg.esg.html) )

` `

Methods defined here:  

 __init__  (self, type, encoding  =None  ) 

 write  (self, fd) 

* * *

Methods inherited from [ Qualified ](/esg.esg.html) :  

 setContent  (self, content) 

  
class  ESGError  ( [ exceptions.Exception ](/exceptions.html) )

` `

Methods defined here:  

 __init__  (self, args  ='Unspecified error from package esg'  ) 

 __str__  (self) 

* * *

Methods inherited from [ exceptions.Exception ](/exceptions.html) :  

 __getitem__  (...) 

  
class  ESGNode 

` `

` Abstract&#160;ESG&#160;node.  
`

Methods defined here:  

 __init__  (self, id, name  =None  ) 

 endwrite  (self, fd) 

 startwrite  (self, fd, nl  =1  , noname  =0  ) 

 write  (self, fd) 
     ` Output&#160;to&#160;a&#160;file.&#160;fd&#160;is&#160;an&#160;open&#160;file&#160;descriptor. `

  
class  Ensemble  ( [ Activity ](/esg.esg.html) )

` `

Method resolution order:

     [ Ensemble ](/esg.esg.html)
     [ Activity ](/esg.esg.html)
     [ ESGNode ](/esg.esg.html)

* * *

Methods defined here:  

 __init__  (self, id, name  =None  , description  =None  , rights  =None  ) 

 write  (self, fd) 

* * *

Methods inherited from [ Activity ](/esg.esg.html) :  

 addDate  (self, date) 

 addDerived  (seld, derived) 

 addNote  (self, note) 

 addParticipant  (self, participant) 

 addReference  (self, reference) 

* * *

Methods inherited from [ ESGNode ](/esg.esg.html) :  

 endwrite  (self, fd) 

 startwrite  (self, fd, nl  =1  , noname  =0  ) 

  
class  Experiment  ( [ Investigation ](/esg.esg.html) )

` `

Method resolution order:

     [ Experiment ](/esg.esg.html)
     [ Investigation ](/esg.esg.html)
     [ Activity ](/esg.esg.html)
     [ ESGNode ](/esg.esg.html)

* * *

Methods defined here:  

 __init__  (self, id, name  =None  , description  =None  , rights  =None  , parent  =None  ) 

 write  (self, fd) 

* * *

Methods inherited from [ Activity ](/esg.esg.html) :  

 addDate  (self, date) 

 addDerived  (seld, derived) 

 addNote  (self, note) 

 addParticipant  (self, participant) 

 addReference  (self, reference) 

* * *

Methods inherited from [ ESGNode ](/esg.esg.html) :  

 endwrite  (self, fd) 

 startwrite  (self, fd, nl  =1  , noname  =0  ) 

  
class  File  ( [ ESGNode ](/esg.esg.html) )

` `

Methods defined here:  

 __init__  (self, id, isPartOf  =None  , name  =None  , size  =None  ) 

 write  (self, fd) 

* * *

Methods inherited from [ ESGNode ](/esg.esg.html) :  

 endwrite  (self, fd) 

 startwrite  (self, fd, nl  =1  , noname  =0  ) 

  
class  Format 

` `

Methods defined here:  

 __init__  (self, uri, ofType) 

 write  (self, fd) 

  
class  Institution  ( [ ESGNode ](/esg.esg.html) )

` `

Methods defined here:  

 __init__  (self, id, name  =None  , ofType  =None  , contact  =None  ) 

 setContact  (self, c) 

 write  (self, fd) 

* * *

Methods inherited from [ ESGNode ](/esg.esg.html) :  

 endwrite  (self, fd) 

 startwrite  (self, fd, nl  =1  , noname  =0  ) 

  
class  Investigation  ( [ Activity ](/esg.esg.html) )

` `

Method resolution order:

     [ Investigation ](/esg.esg.html)
     [ Activity ](/esg.esg.html)
     [ ESGNode ](/esg.esg.html)

* * *

Methods defined here:  

 __init__  (self, id, name  =None  , description  =None  , rights  =None  ) 

* * *

Methods inherited from [ Activity ](/esg.esg.html) :  

 addDate  (self, date) 

 addDerived  (seld, derived) 

 addNote  (self, note) 

 addParticipant  (self, participant) 

 addReference  (self, reference) 

 write  (self, fd) 

* * *

Methods inherited from [ ESGNode ](/esg.esg.html) :  

 endwrite  (self, fd) 

 startwrite  (self, fd, nl  =1  , noname  =0  ) 

  
class  Mapping 

` `

Methods defined here:  

 __init__  (self, authority, standardName  =None  ) 

 write  (self, fd) 

  
class  Metadata  ( [ ESGNode ](/esg.esg.html) )

` `

` Root&#160;node.  
`

Methods defined here:  

 __init__  (self) 

 merge  (self, targetdsetid, sourcemd, sourcedsetid, newlistid, resultid  =None  , include  =None  , exclude  =None  , extralists  =None  , targetParams  =None  , mustResolve  ='no'  ) 
     ` Merge&#160;dataset&#160;sourcedsetid&#160;in&#160;container&#160;sourcemd,&#160;into&#160;dataset&#160;targetdsetid&#160;in&#160;self.   
  
targetdsetid:&#160;string&#160;ID&#160;of&#160;target&#160;dataset,&#160;in&#160;self  
sourcemd&#160;&#160;&#160;&#160;:&#160;metadata&#160;node&#160;containing&#160;source&#160;dataset  
sourcedsetid:&#160;string&#160;ID&#160;of&#160;source&#160;dataset  
newlistid&#160;&#160;&#160;:&#160;string&#160;ID&#160;for&#160;the&#160;new&#160;parameter&#160;list&#160;generated,&#160;if&#160;any.&#160;If&#160;the
target&#160;dataset&#160;has&#160;a  
parameter&#160;list&#160;with&#160;this&#160;ID,&#160;extra&#160;parameters&#160;are&#160;added&#160;to&#160;it&#160;instead.  
resultid&#160;&#160;&#160;&#160;:&#160;string&#160;ID&#160;of&#160;result&#160;dataset.&#160;Defaults&#160;to&#160;targetdsetid  
include&#160;&#160;&#160;&#160;&#160;:&#160;list&#160;of&#160;parameter&#160;names.&#160;If&#160;specified,&#160;only&#160;merge&#160;variables&#160;in
the&#160;list.  
exclude&#160;&#160;&#160;&#160;&#160;:&#160;list&#160;of&#160;parameter&#160;names.&#160;Do&#160;not&#160;merge&#160;variables&#160;in&#160;the&#160;list.  
extralists&#160;&#160;:&#160;list&#160;of&#160;extra&#160;parameters&#160;lists  
targetParams:&#160;list&#160;of&#160;parameters&#160;referenced&#160;by&#160;the&#160;source&#160;dataset,&#160;but&#160;not
included&#160;in&#160;the&#160;source&#160;metadata.  
mustResolve&#160;:&#160;["yes"&#160;|&#160;"no"]&#160;If&#160;yes,&#160;an&#160;error&#160;is&#160;raised&#160;whenever&#160;a
parameterlist&#160;IDREF&#160;cannot&#160;be&#160;resolved  
to&#160;the&#160;list&#160;object.&#160;Default&#160;is&#160;"no".  
  
Note:&#160;the&#160;merge&#160;is&#160;done&#160;in-place.&#160;If&#160;an&#160;exception&#160;occurs,&#160;the&#160;target&#160;dataset
may&#160;be&#160;modified. `

 setActivity  (self, activity) 

 setDataset  (self, dataset) 

 setFile  (self, fileobj) 

 setInstitution  (self, institution) 

 setParameter  (self, parameter) 

 setParameterList  (self, parameterList) 

 setPerson  (self, person) 

 setService  (self, service) 

 write  (self, fd) 

* * *

Methods inherited from [ ESGNode ](/esg.esg.html) :  

 endwrite  (self, fd) 

 startwrite  (self, fd, nl  =1  , noname  =0  ) 

  
class  ObjRef 

` `

Methods defined here:  

 __cmp__  (self, other) 

 __init__  (self, idref) 

 write  (self, fd, tag) 
     ` Write&#160;an&#160;object&#160;reference&#160;type&#160;(has&#160;an&#160;attribute&#160;'idref') `

  
class  Observation  ( [ Investigation ](/esg.esg.html) )

` `

Method resolution order:

     [ Observation ](/esg.esg.html)
     [ Investigation ](/esg.esg.html)
     [ Activity ](/esg.esg.html)
     [ ESGNode ](/esg.esg.html)

* * *

Methods defined here:  

 __init__  (self, id, name  =None  , description  =None  , rights  =None  , parent  =None  ) 

 write  (self, fd) 

* * *

Methods inherited from [ Activity ](/esg.esg.html) :  

 addDate  (self, date) 

 addDerived  (seld, derived) 

 addNote  (self, note) 

 addParticipant  (self, participant) 

 addReference  (self, reference) 

* * *

Methods inherited from [ ESGNode ](/esg.esg.html) :  

 endwrite  (self, fd) 

 startwrite  (self, fd, nl  =1  , noname  =0  ) 

  
class  Parameter  ( [ ESGNode ](/esg.esg.html) )

` `

Methods defined here:  

 __init__  (self, id, name, description  =None  , activityRef  =None  , standardName  =None  , standardAuthority  =None  ) 

 getMapping  (self) 

 setMapping  (self, mapping) 

 write  (self, fd) 

* * *

Methods inherited from [ ESGNode ](/esg.esg.html) :  

 endwrite  (self, fd) 

 startwrite  (self, fd, nl  =1  , noname  =0  ) 

  
class  ParameterList  ( [ ESGNode ](/esg.esg.html) )

` `

Methods defined here:  

 __init__  (self, id, description  =None  , paramrefs  =None  , activityRef  =None  ) 

 addParamRef  (self, paramref) 

 write  (self, fd) 

* * *

Methods inherited from [ ESGNode ](/esg.esg.html) :  

 endwrite  (self, fd) 

 startwrite  (self, fd, nl  =1  , noname  =0  ) 

  
class  Participant  ( [ ObjRef ](/esg.esg.html) )

` `

Methods defined here:  

 __init__  (self, idref, role) 

 write  (self, fd) 
     ` Write&#160;a&#160;participant&#160;type&#160;(has&#160;a&#160;role&#160;and&#160;idref). `

* * *

Methods inherited from [ ObjRef ](/esg.esg.html) :  

 __cmp__  (self, other) 

  
class  Person  ( [ ESGNode ](/esg.esg.html) )

` `

Methods defined here:  

 __init__  (self, id, firstName  =None  , lastName  =None  , contact  =None  , worksFor  =None  ) 

 setContact  (self, contact) 

 write  (self, fd) 

* * *

Methods inherited from [ ESGNode ](/esg.esg.html) :  

 endwrite  (self, fd) 

 startwrite  (self, fd, nl  =1  , noname  =0  ) 

  
class  Project  ( [ Activity ](/esg.esg.html) )

` `

Method resolution order:

     [ Project ](/esg.esg.html)
     [ Activity ](/esg.esg.html)
     [ ESGNode ](/esg.esg.html)

* * *

Methods defined here:  

 __init__  (self, id, name  =None  , description  =None  , rights  =None  , funding  =None  ) 

 setTopic  (self, topic) 

 write  (self, fd) 

* * *

Methods inherited from [ Activity ](/esg.esg.html) :  

 addDate  (self, date) 

 addDerived  (seld, derived) 

 addNote  (self, note) 

 addParticipant  (self, participant) 

 addReference  (self, reference) 

* * *

Methods inherited from [ ESGNode ](/esg.esg.html) :  

 endwrite  (self, fd) 

 startwrite  (self, fd, nl  =1  , noname  =0  ) 

  
class  Qualified 

` `

Methods defined here:  

 __init__  (self, qual, tag  =None  ) 

 setContent  (self, content) 

 write  (self, fd, tag) 
     ` Write&#160;a&#160;qualified&#160;type&#160;(has&#160;an&#160;attribute&#160;'type') `

  
class  Reference 

` `

Methods defined here:  

 __init__  (self, uri, reference  =None  ) 

 setContent  (self, content) 

 write  (self, fd) 
     ` Write&#160;a&#160;reference&#160;type&#160;(has&#160;a&#160;uri). `

  
class  Service  ( [ ESGNode ](/esg.esg.html) )

` `

Methods defined here:  

 __init__  (self, id, name  =None  , description  =None  ) 

* * *

Methods inherited from [ ESGNode ](/esg.esg.html) :  

 endwrite  (self, fd) 

 startwrite  (self, fd, nl  =1  , noname  =0  ) 

 write  (self, fd) 
     ` Output&#160;to&#160;a&#160;file.&#160;fd&#160;is&#160;an&#160;open&#160;file&#160;descriptor. `

  
class  Simulation  ( [ Investigation ](/esg.esg.html) )

` `

Method resolution order:

     [ Simulation ](/esg.esg.html)
     [ Investigation ](/esg.esg.html)
     [ Activity ](/esg.esg.html)
     [ ESGNode ](/esg.esg.html)

* * *

Methods defined here:  

 __init__  (self, id, name  =None  , description  =None  , rights  =None  ) 

 setHardware  (seld, hardware) 

 setInput  (self, input) 

 write  (self, fd) 

* * *

Methods inherited from [ Activity ](/esg.esg.html) :  

 addDate  (self, date) 

 addDerived  (seld, derived) 

 addNote  (self, note) 

 addParticipant  (self, participant) 

 addReference  (self, reference) 

* * *

Methods inherited from [ ESGNode ](/esg.esg.html) :  

 endwrite  (self, fd) 

 startwrite  (self, fd, nl  =1  , noname  =0  ) 

  
class  SimulationInput  ( [ Qualified ](/esg.esg.html) )

` `

Methods defined here:  

 __init__  (self, ofType, input  =None  ) 

* * *

Methods inherited from [ Qualified ](/esg.esg.html) :  

 setContent  (self, content) 

 write  (self, fd, tag) 
     ` Write&#160;a&#160;qualified&#160;type&#160;(has&#160;an&#160;attribute&#160;'type') `

  
class  SpaceRegion 

` `

Methods defined here:  

 __init__  (self, name  =None  , xrange  =None  , yrange  =None  , zrange  =None  ) 

 merge  (self, sr) 

 write  (self, fd) 

  
class  TimeRegion 

` `

Methods defined here:  

 __init__  (self, name  =None  , start  =None  , stop  =None  , encoding  =None  , calendar  ='gregorian'  ) 

 merge  (self, tr) 

 write  (self, fd) 

  
 Functions 

` `

 encodeIsoTime  (timeTuple, toEncoding  =None  ) 
     ` Encode&#160;a&#160;time&#160;tuple&#160;as&#160;an&#160;ISO&#160;8601&#160;time&#160;(see&#160;parseIsoTime).   
  
timeTuple:&#160;tuple&#160;(year,&#160;month,&#160;day,&#160;hour,&#160;minute,&#160;second,&#160;timezoneHour,
timezoneMinute) `

 encodeTime  (timeTuple, toEncoding  =None  ) 
     ` Encode&#160;a&#160;time&#160;tuple.   
  
timeTuple:&#160;tuple&#160;(year,&#160;month,&#160;day,&#160;hour,&#160;minute,&#160;second)  
toEncoding:&#160;encoding&#160;string,&#160;such&#160;as&#160;'yyyy-mm-dd&#160;hh:mi:ss'.&#160;If&#160;omitted,  
the&#160;string&#160;is&#160;generated&#160;based&#160;on&#160;the&#160;non-null&#160;values&#160;of&#160;timeTuple. `

 mapIllegalToEntity  (matchobj) 
     ` #&#160;Map&#160;reserved&#160;XML&#160;characters&#160;to&#160;entity&#160;references:   
#&#160;'<'&#160;\-->&#160;&lt;  
#&#160;'>'&#160;\-->&#160;&gt;  
#&#160;'&'&#160;\-->&#160;&amp;  
#&#160;'"'&#160;\-->&#160;&quot;  
#&#160;"'"&#160;\-->&#160;&apos;  
#&#160;all&#160;other&#160;illegal&#160;characters&#160;are&#160;removed&#160;#" `

 mergeRange  (ra, rb) 

 parseIsoTime  (timeString) 
     ` Parse&#160;an&#160;encoded&#160;time&#160;string&#160;in&#160;ISO&#160;8601&#160;format,&#160;conforming&#160;to&#160;the&#160;W3C&#160;profile&#160;( [ http://www.w3.org/TR/NOTE-datetime ](/TR/NOTE-datetime) ).   
  
A&#160;tuple&#160;of&#160;the&#160;form&#160;(year,&#160;month,&#160;day,&#160;hour,&#160;minute,&#160;second,&#160;timezoneHour,
timezoneMinute)&#160;is&#160;returned.  
  
In&#160;short,&#160;the&#160;encoding&#160;is:  
  
"YYYY(-MM(-DD(Thh(:mi(:ss.s)?)?TZD)?)?)?"  
  
(e.g.&#160;1997-07-16T19:20:30.45+01:00)  
  
where:  
  
YYYY&#160;=&#160;four-digit&#160;year  
MM&#160;&#160;&#160;=&#160;two-digit&#160;month&#160;(01=January,&#160;etc.)  
DD&#160;&#160;&#160;=&#160;two-digit&#160;day&#160;of&#160;month&#160;(01&#160;through&#160;31)  
hh&#160;&#160;&#160;=&#160;two&#160;digits&#160;of&#160;hour&#160;(00&#160;through&#160;23)&#160;(am/pm&#160;NOT&#160;allowed)  
mi&#160;&#160;&#160;=&#160;two&#160;digits&#160;of&#160;minute&#160;(00&#160;through&#160;59)  
ss&#160;&#160;&#160;=&#160;two&#160;digits&#160;of&#160;second&#160;(00&#160;through&#160;59)  
s&#160;&#160;&#160;&#160;=&#160;one&#160;or&#160;more&#160;digits&#160;representing&#160;a&#160;decimal&#160;fraction&#160;of&#160;a&#160;second  
TZD&#160;&#160;=&#160;time&#160;zone&#160;designator&#160;(Z&#160;or&#160;+hh:mm&#160;or&#160;-hh:mm) `

 parseTime  (timeString, fromEncoding  =r'yyyy(-mm(-dd(\s+hh(:mi(:ss)?)?)?)?)?'  ) 
     ` Parse&#160;an&#160;encoded&#160;time&#160;string,&#160;returning&#160;a&#160;tuple&#160;of&#160;the&#160;form   
(year,&#160;month,&#160;day,&#160;hour,&#160;minute,&#160;second).  
  
timeString:&#160;string&#160;representing&#160;an&#160;absolute&#160;time.&#160;If&#160;None,&#160;return&#160;value&#160;is
None.  
fromEncoding:&#160;input&#160;time&#160;encoding,&#160;a&#160;regular&#160;expression&#160;(see&#160;the&#160;re&#160;module),  
defaults&#160;to&#160;"yyyy(-mm(-dd(\s+hh(:mi(:ss)?)?)?)?)?"  
  
An&#160;exception&#160;is&#160;raised&#160;if&#160;the&#160;time&#160;string&#160;and&#160;encoding&#160;don't&#160;match. `

 writes  (fd, tag, s) 
     ` Write&#160;a&#160;string&#160;element. `

  
 Data 

` `

 defaultTimeEncoding  = r'yyyy(-mm(-dd(\s+hh(:mi(:ss)?)?)?)?)?'   
 namespace  = 'http://www.earthsystemgrid.org/'   
 nsprefix  = 'esg'   
 schemaLocation  = 'http://www.ucar.edu/schemas/esg.xsd' 

* * *

UCRL-WEB-213937 | [ Privacy & Legal Notice ](/disclaimer.html)

[ webmaster@pcmdi.llnl.gov ](/webmaster@pcmdi.llnl.gov)

[ ![Powered by Plone](media/plone_powered.gif) ](/)

