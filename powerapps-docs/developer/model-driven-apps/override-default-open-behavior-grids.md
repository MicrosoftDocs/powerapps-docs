---
title: "Override Default Open Behavior of Data Rows in Grids"
description: "Learn how to override the default open behavior of data rows in entity-bound grids with a custom JavaScript action. Follow the steps to customize grid behavior."
author: clromano
ms.author: clromano
ms.date: 08/24/2026
ms.reviewer: jdaly
ms.topic: how-to
ms.subservice: mda-developer
search.audienceType: 
  - developer
contributors: 
  - JimDaly
  - caburk
---

# Override the default open behavior of data rows in an entity-bound grid

[!INCLUDE [cc-modern-commanding](../data-platform/includes/cc-modern-commanding.md)]

Learn how to override the default open behavior of data rows in an entity-bound grid so that selecting a row runs a custom action, such as opening a URL. By default, any of the following actions opens the table record:

- Double-clicking the data row, or selecting the primary column link in the row.
- Selecting a data row, and then pressing the **Enter** key.
- On a touch-enabled device, selecting a data row.

[!INCLUDE[cc-terminology](../data-platform/includes/cc-terminology.md)]

There might be situations where you don't want the table record to open (which is the default behavior), but want a custom action to be performed such as opening a URL using JavaScript functions. You can override the default behavior and define your own custom behavior by creating a command definition for a table with `Mscrm.OpenRecordItem` as the value of the ID parameter `CommandDefinition`, and defining a custom action on the **Actions** tab. The application looks for the `Mscrm.OpenRecordItem` command ID for a table when you try to open a record from the entity-bound grid and&mdash;if one is present&mdash;will execute the custom action instead of performing the default behavior of opening the table record.

> [!NOTE]
> - This feature is supported only for Unified Interface.
> - You can also use Ribbon Workbench, a community tool, to visually edit ribbons by using the UI. Note that tools created by the community aren't supported by Microsoft. If you have questions or issues with community tools, contact the publisher of the tool.

To specify a custom action when a table record is selected, complete the following steps:

1. Create a web resource to perform the action.
1. Create a custom button on the form by editing the customization.xml file.
1. Import the customization.xml file.

## Step 1: Create a web resource

Create a web resource to change the default behavior. In the following example, if you want to open a URL instead of displaying the record, create a JavaScript web resource to perform that action.

### Create a new solution or edit an existing solution

1. Follow the instructions in [Create a solution](../../maker/data-platform/create-solution.md), or sign in to [Power Apps](https://make.powerapps.com/?utm_source=padocs&utm_medium=linkinadoc&utm_campaign=referralsfromdoc) and select **Solutions** from the left navigation. Select the unmanaged solution you want to edit.
1. Open the solution, and then select **Objects** in the left navigation. 
1. In the menu, select **+ New** > **More** > **Web resource**.
 
   :::image type="content" source="media/create-new-web-resources.png" alt-text="Screenshot of the menu option to create a JavaScript web resource.":::


1. Copy the following code, paste it into the **Code** field, and edit the value of the URL you want to open:

   ```JavaScript
   function ChangeBehavior(){
    
    // Enter the url
    var url =  "Enter the URL";
    var OpenUrlOptions = {height: 800, width: 1000};
    Xrm.Navigation.openUrl(url, openUrlOptions);
   }
   ```

1. Enter the **Name** of the web resource, and select the **File type** as **JavaScript (JS)**.
1. Save and publish the web resource.

## Step 2: Create a custom button

Create a custom button on the form where you want to change the default behavior. For example, if you have a subgrid on the accounts form that displays contact records in the subgrid, you need to create a button and add it to the contact form. You can create a button by editing the customization.xml file.

1. Open the solution that you created in step 1, and add the table where you want to create the button. You don't need to include all table components and metadata.
1. Select **Add existing** > **Table**.  
1. From the list, select **Contact**.
1. Save and publish the solution. 
1. Go to **Overview** and select **Export** to make edits to the customization.xml file. 

    :::image type="content" source="media/export-solution-from-command-bar.png" alt-text="Screenshot of the Export command for an unmanaged solution.":::

1. If you made recent changes that you didn't publish, select **Publish**, select **Run** to check whether the solution has any issues or dependencies, and then select **Next**.

    :::image type="content" source="media/publish-before-exporting-solution.png" alt-text="Screenshot of the options to publish the solution before export.":::

1. With the **Unmanaged** option selected, select **Run solution checker on export** and select **Export**.

   :::image type="content" source="media/export-as-unmanaged-solution.png" alt-text="Screenshot of the Unmanaged option selected for solution export.":::

1. When the solution is ready, select the **Download** button.

   :::image type="content" source="media/download-solution-file.png" alt-text="foo":::

1. In the **Downloads** dialog box, select **Open Folder**.
1. Right-click to select the compressed .zip file that you downloaded, and then select **Extract All...**.
1. Select a location to extract the files to, and then select **Extract**.

    The `customizations.xml` file is the file that you edit.

    > [!NOTE]
    > You can enable or disable the button; doing either still overrides the open default behavior.

1. Open the `customization.xml` file, copy the following code, and replace the code inside the `RibbonDiffXml`:

     ```XML
   <RibbonDiffXml>
     <CustomActions>
       <CustomAction Id="cr5c1.Mscrm.OpenRecordItem.CustomAction"
         Location="Mscrm.SubGrid.contact.MainTab.Management.Controls._children"
         Sequence="28">
         <CommandUIDefinition>
           <Button Alt="$LocLabels:Mscrm.OpenRecordItem.Alt"
             Command="Mscrm.OpenRecordItem"
             Id="Mscrm.OpenRecordItem"
             LabelText="$LocLabels:Mscrm.OpenRecordItem.LabelText"
             Sequence="28"
             TemplateAlias="o1"
             ToolTipTitle="$LocLabels:Mscrm.OpenRecordItem.ToolTipTitle"
             ToolTipDescription="$LocLabels:Mscrm.OpenRecordItem.ToolTipDescription" />
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
           <JavaScriptFunction FunctionName="ChangeBehavior"
             Library="$webresource:cr5c1_samplescript" />
         </Actions>
       </CommandDefinition>
     </CommandDefinitions>
   </RibbonDiffXml>
     ```

     > [!NOTE]
     > You need to replace the function name and the name of the web resource in the preceding XML file. Edit the preceding example XML file to replace it with your own default publisher.
     > 
     > This example changes the button for a subgrid on the accounts form that displays contact records in the subgrid. Therefore the `Location` is `Location="Mscrm.SubGrid.contact.MainTab.Management.Controls._children"`. You need to change this value to apply to a different button. 

## Step 3: Import the XML file

1. After you edit the `customization.xml` file, open the containing folder.
1. Select all the files or folders that were included when you extracted the solution. Right-click the selected files, select **Compress To...**, and then select **ZIP File**.  
  
   > [!NOTE]
   >  This step creates a compressed .zip file in the same folder. The name of the file varies, but it's the same as one of the other files in the folder except with a .zip file name extension.  
  
1. Sign in to [Power Apps](https://make.powerapps.com), and select **Solutions** from the left pane.  
1. On the command bar, select **Import solution**.  

    :::image type="content" source="media/import-solution-from-command-bar.png" alt-text="Screenshot of the Import command on the Solutions command bar."::: 
  
1. On the **Import a solution** page, select **Browse** to locate the compressed .zip file that contains the solution you want to import.
1. Select **Next**.  
1. On the page that displays information about the solution, select **Import**.  
1. Wait a few moments while the import completes. View the results, and then select **Close**.  
  
If you import any changes that require publishing, you must publish customizations before they're available. 
  
If the import isn't successful, you see a report that shows any errors or warnings that were captured. Select **Download Log File** to see details about what caused the import to fail. The most common cause for an import to fail is that the solution didn't contain some required components.  
  
When you download the log file, you get an XML file that you can open with Excel to view the contents.

## See also

[Ribbon Workbench](https://www.develop1.net/public/rwb/ribbonworkbench.aspx)<br/>
[Customize the ribbon](customize-commands-ribbon.md)


[!INCLUDE[footer-include](../../includes/footer-banner.md)]
