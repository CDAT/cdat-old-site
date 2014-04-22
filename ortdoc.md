---
layout: default
title: 
---

#  ORT Package Documentation

Read one file of Oort radiosonde data. Each file contains data for all
stations  
for one month. The number of stations changes from month to month.  
  
This program is a modified version of the test-read code "read.f" (GFDL
program  
reado) provided by NCAR.  
  
Input variables:  
  
character*(*) filename ! name of the file to be read  
integer maxsta ! max number of stations (soundings) possible  
integer nvarbs, nlevels ! number of variables and P-levels in each sounding  
  
Output variables:  
  
real lon(maxsta), lat(maxsta) ! longitudes / latitudes of the stations  
real data(nvarbs, nlevels, maxsta) ! sounding data  
integer nr ! actual number of stations with data  
  
  
* Documentation *   
  
Oort radiosonde data (NCAR Data Support Section dataset DS431.0)  
  
From: jrl@GFDL.GOV (John Lanzante) via joseph@ncar.ucar.edu (Dennis Joseph)  
  
______________________________________________________________________________
_  
Datasets: Monthly Rawinsonde Station Covariances - 11 terms  
______________________________________________________________________________
_  
Variables: Su Sv ST Sz Sq Srh Nu NT Nz Nq Nrh  
The variables are u, v, T, z, q, and rh.  
S = sum and N = number of observations.  
NOTE: Nv is not needed since Nv=Nu.  
NOTE: z is given as the geopotential height departure  
(z - zREF) from NMC standard atmosphere (zREF) in gpm.  
______________________________________________________________________________
_  
Time Period: May 1958 to December1989  
______________________________________________________________________________
_  
File Structure: Files named yyyy.mm.ttz where yyyy=four digit year,  
mm=two digit month (leading zeros) and tt=time (either  
00,06,12 or 18 GMT); z indicates GMT.  
______________________________________________________________________________
_  
Units: m/s m/s C m g/kg % num num num num num  
______________________________________________________________________________
_  
  
Original Source: GFDL, Bram Oort (retired)  
______________________________________________________________________________
_  
Bibliography:  
Oort, A., 1983: Global Atmospheric Circulation Statistics, 1958-1973,  
NOAA Professional Paper 14, U.S. Department of Commerce [data set  
has been updated since this publication].  
______________________________________________________________________________
_  
GFDL Contact: John Lanzante or Gabriel Lau  
______________________________________________________________________________
_

* * *

UCRL-WEB-213937 | [ Privacy & Legal Notice ](/disclaimer.html)

[ webmaster@pcmdi.llnl.gov ](/webmaster@pcmdi.llnl.gov)

[ ![Powered by Plone](media/plone_powered.gif) ](/)

