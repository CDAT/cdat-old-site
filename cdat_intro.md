---
layout: default
title: CDAT Introduction
---

###CDAT Introduction

Climate Data Analysis Tools (  CDAT  ) is a software infrastructure that
uses an object-oriented scripting language to link together separate software
subsystems and packages thus forming an integrated environment for solving
model diagnosis problems. The power of the system comes from Python and its
ability to seamlessly interconnect software. Python provides a general purpose
and full-featured scripting language with a variety of user interfaces
including command-line interaction, stand-alone scripts (applications) and
graphical user interfaces (GUI). The CDAT subsystems, implemented as modules,
provide access to and management of gridded data (Climate Data Management
System or  CDMS  ); large-array numerical operations (Numerical Python);
and visualization (Visualization and Control System or  VCS  ).

![](media/images/simple_plot_2)
CDAT Isofill Plot of Total Cloudiness

One of the most difficult challenges facing climate researchers today is the
cataloging and analysis of massive amounts of multi-dimensional global
atmospheric and oceanic model data. To reduce the labor intensive and time-
consuming process of data management, retrieval, and analysis, PCMDI and other
DOE sites have come together to develop intelligent filing system and data
management software for the linking of storage devices located throughout the
United States and the international climate research community. This effort
known as the [Earth System Grid](http://esgf.org) (ESG) and headed by PCMDI, NCAR, and ANL
will allow users anywhere to remotely access this distributed multi-petabyte
archive and perform analysis. PCMDI's CDAT utilizes ESG and is an innovative
system that supports exploration and visualization of climate scientific
datasets. As an "open system", the software sub-systems (i.e., modules) are
independent and freely available to the global climate community. CDAT is
easily extended to include new modules and as a result of its flexibility,
PCMDI has integrated other popular software components, such as: the popular 
[Live Access Server](http://ferret.pmel.noaa.gov/Ferret/LAS/ferret_LAS.html) (LAS) and the 
[Open Data Access Protocol](http://www.opendap.org) (OPeNDAP) - formerly known by the name Distributed
Oceanographic Data System (DODS). Together with ANL's [Globus](http://www.cgt.isi.edu/about.php)
middleware software, CDAT's focus is to allow climate researchers the ability
to access and analyze multi-dimensional distributed climate datasets.
