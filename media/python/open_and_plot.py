# Import modules:
# cdms - Climate Data Management system accesses gridded data.
# vcs - Visualization and control System 1D and 2D plotting routines.
# os - Operation System routines for Mac, DOS, NT, or Posix depending on the 
#      system you're on.
# sys - This module provides access to some objects used or maintained by the
#       interpreter and to functions that interact strongly with the interpreter.
import cdms, vcs, os, sys

# Open data file:
filepath = os.path.join(sys.prefix, 'sample_data/clt.nc')
cdmsfile = cdms.open( filepath )
cdmsfile.listvariables()
data = cdmsfile('clt')

# Initial VCS:
v = vcs.init()

# Plot data using the default boxfill graphics method:
v.plot( data )

print "Press the Return key to see next plot."
sys.stdin.readline()

# Plot data using the isofill graphics method:
v.clear()
v.isofill( data )

print "Press the Return key to see next plot."
sys.stdin.readline()

# Plot data using the isoline graphics method:
v.clear()
v.isoline( data )

print "Press the Return key to see next plot."
sys.stdin.readline()

# Plot data using the boxfill graphics method:
v.clear()
v.boxfill( data )

print "Press the Return key to see next plot."
sys.stdin.readline()

# Plot a simple overlay plot using the isofill and isoline graphics methods:
v.clear()
v.isofill( data )
v.isoline( data )

print "Press the Return key to see next plot."
sys.stdin.readline()