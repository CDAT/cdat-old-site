import streamfunction
import numpy,MV2,cdms2,unidata

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
    
def zm_msf(data,ps,latitude=None,level=None):
    """
    Compute a Zonal Mean Meridional Strema Function
    Input:
    Data: 3D, dimensions are: longitude, latidue, level
    PS: (Surface Pressure) in Pa (or has untis attached to it)
    Optional (if not containe din data)
    level: Level values (from top to bottom)
    latitude: latitude values
    Output
    zm_msf: Dimensions: latitude, level
    """

    if MV2.rank(data)!=3:
        raise Exception,"data input must be of rank 3"

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
    
    if MV2.rank(ps)!=2:
        raise Exception,"surface pressure (ps) input must be of rank 2"

    ps = convert(ps,'Pa')

    if level is None:
        try:
            level = data.getLevel()
            # We need to test the level ordering here too, so we can reorder data if needed
            if level is None:
                raise Exception # to go to the error statement
            if level[0]>level[-1]: # we need to revert data
                data=data(level=(0,1.E20)) # gets the data in right order
                level=data.getLevel()
            level = convert(level,'Pa')
        except:
            raise Exception,"Could not determine levels!"

    if level[0]>level[-1]:
        # need to invert levels
        raise Exception,"Error: levels must be from top to bottom"
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
    zm_mpsi = streamfunction.ccmp_zm_mspi(data,latitude,level,ps,msg)

    # Mask where missing
    zm_mpsi = MV2.masked_equal(zm_mpsi,msg)
    zm_mpsi.id = 'zm_msf'

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

    if orderin is not None:
        ## ok we had a transient variable in
        orderout=""
        for ax in orderin:
            if ax.isLatitude(): # latitude?
                orderout+='y'
            elif ax.isLevel():
                orderout+='z'
        zm_mpsi=zm_mpsi(order=orderout)
    
    return zm_mpsi

