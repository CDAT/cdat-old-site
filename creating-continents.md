---
layout: default
title: 
---

      * [ f2py - Wrapping Fortran Code ](/cdat/tutorials/f2py-wrapping-fortran-code)

    * [ Quick Reference ](/cdat/quick_reference)

    * [ FAQ ](/cdat/FAQ)

    * [ Manuals ](/cdat/manuals)

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

  * [ ![Send this page to somebody](media/mail_icon.gif) ](/cdat/tutorials/cdatbasics/plotting-basics/creating-continents/sendto_form)
  * [ ![Print this page](media/print_icon.gif) ](/this.print\(\))

#  Creating Continents

[ ![Table of Contents](media/arrow-up) ](/)

[ ![Previous](media/arrow-left) ](/modifying-continents-plot)

[ ![Next](media/arrow-right) ](/save-plot-output)

[ Contents ](/)

[ Previous ](/modifying-continents-plot)

[ Next ](/save-plot-output)

 Goal:  Guide you through creating external continents.   

Before running the tutorial below, type _ "python" _ or _ "cdat" _ at the
command line.&#160; You will see the python prompt appear (i.e., ">>>"). You can
now enter the command lines below.  
  
You can [ _ _  view  _ _ ](/../files/show_continents) or [ _ _  download
 _ _ ](/../files/show_continents.py) the full source code. To run the source
code at the command line, type: _ "python show_continents.py" _ .

 EXTERNAL CONTINENTS:    
Included with the CDAT/VCS module are three ASCII continents files:  

  * _ 'data_continent_states' _ ("United States"), continential data for "Fine Continents" and the boundaries of the 48 continental United States; 
  * _ 'data_continent_political' _ ("Political Borders"), continential data for "Fine Continents" and political borders of sovereign countries; 
  * _ 'data_continent_river' _ ("Major North America Rivers"), continential data for "Fine Continents" and major North America rivers. 

(Note, these continents files may be out of date. Particularly, the "Political
Borders" continental file.)  

    
    
    These external continent files are located in the user's:  
    $HOME/PCMDI_GRAPHICS directory.  
    User created external continent files must be also placed in this directory.   
    

 ADDING YOUR OWN EXTERNAL CONTINENTS:    
As many as six additional continental map files can be defined by the user.
These files must be located in the user's $HOME/PCMDI_GRAPHICS directory and
must be named: data_continent_other7, data_continent_other8, ...,
data_continent_other12, respectively.  
  
 ASCII FORMAT FOR THE EXTERNAL CONTINENTS FILES:    
(number of y-x coordinates*2); continental-type value (always 1); values of
y-x coordines  

To indicate the end-of-file, a&#160; value of "&#160; -99&#160;&#160;&#160; -99" is given.

Example of a continents file (e.g., Save the below text in the file
$HOME/PCMDI_GRAPHCIS/data_continent_other8):  

    
    
    &#160;&#160;&#160; 12&#160;&#160; 1&#160;&#160; 64.182&#160;&#160; -180.000 69.763&#160; -170.156  
     64.182 -180.000&#160; 64.182 -170.156&#160; 66.973 -170.156&#160; 66.973 -178.594  
    &#160;69.763 -178.594&#160; 69.763 -180.000  
    &#160;&#160;&#160; 282&#160;&#160; 1&#160; 83.705 -18.281 11.162 -164.531  
    
    
    &#160;69.763 -164.531&#160;&#160; 58.602 -164.531&#160; 58.602&#160; -158.906 55.811 -158.906  
    &#160;55.811 -156.094&#160;&#160; 58.602 -156.094&#160; 58.602&#160; -147.656 61.392 -147.656  
    &#160;61.392 -144.844&#160;&#160; 58.602 -144.844&#160; 58.602&#160; -136.406 55.811 -136.406  
    &#160;55.811 -130.781&#160;&#160; 53.021 -130.781&#160; 53.021&#160; -127.969 50.230 -127.969  
    &#160;50.230 -125.156&#160;&#160; 39.068 -125.156&#160; 39.068&#160; -122.344 36.278 -122.344  
    &#160;36.278 -119.531&#160;&#160; 33.487 -119.531&#160; 33.487&#160; -116.719 30.697 -116.719  
    &#160;30.697 -113.906&#160;&#160; 27.906 -113.906&#160; 27.906&#160; -111.094 25.115 -111.094  
    &#160;25.115 -108.281&#160;&#160; 22.325 -108.281&#160; 22.325&#160; -105.469 19.534 -105.469  
    &#160;19.534 -102.656&#160;&#160; 16.744 -102.656&#160; 16.744&#160;&#160; -94.219 13.953&#160; -94.219  
    &#160;13.953&#160; -85.781&#160;&#160; 11.162&#160; -85.781&#160; 11.162&#160;&#160; -82.969 16.744&#160; -82.969  
    &#160;16.744&#160; -88.594&#160;&#160; 19.534&#160; -88.594&#160; 19.534&#160;&#160; -85.781 22.325&#160; -85.781  
    &#160;22.325&#160; -88.594&#160;&#160; 19.534&#160; -88.594&#160; 19.534&#160;&#160; -97.031 27.906&#160; -97.031  
    &#160;27.906&#160; -94.219&#160;&#160; 30.697&#160; -94.219&#160; 30.697&#160;&#160; -91.406 27.906&#160; -91.406  
    &#160;27.906&#160; -88.594&#160;&#160; 30.697&#160; -88.594&#160; 30.697&#160;&#160; -82.969 25.115&#160; -82.969  
    &#160;25.115&#160; -80.156&#160;&#160; 33.487&#160; -80.156&#160; 33.487&#160;&#160; -77.344 36.278&#160; -77.344  
    &#160;36.278&#160; -74.531&#160;&#160; 39.068&#160; -74.531&#160; 39.068&#160;&#160; -71.719 41.859&#160; -71.719  
    &#160;41.859&#160; -68.906&#160;&#160; 44.649&#160; -68.906&#160; 44.649&#160;&#160; -63.281 50.230&#160; -63.281  
    &#160;50.230&#160; -57.656&#160;&#160; 47.440&#160; -57.656&#160; 47.440&#160;&#160; -54.844 53.021&#160; -54.844  
    &#160;53.021&#160; -57.656&#160;&#160; 55.811&#160; -57.656&#160; 55.811&#160;&#160; -63.281 58.602&#160; -63.281  
    &#160;58.602&#160; -68.906&#160;&#160; 61.392&#160; -68.906&#160; 61.392&#160;&#160; -66.094 64.182&#160; -66.094  
    &#160;64.182&#160; -63.281&#160;&#160; 66.973&#160; -63.281&#160; 66.973&#160;&#160; -66.094 69.763&#160; -66.094  
    &#160;69.763&#160; -71.719&#160;&#160; 72.553&#160; -71.719&#160; 72.553&#160;&#160; -77.344 78.131&#160; -77.344  
    &#160;78.131&#160; -68.906&#160;&#160; 80.919&#160; -68.906&#160; 80.919&#160;&#160; -66.094 78.131&#160; -66.094  
    &#160;78.131&#160; -68.906&#160;&#160; 75.342&#160; -68.906&#160; 75.342&#160;&#160; -57.656 72.553&#160; -57.656  
    &#160;72.553&#160; -54.844&#160;&#160; 66.973&#160; -54.844&#160; 66.973&#160;&#160; -52.031 64.182&#160; -52.031  
    &#160;64.182&#160; -49.219&#160;&#160; 61.392&#160; -49.219&#160; 61.392&#160;&#160; -40.781 64.182&#160; -40.781  
    &#160;64.182&#160; -37.969&#160;&#160; 66.973&#160; -37.969&#160; 66.973&#160;&#160; -26.719 69.763&#160; -26.719  
    &#160;69.763&#160; -21.094&#160;&#160; 72.553&#160; -21.094&#160; 72.553&#160;&#160; -18.281 80.919&#160; -18.281  
    &#160;80.919&#160; -23.906&#160;&#160; 83.705&#160; -23.906&#160; 83.705&#160;&#160; -52.031 80.919&#160; -52.031  
    &#160;80.919&#160; -63.281&#160;&#160; 83.705&#160; -63.281&#160; 83.705&#160;&#160; -85.781 80.919&#160; -85.781  
    &#160;80.919&#160; -97.031&#160;&#160; 78.131&#160; -97.031&#160; 78.131&#160;&#160; -99.844 69.763&#160; -99.844  
    &#160;69.763 -102.656&#160;&#160; 72.553 -102.656&#160; 72.553&#160; -116.719 69.763 -116.719  
    &#160;69.763 -119.531&#160;&#160; 72.553 -119.531&#160; 72.553&#160; -116.719 75.342 -116.719  
    &#160;75.342 -113.906&#160;&#160; 78.131 -113.906&#160; 78.131&#160; -116.719 75.342 -116.719  
    &#160;75.342 -125.156&#160;&#160; 72.553 -125.156&#160; 72.553&#160; -122.344 69.763 -122.344  
    &#160;69.763 -164.531  
    &#160;&#160; -99&#160;&#160;&#160;&#160; -99  
    

  
The first line specifies the connection of six points of (latitude, longitude)
coodinates in the upper left corner of the plot.  
  
The second line of this example specifies the connection of 141 points, which
represents a very rough outline of North America.  
  
The entry "&#160;&#160;&#160;&#160; -99&#160;&#160;&#160;&#160; -99" indicate that no more data are to be read in
(i.e., denotes end-of-file).  

Note the total number of points for any given line should not exceed 200
points.  

    
    
    # Import the modules needed for the tuturial  
    # Import the modules needed for the tuturial  
    # cdms - Climate Data Management system accesses gridded data.  
    # vcs - Visualization and control System 1D and 2D plotting routines.  
    # cdutil - Climate utilitizes that contains miscellaneous routines for   
    #          manipulating variables.  
    # time - This module provides various functions to mainpulate time values.  
    # os - Operation System routines for Mac, DOS, NT, or Posix depending on   
    #      the system you're on.  
    # sys - This module provides access to some objects used or maintained by   
    #       the interpreter and to functions that interact strongly with the interpreter.  
    import vcs, cdms, cdutil, time, os, sys  
      
    # Open data file:  
    filepath = os.path.join(sys.prefix, 'sample_data/clt.nc')  
    cdmsfile = cdms.open( filepath )  
      
    # Extract a 3 dimensional data set and get a subset of the time dimension  
    data = cdmsfile('clt', longitude=(-180, 180), latitude = (-90., 90.))  
      
    # Initial VCS:  
    v = vcs.init()  
      
    #Plot the data using the created data_continent_other8 file.  
    v.plot( data, continents=7 )  
    

![Continents_5](media/continents_5)  
  
 USING THE NEWLY CREATED CONTINENTS:    
The continent-type values in the CDAT API range from 0 to 11, where:  
0 signifies "No Continents"  
1 signifies "Fine Continents"  
2 signifies "Coarse Continents"  
3 signifies "United States Continents"  
4 signifies "Political Borders Continents"  
5 signifies "North American Rivers Continents"  
  
Values 6 through 11 signify the continents files data_continent_other7 through
data_continent_12, respectively.  
  
 EXAMPLE PYTHON SCRIPT SHOWING CONTINENTS:   

    
    
    # Import the modules needed for the tuturial  
    import vcs, cdms, cdutil, time, os, sys  
      
    # Open data file:  
    filepath = os.path.join(sys.prefix, 'sample_data/clt.nc')  
    cdmsfile = cdms.open( filepath )  
      
    # Extract a 3 dimensional data set and get a subset of the time dimension  
    data = cdmsfile('clt', longitude=(-180, 180), latitude = (-90., 90.))  
      
    continent_type = { 0: "0 signifies - No Continents",  
    &#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160; 1: "1 signifies - Fine Continents",  
    &#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160; 2: "2 signifies - Coarse # Continents",  
    &#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160; 3: "3 signifies - United States Continents",  
    &#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160; 4: "4 signifies - Political Borders Continents",  
    &#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160; 5: "5 signifies - North American Rivers Continents",  
    &#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160; 6: "6 signifies - User continent file data_continent_other7",  
    &#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160; 7: "7 signifies - User continent file data_continent_other8",  
    &#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160; 8: "8 signifies - User continent file data_continent_other9",  
    &#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160; 9: "9 signifies - User continent file data_continent_other10",  
    &#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160; 10:&#160; "10 signifies - User continent file data_continent_other11",  
    &#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160; 11:&#160; "11 signifies - User continent file data_continent_other12"  
    &#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160; }  
      
    # Initial VCS:  
    v = vcs.init()  
      
    for i in range( 12 ):  
    print "continent_type ", continent_type[i]  
    v.plot(data, continents=i)  
    time.sleep(2)  
    v.clear()

 EXAMPLE from VCDAT:    

From VCDAT, under the graphics "Options" menu button, you will see the
"Continents Types" pull right menu item. All of the continents (including the
user defined continents) are selectable from here.  
  
MORE INFORMATION:  
There is more information on how to set the continents line type, line color,
etc. in other sections of the tutorial. In VCDAT, you can modify the
continents from the "Set Graphics Method Attributes..." menu panel.  
  
  
ANOTHER ASCII FILE EXAMPLE:  
In your $HOME/PCMDI_GRAPHICS directory, create the file
"data_continents_other9" and enter the following lines to. Then run the Python
and VCDAT examples above. (This ASCII file will draw a coarse continental
outline of North America and Australia.  
  

    
    
    &#160; 282&#160;&#160; 1&#160; 83.705 -18.281 11.162 -164.531   
    69.763 -164.531&#160;&#160; 58.602 -164.531&#160; 58.602&#160; -158.906 55.811 -158.906  
    55.811 -156.094&#160;&#160; 58.602 -156.094&#160; 58.602&#160; -147.656 61.392 -147.656  
    61.392 -144.844&#160;&#160; 58.602 -144.844&#160; 58.602&#160; -136.406 55.811 -136.406  
    55.811 -130.781&#160;&#160; 53.021 -130.781&#160; 53.021&#160; -127.969 50.230 -127.969  
    50.230 -125.156&#160;&#160; 39.068 -125.156&#160; 39.068&#160; -122.344 36.278 -122.344  
    36.278 -119.531&#160;&#160; 33.487 -119.531&#160; 33.487&#160; -116.719 30.697 -116.719  
    30.697 -113.906&#160;&#160; 27.906 -113.906&#160; 27.906&#160; -111.094 25.115 -111.094  
    25.115 -108.281&#160;&#160; 22.325 -108.281&#160; 22.325&#160; -105.469 19.534 -105.469  
    19.534 -102.656&#160;&#160; 16.744 -102.656&#160; 16.744&#160;&#160; -94.219 13.953&#160; -94.219  
    13.953&#160; -85.781&#160;&#160; 11.162&#160; -85.781&#160; 11.162&#160;&#160; -82.969 16.744&#160; -82.969  
    16.744&#160; -88.594&#160;&#160; 19.534&#160; -88.594&#160; 19.534&#160;&#160; -85.781 22.325&#160; -85.781  
    22.325&#160; -88.594&#160;&#160; 19.534&#160; -88.594&#160; 19.534&#160;&#160; -97.031 27.906&#160; -97.031  
    27.906&#160; -94.219&#160;&#160; 30.697&#160; -94.219&#160; 30.697&#160;&#160; -91.406 27.906&#160; -91.406  
    27.906&#160; -88.594&#160;&#160; 30.697&#160; -88.594&#160; 30.697&#160;&#160; -82.969 25.115&#160; -82.969  
    25.115&#160; -80.156&#160;&#160; 33.487&#160; -80.156&#160; 33.487&#160;&#160; -77.344 36.278&#160; -77.344  
    36.278&#160; -74.531&#160;&#160; 39.068&#160; -74.531&#160; 39.068&#160;&#160; -71.719 41.859&#160; -71.719  
    41.859&#160; -68.906&#160;&#160; 44.649&#160; -68.906&#160; 44.649&#160;&#160; -63.281 50.230&#160; -63.281  
    50.230&#160; -57.656&#160;&#160; 47.440&#160; -57.656&#160; 47.440&#160;&#160; -54.844 53.021&#160; -54.844  
    53.021&#160; -57.656&#160;&#160; 55.811&#160; -57.656&#160; 55.811&#160;&#160; -63.281 58.602&#160; -63.281  
    58.602&#160; -68.906&#160;&#160; 61.392&#160; -68.906&#160; 61.392&#160;&#160; -66.094 64.182&#160; -66.094  
    64.182&#160; -63.281&#160;&#160; 66.973&#160; -63.281&#160; 66.973&#160;&#160; -66.094 69.763&#160; -66.094  
    69.763&#160; -71.719&#160;&#160; 72.553&#160; -71.719&#160; 72.553&#160;&#160; -77.344 78.131&#160; -77.344  
    78.131&#160; -68.906&#160;&#160; 80.919&#160; -68.906&#160; 80.919&#160;&#160; -66.094 78.131&#160; -66.094  
    78.131&#160; -68.906&#160;&#160; 75.342&#160; -68.906&#160; 75.342&#160;&#160; -57.656 72.553&#160; -57.656  
    72.553&#160; -54.844&#160;&#160; 66.973&#160; -54.844&#160; 66.973&#160;&#160; -52.031 64.182&#160; -52.031  
    64.182&#160; -49.219&#160;&#160; 61.392&#160; -49.219&#160; 61.392&#160;&#160; -40.781 64.182&#160; -40.781  
    64.182&#160; -37.969&#160;&#160; 66.973&#160; -37.969&#160; 66.973&#160;&#160; -26.719 69.763&#160; -26.719  
    69.763&#160; -21.094&#160;&#160; 72.553&#160; -21.094&#160; 72.553&#160;&#160; -18.281 80.919&#160; -18.281  
    80.919&#160; -23.906&#160;&#160; 83.705&#160; -23.906&#160; 83.705&#160;&#160; -52.031 80.919&#160; -52.031  
    80.919&#160; -63.281&#160;&#160; 83.705&#160; -63.281&#160; 83.705&#160;&#160; -85.781 80.919&#160; -85.781  
    80.919&#160; -97.031&#160;&#160; 78.131&#160; -97.031&#160; 78.131&#160;&#160; -99.844 69.763&#160; -99.844  
    69.763 -102.656&#160;&#160; 72.553 -102.656&#160; 72.553&#160; -116.719 69.763 -116.719  
    69.763 -119.531&#160;&#160; 72.553 -119.531&#160; 72.553&#160; -116.719 75.342 -116.719  
    75.342 -113.906&#160;&#160; 78.131 -113.906&#160; 78.131&#160; -116.719 75.342 -116.719  
    75.342 -125.156&#160;&#160; 72.553 -125.156&#160; 72.553&#160; -122.344 69.763 -122.344  
    69.763 -164.531  
    &#160;&#160;&#160; 66&#160;&#160;&#160;&#160;&#160;&#160; 1&#160;&#160; -36.278&#160; 113.906 -11.162&#160; 153.281  
    -36.278&#160; 136.406 -36.278&#160; 142.031 -39.068&#160; 142.031 -39.068&#160; 150.469  
    -33.487&#160; 150.469 -33.487&#160; 153.281 -25.115&#160; 153.281 -25.115&#160; 150.469  
    -19.534&#160; 150.469 -19.534&#160; 147.656 -16.744&#160; 147.656 -16.744&#160; 144.844  
    -13.953&#160; 144.844 -13.953&#160; 142.031 -16.744&#160; 142.031 -16.744&#160; 136.406  
    -11.162&#160; 136.406 -11.162&#160; 130.781 -13.953&#160; 130.781 -13.953&#160; 125.156  
    -16.744&#160; 125.156 -16.744&#160; 122.344 -19.534&#160; 122.344 -19.534&#160; 116.719  
    -22.325&#160; 116.719 -22.325&#160; 113.906 -30.697&#160; 113.906 -30.697&#160; 116.719  
    -36.278&#160; 116.719 -36.278&#160; 119.531 -33.487&#160; 119.531 -33.487&#160; 136.406  
    -36.278&#160; 136.406&#160;   
    &#160;&#160; -99&#160;&#160;&#160;&#160; -99  
    

![Continents_6](media/continents_6)  
 CONVERTING Gobal Mapping Tool (GMT) COASTLINES INTO VCS FORMAT ( written by Julien Vienne):    

A link to the full source code (i.e., gmt2vcs_continents.py) can be found _ _
 [ here ](/../files/gmt2vcs_continents.py/file_view)  _ _ .

[ ![Table of Contents](media/arrow-up) ](/)

[ ![Previous](media/arrow-left) ](/modifying-continents-plot)

[ ![Next](media/arrow-right) ](/save-plot-output)
