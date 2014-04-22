---
layout: default
title: Basic Open 
---
#  Opening a file and looking at its content

    import cdms, sys

    file=sys.prefix+'/sample_data/clt.nc'

    # Open the file via cdms
    f=cdms.open(file)

    # Now we are going to query the file
    # Get the names of the variables in the file
    variables = f.listvariables()

    print variables        # ['clt', 'u', 'v']

    # Get the names of the dimensions present in files
    dims = f.listdimension()

    # Get the global (file) attributes
    glob = f.listglobal()
    print glob             # ['center', 'comments', 'Conventions', 'model']

    # Get attributes attached to a variable (here clt)
    clt_att = f.listattribute('clt')
    print clt_att 
    # ['units', 'time_statistic', 'long_name', 'grid_name', 'comments', 'missing_value', 'grid_type']
