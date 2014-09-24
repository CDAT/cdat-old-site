---
layout: default
title: VCS Chapter 6
---
##  CHAPTER 6 VCS Primary Objects

In VCS, primary objects define what will be displayed on the VCS Canvas. This
section defines two of the three primary objects and how to modify them
dynamically in the system: graphics methods, which specifies the display
technique; and the picture template, which determines the appearance of each
segment of the display.

Note, to see the list of object attributes, use the list() function. For
example:

import vcs

a=vcs.init()

box=a.createboxfill(`new')

box.list() # This call will list the boxfill attributes and their values

isof=a.createisofill(`new')

isof.list() # This call will list the isofill attributes and their values

tpl=a.createtemplate(`new')

tpl.list() # This call will list the template attributes and their values



######  

Object

Attributes (or Members)

Expected Type(s)

boxfill



(graphics method class name is Gfb)

name

projection

xticlabels1

xticlabels2

xmtics1

xmtics2

yticlabels1

yticlabels2

ymtics1

ymtics2

datawc_x1

datawc_y1

datawc_x2

datawc_y2

xaxisconvert

yaxisconvert

level_1

level_2

color_1

color_2

legend_type

legend

ext_1

ext_2

missing

StringType

Either: `linear', `mollweide', `robinson', or `polar'

StringType or DictType

StringType or DictType

StringType or DictType

StringType or DictType

StringType or DictType

StringType or DictType

StringType or DictType

StringType or DictType

IntType or FloatType

IntType or FloatType

IntType or FloatType

IntType or FloatType

Either: 'linear', 'log10', 'ln','exp','area_wt'

Either: 'linear', 'log10', 'ln','exp','area_wt'

IntType or FloatType

IntType or FloatType

IntType: (Range: 0 to 255)

IntType: (Range: 0 to 255)

Either: 'VCS', 'Pts', 'List'

StringType

Either: 'n', 'y'

Either: 'n', 'y'

IntType: (Range: 0 to 255)

continents



(graphics method class name is Gcon)



name

projection

xticlabels1

xticlabels2

xmtics1

xmtics2

yticlabels1

yticlabels2

ymtics1

ymtics2

datawc_x1

datawc_y1

datawc_x2

datawc_y2

line



linecolor

type



StringType

Either: `linear', `mollweide', `robinson', or `polar'

StringType or DictType

StringType or DictType

StringType or DictType

StringType or DictType

StringType or DictType

StringType or DictType

StringType or DictType

StringType or DictType

IntType or FloatType

IntType or FloatType

IntType or FloatType

IntType or FloatType

LineObject or (Either: 'solid','dash','dot',

'dash-dot','long-dash', 0,1,2,3,4)

IntType: (Range 0 to 255)

IntType: (Range 0 to 11)

isofill



(graphics method class name is Gfi)



name

projection

xticlabels1

xticlabels2

xmtics1

xmtics2

yticlabels1

yticlabels2

ymtics1

ymtics2

datawc_x1

datawc_y1

datawc_x2

datawc_y2

xaxisconvert

yaxisconvert

missing

ext_1

ext_2

fillareaindices



fillareastyle

fillareacolors



levels

StringType

Either: `linear', `mollweide', `robinson', or `polar'

StringType or DictType

StringType or DictType

StringType or DictType

StringType or DictType

StringType or DictType

StringType or DictType

StringType or DictType

StringType or DictType

IntType or FloatType

IntType or FloatType

IntType or FloatType

IntType or FloatType

Either: 'linear', 'log10', 'ln','exp','area_wt'

Either: 'linear', 'log10', 'ln','exp','area_wt'

IntType: (Range 0 to 255)

Either: 'n', 'y'

Either: 'n', 'y'

FillareaObject, or (Either: ListType, or TupleType

[Values range 1 to 20])

Either: 'solid', 'hatch', 'pattern'

ListType, or TupleType (Index values

range 0 to 255)

ListType, TupleType (Values are either

integers, floats)

isoline



(graphics method class name is Gi)



name

projection

xticlabels1

xticlabels2

xmtics1

xmtics2

yticlabels1

yticlabels2

ymtics1

ymtics2

datawc_x1

datawc_y1

datawc_x2

datawc_y2

xaxisconvert

yaxisconvert

label

line



linecolors

text





textcolors

level

StringType

Either: `linear', `mollweide', `robinson', or `polar'

StringType or DictType

StringType or DictType

StringType or DictType

StringType or DictType

StringType or DictType

StringType or DictType

StringType or DictType

StringType or DictType

IntType or FloatType

IntType or FloatType

IntType or FloatType

IntType or FloatType

Either: 'linear', 'log10', 'ln','exp','area_wt'

Either: 'linear', 'log10', 'ln','exp','area_wt'

Either: 'n', 'y', 0, 1

LineObject or (Either: "solid", "dash", "dot", "dash-dot", "long-dash", 0, 1,
2, 3, 4)

ListType, TupleType (Values range 0 to 255)

TextcombinedObject, TextOrientationObject,

TexttableObject, or (Either: ListType, TupleType,

IntType [Values range 1 to 9])

ListType, TupleType (Values range 0 to 255)

ListType, TupleType, IntType, FloatType

outfill



(graphics method class name is Gfo)



name

projection

xticlabels1

xticlabels2

xmtics1

xmtics2

yticlabels1

yticlabels2

ymtics1

ymtics2

datawc_x1

datawc_y1

datawc_x2

datawc_y2

xaxisconvert

yaxisconvert

fillareastyle



fillareaindex

fillareacolor

outfill

StringType

Either: `linear', `mollweide', `robinson', or `polar'

StringType or DictType

StringType or DictType

StringType or DictType

StringType or DictType

StringType or DictType

StringType or DictType

StringType or DictType

StringType or DictType

IntType or FloatType

IntType or FloatType

IntType or FloatType

IntType or FloatType

Either: 'linear', 'log10', 'ln','exp','area_wt'

Either: 'linear', 'log10', 'ln','exp','area_wt'

FillareaObject or (Either: 'solid', 'hatch',

'pattern', 0, 1, 2, 3)

IntType: (Range 0 to 20)

IntType: (Range 0 to 255)

ListType, TupleType, IntType, FloatType

(must be less than 10 values)

outline



(graphics method class name is Go)



name

projection

xticlabels1

xticlabels2

xmtics1

xmtics2

yticlabels1

yticlabels2

ymtics1

ymtics2

datawc_x1

datawc_y1

datawc_x2

datawc_y2

xaxisconvert

yaxisconvert

line



linecolor

outline

StringType

Either: `linear', `mollweide', `robinson', or `polar'

StringType or DictType

StringType or DictType

StringType or DictType

StringType or DictType

StringType or DictType

StringType or DictType

StringType or DictType

StringType or DictType

IntType or FloatType

IntType or FloatType

IntType or FloatType

IntType or FloatType

Either: 'linear', 'log10', 'ln','exp','area_wt'

Either: 'linear', 'log10', 'ln','exp','area_wt'

LineObject or (Either: "solid", "dash", "dot", "dash-dot", "long-dash", 0, 1,
2, 3, 4)

ListType, TupleType (Values range 0 to 255)

ListType, TupleType, IntType, FloatType

(must be less than 10 values)

scatter



(graphics method class name is GSp)



name

projection

xticlabels1

xticlabels2

xmtics1

xmtics2

yticlabels1

yticlabels2

ymtics1

ymtics2

datawc_x1

datawc_y1

datawc_x2

datawc_y2

xaxisconvert

yaxisconvert

marker













markercolor

markersize

StringType

Either: `linear', `mollweide', `robinson', or `polar'

StringType or DictType

StringType or DictType

StringType or DictType

StringType or DictType

StringType or DictType

StringType or DictType

StringType or DictType

StringType or DictType

IntType or FloatType

IntType or FloatType

IntType or FloatType

IntType or FloatType

Either: 'linear', 'log10', 'ln','exp','area_wt'

Either: 'linear', 'log10', 'ln','exp','area_wt'

MarkerObject or (Either: 'dot', 'plus', 'star',

'circle', 'cross', 'diamond', 'triangle_up',

'triangle_down', 'triangle_left', 'triangle_right',

'square', 'diamond_fill', 'triangle_up_fill',

'triangle_down_fill', 'triangle_left_fill',

'triangle_right_fill', 'square_fill', 1, 2, 3, 4, 5, 6,

7, 8, 9, 10, 11, 12, 13, 14 ,15, 16, 17

IntType: (Range 0 to 255)

IntType: (Range 1 to 300)

vector



(graphics method class name is Gv)



name

projection

xticlabels1

xticlabels2

xmtics1

xmtics2

yticlabels1

yticlabels2

ymtics1

ymtics2

datawc_x1

datawc_y1

datawc_x2

datawc_y2

xaxisconvert

yaxisconvert

line



linecolor

scale

alignment

type

reference

StringType

Either: `linear', `mollweide', `robinson', or `polar'

StringType or DictType

StringType or DictType

StringType or DictType

StringType or DictType

StringType or DictType

StringType or DictType

StringType or DictType

StringType or DictType

IntType or FloatType

IntType or FloatType

IntType or FloatType

IntType or FloatType

Either: 'linear', 'log10', 'ln','exp','area_wt'

Either: 'linear', 'log10', 'ln','exp','area_wt'

LineObject or (Either: "solid", "dash", "dot", "dash-dot", "long-dash", 0, 1,
2, 3, 4)

ListType, TupleType (Values range 0 to 255)

IntType, FloatType

Either: 'head', 'center', 'tail', 0, 1, 2

Either: 'arrows', 'barbs', 'solidarrows', 0, 1, 2

FloatType, IntType

xvsy



(graphics method class name is GXY)



name

projection

xticlabels1

xticlabels2

xmtics1

xmtics2

yticlabels1

yticlabels2

ymtics1

ymtics2

datawc_x1

datawc_y1

datawc_x2

datawc_y2

xaxisconvert

yaxisconvert

line



linecolor

marker













markercolor

markersize

StringType

Either: `linear', `mollweide', `robinson', or `polar'

StringType or DictType

StringType or DictType

StringType or DictType

StringType or DictType

StringType or DictType

StringType or DictType

StringType or DictType

StringType or DictType

IntType or FloatType

IntType or FloatType

IntType or FloatType

IntType or FloatType

Either: 'linear', 'log10', 'ln','exp','area_wt'

Either: 'linear', 'log10', 'ln','exp','area_wt'

LineObject or (Either: "solid", "dash", "dot", "dash-dot", "long-dash", 0, 1,
2, 3, 4)

ListType, TupleType (Values range 0 to 255)

MarkerObject or (Either: 'dot', 'plus', 'star',

'circle', 'cross', 'diamond', 'triangle_up',

'triangle_down', 'triangle_left', 'triangle_right',

'square', 'diamond_fill', 'triangle_up_fill',

'triangle_down_fill', 'triangle_left_fill',

'triangle_right_fill', 'square_fill', 1, 2, 3, 4, 5, 6,

7, 8, 9, 10, 11, 12, 13, 14 ,15, 16, 17

IntType: (Range 0 to 255)

IntType: (Range 1 to 300)

xyvsy



(graphics method class name is GXy)



name

projection

xticlabels1

xticlabels2

xmtics1

xmtics2

yticlabels1

yticlabels2

ymtics1

ymtics2

datawc_x1

datawc_y1

datawc_x2

datawc_y2

xaxisconvert

line



linecolor

marker













markercolor

markersize

StringType

Either: `linear', `mollweide', `robinson', or `polar'

StringType or DictType

StringType or DictType

StringType or DictType

StringType or DictType

StringType or DictType

StringType or DictType

StringType or DictType

StringType or DictType

IntType or FloatType

IntType or FloatType

IntType or FloatType

IntType or FloatType

Either: 'linear', 'log10', 'ln','exp','area_wt'

LineObject or (Either: "solid", "dash", "dot", "dash-dot", "long-dash", 0, 1,
2, 3, 4)

ListType, TupleType (Values range 0 to 255)

MarkerObject or (Either: 'dot', 'plus', 'star',

'circle', 'cross', 'diamond', 'triangle_up',

'triangle_down', 'triangle_left', 'triangle_right',

'square', 'diamond_fill', 'triangle_up_fill',

'triangle_down_fill', 'triangle_left_fill',

'triangle_right_fill', 'square_fill', 1, 2, 3, 4, 5, 6,

7, 8, 9, 10, 11, 12, 13, 14 ,15, 16, 17

IntType: (Range 0 to 255)

IntType: (Range 1 to 300)

yxvsx



(graphics method class name is GYx)

name

projection

xticlabels1

xticlabels2

xmtics1

xmtics2

yticlabels1

yticlabels2

ymtics1

ymtics2

datawc_x1

datawc_y1

datawc_x2

datawc_y2

yaxisconvert

line



linecolor

marker













markercolor

markersize

StringType

Either: `linear', `mollweide', `robinson', or `polar'

StringType or DictType

StringType or DictType

StringType or DictType

StringType or DictType

StringType or DictType

StringType or DictType

StringType or DictType

StringType or DictType

IntType or FloatType

IntType or FloatType

IntType or FloatType

IntType or FloatType

Either: 'linear', 'log10', 'ln','exp','area_wt'

LineObject or (Either: "solid", "dash", "dot", "dash-dot", "long-dash", 0, 1,
2, 3, 4)

ListType, TupleType (Values range 0 to 255)

MarkerObject or (Either: 'dot', 'plus', 'star',

'circle', 'cross', 'diamond', 'triangle_up',

'triangle_down', 'triangle_left', 'triangle_right',

'square', 'diamond_fill', 'triangle_up_fill',

'triangle_down_fill', 'triangle_left_fill',

'triangle_right_fill', 'square_fill', 1, 2, 3, 4, 5, 6,

7, 8, 9, 10, 11, 12, 13, 14 ,15, 16, 17

IntType: (Range 0 to 255)

IntType: (Range 1 to 300)

template



(Picture Template class name is P)

member = file

priority

x

y

texttable

textorientation

member = function

priority

x

y

texttable

textorientation

member = logicalmask

priority

x

y

texttable

textorientation

member =

transformation

priority

x

y

texttable

textorientation

member = source

priority

x

y

texttable

textorientation



IntType

IntType, FloatType

IntType, FloatType

TexttableObject, StringType

TextorientationObject, StringType



IntType

IntType, FloatType

IntType, FloatType

TexttableObject, StringType

TextorientationObject, StringType



IntType

IntType, FloatType

IntType, FloatType

TexttableObject, StringType

TextorientationObject, StringType





IntType

IntType, FloatType

IntType, FloatType

TexttableObject, StringType

TextorientationObject, StringType



IntType

IntType, FloatType

IntType, FloatType

TexttableObject, StringType

TextorientationObject, StringType



member = dataname

priority

x

y

texttable

textorientation

member = title

priority

x

y

texttable

textorientation

member = units

priority

x

y

texttable

textorientation

member = crdate

priority

x

y

texttable

textorientation

member = crtime

priority

x

y

texttable

textorientation



IntType

IntType, FloatType

IntType, FloatType

TexttableObject, StringType

TextorientationObject, StringType



IntType

IntType, FloatType

IntType, FloatType

TexttableObject, StringType

TextorientationObject, StringType



IntType

IntType, FloatType

IntType, FloatType

TexttableObject, StringType

TextorientationObject, StringType



IntType

IntType, FloatType

IntType, FloatType

TexttableObject, StringType

TextorientationObject, StringType



IntType

IntType, FloatType

IntType, FloatType

TexttableObject, StringType

TextorientationObject, StringType



member = comment1

priority

x

y

texttable

textorientation

member = comment2

priority

x

y

texttable

textorientation

member = comment3

priority

x

y

texttable

textorientation

member = comment4

priority

x

y

texttable

textorientation

member = xname

priority

x

y

texttable

textorientation



IntType

IntType, FloatType

IntType, FloatType

TexttableObject, StringType

TextorientationObject, StringType



IntType

IntType, FloatType

IntType, FloatType

TexttableObject, StringType

TextorientationObject, StringType



IntType

IntType, FloatType

IntType, FloatType

TexttableObject, StringType

TextorientationObject, StringType



IntType

IntType, FloatType

IntType, FloatType

TexttableObject, StringType

TextorientationObject, StringType



IntType

IntType, FloatType

IntType, FloatType

TexttableObject, StringType

TextorientationObject, StringType



member = yname

priority

x

y

texttable

textorientation

member = zname

priority

x

y

texttable

textorientation

member = tname

priority

x

y

texttable

textorientation

member = xunits

priority

x

y

texttable

textorientation

member = yunits

priority

x

y

texttable

textorientation



IntType

IntType, FloatType

IntType, FloatType

TexttableObject, StringType

TextorientationObject, StringType



IntType

IntType, FloatType

IntType, FloatType

TexttableObject, StringType

TextorientationObject, StringType



IntType

IntType, FloatType

IntType, FloatType

TexttableObject, StringType

TextorientationObject, StringType



IntType

IntType, FloatType

IntType, FloatType

TexttableObject, StringType

TextorientationObject, StringType



IntType

IntType, FloatType

IntType, FloatType

TexttableObject, StringType

TextorientationObject, StringType



member = zunits

priority

x

y

texttable

textorientation

member = tunits

priority

x

y

texttable

textorientation

member = xvalue

priority

x

y

format

texttable

textorientation

member = yvalue

priority

x

y

format

texttable

textorientation



IntType

IntType, FloatType

IntType, FloatType

TexttableObject, StringType

TextorientationObject, StringType



IntType

IntType, FloatType

IntType, FloatType

TexttableObject, StringType

TextorientationObject, StringType



IntType

IntType, FloatType

IntType, FloatType

Currently not able to set

TexttableObject, StringType

TextorientationObject, StringType



IntType

IntType, FloatType

IntType, FloatType

Currently not able to set

TexttableObject, StringType

TextorientationObject, StringType



member = zvalue

priority

x

y

format

texttable

textorientation

member = tvalue

priority

x

y

format

texttable

textorientation

member = mean

priority

x

y

format

texttable

textorientation

member = min

priority

x

y

format

texttable

textorientation



IntType

IntType, FloatType

IntType, FloatType

Currently not able to set

TexttableObject, StringType

TextorientationObject, StringType



IntType

IntType, FloatType

IntType, FloatType

Currently not able to set

TexttableObject, StringType

TextorientationObject, StringType



IntType

IntType, FloatType

IntType, FloatType

Currently not able to set

TexttableObject, StringType

TextorientationObject, StringType



IntType

IntType, FloatType

IntType, FloatType

Currently not able to set

TexttableObject, StringType

TextorientationObject, StringType



member = max

priority

x

y

format

texttable

textorientation

member = xtic1

priority

y1

y2

line

member = xtic2

priority

y1

y2

line

member = xmintic1

priority

y1

y2

line

member = xmintic2

priority

y1

y2

line



IntType

IntType, FloatType

IntType, FloatType

Currently not able to set

TexttableObject, StringType

TextorientationObject, StringType



IntType

IntType, FloatType

IntType, FloatType

LineObject, StringType



IntType

IntType, FloatType

IntType, FloatType

LineObject, StringType



IntType

IntType, FloatType

IntType, FloatType

LineObject, StringType



IntType

IntType, FloatType

IntType, FloatType

LineObject, StringType



member = ytic1

priority

x1

x2

line

member = ytic2

priority

x1

x2

line

member = ymintic1

priority

x1

x2

line

member = ymintic2

priority

x1

x2

line

member = xlabel1

priority

y

texttable

textorientation

member = xlabel2

priority

y

texttable

textorientation



IntType

IntType, FloatType

IntType, FloatType

LineObject, StringType



IntType

IntType, FloatType

IntType, FloatType

LineObject, StringType



IntType

IntType, FloatType

IntType, FloatType

LineObject, StringType



IntType

IntType, FloatType

IntType, FloatType

LineObject, StringType



IntType

IntType, FloatType

TexttableObject, StringType

TextorientationObject, StringType



IntType

IntType, FloatType

TexttableObject, StringType

TextorientationObject, StringType



member = ylabel1

priority

x

texttable

textorientation

member = ylabel2

priority

x

texttable

textorientation

member = box1

priority

x1

y1

x2

y2

line

member = box2

priority

x1

y1

x2

y2

line



IntType

IntType, FloatType

TexttableObject, StringType

TextorientationObject, StringType



IntType

IntType, FloatType

TexttableObject, StringType

TextorientationObject, StringType



IntType

IntType, FloatType

IntType, FloatType

IntType, FloatType

IntType, FloatType

LineObject, StringType



IntType

IntType, FloatType

IntType, FloatType

IntType, FloatType

IntType, FloatType

LineObject, StringType



member = box3

priority

x1

y1

x2

y2

line

member = box4

priority

x1

y1

x2

y2

line

member = line1

priority

x1

y1

x2

y2

line

member = line2

priority

x1

y1

x2

y2

line



IntType

IntType, FloatType

IntType, FloatType

IntType, FloatType

IntType, FloatType

LineObject, StringType



IntType

IntType, FloatType

IntType, FloatType

IntType, FloatType

IntType, FloatType

LineObject, StringType



IntType

IntType, FloatType

IntType, FloatType

IntType, FloatType

IntType, FloatType

LineObject, StringType



IntType

IntType, FloatType

IntType, FloatType

IntType, FloatType

IntType, FloatType

LineObject, StringType



member = line3

priority

x1

y1

x2

y2

line

member = line4

priority

x1

y1

x2

y2

line

member = legend

priority

x1

y1

x2

y2

line

texttable

textorientation

member = data

priority

x1

y1

x2

y2



IntType

IntType, FloatType

IntType, FloatType

IntType, FloatType

IntType, FloatType

LineObject, StringType



IntType

IntType, FloatType

IntType, FloatType

IntType, FloatType

IntType, FloatType

LineObject, StringType



IntType

IntType, FloatType

IntType, FloatType

IntType, FloatType

IntType, FloatType

LineObject, StringType

TexttableObject, StringType

TextorientationObject, StringType



IntType

IntType, FloatType

IntType, FloatType

IntType, FloatType

IntType, FloatType

[Go to Main](vcs.html) [Go to Previous](vcs-5.html) [Go to Next](vcs-7.html)


