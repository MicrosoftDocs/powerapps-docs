---
title: Import or export data from the Common Data Service for Apps
description: Using the Get-Data from Excel and Export Data functionality to bulk-import and export data from Excel or CSV files into entities in Common Data Service (CDS) for Apps
author: sabinn-msft

ms.service: powerapps
ms.topic: conceptual
ms.component: cds
ms.date: 05/14/2018
ms.author: sabinn
---
# Import or export data from the Common Data Service for Apps

If you want the ability to bulk-import and export data from Excel or CSV files, you can use the Get Data from Excel file and Export Data features for updated Common Data Service (CDS) for Apps environments.

There are two ways you can import file into entity from Excel or csv file

## Option 1: Import by creating and modifying a file template

Every entity has required fields that must exist in your input file. For a more seamless approach, we recommend that you create a template by first exporting data from entity and using the same file (modified with your data) to import data into the entity. This will save you time and effort from having to account for the required fields for each entity.

1. Prepare the file template

    - Start by exporting the entity data to csv file by following the steps outlined under Export data to CSV
    - Define a plan to ensure uniqueness of data by either using Primary Keys or Alternate Keys.
    - Please refer to section below on how to ensure uniqueness prior to importing data into entity

1. Modify the file with your data

    - Copy data from your Excel or CSV file into the template that you just created

1. Import the file
    - On [powerapps.com](https://web.powerapps.com/), expand the **Data** section and click or tap **Entities** in the left navigation pane
    - Select the entity that you want to import data into
    - Click on the ellipsis or menu at the top and select **Get Data** and click or tap on **Get data from Excel**

> [!NOTE]
> For importing data into more than one entity, in the menu at the top, select **Get Data** and click or tap **Get data from Excel**. You should be able to choose multiple entities and hit **Next**

![Example of importing data to Account entity](./media/data-platform-import-export/import-data-to-account.png)

- This gets you to the **Import data** screen where you can choose to import data via an Excel or CSV file
- Click or tap on **Upload**
- Choose your file and follow the prompts to start uploading your file

![Example of uploading file to Account entity](./media/data-platform-import-export/upload-account.png)

- Once the file is uploaded and Mapping Status is green, click **Import** in the top right corner. If you encounter errors during mapping, please refere to section below to navigate and fix the mapping errors

![Example of successful Mapping status and Import button](./media/data-platform-import-export/success-map-imp.png)

- Once **Import completed successfully**, it will show you the total inserts and updates

![Example of successful import showing number of inserts and updates](./media/data-platform-import-export/success-imp-insert.png)

> [!NOTE]
> We use the Upsert (Update or Insert) logic to either update the record if it already exists, or insert a new record.

## Option 2: Import by bringing your own source file

If you are an advanced user and well versed with the required fields for a given entity for Common Data service for Apps entity, you can define your own Excel or CSV source file and follow the steps documented under **Import the file**

## Navigating Mapping errors

If you encounter mapping errors, after uploading your file, click on **Map status* , use the following steps to inspect and rectify the field mapping errors.

- Use the drop down on the right, under **Show** to walk through the **Unmapped fields** or **Fields with error** or **Required Fields**

> [!TIP]
> Depending on whether you get a Warning or Error, start with inspecting **Unmapped fields** or **Fields with error** through the drop-down experience in **Field Mappings**

![Example of a partial match due to warnings with field mappings](./media/data-platform-import-export/partial-match.png)

![Example of navigating field mapping issues](./media/data-platform-import-export/navigate-mappings.png)

![ Example of inspecting and rectifying warnings with field mappings](./media/data-platform-import-export/inspect-warnings.png)

- Once you have rectified all the errors and/or warnings, click on **Save Changes** in the top right corner which should take you back to the **Import Data** screen
- Once **Mapping Status** column indicates **Completed** in green, click *Import* in the top right corner
- Once you get the **Import completed successfully** message, it will show you the total inserts and updates

## Ensuring uniqueness while importing data into entity from Excel or CSV

Common Data Service for Apps entities use a Primary Key to uniquely identify records within a CDS entity table. The Primary Key for a CDS entity is a Globally Unique Identifier (GUID) and form the default basis for record identification. Data operations such as importing data into CDS entity will surface the default primary keys.

Example:
The Primary Key for Account entity is accountid

![Sample export file from Account entity showing accountid as Primary Key](./media/data-platform-import-export/export-pk.png)

Sometimes, a Primary Key may not suffice and/or meet the need while integrating data from an external source. For this purpose, CDS lets you define alternate keys to uniquely identify a record in place of the primary key.

Example:
For Account entity, you could set ‘transactioncurrencyid’ as an alternate key by using a natural key based identification (e.g. use ‘US Dollar’ instead of a GUID value *88c6c893-5b45-e811-a953-000d3a33bcb9* shown above). You can also choose currency symbol or currency name as keys.

![Example of creating alternate key on Currency entity](./media/data-platform-import-export/create-ak.png)

![Sample export file from Account entity showing currency Name as natural key](./media/data-platform-import-export/export-nk.png)

User can still use primary keys as identifier after specifying alternate keys. So, in the above sample first file is still valid provided GUIDs are valid data.

# Export data to CSV

You can do a one-time data export from a standard entity or custom entity, and you can export data from more than one entity at a time. If you export data from more than one entity, each entity is exported into its own Microsoft csv file.

1. On [powerapps.com](https://web.powerapps.com/), expand the **Data** section and click or tap **Entities** in the left navigation pane
1. Select the entity that you want to export data from
1. Click on the ellipsis or menu at the top and select **Export** and click or tap on **Data*

![Example of exporting data from Account entity](./media/data-platform-import-export/export-account.png)

[!Note]
For exporting data from multiple entities, in the menu at the top, select **Export** and click or tap on **Data*. You should be able to choose multiple entities

1. Once export completes successfully, you should be able to **Download exported data** which should you give you a link to the downloadable CSV file

![Sample export showing successful export with link downloadable file](./media/data-platform-import-export/export-success.png)

# Unsupported Data Types

Following data types are currently not supported

- Timezone
- Multi-select option set
- Image
