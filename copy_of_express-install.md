---
layout: default
title: Binaries 
---

##  Using the pre-built binaries
Explanation to install CDAT on your system. Using the pre-built binaries

###  Binaries Installation

Note:  There will be no support other than this page for the binary build, if it fails you will have to go with the source build. 

Go get the binary that best-match your system at:

[http://sourceforge.net/projects/cdat/files/](http://sourceforge.net/projects/cdat/files/)

Remember where you stored it (in this case `/Users/doutriaux1/cdat-5.2-MAC-10.5.7-leopard.tar.bz2`)

Then
    
    cd /
    sudo tar xjvf /Users/doutriaux1/cdat-5.2-MAC-10.5.7-leopard.tar.bz2

You now have a working cdat at:
    
    /opt/cdat/bin/cdat

Note: What if you don't have sudo

Then you can TRY to untar anywhere else say
    
    cd /Users/doutriaux1
    tar xjvf cdat-5.2-MAC-10.5.7-leopard.tar.bz2

    mv opt/cdat/* /PATH_TO_YOUR_CDAT

You will need AT LEAST to edit the `/PATH_TO_YOUR_CDAT/bin/cdat` and
`/PATH_TO_YOUR_CDAT/bin/vcdat` files And replace `/opt/cdat` with `/PATH_TO_YOUR_CDAT`

But that might still not be enough!

I would recomend to ask somebody with sudo to at least create a link back to
`/opt/cdat`
    
    ln -s /PATH_TO_YOUR_CDAT /opt/cdat
