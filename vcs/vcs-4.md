---
layout: default
title: VCS Chapter 4
---

##  CHAPTER 4 Overview

####

![](vcs-2.gif)

VCS Model Overview

The VCS model is defined by a trio of named attribute sets, designated the
"Primary Objects" (also known as "Primary Elements"). These include: the data,
which specifies what is to be displayed and are obtained from the "cdms",
"cu", or Numeric modules; the graphics method, which specifies the display
technique; and the picture template, which determines the appearance of each
segment of the display.

####

![](vcs-2.gif)

VCS Primary Objects (or Primary Elements)

A description of each primary object is warranted before showing their use and
usefulness in VCS. See descriptions below.

######  Graphics Method Objects

A graphics method simply defines how data is to be displayed on the screen.
Currently, there are eleven different graphics methods with more on the way.
Each graphics method has its own unique set of attributes (or members) and
functions. They also have a set of core attributes that are common in all
graphics methods. The descriptions of the current set of graphics methods are
as follows:

  * boxfillobject - The boxfill graphics method draws color grid cells to represent the data on the VCS Canvas. Its class symbol or alias is "Gfb".
  * continentsobject - The continents graphics method draws a predefined, generic set of continental outlines in a longitude by latitude space. To draw continental outlines, no external data set is required. Its class symbol or alias is "Gcon".
  * isofillobject - The isofill graphics method fills the area between selected isolevels (levels of constant value) of a two-dimensional array with a user-specified color. Its class symbol or alias is "Gfi".
  * isolineobject - The isoline graphics method draws lines of constant value at specified levels in order to graphically represent a two-dimensional array. It also labels the values of these isolines on the VCS Canvas. Its class symbol or alias is "Gi".
  * outfillobject - The outfill graphics method fills a set of integer values in any data array. Its primary purpose is to display continents by filling their area as defined by a surface type array that indicates land, ocean, and sea-ice points. Its class symbol or alias is "Gfo".
  * outlineobject - The Outline graphics method outlines a set of integer values in any data array. Its primary purpose is to display continental outlines as defined by a surface type array that indicates land, ocean, and sea-ice points. Its class symbol or alias is "Go".
  * scatterobject - The scatter graphics method displays a scatter plot of two 4-dimensional data arrays, e.g. A(x,y,z,t) and B(x,y,z,t). Its class symbol or alias is "GSp".
  * vectorobject - The Vector graphics method displays a vector plot of a 2D vector field. Vectors are located at the coordinate locations and point in the direction of the data vector field. Vector magnitudes are the product of data vector field lengths and a scaling factor. Its class symbol or alias is "Gv".
  * xvsyobject - The XvsY graphics method displays a line plot from two 1D data arrays, that is X(t) and Y(t), where `t' represents the 1D coordinate values. Its class symbol or alias is "GXY".
  * xyvsyobject - The Xyvsy graphics method displays a line plot from a 1D data array, i.e. a plot of X(y) where `y' represents the 1D coordinate values. Its class symbol or alias is "GXy".
  * Yxvsxobject - The Yxvsx graphics method displays a line plot from a 1D data array, i.e. a plot of Y(x) where `x' represents the 1D coordinate values. Its class symbol or alias is "GYx".
  * 3dscalarobject - The 3dscalar graphics method displays an interactive 3D plot of a 4-dimensional (x,y,z,t) data array. Its class symbol or alias is "3d_scalar".
  * 3dvectorobject - The 3dvector graphics method displays an interactive 3D plot of a 4-dimensional (x,y,z,t) vector field. Its class symbol or alias is "3d_vector".

######  Picture Template Object

A picture template determines the location of each picture segment, the space
to be allocated to it, and related properties relevant to its display. The
description of the picture template is as follows:

  * templateobject - Picture Template attributes describe where and how segments of a picture will be displayed. The segments are graphical representations of: textual identification of the data formatted values of single-valued dimensions and mean, maximum, and minimum data values axes, tick marks, labels, boxes, lines, and a legend that is graphics-method specific the data. Picture templates describe where to display all segments including the data. Its class symbol or alias is "P".

######  Data Objects

Array data attribute sets and their associated dimensions are to be modified
outside of VCS. See the CDMS, CU, and Numeric module documentation for data
extraction, creation and manipulation.

####

![](vcs-2.gif)

VCS Secondary Objects (or Secondary Elements)

A description of each secondary object is warranted before showing their use
and usefulness in VCS. It is these secondary objects that defines the detailed
specification of the primary objects' attributes. Currently, there are five
secondary objects with more to follow.

######  Colormap Object

The colormap object is used to specify, create, and modify colormaps. There
are 256 colors and color indices, but only the first 240 color indices can be
modified (indices 240 through 255 are reserved for VCS internal use). The
description of the colormap object is as follows:

  * colormapobject - A colormap contains 240 user-definable colors that are used for graphical displays. The color mixtures are defined in terms of percentages of red, green, and blue colors (0 to 100% for each). The resulting color depends on the specified mixtures of red, green, and blue. Its class symbol or alias is "Cp".

Note: VCS colormaps are objects, but they are not referenced like other
secondary objects.

######  Fillarea Object

The fillarea objects allows the user to edit fillarea attributes, including
fillarea interior style, style index, and color index. The description of the
fillarea object is as follows:

  * fillareaobject - The fill area attributes are used to display regions defined by closed polygons, which can be filled with a uniform color, a pattern, or a hatch style. Attributes specify the style, color, position, and dimensions of the fill area. Its class symbol or alias is "Tf".

######  Line Object

The line object allows the editing of line type, width, and color index. The
description of the line object is as follows:

  * lineobject - The line attributes specify the type, width, and color of the line to be drawn for a graphical display. Its class symbol or alias is "Tl".

######  Marker Object

The marker object allows the editing of the marker type, width, and color
index. The description of the marker object is as follows:

  * markerobject - The marker attribute specifies graphical symbols, symbol sizes, and colors used in appropriate graphics methods. Its class symbol or alias is "Tm".

######  Text Objects

Graphical displays often contain textual inscriptions, which provide further
information. The text-table object attributes allow the generation of
character strings on the VCS Canvas by defining the character font, precision,
expansion, spacing, and color. The text-orientation object attributes allow
the appearance of text character strings to be changed by defining the
character height, up-angle, path, and horizontal and vertical alignment. The
text-combined object is a combination of both text-table and text-orientation
objects. The description of the text objects are as follows:

  * textcombinedobject - The text-combined attributes combine the text-table attributes and a text-orientation attributes together. From combining the two classes, the user is able to set attributes for both classes at once (i.e., define the font, spacing, expansion, color index, height, angle, path, vertical alignment, and horizontal alignment). Its class symbol or alias is "Tc".
  * textorientationobject - The text-orientation attributes set names that define the height, angel, path, horizontal alignment and vertical alignment. Its class symbol or alias is "To".
  * texttableobject - The text-table attributes set names that define the font, spacing, expansion, and color index. Its class symbol or alias is "Tt".

####

![](vcs-2.gif)

Initializing VCS

######  Importing VCS

In Python, before one can start using a module they must first load it. To
load the VCS module, like all other Python modules, either type:

"from vcs import *"; or

"import vcs"

If you use "import vcs", then you must prepend "vcs" to certain calls (e.g.,
"vcs.help()"). If you use "from vcs import *", then you must be aware of
possible name clashes. That is, if two packages are imported using the form
"from name import *" and both have a "help" function, then Python doesn't know
which "help" function to call. For such cases, and indeed as an unspoken rule,
it is best to use "import name" to avoid name clashing between packages.

######  VCS Initialize

To construct a VCS Canvas object type the following:

a=vcs.init()

There can only be at most 8 VCS Canvas objects initialized at any given time.
When a VCS Canvas object is initialized, the current template and graphics
method will be displayed. For example:

"`Template' is currently set to P_default.

Graphics method 'Boxfill' is currently set to Gfb_default.'"

####

![](vcs-2.gif)

VCS Functions

######  Plotting in VCS

There are several different ways to display data on the VCS Canvas. The most
basic way is to use the plot() function. The simple plot() function command:
plot(array1,[array2], [template object], [graphics_method object]). The
examples below are showing how to plot a simple array using default values for
everything else.

######  Plotting a CDMS Persistent Array

import vcs # import the VCS module

import cdms # import CDMS for ingesting data

cdms.setAutoReshapeMode(`on') # needed by CDMS module if

# data is reshaped

f=cdms.openDataset(`example.nc') # open file via the cdms module

psl=f.variables[`clt'] # get the "psl" variable

data=psl[...] # get the "psl" variable data (Note, data is

# now a Numeric array)

v=vcs.init() # "v" is an instance of the VCS class

# object (constructor)

v.plot(data, variable=psl) # call "plot" function to display the CDMS

# Persistent Array on the VCS Canvas

# using default settings

######  Plotting a CU Slab Array

import vcs # import the VCS module

import cu # import CU for ingesting data

f=cu.open(`example.nc') # open file via the cu module

s=f.getslab(`clt') # get the "psl" variable slab

v=vcs.init() # "v" is an instance of the VCS

# class object (constructor)

v.plot(s) # call "plot" function to display the CU "slab"

# array on the VCS Canvas using default settings

######  Plotting a Numeric Array

import vcs # import the VCS module

import Numeric # import Numeric for generating data

a=Numeric.array([[1,2,3],[4,5,6],[7,8,9]]) # create a simple

# multidimensional array

v=vcs.init() # "v" is an instance of the VCS

# class object (constructor)

v.plot(a) # call "plot" function to display the Numeric

# "array" data on the VCS Canvas using

# default settings



######  Plotting Using Keyword Arguments

The plot function has many overriding keyword arguments that control textural
and graphical output of the display. As shown above, the arguments necessary
to plot data can be very simple. Below is a more complex plot() function
showing the uses of array objects, template object, graphics method object,
and key word arguments. Objects placed in brackets "[ ]" indicate optional
entries into the plot function:

plot(array1, [array2 [, template [, graphics method [,key=value [, key=value
[, ...]]]]]]),

where array1 and array2 are Numeric arrays or CU slabs; template represents a
template object; graphics method represents a graphics method object (such as,
boxfill or isofill); and key=value represents one variable attributes used to
display textual information or to modify the plot's output. If no template is
specified, then the default template will be used. If no graphics method is
specified, then the default boxfill graphics method is used.

Variable attribute keys are:

comment1 = string # Comment plotted above file_comment

comment2 = string # Comment plotted above comment1

comment3 = string # Comment plotted above comment2

comment4 = string # Comment plotted above comment3

file_comment = string # Comment (defaults to file.comment)

hms = string (hh:mm:ss) # Hour, minute, second

long_name = string # Descriptive variable name

missing_value= (same type as array) # Missing data value

#(defaults to var.getMissing())

name = string # Variable name (defaults to var.id)

time = cdtime # instance (relative or absolute),

# cdtime, reltime or abstime value

units = string # Variable units

ymd = string (yy/mm/dd) # Year, month, day



Dimension attribute keys (dimension length=n) are:

[x|y|z|t|w]array1 = NumPy array of length n # x or y Dimension values

[x|y|z|t|w]array2 = NumPy array of length n # x or y Dimension



values:

[x|y]bounds = NumPy array of shape (n,2) # x or y Dimension



boundaries:

[x|y|z|t|w]name = string # x or y Dimension name

[x|y|z|t|w]units = string # x or y Dimension units

[x|y]weights = NumPy array of length n # x or y Dimension

# weights (used # to

# calculate area-weighted

# mean)



CDMS object attributes are:

[x|y|z|t|w]axis = CDMS axis object # x or y Axis

grid = CDMS grid object # Grid object (e.g.

# grid=var.getGrid()

variable = CDMS variable object # Variable object



Miscellaneous attributes are:

[x|y]rev = 0|1 # if ==1, reverse the direction of

# the x or y axis

continents = 0,1,2,3,4,5,6,7,8,9,10,11 # if >=1, plot continental

# outlines (default: plot if x-axis is

# longitude, y-axis is latitude -or-

# xname is 'longitude' and yname is

# 'latitude'

# The continents-type values are integers

# ranging from 0 to 11, where:

# 0 signifies "No Continents"

# 1 signifies "Fine Continents"

# 2 signifies "Coarse Continents"

# 3 signifies "United States"

# 4 signifies "Political Borders"

# 5 signifies "Rivers"



# Values 6 through 11 signify the line

# type defined by the files

# data_continent_other7

# through data_continent_other12.



Graphics Output in Background Mode:

bg = 0|1 # if==1, create images in the

# background (Don't display the

# VCS Canvas)

Note: More specific attributes take precedence over general attributes. In
particular, specific attributes override variable object attributes; dimension
attributes and arrays override axis objects, which override grid objects,
which override variable objects.

For example, if both 'file_comment' and 'variable' keywords are specified, the
value of 'file_comment' is used instead of the file comment in the parent of
variable. Similarly, if both 'xaxis' and 'grid' keywords are specified, the
value of 'xaxis' takes precedence over the x-axis of grid.

######  Example Plotting Using Keyword Arguments:

When using the plot() function, keep in mind that all keyword arguments must
be last. Note that the order of the objects is not restrictive, just as long
as they are before any keyword argument. See the two plot() function examples
below.

import vcs # import the VCS module

import cu # import CU for ingesting data

f=cu.open(`example.nc') # open file via the cu module

s=f.getslab(`psl') # get the "psl" variable slab

v=vcs.init() # "v" is an instance of the VCS

# class object (constructor)

t=x.createtemplate('new') # create a new template from the default

# template

iso=x.createisofill(`new') # create a new isofill graphics method from

# the default isofill

x.plot(s, t, iso, continents=0) # call "plot" function to display the CU

# slab "s" using

# newly created template "t" and isofill

# graphics method "iso" and turn

# continents off

x.clear() # clear the VCS Canvas of all plots

x.plot(t,iso,s,continents=0) # shows that the order of the objects are
irrelevant, but

# not that all keyword arguments must be last.

######  Other Plotting functions in VCS

There are other ways to plot data in VCS. These additional plotting routines
utilizes the same parameter format as the plot() function. What makes these
plotting functions unique are their direct association with the graphics
methods. That is, each graphics method has its own plot function. For example,
if the user wishes to plot data using the isofill graphics method, then the
function isofill() can be used instead of the plot() function. If the isofill
object is not specified then the default isofill graphics method will be used.
The user can also pass down the name of the graphics method to be used. In
some ways, the graphics method plot functions can be thought of as short cuts
to plotting data.

Note, if a different graphics method object is specified and passed down to
one of these alternate plot functions, then the alternate plot function will
behave as the plot() function and plot the data in the specified graphics
method format.

See table below for additional plot functions.

######  

Plot Function

Description

boxfill()

plot data using the boxfill graphics method

continents()

plot to the screen continental graphics method

isofill()

plot data using the isofill graphics method

isoline()

plot data using the isoline graphics method

outfill()

plot data using the outfill graphics method

outline()

plot data using the outline graphics method

scatter()

plot data using the scatter graphics method

vector()

plot data using the vector graphics method

xvsy()

plot data using the xvsy graphics method

xyvsy()

plot data using the xyvsy graphics method

yxvsy()

plot data using the yxvsy graphics method

######  Checking VCS Objects

In some cases, there my be a need to check or verify an object in VCS. For
these cases, you may want to use the query functions below.

Check for VCS graphics method objects:

######  

Query Function

Description

isboxfill()

verifies a boxfill graphics method object

iscontinents()

verifies a continents graphics method object

isisofill()

verifies an isofill graphics method object

isisoline()

verifies an isoline graphics method object

isoutfill()

verifies an outfill graphics method object

isoutline()

verifies an outline graphics method object

isscatter()

verifies a scatter graphics method object

isvector()

verifies a vector graphics method object

isxvsy()

verifies a xvsy graphics method object

isxyvsy()

verifies a xyvsy graphics method object

isyxvsx()

verifies a yxvsx graphics method object

is3d_scalar()

verifies a 3d_scalar graphics method object

is3d_vector()

verifies a 3d_vector graphics method object

isgraphicsmethod()

verifies if an object is one of the graphics methods: boxfill, isofill,
isoline, outfill, outline, continents, scatter, vector, xvsy, xyvsy, or yxvsx.

graphicsmethodname()

Returns the name of the graphics methods object. Returns either: `boxfill',
`isofill', `isoline', `outfill', `outline', `continents', `scatter', `vector', '3d_vector', '3d_scalar'
`xvsy', `xyvsy', or `yxvsx'.

Check for VCS secondary objects:

######  

Query Function

Description

isfillarea()

verifies a fillarea secondary object

isline()

verifies a line secondary object

ismarker()

verifies a marker secondary object

istextcombined()

verifies a text-combined secondary object

istextorientation()

verifies a text-orientation secondary object

istexttable()

verifies a text-table secondary object

issecondaryobject()

verifies if an object is one of the secondary objects: fillarea, line, marker,
textcombined, textorientation, or texttable

Check for VCS template objects:

######  

Query Function

Description

istemplate()

verifies a template object

######  Creating VCS Objects

The create functions allow the user to create VCS objects which can be
modified directly to produce the desired results. Since the VCS "default"
objects do allow modifications, it is best to either create a new VCS object
or get an existing one. When a VCS object is created, it is stored in an
internal table for later use and/or recall.

Create the following VCS objects:

######  

Create

Description

createboxfill()

creates a new boxfill graphics method object

createcontinents()

creates a new continents graphics method object

createfillarea()

creates a new fillarea secondary object

createisofill()

creates a new isofill graphics method object

createisoline()

creates a new isoline graphics method object

createline()

creates a new line secondary object

createmarker()

creates a new marker secondary object

createoutfill()

creates a new outfill graphics method object

createoutline()

creates a new outline graphics method object

createscatter()

creates a new scatter graphics method object

createtextcombined()

creates a new text-combined secondary object

createtextorientation()

creates a new text-orientation secondary object

createtexttable()

creates a new text-table secondary object

createvector()

creates a new vector graphics method object

createxvsy()

creates a new xvsy graphics method object

createxyvsy()

creates a new xyvsy graphics method object

createyxvsx()

creates a new xyvsy graphics method object

create3d_scalar()

creates a new 3d_scalar graphics method object

create3d_vector()

creates a new 3d_vector graphics method object

######  Get Existing VCS Objects

The get functions are used to obtain VCS objects that exist in the object
memory tables. The get function directly manipulates the object's attributes
in memory. If the object is used to display data on a plot and is manipulated
by the user, then the plot will be automatically updated.

Get the following VCS objects:

######  

Get

Description

getboxfill()

get specified boxfill graphics method and create boxfill object

getcontinents()

get specified continents graphics method and create continents object

getfillarea()

get specified fillarea secondary object and create fillarea object

getisofill()

get specified isofill graphics method and create fillarea object

getisoline()

get specified isoline graphics method and create isoline object

getline()

get specified line secondary object and create line object

getmarker()

get specified marker secondary object and create marker object

getoutfill()

get specified outfill graphics method and create outfill object

getoutline()

get specifed outline graphics method and create outline object

getscatter()

get specified scatter graphics method and create scatter object

gettextcombined()

get specified text-combined secondary object and create text-combined object

gettextorientation()

get specified text-orientation secondary object and create text-orientation
object

gettexttable()

get specified text-table secondary object and create text-table object

getvector()

get specified vector graphics method and create vector object

getxvsy()

get specified xvsy graphics method and create xvsy object

getxyvsy()

get specified xyvsy graphics method and create xyvsy object

getyxvsx()

get specified yxvsx graphics method and create yxvsx

get3d_scalar()

get specified 3d_scalar graphics method and create 3d_scalar

get3d_vector()

get specified 3d_vector graphics method and create 3d_vector


######  Removing VCS Objects

Unwanted VCS objects can be removed from internal memory with the use of the
remove function. The remove function will identify the VCS object type and
remove it from the appropriate object table.

Remove VCS objects:

######  

Remove

Description

removeobject()

allows the user to remove objects from the appropriate object list

######  Show VCS Object List

The show function is handy to list VCS objects tables.

The show function is used to list the VCS objects in memory:

######  

Show

Description

show()

list VCS primary and secondary class objects in memory

######  Saving VCS Object in a Script File

Script commands define the actions that are necessary to preserve an
interactive session as a script and to mimic that session in a non-interactive
replay of the script. Many attributes are needed to create a graphical
representation of a variable, e.g. attributes to identify the variable and to
label the plotting axes. By use of VCS and Python scripts, most of these
attributes can be manipulated to create the desired visual effect, and the
resulting attributes can be saved for later use. VCS and Python scripts also
allow the user to save a sequence of interactive operations for replay, and to
recover from a system failure.

After creating and/or modifying a VCS object, the user can save the object in
the initial.attributes file. The initial.attributes file contains many
predefined attribute settings to aid the beginning user of VCS. The path to
the file must be:

/$HOME/PCMDI_GRAPHICS/initial.attributes

where /$HOME denotes the user's home directory. (Note, when VCS is executed
for the first time, a /PCMDI_GRAPHICS subdirectory will be created
automatically if one has not already been created.) The user also can
customize the initial.attributes file directly.

To re-save the initial.attributes file, use the function:

######  

Save Initial Script

Description

saveinitialfile()

saves current VCS objects in the initial.attributes file, which is read
initially at start-up

To save VCS objects as Python scripts or VCS scripts, use the function:

######  

Save VCS Objects

Description

scriptobject()

save individual VCS objects as Python or VCS script file

To save the state of the system, use the function:

######  

Save System State

Description

scriptstate()

saves a sequence of interactive operations for replay; or to recover from a
system failure

To run a VCS script file, use the function:

######  

Run Script

Description

scriptrun()

run a previously saved VCS script file

[Go to Main](vcs.html) [Go to Previous](vcs-3.html) [Go to Next](vcs-5.html)


