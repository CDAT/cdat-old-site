---
layout: default
title: VCS Chapter 1
---

##  CHAPTER 1 Introduction

The PCMDI Visualization Control System (VCS) is expressly designed to meet the
needs of climate scientists. Because of the breadth of its capabilities, VCS
can be a useful tool for other scientific applications as well. VCS allows
wide-ranging changes to be made to the data display, provides for hardcopy
output, and includes a means for recovery of a previous display.

![](vcs-2.gif)

Basic Concepts of VCS

In the VCS model, the data display is defined by a trio of named object sets,
designated the "primary objects" (or "primary elements"). These include:

  * the data, which define what is to be displayed and is ingested into the system via other PCMDI software components or via the Numeric module; 
  * the graphics method, which specifies the display technique; and 
  * the picture template, which determines the appearance of each segment of the display. Tables for manipulating these primary objects are stored in VCS for later recall and possible use.

In addition, detailed specification of the primary objects' attributes is
provided by eight "secondary objects" (or secondary elements"):

  1. colormap: specification of combinations of 256 available colors 
  2. fill area: style, style index, and color index 
  3. format: specifications for converting numbers to display strings 
  4. line: line type, width and color index 
  5. list: a sequence of pairs of numerical and character values 
  6. marker: marker type, size, and color index 
  7. text: text font type, character spacing, expansion and color index 
  8. text orientation: character height, angle, path, and horizontal/vertical alignment 

By combining primary and secondary objects in various ways (either at the
command line or in a program), the VCS user can comprehensively diagnose and
intercompare climate model simulations. VCS provides capabilities to:

  * View, select and modify attributes of data variables and of their dimensions
  * Create and modify existing template attributes and graphics methods
  * Save the state-of-the-system as a script to be run interactively or in a program
  * Save a display as a Computer Graphics Metafile (CGM), GIF, Postscript, Sun Raster, or Encapsulated Postscript file 
  * Perform grid transformations and compute new data variables 
  * Create and modify color maps
  * zoom into a specified portion of a display 
  * Change the orientation (portrait vs. landscape) or size (partial vs. full-screen) of a display 
  * Animate a single data variable or more than one data variable simultaneously
  * Display different map projections

####

![](vcs-2.gif)

Purpose of this document

This document will focus primarily on the VCS software commands necessary to
operate VCS with minimal knowledge. The knowledge of VCS will gradually be
increased allowing the user to construct more complex visualization operations
that are vital to their scientific research. The material contained in this
document will walk you through simple VCS operations and use CDMS module to
ingest data sets and to manipulate the data before it is displayed. Because
the best way to learn a new tool is by examples, this document is heavy on
examples and provides an extensive command reference guide.

######  Guide to This Document

Chapter Title and Location

Purpose

[VCS Installation and Setup](vcs-2.html#18892)

This chapter explains how to install and test VCS (either from the source code
or from the distributed shared library).

[Selecting or Creating Data](vcs-3.html#79985)

This chapter explains the type of data needed for the VCS module and how to
read data into the module.

[Overview](vcs-4.html#60683)

Overview chapter explaining VCS's Python Application Interface.

[VCS Command Reference Guide](vcs-5.html#41289)

If you need to know the full extent of a command and all of its parameters,
then this is where you want to be.

[VCS Primary Objects](vcs-6.html#22687)

VCS primary object list and their members.

[VCS Secondary Objects](vcs-7.html#85913)

VCS secondary object list and their members.

[VCS Examples](vcs-8.html#83780)

This chapter has examples showing how to use VCS in the Python environment. If
you just want to get started, then we suggest you start with this chapter in
conjunction with Chapter 5.

[Quick Reference Guides](vcs-9.html#19907) 9\. Includes a one-page "cheat
sheet" on page [VCS Cheat Sheet](vcs-9.html#10473).

If you need a command in a hurry or want to review a command quickly, then
this is the place to be.

[Fonts, Lines, Markers, and Patterns](vcs-10.html#20702)

Font, line, marker, and pattern symbols.

[Go to Main](vcs.html) [Go to Previous](vcs.html) [Go to Next](vcs-2.html)


