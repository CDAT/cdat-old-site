---
layout: default
title: 
---

##  What is the Visualization and Control System
Data visualization is a very important aspect of analyzing data. The
Visualization and Control System, developed by the Program for Climate Model
Diagnosis and intercomparison (PCMDI) at the Lawrence Livermore National
Laboratory, was designed to provide some of the basic capabilities needed for
validating, comparing, and diagnosing climate model behavior. VCS can be
controlled either interactively or from a script file, or control can
alternate between these modes during a CDAT session. A Python or VCS script
can be saved during an interactive session and merely replayed, or it can be
edited and replayed. The state-of-the-system can be dumped as a script, at any
instant, and that script can be used later to restore that instant of the
session.  

A graphics display page is made up of one or more graphics pictures. Each
picture is defined by a trio of named objects: a picture template, a graphics
method, and data. These three objects are termed "Primary Objects" in VCS. The
picture template (or template for short) determines the appearance of each
segment of the display. The graphics method specifies the display technique
(e.g., contour, vector, boxfill, etc.). The data defines what to display.
Tables of attribute sets have been created for each of the primary objects,
and VCS provideds the user with the capability for creating a picture by
choosing entries from these tables. Once a picutre is created, it can be
manipulated by changing the choice of primary objects or by altering them. VCS
also includes secondary objects that describe text, lines, markers, fill
areas, patterns, colormaps, format, and lists. These secondary obects are used
to assign some of the attributes to the primary objects. Pictures can be
manipulated by choosing different secondary objects or by directly altering
these basic elements.  

By combining primary and secondary objects in various ways (either at the
command line or in a program), the VCS user can comprehensively diagnose and
inter-compare climate model simulations. VCS capabilities includes:  

* Create and modify existing template attributes and graphics methods; 
* Save the state-of-the-system as a script to be run interactively or in a program; 
* Save a display as a Computer Graphics Metafile (CGM), GIF, Postscript, Sun Raster, Encapsulated Postscript, TIF, etc.; 
* Create and modify colormaps; 
* Zoom into a specified portion of a display; 
* Change the orientation (portrait vs. landscape) or size (partial vs. full-screen) of a display; 
* Animate a single data variable or more than one data variable simultaneously; 
* Display different map projection and continental outlines; and   
* Provide point and click graphical feedback.   
