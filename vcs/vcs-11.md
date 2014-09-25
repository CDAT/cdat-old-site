---
layout: default
title: VCS Chapter 11
---

##  CHAPTER 11 The VCS Module

The VCS module is designed to provide access to the VCS graphical interface.


###The VCS Graphics Module

VCS is CDAT's interface to a library for two-dimensional graphics that has
been particularly customized for climate data but which in fact can be used by
many scientific applications. VCS has a rich set of facilities that allow you
to easily make sophisticated presentation graphics.

VCS as a module has the principal function init() which returns a Canvas
object. The rest of the commands are methods on the Canvas object. Up to 8
canvases can be active at one time.


<table class="table">
<tbody><tr>
<td rowspan="1" colspan="1">
<p class="Normal">
<a name="pgfId-908099"></a>Command</p>
</td>
<td rowspan="1" colspan="1">
<p class="Normal">
<a name="pgfId-908101"></a>Description</p>
</td>
<td rowspan="1" colspan="1">
<p class="Normal">
<a name="pgfId-908103"></a>Examples</p>
</td>
</tr>
<tr>
<td rowspan="1" colspan="1">
<code class="Normal">
<a name="pgfId-908105"></a>init()</code>
</td>
<td rowspan="1" colspan="1">
<p class="Normal">
<a name="pgfId-908107"></a>Initializes and creates a VCS object, reads in the initial.attribute file and set up the VCS default values.</p>
<p class="Normal">
<a name="pgfId-908108"></a>Note: The number of VCS Canvases is limited to eight.</p>
</td>
<td><pre style="word-break:normal">import vcs
x=vcs.init()</pre></td></tr>
<tr>
<td rowspan="1" colspan="1">
<code class="Normal">
<a name="pgfId-909999"></a>help()</code>
</td>
<td rowspan="1" colspan="1">
<p class="Normal">
<a name="pgfId-910001"></a>Gives insight to other VCS functions by providing a description and at least one example.</p>
</td>
<td><pre style="word-break:normal">import vcs
vcs.help()
vcs.help(`init')</pre></td></tr>
<tr>
<td rowspan="1" colspan="1">
<code class="Normal">
<a name="pgfId-910041"></a>objecthelp()</code>
</td>
<td rowspan="1" colspan="1">
<p class="Normal">
<a name="pgfId-910043"></a>Print out information on VCS objects. See example on its use.</p>
</td>
<td><pre style="word-break:normal">import vcs
x=vcs.init()
ln=a.createline('red')
x.objecthelp(ln)
</pre></td></tr>
<tr>
<td rowspan="1" colspan="1">
<code class="Normal">
<a name="pgfId-910588"></a>plot()</code>
</td>
<td rowspan="1" colspan="1">
<p class="Normal">
<a name="pgfId-910590"></a>Plot an array(s) of data given a template and graphics method. </p>
</td>
<td><pre style="word-break:normal">import vcs
f=cu.open('clt.nc')
s=f.getslab('clt')
x=vcs.init()
x.plot(s)
</pre></td></tr>
<tr>
<td rowspan="1" colspan="1">
<code class="Normal">
<a name="pgfId-911890"></a>clear()</code>
</td>
<td rowspan="1" colspan="1">
<p class="Normal">
<a name="pgfId-911892"></a>This routine will remove all  plots on the VCS Canvas.</p>
</td>
<td><pre style="word-break:normal">import vcs
f=cu.open('clt.nc')
s=f.getslab('clt')
x=vcs.init()
x.plot(s)
x.clear()</pre></td></tr>
<tr>
<td rowspan="1" colspan="1">
<code class="Normal">
<a name="pgfId-910030"></a>mode()</code>
</td>
<td rowspan="1" colspan="1">
<p class="Normal">
<a name="pgfId-910032"></a>Updating of the graphical displays on the VCS Canvas can be deferred until a later time. </p>
</td>
<td><pre style="word-break:normal">import vcs
x=vcs.init()
x.mode=0
</pre></td></tr>
<tr>
<td rowspan="1" colspan="1">
<code class="Normal">
<a name="pgfId-910019"></a>update()</code>
</td>
<td rowspan="1" colspan="1">
<p class="Normal">
<a name="pgfId-910021"></a>If a series of commands are given to VCS and the Canvas Mode is set to manual, then use this function to update the VCS Canvas manually.</p>
</td>
<td><pre style="word-break:normal">import vcs
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
</pre></td></tr>
<tr>
<td rowspan="1" colspan="1">
<code class="Normal">
<a name="pgfId-910135"></a>open()</code>
</td>
<td rowspan="1" colspan="1">
<p class="Normal">
<a name="pgfId-910137"></a>Open VCS Canvas object. This routine really just manages the VCS canvas. It will popup the VCS Canvas for viewing. It can be used to display only the VCS Canvas.</p>
</td>
<td><pre style="word-break:normal">import vcs
x=vcs.init()
x.open()
</pre></td></tr>
<tr>
<td rowspan="1" colspan="1">
<code class="Normal">
<a name="pgfId-910124"></a>close()</code>
</td>
<td rowspan="1" colspan="1">
<p class="Normal">
<a name="pgfId-910126"></a>Close the VCS Canvas. It will remove the VCS Canvas object from the screen, but not deallocate it.</p>
</td>
<td><pre style="word-break:normal">import vcs
x=vcs.init()
x.plot(s)
a.close()</pre></td></tr>
<tr>
<td rowspan="1" colspan="1">
<code class="Normal">
<a name="pgfId-910113"></a>portrait()</code>
</td>
<td rowspan="1" colspan="1">
<p class="Normal">
<a name="pgfId-910115"></a>Change the VCS Canvas orientation to Portrait.</p>
</td>
<td><pre style="word-break:normal">import vcs
f=cu.open('clt.nc')
s=f.getslab('clt')
x=vcs.init()
x.plot(s)
x.portrait()</pre></td></tr>
<tr>
<td rowspan="1" colspan="1">
<code class="Normal">
<a name="pgfId-910102"></a>landscape()</code>
</td>
<td rowspan="1" colspan="1">
<p class="Normal">
<a name="pgfId-910104"></a>Change the VCS Canvas orientation to Landscape.</p>
</td>
<td><pre style="word-break:normal">import vcs
f=cu.open('clt.nc')
s=f.getslab('clt')
x=vcs.init()
x.plot(s)
x.landscape()</pre></td></tr>
<tr>
<td rowspan="1" colspan="1">
<code class="Normal">
<a name="pgfId-910091"></a>page()</code>
</td>
<td rowspan="1" colspan="1">
<p class="Normal">
<a name="pgfId-910093"></a>Change the VCS Canvas orientation to either 'portrait' or 'landscape'.</p>
</td>
<td><pre style="word-break:normal">import vcs
f=cu.open('clt.nc')
s=f.getslab('clt')
x=vcs.init()
x.plot(s)
x.page()</pre></td></tr>
<tr>
<td rowspan="1" colspan="1">
<code class="Normal">
<a name="pgfId-910080"></a>geometry()</code>
</td>
<td rowspan="1" colspan="1">
<p class="Normal">
<a name="pgfId-910082"></a>The geometry command is used to set the size and position of the VCS canvas.</p>
</td>
<td><pre style="word-break:normal">import vcs
f=cu.open('clt.nc')
s=f.getslab('clt')
x=vcs.init()
x.plot(s)
x.geometry(450, 337,100, 100)</pre></td></tr>
<tr>
<td rowspan="1" colspan="1">
<code class="Normal">
<a name="pgfId-910255"></a>printer()</code>
</td>
<td rowspan="1" colspan="1">
<p class="Normal">
<a name="pgfId-910257"></a>his function creates a temporary cgm file and then sends it to the specified printer.</p>
</td>
<td><pre style="word-break:normal">import vcs
f=cu.open('clt.nc')
s=f.getslab('clt')
x=vcs.init()
x.plot(s)
x.printer('printer_name')</pre></td></tr>
<tr>
<td rowspan="1" colspan="1">
<code class="Normal">
<a name="pgfId-910244"></a>gif()</code>
</td>
<td rowspan="1" colspan="1">
<p class="Normal">
<a name="pgfId-910246"></a>Generate a gif file</p>
</td>
<td><pre style="word-break:normal">import vcs
f=cu.open('clt.nc')
s=f.getslab('clt')
x=vcs.init()
x.plot(s)
x.gif('example')</pre></td></tr>
<tr>
<td rowspan="1" colspan="1">
<code class="Normal">
<a name="pgfId-910233"></a>postscript()</code>
</td>
<td rowspan="1" colspan="1">
<p class="Normal">
<a name="pgfId-910235"></a>Generate a postscript file.</p>
</td>
<td><pre style="word-break:normal">import vcs
f=cu.open('clt.nc')
s=f.getslab('clt')
x=vcs.init()
x.plot(s)
x.postscript('example')</pre></td></tr>
<tr>
<td rowspan="1" colspan="1">
<code class="Normal">
<a name="pgfId-910222"></a>cgm()</code>
</td>
<td rowspan="1" colspan="1">
<p class="Normal">
<a name="pgfId-910224"></a>Generate a cgm file.</p>
</td>
<td><pre style="word-break:normal">import vcs
f=cu.open('clt.nc')
s=f.getslab('clt')
x=vcs.init()
x.plot(s)
x.cgm('example')</pre></td></tr>
<tr>
<td rowspan="1" colspan="1">
<code class="Normal">
<a name="pgfId-910519"></a>raster()</code>
</td>
<td rowspan="1" colspan="1">
<p class="Normal">
<a name="pgfId-910521"></a>Generate a raster file.</p>
</td>
<td><pre style="word-break:normal">import vcs
f=cu.open('clt.nc')
s=f.getslab('clt')
x=vcs.init()
x.plot(s)
x.raster('example')</pre></td></tr>
<tr>
<td rowspan="1" colspan="1">
<code class="Normal">
<a name="pgfId-910508"></a>pstogif()</code>
</td>
<td rowspan="1" colspan="1">
<p class="Normal">
<a name="pgfId-910510"></a>Converts a postscript file to a gif file.</p>
</td>
<td><pre style="word-break:normal">import vcs
x=vcs.init()
x.pstogif('filename.ps')</pre></td></tr>
<tr>
<td rowspan="1" colspan="1">
<code class="Normal">
<a name="pgfId-910486"></a>boxfill()</code>
</td>
<td rowspan="1" colspan="1">
<p class="Normal">
<a name="pgfId-910488"></a>Generate a boxfill plot given the data, boxfill graphics method, and  template.</p>
</td>
<td><pre style="word-break:normal">import vcs
f=cu.open('clt.nc')
s=f.getslab('clt')
x=vcs.init()
x.boxfill(s)
</pre></td></tr>
<tr>
<td rowspan="1" colspan="1">
<code class="Normal">
<a name="pgfId-910475"></a>continents()</code>
</td>
<td rowspan="1" colspan="1">
<p class="Normal">
<a name="pgfId-910477"></a>Generate a continents plot given the continents graphics method, and template. </p>
</td>
<td><pre style="word-break:normal">import vcs
f=cu.open('clt.nc')
s=f.getslab('clt')
x=vcs.init()
x.continents(s)
</pre></td></tr>
<tr>
<td rowspan="1" colspan="1">
<code class="Normal">
<a name="pgfId-910464"></a>isofill()</code>
</td>
<td rowspan="1" colspan="1">
<p class="Normal">
<a name="pgfId-910466"></a>Generate a isofill plot given the data, isofill graphics method, and template.</p>
</td>
<td><pre style="word-break:normal">import vcs
f=cu.open('clt.nc')
s=f.getslab('clt')
x=vcs.init()
x.isofill(s)
</pre></td></tr>
<tr>
<td rowspan="1" colspan="1">
<code class="Normal">
<a name="pgfId-910453"></a>isoline()</code>
</td>
<td rowspan="1" colspan="1">
<p class="Normal">
<a name="pgfId-910455"></a>Generate a isoline plot given the data, isoline graphics method, and template.</p>
</td>
<td><pre style="word-break:normal">import vcs
f=cu.open('clt.nc')
s=f.getslab('clt')
x=vcs.init()
x.isoline(s)
</pre></td></tr>
<tr>
<td rowspan="1" colspan="1">
<code class="Normal">
<a name="pgfId-910442"></a>outfill()</code>
</td>
<td rowspan="1" colspan="1">
<p class="Normal">
<a name="pgfId-910444"></a>Generate a outfill plot given the data, outfill graphics method, and template. </p>
</td>
<td><pre style="word-break:normal">import vcs
f=cu.open('clt.nc')
s=f.getslab('clt')
x=vcs.init()
x.outfill(s)
</pre></td></tr>
<tr>
<td rowspan="1" colspan="1">
<code class="Normal">
<a name="pgfId-910431"></a>outline()</code>
</td>
<td rowspan="1" colspan="1">
<p class="Normal">
<a name="pgfId-910433"></a>Generate a outline plot given the data, outline graphics method, and template.</p>
</td>
<td><pre style="word-break:normal">import vcs
f=cu.open('clt.nc')
s=f.getslab('clt')
x=vcs.init()
x.outline(s)
</pre></td></tr>
<tr>
<td rowspan="1" colspan="1">
<code class="Normal">
<a name="pgfId-910420"></a>scatter()</code>
</td>
<td rowspan="1" colspan="1">
<p class="Normal">
<a name="pgfId-910422"></a>Generate a scatter plot given the data, scatter graphics method, and template. </p>
</td>
<td><pre style="word-break:normal">import vcs
f=cu.open('clt.nc')
s=f.getslab('clt')
x=vcs.init()
x.scatter(s)
</pre></td></tr>
<tr>
<td rowspan="1" colspan="1">
<code class="Normal">
<a name="pgfId-910409"></a>vector()</code>
</td>
<td rowspan="1" colspan="1">
<p class="Normal">
<a name="pgfId-910411"></a>Generate a vector plot given the data, vector graphics method, andtemplate.</p>
</td>
<td><pre style="word-break:normal">import vcs
f=cu.open('clt.nc')
s=f.getslab('clt')
x=vcs.init()
x.vector(s)
</pre></td></tr>
<tr>
<td rowspan="1" colspan="1">
<code class="Normal">
<a name="pgfId-910398"></a>xvsy()</code>
</td>
<td rowspan="1" colspan="1">
<p class="Normal">
<a name="pgfId-910400"></a>Generate a XvsY plot given the data, XvsY graphics method, and template.</p>
</td>
<td><pre style="word-break:normal">import vcs
f=cu.open('clt.nc')
s=f.getslab('clt')
x=vcs.init()
x.xvsy(s)
</pre></td></tr>
<tr>
<td rowspan="1" colspan="1">
<code class="Normal">
<a name="pgfId-910387"></a>xyvsy()</code>
</td>
<td rowspan="1" colspan="1">
<p class="Normal">
<a name="pgfId-910389"></a>Generate a Xyvsy plot given the data, Xyvsy graphics method, and template. </p>
</td>
<td><pre style="word-break:normal">import vcs
f=cu.open('clt.nc')
s=f.getslab('clt')
x=vcs.init()
x.xyvsy(s)
</pre></td></tr>
<tr>
<td rowspan="1" colspan="1">
<code class="Normal">
<a name="pgfId-910376"></a>yxvsx()</code>
</td>
<td rowspan="1" colspan="1">
<p class="Normal">
<a name="pgfId-910378"></a>Generate a Yxvsx plot given the data, Yxvsx graphics method, and template. </p>
</td>
<td><pre style="word-break:normal">import vcs
f=cu.open('clt.nc')
s=f.getslab('clt')
x=vcs.init()
x.yxvsx(s)
</pre></td></tr>
<tr>
<td rowspan="1" colspan="1">
<code class="Normal">
<a name="pgfId-910731"></a>graphicsmethodname()</code>
</td>
<td rowspan="1" colspan="1">
<p class="Normal">
<a name="pgfId-910733"></a>Returns the grapics method's type string: boxfill, isofill, isoline, outfill, outline, continents, scatter, vector, xvsy, xyvsy, or yxvsx.</p>
</td>
<td><pre style="word-break:normal">import vcs
x=vcs.init()
box=x.getboxfill()
x.graphicsmethodname(box)</pre></td></tr>
<tr>
<td rowspan="1" colspan="1">
<code class="Normal">
<a name="pgfId-910720"></a>getcontinentstype()</code>
</td>
<td rowspan="1" colspan="1">
<p class="Normal">
<a name="pgfId-910722"></a>Return continents type from VCS. Remember the value can only be between 0 and 11.</p>
</td>
<td><pre style="word-break:normal">import vcs
x=vcs.init()
cont_type = x.getcontinentstype()</pre></td></tr>
<tr>
<td rowspan="1" colspan="1">
<code class="Normal">
<a name="pgfId-910709"></a>isgraphicsmethod()</code>
</td>
<td rowspan="1" colspan="1">
<p class="Normal">
<a name="pgfId-910711"></a>Indicates if the entered argument is one of the following graphics methods: boxfill, isofill, isoline, outfill, outline, continents, scatter, vector, xvsy, xyvsy, yxvsx.</p>
</td>
<td><pre style="word-break:normal">import vcs
x=vcs.init()
box=x.getboxfill('quick')
x.isgraphicsmethod(box)</pre></td></tr>
<tr>
<td rowspan="1" colspan="1">
<code class="Normal">
<a name="pgfId-910698"></a>isboxfill()</code>
</td>
<td rowspan="1" colspan="1">
<p class="Normal">
<a name="pgfId-910700"></a>Check to see if an object is a VCS primary boxfill graphics method object.</p>
</td>
<td><pre style="word-break:normal">import vcs
x=vcs.init()
box=x.getboxfill("quick")
x.isboxfill(box)</pre></td></tr>
<tr>
<td rowspan="1" colspan="1">
<code class="Normal">
<a name="pgfId-910687"></a>iscontinents()</code>
</td>
<td rowspan="1" colspan="1">
<p class="Normal">
<a name="pgfId-910689"></a>Check to see if an object is a VCS primary continents graphics method.</p>
</td>
<td><pre style="word-break:normal">import vcs
x=vcs.init()
con=x.getcontinents("quick")
x.iscontinents(con)
</pre></td></tr>
<tr>
<td rowspan="1" colspan="1">
<code class="Normal">
<a name="pgfId-910676"></a>isisofill()</code>
</td>
<td rowspan="1" colspan="1">
<p class="Normal">
<a name="pgfId-910678"></a>Check to see if an object is a VCS primary isofill graphics method.</p>
</td>
<td><pre style="word-break:normal">import vcs
x=vcs.init()
iso=x.getisofill("quick")
x.isisofill(iso)
</pre></td></tr>
<tr>
<td rowspan="1" colspan="1">
<code class="Normal">
<a name="pgfId-910665"></a>isisoline()</code>
</td>
<td rowspan="1" colspan="1">
<p class="Normal">
<a name="pgfId-910667"></a>Check to see if an object is a VCS primary isoline graphics method.</p>
</td>
<td><pre style="word-break:normal">import vcs
x=vcs.init()
iso=x.getisoline("quick"
x.isisoline(iso)</pre></td></tr>
<tr>
<td rowspan="1" colspan="1">
<code class="Normal">
<a name="pgfId-910654"></a>isoutfill()</code>
</td>
<td rowspan="1" colspan="1">
<p class="Normal">
<a name="pgfId-910656"></a>Check to see if this object is a VCS primary outfill graphics method.</p>
</td>
<td><pre style="word-break:normal">import vcs
x=vcs.init()
out=x.getoutfill("quick")
x.isoutfill(out)</pre></td></tr>
<tr>
<td rowspan="1" colspan="1">
<code class="Normal">
<a name="pgfId-910643"></a>isoutline()</code>
</td>
<td rowspan="1" colspan="1">
<p class="Normal">
<a name="pgfId-910645"></a>Check to see if an object is a VCS primary outline graphics method.</p>
</td>
<td><pre style="word-break:normal">import vcs
x=vcs.init()
out=x.getoutline("quick")
x.isoutline(out)</pre></td></tr>
<tr>
<td rowspan="1" colspan="1">
<code class="Normal">
<a name="pgfId-910632"></a>isvector()</code>
</td>
<td rowspan="1" colspan="1">
<p class="Normal">
<a name="pgfId-910634"></a>Check to see if an object is a VCS primary vector graphics method.</p>
</td>
<td><pre style="word-break:normal">import vcs
x=vcs.init()
vec=x.getvector("quick")
x.isvector(vec)</pre></td></tr>
<tr>
<td rowspan="1" colspan="1">
<code class="Normal">
<a name="pgfId-910621"></a>isxvsy()</code>
</td>
<td rowspan="1" colspan="1">
<p class="Normal">
<a name="pgfId-910623"></a>Check to see if an object is a VCS primary xvsy graphics method.</p>
</td>
<td><pre style="word-break:normal">import vcs
x=vcs.init()
xy=x.getxvsy("quick")
x.isxvsy(xy)</pre></td></tr>
<tr>
<td rowspan="1" colspan="1">
<code class="Normal">
<a name="pgfId-910365"></a>isxyvsy()</code>
</td>
<td rowspan="1" colspan="1">
<p class="Normal">
<a name="pgfId-910367"></a>Check to see if an object is a VCS primary Xyvsy graphics method.</p>
</td>
<td><pre style="word-break:normal">import vcs
x=vcs.init()
xyy=x.getxyvsy("quick")
x.isxyvsy(xyy)</pre></td></tr>
<tr>
<td rowspan="1" colspan="1">
<code class="Normal">
<a name="pgfId-910354"></a>isyxvsx()</code>
</td>
<td rowspan="1" colspan="1">
<p class="Normal">
<a name="pgfId-910356"></a>Check to see if an object is a VCS primary yxvsx graphics method.</p>
</td>
<td><pre style="word-break:normal">import vcs
x=vcs.init()
yxx=x.getyxvsx("quick")
x.isyxvsx(yxx)</pre></td></tr>
<tr>
<td rowspan="1" colspan="1">
<code class="Normal">
<a name="pgfId-910935"></a>istemplate()</code>
</td>
<td rowspan="1" colspan="1">
<p class="Normal">
<a name="pgfId-910937"></a>Indicates if the entered argument a template.</p>
</td>
<td><pre style="word-break:normal">import vcs
x=vcs.init()
templt=x.gettemplate('quick')
x.istemplate(templt)</pre></td></tr>
<tr>
<td rowspan="1" colspan="1">
<code class="Normal">
<a name="pgfId-910927"></a>issecondaryobject()</code>
</td>
<td rowspan="1" colspan="1">
<p class="Normal">
<a name="pgfId-910929"></a>Query to see if an object is a secondary object.</p>
</td>
<td><pre style="word-break:normal">import vcs
x=vcs.init()
line=x.getline()
x.issecondaryobject(line)</pre></td></tr>
<tr>
<td rowspan="1" colspan="1">
<code class="Normal">
<a name="pgfId-910343"></a>isfillarea()</code>
</td>
<td rowspan="1" colspan="1">
<p class="Normal">
<a name="pgfId-910345"></a>Check to see if an object is a VCS secondary fillarea.</p>
</td>
<td><pre style="word-break:normal">import vcs
x=vcs.init()
fa=x.getfillarea("def37")
x.isfillarea(fa)</pre></td></tr>
<tr>
<td rowspan="1" colspan="1">
<code class="Normal">
<a name="pgfId-911021"></a>isline()</code>
</td>
<td rowspan="1" colspan="1">
<p class="Normal">
<a name="pgfId-911023"></a>Check to see if this object is a VCS secondary line.</p>
</td>
<td><pre style="word-break:normal">import vcs
x=vcs.init()
ln=x.getline()
x.isline(ln)</pre></td></tr>
<tr>
<td rowspan="1" colspan="1">
<code class="Normal">
<a name="pgfId-911013"></a>ismarker()</code>
</td>
<td rowspan="1" colspan="1">
<p class="Normal">
<a name="pgfId-911015"></a>Check to see if this object is a VCS secondary marker.</p>
</td>
<td><pre style="word-break:normal">import vcs
x=vcs.init()
ln=x.getmarker()
x.ismarker(ln)</pre></td></tr>
<tr>
<td rowspan="1" colspan="1">
<code class="Normal">
<a name="pgfId-911005"></a>istextcombined()</code>
</td>
<td rowspan="1" colspan="1">
<p class="Normal">
<a name="pgfId-911007"></a>Check to see if an object is a VCS secondary text combined.</p>
</td>
<td><pre style="word-break:normal">import vcs
x=vcs.init()
tc=x.gettextcombined("std", "7left")
x.istextcombined(tc)</pre></td></tr>
<tr>
<td rowspan="1" colspan="1">
<code class="Normal">
<a name="pgfId-910997"></a>istextorientation()</code>
</td>
<td rowspan="1" colspan="1">
<p class="Normal">
<a name="pgfId-910999"></a>Check to see if an object is a VCS secondary text orientation.</p>
</td>
<td><pre style="word-break:normal">import vcs
x=vcs.init()
to=x.gettextorientation("7left")
x.istextorientation(to)</pre></td></tr>
<tr>
<td rowspan="1" colspan="1">
<code class="Normal">
<a name="pgfId-910989"></a>istexttable()</code>
</td>
<td rowspan="1" colspan="1">
<p class="Normal">
<a name="pgfId-910991"></a>Check to see if an object is a VCS secondary text table.</p>
</td>
<td><pre style="word-break:normal">import vcs
x=vcs.init()
tt=x.gettexttable("std")
x.istexttable(tt)</pre></td></tr>
<tr>
<td rowspan="1" colspan="1">
<code class="Normal">
<a name="pgfId-910981"></a>listelements()</code>
</td>
<td rowspan="1" colspan="1">
<p class="Normal">
<a name="pgfId-910983"></a>Returns a Python list of all the VCS class objects.</p>
</td>
<td><pre style="word-break:normal">import vcs
x=vcs.init()
x.listelements()</pre></td></tr>
<tr>
<td rowspan="1" colspan="1">
<code class="Normal">
<a name="pgfId-910332"></a>show()</code>
</td>
<td rowspan="1" colspan="1">
<p class="Normal">
<a name="pgfId-910334"></a>Show the list of VCS primary and secondary class objects.</p>
</td>
<td><pre style="word-break:normal">import vcs
x=vcs.init()
x.show('boxfill')
x.show('isofill')
x.show(`template')
x.show(`line')</pre></td></tr>
<tr>
<td rowspan="1" colspan="1">
<code class="Normal">
<a name="pgfId-910321"></a>createboxfill()</code>
</td>
<td rowspan="1" colspan="1">
<p class="Normal">
<a name="pgfId-910323"></a>Create a new boxfill graphics method given the  name and the existingboxfill graphics method to copy the attributes from. </p>
</td>
<td><pre style="word-break:normal">import vcs
x=vcs.init()
box=x.createboxfill('example','quick')</pre></td></tr>
<tr>
<td rowspan="1" colspan="1">
<code class="Normal">
<a name="pgfId-910310"></a>getboxfill()</code>
</td>
<td rowspan="1" colspan="1">
<p class="Normal">
<a name="pgfId-910312"></a>his function will create a boxfill class object from an existing VCS boxfill graphics method.</p>
</td>
<td><pre style="word-break:normal">import vcs
x=vcs.init()
box2=x.getboxfill('quick')</pre></td></tr>
<tr>
<td rowspan="1" colspan="1">
<code class="Normal">
<a name="pgfId-911193"></a>createcontinents()</code>
</td>
<td rowspan="1" colspan="1">
<p class="Normal">
<a name="pgfId-911195"></a>Create a new continents graphics method given the the name and the existing continents graphics method to copy the attributes from. </p>
</td>
<td><pre style="word-break:normal">import vcs
x=vcs.init()
con=x.createcontinents('example','quick')</pre></td></tr>
<tr>
<td rowspan="1" colspan="1">
<code class="Normal">
<a name="pgfId-911185"></a>getcontinents()</code>
</td>
<td rowspan="1" colspan="1">
<p class="Normal">
<a name="pgfId-911187"></a>This function will create a continents class object from an existing VCS continents graphics method. </p>
</td>
<td><pre style="word-break:normal">import vcs
x=vcs.init()
con2=x.getcontinents('quick')</pre></td></tr>
<tr>
<td rowspan="1" colspan="1">
<code class="Normal">
<a name="pgfId-911177"></a>createisofill()</code>
</td>
<td rowspan="1" colspan="1">
<p class="Normal">
<a name="pgfId-911179"></a>Create a new isofill graphics method given the the name and the existing isofill graphics method to copy the attributes from. </p>
</td>
<td><pre style="word-break:normal">import vcs
x=vcs.init()
iso=x.createisofill('example','quick')</pre></td></tr>
<tr>
<td rowspan="1" colspan="1">
<code class="Normal">
<a name="pgfId-911169"></a>getisofill()</code>
</td>
<td rowspan="1" colspan="1">
<p class="Normal">
<a name="pgfId-911171"></a>This function will create a isofill class object from an existing VCS isofill graphics method. </p>
</td>
<td><pre style="word-break:normal">import vcs
x=vcs.init()
iso2=x.getisofill('quick')</pre></td></tr>
<tr>
<td rowspan="1" colspan="1">
<code class="Normal">
<a name="pgfId-911161"></a>createisoline()</code>
</td>
<td rowspan="1" colspan="1">
<p class="Normal">
<a name="pgfId-911163"></a>Create a new isoline graphics method given the the name and the existing isoline graphics method to copy the attributes from. </p>
</td>
<td><pre style="word-break:normal">import vcs
x=vcs.init()
iso=x.createisoline('example','quick')</pre></td></tr>
<tr>
<td rowspan="1" colspan="1">
<code class="Normal">
<a name="pgfId-911153"></a>getisoline()</code>
</td>
<td rowspan="1" colspan="1">
<p class="Normal">
<a name="pgfId-911155"></a>This function will create a isoline class object from an existing VCS isoline graphics method. </p>
</td>
<td><pre style="word-break:normal">import vcs
x=vcs.init()
iso2=x.getisoline('quick')</pre></td></tr>
<tr>
<td rowspan="1" colspan="1">
<code class="Normal">
<a name="pgfId-911289"></a>createoutfill()</code>
</td>
<td rowspan="1" colspan="1">
<p class="Normal">
<a name="pgfId-911291"></a>Create a new outfill graphics method given the the name and the existing outfill graphics method to copy the attributes from. </p>
</td>
<td><pre style="word-break:normal">import vcs
x=vcs.init()
out=x.createoutfill('example','quick')</pre></td></tr>
<tr>
<td rowspan="1" colspan="1">
<code class="Normal">
<a name="pgfId-911281"></a>getoutfill()</code>
</td>
<td rowspan="1" colspan="1">
<p class="Normal">
<a name="pgfId-911283"></a>This function will create a outfill class object from an existing VCS outfill graphics method. </p>
</td>
<td><pre style="word-break:normal">import vcs
x=vcs.init()
out2=x.getoutfill('quick')</pre></td></tr>
<tr>
<td rowspan="1" colspan="1">
<code class="Normal">
<a name="pgfId-911273"></a>createoutline()</code>
</td>
<td rowspan="1" colspan="1">
<p class="Normal">
<a name="pgfId-911275"></a>Create a new outline graphics method given the the name and the existing outline graphics method to copy the attributes from.</p>
</td>
<td><pre style="word-break:normal">import vcs
x=vcs.init()
out=x.createoutline('example','quick')</pre></td></tr>
<tr>
<td rowspan="1" colspan="1">
<code class="Normal">
<a name="pgfId-911265"></a>getoutline()</code>
</td>
<td rowspan="1" colspan="1">
<p class="Normal">
<a name="pgfId-911267"></a>This function will create a outline class object from an existing VCS outline graphics method. </p>
</td>
<td><pre style="word-break:normal">import vcs
x=vcs.init()
out2=x.getoutline('quick')</pre></td></tr>
<tr>
<td rowspan="1" colspan="1">
<code class="Normal">
<a name="pgfId-911257"></a>createscatter()</code>
</td>
<td rowspan="1" colspan="1">
<p class="Normal">
<a name="pgfId-911259"></a>Create a new scatter graphics method given the the name and the existing mscatter graphics method to copy the attributes from.</p>
</td>
<td><pre style="word-break:normal">import vcs
x=vcs.init()
sct=x.createscatter('example','quick')</pre></td></tr>
<tr>
<td rowspan="1" colspan="1">
<code class="Normal">
<a name="pgfId-911249"></a>getscatter()</code>
</td>
<td rowspan="1" colspan="1">
<p class="Normal">
<a name="pgfId-911251"></a>This function will create a scatter class object from an existing VCS scatter graphics method.</p>
</td>
<td><pre style="word-break:normal">import vcs
x=vcs.init()
sct2=x.getscatter('quick')</pre></td></tr>
<tr>
<td rowspan="1" colspan="1">
<code class="Normal">
<a name="pgfId-911241"></a>createvector()</code>
</td>
<td rowspan="1" colspan="1">
<p class="Normal">
<a name="pgfId-911243"></a>Create a new vector graphics method given the the name and the existing vector graphics method to copy the attributes from. </p>
</td>
<td><pre style="word-break:normal">import vcs
x=vcs.init()
vec=x.createvector('example','quick')</pre></td></tr>
<tr>
<td rowspan="1" colspan="1">
<code class="Normal">
<a name="pgfId-911233"></a>getvector()</code>
</td>
<td rowspan="1" colspan="1">
<p class="Normal">
<a name="pgfId-911235"></a>This function will create a vector class object from an existing VCS vector graphics method.</p>
</td>
<td><pre style="word-break:normal">import vcs
x=vcs.init()
vec2=x.getvector('quick')</pre></td></tr>
<tr>
<td rowspan="1" colspan="1">
<code class="Normal">
<a name="pgfId-911225"></a>createxvsy()</code>
</td>
<td rowspan="1" colspan="1">
<p class="Normal">
<a name="pgfId-911227"></a>Create a new XvsY graphics method given the the name and the existing XvsY graphics method to copy the attributes from.</p>
</td>
<td><pre style="word-break:normal">import vcs
x=vcs.init()
xy=x.createxvsy('example','quick')</pre></td></tr>
<tr>
<td rowspan="1" colspan="1">
<code class="Normal">
<a name="pgfId-911217"></a>getxvsy()</code>
</td>
<td rowspan="1" colspan="1">
<p class="Normal">
<a name="pgfId-911219"></a>This function will create a XvsY class object from an existing VCS XvsY graphics method. </p>
</td>
<td><pre style="word-break:normal">import vcs
x=vcs.init()
xy2=x.getxvsy('quick')</pre></td></tr>
<tr>
<td rowspan="1" colspan="1">
<code class="Normal">
<a name="pgfId-911209"></a>createxyvsy()</code>
</td>
<td rowspan="1" colspan="1">
<p class="Normal">
<a name="pgfId-911211"></a>Create a new Xyvsy graphics method given the the name and the existing Xyvsy graphics method to copy the attributes from. </p>
</td>
<td><pre style="word-break:normal">import vcs
x=vcs.init()
xyy=x.createxyvsy('example','quick')</pre></td></tr>
<tr>
<td rowspan="1" colspan="1">
<code class="Normal">
<a name="pgfId-911201"></a>getxyvsy()</code>
</td>
<td rowspan="1" colspan="1">
<p class="Normal">
<a name="pgfId-911203"></a>This function will create a Xyvsy class object from an existing VCS Xyvsy graphics method.</p>
</td>
<td><pre style="word-break:normal">import vcs
x=vcs.init()
xyy2=x.getxyvsy('quick')</pre></td></tr>
<tr>
<td rowspan="1" colspan="1">
<code class="Normal">
<a name="pgfId-910299"></a>createyxvsx()</code>
</td>
<td rowspan="1" colspan="1">
<p class="Normal">
<a name="pgfId-910301"></a>Create a new Yxvsx graphics method given the the name and the existing Yxvsx graphics method to copy the attributes from. </p>
</td>
<td><pre style="word-break:normal">import vcs
x=vcs.init()
yxx=x.createyxvsx('example','quick')</pre></td></tr>
<tr>
<td rowspan="1" colspan="1">
<code class="Normal">
<a name="pgfId-910288"></a>getyxvsx()</code>
</td>
<td rowspan="1" colspan="1">
<p class="Normal">
<a name="pgfId-910290"></a>This function will create a Yxvsx class object from an existing VCS Yxvsx graphics method. </p>
</td>
<td><pre style="word-break:normal">import vcs
x=vcs.init()
yxx2=x.getyxvsx('quick')</pre></td></tr>
<tr>
<td rowspan="1" colspan="1">
<code class="Normal">
<a name="pgfId-910277"></a>createtemplate()</code>
</td>
<td rowspan="1" colspan="1">
<p class="Normal">
<a name="pgfId-910279"></a>Create a new template given the the name and the existing template to copy the attributes from. </p>
</td>
<td><pre style="word-break:normal">import vcs
x=vcs.init()
con=x.createtemplate('example','quick')</pre></td></tr>
<tr>
<td rowspan="1" colspan="1">
<code class="Normal">
<a name="pgfId-910266"></a>gettemplate()</code>
</td>
<td rowspan="1" colspan="1">
<p class="Normal">
<a name="pgfId-910268"></a>his function will create a  template class object from an existing VCS template. </p>
</td>
<td><pre style="word-break:normal">import vcs
x=vcs.init()
templt2=x.gettemplate('quick')</pre></td></tr>
<tr>
<td rowspan="1" colspan="1">
<code class="Normal">
<a name="pgfId-910211"></a>setcolormap()</code>
</td>
<td rowspan="1" colspan="1">
<p class="Normal">
<a name="pgfId-910213"></a>This routine will change the VCS color map.</p>
</td>
<td><pre style="word-break:normal">import vcs
x=vcs.init()
x.setcolormap("AMIP")</pre></td></tr>
<tr>
<td rowspan="1" colspan="1">
<code class="Normal">
<a name="pgfId-911614"></a>setcolorcell()</code>
</td>
<td rowspan="1" colspan="1">
<p class="Normal">
<a name="pgfId-911616"></a>Set a individual color cell in the active colormap. If default is the active colormap, then return an error string.</p>
</td>
<td><pre style="word-break:normal">import vcs
x=vcs.init()
x.setcolormap("AMIP")
a.setcolorcell(11,0,0,0)
x.setcolorcell(21,100,0,0)</pre></td></tr>
<tr>
<td rowspan="1" colspan="1">
<code class="Normal">
<a name="pgfId-911678"></a>colormapgui()</code>
</td>
<td rowspan="1" colspan="1">
<p class="Normal">
<a name="pgfId-911680"></a>Run the VCS colormap interface.</p>
<p class="Normal">
<a name="pgfId-911695"></a>    The colormapgui command is used to bring up the VCS colormap interface. The interface is used to select, create, change, or remove colormaps.</p>
<p class="Normal">
<a name="pgfId-911696"></a>    Note: </p>
<p class="Normal">
<a name="pgfId-911697"></a>        The colormapgui GUI will only work for 8-bit 'Pseudo Color'.</p>
</td>
<td><pre style="word-break:normal">import vcs
x=vcs.init()
x.colormapgui()</pre></td></tr>
<tr>
<td rowspan="1" colspan="1">
<code class="Normal">
<a name="pgfId-911670"></a>createfillarea()</code>
</td>
<td rowspan="1" colspan="1">
<p class="Normal">
<a name="pgfId-911672"></a>Create a new fillarea secondary method given the the name and the existing fillarea secondary method to copy the attributes from. </p>
</td>
<td><pre style="word-break:normal">import vcs
x=vcs.init()
fa=x.createfillarea('example','black')</pre></td></tr>
<tr>
<td rowspan="1" colspan="1">
<code class="Normal">
<a name="pgfId-911662"></a>getfillarea()</code>
</td>
<td rowspan="1" colspan="1">
<p class="Normal">
<a name="pgfId-911664"></a>This function will create a fillarea class object from an existing VCS fillarea secondary method.</p>
</td>
<td><pre style="word-break:normal">import vcs
x=vcs.init()
fa2=x.getfillarea('quick')</pre></td></tr>
<tr>
<td rowspan="1" colspan="1">
<code class="Normal">
<a name="pgfId-911654"></a>createline()</code>
</td>
<td rowspan="1" colspan="1">
<p class="Normal">
<a name="pgfId-911656"></a>Create a new line secondary method given the the name and the existing line secondary method to copy the attributes from. </p>
</td>
<td><pre style="word-break:normal">import vcs
x=vcs.init()
ln=x.createline('example','black')</pre></td></tr>
<tr>
<td rowspan="1" colspan="1">
<code class="Normal">
<a name="pgfId-911646"></a>getline()</code>
</td>
<td rowspan="1" colspan="1">
<p class="Normal">
<a name="pgfId-911648"></a>This function will create a line class object from an existing VCS line secondary method. </p>
</td>
<td><pre style="word-break:normal">import vcs
x=vcs.init()
ln2=x.getline('quick')</pre></td></tr>
<tr>
<td rowspan="1" colspan="1">
<code class="Normal">
<a name="pgfId-911638"></a>createmarker()</code>
</td>
<td rowspan="1" colspan="1">
<p class="Normal">
<a name="pgfId-911640"></a>Create a new marker secondary method given the the name and the existing marker secondary method to copy the attributes from. </p>
</td>
<td><pre style="word-break:normal">import vcs
x=vcs.init()
mrk=x.createmarker('example','black')</pre></td></tr>
<tr>
<td rowspan="1" colspan="1">
<code class="Normal">
<a name="pgfId-911630"></a>getmarker()</code>
</td>
<td rowspan="1" colspan="1">
<p class="Normal">
<a name="pgfId-911632"></a>This function will create a marker class object from an existing VCS marker secondary method. </p>
</td>
<td><pre style="word-break:normal">import vcs
x=vcs.init()
mrk2=x.getmarker('quick')</pre></td></tr>
<tr>
<td rowspan="1" colspan="1">
<code class="Normal">
<a name="pgfId-911622"></a>createtextcombined()</code>
</td>
<td rowspan="1" colspan="1">
<p class="Normal">
<a name="pgfId-911624"></a>Create a new textcombined secondary method given the the names and the existing texttable and textorientation secondary methods to copy the attributes from. I</p>
</td>
<td><pre style="word-break:normal">import vcs
x=vcs.init()
tc=x.createtextcombined('example1','std','example1','7left')</pre></td></tr>
<tr>
<td rowspan="1" colspan="1">
<code class="Normal">
<a name="pgfId-911606"></a>gettextcombined()</code>
</td>
<td rowspan="1" colspan="1">
<p class="Normal">
<a name="pgfId-911608"></a>This function will create a textcombined class object from an existing VCS texttable secondary method and an existing VCS textorientation secondary method. </p>
</td>
<td><pre style="word-break:normal">import vcs
x=vcs.init()
tc2=x.gettextcombined('std','7left')</pre></td></tr>
<tr>
<td rowspan="1" colspan="1">
<code class="Normal">
<a name="pgfId-911598"></a>createtextorientation()</code>
</td>
<td rowspan="1" colspan="1">
<p class="Normal">
<a name="pgfId-911600"></a>Create a new textorientation secondary method given the the name and  he existing textorientation secondary method to copy the attributes from. </p>
</td>
<td><pre style="word-break:normal">import vcs
x=vcs.init()
to=x.createtextorientation('example1')</pre></td></tr>
<tr>
<td rowspan="1" colspan="1">
<code class="Normal">
<a name="pgfId-911590"></a>gettextorientation()</code>
</td>
<td rowspan="1" colspan="1">
<p class="Normal">
<a name="pgfId-911592"></a>This function will create a textorientation class object from an existing VCS textorientation secondary method. </p>
</td>
<td><pre style="word-break:normal">import vcs
x=vcs.init()
to2=x.gettextorientation('quick')</pre></td></tr>
<tr>
<td rowspan="1" colspan="1">
<code class="Normal">
<a name="pgfId-911768"></a>createtexttable()</code>
</td>
<td rowspan="1" colspan="1">
<p class="Normal">
<a name="pgfId-911770"></a>Create a new texttable secondary method given the the name and the existing texttable secondary method to copy the attributes from. </p>
</td>
<td><pre style="word-break:normal">import vcs
x=vcs.init()
tt=x.createtexttable('example','black')</pre></td></tr>
<tr>
<td rowspan="1" colspan="1">
<code class="Normal">
<a name="pgfId-911760"></a>gettexttable()</code>
</td>
<td rowspan="1" colspan="1">
<p class="Normal">
<a name="pgfId-911762"></a>This function will create a  texttable class object from an existing VCS texttable secondary method. </p>
</td>
<td><pre style="word-break:normal">import vcs
x=vcs.init()
tt2=x.gettexttable('quick')</pre></td></tr>
<tr>
<td rowspan="1" colspan="1">
<code class="Normal">
<a name="pgfId-911752"></a>removeobject()</code>
</td>
<td rowspan="1" colspan="1">
<p class="Normal">
<a name="pgfId-911754"></a>This function allows the user to remove these objects from the appropriate class list. </p>
<p class="Normal">
<a name="pgfId-911819"></a>    Note, To remove the object completely from Python, remember to use the "del" function.</p>
<p class="Normal">
<a name="pgfId-911820"></a>    Also note, The user is not allowed to remove a "default" class object.</p>
</td>
<td><pre style="word-break:normal">import vcs
x=vcs.init()
line=x.getline('red')
x.removeobject(line)
iso=x.createisoline('example')
x.removeobject(iso)</pre></td></tr>
<tr>
<td rowspan="1" colspan="1">
<code class="Normal">
<a name="pgfId-911744"></a>setcontinentstype()</code>
</td>
<td rowspan="1" colspan="1">
<p class="Normal">
<a name="pgfId-911746"></a>One has the option of using continental maps that are predefined or that are user-defined. Predefined continental maps are either internal to VCS or are specified by external files. (The continents type number ranges from 0 to 11.)</p>
</td>
<td><pre style="word-break:normal">import vcs
x=vcs.init()
f=cu.open('clt.nc')
s=f.getslab('clt')
x.setcontinentstype(3)
x.plot(array,'default','isofill','quick')</pre></td></tr>
<tr>
<td rowspan="1" colspan="1">
<code class="Normal">
<a name="pgfId-911736"></a>set()</code>
</td>
<td rowspan="1" colspan="1">
<p class="Normal">
<a name="pgfId-911738"></a>Set the default VCS primary class objects: template and graphics methods.</p>
</td>
<td><pre style="word-break:normal">import vcs
x=vcs.init()
f=cu.open('clt.nc')
s=f.getslab('clt')
x.set('isofill','quick')
x.plot(s)</pre></td></tr>
<tr>
<td rowspan="1" colspan="1">
<code class="Normal">
<a name="pgfId-911728"></a>animate()</code>
</td>
<td rowspan="1" colspan="1">
<p class="Normal">
<a name="pgfId-911730"></a>Animate the contents of the VCS Canvas. Currently, only one display can be shown in the VCS Canvas for the animation to work. This function pops up the animation GUI.</p>
<p class="Normal">
<a name="pgfId-911858"></a>    Note: </p>
<p class="Normal">
<a name="pgfId-911859"></a>        The animation GUI will only work for 8-bit 'Pseudo Color'.</p>
</td>
<td><pre style="word-break:normal">import vcs
x=vcs.init()
f=cu.open('clt.nc')
s=f.getslab('clt')
x.plot(s)
x.animate()</pre></td></tr>
<tr>
<td rowspan="1" colspan="1">
<code class="Normal">
<a name="pgfId-910200"></a>flush()</code>
</td>
<td rowspan="1" colspan="1">
<p class="Normal">
<a name="pgfId-910202"></a>The flush command executes all buffered X events in the que.</p>
</td>
<td><pre style="word-break:normal">import vcs
f=cu.open('clt.nc')
s=f.getslab('clt')
x=vcs.init()
x.plot(s)
x.flush()</pre></td></tr>
<tr>
<td rowspan="1" colspan="1">
<code class="Normal">
<a name="pgfId-911555"></a>grid()</code>
</td>
<td rowspan="1" colspan="1">
<p class="Normal">
<a name="pgfId-911557"></a>Set the default plotting region for variables that have more dimension values than the graphics method. This will also be used for animating plots over the third and fourth dimensions.</p>
</td>
<td><pre style="word-break:normal">import vcs
f=cu.open('clt.nc')
s=f.getslab('clt')
x=vcs.init()
x.grid(12,24, -70,70, -150,150)
x.plot(s)
</pre></td></tr>
<tr>
<td rowspan="1" colspan="1">
<code class="Normal">
<a name="pgfId-911544"></a>resetgrid()</code>
</td>
<td rowspan="1" colspan="1">
<p class="Normal">
<a name="pgfId-911546"></a>Set the plotting region to default values. That is, let the variable's dimension values determine the grid.</p>
</td>
<td><pre style="word-break:normal">import vcs
f=cu.open('clt.nc')
s=f.getslab('clt')
x=vcs.init()
x.resetgrid()
x.plot(s)
</pre></td></tr>
</tbody></table>



###  Index

#####  A

  * [animate](vcs-5.html#marker-910411)

#####  B

  * [boxfill](vcs-5.html#marker-910438)

#####  C

  * [cgm](vcs-5.html#marker-910426)
  * [clear](vcs-5.html#marker-910449)
  * [close](vcs-5.html#marker-910417)
  * [colormapgui](vcs-5.html#marker-910500)
  * [continents](vcs-5.html#marker-910439)
  * [createboxfill](vcs-5.html#marker-910473)
  * [createcontinents](vcs-5.html#marker-910475)
  * [createfillarea](vcs-5.html#marker-910499)
  * [createisofill](vcs-5.html#marker-910477)
  * [createisoline](vcs-5.html#marker-910479)
  * [createline](vcs-5.html#marker-910502)
  * [createmarker](vcs-5.html#marker-910504)
  * [createoutfill](vcs-5.html#marker-910481)
  * [createoutline](vcs-5.html#marker-910484)
  * [createscatter](vcs-5.html#marker-910486)
  * [createtemplate](vcs-5.html#marker-910495)
  * [createtextcombined](vcs-5.html#marker-910506)
  * [createtextorientation](vcs-5.html#marker-910508)
  * [createtexttable](vcs-5.html#marker-910510)
  * [createvector](vcs-5.html#marker-910488)
  * [createxvsy](vcs-5.html#marker-910489)
  * [createxyvsy](vcs-5.html#marker-910491)
  * [createyxvsx](vcs-5.html#marker-910493)

#####  F

  * [flush](vcs-5.html#marker-910513)
  * [fonts, table of](vcs-10.html#marker-911155)

#####  G

  * [geometry](vcs-5.html#marker-910421)
  * [getboxfill](vcs-5.html#marker-910474)
  * [getcontinents](vcs-5.html#marker-910476)
  * [getcontinentstype](vcs-5.html#marker-910451)
  * [getfillarea](vcs-5.html#marker-910501)
  * [getisofill](vcs-5.html#marker-910478)
  * [getisoline](vcs-5.html#marker-910480)
  * [getline](vcs-5.html#marker-910503)
  * [getmarker](vcs-5.html#marker-910505)
  * [getoutfill](vcs-5.html#marker-910482)
  * [getoutline](vcs-5.html#marker-910483)
  * [getscatter](vcs-5.html#marker-910485)
  * [gettemplate](vcs-5.html#marker-910496)
  * [gettextcombined](vcs-5.html#marker-910507)
  * [gettextorientation](vcs-5.html#marker-910509)
  * [gettexttable](vcs-5.html#marker-910511)
  * [getvector](vcs-5.html#marker-910487)
  * [getxvsy](vcs-5.html#marker-910490)
  * [getxyvsy](vcs-5.html#marker-910492)
  * [getyxvsx](vcs-5.html#marker-910494)
  * [gif](vcs-5.html#marker-910423)
  * [graphicsmethodtype](vcs-5.html#marker-910450)
  * [grid](vcs-5.html#marker-910514)

#####  H

  * [help](vcs-5.html#marker-892715)

#####  I

  * [init](vcs-5.html#marker-892680)
  * [isboxfill](vcs-5.html#marker-910453)
  * [iscontinents](vcs-5.html#marker-910454)
  * [isfillarea](vcs-5.html#marker-910465)
  * [isgraphicsmethod](vcs-5.html#marker-910452)
  * [isisofill](vcs-5.html#marker-910455)
  * [isisoline](vcs-5.html#marker-910456)
  * [isline](vcs-5.html#marker-910466)
  * [ismarker](vcs-5.html#marker-910467)
  * [isofill](vcs-5.html#marker-910440)
  * [isoline](vcs-5.html#marker-910441)
  * [isoutfill](vcs-5.html#marker-910457)
  * [isoutline](vcs-5.html#marker-910458)
  * [issecondaryobject](vcs-5.html#marker-910464)
  * [istemplate](vcs-5.html#marker-910463)
  * [istextcombined](vcs-5.html#marker-910468)
  * [istextorientation](vcs-5.html#marker-910469)
  * [istexttable](vcs-5.html#marker-910470)
  * [isvector](vcs-5.html#marker-910459)
  * [isxvsy](vcs-5.html#marker-910460)
  * [isxyvsy](vcs-5.html#marker-910461)
  * [isyxvsx](vcs-5.html#marker-910462)

#####  L

  * [landscape](vcs-5.html#marker-910419)
  * [line styles](vcs-10.html#marker-911154)
  * [listelements](vcs-5.html#marker-910471)

#####  M

  * [mode](vcs-5.html#marker-910414)

#####  O

  * [objecthelp](vcs-5.html#marker-892732)
  * [open](vcs-5.html#marker-910416)
  * [outfill](vcs-5.html#marker-910442)
  * [outline](vcs-5.html#marker-910443)

#####  P

  * [page](vcs-5.html#marker-910420)
  * [plot](vcs-5.html#marker-910437)
  * [portrait](vcs-5.html#marker-910418)
  * [postscript](vcs-5.html#marker-910425)
  * [printer](vcs-5.html#marker-910422)
  * [pstogif](vcs-5.html#marker-910436)

#####  R

  * [raster](vcs-5.html#marker-910427)
  * [removeobject](vcs-5.html#marker-910512)
  * [resetgrid](vcs-5.html#marker-910515)

#####  S

  * [scatter](vcs-5.html#marker-910444)
  * [scripts](vcs-4.html#marker-885201)
  * [saving](vcs-4.html#marker-885201)
  * [Set](vcs-5.html#marker-910412)
  * [setcolorcell](vcs-5.html#marker-910498)
  * [setcolormap](vcs-5.html#marker-910497)
  * [setcontinentstype](vcs-5.html#marker-910413)
  * [show](vcs-5.html#marker-910472)
  * [styles, line](vcs-10.html#marker-911154)

#####  U

  * [update](vcs-5.html#marker-910415)

#####  V

  * [vector](vcs-5.html#marker-910446)

#####  X

  * [xvsy](vcs-5.html#marker-910445)
  * [xyvsy](vcs-5.html#marker-910448)

#####  Y

  * [yxvsx](vcs-5.html#marker-910447)

[Previous](vcs-10.html) \| [Main](vcs.html)


