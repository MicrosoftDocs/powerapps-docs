---
title: "Run Azure Synapse pipelines with your Azure Synapse Link for Dataverse data | MicrosoftDocs"
description: "Learn how to run Azure Synapse pipelines with your exported Dataverse table data"
ms.custom: ""
ms.date: 01/24/2021
ms.reviewer: "Mattp123"

ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "how-to"
applies_to: 
  - "powerapps"
author: "sabinn-msft"
ms.assetid: 
ms.subservice: dataverse-maker
ms.author: "matp"
manager: "kvivek"
search.audienceType: 
  - maker
search.app: 
  - PowerApps
  - D365CE
contributors: "sama-zaki"
---

# Run Azure Synapse pipelines with your Azure Synapse Link for Dataverse data

[!INCLUDE[cc-data-platform-banner](../../includes/cc-data-platform-banner.md)]

You can use the Azure Synapse Link to connect your Microsoft Dataverse data to Azure Synapse Analytics to explore your data and accelerate time to insight. This article shows you how to run Azure Synapse pipelines utilizing the Workspace DB connector in Data Flow activities.

> [!NOTE]
> Azure Synapse Link for Microsoft Dataverse was formerly known as Export to data lake. The service was renamed effective May 2021 and will continue to export data to Azure Data Lake as well as Azure Synapse Analytics.

## Prerequisites

This section describes the prerequisites necessary to query your Dataverse data after using the Azure Synapse Link for Dataverse service.

- **Azure Synapse Link for Dataverse.** This guide assumes that you have already exported data from Dataverse by using the [Azure Synapse Link for Dataverse](export-to-data-lake.md).

- **Storage Account Access.** You must be granted one of the following roles for the storage account: Storage Blob Data Reader, Storage Blob Data Contributor, or Storage Blob Data Owner.

- **Synapse administrator.** You must be granted **Synapse Administrator** role access within Synapse studio.

## Create a data flow with and connect to your Dataverse data with the Workspace DB connector

> [!NOTE]
> Azure Synapse Link for Dataverse does not support the use of dedicated SQL pools at this time.

1. In Power Apps, select your desired Azure Synapse Link from the list, and then select **Go to Azure Synapse workspace**.

    ![Go to workspace.](media/go-to-workspace.png "Go to workspace")

2. Select **Develop** > **+** > **Data flow** to create a new data flow.

    :::image type="content" source="media/develop-data-flow.png" alt-text="Develop data flow":::

3. Select **Add Source** from the workspace area and set the **Source type** to **Workspace DB**. Select the Dataverse database and a table to use in the pipeline.

    :::image type="content" source="media/workspace-db-connector.png" alt-text="Workspace DB Connector":::

4. Optionally, add other transformation steps.

5. Add a sink to your data flow.

## Create and run an Azure Synapse pipeline

1. Select **Integrate** > **+** > **Pipeline**.

    :::image type="content" source="media/create-synapse-pipeline.png" alt-text="Create Synapse Pipeline":::

2. Expand **Move & Transform**, then drag and drop a **Data flow** activity to the workspace.

3. Under **Settings**, select the name of the data flow created in the previous section.

    :::image type="content" source="media/run-synapse-pipeline.png" alt-text="Run Synapse pipeline":::

4. Run the pipeline by selecting **Debug**. Optionally **Add trigger** to run the pipeline on a schedule.

### See also

[Blog: Announcing Azure Synapse Link for Dataverse](https://aka.ms/synapse-dataverse)

[!INCLUDE[footer-include](../../includes/footer-banner.md)]
