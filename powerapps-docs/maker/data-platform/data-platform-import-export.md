---
title: Import or export data from Microsoft Dataverse
description: Bulk import and export data from Excel or CSV files into tables in Microsoft Dataverse by using the Get Data from Excel and Export Data functionality
author: sabinn-msft
ms.service: powerapps
ms.topic: how-to
ms.component: cds
ms.date: 08/27/2020
ms.author: sabinn
search.audienceType: 
  - maker
search.app: 
  - PowerApps
  - D365CE
---
# Import or export data from Microsoft Dataverse

[!INCLUDE[cc-data-platform-banner](../../includes/cc-data-platform-banner.md)]

To bulk import and export data from Microsoft Excel or CSV files, use the Get Data from Excel file and Export Data features for updated Dataverse environments.

There are two ways that you can import files into tables from Excel or CSV files.

## Option 1: Import by creating and modifying a file template

Every table has required columns that must exist in your input file. We recommend that you create a template. First, export data from the table. Use the same file (modified with your data) to import data into the table. This template saves time and effort. You won't have to account for the required columns for each table.

1. Prepare the file template.

    a. Export the table data to the CSV file. Follow the steps in **Export data to CSV**.  
    b. Define a plan to make sure data is unique. Use either **primary keys** or **Alternate Keys**.  
    c. Refer to the next section for instructions to make sure data is unique before you import it into a table. 

1. Modify the file with your data.

    - Copy data from your Excel or CSV file into the template that you just created.

1. Import the file.  
    a. On [powerapps.com](https://make.powerapps.com/), expand the **Data** section. Select **Tables** in the left navigation pane.  
    b. Select the table that you want to import data into.  
    c. Select the ellipsis or menu at the top. Select **Get Data**. Select **Get data from Excel**.  

    > [!NOTE]
    > To import data into more than one table, in the top menu, select **Get Data**. Select **Get data from Excel**. Then you can choose multiple tables and select **Next**.

    > [!div class="mx-imgBorder"] 
    > ![Example of importing data to an **Account** table](./media/data-platform-import-export/import-data-to-account.png)

    d. On the **Import data** screen, choose whether to import data from an Excel or a CSV file.  
    e. Select **Upload**.  
    f. Choose your file. Follow the prompts to upload your file.  

   <!-- > [!div class="mx-imgBorder"] 
    > ![Example of uploading a file to an **Account** table](./media/data-platform-import-export/upload-account.png)  -->

    g. After the file is uploaded and **Mapping status** is green, select **Import** in the top-right corner. Refer to the next section to navigate and fix any mapping errors.  

    h. After the import finishes successfully, you'll see the total number of inserts and updates.  

    > [!NOTE]
    > Use the Upsert (Update or Insert) logic to either update the row, if it already exists, or to insert a new row.

## Option 2: Import by bringing your own source file

If you're an advanced user and know the required columns for a given table for Dataverse tables, define your own Excel or CSV source file. Follow the steps in **Import the file**.

## Navigate mapping errors

If you get mapping errors after you upload your file, select **Map status**. Take the following steps to inspect and rectify the column mapping errors.

1. Use the drop-down menu on the right, under **Show**, to walk through the **Unmapped columns**, **Fields with error**, or **Required Fields**.

    > [!TIP]
    > Depending on whether you get a Warning or an Error, inspect **Unmapped columns** or **Fields with error** through the drop-down menu in **Column Mappings**.

  <!--  > [!div class="mx-imgBorder"] 
    > ![Example of a partial match due to warnings with column mappings](./media/data-platform-import-export/partial-match.png)

    > [!div class="mx-imgBorder"] 
    > ![Example of navigating column mapping issues](./media/data-platform-import-export/navigate-mappings.png)

    > [!div class="mx-imgBorder"] 
    > ![Example of inspecting and rectifying warnings with column mappings](./media/data-platform-import-export/inspect-warnings.png) -->

2. After you resolve all the errors and warnings, select **Save Changes** in the top-right corner. You'll go back to the **Import Data** screen.
3. When the **Mapping Status** column shows **Completed** in green, select **Import** in the top-right corner.
4. When you get the **Import completed successfully** message, it shows the total inserts and updates.

## Ensure uniqueness when you import data into a table from Excel or CSV

Dataverse tables use a primary key to uniquely identify rows within a Dataverse table table. The primary key for a Dataverse table is a globally unique identifier (GUID). It forms the default basis for row identification. Data operations, like importing data into Dataverse tables, surface the default primary keys.

Example:  
The primary key for an **Account** table is **accountid**.

   > [!div class="mx-imgBorder"] 
   > ![Sample export file from an **Account** table showing **accountid** as the primary key](./media/data-platform-import-export/export-pk.png)

Sometimes, a primary key might not work when you integrate data from an external source. Use Dataverse to define alternate keys that uniquely identify a row in place of the primary key.

Example:  
For an **Account** table, you might set **transactioncurrencyid** as an alternate key by using a natural key-based identification. For example, use **US Dollar** instead of the GUID value **88c6c893-5b45-e811-a953-000d3a33bcb9** shown previously. You can also choose **currency symbol** or **currency name** as keys.

   > [!div class="mx-imgBorder"] 
   > ![Example of creating an alternate key on a **Currency** table](./media/data-platform-import-export/create-ak.png)

   > [!div class="mx-imgBorder"] 
   > ![Sample export file from an **Account** table showing **currency name** as a natural key](./media/data-platform-import-export/export-nk.png)

Users can still use primary keys as identifiers after they specify alternate keys. In the preceding sample, the first file is still valid if GUIDs are valid data.

## Export data to CSV

You can do a one-time data export from a standard table or custom table. And you can export data from more than one table at a time. If you export data from more than one table, each table is exported into its own Microsoft CSV file.

1. On [powerapps.com](https://make.powerapps.com/), expand the **Data** section. Select **Tables** on the left navigation pane.
1. Select the table that you want to export data from.
1. Select the ellipsis or menu at the top. Select **Export data**.

    > [!div class="mx-imgBorder"] 
    > ![Example of exporting data from an **Account** table](./media/data-platform-import-export/export-account.png)

    > [!NOTE]
    > To export data from multiple tables, in the top menu, select **Export**. Select **Data**. You can choose multiple tables.

1. After the export finishes successfully, you can **Download exported data**. This download gives you a link to the downloadable CSV file.

  <!--  > [!div class="mx-imgBorder"] 
    > ![Sample export that shows successful export with link downloadable file](./media/data-platform-import-export/export-success.png) -->

## Unsupported data types

The following data types aren't currently supported.

- Timezone
- Multiselect choice 
- Image

    > [!NOTE]
    > Get Data from Excel and Export Data features are currently not included in the Power Apps Developer Plan.


[!INCLUDE[footer-include](../../includes/footer-banner.md)]