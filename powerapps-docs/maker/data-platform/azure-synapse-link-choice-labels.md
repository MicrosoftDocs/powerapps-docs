---
title: "Access Dataverse choice labels directly from Azure Synapse Link for Dataverse | MicrosoftDocs"
description: "Learn how to Access Dataverse choice labels directly from Azure Synapse Link for Dataverse  with Power Apps"
ms.custom: ""
ms.date: 04/27/2022
ms.reviewer: "matp"
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "how-to"
applies_to: 
  - "powerapps"
author: "JasonHQX"
ms.assetid: 
ms.subservice: dataverse-maker
ms.author: "jasonhuang"
search.audienceType: 
  - maker
---
# Access choice labels directly from Azure Synapse Link for Dataverse

Microsoft Dataverse provides rich metadata that can be used directly within Power Apps. A choice (picklist) is one of the most used types of columns that can be included in a table. It defines a set of options. When a choice is displayed in a form, it uses a drop-down list control. You can define a choice to use a set of options defined within itself (locally) or it can use a set of options defined elsewhere (globally), which can be used by other choice columns.  

For more information about choice columns, go to [Create and edit global choices overview](create-edit-global-option-sets.md).

After creating an Azure Synapse Link, the following five tables are created in a folder named **OptionsetMetadata** in Azure Data Lake Storage Gen2:
- OptionsetMetadata
- GlobalOptionsetMetadata
- StateMetadata
- StatusMetadata
- TargetMetadata

:::image type="content" source="media/azure-synapse-link-choice-tables.png" alt-text="Tables created in Azure Synapse Analytics with choice columns":::

**StateMetadata** and **StatusMetadata** store the **State** and **Status** choice value to retrieve. **TargetMetadata** stores table relationships metadata to retrieve.

|Column name  |Data type  |Sample value  |Description  |
|---------|---------|---------|---------|
|EntityName   |String     |account      |Current Dataverse table name.    |
|AttributeName     |String     | transactioncurrencyid     | Current column name     |
|ReferencedEntity  | String     |  transactioncurrency   | Related Dataverse table name    |
|ReferencedAttribute    | String     | transactioncurrencyid    | Related column name      |

More information: [Table relationships overview](relationships-overview.md).

**OptionsetMetadata** stores the local choices label metadata in the imported Dataverse tables. **GlobalOptionsetMetadata** stores the global choices label metadata and follows the same table schema plus one extra column, **GlobalOptionSetName**, a combination of table and choice name.

|Column name  |Data type  |Sample value  |Description  |
|---------|---------|---------|---------|
|EntityName    | String    | account     | Dataverse table name.    |
|OptionSetName       | String     |ownershipcode      | Column name.   |
|Option  | Bigint      | 1      |  User-specified numerical label when the choice item is created.     |
|IsUserLocalizedLabel   | Boolean    | False     | Return False by default.    |
|LocalizedLabelLanguageCode   | Bigint     |1033     |  The language code of the choice label, such as 1033 for English (United States) or 1034 for Spanish (Spain).    |
|LocalizedLabel     | String    | Public     | User-specified text label when the choice item is created.          |
|GlobalOptionSetName (GlobalOptionsetMetadata only)   | String    | socialprofile_community    | a combination of table and choice name         |

:::image type="content" source="media/azure-synapse-link-table-schema.png" alt-text="OptionsetMetadata and GlobalOptionsetMetadata table schema.":::

In the Dataverse tables, the choice column contains a user-specified numerical value, which is the same as **Option** value in **OptionsetMetadata** table described above.

## Prerequisite

Azure Synapse Link for Dataverse. This article assumes that you have already exported data from Dataverse by using [Azure Synapse Link for Dataverse](export-to-data-lake.md).  

## Access choice metadata

1. Select the desired Azure Synapse Link and select the **Go to Azure Synapse Analytics workspace** on the command bar.   
1. Expand **Lake Databases** on the left pane, select **dataverse**-*environmentName*-*organizationUniqueName*, and then expand **Tables**.  
   All the choice metadata listed is available for analysis.

To consume Dataverse choice columns with serverless SQL pool.

1. Right-click the database icon, then select **New SQL script** > **Empty script**.
1. Apply a join SQL script to join the choice metadata with your Dataverse table and store the view in a new database.

### Example SQL script to join choice metadata
Replace **\<DATABASE_NAME\>**,**<COLUMN_NAME>** and **<TABLE_NAME>** with the name of the database, column and table to replace numerical choice value to meaningful text label

```sql
SELECT [LocalizedLabel] as [<COLUMN_NAME>] 
FROM [<DATABASE_NAME>].[dbo].[<TABLE_NAME>_partitioned] 
LEFT JOIN [<DATABASE_NAME>].[dbo].[OptionsetMetadata] 
ON ([<DATABASE_NAME>].[dbo].[OptionsetMetadata].[Option] = [<DATABASE_NAME>].[dbo].[<TABLE_NAME>_partitioned].[<COLUMN_NAME>] AND [<DATABASE_NAME>].[dbo].[OptionsetMetadata].[OptionSetName] = <COLUMN_NAME>)
```

For more information about how to consume multiple option set values, you would have to use [Using Common Table Expressions](/previous-versions/sql/sql-server-2008-r2/ms190766(v=sql.105)?redirectedfrom=MSDN).
