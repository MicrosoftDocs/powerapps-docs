---
title: "Access Dataverse choices with Azure SQL Database serverless | MicrosoftDocs"
description: "Learn how to access Dataverse choice data with Azure SQL Database serverless."
ms.custom: ""
ms.date: 08/06/2021
ms.reviewer: "Mattp123"
ms.service: powerapps
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "conceptual"
applies_to: 
  - "powerapps"
author: "sama-zaki"
ms.assetid: 
ms.subservice: dataverse-maker
ms.author: "matp"
manager: "kvivek"
search.audienceType: 
  - maker
search.app: 
  - PowerApps
  - D365CE
contributors: ""
---

# Access Dataverse choices (option sets) with Azure SQL Database serverless

[!INCLUDE[cc-data-platform-banner](../../includes/cc-data-platform-banner.md)]

For columns that use Microsoft Dataverse [Choices](/powerapps/maker/data-platform/create-edit-global-option-sets), choice values are written as an integer label and not a text label to maintain consistency during edits. The integer-to-text label mapping is stored in the *Microsoft.Athena.TrickleFeedService/table-EntityMetadata.json* file. This article covers how to access the integer-to-text label mapping using Azure SQL Database serverless.

![Access option set.](media/access-option-set.png "Access option set")

> [!NOTE]
>
> - Azure Synapse Link for Microsoft Dataverse was formerly known as Export to data lake. The service was renamed effective May 2021 and will continue to export data to Azure Data Lake as well as Azure Synapse Analytics.
> - This feature is still in preview and preview features are are not complete, but are made available on a “preview” basis so customers can get early access and provide feedback. Preview features may have limited or restricted functionality, are not meant for production use, and may be available only in selected geographic areas.

## Prerequisites

This section describes the prerequisites necessary to consume Dataverse data with Azure SQL Database serverless after using the Azure Synapse Link for Dataverse service.

- **Azure Synapse Link for Dataverse:** This guide assumes that you have already exported data from Dataverse by using the [Azure Synapse Link for Dataverse](export-to-data-lake.md) with and Azure Synapse Analytics workspace.

- **Storage Account Access.** You must be granted one of the following roles for the storage account: Storage Blob Data Reader, Storage Blob Data Contributor, or Storage Blob Data Owner.

## Consuming Dataverse choices with Azure SQL Database serverless

1. Navigate to your Azure Synapse Analytics workspace.

2. Select **Develop** from the left side panel, then select **+** > **SQL script**.

3. Paste the following SQL query and replace **\<STORAGE_ACCOUNT\>** with the storage account name and **\<CONTAINER_NAME\>** with the name of the container.

```SQL
    SELECT [EntityName], [OptionSetName], [Option], [IsUserLocalizedLabel], [LocalizedLabelLanguageCode], [LocalizedLabel]
    FROM OPENROWSET (
        BULK 'https://<STORAGE_ACCOUNT>.dfs.core.windows.net/<CONTAINER_NAME>/Microsoft.Athena.TrickleFeedService/*-EntityMetadata.json', 
        FORMAT = 'csv',
        FIELDTERMINATOR ='0x0b',
        FIELDQUOTE = '0x0b',
        ROWTERMINATOR = '0x0b'
    ) WITH (doc nvarchar(max)) AS rows
    CROSS APPLY OPENJSON(doc, '$.OptionSetMetadata')
    WITH (
            [EntityName] nvarchar(4000) '$.EntityName',
            [OptionSetName] nvarchar(4000) '$.OptionSetName',
            [Option] int '$.Option',
            [IsUserLocalizedLabel] nvarchar(4000) '$.IsUserLocalizedLabel',
            [LocalizedLabelLanguageCode] int '$.LocalizedLabelLanguageCode',
            [LocalizedLabel] nvarchar(4000) '$.LocalizedLabel'
    )
```

4. **Run** the query. A table containing the Dataverse choices is displayed.

5. Join the Dataverse choices with your Dataverse table and store the view in a new database using a three-part naming convention - *[database-name].[schema-name].[table-name]*.

### See also

[Azure Synapse Link for Dataverse](./export-to-data-lake.md)

[Azure SQL Database serverless](/azure/azure-sql/database/serverless-tier-overview)

[!INCLUDE[footer-include](../../includes/footer-banner.md)]
