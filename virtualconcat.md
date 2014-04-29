---
layout: default
title: using cdscan 
---

##  "Virtually" Concatenating NetCDF Files, using cdscan

Here we show how to concatenate NetCDF files without rewriting any data,
simply creating a new "virtual" control file

This is to be executed outside of python, before runnig a script.  
We are assuming your python resides in /usr/local/cdat.  

    cdscan -x u.xml /usr/local/cdat/sample_data/u_*.nc

The newly genrated file: u.xml can now be accessed by python scripts and contains all the years spanned by u in files u_xxxx.nc

