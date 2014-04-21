---
layout: default
title: 
---


    * [ Source Code ](/cdat/source)

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

  * [ ![Send this page to somebody](media/mail_icon.gif) ](/cdat/tutorials/xmgrace_tut.html/xmgrace_reference.html/sendto_form)
  * [ ![Print this page](media/print_icon.gif) ](/this.print\(\))

#  Xmgrace Quick Reference - html

Quick Reference to Xmgrace: Types: fonts, lines, colors, symbols; xmgrace;
graph; axes; sets; functions; others.

  

* * *

#  Overview

[ Types ](/)  
[ Xmgrace ](/)  
[ Graph ](/)  
[ Axes ](/)  
[ Set ](/)  
[ Others ](/)  
[ Functions ](/)  

* * *

#  Sheet 1: _ Types _

Fonts

  

  

Lines

  

1

Times-Roman

  

1

full

2

Times-Italic

  

2

dot

3

Times-BoldItalic

  

3

dash

4

Helvetica

  

4

longdash

5

Helvetica-Oblique

  

5

dot-dash

6

Helvetica-Bold

  

6

dot-longdash

7

Helvetica-BoldOblique

  

7

dot-dot-dash

8

Courirer

  

8

dot-dash-dash

9

Courier-Oblique

  

  

  

10

Courier-Bold

  

  

  

11

Courier-BoldOblique

  

  

  

12

Symbol

  

  

  

13

ZapfDingbats

  

  

  

  

  

  

  

  

Colors

  

  

Symbols

  

0

white

  

0

none

1

black

  

1

circle

2

red

  

2

square

3

green

  

3

diamond

4

blue

  

4

triangle up

5

yellow

  

5

triangle left

6

brown

  

6

triangle down

7

grey

  

7

triangle right

8

violet

  

8

plus

9

cyan

  

9

X

10

magenta

  

10

star

11

orange

  

11

char

12

indigo

  

  

  

13

maroon

  

  

  

14

turquoise

  

  

  

15

green4

  

  

  

* * *

#  Sheet 2: _ Xmgrace _

 Xmgrace  
  

  

_  
_

  

  

  

Graph

See details

_ It's list of graph objects  _

  

  

  

ngraph

1

_ # of graphs  _

  

  

  

Set

See details

_  
_

  

  

  

nset

1

_ # of sets  _

  

  

  

Font

See details

_  
_

  

  

  

nfont

14

_  
_

  

  

  

lfont

  

_  
_

  

  

  

Colors

See details

  

  

  

  

ncolor

  

_  
_

  

  

  

String

See details

_  
_

  

  

  

nstring

  

_  
_

  

  

  

Line

See details

_  
_

  

  

  

nlne

  

_  
_

  

  

  

version

'50102'

_ Xmgrace version  _

  

  

  

pyversion

'1.1.3b'

_ Python module version  _

  

  

  

link_page

Off

_  
_

  

  

  

linewidth

1

_  
_

  

  

  

linestyle

1

  

  

  

  

color

1

_  
_

  

  

  

pattern

1

_  
_

  

  

  

font

0

_  
_

  

  

  

char_size

1

_  
_

  

  

  

symbol_size

1

_  
_

  

  

  

sformat

'"%16.8g"'

_  
_

  

  

  

background_color

0

_  
_

  

  

  

R

See details

_  
_

  

  

  

nr

0

_ # of regions  _

  

  

  

 page  
  

_  
_

  

  

  

  

x

792

_ pixels  _

  

  

  

y

612

_  
_

  

  

  

scroll

5

_  
_

  

  

  

inout

5

_  
_

  

  

  

background_fill

'on'

_ 'off'  _

  

  

 timestamp  
  

_  
_

  

  

  

  

status

'off'

_ 'on'  _

  

  

  

x

0.03

  

  

  

  

y

0.03

  

  

  

  

color

1

  

  

  

  

rot

0

  

  

  

  

font

0

  

  

  

  

char_size

1

  

  

  

  

default

Mon Oct 18 16:55:50 1999

  

  

  

 date  
  

_  
_

  

  

  

  

reference

0

  

  

  

  

 wrap  
_  
_

  

  

  

  

  

status

'off'

_ 'on'  _

  

  

  

year

1950

  

* * *

#  Sheet 3: _ Graph _

 Graph  
_ (parent='xmgrace object,ymin,ymax,xmin,xmax)  _

  

  

  

  

  

xmin

''

_ not recommended, just for backward compatibily  _

  

  

  

xmax

''

_  
_

  

  

  

ymin

''

_  
_

  

  

  

ymax

''

_  
_

  

  

  

vxmin

0.15

_ In % of page  _

  

  

  

vxmax

0.85

_ "  _

  

  

  

vymin

0.15

_ "  _

  

  

  

vymax

0.85

_ "  _

  

  

  

status

'on'

_ 'off'  _

  

  

  

hidden

'false'

_ 'true'  _

  

  

  

type

'xy'

_ ' chart','polar','pie','smith','fixed'  _

  

  

  

stacked

'false'

_ 'true'  _

  

  

  

stack_world

[0,0,0,0]

_  
_

  

  

  

bar_hgap

0

_  
_

  

  

  

titel

''

_  
_

  

  

  

stitle

''

  

  

  

  

 fixedpoint  
  

  

  

  

  

  

status

'off'

_ 'on'  _

  

  

  

type

0

  

  

  

  

xy

[0,0]

  

  

  

  

format

'general'

  

  

  

  

prec

6

  

  

  

 tit  
  

  

  

  

  

  

font

parent=0

_ from xmgrace object  _

  

  

  

size

1.5

_  
_

  

  

  

color

parent=1

_ from xmgrace object  _

  

  

 stit  
  

  

_  
_

  

  

  

font

parent=0

_ from xmgrace object  _

  

  

  

size

1

_  
_

  

  

  

color

parent=1

_ from xmgrace object  _

  

  

 Set  
It's a list of set object, associated with the graph

  

_  
_

  

  

  

see special sheet

  

_  
_

  

  

 x/yaxis  
  

  

_ Identical for 'xaxis and 'yaxis  _

  

  

   

see special sheet

  

_  
_

  

  

 legend  
  

  

  

  

  

  

status

'on'

_ 'off'  _

  

  

  

loctype

'view'

_ 'world'  _

  

  

  

x

0.85

_ % of the page  _

  

  

  

y

0.8

_ % of the page  _

  

  

  

 box  
  

  

  

  

  

  

color

parent=1

_ from xmgrace object  _

  

  

  

pattern

parent=1

_ from xmgrace object  _

  

  

  

linewidth

parent=1

_ from xmgrace object  _

  

  

  

linestyle

parent=1

_ from xmgrace object  _

  

  

  

fcolor

0

  

  

  

  

fpattern

parent=1

_ from xmgrace object  _

  

  

font

parent=0

  

  

  

  

char_size

parent=1

  

  

  

  

color

parent=1

  

  

  

  

length

4

  

  

  

  

vgap

1

  

  

  

  

hgap

1

  

  

  

  

Invert

'false'

_ 'true'  _

  

  

 frame  
  

  

  

  

  

  

type

0

  

  

  

  

linestyle

parent=1

  

  

  

  

linewidth

parent=1

  

  

  

  

color

parent=1

  

  

  

  

pattern

parent=1

  

  

  

  

background_color

  

parent=0

  

  

  

background_pattern

  

parent=1

  

* * *

#  Sheet 4: _ Axes _

 x/yaxis  
   

   

_ Identical for 'xaxis and 'yaxis  _

   

   


  

label

'

  

  

  

  

scale

'normal'

_ 'logarithmic','Reciprocal'  _

  

  

  

Invert

'off'

_ 'on'  _

  

  

  

status

'false'

_  
_

  

  

  

zero

'false'

_ 'true'  _

  

  

  

xoffset

0

_  
_

  

  

  

yoffset

0

_  
_

  

  

  

offset

[]

_ you can pass the xoffset and yoffset values here instead  _

  

  

  

altaxis

'off'

_ 'on'  _

  

  

  

min

0

_ can be changed when creating the graph  _

  

  

  

max

1

"

  

  

   

 bar  
   

   

   

   


  

  

status

'on'

_ 'off'  _

  

  

  

color

parent=1

_ from xmgrace object  _

  

  

  

linestyle

parent=1

_ from xmgrace object  _

  

  

  

linewidth

parent=1

_ from xmgrace object  _

  

  

  

  

  

_  
_

  

   

 lbl  
   

   

 _   
_ 

   


  

  

layout

'para'

_ 'perp' (// or perpendicular)  _

  

  

  

char_size

parent=1

_ from xmgrace object  _

  

  

  

font

parent=0

_ from xmgrace object  _

  

  

  

color

parent=1

_ from xmgrace object  _

  

   

   

 place  
   

   

   


  

  

  

loc

'auto'

  

  

  

  

side

'normal'

_ 'oposite', 'both' : where to put the labels  _

   

 tick  
   

   

   

   


  

  

status

'on'

_ 'off'  _

  

  

  

inc

0.5

_ # or whatever increment value (i.e. Every 0.5 here)  _

  

  

  

minor_ticks

1

_ # of sub tickmarks between the major ones  _

  

  

  

place_rounded

'true'

_ 'false'  _

  

  

  

nsub

6

_ # autotick division (for place rounded ?)  _

  

  

  

orientation

'in'

_ 'out','both'  _

  

  

  

place

'normal'

_ 'oposite','both'  _

  

   

   

 spec  
   

   

   


  

  

  

loc

[]

_ list of loc for ticks or dictionary: loc/label  _

  

  

  

values

[]

_ labels(values) list to write at each loc or dic  _

  

  

  

type

'both'

_ 'none','ticks'  _

   

   

 major  
   

   

   


  

  

  

size

1

  

  

  

  

color

parent=1

_ from xmgrace object  _

  

  

  

linewidth

parent=1

_ from xmgrace object  _

  

  

  

linestyle

parent=1

_ from xmgrace object  _

  

  

  

grid

'off'

_ 'on', draw the grid lines  _

   

   

 minor  
   

   

 _   
_ 

  

  

  

size

0.5

_  
_

  

  

  

color

parent=1

_ from xmgrace object  _

  

  

  

linewidth

parent=1

_ from xmgrace object  _

  

  

  

linestyle

parent=1

_ from xmgrace object  _

  

  

  

'grid'

'off'

_ 'on', draw the grid lines  _

   

   

 label  
   

   

 _   
_ 

  

  

  

status

'on'

_ 'off'  _

  

  

  

prec

5

_  
_

  

  

  

format

'general'

_  
_

  

  

  

append

''

_  
_

  

  

  

prepend

''

_  
_

  

  

  

angle

0

_  
_

  

  

  

skip

0

_  
_

  

  

  

stagger

0

_  
_

  

  

  

place

'normal'

_ 'opposite','both'  _

  

  

  

offset

'auto'

_ [0.,0.], // and perpendicular offsets  _

  

  

  

sign

'normal'

_  
_

  

  

  

start

'auto'

_ or value  _

  

  

  

stop

'auto'

_ or value  _

  

  

  

char_size

parent=1

_  
_

  

  

  

font

parent=0

_  
_

  

  

  

color

parent=1

_  
_

  

  

  

type

'auto'

  

  

  

type

'auto'

_ 'spec','zmean' (for area weighted zonal mean betw -1 and 1)  _

  

  

alt

'off'

'on'

  

  

* * *

#  Sheet 5: _ Set _

 Set  
  

  

  

  

  

  

  

graph

0

_ can be passed at creation time  _

  

  

  

  

hidden

'false'

_ 'true'  _

  

  

  

  

type

'xy'

_ xydx','xydy','xydxdx','xydydy','xydxdy','xydxdxdydy','bar','bardy','bardydy
_

  

  

  

  

  

  

_ 'xyhilo','xyz','xyr','xysize','xycolor','xycolpat','xyvmap','xyboxplot'  _

  

  

  

  

 symbol  
  

  

  

  

  

  

  

type

0

  

  

  

  

  

size

parent=symbol_size=1

_  
_

_ from xmgrace object  _

  

  

  

color

parent=background_color=0

_  
_

_ from xmgrace object  _

  

  

  

pattern

parent=1

_ from xmgrace object  _

  

  

  

  

fcolor

parent=1

_ can be passed at creation time  _

  

  

  

  

fpattern

parent=1

_ from xmgrace object  _

  

  

  

  

linestyle

parent=1

_ from xmgrace object  _

  

  

  

  

linewidth

parent=1

_ from xmgrace object  _

  

  

  

  

char

65

_  
_

  

  

  

  

char_font

parent=0

_ from xmgrace object  _

  

  

  

  

skip

0

  

  

  

  

 line  
  

  

  

  

  

  

  

type

1

  

  

  

  

  

linestyle

parent=1

_ from xmgrace object  _

  

  

  

  

linewidth

parent=1

_ from xmgrace object  _

  

  

  

  

color

parent=1

_ can be passed at creation time  _

  

  

  

  

pattern

parent=1

_ from xmgrace object  _

  

  

  

 baseline  
  

  

  

  

  

  

  

type

0

  

  

  

  

  

status

'off'

_ 'on'  _

  

  

  

dropline

'off'

_ 'on'  _

  

  

  

  

 fill  
  

  

  

  

  

  

  

type

0

_ 0:'none',1:'as polygone',2:'to baseline'  _

  

# only, no string allowed

  

  

rule

0

_ 0:'winding',1:'even-odd'  _

  

# only, no string allowed

  

  

color

parent=1

_ can be passed at creation time  _

  

  

  

  

pattern

parent=1

_ from xmgrace object  _

  

  

  

 avalue  
  

  

  

  

  

  

  

status

'off'

_ 'on'  _

  

  

  

  

type

2

_  
_

  

  

  

  

char_size

parent=1

_ from xmgrace object  _

  

  

  

  

font

parent=0

_ from xmgrace object  _

  

  

  

  

color

parent=1

_ can be passed at creation time  _

  

  

  

  

rot

0

_  
_

  

  

  

  

format

'general'

_  
_

  

  

  

  

prec

3

_  
_

  

  

  

  

prepend

''

_  
_

  

  

  

  

append

''

_  
_

  

  

  

  

xoffset

0

_  
_

  

  

  

  

yoffset

0

_  
_

  

  

  

  

offset

[]

_ you can pass the xoffset and yoffset values here instead  _

  

  

  

 error  
  

  

_  
_

  

  

  

  

status

'off'

_ 'on'  _

  

  

  

  

type

'both'

_ 'normal','opposite'  _

  

  

  

  

length

1

  

  

  

  

  

linewidth

parent=1

_ from xmgrace object  _

  

  

  

  

linsestyle

parent=1

_ from xmgrace object  _

  

  

  

  

 riser  
  

  

  

  

  

  

  

linewidth

parent=1

_ from xmgrace object  _

  

  

  

  

linsestyle

parent=1

_ from xmgrace object  _

  

* * *

#  Sheet 6: _ Others _

 Color  
(name)

  

  

  

  

name

'black'

_ can pass any name  _

  

  

rgb

[0,0,0]

_ red green blue values  _

  

  

change()

  

_ function to change the color, expect a name then reset rgb's  _

  

  

  

  

  

  

 Region  
  

  

_  
_

  

  

status

'off'

_ 'on'  _

  

  

type

'above'

_ 'polyi','polyo','above','below','left','right','horizi','horizo','veri','ver
to'  _

  

  

linestyle

parent=1

_  
_

  

  

linewidth

parent=1

_  
_

  

  

color

parent=1

_  
_

  

  

link

'all'

_  
_

  

  

xy

[]

_ list of [x,y] coordinates to def the polygone  _

  

  

line

[0,0,0,0]

_  
_

  

  

  

  

  

  

 String  
(x,y,text,[color],[char_size],[font],[rot],[just])

  

  

  

  

x

argument

  

  

  

y

argument

  

  

  

text

argument

  

  

  

status

'on'

_ 'off'  _

  

  

xy

[x,y]

_  
_

  

  

loctype

'view'

_ 'world'  _

  

  

color

parent=1

  

  

  

char_size

parent=1

  

  

  

font

parent=0

  

  

  

rot

0

  

  

  

just

14

  

  

  

  

  

  

  

 Line  
(x1,y1,x2,y2,[color],[lwidth],[lstyl],

  

  

  

   

[arrow],[atyp],[algth],[alyo])

  

  

  

  

status

'on'

_ 'off'  _

  

  

loctype

'view'

_ 'world'  _

  

  

color

parent=1

  

  

  

linewidth

parent=1

  

  

  

linestyle

parent=1

  

  

  

 arrow  
  

  

  

  

  

status

'off'

_ 'on'  _

  

  

type

0

_ 0:'line',1:'filled',2:'opaque'  _

  

  

length

2

  

  

  

layout

[1.,1.]

  

  

x1

  

  

  

  

y1

  

  

  

  

x2

  

  

  

  

y2

  

  

  

  

xy

[x1,y1,x2,y2]

  

  

* * *

#  Sheet 7: _ Functions _

Function

Arguments

Return

Comment

Objecthelp

_ (object)  _

return object.__doc__,str(object)

_ return the doc and the print(object)  _

add_r

_ ()  _

None

_ Adds a region  _

list_font

_ ()  _

List of string

_ Return a list with the font names  _

add_font

_ (name)  _

None

_ Add a font, make sur it works with xmgrace first  _

add_color

_ (name)  _

None

_ Add a color object to x.Color  _

add_graph

_ ()  _

None

_ Add a graph to x.Graph list  _

creategraph

_ ()  _

None

_ Add a graph to x.Graph list  _

add_set

_ (color=-1,graph=0)  _

None

_ Add a set to x.Set list  _

  

_  
_

  

_ Color=-1, automatically use color=nset  _

  

_  
_

  

_ Graph sets the graph where to plot it  _

add_string

_ (x,y,text,color=-1,char_size=-1,font=-1,  _

None

_ Add a string to x.String  _

  

_ rot=0,just=14)  _

  

_ -1 means use x.attribute  _

add_line

_ (x1,y1,x2,y2,color=-1,lwidth=-1,lstyl=-1  _

None

_ Add a line to x.Line  _

  

_ arrow='off',atyp=0,algth=2,alyo=[1,1])  _

  

_ -1 means use x.attribute  _

read_parameter

_ (parameterfile)  _

None

_ Reads in a parameter file and applies it,DOESN'T update the x.attributes !
_

make_parameter

_ ()  _

List of strings

_ Creates a list of strings representing the parameter file of x  _

plot

_ (list of datasets)  _

None

_ Plot the datasets, must be in a list  _

  

_  
_

  

_ And each dataset must have a .getdimattribute(0,'values')  _

output

_ (fnm,out='PostScript')  _

None

_ Create an image file at the out format  _

ps,postscript

_ (fnm,[color='color'],[level='level2'],  _

None

_ Create a postscript file  _

  

_ [docdata='8bit'],[xoffset=0],[yoffset=0],[mediafeed='auto'],[hwresolution='o
ff'],[dpi=300])  _

  

_  
_

jpeg

_ (fnm,[color='color'],[optimize='off'],  _

_  
_

_ Create a jpeg file  _

  

_ [quality=75],[smoothing=0],[baseline='off'],[progressive='on'],[dct='islow']
,[dpi=72])  _

  

_  
_

pdf

_ (fnm,[pdf='1.3'],[compression=4],[dpi=72])  _

  

_ Create a pdf file  _

eps

_ (fnm,[color='color'],[level='level2'],[bbox='tight'],[docdata='8bit'],[dpi=3
00])  _

  

_ Create eps file  _

mif

_ (fnm,[dpi=72])  _

None

_ Create a metafile file  _

svg

_ (fnm,[dpi=72])  _

None

_  
_

pnm

_ (fnm,[format='ppm'],[rawbit='on'],[dpi=72])  _

None

_ Create a pnm file, format are: color='ppm',grayscale='pgm',bw='pbm'  _

png

_ (fnm,[interlaced='off'],[transparent='on'],[compression=4],[dpi=72]):  _

  

_ Create a png file  _

metafile

_ (fnm,[dpi=72])  _

None

_ Create a .gmf file  _

close

_ ()  _

None

_ Exit xmgrace  _

redraw

_ ()  _

None

_ Flush the xmgrace queue and redraw the plot  _

update

_ ()  _

None

_ Recreate the plot from the xmgrace object, looses all change made from the
GUI  _

command

_ (cmd)  _

None

_ Pass a command to the xmgrace interpreter, same as (cmd)  _

is_open

_ ()  _

1

_ Returns 1 if xmgrace is open, 0 if closed  _

exit

_ ()  _

None

_ Exit xmgrace (kill the pipe)  _

portrait

_ ()  _

None

_ Put the xmgrace template in portrait mode (i.e. Switch x and y dim if x>y)
_

landscape

_ ()  _

None

_ Put the xmgrace template in landscape mode (i.e. Switch x and y dim if y>x)
_

orientation

_ ()  _

None

_ Switch between portrait or landscape mode  _

col

_ (name)  _

String

_ Return the color index for the color name passed (as a string)  _

lin

_ (name)  _

String

_ Return the xmgrace value for the line type you passed (as a string)  _

whichsets

_ (list_of_graph)  _

List of integer

_ Return all the sets associated with the Graph(s) you passed  _

list

_ ()  _

None
