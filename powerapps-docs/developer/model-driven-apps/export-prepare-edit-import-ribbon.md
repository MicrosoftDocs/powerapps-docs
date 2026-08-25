---
title: Export, Edit, and Import the Ribbon in Model-Driven Apps
description: Export the ribbon in model-driven apps by adding it to a solution, edit the customizations.xml file, then import and publish. Follow the step-by-step guide.
author: clromano
ms.author: clromano
ms.date: 08/24/2026
ms.reviewer: jdaly
ms.topic: article
search.audienceType: 
  - developer
contributors: 
  - JimDaly
  - caburk
---
# Export, prepare to edit, and import the ribbon

[!INCLUDE [cc-modern-commanding](../data-platform/includes/cc-modern-commanding.md)]

This article explains how to edit the ribbon in model-driven apps by exporting a solution, preparing and modifying its XML, and then importing and publishing the customizations. Follow this process to apply ribbon changes successfully:  
  
1. [Export the ribbon](export-prepare-edit-import-ribbon.md#BKMK_ExportTheRibbon)  
1. [Prepare to edit the XML](export-prepare-edit-import-ribbon.md#BKMK_PrepareToEditTheXML)  
1. Edit the `<RibbonDiffXml>`  
1. [Import the ribbon](export-prepare-edit-import-ribbon.md#BKMK_ImportTheRibbon)  
  
<a name="BKMK_ExportTheRibbon"></a>

## Export the ribbon  

You export the ribbon by including it in a solution and then exporting the solution. You can export all the customizations, but that option can represent a large amount of data. Use an existing unmanaged solution or create a new solution.  


### Create a new solution or edit an existing solution

Follow the instructions in [Create a solution](../../maker/data-platform/create-solution.md), or sign in to [Power Apps](https://make.powerapps.com/?utm_source=padocs&utm_medium=linkinadoc&utm_campaign=referralsfromdoc) and select **Solutions** from the left navigation. Select the unmanaged solution you want to edit.

If you want to edit the ribbon for specific tables, add those tables to the solution. For the purpose of editing table ribbons, you don't need to include required components. If you intend to export this solution and apply it to another system, include required components.

If you want to edit global ribbons or add a custom group to all tables, select **Add Existing** and then select **Application Ribbons**.
  

### Export the ribbon  

1. Follow the instructions in [Export a solution](../../maker/data-platform/export-solutions.md#export-from-power-apps) to download an unmanaged solution.
1. Right-click the compressed .zip file that you downloaded and select **Extract All...** .  
1. Select a location to extract the files and then select **Extract**.  
1. Edit the `customizations.xml` file.  
  
<a name="BKMK_PrepareToEditTheXML"></a>   

## Prepare to edit the XML

For a better experience, edit the customizations.xml file with an application that uses schema validation to provide IntelliSense support. For more information, see [Edit the customizations file with schema validation](edit-customizations-xml-file-schema-validation.md).  
  
<a name="BKMK_ImportTheRibbon"></a>

## Import the ribbon  
  
1. After you edit the `customization.xml` file, select the folder that contains the file. 
1. Select all of the files or folders that were included when you extracted the solution. Right-click the selected files, select **Compress to...**, and then select **ZIP File**.  
  
   > [!NOTE]
   >  This step creates a compressed .zip file in the same folder. The name of the file might vary, but it's the same as one of the other files in the folder - except it has a .zip file name extension.  

1. Follow the instructions in [Import a solution](../../maker/data-platform/import-update-export-solutions.md).
1. After you successfully import your solution, you must publish customizations before you can see the changes. In the solutions list menu, select **Publish all customizations**.  
  
<a name="BKMK_DealWithErrorsOnImport"></a>   

### Resolve ribbon import errors  
  
1. If you receive a notification that errors caused the import to fail, select **Export Log**.  
1. Save the export log file. Select the file and right-click it. Select **Open With** and then choose **Microsoft Office Excel**.  
1. Select the **Components** worksheet and note any messages in the **ErrorText** column.  
  
    > [!TIP]
    > The most common type of failure is an error when referencing a dependent element in the RibbonDiffXml. You might have forgotten to include a `LocLabel` that was referenced somewhere. There might be an extra blank character at the end of an XML parameter referencing another element. All references must match exactly.  
  
1. After you correct the error, complete the steps to import the ribbon again.  

## Troubleshoot ribbon issues

If you're experiencing an issue with a ribbon command bar button, use the following articles in the troubleshooting guide to find and solve the problem.

- [Troubleshooting ribbon issues in Power Apps](/troubleshoot/power-platform/power-apps/create-and-use-apps/ribbon-issues)
- [A button on the command bar is hidden when it should be visible in Power Apps](/troubleshoot/power-platform/power-apps/create-and-use-apps/ribbon-issues-button-hidden?tabs=delete)
- [A button on the command bar is visible when it should be hidden](/troubleshoot/power-platform/power-apps/create-and-use-apps/ribbon-issues-button-visible?tabs=delete)
- [A button on the command bar isn't working correctly in Power Apps](/troubleshoot/power-platform/power-apps/create-and-use-apps/ribbon-issues-button-not-working-correctly?tabs=nothing)
- [A button on the command bar has wrong labels or translations](/troubleshoot/power-platform/power-apps/create-and-use-apps/ribbon-issues-button-wrong-label)
- [Noncustomizable buttons in ribbon](/troubleshoot/power-platform/power-apps/create-and-use-apps/ribbon-non-customizable-buttons)
- [Remove an active unmanaged layer of the ribbon in Power Apps](/troubleshoot/power-platform/power-apps/create-and-use-apps/remove-an-unmanaged-layer-for-ribbon)
- [How to regenerate ribbon metadata](/troubleshoot/power-platform/power-apps/create-and-use-apps/regenerate-ribbon-metadata)


### See also  

[Customize the ribbon](customize-commands-ribbon.md)   
[Export ribbon definitions](export-ribbon-definitions.md)   
[Use localized labels with ribbons](use-localized-labels-ribbons.md)


[!INCLUDE[footer-include](../../includes/footer-banner.md)]
