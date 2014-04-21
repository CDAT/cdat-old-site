---
layout: default
title: 
---


  * [ ![Send this page to somebody](media/mail_icon.gif) ](/cdat/quick_reference/controlling-the-aspect-of-the-taylor-diagram/sendto_form)
  * [ ![Print this page](media/print_icon.gif) ](/this.print\(\))

#  Controlling The Aspect of the Taylor diagram

example to show how to control the taylordiagram aspects, also show a trick to
have 2 datasets plotted

The following example shows how to control aspect of a taylordiagram plot ( [
see image here ](/taylor.png) )  

    
    
    import vcs,MV2
    
    data=MV2.array([[5,.81],[6,.8],[4,.85],[4.5,.83]])
    print data.shape
    x=vcs.init()
    x.open()
    
    td=x.createtaylordiagram()
    td.referencevalue=5.
    t=x.createtemplate(source="deftaylor")
    #Sets the correlation major line
    l=x.createline()
    l.type='dash'
    l.width=1
    t.ytic2.x1=t.data.x1
    t.ytic2.line=l
    majorcor=vcs.mklabels([.1,.3,.6,.8,.9,.95,.99])
    td.cticlabels1=majorcor
    #Sets the correlation minor line
    l=x.createline()
    l.type='dot'
    l.width=1
    l.color=[252] # grey
    t.ymintic2.x1=t.data.x1
    t.ymintic2.line=l
    minorcor=vcs.mklabels([.2,.4,.5,.7,.85,.91,.92,.93,.94,.96,.97,.98,.998])
    td.cmtics1=minorcor
    #Sets standard dev major tics
    l=x.createline()
    l.type='dash'
    l.width=1
    t.xtic2.line=l
    t.xtic2.priority=1
    mjrstd1=vcs.mklabels([0.5,1.5,2.5,3.5,4.5,5.5,6.5,7.5,8.5,9.5])
    td.xticlabels1=mjrstd1
    mjrstd2=vcs.mklabels([0.,1.,2.,3.,4.,5.,6.,7.,8.,9.])
    td.yticlabels1=mjrstd2
    #Sets the std minor line
    l=x.createline()
    l.type='dot'
    l.width=1
    l.color=[252] # grey
    t.xmintic2.line=l
    t.xmintic2.priority=1
    mnrstd=vcs.mklabels(MV2.arange(0,10,.25))
    td.xmtics1=mnrstd
    td.ymtics1=mjrstd1
    #Sets the reference
    l=x.createline()
    l.type='solid'
    l.width=2
    l.color=[242] # red
    t.line2.line=l
    
    # Sets the maximum for arc value
    td.max=8.
    # ok now plots the first half of data with these settings
    x.plot(data[:2],t,td)
    
    # now we want another reference value with another color
    # we need to copy the template and graphic method
    t2=x.createtemplate(source=t)
    #Sets the reference
    l=x.createline()
    l.type='solid'
    l.width=2
    l.color=[244] # blue
    t2.line2.line=l
    
    td2=x.createtaylordiagram(source=td)
    td2.referencevalue=4.
    
    # ok now plots the first half of data with these
    x.plot(data[2:],t2,td2)
    raw_input()
