---
layout: default
title: CDMS Table of Contents
---

# CDMS Manual

## Table of Contents

### [CHAPTER 1 Introduction](cdms_chapter_1.html)

- [1.1 Overview](cdms_chapter_1.html#1.1)
- [1.2 Variables](cdms_chapter_1.html#1.2)
- [1.3 File I/O](cdms_chapter_1.html#1.3)
- [1.4 Coordinate Axes](cdms_chapter_1.html#1.4)
- [1.5 Attributes](cdms_chapter_1.html#1.5)
- [1.6 Masked values](cdms_chapter_1.html#1.6)
- [1.7 File Variables](cdms_chapter_1.html#1.7)
- [1.8 Dataset Variables](cdms_chapter_1.html#1.8)
- [1.9 Grids](cdms_chapter_1.html#1.9)
    - [1.9.1 Example: a curvilinear grid](cdms_chapter_1.html#1.9.1)
    - [1.9.2 Example: a generic grid](cdms_chapter_1.html#1.9.2)
- [1.10 Regridding](cdms_chapter_1.html#1.10)
    - [1.10.1 CDMS Regridder](cdms_chapter_1.html#1.10.1)
    - [1.10.2 SCRIP Regridder](cdms_chapter_1.html#1.10.2)
- [1.11 Time types](cdms_chapter_1.html#1.11)
- [1.12 Plotting data](cdms_chapter_1.html#1.12)
- [1.13 Databases](cdms_chapter_1.html#1.13)

### [CHAPTER 2 CDMS Python Application Programming Interface](cdms_chapter_2.html)

- [2.1 Overview](cdms_chapter_2.html#2.1)
    - [Table 2.1 Python types used in CDMS](cdms_chapter_2.html#table_2.1)
- [2.2 A first example](cdms_chapter_2.html#2.2)
- [2.3 cdms module](cdms_chapter_2.html#2.3)
    - [Table 2.2 cdms module functions](cdms_chapter_2.html#table_2.2)
    - [Table 2.3 Class Tags](cdms_chapter_2.html#table_2.3)
- [2.4 CdmsObj](cdms_chapter_2.html#2.4)
    - [Table 2.4 Attributes common to all CDMS objects](cdms_chapter_2.html#table_2.4)
    - [Table 2.5 Getting and setting attributes](cdms_chapter_2.html#table_2.5)
- [2.5 CoordinateAxis](cdms_chapter_2.html#2.5)
    - [Table 2.6 CoordinateAxis types](cdms_chapter_2.html#table_2.6)
    - [Table 2.7 CoordinateAxis Internal Attributes](cdms_chapter_2.html#table_2.7)
    - [Table 2.8 Axis Constructors](cdms_chapter_2.html#table_2.8)
    - [Table 2.9 CoordinateAxis Methods](cdms_chapter_2.html#table_2.9)
    - [Table 2.10 Axis Methods, additional to CoordinateAxis methods](cdms_chapter_2.html#table_2.10)
    - [Table 2.11 Axis Slice Operators](cdms_chapter_2.html#table_2.11)
- [2.6 CdmsFile](cdms_chapter_2.html#2.6)
    - [Table 2.12 CdmsFile Internal Attributes](cdms_chapter_2.html#table_2.12)
    - [Table 2.13 CdmsFile Constructors](cdms_chapter_2.html#table_2.13)
    - [Table 2.14 CdmsFile Methods](cdms_chapter_2.html#table_2.14)
    - [Table 2.15 CDMS Datatypes](cdms_chapter_2.html#table_2.15)
- [2.7 Database](cdms_chapter_2.html#2.7)
    - [2.7.1 Overview](cdms_chapter_2.html#2.7.1)
        - [Table 2.16 Database Internal Attributes](cdms_chapter_2.html#table_2.16)
        - [Table 2.17 Database Constructors](cdms_chapter_2.html#table_2.17)
        - [Table 2.18 Database Methods](cdms_chapter_2.html#table_2.18)
    - [2.7.2 Searching a database](cdms_chapter_2.html#2.7.2)
        - [Table 2.19 SearchResult Methods](cdms_chapter_2.html#table_2.19)
        - [Table 2.20 ResultEntry Attributes](cdms_chapter_2.html#table_2.20)
        - [Table 2.21 ResultEntry Methods](cdms_chapter_2.html#table_2.21)
    - [2.7.3 Accessing data](cdms_chapter_2.html#2.7.3)
    - [2.7.4 Examples of database searches](cdms_chapter_2.html#2.7.4)
- [2.8 Dataset](cdms_chapter_2.html#2.8)
    - [Table 2.22 Dataset Internal Attributes](cdms_chapter_2.html#table_2.22)
    - [Table 2.23 Dataset Constructors](cdms_chapter_2.html#table_2.23)
    - [Table 2.24 Open Modes](cdms_chapter_2.html#table_2.24)
    - [Table 2.25 Dataset Methods](cdms_chapter_2.html#table_2.25)
- [2.9 MV module](cdms_chapter_2.html#2.9)
    - [Table 2.26 Variable Constructors in module MV](cdms_chapter_2.html#table_2.26)
    - [Table 2.27 MV functions](cdms_chapter_2.html#table_2.27)
- [2.10 HorizontalGrid](cdms_chapter_2.html#2.10)
    - [Table 2.28](cdms_chapter_2.html#table_2.28)
    - [Table 2.29 HorizontalGrid Internal Attributes](cdms_chapter_2.html#table_2.29)
    - [Table 2.30 RectGrid Constructors](cdms_chapter_2.html#table_2.30)
    - [Table 2.31 HorizontalGrid Methods](cdms_chapter_2.html#table_2.31)
    - [Table 2.32 RectGrid Methods, additional to HorizontalGrid Methods](cdms_chapter_2.html#table_2.32)
- [2.11 Variable](cdms_chapter_2.html#2.11)
    - [Table 2.33 Variable Internal Attributes](cdms_chapter_2.html#table_2.33)
    - [Table 2.34 Variable Constructors](cdms_chapter_2.html#table_2.34)
    - [Table 2.35 Variable Methods](cdms_chapter_2.html#table_2.35)
    - [Table 2.36 Variable Slice Operators](cdms_chapter_2.html#table_2.36)
    - [Table 2.37 Index and Coordinate Intervals](cdms_chapter_2.html#table_2.37)
    - [2.11.1 Selectors](cdms_chapter_2.html#2.11.1)
        - [Table 2.38 Selector keywords](cdms_chapter_2.html#table_2.38)
    - [2.11.2 Selector examples](cdms_chapter_2.html#2.11.2)
- [2.12 Examples](cdms_chapter_2.html#2.12)

### [CHAPTER 3 cdtime Module](cdms_chapter_3.html)

- [3.1 Time types](cdms_chapter_3.html#3.1)
- [3.2 Calendars](cdms_chapter_3.html#3.2)
- [3.3 Time Constructors](cdms_chapter_3.html#3.3)
    - [Table 3.1 Time Constructors](cdms_chapter_3.html#table_3.1)
- [3.4 Relative Time](cdms_chapter_3.html#3.4)
    - [Table 3.2 Relative Time Members](cdms_chapter_3.html#table_3.2)
- [3.5 Component Time](cdms_chapter_3.html#3.5)
    - [Table 3.3 Component Time Members](cdms_chapter_3.html#table_3.3)
- [3.6 Time Methods](cdms_chapter_3.html#3.6)
    - [Table 3.4 Time Methods](cdms_chapter_3.html#table_3.4)

### [CHAPTER 4 Regridding Data](cdms_chapter_4.html)

- [4.1 Overview](cdms_chapter_4.html#4.1)
    - [4.1.1 CDMS horizontal regridder](cdms_chapter_4.html#4.1.1)
    - [4.1.2 SCRIP horizontal regridder](cdms_chapter_4.html#4.1.2)
    - [4.1.3 Pressure-level regridder](cdms_chapter_4.html#4.1.3)
    - [4.1.4 Cross-section regridder](cdms_chapter_4.html#4.1.4)
- [4.2 regrid module](cdms_chapter_4.html#4.2)
    - [4.2.1 CDMS horizontal regridder](cdms_chapter_4.html#4.2.1)
        - [Table 4.1 CDMS Regridder Constructor](cdms_chapter_4.html#table_4.1)
    - [4.2.2 SCRIP Regridder](cdms_chapter_4.html#4.2.2)
        - [Table 4.2 SCRIP Regridder Constructor](cdms_chapter_4.html#table_4.2)
- [4.3 regridder functions](cdms_chapter_4.html#4.3)
    - [4.3.1 CDMS regridder functions](cdms_chapter_4.html#4.3.1)
        - [Table 4.3 CDMS Regridder function](cdms_chapter_4.html#table_4.3)
    - [4.3.2 SCRIP Regridder functions](cdms_chapter_4.html#4.3.2)
        - [Table 4.4 SCRIP Regridder functions](cdms_chapter_4.html#table_4.4)
- [4.4 Examples](cdms_chapter_4.html#4.4)
    - [4.4.1 CDMS regridder](cdms_chapter_4.html#4.4.1)
    - [4.4.2 SCRIP regridder](cdms_chapter_4.html#4.4.2)

### [CHAPTER 5 Plotting CDMS data in Python](cdms_chapter_5.html)

- [5.1 Overview](cdms_chapter_5.html#5.1)
- [5.2 Examples](cdms_chapter_5.html#5.2)
    - [5.2.1 Example: plotting a gridded variable](cdms_chapter_5.html#5.2.1)
    - [5.2.2 Example: using plot keywords.](cdms_chapter_5.html#5.2.2)
    - [5.2.3 Example: plotting a time-latitude slice](cdms_chapter_5.html#5.2.3)
    - [5.2.4 Example: plotting subsetted data](cdms_chapter_5.html#5.2.4)
- [5.3 plot method](cdms_chapter_5.html#5.3)
    - [Table 5.1 plot keywords](cdms_chapter_5.html#table_5.1)

### [CHAPTER 6 Climate Data Markup Language (CDML)](cdms_chapter_6.html)

- [6.1 Introduction](cdms_chapter_6.html#6.1)
- [6.2 Elements](cdms_chapter_6.html#6.2)
    - [Table 6.1 CDML Tags](cdms_chapter_6.html#table_6.1)
- [6.3 Special Characters](cdms_chapter_6.html#6.3)
    - [Table 6.2 Special Character Encodings](cdms_chapter_6.html#table_6.2)
- [6.4 Identifiers](cdms_chapter_6.html#6.4)
- [6.5 CF Metadata Standard](cdms_chapter_6.html#6.5)
- [6.6 CDML Syntax](cdms_chapter_6.html#6.6)
    - [6.6.1 Dataset Element](cdms_chapter_6.html#6.6.1)
        - [Table 6.3 Dataset Attributes](cdms_chapter_6.html#table_6.3)
    - [6.6.2 Axis Element](cdms_chapter_6.html#6.6.2)
        - [Table 6.4 Axis Attributes](cdms_chapter_6.html#table_6.4)
    - [6.6.3 partition attribute](cdms_chapter_6.html#6.6.3)
    - [6.6.4 Grid Element](cdms_chapter_6.html#6.6.4)
        - [Table 6.5 RectGrid Attributes](cdms_chapter_6.html#table_6.5)
    - [6.6.5 Variable Element](cdms_chapter_6.html#6.6.5)
        - [Table 6.6 Variable Attributes](cdms_chapter_6.html#table_6.6)
    - [6.6.6 Attribute Element](cdms_chapter_6.html#6.6.6)
- [6.7 A Sample CDML Document](cdms_chapter_6.html#6.7)

### [CHAPTER 7 CDMS Utilities](cdms_chapter_7.html)

- [7.1 cdscan: Importing datasets into CDMS](cdms_chapter_7.html#7.1)
    - [7.1.1 Overview](cdms_chapter_7.html#7.1.1)
    - [7.1.2 cdscan Syntax](cdms_chapter_7.html#7.1.2)
        - [Table 7.1 cdscan command options](cdms_chapter_7.html#table_7.1)
    - [7.1.3 Examples](cdms_chapter_7.html#7.1.3)
    - [7.1.4 File Formats](cdms_chapter_7.html#7.1.4)
    - [7.1.5 Name Aliasing](cdms_chapter_7.html#7.1.5)

### [APPENDIX A CDMS Classes](cdms_appendix.html#a)

### [APPENDIX B Version Notes](cdms_appendix.html#b)

- [B.1 Version 4.0](cdms_appendix.html#b.1)
- [B.2 Version 3.0 Overview](cdms_appendix.html#b.2)
- [B.3 V3.0 Details](cdms_appendix.html#b.3)
    - [B.3.1 AbstractVariable](cdms_appendix.html#b.3.1)
    - [B.3.2 AbstractAxis](cdms_appendix.html#b.3.2)
    - [B.3.3 AbstractDatabase](cdms_appendix.html#b.3.3)
    - [B.3.4 Dataset](cdms_appendix.html#b.3.4)
    - [B.3.5 cdms module](cdms_appendix.html#b.3.5)
    - [B.3.6 CdmsFile](cdms_appendix.html#b.3.6)
    - [B.3.7 CDMSError](cdms_appendix.html#b.3.7)
    - [B.3.8 AbstractRectGrid](cdms_appendix.html#b.3.8)
    - [B.3.9 InternalAttributes](cdms_appendix.html#b.3.9)
    - [B.3.10 TransientVariable](cdms_appendix.html#b.3.10)
    - [B.3.11 MV](cdms_appendix.html#b.3.11)

### [APPENDIX C cu Module](cdms_appendix.html#c)

- [C.1 Slab](cdms_appendix.html#c.1)
    - [Table C.1 Slab Methods](cdms_appendix.html#table_c.1)
- [C.2 cuDataset](cdms_appendix.html#c.2)
    - [Table C.2 cuDataset Methods](cdms_appendix.html#table_c.2)