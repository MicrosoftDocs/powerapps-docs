---
title: "Query and analyze the incremental updates | MicrosoftDocs"
description: "Learn how to query and analyze the incremental updates made to Microsoft Dataverse data during a user-specified time interval with Power Apps and Azure Synapse Analytics"
ms.custom: ""
ms.date: 07/29/2024
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

Microsoft Dataverse data (including data from Dynamics 365 apps including Finance and Operations) can continuously change through create, update, and delete transactions. With the incremental update option, you can build incremental data pipelines that apply these changes to downstream systems and databases. Synapse Link for Dataverse exports incremental data in time stamped folders that contain data changes during within a user-specified time interval. 

You can leverage incremental update feature for several scenarios. 

- **Update a downstream Data store or a data warehouse**. You may need to apply changes from your Business data into a downstream data store. Incremental update is a standard capability in most data transformation tools, such as Azure Data Factory. However, for the incremental update feature to work, you must identify the records that changed in source tables. Incremental update feature provides changed data as a set of files such that you don't need to detect changes by comparing before and after images of tables.
  
- **Analyze changes in large datasets**. If you need to analyze changes in large data sets, incremental update feature provides a continuous stream of data in small batches such that you don't need to store all data. 
>
> - Drop stale and stagnant data to save data storage costs.  
> - Track data changes during a user-specified time period.
>   

Azure Synapse Link for Dataverse also provides the option to export and maintain a replica of tables in your Azure Data Lake (Gen 2) storage. You can configure Azure synapse Link to export incremental data in addition to exporting a replica of tables. Each configuration (known as a "Synapse Link profile") can export either tables or incremental. While you can create multiple profiles, you can not configure both tables and incremental updates within the same profile.

> [!IMPORTANT]
> An initial time stamped folder will be created when you enable this feature with a copy of your data. Subsequent Timestamp and table folders are created only when there is a data update during the user-specified time interval. 
>
> Once you create a Synapse Link profile with incremental update feature, the configuration will apply to all selected tables within the Synapse Link profile. 
>
> This feature can't be enabled with the option: **Connect to your Azure Synapse workspace**. For customers who require Azure Synapse analytics access, follow this instruction to setup the link: [Create an Azure Synapse Link for Dataverse with your Azure Synapse Workspace](azure-synapse-link-synapse.md) 
>  
> This feature is equivalent to [**Change feeds** feature in Export to Data lake](https://learn.microsoft.com/dynamics365/fin-ops-core/dev-itpro/data-entities/azure-data-lake-change-feeds) built into Dynamics 365 Finance and Operations apps. Customers using **Change feeds** feature now have the option to enable a Synapse Link profile with change data without having to export Table data.
> 
> This feature is designed to work with Azure Data Factory or Synapse Pipeline to copy data from Azure Data Lake Storage Gen2 to an Azure SQL Database. More information:[Copy Dataverse data into Azure SQL](azure-synapse-link-pipelines.md).
>
> Dynamics 365 Finance and Operations customers transitioning from Change feeds feature can use [Data integration sample tools provided in github](https://github.com/microsoft/Dynamics-365-FastTrack-Implementation-Assets/tree/master/Analytics/DataverseLink/DataIntegration) to update existing data pipelines used with the Change feeds feature.
> 

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
> The minimum time interval is five minutes. That means the incremental update folder is created every five minutes and contain the changes that occurred within the time interval. This setting is also configurable after the link creation via **Manage tables**
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
