---
layout: default
title: VCS Chapter 11
---

##  CHAPTER 11 The VCS Module

The VCS module is designed to provide access to the VCS graphical interface.





####

![](vcs-54.gif)

The VCS Graphics Module

VCS is CDAT's interface to a library for two-dimensional graphics that has
been particularly customized for climate data but which in fact can be used by
many scientific applications. VCS has a rich set of facilities that allow you
to easily make sophisticated presentation graphics.

VCS as a module has the principal function init() which returns a Canvas
object. The rest of the commands are methods on the Canvas object. Up to 8
canvases can be active at one time.



Command

Description

Examples

init()

Initializes and creates a VCS object, reads in the initial.attribute file and
set up the VCS default values.

Note: The number of VCS Canvases is limited to eight.

import vcs

x=vcs.init()

help()

Gives insight to other VCS functions by providing a description and at least
one example.

import vcs

vcs.help()

vcs.help(`init')

objecthelp()

Print out information on VCS objects. See example on its use.

import vcs

x=vcs.init()

ln=a.createline('red')

x.objecthelp(ln)



plot()

Plot an array(s) of data given a template and graphics method.

import vcs

f=cu.open('clt.nc')

s=f.getslab('clt')

x=vcs.init()

x.plot(s)



clear()

This routine will remove all plots on the VCS Canvas.

import vcs

f=cu.open('clt.nc')

s=f.getslab('clt')

x=vcs.init()

x.plot(s)

x.clear()

mode()

Updating of the graphical displays on the VCS Canvas can be deferred until a
later time.

import vcs

x=vcs.init()

x.mode=0



update()

If a series of commands are given to VCS and the Canvas Mode is set to manual,
then use this function to update the VCS Canvas manually.

import vcs

f=cu.open('clt.nc')

s=f.getslab('clt')

x=vcs.init()

x.mode=0

x.plot(s'default','boxfill','quick')

box=x.getboxfill('quick')

box.color_1=100

box.xticlabels('lon30','lon30')

box.xticlabels('','')

box.datawc(1e20,1e20,1e20,1e20)

box.datawc(-45.0, 45.0, -90.0, 90.0)

x.update()



open()

Open VCS Canvas object. This routine really just manages the VCS canvas. It
will popup the VCS Canvas for viewing. It can be used to display only the VCS
Canvas.

import vcs

x=vcs.init()

x.open()



close()

Close the VCS Canvas. It will remove the VCS Canvas object from the screen,
but not deallocate it.

import vcs

x=vcs.init()

x.plot(s)

a.close()

portrait()

Change the VCS Canvas orientation to Portrait.

import vcs

f=cu.open('clt.nc')

s=f.getslab('clt')

x=vcs.init()

x.plot(s)

x.portrait()

landscape()

Change the VCS Canvas orientation to Landscape.

import vcs

f=cu.open('clt.nc')

s=f.getslab('clt')

x=vcs.init()

x.plot(s)

x.landscape()

page()

Change the VCS Canvas orientation to either 'portrait' or 'landscape'.

import vcs

f=cu.open('clt.nc')

s=f.getslab('clt')

x=vcs.init()

x.plot(s)

x.page()

geometry()

The geometry command is used to set the size and position of the VCS canvas.

import vcs

f=cu.open('clt.nc')

s=f.getslab('clt')

x=vcs.init()

x.plot(s)

x.geometry(450, 337,100, 100)

printer()

his function creates a temporary cgm file and then sends it to the specified
printer.

import vcs

f=cu.open('clt.nc')

s=f.getslab('clt')

x=vcs.init()

x.plot(s)

x.printer('printer_name')

gif()

Generate a gif file

import vcs

f=cu.open('clt.nc')

s=f.getslab('clt')

x=vcs.init()

x.plot(s)

x.gif('example')

postscript()

Generate a postscript file.

import vcs

f=cu.open('clt.nc')

s=f.getslab('clt')

x=vcs.init()

x.plot(s)

x.postscript('example')

cgm()

Generate a cgm file.

import vcs

f=cu.open('clt.nc')

s=f.getslab('clt')

x=vcs.init()

x.plot(s)

x.cgm('example')

raster()

Generate a raster file.

import vcs

f=cu.open('clt.nc')

s=f.getslab('clt')

x=vcs.init()

x.plot(s)

x.raster('example')

pstogif()

Converts a postscript file to a gif file.

import vcs

x=vcs.init()

x.pstogif('filename.ps')

boxfill()

Generate a boxfill plot given the data, boxfill graphics method, and template.

import vcs

f=cu.open('clt.nc')

s=f.getslab('clt')

x=vcs.init()

x.boxfill(s)



continents()

Generate a continents plot given the continents graphics method, and template.

import vcs

f=cu.open('clt.nc')

s=f.getslab('clt')

x=vcs.init()

x.continents(s)



isofill()

Generate a isofill plot given the data, isofill graphics method, and template.

import vcs

f=cu.open('clt.nc')

s=f.getslab('clt')

x=vcs.init()

x.isofill(s)



isoline()

Generate a isoline plot given the data, isoline graphics method, and template.

import vcs

f=cu.open('clt.nc')

s=f.getslab('clt')

x=vcs.init()

x.isoline(s)



outfill()

Generate a outfill plot given the data, outfill graphics method, and template.

import vcs

f=cu.open('clt.nc')

s=f.getslab('clt')

x=vcs.init()

x.outfill(s)



outline()

Generate a outline plot given the data, outline graphics method, and template.

import vcs

f=cu.open('clt.nc')

s=f.getslab('clt')

x=vcs.init()

x.outline(s)



scatter()

Generate a scatter plot given the data, scatter graphics method, and template.

import vcs

f=cu.open('clt.nc')

s=f.getslab('clt')

x=vcs.init()

x.scatter(s)



vector()

Generate a vector plot given the data, vector graphics method, andtemplate.

import vcs

f=cu.open('clt.nc')

s=f.getslab('clt')

x=vcs.init()

x.vector(s)



xvsy()

Generate a XvsY plot given the data, XvsY graphics method, and template.

import vcs

f=cu.open('clt.nc')

s=f.getslab('clt')

x=vcs.init()

x.xvsy(s)



xyvsy()

Generate a Xyvsy plot given the data, Xyvsy graphics method, and template.

import vcs

f=cu.open('clt.nc')

s=f.getslab('clt')

x=vcs.init()

x.xyvsy(s)



yxvsx()

Generate a Yxvsx plot given the data, Yxvsx graphics method, and template.

import vcs

f=cu.open('clt.nc')

s=f.getslab('clt')

x=vcs.init()

x.yxvsx(s)



graphicsmethodname()

Returns the grapics method's type string: boxfill, isofill, isoline, outfill,
outline, continents, scatter, vector, xvsy, xyvsy, or yxvsx.

import vcs

x=vcs.init()

box=x.getboxfill()

x.graphicsmethodname(box)

getcontinentstype()

Return continents type from VCS. Remember the value can only be between 0 and
11.

import vcs

x=vcs.init()

cont_type = x.getcontinentstype()

isgraphicsmethod()

Indicates if the entered argument is one of the following graphics methods:
boxfill, isofill, isoline, outfill, outline, continents, scatter, vector,
xvsy, xyvsy, yxvsx.

import vcs

x=vcs.init()

box=x.getboxfill('quick')

x.isgraphicsmethod(box)

isboxfill()

Check to see if an object is a VCS primary boxfill graphics method object.

import vcs

x=vcs.init()

box=x.getboxfill("quick")

x.isboxfill(box)

iscontinents()

Check to see if an object is a VCS primary continents graphics method.

import vcs

x=vcs.init()

con=x.getcontinents("quick")

x.iscontinents(con)



isisofill()

Check to see if an object is a VCS primary isofill graphics method.

import vcs

x=vcs.init()

iso=x.getisofill("quick")

x.isisofill(iso)



isisoline()

Check to see if an object is a VCS primary isoline graphics method.

import vcs

x=vcs.init()

iso=x.getisoline("quick"

x.isisoline(iso)

isoutfill()

Check to see if this object is a VCS primary outfill graphics method.

import vcs

x=vcs.init()

out=x.getoutfill("quick")

x.isoutfill(out)

isoutline()

Check to see if an object is a VCS primary outline graphics method.

import vcs

x=vcs.init()

out=x.getoutline("quick")

x.isoutline(out)

isvector()

Check to see if an object is a VCS primary vector graphics method.

import vcs

x=vcs.init()

vec=x.getvector("quick")

x.isvector(vec)

isxvsy()

Check to see if an object is a VCS primary xvsy graphics method.

import vcs

x=vcs.init()

xy=x.getxvsy("quick")

x.isxvsy(xy)

isxyvsy()

Check to see if an object is a VCS primary Xyvsy graphics method.

import vcs

x=vcs.init()

xyy=x.getxyvsy("quick")

x.isxyvsy(xyy)

isyxvsx()

Check to see if an object is a VCS primary yxvsx graphics method.

import vcs

x=vcs.init()

yxx=x.getyxvsx("quick")

x.isyxvsx(yxx)

istemplate()

Indicates if the entered argument a template.

import vcs

x=vcs.init()

templt=x.gettemplate('quick')

x.istemplate(templt)

issecondaryobject()

Query to see if an object is a secondary object.

import vcs

x=vcs.init()

line=x.getline()

x.issecondaryobject(line)

isfillarea()

Check to see if an object is a VCS secondary fillarea.

import vcs

x=vcs.init()

fa=x.getfillarea("def37")

x.isfillarea(fa)

isline()

Check to see if this object is a VCS secondary line.

import vcs

x=vcs.init()

ln=x.getline()

x.isline(ln)

ismarker()

Check to see if this object is a VCS secondary marker.

import vcs

x=vcs.init()

ln=x.getmarker()

x.ismarker(ln)

istextcombined()

Check to see if an object is a VCS secondary text combined.

import vcs

x=vcs.init()

tc=x.gettextcombined("std", "7left")

x.istextcombined(tc)

istextorientation()

Check to see if an object is a VCS secondary text orientation.

import vcs

x=vcs.init()

to=x.gettextorientation("7left")

x.istextorientation(to)

istexttable()

Check to see if an object is a VCS secondary text table.

import vcs

x=vcs.init()

tt=x.gettexttable("std")

x.istexttable(tt)

listelements()

Returns a Python list of all the VCS class objects.

import vcs

x=vcs.init()

x.listelements()

show()

Show the list of VCS primary and secondary class objects.

import vcs

x=vcs.init()

x.show('boxfill')

x.show('isofill')

x.show(`template')

x.show(`line')

createboxfill()

Create a new boxfill graphics method given the name and the existingboxfill
graphics method to copy the attributes from.

import vcs

x=vcs.init()

box=x.createboxfill('example','quick')

getboxfill()

his function will create a boxfill class object from an existing VCS boxfill
graphics method.

import vcs

x=vcs.init()

box2=x.getboxfill('quick')

createcontinents()

Create a new continents graphics method given the the name and the existing
continents graphics method to copy the attributes from.

import vcs

x=vcs.init()

con=x.createcontinents('example','quick')

getcontinents()

This function will create a continents class object from an existing VCS
continents graphics method.

import vcs

x=vcs.init()

con2=x.getcontinents('quick')

createisofill()

Create a new isofill graphics method given the the name and the existing
isofill graphics method to copy the attributes from.

import vcs

x=vcs.init()

iso=x.createisofill('example','quick')

getisofill()

This function will create a isofill class object from an existing VCS isofill
graphics method.

import vcs

x=vcs.init()

iso2=x.getisofill('quick')

createisoline()

Create a new isoline graphics method given the the name and the existing
isoline graphics method to copy the attributes from.

import vcs

x=vcs.init()

iso=x.createisoline('example','quick')

getisoline()

This function will create a isoline class object from an existing VCS isoline
graphics method.

import vcs

x=vcs.init()

iso2=x.getisoline('quick')

createoutfill()

Create a new outfill graphics method given the the name and the existing
outfill graphics method to copy the attributes from.

import vcs

x=vcs.init()

out=x.createoutfill('example','quick')

getoutfill()

This function will create a outfill class object from an existing VCS outfill
graphics method.

import vcs

x=vcs.init()

out2=x.getoutfill('quick')

createoutline()

Create a new outline graphics method given the the name and the existing
outline graphics method to copy the attributes from.

import vcs

x=vcs.init()

out=x.createoutline('example','quick')

getoutline()

This function will create a outline class object from an existing VCS outline
graphics method.

import vcs

x=vcs.init()

out2=x.getoutline('quick')

createscatter()

Create a new scatter graphics method given the the name and the existing
mscatter graphics method to copy the attributes from.

import vcs

x=vcs.init()

sct=x.createscatter('example','quick')

getscatter()

This function will create a scatter class object from an existing VCS scatter
graphics method.

import vcs

x=vcs.init()

sct2=x.getscatter('quick')

createvector()

Create a new vector graphics method given the the name and the existing vector
graphics method to copy the attributes from.

import vcs

x=vcs.init()

vec=x.createvector('example','quick')

getvector()

This function will create a vector class object from an existing VCS vector
graphics method.

import vcs

x=vcs.init()

vec2=x.getvector('quick')

createxvsy()

Create a new XvsY graphics method given the the name and the existing XvsY
graphics method to copy the attributes from.

import vcs

x=vcs.init()

xy=x.createxvsy('example','quick')

getxvsy()

This function will create a XvsY class object from an existing VCS XvsY
graphics method.

import vcs

x=vcs.init()

xy2=x.getxvsy('quick')

createxyvsy()

Create a new Xyvsy graphics method given the the name and the existing Xyvsy
graphics method to copy the attributes from.

import vcs

x=vcs.init()

xyy=x.createxyvsy('example','quick')

getxyvsy()

This function will create a Xyvsy class object from an existing VCS Xyvsy
graphics method.

import vcs

x=vcs.init()

xyy2=x.getxyvsy('quick')

createyxvsx()

Create a new Yxvsx graphics method given the the name and the existing Yxvsx
graphics method to copy the attributes from.

import vcs

x=vcs.init()

yxx=x.createyxvsx('example','quick')

getyxvsx()

This function will create a Yxvsx class object from an existing VCS Yxvsx
graphics method.

import vcs

x=vcs.init()

yxx2=x.getyxvsx('quick')

createtemplate()

Create a new template given the the name and the existing template to copy the
attributes from.

import vcs

x=vcs.init()

con=x.createtemplate('example','quick')

gettemplate()

his function will create a template class object from an existing VCS
template.

import vcs

x=vcs.init()

templt2=x.gettemplate('quick')

setcolormap()

This routine will change the VCS color map.

import vcs

x=vcs.init()

x.setcolormap("AMIP")

setcolorcell()

Set a individual color cell in the active colormap. If default is the active
colormap, then return an error string.

import vcs

x=vcs.init()

x.setcolormap("AMIP")

a.setcolorcell(11,0,0,0)

x.setcolorcell(21,100,0,0)

colormapgui()

Run the VCS colormap interface.

The colormapgui command is used to bring up the VCS colormap interface. The
interface is used to select, create, change, or remove colormaps.

Note:

The colormapgui GUI will only work for 8-bit 'Pseudo Color'.

import vcs

x=vcs.init()

x.colormapgui()

createfillarea()

Create a new fillarea secondary method given the the name and the existing
fillarea secondary method to copy the attributes from.

import vcs

x=vcs.init()

fa=x.createfillarea('example','black')

getfillarea()

This function will create a fillarea class object from an existing VCS
fillarea secondary method.

import vcs

x=vcs.init()

fa2=x.getfillarea('quick')

createline()

Create a new line secondary method given the the name and the existing line
secondary method to copy the attributes from.

import vcs

x=vcs.init()

ln=x.createline('example','black')

getline()

This function will create a line class object from an existing VCS line
secondary method.

import vcs

x=vcs.init()

ln2=x.getline('quick')

createmarker()

Create a new marker secondary method given the the name and the existing
marker secondary method to copy the attributes from.

import vcs

x=vcs.init()

mrk=x.createmarker('example','black')

getmarker()

This function will create a marker class object from an existing VCS marker
secondary method.

import vcs

x=vcs.init()

mrk2=x.getmarker('quick')

createtextcombined()

Create a new textcombined secondary method given the the names and the
existing texttable and textorientation secondary methods to copy the
attributes from. I

import vcs

x=vcs.init()

tc=x.createtextcombined('example1','std','example1','7left')

gettextcombined()

This function will create a textcombined class object from an existing VCS
texttable secondary method and an existing VCS textorientation secondary
method.

import vcs

x=vcs.init()

tc2=x.gettextcombined('std','7left')

createtextorientation()

Create a new textorientation secondary method given the the name and he
existing textorientation secondary method to copy the attributes from.

import vcs

x=vcs.init()

to=x.createtextorientation('example1')

gettextorientation()

This function will create a textorientation class object from an existing VCS
textorientation secondary method.

import vcs

x=vcs.init()

to2=x.gettextorientation('quick')

createtexttable()

Create a new texttable secondary method given the the name and the existing
texttable secondary method to copy the attributes from.

import vcs

x=vcs.init()

tt=x.createtexttable('example','black')

gettexttable()

This function will create a texttable class object from an existing VCS
texttable secondary method.

import vcs

x=vcs.init()

tt2=x.gettexttable('quick')

removeobject()

This function allows the user to remove these objects from the appropriate
class list.

Note, To remove the object completely from Python, remember to use the "del"
function.

Also note, The user is not allowed to remove a "default" class object.

import vcs

x=vcs.init()

line=x.getline('red')

x.removeobject(line)

iso=x.createisoline('example')

x.removeobject(iso)

setcontinentstype()

One has the option of using continental maps that are predefined or that are
user-defined. Predefined continental maps are either internal to VCS or are
specified by external files. (The continents type number ranges from 0 to 11.)

import vcs

x=vcs.init()

f=cu.open('clt.nc')

s=f.getslab('clt')

x.setcontinentstype(3)

x.plot(array,'default','isofill','quick')

set()

Set the default VCS primary class objects: template and graphics methods.

import vcs

x=vcs.init()

f=cu.open('clt.nc')

s=f.getslab('clt')

x.set('isofill','quick')

x.plot(s)

animate()

Animate the contents of the VCS Canvas. Currently, only one display can be
shown in the VCS Canvas for the animation to work. This function pops up the
animation GUI.

Note:

The animation GUI will only work for 8-bit 'Pseudo Color'.

import vcs

x=vcs.init()

f=cu.open('clt.nc')

s=f.getslab('clt')

x.plot(s)

x.animate()

flush()

The flush command executes all buffered X events in the que.

import vcs

f=cu.open('clt.nc')

s=f.getslab('clt')

x=vcs.init()

x.plot(s)

x.flush()

grid()

Set the default plotting region for variables that have more dimension values
than the graphics method. This will also be used for animating plots over the
third and fourth dimensions.

import vcs

f=cu.open('clt.nc')

s=f.getslab('clt')

x=vcs.init()

x.grid(12,24, -70,70, -150,150)

x.plot(s)



resetgrid()

Set the plotting region to default values. That is, let the variable's
dimension values determine the grid.

import vcs

f=cu.open('clt.nc')

s=f.getslab('clt')

x=vcs.init()

x.resetgrid()

x.plot(s)



###  Index

#####  A

  * [animate 120](vcs-5.html#marker-910411)

#####  B

  * [boxfill 39](vcs-5.html#marker-910438)

#####  C

  * [cgm 36](vcs-5.html#marker-910426)
  * [clear 45](vcs-5.html#marker-910449)
  * [close 32](vcs-5.html#marker-910417)
  * [colormapgui 99](vcs-5.html#marker-910500)
  * [continents 40](vcs-5.html#marker-910439)
  * [createboxfill 53](vcs-5.html#marker-910473)
  * [createcontinents 56](vcs-5.html#marker-910475)
  * [createfillarea 99](vcs-5.html#marker-910499)
  * [createisofill 59](vcs-5.html#marker-910477)
  * [createisoline 63](vcs-5.html#marker-910479)
  * [createline 102](vcs-5.html#marker-910502)
  * [createmarker 105](vcs-5.html#marker-910504)
  * [createoutfill 67](vcs-5.html#marker-910481)
  * [createoutline 70](vcs-5.html#marker-910484)
  * [createscatter 73](vcs-5.html#marker-910486)
  * [createtemplate 95](vcs-5.html#marker-910495)
  * [createtextcombined 108](vcs-5.html#marker-910506)
  * [createtextorientation 112](vcs-5.html#marker-910508)
  * [createtexttable 116](vcs-5.html#marker-910510)
  * [createvector 77](vcs-5.html#marker-910488)
  * [createxvsy 80](vcs-5.html#marker-910489)
  * [createxyvsy 85](vcs-5.html#marker-910491)
  * [createyxvsx 90](vcs-5.html#marker-910493)

#####  F

  * [flush 121](vcs-5.html#marker-910513)
  * [fonts, table of 206](vcs-10.html#marker-911155)

#####  G

  * [geometry 33](vcs-5.html#marker-910421)
  * [getboxfill 53](vcs-5.html#marker-910474)
  * [getcontinents 56](vcs-5.html#marker-910476)
  * [getcontinentstype 45](vcs-5.html#marker-910451)
  * [getfillarea 100](vcs-5.html#marker-910501)
  * [getisofill 59](vcs-5.html#marker-910478)
  * [getisoline 63](vcs-5.html#marker-910480)
  * [getline 103](vcs-5.html#marker-910503)
  * [getmarker 105](vcs-5.html#marker-910505)
  * [getoutfill 67](vcs-5.html#marker-910482)
  * [getoutline 70](vcs-5.html#marker-910483)
  * [getscatter 73](vcs-5.html#marker-910485)
  * [gettemplate 96](vcs-5.html#marker-910496)
  * [gettextcombined 109](vcs-5.html#marker-910507)
  * [gettextorientation 113](vcs-5.html#marker-910509)
  * [gettexttable 116](vcs-5.html#marker-910511)
  * [getvector 77](vcs-5.html#marker-910487)
  * [getxvsy 81](vcs-5.html#marker-910490)
  * [getxyvsy 86](vcs-5.html#marker-910492)
  * [getyxvsx 91](vcs-5.html#marker-910494)
  * [gif 35](vcs-5.html#marker-910423)
  * [graphicsmethodtype 45](vcs-5.html#marker-910450)
  * [grid 121](vcs-5.html#marker-910514)

#####  H

  * [help 30](vcs-5.html#marker-892715)

#####  I

  * [init 29](vcs-5.html#marker-892680)
  * [isboxfill 46](vcs-5.html#marker-910453)
  * [iscontinents 46](vcs-5.html#marker-910454)
  * [isfillarea 50](vcs-5.html#marker-910465)
  * [isgraphicsmethod 46](vcs-5.html#marker-910452)
  * [isisofill 47](vcs-5.html#marker-910455)
  * [isisoline 47](vcs-5.html#marker-910456)
  * [isline 51](vcs-5.html#marker-910466)
  * [ismarker 51](vcs-5.html#marker-910467)
  * [isofill 40](vcs-5.html#marker-910440)
  * [isoline 41](vcs-5.html#marker-910441)
  * [isoutfill 47](vcs-5.html#marker-910457)
  * [isoutline 48](vcs-5.html#marker-910458)
  * [issecondaryobject 50](vcs-5.html#marker-910464)
  * [istemplate 49](vcs-5.html#marker-910463)
  * [istextcombined 51](vcs-5.html#marker-910468)
  * [istextorientation 51](vcs-5.html#marker-910469)
  * [istexttable 52](vcs-5.html#marker-910470)
  * [isvector 48](vcs-5.html#marker-910459)
  * [isxvsy 48](vcs-5.html#marker-910460)
  * [isxyvsy 49](vcs-5.html#marker-910461)
  * [isyxvsx 49](vcs-5.html#marker-910462)

#####  L

  * [landscape 33](vcs-5.html#marker-910419)
  * [line styles 207](vcs-10.html#marker-911154)
  * [listelements 52](vcs-5.html#marker-910471)

#####  M

  * [mode 31](vcs-5.html#marker-910414)

#####  O

  * [objecthelp 30](vcs-5.html#marker-892732)
  * [open 32](vcs-5.html#marker-910416)
  * [outfill 41](vcs-5.html#marker-910442)
  * [outline 42](vcs-5.html#marker-910443)

#####  P

  * [page 33](vcs-5.html#marker-910420)
  * [plot 38](vcs-5.html#marker-910437)
  * [portrait 33](vcs-5.html#marker-910418)
  * [postscript 36](vcs-5.html#marker-910425)
  * [printer 34](vcs-5.html#marker-910422)
  * [pstogif 37](vcs-5.html#marker-910436)

#####  R

  * [raster 37](vcs-5.html#marker-910427)
  * [removeobject 118](vcs-5.html#marker-910512)
  * [resetgrid 121](vcs-5.html#marker-910515)

#####  S

  * [scatter 42](vcs-5.html#marker-910444)
  * [scripts 26](vcs-4.html#marker-885201)
    * [saving 26](vcs-4.html#marker-885201)
  * [Set 120](vcs-5.html#marker-910412)
  * [setcolorcell 98](vcs-5.html#marker-910498)
  * [setcolormap 98](vcs-5.html#marker-910497)
  * [setcontinentstype 119](vcs-5.html#marker-910413)
  * [show 52](vcs-5.html#marker-910472)
  * [styles, line 207](vcs-10.html#marker-911154)

#####  U

  * [update 32](vcs-5.html#marker-910415)

#####  V

  * [vector 43](vcs-5.html#marker-910446)

#####  X

  * [xvsy 43](vcs-5.html#marker-910445)
  * [xyvsy 44](vcs-5.html#marker-910448)

#####  Y

  * [yxvsx 44](vcs-5.html#marker-910447)

[Go to Previous](vcs-10.html) [Go to Main](vcs.html)


