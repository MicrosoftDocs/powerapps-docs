---
title: "Query and analyze the incremental updates | MicrosoftDocs"
description: "Learn how to query and analyze the incremental updates made to Microsoft Dataverse data during a user-specified time interval with Power Apps and Azure Synapse Analytics"
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
manager: "kvivek"
search.audienceType: 
  - maker
search.app: 
  - PowerApps
  - D365CE
contributors:
  - 
---
# Query and analyze the incremental updates (preview)

[!INCLUDE [cc-beta-prerelease-disclaimer](../../includes/cc-beta-prerelease-disclaimer.md)]

Microsoft Dataverse data can continuously change through create, update, and delete transactions. Synapse Link for Dataverse provides incremental folders to help you query and analyze the incremental updates made to Dataverse data during a user-specified time interval. Organizations with large datasets can analyze the incremental update data and:

- Drop stale and stagnant data to save data processing costs and increase efficiency in Azure Synapse Analytics.  
- Track data changes during a user-specified time period.

When creating an Azure Synapse Link for Dataverse with your Azure Synapse Workspace, you can enable the incremental update feature to create a series of timestamped folders containing only the changes to the Dataverse data that occurred during the user-specified time interval. In each timestamp folder, each exported table is stored under a separate *DataverseTableName* folder.

> [!NOTE]
> This is a preview feature.
> 
> Timestamp and table folders are created only when there is a data update during the user-specified time interval.

## Prerequisites

Azure Synapse Link for Dataverse. This guide assumes that you have already met the prerequisites to create an Azure Synapse Link with a Synapse workspace.  More information: [Create an Azure Synapse Link for Dataverse with your Azure Synapse Workspace](azure-synapse-link-synapse.md#prerequisites)

## Connect Dataverse to Synapse workspace with incremental folder enabled 

1. Sign in to [Power Apps](https://make.powerapps.com/?utm_source=padocs&utm_medium=linkinadoc&utm_campaign=referralsfromdoc) and select your environment.
1. On the left navigation pane, select **Dataverse**, select **Azure Synapse Link**, and then on the command bar, select **+ New link**.
1. In your web browsers address bar, append `?athena.folderSplit=true` to the web address that ends with **exporttodatalake**.
1. Select the **Subscription**, **Resource group**, and **Storage account**. Select **Next**.  
1. Add the tables you want to export, and then select **Advanced**.  
1. Turn on **Show advanced configuration settings** and **Enable Incremental Update Folder Structure**.
1. Enter the time interval (in minutes) for how often the incremental updates should be captured, and then select **Save**.  

   :::image type="content" source="media/azure-synapse-add-tables-settings.png" alt-text="Add tables settings":::

> [!NOTE]
> The minimum time interval should be 15. That means the incremental update folder will be created every 15 minutes and contain the changes that occurred within the time interval.

## View incremental folder at Microsoft Azure Storage

1. Select the desired Azure Synapse Link, and then select **Go to Azure data lake** on the command bar.
1. Select the **Containers** under **Data Storage**.
1. Select **dataverse**-*environmentName*-*organizationUniqueName*. Incremental updates folders are named by creation timestamp ("yyyy-MM-dd'T'HH:mm:ss.SSSz") in UTC.  

   :::image type="content" source="media/azure-synapse-incremental-folders.png" alt-text="Incremental folders in Azure Synapse":::

## View incremental folder enabled table data at Azure Synapse Analytics workspace

1. Select the desired Azure Synapse Link, and select **Go to Azure Synapse Analytics workspace**.
1. Expand **Lake Databases** from the left pane, select **dataverse**-*environmentName*-*sessionid*, and then expand **Tables**.  

For each synced table, all stored records are merged into one complete table for efficient consumption.

> [!NOTE]
> The built-in SQL template is ready for a quick table view. Right-click the table, and then select **New SQL Script – Select TOP 100 rows**. A SQL script appears. Select **Run** to check the result.

### See also

[What is Azure Synapse Link for Dataverse?](export-to-data-lake.md)