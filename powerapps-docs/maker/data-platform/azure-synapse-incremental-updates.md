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

## Prerequisites

Azure Synapse Link for Dataverse. This guide assumes that you have already met the prerequisites to create an Azure Synapse Link. More information: [Create an Azure Synapse Link for Dataverse with Azure Data Lake](azure-synapse-link-data-lake.md#prerequisites)

## Create a Synapse Link profile to export incremental data 

1. Sign in to [Power Apps](https://make.powerapps.com/?utm_source=padocs&utm_medium=linkinadoc&utm_campaign=referralsfromdoc) and select your environment.
2. On the left navigation pane,  select **Azure Synapse Link**. [!INCLUDE [left-navigation-pane](../../includes/left-navigation-pane.md)]
3. On the command bar, select **+ New link**.
4. Select the **Subscription**, **Resource group**, and **Storage account**. Select **Next**.
5. Do not select the option **Connect to your Azure Synapse workspace**. If you choose this option, incremental update feature is disabled.
6. Add the tables you want to export, If your Dataverse environment is linked to Finance and Operations apps, you can also select Tables from Finance and Operations apps. 
7. Select **Advanced**. 8. Turn on **Show advanced configuration settings** and **Enable Incremental Update Folder Structure**.
9. Enter the time interval (in minutes) for how often the incremental updates should be captured, and then select **Save**.  

   :::image type="content" source="media/azure-synapse-add-tables-settings.png" alt-text="Add tables settings":::

> [!NOTE]
> The minimum time interval is 5 minutes. That means the incremental update folder is created every five minutes and contain the changes that occurred within the time interval. This setting is also configurable after the link creation via **Manage tables**. Maximum time interval is 1140 (ie. 24 hrs). 
>
> Ensure **Connect to your Azure Synapse workspace Azure Synapse workspace** is not checked in the first page of setup.
>
> Incremental data in time stamped folders are stored as Comma Separated text files (CSV files). 

## View incremental folder at Microsoft Azure Storage
When you create a Synapse Link profile with incremental data, the system makes an initial copy of all tables and stores it in the first incremental update folder. Once the initial copy is created, system will create subsequent update folders with changed data. If there are no changes in any of the tables selected, you will not see incremental data folders.

To see incremental data folders in the storage account

1. Select the desired Azure Synapse Link, and then select **Go to Azure data lake** on the command bar.
2. Select the **Containers** under **Data Storage**.
3. Select **dataverse**-*environmentName*-*organizationUniqueName*. Incremental updates folders are named by creation timestamp ("yyyy-MM-dd'T'HH:mm:ss.SSSz") in UTC. You will notice that the time difference between time stamped folders is the time interval specified by you in advanced settings. 
4. Within each Time stamped folder, you will see folders for each tables. Not all tables chosen may have changed during the time interval and you will only see folders corresponding to tables whose data changed. 

   :::image type="content" source="media/Synapse_Link-Storage-folders.png" alt-text="Incremental folders in Azure Data lake storage created by Synapse Link":::

> [!NOTE]
> Due to the retry mechanism features, an extra empty timestamp folder might be created within the user-specified time interval.

## Consume incremental data
You can copy incremental into an Azure SQL Database or a Data warehouse using data integration tools such as Azure Data Factory or Synapse Pipelines. We have provided a sample Data pipeline that can be used for this purpoe. For more information:[Copy Dataverse data into Azure SQL](azure-synapse-link-pipelines.md).

If you are a Dynamics 365 Finance and Operations customers transitioning from Change feeds feature you can use [Data integration sample tools provided in github](https://github.com/microsoft/Dynamics-365-FastTrack-Implementation-Assets/tree/master/Analytics/DataverseLink/DataIntegration) to update existing data pipelines used with the Change feeds feature.

You can also build your own data pipeline to consume incremental data. However, you need to consider the following best practices when designing your own pipeline.
- **Consume data from previous time stamped folders only**: This way, you can avoid read-write conflicts with the Synapse Link service which may be continupusly updating data in the current folder. You can find the current Folder by using the **Changelog/changelog.info** file. This file is a read-only file which contains a single row with the folder name that is being currently being updated. You should not update this file as it may cause system instability.
- You can leverage **model.json** file located within each Time stamped folder to read metadata such as column names for the data contained in table folders. Notice that each model.json file in the folder located within  time stamped folders contain metadata for all the tables. Not just the tables contained within the time stamped folder.
- Avoid using other logfiles such as Synapse.log file. This file is used for internal purposes and may not reflect accurate data.
- You can consider deleting obsolete incremental folders from your Azure Data lake after you have finished processing. At present, Synapse Link maintains a lease on these files in Azure Storage to recover from any failures. System may release the lease after a time period.

:::image type="content" source="media/Synapse-Link-storage-change-Log-folder.png" alt-text="Incremental folders in Azure Data lake storage created by Synapse Link":::

### See also

[What is Azure Synapse Link for Dataverse?](export-to-data-lake.md)
