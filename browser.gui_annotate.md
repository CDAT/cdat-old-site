---
layout: default
title: browser gui_annotate
---

##  Python: module browser.gui_annotate

    #ThePCMDIDataBrowserPlotAnnotation-gui_annotatemodule  
    ##############################################################################
    #Module:gui_annotatemodule
    #Copyright:"SeefileLegal.htmforcopyrightinformation."
    #Authors:PCMDISoftwareTeam
    #LawrenceLivermoreNationalLaboratory:
    #support@pcmdi.llnl.gov
    #Description:PCMDISoftwareSystembrowserVCSplotannotation.
    #Version:4.0
    ##############################################################################
    #---------------------------------------------------------------------  
    #NOTE:needtouseversionofPythonthatimportsTkinterandPmw  
    #--------------------------------------------------------------------- 
  
### Modules 
* [Numeric](Numeric.html)  
* [Tkinter](Tkinter.html)  
* [__main__](__main__.html)  
* [cdms](cdms.html)  
* [cdtime](cdtime.html)  
* [gui_support.gui_color](gui_support.gui_color.html)  
* [browser.gui_control](browser.gui_control.html)  
* [browser.gui_functions](browser.gui_functions.html)  
* [browser.gui_menu](browser.gui_menu.html)  
* [browser.gui_set_text_object](browser.gui_set_text_object.html)  
* [math](math.html)  
* [string](string.html)  
* [sys](sys.html)  
* [vcs](vcs.html)  
* [browser.vcs_function](browser.vcs_function.html)  

### Classes 
* [Tkinter.Button](Tkinter.html) ( * [Tkinter.Widget](Tkinter.html) )
* [EntryButton](browser.gui_annotate.html)
* [create](browser.gui_annotate.html)
  
class  EntryButton  ( * [Tkinter.Button](Tkinter.html) )

####Method resolution order:
* [EntryButton](browser.gui_annotate.html)
* [Tkinter.Button](Tkinter.html)
* [Tkinter.Widget](Tkinter.html)
* [Tkinter.BaseWidget](Tkinter.html)
* [Tkinter.Misc](Tkinter.html)
* [Tkinter.Pack](Tkinter.html)
* [Tkinter.Place](Tkinter.html)
* [Tkinter.Grid](Tkinter.html)

* * *

Methods defined here:  

    __init__  (self, master  =None  , cnf  ={}  , kw) 

* * *

Methods inherited from * [Tkinter.Button](Tkinter.html) :  

flash  (self) 

    Flashthebutton.   
  
    This is accomplished by redisplaying  
    thebuttonseveraltimes,alternatingbetweenactiveand  
    normalcolors.Attheendoftheflashthebuttonisleft  
    inthesamenormal/activestateaswhenthecommandwas  
    invoked.Thiscommandisignoredifthebutton'sstateis  
    disabled. 

    invoke  (self) 
    Invokethecommandassociatedwiththebutton.   
  
    Thereturnvalueisthereturnvaluefromthecommand,  
    oranemptystringifthereisnocommandassociatedwith  
    thebutton.Thiscommandisignoredifthebutton'sstate  
    isdisabled. 

    tkButtonDown  (self, *dummy) 
    tkButtonEnter  (self, *dummy) 
    tkButtonInvoke  (self, *dummy) 
    tkButtonLeave  (self, *dummy) 
    tkButtonUp  (self, *dummy) 

* * *

Methods inherited from * [Tkinter.BaseWidget](Tkinter.html) :  

    destroy  (self) 
    Destroythisandalldescendantswidgets. 

* * *

Methods inherited from * [Tkinter.Misc](Tkinter.html) :  

__getitem__  = cget(self, key) 

    ReturntheresourcevalueforaKEYgivenasstring. 

__setitem__  (self, key, value) 
    
__str__  (self) 

    Returnthewindowpathnameofthiswidget. 

     after  (self, ms, func  =None  , *args) 
          Callfunctiononceaftergiventime.   
  
    MSspecifiesthetimeinmilliseconds.FUNCgivesthe  
    functionwhichshallbecalled.Additionalparameters  
    aregivenasparameterstothefunctioncall.Return  
    identifiertocancelschedulingwithafter_cancel. 

     after_cancel  (self, id) 
          CancelschedulingoffunctionidentifiedwithID.   
  
    Identifierreturnedbyafterorafter_idlemustbe  
    givenasfirstparameter. 
    
     after_idle  (self, func, *args) 
          CallFUNConceiftheTclmainloophasnoeventtoprocess.  
  
    Returnanidentifiertocanceltheschedulingwith  
    after_cancel. 
    
     bbox  = grid_bbox(self, column  =None  , row  =None  , col2  =None  , row2  =None  ) 
          Returnatupleofintegercoordinatesforthebounding   
    boxofthiswidgetcontrolledbythegeometrymanagergrid.  
      
    IfCOLUMN,ROWisgiventheboundingboxappliesfrom  
    thecellwithrowandcolumn0tothespecified  
    cell.IfCOL2andROW2aregiventheboundingbox  
    startsatthatcell.  
      
    Thereturnedintegersspecifytheoffsetoftheupperleft  
    cornerinthemasterwidgetandthewidthandheight. 
    
     bell  (self, displayof  =0  ) 
          Ringadisplay'sbell. 
    
     bind  (self, sequence  =None  , func  =None  , add  =None  ) 
          BindtothiswidgetateventSEQUENCEacalltofunctionFUNC.   
    
SEQUENCEisastringofconcatenatedevent  
patterns.Aneventpatternisoftheform  
<MODIFIER-MODIFIER-TYPE-DETAIL>whereMODIFIERisone  
ofControl,Mod2,M2,Shift,Mod3,M3,Lock,Mod4,M4,  
Button1,B1,Mod5,M5Button2,B2,Meta,M,Button3,  
B3,Alt,Button4,B4,Double,Button5,B5Triple,  
Mod1,M1.TYPEisoneofActivate,Enter,Map,  
ButtonPress, * [Button](Tkinter.html) ,Expose,Motion,ButtonRelease  
FocusIn,MouseWheel,Circulate,FocusOut,Property,  
Colormap,GravityReparent,Configure,KeyPress,Key,  
Unmap,Deactivate,KeyReleaseVisibility,Destroy,  
LeaveandDETAIListhebuttonnumberforButtonPress,  
ButtonReleaseandDETAIListheKeysymforKeyPressand  
KeyRelease.Examplesare  
<Control- * [Button](Tkinter.html) -1>forpressingControlandmousebutton
1or  
<Alt-A>forpressingAandtheAltkey(KeyPresscanbeomitted).  
Aneventpatterncanalsobeavirtualeventoftheform  
<<AString>>whereAStringcanbearbitrary.This  
eventcanbegeneratedbyevent_generate.  
Ifeventsareconcatenatedtheymustappearshortly  
aftereachother.  
  
FUNCwillbecallediftheeventsequenceoccurswithan  
instanceofEventasargument.IfthereturnvalueofFUNCis  
"break"nofurtherboundfunctionisinvoked.  
  
AnadditionalbooleanparameterADDspecifieswhetherFUNCwill  
becalledadditionallytotheotherboundfunctionorwhether  
itwillreplacethepreviousfunction.  
  
Bindwillreturnanidentifiertoallowdeletionoftheboundfunctionwith  
unbindwithoutmemoryleak.  
  
IfFUNCorSEQUENCEisomittedtheboundfunctionorlist  
ofboundeventsarereturned. 

 bind_all  (self, sequence  =None  , func  =None  , add  =None  ) 
      BindtoallwidgetsataneventSEQUENCEacalltofunctionFUNC.   
AnadditionalbooleanparameterADDspecifieswhetherFUNCwill  
becalledadditionallytotheotherboundfunctionorwhether  
itwillreplacethepreviousfunction.Seebindforthereturnvalue. 

 bind_class  (self, className, sequence  =None  , func  =None  , add  =None  ) 
      BindtowidgetswithbindtagCLASSNAMEatevent   
SEQUENCEacalloffunctionFUNC.Anadditional  
booleanparameterADDspecifieswhetherFUNCwillbe  
calledadditionallytotheotherboundfunctionor  
whetheritwillreplacethepreviousfunction.Seebindfor  
thereturnvalue. 

 bindtags  (self, tagList  =None  ) 
      Setorgetthelistofbindtagsforthiswidget.   
  
Withnoargumentreturnthelistofallbindtagsassociatedwith  
thiswidget.Withalistofstringsasargumentthebindtagsare  
settothislist.Thebindtagsdetermineinwhichordereventsare  
processed(seebind). 

 cget  (self, key) 
      ReturntheresourcevalueforaKEYgivenasstring. 

 clipboard_append  (self, string, kw) 
      AppendSTRINGtotheTkclipboard.   
  
Awidgetspecifiedattheoptionaldisplayofkeyword  
argumentspecifiesthetargetdisplay.Theclipboard  
canberetrievedwithselection_get. 

 clipboard_clear  (self, kw) 
      ClearthedataintheTkclipboard.   
  
Awidgetspecifiedfortheoptionaldisplayofkeyword  
argumentspecifiesthetargetdisplay. 

 colormodel  (self, value  =None  ) 
      Useless.NotimplementedinTk. 

 columnconfigure  = grid_columnconfigure(self, index, cnf  ={}  , kw) 
      ConfigurecolumnINDEXofagrid.   
  
Validresourcesareminsize(minimumsizeofthecolumn),  
weight(howmuchdoesadditionalspacepropagatetothiscolumn)  
andpad(howmuchspacetoletadditionally). 

 config  = configure(self, cnf  =None  , kw) 
      Configureresourcesofawidget.   
  
Thevaluesforresourcesarespecifiedaskeyword  
arguments.Togetanoverviewabout  
theallowedkeywordargumentscallthemethodkeys. 

 configure  (self, cnf  =None  , kw) 
      Configureresourcesofawidget.   
  
Thevaluesforresourcesarespecifiedaskeyword  
arguments.Togetanoverviewabout  
theallowedkeywordargumentscallthemethodkeys. 

 deletecommand  (self, name) 
      Internalfunction.   
  
DeletetheTclcommandprovidedinNAME. 

 event_add  (self, virtual, *sequences) 
      BindavirtualeventVIRTUAL(oftheform<<Name>>)   
toaneventSEQUENCEsuchthatthevirtualeventistriggered  
wheneverSEQUENCEoccurs. 

 event_delete  (self, virtual, *sequences) 
      UnbindavirtualeventVIRTUALfromSEQUENCE. 

 event_generate  (self, sequence, kw) 
      GenerateaneventSEQUENCE.Additional   
keywordargumentsspecifyparameteroftheevent  
(e.g.x,y,rootx,rooty). 

 event_info  (self, virtual  =None  ) 
      Returnalistofallvirtualeventsortheinformation   
abouttheSEQUENCEboundtothevirtualeventVIRTUAL. 

 focus  = focus_set(self) 
      Directinputfocustothiswidget.   
  
Iftheapplicationcurrentlydoesnothavethefocus  
thiswidgetwillgetthefocusiftheapplicationgets  
thefocusthroughthewindowmanager. 

 focus_displayof  (self) 
      Returnthewidgetwhichhascurrentlythefocusonthe   
displaywherethiswidgetislocated.  
  
ReturnNoneiftheapplicationdoesnothavethefocus. 

 focus_force  (self) 
      Directinputfocustothiswidgetevenifthe   
applicationdoesnothavethefocus.Usewith  
caution! 

 focus_get  (self) 
      Returnthewidgetwhichhascurrentlythefocusinthe   
application.  
  
Usefocus_displayoftoallowworkingwithseveral  
displays.ReturnNoneifapplicationdoesnothave  
thefocus. 

 focus_lastfor  (self) 
      Returnthewidgetwhichwouldhavethefocusiftoplevel   
forthiswidgetgetsthefocusfromthewindowmanager. 

 focus_set  (self) 
      Directinputfocustothiswidget.   
  
Iftheapplicationcurrentlydoesnothavethefocus  
thiswidgetwillgetthefocusiftheapplicationgets  
thefocusthroughthewindowmanager. 

 getboolean  (self, s) 
      ReturnabooleanvalueforTclbooleanvaluestrueandfalsegivenasparameter. 

 getvar  (self, name  ='PY_VAR'  ) 
      ReturnvalueofTclvariableNAME. 

 grab_current  (self) 
      Returnwidgetwhichhascurrentlythegrabinthisapplication   
orNone. 

 grab_release  (self) 
      Releasegrabforthiswidgetifcurrentlyset. 

 grab_set  (self) 
      Setgrabforthiswidget.   
  
Agrabdirectsalleventstothisanddescendant  
widgetsintheapplication. 

 grab_set_global  (self) 
      Setglobalgrabforthiswidget.   
  
Aglobalgrabdirectsalleventstothisand  
descendantwidgetsonthedisplay.Usewithcaution\-  
otherapplicationsdonotgeteventsanymore. 

 grab_status  (self) 
      ReturnNone,"local"or"global"ifthiswidgethas   
no,alocaloraglobalgrab. 

 grid_bbox  (self, column  =None  , row  =None  , col2  =None  , row2  =None  ) 
      Returnatupleofintegercoordinatesforthebounding   
boxofthiswidgetcontrolledbythegeometrymanagergrid.  
  
IfCOLUMN,ROWisgiventheboundingboxappliesfrom  
thecellwithrowandcolumn0tothespecified  
cell.IfCOL2andROW2aregiventheboundingbox  
startsatthatcell.  
  
Thereturnedintegersspecifytheoffsetoftheupperleft  
cornerinthemasterwidgetandthewidthandheight. 

 grid_columnconfigure  (self, index, cnf  ={}  , kw) 
      ConfigurecolumnINDEXofagrid.   
  
Validresourcesareminsize(minimumsizeofthecolumn),  
weight(howmuchdoesadditionalspacepropagatetothiscolumn)  
andpad(howmuchspacetoletadditionally). 

 grid_location  (self, x, y) 
      Returnatupleofcolumnandrowwhichidentifythecell   
atwhichthepixelatpositionXandYinsidethemaster  
widgetislocated. 

 grid_propagate  (self, flag  =['_noarg_']  ) 
      Setorgetthestatusforpropagationofgeometryinformation.   
  
Abooleanargumentspecifieswhetherthegeometryinformation  
oftheslaveswilldeterminethesizeofthiswidget.Ifnoargument  
isgiven,thecurrentsettingwillbereturned. 

 grid_rowconfigure  (self, index, cnf  ={}  , kw) 
      ConfigurerowINDEXofagrid.   
  
Validresourcesareminsize(minimumsizeoftherow),  
weight(howmuchdoesadditionalspacepropagatetothisrow)  
andpad(howmuchspacetoletadditionally). 

 grid_size  (self) 
      Returnatupleofthenumberofcolumnandrowsinthegrid. 

 grid_slaves  (self, row  =None  , column  =None  ) 
      Returnalistofallslavesofthiswidget   
initspackingorder. 

 image_names  (self) 
      Returnalistofallexistingimagenames. 

 image_types  (self) 
      Returnalistofallavailableimagetypes(e.g.photebitmap). 

 keys  (self) 
      Returnalistofallresourcenamesofthiswidget. 

 lift  = tkraise(self, aboveThis  =None  ) 
      Raisethiswidgetinthestackingorder. 

 lower  (self, belowThis  =None  ) 
      Lowerthiswidgetinthestackingorder. 

 mainloop  (self, n  =0  ) 
      CallthemainloopofTk. 

 nametowidget  (self, name) 
      ReturntheTkinterinstanceofawidgetidentifiedby   
itsTclnameNAME. 

 option_add  (self, pattern, value, priority  =None  ) 
      SetaVALUE(secondparameter)foranoption   
PATTERN(firstparameter).  
  
Anoptionalthirdparametergivesthenumericpriority  
(defaultsto80). 

 option_clear  (self) 
      Cleartheoptiondatabase.   
  
Itwillbereloadedifoption_addiscalled. 

 option_get  (self, name, className) 
      ReturnthevalueforanoptionNAMEforthiswidget   
withCLASSNAME.  
  
Valueswithhigherpriorityoverridelowervalues. 

 option_readfile  (self, fileName, priority  =None  ) 
      ReadfileFILENAMEintotheoptiondatabase.   
  
Anoptionalsecondparametergivesthenumeric  
priority. 

 pack_propagate  (self, flag  =['_noarg_']  ) 
      Setorgetthestatusforpropagationofgeometryinformation.   
  
Abooleanargumentspecifieswhetherthegeometryinformation  
oftheslaveswilldeterminethesizeofthiswidget.Ifnoargument  
isgiventhecurrentsettingwillbereturned. 

 pack_slaves  (self) 
      Returnalistofallslavesofthiswidget   
initspackingorder. 

 place_slaves  (self) 
      Returnalistofallslavesofthiswidget   
initspackingorder. 

 propagate  = pack_propagate(self, flag  =['_noarg_']  ) 
      Setorgetthestatusforpropagationofgeometryinformation.   
  
Abooleanargumentspecifieswhetherthegeometryinformation  
oftheslaveswilldeterminethesizeofthiswidget.Ifnoargument  
isgiventhecurrentsettingwillbereturned. 

 quit  (self) 
      QuittheTclinterpreter.Allwidgetswillbedestroyed. 

 register  = _register(self, func, subst  =None  , needcleanup  =1  ) 
      ReturnanewlycreatedTclfunction.Ifthis   
functioniscalled,thePythonfunctionFUNCwill  
beexecuted.AnoptionalfunctionSUBSTcan  
begivenwhichwillbeexecutedbeforeFUNC. 

 rowconfigure  = grid_rowconfigure(self, index, cnf  ={}  , kw) 
      ConfigurerowINDEXofagrid.   
  
Validresourcesareminsize(minimumsizeoftherow),  
weight(howmuchdoesadditionalspacepropagatetothisrow)  
andpad(howmuchspacetoletadditionally). 

 selection_clear  (self, kw) 
      ClearthecurrentXselection. 

 selection_get  (self, kw) 
      ReturnthecontentsofthecurrentXselection.   
  
Akeywordparameterselectionspecifiesthenameof  
theselectionanddefaultstoPRIMARY.Akeyword  
parameterdisplayofspecifiesawidgetonthedisplay  
touse. 

 selection_handle  (self, command, kw) 
      SpecifyafunctionCOMMANDtocalliftheX   
selectionownedbythiswidgetisqueriedbyanother  
application.  
  
Thisfunctionmustreturnthecontentsofthe  
selection.Thefunctionwillbecalledwiththe  
argumentsOFFSETandLENGTHwhichallowsthechunking  
ofverylongselections.Thefollowingkeyword  
parameterscanbeprovided:  
selection-nameoftheselection(defaultPRIMARY),  
type-typeoftheselection(e.g.STRING,FILE_NAME). 

 selection_own  (self, kw) 
      BecomeownerofXselection.   
  
Akeywordparameterselectionspecifiesthenameof  
theselection(defaultPRIMARY). 

 selection_own_get  (self, kw) 
      ReturnownerofXselection.   
  
Thefollowingkeywordparametercan  
beprovided:  
selection-nameoftheselection(defaultPRIMARY),  
type-typeoftheselection(e.g.STRING,FILE_NAME). 

 send  (self, interp, cmd, *args) 
      SendTclcommandCMDtodifferentinterpreterINTERPtobeexecuted. 

 setvar  (self, name  ='PY_VAR'  , value  ='1'  ) 
      SetTclvariableNAMEtoVALUE. 

 size  = grid_size(self) 
      Returnatupleofthenumberofcolumnandrowsinthegrid. 

 slaves  = pack_slaves(self) 
      Returnalistofallslavesofthiswidget   
initspackingorder. 

 tk_bisque  (self) 
      ChangethecolorschemetolightbrownasusedinTk3.6andbefore. 

 tk_focusFollowsMouse  (self) 
      Thewidgetundermousewillgetautomaticallyfocus.Cannot   
bedisabledeasily. 

 tk_focusNext  (self) 
      Returnthenextwidgetinthefocusorderwhichfollows   
widgetwhichhascurrentlythefocus.  
  
Thefocusorderfirstgoestothenextchild,thento  
thechildrenofthechildrecursivelyandthentothe  
nextsiblingwhichishigherinthestackingorder.A  
widgetisomittedifithasthetakefocusresourceset  
to0\. 

 tk_focusPrev  (self) 
      Returnpreviouswidgetinthefocusorder.Seetk_focusNextfordetails. 

 tk_menuBar  (self, *args) 
      Donotuse.NeededinTk3.6andearlier. 

 tk_setPalette  (self, *args, kw) 
      Setanewcolorschemeforallwidgetelements.   
  
AsinglecolorasargumentwillcausethatallcolorsofTk  
widgetelementsarederivedfromthis.  
Alternativelyseveralkeywordparametersanditsassociated  
colorscanbegiven.Thefollowingkeywordsarevalid:  
activeBackground,foreground,selectColor,  
activeForeground,highlightBackground,selectBackground,  
background,highlightColor,selectForeground,  
disabledForeground,insertBackground,troughColor. 

 tk_strictMotif  (self, boolean  =None  ) 
      SetTclinternalvariable,whetherthelookandfeel   
shouldadheretoMotif.  
  
Aparameterof1meansadheretoMotif(e.g.nocolor  
changeifmousepassesoverslider).  
Returnsthesetvalue. 

 tkraise  (self, aboveThis  =None  ) 
      Raisethiswidgetinthestackingorder. 

 unbind  (self, sequence, funcid  =None  ) 
      UnbindforthiswidgetforeventSEQUENCEthe   
functionidentifiedwithFUNCID. 

 unbind_all  (self, sequence) 
      UnbindforallwidgetsforeventSEQUENCEallfunctions. 

 unbind_class  (self, className, sequence) 
      UnbindforaallwidgetswithbindtagCLASSNAMEforeventSEQUENCE   
allfunctions. 

 update  (self) 
      EntereventloopuntilallpendingeventshavebeenprocessedbyTcl. 

 update_idletasks  (self) 
      Entereventloopuntilallidlecallbackshavebeencalled.This   
willupdatethedisplayofwindowsbutnotprocesseventscausedby  
theuser. 

 wait_variable  (self, name  ='PY_VAR'  ) 
      Waituntilthevariableismodified.   
  
AparameteroftypeIntVar,StringVar,DoubleVaror  
BooleanVarmustbegiven. 

 wait_visibility  (self, window  =None  ) 
      WaituntilthevisibilityofaWIDGETchanges   
(e.g.itappears).  
  
Ifnoparameterisgivenselfisused. 

 wait_window  (self, window  =None  ) 
      WaituntilaWIDGETisdestroyed.   
  
Ifnoparameterisgivenselfisused. 

 waitvar  = wait_variable(self, name  ='PY_VAR'  ) 
      Waituntilthevariableismodified.   
  
AparameteroftypeIntVar,StringVar,DoubleVaror  
BooleanVarmustbegiven. 

 winfo_atom  (self, name, displayof  =0  ) 
      ReturnintegerwhichrepresentsatomNAME. 

 winfo_atomname  (self, id, displayof  =0  ) 
      ReturnnameofatomwithidentifierID. 

 winfo_cells  (self) 
      Returnnumberofcellsinthecolormapforthiswidget. 

 winfo_children  (self) 
      Returnalistofallwidgetswhicharechildrenofthiswidget. 

 winfo_class  (self) 
      Returnwindowclassnameofthiswidget. 

 winfo_colormapfull  (self) 
      Returntrueifatthelastcolorrequestthecolormapwasfull. 

 winfo_containing  (self, rootX, rootY, displayof  =0  ) 
      ReturnthewidgetwhichisattherootcoordinatesROOTX,ROOTY. 

 winfo_depth  (self) 
      Returnthenumberofbitsperpixel. 

 winfo_exists  (self) 
      Returntrueifthiswidgetexists. 

 winfo_fpixels  (self, number) 
      ReturnthenumberofpixelsforthegivendistanceNUMBER   
(e.g."3c")asfloat. 

 winfo_geometry  (self) 
      Returngeometrystringforthiswidgetintheform"widthxheight+X+Y". 

 winfo_height  (self) 
      Returnheightofthiswidget. 

 winfo_id  (self) 
      ReturnidentifierIDforthiswidget. 

 winfo_interps  (self, displayof  =0  ) 
      ReturnthenameofallTclinterpretersforthisdisplay. 

 winfo_ismapped  (self) 
      Returntrueifthiswidgetismapped. 

 winfo_manager  (self) 
      Returnthewindowmanangernameforthiswidget. 

 winfo_name  (self) 
      Returnthenameofthiswidget. 

 winfo_parent  (self) 
      Returnthenameoftheparentofthiswidget. 

 winfo_pathname  (self, id, displayof  =0  ) 
      ReturnthepathnameofthewidgetgivenbyID. 

 winfo_pixels  (self, number) 
      Roundedintegervalueofwinfo_fpixels. 

 winfo_pointerx  (self) 
      Returnthexcoordinateofthepointerontherootwindow. 

 winfo_pointerxy  (self) 
      Returnatupleofxandycoordinatesofthepointerontherootwindow. 

 winfo_pointery  (self) 
      Returntheycoordinateofthepointerontherootwindow. 

 winfo_reqheight  (self) 
      Returnrequestedheightofthiswidget. 

 winfo_reqwidth  (self) 
      Returnrequestedwidthofthiswidget. 

 winfo_rgb  (self, color) 
      Returntupleofdecimalvaluesforred,green,bluefor   
COLORinthiswidget. 

 winfo_rootx  (self) 
      Returnxcoordinateofupperleftcornerofthiswidgetonthe   
rootwindow. 

 winfo_rooty  (self) 
      Returnycoordinateofupperleftcornerofthiswidgetonthe   
rootwindow. 

 winfo_screen  (self) 
      Returnthescreennameofthiswidget. 

 winfo_screencells  (self) 
      Returnthenumberofthecellsinthecolormapofthescreen   
ofthiswidget. 

 winfo_screendepth  (self) 
      Returnthenumberofbitsperpixeloftherootwindowofthe   
screenofthiswidget. 

 winfo_screenheight  (self) 
      Returnthenumberofpixelsoftheheightofthescreenofthiswidget   
inpixel. 

 winfo_screenmmheight  (self) 
      Returnthenumberofpixelsoftheheightofthescreenof   
thiswidgetinmm. 

 winfo_screenmmwidth  (self) 
      Returnthenumberofpixelsofthewidthofthescreenof   
thiswidgetinmm. 

 winfo_screenvisual  (self) 
      Returnoneofthestringsdirectcolor,grayscale,pseudocolor,   
staticcolor,staticgray,ortruecolorforthedefault  
colormodelofthisscreen. 

 winfo_screenwidth  (self) 
      Returnthenumberofpixelsofthewidthofthescreenof   
thiswidgetinpixel. 

 winfo_server  (self) 
      ReturninformationoftheX-Serverofthescreenofthiswidgetin   
theform"XmajorRminorvendorvendorVersion". 

 winfo_toplevel  (self) 
      Returnthetoplevelwidgetofthiswidget. 

 winfo_viewable  (self) 
      Returntrueifthewidgetandallitshigherancestorsaremapped. 

 winfo_visual  (self) 
      Returnoneofthestringsdirectcolor,grayscale,pseudocolor,   
staticcolor,staticgray,ortruecolorforthe  
colormodelofthiswidget. 

 winfo_visualid  (self) 
      ReturntheXidentifierforthevisualforthiswidget. 

 winfo_visualsavailable  (self, includeids  =0  ) 
      Returnalistofallvisualsavailableforthescreen   
ofthiswidget.  
  
Eachiteminthelistconsistsofavisualname(seewinfo_visual),a  
depthandifINCLUDEIDS=1isgivenalsotheXidentifier. 

 winfo_vrootheight  (self) 
      Returntheheightofthevirtualrootwindowassociatedwiththis   
widgetinpixels.Ifthereisnovirtualrootwindowreturnthe  
heightofthescreen. 

 winfo_vrootwidth  (self) 
      Returnthewidthofthevirtualrootwindowassociatedwiththis   
widgetinpixel.Ifthereisnovirtualrootwindowreturnthe  
widthofthescreen. 

 winfo_vrootx  (self) 
      Returnthexoffsetofthevirtualrootrelativetotheroot   
windowofthescreenofthiswidget. 

 winfo_vrooty  (self) 
      Returntheyoffsetofthevirtualrootrelativetotheroot   
windowofthescreenofthiswidget. 

 winfo_width  (self) 
      Returnthewidthofthiswidget. 

 winfo_x  (self) 
      Returnthexcoordinateoftheupperleftcornerofthiswidget   
intheparent. 

 winfo_y  (self) 
      Returntheycoordinateoftheupperleftcornerofthiswidget   
intheparent. 

* * *

Data and other attributes inherited from * [Tkinter.Misc](Tkinter.html) :  

 getdouble  = <type 'float'>
      float(x)->floatingpointnumber   
  
Convertastringornumbertoafloatingpointnumber,ifpossible. 

 getint  = <type 'int'>
      int(x[,base])->integer   
  
Convertastringornumbertoaninteger,ifpossible.Afloatingpoint  
argumentwillbetruncatedtowardszero(thisdoesnotincludeastring  
representationofafloatingpointnumber!)Whenconvertingastring,use  
theoptionalbase.Itisanerrortosupplyabasewhenconvertinga  
non-string.Iftheargumentisoutsidetheintegerrangealongobject  
willbereturnedinstead. 

* * *

Methods inherited from * [Tkinter.Pack](Tkinter.html) :  

 forget  = pack_forget(self) 
      Unmapthiswidgetanddonotuseitforthepackingorder. 

 info  = pack_info(self) 
      Returninformationaboutthepackingoptions   
forthiswidget. 

 pack  = pack_configure(self, cnf  ={}  , kw) 
      Packawidgetintheparentwidget.Useasoptions:   
after=widget-packitafteryouhavepackedwidget  
anchor=NSEW(orsubset)-positionwidgetaccordingto  
givendirection  
before=widget-packitbeforeyouwillpackwidget  
expand=bool-expandwidgetifparentsizegrows  
fill=NONEorXorYorBOTH-fillwidgetifwidgetgrows  
in=master-usemastertocontainthiswidget  
ipadx=amount-addinternalpaddinginxdirection  
ipady=amount-addinternalpaddinginydirection  
padx=amount-addpaddinginxdirection  
pady=amount-addpaddinginydirection  
side=TOPorBOTTOMorLEFTorRIGHT-wheretoaddthiswidget. 

 pack_configure  (self, cnf  ={}  , kw) 
      Packawidgetintheparentwidget.Useasoptions:   
after=widget-packitafteryouhavepackedwidget  
anchor=NSEW(orsubset)-positionwidgetaccordingto  
givendirection  
before=widget-packitbeforeyouwillpackwidget  
expand=bool-expandwidgetifparentsizegrows  
fill=NONEorXorYorBOTH-fillwidgetifwidgetgrows  
in=master-usemastertocontainthiswidget  
ipadx=amount-addinternalpaddinginxdirection  
ipady=amount-addinternalpaddinginydirection  
padx=amount-addpaddinginxdirection  
pady=amount-addpaddinginydirection  
side=TOPorBOTTOMorLEFTorRIGHT-wheretoaddthiswidget. 

 pack_forget  (self) 
      Unmapthiswidgetanddonotuseitforthepackingorder. 

 pack_info  (self) 
      Returninformationaboutthepackingoptions   
forthiswidget. 

* * *

Methods inherited from * [Tkinter.Place](Tkinter.html) :  

 place  = place_configure(self, cnf  ={}  , kw) 
      Placeawidgetintheparentwidget.Useasoptions:   
in=master-masterrelativetowhichthewidgetisplaced.  
x=amount-locateanchorofthiswidgetatpositionxofmaster  
y=amount-locateanchorofthiswidgetatpositionyofmaster  
relx=amount-locateanchorofthiswidgetbetween0.0and1.0  
relativetowidthofmaster(1.0isrightedge)  
rely=amount-locateanchorofthiswidgetbetween0.0and1.0  
relativetoheightofmaster(1.0isbottomedge)  
anchor=NSEW(orsubset)-positionanchoraccordingtogivendirection  
width=amount-widthofthiswidgetinpixel  
height=amount-heightofthiswidgetinpixel  
relwidth=amount-widthofthiswidgetbetween0.0and1.0  
relativetowidthofmaster(1.0isthesamewidth  
asthemaster)  
relheight=amount-heightofthiswidgetbetween0.0and1.0  
relativetoheightofmaster(1.0isthesame  
heightasthemaster)  
bordermode="inside"or"outside"-whethertotakeborderwidthofmaster
widget  
intoaccount 

 place_configure  (self, cnf  ={}  , kw) 
      Placeawidgetintheparentwidget.Useasoptions:   
in=master-masterrelativetowhichthewidgetisplaced.  
x=amount-locateanchorofthiswidgetatpositionxofmaster  
y=amount-locateanchorofthiswidgetatpositionyofmaster  
relx=amount-locateanchorofthiswidgetbetween0.0and1.0  
relativetowidthofmaster(1.0isrightedge)  
rely=amount-locateanchorofthiswidgetbetween0.0and1.0  
relativetoheightofmaster(1.0isbottomedge)  
anchor=NSEW(orsubset)-positionanchoraccordingtogivendirection  
width=amount-widthofthiswidgetinpixel  
height=amount-heightofthiswidgetinpixel  
relwidth=amount-widthofthiswidgetbetween0.0and1.0  
relativetowidthofmaster(1.0isthesamewidth  
asthemaster)  
relheight=amount-heightofthiswidgetbetween0.0and1.0  
relativetoheightofmaster(1.0isthesame  
heightasthemaster)  
bordermode="inside"or"outside"-whethertotakeborderwidthofmaster
widget  
intoaccount 

 place_forget  (self) 
      Unmapthiswidget. 

 place_info  (self) 
      Returninformationabouttheplacingoptions   
forthiswidget. 

* * *

Methods inherited from * [Tkinter.Grid](Tkinter.html) :  

    grid  = grid_configure(self, cnf  ={}  , kw) 
          Positionawidgetintheparentwidgetinagrid.Useasoptions:   
    column=number-usecellidentifiedwithgivencolumn(startingwith0)  
    columnspan=number-thiswidgetwillspanseveralcolumns  
    in=master-usemastertocontainthiswidget  
    ipadx=amount-addinternalpaddinginxdirection  
    ipady=amount-addinternalpaddinginydirection  
    padx=amount-addpaddinginxdirection  
    pady=amount-addpaddinginydirection  
    row=number-usecellidentifiedwithgivenrow(startingwith0)  
    rowspan=number-thiswidgetwillspanseveralrows  
    sticky=NSEW-ifcellislargeronwhichsideswillthis  
    widgetsticktothecellboundary 
  
     grid_configure  (self, cnf  ={}  , kw) 
          Positionawidgetintheparentwidgetinagrid.Useasoptions:   
    column=number-usecellidentifiedwithgivencolumn(startingwith0)  
    columnspan=number-thiswidgetwillspanseveralcolumns  
    in=master-usemastertocontainthiswidget  
    ipadx=amount-addinternalpaddinginxdirection  
    ipady=amount-addinternalpaddinginydirection  
    padx=amount-addpaddinginxdirection  
    pady=amount-addpaddinginydirection  
    row=number-usecellidentifiedwithgivenrow(startingwith0)  
    rowspan=number-thiswidgetwillspanseveralrows  
    sticky=NSEW-ifcellislargeronwhichsideswillthis  
    widgetsticktothecellboundary 

     grid_forget  (self) 
          Unmapthiswidget. 
    
     grid_info  (self) 
          Returninformationabouttheoptions   
    forpositioningthiswidgetinagrid. 
    
     grid_remove  (self) 
          Unmapthiswidgetbutrememberthegridoptions. 
    
     location  = grid_location(self, x, y) 
          Returnatupleofcolumnandrowwhichidentifythecell   
    atwhichthepixelatpositionXandYinsidethemaster  
    widgetislocated. 

  
    class  create 
    #---------------------------------------------------------------------  
    #  
    #StartofPopupDialog  
    #  
    #---------------------------------------------------------------------------  
    #VCSPlotAnnotationDialogPopup  
    #---------------------------------------------------------------------------  


    Methods defined here:  
    
    __init__  (self, parent) 
    annotate_cancel  (self, parent) 
    annotate_clear  (self, parent) 
    annotate_replot  (self, parent) 
    annotate_reset  (self, parent) 
    evt_set_toggle_state  (self, parent, id) 
    execute  (self, parent, result) 
    get_settings  (self, parent) 
    hold_annotate_cancel_settings  (self, parent) 
    hold_annotate_original_settings  (self, parent) 
    master_switch  (self, parent, result) 
    retain_switch  (self, parent, result) 
  
###Functions 

    get_annotation_info  (parent, data_name  =None  ) 
    #---------------------------------------------------------------------   
    #Gettheannotationinfomationfromthedatavariable  
    #--------------------------------------------------------------------------- 

  
### Data 

    Pmw  = <Pmw.Pmw_1_2.lib.PmwLoader.PmwLoader instance>
