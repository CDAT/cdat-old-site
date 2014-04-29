#!/usr/bin/env python
# -*- coding: utf-8 -*-
# gmt2vcs_continents.py 0.1
# Author: Julien VIENNE (jv@climpact.com)
# Transcription from GMT coastline files to VCS compatible coastlines file.
# For a correct use with VCS follow the instructions :
#
#      1) In a shell, call the pscoast function with your region (GMT must be
#              installed):
#             $ pscoast -M -W -Ia -R-2/5/45/51 -Df > coasts.gmt
#             -M gives an ascii output (obligatory)
#             -R specifies the region to be extracted (obligatory)
#             -D specifies the resolution (optional, default = high)
#              (f=full,h=high,i=intermediate,l=low,c=crude)
#             -W for coastlines (optional)
#             -Na for political boundaries (optional)
#             -Ia  for rivers (optional)
#              (type 'man pscoast' for more indications)
#
#      2) Apply gmt2vcs_continents.py on the coasts.gmt file as following:
#
#             $ gmt2vcs_continents.py [-o data_continent_other8] coasts.gmt
#
#             -o specifies the name of the vcs output file name
#                     This file MUST start with 'data_continent_other'
#                     Without the -o option,  default name is 'data_continent_other7'
#
#      3) Place the output file in your PCMDI_GRAPHICS folder
#
#     4) Select the user continent option in VCDAT
#             data_continent_other7 corresponds to 'User1 continents'
#             data_continent_other8 corresponds to 'User2 continents'
#             ...
#             OR
#        Use the option continent=8 in a template definition...
#-----------------------------------------------------------------------------------------------------------------------------------#
import string,getopt,sys
def help():
	man="""Convert the output of pscoast (GMT function) into VCS compatible continent file.
	
Usage:
1) In a shell, call the pscoast function (GMT must be installed):
	$ pscoast -M -W -R-2/5/45/51 -Df > coasts.gmt
	-M gives an ascii output
	-R specifies the region to be extracted
	-D specifies the resolution (f=full,h=high,i=intermediate,l=low,c=crude)
	-W for coastlines
	-N for political boundaries
	-I for rivers
	(type man pscoast for more indications)
2) Apply gmt2vcs_continents.py on the coasts.gmt file as following:
	$ gmt2vcs_continents.py -o data_continent_other8 coasts.gmt
	-o specifies the name of the vcs output file name
		This file MUST start with 'data_continent_other'
		Default name is 'data_continent_other7'
3) Place the output file in your PCMDI_GRAPHICS folder

Enjoy!
Author: Julien VIENNE (jv@climpact.com)
"""
	print man


# Function which prints polyline in output file
def print_poly(OutputFile,x,y):
	if len(x) !=0 and len(y) !=0:
		n=len(x)
		OutputFile.write('%i 1 %f %f %f %f\n'%(2*n,min(y),max(y),min(x),max(x)))
		for i in range(n):
			if (i+1)%NbPtLigne == 0 or  i==n-1:
				OutputFile.write('%f %f\n'%(y[i],x[i]))
			else:
				OutputFile.write('%f %f '%(y[i],x[i]))

# Default outpout file
OutFileName='data_continent_other7'
stderr=sys.stderr
# Get options
try:
	myopts,myargs = getopt.getopt(sys.argv[1:], 'ho:',["help"])
except getopt.GetoptError:
	print >>stderr,"ERROR [gmt2vcs_continents.py]!! Syntax error..."
	print >>stderr,"Please type 'gmt2vcs_continents.py -h' for help"
	sys.exit(1)
	
# Manage options
for myopt, myval in myopts:
	if myopt in ('-h','--help'):
		help()
		sys.exit(0)
	elif myopt == '-o':
		OutFileName=myval
		if OutFileName[:20] != 'data_continent_other':
			print >>stderr,"WARNING [gmt2vcs_continents.py]!!"
			print >>stderr,"To be compatible with VCS, outfile name must start "
			print >>stderr,"with 'data_continent_other'"
# If no input file
if len(myargs)==0:
	print >>stderr,"ERROR [gmt2vcs_continents.py]!!"
	print >>stderr,"Give a GMT coastline file name"
	print >>stderr,"Type gmt2vcs_continents.py -h for help"
	sys.exit(1)
# Open GMT file
try:
	f=open(myargs[0])
except :
	print >>stderr,"ERROR [gmt2vcs_continents.py]!!"
	print >>stderr,"File %s not found."%myargs[0]
	sys.exit(1)
	
# Open VCS output file
try:
	fout=open(OutFileName,'w')
except :
	print >>stderr,"ERROR [gmt2vcs_continents.py]!!"
	print >>stderr,"Can't open %s for writting."%OutFileName
	sys.exit(1)
	
y=[]
x=[]

# Nb of points per line in VCS file (for lisibility)
NbPtLigne=4
# Maximum points for one polyline
NbMaxPts=100

for l in f.xreadlines():
	# special character'>' for new polyline
	if l[0]=='>':
		print_poly(fout,x,y)
		x=[]
		y=[]
	elif l[0] == '#': # Comments
		pass
	else:
		# In VCS polylines must not have more than 200 points
		if len(x) >= NbMaxPts: 
			print_poly(fout,x,y)
			# Last point of the last polyline is the first of next one
			x=[x[NbMaxPts-1]]
			y=[y[NbMaxPts-1]]
		sp=l.split()
		
		lon=string.atof(sp[0])
		lat=string.atof(sp[1])
		if lon>180:lon=lon-360
		x.append(lon)
		y.append(lat)
# Last polyline
print_poly(fout,x,y)
# Closing file characters
print >> fout," -99    -99 "
fout.close()
