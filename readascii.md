---
layout: default
title: Opening ASCII Files
---

##  Opening and Reading an ASCII file

In this example we open an ASCII file and show how to read and parse its
content
    
    import string,sys,MV  
      
    # First of all we need to open the ASCII file  
    # For this we used the Python built-in command "open"  
    f=open(sys.prefix+'/sample_data/test_col.asc')  
      
    # Now we need to read its content  
    # To read all of its content we use the "readlines" command  
    # This returns a list of strings, each element of the list represents  
    # one line in the file  
    lines=f.readlines()  
      
    # Note to read one line at a time (inside a loop for example, if the ascii file is too big  
    # You can also f.readline()  
      
    # Now we can loop through the lines and look at the content  
    data1=[]  
    data2=[]  
      
    for line in lines:  
        # Splits the line into a list of string with seprartion   
        # when it finds space or tabs or return      
        sp=string.split(line)   
      
        # Now try to see if the first element is a number, if not skip  
       # we are only interested in the 2nd and third column here  
        try:  
         val1=float(sp[1])   # second column  
         val2=float(sp[2])   # third column  
           
            data1.append(val1)  
         data2.append(val2)  
      
       except:  
         pass       # we didn't have 2 float at the begining of this line  
      
    # Now converts the 2 datasets to MV for use in other CDAT Packages  
    data1=MV.array(data1,id='dataset1')  
    data2=MV.array(data2,id='dataset2')  
    
    # Just for fun prints the average of data1
    print MV.average(data1)
