---
layout: default
title:
---

#  Python: module browser.gui_functions

#ThePCMDIDataBrowserMiscellaneousFunctions-gui_functionsmodule  
##############################################################################
#Module:gui_functionsmodule
#Copyright:"SeefileLegal.htmforcopyrightinformation."
#Authors:PCMDISoftwareTeam
#LawrenceLivermoreNationalLaboratory:
#support@pcmdi.llnl.gov
#Description:PCMDISoftwareSystemBrowsermiscellaneousGUIfunctions.
#Version:4.0
##############################################################################
#---------------------------------------------------------------------  
#NOTE:needtouseversionofPythonthatimportsTkinterandPmw  
#--------------------------------------------------------------------- 
  
Modules 
* [Numeric](Numeric.html)  
* [Tkinter](Tkinter.html)  
* [__main__](__main__.html)  
* [cdms](cdms.html)  
* [cdtime](cdtime.html)  
* [copy](copy.html)  
* [copy_reg](copy_reg.html)  
* [gui_support.gui_color](gui_support.gui_color.html)  
* [browser.gui_control](browser.gui_control.html)  
* [browser.gui_defined_variables](browser.gui_defined_variables.html)  
* [browser.gui_message](browser.gui_message.html)  
* [browser.gui_reset](browser.gui_reset.html)  
* [math](math.html)  
* [multiarray](multiarray.html)  
* [os](os.html)  
* [vcs.pagegui](vcs.pagegui.html)  
* [pickle](pickle.html)  
* [string](string.html)  
* [sys](sys.html)  
* [types](types.html)  
* [vcs](vcs.html)  

Classes 
* [generate_labels_list](browser.gui_functions.html)
* [replace_axis_values](browser.gui_functions.html)
  
class  generate_labels_list 

Methods defined here:  

    __init__  (self, parent, dim_index, axis) 
    generatelist  (self, button) 
  
class  replace_axis_values 

Methods defined here:  

    __init__  (self, parent, dim_index, replace_type  =None  ) 

Functions 

    arange  (...) 
    * [arange]() (start,stop=None,step=1,typecode=None)   
  
    Justlikerange()exceptitreturnsanarraywhosetypecanbe  
    specifiedbythekeywordargumenttypecode. 

    array  (...) 
    * [array]() (sequence,typecode=None,copy=1,savespace=0)willreturnanewarrayformedfromthegiven(potentiallynested)sequencewithtypegivenbytypecode.Ifnotypecodeisgiven,thenthetypewillbedeterminedastheminimumtyperequiredtoholdtheobjectsinsequence.Ifcopyiszeroandsequenceisalreadyanarray,areferencewillbereturned.Ifsavespaceisnonzero,thenewarraywillmaintainitsprecisioninoperations. 

    arrayrange  = arange(...) 
    * [arange]() (start,stop=None,step=1,typecode=None)   
  
    Justlikerange()exceptitreturnsanarraywhosetypecanbe  
    specifiedbythekeywordargumenttypecode. 

    choose  (...) 
    * [choose]() (a,(b1,b2,...)) 

    cross_correlate  (...) 
    * [cross_correlate]() (a,v,mode=0) 

    evt_menu_index  (parent, dim_index, called_from) 
    
    evt_menu_raw  (parent, dim_index) 
    
    evt_transpose_dimensions  (index, dim_name, t_index, t_dim_name, parent) 
    #-----------------------------------------------------------------------------------   
    #Transposetwodimensions  
    #----------------------------------------------------------------------------------- 
    
    fromstring  (...) 
    * [fromstring]() (string,typecode='l',count=-1)returnsanew1darrayinitializedfromtherawbinarydatainstring.Ifcountispositive,thenewarraywillhavecountelements,otherwiseit'ssizeisdeterminedbythesizeofstring. 

    get_available_printers  () 
    #------------------------------------------------------------------------   
    #Returnthelistofavailableprinters.Printernamesshouldbelocated  
    #intheuser's$HOME/PCMDI_GRAPHICS/HARD_COPYfile  
    #------------------------------------------------------------------------ 

    get_axis_values  (parent, dim_index) 
    get_axis_weight_values  (parent, dim_index) 
    get_dimension_selections  (Csrl, Cpts) 
    
    #-----------------------------------------------------------------------------------   
    #Selectthefirstandlastdimensionvalues\--Willalsohighlightthe dimension's  
    #newrange  
    #----------------------------------------------------------------------------------- 

    reshape  (...) 
    * [reshape]() (a,(d1,d2,...,dn)).Changetheshapeofatobeann-dimensionalarraywithdimensionsgivenbyd1...dn.Note:thesizespecifiedforthenewarraymustbeexactlyequaltothesizeoftheoldoneoranerrorwilloccur. 
    
    return_axis_size  (parent, dim_index) 
    return_latitude_region_values  (region) 
    return_longitude_region_values  (region) 
    searchsorted  = binarysearch(...) 
    binarysearch(a,v) 
    set_lat_lon  (parent, R0, R1) 
    
    set_region_index_values  (parent, dim_name, region, dim_index) 
    take  (...) 
    * [take]() (a,indices,axis=0).Selectstheelementsinindicesfromarrayaalongthegivenaxis. 
    zeros  (...) 
    * [zeros]() ((d1,...,dn),typecode='l',savespace=0)willreturnanewarrayofshape(d1,...,dn)andtypetypecodewithallit'sentriesinitializedtozero.Ifsavespaceisnonzerothearraywillbeaspacesaverarray. 
      
###Data 

    Character  = 'c'   
    Complex  = 'D'   
    Complex0  = 'F'   
    Complex16  = 'F'   
    Complex32  = 'F'   
    Complex64  = 'D'   
    Complex8  = 'F'   
    Float  = 'd'   
    Float0  = 'f'   
    Float16  = 'f'   
    Float32  = 'f'   
    Float64  = 'd'   
    Float8  = 'f'   
    Int  = 'l'   
    Int0  = '1'   
    Int16  = 's'   
    Int32  = 'i'   
    Int8  = '1'   
    LittleEndian  = True   
    NewAxis  = None   
    Pmw  = <Pmw.Pmw_1_2.lib.PmwLoader.PmwLoader instance>   
    PyObject  = 'O'   
    UInt  = 'u'   
    UInt16  = 'w'   
    UInt32  = 'u'   
    UInt8  = 'b'   
    UnsignedInt16  = 'w'   
    UnsignedInt32  = 'u'   
    UnsignedInt8  = 'b'   
    UnsignedInteger  = 'u'   
    absolute  = <ufunc 'absolute'>   
    add  = <ufunc 'add'>   
    arccos  = <ufunc 'arccos'>   
    arccosh  = <ufunc 'arccosh'>   
    arcsin  = <ufunc 'arcsin'>   
    arcsinh  = <ufunc 'arcsinh'>   
    arctan  = <ufunc 'arctan'>   
    arctan2  = <ufunc 'arctan2'>   
    arctanh  = <ufunc 'arctanh'>   
    bitwise_and  = <ufunc 'bitwise_and'>   
    bitwise_or  = <ufunc 'bitwise_or'>   
    bitwise_xor  = <ufunc 'bitwise_xor'>   
    ceil  = <ufunc 'ceil'>   
    conjugate  = <ufunc 'conjugate'>   
    cos  = <ufunc 'cos'>   
    cosh  = <ufunc 'cosh'>   
    divide  = <ufunc 'divide'>   
    divide_safe  = <ufunc 'divide_safe'>   
    e  = 2.7182818284590451   
    equal  = <ufunc 'equal'>   
    exp  = <ufunc 'exp'>   
    fabs  = <ufunc 'fabs'>   
    floor  = <ufunc 'floor'>   
    floor_divide  = <ufunc 'floor_divide'>   
    fmod  = <ufunc 'fmod'>   
    greater  = <ufunc 'greater'>   
    greater_equal  = <ufunc 'greater_equal'>   
    hypot  = <ufunc 'hypot'>   
    invert  = <ufunc 'invert'>   
    left_shift  = <ufunc 'left_shift'>   
    less  = <ufunc 'less'>   
    less_equal  = <ufunc 'less_equal'>   
    log  = <ufunc 'log'>   
    log10  = <ufunc 'log10'>   
    logical_and  = <ufunc 'logical_and'>   
    logical_not  = <ufunc 'logical_not'>   
    logical_or  = <ufunc 'logical_or'>   
    logical_xor  = <ufunc 'logical_xor'>   
    maximum  = <ufunc 'maximum'>   
    minimum  = <ufunc 'minimum'>   
    multiply  = <ufunc 'multiply'>   
    negative  = <ufunc 'negative'>   
    not_equal  = <ufunc 'not_equal'>   
    pi  = 3.1415926535897931   
    power  = <ufunc 'power'>   
    remainder  = <ufunc 'remainder'>   
    right_shift  = <ufunc 'right_shift'>   
    sin  = <ufunc 'sin'>   
    sinh  = <ufunc 'sinh'>   
    sqrt  = <ufunc 'sqrt'>   
    subtract  = <ufunc 'subtract'>   
    tan  = <ufunc 'tan'>   
    tanh  = <ufunc 'tanh'>   
    true_divide  = <ufunc 'true_divide'>   
    typecodes  = {'Character': 'c', 'Complex': 'FD', 'Float': 'fd', 'Integer': '1sil', 'UnsignedInteger': 'bwu'} 
