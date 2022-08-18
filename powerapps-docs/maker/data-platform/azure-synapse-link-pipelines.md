---
title: "Run Azure Synapse pipelines with your Azure Synapse Link for Dataverse data | MicrosoftDocs"
description: "Learn how to run Azure Synapse pipelines with your exported Dataverse table data"
ms.custom: ""
ms.date: 08/18/2022
ms.reviewer: "Mattp123"
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "how-to"
applies_to: 
  - "powerapps"
author: "JasonHQX"
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

# Copy Dataverse data into Azure SQL using Synapse Link

[!INCLUDE[cc-data-platform-banner](../../includes/cc-data-platform-banner.md)]

Use the Azure Synapse Link to connect your Microsoft Dataverse data to Azure Synapse Analytics to explore your data and accelerate time to insight. This article shows you how to run Azure Synapse pipelines to copy data from Azure Data Lake Storage Gen2 to an Azure SQL Database utilizing the Workspace DB connector with incremental updates feature enabled in Synapse Link.

> [!NOTE]
> Azure Synapse Link for Microsoft Dataverse was formerly known as Export to data lake. The service was renamed effective May 2021 and will continue to export data to Azure Data Lake as well as Azure Synapse Analytics.

## Prerequisites

1. Azure Synapse Link for Dataverse. This guide assumes that you have already met the prerequisites to create an Azure Synapse Link with a Synapse workspace. More information: [Prerequisites for an Azure Synapse Link for Dataverse with your Azure Synapse Workspace](azure-synapse-link-synapse.md#prerequisites)
2. Create an Azure Synapse Workspace or Azure Data Factory under the same Azure Active Directory (Azure AD) tenant as your Power Apps tenant.
3. Create a Synapse Link for Dataverse with the incremental folder update enabled. More information: [Query and analyze the incremental updates](azure-synapse-incremental-updates.md)
4. Microsoft.EventGrid provider needs to be registered for trigger. More information: [Azure portal](/azure/azure-resource-manager/management/resource-providers-and-types#azure-portal)
5. Create Azure SQL DB with the **Allow Azure services and resources to access this server** property enabled. More information: [What should I know when setting up my Azure SQL Database (PaaS)?](/archive/blogs/azureedu/what-should-i-know-when-setting-up-my-azure-sql-database-paas#firewall)
6. Create and configure Azure Integration Runtime. More information: [Create Azure integration runtime - Azure Data Factory & Azure Synapse](/azure/data-factory/create-azure-integration-runtime?tabs=data-factory)


<!--Start revising here-->
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
