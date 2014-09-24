---
layout: default
title: VCS Chapter 5
---
##  CHAPTER 5 VCS Command Reference Guide

If you want the full description of a command, then you've made it to the
right place.

Note, in the "Options" column, any item(s) surrounded by "[]" are optional to
the function.



Command

Description

Options

Examples

Initializing

init

Function: init  
# Initialize, Construct a VCS Canvas Object



Description of Function:

Construct the VCS Canas object. There can only be at most 8 VCS Canvases open
at any given time.



Example of Use:

import vcs,cu



file=cu.open(`filename.nc')

slab=file.getslab(`variable')

a=vcs.init()  
# This examples constructs 4 VCS Canvas a.plot(slab)  
# Plot slab using default settings

b=vcs.init()  
# Construct VCS object

template=b.gettemplate(`AMIP')  
# Get `example' template object

b.plot(slab,template)  
# Plot slab using template `AMIP'

c=vcs.init()  
# Construct new VCS object

isofill=c.getisofill(`quick')  
# Get `quick' isofill graphics method

c.plot(slab,template,isofill)  
# Plot slab using template and isofill objects

d=vcs.init()  
# Construct new VCS object

isoline=c.getisoline(`quick')

  
# Get `quick' isoline graphics method

c.plot(isoline,slab,template)  
# Plot slab using isoline and template objects

Help Commands

help

Function: help  
# On-Line HELP!!!



Description of Function:

Gives insight to other VCS functions by providing a description and at least
one example.



Example of Use:

import vcs



vcs.help()

vcs.help(`init')

vcs.help(`plot')

objecthelp

Function: objecthelp  
# Print out the object's doc string



Description of Function:

Print out information on VCS objects. See example on its use.



Example of Use:

import vcs

a=vcs.init()

ln=a.getline('red')  
# Get a VCS line object

a.objecthelp(ln)  
# This will print out information on how to use ln

Canvas

mode

Function: mode  
# Update the VCS Canvas.



Description of Function:

Updating of the graphical displays on the VCS Canvas can be deferred until a
later time. This is helpful when generating templates or displaying numerous
plots. If a series of commands are given to VCS and the Canvas Mode is set to
manual (i.e., 0), then no updating of the VCS Canvas occurs until the 'update'
function is executed.

Note, by default the VCS Canvas Mode is set to `Automatic', which means VCS
will update the VCS Canvas as necessary without prompting from the user.

1|0



1 = automatic

0=manual

Example of Use:

import vcs

...

a=vcs.init()

a.mode=0  
# Set updating to manual mode

a.plot(array,'default','boxfill','quick')

box=x.getboxfill('quick')

box.color_1=100

box.xticlabels('lon30','lon30')

box.xticlabels('','')

box.datawc(1e20,1e20,1e20,1e20)

box.datawc(-45.0, 45.0, -90.0, 90.0)

...

a.update()  
# Update the changes manually

update

Function: update



Description of Function:

If a series of commands are given to VCS and the Canvas Mode is set to manual,
then use this function to update the VCS Canvas manually.



Example of Use:

import vcs

...

a=vcs.init()

a.mode=0  
# Go to manual mode a.plot(s,'default','boxfill','quick')

box=x.getboxfill('quick')

box.color_1=100

box.xticlabels('lon30','lon30')

box.xticlabels('','')

box.datawc(1e20,1e20,1e20,1e20)

box.datawc(-45.0, 45.0, -90.0, 90.0)

a.update()  
# Update the changes manually

open

Function: open



Description of Function:

Open VCS Canvas object. This routine really just manages the VCS canvas. It
will popup the VCS Canvas for viewing. It can be used to display the VCS
Canvas.



Example of Use:

import vcs

a=vcs.init()

a.open()

close

Function: close



Description of Function:

Close the VCS Canvas. It will remove the VCS Canvas object from the screen,
but not deallocate it.



Example of Use:

import vcs

a=vcs.init()

a.plot(array,'default','isofill','quick')

a.close()

portrait

Function: portrait



Description of Function:

Change the VCS Canvas orientation to Portrait.



Example of Use:

a=vcs.init()

a.plot(array)

a.portrait()  
# Change the VCS Canvas orientation and set object flag to portrait

landscape

Function: landscape



Description of Function:

Change the VCS Canvas orientation to Landscape.



Example of Use:

a=vcs.init()

a.plot(array)

a.landscape()  
# Change the VCS Canvas orientation and set object flag to landscape

page

Function: page



Description of Function:

Change the VCS Canvas orientation to either 'portrait' or 'landscape'.

The orientation of the VCS Canvas and of cgm and raster images is controlled
by the PAGE command. Only portrait (y > x) or landscape (x > y) orientations
are permitted.



Example of Use:

a=vcs.init()

a.plot(array)

a.page()  
# Change the VCS Canvas orientation and set object flag to portrait

geometry

Function: geometry



Description of Function:

The geometry command is used to set the size and position of the VCS canvas.

(w,h,x,y), where w=width, h=height, x=x_position, y=y_position

Example of Use:

a=vcs.init()

a.plot(array,'default','isofill','quick')

a.geometry(450, 337,100, 100)

Printing and Saving Graphics

printer

Function: printer  
# Send plots to the printer



Description of Function:

This function creates a temporary cgm file and then sends it to the specified
printer. Once the printer received the information, then the temporary cgm
file is deleted. The temporary cgm file is created in the user's
PCMDI_GRAPHICS directory.

The PRINTER command is used to send the VCS Canvas plot(s) directly to the
printer.

Note: VCS graphical displays can be printed only if the user customizes a
HARD_COPY file (included with the VCS software) for the home system. The path
to the HARD_COPY file must be:

/$HOME/PCMDI_GRAPHICS/HARD_COPY

where /$HOME denotes the user's home directory.

For more information on the HARD_COPY file, see URL:



http://www-pcmdi.llnl.gov/software/vcs/vcs_guidetoc.html  
#1.Setup

printer's name



l|p -

Orientation can be either: 'l' = landscape, or 'p' = portrait.

Example of Use:

import vcs

a=vcs.init()

a.plot(array)

a.printer('printer_name')  
# Send plot(s) to postscript printer

a.printer(`printer_name','p')  
# Send plot(s) to the printer in portrait mode

gif

Function: gif  
# Save plot(s) as gif image



Description of Function:

In some cases, the user may want to save the plot out as a gif image. This
routine allows the user to save the VCS canvas output as a gif file.

This file can be converted to other gif formats with the aid of xv and other
such imaging tools found freely on the web.

If no path/file name is given and no previously created gif file has been

designated, then file

/$HOME/PCMDI_GRAPHICS/default.gif

will be used for storing gif images. However, if a previously created gif file
is designated, that file will be used for gif output.

By default, the page orientation is in Landscape mode (l). To translate the
page orientation to portrait mode (p), enter 'p' as the second parameter.

The GIF command is used to create or append to a gif file. There are two modes
for saving a gif file: `Append' mode (a) appends gif output to an existing gif
file(i.e., making it an animated gif); `Replace' (r) mode overwrites an
existing gif file with new gif output.

gif file name



`a'=will append (or merge) image to an existing file, making it an animated
gif

`r'=will replace file with new image

`l'=landscape mode

`p'=portrait mode

Example of Use:

import vcs

a=vcs.init()

a.plot(array)

# Note, if you don't specify the extension `.gif' at the end of file name,
then the extension `.gif' will be put on for you.

a.gif('example')  
# merge gif image into existing gif file

a.gif('example','r')  
# over write existing gif file

a.gif('example','a')  
# merge gif image into existing gif file

a.gif('example','a','p')  
# merge gif image into existing gif file with portrait orientation

a.gif('example.gif','r','p')  
# over write gif image file with new portrait orientation gif

postscript

Function: postscript  
# Save plot(s) to a postscript file



Description of Function:

Postscript output is another form of vector graphics. It is larger than its
CGM output counter part, because it is not stored out in ASCII format. To save
out a postscript file, VCS will first create a cgm file in the user's
PCMDI_GRAPHICS directory. Then it will use gplot to convert the cgm file to a
postscript file in the location the user has chosen.

postscript file name



`a'=will append postscript to an existing file

`r'=will replace postscript file with new apostscript file

Example of Use:

import vcs

a=vcs.init()

a.plot(array)

# Note, if you don't specify the extension `.ps' at the end of file name, then
the extension `.ps' will be put on for you.

a.postscript('example')  
# Creates a landscape postscript file a.postscript('example','p')  
# Creates a portrait postscript file

cgm

Function: cgm



Description of Function:

To save a graphics plot in VCS the user can call CGM along with the name of
the output. This routine will save the displayed image on the VCS canvas as a
binary vector graphics that can be imported into MSWord or Framemaker. CGM
files are in ISO standards output format.

The CGM command is used to create or append to a cgm file. There are two modes
for saving a cgm file: `Append' mode (a) appends cgm output to an existing cgm
file; `Replace' (r) mode overwrites an existing cgm file with new cgm output.

cgm file name



`a'=will append cgm to an existing file

`r'=will replace cgm file with a new cgm file

Example of Use:

a=vcs.init()

a.plot(array,'default','isofill','quick')

# Note, if you don't specify the extension `.cgm' at the end of file name,
then the extension `.cgm' will be put on for you.

a.cgm(o)

a.cgm('example')  
# by default a cgm file will be appended it an existing file

a.cgm('example','a')  
# 'a' will instruct cgm to append to an existing file

a.cgm('example','r')  
# 'r' will instruct cgm to over write an existing file

raster

Function: raster



Description of Function:

In some cases, the user may want to save the plot out as an raster image. This
routine allows the user to save the VCS canvas output as a SUN raster file.

This file can be converted to other raster formats with the aid of xv and
other such imaging tools found freely on the web.

If no path/file name is given and no previously created raster file has
beendesignated, then file

/$HOME/PCMDI_GRAPHICS/default.ras

will be used for storing raster images. However, if a previously created
raster file is designated, that file will be used for raster output.

raster file name



`a'=will append raster image to an existing raster file

`r'=will replace a raster file with a new raster file



Example of Use:

import vcs

a=vcs.init()

a.plot(array)

# Note, if you don't specify the extension `.ras' at the end of file name,
then the extension `.ras' will be put on for you.

a.raster('example','a')  
# append raster image to existing file

a.raster('example','r')  
# over write existing raster file

pstogif

Function: pstogif



Description of Function:

This function allows the user to convert a postscript file to a gif file.

postscript file name

[`l'=landscape `p'=portrait]

Example of Use:

import vcs

a=vcs.init()

a.plot(array)

a.pstogif('filename.ps') # convert to landscape gif file

a.pstogif('filename.ps','l') # convert to landscape gif file

a.pstogif('filename.ps','p') # convert to portrait gif file

Plot and Clear Commands

plot

Function: plot



Description of Function:

Plot an array(s) of data given a template and graphics method. The VCS
template is used to define where the data and variable attributes will be
displayed on the VCS Canvas. The VCS graphics method is used to define how the
array(s) will be shown on the VCS Canvas.



The form of the call is:

plot(array1=None, array2=None, template_name=None,
graphics_method=None,graphics_name=None, [key=value [, key=value [, ...]]])
where array1 and array2 are NumPy arrays, such that 2<=rank(ar)<=5.



See section 4.5.1 for a detail listing of possible plot options.

Example of Use:

import vcs

x=vcs.init()  
# x is an instance of the VCS class object (constructor)

x.plot(array)  
# this call will use default settings for template and boxfill

x.plot(array, 'AMIP', 'isofill','AMIP_psl')  
# this is specifying the template and graphics method

t=x.gettemplate('AMIP')  
# get a predefined the template 'AMIP'

vec=x.getvector('quick')  
# get a predefined the vector graphics method 'quick'

x.plot(array1, array2, t, vec)  
# plot the data as a vector using the 'AMIP' template

x.clear()  
# clear the VCS Canvas of all plots

box=x.createboxfill('new')  
# create boxfill graphics method 'new'

x.plot(box,t,array)  
# plot array data using box 'new' and template 't'

boxfill

Function: boxfill  
# Generate a boxfill plot



Description of Function:

Generate a boxfill plot given the data, boxfill graphics method, and template.
If no boxfill class object is given, then the 'default' boxfill graphics
method is used. Similarly, if no template class object is given, then the
'default' template is used.

See plot command for options.

Example of Use:

import vcs

a=vcs.init()

a.show('boxfill')  
# Show all the existing boxfill graphics methods

box=a.getboxfill('quick')  
# Create instance of 'quick'

a.boxfill(array,box)  
# Plot array using specified box and default template

templt=a.gettemplate('AMIP')  
# Create an instance of template 'AMIP'

a.clear()  
# Clear VCS canvas

a.boxfill(array,box,template)  
# Plot array using specified box and template

a.boxfill(box,array,template)  
# Plot array using specified box and template

a.boxfill(template,array,box)  
# Plot array using specified box and template

a.boxfill(template,array,box)  
# Plot array using specified box and template

a.boxfill(array,'AMIP','quick')  
# Use 'AMIP' template and 'quick' boxfill

a.boxfill('AMIP',array,'quick')  
# Use 'AMIP' template and 'quick' boxfill

a.boxfill('AMIP','quick',array)  
# Use 'AMIP' template and 'quick' boxfill

continents

Function: continents  
# Generate a continents plot



Description of Function:

Generate a continents plot given the continents graphics method, and template.
If no continents class object is given, then the 'default' continents graphics
method is used. Similarly, if no template class object is given, then the
'default' template is used.

See plot command for options.

Example of Use:

import vcs

a=vcs.init()

a.show('continents')  
# Show all the existing continents graphics methods

con=a.getcontinents('quick')  
# Create instance of 'quick'

a.continents(array,con)  
# Plot array using specified con and default template

a.clear()  
# Clear VCS canvas

a.continents(array,con,template)  
# Plot array using specified con and template

isofill

Function: isofill  
# Generate an isofill plot



Description of Function:

Generate a isofill plot given the data, isofill graphics method, and template.
If no isofill class object is given, then the 'default' isofill graphics
method is used. Similarly, if no template class object is given, then the
'default' template is used.

See plot command for options.

Example of Use:

import vcs

a=vcs.init()

a.show('isofill')  
# Show all the existing isofill graphics methods

iso=a.getisofill('quick')  
# Create instance of 'quick'

a.isofill(array,iso)  
# Plot array using specified iso and defaul template

a.clear()  
# Clear VCS canvas

a.isofill(array,iso,template)  
# Plot array using specified iso and template

isoline

Function: isoline  
# Generate an isoline plot



Description of Function:

Generate a isoline plot given the data, isoline graphics method, and template.
If no isoline class object is given, then the 'default' isoline graphics
method is used. Similarly, if no template class object is given, then the
'default' template is used.

See plot command for options.

Example of Use:

a=vcs.init()

a.show('isoline')  
# Show all the existing isoline graphics methods

iso=a.getisoline('quick')  
# Create instance of 'quick'

a.isoline(array,iso)  
# Plot array using specified iso and default template

a.clear()  
# Clear VCS canvas a.isoline(array,iso,template)  
# Plot array using specified iso and template

outfill

Function: outfill  
# Generate an outfill plot



Description of Function:

Generate a outfill plot given the data, outfill graphics method, and template.
If no outfill class object is given, then the 'default' outfill graphics
method is used. Similarly, if no template class object is given, then the
'default' template is used.

See plot command for options.

Example of Use:

a=vcs.init()

a.show('outfill')  
# Show all the existing outfill graphics methods

out=a.getoutfill('quick')  
# Create instance of 'quick'

a.outfill(array,out)  
# Plot array using specified out and default template

a.clear()  
# Clear VCS canvas

a.outfill(array,out,template)  
# Plot array using specified out and template

outline

Function: outline  
# Generate an outline plot



Description of Function:

Generate a outline plot given the data, outline graphics method, and template.
If no outline class object is given, then the 'default' outline graphics
method is used. Similarly, if no template class object is given, then the
'default' template is used.

See plot command for options.

Example of Use:

import vcs

a=vcs.init()

a.show('outline')  
# Show all the existing outline graphics methods

out=a.getoutline('quick')  
# Create instance of 'quick'

a.outline(array,out)  
# Plot array using specified out and default template

a.clear()  
# Clear VCS canvas a.outline(array,out,template)  
# Plot array using specified out and template

scatter

Function: scatter  
# Generate a scatter plot



Description of Function:

Generate a scatter plot given the data, scatter graphics method, and template.
If no scatter class object is given, then the 'default' scatter graphics
method is used. Similarly, if no template class object is given, then the
'default' template is used.

See plot command for options.

Example of Use:

a=vcs.init()

a.show('scatter')  
# Show all the existing scatter graphics methods

sct=a.getscatter('quick')  
# Create instance of 'quick'

a.scatter(array1,array2,sct)  
# Plot array using specified sct and default template

a.clear()  
# Clear VCS canvas

a.scatter(array1,array2,sct,template)  
# Plot array using specified sct and template

vector

Function: vector  
# Generate a vector plot



Description of Function:

Generate a vector plot given the data, vector graphics method, andtemplate. If
no vector class object is given, then the 'default' vectorgraphics method is
used. Similarly, if no template class object is given,then the 'default'
template is used.

See plot command for options.

Example of Use:

import vcs

a=vcs.init()

a.show('vector')  
# Show all the existing vector graphics methods

vec=a.getvector('quick')  
# Create instance of 'quick'

a.vector(array1,array2,vec)  
# Plot array using specified vec and default template

a.clear()  
# Clear VCS canvas

a.vector(array1,array2,vec,template)  
# Plot array using specified vec and template

xvsy

Function: xvsy  
# Generate a Xvsy plot



Description of Function:

Generate a XvsY plot given the data, XvsY graphics method, and template. If no
XvsY class object is given, then the 'default' XvsY graphics method is used.
Similarly, if no template class object is given, then the 'default' template
is used.

See plot command for options.

Example of Use:

import vcs

a=vcs.init()

a.show('xvsy')  
# Show all the existing XvsY graphics methods

xy=a.getxvsy('quick')  
# Create instance of 'quick'

a.xvsy(array1,array2,xy)  
# Plot array using specified xy and default template

a.clear()  
# Clear VCS canvas

a.xvsy(array1,array2,xy,template)  
# Plot array using specified xy and template

xyvsy

Function: xyvsy  
# Generate a Xyvsy plot



Description of Function:

Generate a Xyvsy plot given the data, Xyvsy graphics method, and template. If
no Xyvsy class object is given, then the 'default' Xyvsy graphics method is
used. Simerly, if no template class object is given, then the 'default'
template is used.



See plot command for options.

Example of Use:

import vcs

a=vcs.init()

a.show('xyvsy')  
# Show all the existing Xyvsy graphics methods

xyy=a.getxyvsy('quick')  
# Create instance of 'quick'

a.xyvsy(array,xyy)  
# Plot array using specified xyy and default template

a.clear()  
# Clear VCS canvas

a.xyvsy(array,xyy,template)  
# Plot array using specified xyy and template



yxvsx

Function: yxvsx  
# Generate a Yxvsx plot



Description of Function:

Generate a Yxvsx plot given the data, Yxvsx graphics method, and template. If
no Yxvsx class object is given, then the 'default' Yxvsx graphics method is
used. Simerly, if no template class object is given, then the 'default'
template is used.

See plot command for options.

Example of Use:

import vcs

a=vcs.init()

a.show('yxvsx')  
# Show all the existing Yxvsx graphics methods

yxx=a.getyxvsx('quick')  
# Create instance of 'quick'

a.yxvsx(array,yxx)  
# Plot array using specified yxx and default template

a.clear()  
# Clear VCS canvas

a.yxvsx(array,yxx,template)  
# Plot array using specified yxx and template

clear

Function: clear  
# Generate a Yxvsx plot



Description of Function:

At some point it will become necessary to clear all the plots from the VCS
Canvas. This routine will remove all plots on the VCS Canvas.



Example of Use:

import vcs

a=vcs.init()

a.plot(array,'default','isofill','quick')

a.clear()

Query Functions

graphicsmethodname

Function: graphicsmethodname



Description of Function:

Returns the grapics method's type string: boxfill, isofill, isoline, outfill,
outline, continents, scatter, vector, xvsy, xyvsy, or yxvsx.



Example of Use:

import vcs

a=vcs.init()

box=a.getboxfill() # Get an default boxfill

iso=a.getisofill() # Get default isofill

ln=a.getline() # Get default line

print a.graphicsmethodname(box) # Will

# print 'boxfill'

print a.graphicsmethodname(iso) # Will

# print 'isofill'

print a.graphicsmethodname(ln) # Will return

# None, because ln is not a

# graphics method

getcontinentstype

Function: getcontinentstype



Description of Function:

Return continents type from VCS. Remember the value can only be between 0 and
11.



Example of Use:

import vcs

a=vcs.init()

cont_type = a.getcontinentstype() # Get the

# continents type

isgraphicsmethod

Function: isgraphicsmethod



Description of Function:

Indicates if the entered argument is one of the following graphics methods:
boxfill, isofill, isoline, outfill, outline, continents, scatter, vector,
xvsy, xyvsy, yxvsx.

Returns a 1, which indicates true, if the argment is one of the above.

Otherwise, it will return a 0, indicating false.



Example of Use:

import vcs

a=vcs.init()

box=a.getboxfill('quick')  
# To Modify an existing boxfill use:

...

if a.isgraphicsmethod(box):

box.list()

isboxfill

Function: isboxfill



Description of Function:

Check to see if an object is a VCS primary boxfill graphics method object.

Returns a 1 if the argment true.

Otherwise, it will return a 0, indicating false.



Example of Use:

import vcs

a=vcs.init()

box=a.getboxfill("quick")  
# To Modify an existing boxfill object

...

if a.isboxfill(box):

box.list()

iscontinents

Function: iscontinents



Description of Function:

Check to see if an object is a VCS primary continents graphics method.

Returns a 1 if the argment true.

Otherwise, it will return a 0, indicating false.



Example of Use:

import vcs

a=vcs.init()

con=a.getcontinents("quick")  
# To Modify an existing continents object

...

if a.iscontinents(con):

con.list()



isisofill

Function: isisofill



Description of Function:

Check to see if an object is a VCS primary isofill graphics method.

Returns a 1 if the argment true.

Otherwise, it will return a 0, indicating false.



Example of Use:

import vcs

a=vcs.init()

iso=a.getisofill("quick")  
# To Modify an existing isofill object

...

if a.isisofill(iso):

iso.list()

isisoline

Function: isisoline



Description of Function:

Check to see if an object is a VCS primary isoline graphics method.

Returns a 1 if the argment true.

Otherwise, it will return a 0, indicating false.



Example of Use:

import vcs

a=vcs.init()

iso=a.getisoline("quick")  
# To Modify an existing isoline object

...

if a.isisoline(iso):

iso.list()

isoutfill

Function: isoutfill



Description of Function:

Check to see if this object is a VCS primary outfill graphics method.

Returns a 1 if the argment true.

Otherwise, it will return a 0, indicating false.



Example of Use:

import vcs

a=vcs.init()

out=a.getoutfill("quick")  
# To Modify an existing outfill object

...



if a.isoutfill(out):

out.list()



isoutline

Function: isoutline



Description of Function:

Check to see if an object is a VCS primary outline graphics method.

Returns a 1 if the argment true.

Otherwise, it will return a 0, indicating false.



Example of Use:

import vcs

a=vcs.init()

out=a.getoutline("quick")  
# To Modify an existing outline object

...

if a.isoutline(out):

out.list()

isvector

Function: isvector



Description of Function:

Check to see if an object is a VCS primary vector graphics method.

Returns a 1 if the argment true.

Otherwise, it will return a 0, indicating false.



Example of Use:

import vcs

a=vcs.init()

vec=a.getvector("quick")  
# To Modify an existing vector object

...

if a.isvector(vec):

vec.list()

isxvsy

Function: isxvsy



Description of Function:

Check to see if an object is a VCS primary xvsy graphics method.

Returns a 1 if the argment true.

Otherwise, it will return a 0, indicating false.



Example of Use:

import vcs

a=vcs.init()

xy=a.getxvsy("quick")  
# To Modify an existing xvsy object

...

if a.isxvsy(xy):

xy.list()

isxyvsy

Function: isxyvsy



Description of Function:

Check to see if an object is a VCS primary Xyvsy graphics method.

Returns a 1 if the argment true.

Otherwise, it will return a 0, indicating false.



Example of Use:

import vcs

a=vcs.init()

xyy=a.getxyvsy("quick")  
# To Modify an existing Xyvsy object

...

if a.isxyvsy(xyy):

xyy.list()

isyxvsx

Function: isyxvsx



Description of Function:

Check to see if an object is a VCS primary yxvsx graphics method.

Returns a 1 if the argment true.

Otherwise, it will return a 0, indicating false.



Example of Use:

a=vcs.init()

yxx=a.getyxvsx("quick")  
# To Modify an existing yxvsx object

...

if a.isyxvsx(yxx):

yxx.list()

istemplate

Function: istemplate



Description of Function:

Indicates if the entered argument a template.

Returns a 1 if the argment true.

Otherwise, it will return a 0, indicating false.



Example of Use:

a=vcs.init()

templt=a.gettemplate('quick')  
# Modify an existing template named 'quick'

...

if a.istemplate(templt):

templt.list()  
# If it is a template then list its members

issecondaryobject

Function: issecondaryobject



Description of Function:

In addition, detailed specification of the primary elements' (or primary class
elements'), attributes is provided by eight secondary elements or (secondary
class elements):

1.) colormap: specification of combinations of 256 available colors

2.) fill area: style, style index, and color index

3.) format: specifications for converting numbers to display strings

4.) line: line type, width, and color index

5.) list: a sequence of pairs of numerical and character values

6.) marker: marker type, size, and color index

7.) text table: text font type, character spacing, expansion, and color index

8.) text orientation: character height, angle, path, and horizontal/vertical
alignment



Example of Use:

a=vcs.init()

line=a.getline('red')  
# To Modify an existing line object

...

if a.issecondaryobject(line):

box.list()

isfillarea

Function: isfillarea



Description of Function:

Check to see if an object is a VCS secondary fillarea.



Example of Use:

a=vcs.init()

fa=a.getfillarea("def37")  
# To Modify an existing fillarea object

...

if a.isfillarea(fa):

fa.list()

isline

Function: isline



Description of Function:

Check to see if this object is a VCS secondary line.



Example of Use:

a=vcs.init()

ln=a.getline("red")  
# To Modify an existing line object

...

if a.isline(ln):

ln.list()

ismarker

Function: ismarker



Description of Function:

Check to see if an object is a VCS secondary marker.



Example of Use:

a=vcs.init()

mk=a.getmarker("red")  
# To Modify an existing marker object

...

if a.ismarker(mk):

mk.list()

istextcombined

Function: istextcombined



Description of Function:

Check to see if an object is a VCS secondary text combined.



Example of Use:

a=vcs.init()

tc=a.gettextcombined("std", "7left")  
# To Modify existing text table and orientation objects

...

if a.istextcombined(tc):

tc.list()

if a.istexttable(tc):

tc.list()

if a.istextorientation(tc):

tc.list()

istextorientation

Function: istextorientation



Description of Function:

Check to see if an object is a VCS secondary text orientation.



Example of Use:

a=vcs.init()

to=a.gettextorientation("7left")  
# To Modify an existing text orientation object

...

if a.istextorientation(to):

to.list()

istexttable

Function: istexttable



Description of Function:

Check to see if an object is a VCS secondary text table.



Example of Use:

a=vcs.init()

tt=a.gettexttable("std")  
# To Modify an existing text table object

...

if a.istexttable(tt):

tt.list()

List Available Templates, Graphics Methods and Secondary Objects

listelements

Function: listelements



Description of Function:

Returns a Python list of all the VCS class objects.



Example of Use:

import vcs

a=vcs.init()

a.listelements()

show

Function: show



Description of Function:

Show the list of VCS primary and secondary class objects.



Example of Use:

import vcs

a=vcs.init()

a.show('boxfill')

a.show('isofill')

a.show(`template')

a.show('line')

a.show('marker')

Graphics Method Objects

Boxfill

createboxfill

Function: createboxfill



Description of Function:

Create a new boxfill graphics method given the name and the existingboxfill
graphics method to copy the attributes from. If no existing boxfill graphics
method name is given, then the default boxfill graphics method will be used as
the graphics method to which the attributes will be copied from.

If the name provided already exists, then a error will be returned. Graphics
method names must be unique.

new boxfill name



[name of boxfill to copy attributes from]

Example of Use:

import vcs

a=vcs.init()

a.show('boxfill')

box=a.createboxfill('example1')

a.show('boxfill')

box=a.createboxfill('example2','quick')

a.show('boxfill')

getboxfill

Function: getboxfill



Description of Function:

VCS contains a list of graphics methods. This function will create a boxfill
class object from an existing VCS boxfill graphics method. If no boxfill name
is given, then boxfill 'default' will be used.

Note, VCS does not allow the modification of `default' attribute sets.
However, a `default' attribute set that has been copied under a different name
can be modified. (See the createboxfill function.)

[boxfill name]

Example of Use:

import vcs

a=vcs.init()

a.show('boxfill')  
# Show all the existing boxfill graphics methods

box=a.getboxfill()  
# box instance of 'default' boxfill graphics method

box2=a.getboxfill('quick')  
# box2 instance of existing 'quick' boxfill graphics method



Object: boxfillobject



Description of Function:

The boxfill graphics method (Gfb) displays a two-dimensional data array by
surrounding each data value by a colored grid box.

This class is used to define a boxfill table entry used in VCS, or it can be
used to change some or all of the attributes in an existing boxfill table
entry. Other Useful Functions:

a=vcs.init()  
# Constructor a.show('boxfill')  
# Show predefined boxfill graphics methods

a.setcolormap("AMIP")  
# Change the VCS color map

a.boxfill(s,b,'default')  
# Plot data 's' with boxfill 'b' and 'default' template a.update()  
# Updates the VCS Canvas at user's request a.mode=1, or 0  
# If 1, then automatic update, else if 0, then use the update function to
update the VCS Canvas.

See Chapter 6 for additional information.

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

Example of Use:

import vcs

a=vcs.init()

  
# To Create a new instance of boxfill use:

box=a.createboxfill('new','quick')  
# Copies content of 'quick' to 'new'

box=a.createboxfill('new')  
# Copies content of 'default' to 'new'

  
# To Modify an existing boxfill use: box=a.getboxfill('AMIP_psl') box.list()  
# Will list all the boxfill attribute values

box.projection='linear'

lon30={-180:'180W',-150:'150W',0:'Eq'} box.xticlabels1=lon30
box.xticlabels2=lon30 box.xticlabels(lon30, lon30)  
# Will set them both

box.xmtics1=''

box.xmtics2=''

box.xmtics(lon30, lon30)  
# Will set them both

box.yticlabels1=lat10 box.yticlabels2=lat10

box.yticlabels(lat10, lat10)  
# Will set them both

box.ymtics1='' box.ymtics2='' box.ymtics(lat10, lat10)  
# Will set them both

box.datawc_y1=-90.0 box.datawc_y2=90.0 box.datawc_x1=-180.0
box.datawc_x2=180.0 box.datawc(-90,90,-180,180)  
box.exts('n', 'y' )  
# Will set them both









# Will set them all

xaxisconvert='linear'

yaxisconvert='linear'

box.xyscale('linear', 'area_wt')  
# Will set them both

level_1=1e20

level_2=1e20

box.levels(10, 90)  
# Will set them both

color_1=16

color_2=239

box.colors(16, 239 )  
# Will set them both

legend_type='VCS'

legend=''

ext_1='n'

ext_2='y'

missing=241  
# Color index value range 0 to 255



Continents

createcontinents

Function: createcontinents



Description of Function:

Create a new continents graphics method given the the name and the existing
continents graphics method to copy the attributes from. If no existing
continents graphics method name is given, then the default continents graphics
method will be used as the graphics method to which the attributes will be
copied from.

If the name provided already exists, then a error will be returned. Graphics
method names must be unique.

new continents name



[name of continents to copy attributes from]

Example of Use:

import vcs

a=vcs.init()

a.show('continents')

con=a.createcontinents('example1',)

a.show('continents')

con=a.createcontinents('example2','quick')

a.show('continents')

getcontinents

Function: getcontinents



Description of Function:

VCS contains a list of graphics methods. This function will create a
continents class object from an existing VCS continents graphics method. If no
continents name is given, then continents 'default' will be used.

Note, VCS does not allow the modification of `default' attribute sets.
However, a `default' attribute set that has been copied under a different name
can be modified. (See the createcontinents function.)

[continents name]

Example of Use:

import vcs

a=vcs.init()

a.show('continents')  
# Show all the existing continents graphics methods

con=a.getcontinents()  
# con instance of 'default' continents graphics method

con2=a.getcontinents('quick')  
# con2 instance of existing 'quick' continents graphics method



Object: continentsobject



Description of Function:

The Continents graphics method draws a predefined, generic set of continental
outlines in a longitude by latitude space. (To draw continental outlines, no
external data set is required.)

This class is used to define an continents table entry used in VCS, or it can
be used to change some or all of the continents attributes in an existing
continents table entry.

Other Useful Functions:

a=vcs.init()  
# Constructor

a.show('continents')  
# Show predefined boxfill graphics methods

a.show('line')  
# Show predefined line class objects

a.setcolormap("AMIP")  
# Change the VCS color map

a.continents(c,'default')  
# Plot continents, where 'c' is the defined continents object

a.update()  
# Updates the VCS Canvas at user's request a.mode=1, or 0. If 1, then
automatic update, else if 0, then use update function to update the VCS
Canvas.

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

Example of Use:

import vcs

a=vcs.init()

  
# To Create a new instance of continents use:

con=a.createcontinents('new','quick')  
#copies content of 'quick' to 'new'

con=a.createcontinents('new')  
# copies content of 'default' to 'new'

  
# To Modify an existing continents use:

con=a.getcontinents('AMIP_psl')

con.list()  
# Will list all the continents attribute values

con.projection='linear'

lon30={-180:'180W',-150:'150W',0:'Eq'}

con.xticlabels1=lon30

con.xticlabels2=lon30

con.xticlabels(lon30, lon30)  
# Will set them both

con.xmtics1=''

con.xmtics2=''

con.xmtics(lon30, lon30)  
# Will set them both

con.yticlabels1=lat10

con.yticlabels2=lat10

con.yticlabels(lat10, lat10)  
# Will set them both

con.ymtics1=''

con.ymtics2=''

con.ymtics(lat10, lat10)





See Chapter 6 for additional information.



# Will set them both

con.datawc_y1=-90.0

con.datawc_y2=90.0

con.datawc_x1=-180.0

con.datawc_x2=180.0

con.datawc(-90, 90, -180, 180) # Will set them all

# Specify the continents line style (or type):

con.line=0 # Same as con.line='solid'

con.line=1 # Same as con.line='dash'

con.line=2 # Same as con.line='dot'

con.line=3 # Same as con.line='dash-dot'

con.line=4 # Same as con.line='long-dash'

# There are three possibilities for setting the line #color indices (Ex):

con.linecolor=22 # Same as con.line-color=(22)

con.linecolor=([22])

# Will set the continents to a specific color index

con.linecolor=None # Turns off the line color index, defaults to Black



Isofill

createisofill

Function: createisofill



Description of Function:

Create a new isofill graphics method given the the name and the existing
isofill graphics method to copy the attributes from. If no existing isofill
graphics method name is given, then the default isofill graphics method will
be used as the graphics method to which the attributes will be copied from.

If the name provided already exists, then a error will be returned. Graphics
method names must be unique.

new isofill name



[name of isofill to copy attributes from]



Example of Use:

import vcs

a=vcs.init()

a.show('isofill')

iso=a.createisofill('example1',)

a.show('isofill')

iso=a.createisofill('example2','quick')

a.show('isofill')

getisofill

Function: getisofill



Description of Function:

VCS contains a list of graphics methods. This function will create a isofill
class object from an existing VCS isofill graphics method. If no isofill name
is given, then isofill 'default' will be used.

Note, VCS does not allow the modification of `default' attribute sets.
However, a `default' attribute set that has been copied under a different name
can be modified. (See the createisofill function.)

[continents name]



Example of Use:

import vcs

a=vcs.init()

a.show('isofill')  
# Show all the existing isofill graphics methods

iso=a.getisofill()  
# iso instance of 'default' isofill graphics method

iso2=a.getisofill('quick')  
# iso2 instance of existing 'quick' isofill graphics method



Object: isofillobject



Description of Function:

The Isofill graphics method fills the area between selected isolevels (levels
of constant value) of a two-dimensional array with a user-specified color. The
example below shows how to display an isofill plot on the VCS Canvas and how
to create and remove isofill isolevels.

This class is used to define an isofill table entry used in VCS, or it can be
used to change some or all of the isofill attributes in anexisting isofill
table entry.

Other Useful Functions:

a=vcs.init()  
# Constructor

a.show('isofill')  
# Show predefined isofill graphics methods

a.show('fillarea')  
# Show predefined fillarea objects

a.show('template')  
# Show predefined fillarea objects

a.setcolormap("AMIP")  
# Change the VCS color map

a.createtemplate('test')  
# Create a template

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

Example of Use:

import vcs

a=vcs.init()

  
# To Create a new instance of isofill use:

iso=a.createisofill('new','quick')  
# Copies content of 'quick' to 'new'

iso=a.createisofill('new')  
# Copies content of 'default' to 'new'

  
# To Modify an existing isofill use:

iso=a.getisofill('AMIP_psl')



iso.list()  
# Will list all the isofill attribute values

iso.projection='linear'

lon30={-180:'180W',-150:'150W',0:'Eq'}

iso.xticlabels1=lon30

iso.xticlabels2=lon30

iso.xticlabels(lon30, lon30)  
# Will set them both

iso.xmtics1=''

iso.xmtics2=''

iso.xmtics(lon30, lon30)  
# Will set them both

iso.yticlabels1=lat10

iso.yticlabels2=lat10

iso.yticlabels(lat10, lat10)  
# Will set them both

iso.ymtics1=''

iso.ymtics2=''

iso.ymtics(lat10, lat10)





a.createfillarea('fill') # Create a fillarea

a.gettemplate('AMIP') # Get an existing template

a.getfillarea('def37') # Get an existing fillarea

a.isofill(s,i,t) # Plot array 's' with isofill 'i' and template 't'

a.update() # Updates the VCS Canvas at user's request a.mode=1, or 0. If 1,
then automatic update,

else if 0, then use update function to update the VCS Canvas.

See Chapter 6 for additional information.



# Will set them both

iso.datawc_y1=-90.0

iso.datawc_y2=90.0

iso.datawc_x1=-180.0

iso.datawc_x2=180.0

iso.datawc(-90, 90, -180, 180) # Will set them all

xaxisconvert='linear'

yaxisconvert='linear'

iso.xyscale('linear', 'area_wt') # Will set them both

missing=241 # Color index value range 0 to 255

# There are two possibilities for setting the isofill levels:

# A) Levels are all contiguous (Examples):

iso.levels=([0,20,25,30,35,40],)

iso.levels=([0,20,25,30,35,40,45,50])

iso.levels=[0,20,25,30,35,40]

iso.levels=(0.0,20.0,25.0,30.0,35.0,40.0,50.0)

# B) Levels are not contiguous (Examples):

iso.levels=([0,20],[30,40],[50,60])

iso.levels=([0,20,25,30,35,40],[30,40],[50,60])

iso.fillareaindices=(7,fill,4,9,fill,15) # Set index using fillarea

fill.list() # list fillarea attributes

fill.style='hatch' # change style

fill.color=241 # change color

fill.index=3 # change style index



ext_1='n'







ext_2='y'

iso.exts('n', 'y' ) # Will set them both



There are three possibilities for setting the fillarea color indices (Ex):

iso.fillareacolors=([22,33,44,55,66,77])

iso.fillareacolors=(16,19,33,44)

iso.fillareacolors=None



There are three possibilities for setting the fillarea style (Ex):

iso.fillareastyle = 'solid'

iso.fillareastyle = 'hatch'

iso.fillareastyle = 'pattern'

There are two ways to set the fillarea hatch or pattern indices (Ex):

iso.fillareaindices=([1,3,5,6,9,20])

iso.fillareaindices=(7,1,4,9,6,15)

See using fillarea objects below!



Using the fillarea secondary object (Ex):

f=createfillarea('fill1')

To Create a new instance of fillarea use:

fill=a.createisofill('new','quick') # Copies 'quick' to 'new'

fill=a.createisofill('new') # Copies 'default' to 'new'



To Modify an existing isofill use:

fill=a.getisofill('def37')



Isoline

createisoline

Function: createisoline



Description of Function:

Create a new isoline graphics method given the the name and the existing
isoline graphics method to copy the attributes from. If no existing isoline
graphics method name is given, then the default isoline graphics method will
be used as the graphics method to which the attributes will be copied from.

If the name provided already exists, then a error will be returned.
Graphicsmethod names must be unique.

new isoline name



[name of isoline to copy attributes from]



Example of Use:

import vcs

a=vcs.init()

a.show('isoline')

iso=a.createisoline('example1',)

a.show('isoline')

iso=a.createisoline('example2','quick')

a.show('isoline')

getisoline

Function: getisoline



Description of Function:

VCS contains a list of graphics methods. This function will create a isoline
class object from an existing VCS isoline graphics method. If no isoline name
is given, then isoline 'default' will be used.

Note, VCS does not allow the modification of `default' attribute sets.
However, a `default' attribute set that has been copied under a different name
can be modified. (See the createisoline function.)

[isoline name]



Example of Use:

import vcs

a=vcs.init()

a.show('isoline')  
# Show all the existing isoline graphics methods

iso=a.getisoline()  
# iso instance of 'default' isoline graphics method

iso2=a.getisoline('quick')  
# iso2 instance of existing 'quick' isoline graphics method



Object: isolineobject



Description of Function:

The Isoline graphics method draws lines of constant value at specified levels
in order to graphically represent a two-dimensional array. It also labels the
values of these isolines on the VCS Canvas. The example below shows how to
plot isolines of different types at specified levels and how to create isoline
labels having user-specified text and line type and color.

This class is used to define an isoline table entry used in VCS, or it can be
used to change some or all of the isoline attributes in an existing isoline
table entry.

Other Useful Functions:

a=vcs.init()  
# Constructor

a.show('isoline')  
# Show predefined isoline graphics methods

a.show('line')  
# Show predefined VCS line objects



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

Example of Use:

import vcs

a=vcs.init()

  
# To Create a new instance of isoline use:

iso=a.createisoline('new','quick')  
# Copies content of 'quick' to 'new'

iso=a.createisoline('new')  
# Copies content of 'default' to 'new'

  
# To Modify an existing isoline use:

iso=a.getisoline('AMIP_psl')

iso.list()  
# Will list all the isoline attribute values

iso.projection='linear'

lon30={-180:'180W',-150:'150W',0:'Eq'}

iso.xticlabels1=lon30

iso.xticlabels2=lon30

iso.xticlabels(lon30, lon30)  
# Will set them both

iso.xmtics1=''

iso.xmtics2=''

iso.xmtics(lon30, lon30)  
# Will set them both

iso.yticlabels1=lat10

iso.yticlabels2=lat10

iso.yticlabels(lat10, lat10)  



a.update()  
# Updates the VCS Canvas at user's request

a.mode=1, or 0  
# If 1, then automatic update, else if 0, then use update function.

a.setcolormap("AMIP")  
# Change the VCS color map

a.isoline(s,a,'default')  
# Plot data 's' with isoline 'i' and 'default' template

tion to update the VCS Canvas.

See Chapter 6 for additional information.



# Will set them both

iso.datawc_y1=-90.0

iso.datawc_y2=90.0

iso.datawc_x1=-180.0

iso.datawc_x2=180.0

iso.datawc(-90, 90, -180, 180) # Will set them all

xaxisconvert='linear'

yaxisconvert='linear'

iso.xyscale('linear', 'area_wt') # Will set them both

# There are many possibilities ways to set the isoline values:

# A) As a list of tuples (Examples):

iso.level=[(23,32,45,50,76),]

iso.level=[(22,33,44,55,66)]

iso.level=[(20,0.0),(30,0),(50,0)]

iso.level=[(23,32,45,50,76), (35, 45, 55)]

# B) As a tuple of lists (Examples):

iso.level=([23,32,45,50,76],)

iso.level=([22,33,44,55,66])

iso.level=([23,32,45,50,76],)

iso.level=([0,20,25,30,35,40],[30,40],[50,60]

)

# C) As a list of lists (Examples):

iso.level=[[20,0.0],[30,0],[50,0]]

# D) As a tuple of tuples (Examples):

iso.level=((20,0.0),(30,0),(50,0),(60,0),(70,0))











# Note: a combination of a pair (i.e., (30,0) or [30,0]) represents

the isoline value plus it increment

value. Thus, to let VCS

generate "default" isolines enter the following:

iso.level=[[0,1e20]]  
# Same as iso.level=((0,1e20),)



Displaying isoline labels:

iso.label='y'  
# Same as iso.label=1, will display isoline labels

iso.label='n'  
# Same as iso.label=0, will turn isoline labels off

# color index

iso.linecolors=None # Turns off the line color index



There are three ways to specify the text or font number:

iso.text=(1,2,3,4,5,6,7,8,9) # Font numbers are between 1 and 9

iso.text=[9,8,7,6,5,4,3,2,1]

iso.text=([1,3,5,6,9,2])

iso.text=None # Removes the text settings

There are three possibilities for setting the text color indices (Ex.):

iso.textcolors=([22,33,44,55,66,77])

iso.textcolors=(16,19,33,44)

iso.textcolors=None # Turns off the text color index

Outfill

createoutfill

Function: createoutfill



Description of Function:

Create a new outfill graphics method given the the name and the existing
outfill graphics method to copy the attributes from. If no existing outfill
graphics method name is given, then the default outfill graphics method will
be used as the graphics method to which the attributes will be copied from.

If the name provided already exists, then a error will be returned. Graphics
method names must be unique.

new outfill name



[name of outfill to copy attributes from]



Example of Use:

import vcs

a=vcs.init()

a.show('outfill')

out=a.createoutfill('example1',)

a.show('outfill')

out=a.createoutfill('example2','quick')

a.show('outfill')

getoutfill

Function: getoutfill



Description of Function:

VCS contains a list of graphics methods. This function will create a outfill
class object from an existing VCS outfill graphics method. If no outfill name
is given, then outfill 'default' will be used.

Note, VCS does not allow the modification of `default' attribute sets.
However, a `default' attribute set that has been copied under a different name
can be modified. (See the createoutfill function.)

[outfill name]



Example of Use:

import vcs

a=vcs.init()

a.show('outfill')  
# Show all the existing outfill graphics methods

out=a.getoutfill()  
# out instance of 'default' outfill graphics method

out2=a.getoutfill('quick')  
# out2 instance of existing 'quick' outfill graphics method



Object: outfillobject



Description of Function:

The outfill graphics method fills a set of integer values in any data array.

Its primary purpose is to display continents by filling their area as defined
by a surface type array that indicates land, ocean, and sea-ice points. The
example below shows how to apply the outfill graphics method and how to modify

Fillarea and outfill attributes. Other Useful Functions:

a=vcs.init()  
# Constructor

a.show('outfill')  
# Show predefined outfill graphics methods

a.show('line')  
# Show predefined VCS line objects

a.setcolormap("AMIP")  
# Change the VCS color map

a.outfill(s,o,'default')  
# Plot data 's' with outfill 'o' and 'default' template

a.update()  
# Updates the VCS Canvas at user's request a.mode=1, or 0 . If 1, then
automatic update, else if 0, then use update function to update the VCS
Canvas.

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

Example of Use:

import vcs

a=vcs.init()

  
# To Create a new instance of outfill use:

out=a.createoutfill('new','quick')  
# Copies content of 'quick' to 'new'

out=a.createoutfill('new')  
# Copies content of 'default' to 'new'



  
# To Modify an existing outfill use:

out=a.getoutfill('AMIP_psl')

out.list()  
# Will list all the outfill attribute values

out.projection='linear'

lon30={-180:'180W',-150:'150W',0:'Eq'}

out.xticlabels1=lon30

out.xticlabels2=lon30

out.xticlabels(lon30, lon30)  
# Will set them both

out.xmtics1=''

out.xmtics2=''

out.xmtics(lon30, lon30)  
# Will set them both

out.yticlabels1=lat10

out.yticlabels2=lat10

out.yticlabels(lat10, lat10)



See Chapter 6 for additional information.



# Will set them both

out.datawc_y1=-90.0

out.datawc_y2=90.0

out.datawc_x1=-180.0

out.datawc_x2=180.0

out.datawc(-90, 90, -180, 180) # Will set them all

xaxisconvert='linear'

yaxisconvert='linear'

out.xyscale('linear', 'area_wt') # Will set them both

# Specify the outfill fill values:

out.outfill=([0,1,2,3,4]) # Same as below

out.outfill=(0,1,2,3,4) # Will specify the outfill values

# There are four possibilities for setting the color index (Ex):

out.fillareacolor=22 # Same as below

out.fillareacolor=(22) # Same as below

out.fillareacolor=([22]) # Will set the outfill to a specific color index

out.fillareacolor=None # Turns off the color index



Outline

createoutline

Function: createoutline



Description of Function:

Create a new outline graphics method given the the name and the existing
outline graphics method to copy the attributes from. If no existing outline
graphics method name is given, then the default outline graphics method will
be used as the graphics method to which the attributes will be copied from.

If the name provided already exists, then a error will be returned. Graphics
method names must be unique.

new outline name



[name of outline to copy attributes from]



Example of Use:

import vcs

a=vcs.init()

a.show('outline')

out=a.createoutline('example1',)

a.show('outline')

out=a.createoutline('example2','quick')

a.show('outline')

getoutline

Function: getoutline



Description of Function:

VCS contains a list of graphics methods. This function will create a outline
class object from an existing VCS outline graphics method. If no outline name
is given, then outline 'default' will be used.

Note, VCS does not allow the modification of `default' attribute sets.
However, a `default' attribute set that has been copied under a different name
can be modified. (See the createoutline function.)

[outline name]



Example of Use:

import vcs

a=vcs.init()

a.show('outline')  
# Show all the existing outline graphics methods

out=a.getoutline()  
# out instance of 'default' outline graphics method

out2=a.getoutline('quick')  
# out2 instance of existing 'quick' outline graphics method



Object: outlineobject



Description of Function:

The Outline graphics method outlines a set of integer values in any data
array.

Its primary purpose is to display continental outlines as defined by a surface

type array that indicates land, ocean, and sea-ice points. The example below

shows how to change such an outline by modifying its attributes.



Other Useful Functions:

a=vcs.init()  
# Constructor

a.show('outline')  
# Show predefined outline graphics methods

a.show('line')  
# Show predefined VCS line objects

a.setcolormap("AMIP")  
# Change the VCS color map

a.outline(s,o,'default')  
# Plot data 's' with outline 'o' and 'default' template

a.update()

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

Example of Use:

import vcs

a=vcs.init()

  
# To Create a new instance of outline use:

out=a.createoutline('new','quick')  
# Copies content of 'quick' to 'new'

out=a.createoutline('new')  
# Copies content of 'default' to 'new'



  
# To Modify an existing outline use:

out=a.getoutline('AMIP_psl')

out.list()  
# Will list all the outline attribute values

out.projection='linear'

lon30={-180:'180W',-150:'150W',0:'Eq'}

out.xticlabels1=lon30

out.xticlabels2=lon30

out.xticlabels(lon30, lon30)  
# Will set them both

out.xmtics1=''

out.xmtics2=''

out.xmtics(lon30, lon30)  
# Will set them both

out.yticlabels1=lat10

out.yticlabels2=lat10

out.yticlabels(lat10, lat10)  
# Will set them both

out.ymtics1=''

out.ymtics2=''

out.ymtics(lat10, lat10)  



# Updates the VCS Canvas at user's request a.mode=1, or 0 # If 1, then
automatic update, else if 0, then use u pdate function to update the VCS
Canvas.

See Chapter 6 for additional information.



# Will set them both

out.datawc_y1=-90.0

out.datawc_y2=90.0

out.datawc_x1=-180.0

out.datawc_x2=180.0

out.datawc(-90, 90, -180, 180) # Will set them all

xaxisconvert='linear'

yaxisconvert='linear'

out.xyscale('linear', 'area_wt') # Will set them both

# Specify the outline fill values:

out.outline=([0,1,2,3,4]) # Same as below

out.outline=(0,1,2,3,4) # Will specify the outline values

# Specify the outline line type:

out.line=0 # same as out.line = 'solid'

out.line=1 # same as out.line = 'dash'

out.line=2 # same as out.line = 'dot'

out.line=3

# same as out.line = 'dash-dot'

out.line=4 # same as out.line = 'long-dash'



# There are four possibilities for setting the line color index (Ex):

out.linecolor=22 # Same as below

# Same as below

out.linecolor=([22]) # Will set the outline to a specific color index

out.linecolor=None # Turns off the color index



Scatter

createscatter

Function: createscatter



Description of Function:

Create a new scatter graphics method given the the name and the existing
mscatter graphics method to copy the attributes from. If no existing scatter
graphics method name is given, then the default scatter graphics method will
be used as the graphics method to which the attributes will be copied from.

If the name provided already exists, then a error will be returned. Graphics
method names must be unique

new scatter name



[name of scatter to copy attributes from]



Example of Use:

import vcs

a=vcs.init()

a.show('scatter')

sct=a.createscatter('example1',)

a.show('scatter')

sct=a.createscatter('example2','quick')

a.show('scatter')

getscatter

Function: getscatter



Description of Function:

VCS contains a list of graphics methods. This function will create a scatter
class object from an existing VCS scatter graphics method. If no scatter name
is given, then scatter 'default' will be used.

Note, VCS does not allow the modification of `default' attribute sets.
However, a `default' attribute set that has been copied under a different name
can be modified. (See the createscatter function.)



[scatter name]



Example of Use:

import vcs

a=vcs.init()

a.show('scatter')  
# Show all the existing scatter graphics methods

sct=a.getscatter()  
# sct instance of 'default' scatter graphics method

sct2=a.getscatter('quick')  
# sct2 instance of existing 'quick' scatter graphics method





Object: scatterobject



Description of Function:

The Scatter graphics method displays a scatter plot of two 4-dimensional data
arrays, e.g. A(x,y,z,t) and B(x,y,z,t). The example below shows how to change
the marker attributes of a scatter plot.

This class is used to define an scatter table entry used in VCS, or it can be
used to change some or all of the scatter attributes in an existing scatter
table entry.

Other Useful Functions:

a=vcs.init()  
# Constructor

a.show('scatter')  
# Show predefined scatter graphics methods

a.show('marker')  
# Show predefined marker objects

a.setcolormap("AMIP")  
# Change the VCS color map

a.scatter(s1, s2, s,'default')  
# Plot data 's1' and 's2' with scatter 's' and 'default' template

a.update()  
# Updates the VCS Canvas at user's request a.mode=1, or 0. If 1, then
automatic update, else if 0, then use update function to update the VCS
Canvas.

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

Example of Use:

import vcs

a=vcs.init()

  
# To Create a new instance of scatter use:

sr=a.createscatter('new','quick')  
# copies content of 'quick' to 'new'

sr=a.createscatter('new')  
# copies content of 'default' to 'new'

  
# To Modify an existing scatter use:

sr=a.getscatter('AMIP_psl')

sr.list()  
# Will list all the scatter attribute values

sr.projection='linear'  
# Can only be 'linear'

lon30={-180:'180W',-150:'150W',0:'Eq'}

sr.xticlabels1=lon30

sr.xticlabels2=lon30

sr.xticlabels(lon30, lon30)  
# Will set them both

sr.xmtics1=''

sr.xmtics2=''

sr.xmtics(lon30, lon30)  
# Will set them both

sr.yticlabels1=lat10

sr.yticlabels2=lat10

sr.yticlabels(lat10, lat10)  
# Will set them both

sr.ymtics1=''

sr.ymtics2=''

sr.ymtics(lat10, lat10)



See Chapter 6 for additional information.



# Will set them both

sr.datawc_y1=-90.0

sr.datawc_y2=90.0

sr.datawc_x1=-180.0

sr.datawc_x2=180.0

sr.datawc(-90, 90, -180, 180) # Will set them all

sr.xaxisconvert='linear'

sr.yaxisconvert='linear'

sr.xyscale('linear', 'area_wt') # Will set them both

# Specify the marker type:

sr.marker=1 # Same as sr.marker='dot'

sr.marker=2 # Same as sr.marker='plus'

sr.marker=3 # Same as sr.marker='star'

sr.marker=4 # Same as sr.marker='circle'

sr.marker=5 # Same as sr.marker='cross'

sr.marker=6 # Same as sr.marker='diamond'

sr.marker=7

# Same as sr.marker='triangle_up'

sr.marker=8 # Same as sr.marker='triangle_down'

sr.marker=9 # Same as sr.marker='triangle_left'

sr.marker=10 # Same as sr.marker='triangle_right'

sr.marker=11 # Same as sr.marker='square'

sr.marker=12 # Same as sr.marker='diamond_fill'

sr.marker=13 # Same as sr.marker='triangle_up_fill'







sr.marker=14 # Same as sr.marker='triangle_down_fill'

sr.marker=15 # Same as sr.marker='triangle_left_fill'

sr.marker=16

# Same as below

sr.markercolors=(22) # Same as below

sr.markercolors=([22]) # Will set the markers to a specific

# color index

sr.markercolors=None # Color index defaults to Black



To set the Marker sizie:

sr.markersize=5

sr.markersize=55

sr.markersize=100

sr.markersize=300

sr.markersize=None



Vector

createvector

Function: createvector



Description of Function:

Create a new vector graphics method given the the name and the existing vector
graphics method to copy the attributes from. If no existing vector graphics
method name is given, then the default vector graphics method will be used as
the graphics method to which the attributes will be copied from.

If the name provided already exists, then a error will be returned. Graphics
method names must be unique.

new vector name



[name of vector to copy attributes from]



Example of Use:

import vcs

a=vcs.init()

a.show('vector')

vec=a.createvector('example1',)

a.show('vector')

vec=a.createvector('example2','quick')

a.show('vector')

getvector

Function: getvector



Description of Function:

VCS contains a list of graphics methods. This function will create a vector
class object from an existing VCS vector graphics method. If no vector name is
given, then vector 'default' will be used.

Note, VCS does not allow the modification of `default' attribute sets.
However, a `default' attribute set that has been copied under a different name
can be modified. (See the createvector function.)

[vector name]



Example of Use:

import vcs

a=vcs.init()

a.show('vector')  
# Show all the existing vector graphics methods

vec=a.getvector()  
# vec instance of 'default' vector graphics method

vec2=a.getvector('quick')  
# vec2 instance of existing 'quick' vector graphics method



Object: vectorobject



Description of Function:

The vector graphics method displays a vector plot of a 2D vector field.
Vectors

are located at the coordinate locations and point in the direction of the data
vector field. Vector magnitudes are the product of data vector field lengths
and a scaling factor. The example below shows how to modify the vector's line,
scale, alignment, type, and reference.

This class is used to define an vector table entry used in VCS, or it can be
used to change some or all of the vector attributes in an existing vector
table entry.

Other Useful Functions:

a=vcs.init()  
# Constructor

a.show('vector')  
# Show predefined vector graphics methods

a.show('line')  
# Show predefined VCS line objects

a.setcolormap("AMIP")  
# Change the VCS color Map

a.vector(s1, s2, v,'default')  
# Plot data 's1', and 's2' with vector 'v' and 'default' template



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

Example of Use:

import vcs

a=vcs.init()

  
# To Create a new instance of vector use:

vc=a.createvector('new','quick')  
# Copies content of 'quick' to 'new'

vc=a.createvector('new')  
# Copies content of 'default' to 'new'

  
# To Modify an existing vector use:

vc=a.getvector('AMIP_psl')

vc.list()  
# Will list all the vector attribute values

vc.projection='linear'  
# Can only be 'linear'

lon30={-180:'180W',-150:'150W',0:'Eq'}

vc.xticlabels1=lon30

vc.xticlabels2=lon30

vc.xticlabels(lon30, lon30)  
# Will set them both

vc.xmtics1=''

vc.xmtics2=''

vc.xmtics(lon30, lon30)  
# Will set them both

vc.yticlabels1=lat10

vc.yticlabels2=lat10

vc.yticlabels(lat10, lat10)  
# Will set them both

vc.ymtics1=''

vc.ymtics2=''

vc.ymtics(lat10, lat10)  



a.update() # Updates the VCS Canvas at user's request a.mode=1, or 0. If 1,
then automatic update, else if 0, then use update function to update the VCS
Canvas.

See Chapter 6 for additional information.



# Will set them both

vc.datawc_y1=-90.0

vc.datawc_y2=90.0

vc.datawc_x1=-180.0

vc.datawc_x2=180.0

vc.datawc(-90, 90, -180, 180) # Will set them all

xaxisconvert='linear'

yaxisconvert='linear'

vc.xyscale('linear', 'area_wt') # Will set them both

# Specify the line style:

vc.line=0 # Same as vc.line='solid'

vc.line=1 # Same as vc.line='davc.line=2 # Same as vc.line='dot'

vc.line=3 # Same as vc.line='dash-dot'

vc.line=4 # Same as vc.line='long-dot'

# Specify the line color of the vectors:

vc.linecolor=16

# Color range: 16 to 230, default line color is black

# Specify the vector scale factor:

vc.scale=2.0 # Can be an integer or float

# Specify the vector alignment:

vc.alignment=0

# Same as vc.alignment='head'

vc.alignment=1 # Same as vc.alignment='center'









vc.alignment=2 # Same as vc.alignment='tail'

# Specify the vector type:

vc.type=0 # Same as vc.type='arrow head'

vc.type=1 # Same as vc.type='wind barbs'

vc.type=2 # Same as vc.type='solid arrow head'

Specify the vector reference:

vc.reference=4 # Can be an integer or float



XvsY

createxvsy

Function: createxvsy



Description of Function:

Create a new XvsY graphics method given the the name and the existing XvsY
graphics method to copy the attributes from. If no existing XvsY graphics
method name is given, then the default XvsY graphics method will be used as
the graphics method to which the attributes will be copied from.

If the name provided already exists, then a error will be returned. Graphics
method names must be unique.

new xvsy name



[name of xvsy to copy attributes from]



Example of Use:

import vcs

a=vcs.init()

a.show('xvsy')

xy=a.createxvsy('example1',)

a.show('xvsy')

xy=a.createxvsy('example2','quick')

a.show('xvsy')

getxvsy

Function: getxvsy



Description of Function:

VCS contains a list of graphics methods. This function will create a XvsY
class object from an existing VCS XvsY graphics method. If no XvsY name is
given, then XvsY 'default' will be used.

Note, VCS does not allow the modification of `default' attribute sets.
However, a `default' attribute set that has been copied under a different name
can be modified. (See the createxvsy function.)

[xvsy name]



Example of Use:

import vcs

a=vcs.init()

a.show('xvsy')  
# Show all the existing XvsY xy=a.getxvsy()  
# graphics methods xy instance of 'default' XvsY graphics method

xy2=a.getxvsy('quick')  
# xy2 instance of existing 'quick' XvsY graphics method



Object: xvsyobject



Description of Function:

The XvsY graphics method displays a line plot from two 1D data arrays, that is
X(t) and Y(t), where t represents the 1D coordinate values. The example below
shows how to change line and marker attributes for the XvsY graphics method.

This class is used to define an XvsY table entry used in VCS, or it can be
used to change some or all of the XvsY attributes in an existing XvsY table
entry.

Other Useful Functions:

a=vcs.init()  
# Constructor

a.show('xvsy')  
# Show predefined XvsY graphics methonds

a.show('line')  
# Show predefined VCS line objects

a.show('marker')  
# Show predefined VCS marker objects

a.setcolormap("AMIP")  
# Change the VCS color map

a.xvsy(s1, s2, ,x,'default')  
# Plot data 's1' and 's2' with XvsY 'x' and 'default' template



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

Example of Use:

import vcs

a=vcs.init()

  
# To Create a new instance of XvsY use:

xy=a.createxvsy('new','quick')  
# Copies content of 'quick' to 'new'

xy=a.createxvsy('new')  
# Copies content of 'default' to 'new'

  
# To Modify an existing XvsY use:

xy=a.getxvsy('AMIP_psl')

xy.list()  
# Will list all the XvsY attribute values

xy.projection='linear'  
# Can only be 'linear'

lon30={-180:'180W',-150:'150W',0:'Eq'}

xy.xticlabels1=lon30

xy.xticlabels2=lon30

xy.xticlabels(lon30, lon30)  
# Will set them both

xy.xmtics1=''

xy.xmtics2=''

xy.xmtics(lon30, lon30)  
# Will set them both

xy.yticlabels1=lat10

xy.yticlabels2=lat10

xy.yticlabels(lat10, lat10)  



a.update() # Updates the VCS Canvas at user's request a.mode=1, or 0. If 1,
then automatic update, else if 0, then use update function to Update the VCS
Canvas.

See Chapter 6 for additional information.



# Will set them both

xy.datawc_y1=-90.0

xy.datawc_y2=90.0

xy.datawc_x1=-180.0

xy.datawc_x2=180.0

xy.datawc(-90, 90, -180, 180) # Will set them all

xaxisconvert='linear'

yaxisconvert='linear'

xy.xyscale('linear', 'area_wt') # Will set them both

# Specify the XvsY line type:

xy.line=0 # same as xy.line = 'solid'

xy.line=1 # same as xy.line = 'dash'

xy.line=2 # same as xy.line = 'dot'

xy.line=3 # same as xy.line = 'dash-dot'

xy.line=4 # same as xy.line = 'long-dash

# Specify the Xvsy line color:

xy.line# color range: 16 to 230, default color is black

# Specify the XvsY marker type:

xy.marker=1 # Same as xy.marker='dot'

xy.marker=2 # Same as xy.marker='plus'

xy.marker=3

color=16 # color index







# Same as xy.marker='star'

xy.marker=4 # Same as xy.marker='circle'

xy.marker=5 # Same as xy.marker='cross'

xy.marker=6 # Same as xy.marker='diamond'

xy.marker=7 # Same as xy.marker='triangle_up'

xy.marker=8 # Same as xy.marker='triangle_down'

xy.marker=9 # Same as xy.marker='triangle_left'

xy.marker=10 # Same as xy.marker='triangle_right'

xy.marker=11 # Same as xy.marker='square'

xy.marker=12

# Same as xy.marker='square'

xy.marker=12 # Same as xy.marker='diamond_fill'

xy.marker=13 # Same as xy.marker='triangle_up_fill'

xy.marker=14 # Same as xy.marker='triangle_down_fill'

xy.marker=15 # Same as xy.marker='triangle_left_fill'

xy.marker=16 # Same as xy.marker='triangle_right_fill'

xy.marker=17 # Same as xy.marker='square_fill'

xy.marker=None # Draw no markers



There are four possibilities for setting the marker color index (Ex):







xy.markercolors=22 # Same as below

xy.markercolors=(22) # Same as below

xy.markercolors=([22]) # Will set the markers to a specific

xy.markercolors=None # Color index defaults to Black



To set the XvsY Marker sizie:

xy.markersize=5

xy.markersize=55

xy.markersize=100

xy.markersize=300

xy.markersize=None



Xyvsy

createxyvsy

Function: createxyvsy



Description of Function:

Create a new Xyvsy graphics method given the the name and the existing Xyvsy
graphics method to copy the attributes from. If no existing Xyvsy graphics
method name is given, then the default Xyvsy graphics method will be used as
the graphics method to which the attributes will be copied from.

If the name provided already exists, then a error will be returned. Graphics
method names must be unique.

new xyvsy name



[name of xyvsy to copy attributes from]



Example of Use:

import vcs

a=vcs.init()

a.show('xyvsy')

xyy=a.createxyvsy('example1',)

a.show('xyvsy')

xyy=a.createxyvsy('example2','quick')

a.show('xyvsy')

getxyvsy

Function: getxyvsy



Description of Function:

VCS contains a list of graphics methods. This function will create a Xyvsy
class object from an existing VCS Xyvsy graphics method. If no Xyvsy name is
given, then Xyvsy 'default' will be used.

Note, VCS does not allow the modification of `default' attribute sets.
However, a `default' attribute set that has been copied under a different name
can be modified. (See the createxyvsy function.)

[xyvsy name]



Example of Use:

import vcs

a=vcs.init()

a.show('xyvsy')  
# Show all the existing Xyvsy graphics methods

xyy=a.getxyvsy()  
# xyy instance of 'default' Xyvsy graphics method

xyy2=a.getxyvsy('quick')  
# xyy2 instance of existing 'quick' Xyvsy graphics method



Object: xyvsyobject



Description of Function:

The Xyvsy graphics method displays a line plot from a 1D data array (i.e. a
plot of X(y), where y represents the 1D coordinate values). The example below
ributes for the Xyvsy graphics method.

This class is used to define an Xyvsy table entry used in VCS, or it can be
used to change some or all of the Xyvsy attributes in an existing Xyvsy table
entry.

Other Useful Functions:

a=vcs.init()  
# Constructor

a.show('xyvsy')  
# Show predefined Xyvsy graphics methonds

a.show('line')  
# Show predefined VCS line objects

a.show('marker')  
# Show predefined VCS marker objects

a.setcolormap("AMIP")  
# Change the VCS color map

a.xyvsy(s, x, 'default')  
# Plot data 's' with Xyvsy 'x' and 'default' template

a.update()  
# Updates the VCS Canvas at user's request a.mode=1, or 0 . If 1, then
automatic update, else if 0, then use update function.

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

Example of Use:

import vcs

a=vcs.init()

  
# To Create a new instance of Xyvsy use:

xyy=a.createxyvsy('new','quick')  
# Copies content of 'quick' to 'new'

xyy=a.createxyvsy('new')  
# Copies content of 'default' to 'new'

  
# To Modify an existing Xyvsy use:

xyy=a.getxyvsy('AMIP_psl')

xyy.list()  
# Will list all the Xyvsy attribute values

xyy.projection='linear'  
# Can only be 'linear'

lon30={-180:'180W',-150:'150W',0:'Eq'}

xyy.xticlabels1=lon30

xyy.xticlabels2=lon30

xyy.xticlabels(lon30, lon30)  
# Will set them both

xyy.xmtics1=''

xyy.xmtics2=''

xyy.xmtics(lon30, lon30)  
# Will set them both

xyy.yticlabels1=lat10

xyy.yticlabels2=lat10

xyy.yticlabels(lat10, lat10)  
# Will set them both

xyy.ymtics1=''

xyy.ymtics2=''

xyy.ymtics(lat10, lat10)



See Chapter 6 for additional information.



# Will set them both

xyy.datawc_y1=-90.0

xyy.datawc_y2=90.0

xyy.datawc_x1=-180.0

xyy.datawc_x2=180.0

xyy.datawc(-90, 90, -180, 180) # Will set them all

xyy.xaxisconvert='linear'

# Specify the Xyvsy line type:

xyy.line=0 # same as xyy.line = 'solid'

xyy.line=1 # same as xyy.line = 'dash'

xyy.line=2 # same as xyy.line = 'dot'

xyy.line=3

same as xyy.line = 'dash-dot'

xyy.line=4 # same as xyy.line = 'long-dash

# Specify the Xyvsy line color:

xyy.linecolor=16 # color range: 16 to 230, default color is black

# Specify the Xyvsy marker type:

xyy.marker=1 # Same as xyy.marker='dot'

xyy.marker=2 # Same as xyy.marker='plus'

xyy.marker=3 # Same as xyy.marker='star'

xyy.marker=4

# Same as xyy.marker='circle'

xyy.marker=5 # Same as xyy.marker='cross'

xyy.marker=6 # Same as xyy.marker='diamond'

xyy.marker=7 # Same as xyy.marker='triangle_up'







xyy.marker=8 # Same as xyy.marker='triangle_down'

xyy.marker=9 # Same as xyy.marker='triangle_left'

xyy.marker=10 # Same as xyy.marker='triangle_right'

xyy.marker=11 # Same as xyy.marker='square'

xyy.marker=12 # Same as xyy.marker='diamond_fill'

xyy.marker=13

# Same as xyy.marker='triangle_up_fill'

xyy.marker=14 # Same as xyy.marker='triangle_down_fill'

xyy.marker=15 # Same as xyy.marker='triangle_left_fill'

xyy.marker=16 # Same as xyy.marker='triangle_right_fill'

xyy.marker=17 # Same as xyy.marker='square_fill'

xyy.marker=None # Draw no markers



There are four possibilities for setting the marker color index (Ex):

xyy.markercolors=22 # Same as below

xyy.markercolors=(22) # Same as below

xyy.markercolors=([22]) # Will set the markers to a specific

# color index

xyy.markercolors=None # Color index defaults to Black



To set the Xyvsy Marker sizie:

xyy.markersize=5







xyy.markersize=55

xyy.markersize=100

xyy.markersize=300

xyy.markersize=None

Yxvsx

createyxvsx

Function: createyxvsx



Description of Function:

Create a new Yxvsx graphics method given the the name and the existing Yxvsx
graphics method to copy the attributes from. If no existing Yxvsx graphics
method name is given, then the default Yxvsx graphics method will be used as
the graphics method to which the attributes will be copied from.

If the name provided already exists, then a error will be returned. Graphics
method names must be unique

new yxvsx name



[name of yxvsx to copy attributes from]



Example of Use:

import vcs

a=vcs.init()

a.show('yxvsx')

yxx=a.createyxvsx('example1',)

a.show('yxvsx')

yxx=a.createyxvsx('example2','quick')

a.show('yxvsx')

getyxvsx

Function: getyxvsx



Description of Function:

VCS contains a list of graphics methods. This function will create a Yxvsx
class object from an existing VCS Yxvsx graphics method. If no Yxvsx name is
given, then Yxvsx 'default' will be used.

Note, VCS does not allow the modification of `default' attribute sets.
However, a `default' attribute set that has been copied under a different name
can be modified. (See the createyxvsx function.)

[yxvsx name]



Example of Use:

import vcs

a=vcs.init()

a.show('yxvsx')  
# Show all the existing Yxvsx graphics methods

yxx=a.getyxvsx()  
# yxx instance of 'default' Yxvsx graphics method

yxx2=a.getyxvsx('quick')  
# yxx2 instance of existing 'quick' Yxvsx graphics method



Object: yxvsxobject



Description of Function:

The Yxvsx graphics method displays a line plot from a 1D data array (i.e.
aplot of Y(x), where y represents the 1D coordinate values). The example
belowshows how to change line and marker attributes for the Yxvsx graphics
method.

This class is used to define an Yxvsx table entry used in VCS, or it can
beused to change some or all of the Yxvsx attributes in an existing Yxvsx
table entry.

Other Useful Functions:

a=vcs.init()  
# Constructor

a.show('yxvsx')  
# Show predefined Yxvsx graphics methonds

a.show('line')  
# Show predefined VCS line objects

a.show('marker')  
# Show predefined VCS marker objects

a.setcolormap("AMIP")  
# Change the VCS color map

a.yxvsx(s, x, 'default')  
# Plot data 's' with Yxvsx 'x' and 'default' template

a.update()  
# Updates the VCS Canvas at user's request

a.mode=1, or 0 If 1, then automatic update, else if 0, then use update
function.

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

Example of Use:

import vcs

a=vcs.init()

  
# To Create a new instance of Yxvsx use:

yxx=a.createxyvsy('new','quick')  
# Copies content of 'quick' to 'new'

yxx=a.createxyvsy('new')  
# Copies content of 'default' to 'new'

  
# To Modify an existing Yxvsx use:

yxx=a.getxyvsy('AMIP_psl')

yxx.list()  
# Will list all the Yxvsx attribute values

yxx.projection='linear'  
# Can only be 'linear'

lon30={-180:'180W',-150:'150W',0:'Eq'}

yxx.xticlabels1=lon30

yxx.xticlabels2=lon30

yxx.xticlabels(lon30, lon30)  
# Will set them both

yxx.xmtics1=''

yxx.xmtics2=''

yxx.xmtics(lon30, lon30)  
# Will set them both

yxx.yticlabels1=lat10

yxx.yticlabels2=lat10

yxx.yticlabels(lat10, lat10)  



See Chapter 6 for additional information.



# Will set them both

yxx.datawc_y1=-90.0

yxx.datawc_y2=90.0

yxx.datawc_x1=-180.0

yxx.datawc_x2=180.0

yxx.datawc(-90, 90, -180, 180) # Will set them all

yxx.yaxisconvert='linear'

# Specify the Yxvsx line type:

yxx.line=0 # same as yxx.line = 'solid'

yxx.line=1 # same as yxx.line = 'dash'

yxx.line=2 # same as yxx.line = 'dot'

yxx.line=3

# same as yxx.line = 'dash-dot'

yxx.line=4 # same as yxx.line = 'long-dash

# Specify the Yxvsx line color:

yxx.linecolor=16 # color range: 16 to 230, default color is black

yxx.linecolor=16 # color range: 16 to 230, default color is black

# Specify the Yxvsx marker type:

yxx.marker=1 # Same as yxx.marker='dot'

yxx.marker=2 # Same as yxx.marker='plus'

yxx.marker=3 # Same as yxx.marker='star'

yxx.marker=4 # Same as yxx.marker='circle'

yxx.marker=5 # Same as yxx.marker='cross'

yxx.marker=6 # Same as yxx.marker='diamond'







yxx.marker=7 # Same as yxx.marker='triangle_up'

yxx.marker=8 # Same as yxx.marker='triangle_down'

yxx.marker=9 # Same as yxx.marker='triangle_left'

yxx.marker=10 # Same as yxx.marker='triangle_right'

yxx.marker=11 # Same as yxx.marker='square'

yxx.marker=12 # Same as yxx.marker='diamond_fill'

yxx.marker=13 # Same as yxx.marker='triangle_up_fill'

yxx.marker=14 # Same as yxx.marker='triangle_down_fill'

yxx.marker=15 # Same as yxx.marker='triangle_left_fill'

yxx.marker=16 # Same as yxx.marker='triangle_right_fill'

yxx.marker=17 # Same as yxx.marker='square_fill'

yxx.marker=None # Draw no markers



There are four possibilities for setting the marker color index (Ex):

yxx.markercolors=22 # Same as below

yxx.markercolors=(22) # Same as below

yxx.markercolors=([22])

# Will set the markers to a specific

color index

yxx.markercolors=None # Color







index defaults to Black



To set the Yxvsx Marker size:

yxx.markersize=5

yxx.markersize=55

yxx.markersize=100

yxx.markersize=300

yxx.markersize=None



Picture Template

createtemplate

Function: createtemplate



Description of Function:

Create a new template given the the name and the existing template to copy the
attributes from. If no existing template name is given, then the default
template will be used as the template to which the attributes will be copied
from.

If the name provided already exists, then a error will be returned. Template
names must be unique.

new template name



[name of template to copy attributes from]

Example of Use:

import vcs

a=vcs.init()

a.show('template')  
# Show all the existing templates

con=a.createtemplate('example1')  
# create 'example1' template from 'default' template

a.show('template')  
# Show all the existing templates

con=a.createtemplate('example2','quick')  
# create 'example2' from 'quick' template

a.listelements('template')  
# Show all the templates as a Python list

gettemplate

Function: gettemplate



Description of Function:

VCS contains a list of predefined templates. This function will create a
template class object from an existing VCS template. If no template name is
given, then template 'default' will be used.

Note, VCS does not allow the modification of `default' attribute sets.
However, a `default' attribute set that has been copied under a different name
can be modified. (See the createtemplate function.)

[template name]

Example of Use:

import vcs

a=vcs.init()

a.show('template')  
# Show all the existing templates

templt=a.gettemplate()  
# templt instance of 'default' template

templt2=a.gettemplate('quick')  
# templt2 contains 'quick' template



Object: templateobject



Description of Function:

The template primary method (P) determines the location of each picture
segment, the space to be allocated to it, and related properties relevant to
its display.

Other Useful Functions:

a.show('template')  
# Show predefined templates

a.show('texttable')  
# Show predefined text table methods

a.show('textorientation')  
# Show predefined text orientation methods

a.show('line')  
# Show predefined line methods

a.listelements('template')  
# Show templates as a Python list

a.update()  
# Updates the VCS Canvas at user's request a.mode=1, or 0. If 1, then
automatic update, else if 0, then use the update function toupdate the VCS
Canvas.

See Chapter 6 for the long list of options.

Example of Use:

import vcs

a=vcs.init()

  
# To Create a new instance of boxfill use:

box=a.createboxfill('new','quick')  
# Copies content of 'quick' to 'new'

box=a.createboxfill('new')  
# Copies content of 'default' to 'new'

  
# To Modify an existing boxfill use:

box=a.getboxfill('AMIP_psl')

  
# To Create a new instance of template use:

tpl=a.createtemplate('new','AMIP')  
# Copies content of 'AMIP' to 'new'

tpl=a.createtemplate('new')  
# Copies content of 'default' to 'new'

  
# To Modify an existing template use:

tpl=a.gettemplate('AMIP')

Secondary Objects

Colormap Commands

setcolormap

Function: setcolormap



Description of Function:

It is necessary to change the colormap. This routine will change the VCS color
map.

If the the visul display is 16-bit, 24-bit, or 32-bit TrueColor, then a
redrawing of the VCS Canvas is made evertime the colormap is changed.



Example of Use:

import vcsa=vcs.init()

a.plot(array,'default','isofill','quick')

a.setcolormap("AMIP")

setcolorcell

Function: setcolorcell



Description of Function:

Set a individual color cell in the active colormap. If default is the active
colormap, then return an error string.

If the the visul display is 16-bit, 24-bit, or 32-bit TrueColor, then a
redrawing of the VCS Canvas is made evertime the color cell is changed.

Note, the user can only change color cells 0 through 239 and R,G,Bvalue must
range from 0 to 100. Where 0 represents no color intensity and 100 is the
greatest color intensity.

colormap index: 0 to 239

R - Red intensity value: 0 to 100

G - Green intensity value: 0 to 100

B - Blue intensity value: 0 to 100

Example of Use:

import vcs

a=vcs.init()

a.plot(array,'default','isofill','quick')

a.setcolormap("AMIP")

a.setcolorcell(11,0,0,0)

a.setcolorcell(21,100,0,0)

a.setcolorcell(31,0,100,0)

a.setcolorcell(41,0,0,100)

a.setcolorcell(51,100,100,100)

a.setcolorcell(61,70,70,70)

colormapgui

Function: colormapgui



Description of Function:

Run the VCS colormap interface.

The colormapgui command is used to bring up the VCS colormap interface. The
interface is used to select, create, change, or remove colormaps.

Note:

The colormapgui GUI will only work for 8-bit 'Pseudo Color'.



Example of Use:

import vcs

a=vcs.init()

a.colormapgui()

Fill Area

createfillarea

Function: createfillarea



Description of Function:

Create a new fillarea secondary method given the the name and the existing
fillarea secondary method to copy the attributes from. If no existing fillarea
secondary method name is given, then the default fillarea secondary method
will be used as the secondary method to which the attributes will be copied
from.

If the name provided already exists, then a error will be returned. Secondary
method names must be unique.

new fillarea name



[name of fillarea to copy attributes from]



Example of Use:

import vcs

a=vcs.init()

a.show('fillarea')

fa=a.createfillarea('example1',)

a.show('fillarea')

fa=a.createfillarea('example2','black')

a.show('fillarea')

getfillarea

Function: getfillarea



Description of Function:

VCS contains a list of secondary methods. This function will create a fillarea
class object from an existing VCS fillarea secondary method. If no fillarea
name is given, then fillarea 'default' will be used.

Note, VCS does not allow the modification of `default' attribute sets.
However, a `default' attribute set that has been copied under a different name
can be modified. (See the createfillarea function.)

[fillarea name]



Example of Use:

import vcs

a=vcs.init()

a.show('fillarea')  
# Show all the existing fillarea secondary methods

fa=a.getfillarea()  
# fa instance of 'default' fillarea secondary method

fa2=a.getfillarea('quick')  
# fa2 instance of existing 'quick' fillarea secondary method



Object: fillareaobject



Description of Function:

The Fillarea class object allows the user to edit fillarea attributes,
including

fillarea interior style, style index, and color index.

This class is used to define an fillarea table entry used in VCS, or itcan be
used to change some or all of the fillarea attributes in an existing fillarea
table entry.

Other Useful Functions:

a=vcs.init()  
# Constructor

a.show('fillarea')  
# Show predefined fillarea objects

a.update()  
# Updates the VCS Canvas at user's request a.mode=1, or 0  
# If 1, then automatic update, else if 0, then use update function to update
the VCS Canvas.

name

style

index

color

Example of Use:

import vcs

a=vcs.init()

  
# To Create a new instance of fillarea use:

fa=a.createfillarea('new','def37')  
# Copies content of 'def37' to 'new'

fa=a.createfillarea('new')  
# Copies content of 'default' to 'new'

  
# To Modify an existing fillarea use:

fa=a.getfillarea('red')

  
# fa.list()  
# Will list all the fillarea attribute values

  
# There are three possibilities for setting the isofill style (Ex):

fa.style = 'solid'

fa.style = 'hatch'

fa.style = 'pattern'

fa.index=1  
# Range from 1 to 20

fa.color=100  
# Range from 1 to 256

  
# Specify the fillarea index:

fa.index=1

fa.index=2

fa.index=3

fa.index=4

fa.index=5

fa.index=6

fa.index=7







fa.index=8

fa.index=9

fa.index=10

fa.index=11

fa.index=12

fa.index=13

fa.index=14

fa.index=15

fa.index=16

fa.index=17

fa.index=18

fa.index=19

fa.index=20

Line

createline

Function: createline



Description of Function:

Create a new line secondary method given the the name and the existing line
secondary method to copy the attributes from. If no existing line secondary
method name is given, then the default line secondary method will be used as
the secondary method to which the attributes will be copied from.

If the name provided already exists, then a error will be returned. Secondary
method names must be unique

new line name



[name of line to copy attributes from]



Example of Use:

import vcs

a=vcs.init()

a.show('line')

ln=a.createline('example1',)

a.show('line')

ln=a.createline('example2','black')

a.show('line')

getline

Function: getline



Description of Function:

VCS contains a list of secondary methods. This function will create a line
class object from an existing VCS line secondary method. If no line name is
given, then line 'default' will be used.

Note, VCS does not allow the modification of `default' attribute sets.

However, a `default' attribute set that has been copied under a different name
can be modified. (See the createline function.)

[line name]



Example of Use:

import vcs

a=vcs.init()

a.show('line')  
# Show all the existing line secondary methods

ln=a.getline()  
# ln instance of 'default' line secondary method

ln2=a.getline('quick')  
# ln2 instance of existing 'quick' line secondary method



Object: lineobject



Description of Function:

The Line object allows the manipulation of line type, width, and color index.

This class is used to define an line table entry used in VCS, or itcan be used
to change some or all of the line attributes in an existing line table entry.

Other Useful Functions:

a=vcs.init()  
# Constructor

a.show('line')  
# Show predefined line objects

a.update()  
# Updates the VCS Canvas at user's request a.mode=1, or 0  
# If 1, then automatic update, else if 0, then use update function to update
the VCS Canvas.

name

type

width

color

Example of Use:

import vcs

a=vcs.init()

  
# To Create a new instance of line use:

ln=a.createline('new','red')  
# Copies content of 'red' to 'new'

ln=a.createline('new')  
# Copies content of 'default' to 'new'

  
# To Modify an existing line use:

ln=a.getline('red')

ln.list()  
# Will list all the line attribute values

ln.color=100  
# Range from 1 to 256

ln.width=100  
# Range from 1 to 300

  
# Specify the line type:

ln.type='solid'  
# Same as ln.type=0

ln.type='dash'  
# Same as ln.type=1

ln.type='dot'  
# Same as ln.type=2

ln.type='dash-dot'  
# Same as ln.type=3

ln.type='long-dash'  
# Same as ln.type=4



Marker

createmarker

Function: createmarker

Description of Function:

Create a new marker secondary method given the the name and the existing
marker secondary method to copy the attributes from. If no existing marker
secondary method name is given, then the default marker secondary method will
be used as the secondary method to which the attributes will be copied from.

If the name provided already exists, then a error will be returned.

Secondary method names must be unique.

new marker name



[name of marker to copy attributes from]



Example of Use:

import vcs

a=vcs.init()

a.show('marker')

mrk=a.createmarker('example1',)

a.show('marker')

mrk=a.createmarker('example2','black')

a.show('boxfill')

getmarker

Function: getmarker



Description of Function:

VCS contains a list of secondary methods. This function will create a marker
class object from an existing VCS marker secondary method. If no marker name
is given, then marker 'default' will be used.

Note, VCS does not allow the modification of `default' attribute sets.

However, a `default' attribute set that has been copied under a different name
can be modified. (See the createmarker function.)

[marker name]



Example of Use:

import vcs

a=vcs.init()

a.show('marker')  
# Show all the existing marker secondary methods

mrk=a.getmarker()  
# mrk instance of 'default' marker secondary method

mrk2=a.getmarker('quick')  
# mrk2 instance of existing 'quick' marker secondary method



Object: markerobject



Description of Function:

The Marker object allows the manipulation of marker type, size, and color
index.

This class is used to define an marker table entry used in VCS, or it can be
used to change some or all of the marker attributes in an existing marker
table entry.

Other Useful Functions:

a=vcs.init()  
# Constructor

a.show('marker')  
# Show predefined marker objects

a.update()  
# Updates the VCS Canvas at user's request a.mode=1, or 0. If 1, then
automatic update, else if 0, then use update function to update the VCS
Canvas.

name

type

size

color

Example of Use:

import vcs

a=vcs.init()

  
# To Create a new instance of marker use:

mk=a.createmarker('new','red')  
# Copies content of 'red' to 'new'

mk=a.createmarker('new')  
# Copies content of 'default' to 'new'

  
# To Modify an existing marker use:

mk=a.getmarker('red')



mk.list()  
# Will list all the marker attribute values

mk.color=100  
# Range from 1 to 256

mk.size=100  
# Range from 1 to 300

  
# Specify the marker type:

mk.type='dot'  
# Same as mk.type=1

mk.type='plus'  
# Same as mk.type=2

mk.type='star'  
# Same as mk.type=3

mk.type='circle'  
# Same as mk.type=4

mk.type='cross'  
# Same as mk.type=5

mk.type='diamond'  
# Same as mk.type=6

mk.type='triangle_up'  
# Same as mk.type=7







mk.type='triangle_down' # Same as mk.type=8

mk.type='triangle_left' # Same as mk.type=9

mk.type='triangle_right' # Same as mk.type=10

mk.type='square'

# Same as mk.type=11

mk.type='diamond_fill' # Same as mk.type=12

mk.type='triangle_up_fill' # Same as mk.type=13

mk.type='triangle_down_fill' # Same as mk.type=14

mk.type='triangle_left_fill' # Same as mk.type=15

mk.type='triangle_right_fill' # Same as mk.type=16

mk.type='square_fill' # Same as mk.type=17



Text-Combined

createtextcombined

Function: createtextcombined



Description of Function:

Create a new textcombined secondary method given the the names and the
existing texttable and textorientation secondary methods to copy the
attributes from. If no existing texttable and textorientation secondary method
names are given, then the default texttable and textorientation secondary
methods will be used as the secondary method to which the attributes will be
copied from.

If the name provided already exists, then a error will be returned.

Secondary method names must be unique.

new textcombined name



[name of textcombined to copy attributes from]

Example of Use:

import vcs

a=vcs.init()

a.show('texttable')

a.show('textorientation')

tc=a.createtextcombined('example1','std','example1','7left')

a.show('texttable')

a.show('textorientation')

gettextcombined

Function: gettextcombined



Description of Function:

VCS contains a list of secondary methods. This function will create a
textcombined class object from an existing VCS texttable secondary method and
an existing VCS textorientation secondary method. If no texttable or
textorientation names are given, then the 'default' names will be used in both
cases.

Note, VCS does not allow the modification of `default' attribute sets.

However, a `default' attribute set that has been copied under a different name
can be modified. (See the createtextcombined function.)

[textcombined name]



Example of Use:

import vcs

a=vcs.init()

a.show('texttable')  
# Show all the existing texttable secondary methods

a.show('textorientation')  
# Show all the existing textorientation secondary methods

tc=a.gettextcombined()  
# Use 'default' for texttable and textorientation

tc2=a.gettextcombined('std','7left')  
# Use 'std' texttable and '7left' textorientation

if istextcombined(tc):  
# Check to see if tc is a textcombined

tc.list()  
# Print out all its attriubtes



Object: textcombinedobject



Description of Function:

The (Tc) Text Combined class will combine a text table class and a text
orientation class together. From combining the two classess, the user will be
able to set attributes for both classes (i.e., define the font, spacing,
expansion, color index, height, angle, path, vertical alignment, and
horizontal alignment).

This class is used to define and list a combined text table and text
orientation

entry used in VCS.

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

Example of Use:

import vcs

a=vcs.init()

  
# To Create a new instance of text table use:

tc=a.createtextcombined('new_tt','std','new_to','7left')  
# Copies content of 'std' to 'new_tt' and '7left' to 'new_to'



  
# To Modify an existing texttable use:

tc=a.gettextcombined('std','7left')

tc.list()  
# Will list all the textcombined attribute values (i.e., texttable and
textorientation attributes

  
# Specify the text font type:

tc.font=1  
# The font value must be in the range 1 to 9

  
#Specify the text spacing:

tc.spacing=2  
# The spacing value must be in the range -50 to 50

  
# Specify the text expansion:

tc.expansion=100  
# The expansion value ranges from 50 to 150

  
# Specify the text color:

tc.color=241  
# The text color value ranges from 1 to 257

  








# Specify the text height:

tc.height=20 # The height value must be in the range 1 to 100

# Specify the text angle:

tc.angle=0 # The angle value ran # Specify the text path:

tc.path='right' # Same as tc.path=0

tc.path='left' # Same as tc.path=1

tc.path='up' # Same as tc.path=2 ges from 0 to 360

tc.path='down' # Same as tc.path=3

# Specify the text horizontal alignment:

tc.halign='right' # Same as tc.halign=0

tc.halign='center' # Same as tc.halign=1

tc.halign='right' # Same as tc.halign=2

# Specify the text vertical alignment:

tc.valign='tcp' # Same as tcvalign=0

tc.valign='cap' # Same as tcvalign=1

tc.valign='half' # Same as tcvalign=2

tc.valign='base' # Same as tcvalign=3

tc.valign='bottom' # Same as tcvalign=4

Text-Orientation

createtextorientation

Function: createtextorientation



Description of Function:

Create a new textorientation secondary method given the the name and he
existing textorientation secondary method to copy the attributes from. If no
existing textorientation secondary method name is given, then the default
textorientation secondary method will be used as the secondary method to which
the attributes will be copied from.

If the name provided already exists, then a error will be returned.

Secondary method names must be unique.

new textorientation name



[name of textorientation to copy attributes from]



Example of Use:

import vcs

a=vcs.init()

a.show('textorientation')

to=a.createtextorientation('example1')

a.show('textorientation')

to=a.createtextorientation('example2','black')

a.show('textorientation')

gettextorientation

Function: gettextorientation



Description of Function:

VCS contains a list of secondary methods. This function will create a
textorientation class object from an existing VCS textorientation secondary
method. If no textorientation name is given, then textorientation 'default'
will be used.

Note, VCS does not allow the modification of `default' attribute sets.

However, a `default' attribute set that has been copied under a different name
can be modified. (See the createtextorientation function.)

[textorientation name]



Example of Use:

import vcs

a=vcs.init()

a.show('textorientation')  
# Show all the existing textorientation secondary methods

to=a.gettextorientation()  
# to instance of 'default' textorientation secondary method

to2=a.gettextorientation('quick')  
# to2 instance of existing 'quick' textorientation secondary method



Object: textorientationobject



Description of Function:

The (To) Text Orientation lists text attribute set names that define the font,
spacing, expansion, and color index.

This class is used to define an text orientation table entry used in VCS, or
it can be used to change some or all of the text orientation attributes in an
existing text orientation table entry.

Other Useful Functions:

a=vcs.init()  
# Constructor

a.show('textorientation')  
# Show predefined text orientation objects

a.update()  
# Updates the VCS Canvas at user's request a.mode=1, or 0. If 1, then
automatic update, else if 0, then use update function to update the VCS
Canvas.

name

height

angel

path

halign

valign

Example of Use:

import vcs

a=vcs.init()

  
# To Create a new instance of text orientation use:

to=a.createtextorientation('new','7left')  
# Copies content of '7left' to 'new'

to=a.createtextorientation('new')  
# Copies content of 'default' to 'new'

  
# To Modify an existing textorientation use:

to=a.gettextorientation('7left')

to.list()  
# Will list all the textorientation attribute values

  
# Specify the text height:

to.height=20  
# The height value must be in the range 1 to 100

  
#ecify the text angle:

to.angle=0  
# The angle value must be in the range 0 to 360

  
# Specify the text path:

to.path='right'  
# Same as to.path=0

to.path='left'  
# Same as to.path=1

to.path='up'  
# Same as to.path=2

to.path='down'  
# Same as to.path=3









# Specify the text horizontal alignment:

to.halign='right' # Same as to.halign=0

to.halign='center' # Same as to.halign=1

to.halign='right'

# Same as to.halign=2

# Specify the text vertical alignment:

to.valign='top' # Same as tovalign=0

to.valign='cap'

# Same as tovalign=1

to.valign='half' # Same as tovalign=2

to.valign='base' # Same as tovalign=3

to.valign='bottom'

# Same as tovalign=4

Text-Table

createtexttable

Function: createtexttable



Description of Function:

Create a new texttable secondary method given the the name and the existing
texttable secondary method to copy the attributes from. If no existing
texttable secondary method name is given, then the default texttable secondary
method will be used as the secondary method to which the attributes will be
copied from.

If the name provided already exists, then a error will be returned.

Secondary method names must be unique.

new texttable name



[name of texttable to copy attributes from]



Example of Use:

import vcs

a=vcs.init()

a.show('texttable')

tt=a.createtexttable('example1',)

a.show('texttable')

tt=a.createtexttable('example2','black')

a.show('texttable')

gettexttable

Function: gettexttable



Description of Function:

VCS contains a list of secondary methods. This function will create a
texttable class object from an existing VCS texttable secondary method. If no
texttable name is given, then texttable 'default' will be used.

Note, VCS does not allow the modification of `default' attribute sets.

However, a `default' attribute set that has been copied under a different name
can be modified. (See the createtexttable function.)

[texttable name]



Example of Use:

import vcs

a=vcs.init()

a.show('texttable')  
# Show all the existing texttable secondary methods

tt=a.gettexttable()  
# tt instance of 'default' texttable secondary method

tt2=a.gettexttable('quick')  
# tt2 instance of existing 'quick' texttable secondary method



Object: texttableobject



Description of Function:

The (Tt) Text Table lists text attribute set names that define the font,
spacing, expansion, and color index.

This class is used to define an text table table entry used in VCS, or it can
be used to change some or all of the text table attributes in an existing text
table table entry.

Other Useful Functions:

a=vcs.init()  
# Constructor

a.show('texttable')  
# Show predefined text table objects

a.update()  
# Updates the VCS Canvas at user's request a.mode=1, or 0. If 1, then
automatic update, else if 0, then use update function to update the VCS
Canvas.

name

font

spacing

expansion

color

Example of Use:

import vcs

a=vcs.init()

  
# To Create a new instance of text table use:

tt=a.createtexttable('new','std')  
# Copies content of 'std' to 'new'

tt=a.createtexttable('new')  
# Copies content of 'default' to 'new'

  
# To Modify an existing texttable use:

tt=a.gettexttable('std')

tt.list()  
# Will list all the texttable attribute values

  
# Specify the text font type:

tt.font=1  
# The font value must be in the range 1 to 9

  
# Specify the text spacing:

tt.spacing=2  
# The spacing value must be in the range -50 to 50

  
# Specify the text expansion:

tt.expansion=100  
# The expansion value must be in the range 50 to 150

  
# Specify the text color:

tt.color=241  
# The text color attribute value must be in the range 1 to 257

Remove Objects

removeobject

Function: removeobject



Description of Function:

The user has the ability to create primary and secondary class objects. This
function allows the user to remove these objects from the appropriate class
list.

Note, To remove the object completely from Python, remember to use the "del"
function.

Also note, The user is not allowed to remove a "default" class object.

object

Example of Use:

import vcs

a=vcs.init()

line=a.getline('red')  
# To Modify an existing line object

iso=a.createisoline('dean')  
# Create an instance of an isoline object

...

a.removeobject(line)  
# Removes line object from VCS list

del line  
# Destroy instance "line", garbage collection

a.removeobject(iso)  
# Remove isoline object from VCS list

del iso  
# Destroy instance "iso", garbage collection

Set Continents Type

setcontinentstype

Function: setcontinentstype



Description of Function:

One has the option of using continental maps that are predefined or that are
user-defined. Predefined continental maps are either internal to VCS or are
specified by external files. User-defined continental maps are specified by
additional external files that must be read as input.

The continents-type values are integers ranging from 0 to 11, where:

0 signifies "No Continents"

1 signifies "Fine Continents"

2 signifies "Coarse Continents"

3 signifies "United States" (with "Fine Continents")

4 signifies "Political Borders" (with "Fine Continents")

5 signifies "Rivers" (with "Fine Continents")

Values 6 through 11 signify the line type defined by the files

data_continent_other7 through data_continent_other12.

continents type number, ranging from 0 to 11

Example of Use:

import vcs

a=vcs.init()

# Set continents to "United States"

a.setcontinentstype(3)

a.plot(array,'default','isofill','quick'

Set Default Picture Template and Graphics Methods

set

Function: set



Description of Function:

Set the default VCS primary class objects: template and graphics methods.

Keep in mind the template, determines the appearance of each graphics segment;
the graphic method specifies the display technique; and the data defines what
is to be displayed. Note, the data cannot be set with this function.

template or graphics methods type,

[template name or graphics method name]

Example of Use:

import vcs

a=vcs.init()

a.set('isofill','quick')  
# Changes the default graphics method to Isofill: 'quick'

a.plot(array)

Animation

animate

Function: animate



Description of Function:

Animate the contents of the VCS Canvas. Currently, only one display can be
shown in the VCS Canvas for the animation to work. This function pops up the
animation GUI.

Note:

The animation GUI will only work for 8-bit 'Pseudo Color'.

See the animation GUI documenation located at URL:

http://www-pcmdi.llnl.gov/software/vcs



Example of Use:

import vcs

a=vcs.init()

a.plot(array,'default','isofill','quick')

a.animate()

Flush

flush

Function: flush



Description of Function:

The flush command executes all buffered X events in the que.



Example of Use:

import vcs

a=vcs.init()

a.plot(array,'default','isofill','quick')

a.flush()

Grid

grid

Function: grid



Description of Function:

Set the default plotting region for variables that have more dimension values
than the graphics method. This will also be used for animating plots over the
third and fourth dimensions.

([first dim's 1st value, first dim's last value] ,..., [last dim's 1st value,
last dim's last value]

Example of Use:

import vcs

a=vcs.init()

a=vcs.init()

a.grid(12,24, -70,70, -150,150)

a.plot(array,'default','isofill','quick')

resetgrid

Function: resetgrid



Description of Function:

Set the plotting region to default values. That is, let the variable's
dimension values determine the grid



Example of Use:

import vcs

a=vcs.init()

a=vcs.init()

a.resetgrid()

a.plot(array,'default','isofill','quick')



[Go to Main](vcs.html) [Go to Previous](vcs-4.html) [Go to Next](vcs-6.html)


