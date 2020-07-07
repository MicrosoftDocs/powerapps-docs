---
title: "Override the default open behavior of data rows in grids (model-driven apps) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "Provides information on how to override the default open behavior of the records in grids" # 115-145 characters including spaces. This abstract displays in the search result.
ms.custom: ""
ms.date: 07/08/2020
ms.reviewer: ""
ms.service: powerapps
ms.topic: "article"
author: "nkrb" # GitHub ID
ms.author: "nabuthuk" # MSFT alias of Microsoft employees only
manager: "kvivek" # MSFT alias of manager or PM counterpart
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---
# Override the default open behavior of data rows in an entity-bound grid

This article provides step-by-step instructions on how to override the default open behavior of data rows in an entity-bound grid. Currently, performing any of the following actions in a data row in an entity-bound grid opens the entity record by default:

- Double-clicking the data row or clicking the primary attribute link in the row.
- Selecting a data row, and pressing ENTER.
- On a touch-enabled device, selecting a data row.

There might be situations where you do not want the entity record to open, such as, for document management records, you might want to open a SharePoint site instead of displaying the record. You can now override the default behavior to define your own custom behavior.

> [!NOTE] 
> This feature is supported only for Unified Interface.

You can now create a command definition for an entity with `Mscrm.OpenRecordItem` as the value of the Id attribute `CommandDefinition`, and define custom action in the `Actions` tab. The application looks for this command Id for an entity when you try to open a record from the entity-bound grid, and if present, will execute the custom action instead of opening the entity record (default behavior).

You can override the default open behavior of data rows in two ways:

1. [Customizing XML file](#customizing-xml-file)
2. [Using Ribbon Workbench](#using-ribbon-workbench)

## Customizing XML file

To customize the xml file to override the default behavior, follow steps below:

### Step1: Create a web resource

Create a web resource to change the default behavior. For example, if you wish to open a SharePoint site instead of displaying the record, you need to create a JavaScript web resource. To create a web resource:

1. Open solution explorer, and then select **Web Resources**.

2. Under **Components**, choose **Web Resources**.

3. To create a web resource select **New**.

4. Enter the name of the web resource and select the **Type** as **Script(JScript)**.

5. Select the text editor, copy-paste the code shown below and  enter the url value:

   ```JavaScript
   function ChangeBehavior(){
    
    // Enter the SharePoint url
    var url =  "Enter SharePoint URL";
    var OpenUrlOptions = {height: 800, width: 1000, openInNewWindow:true};
    Xrm.Navigation.openUrl(url, openUrlOptions);
   }
   ```

6. Save and publish the web resource.

### Step2: Create a custom button

You need to create a custom button on the entity form where you want to change the default behavior. For example, if you have a subgrid on accounts form that displays contact records in the subgrid, you need to create a button and add custom action on the contact form. You can create buttons by editing the customization.xml file:

1. Create a new solution and add the entity where you want to create the button. 

2. Add the SiteMap to the newly creates solution. 

3. Add the web resource that we created earlier in the article. 

4. Save and publish the solution. 

5. From the solution explorer, select the solution and select **Export**. 

6. If you have made recent changes that have not yet been published, select **Publish All Customizations**. Otherwise, select **Next**.

7. With the Unmanaged option selected, select **Export**.

8. Select **Save** in the file download dialog box and then select **Open Folder** in the download complete dialog box.

9. Right-click the compressed .zip file that you downloaded and select **Extract All**.

10. Select a location to extract the files and then select **Extract**.

11. The customizations.xml file is the file that you will edit.

    > [!NOTE]
    > You can enable or disable the button, doing either of the ones will still override the open default behavior.

12. Open the customization.xml file and copy-paste the code shown below:

     ```XML
    <CustomActions>
    <CustomAction Id="Mscrm.OpenRecordItem.CustomAction" Location="Mscrm.SubGrid.account.MainTab.Management.Controls._children" Sequence="28">
      <CommandUIDefinition>
        <Button Alt="$LocLabels:Mscrm.OpenRecordItem.Alt" Command="Mscrm.OpenRecordItem" Id="Mscrm.OpenRecordItem" LabelText="$LocLabels:Mscrm.OpenRecordItem.LabelText" Sequence="28" TemplateAlias="o1" ToolTipTitle="$LocLabels:Mscrm.OpenRecordItem.ToolTipTitle" ToolTipDescription="$LocLabels:Mscrm.OpenRecordItem.ToolTipDescription" />
      </CommandUIDefinition>
      </CustomAction>
     </CustomActions>
    <Templates>
     <RibbonTemplates Id="Mscrm.Templates" />
    </Templates>
    <CommandDefinitions>
    <CommandDefinition Id="Mscrm.OpenRecordItem">
      <EnableRules />
      <DisplayRules />
      <Actions>
        <JavaScriptFunction FunctionName="sampleoperations" Library="$webresource:cr5c1_samplescript" />
      </Actions>
      </CommandDefinition>
       </CommandDefinitions>
     ```

### Step 3: Import the XML file


1. After you have edited the customization.xml file, right-click the customization.xml tab and select **Open Containing Folder**.  
2. Select all of the files or folders that were included when you extracted the solution. Right-click the selected files, select **Send To**, and then select **Compressed (zipped) folder**.  
  
   > [!NOTE]
   >  This creates a compressed .zip file in the same folder. The name of the file may vary, but it will be the same as one of the other files in the folder - except with a .zip file name extension.  
  
3. On the navigation bar, choose **Settings**. 
  
4. Go to **Settings** > **Customizations**.
  
5. Go to **Settings** > **Solutions**. 
  
6. Select **Import**.  
  
7. Select **Browse** and locate the compressed .zip file that you created in step 2 of this procedure.  
  
8. Select **Next**, and then select **Import**.  
  
9. After the import has finished, you will see the message indicating that the import completed successfully. Select Close.  
  
10. After you have successfully imported your solution, you must publish customizations before you can see the changes. In the Solutions list, select **Publish All Customizations**.  

 
## Using Ribbon Workbench

Ribbon Workbench tool allows developers to quickly create custom buttons on forms. Before you create a custom button to override the default open behavior, create a web resource as mentioned above to perform the custom action instead of the default open behavior. To create a custom button:

1. Create a new solution and add the entity where you want to create the button.

2. Add the web resource that we created earlier in the article.

3. Save and publish the solution.

4. Open the Ribbon workbench tool and sign in to the environment where you want to create the button.

5. Select **Open Solution** and select the solution from the list of available solutions.

6. Drag and drop the **Button** from the **ToolBox** tab and place it on the subgrid section.

   > [!div class="mx-imgBorder"]
   > ![ToolBox](media/toolbox-rwb.png "ToolBox")

7. Select **+** next to **Commands** and enter the details as shown below:

    > [!div class="mx-imgBorder"]
    > ![Command Window](media/command-windows.png "Command Window")

8. Similarly, select **+** next to **Button** and enter the details as shown below:

    > [!div class="mx-imgBorder"]
    > ![Button Window](media/button-properties-window.png "Button Window")

9. Select **Publish** to push the changes.

## See also

[Ribbon Workbench](https://www.develop1.net/public/rwb/ribbonworkbench.aspx)<br/>
[Customize the ribbon](customize-commands-ribbon.md)