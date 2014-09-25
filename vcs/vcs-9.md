---
layout: default
title: VCS Chapter 9
---
##  CHAPTER 9 Quick Reference Guides


###Commands and Their Usage

<table class="table">
<tr>
<th rowspan="1" colspan="1">
<p class="CellHeading">
<a name="pgfId-901807"></a>Command</p>
</th>
<th rowspan="1" colspan="1">
<p class="CellHeading">
<a name="pgfId-901809"></a>Usage</p>
</th>
</tr>
<tr>
<td rowspan="1" colspan="2">
	<strong>
<a name="pgfId-901811"></a>Initialization</strong>
</td>
</tr>
<tr>
<td rowspan="1" colspan="1">
<p class="CellBody">
<a name="pgfId-901815"></a>init</p>
</td>
<td rowspan="1" colspan="1">
<code>
<a name="pgfId-901817"></a>a = vcs.init()</code>
</td>
</tr>
<tr>
<td rowspan="1" colspan="2">
	<strong>
<a name="pgfId-901819"></a>Help</strong>
</td>
</tr>
<tr>
<td rowspan="1" colspan="1">
<p class="CellBody">
<a name="pgfId-901823"></a>help</p>
</td>
<td rowspan="1" colspan="1">
<code>
<a name="pgfId-901825"></a>vcs.help()</code>
</td>
</tr>
<tr>
<td rowspan="1" colspan="1">
<p class="CellBody">
<a name="pgfId-901827"></a>objecthelp</p>
</td>
<td rowspan="1" colspan="1">
<code>
<a name="pgfId-901829"></a>a.objecthelp(b)</code>
</td>
</tr>
<tr>
<td rowspan="1" colspan="2">
	<strong>
<a name="pgfId-901831"></a>Canvas</strong>
</td>
</tr>
<tr>
<td rowspan="1" colspan="1">
<p class="CellBody">
<a name="pgfId-901835"></a>mode</p>
</td>
<td rowspan="1" colspan="1">
<code>
<a name="pgfId-901837"></a>a.mode = 1</code>
</td>
</tr>
<tr>
<td rowspan="1" colspan="1">
<p class="CellBody">
<a name="pgfId-901839"></a>update</p>
</td>
<td rowspan="1" colspan="1">
<code>
<a name="pgfId-901841"></a>a.update()</code>
</td>
</tr>
<tr>
<td rowspan="1" colspan="1">
<p class="CellBody">
<a name="pgfId-901843"></a>open</p>
</td>
<td rowspan="1" colspan="1">
<code>
<a name="pgfId-901845"></a>a.open()</code>
</td>
</tr>
<tr>
<td rowspan="1" colspan="1">
<p class="CellBody">
<a name="pgfId-901847"></a>close</p>
</td>
<td rowspan="1" colspan="1">
<code>
<a name="pgfId-901849"></a>a.close()</code>
</td>
</tr>
<tr>
<td rowspan="1" colspan="1">
<p class="CellBody">
<a name="pgfId-901851"></a>flushcanvas</p>
</td>
<td rowspan="1" colspan="1">
<code>
<a name="pgfId-901853"></a>a.flushcanvas()</code>
</td>
</tr>
<tr>
<td rowspan="1" colspan="1">
<p class="CellBody">
<a name="pgfId-901855"></a>refreshcanvas</p>
</td>
<td rowspan="1" colspan="1">
<code>
<a name="pgfId-901857"></a>a.refreshcanvas()</code>
</td>
</tr>
<tr>
<td rowspan="1" colspan="1">
<p class="CellBody">
<a name="pgfId-901859"></a>portrait</p>
</td>
<td rowspan="1" colspan="1">
<code>
<a name="pgfId-901861"></a>a.portrait()</code>
</td>
</tr>
<tr>
<td rowspan="1" colspan="1">
<p class="CellBody">
<a name="pgfId-901863"></a>landscape</p>
</td>
<td rowspan="1" colspan="1">
<code>
<a name="pgfId-901865"></a>a.landscape()</code>
</td>
</tr>
<tr>
<td rowspan="1" colspan="1">
<p class="CellBody">
<a name="pgfId-901867"></a>page</p>
</td>
<td rowspan="1" colspan="1">
<code>
<a name="pgfId-901869"></a>a.page()</code>
</td>
</tr>
<tr>
<td rowspan="1" colspan="1">
<p class="CellBody">
<a name="pgfId-901871"></a>geometry</p>
</td>
<td rowspan="1" colspan="1">
<code>
<a name="pgfId-901873"></a>a.geometry(450, 337,100, 100)</code>
</td>
</tr>
<tr>
<td rowspan="1" colspan="2">
	<strong>
<a name="pgfId-901875"></a>Printing and Saving Graphics</strong>
</td>
</tr>
<tr>
<td rowspan="1" colspan="1">
<p class="CellBody">
<a name="pgfId-901879"></a>printer</p>
</td>
<td rowspan="1" colspan="1">
<code>
<a name="pgfId-901881"></a>a.printer('printer_name') </code>
</td>
</tr>
<tr>
<td rowspan="1" colspan="1">
<p class="CellBody">
<a name="pgfId-901883"></a>gif</p>
</td>
<td rowspan="1" colspan="1">
<code>
<a name="pgfId-901885"></a>a.gif('gif_file_name')</code>
</td>
</tr>
<tr>
<td rowspan="1" colspan="1">
<p class="CellBody">
<a name="pgfId-901887"></a>postscript</p>
</td>
<td rowspan="1" colspan="1">
<code>
<a name="pgfId-901889"></a>a.postscript('postscript_file_name')</code>
</td>
</tr>
<tr>
<td rowspan="1" colspan="1">
<p class="CellBody">
<a name="pgfId-901891"></a>cgm</p>
</td>
<td rowspan="1" colspan="1">
<code>
<a name="pgfId-901893"></a>a.cgm('cgm_file_name')</code>
</td>
</tr>
<tr>
<td rowspan="1" colspan="1">
<p class="CellBody">
<a name="pgfId-901895"></a>raster</p>
</td>
<td rowspan="1" colspan="1">
<code>
<a name="pgfId-901897"></a>a.raster('raster_file_name')</code>
</td>
</tr>
<tr>
<td rowspan="1" colspan="1">
<p class="CellBody">
<a name="pgfId-901899"></a>pstogif</p>
</td>
<td rowspan="1" colspan="1">
<code>
<a name="pgfId-901901"></a>a.pstogif('postscript_file_name')</code>
</td>
</tr>
<tr>
<td rowspan="1" colspan="2">
	<strong>
<a name="pgfId-901903"></a>Plot and Clear Commands</strong>
</td>
</tr>
<tr>
<td rowspan="1" colspan="1">
<p class="CellBody">
<a name="pgfId-901907"></a>plot</p>
</td>
<td rowspan="1" colspan="1">
<code>
<a name="pgfId-901909"></a>a.plot(array)  </code>
</td>
</tr>
<tr>
<td rowspan="1" colspan="1">
<p class="CellBody">
<a name="pgfId-901911"></a>boxfill</p>
</td>
<td rowspan="1" colspan="1">
<code>
<a name="pgfId-901913"></a>a.boxfill(array)</code>
</td>
</tr>
<tr>
<td rowspan="1" colspan="1">
<p class="CellBody">
<a name="pgfId-901915"></a>continents</p>
</td>
<td rowspan="1" colspan="1">
<code>
<a name="pgfId-901917"></a>a.continents(array)</code>
</td>
</tr>
<tr>
<td rowspan="1" colspan="1">
<p class="CellBody">
<a name="pgfId-901919"></a>isofill</p>
</td>
<td rowspan="1" colspan="1">
<code>
<a name="pgfId-901921"></a>a.isofill(array)</code>
</td>
</tr>
<tr>
<td rowspan="1" colspan="1">
<p class="CellBody">
<a name="pgfId-901923"></a>isoline</p>
</td>
<td rowspan="1" colspan="1">
<code>
<a name="pgfId-901925"></a>a.isoline(array)</code>
</td>
</tr>
<tr>
<td rowspan="1" colspan="1">
<p class="CellBody">
<a name="pgfId-901927"></a>outfill</p>
</td>
<td rowspan="1" colspan="1">
<code>
<a name="pgfId-901929"></a>a.outfill(array)</code>
</td>
</tr>
<tr>
<td rowspan="1" colspan="1">
<p class="CellBody">
<a name="pgfId-901931"></a>outline</p>
</td>
<td rowspan="1" colspan="1">
<code>
<a name="pgfId-901933"></a>a.outline(array)</code>
</td>
</tr>
<tr>
<td rowspan="1" colspan="1">
<p class="CellBody">
<a name="pgfId-901935"></a>scatter</p>
</td>
<td rowspan="1" colspan="1">
<code>
<a name="pgfId-901937"></a>a.scatter(array)</code>
</td>
</tr>
<tr>
<td rowspan="1" colspan="1">
<p class="CellBody">
<a name="pgfId-901939"></a>vector</p>
</td>
<td rowspan="1" colspan="1">
<code>
<a name="pgfId-901941"></a>a.vector(array)</code>
</td>
</tr>
<tr>
<td rowspan="1" colspan="1">
<p class="CellBody">
<a name="pgfId-901943"></a>xvsy</p>
</td>
<td rowspan="1" colspan="1">
<code>
<a name="pgfId-901945"></a>a.xvsy(array)</code>
</td>
</tr>
<tr>
<td rowspan="1" colspan="1">
<p class="CellBody">
<a name="pgfId-901947"></a>xyvsy</p>
</td>
<td rowspan="1" colspan="1">
<code>
<a name="pgfId-901949"></a>a.xyvsy(array)</code>
</td>
</tr>
<tr>
<td rowspan="1" colspan="1">
<p class="CellBody">
<a name="pgfId-901951"></a>yxvsx</p>
</td>
<td rowspan="1" colspan="1">
<code>
<a name="pgfId-901953"></a>a.yxvsx(array)</code>
</td>
</tr>
<tr>
<td rowspan="1" colspan="1">
<p class="CellBody">
<a name="pgfId-901955"></a>clear</p>
</td>
<td rowspan="1" colspan="1">
<code>
<a name="pgfId-901957"></a>a.clear()</code>
</td>
</tr>
<tr>
<td rowspan="1" colspan="2">
	<strong>
<a name="pgfId-901959"></a>Query Functions</strong>
</td>
</tr>
<tr>
<td rowspan="1" colspan="1">
<p class="CellBody">
<a name="pgfId-901963"></a>graphicsmethodname</p>
</td>
<td rowspan="1" colspan="1">
<code>
<a name="pgfId-901965"></a>a.graphicsmethodname('box')</code>
</td>
</tr>
<tr>
<td rowspan="1" colspan="1">
<p class="CellBody">
<a name="pgfId-901967"></a>getcontinentstype</p>
</td>
<td rowspan="1" colspan="1">
<code>
<a name="pgfId-901969"></a>a.getcontinentstype()</code>
</td>
</tr>
<tr>
<td rowspan="1" colspan="1">
<p class="CellBody">
<a name="pgfId-901971"></a>isgraphicsmethod</p>
</td>
<td rowspan="1" colspan="1">
<code>
<a name="pgfId-901973"></a>a.isgraphicsmethod()</code>
</td>
</tr>
<tr>
<td rowspan="1" colspan="1">
<p class="CellBody">
<a name="pgfId-901975"></a>isboxfill</p>
</td>
<td rowspan="1" colspan="1">
<code>
<a name="pgfId-901977"></a>a.isboxfill()</code>
</td>
</tr>
<tr>
<td rowspan="1" colspan="1">
<p class="CellBody">
<a name="pgfId-901979"></a>iscontinents</p>
</td>
<td rowspan="1" colspan="1">
<code>
<a name="pgfId-901981"></a>a.iscontinents()</code>
</td>
</tr>
<tr>
<td rowspan="1" colspan="1">
<p class="CellBody">
<a name="pgfId-901983"></a>isisofill</p>
</td>
<td rowspan="1" colspan="1">
<code>
<a name="pgfId-901985"></a>a.isisofill()</code>
</td>
</tr>
<tr>
<td rowspan="1" colspan="1">
<p class="CellBody">
<a name="pgfId-901987"></a>isisoline</p>
</td>
<td rowspan="1" colspan="1">
<code>
<a name="pgfId-901989"></a>a.isisoline()</code>
</td>
</tr>
<tr>
<td rowspan="1" colspan="1">
<p class="CellBody">
<a name="pgfId-901991"></a>isoutfill</p>
</td>
<td rowspan="1" colspan="1">
<code>
<a name="pgfId-901993"></a>a.isoutfill()</code>
</td>
</tr>
<tr>
<td rowspan="1" colspan="1">
<p class="CellBody">
<a name="pgfId-901995"></a>isoutline</p>
</td>
<td rowspan="1" colspan="1">
<code>
<a name="pgfId-901997"></a>a.isoutline()</code>
</td>
</tr>
<tr>
<td rowspan="1" colspan="1">
<p class="CellBody">
<a name="pgfId-901999"></a>isvector</p>
</td>
<td rowspan="1" colspan="1">
<code>
<a name="pgfId-902001"></a>a.isvector()</code>
</td>
</tr>
<tr>
<td rowspan="1" colspan="1">
<p class="CellBody">
<a name="pgfId-902003"></a>isxvsy</p>
</td>
<td rowspan="1" colspan="1">
<code>
<a name="pgfId-902005"></a>a.isxvsy()</code>
</td>
</tr>
<tr>
<td rowspan="1" colspan="1">
<p class="CellBody">
<a name="pgfId-902007"></a>isxyvsy</p>
</td>
<td rowspan="1" colspan="1">
<code>
<a name="pgfId-902009"></a>a.isxyvsy()</code>
</td>
</tr>
<tr>
<td rowspan="1" colspan="1">
<p class="CellBody">
<a name="pgfId-902011"></a>isyxvsx</p>
</td>
<td rowspan="1" colspan="1">
<code>
<a name="pgfId-902013"></a>a.isyxvsx()</code>
</td>
</tr>
<tr>
<td rowspan="1" colspan="1">
<p class="CellBody">
<a name="pgfId-902015"></a>istemplate</p>
</td>
<td rowspan="1" colspan="1">
<code>
<a name="pgfId-902017"></a>a.istemplate()</code>
</td>
</tr>
<tr>
<td rowspan="1" colspan="1">
<p class="CellBody">
<a name="pgfId-902019"></a>issecondaryobject</p>
</td>
<td rowspan="1" colspan="1">
<code>
<a name="pgfId-902021"></a>a.issecondaryobject()</code>
</td>
</tr>
<tr>
<td rowspan="1" colspan="1">
<p class="CellBody">
<a name="pgfId-902023"></a>isfillarea</p>
</td>
<td rowspan="1" colspan="1">
<code>
<a name="pgfId-902025"></a>a.isfillarea()</code>
</td>
</tr>
<tr>
<td rowspan="1" colspan="1">
<p class="CellBody">
<a name="pgfId-902027"></a>isline</p>
</td>
<td rowspan="1" colspan="1">
<code>
<a name="pgfId-902029"></a>a.isline()</code>
</td>
</tr>
<tr>
<td rowspan="1" colspan="1">
<p class="CellBody">
<a name="pgfId-902031"></a>ismarker</p>
</td>
<td rowspan="1" colspan="1">
<code>
<a name="pgfId-902033"></a>a.ismarker()</code>
</td>
</tr>
<tr>
<td rowspan="1" colspan="1">
<p class="CellBody">
<a name="pgfId-902035"></a>istextcombined</p>
</td>
<td rowspan="1" colspan="1">
<code>
<a name="pgfId-902037"></a>a.istextcombined()</code>
</td>
</tr>
<tr>
<td rowspan="1" colspan="1">
<p class="CellBody">
<a name="pgfId-902039"></a>istextorientation</p>
</td>
<td rowspan="1" colspan="1">
<code>
<a name="pgfId-902041"></a>a.istextorientation()</code>
</td>
</tr>
<tr>
<td rowspan="1" colspan="1">
<p class="CellBody">
<a name="pgfId-902043"></a>istexttable</p>
</td>
<td rowspan="1" colspan="1">
<code>
<a name="pgfId-902045"></a>a.istexttable()</code>
</td>
</tr>
<tr>
<td rowspan="1" colspan="2">
	<strong>
<a name="pgfId-902047"></a>List Available Templates, Graphics Methods and Secondary Objects</strong>
</td>
</tr>
<tr>
<td rowspan="1" colspan="1">
<p class="CellBody">
<a name="pgfId-902051"></a>listelements</p>
</td>
<td rowspan="1" colspan="1">
<code>
<a name="pgfId-902053"></a>a.listelements()</code>
</td>
</tr>
<tr>
<td rowspan="1" colspan="1">
<p class="CellBody">
<a name="pgfId-902055"></a>show</p>
</td>
<td rowspan="1" colspan="1">
<code>
<a name="pgfId-902057"></a>a.show(`boxfill')</code>
</td>
</tr>
<tr>
<td rowspan="1" colspan="1">
<p class="CellBody">
<a name="pgfId-910585"></a>list</p>
</td>
<td rowspan="1" colspan="1">
<p><code>
<a name="pgfId-910587"></a>box.list()</code></p>
<p><code class="CellBody">
<a name="codegfId-910592"></a>con.list</code></p>
<p><code class="CellBody">
<a name="codegfId-910590"></a>isol.list()</code></p>
<p><code class="CellBody">
<a name="codegfId-910593"></a>isof.list()</code></p>
<p><code class="CellBody">
<a name="codegfId-910594"></a>outl.list()</code></p>
<p><code class="CellBody">
<a name="codegfId-910595"></a>outf.list()</code></p>
<p><code class="CellBody">
<a name="codegfId-910596"></a>sct.list()</code></p>
<p><code class="CellBody">
<a name="codegfId-910597"></a>vc.list()</code></p>
<p><code class="CellBody">
<a name="codegfId-910598"></a>xy.list()</code></p>
<p><code class="CellBody">
<a name="codegfId-910591"></a>tcodel.list()</code></p>
<p><code class="CellBody">
<a name="codegfId-910599"></a>fa.list()</code></p>
<p><code class="CellBody">
<a name="codegfId-910600"></a>tt.list()</code></p>
<p><code class="CellBody">
<a name="codegfId-910601"></a>to.list()</code></p>
<p><code class="CellBody">
<a name="codegfId-910602"></a>tc.list()</code></p>
</td>
</tr>
<tr>
<td rowspan="1" colspan="2">
	<strong>
<a name="pgfId-902059"></a>Graphics Methods Objects</strong>
</td>
</tr>
<tr>
<td rowspan="1" colspan="2">
	<strong>
<a name="pgfId-902063"></a>Boxfill</strong>
</td>
</tr>
<tr>
<td rowspan="1" colspan="1">
<p class="CellBody">
<a name="pgfId-902067"></a>createboxfill</p>
</td>
<td rowspan="1" colspan="1">
<code>
<a name="pgfId-902069"></a>box = a.createboxfill('new')</code>
</td>
</tr>
<tr>
<td rowspan="1" colspan="1">
<p class="CellBody">
<a name="pgfId-902071"></a>getboxfill</p>
</td>
<td rowspan="1" colspan="1">
<code>
<a name="pgfId-902073"></a>box = a.getboxfill() </code>
</td>
</tr>
<tr>
<td rowspan="1" colspan="2">
	<strong>
<a name="pgfId-902079"></a>Continents</strong>
</td>
</tr>
<tr>
<td rowspan="1" colspan="1">
<p class="CellBody">
<a name="pgfId-902083"></a>createcontinents</p>
</td>
<td rowspan="1" colspan="1">
<code>
<a name="pgfId-902085"></a>con = a.createcontinents('new')</code>
</td>
</tr>
<tr>
<td rowspan="1" colspan="1">
<p class="CellBody">
<a name="pgfId-902087"></a>getcontinents</p>
</td>
<td rowspan="1" colspan="1">
<code>
<a name="pgfId-902089"></a>con = a.getcontinents() </code>
</td>
</tr>
<tr>
<td rowspan="1" colspan="2">
	<strong>
<a name="pgfId-902095"></a>Isofill</strong>
</td>
</tr>
<tr>
<td rowspan="1" colspan="1">
<p class="CellBody">
<a name="pgfId-902099"></a>createisofill</p>
</td>
<td rowspan="1" colspan="1">
<code>
<a name="pgfId-902101"></a>iso = a.createisofill('new')</code>
</td>
</tr>
<tr>
<td rowspan="1" colspan="1">
<p class="CellBody">
<a name="pgfId-902103"></a>getisofill</p>
</td>
<td rowspan="1" colspan="1">
<code>
<a name="pgfId-902105"></a>iso = a.getisofill()</code>
</td>
</tr>
<tr>
<td rowspan="1" colspan="2">
	<strong>
<a name="pgfId-902111"></a>Isoline</strong>
</td>
</tr>
<tr>
<td rowspan="1" colspan="1">
<p class="CellBody">
<a name="pgfId-902115"></a>createisoline</p>
</td>
<td rowspan="1" colspan="1">
<code>
<a name="pgfId-902117"></a>iso = a.createisoline(`new')</code>
</td>
</tr>
<tr>
<td rowspan="1" colspan="1">
<p class="CellBody">
<a name="pgfId-902119"></a>getisoline</p>
</td>
<td rowspan="1" colspan="1">
<code>
<a name="pgfId-902121"></a>iso = a.getisoline()</code>
</td>
</tr>
<tr>
<td rowspan="1" colspan="2">
	<strong>
<a name="pgfId-902127"></a>Outfill</strong>
</td>
</tr>
<tr>
<td rowspan="1" colspan="1">
<p class="CellBody">
<a name="pgfId-902131"></a>createoutfill</p>
</td>
<td rowspan="1" colspan="1">
<code>
<a name="pgfId-902133"></a>out = a.createoutfill(`new')</code>
</td>
</tr>
<tr>
<td rowspan="1" colspan="1">
<p class="CellBody">
<a name="pgfId-902135"></a>getoutfill</p>
</td>
<td rowspan="1" colspan="1">
<code>
<a name="pgfId-902137"></a>out = a.getoutfill()</code>
</td>
</tr>
<tr>
<td rowspan="1" colspan="2">
	<strong>
<a name="pgfId-902143"></a>Outline</strong>
</td>
</tr>
<tr>
<td rowspan="1" colspan="1">
<p class="CellBody">
<a name="pgfId-902147"></a>createoutline</p>
</td>
<td rowspan="1" colspan="1">
<code>
<a name="pgfId-902149"></a>out = a.createoutline(`new')</code>
</td>
</tr>
<tr>
<td rowspan="1" colspan="1">
<p class="CellBody">
<a name="pgfId-902151"></a>getoutline</p>
</td>
<td rowspan="1" colspan="1">
<code>
<a name="pgfId-902153"></a>out = a.getoutline()</code>
</td>
</tr>
<tr>
<td rowspan="1" colspan="2">
	<strong>
<a name="pgfId-902159"></a>Scatter</strong>
</td>
</tr>
<tr>
<td rowspan="1" colspan="1">
<p class="CellBody">
<a name="pgfId-902163"></a>createscatter</p>
</td>
<td rowspan="1" colspan="1">
<code>
<a name="pgfId-902165"></a>scr = a.createscatter(`new')</code>
</td>
</tr>
<tr>
<td rowspan="1" colspan="1">
<p class="CellBody">
<a name="pgfId-902167"></a>getscatter</p>
</td>
<td rowspan="1" colspan="1">
<code>
<a name="pgfId-902169"></a>scr = a.getscatter()</code>
</td>
</tr>
<tr>
<td rowspan="1" colspan="2">
	<strong>
<a name="pgfId-902175"></a>Vector</strong>
</td>
</tr>
<tr>
<td rowspan="1" colspan="1">
<p class="CellBody">
<a name="pgfId-902179"></a>createvector</p>
</td>
<td rowspan="1" colspan="1">
<code>
<a name="pgfId-902181"></a>vc = a.createvector(`new')</code>
</td>
</tr>
<tr>
<td rowspan="1" colspan="1">
<p class="CellBody">
<a name="pgfId-902183"></a>getvector</p>
</td>
<td rowspan="1" colspan="1">
<code>
<a name="pgfId-902185"></a>vc = a.getvector()</code>
</td>
</tr>
<tr>
<td rowspan="1" colspan="2">
	<strong>
<a name="pgfId-902191"></a>XvsY</strong>
</td>
</tr>
<tr>
<td rowspan="1" colspan="1">
<p class="CellBody">
<a name="pgfId-902195"></a>createxvsy</p>
</td>
<td rowspan="1" colspan="1">
<code>
<a name="pgfId-902197"></a>xy = a.createxvsy(`new')</code>
</td>
</tr>
<tr>
<td rowspan="1" colspan="1">
<p class="CellBody">
<a name="pgfId-902199"></a>getxvsy</p>
</td>
<td rowspan="1" colspan="1">
<code>
<a name="pgfId-902201"></a>xy = a.getxvsy()</code>
</td>
</tr>
<tr>
<td rowspan="1" colspan="2">
	<strong>
<a name="pgfId-902207"></a>Xyvsy</strong>
</td>
</tr>
<tr>
<td rowspan="1" colspan="1">
<p class="CellBody">
<a name="pgfId-902211"></a>createxyvsy</p>
</td>
<td rowspan="1" colspan="1">
<code>
<a name="pgfId-902213"></a>xy = a.createxyvsy(`new')</code>
</td>
</tr>
<tr>
<td rowspan="1" colspan="1">
<p class="CellBody">
<a name="pgfId-902215"></a>getxyvsy</p>
</td>
<td rowspan="1" colspan="1">
<code>
<a name="pgfId-902217"></a>xy = a.getxyvsy()</code>
</td>
</tr>
<tr>
<td rowspan="1" colspan="2">
	<strong>
<a name="pgfId-902223"></a>Yxvsx</strong>
</td>
</tr>
<tr>
<td rowspan="1" colspan="1">
<p class="CellBody">
<a name="pgfId-902227"></a>createyxvsx</p>
</td>
<td rowspan="1" colspan="1">
<code>
<a name="pgfId-902229"></a>yx = a.createyxvsx(`new')</code>
</td>
</tr>
<tr>
<td rowspan="1" colspan="1">
<p class="CellBody">
<a name="pgfId-902231"></a>getyxvsx</p>
</td>
<td rowspan="1" colspan="1">
<code>
<a name="pgfId-902233"></a>yx = a.createyxvsx()</code>
</td>
</tr>
<tr>
<td rowspan="1" colspan="2">
	<strong>
<a name="pgfId-902239"></a>Picture Template</strong>
</td>
</tr>
<tr>
<td rowspan="1" colspan="1">
<p class="CellBody">
<a name="pgfId-902243"></a>createtemplate</p>
</td>
<td rowspan="1" colspan="1">
<code>
<a name="pgfId-902245"></a>tpl = a.createtemplate(`new')</code>
</td>
</tr>
<tr>
<td rowspan="1" colspan="1">
<p class="CellBody">
<a name="pgfId-902247"></a>gettemplate</p>
</td>
<td rowspan="1" colspan="1">
<code>
<a name="pgfId-902249"></a>tpl = gettemplate()</code>
</td>
</tr>
<tr>
<td rowspan="1" colspan="2">
	<strong>
<a name="pgfId-902255"></a>Secondary Objects</strong>
</td>
</tr>
<tr>
<td rowspan="1" colspan="2">
	<strong>
<a name="pgfId-902259"></a>Colormap Commands</strong>
</td>
</tr>
<tr>
<td rowspan="1" colspan="1">
<p class="CellBody">
<a name="pgfId-902263"></a>setcolormap</p>
</td>
<td rowspan="1" colspan="1">
<code>
<a name="pgfId-902265"></a>a.setcolormap("colormap_name")</code>
</td>
</tr>
<tr>
<td rowspan="1" colspan="1">
<p class="CellBody">
<a name="pgfId-902267"></a>setcolorcell</p>
</td>
<td rowspan="1" colspan="1">
<code>
<a name="pgfId-902269"></a>.setcolorcell(16,100,100,100)</code>
</td>
</tr>
<tr>
<td rowspan="1" colspan="1">
<p class="CellBody">
<a name="pgfId-902271"></a>colormapgui</p>
</td>
<td rowspan="1" colspan="1">
<code>
<a name="pgfId-902273"></a>a.colormapgui()</code>
</td>
</tr>
<tr>
<td rowspan="1" colspan="2">
	<strong>
<a name="pgfId-902275"></a>Fill Area </strong>
</td>
</tr>
<tr>
<td rowspan="1" colspan="1">
<p class="CellBody">
<a name="pgfId-902279"></a>createfillarea</p>
</td>
<td rowspan="1" colspan="1">
<code>
<a name="pgfId-902281"></a>fa = a.createfillarea('new')</code>
</td>
</tr>
<tr>
<td rowspan="1" colspan="1">
<p class="CellBody">
<a name="pgfId-902283"></a>getfillarea</p>
</td>
<td rowspan="1" colspan="1">
<code>
<a name="pgfId-902285"></a>fa = a.getfillarea() </code>
</td>
</tr>
<tr>
<td rowspan="1" colspan="2">
	<strong>
<a name="pgfId-902291"></a>Line</strong>
</td>
</tr>
<tr>
<td rowspan="1" colspan="1">
<p class="CellBody">
<a name="pgfId-902295"></a>createline</p>
</td>
<td rowspan="1" colspan="1">
<code>
<a name="pgfId-902297"></a>ln = a.createline(`new')</code>
</td>
</tr>
<tr>
<td rowspan="1" colspan="1">
<p class="CellBody">
<a name="pgfId-902299"></a>getline</p>
</td>
<td rowspan="1" colspan="1">
<code>
<a name="pgfId-902301"></a>ln = a.getline()</code>
</td>
</tr>
<tr>
<td rowspan="1" colspan="2">
	<strong>
<a name="pgfId-902307"></a>marker</strong>
</td>
</tr>
<tr>
<td rowspan="1" colspan="1">
<p class="CellBody">
<a name="pgfId-902311"></a>createmarker</p>
</td>
<td rowspan="1" colspan="1">
<code>
<a name="pgfId-902313"></a>mk = a.createmarker(`new')</code>
</td>
</tr>
<tr>
<td rowspan="1" colspan="1">
<p class="CellBody">
<a name="pgfId-902315"></a>getmarker</p>
</td>
<td rowspan="1" colspan="1">
<code>
<a name="pgfId-902317"></a>mk = a.getlmarker()</code>
</td>
</tr>
<tr>
<td rowspan="1" colspan="2">
	<strong>
<a name="pgfId-902323"></a>Text-Combined</strong>
</td>
</tr>
<tr>
<td rowspan="1" colspan="1">
<p class="CellBody">
<a name="pgfId-902327"></a>createtextcombined</p>
</td>
<td rowspan="1" colspan="1">
<code>
<a name="pgfId-902329"></a>tc = a.createtextcombined(`new')</code>
</td>
</tr>
<tr>
<td rowspan="1" colspan="1">
<p class="CellBody">
<a name="pgfId-902331"></a>gettextcombined</p>
</td>
<td rowspan="1" colspan="1">
<code>
<a name="pgfId-902333"></a>tc = a.gettextcombined()</code>
</td>
</tr>
<tr>
<td rowspan="1" colspan="2">
	<strong>
<a name="pgfId-902339"></a>Text-Orientation</strong>
</td>
</tr>
<tr>
<td rowspan="1" colspan="1">
<p class="CellBody">
<a name="pgfId-902343"></a>createtextorientation</p>
</td>
<td rowspan="1" colspan="1">
<code>
<a name="pgfId-902345"></a>to.createtextorientation(`new')</code>
</td>
</tr>
<tr>
<td rowspan="1" colspan="1">
<p class="CellBody">
<a name="pgfId-902347"></a>gettextorientation</p>
</td>
<td rowspan="1" colspan="1">
<code>
<a name="pgfId-902349"></a>to = a.gettextorientation()</code>
</td>
</tr>
<tr>
<td rowspan="1" colspan="2">
	<strong>
<a name="pgfId-902355"></a>Text-Table</strong>
</td>
</tr>
<tr>
<td rowspan="1" colspan="1">
<p class="CellBody">
<a name="pgfId-902359"></a>createtexttable</p>
</td>
<td rowspan="1" colspan="1">
<code>
<a name="pgfId-902361"></a>tt = a.createtexttable(`new')</code>
</td>
</tr>
<tr>
<td rowspan="1" colspan="1">
<p class="CellBody">
<a name="pgfId-902363"></a>gettexttable</p>
</td>
<td rowspan="1" colspan="1">
<code>
<a name="pgfId-902365"></a>tt = a.gettexttable()</code>
</td>
</tr>
<tr>
<td rowspan="1" colspan="2">
	<strong>
<a name="pgfId-902371"></a>Remove Objects</strong>
</td>
</tr>
<tr>
<td rowspan="1" colspan="1">
<p class="CellBody">
<a name="pgfId-902375"></a>removeobject</p>
</td>
<td rowspan="1" colspan="1">
<code>
<a name="pgfId-902377"></a>a.removeobject(a)</code>
</td>
</tr>
<tr>
<td rowspan="1" colspan="2">
	<strong>
<a name="pgfId-902379"></a>Set Default Picture Template and Graphics Methods</strong>
</td>
</tr>
<tr>
<td rowspan="1" colspan="1">
<p class="CellBody">
<a name="pgfId-902383"></a>set</p>
</td>
<td rowspan="1" colspan="1">
<code>
<a name="pgfId-902385"></a>a.set('isofill','some_isofill_name') </code>
</td>
</tr>
<tr>
<td rowspan="1" colspan="2">
	<strong>
<a name="pgfId-902387"></a>Set Continents Type</strong>
</td>
</tr>
<tr>
<td rowspan="1" colspan="1">
<p class="CellBody">
<a name="pgfId-902391"></a>setcontinentstype</p>
</td>
<td rowspan="1" colspan="1">
<code>
<a name="pgfId-902393"></a>a.setcontinentstype(3) </code>
</td>
</tr>
<tr>
<td rowspan="1" colspan="2">
	<strong>
<a name="pgfId-902395"></a>Animation</strong>
</td>
</tr>
<tr>
<td rowspan="1" colspan="1">
<p class="CellBody">
<a name="pgfId-902399"></a>animate</p>
</td>
<td rowspan="1" colspan="1">
<code>
<a name="pgfId-902401"></a>a.animate()</code>
</td>
</tr>
<tr>
<td rowspan="1" colspan="2">
	<strong>
<a name="pgfId-902403"></a>Flush</strong>
</td>
</tr>
<tr>
<td rowspan="1" colspan="1">
<p class="CellBody">
<a name="pgfId-902407"></a>flush</p>
</td>
<td rowspan="1" colspan="1">
<code>
<a name="pgfId-902409"></a>a.flush()</code>
</td>
</tr>
<tr>
<td rowspan="1" colspan="2">
	<strong>
<a name="pgfId-902411"></a>Grid</strong>
</td>
</tr>
<tr>
<td rowspan="1" colspan="1">
<p class="CellBody">
<a name="pgfId-902415"></a>grid</p>
</td>
<td rowspan="1" colspan="1">
<code>
<a name="pgfId-902417"></a>a.grid(12,24, -90,90, -180,180)</code>
</td>
</tr>
<tr>
<td rowspan="1" colspan="1">
<p class="CellBody">
<a name="pgfId-902419"></a>resetgrid</p>
</td>
<td rowspan="1" colspan="1">
<code>
<a name="pgfId-902421"></a>a.resetgrid()</code>
</td>
</tr>
</table>

###VCS Cheat Sheet

<table class="table">
<tbody><tr>
<td rowspan="1" colspan="1">
<code class="CellBody">
<a name="pgfId-910154"></a>init</code>
</td>
<td rowspan="1" colspan="1">
<code>
<a name="pgfId-910156"></a>graphicsmethodname</code>
</td>
<td rowspan="1" colspan="1">
<code>
<a name="pgfId-910158"></a>createisoline</code>
</td>
<td rowspan="1" colspan="1">
<code>
<a name="pgfId-910160"></a>fillareaobject</code>
</td>
</tr>
<tr>
<td rowspan="1" colspan="1">
<code class="CellBody">
<a name="pgfId-910162"></a>help</code>
</td>
<td rowspan="1" colspan="1">
<code>
<a name="pgfId-910164"></a>getcontinentstype</code>
</td>
<td rowspan="1" colspan="1">
<code>
<a name="pgfId-910166"></a>getisoline</code>
</td>
<td rowspan="1" colspan="1">
<code>
<a name="pgfId-910168"></a>createline</code>
</td>
</tr>
<tr>
<td rowspan="1" colspan="1">
<code class="CellBody">
<a name="pgfId-910170"></a>objecthelp</code>
</td>
<td rowspan="1" colspan="1">
<code>
<a name="pgfId-910172"></a>isgraphicsmethod</code>
</td>
<td rowspan="1" colspan="1">
<code>
<a name="pgfId-910174"></a>isolineobject</code>
</td>
<td rowspan="1" colspan="1">
<code>
<a name="pgfId-910176"></a>getline</code>
</td>
</tr>
<tr>
<td rowspan="1" colspan="1">
<code class="CellBody">
<a name="pgfId-910178"></a>mode</code>
</td>
<td rowspan="1" colspan="1">
<code>
<a name="pgfId-910180"></a>isboxfill</code>
</td>
<td rowspan="1" colspan="1">
<code>
<a name="pgfId-910182"></a>createoutfill</code>
</td>
<td rowspan="1" colspan="1">
<code>
<a name="pgfId-910184"></a>lineobject</code>
</td>
</tr>
<tr>
<td rowspan="1" colspan="1">
<code class="CellBody">
<a name="pgfId-910186"></a>update</code>
</td>
<td rowspan="1" colspan="1">
<code>
<a name="pgfId-910188"></a>iscontinents</code>
</td>
<td rowspan="1" colspan="1">
<code>
<a name="pgfId-910190"></a>getoutfill</code>
</td>
<td rowspan="1" colspan="1">
<code>
<a name="pgfId-910192"></a>marker</code>
</td>
</tr>
<tr>
<td rowspan="1" colspan="1">
<code class="CellBody">
<a name="pgfId-910194"></a>open</code>
</td>
<td rowspan="1" colspan="1">
<code>
<a name="pgfId-910196"></a>isisofill</code>
</td>
<td rowspan="1" colspan="1">
<code>
<a name="pgfId-910198"></a>outfillobject</code>
</td>
<td rowspan="1" colspan="1">
<code>
<a name="pgfId-910200"></a>createmarker</code>
</td>
</tr>
<tr>
<td rowspan="1" colspan="1">
<code class="CellBody">
<a name="pgfId-910202"></a>close</code>
</td>
<td rowspan="1" colspan="1">
<code>
<a name="pgfId-910204"></a>isisoline</code>
</td>
<td rowspan="1" colspan="1">
<code>
<a name="pgfId-910206"></a>createoutline</code>
</td>
<td rowspan="1" colspan="1">
<code>
<a name="pgfId-910208"></a>getmarker</code>
</td>
</tr>
<tr>
<td rowspan="1" colspan="1">
<code class="CellBody">
<a name="pgfId-910210"></a>flushcanvas</code>
</td>
<td rowspan="1" colspan="1">
<code>
<a name="pgfId-910212"></a>isoutfill</code>
</td>
<td rowspan="1" colspan="1">
<code>
<a name="pgfId-910214"></a>getoutline</code>
</td>
<td rowspan="1" colspan="1">
<code>
<a name="pgfId-910216"></a>markerobject</code>
</td>
</tr>
<tr>
<td rowspan="1" colspan="1">
<code class="CellBody">
<a name="pgfId-910218"></a>refreshcanvas</code>
</td>
<td rowspan="1" colspan="1">
<code>
<a name="pgfId-910220"></a>isoutline</code>
</td>
<td rowspan="1" colspan="1">
<code>
<a name="pgfId-910222"></a>outlineobject</code>
</td>
<td rowspan="1" colspan="1">
<code>
<a name="pgfId-910224"></a>createtextcombined</code>
</td>
</tr>
<tr>
<td rowspan="1" colspan="1">
<code class="CellBody">
<a name="pgfId-910226"></a>portrait</code>
</td>
<td rowspan="1" colspan="1">
<code>
<a name="pgfId-910228"></a>isvector</code>
</td>
<td rowspan="1" colspan="1">
<code>
<a name="pgfId-910230"></a>createscatter</code>
</td>
<td rowspan="1" colspan="1">
<code>
<a name="pgfId-910232"></a>gettextcombined</code>
</td>
</tr>
<tr>
<td rowspan="1" colspan="1">
<code class="CellBody">
<a name="pgfId-910234"></a>landscape</code>
</td>
<td rowspan="1" colspan="1">
<code>
<a name="pgfId-910236"></a>isxvsy</code>
</td>
<td rowspan="1" colspan="1">
<code>
<a name="pgfId-910238"></a>getscatter</code>
</td>
<td rowspan="1" colspan="1">
<code>
<a name="pgfId-910240"></a>textcombinedobject</code>
</td>
</tr>
<tr>
<td rowspan="1" colspan="1">
<code class="CellBody">
<a name="pgfId-910242"></a>page</code>
</td>
<td rowspan="1" colspan="1">
<code>
<a name="pgfId-910244"></a>isxyvsy</code>
</td>
<td rowspan="1" colspan="1">
<code>
<a name="pgfId-910246"></a>scatterobject</code>
</td>
<td rowspan="1" colspan="1">
<code>
<a name="pgfId-910248"></a>createtextorientation</code>
</td>
</tr>
<tr>
<td rowspan="1" colspan="1">
<code class="CellBody">
<a name="pgfId-910250"></a>geometry</code>
</td>
<td rowspan="1" colspan="1">
<code>
<a name="pgfId-910252"></a>isyxvsx</code>
</td>
<td rowspan="1" colspan="1">
<code>
<a name="pgfId-910254"></a>createvector</code>
</td>
<td rowspan="1" colspan="1">
<code>
<a name="pgfId-910256"></a>gettextorientation</code>
</td>
</tr>
<tr>
<td rowspan="1" colspan="1">
<code class="CellBody">
<a name="pgfId-910258"></a>printer</code>
</td>
<td rowspan="1" colspan="1">
<code>
<a name="pgfId-910260"></a>istemplate</code>
</td>
<td rowspan="1" colspan="1">
<code>
<a name="pgfId-910262"></a>getvector</code>
</td>
<td rowspan="1" colspan="1">
<code>
<a name="pgfId-910264"></a>textorientationobject</code>
</td>
</tr>
<tr>
<td rowspan="1" colspan="1">
<code class="CellBody">
<a name="pgfId-910266"></a>gif</code>
</td>
<td rowspan="1" colspan="1">
<code>
<a name="pgfId-910268"></a>issecondaryobject</code>
</td>
<td rowspan="1" colspan="1">
<code>
<a name="pgfId-910270"></a>vectorobject</code>
</td>
<td rowspan="1" colspan="1">
<code>
<a name="pgfId-910272"></a>createtexttable</code>
</td>
</tr>
<tr>
<td rowspan="1" colspan="1">
<code class="CellBody">
<a name="pgfId-910274"></a>postscript</code>
</td>
<td rowspan="1" colspan="1">
<code>
<a name="pgfId-910276"></a>isfillarea</code>
</td>
<td rowspan="1" colspan="1">
<code>
<a name="pgfId-910278"></a>createxvsy</code>
</td>
<td rowspan="1" colspan="1">
<code>
<a name="pgfId-910280"></a>gettexttable</code>
</td>
</tr>
<tr>
<td rowspan="1" colspan="1">
<code class="CellBody">
<a name="pgfId-910282"></a>cgm</code>
</td>
<td rowspan="1" colspan="1">
<code>
<a name="pgfId-910284"></a>isline</code>
</td>
<td rowspan="1" colspan="1">
<code>
<a name="pgfId-910286"></a>getxvsy</code>
</td>
<td rowspan="1" colspan="1">
<code>
<a name="pgfId-910288"></a>texttableobject</code>
</td>
</tr>
<tr>
<td rowspan="1" colspan="1">
<code class="CellBody">
<a name="pgfId-910290"></a>raster</code>
</td>
<td rowspan="1" colspan="1">
<code>
<a name="pgfId-910292"></a>ismarker</code>
</td>
<td rowspan="1" colspan="1">
<code>
<a name="pgfId-910294"></a>xvsyobject</code>
</td>
<td rowspan="1" colspan="1">
<code>
<a name="pgfId-910296"></a>removeobject</code>
</td>
</tr>
<tr>
<td rowspan="1" colspan="1">
<code class="CellBody">
<a name="pgfId-910298"></a>pstogif</code>
</td>
<td rowspan="1" colspan="1">
<code>
<a name="pgfId-910300"></a>istextcombined</code>
</td>
<td rowspan="1" colspan="1">
<code>
<a name="pgfId-910302"></a>createxyvsy</code>
</td>
<td rowspan="1" colspan="1">
<code>
<a name="pgfId-910304"></a>set</code>
</td>
</tr>
<tr>
<td rowspan="1" colspan="1">
<code class="CellBody">
<a name="pgfId-910306"></a>plot</code>
</td>
<td rowspan="1" colspan="1">
<code>
<a name="pgfId-910308"></a>istextorientation</code>
</td>
<td rowspan="1" colspan="1">
<code>
<a name="pgfId-910310"></a>getxyvsy</code>
</td>
<td rowspan="1" colspan="1">
<code>
<a name="pgfId-910312"></a>setcontinentstype</code>
</td>
</tr>
<tr>
<td rowspan="1" colspan="1">
<code class="CellBody">
<a name="pgfId-910314"></a>boxfill</code>
</td>
<td rowspan="1" colspan="1">
<code>
<a name="pgfId-910316"></a>istexttable</code>
</td>
<td rowspan="1" colspan="1">
<code>
<a name="pgfId-910318"></a>xyvsyobject</code>
</td>
<td rowspan="1" colspan="1">
<code>
<a name="pgfId-910320"></a>animate</code>
</td>
</tr>
<tr>
<td rowspan="1" colspan="1">
<code class="CellBody">
<a name="pgfId-910322"></a>continents</code>
</td>
<td rowspan="1" colspan="1">
<code>
<a name="pgfId-910324"></a>listelements</code>
</td>
<td rowspan="1" colspan="1">
<code>
<a name="pgfId-910326"></a>createyxvsx</code>
</td>
<td rowspan="1" colspan="1">
<code>
<a name="pgfId-910328"></a>flush</code>
</td>
</tr>
<tr>
<td rowspan="1" colspan="1">
<code class="CellBody">
<a name="pgfId-910330"></a>isofill</code>
</td>
<td rowspan="1" colspan="1">
<code>
<a name="pgfId-910332"></a>show</code>
</td>
<td rowspan="1" colspan="1">
<code>
<a name="pgfId-910334"></a>getyxvsx</code>
</td>
<td rowspan="1" colspan="1">
<code>
<a name="pgfId-910336"></a>grid</code>
</td>
</tr>
<tr>
<td rowspan="1" colspan="1">
<code class="CellBody">
<a name="pgfId-910338"></a>isoline</code>
</td>
<td rowspan="1" colspan="1">
<code>
<a name="pgfId-910340"></a>createboxfill</code>
</td>
<td rowspan="1" colspan="1">
<code>
<a name="pgfId-910342"></a>yxvsxobject</code>
</td>
<td rowspan="1" colspan="1">
<code>
<a name="pgfId-910344"></a>resetgrid</code>
</td>
</tr>
<tr>
<td rowspan="1" colspan="1">
<code class="CellBody">
<a name="pgfId-910346"></a>outfill</code>
</td>
<td rowspan="1" colspan="1">
<code>
<a name="pgfId-910348"></a>getboxfill</code>
</td>
<td rowspan="1" colspan="1">
<code>
<a name="pgfId-910350"></a>createtemplate</code>
</td>
<td rowspan="1" colspan="1">
<code>
<a name="pgfId-910352"></a>list</code>
</td>
</tr>
<tr>
<td rowspan="1" colspan="1">
<code class="CellBody">
<a name="pgfId-910354"></a>outline</code>
</td>
<td rowspan="1" colspan="1">
<code>
<a name="pgfId-910356"></a>boxfillobject</code>
</td>
<td rowspan="1" colspan="1">
<code>
<a name="pgfId-910358"></a>gettemplate</code>
</td>
<td rowspan="1" colspan="1">

</td>
</tr>
<tr>
<td rowspan="1" colspan="1">
<code class="CellBody">
<a name="pgfId-910362"></a>scatter</code>
</td>
<td rowspan="1" colspan="1">
<code>
<a name="pgfId-910364"></a>createcontinents</code>
</td>
<td rowspan="1" colspan="1">
<code>
<a name="pgfId-910366"></a>templateobject</code>
</td>
<td rowspan="1" colspan="1">

</td>
</tr>
<tr>
<td rowspan="1" colspan="1">
<code class="CellBody">
<a name="pgfId-910370"></a>vector</code>
</td>
<td rowspan="1" colspan="1">
<code>
<a name="pgfId-910372"></a>getcontinents</code>
</td>
<td rowspan="1" colspan="1">
<code>
<a name="pgfId-910374"></a>setcolormap</code>
</td>
<td rowspan="1" colspan="1">

</td>
</tr>
<tr>
<td rowspan="1" colspan="1">
<code class="CellBody">
<a name="pgfId-910378"></a>xvsy</code>
</td>
<td rowspan="1" colspan="1">
<code>
<a name="pgfId-910380"></a>continentsobject</code>
</td>
<td rowspan="1" colspan="1">
<code>
<a name="pgfId-910382"></a>setcolorcell</code>
</td>
<td rowspan="1" colspan="1">

</td>
</tr>
<tr>
<td rowspan="1" colspan="1">
<code class="CellBody">
<a name="pgfId-910386"></a>xyvsy</code>
</td>
<td rowspan="1" colspan="1">
<code>
<a name="pgfId-910388"></a>createisofill</code>
</td>
<td rowspan="1" colspan="1">
<code>
<a name="pgfId-910390"></a>colormapgui</code>
</td>
<td rowspan="1" colspan="1">

</td>
</tr>
<tr>
<td rowspan="1" colspan="1">
<code class="CellBody">
<a name="pgfId-910394"></a>yxvsx</code>
</td>
<td rowspan="1" colspan="1">
<code>
<a name="pgfId-910396"></a>getisofill</code>
</td>
<td rowspan="1" colspan="1">
<code>
<a name="pgfId-910398"></a>createfillarea</code>
</td>
<td rowspan="1" colspan="1">

</td>
</tr>
<tr>
<td rowspan="1" colspan="1">
<code class="CellBody">
<a name="pgfId-910402"></a>clear</code>
</td>
<td rowspan="1" colspan="1">
<code>
<a name="pgfId-910404"></a>isofillobject</code>
</td>
<td rowspan="1" colspan="1">
<code>
<a name="pgfId-910406"></a>getfillarea</code>
</td>
<td rowspan="1" colspan="1">

</td>
</tr>
</tbody></table>


[Main](vcs.html) \| [Previous](vcs-8.html) \| [Next](vcs-10.html)


