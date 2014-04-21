---
layout: default
title: 
---

    * [ Tips and Tricks ](/cdat/tips_and_tricks)

    * [ Source Code ](/cdat/source)

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

  * [ ![Send this page to somebody](media/mail_icon.gif) ](/cdat/tutorials/f2py-wrapping-fortran-code/part-3-wrapping-a-python-function-to-pre-post-process-argument-to-the-fortran/sendto_form)
  * [ ![Print this page](media/print_icon.gif) ](/this.print\(\))

#  Part 3: Creating a Python function to pre/post process argument to the
fortran (intermediate)

This section show an example of a python wrapping that will make sure the
arguments passed are correct

Get the full function [ here ](/stream_function_wrapper.py)

Let's write a piece of python that will do the following for us:

  
1- Make sure the arguments have the right number of dimensions, determine
optional arrays if possible, convert arguments to numpy

2- If possible make sure the arguments are ordered correctly

3- If possible make sure the level are from top to bottom

4- If possible check units for levels and ps

5- Mask results where needed

6- If possible puts axes back on results

7- If possible reorder the results accordingly to the data passed in

Will do this in stages 0 thru 6

0- Passing arrays to the fortran and back

These are the bare bones, no checking is done, simply passes what it receives
and retuns back

Not too interesting at this point!

    
    
    import streamfunction
    def zm_msf(data,ps,latitudes=None,level=None):
        """
        Compute a Zonal Mean Meridional Strema Function
        Input:
        Data: 3D, dimensions are: longitude, latidue, level
        PS: (Surface Pressure) in Pa (or has untis attached to it)
        Optional (if not containe din data)
        levels: Levels (from top to bottom)
        latitudes
        Output
        zm_msf: Dimensions: latitude, level
        """
        # Some check code here
        if level is None:
            raise Exception,"Could not determine levels!"
        if level is None:
            raise Exception,"Could not determine latitudes!"
    
        msg = 1.E20
        zm_mpsi=streamfunction.ccmp_zm_mspi(data,latitude,level,ps,msg)
    
        return zm_mpsi
    

1- Checking arrays dimensions, determining optional arrays, converting
everything to numpy/list

Here it gets more interesting, we're now doing sometihng for the user, we
check that the data have the right number of dimensions and try to generate
latitude and levels

Once this is done we make sure f2py will understand the passed data (i.e.
numpy or list)

    
    
    import streamfunction
    import numpy,MV2,cdms2,unidata
    def zm_msf(data,ps,latitude=None,levels=None):
        """
        Compute a Zonal Mean Meridional Strema Function
        Input:
        Data: 3D, dimensions are: longitude, latidue, level
        PS: (Surface Pressure) in Pa (or has untis attached to it)
        Optional (if not containe din data)
        levels: Levels (from top to bottom)
        latitude
        Output
        zm_msf: Dimensions: latitude, level
        """
    
        if MV2.rank(data)!=3:
            raise Exception,"data input must be of rank 3"
    
        if MV2.rank(ps)!=2:
            raise Exception,"surface pressure (ps) input must be of rank 2"
    
        if levels is None:
            try:
                levels = data.getLevel()
            except:
                raise Exception,"Could not determine levels!"
        if latitude is None:
            try:
                latitude = data.getLatitude()
            except:
                raise Exception,"Could not determine latitude!"
    
        # Now we need to convert axes to numpy
        if not isinstance(data,(numpy.ndarray,list)):
            if isinstance(data,(cdms2.tvariable.TransientVariable,numpy.core.ma.MaskedArray)):
                data=data.filled()
            else:
                raise Exception, "wrong type for data"
        if not isinstance(ps,(numpy.ndarray,list)):
            if isinstance(ps,(cdms2.tvariable.TransientVariable,numpy.core.ma.MaskedArray)):
                ps=ps.filled()
            else:
                raise Exception, "wrong type for ps"
        if not isinstance(latitude,(numpy.ndarray,list)):
            if isinstance(latitude,(cdms2.tvariable.TransientVariable,numpy.core.ma.MaskedArray)):
                latitude=latitude.filled()
            elif isinstance(latitude,cdms2.axis.TransientAxis): # axis!
                latitude=latitude[:]
            else:
                raise Exception, "wrong type for latitude"
        if not isinstance(level,(numpy.ndarray,list)):
            if isinstance(level,(cdms2.tvariable.TransientVariable,numpy.core.ma.MaskedArray)):
                level=level.filled()
            elif isinstance(level,cdms2.axis.TransientAxis): # axis!
                level=level[:]
            else:
                raise Exception, "wrong type for level"
        msg = 1.E20
        zm_mpsi=streamfunction.ccmp_zm_mspi(data,latitude,level,ps,msg)
    
        return zm_mpsi

2- Checking dimensions order (if possible)

Now we're going to try to get the order of the dimensions and reorder

    
    
    _.
    .
    .
       &#160;if MV2.rank(data)!=3:
            raise Exception,"data input must be of rank 3"
    _
        try:
            orderin = data.getAxisList() # remember axes for later
            data=data(order='xyz')
        except:
            orderin = None
            # Could not reorder, dimensions info not sufficent
            pass
        try:
            ps=ps(order='xy')
        except:
            # Could not reorder, dimensions info not sufficent
            pass
    
    _    if MV2.rank(ps)!=2:
            raise Exception,"surface pressure (ps) input must be of rank 2"
    .
    .
    ._

3- Checking levels from top to bottom

Here we'll reorder levels if they are not order from top to bottom (low value
to big value)

but only if the levels are obtained from the data, otherwise we can't know if
the data need to be inverted as well, and we'll generate an exception rather
than allowing the function to return what is probably wrong result

    
    
    _.
    .
    .
       &#160;if MV2.rank(ps)!=2:
            raise Exception,"surface pressure (ps) input must be of rank 2"
        _
        if level is None:
            try:
                level = data.getLevel()
                # We need to test the level ordering here too, so we can reorder data if needed
                if level is None:
                    raise Exception # to go to the error statement
                if level[0]>level[-1]: # we need to revert data
                    data=data(level=(0,1.E20)) # gets the data in right order
                    level=data.getLevel()
            except:
                raise Exception,"Could not determine levels!"
    
        if level[0]>level[-1]:
            # need to invert levels
            raise Exception,"Error: levels must be from top to bottom"
    
    _    if latitude is None:
    .
    .
    ._

4- Checking units

Ok now we'll try to see if ps and level have units associated with them, if so
we'll try to convert them to Pa (if it is not)

For this will add a function "convert" that checks for the units attribute and
try to conver tto some other units

    
    
    _.
    .
    .
    import streamfunction
    import numpy,MV2,cdms2,unidata
    _
    def convert(data,unitsout="Pa"):
        """ Convert data into unitsout if possible
        """
        if hasattr(data,'units'):
            units = data.units
            if units!=unitsout:
                u = unidata.udunits(1,units)
                try:
                    sc,off = u.how(unitsout) # how to convert in Pa
                    ps = ps*sc+off
                except:
                    # well couldn't figure it out, assume it's ok but print a warning
                    raise Warning, "Couldn't convert units %s to %s, assuming you know what you're doing" % (units, unitsout)
        return data
        
    _def zm_msf(data,ps,latitude=None,level=None):
    .
    .
    .
        if MV2.rank(ps)!=2:
            raise Exception,"surface pressure (ps) input must be of rank 2"
    _
        ps = convert(ps,'Pa')
    
        if level is None:
            try:
    _.
    .
    .
                if level[0]>level[-1]: # we need to revert data
                    data=data(level=(0,1.E20)) # gets the data in right order
                    level=data.getLevel()_
                level = convert(level,'Pa')
    _        except:
                raise Exception,"Could not determine levels!"
    .
    .
    ._

5- Mask output

We know that the fortran sets missing values to a value set by user (we chose
1.E20 in the call), we're using that information to actually mask the output,
while we're at it we name it "zm_msf" as well

    
    
    _.
    .
    .
        msg = 1.E20
        zm_mpsi = streamfunction.ccmp_zm_mspi(data,latitude,level,ps,msg)_
    
        # Mask where missing
        zm_mpsi = MV2.masked_equal(zm_mpsi,msg)
        zm_mpsi.id = 'zm_msf'
        
    _    return zm_mpsi
    
    _

6- Putting axes back on result

Now we are trying if possible to put axes back onto the output

    
    
    _.
    .
    .
        # Mask where missing
        zm_mpsi = MV2.masked_equal(zm_mpsi,msg)
        zm_mpsi.id = 'zm_msf'
    _
        # creates the axes
        lev = cdms2.createAxis(level)
        try:
            l=data.getLevel()
            id = l.id
        except:
            id='level'
        lev.id=id
        lev.units='Pa'
        lat = cdms2.createAxis(latitude)
        try:
            lat=data.getLatitude()
            id = lat.id
            units = lat.units
        except:
            id='latitude'
            units='degrees_north'
            
        lat.id=id
        lat.units=units
    
        # And now sets the axis onto output
        zm_mpsi.setAxisList([lat,lev])
    
     _   
        return zm_mpsi_

7- Reordering results

Here we are trying to see the input data were in another order and we try to
reorder the output correspondingly

    
    
    _.
    .
    .
        # And now sets the axis onto output
        zm_mpsi.setAxisList([lat,lev])_
    
        if orderin is not None:
            ## ok we had a transient variable in
            orderout=""
            for ax in orderin:
                if ax.isLatitude(): # latitude?
                    orderout+='y'
                elif ax.isLevel():
                    orderout+='z'
            zm_mpsi=zm_mpsi(order=orderout)
        
    _    return zm_mpsi_

That it's for now, you can get the full function here

Let's just run it a few times with some examples

    
    
    &#160;# calculate stream function with a twist - meridonal circulation
    import [stream_function_wrapper](/stream_function_wrapper.py)
    import cdms2
    # Open data file 1
    f=cdms2.open('[va_djf.nc](/va_djf.nc)')
    # reads in data, makes sure order is right and levels are top to bottom
    v=f('v')
    f.close()
    fp=cdms2.open('[ps.nc](/ps.nc)')
    ps=fp('ps')
    fp.close()
    
    # we read data ordered incorectly
    # level are bottom to top
    v.info()
    ps.info()
    
    # But it still works with our wrpping function
