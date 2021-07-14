---
title: "Import data in model-driven apps| MicrosoftDocs"
description: How to import data
ms.custom: ""
author: mduelae
manager: kvivek
ms.service: powerapps
ms.component: pa-user
ms.topic: conceptual
ms.date: 03/12/2021
ms.subservice: end-user
ms.author: mkaur
ms.reviewer: ""
ms.assetid: 
search.audienceType: 
  - enduser
search.app: 
  - PowerApps
  - D365CE
---
# How to import data

Import data that's stored somewhere else into your model-drvien app using the import feature in Power Apps. 

Every table has required columns that must exist in your input file. It's recommended that you download an Excel template, add your data, and then import the file to your app. The template saves time and effort. Don't add or modify columns in the template to avoid issues during the import.

Before you import a file make sure the column headings match the table names in your app. During the import process, the system will try to map the table names from your input file to the table names in the app. If they don't match, then you'll have to manually map the fields or you may run into issues during the import process.

If you're an advanced user and know the required columns for a given Dataverse table, define your own Excel, CSV, or XML source file and then follow the steps in this article on how to [import data](import-data.md#import-your-data) to your app. These file formats are supported:

 - Excel workbook (.xlsx)
 - Comma-separated values (.csv)
 - XML Spreadsheet 2003 (.xml)
 
The maximum file size allowed for .zip files is 32 MB. For the other file formats, the maximum file size allowed is 8 MB.   

## Download an Excel template

To avoid mapping issue, it's recommended that you use an Excel template that you can download from your app. Once the template is downloaded add your data and then import the file back to your app. Remember don't add or modify columns in the template to avoid issues during the import process.

1. Open your app and from the left nav select a table.

2. On the command bar, select **Excel Templates** > **Download Template**.

3. Select the table type and view that to download or select **Edit Columns** and choose the rows to include in the template.

5. Select **Download**. 
 
   > [!div class="mx-imgBorder"]
   > ![How to download an Excel template from your app.](media/download-excel-template.gif "How to download an Excel template from your ap")

## Import your data

Use the template that you downloaded in the previous step (modified with your data) and import the file to your app. 

1. Open an app and from the left nav select a table.
 
   > [!div class="mx-imgBorder"]
   > ![From the site map select a table.](media/left-nav-select-table.png "From the site pay select a table")

3. On the command bar, select the file type to import from:

   - **Import from Excel**: Select **Import from Excel** if you're using an Excel template.
   - **Import from CSV**
   - **Import from XML**

   > [!div class="mx-imgBorder"]
   > ![Shows the three import options in Power Apps.](media/import-files.gif "Shows the three import options in Power Apps")
  
2. Select **Choose File** and browse to the folder where the file is saved. Select the file, select **Open**, and then select **Next**.  
  
   > [!TIP]
   > You can only import one file at a time. To bring in more files, run the wizard again.
   
3. Select whether to **Allow Duplicates** or not. More information, see [Set up duplicate detection rules to keep your data clean](/power-platform/admin/set-up-duplicate-detection-rules-keep-data-clean).

4. For CSV and XML files (skip this step if you're importing an Excel file): 

   - For a CSV file: Select the drop-down list and select the data delimiter and field delimiter that's used the CSV file.
   
   - For CSV or XML file: If you have an alternate key defined, select it from the alternate Key drop-down list. The alternate key is used to uniquely identify and update rows during import. More information: [Define alternate keys to reference rows](../maker/data-platform/define-alternate-keys-reference-records.md).

     > [!div class="mx-imgBorder"]
     > ![Select the alternate key.](media/import-xml-alternate-key.png "Select the alternate key") 
   
5. Select **[Review Mapping](import-data.md#review-mapping)** and verify the columns (fields) are mapped correctly. If everything looks good, select **Finish Import**.  

   > [!div class="mx-imgBorder"]
   > ![Import selected Excel file and checking mapping.](media/mapping-excel-file.png "Import selected Excel file and checking mapping")

4. Select **Track Progress** see the progress of the import.

   > [!div class="mx-imgBorder"]
   > ![Track the progress of the file that you're importing.](media/track-progress.png "Track import file progress")
   
## Review mapping

When you import a file, it's important to review the column headings and verify that they match the columns (fields) in your app.

> [!div class="mx-imgBorder"]
> ![Review mapping.](media/review-mapping-legend.png "Review mapping")


Legend:

1. **Primary Fields**: Shows all the required columns for the table that must be mapped for the data to be imported successfully. If the column headings of your source file match the column display names, these columns will be automatically mapped. 

2. **Mapped columns**: Correctly mapped columns will be shown with a green check mark.

3. **Optional Fields**: These are optional column headings in your source file. If the column headings match the column display names, the columns will be automatically selected in the corresponding drop-down lists. 

4. **Unmatched columns**: If the column headings don't match, the unmapped columns will be shown with a red exclamation point. To map the column correctly, select a column to map to the unmapped column heading of your file. 

5. **Ignore** (For **Optional Fields** only): Choose **Ignore** from the drop-down list. Data from ignored columns won't be imported into your app.

### Option set

If any column in your source file includes a fixed set of values, you must map the column to a column of type **Option Set**. A column of this type has values such as **Yes** and **No** or  **Low** and **High**.

To do this, select the ![The Option Set button.](media/import-option-set-button.png "The Option Set button") button next to the option set column, select the values, and then select **OK**. 


   > [!div class="mx-imgBorder"]
   > ![The option-set value mapping menu.](media/import-files-option-set.gif "The option-set value mapping menu")

The option values drop-down list combines the values available in the incoming file with those already in your app. For example:

- **Values in import file**: Low, High
- **Values already in your app**: Cold, Warm, Hot
- **Resulting target values**: Cold, Warm, Hot, Low, High
 
After import, the import wizard will add all mapped values in your app, but will drop unmapped values from the import file that aren't yet in your app. For example, you could map the "Low" source value to the "Cold" target value, but map the "High" source value to the (new) "High" target value. Based on these mappings, the import wizard creates "High" as a target value in your app. It does not create "Low" as a target value in your app because you didn't map any source to this target value.

>[!NOTE]
>You can also map a column in your source file to a column of type "Two Options" and "Multiselect Option Set" (where a column can have multiple values). You must map each **Source Option Values** to the items in the **Dynamics 365 Option Values** list. When mapping to a column of type "Multiselect Option Set," if your source file includes values that aren't available in your app, new values won't be created in your app.

If some data in your source file references other existing rows in your app, you must map the column in the source file to a lookup column in your app.

For example, you might want to import a file named Leads.csv, which contains customer rows. The **Customer** column in Leads.csv contains the associated account or contact data. To map this, select the **Lookup Reference** button next to the lookup column. The **Lookup Reference** section opens and lists the tables related to the current table.

> [!div class="mx-imgBorder"]
> ![The Lookup Reference section.](media/import-lookup-reference-section.png "The Lookup Reference section")

For each table, select the columns to search during import to retain the relationships between the rows, and then select **OK**.

### Save mapping settings

To save the mapping settings for next time, enter a name in the **Name your data map** box. This way, the next time you import a similar set of data, you'll be able to use the same mapping.

> [!div class="mx-imgBorder"]
> ![Name your data map here.](media/import-save-settings.png "Name your data map here")


### See also
[Download a template for data import](/power-platform/admin/download-template-data-import)



[!INCLUDE[footer-include](../includes/footer-banner.md)]
