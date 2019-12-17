---
title: Configure event handlers for model-driven app Main forms in Power Apps | MicrosoftDocs
description: Understand how to configure event handlers
author: Mattp123
ms.author: matp
manager: kvivek
ms.date: 06/27/2018
ms.service: powerapps
ms.topic: article
ms.assetid: dc0ebb3f-0c00-413a-968f-9cfd107055c0
search.audienceType: 
  - maker
search.app: 
  - PowerApps
  - D365CE
---
# Configure model-driven app form event handlers

 Form event handlers for Power Apps forms can be configured for the following areas in a form:  
  
|Element|Event|Description|  
|-------------|-----------|-----------------|  
|Form|`OnLoad`|Occurs when the form loads.|  
||`OnSave`|Occurs when data is saved.|  
|Tab|`TabStateChange`|Occurs when the tab is expanded or collapsed.|  
|Field|`OnChange`|Occurs when data in the field changes and the control loses focus.|  
|IFRAME|`OnReadyStateComplete`|Occurs when the content of an IFRAME loads.|  
  
 An event handler consists of a reference to a JavaScript web resource and a function defined within that web resource that will execute when the event occurs. Each element can have up to 50 separate event handlers configured.  
  
> [!IMPORTANT]
>  Configuring an event handler incorrectly can result in script errors that may cause the form to fail to load or function correctly. If you are not the developer of the script, make sure you understand exactly what configuration options the script requires.  
>   
>  Do not configure a script event handler using a library that does not come from a source you trust. Scripts can be used to perform any action a user might perform and a poorly written script can significantly damage the performance of a form.  
>   
>  After you configure an event handler always test it to verify it is working correctly.  
  
### To configure an event handler 
  
1.  In the form editor, select the element with the event you want to configure a handler for.  
  
2.  On the [Home tab](form-editor-user-interface-legacy.md#home-tab), in the **Edit** group, select **Change Properties** or simply double-click the element.  
  
3.  In the element properties dialog, select the **Events** tab.  
  
4.  Expand the **Form Libraries** area. If the library containing the function you want to set as the event handler is not already listed, add the library.  
  
5.  To add a form library to an event handler:  
    1.  In the **Form Libraries** section of the **Event List**, select **Add**.  
  
    2.  Locate the JavaScript web resource in the list of available web resources. Select it and then select **Add**.  
  
         If the JavaScript web resource you need does not exist, select **New** to open a new web resource form and create one.  
  
    3.  To create a JavaScript web resource:  
        1.  In the web resource form set the following properties:  
  
            |Property|Value|  
            |--------------|-----------|  
            |Name|**Required**. Type the name of the web resource.|  
            |Display Name|**Required**. Type the name to be displayed in the list of web resources.|  
            |Description|Optional. Type a description of the web resource.|  
            |Type|**Required**. Select **Script (JScript)**.|  
            |Language|Optional. Choose one of the languages available for your organization.|  
  
        2.  If you have been provided with a script, we highly recommend that you use the **Browse** button to locate the file and upload it.  
  
             Alternatively, you can select the **Text Editor** button and paste or type the contents of the script in the **Edit Content** dialog.  
  
            > [!NOTE]
            >  Because this simple text editor does not provide any features to check the correctness of the script, generally you should always try to use a separate application like Visual Studio to edit scripts and then upload them.  
  
        3.  Select **Save** and close the web resource dialog.  
  
        4.  The web resource you created is now selected in the **Look Up Record** dialog. Select **Add** to close the dialog.  
6.  In the **Event Handlers** section, select the event you want to set an event handler for.  
  
7.  Select **Add** to open the **Handler Properties** dialog.  
  
8. On the **Details** tab choose the appropriate library and type the name of the function that should be executed for the event.  
  
9. By default the event handler is enabled. Clear the **Enabled** checkbox if you do not want to enable this event.  
  
     Some functions require an execution context to be passed to the function. Select **Pass execution context as the first parameter** if it is required.  
  
     Some functions can accept a set of parameters to control the behavior of a function. If these are required, enter them in the **Comma separated list of parameters that will be passed to the function**.  
  
10. On the **Dependencies** tab, add any fields that the script depends on into the **Dependent Fields** area.  
  
11. Select **OK** to close the **Handler Properties** dialog.  
  
12. When the event handler is entered you may adjust the order in which the function will be executed relative to any other functions by using the green arrows to move it up or down.  
  
13. Select **OK** to close the element properties dialog.  
  
14. Select **Save** to save your changes. Select **Publish** to publish the form.  
  
> [!NOTE]
>  While the user interface (UI) lets you adjust the order in which the scripts are loaded by using the up and down green arrows, the scripts are actually not loaded sequentially.   

## Next steps

[Use the Main form and its components](use-main-form-and-components.md)
