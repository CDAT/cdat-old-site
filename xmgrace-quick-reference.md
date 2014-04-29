---
layout: default
title: xmgrace quick reference
---

##Xmgrace Quick Reference - html
Quick Reference to Xmgrace: Types: fonts, lines, colors, symbols; xmgrace;
graph; axes; sets; functions; others.

###Sheet 1: Types

\# | Fonts | Lines | Type
--- | --- | --- | ---
1 | Times-Roman | 1 | full
2 | Times-Italic | 2 | dot
3 | Times-BoldItalic | 3 | dash
4 | Helvetica | 4 | longdash
5 | Helvetica-Oblique | 5 | dot-dash
6 | Helvetica-Bold | 6 | dot-longdash
7 | Helvetica-BoldOblique | 7 | dot-dot-dash
8 | Courirer | 8 | dot-dash-dash
9 | Courier-Oblique | |
10 |Courier-Bold | | 
11 | Courier-BoldOblique | | 
12 | Symbol | |
13 | ZapfDingbats | | 

\# | Colors | \# | Symbols
0 | white | 0 | none
1 | black | 1 | circle
2 | red | 2 | square
3 | green | 3 | diamond
4 | blue | 4 | triangle up
5 | yellow | 5 | triangle left
6 | brown | 6 | triangle down
7 | grey  | 7 | triangle right
8 | violet | 8 | plus
9 | cyan | 9 | X
10 | magenta | 10 | star
11 | orange | 11 | char
12 | indigo
13 | maroon
14 | turquoise
15 | green4


###Sheet 2: Xmgrace

**Xmgrace | | 
Graph | See details | It's list of graph objects
ngraph | 1 | # of graphs
Set | See details | 
nset | 1 | # of sets
Font | See details 
nfont | 14
lfont | 
Colors | See details
ncolor
String | See details
nstring
Line | See details
nlne
version | 50102 | Xmgrace version
pyversion | 1.1.3b | Python module version
link_page | Off
linewidth | 1
linestyle | 1 
color | 1
pattern | 1
font | 0
char_size | 1
symbol_size | 1
sformat | %16.8g
background_color | 0
R | See details
nr | 0 | # of regions
**page** | | 
x | 792 | pixels
y | 612 | 
scroll | 5
inout | 5
background_fill | on | off
**timestamp** | | 
status | off | on
x | 0.03 
y | 0.03
color | 1  
rot | 0
font | 0
char_size | 1
default | Mon Oct 18 16:55:50 1999
**date** | | 
reference | 0
**wrap** | | 
status | off | on
year | 1950 | 


###Sheet 3: Graph
 Graph
_ (parent='xmgrace object,ymin,ymax,xmin,xmax)_
xmin
''
_ not recommended, just for backward compatibily_
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
_ In % of page_
vxmax
0.85
_ "_
vymin
0.15
_ "_
vymax
0.85
_ "_
status
'on'
_ 'off'_
hidden
'false'
_ 'true'_
type
'xy'
_ ' chart','polar','pie','smith','fixed'_
stacked
'false'
_ 'true'_
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
_ 'on'_
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
_ from xmgrace object_
size
1.5
_
_
color
parent=1
_ from xmgrace object_
 stit
_
_
font
parent=0
_ from xmgrace object_
size
1
_
_
color
parent=1
_ from xmgrace object_
 Set
It's a list of set object, associated with the graph
_
_
see special sheet
_
_
 x/yaxis
_ Identical for 'xaxis and 'yaxis_
 
see special sheet
_
_
 legend
status
'on'
_ 'off'_
loctype
'view'
_ 'world'_
x
0.85
_ % of the page_
y
0.8
_ % of the page_
 box
color
parent=1
_ from xmgrace object_
pattern
parent=1
_ from xmgrace object_
linewidth
parent=1
_ from xmgrace object_
linestyle
parent=1
_ from xmgrace object_
fcolor
0
fpattern
parent=1
_ from xmgrace object_
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
_ 'true'_
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
#Sheet 4: _ Axes _
 x/yaxis
 
 
_ Identical for 'xaxis and 'yaxis_
 
 
label
'
scale
'normal'
_ 'logarithmic','Reciprocal'_
Invert
'off'
_ 'on'_
status
'false'
_
_
zero
'false'
_ 'true'_
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
_ you can pass the xoffset and yoffset values here instead_
altaxis
'off'
_ 'on'_
min
0
_ can be changed when creating the graph_
max
1
"
 
 bar
 
 
 
 
status
'on'
_ 'off'_
color
parent=1
_ from xmgrace object_
linestyle
parent=1
_ from xmgrace object_
linewidth
parent=1
_ from xmgrace object_
_
_
 
 lbl
 
 
 _ 
_ 
 
layout
'para'
_ 'perp' (// or perpendicular)_
char_size
parent=1
_ from xmgrace object_
font
parent=0
_ from xmgrace object_
color
parent=1
_ from xmgrace object_
 
 
 place
 
 
 
loc
'auto'
side
'normal'
_ 'oposite', 'both' : where to put the labels_
 
 tick
 
 
 
 
status
'on'
_ 'off'_
inc
0.5
_ # or whatever increment value (i.e. Every 0.5 here)_
minor_ticks
1
_ # of sub tickmarks between the major ones_
place_rounded
'true'
_ 'false'_
nsub
6
_ # autotick division (for place rounded ?)_
orientation
'in'
_ 'out','both'_
place
'normal'
_ 'oposite','both'_
 
 
 spec
 
 
 
loc
[]
_ list of loc for ticks or dictionary: loc/label_
values
[]
_ labels(values) list to write at each loc or dic_
type
'both'
_ 'none','ticks'_
 
 
 major
 
 
 
size
1
color
parent=1
_ from xmgrace object_
linewidth
parent=1
_ from xmgrace object_
linestyle
parent=1
_ from xmgrace object_
grid
'off'
_ 'on', draw the grid lines_
 
 
 minor
 
 
 _ 
_ 
size
0.5
_
_
color
parent=1
_ from xmgrace object_
linewidth
parent=1
_ from xmgrace object_
linestyle
parent=1
_ from xmgrace object_
'grid'
'off'
_ 'on', draw the grid lines_
 
 
 label
 
 
 _ 
_ 
status
'on'
_ 'off'_
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
_ 'opposite','both'_
offset
'auto'
_ [0.,0.], // and perpendicular offsets_
sign
'normal'
_
_
start
'auto'
_ or value_
stop
'auto'
_ or value_
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
_ 'spec','zmean' (for area weighted zonal mean betw -1 and 1)_
alt
'off'
'on'
* * *
#Sheet 5: _ Set _
 Set
graph
0
_ can be passed at creation time_
hidden
'false'
_ 'true'_
type
'xy'
_ xydx','xydy','xydxdx','xydydy','xydxdy','xydxdxdydy','bar','bardy','bardydy
_
_ 'xyhilo','xyz','xyr','xysize','xycolor','xycolpat','xyvmap','xyboxplot'_
 symbol
type
0
size
parent=symbol_size=1
_
_
_ from xmgrace object_
color
parent=background_color=0
_
_
_ from xmgrace object_
pattern
parent=1
_ from xmgrace object_
fcolor
parent=1
_ can be passed at creation time_
fpattern
parent=1
_ from xmgrace object_
linestyle
parent=1
_ from xmgrace object_
linewidth
parent=1
_ from xmgrace object_
char
65
_
_
char_font
parent=0
_ from xmgrace object_
skip
0
 line
type
1
linestyle
parent=1
_ from xmgrace object_
linewidth
parent=1
_ from xmgrace object_
color
parent=1
_ can be passed at creation time_
pattern
parent=1
_ from xmgrace object_
 baseline
type
0
status
'off'
_ 'on'_
dropline
'off'
_ 'on'_
 fill
type
0
_ 0:'none',1:'as polygone',2:'to baseline'_
# only, no string allowed
rule
0
_ 0:'winding',1:'even-odd'_
# only, no string allowed
color
parent=1
_ can be passed at creation time_
pattern
parent=1
_ from xmgrace object_
 avalue
status
'off'
_ 'on'_
type
2
_
_
char_size
parent=1
_ from xmgrace object_
font
parent=0
_ from xmgrace object_
color
parent=1
_ can be passed at creation time_
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
_ you can pass the xoffset and yoffset values here instead_
 error
_
_
status
'off'
_ 'on'_
type
'both'
_ 'normal','opposite'_
length
1
linewidth
parent=1
_ from xmgrace object_
linsestyle
parent=1
_ from xmgrace object_
 riser
linewidth
parent=1
_ from xmgrace object_
linsestyle
parent=1
_ from xmgrace object_
* * *
#Sheet 6: _ Others _
 Color
(name)
name
'black'
_ can pass any name_
rgb
[0,0,0]
_ red green blue values_
change()
_ function to change the color, expect a name then reset rgb's_
 Region
_
_
status
'off'
_ 'on'_
type
'above'
_ 'polyi','polyo','above','below','left','right','horizi','horizo','veri','ver
to'_
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
_ list of [x,y] coordinates to def the polygone_
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
_ 'off'_
xy
[x,y]
_
_
loctype
'view'
_ 'world'_
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
_ 'off'_
loctype
'view'
_ 'world'_
color
parent=1
linewidth
parent=1
linestyle
parent=1
 arrow
status
'off'
_ 'on'_
type
0
_ 0:'line',1:'filled',2:'opaque'_
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
#Sheet 7: _ Functions _
Function
Arguments
Return
Comment
Objecthelp
_ (object)_
return object.__doc__,str(object)
_ return the doc and the print(object)_
add_r
_ ()_
None
_ Adds a region_
list_font
_ ()_
List of string
_ Return a list with the font names_
add_font
_ (name)_
None
_ Add a font, make sur it works with xmgrace first_
add_color
_ (name)_
None
_ Add a color object to x.Color_
add_graph
_ ()_
None
_ Add a graph to x.Graph list_
creategraph
_ ()_
None
_ Add a graph to x.Graph list_
add_set
_ (color=-1,graph=0)_
None
_ Add a set to x.Set list_
_
_
_ Color=-1, automatically use color=nset_
_
_
_ Graph sets the graph where to plot it_
add_string
_ (x,y,text,color=-1,char_size=-1,font=-1,_
None
_ Add a string to x.String_
_ rot=0,just=14)_
_ -1 means use x.attribute_
add_line
_ (x1,y1,x2,y2,color=-1,lwidth=-1,lstyl=-1_
None
_ Add a line to x.Line_
_ arrow='off',atyp=0,algth=2,alyo=[1,1])_
_ -1 means use x.attribute_
read_parameter
_ (parameterfile)_
None
_ Reads in a parameter file and applies it,DOESN'T update the x.attributes !
_
make_parameter
_ ()_
List of strings
_ Creates a list of strings representing the parameter file of x_
plot
_ (list of datasets)_
None
_ Plot the datasets, must be in a list_
_
_
_ And each dataset must have a .getdimattribute(0,'values')_
output
_ (fnm,out='PostScript')_
None
_ Create an image file at the out format_
ps,postscript
_ (fnm,[color='color'],[level='level2'],_
None
_ Create a postscript file_
_ [docdata='8bit'],[xoffset=0],[yoffset=0],[mediafeed='auto'],[hwresolution='o
ff'],[dpi=300])_
_
_
jpeg
_ (fnm,[color='color'],[optimize='off'],_
_
_
_ Create a jpeg file_
_ [quality=75],[smoothing=0],[baseline='off'],[progressive='on'],[dct='islow']
,[dpi=72])_
_
_
pdf
_ (fnm,[pdf='1.3'],[compression=4],[dpi=72])_
_ Create a pdf file_
eps
_ (fnm,[color='color'],[level='level2'],[bbox='tight'],[docdata='8bit'],[dpi=3
00])_
_ Create eps file_
mif
_ (fnm,[dpi=72])_
None
_ Create a metafile file_
svg
_ (fnm,[dpi=72])_
None
_
_
pnm
_ (fnm,[format='ppm'],[rawbit='on'],[dpi=72])_
None
_ Create a pnm file, format are: color='ppm',grayscale='pgm',bw='pbm'_
png
_ (fnm,[interlaced='off'],[transparent='on'],[compression=4],[dpi=72]):_
_ Create a png file_
metafile
_ (fnm,[dpi=72])_
None
_ Create a .gmf file_
close
_ ()_
None
_ Exit xmgrace_
redraw
_ ()_
None
_ Flush the xmgrace queue and redraw the plot_
update
_ ()_
None
_ Recreate the plot from the xmgrace object, looses all change made from the
GUI_
command
_ (cmd)_
None
_ Pass a command to the xmgrace interpreter, same as (cmd)_
is_open
_ ()_
1
_ Returns 1 if xmgrace is open, 0 if closed_
exit
_ ()_
None
_ Exit xmgrace (kill the pipe)_
portrait
_ ()_
None
_ Put the xmgrace template in portrait mode (i.e. Switch x and y dim if x>y)
_
landscape
_ ()_
None
_ Put the xmgrace template in landscape mode (i.e. Switch x and y dim if y>x)
_
orientation
_ ()_
None
_ Switch between portrait or landscape mode_
col
_ (name)_
String
_ Return the color index for the color name passed (as a string)_
lin
_ (name)_
String
_ Return the xmgrace value for the line type you passed (as a string)_
whichsets
_ (list_of_graph)_
List of integer
_ Return all the sets associated with the Graph(s) you passed_
list
_ ()_
None
