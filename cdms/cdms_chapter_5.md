---
layout: default
title: CDAT CDMS Chapter 5
---
CHAPTER 5 Plotting CDMS data in Python

 

5.1 Overview

Data read via the CDMS Python interface can be plotted using the vcs module. This module, part of the Climate Data Analysis Tool (CDAT) is documented in the CDAT reference manual. The vcs module provides access to the functionality of the VCS visualization program.

Examples of plotting data accessed from CDMS are given below, as well as documentation for the plot routine keywords.

5.2 Examples

In the following examples, it is assumed that variable psl is dimensioned (time, latitude, longitude). psl is contained in the dataset named 'sample.xml'.

5.2.1 Example: plotting a gridded variable

1 import cdms, vcs
2 #
3 f = cdms.open('sample.xml')
4 psl = f.variables['psl']
5 sample = psl[0]
6 w=vcs.init()
7 #
8 w.plot(sample)
9 f.close()

Notes:

Line Notes

5 Get a horizontal slice, for the first timepoint.

6 Create a VCS Canvas w.

8 Plot the data. Because sample is a transient variable, it encapsulates all the time, latitude, longitude, and attribute information.

9 Close the file. This must be done after the reference to the persistent variable 'psl'.

Thats it! The axis coordinates, variable name, description, units, etc. are obtained from variable sample.

What if the units are not explicitly defined for psl, or a different description is desired? plot has a number of other keywords which fill in the extra plot information.

5.2.2 Example: using plot keywords.

w.plot(array, units='mm/day', file_comment='High-frequency
reanalysis', long_name="Sea level pressure", comment1="Sample
plot", hms="18:00:00", ymd="1978/01/01")

Note: Keyword arguments can be listed in any order.

5.2.3 Example: plotting a time-latitude slice

Assuming that variable psl has domain (time,latitude,longitude), this example selects and plots a time-latitude slice:

1 samp = psl[:,:,0]
2 w = vcs.init()
3 w.plot(samp, name='sea level pressure')

Notes:

Line Notes

1 samp is a slice of psl, at index 0 of the last dimension. Since samp was obtained from the slice operator, it is a transient variable, which includes the latitude and time information.

3 The name keyword defines the identifier, by default the name in the file.

5.2.4 Example: plotting subsetted data

Calling the variable psl as a function reads a subset of the variable. The result variable samp can be plotted directly:

...
1 samp = psl(time=(0.0,100.0), longitude=180.0)
2 w = vcs.init()
3 w.plot(samp)

 

5.3 plot method

The plot method is documented in the CDAT Reference Manual. This

section augments the documentation with a description of the optional key

word arguments.

The general form of the plot command is:ch4_cdms_4.0.html/#4.1_Overview

canvas.plot(array [, args] [,key=value [, key=value [, ...] ] ])

where:

    canvas is a VCS Canvas object, created with the vcs.init method.
    array is a variable, masked array, or Numeric array having between two and five dimensions. The last dimensions of the array is termed the 'x' dimension, the next-to-last the 'y' dimension, then 'z', 't', and 'w'. For example, if array is three-dimensional, the axes are (z,y,x), and if array is four-dimensional, the axes are (t,z,y,x). (Note that the t dimension need have no connection with time; any spatial axis can be mapped to any plot dimension. For a graphics method which is two-dimensional, such as boxfill, the y-axis is plotted on the horizontal, and the x-axis on the vertical.

If array is a gridded variable on a rectangular grid, the plot function uses a box-fill graphics method. If it is non-rectangular, the meshfill graphics method is used.

Note that some plot keywords apply only to rectangular grids only.

    args are optional positional arguments:

args := template_name, graphics_method, graphics_name
template_name: the name of the VCS template (e.g., 'AMIP')
graphics_method : the VCS graphics method (boxfill)
graphics_name: the name of the specific graphics method ('default')

See the CDAT Reference Manual and VCS Reference Manual for a detailed description of these arguments.

    key=value, ... are optional keyword/value pairs, listed in any order. These are defined in Table 5.1 on page 145.

Table 5.1 plot keywords

  key                                type                            value
comment1 	string 	Comment plotted above file_comment
comment2 	string 	Comment plotted above comment1
comment3 	string 	Comment plotted above comment2
continents 	0 or 1 	if ==1, plot continental outlines (default:plot if xaxis is longitude, yaxis is latitude -or- xname is ’longitude’ and yname is ’latitude’
file_comment 	string 	Comment, defaults to variable.parent.comment)
grid 	CDMS grid
object 	Grid associated with the data. Defaults to variable.getGrid()
hms 	string 	Hour, minute, second
long_name 	string 	Descriptive variable name, defaults to variable.long_name.
missing_value 	same type as
array 	Missing data value, defaults to variable.getMissing()
name 	string 	Variable name, defaults to variable.id
time 	cdtime relative
or absolute
time 	time associated with the data. Example: cdtime.reltime(30.0, “days since 1978-1-1”).
units 	string 	Data units. Defaults to variable.units
variable 	CDMS variable
object 	Variable associated with the data. The variable grid must have the same shape as the data array.
xarray
([y|z|t|w] array) 	1-D Numeric array 	[rectangular grids only]
Array of coordinate values, having the same length as the corresponding dimension. Defaults to xaxis[:] (y|z|t|waxis[:])
xaxis
([y|z|t|w] axis) 	CDMS axis object 	[rectangular grids only]
Axis object. xaxis defaults to grid.getAxis(0), yaxis defaults to grid.getAxis(1)
xbounds
(ybounds) 	2-D Numeric
array 	[rectangular grids only]
Boundary array of shape (n,2) where n is the axis length. Defaults to xaxis.getBounds(), or xaxis.genGenericBounds()
if None, similarly for ybounds.
xname
([y|z|t|w]name) 	string 	[rectangular grids only]
Axis name. Defaults to xaxis.id ([y|z|t|w]axis.id)
xrev (yrev)




	0 or 1




	If xrev (yrev) is 1, reverse the direction of the x-axis (y-axis). Defaults to 0, with the following exceptions:
• If the y-axis is latitude, and has decreasing values, yrev defaults to 1
• If the y-axis is a vertical level, and has increasing pressure levels, yrev defaults to 1.
xunits
([y|z|t|w] units) 	string 	[rectangular grids only]
Axis units. Defaults to xaxis.units ([y|z|t|w]axis.units).

 