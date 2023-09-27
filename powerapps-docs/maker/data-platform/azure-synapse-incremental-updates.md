---
title: "Query and analyze the incremental updates | MicrosoftDocs"
description: "Learn how to query and analyze the incremental updates made to Microsoft Dataverse data during a user-specified time interval with Power Apps and Azure Synapse Analytics"
ms.custom: ""
ms.date: 02/07/2023
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
# Query and analyze the incremental updates

Microsoft Dataverse data can continuously change through create, update, and delete transactions. Synapse Link for Dataverse provides incremental folders to help you query and analyze the incremental updates made to Dataverse data during a user-specified time interval. Organizations with large datasets can analyze the incremental update data and:

- Drop stale and stagnant data to save data storage costs.  
- Track data changes during a user-specified time period.

When creating an Azure Synapse Link for Dataverse, you can enable the incremental update feature to create a series of timestamped folders containing only the changes to the Dataverse data that occurred during the user-specified time interval. In each timestamp folder, each exported table is stored under a separate *DataverseTableName* folder.

> [!IMPORTANT]
> Timestamp and table folders are created only when there is a data update during the user-specified time interval.
>
> This feature will apply to all selected tables within Azure Synapse Link for Dataverse and, by default, all the tables selected will be assigned append-only mode with incremental updates.
>
> This feature can't be enabled with the option: **Connect to your Azure Synapse workspace**. For customers who require Azure Synapse analytics access, follow this instruction to setup the link: [Create an Azure Synapse Link for Dataverse with your Azure Synapse Workspace](azure-synapse-link-synapse.md) 
>  
> This feature is designed to work with Azure Data Factory or Synapse Pipeline to copy data from Azure Data Lake Storage Gen2 to an Azure SQL Database. More information:[Copy Dataverse data into Azure SQL](azure-synapse-link-pipelines.md)

## Prerequisites

Azure Synapse Link for Dataverse. This guide assumes that you have already met the prerequisites to create an Azure Synapse Link. More information: [Create an Azure Synapse Link for Dataverse with Azure Data Lake](azure-synapse-link-data-lake.md#prerequisites)

## Connect Dataverse to Synapse workspace with incremental folder enabled 

1. Sign in to [Power Apps](https://make.powerapps.com/?utm_source=padocs&utm_medium=linkinadoc&utm_campaign=referralsfromdoc) and select your environment.
1. On the left navigation pane,  select **Azure Synapse Link**. [!INCLUDE [left-navigation-pane](../../includes/left-navigation-pane.md)] 
1. On the command bar, select **+ New link**.
1. Select the **Subscription**, **Resource group**, and **Storage account**. Select **Next**.  
1. Add the tables you want to export, and then select **Advanced**.  
1. Turn on **Show advanced configuration settings** and **Enable Incremental Update Folder Structure**.
1. Enter the time interval (in minutes) for how often the incremental updates should be captured, and then select **Save**.  

   :::image type="content" source="media/azure-synapse-add-tables-settings.png" alt-text="Add tables settings":::

> [!NOTE]
> The minimum time interval is 15 minutes. That means the incremental update folder will be created every 15 minutes and contain the changes that occurred within the time interval. This setting is also configurable after the link creation via **Manage tables**
>
> Ensure **Connect to your Azure Synapse workspace Azure Synapse workspace** is not checked in the first page of setup.

## View incremental folder at Microsoft Azure Storage

1. Select the desired Azure Synapse Link, and then select **Go to Azure data lake** on the command bar.
1. Select the **Containers** under **Data Storage**.
1. Select **dataverse**-*environmentName*-*organizationUniqueName*. Incremental updates folders are named by creation timestamp ("yyyy-MM-dd'T'HH:mm:ss.SSSz") in UTC.  

   :::image type="content" source="media/azure-synapse-incremental-folders.png" alt-text="Incremental folders in Azure Synapse":::

> [!NOTE]
> Due to the retry mechanism features, an extra empty timestamp folder might be created within the user-specified time interval.

### See also

[What is Azure Synapse Link for Dataverse?](export-to-data-lake.md)
