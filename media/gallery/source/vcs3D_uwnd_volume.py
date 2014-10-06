'''
Created on Jun 18, 2014

@author: tpmaxwel
'''
import vcs, cdms2, sys

x = vcs.init()
f = cdms2.open( sys.prefix+"/sample_data/geos5-sample.nc" )  
dv3d = vcs.get3d_scalar()    
dv3d.ToggleVolumePlot = vcs.on
dv3d.Camera={'Position': (-161, -171, 279), 'ViewUp': (.29, 0.67, 0.68), 'FocalPoint': (146.7, 8.5, -28.6)}
dv3d_v = vcs.get3d_vector()    
v = f["uwnd"] 
dv3d.VerticalScaling = 4.0 
dv3d.ScaleColormap = [-46.0, 46.0, 1] 
dv3d.ScaleTransferFunction =  [10.0, 77.0, 1]   
x.plot( v, dv3d )
x.interact()




