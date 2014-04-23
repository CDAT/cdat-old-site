---
layout: default
title: Printing to ASCII
---

##  Printing to an ASCII File

In this tutorial we show how to write data to an ascii file

    # First open the ascii file
    # Note we do NOT use the cdms.open here!
    f=open('text.txt','w') 
    
    # Now writing to the file works just like writing to the screen
    print >> f, '# Example file to write data to it'
    
    # At the end do not forget to close the file
    f.close()
