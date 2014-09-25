---
layout: default
title: VCS Chapter 7
---
##  CHAPTER 7 VCS Secondary Objects

Secondary objects help to specify and define primary objects in VCS. The list
of secondary objects include: colormap, fill area, format, line, marker, list,
text-combined, text-orientation, and text-table. Note, although the colormap
is considered a secondary object, it is acessed differenly. Therefore, the
colormap object will not be described below. See the [VCS Command Reference
Guide](vcs-5.html) for colormap commands.

**Note**, to see the list of object attributes, use the list() function. For
example:

~~~ python
import vcs

a=vcs.init()

ln=a.createline(`new')
ln.list() # This call will list the line attributes and their values

tt=a.createtexttable(`new')
tt.list() # This call will list the text-table attributes and their values
~~~

<table class="table">
    <tr>
      <th rowspan="1" colspan="1">
        <p class="CellHeading"><a name="pgfId-904170" id="pgfId-904170"></a>Attributes
        (or Members)</p>
      </th>

      <th rowspan="1" colspan="1">
        <p class="CellHeading"><a name="pgfId-904172" id="pgfId-904172"></a>Exception
        Type(s)</p>
      </th>
    </tr>

    <tr>
      <td><strong class="CellBody">Object:&nbsp;<a name="pgfId-904174" id=
      "pgfId-904174"></a>fillarea</strong></td>

      <td class="CellBody"><a name="pgfId-904175" id="pgfId-904175"></a>(graphics method
      class name is Tf)</td>
    </tr>

    <tr>
      <td><code>name</code></td>

      <td>StringType</td>
    </tr>

    <tr>
      <td><code>style</code></td>

      <td>Either: 'solid', 'hatch', 'pattern'</td>
    </tr>

    <tr>
      <td><code>index</code></td>

      <td>IntType: (Range 1 to 20)</td>
    </tr>

    <tr>
      <td><code>color</code></td>

      <td>IntType: (Range 0 to 255)</td>
    </tr>

    <tr>
      <td><strong class="CellBody">Object:&nbsp;<a name="pgfId-904188" id=
      "pgfId-904188"></a>line</strong></td>

      <td class="CellBody"><a name="pgfId-904189" id="pgfId-904189"></a>(graphics method
      class name is Tl)</td>
    </tr>

    <tr>
      <td><code>name</code></td>

      <td>StringType</td>
    </tr>

    <tr>
      <td><code>type</code></td>

      <td>Either: 'solid', 'dash', 'dot', 'dash-dot', 'long-dash', 0, 1, 2, 3, 4</td>
    </tr>

    <tr>
      <td><code>width</code></td>

      <td>IntType: (Range 1 to 300)</td>
    </tr>

    <tr>
      <td><code>color</code></td>

      <td>IntType: (Range 0 to 255)</td>
    </tr>

    <tr>
      <td><strong class="CellBody">Object:&nbsp;<a name="pgfId-904203" id=
      "pgfId-904203"></a>marker</strong></td>

      <td class="CellBody"><a name="pgfId-904204" id="pgfId-904204"></a>(graphics method
      class name is Tm)</td>
    </tr>

    <tr>
      <td><code>name</code></td>

      <td>StringType</td>
    </tr>

    <tr>
      <td><code>type</code></td>

      <td>Either: "dot", "plus", "star", "circle", "cross", "diamond", "triangle_up",
      "triangle_down", "triangle_left", "triangle_right", "square", "diamond_fill",
      "triangle_up_fill", "triangle_down_fill", "triangle_left_fill",
      "triangle_right_fill", "square_fill", 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13,
      14, 15, 16, 17</td>
    </tr>

    <tr>
      <td><code>size</code></td>

      <td>IntType: (Range 1 to 300)</td>
    </tr>

    <tr>
      <td><code>color</code></td>

      <td>IntType: (Range 0 to 255)</td>
    </tr>

    <tr>
      <td><strong class="CellBody">Object:&nbsp;<a name="pgfId-904228" id=
      "pgfId-904228"></a>text-combined</strong></td>

      <td class="CellBody"><a name="pgfId-904229" id="pgfId-904229"></a>(graphics method
      class name is Tc)</td>
    </tr>

    <tr>
      <td><code>name</code></td>

      <td>StringType</td>
    </tr>

    <tr>
      <td><code>font</code></td>

      <td>IntType: (Range 1 to 9)</td>
    </tr>

    <tr>
      <td><code>spacing</code></td>

      <td>IntType: (Range -50 to 50)</td>
    </tr>

    <tr>
      <td><code>expansion</code></td>

      <td>IntType: (Range 50 to 150)</td>
    </tr>

    <tr>
      <td><code>color</code></td>

      <td>IntType: (Range 0 to 255)</td>
    </tr>

    <tr>
      <td><code>name</code></td>

      <td>StringType</td>
    </tr>

    <tr>
      <td><code>height</code></td>

      <td>IntType: (Range 1 to 100)</td>
    </tr>

    <tr>
      <td><code>angel</code></td>

      <td>IntType: (Range 0 to 360)</td>
    </tr>

    <tr>
      <td><code>path</code></td>

      <td>Either: 'right', 'left', 'up', 'down', 0, 1, 2, 3</td>
    </tr>

    <tr>
      <td><code>halign</code></td>

      <td>Either: 'left', 'center', 'right', 0, 1, 2</td>
    </tr>

    <tr>
      <td><code>valign</code></td>

      <td>Either: 'top', 'cap', 'half', 'base', 'bottom', 0, 1, 2, 3, 4</td>
    </tr>

    <tr>
      <td><strong class="CellBody">Object:&nbsp;<a name="pgfId-904256" id=
      "pgfId-904256"></a>text-orientation</strong></td>

      <td class="CellBody"><a name="pgfId-904257" id="pgfId-904257"></a>(graphics method
      class name is To)</td>
    </tr>

    <tr>
      <td><code>name</code></td>

      <td>StringType</td>
    </tr>

    <tr>
      <td><code>height</code></td>

      <td>IntType: (Range 1 to 100)</td>
    </tr>

    <tr>
      <td><code>angle</code></td>

      <td>IntType: (Range 0 to 360)</td>
    </tr>

    <tr>
      <td><code>path</code></td>

      <td>Either: 'right', 'left', 'up', 'down', 0, 1, 2, 3</td>
    </tr>

    <tr>
      <td><code>halign</code></td>

      <td>Either: 'left', 'center', 'right', 0, 1, 2</td>
    </tr>

    <tr>
      <td><code>valign</code></td>

      <td>Either: 'top', 'cap', 'half', 'base', 'bottom', 0, 1, 2, 3, 4</td>
    </tr>

    <tr>
      <td><strong class="CellBody">Object:&nbsp;<a name="pgfId-904274" id=
      "pgfId-904274"></a>text-table</strong></td>

      <td class="CellBody"><a name="pgfId-904275" id="pgfId-904275"></a>(graphics method
      class name is Tt)</td>
    </tr>

    <tr>
      <td><code>name</code></td>

      <td>StringType</td>
    </tr>

    <tr>
      <td><code>font</code></td>

      <td>IntType: (Range 1 to 9)</td>
    </tr>

    <tr>
      <td><code>spacing</code></td>

      <td>IntType: (Range -50 to 50)</td>
    </tr>

    <tr>
      <td><code>expansion</code></td>

      <td>IntType: (Range 50 to 150)</td>
    </tr>

    <tr>
      <td><code>color</code></td>

      <td>IntType: (Range 0 to 255)</td>
    </tr>
  </table>


[Main](vcs.html) \| [Previous](vcs-6.html) \| [Next](vcs-8.html)


