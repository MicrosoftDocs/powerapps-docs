---
title: "Export, prepare to edit, and import the ribbon(model-driven apps) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "Learn about exporting the ribbon by including it in a solution and then exporting the solution. You can export all the customizations, but that can represent a large amount of data. We recommend that you use an existing unmanaged solution or create a new solution." # 115-145 characters including spaces. This abstract displays in the search result.
ms.custom: ""
ms.date: 08/01/2018
ms.reviewer: ""
ms.service: "powerapps"
ms.topic: "article"
author: "KumarVivek" # GitHub ID
ms.author: "kvivek" # MSFT alias of Microsoft employees only
manager: "shilpas" # MSFT alias of manager or PM counterpart
---
# Export, prepare to edit, and import the ribbon

<!-- https://docs.microsoft.com/en-us/dynamics365/customer-engagement/developer/customize-dev/export-prepare-edit-import-ribbon -->

To edit the ribbon, you must perform the following steps:  
  
1.  [Export the ribbon](export-prepare-edit-import-ribbon.md#BKMK_ExportTheRibbon)  
  
2.  [Prepare to edit the XML](export-prepare-edit-import-ribbon.md#BKMK_PrepareToEditTheXML)  
  
3.  Edit the `<RibbonDiffXml>`  
  
4.  [Import the ribbon](export-prepare-edit-import-ribbon.md#BKMK_ImportTheRibbon)  
  
<a name="BKMK_ExportTheRibbon"></a>   
## Export the ribbon  
 You export the ribbon by including it in a solution and then exporting the solution. You can export all the customizations, but that can represent a large amount of data. We recommend that you use an existing unmanaged solution or create a new solution.  
  
#### Create a new solution  
  
1. Go to **Settings > Customizations**.
1. Go to **Settings > Solutions**.
1. Click or tap **New**.  
1. Type a meaningful **Display Name**, **Unique Name** and enter a **Publisher** and type a **Version** number.  
  
   > [!NOTE]
   >  You can usually use the default publisher for the organization.  
  
6. Click the **Save** icon.  
  
7. If you want to edit the ribbon for specific entities:  
  
   1.  Click **Add Existing** and then click **Entity**.  
  
   2.  Select the entities you want to include in the Solution and then click **OK**.  
  
       > [!NOTE]
       >  For the purpose of editing entity ribbons, you do not have to include required components. If you intend to export this solution and apply it to another system, you should include required components.  
  
8. If you want to edit global ribbons or add a custom group to all entities, click **Add Existing** and then click **Application Ribbons**.  
  
9. Click **Save and Close**.  
  
#### Use an existing solution  
  
1. Go to **Settings > Customizations**.
1. Go to **Settings > Solutions**. 
1. Double-click a solution to open it.  
  
5. If you want to edit the ribbon for specific entities:  
  
   1.  Click **Add Existing** and then click **Entity**.  
  
   2.  Select the entities you want to include in the Solution and then click **OK**.  
  
       > [!NOTE]
       >  For the purpose of editing entity ribbons, you do not have to include required components. If you intend to export this solution and apply it to another system, you should include required components.  
  
6. If you want to edit global ribbons, such as to add custom button to all entities: click **Add Existing** and then click **Application Ribbons**.  
  
7. Click **Save and Close**.  
  
#### Export the ribbon  
  
1. Go to **Settings > Customizations**.
1. Go to **Settings > Solutions**.
  
4. Select the solution you want and then click **Export**.  
  
5. If you have made recent changes that have not yet been published, click **Publish All Customizations**. Otherwise, click **Next**.  
  
6. With the **Unmanaged** option selected, click **Export**.  
  
7. Click **Save** in the **File Download** dialog box and then click **Open Folder** in the **Download complete** dialog box.  
  
8. Right-click the compressed .zip file that you downloaded and select **Extract All...** .  
  
9. Select a location to extract the files and then click **Extract**.  
  
10. The customizations.xml file is the file that you will edit.  
  
<a name="BKMK_PrepareToEditTheXML"></a>   
## Prepare to edit the XML  
 For a better experience, edit the customizations.xml file with an application that can use schema validation to provide IntelliSense support. For more information, see [Edit the Customizations file with Schema Validation](edit-customizations-xml-file-schema-validation.md).  
  
<a name="BKMK_ImportTheRibbon"></a>   
## Import the ribbon  
  
1. After you have edited the customization.xml file, from Visual Studio or Visual Web Developer 2010 Express, right-click the customization.xml tab and select **Open Containing Folder**.  
  
2. Select all of the files or folders that were included when you extracted the solution. Right-click the selected files, select **Send To**, and then select **Compressed (zipped) folder**.  
  
   > [!NOTE]
   >  This creates a compressed .zip file in the same folder. The name of the file may vary, but it will be the same as one of the other files in the folder - except with a .zip file name extension.  
  
1. Go to **Settings > Customizations**.
1. Go to **Settings > Solutions**. 
  
6. Click **Import**.  
  
7. Click **Browse** and locate the compressed .zip file that you created in step 2 of this procedure.  
  
8. Click **Next** and then click **Import**.  
  
9. After the import has finished, you will see the message indicating that the import completed successfully. Click Close.  
  
10. After you have successfully imported your solution, you must publish customizations before you can see the changes. In the Solutions list, click **Publish All Customizations**.  
  
<a name="BKMK_DealWithErrorsOnImport"></a>   
### Dealing with errors on import  
  
1.  If you receive a notification that there were errors that caused the import to fail, click **Export Log**.  
  
2.  Save the export log file. Select the file and right-click it. Click **Open With** and then select **Microsoft Office Excel**.  
  
3.  Select the **Components** worksheet and note any messages in the **ErrorText** column.  
  
    > [!TIP]
    >  The most common type of failure is an error when referencing a dependent element in the RibbonDiffXml. Perhaps you forgot to include a LocLabel that was referenced somewhere. Perhaps there is an extra blank character included at the end of an XML attribute referencing another element. All references must match exactly.  
  
4.  After you have corrected the error, complete the steps to import the Ribbon again.  
  
### See also  
 [Customize the Ribbon](customize-commands-ribbon.md)   
 [Export Ribbon Definitions](export-ribbon-definitions.md)   
 [Use Localized Labels with Ribbons](use-localized-labels-ribbons.md)
