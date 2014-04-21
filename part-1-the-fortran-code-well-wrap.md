---
layout: default
title: 
---


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

  * [ ![Send this page to somebody](media/mail_icon.gif) ](/cdat/tutorials/f2py-wrapping-fortran-code/part-1-the-fortran-code-well-wrap/sendto_form)
  * [ ![Print this page](media/print_icon.gif) ](/this.print\(\))

#  Part 1 : The Fortran Code we'll wrap

This ection shows the fortran code that will be used as our example

Get the full fortran [ here ](/sf.f90)

There's a few important basics we need to point out at first.

f2py wraps subroutine or function, not actual program.

Usually this means strip out your program from all its preliminary and post
processing section,

identify "actual" computation part and put them into "subroutines" or
"function"

Python is much better suited to do all the file I/O than fortran

The example we're wrapping is a stream function subroutine

Here is the actul call in fortran:

    
    
    &#160;&#160;&#160;&#160; call CCMP_ZM_MSPI( nlon, nlat, nlev, V, lat, p, PS, msg, ZM_MPSI )

Let's examine the arguments:

INPUT ARGS:

nlon: Number of longitudes of longitude dimension. Type INTEGER.

nlat: Number of latitudes of latitude dimension. Type INTEGER.

nlev: Number of levels of pressure level dimension. Type

INTEGER.

V: Three-dimensional (lon,lat,lev) array of meridional wind

values in which THE PRESSURE LEVEL DIMENSION MUST BE ORDERED

TOP TO BOTTOM. Units must be m s^-1. Type REAL.

_

(The zonal mean of V, i.e. V, will be computed in this sub-

routine in allocated memory.)

lat: One-dimensional array of latitude values of latitude dimension

in degrees. Type REAL.

p: One-dimensional array of pressure level values of vertical

dimension ORDERED TOP TO BOTTOM. Units must be Pa. Type REAL.

The first value must be greater than 500 Pa (5mb), and the

last value must be less than 100500 Pa (1005mb).

PS: Two-dimensional (lon,lat) array of surface pressures. Units

must be Pa. Type REAL.

msg: Missing value (fill value) of stream function where V occurs

entirely below the earth's surface for all longitudes at fixed

latitude and pressure level. Type REAL.

OUTPUT ARGS:

ZM_MPSI: Two-dimensional (lat,lev) array of zonal mean meridional

stream function values in which the first dimension is lati-

tude and the second dimension is pressure level. THE PRESSURE

LEVEL DIMENSION IS ORDERED TOP TO BOTTOM UPON RETURN. Missing
