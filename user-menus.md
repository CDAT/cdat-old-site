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

  * [ ![Send this page to somebody](media/mail_icon.gif) ](/cdat/tutorials/getting-started/user-menus/sendto_form)
  * [ ![Print this page](media/print_icon.gif) ](/this.print\(\))

#  Create-New-User-Menus

[ ![Table of Contents](media/arrow-up) ](/)

[ ![Previous](media/arrow-left) ](/animation)

[ Contents ](/)

[ Previous ](/color-map)

 Goal:  To introduce you creating your own user menus. 

![User-Menu](media/user-menu)  

To add your own menu in the main menu bar (i.e., just to the left of
"PCMDITools"), select in the main menu bar items: "Tools" -> "Add User New
Menu...". The following "User Menus" window will appear.  

![User-Menus-Popup](media/user-menus-popup)  

Enter the menu name and description of the menu, then select the "Add" button.
(For example, Menu name: "newMenu" and Description: "This is only a test!".)
The "newMenu" item will appear immediately in the main menu bar.  

![User-Menus-Label](media/user-menus-label)  

Add menu items functions to the "newMenu" item by editing the "Add function to
menu from file:" section. For this example, created a simple Python script in
your home directory (i.e., $HOME) called functions.py. In functions.py, create
two functions: func1 and func2.  

    
    
    # This is the first function in functions.py  
    def func1( d1 ):  
        nd = d1 * 100  
        return nd1  
      
    # This is the second function in functions.py  
    def func2 ( d1, d2 ):  
        nd = d1 * d2  
        return nd   
    

Select the "Browse" button and select the "functions.py" file in your home
directory. (Or if you know the path and file name, you can type the
information directly into the entry window.) The functions (i.e., "func1" and
"func2") will be displayed in the "Function" row. Select the "Add" button to
include the function as a pulldown menu item option. This action will cause
the "func1" to immediately appear under "newMenu" as a menu item. Select the
arrow button in the "Function" row and select&#160; "func2". In the "Function name"
row enter "multiply", then the "Add" button. This action will cause "func2" to
be listed in "newMenu" as the name "multiply".  

    
    
    Note to SuSE 9.1 users: Some users have stated that when they click on  
    the "Browse" button from the "User menus" window nothing appears to  
    happen. However, when they move the "User menus" window, the "File  
    Selection" window is there behind the "User menus" rather than in front  
    of it. This problem is specific to the SuSE 9.1 platform.

To add a function from an import module, toggle the "File" choice button to
"Import". Select or enter the desired import module. Then select the desired
function (e.g., "MV" and "cos". The function will immediately appear in the
pull down menu.  
  
Follow the menu panel instructions to "Remove or Rename a function" and to
"Delete a user menu".  
  

![User-Menus-Item](media/user-menus-item)  

   
Using the new function "func1":  
 Reselect the variable "clt" in the "Variable" selection window. Then select the cyan colored "Define" button. This action will copy the "clt" variable into memory and display it in the "Defined Variables" window below. Select the "clt (120, 46, 72)" variable in the "Defined Variables" window. This will reinitialize the "Dimension Manipulation Panel" and highlight the panel in cyan color. Now select the "newMenu" -> "func1" menu item. A new variable "clt_functions_func1 (120, 46, 72)" shows up in the "Defined Variables list. That is, the function "func1" multiplied the variable "clt" by 100.0.   
  

![User-Menus-func1](media/user-menus-func1)  

 Using the new function "multiply":   
 Select the variable "u" in the "Variable" selection window. Then select the cyan colored "Define" button. This action will copy the "u" variable into memory and display it in the "Defined Variables" window below. Do the same for the variable "v". In the "Defined Variables" window, select the "u (2, 80, 97)" variable, then select the "v (2, 80, 97) variable. Now select the "newMenu" -> "multiply" menu item. A new variable "u_functions_multiply (2, 80, 97)" will appear in the "Defined Variables list. That is, the variables "u" and "v" were multiplied together according to "func2". 

  

![User-Menus-Multiply2](media/user-menus-multiply2)  

 Using the new function "cos":   
 Reselect the variable "clt" in the "Variable" selection window. Then select the cyan colored "Define" button. This action will copy the "clt" variable into memory and display it in the "Defined Variables" window below. Select the "clt (120, 46, 72)" variable in the "Defined Variables" window. This will reinitialize the "Dimension Manipulation Panel" and highlight the panel in cyan color. Now select the "newMenu" -> "cos" menu item. A new variable "clt_MV_cos (120, 46, 72)" shows up in the "Defined Variables list.   

  

![User-Menus-Cos](media/user-menus-cos)  

[ ![Table of Contents](media/arrow-up) ](/)

[ ![Previous](media/arrow-left) ](/animation)
