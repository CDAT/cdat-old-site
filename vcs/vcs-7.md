---
layout: default
title: VCS Chapter 7
---
##  CHAPTER 7 VCS Secondary Objects

Secondary objects help to specify and define primary objects in VCS. The list
of secondary objects include: colormap, fill area, format, line, marker, list,
text-combined, text-orientation, and text-table. Note, although the colormap
is considered a secondary object, it is acessed differenly. Therefore, the
colormap object will not be described below. See the "VCS Command Reference
Guide" for colormap commands.

Note, to see the list of object attributes, use the list() function. For
example:

import vcs

a=vcs.init()

ln=a.createline(`new')

ln.list() # This call will list the line attributes and their values

tt=a.createtexttable(`new')

tt.list() # This call will list the text-table attributes and their values





######  

Object

Attributes (or Members)

Exception Type(s)

fillarea

(graphics method class name is Tf)



name

style

index

color

StringType

Either: 'solid', 'hatch', 'pattern'

IntType: (Range 1 to 20)

IntType: (Range 0 to 255)

line

(graphics method class name is Tl)

name

type



width

color

StringType

Either: 'solid', 'dash', 'dot', 'dash-dot',

'long-dash', 0, 1, 2, 3, 4

IntType: (Range 1 to 300)

IntType: (Range 0 to 255)

marker

(graphics method class name is Tm)

name

type













size

color

StringType

Either: "dot", "plus", "star", "circle", "cross",

"diamond", "triangle_up", "triangle_down",

"triangle_left", "triangle_right", "square",

"diamond_fill", "triangle_up_fill",

"triangle_down_fill", "triangle_left_fill",

"triangle_right_fill", "square_fill", 0, 1, 2, 3, 4, 5,

6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17

IntType: (Range 1 to 300)

IntType: (Range 0 to 255)

text-combined

(graphics method class name is Tc)

name

font

spacing

expansion

color

name

height

angel

path

halign

valign

StringType

IntType: (Range 1 to 9)

IntType: (Range -50 to 50)

IntType: (Range 50 to 150)

IntType: (Range 0 to 255)

StringType

IntType: (Range 1 to 100)

IntType: (Range 0 to 360)

Either: 'right', 'left', 'up', 'down', 0, 1, 2, 3

Either: 'left', 'center', 'right', 0, 1, 2

Either: 'top', 'cap', 'half', 'base', 'bottom',

0, 1, 2, 3, 4

text-orientation

(graphics method class name is To)

name

height

angel

path

halign

valign

StringType

IntType: (Range 1 to 100)

IntType: (Range 0 to 360)

Either: 'right', 'left', 'up', 'down', 0, 1, 2, 3

Either: 'left', 'center', 'right', 0, 1, 2

Either: 'top', 'cap', 'half', 'base', 'bottom',

0, 1, 2, 3, 4

text-table

(graphics method class name is Tt)

name

font

spacing

expansion

color

StringType

IntType: (Range 1 to 9)

IntType: (Range -50 to 50)

IntType: (Range 50 to 150)

IntType: (Range 0 to 255)

[Go to Main](vcs.html) [Go to Previous](vcs-6.html) [Go to Next](vcs-8.html)


