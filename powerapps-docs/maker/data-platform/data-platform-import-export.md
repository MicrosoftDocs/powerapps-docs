---
title: Import or export data from Microsoft Dataverse
description: Bulk import and export data from Excel or CSV files into tables in Microsoft Dataverse by using the Get Data from Excel and Export Data functionality
author: sabinn-msft
ms.topic: how-to
ms.component: cds
ms.date: 07/25/2023
ms.subservice: dataverse-maker
ms.author: sabinn
search.audienceType: 
  - maker
---
# Import or export data from Dataverse

To get (import) data into Microsoft Dataverse tables, use an Excel worksheet file, a comma-separated values (CSV) file, or one of the many connectors available.

When you export Dataverse table data, it's exported as a CSV file.

## Import using a connector

Use a connector to import data from a selection of many different sources, such as Microsoft Excel, Azure, SQL Server database, SharePoint, Access, OData, and more.

1. Sign into [Power Apps](https://make.powerapps.com/?utm_source=padocs&utm_medium=linkinadoc&utm_campaign=referralsfromdoc).
1. On the left navigation pane select **Tables**. [!INCLUDE [left-navigation-pane](../../includes/left-navigation-pane.md)]
1. Select **Data** > **Get data** > **Get data**.
1. From the **Data sources** list, select the connector that you want to import data from.

For information about the connector you want to use as your data source, see [List of all Power Apps connectors](/connectors/connector-reference/connector-reference-powerapps-connectors) and [List of all connectors published by Microsoft](/connectors/connector-reference/connector-reference-microsoft-connectors).

## Import from an Excel or CSV file

There are two ways to import data from Excel.
- [Option 1: Import by creating and modifying a file template](#option-1-import-by-creating-and-modifying-a-file-template)
- [Option 2: Import by bringing your own source file](#option-2-import-by-bringing-your-own-source-file)

### Option 1: Import by creating and modifying a file template

Every table has required columns that must exist in your input file. We recommend that you create a template. To do this, export data from the table. Then, use the same file and modify it with your data. Finally, import the modified file back into the table. Using a template can save you time because you won't have to specify the required columns for each table.

#### Prepare the file template

1. [Export the table data](#export-data).
1. Define a plan to make sure data is unique before you import it. Use either primary keys or alternate keys. More information: [Ensure uniqueness when you import data into a table from Excel or CSV](#ensure-uniqueness-when-you-import-data-into-a-table-from-excel-or-csv)

#### Modify the file with your data

Copy data from your Excel or CSV file into the template that you created in the previous step.

#### Import the file

1. On [powerapps.com](https://make.powerapps.com/) select **Tables** in the left navigation pane. [!INCLUDE [left-navigation-pane](../../includes/left-navigation-pane.md)]
1. Select **Data**, to the right of **Get Data** select **>**, and then select **Get data from Excel**.
1. Select the tables where you want to import data, and then select **Next**.
1. On the **Import data** page, select **Upload**, and choose your file. Follow the prompts to upload your file.
1. After the file is uploaded and **Mapping status** indicates **Mapping was successful**, select **Import** from the top-right corner. Go to [Troubleshoot mapping errors with Excel](#troubleshoot-mapping-errors-with-excel) to navigate and fix any mapping errors.
   :::image type="content" source="media/data-platform-import-export/import-mapping-successful.png" alt-text="Import mapping successful":::
  After the import finishes successfully, you'll see the total number of inserts and updates.  

### Option 2: Import by bringing your own source file

If you're an advanced user and know the required columns for a given table for Dataverse tables, define your own Excel or CSV source file. Follow the steps in [Import the file](#import-the-file).

### Troubleshoot mapping errors with Excel

If you get mapping errors after you upload your file, select **Map status**. Take the following steps to inspect and rectify the column mapping errors.

1. Use the drop-down menu on the right, under **Show**, to walk through the **Unmapped columns**, **Fields with error**, or **Required Fields**.

    > [!TIP]
    >
    > - Depending on whether you get a **Warning** or an **Error**, inspect **Unmapped columns** or **Fields with error** through the drop-down menu in **Column Mappings**.
    > - Use the *upsert* (**Update** or **Insert**) logic to either update the row, if it already exists, or to insert a new row.

1. After you resolve all the errors and warnings, select **Save Changes** in the top-right corner. You'll go back to the **Import Data** screen.
1. When the **Mapping status** column shows **Mapping was successful**, select **Import** from the top-right corner.

When the **Import completed successfully** message appears, the total inserts and updates are displayed.

### Ensure uniqueness when you import data into a table from Excel or CSV

Dataverse tables use a primary key to uniquely identify rows within a Dataverse table. The primary key for a Dataverse table is a globally unique identifier (GUID). It forms the default basis for row identification. Data operations, like importing data into Dataverse tables, surface the default primary keys.

Example:  
The primary key for an **Account** table is **accountid**.

> [!div class="mx-imgBorder"] 
> ![Sample export file from an **Account** table showing **accountid** as the primary key.](./media/data-platform-import-export/export-pk.png)

Sometimes, a primary key might not work when you integrate data from an external source. Use Dataverse to define alternate keys that uniquely identify a row in place of the primary key.

Example:  
For an **Account** table, you might set **transactioncurrencyid** as an alternate key by using a natural key-based identification. For example, use **US Dollar** instead of the GUID value **88c6c893-5b45-e811-a953-000d3a33bcb9** shown previously. You can also choose **currency symbol** or **currency name** as keys.  More information: [Define alternate keys using Power Apps portal](define-alternate-keys-portal.md)

> [!div class="mx-imgBorder"] 
> ![Example of creating an alternate key on a **Currency** table.](./media/data-platform-import-export/create-ak.png)

> [!div class="mx-imgBorder"] 
> ![Sample export file from an **Account** table showing **currency name** as a natural key.](./media/data-platform-import-export/export-nk.png)

You can still use primary keys as identifiers after you specify alternate keys. In the preceding sample, the first file is still valid if GUIDs are valid data.

## Export data

Export data from one or more tables. Exported data is in comma-separated value (CSV) format. When you export data from more than one table, each table is exported into its own CSV file.

1. Sign into [Power Apps](https://make.powerapps.com/?utm_source=padocs&utm_medium=linkinadoc&utm_campaign=referralsfromdoc), on the left navigation pane select **Tables**. [!INCLUDE [left-navigation-pane](../../includes/left-navigation-pane.md)]
1. Select **Export** > **Export data**.
1. Select the tables that you want to export data from, and then select **Export data**.

   > [!div class="mx-imgBorder"] 
   > ![Example of exporting data from an **Account** table.](./media/data-platform-import-export/export-account.png)

1. After the export finishes successfully, select **Download exported data** to download the CSV file to the download folder specified in your web browser.

   > [!div class="mx-imgBorder"] 
   > ![Sample export that shows successful export with link downloadable file.](./media/data-platform-import-export/export-success.png)

> [!NOTE]
> Exports have a 12 minute time limit. If the volumne of data exported exceeds 12 minutes the export will fail. If this occurs, export data in smaller segments.

## Unsupported data types and fields

The following data types aren't currently supported for import or export.

- Timezone
- Choices (multiselect)
- Image
- File

The following fields are system fields and are not supported for import and export.

- Ownerid
- Createdby
- Createdonbehalfby
- Createdon
- Modifiedby
- Modifiedonbehalfby
- Modifiedon
- Overriddencreatedon

 > [!NOTE]
 > Get Data from Excel and Export Data features are currently not included in the Power Apps Developer Plan.

## Troubleshoot connection issues

Users might receive an error message if the connection they are using for export requires a fix. In this case, the user receives an error message that states **Connection to Dataverse failed. Please check the link below on how to fix this issue**.

To fix this issue:

1. In Power Apps (make.powerapps.com), select **Connections** from the left navigation pane. [!INCLUDE [left-navigation-pane](../../includes/left-navigation-pane.md)]
2. Locate the **Microsoft Dataverse (legacy)** connection.
3. Select the **Fix connection** link in the **Status** column, and follow the instructions on your screen.

After the fix completes, retry the export.

[!INCLUDE[footer-include](../../includes/footer-banner.md)]
