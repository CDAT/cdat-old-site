---
layout: default
title: Create Axes 
---
##  Creating Axes
Explains how to create axes, and what is important to know about them.

Axes are important in CDAT because they add information about the variable.  
A variable is basically an array with a lot of information associated with
itself.  
Axes are very important as they describe the array's dimensions  
  
There's basically 4 important things on an axes  
    
1. its  values   
2. its name or  id  
3. its  bounds    
4. its  units   
  
Let's say in this example that we a dataset representing the amount of rain in
a day.  
Also we'll say that the data are only collected if it actually rained  
  
Here are the mini dataset will be using  
  
Date   | Value  
---    | ---
Jan  3 | 2 cm  
Jan  5 | 15 cm  
Jan 17 | 3.5 cm  
Jan 23 | 4 cm  
    
    # Let's import the necessary modules  
    import cdms,MV  
      
    # Let's create the variable first  
    rain = MV.array([2.,15.,3.5,4.])  
    rain.id    = 'pr'  
    rain.units = 'cm'  
      
    # Now we need to create the associated "time" axis, let's use days' since 2005 as units  
    # First the axis itslef with its values  
    # values can be passed as a list, an array or a variable  
    time = cdms.createAxis([2,4,16,22]) # Remember Jan 1st, is 0 days since Jan 1st!  
    # Now let's name it  
    time.id = 'time'  
    # Let's give it some units  
    time.units = 'days since 2005-1-1'  
      
    # Another very important attribute are the bounds, indeed we need to know the "extend" of each value  
    # Here we will assume that the data span a full day everytime, but they could as well spend a few hours   
    # of these days only  
      
    bounds = MV.array ([[2.,3.],  
    		    [4.,5.],  
    		    [16.,17.],  
    		    [22.,23.] ])  
      
    time.setBounds(bounds)  
      
    # Now we have to link the variable dimension to this axes object  
      
    rain.setAxis(0,time)  
      
    rain.info()

---    

    *** Description of Slab pr ***
    id: pr
    shape: (4,)
    filename:
    missing_value: None
    comments:
    grid_name: N/A
    grid_type: N/A
    time_statistic:
    long_name:
    units:
    No grid present.
    ** Dimension 1 **
       id: time
       Designated a time axis.
       units:  days since 2005-1-1
       Length: 4
       First:  2
       Last:   22
       Python id:  -0x486cf214
    *** End of description for pr ***
