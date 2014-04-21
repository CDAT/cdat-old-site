---
layout: default
title: 
---


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

  * [ ![Send this page to somebody](media/mail_icon.gif) ](/cdat/tutorials/getting-started/accessing-ipcc-data-from-vcdat/sendto_form)
  * [ ![Print this page](media/print_icon.gif) ](/this.print\(\))

#  Accessing IPCC data from VCDAT

VCDAT OPeNDAP server access  

[ ![Table of Contents](media/arrow-up.gif) ](/index.html)

[ ![Previous](media/arrow-left.gif) ](/user-menus)

[ ![Next](media/arrow-right.gif) ](/index.html)

[ Contents ](/index.html)

[ Previous ](/user-menus)

[ Next ](/index.html)

 Goal:  To learn about OPeNDAP access from VCDAT. 

New CDAT v4.1 enables [ OPeNDAP ](/) interface to the  [ IPCC ](/) [ ESG
](/index.jsp) climate model simulations data holdings.&#160; The OPeNDAP server
enables to authenticate the user access, list files and subdirectories,
display metadata information, allow user to browse and download the chosen
data&#160; directly into the VCDAT for analysis.

[ OPeNDAP ](/) is a software framework that allows access to remote scientific
datasets. The core of OPeNDAP is a specification of an http-based protocol
that describes how clients and servers should communicate data over the
network. There are a variety of clients and servers available that understand
DAP; an adaptation of the  [ PyDAP ](/) server is being used for the IPCC AR4
model output database.  

  

The server provides access to IPCC datasets. A  dataset  is an aggregation of
a set of related data files into a single virtual file. In general, a dataset
consists of all data variables for a given combination of model, scenario,
experimental&#160; run, temporal frequency, and&#160; submodel (ocean or atmosphere). A
dataset is represented by a  [ CDMS XML
](/../../cdat/manuals/cdms_v4.0_html/ch6_cdms_4.0.html) file.  

  

Be aware that there is a definite overhead to accessing data through the
OPeNDAP server. Network speed, HTTP protocol, and server delays combine to
limit access speed in comparison to direct disk reads.  

  
You can access the IPCC AR4 data in a variety of ways:  

  * from VCDAT 
  * from CDMS 
  * through &#160;the web browser 

  
To access the IPCC data  from VCDAT  click on the '  Portal Internet Manager
' Button as shown in the image below (click on the image to see the bigger
picture)  
  

[ ![vcdat main window](media/vcdat_main_s.jpg) ](/images/vcdat_main.jpg)  

This will open a new window with the data holdings directory. For your
convenience the IPCC AR4 data portal catalog has been selected. In the future,
more portal catalogs will be added.

[ ![opendap main window](media/vcdat_opendap_s.jpg)
](/images/vcdat_opendap.jpg)

Click on&#160;the '  PyDAP server  ' tab (  \+  ) to open it  
  

[ ![opendap 1](media/vcdat_opendap1_s.jpg) ](/images/vcdat_opendap1.jpg)

When you further click on the choosen model run, first you will be presented
with the password authentication window, and after entering the username and
password to the IPCC AR4 data holdings, you will see the metadata for the
choosen dataset appear in the right window.

Click on the '  Open File  ' or '  Open File and Exit  '  buttons at the
bottom of the window to import the data into the VCDAT. From there on, you can
select the variable in the VCDAT in the usual way and plot it.

[ ![opendap and vcdat](media/vcdat_opendap4s.jpg)
](/images/vcdat_opendap4-800.jpg)

To learn how to access the IPCC data  from CDMS module  and  from the web
browser  see [ IPCC OPeNDAP Server ](/software-
portal/esg_data_portal/dapserver/) page.

  
  

[ ![Table of Contents](media/arrow-up.gif) ](/index.html)

[ ![Previous](media/arrow-left.gif) ](/user-menus)

[ ![Next](media/arrow-right.gif) ](/index.html)
