---
title: "Read the incremental updates of Dataverse data | MicrosoftDocs"
description: "Learn how to read the incremental updates of your Dataverse data."
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

# Read the incremental updates of Dataverse data

[!INCLUDE[cc-data-platform-banner](../../includes/cc-data-platform-banner.md)]

After creating a continuous pipeline of data from Microsoft Dataverse to your Synapse workspace with Azure Synapse Link for Dataverse, you can read the incremental updates of a specified time interval. Every Dataverse table exported with Azure Synapse Link for Dataverse contains a *SinkModifiedOn* column which can be used to get the incremental updates.

> [!NOTE]
>
> - Azure Synapse Link for Microsoft Dataverse was formerly known as Export to data lake. The service was renamed effective May 2021 and will continue to export data to Azure Data Lake as well as Azure Synapse Analytics.

## Prerequisites

This section describes the prerequisites necessary to read the incremental updates of your exported Dataverse data.

- **Azure Synapse Link for Dataverse.** This guide assumes that you have already exported data from Dataverse by using the [Azure Synapse Link for Dataverse](export-to-data-lake.md).

- **Storage Account Access.** You must be granted one of the following roles for the storage account: Storage Blob Data Reader, Storage Blob Data Contributor, or Storage Blob Data Owner.

- **Synapse administrator.** You must be granted the **Synapse Administrator** role access within Synapse studio.

## Read the Incremental Updates of your Dataverse data

1. Navigate to you Azure Synapse Analytics workspace.

2. Select **Develop** from the left side panel, then select **+** > **SQL script**.

3. Paste the following SQL query and replace **CONTAINER_NAME** with the name of the container, **TABLE_NAME** with the name of the Dataverse table, and **TIMESTAMP_START** and **TIMESTAMP_END** with the time interval in UTC format (YYYY-MM-DDTHH:MM:SS).

   ```SQL
       SELECT * 
       FROM [CONTAINER_NAME].[dbo].[TABLE_NAME]
       WHERE [SinkModifiedOn] >= TIMESTAMP_START AND [SinkModifiedOn] <= TIMESTAMP_END
   ```

4. **Run** the query and a table containing the incremental updates to the Dataverse table from the specified time interval will be displayed.

### See also

[Azure Synapse Link for Dataverse](./export-to-data-lake.md)

[!INCLUDE[footer-include](../../includes/footer-banner.md)]
