---
layout: default
title: VCS Chapter 9
---
##  CHAPTER 9 Quick Reference Guides

####

![](vcs-2.gif)

Commands and Their Usage

Command

Usage

Initialization

init

a = vcs.init()

Help

help

vcs.help()

objecthelp

a.objecthelp(b)

Canvas

mode

a.mode=1

update

a.update()

open

a.open()

close

a.close()

flushcanvas

a.flushcanvas()

refreshcanvas

a.refreshcanvas()

portrait

a.portrait()

landscape

a.landscape()

page

a.page()

geometry

a.geometry(450, 337,100, 100)

Printing and Saving Graphics

printer

a.printer('printer_name')

gif

a.gif('gif_file_name')

postscript

a.postscript('postscript_file_name')

cgm

a.cgm('cgm_file_name')

raster

a.raster('raster_file_name')

pstogif

a.pstogif('postscript_file_name')

Plot and Clear Commands

plot

a.plot(array)

boxfill

a.boxfill(array)

continents

a.continents(array)

isofill

a.isofill(array)

isoline

a.isoline(array)

outfill

a.outfill(array)

outline

a.outline(array)

scatter

a.scatter(array)

vector

a.vector(array)

xvsy

a.xvsy(array)

xyvsy

a.xyvsy(array)

yxvsx

a.yxvsx(array)

clear

a.clear()

Query Functions

graphicsmethodname

a.graphicsmethodname('box')

getcontinentstype

a.getcontinentstype()

isgraphicsmethod

a.isgraphicsmethod()

isboxfill

a.isboxfill()

iscontinents

a.iscontinents()

isisofill

a.isisofill()

isisoline

a.isisoline()

isoutfill

a.isoutfill()

isoutline

a.isoutline()

isvector

a.isvector()

isxvsy

a.isxvsy()

isxyvsy

a.isxyvsy()

isyxvsx

a.isyxvsx()

istemplate

a.istemplate()

issecondaryobject

a.issecondaryobject()

isfillarea

a.isfillarea()

isline

a.isline()

ismarker

a.ismarker()

istextcombined

a.istextcombined()

istextorientation

a.istextorientation()

istexttable

a.istexttable()

List Available Templates, Graphics Methods and Secondary Objects

listelements

a.listelements()

show

a.show(`boxfill')

list

box.list()

con.list

isol.list()

isof.list()

outl.list()

outf.list()

sct.list()

vc.list()

xy.list()

tpl.list()

fa.list()

tt.list()

to.list()

tc.list()

Graphics Methods Objects

Boxfill

createboxfill

box=a.createboxfill('new')

getboxfill

box=a.getboxfill()

Continents

createcontinents

con=a.createcontinents('new')

getcontinents

con=a.getcontinents()

Isofill

createisofill

iso=a.createisofill('new')

getisofill

iso=a.getisofill()

Isoline

createisoline

iso=a.createisoline(`new')

getisoline

iso=a.getisoline()

Outfill

createoutfill

out=a.createoutfill(`new')

getoutfill

out=a.getoutfill()

Outline

createoutline

out=a.createoutline(`new')

getoutline

out=a.getoutline()

Scatter

createscatter

scr=a.createscatter(`new')

getscatter

scr=a.getscatter()

Vector

createvector

vc=a.createvector(`new')

getvector

vc=a.getvector()

XvsY

createxvsy

xy=a.createxvsy(`new')

getxvsy

xy=a.getxvsy()

Xyvsy

createxyvsy

xy=a.createxyvsy(`new')

getxyvsy

xy=a.getxyvsy()

Yxvsx

createyxvsx

yx=a.createyxvsx(`new')

getyxvsx

yx=a.createyxvsx()

Picture Template

createtemplate

tpl=a.createtemplate(`new')

gettemplate

tpl=gettemplate()

Secondary Objects

Colormap Commands

setcolormap

a.setcolormap("colormap_name")

setcolorcell

.setcolorcell(16,100,100,100)

colormapgui

a.colormapgui()

Fill Area

createfillarea

fa=a.createfillarea('new')

getfillarea

fa=a.getfillarea()

Line

createline

ln=a.createline(`new')

getline

ln=a.getline()

marker

createmarker

mk=a.createmarker(`new')

getmarker

mk=a.getlmarker()

Text-Combined

createtextcombined

tc=a.createtextcombined(`new')

gettextcombined

tc=a.gettextcombined()

Text-Orientation

createtextorientation

to.createtextorientation(`new')

gettextorientation

to=a.gettextorientation()

Text-Table

createtexttable

tt=a.createtexttable(`new')

gettexttable

tt=a.gettexttable()

Remove Objects

removeobject

a.removeobject(a)

Set Default Picture Template and Graphics Methods

set

a.set('isofill','some_isofill_name')

Set Continents Type

setcontinentstype

a.setcontinentstype(3)

Animation

animate

a.animate()

Flush

flush

a.flush()

Grid

grid

a.grid(12,24, -90,90, -180,180)

resetgrid

a.resetgrid()

####

![](vcs-2.gif)

VCS Cheat Sheet

init

graphicsmethodname

createisoline

fillareaobject

help

getcontinentstype

getisoline

createline

objecthelp

isgraphicsmethod

isolineobject

getline

mode

isboxfill

createoutfill

lineobject

update

iscontinents

getoutfill

marker

open

isisofill

outfillobject

createmarker

close

isisoline

createoutline

getmarker

flushcanvas

isoutfill

getoutline

markerobject

refreshcanvas

isoutline

outlineobject

createtextcombined

portrait

isvector

createscatter

gettextcombined

landscape

isxvsy

getscatter

textcombinedobject

page

isxyvsy

scatterobject

createtextorientation

geometry

isyxvsx

createvector

gettextorientation

printer

istemplate

getvector

textorientationobject

gif

issecondaryobject

vectorobject

createtexttable

postscript

isfillarea

createxvsy

gettexttable

cgm

isline

getxvsy

texttableobject

raster

ismarker

xvsyobject

removeobject

pstogif

istextcombined

createxyvsy

set

plot

istextorientation

getxyvsy

setcontinentstype

boxfill

istexttable

xyvsyobject

animate

continents

listelements

createyxvsx

flush

isofill

show

getyxvsx

grid

isoline

createboxfill

yxvsxobject

resetgrid

outfill

getboxfill

createtemplate

list

outline

boxfillobject

gettemplate



scatter

createcontinents

templateobject



vector

getcontinents

setcolormap



xvsy

continentsobject

setcolorcell



xyvsy

createisofill

colormapgui



yxvsx

getisofill

createfillarea



clear

isofillobject

getfillarea



[Go to Main](vcs.html) [Go to Previous](vcs-8.html) [Go to Next](vcs-10.html)


