---
layout: default
title: Opening Files 
---

##  Opening Files, Reading-in Data
Explains how to open a file a read-in variables.

CDMS is an easy to use interface to read in data from multiple binary formats,
such as NetCDF, HDF, Grads/GRIB (with a control file), PP, DRS (special build
need), ...

CDMS is also an OpenDAP client, you can access OpenDAP served data by typing
the URL instead of the file name

In this example we will open a file contained in your cdat distribution under
the sample_data directory and read the variable named 'clt' contained in it.

    # Import the cdms module and the sys module
    import cdms,sys
    
    # Construct the string containing the path to the data_file
    file_name=sys.prefix+'/sample_data/clt.nc'
    
    # open the file with the cdms interface
    file=cdms.open(file_name)
