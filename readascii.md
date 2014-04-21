---
layout: default
title: 
---


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

  * [ ![Send this page to somebody](media/mail_icon.gif) ](/cdat/tutorials/cdatbasics/files/readascii/sendto_form)
  * [ ![Print this page](media/print_icon.gif) ](/this.print\(\))

#  Opening and Reading an ASCII file

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
    &#160;   # we are only interested in the 2nd and third column here  
        try:  
    &#160;&#160;&#160;     val1=float(sp[1])   # second column  
    &#160;&#160;&#160;     val2=float(sp[2])   # third column  
    &#160;&#160;&#160;       
            data1.append(val1)  
    &#160;&#160;&#160;     data2.append(val2)  
      
    &#160;   except:  
    &#160;&#160;&#160;     pass       #&#160; we didn't have 2 float at the begining of this line  
      
      
    # Now converts the 2 datasets to MV for use in other CDAT Packages  
    data1=MV.array(data1,id='dataset1')  
    data2=MV.array(data2,id='dataset2')  
