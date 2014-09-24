---
layout: default
title: VCS Chapter 5
---
##  CHAPTER 5 VCS Command Reference Guide

If you want the full description of a command, then you've made it to the
right place.

Note, in the "Options" column, any item(s) surrounded by "[]" are optional to
the function.

<table class="table">
    <tr>
      <th rowspan="1" colspan="1">
        <p class="CellHeading"><a name="pgfId-892664" id="pgfId-892664"></a>Command</p>
      </th>

      <th rowspan="1" colspan="1">
        <p class="CellHeading"><a name="pgfId-892666" id="pgfId-892666"></a>Description</p>
      </th>

      <th rowspan="1" colspan="1">
        <p class="CellHeading"><a name="pgfId-892668" id="pgfId-892668"></a>Options</p>
      </th>

      <th rowspan="1" colspan="1">
        <p class="CellHeading"><a name="pgfId-892670" id="pgfId-892670"></a>Examples</p>
      </th>
    </tr>

    <tr>
      <td rowspan="1" colspan="4">
        <p class="CellHeading"><a name="pgfId-892672" id="pgfId-892672"></a>Initializing</p>
      </td>
    </tr>

    <tr>
      <td rowspan="1" colspan="1">
        <code class=""><a name="pgfId-892681" id="pgfId-892681"></a><a name="marker-892680" id="marker-892680"></a>init</code>
      </td>

      <td rowspan="1" colspan="1">
        <p class="CellBody"><a name="pgfId-892683" id="pgfId-892683"></a>Function:
        init<br/>
        # Initialize, Construct a VCS Canvas Object</p>

        <p class="CellBody"><a name="pgfId-892684" id="pgfId-892684"></a></p>

        <p class="CellBody"><a name="pgfId-892685" id="pgfId-892685"></a>Description of
        Function:</p>

        <p class="CellBody"><a name="pgfId-892686" id="pgfId-892686"></a> Construct the
        VCS Canas object. There can only be at most 8 VCS Canvases open at any given
        time.</p>
      </td>

      <td rowspan="1" colspan="1">
        <p class="CellBody"><a name="pgfId-892688" id="pgfId-892688"></a></p>
      </td>

      <td rowspan="1" colspan="1">
        <p class="CellBody"><a name="pgfId-892690" id="pgfId-892690"></a>Example of
        Use:</p>

        <pre style="word-break:normal;">import vcs,cu

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
</pre></td>
    </tr>

    <tr>
      <td rowspan="1" colspan="4">
        <p class="CellHeading"><a name="pgfId-892707" id="pgfId-892707"></a>Help
        Commands</p>
      </td>
    </tr>

    <tr>
      <td rowspan="1" colspan="1">
        <code class=""><a name="pgfId-892716" id="pgfId-892716"></a><a name="marker-892715" id="marker-892715"></a>help</code>
      </td>

      <td rowspan="1" colspan="1">
        <p class="CellBody"><a name="pgfId-892718" id="pgfId-892718"></a>Function:
        help<br/>
        # On-Line HELP!!!</p>

        <p class="CellBody"><a name="pgfId-892719" id="pgfId-892719"></a></p>

        <p class="CellBody"><a name="pgfId-892720" id="pgfId-892720"></a>Description of
        Function:</p>

        <p class="CellBody"><a name="pgfId-892721" id="pgfId-892721"></a> Gives insight
        to other VCS functions by providing a description and at least one example.</p>
      </td>

      <td rowspan="1" colspan="1">
        <p class="CellBody"><a name="pgfId-892723" id="pgfId-892723"></a></p>
      </td>

      <td rowspan="1" colspan="1">
        <p class="CellBody"><a name="pgfId-892725" id="pgfId-892725"></a>Example of
        Use:</p>

        <pre style="word-break:normal;">import vcs

vcs.help()
vcs.help(`init')
vcs.help(`plot')
</pre></td>
    </tr>

    <tr>
      <td rowspan="1" colspan="1">
        <code class=""><a name="pgfId-892733" id="pgfId-892733"></a><a name="marker-892732" id="marker-892732"></a>objecthelp</code>
      </td>

      <td rowspan="1" colspan="1">
        <p class="CellBody"><a name="pgfId-892735" id="pgfId-892735"></a> Function:
        objecthelp<br/>
        # Print out the object's doc string</p>

        <p class="CellBody"><a name="pgfId-892736" id="pgfId-892736"></a></p>

        <p class="CellBody"><a name="pgfId-892737" id="pgfId-892737"></a>Description of
        Function:</p>

        <p class="CellBody"><a name="pgfId-892738" id="pgfId-892738"></a> Print out
        information on VCS objects. See example on its use.</p>
      </td>

      <td rowspan="1" colspan="1">
        <p class="CellBody"><a name="pgfId-892740" id="pgfId-892740"></a></p>
      </td>

      <td rowspan="1" colspan="1">
        <p class="CellBody"><a name="pgfId-892742" id="pgfId-892742"></a>Example of
        Use:</p>

        <pre style="word-break:normal;">import vcs
a=vcs.init()
ln=a.getline('red')
# Get a VCS line object
a.objecthelp(ln)
# This will print out information on how to use ln
</pre></td>
    </tr>

    <tr>
      <td rowspan="1" colspan="4">
        <p class="CellHeading"><a name="pgfId-892748" id="pgfId-892748"></a>Canvas</p>
      </td>
    </tr>

    <tr>
      <td rowspan="1" colspan="1">
        <code class=""><a name="pgfId-892756" id="pgfId-892756"></a><a name="marker-910414" id="marker-910414"></a>mode</code>
      </td>

      <td rowspan="1" colspan="1">
        <p class="CellBody"><a name="pgfId-892758" id="pgfId-892758"></a>Function:
        mode<br/>
        # Update the VCS Canvas.</p>

        <p class="CellBody"><a name="pgfId-892759" id="pgfId-892759"></a></p>

        <p class="CellBody"><a name="pgfId-892760" id="pgfId-892760"></a>Description of
        Function:</p>

        <p class="CellBody"><a name="pgfId-892761" id="pgfId-892761"></a> Updating of the
        graphical displays on the VCS Canvas can be deferred until a later time. This is
        helpful when generating templates or displaying numerous plots. If a series of
        commands are given to VCS and the Canvas Mode is set to manual (i.e., 0), then no
        updating of the VCS Canvas occurs until the 'update' function is executed.</p>

        <p class="CellBody"><a name="pgfId-892762" id="pgfId-892762"></a> Note, by
        default the VCS Canvas Mode is set to `Automatic', which means VCS will update
        the VCS Canvas as necessary without prompting from the user.</p>
      </td>

      <td rowspan="1" colspan="1">
        <p class="CellBody"><a name="pgfId-892764" id="pgfId-892764"></a>1|0</p>

        <p class="CellBody"><a name="pgfId-892765" id="pgfId-892765"></a></p>

        <p class="CellBody"><a name="pgfId-892766" id="pgfId-892766"></a>1 =
        automatic</p>

        <p class="CellBody"><a name="pgfId-892767" id="pgfId-892767"></a>0=manual</p>
      </td>

      <td rowspan="1" colspan="1">
        <p class="CellBody"><a name="pgfId-892769" id="pgfId-892769"></a>Example of
        Use:</p>

        <pre style="word-break:normal;">import vcs
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
</pre></td>
    </tr>

    <tr>
      <td rowspan="1" colspan="1">
        <code class=""><a name="pgfId-892784" id="pgfId-892784"></a><a name="marker-910415" id="marker-910415"></a>update</code>
      </td>

      <td rowspan="1" colspan="1">
        <p class="CellBody"><a name="pgfId-892786" id="pgfId-892786"></a>Function:
        update</p>

        <p class="CellBody"><a name="pgfId-892787" id="pgfId-892787"></a></p>

        <p class="CellBody"><a name="pgfId-892788" id="pgfId-892788"></a>Description of
        Function:</p>

        <p class="CellBody"><a name="pgfId-892789" id="pgfId-892789"></a> If a series of
        commands are given to VCS and the Canvas Mode is set to manual, then use this
        function to update the VCS Canvas manually.</p>
      </td>

      <td rowspan="1" colspan="1">
        <p class="CellBody"><a name="pgfId-892791" id="pgfId-892791"></a></p>
      </td>

      <td rowspan="1" colspan="1">
        <p class="CellBody"><a name="pgfId-892793" id="pgfId-892793"></a>Example of
        Use:</p>

        <pre style="word-break:normal;">import vcs
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
</pre></td>
    </tr>

    <tr>
      <td rowspan="1" colspan="1">
        <code class=""><a name="pgfId-892806" id="pgfId-892806"></a><a name="marker-910416" id="marker-910416"></a>open</code>
      </td>

      <td rowspan="1" colspan="1">
        <p class="CellBody"><a name="pgfId-892808" id="pgfId-892808"></a>Function:
        open</p>

        <p class="CellBody"><a name="pgfId-892809" id="pgfId-892809"></a></p>

        <p class="CellBody"><a name="pgfId-892810" id="pgfId-892810"></a>Description of
        Function:</p>

        <p class="CellBody"><a name="pgfId-892811" id="pgfId-892811"></a> Open VCS Canvas
        object. This routine really just manages the VCS canvas. It will popup the VCS
        Canvas for viewing. It can be used to display the VCS Canvas.</p>
      </td>

      <td rowspan="1" colspan="1">
        <p class="CellBody"><a name="pgfId-892813" id="pgfId-892813"></a></p>
      </td>

      <td rowspan="1" colspan="1">
        <p class="CellBody"><a name="pgfId-892815" id="pgfId-892815"></a>Example of
        Use:</p>

        <pre style="word-break:normal;">import vcs
a=vcs.init()
a.open()
</pre></td>
    </tr>

    <tr>
      <td rowspan="1" colspan="1">
        <code class=""><a name="pgfId-892820" id="pgfId-892820"></a><a name="marker-910417" id="marker-910417"></a>close</code>
      </td>

      <td rowspan="1" colspan="1">
        <p class="CellBody"><a name="pgfId-892822" id="pgfId-892822"></a>Function:
        close</p>

        <p class="CellBody"><a name="pgfId-892823" id="pgfId-892823"></a></p>

        <p class="CellBody"><a name="pgfId-892824" id="pgfId-892824"></a>Description of
        Function:</p>

        <p class="CellBody"><a name="pgfId-892825" id="pgfId-892825"></a> Close the VCS
        Canvas. It will remove the VCS Canvas object from the screen, but not deallocate
        it.</p>
      </td>

      <td rowspan="1" colspan="1">
        <p class="CellBody"><a name="pgfId-892827" id="pgfId-892827"></a></p>
      </td>

      <td rowspan="1" colspan="1">
        <p class="CellBody"><a name="pgfId-892829" id="pgfId-892829"></a>Example of
        Use:</p>

        <pre style="word-break:normal;">import vcs
a=vcs.init()
a.plot(array,'default','isofill','quick')
a.close()
</pre></td>
    </tr>

    <tr>
      <td rowspan="1" colspan="1">
        <code class=""><a name="pgfId-892865" id="pgfId-892865"></a><a name="marker-910418" id="marker-910418"></a>portrait</code>
      </td>

      <td rowspan="1" colspan="1">
        <p class="CellBody"><a name="pgfId-892867" id="pgfId-892867"></a>Function:
        portrait</p>

        <p class="CellBody"><a name="pgfId-892868" id="pgfId-892868"></a></p>

        <p class="CellBody"><a name="pgfId-892869" id="pgfId-892869"></a>Description of
        Function:</p>

        <p class="CellBody"><a name="pgfId-892870" id="pgfId-892870"></a> Change the VCS
        Canvas orientation to Portrait.</p>
      </td>

      <td rowspan="1" colspan="1">
        <p class="CellBody"><a name="pgfId-892872" id="pgfId-892872"></a></p>
      </td>

      <td rowspan="1" colspan="1">
        <p class="CellBody"><a name="pgfId-892874" id="pgfId-892874"></a>Example of
        Use:</p>

        <pre style="word-break:normal;">a=vcs.init()
a.plot(array)
a.portrait()
# Change the VCS Canvas orientation and set object flag to portrait
</pre></td>
    </tr>

    <tr>
      <td rowspan="1" colspan="1">
        <code class=""><a name="pgfId-892879" id="pgfId-892879"></a><a name="marker-910419" id="marker-910419"></a>landscape</code>
      </td>

      <td rowspan="1" colspan="1">
        <p class="CellBody"><a name="pgfId-892881" id="pgfId-892881"></a>Function:
        landscape</p>

        <p class="CellBody"><a name="pgfId-892882" id="pgfId-892882"></a></p>

        <p class="CellBody"><a name="pgfId-892883" id="pgfId-892883"></a>Description of
        Function:</p>

        <p class="CellBody"><a name="pgfId-892884" id="pgfId-892884"></a> Change the VCS
        Canvas orientation to Landscape.</p>
      </td>

      <td rowspan="1" colspan="1">
        <p class="CellBody"><a name="pgfId-892886" id="pgfId-892886"></a></p>
      </td>

      <td rowspan="1" colspan="1">
        <p class="CellBody"><a name="pgfId-892888" id="pgfId-892888"></a>Example of
        Use:</p>

        <pre style="word-break:normal;">a=vcs.init()
a.plot(array)
a.landscape()
# Change the VCS Canvas orientation and set object flag to landscape
</pre></td>
    </tr>

    <tr>
      <td rowspan="1" colspan="1">
        <code class=""><a name="pgfId-892893" id="pgfId-892893"></a><a name="marker-910420" id="marker-910420"></a>page</code>
      </td>

      <td rowspan="1" colspan="1">
        <p class="CellBody"><a name="pgfId-892895" id="pgfId-892895"></a>Function:
        page</p>

        <p class="CellBody"><a name="pgfId-892896" id="pgfId-892896"></a></p>

        <p class="CellBody"><a name="pgfId-892897" id="pgfId-892897"></a>Description of
        Function:</p>

        <p class="CellBody"><a name="pgfId-892898" id="pgfId-892898"></a> Change the VCS
        Canvas orientation to either 'portrait' or 'landscape'.</p>

        <p class="CellBody"><a name="pgfId-892899" id="pgfId-892899"></a> The orientation
        of the VCS Canvas and of cgm and raster images is controlled by the PAGE command.
        Only portrait (y &gt; x) or landscape (x &gt; y) orientations are permitted.</p>
      </td>

      <td rowspan="1" colspan="1">
        <p class="CellBody"><a name="pgfId-892901" id="pgfId-892901"></a></p>
      </td>

      <td rowspan="1" colspan="1">
        <p class="CellBody"><a name="pgfId-892903" id="pgfId-892903"></a>Example of
        Use:</p>

        <pre style="word-break:normal;">a=vcs.init()
a.plot(array)
a.page()
# Change the VCS Canvas orientation and set object flag to portrait
</pre></td>
    </tr>

    <tr>
      <td rowspan="1" colspan="1">
        <code class=""><a name="pgfId-892908" id="pgfId-892908"></a><a name="marker-910421" id="marker-910421"></a>geometry</code>
      </td>

      <td rowspan="1" colspan="1">
        <p class="CellBody"><a name="pgfId-892910" id="pgfId-892910"></a>Function:
        geometry</p>

        <p class="CellBody"><a name="pgfId-892911" id="pgfId-892911"></a></p>

        <p class="CellBody"><a name="pgfId-892912" id="pgfId-892912"></a>Description of
        Function:</p>

        <p class="CellBody"><a name="pgfId-892913" id="pgfId-892913"></a> The geometry
        command is used to set the size and position of the VCS canvas.</p>
      </td>

      <td rowspan="1" colspan="1">
        <p class="CellBody"><a name="pgfId-892915" id="pgfId-892915"></a>(w,h,x,y), where
        w=width, h=height, x=x_position, y=y_position</p>
      </td>

      <td rowspan="1" colspan="1">
        <p class="CellBody"><a name="pgfId-892917" id="pgfId-892917"></a>Example of
        Use:</p>

        <pre style="word-break:normal;">a=vcs.init()
a.plot(array,'default','isofill','quick')
a.geometry(450, 337,100, 100)
</pre></td>
    </tr>

    <tr>
      <td rowspan="1" colspan="4">
        <p class="CellHeading"><a name="pgfId-892922" id="pgfId-892922"></a>Printing and
        Saving Graphics</p>
      </td>
    </tr>

    <tr>
      <td rowspan="1" colspan="1">
        <code class=""><a name="pgfId-892930" id="pgfId-892930"></a><a name="marker-910422" id="marker-910422"></a>printer</code>
      </td>

      <td rowspan="1" colspan="1">
        <p class="CellBody"><a name="pgfId-892932" id="pgfId-892932"></a>Function:
        printer<br/>
        # Send plots to the printer</p>

        <p class="CellBody"><a name="pgfId-892933" id="pgfId-892933"></a></p>

        <p class="CellBody"><a name="pgfId-892934" id="pgfId-892934"></a>Description of
        Function:</p>

        <p class="CellBody"><a name="pgfId-892935" id="pgfId-892935"></a> This function
        creates a temporary cgm file and then sends it to the specified printer. Once the
        printer received the information, then the temporary cgm file is deleted. The
        temporary cgm file is created in the user's PCMDI_GRAPHICS directory.</p>

        <p class="CellBody"><a name="pgfId-892936" id="pgfId-892936"></a> The PRINTER
        command is used to send the VCS Canvas plot(s) directly to the printer.</p>

        <p class="CellBody"><a name="pgfId-892937" id="pgfId-892937"></a> Note: VCS
        graphical displays can be printed only if the user customizes a HARD_COPY file
        (included with the VCS software) for the home system. The path to the HARD_COPY
        file must be:</p>

        <p class="CellBody"><a name="pgfId-892938" id="pgfId-892938"></a>
        /$HOME/PCMDI_GRAPHICS/HARD_COPY</p>

        <p class="CellBody"><a name="pgfId-892939" id="pgfId-892939"></a> where /$HOME
        denotes the user's home directory.</p>

        <p class="CellBody"><a name="pgfId-892940" id="pgfId-892940"></a> For more
        information on the HARD_COPY file, see URL:</p>

        <p class="CellBody"><a name="pgfId-892941" id="pgfId-892941"></a></p>

        <p class="CellBody"><a name="pgfId-892942" id="pgfId-892942"></a>
        http://www-pcmdi.llnl.gov/software/vcs/vcs_guidetoc.html<br/>
        #1.Setup</p>
      </td>

      <td rowspan="1" colspan="1">
        <p class="CellBody"><a name="pgfId-892944" id="pgfId-892944"></a>printer's
        name</p>

        <p class="CellBody"><a name="pgfId-892945" id="pgfId-892945"></a></p>

        <p class="CellBody"><a name="pgfId-892946" id="pgfId-892946"></a>l|p -</p>

        <p class="CellBody"><a name="pgfId-892947" id="pgfId-892947"></a>Orientation can
        be either: 'l' = landscape, or 'p' = portrait.</p>
      </td>

      <td rowspan="1" colspan="1">
        <p class="CellBody"><a name="pgfId-892949" id="pgfId-892949"></a>Example of
        Use:</p>

        <pre style="word-break:normal;">import vcs
a=vcs.init()
a.plot(array)
a.printer('printer_name')
# Send plot(s) to postscript printer
a.printer(`printer_name','p')
# Send plot(s) to the printer in portrait mode
</pre></td>
    </tr>

    <tr>
      <td rowspan="1" colspan="1">
        <code class=""><a name="pgfId-892955" id="pgfId-892955"></a><a name="marker-910423" id="marker-910423"></a>gif</code>
      </td>

      <td rowspan="1" colspan="1">
        <p class="CellBody"><a name="pgfId-892957" id="pgfId-892957"></a>Function:
        gif<br/>
        # Save plot(s) as gif image</p>

        <p class="CellBody"><a name="pgfId-892958" id="pgfId-892958"></a></p>

        <p class="CellBody"><a name="pgfId-892959" id="pgfId-892959"></a>Description of
        Function:</p>

        <p class="CellBody"><a name="pgfId-892960" id="pgfId-892960"></a> In some cases,
        the user may want to save the plot out as a gif image. This routine allows the
        user to save the VCS canvas output as a gif file.</p>

        <p class="CellBody"><a name="pgfId-892961" id="pgfId-892961"></a> This file can
        be converted to other gif formats with the aid of xv and other such imaging tools
        found freely on the web.</p>

        <p class="CellBody"><a name="pgfId-892962" id="pgfId-892962"></a> If no path/file
        name is given and no previously created gif file has been</p>

        <p class="CellBody"><a name="pgfId-892963" id="pgfId-892963"></a>designated, then
        file</p>

        <p class="CellBody"><a name="pgfId-892964" id="pgfId-892964"></a>
        /$HOME/PCMDI_GRAPHICS/default.gif</p>

        <p class="CellBody"><a name="pgfId-892965" id="pgfId-892965"></a> will be used
        for storing gif images. However, if a previously created gif file is designated,
        that file will be used for gif output.</p>

        <p class="CellBody"><a name="pgfId-892966" id="pgfId-892966"></a> By default, the
        page orientation is in Landscape mode (l). To translate the page orientation to
        portrait mode (p), enter 'p' as the second parameter.</p>

        <p class="CellBody"><a name="pgfId-892967" id="pgfId-892967"></a> The GIF command
        is used to create or append to a gif file. There are two modes for saving a gif
        file: `Append' mode (a) appends gif output to an existing gif file(i.e., making
        it an animated gif); `Replace' (r) mode overwrites an existing gif file with new
        gif output.</p>
      </td>

      <td rowspan="1" colspan="1">
        <p class="CellBody"><a name="pgfId-892969" id="pgfId-892969"></a>gif file
        name</p>

        <p class="CellBody"><a name="pgfId-892970" id="pgfId-892970"></a></p>

        <p class="CellBody"><a name="pgfId-892971" id="pgfId-892971"></a>`a'=will append
        (or merge) image to an existing file, making it an animated gif</p>

        <p class="CellBody"><a name="pgfId-892972" id="pgfId-892972"></a>`r'=will replace
        file with new image</p>

        <p class="CellBody"><a name="pgfId-892973" id="pgfId-892973"></a>`l'=landscape
        mode</p>

        <p class="CellBody"><a name="pgfId-892974" id="pgfId-892974"></a>`p'=portrait
        mode</p>
      </td>

      <td rowspan="1" colspan="1">
        <p class="CellBody"><a name="pgfId-892976" id="pgfId-892976"></a>Example of
        Use:</p>

        <pre style="word-break:normal;">import vcs
a=vcs.init()
a.plot(array)
# Note, if you don't specify the extension `.gif' at the end of file name, then the extension `.gif' will be put on for you.
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
</pre></td>
    </tr>

    <tr>
      <td rowspan="1" colspan="1">
        <code class=""><a name="pgfId-892986" id="pgfId-892986"></a><a name="marker-910425" id="marker-910425"></a>postscript</code>
      </td>

      <td rowspan="1" colspan="1">
        <p class="CellBody"><a name="pgfId-892988" id="pgfId-892988"></a>Function:
        postscript<br/>
        # Save plot(s) to a postscript file</p>

        <p class="CellBody"><a name="pgfId-892989" id="pgfId-892989"></a></p>

        <p class="CellBody"><a name="pgfId-892990" id="pgfId-892990"></a>Description of
        Function:</p>

        <p class="CellBody"><a name="pgfId-892991" id="pgfId-892991"></a> Postscript
        output is another form of vector graphics. It is larger than its CGM output
        counter part, because it is not stored out in ASCII format. To save out a
        postscript file, VCS will first create a cgm file in the user's PCMDI_GRAPHICS
        directory. Then it will use gplot to convert the cgm file to a postscript file in
        the location the user has chosen.</p>
      </td>

      <td rowspan="1" colspan="1">
        <p class="CellBody"><a name="pgfId-892993" id="pgfId-892993"></a>postscript file
        name</p>

        <p class="CellBody"><a name="pgfId-892994" id="pgfId-892994"></a></p>

        <p class="CellBody"><a name="pgfId-892995" id="pgfId-892995"></a>`a'=will append
        postscript to an existing file</p>

        <p class="CellBody"><a name="pgfId-892996" id="pgfId-892996"></a>`r'=will replace
        postscript file with new apostscript file</p>
      </td>

      <td rowspan="1" colspan="1">
        <p class="CellBody"><a name="pgfId-892998" id="pgfId-892998"></a>Example of
        Use:</p>

        <pre style="word-break:normal;">import vcs
a=vcs.init()
a.plot(array)
# Note, if you don't specify the extension `.ps' at the end of file name, then the extension `.ps' will be put on for you.
a.postscript('example')
# Creates a landscape postscript file a.postscript('example','p')
# Creates a portrait postscript file
</pre></td>
    </tr>

    <tr>
      <td rowspan="1" colspan="1">
        <code class=""><a name="pgfId-893004" id="pgfId-893004"></a><a name="marker-910426" id="marker-910426"></a>cgm</code>
      </td>

      <td rowspan="1" colspan="1">
        <p class="CellBody"><a name="pgfId-893006" id="pgfId-893006"></a>Function:
        cgm</p>

        <p class="CellBody"><a name="pgfId-893007" id="pgfId-893007"></a></p>

        <p class="CellBody"><a name="pgfId-893008" id="pgfId-893008"></a>Description of
        Function:</p>

        <p class="CellBody"><a name="pgfId-893009" id="pgfId-893009"></a> To save a
        graphics plot in VCS the user can call CGM along with the name of the output.
        This routine will save the displayed image on the VCS canvas as a binary vector
        graphics that can be imported into MSWord or Framemaker. CGM files are in ISO
        standards output format.</p>

        <p class="CellBody"><a name="pgfId-893010" id="pgfId-893010"></a> The CGM command
        is used to create or append to a cgm file. There are two modes for saving a cgm
        file: `Append' mode (a) appends cgm output to an existing cgm file; `Replace' (r)
        mode overwrites an existing cgm file with new cgm output.</p>
      </td>

      <td rowspan="1" colspan="1">
        <p class="CellBody"><a name="pgfId-893012" id="pgfId-893012"></a>cgm file
        name</p>

        <p class="CellBody"><a name="pgfId-893013" id="pgfId-893013"></a></p>

        <p class="CellBody"><a name="pgfId-893014" id="pgfId-893014"></a>`a'=will append
        cgm to an existing file</p>

        <p class="CellBody"><a name="pgfId-893015" id="pgfId-893015"></a>`r'=will replace
        cgm file with a new cgm file</p>
      </td>

      <td rowspan="1" colspan="1">
        <p class="CellBody"><a name="pgfId-893017" id="pgfId-893017"></a>Example of
        Use:</p>

        <pre style="word-break:normal;">a=vcs.init()
a.plot(array,'default','isofill','quick')
# Note, if you don't specify the extension `.cgm' at the end of file name, then the extension `.cgm' will be put on for you.
a.cgm(o)
a.cgm('example')
# by default a cgm file will be appended it an existing file
a.cgm('example','a')
# 'a' will instruct cgm to append to an existing file
a.cgm('example','r')
# 'r' will instruct cgm to over write an existing file
</pre></td>
    </tr>

    <tr>
      <td rowspan="1" colspan="1">
        <code class=""><a name="pgfId-893025" id="pgfId-893025"></a><a name="marker-910427" id="marker-910427"></a>raster</code>
      </td>

      <td rowspan="1" colspan="1">
        <p class="CellBody"><a name="pgfId-893027" id="pgfId-893027"></a>Function:
        raster</p>

        <p class="CellBody"><a name="pgfId-893028" id="pgfId-893028"></a></p>

        <p class="CellBody"><a name="pgfId-893029" id="pgfId-893029"></a>Description of
        Function:</p>

        <p class="CellBody"><a name="pgfId-893030" id="pgfId-893030"></a> In some cases,
        the user may want to save the plot out as an raster image. This routine allows
        the user to save the VCS canvas output as a SUN raster file.</p>

        <p class="CellBody"><a name="pgfId-893031" id="pgfId-893031"></a> This file can
        be converted to other raster formats with the aid of xv and other such imaging
        tools found freely on the web.</p>

        <p class="CellBody"><a name="pgfId-893032" id="pgfId-893032"></a> If no path/file
        name is given and no previously created raster file has beendesignated, then
        file</p>

        <p class="CellBody"><a name="pgfId-893033" id="pgfId-893033"></a>
        /$HOME/PCMDI_GRAPHICS/default.ras</p>

        <p class="CellBody"><a name="pgfId-893034" id="pgfId-893034"></a> will be used
        for storing raster images. However, if a previously created raster file is
        designated, that file will be used for raster output.</p>
      </td>

      <td rowspan="1" colspan="1">
        <p class="CellBody"><a name="pgfId-893036" id="pgfId-893036"></a>raster file
        name</p>

        <p class="CellBody"><a name="pgfId-893037" id="pgfId-893037"></a></p>

        <p class="CellBody"><a name="pgfId-893038" id="pgfId-893038"></a>`a'=will append
        raster image to an existing raster file</p>

        <p class="CellBody"><a name="pgfId-893039" id="pgfId-893039"></a>`r'=will replace
        a raster file with a new raster file</p>

        <p class="CellBody"><a name="pgfId-893040" id="pgfId-893040"></a></p>
      </td>

      <td rowspan="1" colspan="1">
        <p class="CellBody"><a name="pgfId-893042" id="pgfId-893042"></a>Example of
        Use:</p>

        <pre style="word-break:normal;">import vcs
a=vcs.init()
a.plot(array)
# Note, if you don't specify the extension `.ras' at the end of file name, then the extension `.ras' will be put on for you.
a.raster('example','a')
# append raster image to existing file
a.raster('example','r')
# over write existing raster file
</pre></td>
    </tr>

    <tr>
      <td rowspan="1" colspan="1">
        <code class=""><a name="pgfId-899941" id="pgfId-899941"></a><a name="marker-910436" id="marker-910436"></a>pstogif</code>
      </td>

      <td rowspan="1" colspan="1">
        <p class="CellBody"><a name="pgfId-899943" id="pgfId-899943"></a>Function:
        pstogif</p>

        <p class="CellBody"><a name="pgfId-899944" id="pgfId-899944"></a></p>

        <p class="CellBody"><a name="pgfId-899945" id="pgfId-899945"></a>Description of
        Function:</p>

        <p class="CellBody"><a name="pgfId-899946" id="pgfId-899946"></a> This function
        allows the user to convert a postscript file to a gif file.</p>
      </td>

      <td rowspan="1" colspan="1">
        <p class="CellBody"><a name="pgfId-899952" id="pgfId-899952"></a>postscript file
        name</p>

        <p class="CellBody"><a name="pgfId-899954" id="pgfId-899954"></a>[`l'=landscape
        `p'=portrait]</p>
      </td>

      <td rowspan="1" colspan="1">
        <p class="CellBody"><a name="pgfId-900006" id="pgfId-900006"></a>Example of
        Use:</p>

        <pre style="word-break:normal;">import vcs
a=vcs.init()
a.plot(array)
a.pstogif('filename.ps') # convert to landscape gif file
a.pstogif('filename.ps','l') # convert to landscape gif file
a.pstogif('filename.ps','p') # convert to portrait gif file
</pre></td>
    </tr>

    <tr>
      <td rowspan="1" colspan="4">
        <p class="CellHeading"><a name="pgfId-893049" id="pgfId-893049"></a>Plot and
        Clear Commands</p>
      </td>
    </tr>

    <tr>
      <td rowspan="1" colspan="1">
        <code class=""><a name="pgfId-893057" id="pgfId-893057"></a><a name="marker-910437" id="marker-910437"></a>plot</code>
      </td>

      <td rowspan="1" colspan="1">
        <p class="CellBody"><a name="pgfId-893059" id="pgfId-893059"></a>Function:
        plot</p>

        <p class="CellBody"><a name="pgfId-893060" id="pgfId-893060"></a></p>

        <p class="CellBody"><a name="pgfId-893061" id="pgfId-893061"></a>Description of
        Function:</p>

        <p class="CellBody"><a name="pgfId-893062" id="pgfId-893062"></a> Plot an
        array(s) of data given a template and graphics method. The VCS template is used
        to define where the data and variable attributes will be displayed on the VCS
        Canvas. The VCS graphics method is used to define how the array(s) will be shown
        on the VCS Canvas.</p>

        <p class="CellBody"><a name="pgfId-893063" id="pgfId-893063"></a></p>
      </td>

      <td rowspan="1" colspan="1">
        <p class="CellBody"><a name="pgfId-893065" id="pgfId-893065"></a>The form of the
        call is:</p>

        <p class="CellBody"><a name="pgfId-893066" id="pgfId-893066"></a>
        plot(array1=None, array2=None, template_name=None,
        graphics_method=None,graphics_name=None, [key=value [, key=value [, ...]]]) where
        array1 and array2 are NumPy arrays, such that 2&lt;=rank(ar)&lt;=5.</p>

        <p class="CellBody"><a name="pgfId-893067" id="pgfId-893067"></a></p>

        <p class="CellBody"><a name="pgfId-893068" id="pgfId-893068"></a>See section
        4.5.1 for a detail listing of possible plot options.</p>
      </td>

      <td rowspan="1" colspan="1">
        <p class="CellBody"><a name="pgfId-893070" id="pgfId-893070"></a>Example of
        Use:</p>

        <pre style="word-break:normal;">
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
</pre></td>
    </tr>

    <tr>
      <td rowspan="1" colspan="1">
        <code class=""><a name="pgfId-893083" id="pgfId-893083"></a><a name="marker-910438" id="marker-910438"></a>boxfill</code>
      </td>

      <td rowspan="1" colspan="1">
        <p class="CellBody"><a name="pgfId-893085" id="pgfId-893085"></a>Function:
        boxfill<br/>
        # Generate a boxfill plot</p>

        <p class="CellBody"><a name="pgfId-893086" id="pgfId-893086"></a></p>

        <p class="CellBody"><a name="pgfId-893087" id="pgfId-893087"></a>Description of
        Function:</p>

        <p class="CellBody"><a name="pgfId-893088" id="pgfId-893088"></a> Generate a
        boxfill plot given the data, boxfill graphics method, and template. If no boxfill
        class object is given, then the 'default' boxfill graphics method is used.
        Similarly, if no template class object is given, then the 'default' template is
        used.</p>
      </td>

      <td rowspan="1" colspan="1">
        <p class="CellBody"><a name="pgfId-893090" id="pgfId-893090"></a>See plot command
        for options.</p>
      </td>

      <td rowspan="1" colspan="1">
        <p class="CellBody"><a name="pgfId-893092" id="pgfId-893092"></a>Example of
        Use:</p>

        <pre style="word-break:normal;">import vcs
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
</pre></td>
    </tr>

    <tr>
      <td rowspan="1" colspan="1">
        <code class=""><a name="pgfId-893108" id="pgfId-893108"></a><a name="marker-910439" id="marker-910439"></a>continents</code>
      </td>

      <td rowspan="1" colspan="1">
        <p class="CellBody"><a name="pgfId-893110" id="pgfId-893110"></a>Function:
        continents<br/>
        # Generate a continents plot</p>

        <p class="CellBody"><a name="pgfId-893111" id="pgfId-893111"></a></p>

        <p class="CellBody"><a name="pgfId-893112" id="pgfId-893112"></a>Description of
        Function:</p>

        <p class="CellBody"><a name="pgfId-893113" id="pgfId-893113"></a> Generate a
        continents plot given the continents graphics method, and template. If no
        continents class object is given, then the 'default' continents graphics method
        is used. Similarly, if no template class object is given, then the 'default'
        template is used.</p>
      </td>

      <td rowspan="1" colspan="1">
        <p class="CellBody"><a name="pgfId-893115" id="pgfId-893115"></a>See plot command
        for options.</p>
      </td>

      <td rowspan="1" colspan="1">
        <p class="CellBody"><a name="pgfId-893117" id="pgfId-893117"></a>Example of
        Use:</p>

        <pre style="word-break:normal;">import vcs
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
</pre></td>
    </tr>

    <tr>
      <td rowspan="1" colspan="1">
        <code class=""><a name="pgfId-893126" id="pgfId-893126"></a><a name="marker-910440" id="marker-910440"></a>isofill</code>
      </td>

      <td rowspan="1" colspan="1">
        <p class="CellBody"><a name="pgfId-893128" id="pgfId-893128"></a>Function:
        isofill<br/>
        # Generate an isofill plot</p>

        <p class="CellBody"><a name="pgfId-893129" id="pgfId-893129"></a></p>

        <p class="CellBody"><a name="pgfId-893130" id="pgfId-893130"></a>Description of
        Function:</p>

        <p class="CellBody"><a name="pgfId-893131" id="pgfId-893131"></a> Generate a
        isofill plot given the data, isofill graphics method, and template. If no isofill
        class object is given, then the 'default' isofill graphics method is used.
        Similarly, if no template class object is given, then the 'default' template is
        used.</p>
      </td>

      <td rowspan="1" colspan="1">
        <p class="CellBody"><a name="pgfId-893133" id="pgfId-893133"></a>See plot command
        for options.</p>
      </td>

      <td rowspan="1" colspan="1">
        <p class="CellBody"><a name="pgfId-893135" id="pgfId-893135"></a>Example of
        Use:</p>

        <pre style="word-break:normal;">import vcs
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
</pre></td>
    </tr>

    <tr>
      <td rowspan="1" colspan="1">
        <code class=""><a name="pgfId-893144" id="pgfId-893144"></a><a name="marker-910441" id="marker-910441"></a>isoline</code>
      </td>

      <td rowspan="1" colspan="1">
        <p class="CellBody"><a name="pgfId-893146" id="pgfId-893146"></a>Function:
        isoline<br/>
        # Generate an isoline plot</p>

        <p class="CellBody"><a name="pgfId-893147" id="pgfId-893147"></a></p>

        <p class="CellBody"><a name="pgfId-893148" id="pgfId-893148"></a>Description of
        Function:</p>

        <p class="CellBody"><a name="pgfId-893149" id="pgfId-893149"></a> Generate a
        isoline plot given the data, isoline graphics method, and template. If no isoline
        class object is given, then the 'default' isoline graphics method is used.
        Similarly, if no template class object is given, then the 'default' template is
        used.</p>
      </td>

      <td rowspan="1" colspan="1">
        <p class="CellBody"><a name="pgfId-893151" id="pgfId-893151"></a>See plot command
        for options.</p>
      </td>

      <td rowspan="1" colspan="1">
        <p class="CellBody"><a name="pgfId-893153" id="pgfId-893153"></a>Example of
        Use:</p>

        <pre style="word-break:normal;">a=vcs.init()
a.show('isoline')
# Show all the existing isoline graphics methods
iso=a.getisoline('quick')
# Create instance of 'quick'
a.isoline(array,iso)
# Plot array using specified iso and default template
a.clear()
# Clear VCS canvas a.isoline(array,iso,template)
# Plot array using specified iso and template
</pre></td>
    </tr>

    <tr>
      <td rowspan="1" colspan="1">
        <code class=""><a name="pgfId-893160" id="pgfId-893160"></a><a name="marker-910442" id="marker-910442"></a>outfill</code>
      </td>

      <td rowspan="1" colspan="1">
        <p class="CellBody"><a name="pgfId-893162" id="pgfId-893162"></a>Function:
        outfill<br/>
        # Generate an outfill plot</p>

        <p class="CellBody"><a name="pgfId-893163" id="pgfId-893163"></a></p>

        <p class="CellBody"><a name="pgfId-893164" id="pgfId-893164"></a>Description of
        Function:</p>

        <p class="CellBody"><a name="pgfId-893165" id="pgfId-893165"></a> Generate a
        outfill plot given the data, outfill graphics method, and template. If no outfill
        class object is given, then the 'default' outfill graphics method is used.
        Similarly, if no template class object is given, then the 'default' template is
        used.</p>
      </td>

      <td rowspan="1" colspan="1">
        <p class="CellBody"><a name="pgfId-893167" id="pgfId-893167"></a>See plot command
        for options.</p>
      </td>

      <td rowspan="1" colspan="1">
        <p class="CellBody"><a name="pgfId-893169" id="pgfId-893169"></a>Example of
        Use:</p>

        <pre style="word-break:normal;">a=vcs.init()
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
</pre></td>
    </tr>

    <tr>
      <td rowspan="1" colspan="1">
        <code class=""><a name="pgfId-893177" id="pgfId-893177"></a><a name="marker-910443" id="marker-910443"></a>outline</code>
      </td>

      <td rowspan="1" colspan="1">
        <p class="CellBody"><a name="pgfId-893179" id="pgfId-893179"></a>Function:
        outline<br/>
        # Generate an outline plot</p>

        <p class="CellBody"><a name="pgfId-893180" id="pgfId-893180"></a></p>

        <p class="CellBody"><a name="pgfId-893181" id="pgfId-893181"></a>Description of
        Function:</p>

        <p class="CellBody"><a name="pgfId-893182" id="pgfId-893182"></a> Generate a
        outline plot given the data, outline graphics method, and template. If no outline
        class object is given, then the 'default' outline graphics method is used.
        Similarly, if no template class object is given, then the 'default' template is
        used.</p>
      </td>

      <td rowspan="1" colspan="1">
        <p class="CellBody"><a name="pgfId-893184" id="pgfId-893184"></a>See plot command
        for options.</p>
      </td>

      <td rowspan="1" colspan="1">
        <p class="CellBody"><a name="pgfId-893186" id="pgfId-893186"></a>Example of
        Use:</p>

        <pre style="word-break:normal;">import vcs
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
</pre></td>
    </tr>

    <tr>
      <td rowspan="1" colspan="1">
        <code class=""><a name="pgfId-893194" id="pgfId-893194"></a><a name="marker-910444" id="marker-910444"></a>scatter</code>
      </td>

      <td rowspan="1" colspan="1">
        <p class="CellBody"><a name="pgfId-893196" id="pgfId-893196"></a>Function:
        scatter<br/>
        # Generate a scatter plot</p>

        <p class="CellBody"><a name="pgfId-893197" id="pgfId-893197"></a></p>

        <p class="CellBody"><a name="pgfId-893198" id="pgfId-893198"></a>Description of
        Function:</p>

        <p class="CellBody"><a name="pgfId-893199" id="pgfId-893199"></a> Generate a
        scatter plot given the data, scatter graphics method, and template. If no scatter
        class object is given, then the 'default' scatter graphics method is used.
        Similarly, if no template class object is given, then the 'default' template is
        used.</p>
      </td>

      <td rowspan="1" colspan="1">
        <p class="CellBody"><a name="pgfId-893201" id="pgfId-893201"></a>See plot command
        for options.</p>
      </td>

      <td rowspan="1" colspan="1">
        <p class="CellBody"><a name="pgfId-893203" id="pgfId-893203"></a>Example of
        Use:</p>

        <pre style="word-break:normal;">a=vcs.init()
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
</pre></td>
    </tr>

    <tr>
      <td rowspan="1" colspan="1">
        <code class=""><a name="pgfId-893211" id="pgfId-893211"></a><a name="marker-910446" id="marker-910446"></a>vector</code>
      </td>

      <td rowspan="1" colspan="1">
        <p class="CellBody"><a name="pgfId-893213" id="pgfId-893213"></a>Function:
        vector<br/>
        # Generate a vector plot</p>

        <p class="CellBody"><a name="pgfId-893214" id="pgfId-893214"></a></p>

        <p class="CellBody"><a name="pgfId-893215" id="pgfId-893215"></a>Description of
        Function:</p>

        <p class="CellBody"><a name="pgfId-893216" id="pgfId-893216"></a> Generate a
        vector plot given the data, vector graphics method, andtemplate. If no vector
        class object is given, then the 'default' vectorgraphics method is used.
        Similarly, if no template class object is given,then the 'default' template is
        used.</p>
      </td>

      <td rowspan="1" colspan="1">
        <p class="CellBody"><a name="pgfId-893218" id="pgfId-893218"></a>See plot command
        for options.</p>
      </td>

      <td rowspan="1" colspan="1">
        <p class="CellBody"><a name="pgfId-893220" id="pgfId-893220"></a>Example of
        Use:</p>

        <pre style="word-break:normal;">import vcs
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
</pre></td>
    </tr>

    <tr>
      <td rowspan="1" colspan="1">
        <code class=""><a name="pgfId-893229" id="pgfId-893229"></a><a name="marker-910445" id="marker-910445"></a>xvsy</code>
      </td>

      <td rowspan="1" colspan="1">
        <p class="CellBody"><a name="pgfId-893231" id="pgfId-893231"></a>Function:
        xvsy<br/>
        # Generate a Xvsy plot</p>

        <p class="CellBody"><a name="pgfId-893232" id="pgfId-893232"></a></p>

        <p class="CellBody"><a name="pgfId-893233" id="pgfId-893233"></a>Description of
        Function:</p>

        <p class="CellBody"><a name="pgfId-893234" id="pgfId-893234"></a> Generate a XvsY
        plot given the data, XvsY graphics method, and template. If no XvsY class object
        is given, then the 'default' XvsY graphics method is used. Similarly, if no
        template class object is given, then the 'default' template is used.</p>
      </td>

      <td rowspan="1" colspan="1">
        <p class="CellBody"><a name="pgfId-893236" id="pgfId-893236"></a>See plot command
        for options.</p>
      </td>

      <td rowspan="1" colspan="1">
        <p class="CellBody"><a name="pgfId-893238" id="pgfId-893238"></a>Example of
        Use:</p>

        <pre style="word-break:normal;">import vcs
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
</pre></td>
    </tr>

    <tr>
      <td rowspan="1" colspan="1">
        <code class=""><a name="pgfId-893247" id="pgfId-893247"></a><a name="marker-910448" id="marker-910448"></a>xyvsy</code>
      </td>

      <td rowspan="1" colspan="1">
        <p class="CellBody"><a name="pgfId-893249" id="pgfId-893249"></a>Function:
        xyvsy<br/>
        # Generate a Xyvsy plot</p>

        <p class="CellBody"><a name="pgfId-893250" id="pgfId-893250"></a></p>

        <p class="CellBody"><a name="pgfId-893251" id="pgfId-893251"></a>Description of
        Function:</p>

        <p class="CellBody"><a name="pgfId-893252" id="pgfId-893252"></a> Generate a
        Xyvsy plot given the data, Xyvsy graphics method, and template. If no Xyvsy class
        object is given, then the 'default' Xyvsy graphics method is used. Simerly, if no
        template class object is given, then the 'default' template is used.</p>

        <p class="CellBody"><a name="pgfId-893253" id="pgfId-893253"></a></p>
      </td>

      <td rowspan="1" colspan="1">
        <p class="CellBody"><a name="pgfId-893255" id="pgfId-893255"></a>See plot command
        for options.</p>
      </td>

      <td rowspan="1" colspan="1">
        <p class="CellBody"><a name="pgfId-893257" id="pgfId-893257"></a>Example of
        Use:</p>

        <pre style="word-break:normal;">import vcs
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

</pre></td>
    </tr>

    <tr>
      <td rowspan="1" colspan="1">
        <code class=""><a name="pgfId-893267" id="pgfId-893267"></a><a name="marker-910447" id="marker-910447"></a>yxvsx</code>
      </td>

      <td rowspan="1" colspan="1">
        <p class="CellBody"><a name="pgfId-893269" id="pgfId-893269"></a>Function:
        yxvsx<br/>
        # Generate a Yxvsx plot</p>

        <p class="CellBody"><a name="pgfId-893270" id="pgfId-893270"></a></p>

        <p class="CellBody"><a name="pgfId-893271" id="pgfId-893271"></a>Description of
        Function:</p>

        <p class="CellBody"><a name="pgfId-893272" id="pgfId-893272"></a> Generate a
        Yxvsx plot given the data, Yxvsx graphics method, and template. If no Yxvsx class
        object is given, then the 'default' Yxvsx graphics method is used. Simerly, if no
        template class object is given, then the 'default' template is used.</p>
      </td>

      <td rowspan="1" colspan="1">
        <p class="CellBody"><a name="pgfId-893274" id="pgfId-893274"></a>See plot command
        for options.</p>
      </td>

      <td rowspan="1" colspan="1">
        <p class="CellBody"><a name="pgfId-893276" id="pgfId-893276"></a>Example of
        Use:</p>

        <pre style="word-break:normal;">import vcs
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
</pre></td>
    </tr>

    <tr>
      <td rowspan="1" colspan="1">
        <code class=""><a name="pgfId-893285" id="pgfId-893285"></a><a name="marker-910449" id="marker-910449"></a>clear</code>
      </td>

      <td rowspan="1" colspan="1">
        <p class="CellBody"><a name="pgfId-893287" id="pgfId-893287"></a>Function:
        clear<br/>
        # Generate a Yxvsx plot</p>

        <p class="CellBody"><a name="pgfId-893288" id="pgfId-893288"></a></p>

        <p class="CellBody"><a name="pgfId-893289" id="pgfId-893289"></a>Description of
        Function:</p>

        <p class="CellBody"><a name="pgfId-893290" id="pgfId-893290"></a> At some point
        it will become necessary to clear all the plots from the VCS Canvas. This routine
        will remove all plots on the VCS Canvas.</p>
      </td>

      <td rowspan="1" colspan="1">
        <p class="CellBody"><a name="pgfId-893292" id="pgfId-893292"></a></p>
      </td>

      <td rowspan="1" colspan="1">
        <p class="CellBody"><a name="pgfId-893294" id="pgfId-893294"></a>Example of
        Use:</p>

        <pre style="word-break:normal;">import vcs
a=vcs.init()
a.plot(array,'default','isofill','quick')
a.clear()
</pre></td>
    </tr>

    <tr>
      <td rowspan="1" colspan="4">
        <p class="CellHeading"><a name="pgfId-893300" id="pgfId-893300"></a>Query
        Functions</p>
      </td>
    </tr>

    <tr>
      <td rowspan="1" colspan="1">
        <code class=""><a name="pgfId-893308" id="pgfId-893308"></a><a name="marker-910450" id="marker-910450"></a>graphicsmethodname</code>
      </td>

      <td rowspan="1" colspan="1">
        <p class="CellBody"><a name="pgfId-893310" id="pgfId-893310"></a>Function:
        graphicsmethodname</p>

        <p class="CellBody"><a name="pgfId-893311" id="pgfId-893311"></a></p>

        <p class="CellBody"><a name="pgfId-893312" id="pgfId-893312"></a>Description of
        Function:</p>

        <p class="CellBody"><a name="pgfId-893313" id="pgfId-893313"></a> Returns the
        grapics method's type string: boxfill, isofill, isoline, outfill, outline,
        continents, scatter, vector, xvsy, xyvsy, or yxvsx.</p>
      </td>

      <td rowspan="1" colspan="1">
        <p class="CellBody"><a name="pgfId-893317" id="pgfId-893317"></a></p>
      </td>

      <td rowspan="1" colspan="1">
        <p class="CellBody"><a name="pgfId-893319" id="pgfId-893319"></a>Example of
        Use:</p>

        <pre style="word-break:normal;">import vcs
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
</pre></td>
    </tr>

    <tr>
      <td rowspan="1" colspan="1">
        <code class=""><a name="pgfId-900166" id="pgfId-900166"></a><a name="marker-910451" id="marker-910451"></a>getcontinentstype</code>
      </td>

      <td rowspan="1" colspan="1">
        <p class="CellBody"><a name="pgfId-900168" id="pgfId-900168"></a>Function:
        getcontinentstype</p>

        <p class="CellBody"><a name="pgfId-900169" id="pgfId-900169"></a></p>

        <p class="CellBody"><a name="pgfId-900170" id="pgfId-900170"></a>Description of
        Function:</p>

        <p class="CellBody"><a name="pgfId-900171" id="pgfId-900171"></a> Return
        continents type from VCS. Remember the value can only be between 0 and 11.</p>
      </td>

      <td rowspan="1" colspan="1">
        <p class="CellBody"><a name="pgfId-900173" id="pgfId-900173"></a></p>
      </td>

      <td rowspan="1" colspan="1">
        <p class="CellBody"><a name="pgfId-900175" id="pgfId-900175"></a>Example of
        Use:</p>

        <pre style="word-break:normal;">import vcs
a=vcs.init()
cont_type = a.getcontinentstype() # Get the
# continents type
</pre></td>
    </tr>

    <tr>
      <td rowspan="1" colspan="1">
        <code class=""><a name="pgfId-900055" id="pgfId-900055"></a><a name="marker-910452" id="marker-910452"></a>isgraphicsmethod</code>
      </td>

      <td rowspan="1" colspan="1">
        <p class="CellBody"><a name="pgfId-900057" id="pgfId-900057"></a>Function:
        isgraphicsmethod</p>

        <p class="CellBody"><a name="pgfId-900058" id="pgfId-900058"></a></p>

        <p class="CellBody"><a name="pgfId-900059" id="pgfId-900059"></a>Description of
        Function:</p>

        <p class="CellBody"><a name="pgfId-900060" id="pgfId-900060"></a> Indicates if
        the entered argument is one of the following graphics methods: boxfill, isofill,
        isoline, outfill, outline, continents, scatter, vector, xvsy, xyvsy, yxvsx.</p>

        <p class="CellBody"><a name="pgfId-900061" id="pgfId-900061"></a> Returns a 1,
        which indicates true, if the argment is one of the above.</p>

        <p class="CellBody"><a name="pgfId-900062" id="pgfId-900062"></a> Otherwise, it
        will return a 0, indicating false.</p>
      </td>

      <td rowspan="1" colspan="1">
        <p class="CellBody"><a name="pgfId-900064" id="pgfId-900064"></a></p>
      </td>

      <td rowspan="1" colspan="1">
        <p class="CellBody"><a name="pgfId-900066" id="pgfId-900066"></a>Example of
        Use:</p>

        <pre style="word-break:normal;">import vcs
a=vcs.init()
box=a.getboxfill('quick')
# To Modify an existing boxfill use:
...
if a.isgraphicsmethod(box):
box.list()
</pre></td>
    </tr>

    <tr>
      <td rowspan="1" colspan="1">
        <code class=""><a name="pgfId-893327" id="pgfId-893327"></a><a name="marker-910453" id="marker-910453"></a>isboxfill</code>
      </td>

      <td rowspan="1" colspan="1">
        <p class="CellBody"><a name="pgfId-893329" id="pgfId-893329"></a>Function:
        isboxfill</p>

        <p class="CellBody"><a name="pgfId-893330" id="pgfId-893330"></a></p>

        <p class="CellBody"><a name="pgfId-893331" id="pgfId-893331"></a>Description of
        Function:</p>

        <p class="CellBody"><a name="pgfId-893332" id="pgfId-893332"></a> Check to see if
        an object is a VCS primary boxfill graphics method object.</p>

        <p class="CellBody"><a name="pgfId-893333" id="pgfId-893333"></a> Returns a 1 if
        the argment true.</p>

        <p class="CellBody"><a name="pgfId-893334" id="pgfId-893334"></a> Otherwise, it
        will return a 0, indicating false.</p>
      </td>

      <td rowspan="1" colspan="1">
        <p class="CellBody"><a name="pgfId-893336" id="pgfId-893336"></a></p>
      </td>

      <td rowspan="1" colspan="1">
        <p class="CellBody"><a name="pgfId-893338" id="pgfId-893338"></a>Example of
        Use:</p>

        <pre style="word-break:normal;">import vcs
a=vcs.init()
box=a.getboxfill("quick")
# To Modify an existing boxfill object
...
if a.isboxfill(box):
box.list()
</pre></td>
    </tr>

    <tr>
      <td rowspan="1" colspan="1">
        <code class=""><a name="pgfId-893346" id="pgfId-893346"></a><a name="marker-910454" id="marker-910454"></a>iscontinents</code>
      </td>

      <td rowspan="1" colspan="1">
        <p class="CellBody"><a name="pgfId-893348" id="pgfId-893348"></a>Function:
        iscontinents</p>

        <p class="CellBody"><a name="pgfId-893349" id="pgfId-893349"></a></p>

        <p class="CellBody"><a name="pgfId-893350" id="pgfId-893350"></a>Description of
        Function:</p>

        <p class="CellBody"><a name="pgfId-893351" id="pgfId-893351"></a> Check to see if
        an object is a VCS primary continents graphics method.</p>

        <p class="CellBody"><a name="pgfId-893352" id="pgfId-893352"></a> Returns a 1 if
        the argment true.</p>

        <p class="CellBody"><a name="pgfId-893353" id="pgfId-893353"></a> Otherwise, it
        will return a 0, indicating false.</p>
      </td>

      <td rowspan="1" colspan="1">
        <p class="CellBody"><a name="pgfId-893355" id="pgfId-893355"></a></p>
      </td>

      <td rowspan="1" colspan="1">
        <p class="CellBody"><a name="pgfId-893357" id="pgfId-893357"></a>Example of
        Use:</p>

        <pre style="word-break:normal;">import vcs
a=vcs.init()
con=a.getcontinents("quick")
# To Modify an existing continents object
...
if a.iscontinents(con):
con.list()

</pre></td>
    </tr>

    <tr>
      <td rowspan="1" colspan="1">
        <code class=""><a name="pgfId-893366" id="pgfId-893366"></a><a name="marker-910455" id="marker-910455"></a>isisofill</code>
      </td>

      <td rowspan="1" colspan="1">
        <p class="CellBody"><a name="pgfId-893368" id="pgfId-893368"></a>Function:
        isisofill</p>

        <p class="CellBody"><a name="pgfId-893369" id="pgfId-893369"></a></p>

        <p class="CellBody"><a name="pgfId-893370" id="pgfId-893370"></a>Description of
        Function:</p>

        <p class="CellBody"><a name="pgfId-893371" id="pgfId-893371"></a> Check to see if
        an object is a VCS primary isofill graphics method.</p>

        <p class="CellBody"><a name="pgfId-893372" id="pgfId-893372"></a> Returns a 1 if
        the argment true.</p>

        <p class="CellBody"><a name="pgfId-893373" id="pgfId-893373"></a> Otherwise, it
        will return a 0, indicating false.</p>
      </td>

      <td rowspan="1" colspan="1">
        <p class="CellBody"><a name="pgfId-893375" id="pgfId-893375"></a></p>
      </td>

      <td rowspan="1" colspan="1">
        <p class="CellBody"><a name="pgfId-893377" id="pgfId-893377"></a>Example of
        Use:</p>

        <pre style="word-break:normal;">import vcs
a=vcs.init()
iso=a.getisofill("quick")
# To Modify an existing isofill object
...
if a.isisofill(iso):
iso.list()
</pre></td>
    </tr>

    <tr>
      <td rowspan="1" colspan="1">
        <code class=""><a name="pgfId-893385" id="pgfId-893385"></a><a name="marker-910456" id="marker-910456"></a>isisoline</code>
      </td>

      <td rowspan="1" colspan="1">
        <p class="CellBody"><a name="pgfId-893387" id="pgfId-893387"></a>Function:
        isisoline</p>

        <p class="CellBody"><a name="pgfId-893388" id="pgfId-893388"></a></p>

        <p class="CellBody"><a name="pgfId-893389" id="pgfId-893389"></a>Description of
        Function:</p>

        <p class="CellBody"><a name="pgfId-893390" id="pgfId-893390"></a> Check to see if
        an object is a VCS primary isoline graphics method.</p>

        <p class="CellBody"><a name="pgfId-893391" id="pgfId-893391"></a> Returns a 1 if
        the argment true.</p>

        <p class="CellBody"><a name="pgfId-893392" id="pgfId-893392"></a> Otherwise, it
        will return a 0, indicating false.</p>
      </td>

      <td rowspan="1" colspan="1">
        <p class="CellBody"><a name="pgfId-893394" id="pgfId-893394"></a></p>
      </td>

      <td rowspan="1" colspan="1">
        <p class="CellBody"><a name="pgfId-893396" id="pgfId-893396"></a>Example of
        Use:</p>

        <pre style="word-break:normal;">import vcs
a=vcs.init()
iso=a.getisoline("quick")
# To Modify an existing isoline object
...
if a.isisoline(iso):
iso.list()
</pre></td>
    </tr>

    <tr>
      <td rowspan="1" colspan="1">
        <code class=""><a name="pgfId-893404" id="pgfId-893404"></a><a name="marker-910457" id="marker-910457"></a>isoutfill</code>
      </td>

      <td rowspan="1" colspan="1">
        <p class="CellBody"><a name="pgfId-893406" id="pgfId-893406"></a>Function:
        isoutfill</p>

        <p class="CellBody"><a name="pgfId-893407" id="pgfId-893407"></a></p>

        <p class="CellBody"><a name="pgfId-893408" id="pgfId-893408"></a>Description of
        Function:</p>

        <p class="CellBody"><a name="pgfId-893409" id="pgfId-893409"></a> Check to see if
        this object is a VCS primary outfill graphics method.</p>

        <p class="CellBody"><a name="pgfId-893410" id="pgfId-893410"></a> Returns a 1 if
        the argment true.</p>

        <p class="CellBody"><a name="pgfId-893411" id="pgfId-893411"></a> Otherwise, it
        will return a 0, indicating false.</p>
      </td>

      <td rowspan="1" colspan="1">
        <p class="CellBody"><a name="pgfId-893413" id="pgfId-893413"></a></p>
      </td>

      <td rowspan="1" colspan="1">
        <p class="CellBody"><a name="pgfId-893415" id="pgfId-893415"></a>Example of
        Use:</p>

        <pre style="word-break:normal;">import vcs
a=vcs.init()
out=a.getoutfill("quick")
# To Modify an existing outfill object
...

if a.isoutfill(out):
out.list()

</pre></td>
    </tr>

    <tr>
      <td rowspan="1" colspan="1">
        <code class=""><a name="pgfId-893425" id="pgfId-893425"></a><a name="marker-910458" id="marker-910458"></a>isoutline</code>
      </td>

      <td rowspan="1" colspan="1">
        <p class="CellBody"><a name="pgfId-893427" id="pgfId-893427"></a>Function:
        isoutline</p>

        <p class="CellBody"><a name="pgfId-893428" id="pgfId-893428"></a></p>

        <p class="CellBody"><a name="pgfId-893429" id="pgfId-893429"></a>Description of
        Function:</p>

        <p class="CellBody"><a name="pgfId-893430" id="pgfId-893430"></a> Check to see if
        an object is a VCS primary outline graphics method.</p>

        <p class="CellBody"><a name="pgfId-893431" id="pgfId-893431"></a> Returns a 1 if
        the argment true.</p>

        <p class="CellBody"><a name="pgfId-893432" id="pgfId-893432"></a> Otherwise, it
        will return a 0, indicating false.</p>
      </td>

      <td rowspan="1" colspan="1">
        <p class="CellBody"><a name="pgfId-893434" id="pgfId-893434"></a></p>
      </td>

      <td rowspan="1" colspan="1">
        <p class="CellBody"><a name="pgfId-893436" id="pgfId-893436"></a>Example of
        Use:</p>

        <pre style="word-break:normal;">import vcs
a=vcs.init()
out=a.getoutline("quick")
# To Modify an existing outline object
...
if a.isoutline(out):
out.list()
</pre></td>
    </tr>

    <tr>
      <td rowspan="1" colspan="1">
        <code class=""><a name="pgfId-893444" id="pgfId-893444"></a><a name="marker-910459" id="marker-910459"></a>isvector</code>
      </td>

      <td rowspan="1" colspan="1">
        <p class="CellBody"><a name="pgfId-893446" id="pgfId-893446"></a>Function:
        isvector</p>

        <p class="CellBody"><a name="pgfId-893447" id="pgfId-893447"></a></p>

        <p class="CellBody"><a name="pgfId-893448" id="pgfId-893448"></a>Description of
        Function:</p>

        <p class="CellBody"><a name="pgfId-893449" id="pgfId-893449"></a> Check to see if
        an object is a VCS primary vector graphics method.</p>

        <p class="CellBody"><a name="pgfId-893450" id="pgfId-893450"></a> Returns a 1 if
        the argment true.</p>

        <p class="CellBody"><a name="pgfId-893451" id="pgfId-893451"></a> Otherwise, it
        will return a 0, indicating false.</p>
      </td>

      <td rowspan="1" colspan="1">
        <p class="CellBody"><a name="pgfId-893453" id="pgfId-893453"></a></p>
      </td>

      <td rowspan="1" colspan="1">
        <p class="CellBody"><a name="pgfId-893455" id="pgfId-893455"></a>Example of
        Use:</p>

        <pre style="word-break:normal;">import vcs
a=vcs.init()
vec=a.getvector("quick")
# To Modify an existing vector object
...
if a.isvector(vec):
vec.list()
</pre></td>
    </tr>

    <tr>
      <td rowspan="1" colspan="1">
        <code class=""><a name="pgfId-893463" id="pgfId-893463"></a><a name="marker-910460" id="marker-910460"></a>isxvsy</code>
      </td>

      <td rowspan="1" colspan="1">
        <p class="CellBody"><a name="pgfId-893465" id="pgfId-893465"></a>Function:
        isxvsy</p>

        <p class="CellBody"><a name="pgfId-893466" id="pgfId-893466"></a></p>

        <p class="CellBody"><a name="pgfId-893467" id="pgfId-893467"></a>Description of
        Function:</p>

        <p class="CellBody"><a name="pgfId-893468" id="pgfId-893468"></a> Check to see if
        an object is a VCS primary xvsy graphics method.</p>

        <p class="CellBody"><a name="pgfId-893469" id="pgfId-893469"></a> Returns a 1 if
        the argment true.</p>

        <p class="CellBody"><a name="pgfId-893470" id="pgfId-893470"></a> Otherwise, it
        will return a 0, indicating false.</p>
      </td>

      <td rowspan="1" colspan="1">
        <p class="CellBody"><a name="pgfId-893472" id="pgfId-893472"></a></p>
      </td>

      <td rowspan="1" colspan="1">
        <p class="CellBody"><a name="pgfId-893474" id="pgfId-893474"></a>Example of
        Use:</p>

        <pre style="word-break:normal;">import vcs
a=vcs.init()
xy=a.getxvsy("quick")
# To Modify an existing xvsy object
...
if a.isxvsy(xy):
xy.list()
</pre></td>
    </tr>

    <tr>
      <td rowspan="1" colspan="1">
        <code class=""><a name="pgfId-893482" id="pgfId-893482"></a><a name="marker-910461" id="marker-910461"></a>isxyvsy</code>
      </td>

      <td rowspan="1" colspan="1">
        <p class="CellBody"><a name="pgfId-893484" id="pgfId-893484"></a>Function:
        isxyvsy</p>

        <p class="CellBody"><a name="pgfId-893485" id="pgfId-893485"></a></p>

        <p class="CellBody"><a name="pgfId-893486" id="pgfId-893486"></a>Description of
        Function:</p>

        <p class="CellBody"><a name="pgfId-893487" id="pgfId-893487"></a> Check to see if
        an object is a VCS primary Xyvsy graphics method.</p>

        <p class="CellBody"><a name="pgfId-893488" id="pgfId-893488"></a> Returns a 1 if
        the argment true.</p>

        <p class="CellBody"><a name="pgfId-893489" id="pgfId-893489"></a> Otherwise, it
        will return a 0, indicating false.</p>
      </td>

      <td rowspan="1" colspan="1">
        <p class="CellBody"><a name="pgfId-893491" id="pgfId-893491"></a></p>
      </td>

      <td rowspan="1" colspan="1">
        <p class="CellBody"><a name="pgfId-893493" id="pgfId-893493"></a>Example of
        Use:</p>

        <pre style="word-break:normal;">import vcs
a=vcs.init()
xyy=a.getxyvsy("quick")
# To Modify an existing Xyvsy object
...
if a.isxyvsy(xyy):
xyy.list()
</pre></td>
    </tr>

    <tr>
      <td rowspan="1" colspan="1">
        <code class=""><a name="pgfId-893501" id="pgfId-893501"></a><a name="marker-910462" id="marker-910462"></a>isyxvsx</code>
      </td>

      <td rowspan="1" colspan="1">
        <p class="CellBody"><a name="pgfId-893503" id="pgfId-893503"></a>Function:
        isyxvsx</p>

        <p class="CellBody"><a name="pgfId-893504" id="pgfId-893504"></a></p>

        <p class="CellBody"><a name="pgfId-893505" id="pgfId-893505"></a>Description of
        Function:</p>

        <p class="CellBody"><a name="pgfId-893506" id="pgfId-893506"></a> Check to see if
        an object is a VCS primary yxvsx graphics method.</p>

        <p class="CellBody"><a name="pgfId-893507" id="pgfId-893507"></a> Returns a 1 if
        the argment true.</p>

        <p class="CellBody"><a name="pgfId-893508" id="pgfId-893508"></a> Otherwise, it
        will return a 0, indicating false.</p>
      </td>

      <td rowspan="1" colspan="1">
        <p class="CellBody"><a name="pgfId-893510" id="pgfId-893510"></a></p>
      </td>

      <td rowspan="1" colspan="1">
        <p class="CellBody"><a name="pgfId-893512" id="pgfId-893512"></a>Example of
        Use:</p>

        <pre style="word-break:normal;">a=vcs.init()
yxx=a.getyxvsx("quick")
# To Modify an existing yxvsx object
...
if a.isyxvsx(yxx):
yxx.list()
</pre></td>
    </tr>

    <tr>
      <td rowspan="1" colspan="1">
        <code class=""><a name="pgfId-893519" id="pgfId-893519"></a><a name="marker-910463" id="marker-910463"></a>istemplate</code>
      </td>

      <td rowspan="1" colspan="1">
        <p class="CellBody"><a name="pgfId-893521" id="pgfId-893521"></a>Function:
        istemplate</p>

        <p class="CellBody"><a name="pgfId-893522" id="pgfId-893522"></a></p>

        <p class="CellBody"><a name="pgfId-893523" id="pgfId-893523"></a>Description of
        Function:</p>

        <p class="CellBody"><a name="pgfId-893524" id="pgfId-893524"></a> Indicates if
        the entered argument a template.</p>

        <p class="CellBody"><a name="pgfId-893525" id="pgfId-893525"></a> Returns a 1 if
        the argment true.</p>

        <p class="CellBody"><a name="pgfId-893526" id="pgfId-893526"></a> Otherwise, it
        will return a 0, indicating false.</p>
      </td>

      <td rowspan="1" colspan="1">
        <p class="CellBody"><a name="pgfId-893528" id="pgfId-893528"></a></p>
      </td>

      <td rowspan="1" colspan="1">
        <p class="CellBody"><a name="pgfId-893530" id="pgfId-893530"></a>Example of
        Use:</p>

        <pre style="word-break:normal;">a=vcs.init()
templt=a.gettemplate('quick')
# Modify an existing template named 'quick'
...
if a.istemplate(templt):
templt.list()
# If it is a template then list its members
</pre></td>
    </tr>

    <tr>
      <td rowspan="1" colspan="1">
        <code class=""><a name="pgfId-893537" id="pgfId-893537"></a><a name="marker-910464" id="marker-910464"></a>issecondaryobject</code>
      </td>

      <td rowspan="1" colspan="1">
        <p class="CellBody"><a name="pgfId-893539" id="pgfId-893539"></a>Function:
        issecondaryobject</p>

        <p class="CellBody"><a name="pgfId-893540" id="pgfId-893540"></a></p>

        <p class="CellBody"><a name="pgfId-893541" id="pgfId-893541"></a>Description of
        Function:</p>

        <p class="CellBody"><a name="pgfId-893542" id="pgfId-893542"></a> In addition,
        detailed specification of the primary elements' (or primary class elements'),
        attributes is provided by eight secondary elements or (secondary class
        elements):</p>

        <p class="CellBody"><a name="pgfId-893543" id="pgfId-893543"></a> 1.) colormap:
        specification of combinations of 256 available colors</p>

        <p class="CellBody"><a name="pgfId-893544" id="pgfId-893544"></a> 2.) fill area:
        style, style index, and color index</p>

        <p class="CellBody"><a name="pgfId-893545" id="pgfId-893545"></a> 3.) format:
        specifications for converting numbers to display strings</p>

        <p class="CellBody"><a name="pgfId-893546" id="pgfId-893546"></a> 4.) line: line
        type, width, and color index</p>

        <p class="CellBody"><a name="pgfId-893547" id="pgfId-893547"></a> 5.) list: a
        sequence of pairs of numerical and character values</p>

        <p class="CellBody"><a name="pgfId-893548" id="pgfId-893548"></a> 6.) marker:
        marker type, size, and color index</p>

        <p class="CellBody"><a name="pgfId-893549" id="pgfId-893549"></a> 7.) text table:
        text font type, character spacing, expansion, and color index</p>

        <p class="CellBody"><a name="pgfId-893550" id="pgfId-893550"></a> 8.) text
        orientation: character height, angle, path, and horizontal/vertical alignment</p>
      </td>

      <td rowspan="1" colspan="1">
        <p class="CellBody"><a name="pgfId-893552" id="pgfId-893552"></a></p>
      </td>

      <td rowspan="1" colspan="1">
        <p class="CellBody"><a name="pgfId-893554" id="pgfId-893554"></a>Example of
        Use:</p>

        <pre style="word-break:normal;">a=vcs.init()
line=a.getline('red')
# To Modify an existing line object
...
if a.issecondaryobject(line):
box.list()
</pre></td>
    </tr>

    <tr>
      <td rowspan="1" colspan="1">
        <code class=""><a name="pgfId-893561" id="pgfId-893561"></a><a name="marker-910465" id="marker-910465"></a>isfillarea</code>
      </td>

      <td rowspan="1" colspan="1">
        <p class="CellBody"><a name="pgfId-893563" id="pgfId-893563"></a>Function:
        isfillarea</p>

        <p class="CellBody"><a name="pgfId-893564" id="pgfId-893564"></a></p>

        <p class="CellBody"><a name="pgfId-893565" id="pgfId-893565"></a>Description of
        Function:</p>

        <p class="CellBody"><a name="pgfId-893566" id="pgfId-893566"></a> Check to see if
        an object is a VCS secondary fillarea.</p>
      </td>

      <td rowspan="1" colspan="1">
        <p class="CellBody"><a name="pgfId-893568" id="pgfId-893568"></a></p>
      </td>

      <td rowspan="1" colspan="1">
        <p class="CellBody"><a name="pgfId-893570" id="pgfId-893570"></a>Example of
        Use:</p>

        <pre style="word-break:normal;">a=vcs.init()
fa=a.getfillarea("def37")
# To Modify an existing fillarea object
...
if a.isfillarea(fa):
fa.list()
</pre></td>
    </tr>

    <tr>
      <td rowspan="1" colspan="1">
        <code class=""><a name="pgfId-893577" id="pgfId-893577"></a><a name="marker-910466" id="marker-910466"></a>isline</code>
      </td>

      <td rowspan="1" colspan="1">
        <p class="CellBody"><a name="pgfId-893579" id="pgfId-893579"></a>Function:
        isline</p>

        <p class="CellBody"><a name="pgfId-893580" id="pgfId-893580"></a></p>

        <p class="CellBody"><a name="pgfId-893581" id="pgfId-893581"></a>Description of
        Function:</p>

        <p class="CellBody"><a name="pgfId-893582" id="pgfId-893582"></a> Check to see if
        this object is a VCS secondary line.</p>
      </td>

      <td rowspan="1" colspan="1">
        <p class="CellBody"><a name="pgfId-893584" id="pgfId-893584"></a></p>
      </td>

      <td rowspan="1" colspan="1">
        <p class="CellBody"><a name="pgfId-893586" id="pgfId-893586"></a>Example of
        Use:</p>

        <pre style="word-break:normal;">a=vcs.init()
ln=a.getline("red")
# To Modify an existing line object
...
if a.isline(ln):
ln.list()
</pre></td>
    </tr>

    <tr>
      <td rowspan="1" colspan="1">
        <code class=""><a name="pgfId-893593" id="pgfId-893593"></a><a name="marker-910467" id="marker-910467"></a>ismarker</code>
      </td>

      <td rowspan="1" colspan="1">
        <p class="CellBody"><a name="pgfId-893595" id="pgfId-893595"></a>Function:
        ismarker</p>

        <p class="CellBody"><a name="pgfId-893596" id="pgfId-893596"></a></p>

        <p class="CellBody"><a name="pgfId-893597" id="pgfId-893597"></a>Description of
        Function:</p>

        <p class="CellBody"><a name="pgfId-893598" id="pgfId-893598"></a> Check to see if
        an object is a VCS secondary marker.</p>
      </td>

      <td rowspan="1" colspan="1">
        <p class="CellBody"><a name="pgfId-893600" id="pgfId-893600"></a></p>
      </td>

      <td rowspan="1" colspan="1">
        <p class="CellBody"><a name="pgfId-893602" id="pgfId-893602"></a>Example of
        Use:</p>

        <pre style="word-break:normal;">a=vcs.init()
mk=a.getmarker("red")
# To Modify an existing marker object
...
if a.ismarker(mk):
mk.list()
</pre></td>
    </tr>

    <tr>
      <td rowspan="1" colspan="1">
        <code class=""><a name="pgfId-893609" id="pgfId-893609"></a><a name="marker-910468" id="marker-910468"></a>istextcombined</code>
      </td>

      <td rowspan="1" colspan="1">
        <p class="CellBody"><a name="pgfId-893611" id="pgfId-893611"></a>Function:
        istextcombined</p>

        <p class="CellBody"><a name="pgfId-893612" id="pgfId-893612"></a></p>

        <p class="CellBody"><a name="pgfId-893613" id="pgfId-893613"></a>Description of
        Function:</p>

        <p class="CellBody"><a name="pgfId-893614" id="pgfId-893614"></a> Check to see if
        an object is a VCS secondary text combined.</p>
      </td>

      <td rowspan="1" colspan="1">
        <p class="CellBody"><a name="pgfId-893616" id="pgfId-893616"></a></p>
      </td>

      <td rowspan="1" colspan="1">
        <p class="CellBody"><a name="pgfId-893618" id="pgfId-893618"></a>Example of
        Use:</p>

        <pre style="word-break:normal;">a=vcs.init()
tc=a.gettextcombined("std", "7left")
# To Modify existing text table and orientation objects
...
if a.istextcombined(tc):
tc.list()
if a.istexttable(tc):
tc.list()
if a.istextorientation(tc):
tc.list()
</pre></td>
    </tr>

    <tr>
      <td rowspan="1" colspan="1">
        <code class=""><a name="pgfId-893629" id="pgfId-893629"></a><a name="marker-910469" id="marker-910469"></a>istextorientation</code>
      </td>

      <td rowspan="1" colspan="1">
        <p class="CellBody"><a name="pgfId-893631" id="pgfId-893631"></a>Function:
        istextorientation</p>

        <p class="CellBody"><a name="pgfId-893632" id="pgfId-893632"></a></p>

        <p class="CellBody"><a name="pgfId-893633" id="pgfId-893633"></a>Description of
        Function:</p>

        <p class="CellBody"><a name="pgfId-893634" id="pgfId-893634"></a> Check to see if
        an object is a VCS secondary text orientation.</p>
      </td>

      <td rowspan="1" colspan="1">
        <p class="CellBody"><a name="pgfId-893636" id="pgfId-893636"></a></p>
      </td>

      <td rowspan="1" colspan="1">
        <p class="CellBody"><a name="pgfId-893638" id="pgfId-893638"></a>Example of
        Use:</p>

        <pre style="word-break:normal;">a=vcs.init()
to=a.gettextorientation("7left")
# To Modify an existing text orientation object
...
if a.istextorientation(to):
to.list()
</pre></td>
    </tr>

    <tr>
      <td rowspan="1" colspan="1">
        <code class=""><a name="pgfId-893645" id="pgfId-893645"></a><a name="marker-910470" id="marker-910470"></a>istexttable</code>
      </td>

      <td rowspan="1" colspan="1">
        <p class="CellBody"><a name="pgfId-893647" id="pgfId-893647"></a>Function:
        istexttable</p>

        <p class="CellBody"><a name="pgfId-893648" id="pgfId-893648"></a></p>

        <p class="CellBody"><a name="pgfId-893649" id="pgfId-893649"></a>Description of
        Function:</p>

        <p class="CellBody"><a name="pgfId-893650" id="pgfId-893650"></a> Check to see if
        an object is a VCS secondary text table.</p>
      </td>

      <td rowspan="1" colspan="1">
        <p class="CellBody"><a name="pgfId-893652" id="pgfId-893652"></a></p>
      </td>

      <td rowspan="1" colspan="1">
        <p class="CellBody"><a name="pgfId-893654" id="pgfId-893654"></a>Example of
        Use:</p>

        <pre style="word-break:normal;">a=vcs.init()
tt=a.gettexttable("std")
# To Modify an existing text table object
...
if a.istexttable(tt):
tt.list()
</pre></td>
    </tr>

    <tr>
      <td rowspan="1" colspan="4">
        <p class="CellHeading"><a name="pgfId-893661" id="pgfId-893661"></a>List
        Available Templates, Graphics Methods and Secondary Objects</p>
      </td>
    </tr>

    <tr>
      <td rowspan="1" colspan="1">
        <code class=""><a name="pgfId-893669" id="pgfId-893669"></a><a name="marker-910471" id="marker-910471"></a>listelements</code>
      </td>

      <td rowspan="1" colspan="1">
        <p class="CellBody"><a name="pgfId-893671" id="pgfId-893671"></a>Function:
        listelements</p>

        <p class="CellBody"><a name="pgfId-893672" id="pgfId-893672"></a></p>

        <p class="CellBody"><a name="pgfId-893673" id="pgfId-893673"></a>Description of
        Function:</p>

        <p class="CellBody"><a name="pgfId-893674" id="pgfId-893674"></a> Returns a
        Python list of all the VCS class objects.</p>
      </td>

      <td rowspan="1" colspan="1">
        <p class="CellBody"><a name="pgfId-893676" id="pgfId-893676"></a></p>
      </td>

      <td rowspan="1" colspan="1">
        <p class="CellBody"><a name="pgfId-893678" id="pgfId-893678"></a>Example of
        Use:</p>

        <pre style="word-break:normal;">import vcs
a=vcs.init()
a.listelements()
</pre></td>
    </tr>

    <tr>
      <td rowspan="1" colspan="1">
        <code class=""><a name="pgfId-900312" id="pgfId-900312"></a><a name="marker-910472" id="marker-910472"></a>show</code>
      </td>

      <td rowspan="1" colspan="1">
        <p class="CellBody"><a name="pgfId-900314" id="pgfId-900314"></a>Function:
        show</p>

        <p class="CellBody"><a name="pgfId-900315" id="pgfId-900315"></a></p>

        <p class="CellBody"><a name="pgfId-900316" id="pgfId-900316"></a>Description of
        Function:</p>

        <p class="CellBody"><a name="pgfId-900317" id="pgfId-900317"></a> Show the list
        of VCS primary and secondary class objects.</p>
      </td>

      <td rowspan="1" colspan="1">
        <p class="CellBody"><a name="pgfId-900319" id="pgfId-900319"></a></p>
      </td>

      <td rowspan="1" colspan="1">
        <p class="CellBody"><a name="pgfId-900321" id="pgfId-900321"></a>Example of
        Use:</p>

        <pre style="word-break:normal;">import vcs
a=vcs.init()
a.show('boxfill')
a.show('isofill')
a.show(`template')
a.show('line')
a.show('marker')
</pre></td>
    </tr>

    <tr>
      <td rowspan="1" colspan="4">
        <p class="CellHeading"><a name="pgfId-893686" id="pgfId-893686"></a>Graphics
        Method Objects</p>
      </td>
    </tr>

    <tr>
      <td rowspan="1" colspan="4">
        <p class="CellHeading"><a name="pgfId-893694" id="pgfId-893694"></a>Boxfill</p>
      </td>
    </tr>

    <tr>
      <td rowspan="1" colspan="1">
        <code class=""><a name="pgfId-893702" id="pgfId-893702"></a><a name="marker-910473" id="marker-910473"></a>createboxfill</code>
      </td>

      <td rowspan="1" colspan="1">
        <p class="CellBody"><a name="pgfId-893704" id="pgfId-893704"></a>Function:
        createboxfill</p>

        <p class="CellBody"><a name="pgfId-893705" id="pgfId-893705"></a></p>

        <p class="CellBody"><a name="pgfId-893706" id="pgfId-893706"></a>Description of
        Function:</p>

        <p class="CellBody"><a name="pgfId-893707" id="pgfId-893707"></a> Create a new
        boxfill graphics method given the name and the existingboxfill graphics method to
        copy the attributes from. If no existing boxfill graphics method name is given,
        then the default boxfill graphics method will be used as the graphics method to
        which the attributes will be copied from.</p>

        <p class="CellBody"><a name="pgfId-893708" id="pgfId-893708"></a> If the name
        provided already exists, then a error will be returned. Graphics method names
        must be unique.</p>
      </td>

      <td rowspan="1" colspan="1">
        <p class="CellBody"><a name="pgfId-893710" id="pgfId-893710"></a>new boxfill
        name</p>

        <p class="CellBody"><a name="pgfId-893711" id="pgfId-893711"></a></p>

        <p class="CellBody"><a name="pgfId-893712" id="pgfId-893712"></a>[name of boxfill
        to copy attributes from]</p>
      </td>

      <td rowspan="1" colspan="1">
        <p class="CellBody"><a name="pgfId-893714" id="pgfId-893714"></a>Example of
        Use:</p>

        <pre style="word-break:normal;">import vcs
a=vcs.init()
a.show('boxfill')
box=a.createboxfill('example1')
a.show('boxfill')
box=a.createboxfill('example2','quick')
a.show('boxfill')
</pre></td>
    </tr>

    <tr>
      <td rowspan="1" colspan="1">
        <code class=""><a name="pgfId-893723" id="pgfId-893723"></a><a name="marker-910474" id="marker-910474"></a>getboxfill</code>
      </td>

      <td rowspan="1" colspan="1">
        <p class="CellBody"><a name="pgfId-893725" id="pgfId-893725"></a>Function:
        getboxfill</p>

        <p class="CellBody"><a name="pgfId-893726" id="pgfId-893726"></a></p>

        <p class="CellBody"><a name="pgfId-893727" id="pgfId-893727"></a>Description of
        Function:</p>

        <p class="CellBody"><a name="pgfId-893728" id="pgfId-893728"></a> VCS contains a
        list of graphics methods. This function will create a boxfill class object from
        an existing VCS boxfill graphics method. If no boxfill name is given, then
        boxfill 'default' will be used.</p>

        <p class="CellBody"><a name="pgfId-893729" id="pgfId-893729"></a> Note, VCS does
        not allow the modification of `default' attribute sets. However, a `default'
        attribute set that has been copied under a different name can be modified. (See
        the createboxfill function.)</p>
      </td>

      <td rowspan="1" colspan="1">
        <p class="CellBody"><a name="pgfId-893731" id="pgfId-893731"></a>[boxfill
        name]</p>
      </td>

      <td rowspan="1" colspan="1">
        <p class="CellBody"><a name="pgfId-893733" id="pgfId-893733"></a>Example of
        Use:</p>

        <pre style="word-break:normal;">import vcs
a=vcs.init()
a.show('boxfill')
# Show all the existing boxfill graphics methods
box=a.getboxfill()
# box instance of 'default' boxfill graphics method
box2=a.getboxfill('quick')
# box2 instance of existing 'quick' boxfill graphics method
</pre></td>
    </tr>

    <tr>
      <td rowspan="1" colspan="1">
        <a name="pgfId-893740" id="pgfId-893740"></a>
      </td>

      <td rowspan="1" colspan="1">
        <p class="CellBody"><a name="pgfId-893742" id="pgfId-893742"></a>Object:
        boxfillobject</p>

        <p class="CellBody"><a name="pgfId-893743" id="pgfId-893743"></a></p>

        <p class="CellBody"><a name="pgfId-893744" id="pgfId-893744"></a>Description of
        Function:</p>

        <p class="CellBody"><a name="pgfId-893745" id="pgfId-893745"></a> The boxfill
        graphics method (Gfb) displays a two-dimensional data array by surrounding each
        data value by a colored grid box.</p>

        <p class="CellBody"><a name="pgfId-893746" id="pgfId-893746"></a> This class is
        used to define a boxfill table entry used in VCS, or it can be used to change
        some or all of the attributes in an existing boxfill table entry. Other Useful
        Functions:</p>

        <p class="CellBody"><a name="pgfId-893747" id="pgfId-893747"></a>
        a=vcs.init()<br/>
        # Constructor a.show('boxfill')<br/>
        # Show predefined boxfill graphics methods</p>

        <p class="CellBody"><a name="pgfId-893748" id="pgfId-893748"></a>a.setcolormap("AMIP")<br/>
        # Change the VCS color map</p>

        <p class="CellBody"><a name="pgfId-893749" id="pgfId-893749"></a>a.boxfill(s,b,'default')<br/>
        # Plot data 's' with boxfill 'b' and 'default' template a.update()<br/>
        # Updates the VCS Canvas at user's request a.mode=1, or 0<br/>
        # If 1, then automatic update, else if 0, then use the update function to update
        the VCS Canvas.</p>

        <p class="CellBody"><a name="pgfId-905024" id="pgfId-905024"></a> See Chapter 6
        for additional information.</p>
      </td>

      <td rowspan="1" colspan="1">
        <p class="CellBody"><a name="pgfId-893751" id="pgfId-893751"></a>name</p>

        <p class="CellBody"><a name="pgfId-904997" id="pgfId-904997"></a>projection</p>

        <p class="CellBody"><a name="pgfId-904998" id="pgfId-904998"></a>xticlabels1</p>

        <p class="CellBody"><a name="pgfId-904999" id="pgfId-904999"></a>xticlabels2</p>

        <p class="CellBody"><a name="pgfId-905000" id="pgfId-905000"></a>xmtics1</p>

        <p class="CellBody"><a name="pgfId-905001" id="pgfId-905001"></a>xmtics2</p>

        <p class="CellBody"><a name="pgfId-905002" id="pgfId-905002"></a>yticlabels1</p>

        <p class="CellBody"><a name="pgfId-905003" id="pgfId-905003"></a>yticlabels2</p>

        <p class="CellBody"><a name="pgfId-905004" id="pgfId-905004"></a>ymtics1</p>

        <p class="CellBody"><a name="pgfId-905005" id="pgfId-905005"></a>ymtics2</p>

        <p class="CellBody"><a name="pgfId-905006" id="pgfId-905006"></a>datawc_x1</p>

        <p class="CellBody"><a name="pgfId-905007" id="pgfId-905007"></a>datawc_y1</p>

        <p class="CellBody"><a name="pgfId-905008" id="pgfId-905008"></a>datawc_x2</p>

        <p class="CellBody"><a name="pgfId-905009" id="pgfId-905009"></a>datawc_y2</p>

        <p class="CellBody"><a name="pgfId-905010" id="pgfId-905010"></a>xaxisconvert</p>

        <p class="CellBody"><a name="pgfId-905011" id="pgfId-905011"></a>yaxisconvert</p>

        <p class="CellBody"><a name="pgfId-905012" id="pgfId-905012"></a>level_1</p>

        <p class="CellBody"><a name="pgfId-905013" id="pgfId-905013"></a>level_2</p>

        <p class="CellBody"><a name="pgfId-905014" id="pgfId-905014"></a>color_1</p>

        <p class="CellBody"><a name="pgfId-905015" id="pgfId-905015"></a>color_2</p>

        <p class="CellBody"><a name="pgfId-905016" id="pgfId-905016"></a>legend_type</p>

        <p class="CellBody"><a name="pgfId-905017" id="pgfId-905017"></a>legend</p>

        <p class="CellBody"><a name="pgfId-905018" id="pgfId-905018"></a>ext_1</p>

        <p class="CellBody"><a name="pgfId-905019" id="pgfId-905019"></a>ext_2</p>

        <p class="CellBody"><a name="pgfId-905020" id="pgfId-905020"></a>missing</p>
      </td>

      <td rowspan="1" colspan="1">
        <p class="CellBody"><a name="pgfId-893753" id="pgfId-893753"></a>Example of
        Use:</p>

        <pre style="word-break:normal;">import vcs
a=vcs.init()

# To Create a new instance of boxfill use:
box=a.createboxfill('new','quick')
# Copies content of 'quick' to 'new'
box=a.createboxfill('new')
# Copies content of 'default' to 'new'

# To Modify an existing boxfill use: box=a.getboxfill('AMIP_psl') box.list()
# Will list all the boxfill attribute values
box.projection='linear'
lon30={-180:'180W',-150:'150W',0:'Eq'} box.xticlabels1=lon30 box.xticlabels2=lon30 box.xticlabels(lon30, lon30)
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
box.datawc_y1=-90.0 box.datawc_y2=90.0 box.datawc_x1=-180.0 box.datawc_x2=180.0 box.datawc(-90,90,-180,180)
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

</pre></td>
    </tr>

    <tr>
      <td rowspan="1" colspan="4">
        <p class="CellHeading"><a name="pgfId-893794" id="pgfId-893794"></a>Continents</p>
      </td>
    </tr>

    <tr>
      <td rowspan="1" colspan="1">
        <code class=""><a name="pgfId-893802" id="pgfId-893802"></a><a name="marker-910475" id="marker-910475"></a>createcontinents</code>
      </td>

      <td rowspan="1" colspan="1">
        <p class="CellBody"><a name="pgfId-893804" id="pgfId-893804"></a>Function:
        createcontinents</p>

        <p class="CellBody"><a name="pgfId-893805" id="pgfId-893805"></a></p>

        <p class="CellBody"><a name="pgfId-893806" id="pgfId-893806"></a>Description of
        Function:</p>

        <p class="CellBody"><a name="pgfId-893807" id="pgfId-893807"></a> Create a new
        continents graphics method given the the name and the existing continents
        graphics method to copy the attributes from. If no existing continents graphics
        method name is given, then the default continents graphics method will be used as
        the graphics method to which the attributes will be copied from.</p>

        <p class="CellBody"><a name="pgfId-893808" id="pgfId-893808"></a> If the name
        provided already exists, then a error will be returned. Graphics method names
        must be unique.</p>
      </td>

      <td rowspan="1" colspan="1">
        <p class="CellBody"><a name="pgfId-893810" id="pgfId-893810"></a>new continents
        name</p>

        <p class="CellBody"><a name="pgfId-893811" id="pgfId-893811"></a></p>

        <p class="CellBody"><a name="pgfId-893812" id="pgfId-893812"></a>[name of
        continents to copy attributes from]</p>
      </td>

      <td rowspan="1" colspan="1">
        <p class="CellBody"><a name="pgfId-893814" id="pgfId-893814"></a>Example of
        Use:</p>

        <pre style="word-break:normal;">import vcs
a=vcs.init()
a.show('continents')
con=a.createcontinents('example1',)
a.show('continents')
con=a.createcontinents('example2','quick')
a.show('continents')
</pre></td>
    </tr>

    <tr>
      <td rowspan="1" colspan="1">
        <code class=""><a name="pgfId-893823" id="pgfId-893823"></a><a name="marker-910476" id="marker-910476"></a>getcontinents</code>
      </td>

      <td rowspan="1" colspan="1">
        <p class="CellBody"><a name="pgfId-893825" id="pgfId-893825"></a>Function:
        getcontinents</p>

        <p class="CellBody"><a name="pgfId-893826" id="pgfId-893826"></a></p>

        <p class="CellBody"><a name="pgfId-893827" id="pgfId-893827"></a>Description of
        Function:</p>

        <p class="CellBody"><a name="pgfId-893828" id="pgfId-893828"></a> VCS contains a
        list of graphics methods. This function will create a continents class object
        from an existing VCS continents graphics method. If no continents name is given,
        then continents 'default' will be used.</p>

        <p class="CellBody"><a name="pgfId-893829" id="pgfId-893829"></a> Note, VCS does
        not allow the modification of `default' attribute sets. However, a `default'
        attribute set that has been copied under a different name can be modified. (See
        the createcontinents function.)</p>
      </td>

      <td rowspan="1" colspan="1">
        <p class="CellBody"><a name="pgfId-893831" id="pgfId-893831"></a>[continents
        name]</p>
      </td>

      <td rowspan="1" colspan="1">
        <p class="CellBody"><a name="pgfId-893833" id="pgfId-893833"></a>Example of
        Use:</p>

        <pre style="word-break:normal;">import vcs
a=vcs.init()
a.show('continents')
# Show all the existing continents graphics methods
con=a.getcontinents()
# con instance of 'default' continents graphics method
con2=a.getcontinents('quick')
# con2 instance of existing 'quick' continents graphics method
</pre></td>
    </tr>

    <tr>
      <td rowspan="1" colspan="1">
        <a name="pgfId-893840" id="pgfId-893840"></a>
      </td>

      <td rowspan="1" colspan="1">
        <p class="CellBody"><a name="pgfId-893842" id="pgfId-893842"></a>Object:
        continentsobject</p>

        <p class="CellBody"><a name="pgfId-893843" id="pgfId-893843"></a></p>

        <p class="CellBody"><a name="pgfId-893844" id="pgfId-893844"></a>Description of
        Function:</p>

        <p class="CellBody"><a name="pgfId-893845" id="pgfId-893845"></a> The Continents
        graphics method draws a predefined, generic set of continental outlines in a
        longitude by latitude space. (To draw continental outlines, no external data set
        is required.)</p>

        <p class="CellBody"><a name="pgfId-893846" id="pgfId-893846"></a> This class is
        used to define an continents table entry used in VCS, or it can be used to change
        some or all of the continents attributes in an existing continents table
        entry.</p>

        <p class="CellBody"><a name="pgfId-893847" id="pgfId-893847"></a> Other Useful
        Functions:</p>

        <p class="CellBody"><a name="pgfId-893848" id="pgfId-893848"></a>a=vcs.init()<br/>
        # Constructor</p>

        <p class="CellBody"><a name="pgfId-893849" id="pgfId-893849"></a>a.show('continents')<br/>
        # Show predefined boxfill graphics methods</p>

        <p class="CellBody"><a name="pgfId-893850" id="pgfId-893850"></a>a.show('line')<br/>
        # Show predefined line class objects</p>

        <p class="CellBody"><a name="pgfId-893851" id="pgfId-893851"></a>a.setcolormap("AMIP")<br/>
        # Change the VCS color map</p>

        <p class="CellBody"><a name="pgfId-893852" id="pgfId-893852"></a>a.continents(c,'default')<br/>
        # Plot continents, where 'c' is the defined continents object</p>

        <p class="CellBody"><a name="pgfId-893853" id="pgfId-893853"></a>a.update()<br/>
        # Updates the VCS Canvas at user's request a.mode=1, or 0. If 1, then automatic
        update, else if 0, then use update function to update the VCS Canvas.</p>
        <p>See Chapter 6
        for additional information.</p>
      </td>

      <td rowspan="1" colspan="1">
        <p class="CellBody"><a name="pgfId-893855" id="pgfId-893855"></a>name</p>

        <p class="CellBody"><a name="pgfId-905031" id="pgfId-905031"></a>projection</p>

        <p class="CellBody"><a name="pgfId-905032" id="pgfId-905032"></a>xticlabels1</p>

        <p class="CellBody"><a name="pgfId-905033" id="pgfId-905033"></a>xticlabels2</p>

        <p class="CellBody"><a name="pgfId-905034" id="pgfId-905034"></a>xmtics1</p>

        <p class="CellBody"><a name="pgfId-905035" id="pgfId-905035"></a>xmtics2</p>

        <p class="CellBody"><a name="pgfId-905036" id="pgfId-905036"></a>yticlabels1</p>

        <p class="CellBody"><a name="pgfId-905037" id="pgfId-905037"></a>yticlabels2</p>

        <p class="CellBody"><a name="pgfId-905038" id="pgfId-905038"></a>ymtics1</p>

        <p class="CellBody"><a name="pgfId-905039" id="pgfId-905039"></a>ymtics2</p>

        <p class="CellBody"><a name="pgfId-905040" id="pgfId-905040"></a>datawc_x1</p>

        <p class="CellBody"><a name="pgfId-905041" id="pgfId-905041"></a>datawc_y1</p>

        <p class="CellBody"><a name="pgfId-905042" id="pgfId-905042"></a>datawc_x2</p>

        <p class="CellBody"><a name="pgfId-905043" id="pgfId-905043"></a>datawc_y2</p>

        <p class="CellBody"><a name="pgfId-905044" id="pgfId-905044"></a>line</p>

        <p class="CellBody"><a name="pgfId-905045" id="pgfId-905045"></a></p>

        <p class="CellBody"><a name="pgfId-905046" id="pgfId-905046"></a>linecolor</p>

        <p class="CellBody"><a name="pgfId-905047" id="pgfId-905047"></a>type</p>
      </td>

      <td rowspan="1" colspan="1">
        <p class="CellBody"><a name="pgfId-893857" id="pgfId-893857"></a>Example of
        Use:</p>

        <pre style="word-break:normal;">import vcs
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

</pre></td>
    </tr>

    <tr>
      <td rowspan="1" colspan="4">
        <p class="CellHeading"><a name="pgfId-893907" id="pgfId-893907"></a>Isofill</p>
      </td>
    </tr>

    <tr>
      <td rowspan="1" colspan="1">
        <code class=""><a name="pgfId-893915" id="pgfId-893915"></a><a name="marker-910477" id="marker-910477"></a>createisofill</code>
      </td>

      <td rowspan="1" colspan="1">
        <p class="CellBody"><a name="pgfId-893917" id="pgfId-893917"></a>Function:
        createisofill</p>

        <p class="CellBody"><a name="pgfId-893918" id="pgfId-893918"></a></p>

        <p class="CellBody"><a name="pgfId-893919" id="pgfId-893919"></a>Description of
        Function:</p>

        <p class="CellBody"><a name="pgfId-893920" id="pgfId-893920"></a> Create a new
        isofill graphics method given the the name and the existing isofill graphics
        method to copy the attributes from. If no existing isofill graphics method name
        is given, then the default isofill graphics method will be used as the graphics
        method to which the attributes will be copied from.</p>

        <p class="CellBody"><a name="pgfId-893921" id="pgfId-893921"></a> If the name
        provided already exists, then a error will be returned. Graphics method names
        must be unique.</p>
      </td>

      <td rowspan="1" colspan="1">
        <p class="CellBody"><a name="pgfId-893923" id="pgfId-893923"></a>new isofill
        name</p>

        <p class="CellBody"><a name="pgfId-893924" id="pgfId-893924"></a></p>

        <p class="CellBody"><a name="pgfId-893925" id="pgfId-893925"></a>[name of isofill
        to copy attributes from]</p>

        <p class="CellBody"><a name="pgfId-893926" id="pgfId-893926"></a></p>
      </td>

      <td rowspan="1" colspan="1">
        <p class="CellBody"><a name="pgfId-893928" id="pgfId-893928"></a>Example of
        Use:</p>

        <pre style="word-break:normal;">import vcs
a=vcs.init()
a.show('isofill')
iso=a.createisofill('example1',)
a.show('isofill')
iso=a.createisofill('example2','quick')
a.show('isofill')
</pre></td>
    </tr>

    <tr>
      <td rowspan="1" colspan="1">
        <code class=""><a name="pgfId-893937" id="pgfId-893937"></a><a name="marker-910478" id="marker-910478"></a>getisofill</code>
      </td>

      <td rowspan="1" colspan="1">
        <p class="CellBody"><a name="pgfId-893939" id="pgfId-893939"></a>Function:
        getisofill</p>

        <p class="CellBody"><a name="pgfId-893940" id="pgfId-893940"></a></p>

        <p class="CellBody"><a name="pgfId-893941" id="pgfId-893941"></a>Description of
        Function:</p>

        <p class="CellBody"><a name="pgfId-893942" id="pgfId-893942"></a> VCS contains a
        list of graphics methods. This function will create a isofill class object from
        an existing VCS isofill graphics method. If no isofill name is given, then
        isofill 'default' will be used.</p>

        <p class="CellBody"><a name="pgfId-893943" id="pgfId-893943"></a> Note, VCS does
        not allow the modification of `default' attribute sets. However, a `default'
        attribute set that has been copied under a different name can be modified. (See
        the createisofill function.)</p>
      </td>

      <td rowspan="1" colspan="1">
        <p class="CellBody"><a name="pgfId-893945" id="pgfId-893945"></a>[continents
        name]</p>

        <p class="CellBody"><a name="pgfId-893946" id="pgfId-893946"></a></p>
      </td>

      <td rowspan="1" colspan="1">
        <p class="CellBody"><a name="pgfId-893948" id="pgfId-893948"></a>Example of
        Use:</p>

        <pre style="word-break:normal;">import vcs
a=vcs.init()
a.show('isofill')
# Show all the existing isofill graphics methods
iso=a.getisofill()
# iso instance of 'default' isofill graphics method
iso2=a.getisofill('quick')
# iso2 instance of existing 'quick' isofill graphics method
</pre></td>
    </tr>

    <tr>
      <td rowspan="1" colspan="1">
        <a name="pgfId-893955" id="pgfId-893955"></a>
      </td>

      <td rowspan="1" colspan="1">
        <p class="CellBody"><a name="pgfId-893957" id="pgfId-893957"></a>Object:
        isofillobject</p>

        <p class="CellBody"><a name="pgfId-893958" id="pgfId-893958"></a></p>

        <p class="CellBody"><a name="pgfId-893959" id="pgfId-893959"></a>Description of
        Function:</p>

        <p class="CellBody"><a name="pgfId-893960" id="pgfId-893960"></a> The Isofill
        graphics method fills the area between selected isolevels (levels of constant
        value) of a two-dimensional array with a user-specified color. The example below
        shows how to display an isofill plot on the VCS Canvas and how to create and
        remove isofill isolevels.</p>

        <p class="CellBody"><a name="pgfId-893961" id="pgfId-893961"></a> This class is
        used to define an isofill table entry used in VCS, or it can be used to change
        some or all of the isofill attributes in anexisting isofill table entry.</p>

        <p class="CellBody"><a name="pgfId-893962" id="pgfId-893962"></a> Other Useful
        Functions:</p>

        <p class="CellBody"><a name="pgfId-893963" id="pgfId-893963"></a>a=vcs.init()<br/>
        # Constructor</p>

        <p class="CellBody"><a name="pgfId-893964" id="pgfId-893964"></a>a.show('isofill')<br/>
        # Show predefined isofill graphics methods</p>

        <p class="CellBody"><a name="pgfId-893965" id="pgfId-893965"></a>a.show('fillarea')<br/>
        # Show predefined fillarea objects</p>

        <p class="CellBody"><a name="pgfId-893966" id="pgfId-893966"></a>a.show('template')<br/>
        # Show predefined fillarea objects</p>

        <p class="CellBody"><a name="pgfId-893967" id="pgfId-893967"></a>a.setcolormap("AMIP")<br/>
        # Change the VCS color map</p>

        <p class="CellBody"><a name="pgfId-893968" id="pgfId-893968"></a>a.createtemplate('test')<br/>
        # Create a template</p>
                <p class="CellBody"><a name="pgfId-894000" id="pgfId-894000"></a>a.createfillarea('fill') # Create a fillarea</p>

        <p class="CellBody"><a name="pgfId-894001" id="pgfId-894001"></a>a.gettemplate('AMIP') # Get an existing template</p>

        <p class="CellBody"><a name="pgfId-894002" id="pgfId-894002"></a>a.getfillarea('def37') # Get an existing fillarea</p>

        <p class="CellBody"><a name="pgfId-894003" id="pgfId-894003"></a>a.isofill(s,i,t)
        # Plot array 's' with isofill 'i' and template 't'</p>

        <p class="CellBody"><a name="pgfId-894004" id="pgfId-894004"></a>a.update() #
        Updates the VCS Canvas at user's request a.mode=1, or 0. If 1, then automatic
        update,</p>

        <p class="CellBody"><a name="pgfId-894005" id="pgfId-894005"></a>else if 0, then
        use update function to update the VCS Canvas.</p>

        <p class="CellBody"><a name="pgfId-905049" id="pgfId-905049"></a> See Chapter 6
        for additional information.</p>
      </td>

      <td rowspan="1" colspan="1">
        <p class="CellBody"><a name="pgfId-893970" id="pgfId-893970"></a>name</p>

        <p class="CellBody"><a name="pgfId-905051" id="pgfId-905051"></a>projection</p>

        <p class="CellBody"><a name="pgfId-905052" id="pgfId-905052"></a>xticlabels1</p>

        <p class="CellBody"><a name="pgfId-905053" id="pgfId-905053"></a>xticlabels2</p>

        <p class="CellBody"><a name="pgfId-905054" id="pgfId-905054"></a>xmtics1</p>

        <p class="CellBody"><a name="pgfId-905055" id="pgfId-905055"></a>xmtics2</p>

        <p class="CellBody"><a name="pgfId-905056" id="pgfId-905056"></a>yticlabels1</p>

        <p class="CellBody"><a name="pgfId-905057" id="pgfId-905057"></a>yticlabels2</p>

        <p class="CellBody"><a name="pgfId-905058" id="pgfId-905058"></a>ymtics1</p>

        <p class="CellBody"><a name="pgfId-905059" id="pgfId-905059"></a>ymtics2</p>

        <p class="CellBody"><a name="pgfId-905060" id="pgfId-905060"></a>datawc_x1</p>

        <p class="CellBody"><a name="pgfId-905061" id="pgfId-905061"></a>datawc_y1</p>

        <p class="CellBody"><a name="pgfId-905062" id="pgfId-905062"></a>datawc_x2</p>

        <p class="CellBody"><a name="pgfId-905063" id="pgfId-905063"></a>datawc_y2</p>

        <p class="CellBody"><a name="pgfId-905064" id="pgfId-905064"></a>xaxisconvert</p>

        <p class="CellBody"><a name="pgfId-905065" id="pgfId-905065"></a>yaxisconvert</p>

        <p class="CellBody"><a name="pgfId-905066" id="pgfId-905066"></a>missing</p>

        <p class="CellBody"><a name="pgfId-905067" id="pgfId-905067"></a>ext_1</p>

        <p class="CellBody"><a name="pgfId-905068" id="pgfId-905068"></a>ext_2</p>

        <p class="CellBody"><a name="pgfId-905069" id="pgfId-905069"></a>fillareaindices</p>

        <p class="CellBody"><a name="pgfId-905071" id="pgfId-905071"></a>fillareastyle</p>

        <p class="CellBody"><a name="pgfId-905072" id="pgfId-905072"></a>fillareacolors</p>

        <p class="CellBody"><a name="pgfId-905074" id="pgfId-905074"></a>levels</p>
      </td>

      <td rowspan="1" colspan="1">
        <p class="CellBody"><a name="pgfId-893972" id="pgfId-893972"></a>Example of
        Use:</p>

        <pre style="word-break:normal;">import vcs
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

# There are three possibilities for setting the fillarea color indices (Ex):
iso.fillareacolors=([22,33,44,55,66,77])
iso.fillareacolors=(16,19,33,44)
iso.fillareacolors=None

# There are three possibilities for setting the fillarea style (Ex):
iso.fillareastyle = 'solid'
iso.fillareastyle = 'hatch'
iso.fillareastyle = 'pattern'
# There are two ways to set the fillarea hatch or pattern indices (Ex):
iso.fillareaindices=([1,3,5,6,9,20])
iso.fillareaindices=(7,1,4,9,6,15)
See using fillarea objects below!

# Using the fillarea secondary object (Ex):
f=createfillarea('fill1')
# To Create a new instance of fillarea use:
fill=a.createisofill('new','quick') # Copies 'quick' to 'new'
fill=a.createisofill('new') # Copies 'default' to 'new'

# To Modify an existing isofill use:
fill=a.getisofill('def37')

</pre></td>
    </tr>

    <tr>
      <td rowspan="1" colspan="4">
        <p class="CellHeading"><a name="pgfId-894069" id="pgfId-894069"></a>Isoline</p>
      </td>
    </tr>

    <tr>
      <td rowspan="1" colspan="1">
        <code class=""><a name="pgfId-894077" id="pgfId-894077"></a><a name="marker-910479" id="marker-910479"></a>createisoline</code>
      </td>

      <td rowspan="1" colspan="1">
        <p class="CellBody"><a name="pgfId-894079" id="pgfId-894079"></a>Function:
        createisoline</p>

        <p class="CellBody"><a name="pgfId-894080" id="pgfId-894080"></a></p>

        <p class="CellBody"><a name="pgfId-894081" id="pgfId-894081"></a>Description of
        Function:</p>

        <p class="CellBody"><a name="pgfId-894082" id="pgfId-894082"></a> Create a new
        isoline graphics method given the the name and the existing isoline graphics
        method to copy the attributes from. If no existing isoline graphics method name
        is given, then the default isoline graphics method will be used as the graphics
        method to which the attributes will be copied from.</p>

        <p class="CellBody"><a name="pgfId-894083" id="pgfId-894083"></a> If the name
        provided already exists, then a error will be returned. Graphicsmethod names must
        be unique.</p>
      </td>

      <td rowspan="1" colspan="1">
        <p class="CellBody"><a name="pgfId-894085" id="pgfId-894085"></a>new isoline
        name</p>

        <p class="CellBody"><a name="pgfId-894086" id="pgfId-894086"></a></p>

        <p class="CellBody"><a name="pgfId-894087" id="pgfId-894087"></a>[name of isoline
        to copy attributes from]</p>

        <p class="CellBody"><a name="pgfId-894088" id="pgfId-894088"></a></p>
      </td>

      <td rowspan="1" colspan="1">
        <p class="CellBody"><a name="pgfId-894090" id="pgfId-894090"></a>Example of
        Use:</p>

        <pre style="word-break:normal;">import vcs
a=vcs.init()
a.show('isoline')
iso=a.createisoline('example1',)
a.show('isoline')
iso=a.createisoline('example2','quick')
a.show('isoline')
</pre></td>
    </tr>

    <tr>
      <td rowspan="1" colspan="1">
        <code class=""><a name="pgfId-894099" id="pgfId-894099"></a><a name="marker-910480" id="marker-910480"></a>getisoline</code>
      </td>

      <td rowspan="1" colspan="1">
        <p class="CellBody"><a name="pgfId-894101" id="pgfId-894101"></a>Function:
        getisoline</p>

        <p class="CellBody"><a name="pgfId-894102" id="pgfId-894102"></a></p>

        <p class="CellBody"><a name="pgfId-894103" id="pgfId-894103"></a>Description of
        Function:</p>

        <p class="CellBody"><a name="pgfId-894104" id="pgfId-894104"></a> VCS contains a
        list of graphics methods. This function will create a isoline class object from
        an existing VCS isoline graphics method. If no isoline name is given, then
        isoline 'default' will be used.</p>

        <p class="CellBody"><a name="pgfId-894105" id="pgfId-894105"></a> Note, VCS does
        not allow the modification of `default' attribute sets. However, a `default'
        attribute set that has been copied under a different name can be modified. (See
        the createisoline function.)</p>
      </td>

      <td rowspan="1" colspan="1">
        <p class="CellBody"><a name="pgfId-894107" id="pgfId-894107"></a>[isoline
        name]</p>

        <p class="CellBody"><a name="pgfId-894108" id="pgfId-894108"></a></p>
      </td>

      <td rowspan="1" colspan="1">
        <p class="CellBody"><a name="pgfId-894110" id="pgfId-894110"></a>Example of
        Use:</p>

        <pre style="word-break:normal;">import vcs
a=vcs.init()
a.show('isoline')
# Show all the existing isoline graphics methods
iso=a.getisoline()
# iso instance of 'default' isoline graphics method
iso2=a.getisoline('quick')
# iso2 instance of existing 'quick' isoline graphics method
</pre></td>
    </tr>

    <tr>
      <td rowspan="1" colspan="1">
        <a name="pgfId-894117" id="pgfId-894117"></a>
      </td>

      <td rowspan="1" colspan="1">
        <p class="CellBody"><a name="pgfId-894119" id="pgfId-894119"></a>Object:
        isolineobject</p>

        <p class="CellBody"><a name="pgfId-894120" id="pgfId-894120"></a></p>

        <p class="CellBody"><a name="pgfId-894121" id="pgfId-894121"></a>Description of
        Function:</p>

        <p class="CellBody"><a name="pgfId-894122" id="pgfId-894122"></a> The Isoline
        graphics method draws lines of constant value at specified levels in order to
        graphically represent a two-dimensional array. It also labels the values of these
        isolines on the VCS Canvas. The example below shows how to plot isolines of
        different types at specified levels and how to create isoline labels having
        user-specified text and line type and color.</p>

        <p class="CellBody"><a name="pgfId-894123" id="pgfId-894123"></a> This class is
        used to define an isoline table entry used in VCS, or it can be used to change
        some or all of the isoline attributes in an existing isoline table entry.</p>

        <p class="CellBody"><a name="pgfId-894124" id="pgfId-894124"></a> Other Useful
        Functions:</p>

        <p class="CellBody"><a name="pgfId-894125" id="pgfId-894125"></a>a=vcs.init()<br/>
        # Constructor</p>

        <p class="CellBody"><a name="pgfId-894126" id="pgfId-894126"></a>a.show('isoline')<br/>
        # Show predefined isoline graphics methods</p>

        <p class="CellBody"><a name="pgfId-894127" id="pgfId-894127"></a>a.show('line')<br/>
        # Show predefined VCS line objects</p>
        <p class="CellBody"><a name="pgfId-894155" id="pgfId-894155"></a>a.update()<br/>
        # Updates the VCS Canvas at user's request</p>

        <p class="CellBody"><a name="pgfId-894156" id="pgfId-894156"></a>a.mode=1, or
        0<br/>
        # If 1, then automatic update, else if 0, then use update function.</p>

        <p class="CellBody"><a name="pgfId-894157" id="pgfId-894157"></a>a.setcolormap("AMIP")<br/>
        # Change the VCS color map</p>

        <p class="CellBody"><a name="pgfId-894158" id="pgfId-894158"></a>a.isoline(s,a,'default')<br/>
        # Plot data 's' with isoline 'i' and 'default' template</p>

        <p class="CellBody"><a name="pgfId-894159" id="pgfId-894159"></a>tion to update
        the VCS Canvas.</p>

        <p class="CellBody"><a name="pgfId-894160" id="pgfId-894160"></a> See Chapter 6
        for additional information.</p>
        <p class="CellBody"><a name="pgfId-894128" id="pgfId-894128"></a></p>
      </td>

      <td rowspan="1" colspan="1">
        <p class="CellBody"><a name="pgfId-894130" id="pgfId-894130"></a>name</p>

        <p class="CellBody"><a name="pgfId-905085" id="pgfId-905085"></a>projection</p>

        <p class="CellBody"><a name="pgfId-905086" id="pgfId-905086"></a>xticlabels1</p>

        <p class="CellBody"><a name="pgfId-905087" id="pgfId-905087"></a>xticlabels2</p>

        <p class="CellBody"><a name="pgfId-905088" id="pgfId-905088"></a>xmtics1</p>

        <p class="CellBody"><a name="pgfId-905089" id="pgfId-905089"></a>xmtics2</p>

        <p class="CellBody"><a name="pgfId-905090" id="pgfId-905090"></a>yticlabels1</p>

        <p class="CellBody"><a name="pgfId-905091" id="pgfId-905091"></a>yticlabels2</p>

        <p class="CellBody"><a name="pgfId-905092" id="pgfId-905092"></a>ymtics1</p>

        <p class="CellBody"><a name="pgfId-905093" id="pgfId-905093"></a>ymtics2</p>

        <p class="CellBody"><a name="pgfId-905094" id="pgfId-905094"></a>datawc_x1</p>

        <p class="CellBody"><a name="pgfId-905095" id="pgfId-905095"></a>datawc_y1</p>

        <p class="CellBody"><a name="pgfId-905096" id="pgfId-905096"></a>datawc_x2</p>

        <p class="CellBody"><a name="pgfId-905097" id="pgfId-905097"></a>datawc_y2</p>

        <p class="CellBody"><a name="pgfId-905098" id="pgfId-905098"></a>xaxisconvert</p>

        <p class="CellBody"><a name="pgfId-905099" id="pgfId-905099"></a>yaxisconvert</p>

        <p class="CellBody"><a name="pgfId-905100" id="pgfId-905100"></a>label</p>

        <p class="CellBody"><a name="pgfId-905101" id="pgfId-905101"></a>line</p>

        <p class="CellBody"><a name="pgfId-905103" id="pgfId-905103"></a>linecolors</p>

        <p class="CellBody"><a name="pgfId-905104" id="pgfId-905104"></a>text</p>

        <p class="CellBody"><a name="pgfId-905107" id="pgfId-905107"></a>textcolors</p>

        <p class="CellBody"><a name="pgfId-905108" id="pgfId-905108"></a>level</p>
      </td>

      <td rowspan="1" colspan="1">
        <p class="CellBody"><a name="pgfId-894132" id="pgfId-894132"></a>Example of
        Use:</p>

        <pre style="word-break:normal;">import vcs
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
# Note: a combination of a pair (i.e., (30,0) or [30,0]) represents the isoline value plus it increment value. Thus, to let VCS generate "default" isolines enter the following:
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
</pre></td>
    </tr>

    <tr>
      <td rowspan="1" colspan="4">
        <p class="CellHeading"><a name="pgfId-894220" id="pgfId-894220"></a>Outfill</p>
      </td>
    </tr>

    <tr>
      <td rowspan="1" colspan="1">
        <code class=""><a name="pgfId-894228" id="pgfId-894228"></a><a name="marker-910481" id="marker-910481"></a>createoutfill</code>
      </td>

      <td rowspan="1" colspan="1">
        <p class="CellBody"><a name="pgfId-894230" id="pgfId-894230"></a>Function:
        createoutfill</p>

        <p class="CellBody"><a name="pgfId-894231" id="pgfId-894231"></a></p>

        <p class="CellBody"><a name="pgfId-894232" id="pgfId-894232"></a>Description of
        Function:</p>

        <p class="CellBody"><a name="pgfId-894233" id="pgfId-894233"></a> Create a new
        outfill graphics method given the the name and the existing outfill graphics
        method to copy the attributes from. If no existing outfill graphics method name
        is given, then the default outfill graphics method will be used as the graphics
        method to which the attributes will be copied from.</p>

        <p class="CellBody"><a name="pgfId-894234" id="pgfId-894234"></a> If the name
        provided already exists, then a error will be returned. Graphics method names
        must be unique.</p>
      </td>

      <td rowspan="1" colspan="1">
        <p class="CellBody"><a name="pgfId-894236" id="pgfId-894236"></a>new outfill
        name</p>

        <p class="CellBody"><a name="pgfId-894237" id="pgfId-894237"></a></p>

        <p class="CellBody"><a name="pgfId-894238" id="pgfId-894238"></a>[name of outfill
        to copy attributes from]</p>

        <p class="CellBody"><a name="pgfId-894239" id="pgfId-894239"></a></p>
      </td>

      <td rowspan="1" colspan="1">
        <p class="CellBody"><a name="pgfId-894241" id="pgfId-894241"></a>Example of
        Use:</p>

        <pre style="word-break:normal;">import vcs
a=vcs.init()
a.show('outfill')
out=a.createoutfill('example1',)
a.show('outfill')
out=a.createoutfill('example2','quick')
a.show('outfill')
</pre></td>
    </tr>

    <tr>
      <td rowspan="1" colspan="1">
        <code class=""><a name="pgfId-894250" id="pgfId-894250"></a><a name="marker-910482" id="marker-910482"></a>getoutfill</code>
      </td>

      <td rowspan="1" colspan="1">
        <p class="CellBody"><a name="pgfId-894252" id="pgfId-894252"></a>Function:
        getoutfill</p>

        <p class="CellBody"><a name="pgfId-894253" id="pgfId-894253"></a></p>

        <p class="CellBody"><a name="pgfId-894254" id="pgfId-894254"></a>Description of
        Function:</p>

        <p class="CellBody"><a name="pgfId-894255" id="pgfId-894255"></a> VCS contains a
        list of graphics methods. This function will create a outfill class object from
        an existing VCS outfill graphics method. If no outfill name is given, then
        outfill 'default' will be used.</p>

        <p class="CellBody"><a name="pgfId-894256" id="pgfId-894256"></a> Note, VCS does
        not allow the modification of `default' attribute sets. However, a `default'
        attribute set that has been copied under a different name can be modified. (See
        the createoutfill function.)</p>
      </td>

      <td rowspan="1" colspan="1">
        <p class="CellBody"><a name="pgfId-894258" id="pgfId-894258"></a>[outfill
        name]</p>

        <p class="CellBody"><a name="pgfId-894259" id="pgfId-894259"></a></p>
      </td>

      <td rowspan="1" colspan="1">
        <p class="CellBody"><a name="pgfId-894261" id="pgfId-894261"></a>Example of
        Use:</p>

        <pre style="word-break:normal;">import vcs
a=vcs.init()
a.show('outfill')
# Show all the existing outfill graphics methods
out=a.getoutfill()
# out instance of 'default' outfill graphics method
out2=a.getoutfill('quick')
# out2 instance of existing 'quick' outfill graphics method
</pre></td>
    </tr>

    <tr>
      <td rowspan="1" colspan="1">
        <a name="pgfId-894268" id="pgfId-894268"></a>
      </td>

      <td rowspan="1" colspan="1">
        <p class="CellBody"><a name="pgfId-894270" id="pgfId-894270"></a>Object:
        outfillobject</p>

        <p class="CellBody"><a name="pgfId-894271" id="pgfId-894271"></a></p>

        <p class="CellBody"><a name="pgfId-894272" id="pgfId-894272"></a>Description of
        Function:</p>

        <p class="CellBody"><a name="pgfId-894273" id="pgfId-894273"></a> The outfill
        graphics method fills a set of integer values in any data array.</p>

        <p class="CellBody"><a name="pgfId-894274" id="pgfId-894274"></a> Its primary
        purpose is to display continents by filling their area as defined by a surface
        type array that indicates land, ocean, and sea-ice points. The example below
        shows how to apply the outfill graphics method and how to modify</p>

        <p class="CellBody"><a name="pgfId-894275" id="pgfId-894275"></a> Fillarea and
        outfill attributes. Other Useful Functions:</p>

        <p class="CellBody"><a name="pgfId-894276" id="pgfId-894276"></a>a=vcs.init()<br/>
        # Constructor</p>

        <p class="CellBody"><a name="pgfId-894277" id="pgfId-894277"></a>a.show('outfill')<br/>
        # Show predefined outfill graphics methods</p>

        <p class="CellBody"><a name="pgfId-894278" id="pgfId-894278"></a>a.show('line')<br/>
        # Show predefined VCS line objects</p>

        <p class="CellBody"><a name="pgfId-894279" id="pgfId-894279"></a>a.setcolormap("AMIP")<br/>
        # Change the VCS color map</p>

        <p class="CellBody"><a name="pgfId-894280" id="pgfId-894280"></a>a.outfill(s,o,'default')<br/>
        # Plot data 's' with outfill 'o' and 'default' template</p>

        <p class="CellBody"><a name="pgfId-894281" id="pgfId-894281"></a>a.update()<br/>
        # Updates the VCS Canvas at user's request a.mode=1, or 0 . If 1, then automatic
        update, else if 0, then use update function to update the VCS Canvas.</p>
        <p>See Chapter 6 for additional information.</p>
      </td>

      <td rowspan="1" colspan="1">
        <p class="CellBody"><a name="pgfId-894283" id="pgfId-894283"></a>name</p>

        <p class="CellBody"><a name="pgfId-905115" id="pgfId-905115"></a>projection</p>

        <p class="CellBody"><a name="pgfId-905116" id="pgfId-905116"></a>xticlabels1</p>

        <p class="CellBody"><a name="pgfId-905117" id="pgfId-905117"></a>xticlabels2</p>

        <p class="CellBody"><a name="pgfId-905118" id="pgfId-905118"></a>xmtics1</p>

        <p class="CellBody"><a name="pgfId-905119" id="pgfId-905119"></a>xmtics2</p>

        <p class="CellBody"><a name="pgfId-905120" id="pgfId-905120"></a>yticlabels1</p>

        <p class="CellBody"><a name="pgfId-905121" id="pgfId-905121"></a>yticlabels2</p>

        <p class="CellBody"><a name="pgfId-905122" id="pgfId-905122"></a>ymtics1</p>

        <p class="CellBody"><a name="pgfId-905123" id="pgfId-905123"></a>ymtics2</p>

        <p class="CellBody"><a name="pgfId-905124" id="pgfId-905124"></a>datawc_x1</p>

        <p class="CellBody"><a name="pgfId-905125" id="pgfId-905125"></a>datawc_y1</p>

        <p class="CellBody"><a name="pgfId-905126" id="pgfId-905126"></a>datawc_x2</p>

        <p class="CellBody"><a name="pgfId-905127" id="pgfId-905127"></a>datawc_y2</p>

        <p class="CellBody"><a name="pgfId-905128" id="pgfId-905128"></a>xaxisconvert</p>

        <p class="CellBody"><a name="pgfId-905129" id="pgfId-905129"></a>yaxisconvert</p>

        <p class="CellBody"><a name="pgfId-905130" id="pgfId-905130"></a>fillareastyle</p>

        <p class="CellBody"><a name="pgfId-905132" id="pgfId-905132"></a>fillareaindex</p>

        <p class="CellBody"><a name="pgfId-905133" id="pgfId-905133"></a>fillareacolor</p>

        <p class="CellBody"><a name="pgfId-905134" id="pgfId-905134"></a>outfill</p>
      </td>

      <td rowspan="1" colspan="1">
        <p class="CellBody"><a name="pgfId-894285" id="pgfId-894285"></a>Example of
        Use:</p>

        <pre style="word-break:normal;">import vcs
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

</pre></td>
    </tr>

    <tr>
      <td rowspan="1" colspan="4">
        <p class="CellHeading"><a name="pgfId-894332" id="pgfId-894332"></a>Outline</p>
      </td>
    </tr>

    <tr>
      <td rowspan="1" colspan="1">
        <code class=""><a name="pgfId-894340" id="pgfId-894340"></a><a name="marker-910484" id="marker-910484"></a>createoutline</code>
      </td>

      <td rowspan="1" colspan="1">
        <p class="CellBody"><a name="pgfId-894342" id="pgfId-894342"></a>Function:
        createoutline</p>

        <p class="CellBody"><a name="pgfId-894343" id="pgfId-894343"></a></p>

        <p class="CellBody"><a name="pgfId-894344" id="pgfId-894344"></a>Description of
        Function:</p>

        <p class="CellBody"><a name="pgfId-894345" id="pgfId-894345"></a> Create a new
        outline graphics method given the the name and the existing outline graphics
        method to copy the attributes from. If no existing outline graphics method name
        is given, then the default outline graphics method will be used as the graphics
        method to which the attributes will be copied from.</p>

        <p class="CellBody"><a name="pgfId-894346" id="pgfId-894346"></a> If the name
        provided already exists, then a error will be returned. Graphics method names
        must be unique.</p>
      </td>

      <td rowspan="1" colspan="1">
        <p class="CellBody"><a name="pgfId-894348" id="pgfId-894348"></a>new outline
        name</p>

        <p class="CellBody"><a name="pgfId-894349" id="pgfId-894349"></a></p>

        <p class="CellBody"><a name="pgfId-894350" id="pgfId-894350"></a>[name of outline
        to copy attributes from]</p>

        <p class="CellBody"><a name="pgfId-894351" id="pgfId-894351"></a></p>
      </td>

      <td rowspan="1" colspan="1">
        <p class="CellBody"><a name="pgfId-894353" id="pgfId-894353"></a>Example of
        Use:</p>

        <pre style="word-break:normal;">import vcs
a=vcs.init()
a.show('outline')
out=a.createoutline('example1',)
a.show('outline')
out=a.createoutline('example2','quick')
a.show('outline')
</pre></td>
    </tr>

    <tr>
      <td rowspan="1" colspan="1">
        <code class=""><a name="pgfId-894362" id="pgfId-894362"></a><a name="marker-910483" id="marker-910483"></a>getoutline</code>
      </td>

      <td rowspan="1" colspan="1">
        <p class="CellBody"><a name="pgfId-894364" id="pgfId-894364"></a>Function:
        getoutline</p>

        <p class="CellBody"><a name="pgfId-894365" id="pgfId-894365"></a></p>

        <p class="CellBody"><a name="pgfId-894366" id="pgfId-894366"></a>Description of
        Function:</p>

        <p class="CellBody"><a name="pgfId-894367" id="pgfId-894367"></a> VCS contains a
        list of graphics methods. This function will create a outline class object from
        an existing VCS outline graphics method. If no outline name is given, then
        outline 'default' will be used.</p>

        <p class="CellBody"><a name="pgfId-894368" id="pgfId-894368"></a> Note, VCS does
        not allow the modification of `default' attribute sets. However, a `default'
        attribute set that has been copied under a different name can be modified. (See
        the createoutline function.)</p>
      </td>

      <td rowspan="1" colspan="1">
        <p class="CellBody"><a name="pgfId-894370" id="pgfId-894370"></a>[outline
        name]</p>

        <p class="CellBody"><a name="pgfId-894371" id="pgfId-894371"></a></p>
      </td>

      <td rowspan="1" colspan="1">
        <p class="CellBody"><a name="pgfId-894373" id="pgfId-894373"></a>Example of
        Use:</p>

        <pre style="word-break:normal;">import vcs
a=vcs.init()
a.show('outline')
# Show all the existing outline graphics methods
out=a.getoutline()
# out instance of 'default' outline graphics method
out2=a.getoutline('quick')
# out2 instance of existing 'quick' outline graphics method
</pre></td>
    </tr>

    <tr>
      <td rowspan="1" colspan="1">
        <a name="pgfId-894380" id="pgfId-894380"></a>
      </td>

      <td rowspan="1" colspan="1">
        <p class="CellBody"><a name="pgfId-894382" id="pgfId-894382"></a>Object:
        outlineobject</p>

        <p class="CellBody"><a name="pgfId-894383" id="pgfId-894383"></a></p>

        <p class="CellBody"><a name="pgfId-894384" id="pgfId-894384"></a>Description of
        Function:</p>

        <p class="CellBody"><a name="pgfId-894385" id="pgfId-894385"></a> The Outline
        graphics method outlines a set of integer values in any data array.</p>

        <p class="CellBody"><a name="pgfId-894386" id="pgfId-894386"></a> Its primary
        purpose is to display continental outlines as defined by a surface</p>

        <p class="CellBody"><a name="pgfId-894387" id="pgfId-894387"></a> type array that
        indicates land, ocean, and sea-ice points. The example below</p>

        <p class="CellBody"><a name="pgfId-894388" id="pgfId-894388"></a> shows how to
        change such an outline by modifying its attributes.</p>

        <p class="CellBody"><a name="pgfId-894389" id="pgfId-894389"></a></p>

        <p class="CellBody"><a name="pgfId-894390" id="pgfId-894390"></a> Other Useful
        Functions:</p>

        <p class="CellBody"><a name="pgfId-894391" id="pgfId-894391"></a>
        a=vcs.init()<br/>
        # Constructor</p>

        <p class="CellBody"><a name="pgfId-894392" id="pgfId-894392"></a>a.show('outline')<br/>
        # Show predefined outline graphics methods</p>

        <p class="CellBody"><a name="pgfId-894393" id="pgfId-894393"></a>a.show('line')<br/>
        # Show predefined VCS line objects</p>

        <p class="CellBody"><a name="pgfId-894394" id="pgfId-894394"></a>a.setcolormap("AMIP")<br/>
        # Change the VCS color map</p>

        <p class="CellBody"><a name="pgfId-894395" id="pgfId-894395"></a>a.outline(s,o,'default')<br/>
        # Plot data 's' with outline 'o' and 'default' template</p>

        <p class="CellBody"><a name="pgfId-894397" id="pgfId-894397"></a> a.update()</p>
        <p class="CellBody"><a name="pgfId-894428" id="pgfId-894428"></a># Updates the
        VCS Canvas at user's request a.mode=1, or 0 # If 1, then automatic update, else
        if 0, then use u pdate function to update the VCS Canvas.</p>

        <p class="CellBody"><a name="pgfId-905136" id="pgfId-905136"></a> See Chapter 6
        for additional information.</p>
      </td>

      <td rowspan="1" colspan="1">
        <p class="CellBody"><a name="pgfId-894399" id="pgfId-894399"></a>name</p>

        <p class="CellBody"><a name="pgfId-905162" id="pgfId-905162"></a>projection</p>

        <p class="CellBody"><a name="pgfId-905163" id="pgfId-905163"></a>xticlabels1</p>

        <p class="CellBody"><a name="pgfId-905164" id="pgfId-905164"></a>xticlabels2</p>

        <p class="CellBody"><a name="pgfId-905165" id="pgfId-905165"></a>xmtics1</p>

        <p class="CellBody"><a name="pgfId-905166" id="pgfId-905166"></a>xmtics2</p>

        <p class="CellBody"><a name="pgfId-905167" id="pgfId-905167"></a>yticlabels1</p>

        <p class="CellBody"><a name="pgfId-905168" id="pgfId-905168"></a>yticlabels2</p>

        <p class="CellBody"><a name="pgfId-905169" id="pgfId-905169"></a>ymtics1</p>

        <p class="CellBody"><a name="pgfId-905170" id="pgfId-905170"></a>ymtics2</p>

        <p class="CellBody"><a name="pgfId-905171" id="pgfId-905171"></a>datawc_x1</p>

        <p class="CellBody"><a name="pgfId-905172" id="pgfId-905172"></a>datawc_y1</p>

        <p class="CellBody"><a name="pgfId-905173" id="pgfId-905173"></a>datawc_x2</p>

        <p class="CellBody"><a name="pgfId-905174" id="pgfId-905174"></a>datawc_y2</p>

        <p class="CellBody"><a name="pgfId-905175" id="pgfId-905175"></a>xaxisconvert</p>

        <p class="CellBody"><a name="pgfId-905176" id="pgfId-905176"></a>yaxisconvert</p>

        <p class="CellBody"><a name="pgfId-905177" id="pgfId-905177"></a>line</p>

        <p class="CellBody"><a name="pgfId-905179" id="pgfId-905179"></a>linecolor</p>

        <p class="CellBody"><a name="pgfId-905180" id="pgfId-905180"></a>outline</p>
      </td>

      <td rowspan="1" colspan="1">
        <p class="CellBody"><a name="pgfId-894401" id="pgfId-894401"></a>Example of
        Use:</p>

        <pre style="word-break:normal;">import vcs
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
# Will set them both
 xyvsyobjectout.datawc_y1=-90.0
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

</pre></td>
    </tr>

    <tr>
      <td rowspan="1" colspan="4">
        <p class="CellHeading"><a name="pgfId-894461" id="pgfId-894461"></a>Scatter</p>
      </td>
    </tr>

    <tr>
      <td rowspan="1" colspan="1">
        <code class=""><a name="pgfId-894469" id="pgfId-894469"></a><a name="marker-910486" id="marker-910486"></a>createscatter</code>
      </td>

      <td rowspan="1" colspan="1">
        <p class="CellBody"><a name="pgfId-894471" id="pgfId-894471"></a>Function:
        createscatter</p>

        <p class="CellBody"><a name="pgfId-894472" id="pgfId-894472"></a></p>

        <p class="CellBody"><a name="pgfId-894473" id="pgfId-894473"></a>Description of
        Function:</p>

        <p class="CellBody"><a name="pgfId-894474" id="pgfId-894474"></a> Create a new
        scatter graphics method given the the name and the existing mscatter graphics
        method to copy the attributes from. If no existing scatter graphics method name
        is given, then the default scatter graphics method will be used as the graphics
        method to which the attributes will be copied from.</p>

        <p class="CellBody"><a name="pgfId-894475" id="pgfId-894475"></a> If the name
        provided already exists, then a error will be returned. Graphics method names
        must be unique</p>
      </td>

      <td rowspan="1" colspan="1">
        <p class="CellBody"><a name="pgfId-894477" id="pgfId-894477"></a>new scatter
        name</p>

        <p class="CellBody"><a name="pgfId-894478" id="pgfId-894478"></a></p>

        <p class="CellBody"><a name="pgfId-894479" id="pgfId-894479"></a>[name of scatter
        to copy attributes from]</p>

        <p class="CellBody"><a name="pgfId-894480" id="pgfId-894480"></a></p>
      </td>

      <td rowspan="1" colspan="1">
        <p class="CellBody"><a name="pgfId-894482" id="pgfId-894482"></a>Example of
        Use:</p>

        <pre style="word-break:normal;">import vcs
a=vcs.init()
a.show('scatter')
sct=a.createscatter('example1',)
a.show('scatter')
sct=a.createscatter('example2','quick')
a.show('scatter')
</pre></td>
    </tr>

    <tr>
      <td rowspan="1" colspan="1">
        <code class=""><a name="pgfId-894491" id="pgfId-894491"></a><a name="marker-910485" id="marker-910485"></a>getscatter</code>
      </td>

      <td rowspan="1" colspan="1">
        <p class="CellBody"><a name="pgfId-894493" id="pgfId-894493"></a>Function:
        getscatter</p>

        <p class="CellBody"><a name="pgfId-894494" id="pgfId-894494"></a></p>

        <p class="CellBody"><a name="pgfId-894495" id="pgfId-894495"></a>Description of
        Function:</p>

        <p class="CellBody"><a name="pgfId-894496" id="pgfId-894496"></a> VCS contains a
        list of graphics methods. This function will create a scatter class object from
        an existing VCS scatter graphics method. If no scatter name is given, then
        scatter 'default' will be used.</p>

        <p class="CellBody"><a name="pgfId-894497" id="pgfId-894497"></a> Note, VCS does
        not allow the modification of `default' attribute sets. However, a `default'
        attribute set that has been copied under a different name can be modified. (See
        the createscatter function.)</p>

        <p class="CellBody"><a name="pgfId-894498" id="pgfId-894498"></a></p>
      </td>

      <td rowspan="1" colspan="1">
        <p class="CellBody"><a name="pgfId-894500" id="pgfId-894500"></a>[scatter
        name]</p>

        <p class="CellBody"><a name="pgfId-894501" id="pgfId-894501"></a></p>
      </td>

      <td rowspan="1" colspan="1">
        <p class="CellBody"><a name="pgfId-894503" id="pgfId-894503"></a>Example of
        Use:</p>

        <pre style="word-break:normal;">import vcs
a=vcs.init()
a.show('scatter')
# Show all the existing scatter graphics methods
sct=a.getscatter()
# sct instance of 'default' scatter graphics method
sct2=a.getscatter('quick')
# sct2 instance of existing 'quick' scatter graphics method

</pre></td>
    </tr>

    <tr>
      <td rowspan="1" colspan="1">
        <a name="pgfId-894511" id="pgfId-894511"></a>
      </td>

      <td rowspan="1" colspan="1">
        <p class="CellBody"><a name="pgfId-894513" id="pgfId-894513"></a>Object:
        scatterobject</p>

        <p class="CellBody"><a name="pgfId-894514" id="pgfId-894514"></a></p>

        <p class="CellBody"><a name="pgfId-894515" id="pgfId-894515"></a>Description of
        Function:</p>

        <p class="CellBody"><a name="pgfId-894516" id="pgfId-894516"></a> The Scatter
        graphics method displays a scatter plot of two 4-dimensional data arrays, e.g.
        A(x,y,z,t) and B(x,y,z,t). The example below shows how to change the marker
        attributes of a scatter plot.</p>

        <p class="CellBody"><a name="pgfId-894517" id="pgfId-894517"></a> This class is
        used to define an scatter table entry used in VCS, or it can be used to change
        some or all of the scatter attributes in an existing scatter table entry.</p>

        <p class="CellBody"><a name="pgfId-894518" id="pgfId-894518"></a> Other Useful
        Functions:</p>

        <p class="CellBody"><a name="pgfId-894519" id="pgfId-894519"></a>a=vcs.init()<br/>
        # Constructor</p>

        <p class="CellBody"><a name="pgfId-894520" id="pgfId-894520"></a>a.show('scatter')<br/>
        # Show predefined scatter graphics methods</p>

        <p class="CellBody"><a name="pgfId-894521" id="pgfId-894521"></a>a.show('marker')<br/>
        # Show predefined marker objects</p>

        <p class="CellBody"><a name="pgfId-894522" id="pgfId-894522"></a>a.setcolormap("AMIP")<br/>
        # Change the VCS color map</p>

        <p class="CellBody"><a name="pgfId-894523" id="pgfId-894523"></a>a.scatter(s1,
        s2, s,'default')<br/>
        # Plot data 's1' and 's2' with scatter 's' and 'default' template</p>

        <p class="CellBody"><a name="pgfId-894524" id="pgfId-894524"></a>a.update()<br/>
        # Updates the VCS Canvas at user's request a.mode=1, or 0. If 1, then automatic
        update, else if 0, then use update function to update the VCS Canvas.</p>
        <p>See Chapter 6
        for additional information.</p>
      </td>

      <td rowspan="1" colspan="1">
        <p class="CellBody"><a name="pgfId-894526" id="pgfId-894526"></a>name</p>

        <p class="CellBody"><a name="pgfId-905187" id="pgfId-905187"></a>projection</p>

        <p class="CellBody"><a name="pgfId-905188" id="pgfId-905188"></a>xticlabels1</p>

        <p class="CellBody"><a name="pgfId-905189" id="pgfId-905189"></a>xticlabels2</p>

        <p class="CellBody"><a name="pgfId-905190" id="pgfId-905190"></a>xmtics1</p>

        <p class="CellBody"><a name="pgfId-905191" id="pgfId-905191"></a>xmtics2</p>

        <p class="CellBody"><a name="pgfId-905192" id="pgfId-905192"></a>yticlabels1</p>

        <p class="CellBody"><a name="pgfId-905193" id="pgfId-905193"></a>yticlabels2</p>

        <p class="CellBody"><a name="pgfId-905194" id="pgfId-905194"></a>ymtics1</p>

        <p class="CellBody"><a name="pgfId-905195" id="pgfId-905195"></a>ymtics2</p>

        <p class="CellBody"><a name="pgfId-905196" id="pgfId-905196"></a>datawc_x1</p>

        <p class="CellBody"><a name="pgfId-905197" id="pgfId-905197"></a>datawc_y1</p>

        <p class="CellBody"><a name="pgfId-905198" id="pgfId-905198"></a>datawc_x2</p>

        <p class="CellBody"><a name="pgfId-905199" id="pgfId-905199"></a>datawc_y2</p>

        <p class="CellBody"><a name="pgfId-905200" id="pgfId-905200"></a>xaxisconvert</p>

        <p class="CellBody"><a name="pgfId-905201" id="pgfId-905201"></a>yaxisconvert</p>

        <p class="CellBody"><a name="pgfId-905202" id="pgfId-905202"></a>marker</p>

        <p class="CellBody"><a name="pgfId-905209" id="pgfId-905209"></a>markercolor</p>

        <p class="CellBody"><a name="pgfId-905210" id="pgfId-905210"></a>markersize</p>
      </td>

      <td rowspan="1" colspan="1">
        <p class="CellBody"><a name="pgfId-894528" id="pgfId-894528"></a>Example of
        Use:</p>

        <pre style="word-break:normal;">import vcs
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

#To set the Marker sizie:
sr.markersize=5
sr.markersize=55
sr.markersize=100
sr.markersize=300
sr.markersize=None

</pre></td>
    </tr>

    <tr>
      <td rowspan="1" colspan="4">
        <p class="CellHeading"><a name="pgfId-894606" id="pgfId-894606"></a>Vector</p>
      </td>
    </tr>

    <tr>
      <td rowspan="1" colspan="1">
        <code class=""><a name="pgfId-894614" id="pgfId-894614"></a><a name="marker-910488" id="marker-910488"></a>createvector</code>
      </td>

      <td rowspan="1" colspan="1">
        <p class="CellBody"><a name="pgfId-894616" id="pgfId-894616"></a>Function:
        createvector</p>

        <p class="CellBody"><a name="pgfId-894617" id="pgfId-894617"></a></p>

        <p class="CellBody"><a name="pgfId-894618" id="pgfId-894618"></a>Description of
        Function:</p>

        <p class="CellBody"><a name="pgfId-894619" id="pgfId-894619"></a> Create a new
        vector graphics method given the the name and the existing vector graphics method
        to copy the attributes from. If no existing vector graphics method name is given,
        then the default vector graphics method will be used as the graphics method to
        which the attributes will be copied from.</p>

        <p class="CellBody"><a name="pgfId-894620" id="pgfId-894620"></a> If the name
        provided already exists, then a error will be returned. Graphics method names
        must be unique.</p>
      </td>

      <td rowspan="1" colspan="1">
        <p class="CellBody"><a name="pgfId-894622" id="pgfId-894622"></a>new vector
        name</p>

        <p class="CellBody"><a name="pgfId-894623" id="pgfId-894623"></a></p>

        <p class="CellBody"><a name="pgfId-894624" id="pgfId-894624"></a>[name of vector
        to copy attributes from]</p>

        <p class="CellBody"><a name="pgfId-894625" id="pgfId-894625"></a></p>
      </td>

      <td rowspan="1" colspan="1">
        <p class="CellBody"><a name="pgfId-894627" id="pgfId-894627"></a>Example of
        Use:</p>

        <pre style="word-break:normal;">import vcs
a=vcs.init()
a.show('vector')
vec=a.createvector('example1',)
a.show('vector')
vec=a.createvector('example2','quick')
a.show('vector')
</pre></td>
    </tr>

    <tr>
      <td rowspan="1" colspan="1">
        <code class=""><a name="pgfId-894636" id="pgfId-894636"></a><a name="marker-910487" id="marker-910487"></a>getvector</code>
      </td>

      <td rowspan="1" colspan="1">
        <p class="CellBody"><a name="pgfId-894638" id="pgfId-894638"></a>Function:
        getvector</p>

        <p class="CellBody"><a name="pgfId-894639" id="pgfId-894639"></a></p>

        <p class="CellBody"><a name="pgfId-894640" id="pgfId-894640"></a>Description of
        Function:</p>

        <p class="CellBody"><a name="pgfId-894641" id="pgfId-894641"></a> VCS contains a
        list of graphics methods. This function will create a vector class object from an
        existing VCS vector graphics method. If no vector name is given, then vector
        'default' will be used.</p>

        <p class="CellBody"><a name="pgfId-894642" id="pgfId-894642"></a> Note, VCS does
        not allow the modification of `default' attribute sets. However, a `default'
        attribute set that has been copied under a different name can be modified. (See
        the createvector function.)</p>
      </td>

      <td rowspan="1" colspan="1">
        <p class="CellBody"><a name="pgfId-894644" id="pgfId-894644"></a>[vector
        name]</p>

        <p class="CellBody"><a name="pgfId-894645" id="pgfId-894645"></a></p>
      </td>

      <td rowspan="1" colspan="1">
        <p class="CellBody"><a name="pgfId-894647" id="pgfId-894647"></a>Example of
        Use:</p>

        <pre style="word-break:normal;">import vcs
a=vcs.init()
a.show('vector')
# Show all the existing vector graphics methods
vec=a.getvector()
# vec instance of 'default' vector graphics method
vec2=a.getvector('quick')
# vec2 instance of existing 'quick' vector graphics method
</pre></td>
    </tr>

    <tr>
      <td rowspan="1" colspan="1">
        <a name="pgfId-894654" id="pgfId-894654"></a>
      </td>

      <td rowspan="1" colspan="1">
        <p class="CellBody"><a name="pgfId-894656" id="pgfId-894656"></a>Object:
        vectorobject</p>

        <p class="CellBody"><a name="pgfId-894657" id="pgfId-894657"></a></p>

        <p class="CellBody"><a name="pgfId-894658" id="pgfId-894658"></a>Description of
        Function:</p>

        <p class="CellBody"><a name="pgfId-894659" id="pgfId-894659"></a> The vector
        graphics method displays a vector plot of a 2D vector field. Vectors</p>

        <p class="CellBody"><a name="pgfId-894660" id="pgfId-894660"></a> are located at
        the coordinate locations and point in the direction of the data vector field.
        Vector magnitudes are the product of data vector field lengths and a scaling
        factor. The example below shows how to modify the vector's line, scale,
        alignment, type, and reference.</p>

        <p class="CellBody"><a name="pgfId-894661" id="pgfId-894661"></a> This class is
        used to define an vector table entry used in VCS, or it can be used to change
        some or all of the vector attributes in an existing vector table entry.</p>

        <p class="CellBody"><a name="pgfId-894662" id="pgfId-894662"></a> Other Useful
        Functions:</p>

        <p class="CellBody"><a name="pgfId-894663" id="pgfId-894663"></a>a=vcs.init()<br/>
        # Constructor</p>

        <p class="CellBody"><a name="pgfId-894664" id="pgfId-894664"></a>a.show('vector')<br/>
        # Show predefined vector graphics methods</p>

        <p class="CellBody"><a name="pgfId-894665" id="pgfId-894665"></a>a.show('line')<br/>
        # Show predefined VCS line objects</p>

        <p class="CellBody"><a name="pgfId-894666" id="pgfId-894666"></a>a.setcolormap("AMIP")<br/>
        # Change the VCS color Map</p>

        <p class="CellBody"><a name="pgfId-894667" id="pgfId-894667"></a>a.vector(s1, s2,
        v,'default')<br/>
        # Plot data 's1', and 's2' with vector 'v' and 'default' template</p>
<p class="CellBody"><a name="pgfId-894698" id="pgfId-894698"></a>a.update() #
        Updates the VCS Canvas at user's request a.mode=1, or 0. If 1, then automatic
        update, else if 0, then use update function to update the VCS Canvas.</p>

        <p class="CellBody"><a name="pgfId-905216" id="pgfId-905216"></a> See Chapter 6
        for additional information.</p>
        <p class="CellBody"><a name="pgfId-894668" id="pgfId-894668"></a></p>
      </td>

      <td rowspan="1" colspan="1">
        <p class="CellBody"><a name="pgfId-894670" id="pgfId-894670"></a>name</p>

        <p class="CellBody"><a name="pgfId-905222" id="pgfId-905222"></a>projection</p>

        <p class="CellBody"><a name="pgfId-905223" id="pgfId-905223"></a>xticlabels1</p>

        <p class="CellBody"><a name="pgfId-905224" id="pgfId-905224"></a>xticlabels2</p>

        <p class="CellBody"><a name="pgfId-905225" id="pgfId-905225"></a>xmtics1</p>

        <p class="CellBody"><a name="pgfId-905226" id="pgfId-905226"></a>xmtics2</p>

        <p class="CellBody"><a name="pgfId-905227" id="pgfId-905227"></a>yticlabels1</p>

        <p class="CellBody"><a name="pgfId-905228" id="pgfId-905228"></a>yticlabels2</p>

        <p class="CellBody"><a name="pgfId-905229" id="pgfId-905229"></a>ymtics1</p>

        <p class="CellBody"><a name="pgfId-905230" id="pgfId-905230"></a>ymtics2</p>

        <p class="CellBody"><a name="pgfId-905231" id="pgfId-905231"></a>datawc_x1</p>

        <p class="CellBody"><a name="pgfId-905232" id="pgfId-905232"></a>datawc_y1</p>

        <p class="CellBody"><a name="pgfId-905233" id="pgfId-905233"></a>datawc_x2</p>

        <p class="CellBody"><a name="pgfId-905234" id="pgfId-905234"></a>datawc_y2</p>

        <p class="CellBody"><a name="pgfId-905235" id="pgfId-905235"></a>xaxisconvert</p>

        <p class="CellBody"><a name="pgfId-905236" id="pgfId-905236"></a>yaxisconvert</p>

        <p class="CellBody"><a name="pgfId-905237" id="pgfId-905237"></a>line</p>

        <p class="CellBody"><a name="pgfId-905239" id="pgfId-905239"></a>linecolor</p>

        <p class="CellBody"><a name="pgfId-905240" id="pgfId-905240"></a>scale</p>

        <p class="CellBody"><a name="pgfId-905241" id="pgfId-905241"></a>alignment</p>

        <p class="CellBody"><a name="pgfId-905242" id="pgfId-905242"></a>type</p>

        <p class="CellBody"><a name="pgfId-905243" id="pgfId-905243"></a>reference</p>
      </td>

      <td rowspan="1" colspan="1">
        <p class="CellBody"><a name="pgfId-894672" id="pgfId-894672"></a>Example of
        Use:</p>

        <pre style="word-break:normal;">import vcs
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

</pre></td>
    </tr>

    <tr>
      <td rowspan="1" colspan="4">
        <p class="CellHeading"><a name="pgfId-894743" id="pgfId-894743"></a>XvsY</p>
      </td>
    </tr>

    <tr>
      <td rowspan="1" colspan="1">
        <code class=""><a name="pgfId-894751" id="pgfId-894751"></a><a name="marker-910489" id="marker-910489"></a>createxvsy</code>
      </td>

      <td rowspan="1" colspan="1">
        <p class="CellBody"><a name="pgfId-894753" id="pgfId-894753"></a>Function:
        createxvsy</p>

        <p class="CellBody"><a name="pgfId-894754" id="pgfId-894754"></a></p>

        <p class="CellBody"><a name="pgfId-894755" id="pgfId-894755"></a>Description of
        Function:</p>

        <p class="CellBody"><a name="pgfId-894756" id="pgfId-894756"></a> Create a new
        XvsY graphics method given the the name and the existing XvsY graphics method to
        copy the attributes from. If no existing XvsY graphics method name is given, then
        the default XvsY graphics method will be used as the graphics method to which the
        attributes will be copied from.</p>

        <p class="CellBody"><a name="pgfId-894757" id="pgfId-894757"></a> If the name
        provided already exists, then a error will be returned. Graphics method names
        must be unique.</p>
      </td>

      <td rowspan="1" colspan="1">
        <p class="CellBody"><a name="pgfId-894759" id="pgfId-894759"></a>new xvsy
        name</p>

        <p class="CellBody"><a name="pgfId-894760" id="pgfId-894760"></a></p>

        <p class="CellBody"><a name="pgfId-894761" id="pgfId-894761"></a>[name of xvsy to
        copy attributes from]</p>

        <p class="CellBody"><a name="pgfId-894762" id="pgfId-894762"></a></p>
      </td>

      <td rowspan="1" colspan="1">
        <p class="CellBody"><a name="pgfId-894764" id="pgfId-894764"></a>Example of
        Use:</p>

        <pre style="word-break:normal;">import vcs
a=vcs.init()
a.show('xvsy')
xy=a.createxvsy('example1',)
a.show('xvsy')
xy=a.createxvsy('example2','quick')
a.show('xvsy')
</pre></td>
    </tr>

    <tr>
      <td rowspan="1" colspan="1">
        <code class=""><a name="pgfId-894773" id="pgfId-894773"></a><a name="marker-910490" id="marker-910490"></a>getxvsy</code>
      </td>

      <td rowspan="1" colspan="1">
        <p class="CellBody"><a name="pgfId-894775" id="pgfId-894775"></a>Function:
        getxvsy</p>

        <p class="CellBody"><a name="pgfId-894776" id="pgfId-894776"></a></p>

        <p class="CellBody"><a name="pgfId-894777" id="pgfId-894777"></a>Description of
        Function:</p>

        <p class="CellBody"><a name="pgfId-894778" id="pgfId-894778"></a> VCS contains a
        list of graphics methods. This function will create a XvsY class object from an
        existing VCS XvsY graphics method. If no XvsY name is given, then XvsY 'default'
        will be used.</p>

        <p class="CellBody"><a name="pgfId-894779" id="pgfId-894779"></a> Note, VCS does
        not allow the modification of `default' attribute sets. However, a `default'
        attribute set that has been copied under a different name can be modified. (See
        the createxvsy function.)</p>
      </td>

      <td rowspan="1" colspan="1">
        <p class="CellBody"><a name="pgfId-894781" id="pgfId-894781"></a>[xvsy name]</p>

        <p class="CellBody"><a name="pgfId-894782" id="pgfId-894782"></a></p>
      </td>

      <td rowspan="1" colspan="1">
        <p class="CellBody"><a name="pgfId-894784" id="pgfId-894784"></a>Example of
        Use:</p>

        <pre style="word-break:normal;">import vcs
a=vcs.init()
a.show('xvsy')
# Show all the existing XvsY xy=a.getxvsy()
# graphics methods xy instance of 'default' XvsY graphics method
xy2=a.getxvsy('quick')
# xy2 instance of existing 'quick' XvsY graphics method
</pre></td>
    </tr>

    <tr>
      <td rowspan="1" colspan="1">
        <a name="pgfId-894790" id="pgfId-894790"></a>
      </td>

      <td rowspan="1" colspan="1">
        <p class="CellBody"><a name="pgfId-894792" id="pgfId-894792"></a>Object:
        xvsyobject</p>

        <p class="CellBody"><a name="pgfId-894793" id="pgfId-894793"></a></p>

        <p class="CellBody"><a name="pgfId-894794" id="pgfId-894794"></a>Description of
        Function:</p>

        <p class="CellBody"><a name="pgfId-894795" id="pgfId-894795"></a> The XvsY
        graphics method displays a line plot from two 1D data arrays, that is X(t) and
        Y(t), where t represents the 1D coordinate values. The example below shows how to
        change line and marker attributes for the XvsY graphics method.</p>

        <p class="CellBody"><a name="pgfId-894796" id="pgfId-894796"></a> This class is
        used to define an XvsY table entry used in VCS, or it can be used to change some
        or all of the XvsY attributes in an existing XvsY table entry.</p>

        <p class="CellBody"><a name="pgfId-894797" id="pgfId-894797"></a> Other Useful
        Functions:</p>

        <p class="CellBody"><a name="pgfId-894798" id="pgfId-894798"></a>a=vcs.init()<br/>
        # Constructor</p>

        <p class="CellBody"><a name="pgfId-894799" id="pgfId-894799"></a>a.show('xvsy')<br/>
        # Show predefined XvsY graphics methonds</p>

        <p class="CellBody"><a name="pgfId-894800" id="pgfId-894800"></a>
        a.show('line')<br/>
        # Show predefined VCS line objects</p>

        <p class="CellBody"><a name="pgfId-894801" id="pgfId-894801"></a>a.show('marker')<br/>
        # Show predefined VCS marker objects</p>

        <p class="CellBody"><a name="pgfId-894802" id="pgfId-894802"></a>a.setcolormap("AMIP")<br/>
        # Change the VCS color map</p>

        <p class="CellBody"><a name="pgfId-894803" id="pgfId-894803"></a>a.xvsy(s1, s2,
        ,x,'default')<br/>
        # Plot data 's1' and 's2' with XvsY 'x' and 'default' template</p>
        <p class="CellBody"><a name="pgfId-894887" id="pgfId-894887"></a>a.update() #
        Updates the VCS Canvas at user's request a.mode=1, or 0. If 1, then automatic
        update, else if 0, then use update function to Update the VCS Canvas.</p>

        <p class="CellBody"><a name="pgfId-905247" id="pgfId-905247"></a> See Chapter 6
        for additional information.</p>
        <p class="CellBody"><a name="pgfId-894804" id="pgfId-894804"></a></p>
      </td>

      <td rowspan="1" colspan="1">
        <p class="CellBody"><a name="pgfId-894806" id="pgfId-894806"></a>name</p>

        <p class="CellBody"><a name="pgfId-905258" id="pgfId-905258"></a>projection</p>

        <p class="CellBody"><a name="pgfId-905259" id="pgfId-905259"></a>xticlabels1</p>

        <p class="CellBody"><a name="pgfId-905260" id="pgfId-905260"></a>xticlabels2</p>

        <p class="CellBody"><a name="pgfId-905261" id="pgfId-905261"></a>xmtics1</p>

        <p class="CellBody"><a name="pgfId-905262" id="pgfId-905262"></a>xmtics2</p>

        <p class="CellBody"><a name="pgfId-905263" id="pgfId-905263"></a>yticlabels1</p>

        <p class="CellBody"><a name="pgfId-905264" id="pgfId-905264"></a>yticlabels2</p>

        <p class="CellBody"><a name="pgfId-905265" id="pgfId-905265"></a>ymtics1</p>

        <p class="CellBody"><a name="pgfId-905266" id="pgfId-905266"></a>ymtics2</p>

        <p class="CellBody"><a name="pgfId-905267" id="pgfId-905267"></a>datawc_x1</p>

        <p class="CellBody"><a name="pgfId-905268" id="pgfId-905268"></a>datawc_y1</p>

        <p class="CellBody"><a name="pgfId-905269" id="pgfId-905269"></a>datawc_x2</p>

        <p class="CellBody"><a name="pgfId-905270" id="pgfId-905270"></a>datawc_y2</p>

        <p class="CellBody"><a name="pgfId-905271" id="pgfId-905271"></a>xaxisconvert</p>

        <p class="CellBody"><a name="pgfId-905272" id="pgfId-905272"></a>yaxisconvert</p>

        <p class="CellBody"><a name="pgfId-905273" id="pgfId-905273"></a>line</p>

        <p class="CellBody"><a name="pgfId-905275" id="pgfId-905275"></a>linecolor</p>

        <p class="CellBody"><a name="pgfId-905276" id="pgfId-905276"></a>marker</p>

        <p class="CellBody"><a name="pgfId-905283" id="pgfId-905283"></a>markercolor</p>

        <p class="CellBody"><a name="pgfId-905284" id="pgfId-905284"></a>markersize</p>
      </td>

      <td rowspan="1" colspan="1">
        <p class="CellBody"><a name="pgfId-894808" id="pgfId-894808"></a>Example of
        Use:</p>

        <pre style="word-break:normal;">import vcs
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
</pre>
<p>There are four possibilities for setting the marker color index (<strong>Example</strong>):</p>
<pre style="word-break:normal;">
xy.markercolors=22 # Same as below
xy.markercolors=(22) # Same as below
xy.markercolors=([22]) # Will set the markers to a specific
xy.markercolors=None # Color index defaults to Black
</pre>
<p>To set the XvsY Marker sizie:</p>
<pre style="word-break:normal;">xy.markersize=5
xy.markersize=55
xy.markersize=100
xy.markersize=300
xy.markersize=None
</pre></td>
    </tr>

    <tr>
      <td rowspan="1" colspan="4">
        <p class="CellHeading"><a name="pgfId-894925" id="pgfId-894925"></a>Xyvsy</p>
      </td>
    </tr>

    <tr>
      <td rowspan="1" colspan="1">
        <code class=""><a name="pgfId-894933" id="pgfId-894933"></a><a name="marker-910491" id="marker-910491"></a>createxyvsy</code>
      </td>

      <td rowspan="1" colspan="1">
        <p class="CellBody"><a name="pgfId-894935" id="pgfId-894935"></a>Function:
        createxyvsy</p>

        <p class="CellBody"><a name="pgfId-894936" id="pgfId-894936"></a></p>

        <p class="CellBody"><a name="pgfId-894937" id="pgfId-894937"></a>Description of
        Function:</p>

        <p class="CellBody"><a name="pgfId-894938" id="pgfId-894938"></a> Create a new
        Xyvsy graphics method given the the name and the existing Xyvsy graphics method
        to copy the attributes from. If no existing Xyvsy graphics method name is given,
        then the default Xyvsy graphics method will be used as the graphics method to
        which the attributes will be copied from.</p>

        <p class="CellBody"><a name="pgfId-894939" id="pgfId-894939"></a> If the name
        provided already exists, then a error will be returned. Graphics method names
        must be unique.</p>
      </td>

      <td rowspan="1" colspan="1">
        <p class="CellBody"><a name="pgfId-894941" id="pgfId-894941"></a>new xyvsy
        name</p>

        <p class="CellBody"><a name="pgfId-894942" id="pgfId-894942"></a></p>

        <p class="CellBody"><a name="pgfId-894943" id="pgfId-894943"></a>[name of xyvsy
        to copy attributes from]</p>

        <p class="CellBody"><a name="pgfId-894944" id="pgfId-894944"></a></p>
      </td>

      <td rowspan="1" colspan="1">
        <p class="CellBody"><a name="pgfId-894946" id="pgfId-894946"></a>Example of
        Use:</p>

        <pre style="word-break:normal;">import vcs
a=vcs.init()
a.show('xyvsy')
xyy=a.createxyvsy('example1',)
a.show('xyvsy')
xyy=a.createxyvsy('example2','quick')
a.show('xyvsy')
</pre></td>
    </tr>

    <tr>
      <td rowspan="1" colspan="1">
        <code class=""><a name="pgfId-894955" id="pgfId-894955"></a><a name="marker-910492" id="marker-910492"></a>getxyvsy</code>
      </td>

      <td rowspan="1" colspan="1">
        <p class="CellBody"><a name="pgfId-894957" id="pgfId-894957"></a>Function:
        getxyvsy</p>

        <p class="CellBody"><a name="pgfId-894958" id="pgfId-894958"></a></p>

        <p class="CellBody"><a name="pgfId-894959" id="pgfId-894959"></a>Description of
        Function:</p>

        <p class="CellBody"><a name="pgfId-894960" id="pgfId-894960"></a> VCS contains a
        list of graphics methods. This function will create a Xyvsy class object from an
        existing VCS Xyvsy graphics method. If no Xyvsy name is given, then Xyvsy
        'default' will be used.</p>

        <p class="CellBody"><a name="pgfId-894961" id="pgfId-894961"></a> Note, VCS does
        not allow the modification of `default' attribute sets. However, a `default'
        attribute set that has been copied under a different name can be modified. (See
        the createxyvsy function.)</p>
      </td>

      <td rowspan="1" colspan="1">
        <p class="CellBody"><a name="pgfId-894963" id="pgfId-894963"></a>[xyvsy name]</p>

        <p class="CellBody"><a name="pgfId-894964" id="pgfId-894964"></a></p>
      </td>

      <td rowspan="1" colspan="1">
        <p class="CellBody"><a name="pgfId-894966" id="pgfId-894966"></a>Example of
        Use:</p>

        <pre style="word-break:normal;">import vcs
a=vcs.init()
a.show('xyvsy')
# Show all the existing Xyvsy graphics methods
xyy=a.getxyvsy()
# xyy instance of 'default' Xyvsy graphics method
xyy2=a.getxyvsy('quick')
# xyy2 instance of existing 'quick' Xyvsy graphics method
</pre></td>
    </tr>

    <tr>
      <td rowspan="1" colspan="1">
        <a name="pgfId-894973" id="pgfId-894973"></a>
      </td>

      <td rowspan="1" colspan="1">
        <p class="CellBody"><a name="pgfId-894975" id="pgfId-894975"></a>Object:
        xyvsyobject</p>

        <p class="CellBody"><a name="pgfId-894976" id="pgfId-894976"></a></p>

        <p class="CellBody"><a name="pgfId-894977" id="pgfId-894977"></a>Description of
        Function:</p>

        <p class="CellBody"><a name="pgfId-894978" id="pgfId-894978"></a> The Xyvsy
        graphics method displays a line plot from a 1D data array (i.e. a plot of X(y),
        where y represents the 1D coordinate values). The example below ributes for the
        Xyvsy graphics method.</p>

        <p class="CellBody"><a name="pgfId-894979" id="pgfId-894979"></a> This class is
        used to define an Xyvsy table entry used in VCS, or it can be used to change some
        or all of the Xyvsy attributes in an existing Xyvsy table entry.</p>

        <p class="CellBody"><a name="pgfId-894980" id="pgfId-894980"></a> Other Useful
        Functions:</p>

        <p class="CellBody"><a name="pgfId-894981" id="pgfId-894981"></a>a=vcs.init()<br/>
        # Constructor</p>

        <p class="CellBody"><a name="pgfId-894982" id="pgfId-894982"></a>a.show('xyvsy')<br/>
        # Show predefined Xyvsy graphics methonds</p>

        <p class="CellBody"><a name="pgfId-894983" id="pgfId-894983"></a>a.show('line')<br/>
        # Show predefined VCS line objects</p>

        <p class="CellBody"><a name="pgfId-894984" id="pgfId-894984"></a>a.show('marker')<br/>
        # Show predefined VCS marker objects</p>

        <p class="CellBody"><a name="pgfId-894985" id="pgfId-894985"></a>a.setcolormap("AMIP")<br/>
        # Change the VCS color map</p>

        <p class="CellBody"><a name="pgfId-894986" id="pgfId-894986"></a>a.xyvsy(s, x,
        'default')<br/>
        # Plot data 's' with Xyvsy 'x' and 'default' template</p>

        <p class="CellBody"><a name="pgfId-894987" id="pgfId-894987"></a>a.update()<br/>
        # Updates the VCS Canvas at user's request a.mode=1, or 0 . If 1, then automatic
        update, else if 0, then use update function.</p><p class="CellBody"><a name="pgfId-896159" id="pgfId-896159"></a> See Chapter 6
        for additional information.</p>
      </td>

      <td rowspan="1" colspan="1">
        <p class="CellBody"><a name="pgfId-894989" id="pgfId-894989"></a>name</p>

        <p class="CellBody"><a name="pgfId-905292" id="pgfId-905292"></a>projection</p>

        <p class="CellBody"><a name="pgfId-905293" id="pgfId-905293"></a>xticlabels1</p>

        <p class="CellBody"><a name="pgfId-905294" id="pgfId-905294"></a>xticlabels2</p>

        <p class="CellBody"><a name="pgfId-905295" id="pgfId-905295"></a>xmtics1</p>

        <p class="CellBody"><a name="pgfId-905296" id="pgfId-905296"></a>xmtics2</p>

        <p class="CellBody"><a name="pgfId-905297" id="pgfId-905297"></a>yticlabels1</p>

        <p class="CellBody"><a name="pgfId-905298" id="pgfId-905298"></a>yticlabels2</p>

        <p class="CellBody"><a name="pgfId-905299" id="pgfId-905299"></a>ymtics1</p>

        <p class="CellBody"><a name="pgfId-905300" id="pgfId-905300"></a>ymtics2</p>

        <p class="CellBody"><a name="pgfId-905301" id="pgfId-905301"></a>datawc_x1</p>

        <p class="CellBody"><a name="pgfId-905302" id="pgfId-905302"></a>datawc_y1</p>

        <p class="CellBody"><a name="pgfId-905303" id="pgfId-905303"></a>datawc_x2</p>

        <p class="CellBody"><a name="pgfId-905304" id="pgfId-905304"></a>datawc_y2</p>

        <p class="CellBody"><a name="pgfId-905305" id="pgfId-905305"></a>xaxisconvert</p>

        <p class="CellBody"><a name="pgfId-905306" id="pgfId-905306"></a>line</p>

        <p class="CellBody"><a name="pgfId-905308" id="pgfId-905308"></a>linecolor</p>

        <p class="CellBody"><a name="pgfId-905309" id="pgfId-905309"></a>marker</p>

        <p class="CellBody"><a name="pgfId-905316" id="pgfId-905316"></a>markercolor</p>

        <p class="CellBody"><a name="pgfId-905317" id="pgfId-905317"></a>markersize</p>
      </td>

      <td rowspan="1" colspan="1">
        <p class="CellBody"><a name="pgfId-894991" id="pgfId-894991"></a>Example of
        Use:</p>

        <pre style="word-break:normal;">import vcs
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
</pre>
<p>
There are four possibilities for setting the marker color index (Ex):
</P>
<pre style="word-break:normal;">xyy.markercolors=22 # Same as below
xyy.markercolors=(22) # Same as below
xyy.markercolors=([22]) # Will set the markers to a specific
# color index
xyy.markercolors=None # Color index defaults to Black
</pre>
<p>
To set the Xyvsy Marker sizie:
</p>
<pre style="word-break:normal;">xyy.markersize=5
xyy.markersize=55
xyy.markersize=100
xyy.markersize=300
xyy.markersize=None
</pre></td>
    </tr>

    <tr>
      <td rowspan="1" colspan="4">
        <p class="CellHeading"><a name="pgfId-895062" id="pgfId-895062"></a>Yxvsx</p>
      </td>
    </tr>

    <tr>
      <td rowspan="1" colspan="1">
        <code class=""><a name="pgfId-895070" id="pgfId-895070"></a><a name="marker-910493" id="marker-910493"></a>createyxvsx</code>
      </td>

      <td rowspan="1" colspan="1">
        <p class="CellBody"><a name="pgfId-895072" id="pgfId-895072"></a>Function:
        createyxvsx</p>

        <p class="CellBody"><a name="pgfId-895073" id="pgfId-895073"></a></p>

        <p class="CellBody"><a name="pgfId-895074" id="pgfId-895074"></a>Description of
        Function:</p>

        <p class="CellBody"><a name="pgfId-895075" id="pgfId-895075"></a> Create a new
        Yxvsx graphics method given the the name and the existing Yxvsx graphics method
        to copy the attributes from. If no existing Yxvsx graphics method name is given,
        then the default Yxvsx graphics method will be used as the graphics method to
        which the attributes will be copied from.</p>

        <p class="CellBody"><a name="pgfId-895076" id="pgfId-895076"></a> If the name
        provided already exists, then a error will be returned. Graphics method names
        must be unique</p>
      </td>

      <td rowspan="1" colspan="1">
        <p class="CellBody"><a name="pgfId-895078" id="pgfId-895078"></a>new yxvsx
        name</p>

        <p class="CellBody"><a name="pgfId-895079" id="pgfId-895079"></a></p>

        <p class="CellBody"><a name="pgfId-895080" id="pgfId-895080"></a>[name of yxvsx
        to copy attributes from]</p>

        <p class="CellBody"><a name="pgfId-895081" id="pgfId-895081"></a></p>
      </td>

      <td rowspan="1" colspan="1">
        <p class="CellBody"><a name="pgfId-895083" id="pgfId-895083"></a>Example of
        Use:</p>

        <pre style="word-break:normal;">import vcs
a=vcs.init()
a.show('yxvsx')
yxx=a.createyxvsx('example1',)
a.show('yxvsx')
yxx=a.createyxvsx('example2','quick')
a.show('yxvsx')
</pre></td>
    </tr>

    <tr>
      <td rowspan="1" colspan="1">
        <code class=""><a name="pgfId-895092" id="pgfId-895092"></a><a name="marker-910494" id="marker-910494"></a>getyxvsx</code>
      </td>

      <td rowspan="1" colspan="1">
        <p class="CellBody"><a name="pgfId-895094" id="pgfId-895094"></a>Function:
        getyxvsx</p>

        <p class="CellBody"><a name="pgfId-895095" id="pgfId-895095"></a></p>

        <p class="CellBody"><a name="pgfId-895096" id="pgfId-895096"></a>Description of
        Function:</p>

        <p class="CellBody"><a name="pgfId-895097" id="pgfId-895097"></a> VCS contains a
        list of graphics methods. This function will create a Yxvsx class object from an
        existing VCS Yxvsx graphics method. If no Yxvsx name is given, then Yxvsx
        'default' will be used.</p>

        <p class="CellBody"><a name="pgfId-895098" id="pgfId-895098"></a> Note, VCS does
        not allow the modification of `default' attribute sets. However, a `default'
        attribute set that has been copied under a different name can be modified. (See
        the createyxvsx function.)</p>
      </td>

      <td rowspan="1" colspan="1">
        <p class="CellBody"><a name="pgfId-895100" id="pgfId-895100"></a>[yxvsx name]</p>

        <p class="CellBody"><a name="pgfId-895101" id="pgfId-895101"></a></p>
      </td>

      <td rowspan="1" colspan="1">
        <p class="CellBody"><a name="pgfId-895103" id="pgfId-895103"></a>Example of
        Use:</p>

        <pre style="word-break:normal;">import vcs
a=vcs.init()
a.show('yxvsx')
# Show all the existing Yxvsx graphics methods
yxx=a.getyxvsx()
# yxx instance of 'default' Yxvsx graphics method
yxx2=a.getyxvsx('quick')
# yxx2 instance of existing 'quick' Yxvsx graphics method
</pre></td>
    </tr>

    <tr>
      <td rowspan="1" colspan="1">
        <a name="pgfId-895110" id="pgfId-895110"></a>
      </td>

      <td rowspan="1" colspan="1">
        <p class="CellBody"><a name="pgfId-895112" id="pgfId-895112"></a>Object:
        yxvsxobject</p>

        <p class="CellBody"><a name="pgfId-895113" id="pgfId-895113"></a></p>

        <p class="CellBody"><a name="pgfId-895114" id="pgfId-895114"></a>Description of
        Function:</p>

        <p class="CellBody"><a name="pgfId-895115" id="pgfId-895115"></a> The Yxvsx
        graphics method displays a line plot from a 1D data array (i.e. aplot of Y(x),
        where y represents the 1D coordinate values). The example belowshows how to
        change line and marker attributes for the Yxvsx graphics method.</p>

        <p class="CellBody"><a name="pgfId-895116" id="pgfId-895116"></a> This class is
        used to define an Yxvsx table entry used in VCS, or it can beused to change some
        or all of the Yxvsx attributes in an existing Yxvsx table entry.</p>

        <p class="CellBody"><a name="pgfId-895117" id="pgfId-895117"></a> Other Useful
        Functions:</p>

        <p class="CellBody"><a name="pgfId-895118" id="pgfId-895118"></a>a=vcs.init()<br/>
        # Constructor</p>

        <p class="CellBody"><a name="pgfId-895119" id="pgfId-895119"></a>a.show('yxvsx')<br/>
        # Show predefined Yxvsx graphics methonds</p>

        <p class="CellBody"><a name="pgfId-895120" id="pgfId-895120"></a>a.show('line')<br/>
        # Show predefined VCS line objects</p>

        <p class="CellBody"><a name="pgfId-895121" id="pgfId-895121"></a>a.show('marker')<br/>
        # Show predefined VCS marker objects</p>

        <p class="CellBody"><a name="pgfId-895122" id="pgfId-895122"></a>a.setcolormap("AMIP")<br/>
        # Change the VCS color map</p>

        <p class="CellBody"><a name="pgfId-895123" id="pgfId-895123"></a>a.yxvsx(s, x,
        'default')<br/>
        # Plot data 's' with Yxvsx 'x' and 'default' template</p>

        <p class="CellBody"><a name="pgfId-895124" id="pgfId-895124"></a>a.update()<br/>
        # Updates the VCS Canvas at user's request</p>

        <p class="CellBody"><a name="pgfId-895125" id="pgfId-895125"></a>a.mode=1, or 0
        If 1, then automatic update, else if 0, then use update function.</p>
        <p>See Chapter 6 for additional information.</p>
      </td>

      <td rowspan="1" colspan="1">
        <p class="CellBody"><a name="pgfId-895127" id="pgfId-895127"></a>name</p>

        <p class="CellBody"><a name="pgfId-905330" id="pgfId-905330"></a>projection</p>

        <p class="CellBody"><a name="pgfId-905331" id="pgfId-905331"></a>xticlabels1</p>

        <p class="CellBody"><a name="pgfId-905332" id="pgfId-905332"></a>xticlabels2</p>

        <p class="CellBody"><a name="pgfId-905333" id="pgfId-905333"></a>xmtics1</p>

        <p class="CellBody"><a name="pgfId-905334" id="pgfId-905334"></a>xmtics2</p>

        <p class="CellBody"><a name="pgfId-905335" id="pgfId-905335"></a>yticlabels1</p>

        <p class="CellBody"><a name="pgfId-905336" id="pgfId-905336"></a>yticlabels2</p>

        <p class="CellBody"><a name="pgfId-905337" id="pgfId-905337"></a>ymtics1</p>

        <p class="CellBody"><a name="pgfId-905338" id="pgfId-905338"></a>ymtics2</p>

        <p class="CellBody"><a name="pgfId-905339" id="pgfId-905339"></a>datawc_x1</p>

        <p class="CellBody"><a name="pgfId-905340" id="pgfId-905340"></a>datawc_y1</p>

        <p class="CellBody"><a name="pgfId-905341" id="pgfId-905341"></a>datawc_x2</p>

        <p class="CellBody"><a name="pgfId-905342" id="pgfId-905342"></a>datawc_y2</p>

        <p class="CellBody"><a name="pgfId-905343" id="pgfId-905343"></a>yaxisconvert</p>

        <p class="CellBody"><a name="pgfId-905344" id="pgfId-905344"></a>line</p>

        <p class="CellBody"><a name="pgfId-905346" id="pgfId-905346"></a>linecolor</p>

        <p class="CellBody"><a name="pgfId-905347" id="pgfId-905347"></a>marker</p>

        <p class="CellBody"><a name="pgfId-905354" id="pgfId-905354"></a>markercolor</p>

        <p class="CellBody"><a name="pgfId-905355" id="pgfId-905355"></a>markersize</p>
      </td>

      <td rowspan="1" colspan="1">
        <p class="CellBody"><a name="pgfId-895129" id="pgfId-895129"></a>Example of
        Use:</p>

        <pre style="word-break:normal;">import vcs
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
yxx.yticlabels(lat10, lat10
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
# There are four possibilities for setting the marker color index (Example):
yxx.markercolors=22 # Same as below
yxx.markercolors=(22) # Same as below
yxx.markercolors=([22])
# Will set the markers to a specific color index
yxx.markercolors=None # Color index defaults to Black
# To set the Yxvsx Marker size:
yxx.markersize=5
yxx.markersize=55
yxx.markersize=100
yxx.markersize=300
yxx.markersize=None
</pre></td>
    </tr>

    <tr>
      <td rowspan="1" colspan="4">
        <p class="CellHeading"><a name="pgfId-895200" id="pgfId-895200"></a>Picture
        Template</p>
      </td>
    </tr>

    <tr>
      <td rowspan="1" colspan="1">
        <code class=""><a name="pgfId-895208" id="pgfId-895208"></a><a name="marker-910495" id="marker-910495"></a>createtemplate</code>
      </td>

      <td rowspan="1" colspan="1">
        <p class="CellBody"><a name="pgfId-895210" id="pgfId-895210"></a>Function:
        createtemplate</p>

        <p class="CellBody"><a name="pgfId-895211" id="pgfId-895211"></a></p>

        <p class="CellBody"><a name="pgfId-895212" id="pgfId-895212"></a>Description of
        Function:</p>

        <p class="CellBody"><a name="pgfId-895213" id="pgfId-895213"></a> Create a new
        template given the the name and the existing template to copy the attributes
        from. If no existing template name is given, then the default template will be
        used as the template to which the attributes will be copied from.</p>

        <p class="CellBody"><a name="pgfId-895214" id="pgfId-895214"></a> If the name
        provided already exists, then a error will be returned. Template names must be
        unique.</p>
      </td>

      <td rowspan="1" colspan="1">
        <p class="CellBody"><a name="pgfId-895216" id="pgfId-895216"></a>new template
        name</p>

        <p class="CellBody"><a name="pgfId-895217" id="pgfId-895217"></a></p>

        <p class="CellBody"><a name="pgfId-895218" id="pgfId-895218"></a>[name of
        template to copy attributes from]</p>
      </td>

      <td rowspan="1" colspan="1">
        <p class="CellBody"><a name="pgfId-895220" id="pgfId-895220"></a>Example of
        Use:</p>

        <pre style="word-break:normal;">import vcs
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
</pre></td>
    </tr>

    <tr>
      <td rowspan="1" colspan="1">
        <code class=""><a name="pgfId-895229" id="pgfId-895229"></a><a name="marker-910496" id="marker-910496"></a>gettemplate</code>
      </td>

      <td rowspan="1" colspan="1">
        <p class="CellBody"><a name="pgfId-895231" id="pgfId-895231"></a>Function:
        gettemplate</p>

        <p class="CellBody"><a name="pgfId-895232" id="pgfId-895232"></a></p>

        <p class="CellBody"><a name="pgfId-895233" id="pgfId-895233"></a>Description of
        Function:</p>

        <p class="CellBody"><a name="pgfId-895234" id="pgfId-895234"></a> VCS contains a
        list of predefined templates. This function will create a template class object
        from an existing VCS template. If no template name is given, then template
        'default' will be used.</p>

        <p class="CellBody"><a name="pgfId-895235" id="pgfId-895235"></a> Note, VCS does
        not allow the modification of `default' attribute sets. However, a `default'
        attribute set that has been copied under a different name can be modified. (See
        the createtemplate function.)</p>
      </td>

      <td rowspan="1" colspan="1">
        <p class="CellBody"><a name="pgfId-895237" id="pgfId-895237"></a>[template
        name]</p>
      </td>

      <td rowspan="1" colspan="1">
        <p class="CellBody"><a name="pgfId-895239" id="pgfId-895239"></a>Example of
        Use:</p>

        <pre style="word-break:normal;">import vcs
a=vcs.init()
a.show('template')
# Show all the existing templates
templt=a.gettemplate()
# templt instance of 'default' template
templt2=a.gettemplate('quick')
# templt2 contains 'quick' template
</pre></td>
    </tr>

    <tr>
      <td rowspan="1" colspan="1">
        <a name="pgfId-895246" id="pgfId-895246"></a>
      </td>

      <td rowspan="1" colspan="1">
        <p class="CellBody"><a name="pgfId-895248" id="pgfId-895248"></a>Object:
        templateobject</p>

        <p class="CellBody"><a name="pgfId-905368" id="pgfId-905368"></a></p>

        <p class="CellBody"><a name="pgfId-895250" id="pgfId-895250"></a>Description of
        Function:</p>

        <p class="CellBody"><a name="pgfId-895251" id="pgfId-895251"></a> The template
        primary method (P) determines the location of each picture segment, the space to
        be allocated to it, and related properties relevant to its display.</p>

        <p class="CellBody"><a name="pgfId-895252" id="pgfId-895252"></a>Other Useful
        Functions:</p>

        <p class="CellBody"><a name="pgfId-895253" id="pgfId-895253"></a>a.show('template')<br/>
        # Show predefined templates</p>

        <p class="CellBody"><a name="pgfId-895254" id="pgfId-895254"></a>a.show('texttable')<br/>
        # Show predefined text table methods</p>

        <p class="CellBody"><a name="pgfId-895255" id="pgfId-895255"></a>a.show('textorientation')<br/>
        # Show predefined text orientation methods</p>

        <p class="CellBody"><a name="pgfId-895256" id="pgfId-895256"></a>a.show('line')<br/>
        # Show predefined line methods</p>

        <p class="CellBody"><a name="pgfId-895257" id="pgfId-895257"></a>a.listelements('template')<br/>
        # Show templates as a Python list</p>

        <p class="CellBody"><a name="pgfId-895258" id="pgfId-895258"></a>a.update()<br/>
        # Updates the VCS Canvas at user's request a.mode=1, or 0. If 1, then automatic
        update, else if 0, then use the update function toupdate the VCS Canvas.</p>
      </td>

      <td rowspan="1" colspan="1">
        <p class="CellBody"><a name="pgfId-895260" id="pgfId-895260"></a>See Chapter 6
        for the long list of options.</p>
      </td>

      <td rowspan="1" colspan="1">
        <p class="CellBody"><a name="pgfId-895262" id="pgfId-895262"></a>Example of
        Use:</p>

        <pre style="word-break:normal;">import vcs
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
</pre></td>
    </tr>

    <tr>
      <td rowspan="1" colspan="4">
        <p class="CellHeading"><a name="pgfId-895276" id="pgfId-895276"></a>Secondary
        Objects</p>
      </td>
    </tr>

    <tr>
      <td rowspan="1" colspan="4">
        <p class="CellHeading"><a name="pgfId-895284" id="pgfId-895284"></a>Colormap
        Commands</p>
      </td>
    </tr>

    <tr>
      <td rowspan="1" colspan="1">
        <code class=""><a name="pgfId-895292" id="pgfId-895292"></a><a name="marker-910497" id="marker-910497"></a>setcolormap</code>
      </td>

      <td rowspan="1" colspan="1">
        <p class="CellBody"><a name="pgfId-895294" id="pgfId-895294"></a>Function:
        setcolormap</p>

        <p class="CellBody"><a name="pgfId-895295" id="pgfId-895295"></a></p>

        <p class="CellBody"><a name="pgfId-895296" id="pgfId-895296"></a>Description of
        Function:</p>

        <p class="CellBody"><a name="pgfId-895297" id="pgfId-895297"></a> It is necessary
        to change the colormap. This routine will change the VCS color map.</p>

        <p class="CellBody"><a name="pgfId-895298" id="pgfId-895298"></a> If the the
        visul display is 16-bit, 24-bit, or 32-bit TrueColor, then a redrawing of the VCS
        Canvas is made evertime the colormap is changed.</p>
      </td>

      <td rowspan="1" colspan="1">
        <p class="CellBody"><a name="pgfId-895300" id="pgfId-895300"></a></p>
      </td>

      <td rowspan="1" colspan="1">
        <p class="CellBody"><a name="pgfId-895302" id="pgfId-895302"></a>Example of
        Use:</p>

        <pre style="word-break:normal;">import vcsa=vcs.init()
a.plot(array,'default','isofill','quick')
a.setcolormap("AMIP")
</pre></td>
    </tr>

    <tr>
      <td rowspan="1" colspan="1">
        <code class=""><a name="pgfId-895307" id="pgfId-895307"></a><a name="marker-910498" id="marker-910498"></a>setcolorcell</code>
      </td>

      <td rowspan="1" colspan="1">
        <p class="CellBody"><a name="pgfId-895309" id="pgfId-895309"></a>Function:
        setcolorcell</p>

        <p class="CellBody"><a name="pgfId-895310" id="pgfId-895310"></a></p>

        <p class="CellBody"><a name="pgfId-895311" id="pgfId-895311"></a>Description of
        Function:</p>

        <p class="CellBody"><a name="pgfId-895312" id="pgfId-895312"></a> Set a
        individual color cell in the active colormap. If default is the active colormap,
        then return an error string.</p>

        <p class="CellBody"><a name="pgfId-895313" id="pgfId-895313"></a> If the the
        visul display is 16-bit, 24-bit, or 32-bit TrueColor, then a redrawing of the VCS
        Canvas is made evertime the color cell is changed.</p>

        <p class="CellBody"><a name="pgfId-895314" id="pgfId-895314"></a> Note, the user
        can only change color cells 0 through 239 and R,G,Bvalue must range from 0 to
        100. Where 0 represents no color intensity and 100 is the greatest color
        intensity.</p>
      </td>

      <td rowspan="1" colspan="1">
        <p class="CellBody"><a name="pgfId-895316" id="pgfId-895316"></a>colormap index:
        0 to 239</p>

        <p class="CellBody"><a name="pgfId-895317" id="pgfId-895317"></a>R - Red
        intensity value: 0 to 100</p>

        <p class="CellBody"><a name="pgfId-895318" id="pgfId-895318"></a>G - Green
        intensity value: 0 to 100</p>

        <p class="CellBody"><a name="pgfId-895319" id="pgfId-895319"></a>B - Blue
        intensity value: 0 to 100</p>
      </td>

      <td rowspan="1" colspan="1">
        <p class="CellBody"><a name="pgfId-895321" id="pgfId-895321"></a>Example of
        Use:</p>

        <pre style="word-break:normal;">import vcs
a=vcs.init()
a.plot(array,'default','isofill','quick')
a.setcolormap("AMIP")
a.setcolorcell(11,0,0,0)
a.setcolorcell(21,100,0,0)
a.setcolorcell(31,0,100,0)
a.setcolorcell(41,0,0,100)
a.setcolorcell(51,100,100,100)
a.setcolorcell(61,70,70,70)
</pre></td>
    </tr>

    <tr>
      <td rowspan="1" colspan="1">
        <code class=""><a name="pgfId-895333" id="pgfId-895333"></a><a name="marker-910500" id="marker-910500"></a>colormapgui</code>
      </td>

      <td rowspan="1" colspan="1">
        <p class="CellBody"><a name="pgfId-895335" id="pgfId-895335"></a>Function:
        colormapgui</p>

        <p class="CellBody"><a name="pgfId-895336" id="pgfId-895336"></a></p>

        <p class="CellBody"><a name="pgfId-895337" id="pgfId-895337"></a>Description of
        Function:</p>

        <p class="CellBody"><a name="pgfId-895338" id="pgfId-895338"></a> Run the VCS
        colormap interface.</p>

        <p class="CellBody"><a name="pgfId-895339" id="pgfId-895339"></a> The colormapgui
        command is used to bring up the VCS colormap interface. The interface is used to
        select, create, change, or remove colormaps.</p>

        <p class="CellBody"><a name="pgfId-895340" id="pgfId-895340"></a> Note:</p>

        <p class="CellBody"><a name="pgfId-895341" id="pgfId-895341"></a> The colormapgui
        GUI will only work for 8-bit 'Pseudo Color'.</p>
      </td>

      <td rowspan="1" colspan="1">
        <p class="CellBody"><a name="pgfId-895343" id="pgfId-895343"></a></p>
      </td>

      <td rowspan="1" colspan="1">
        <p class="CellBody"><a name="pgfId-895345" id="pgfId-895345"></a>Example of
        Use:</p>

        <pre style="word-break:normal;">import vcs
a=vcs.init()
a.colormapgui()
</pre></td>
    </tr>

    <tr>
      <td rowspan="1" colspan="4">
        <p class="CellHeading"><a name="pgfId-895350" id="pgfId-895350"></a>Fill Area</p>
      </td>
    </tr>

    <tr>
      <td rowspan="1" colspan="1">
        <code class=""><a name="pgfId-895358" id="pgfId-895358"></a><a name="marker-910499" id="marker-910499"></a>createfillarea</code>
      </td>

      <td rowspan="1" colspan="1">
        <p class="CellBody"><a name="pgfId-895360" id="pgfId-895360"></a>Function:
        createfillarea</p>

        <p class="CellBody"><a name="pgfId-895361" id="pgfId-895361"></a></p>

        <p class="CellBody"><a name="pgfId-895362" id="pgfId-895362"></a>Description of
        Function:</p>

        <p class="CellBody"><a name="pgfId-895363" id="pgfId-895363"></a> Create a new
        fillarea secondary method given the the name and the existing fillarea secondary
        method to copy the attributes from. If no existing fillarea secondary method name
        is given, then the default fillarea secondary method will be used as the
        secondary method to which the attributes will be copied from.</p>

        <p class="CellBody"><a name="pgfId-895364" id="pgfId-895364"></a> If the name
        provided already exists, then a error will be returned. Secondary method names
        must be unique.</p>
      </td>

      <td rowspan="1" colspan="1">
        <p class="CellBody"><a name="pgfId-895366" id="pgfId-895366"></a>new fillarea
        name</p>

        <p class="CellBody"><a name="pgfId-895367" id="pgfId-895367"></a></p>

        <p class="CellBody"><a name="pgfId-895368" id="pgfId-895368"></a>[name of
        fillarea to copy attributes from]</p>

        <p class="CellBody"><a name="pgfId-895369" id="pgfId-895369"></a></p>
      </td>

      <td rowspan="1" colspan="1">
        <p class="CellBody"><a name="pgfId-895371" id="pgfId-895371"></a>Example of
        Use:</p>

        <pre style="word-break:normal;">import vcs
a=vcs.init()
a.show('fillarea')
fa=a.createfillarea('example1',)
a.show('fillarea')
fa=a.createfillarea('example2','black')
a.show('fillarea')
</pre></td>
    </tr>

    <tr>
      <td rowspan="1" colspan="1">
        <code class=""><a name="pgfId-895380" id="pgfId-895380"></a><a name="marker-910501" id="marker-910501"></a>getfillarea</code>
      </td>

      <td rowspan="1" colspan="1">
        <p class="CellBody"><a name="pgfId-895382" id="pgfId-895382"></a>Function:
        getfillarea</p>

        <p class="CellBody"><a name="pgfId-895383" id="pgfId-895383"></a></p>

        <p class="CellBody"><a name="pgfId-895384" id="pgfId-895384"></a>Description of
        Function:</p>

        <p class="CellBody"><a name="pgfId-895385" id="pgfId-895385"></a> VCS contains a
        list of secondary methods. This function will create a fillarea class object from
        an existing VCS fillarea secondary method. If no fillarea name is given, then
        fillarea 'default' will be used.</p>

        <p class="CellBody"><a name="pgfId-895386" id="pgfId-895386"></a> Note, VCS does
        not allow the modification of `default' attribute sets. However, a `default'
        attribute set that has been copied under a different name can be modified. (See
        the createfillarea function.)</p>
      </td>

      <td rowspan="1" colspan="1">
        <p class="CellBody"><a name="pgfId-895388" id="pgfId-895388"></a>[fillarea
        name]</p>

        <p class="CellBody"><a name="pgfId-895389" id="pgfId-895389"></a></p>
      </td>

      <td rowspan="1" colspan="1">
        <p class="CellBody"><a name="pgfId-895391" id="pgfId-895391"></a>Example of
        Use:</p>

        <pre style="word-break:normal;">import vcs
a=vcs.init()
a.show('fillarea')
# Show all the existing fillarea secondary methods
fa=a.getfillarea()
# fa instance of 'default' fillarea secondary method
fa2=a.getfillarea('quick')
# fa2 instance of existing 'quick' fillarea secondary method
</pre></td>
    </tr>

    <tr>
      <td rowspan="1" colspan="1">
        <a name="pgfId-895398" id="pgfId-895398"></a>
      </td>

      <td rowspan="1" colspan="1">
        <p class="CellBody"><a name="pgfId-895400" id="pgfId-895400"></a>Object:
        fillareaobject</p>

        <p class="CellBody"><a name="pgfId-895401" id="pgfId-895401"></a></p>

        <p class="CellBody"><a name="pgfId-895402" id="pgfId-895402"></a>Description of
        Function:</p>

        <p class="CellBody"><a name="pgfId-895403" id="pgfId-895403"></a> The Fillarea
        class object allows the user to edit fillarea attributes, including</p>

        <p class="CellBody"><a name="pgfId-895404" id="pgfId-895404"></a> fillarea
        interior style, style index, and color index.</p>

        <p class="CellBody"><a name="pgfId-895405" id="pgfId-895405"></a> This class is
        used to define an fillarea table entry used in VCS, or itcan be used to change
        some or all of the fillarea attributes in an existing fillarea table entry.</p>

        <p class="CellBody"><a name="pgfId-895406" id="pgfId-895406"></a> Other Useful
        Functions:</p>

        <p class="CellBody"><a name="pgfId-895407" id="pgfId-895407"></a>a=vcs.init()<br/>
        # Constructor</p>

        <p class="CellBody"><a name="pgfId-895408" id="pgfId-895408"></a>a.show('fillarea')<br/>
        # Show predefined fillarea objects</p>

        <p class="CellBody"><a name="pgfId-895409" id="pgfId-895409"></a>a.update()<br/>
        # Updates the VCS Canvas at user's request a.mode=1, or 0<br/>
        # If 1, then automatic update, else if 0, then use update function to update the
        VCS Canvas.</p>
      </td>

      <td rowspan="1" colspan="1">
        <p class="CellBody"><a name="pgfId-895411" id="pgfId-895411"></a>name</p>

        <p class="CellBody"><a name="pgfId-905388" id="pgfId-905388"></a>style</p>

        <p class="CellBody"><a name="pgfId-905389" id="pgfId-905389"></a>index</p>

        <p class="CellBody"><a name="pgfId-905390" id="pgfId-905390"></a>color</p>
      </td>

      <td rowspan="1" colspan="1">
        <p class="CellBody"><a name="pgfId-895413" id="pgfId-895413"></a>Example of
        Use:</p>

        <pre style="word-break:normal;">import vcs
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
</pre></td>
    </tr>

    <tr>
      <td rowspan="1" colspan="4">
        <p class="CellHeading"><a name="pgfId-895450" id="pgfId-895450"></a>Line</p>
      </td>
    </tr>

    <tr>
      <td rowspan="1" colspan="1">
        <code class=""><a name="pgfId-895458" id="pgfId-895458"></a><a name="marker-910502" id="marker-910502"></a>createline</code>
      </td>

      <td rowspan="1" colspan="1">
        <p class="CellBody"><a name="pgfId-895460" id="pgfId-895460"></a>Function:
        createline</p>

        <p class="CellBody"><a name="pgfId-895461" id="pgfId-895461"></a></p>

        <p class="CellBody"><a name="pgfId-895462" id="pgfId-895462"></a>Description of
        Function:</p>

        <p class="CellBody"><a name="pgfId-895463" id="pgfId-895463"></a> Create a new
        line secondary method given the the name and the existing line secondary method
        to copy the attributes from. If no existing line secondary method name is given,
        then the default line secondary method will be used as the secondary method to
        which the attributes will be copied from.</p>

        <p class="CellBody"><a name="pgfId-895464" id="pgfId-895464"></a> If the name
        provided already exists, then a error will be returned. Secondary method names
        must be unique</p>
      </td>

      <td rowspan="1" colspan="1">
        <p class="CellBody"><a name="pgfId-895466" id="pgfId-895466"></a>new line
        name</p>

        <p class="CellBody"><a name="pgfId-895467" id="pgfId-895467"></a></p>

        <p class="CellBody"><a name="pgfId-895468" id="pgfId-895468"></a>[name of line to
        copy attributes from]</p>

        <p class="CellBody"><a name="pgfId-895469" id="pgfId-895469"></a></p>
      </td>

      <td rowspan="1" colspan="1">
        <p class="CellBody"><a name="pgfId-895471" id="pgfId-895471"></a>Example of
        Use:</p>

        <pre style="word-break:normal;">import vcs
a=vcs.init()
a.show('line')
ln=a.createline('example1',)
a.show('line')
ln=a.createline('example2','black')
a.show('line')
</pre></td>
    </tr>

    <tr>
      <td rowspan="1" colspan="1">
        <code class=""><a name="pgfId-895480" id="pgfId-895480"></a><a name="marker-910503" id="marker-910503"></a>getline</code>
      </td>

      <td rowspan="1" colspan="1">
        <p class="CellBody"><a name="pgfId-895482" id="pgfId-895482"></a>Function:
        getline</p>

        <p class="CellBody"><a name="pgfId-895483" id="pgfId-895483"></a></p>

        <p class="CellBody"><a name="pgfId-895484" id="pgfId-895484"></a>Description of
        Function:</p>

        <p class="CellBody"><a name="pgfId-895485" id="pgfId-895485"></a> VCS contains a
        list of secondary methods. This function will create a line class object from an
        existing VCS line secondary method. If no line name is given, then line 'default'
        will be used.</p>

        <p class="CellBody"><a name="pgfId-895486" id="pgfId-895486"></a> Note, VCS does
        not allow the modification of `default' attribute sets.</p>

        <p class="CellBody"><a name="pgfId-895487" id="pgfId-895487"></a> However, a
        `default' attribute set that has been copied under a different name can be
        modified. (See the createline function.)</p>
      </td>

      <td rowspan="1" colspan="1">
        <p class="CellBody"><a name="pgfId-895489" id="pgfId-895489"></a>[line name]</p>

        <p class="CellBody"><a name="pgfId-895490" id="pgfId-895490"></a></p>
      </td>

      <td rowspan="1" colspan="1">
        <p class="CellBody"><a name="pgfId-895492" id="pgfId-895492"></a>Example of
        Use:</p>

        <pre style="word-break:normal;">import vcs
a=vcs.init()
a.show('line')
# Show all the existing line secondary methods
ln=a.getline()
# ln instance of 'default' line secondary method
ln2=a.getline('quick')
# ln2 instance of existing 'quick' line secondary method
</pre></td>
    </tr>

    <tr>
      <td rowspan="1" colspan="1">
        <a name="pgfId-895499" id="pgfId-895499"></a>
      </td>

      <td rowspan="1" colspan="1">
        <p class="CellBody"><a name="pgfId-895501" id="pgfId-895501"></a>Object:
        lineobject</p>

        <p class="CellBody"><a name="pgfId-895502" id="pgfId-895502"></a></p>

        <p class="CellBody"><a name="pgfId-895503" id="pgfId-895503"></a>Description of
        Function:</p>

        <p class="CellBody"><a name="pgfId-895504" id="pgfId-895504"></a> The Line object
        allows the manipulation of line type, width, and color index.</p>

        <p class="CellBody"><a name="pgfId-895505" id="pgfId-895505"></a> This class is
        used to define an line table entry used in VCS, or itcan be used to change some
        or all of the line attributes in an existing line table entry.</p>

        <p class="CellBody"><a name="pgfId-895506" id="pgfId-895506"></a> Other Useful
        Functions:</p>

        <p class="CellBody"><a name="pgfId-895507" id="pgfId-895507"></a>a=vcs.init()<br/>
        # Constructor</p>

        <p class="CellBody"><a name="pgfId-895508" id="pgfId-895508"></a>a.show('line')<br/>
        # Show predefined line objects</p>

        <p class="CellBody"><a name="pgfId-895509" id="pgfId-895509"></a>a.update()<br/>
        # Updates the VCS Canvas at user's request a.mode=1, or 0<br/>
        # If 1, then automatic update, else if 0, then use update function to update the
        VCS Canvas.</p>
      </td>

      <td rowspan="1" colspan="1">
        <p class="CellBody"><a name="pgfId-895511" id="pgfId-895511"></a>name</p>

        <p class="CellBody"><a name="pgfId-905396" id="pgfId-905396"></a>type</p>

        <p class="CellBody"><a name="pgfId-905398" id="pgfId-905398"></a>width</p>

        <p class="CellBody"><a name="pgfId-905399" id="pgfId-905399"></a>color</p>
      </td>

      <td rowspan="1" colspan="1">
        <p class="CellBody"><a name="pgfId-895513" id="pgfId-895513"></a>Example of
        Use:</p>

        <pre style="word-break:normal;">import vcs
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

</pre></td>
    </tr>

    <tr>
      <td rowspan="1" colspan="4">
        <p class="CellHeading"><a name="pgfId-895532" id="pgfId-895532"></a>Marker</p>
      </td>
    </tr>

    <tr>
      <td rowspan="1" colspan="1">
        <code class=""><a name="pgfId-895540" id="pgfId-895540"></a><a name="marker-910504" id="marker-910504"></a>createmarker</code>
      </td>

      <td rowspan="1" colspan="1">
        <p class="CellBody"><a name="pgfId-895542" id="pgfId-895542"></a>Function:
        createmarker</p>

        <p class="CellBody"><a name="pgfId-895543" id="pgfId-895543"></a>Description of
        Function:</p>

        <p class="CellBody"><a name="pgfId-895544" id="pgfId-895544"></a> Create a new
        marker secondary method given the the name and the existing marker secondary
        method to copy the attributes from. If no existing marker secondary method name
        is given, then the default marker secondary method will be used as the secondary
        method to which the attributes will be copied from.</p>

        <p class="CellBody"><a name="pgfId-895545" id="pgfId-895545"></a> If the name
        provided already exists, then a error will be returned.</p>

        <p class="CellBody"><a name="pgfId-895546" id="pgfId-895546"></a> Secondary
        method names must be unique.</p>
      </td>

      <td rowspan="1" colspan="1">
        <p class="CellBody"><a name="pgfId-895548" id="pgfId-895548"></a>new marker
        name</p>

        <p class="CellBody"><a name="pgfId-895549" id="pgfId-895549"></a></p>

        <p class="CellBody"><a name="pgfId-895550" id="pgfId-895550"></a>[name of marker
        to copy attributes from]</p>

        <p class="CellBody"><a name="pgfId-895551" id="pgfId-895551"></a></p>
      </td>

      <td rowspan="1" colspan="1">
        <p class="CellBody"><a name="pgfId-895553" id="pgfId-895553"></a>Example of
        Use:</p>

        <pre style="word-break:normal;">import vcs
a=vcs.init()
a.show('marker')
mrk=a.createmarker('example1',)
a.show('marker')
mrk=a.createmarker('example2','black')
a.show('boxfill')
</pre></td>
    </tr>

    <tr>
      <td rowspan="1" colspan="1">
        <code class=""><a name="pgfId-895562" id="pgfId-895562"></a><a name="marker-910505" id="marker-910505"></a>getmarker</code>
      </td>

      <td rowspan="1" colspan="1">
        <p class="CellBody"><a name="pgfId-895564" id="pgfId-895564"></a>Function:
        getmarker</p>

        <p class="CellBody"><a name="pgfId-895565" id="pgfId-895565"></a></p>

        <p class="CellBody"><a name="pgfId-895566" id="pgfId-895566"></a>Description of
        Function:</p>

        <p class="CellBody"><a name="pgfId-895567" id="pgfId-895567"></a> VCS contains a
        list of secondary methods. This function will create a marker class object from
        an existing VCS marker secondary method. If no marker name is given, then marker
        'default' will be used.</p>

        <p class="CellBody"><a name="pgfId-895568" id="pgfId-895568"></a> Note, VCS does
        not allow the modification of `default' attribute sets.</p>

        <p class="CellBody"><a name="pgfId-895569" id="pgfId-895569"></a> However, a
        `default' attribute set that has been copied under a different name can be
        modified. (See the createmarker function.)</p>
      </td>

      <td rowspan="1" colspan="1">
        <p class="CellBody"><a name="pgfId-895571" id="pgfId-895571"></a>[marker
        name]</p>

        <p class="CellBody"><a name="pgfId-895572" id="pgfId-895572"></a></p>
      </td>

      <td rowspan="1" colspan="1">
        <p class="CellBody"><a name="pgfId-895574" id="pgfId-895574"></a>Example of
        Use:</p>

        <pre style="word-break:normal;">import vcs
a=vcs.init()
a.show('marker')
# Show all the existing marker secondary methods
mrk=a.getmarker()
# mrk instance of 'default' marker secondary method
mrk2=a.getmarker('quick')
# mrk2 instance of existing 'quick' marker secondary method
</pre></td>
    </tr>

    <tr>
      <td rowspan="1" colspan="1">
        <a name="pgfId-895581" id="pgfId-895581"></a>
      </td>

      <td rowspan="1" colspan="1">
        <p class="CellBody"><a name="pgfId-895583" id="pgfId-895583"></a>Object:
        markerobject</p>

        <p class="CellBody"><a name="pgfId-895584" id="pgfId-895584"></a></p>

        <p class="CellBody"><a name="pgfId-895585" id="pgfId-895585"></a>Description of
        Function:</p>

        <p class="CellBody"><a name="pgfId-895586" id="pgfId-895586"></a> The Marker
        object allows the manipulation of marker type, size, and color index.</p>

        <p class="CellBody"><a name="pgfId-895587" id="pgfId-895587"></a> This class is
        used to define an marker table entry used in VCS, or it can be used to change
        some or all of the marker attributes in an existing marker table entry.</p>

        <p class="CellBody"><a name="pgfId-895588" id="pgfId-895588"></a> Other Useful
        Functions:</p>

        <p class="CellBody"><a name="pgfId-895589" id="pgfId-895589"></a>a=vcs.init()<br/>
        # Constructor</p>

        <p class="CellBody"><a name="pgfId-895590" id="pgfId-895590"></a>a.show('marker')<br/>
        # Show predefined marker objects</p>

        <p class="CellBody"><a name="pgfId-895591" id="pgfId-895591"></a>a.update()<br/>
        # Updates the VCS Canvas at user's request a.mode=1, or 0. If 1, then automatic
        update, else if 0, then use update function to update the VCS Canvas.</p>
      </td>

      <td rowspan="1" colspan="1">
        <p class="CellBody"><a name="pgfId-895593" id="pgfId-895593"></a>name</p>

        <p class="CellBody"><a name="pgfId-905407" id="pgfId-905407"></a>type</p>

        <p class="CellBody"><a name="pgfId-905414" id="pgfId-905414"></a>size</p>

        <p class="CellBody"><a name="pgfId-905415" id="pgfId-905415"></a>color</p>
      </td>

      <td rowspan="1" colspan="1">
        <p class="CellBody"><a name="pgfId-895595" id="pgfId-895595"></a>Example of
        Use:</p>

        <pre style="word-break:normal;">import vcs
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

</pre></td>
    </tr>

    <tr>
      <td rowspan="1" colspan="4">
        <p class="CellHeading"><a name="pgfId-895626" id="pgfId-895626"></a>Text-Combined</p>
      </td>
    </tr>

    <tr>
      <td rowspan="1" colspan="1">
        <code class=""><a name="pgfId-895634" id="pgfId-895634"></a><a name="marker-910506" id="marker-910506"></a>createtextcombined</code>
      </td>

      <td rowspan="1" colspan="1">
        <p class="CellBody"><a name="pgfId-895636" id="pgfId-895636"></a>Function:
        createtextcombined</p>

        <p class="CellBody"><a name="pgfId-895637" id="pgfId-895637"></a></p>

        <p class="CellBody"><a name="pgfId-895638" id="pgfId-895638"></a>Description of
        Function:</p>

        <p class="CellBody"><a name="pgfId-895639" id="pgfId-895639"></a> Create a new
        textcombined secondary method given the the names and the existing texttable and
        textorientation secondary methods to copy the attributes from. If no existing
        texttable and textorientation secondary method names are given, then the default
        texttable and textorientation secondary methods will be used as the secondary
        method to which the attributes will be copied from.</p>

        <p class="CellBody"><a name="pgfId-895640" id="pgfId-895640"></a> If the name
        provided already exists, then a error will be returned.</p>

        <p class="CellBody"><a name="pgfId-895641" id="pgfId-895641"></a> Secondary
        method names must be unique.</p>
      </td>

      <td rowspan="1" colspan="1">
        <p class="CellBody"><a name="pgfId-895643" id="pgfId-895643"></a>new textcombined
        name</p>

        <p class="CellBody"><a name="pgfId-895644" id="pgfId-895644"></a></p>

        <p class="CellBody"><a name="pgfId-895645" id="pgfId-895645"></a>[name of
        textcombined to copy attributes from]</p>
      </td>

      <td rowspan="1" colspan="1">
        <p class="CellBody"><a name="pgfId-895647" id="pgfId-895647"></a>Example of
        Use:</p>

        <pre style="word-break:normal;">import vcs
a=vcs.init()
a.show('texttable')
a.show('textorientation')
tc=a.createtextcombined('example1','std','example1','7left')
a.show('texttable')
a.show('textorientation')
</pre></td>
    </tr>

    <tr>
      <td rowspan="1" colspan="1">
        <code class=""><a name="pgfId-895656" id="pgfId-895656"></a><a name="marker-910507" id="marker-910507"></a>gettextcombined</code>
      </td>

      <td rowspan="1" colspan="1">
        <p class="CellBody"><a name="pgfId-895658" id="pgfId-895658"></a>Function:
        gettextcombined</p>

        <p class="CellBody"><a name="pgfId-895659" id="pgfId-895659"></a></p>

        <p class="CellBody"><a name="pgfId-895660" id="pgfId-895660"></a>Description of
        Function:</p>

        <p class="CellBody"><a name="pgfId-895661" id="pgfId-895661"></a> VCS contains a
        list of secondary methods. This function will create a textcombined class object
        from an existing VCS texttable secondary method and an existing VCS
        textorientation secondary method. If no texttable or textorientation names are
        given, then the 'default' names will be used in both cases.</p>

        <p class="CellBody"><a name="pgfId-895662" id="pgfId-895662"></a> Note, VCS does
        not allow the modification of `default' attribute sets.</p>

        <p class="CellBody"><a name="pgfId-895663" id="pgfId-895663"></a> However, a
        `default' attribute set that has been copied under a different name can be
        modified. (See the createtextcombined function.)</p>
      </td>

      <td rowspan="1" colspan="1">
        <p class="CellBody"><a name="pgfId-895665" id="pgfId-895665"></a>[textcombined
        name]</p>

        <p class="CellBody"><a name="pgfId-895666" id="pgfId-895666"></a></p>
      </td>

      <td rowspan="1" colspan="1">
        <p class="CellBody"><a name="pgfId-895668" id="pgfId-895668"></a>Example of
        Use:</p>

        <pre style="word-break:normal;">import vcs
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
</pre></td>
    </tr>

    <tr>
      <td rowspan="1" colspan="1">
        <a name="pgfId-895678" id="pgfId-895678"></a>
      </td>

      <td rowspan="1" colspan="1">
        <p class="CellBody"><a name="pgfId-895680" id="pgfId-895680"></a>Object:
        textcombinedobject</p>

        <p class="CellBody"><a name="pgfId-895681" id="pgfId-895681"></a></p>

        <p class="CellBody"><a name="pgfId-895682" id="pgfId-895682"></a>Description of
        Function:</p>

        <p class="CellBody"><a name="pgfId-895683" id="pgfId-895683"></a> The (Tc) Text
        Combined class will combine a text table class and a text orientation class
        together. From combining the two classess, the user will be able to set
        attributes for both classes (i.e., define the font, spacing, expansion, color
        index, height, angle, path, vertical alignment, and horizontal alignment).</p>

        <p class="CellBody"><a name="pgfId-895684" id="pgfId-895684"></a> This class is
        used to define and list a combined text table and text orientation</p>

        <p class="CellBody"><a name="pgfId-895685" id="pgfId-895685"></a> entry used in
        VCS.</p>
      </td>

      <td rowspan="1" colspan="1">
        <p class="CellBody"><a name="pgfId-895687" id="pgfId-895687"></a>name</p>

        <p class="CellBody"><a name="pgfId-905428" id="pgfId-905428"></a>font</p>

        <p class="CellBody"><a name="pgfId-905429" id="pgfId-905429"></a>spacing</p>

        <p class="CellBody"><a name="pgfId-905430" id="pgfId-905430"></a>expansion</p>

        <p class="CellBody"><a name="pgfId-905431" id="pgfId-905431"></a>color</p>

        <p class="CellBody"><a name="pgfId-905432" id="pgfId-905432"></a>name</p>

        <p class="CellBody"><a name="pgfId-905433" id="pgfId-905433"></a>height</p>

        <p class="CellBody"><a name="pgfId-905434" id="pgfId-905434"></a>angel</p>

        <p class="CellBody"><a name="pgfId-905435" id="pgfId-905435"></a>path</p>

        <p class="CellBody"><a name="pgfId-905436" id="pgfId-905436"></a>halign</p>

        <p class="CellBody"><a name="pgfId-905437" id="pgfId-905437"></a>valign</p>
      </td>

      <td rowspan="1" colspan="1">
        <p class="CellBody"><a name="pgfId-895689" id="pgfId-895689"></a>Example of
        Use:</p>

        <pre style="word-break:normal;">import vcs
a=vcs.init()

# To Create a new instance of text table use:
tc=a.createtextcombined('new_tt','std','new_to','7left')
# Copies content of 'std' to 'new_tt' and '7left' to 'new_to'


# To Modify an existing texttable use:
tc=a.gettextcombined('std','7left')
tc.list()
# Will list all the textcombined attribute values (i.e., texttable and textorientation attributes

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
</pre></td>
    </tr>

    <tr>
      <td rowspan="1" colspan="4">
        <p class="CellHeading"><a name="pgfId-895726" id="pgfId-895726"></a>Text-Orientation</p>
      </td>
    </tr>

    <tr>
      <td rowspan="1" colspan="1">
        <code class=""><a name="pgfId-895734" id="pgfId-895734"></a><a name="marker-910508" id="marker-910508"></a>createtextorientation</code>
      </td>

      <td rowspan="1" colspan="1">
        <p class="CellBody"><a name="pgfId-895736" id="pgfId-895736"></a>Function:
        createtextorientation</p>

        <p class="CellBody"><a name="pgfId-895737" id="pgfId-895737"></a></p>

        <p class="CellBody"><a name="pgfId-895738" id="pgfId-895738"></a>Description of
        Function:</p>

        <p class="CellBody"><a name="pgfId-895739" id="pgfId-895739"></a> Create a new
        textorientation secondary method given the the name and he existing
        textorientation secondary method to copy the attributes from. If no existing
        textorientation secondary method name is given, then the default textorientation
        secondary method will be used as the secondary method to which the attributes
        will be copied from.</p>

        <p class="CellBody"><a name="pgfId-895740" id="pgfId-895740"></a> If the name
        provided already exists, then a error will be returned.</p>

        <p class="CellBody"><a name="pgfId-895741" id="pgfId-895741"></a> Secondary
        method names must be unique.</p>
      </td>

      <td rowspan="1" colspan="1">
        <p class="CellBody"><a name="pgfId-895743" id="pgfId-895743"></a>new
        textorientation name</p>

        <p class="CellBody"><a name="pgfId-895744" id="pgfId-895744"></a></p>

        <p class="CellBody"><a name="pgfId-895745" id="pgfId-895745"></a>[name of
        textorientation to copy attributes from]</p>

        <p class="CellBody"><a name="pgfId-895746" id="pgfId-895746"></a></p>
      </td>

      <td rowspan="1" colspan="1">
        <p class="CellBody"><a name="pgfId-895748" id="pgfId-895748"></a>Example of
        Use:</p>

        <pre style="word-break:normal;">import vcs
a=vcs.init()
a.show('textorientation')
to=a.createtextorientation('example1')
a.show('textorientation')
to=a.createtextorientation('example2','black')
a.show('textorientation')
</pre></td>
    </tr>

    <tr>
      <td rowspan="1" colspan="1">
        <code class=""><a name="pgfId-895757" id="pgfId-895757"></a><a name="marker-910509" id="marker-910509"></a>gettextorientation</code>
      </td>

      <td rowspan="1" colspan="1">
        <p class="CellBody"><a name="pgfId-895759" id="pgfId-895759"></a>Function:
        gettextorientation</p>

        <p class="CellBody"><a name="pgfId-895760" id="pgfId-895760"></a></p>

        <p class="CellBody"><a name="pgfId-895761" id="pgfId-895761"></a>Description of
        Function:</p>

        <p class="CellBody"><a name="pgfId-895762" id="pgfId-895762"></a> VCS contains a
        list of secondary methods. This function will create a textorientation class
        object from an existing VCS textorientation secondary method. If no
        textorientation name is given, then textorientation 'default' will be used.</p>

        <p class="CellBody"><a name="pgfId-895763" id="pgfId-895763"></a> Note, VCS does
        not allow the modification of `default' attribute sets.</p>

        <p class="CellBody"><a name="pgfId-895764" id="pgfId-895764"></a> However, a
        `default' attribute set that has been copied under a different name can be
        modified. (See the createtextorientation function.)</p>
      </td>

      <td rowspan="1" colspan="1">
        <p class="CellBody"><a name="pgfId-895766" id="pgfId-895766"></a>[textorientation
        name]</p>

        <p class="CellBody"><a name="pgfId-895767" id="pgfId-895767"></a></p>
      </td>

      <td rowspan="1" colspan="1">
        <p class="CellBody"><a name="pgfId-895769" id="pgfId-895769"></a>Example of
        Use:</p>

        <pre style="word-break:normal;">import vcs
a=vcs.init()
a.show('textorientation')
# Show all the existing textorientation secondary methods
to=a.gettextorientation()
# to instance of 'default' textorientation secondary method
to2=a.gettextorientation('quick')
# to2 instance of existing 'quick' textorientation secondary method
</pre></td>
    </tr>

    <tr>
      <td rowspan="1" colspan="1">
        <a name="pgfId-895776" id="pgfId-895776"></a>
      </td>

      <td rowspan="1" colspan="1">
        <p class="CellBody"><a name="pgfId-895778" id="pgfId-895778"></a>Object:
        textorientationobject</p>

        <p class="CellBody"><a name="pgfId-895779" id="pgfId-895779"></a></p>

        <p class="CellBody"><a name="pgfId-895780" id="pgfId-895780"></a>Description of
        Function:</p>

        <p class="CellBody"><a name="pgfId-895781" id="pgfId-895781"></a> The (To) Text
        Orientation lists text attribute set names that define the font, spacing,
        expansion, and color index.</p>

        <p class="CellBody"><a name="pgfId-895782" id="pgfId-895782"></a> This class is
        used to define an text orientation table entry used in VCS, or it can be used to
        change some or all of the text orientation attributes in an existing text
        orientation table entry.</p>

        <p class="CellBody"><a name="pgfId-895783" id="pgfId-895783"></a> Other Useful
        Functions:</p>

        <p class="CellBody"><a name="pgfId-895784" id="pgfId-895784"></a>a=vcs.init()<br/>
        # Constructor</p>

        <p class="CellBody"><a name="pgfId-895785" id="pgfId-895785"></a>a.show('textorientation')<br/>
        # Show predefined text orientation objects</p>

        <p class="CellBody"><a name="pgfId-895786" id="pgfId-895786"></a>a.update()<br/>
        # Updates the VCS Canvas at user's request a.mode=1, or 0. If 1, then automatic
        update, else if 0, then use update function to update the VCS Canvas.</p>
      </td>

      <td rowspan="1" colspan="1">
        <p class="CellBody"><a name="pgfId-895788" id="pgfId-895788"></a>name</p>

        <p class="CellBody"><a name="pgfId-905443" id="pgfId-905443"></a>height</p>

        <p class="CellBody"><a name="pgfId-905444" id="pgfId-905444"></a>angel</p>

        <p class="CellBody"><a name="pgfId-905445" id="pgfId-905445"></a>path</p>

        <p class="CellBody"><a name="pgfId-905446" id="pgfId-905446"></a>halign</p>

        <p class="CellBody"><a name="pgfId-905447" id="pgfId-905447"></a>valign</p>
      </td>

      <td rowspan="1" colspan="1">
        <p class="CellBody"><a name="pgfId-895790" id="pgfId-895790"></a>Example of
        Use:</p>

        <pre style="word-break:normal;">import vcs
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
</pre></td>
    </tr>

    <tr>
      <td rowspan="1" colspan="4">
        <p class="CellHeading"><a name="pgfId-895819" id="pgfId-895819"></a>Text-Table</p>
      </td>
    </tr>

    <tr>
      <td rowspan="1" colspan="1">
        <code class=""><a name="pgfId-895827" id="pgfId-895827"></a><a name="marker-910510" id="marker-910510"></a>createtexttable</code>
      </td>

      <td rowspan="1" colspan="1">
        <p class="CellBody"><a name="pgfId-895829" id="pgfId-895829"></a>Function:
        createtexttable</p>

        <p class="CellBody"><a name="pgfId-895830" id="pgfId-895830"></a></p>

        <p class="CellBody"><a name="pgfId-895831" id="pgfId-895831"></a>Description of
        Function:</p>

        <p class="CellBody"><a name="pgfId-895832" id="pgfId-895832"></a> Create a new
        texttable secondary method given the the name and the existing texttable
        secondary method to copy the attributes from. If no existing texttable secondary
        method name is given, then the default texttable secondary method will be used as
        the secondary method to which the attributes will be copied from.</p>

        <p class="CellBody"><a name="pgfId-895833" id="pgfId-895833"></a> If the name
        provided already exists, then a error will be returned.</p>

        <p class="CellBody"><a name="pgfId-895834" id="pgfId-895834"></a> Secondary
        method names must be unique.</p>
      </td>

      <td rowspan="1" colspan="1">
        <p class="CellBody"><a name="pgfId-895836" id="pgfId-895836"></a>new texttable
        name</p>

        <p class="CellBody"><a name="pgfId-895837" id="pgfId-895837"></a></p>

        <p class="CellBody"><a name="pgfId-895838" id="pgfId-895838"></a>[name of
        texttable to copy attributes from]</p>

        <p class="CellBody"><a name="pgfId-895839" id="pgfId-895839"></a></p>
      </td>

      <td rowspan="1" colspan="1">
        <p class="CellBody"><a name="pgfId-895841" id="pgfId-895841"></a>Example of
        Use:</p>

        <pre style="word-break:normal;">import vcs
a=vcs.init()
a.show('texttable')
tt=a.createtexttable('example1',)
a.show('texttable')
tt=a.createtexttable('example2','black')
a.show('texttable')
</pre></td>
    </tr>

    <tr>
      <td rowspan="1" colspan="1">
        <code class=""><a name="pgfId-895850" id="pgfId-895850"></a><a name="marker-910511" id="marker-910511"></a>gettexttable</code>
      </td>

      <td rowspan="1" colspan="1">
        <p class="CellBody"><a name="pgfId-895852" id="pgfId-895852"></a>Function:
        gettexttable</p>

        <p class="CellBody"><a name="pgfId-895853" id="pgfId-895853"></a></p>

        <p class="CellBody"><a name="pgfId-895854" id="pgfId-895854"></a>Description of
        Function:</p>

        <p class="CellBody"><a name="pgfId-895855" id="pgfId-895855"></a> VCS contains a
        list of secondary methods. This function will create a texttable class object
        from an existing VCS texttable secondary method. If no texttable name is given,
        then texttable 'default' will be used.</p>

        <p class="CellBody"><a name="pgfId-895856" id="pgfId-895856"></a> Note, VCS does
        not allow the modification of `default' attribute sets.</p>

        <p class="CellBody"><a name="pgfId-895857" id="pgfId-895857"></a> However, a
        `default' attribute set that has been copied under a different name can be
        modified. (See the createtexttable function.)</p>
      </td>

      <td rowspan="1" colspan="1">
        <p class="CellBody"><a name="pgfId-905460" id="pgfId-905460"></a>[texttable
        name]</p>

        <p class="CellBody"><a name="pgfId-895859" id="pgfId-895859"></a></p>
      </td>

      <td rowspan="1" colspan="1">
        <p class="CellBody"><a name="pgfId-895861" id="pgfId-895861"></a>Example of
        Use:</p>

        <pre style="word-break:normal;">import vcs
a=vcs.init()
a.show('texttable')
# Show all the existing texttable secondary methods
tt=a.gettexttable()
# tt instance of 'default' texttable secondary method
tt2=a.gettexttable('quick')
# tt2 instance of existing 'quick' texttable secondary method
</pre></td>
    </tr>

    <tr>
      <td rowspan="1" colspan="1">
        <a name="pgfId-895868" id="pgfId-895868"></a>
      </td>

      <td rowspan="1" colspan="1">
        <p class="CellBody"><a name="pgfId-895870" id="pgfId-895870"></a>Object:
        texttableobject</p>

        <p class="CellBody"><a name="pgfId-895871" id="pgfId-895871"></a></p>

        <p class="CellBody"><a name="pgfId-895872" id="pgfId-895872"></a>Description of
        Function:</p>

        <p class="CellBody"><a name="pgfId-895873" id="pgfId-895873"></a> The (Tt) Text
        Table lists text attribute set names that define the font, spacing, expansion,
        and color index.</p>

        <p class="CellBody"><a name="pgfId-895874" id="pgfId-895874"></a> This class is
        used to define an text table table entry used in VCS, or it can be used to change
        some or all of the text table attributes in an existing text table table
        entry.</p>

        <p class="CellBody"><a name="pgfId-895875" id="pgfId-895875"></a> Other Useful
        Functions:</p>

        <p class="CellBody"><a name="pgfId-895876" id="pgfId-895876"></a>a=vcs.init()<br/>
        # Constructor</p>

        <p class="CellBody"><a name="pgfId-895877" id="pgfId-895877"></a>a.show('texttable')<br/>
        # Show predefined text table objects</p>

        <p class="CellBody"><a name="pgfId-895878" id="pgfId-895878"></a>a.update()<br/>
        # Updates the VCS Canvas at user's request a.mode=1, or 0. If 1, then automatic
        update, else if 0, then use update function to update the VCS Canvas.</p>
      </td>

      <td rowspan="1" colspan="1">
        <p class="CellBody"><a name="pgfId-895881" id="pgfId-895881"></a>name</p>

        <p class="CellBody"><a name="pgfId-905453" id="pgfId-905453"></a>font</p>

        <p class="CellBody"><a name="pgfId-905454" id="pgfId-905454"></a>spacing</p>

        <p class="CellBody"><a name="pgfId-905455" id="pgfId-905455"></a>expansion</p>

        <p class="CellBody"><a name="pgfId-905456" id="pgfId-905456"></a>color</p>
      </td>

      <td rowspan="1" colspan="1">
        <p class="CellBody"><a name="pgfId-895883" id="pgfId-895883"></a>Example of
        Use:</p>

        <pre style="word-break:normal;">import vcs
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
</pre></td>
    </tr>

    <tr>
      <td rowspan="1" colspan="4">
        <p class="CellHeading"><a name="pgfId-895901" id="pgfId-895901"></a>Remove
        Objects</p>
      </td>
    </tr>

    <tr>
      <td rowspan="1" colspan="1">
        <code class=""><a name="pgfId-895909" id="pgfId-895909"></a><a name="marker-910512" id="marker-910512"></a>removeobject</code>
      </td>

      <td rowspan="1" colspan="1">
        <p class="CellBody"><a name="pgfId-895911" id="pgfId-895911"></a>Function:
        removeobject</p>

        <p class="CellBody"><a name="pgfId-895912" id="pgfId-895912"></a></p>

        <p class="CellBody"><a name="pgfId-895913" id="pgfId-895913"></a>Description of
        Function:</p>

        <p class="CellBody"><a name="pgfId-895914" id="pgfId-895914"></a> The user has
        the ability to create primary and secondary class objects. This function allows
        the user to remove these objects from the appropriate class list.</p>

        <p class="CellBody"><a name="pgfId-895915" id="pgfId-895915"></a> Note, To remove
        the object completely from Python, remember to use the "del" function.</p>

        <p class="CellBody"><a name="pgfId-895916" id="pgfId-895916"></a> Also note, The
        user is not allowed to remove a "default" class object.</p>
      </td>

      <td rowspan="1" colspan="1">
        <p class="CellBody"><a name="pgfId-895918" id="pgfId-895918"></a>object</p>
      </td>

      <td rowspan="1" colspan="1">
        <p class="CellBody"><a name="pgfId-895920" id="pgfId-895920"></a>Example of
        Use:</p>

        <pre style="word-break:normal;">import vcs
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
</pre></td>
    </tr>

    <tr>
      <td rowspan="1" colspan="4">
        <p class="CellHeading"><a name="pgfId-895931" id="pgfId-895931"></a>Set
        Continents Type</p>
      </td>
    </tr>

    <tr>
      <td rowspan="1" colspan="1">
        <code class=""><a name="pgfId-895939" id="pgfId-895939"></a><a name="marker-910413" id="marker-910413"></a>setcontinentstype</code>
      </td>

      <td rowspan="1" colspan="1">
        <p class="CellBody"><a name="pgfId-895941" id="pgfId-895941"></a>Function:
        setcontinentstype</p>

        <p class="CellBody"><a name="pgfId-895942" id="pgfId-895942"></a></p>

        <p class="CellBody"><a name="pgfId-895943" id="pgfId-895943"></a>Description of
        Function:</p>

        <p class="CellBody"><a name="pgfId-895944" id="pgfId-895944"></a> One has the
        option of using continental maps that are predefined or that are user-defined.
        Predefined continental maps are either internal to VCS or are specified by
        external files. User-defined continental maps are specified by additional
        external files that must be read as input.</p>

        <p class="CellBody"><a name="pgfId-900450" id="pgfId-900450"></a> The
        continents-type values are integers ranging from 0 to 11, where:</p>

        <p class="CellBody"><a name="pgfId-900451" id="pgfId-900451"></a> 0 signifies "No
        Continents"</p>

        <p class="CellBody"><a name="pgfId-900452" id="pgfId-900452"></a> 1 signifies
        "Fine Continents"</p>

        <p class="CellBody"><a name="pgfId-900453" id="pgfId-900453"></a> 2 signifies
        "Coarse Continents"</p>

        <p class="CellBody"><a name="pgfId-900454" id="pgfId-900454"></a> 3 signifies
        "United States" (with "Fine Continents")</p>

        <p class="CellBody"><a name="pgfId-900455" id="pgfId-900455"></a> 4 signifies
        "Political Borders" (with "Fine Continents")</p>

        <p class="CellBody"><a name="pgfId-900456" id="pgfId-900456"></a> 5 signifies
        "Rivers" (with "Fine Continents")</p>

        <p class="CellBody"><a name="pgfId-900458" id="pgfId-900458"></a> Values 6
        through 11 signify the line type defined by the files</p>

        <p class="CellBody"><a name="pgfId-900459" id="pgfId-900459"></a>
        data_continent_other7 through data_continent_other12.</p>
      </td>

      <td rowspan="1" colspan="1">
        <p class="CellBody"><a name="pgfId-895948" id="pgfId-895948"></a>continents type
        number, ranging from 0 to 11</p>
      </td>

      <td rowspan="1" colspan="1">
        <p class="CellBody"><a name="pgfId-895950" id="pgfId-895950"></a>Example of
        Use:</p>

        <pre style="word-break:normal;">import vcs
a=vcs.init()
# Set continents to "United States"
a.setcontinentstype(3)
a.plot(array,'default','isofill','quick'
</pre></td>
    </tr>

    <tr>
      <td rowspan="1" colspan="4">
        <p class="CellHeading"><a name="pgfId-900429" id="pgfId-900429"></a>Set Default
        Picture Template and Graphics Methods</p>
      </td>
    </tr>

    <tr>
      <td rowspan="1" colspan="1">
        <code class=""><a name="pgfId-900412" id="pgfId-900412"></a><a name="marker-910412" id="marker-910412"></a>set</code>
      </td>

      <td rowspan="1" colspan="1">
        <p class="CellBody"><a name="pgfId-900414" id="pgfId-900414"></a>Function:
        set</p>

        <p class="CellBody"><a name="pgfId-900415" id="pgfId-900415"></a></p>

        <p class="CellBody"><a name="pgfId-900416" id="pgfId-900416"></a>Description of
        Function:</p>

        <p class="CellBody"><a name="pgfId-900417" id="pgfId-900417"></a> Set the default
        VCS primary class objects: template and graphics methods.</p>

        <p class="CellBody"><a name="pgfId-900418" id="pgfId-900418"></a> Keep in mind
        the template, determines the appearance of each graphics segment; the graphic
        method specifies the display technique; and the data defines what is to be
        displayed. Note, the data cannot be set with this function.</p>
      </td>

      <td rowspan="1" colspan="1">
        <p class="CellBody"><a name="pgfId-900420" id="pgfId-900420"></a>template or
        graphics methods type,</p>

        <p class="CellBody"><a name="pgfId-900421" id="pgfId-900421"></a>[template name
        or graphics method name]</p>
      </td>

      <td rowspan="1" colspan="1">
        <p class="CellBody"><a name="pgfId-900423" id="pgfId-900423"></a>Example of
        Use:</p>

        <pre style="word-break:normal;">import vcs
a=vcs.init()
a.set('isofill','quick')
# Changes the default graphics method to Isofill: 'quick'
a.plot(array)
</pre></td>
    </tr>

    <tr>
      <td rowspan="1" colspan="4">
        <p class="CellHeading"><a name="pgfId-895956" id="pgfId-895956"></a>Animation</p>
      </td>
    </tr>

    <tr>
      <td rowspan="1" colspan="1">
        <code class=""><a name="pgfId-895964" id="pgfId-895964"></a><a name="marker-910411" id="marker-910411"></a>animate</code>
      </td>

      <td rowspan="1" colspan="1">
        <p class="CellBody"><a name="pgfId-895966" id="pgfId-895966"></a>Function:
        animate</p>

        <p class="CellBody"><a name="pgfId-895967" id="pgfId-895967"></a></p>

        <p class="CellBody"><a name="pgfId-895968" id="pgfId-895968"></a>Description of
        Function:</p>

        <p class="CellBody"><a name="pgfId-895969" id="pgfId-895969"></a> Animate the
        contents of the VCS Canvas. Currently, only one display can be shown in the VCS
        Canvas for the animation to work. This function pops up the animation GUI.</p>

        <p class="CellBody"><a name="pgfId-895970" id="pgfId-895970"></a> Note:</p>

        <p class="CellBody"><a name="pgfId-895971" id="pgfId-895971"></a> The animation
        GUI will only work for 8-bit 'Pseudo Color'.</p>

        <p class="CellBody"><a name="pgfId-895972" id="pgfId-895972"></a> See the
        animation GUI documenation located at URL:</p>

        <p class="CellBody"><a name="pgfId-895973" id="pgfId-895973"></a>
        http://www-pcmdi.llnl.gov/software/vcs</p>
      </td>

      <td rowspan="1" colspan="1">
        <p class="CellBody"><a name="pgfId-895975" id="pgfId-895975"></a></p>
      </td>

      <td rowspan="1" colspan="1">
        <p class="CellBody"><a name="pgfId-895977" id="pgfId-895977"></a>Example of
        Use:</p>

        <pre style="word-break:normal;">import vcs
a=vcs.init()
a.plot(array,'default','isofill','quick')
a.animate()
</pre></td>
    </tr>

    <tr>
      <td rowspan="1" colspan="4">
        <p class="CellHeading"><a name="pgfId-895983" id="pgfId-895983"></a>Flush</p>
      </td>
    </tr>

    <tr>
      <td rowspan="1" colspan="1">
        <code class=""><a name="pgfId-895991" id="pgfId-895991"></a><a name="marker-910513" id="marker-910513"></a>flush</code>
      </td>

      <td rowspan="1" colspan="1">
        <p class="CellBody"><a name="pgfId-895993" id="pgfId-895993"></a>Function:
        flush</p>

        <p class="CellBody"><a name="pgfId-895994" id="pgfId-895994"></a></p>

        <p class="CellBody"><a name="pgfId-895995" id="pgfId-895995"></a>Description of
        Function:</p>

        <p class="CellBody"><a name="pgfId-895996" id="pgfId-895996"></a> The flush
        command executes all buffered X events in the que.</p>
      </td>

      <td rowspan="1" colspan="1">
        <p class="CellBody"><a name="pgfId-895998" id="pgfId-895998"></a></p>
      </td>

      <td rowspan="1" colspan="1">
        <p class="CellBody"><a name="pgfId-896000" id="pgfId-896000"></a>Example of
        Use:</p>

        <pre style="word-break:normal;">import vcs
a=vcs.init()
a.plot(array,'default','isofill','quick')
a.flush()
</pre></td>
    </tr>

    <tr>
      <td rowspan="1" colspan="4">
        <p class="CellHeading"><a name="pgfId-900261" id="pgfId-900261"></a>Grid</p>
      </td>
    </tr>

    <tr>
      <td rowspan="1" colspan="1">
        <code class=""><a name="pgfId-900246" id="pgfId-900246"></a><a name="marker-910514" id="marker-910514"></a>grid</code>
      </td>

      <td rowspan="1" colspan="1">
        <p class="CellBody"><a name="pgfId-900248" id="pgfId-900248"></a>Function:
        grid</p>

        <p class="CellBody"><a name="pgfId-900249" id="pgfId-900249"></a></p>

        <p class="CellBody"><a name="pgfId-900250" id="pgfId-900250"></a>Description of
        Function:</p>

        <p class="CellBody"><a name="pgfId-900251" id="pgfId-900251"></a> Set the default
        plotting region for variables that have more dimension values than the graphics
        method. This will also be used for animating plots over the third and fourth
        dimensions.</p>
      </td>

      <td rowspan="1" colspan="1">
        <p class="CellBody"><a name="pgfId-900253" id="pgfId-900253"></a>([first dim's
        1st value, first dim's last value] ,..., [last dim's 1st value, last dim's last
        value]</p>
      </td>

      <td rowspan="1" colspan="1">
        <p class="CellBody"><a name="pgfId-900255" id="pgfId-900255"></a>Example of
        Use:</p>

        <pre style="word-break:normal;">import vcs
a=vcs.init()
a=vcs.init()
a.grid(12,24, -70,70, -150,150)
a.plot(array,'default','isofill','quick')
</pre></td>
    </tr>

    <tr>
      <td rowspan="1" colspan="1">
        <code class=""><a name="pgfId-900360" id="pgfId-900360"></a><a name="marker-910515" id="marker-910515"></a>resetgrid</code>
      </td>

      <td rowspan="1" colspan="1">
        <p class="CellBody"><a name="pgfId-900362" id="pgfId-900362"></a>Function:
        resetgrid</p>

        <p class="CellBody"><a name="pgfId-900363" id="pgfId-900363"></a></p>

        <p class="CellBody"><a name="pgfId-900364" id="pgfId-900364"></a>Description of
        Function:</p>

        <p class="CellBody"><a name="pgfId-900365" id="pgfId-900365"></a> Set the
        plotting region to default values. That is, let the variable's dimension values
        determine the grid</p>
      </td>

      <td rowspan="1" colspan="1">
        <p class="CellBody"><a name="pgfId-900367" id="pgfId-900367"></a></p>
      </td>

      <td rowspan="1" colspan="1">
        <p class="CellBody"><a name="pgfId-900369" id="pgfId-900369"></a>Example of
        Use:</p>

        <pre style="word-break:normal;">import vcs
a=vcs.init()
a=vcs.init()
a.resetgrid()
a.plot(array,'default','isofill','quick')
</pre></td>
    </tr>
  </table>



[Main](vcs.html) \| [Previous](vcs-4.html) \| [Next](vcs-6.html)


