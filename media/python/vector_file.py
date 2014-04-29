# Import the modules needed for the tuturial
import vcs, cdms, cdutil, time, os, sys

# Open data file:
filepath = os.path.join(sys.prefix, 'sample_data/clt.nc')
cdmsfile = cdms.open( filepath )

# Extract two 3 dimensional data sets and get a subset of the time dimension
data1 = cdmsfile('u', longitude=(-180, -48.75), latitude = (10., 70.43))
data2 = cdmsfile('v', longitude=(-180, -48.75), latitude = (10., 70.43))

# Initial VCS:
v = vcs.init()

# Show the list of persistent vector graphics methods.
v.show('vector')

# Assign the variable "vf_asd" to the persistent 'ASD' isoline graphics methods.
vf_asd = v.getvector( 'quick' )

# Plot the data using the above vectory graphics method.
v.plot( data1, data2, vf_asd )
print ""
print "Press the Return key to see next plot."
sys.stdin.readline()

# List the 'quick' vector graphics methods attributes.
vf_asd.list()

# Change the vector scale value
vf_asd.scale = 5.0
print "Press the Return key to see next plot."
sys.stdin.readline()

# Change the vector scale value to a negative number
vf_asd.scale = -5.0
print "Press the Return key to see next plot."
sys.stdin.readline()

# Change the vector type to wind barbs
vf_asd.scale = 2.0
vf_asd.type = 1
print "Press the Return key to see next plot."
sys.stdin.readline()

# Change the vector type to solid arrow head
vf_asd.scale = 3.0
vf_asd.type = 2
print "Press the Return key to see next plot."
sys.stdin.readline()

# Change the vector reference and vector alignment
vf_asd.scale = 1.0
vf_asd.type = 0
vf_asd.reference = 15.
vf_asd.alignment = 'tail'
vf_asd.linecolor = 242
print "Press the Return key to see next plot."
sys.stdin.readline()

# Create a persistent vector graphics methods from an existing vector graphics method.
cf_new = v.createvector( 'new', 'quick' ) # create new from quick
cf_new2 = v.createvector( 'new2','quick' )# create new2 from quick
cf_new.list()                        # list its attributes
v.show('vector')                    # show vector list with new and new2
v.removeobject( cf_new )             # remove new from vector list
v.show('vector')                    # show vector list without new