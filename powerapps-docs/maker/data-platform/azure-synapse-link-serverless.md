---
title: "Query Azure Synapse Link for Dataverse data with Serverless SQL | MicrosoftDocs"
description: "Learn how to query exported Dataverse table data with Serverless SQL"
ms.custom: ""
ms.date: 08/06/2021
ms.reviewer: "Mattp123"
ms.service: powerapps
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "how-to"
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

# Query Azure Synapse Link for Dataverse data with Serverless SQL

[!INCLUDE[cc-data-platform-banner](../../includes/cc-data-platform-banner.md)]

You can use the Azure Synapse Link to connect your Microsoft Dataverse data to Azure Synapse Analytics to explore your data and accelerate time to insight. This article shows you how to query your Dataverse data with built-in Serverless SQL pool in your Azure Synapse Analytics workspace.

> [!NOTE]
>
> - Azure Synapse Link for Microsoft Dataverse was formerly known as Export to data lake. The service was renamed effective May 2021 and will continue to export data to Azure Data Lake as well as Azure Synapse Analytics.
> - This feature is still in preview and preview features are are not complete, but are made available on a “preview” basis so customers can get early access and provide feedback. Preview features may have limited or restricted functionality, are not meant for production use, and may be available only in selected geographic areas.

## Prerequisites

This section describes the prerequisites necessary to query your Dataverse data after using the Azure Synapse Link for Dataverse service.

- **Azure Synapse Link for Dataverse:** This guide assumes that you have already exported data from Dataverse by using the [Azure Synapse Link for Dataverse](export-to-data-lake.md).

- **Storage Account Access.** You must be granted one of the following roles for the storage account: Storage Blob Data Reader, Storage Blob Data Contributor, or Storage Blob Data Owner.

- **Synapse administrator.** You must be granted the **Synapse Administrator** role access within Synapse studio.

## Query your Dataverse data with serverless SQL pool

> [!NOTE]
> Azure Synapse Link for Dataverse does not support the use of dedicated SQL pools at this time.

1. In Power Apps, select your desired Azure Synapse Link from the list, and then select **Go to Azure Synapse workspace**.

    ![Go to workspace.](media/go-to-workspace.png "Go to workspace")

2. Expand **Databases**, select your Dataverse container. Your exported tables are displayed under the **Tables** directory on the left sidebar.

    ![Find tables in Synapse.](media/find-tables-synapse.png "Find tables in Synapse")

3. Right-click the desired table and select **New SQL script** > **Select TOP 100 rows**.

    ![Select top rows.](media/select-top-rows.png "Select top rows")

4. Select **Run**. Your query results are displayed on the **Results** tab. Alternatively, you can edit the script to your needs.

    ![Run query.](media/run-query.png "Run query")

## Query multiple Dataverse databases with serverless SQL pool

> [!NOTE]
>
> - Azure Synapse Link for Dataverse does not support the use of dedicated SQL pools at this time.
> - Querying multiple Dataverse databases requires that both Dataverse environments are in the same region.

1. Add another Azure Data Lake Storage Gen2 account as a Linked service to the same Azure Synapse Analytics workspace where the current link resides.

2. Follow the configuration steps to create a new Azure Synapse Link with the new Azure Synapse Analytics and Azure Data Lake combination.

3. Navigate to the shared Synapse workspace and expand **Databases**. Select one of the Dataverse containers. Your exported tables are displayed under the **Tables** directory on the left sidebar.

4. Right-click the a table and select **New SQL script** > **Select TOP 100 rows**.

5. Edit the query to combine the two datasets. For instance, you can join the datasets based on a unique ID value.

6. Select **Run**. Your query results are displayed on the **Results** tab.

### See also

[Blog: Announcing Azure Synapse Link for Dataverse](https://aka.ms/synapse-dataverse)

[!INCLUDE[footer-include](../../includes/footer-banner.md)]
