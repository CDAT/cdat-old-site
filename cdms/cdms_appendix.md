---
layout: default
title: CDAT CDMS Appendix
---

<a name="a"></a>

## APPENDIX A

### CDMS Classes

Figure 1, "CDMS Classes", on page 175 illustrates the class inheritance structure of CDMS. The classes may be categorized as abstract or concrete. Only concrete classes are meant to be used directly. In contrast an abstract class defines the common interface of its subclasses. For example, the class AbstractAxis2D defines the common interface for two-dimensional coordinate axes. It has concrete subclasses DatasetAxis2D, FileAxis2D, and TransientAxis2D, which are used in applications. Abstract classes are denoted in italics.

For many abstract classes there are three 'flavors' of subclass: dataset, file, and transient. Dataset-related objects are thought of as being contained in datasets in the sense that operations on those objects result in I/O operations on the corresponding dataset. The same is true of file-related objects. Objects in datasets and files are examples of persistent objects, whose state persists after the application exits. On the other hand, transient objects live in memory and are not persistent.

In general the concrete subclasses closely mirror the interface of the abstract parent class. For this reason this document defines the interfaces of the abstract classes, and only discusses a concrete class in the few cases where the interface has been extended. This allows applications to treat the behavior of, say a dataset axis and file axis, as identical.

<a name="fig_1"></a>

![]({{site.baseurl}}/media/images/cdms_classes.jpg)

###### FIGURE 1. CDMS Classes

<a name="b"></a>

## APPENDIX B

### Version Notes

<a name="b.1"></a>

#### B.1 Version 4.0

CDMS version 4.0 adds support for nonrectangular grids:

 - The following grid classes were added: AbstractHorizontalGrid, AbstractCurve-Grid, AbstractGenericGrid, DatasetCurveGrid, FileCurveGrid, TransientCurve-Grid, DatasetGenericGrid, FileGenericGrid, and TransientGenericGrid.
 - The following axis classes were added: AbstractCoordinateAxis, AbstractAuxAxis1D, AbstractAxis2D, DatasetAuxAxis1D, FileAuxAxis1D, TransientAuxAxis1D, DatasetAxis2D, FileAxis2D, and TransientAxis2D.
 - The getMesh and clone methods were added for grids.
 - An interface to the SCRIP package was added.

<a name="b.2"></a>

#### B.2 Version 3.0 Overview

CDMS version 3.0 is a significant enhancement of previous versions. The major changes were:

 - CDAT/CDMS was integrated with the Numerical Python masked array class MA.MaskedVariable. The MV submodule was added as a wrapper around MA.
 - Methods that read data, such as subRegion, subSlice, and the slice operations, return instances of class TransientVariable. The plot and regrid modules were modified to handle masked array input. The specifiers time=..., latitude=..., etc. were added to the I/O routines.
 - The class TransientVariable was added.
 - A number of new functions were added, notably subRegion and subSlice, which return instances of TransientVariable.
 - When a masked array is returned from a method, it is "squeezed": singleton dimensions are removed. In contrast, transient variables are not squeezed. I/O functions have a squeeze option. The method setAutoReshapeMode was removed.
 - Internal attributes are handled in the InternalAttributes class. This allows CDMS classes to be subclassed more readily.
 - The class Variable was renamed DatasetVariable.
 - The cu module was emulated in cdms. cu and cdms methods can be mixed.
 - The code was modularized, so that Python, CDMS, and Numerical Python can be built and installed separately. This significantly enhances the portability of the code.

<a name="b.3"></a>

#### B.3 V3.0 Details

<a name="b.3.1"></a>

##### B.3.1 AbstractVariable

 - Functions getDomain, getSlice, rank, regrid, setMissing, size, subRegion, and subSlice were added.
 - The functions getRegion, getSlice, getValue, and the slice operators all return an instance of MA, a masked array. Singleton dimensions are squeezed.
 - The functions subRegion and subSlice return an instance of TransientVariable. Singleton dimensions are not squeezed.
 - The xxSlice and xxRegion functions have keywords time, level, latitude, and longitude.
 - The input functions have the keyword squeeze.
 - AbstractVariable inherits from class Slab. The following functions previously available in module cu are Slab methods: getattribute, setattribute, listdimattributes, getdimattribute, listall, and info.
 - AbstractVariable implements arithmetic functions, astype.
 - The write function was added.

<a name="b.3.2"></a>

##### B.3.2 AbstractAxis

 - The functions asComponentTime, asRelativeTime, clone, getAxisIds, getAxis-Index, getAxisList, getAxisListIndex, mapIntervalExt were added.
 - subaxis was renamed subAxis for consistency.
 - Generalized wraparound was implemented, to handle multiple cycles, reversing, and negative strides. By default, coordinate intervals are closed. The intersection options 'n','e','b',and 's' were added to the interval indicator - see mapIntervalExt.

<a name="b.3.3"></a>

##### B.3.3 AbstractDatabase

 - The function open is synonymous with openDataset.

<a name="b.3.4"></a>

##### B.3.4 Dataset

 - The function open is synonymous with openDataset.

<a name="b.3.5"></a>

##### B.3.5 cdms module

 - The functions asVariable, isVariable, and createVariable were added.
 - The function setAutoReshapeMode was removed. It is replaced by the squeeze option for all I/O functions.

##### B.3.6 CdmsFile

 - The function createVariable has a keyword fill_value. The datatype may be a Numeric/MA typecode.
 - The function write was added.

##### B.3.7 CDMSError

 - All errors are an instance of the class CDMSError.

##### B.3.8 AbstractRectGrid

 - The function createGaussianGrid was added.

##### B.3.9 InternalAttributes

 - The class InternalAttributes was added. It has methods add_internal_attribute, is_internal_attribute, and replace_external_attributes.

##### B.3.10 TransientVariable

 - The class TransientVariable was added. It inherits from both AbstractVariable and MA.
 - The cdms module function createVariable returns a transient variable.
 - This class does not implement the functions getPaths or getTemplate.

##### B.3.11 MV

 - The MV submodule of cdms was added.

<a name="c"></a>

## APPENDIX C

### `cu` Module

The `cu` module is the original CDAT I/O interface. As of version 3 it is emulated in the `cdms` module. It is maintained for backward compatibility.

The `cu` classes are `Slab`, corresponding to `TransientVariable` in CDMS, and `cuDataset`, corresponding to `Dataset` in CDMS.

### C.1 Slab

###### Table C.1 Slab Methods

{:.table}
|Type |Method|Definition|
|---|---|---|
|Various|`getattribute(name)`|Get the value of an attribute. `name` is the string name of the attribute. The following special names can always be used: 'filename', 'comments', 'grid_name', 'grid_type', 'time_statistic', 'long_name', 'units'.|
|Various|`getdimattribute(dim, field)`|Get the value of a dimension attribute. `dim` is the dimension number, an integer in the range 0..rank-1. `field` is a string, one of: "name", "values", "length", "units", "weights", "bounds".|
|None|`info(flag=None, device=sys.stdout)`|Print slab information. If `flag` is nonzero, dimension values, weights, and bounds are also printed. Output is sent to `device`.|
|List|`listall(all=None)`|Print slab information. If `all` is nonzero, dimension values, weights, and bounds are also printed.|
|List|`listdimattributes(dim, field)`|List dimension attributes. Returns a list of string attribute names which can be input to `getdimattribute`. `dim` is the dimension number, an integer in the range 0..rank-1. `field` is a string, one of: "name", "values", "length", "units", "weights", "bounds".|
|None|`setattribute(name, value)`|Set an attribute. `name` is the string name of the attribute. `value` is the value of the attribute|


### C.2 `cuDataset`


<a name="table_c.2"></a>

###### Table C.2 cuDataset Methods

<table class="table">
<tr>
<th>Type</th>
<th>Method</th>
<th>Definition</th>
</tr>
<tr>
<td>None</td>
<td><code>cleardefault()</code></td>
<td>Clear the default variable name.</td>
</tr>
<tr>
<td>None</td>
<td><code>default_variable(vname )</code></td>
<td><p>Set the default variable name.</p><p><code>vname</code> is the string variable name.</p></td>
</tr>
<tr>
<td>Array</td>
<td><code>dimensionarray(dname, vname=None)</code></td>
<td><p>Values of the axis named dname.</p> <p> <code>dname</code> is the string axis name.</p> <p> <code>vname</code> is the string variable name. The default is the variable name set by <code>default_variable</code>.</p></td>
</tr>
<tr>
<td>Axis</td>
<td><code>dimensionobject(dname, vname=None)</code></td>
<td>Get an axis. <code>dname</code> is the string name of an axis. <code>vname</code> is a string variable name. The default is the variable name set by <code>default_variable</code>.</td>
</tr>
<tr>
<td>Various</td>
<td><code>getattribute (vname, attribute)</code></td>
<td>Get an attribute value. <code>vname</code> is a string variable name. <code>attribute</code> is the string attribute name.</td>
</tr>
<tr>
<td>String</td>
<td><code>getdimensionunits (dname,vname=None)</code></td>
<td><p>Get the units for the given dimension.</p> <p><code>dname</code> is the string name of an axis.</p><p> <code>vname</code>is a string variable name. The default is the variable name set by <code>default_variable</code>.</p></td>
</tr>
<tr>
<td>Various</td>
<td><code>getglobal (attribute)</code></td>
<td>Get the value of the global attribute. <code>attribute</code> is the string attribute name.</td>
</tr>
<tr>
<td>Variable</td>
<td><code>getslab (vname, *args)</code></td>
<td><p>Read data for a variable.</p> <p><code>vname</code> is the string name of the variable.</p> <p>args is an argument list corresponding to the dimensions of the variable. Arguments for each dimension can be:</p> <ol> <li>":" or None -- select the entire dimension</li> <li>Ellipsis -- select entire dimensions between the ones given.</li> <li>a pair of successive arguments giving an interval in world coordinates.</li> <li>a CDMS-style tuple of world coordinates e.g. (start, stop, 'cc')</li> </ol></td>
</tr>
<tr>
<td>List</td>
<td><code>listall (vname=None, all=None)</code></td>
<td><p>Get info about data from the file.</p> <p><code>vname</code> is the string name of the variable.</p><p> If <code>all</code> is non-zero, dimension values, weights, and bounds are returned as well</p></td>
</tr>
<tr>
<td>List</td>
<td><code>listattribute (vname=None )</code></td>
<td>Return a list of attribute names. <code>vname</code> is the name of the variable. The default is the variable name set by <code>default_variable</code>.</td>
</tr>
<tr>
<td>List</td>
<td><code>listdimension (vname=None)</code></td>
<td>Return a list of the dimension names associated with a variable. <code>vname</code> is the name of the variable. The default is the variable name set by <code>default_variable</code>.</td>
</tr>
<tr>
<td>List</td>
<td><code>listglobal ()</code></td>
<td>Return a list of the global attribute names.</td>
</tr>
<tr>
<td>List</td>
<td><code>listvariable ()</code></td>
<td>Return a list of the variables in the file.</td>
</tr>
<tr>
<td>None</td>
<td><code>showall (vname=None, all=None, device=sys.stdout)</code></td>
<td>Print a description of the variable. <code>vname</code> is the string name of the variable. If <code>all</code> is non-zero, dimension values, weights, and bounds are returned as well. Output is sent to <code>device</code>.</td>
</tr>
<tr>
<td>None</td>
<td><code>showattribute (vname=None, device=sys.stdout)</code></td>
<td>Print the attributes of a variable. <code>vname</code> is the string name of the variable. Output is sent to <code>device</code>.</td>
</tr>
<tr>
<td>None</td>
<td><code>showdimension (vname=None, device=sys.stdout)</code></td>
<td>Print the dimension names associated with a variable. <code>vname</code> is the string name of the variable. Output is sent to <code>device</code>.</td>
</tr>
<tr>
<td>None</td>
<td><code>showglobal (device=sys.stdout )</code></td>
<td>Print the global file attributes. Output is sent to <code>device</code>.</td>
</tr>
<tr>
<td>None</td>
<td><code>showvariable (device=sys.stdout )</code></td>
<td>Print the list of variables in the file.</td>
</tr>
</table>
