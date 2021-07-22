---
title: "Connect Azure Data Lake Storage Gen2 for dataflow storage | MicrosoftDocs"
description: "Learn how to connect Azure Data Lake Storage Gen2 for dataflow storage"
ms.custom: ""
ms.date: 12/05/2019
ms.reviewer: ""
ms.service: powerapps
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "how-to"
applies_to: 
  - "Dynamics 365 (online)"
  - "Dynamics 365 Version 9.x"
  - "powerapps"
author: "Mattp123"
ms.assetid: 
caps.latest.revision: 
ms.subservice: dataverse-maker
ms.author: "matp"
manager: "kvivek"
tags: 
search.audienceType: 
  - maker
search.app: 
  - PowerApps
  - D365CE
---
# Connect Azure Data Lake Storage Gen2 for dataflow storage

[!INCLUDE[cc-data-platform-banner](../../includes/cc-data-platform-banner.md)]

You can configure dataflows to store their data in your organization’s Azure Data Lake Storage Gen2 account. This article describes the general steps necessary to do so, and provides guidance and best practices along the way. 

> [!IMPORTANT]
> Dataflow with Analytical tables feature utilizes the Azure Synapse Link for Dataverse service, which may offer varying levels of compliance, privacy, security, and data location commitments. For more information about Azure Synapse Link for Dataverse, see the [blog article](https://go.microsoft.com/fwlink/?linkid=2109088).

There are some advantages to configuring dataflows to store their definitions and datafiles in your data lake, including the following:
- Azure Data Lake Storage Gen2 provides an enormously scalable storage facility for data.
- Dataflow data and definition files can be leveraged by your IT department's developers to leverage Azure data and artificial intelligence (AI) services as demonstrated in the GitHub samples from Azure data services.
- It enables developers in your organization to integrate dataflow data into internal applications and line-of-business solutions, using developer resources for dataflows and Azure.

## Requirements
To use Azure Data Lake Storage Gen2 for dataflows, you need the following:
- A Power Apps environment. Any Power Apps plan will allow you to create dataflows with Azure Data Lake Storage Gen2 as a destination. You'll need to be authorized in the environment as a maker. 
- An Azure subscription. You need an Azure subscription to use Azure Data Lake Storage Gen2.
- A resource group. Use a resource group you already have, or create a new one.
- An Azure storage account. The storage account must have the Data Lake Storage Gen2 feature enabled.

> [!TIP]
> If you don't have an Azure subscription, [create a free trial account](https://azure.microsoft.com/free/) before you begin.

## Prepare your Azure Data Lake Storage Gen2 for Power Platform Dataflows
Before you configure your environment with an Azure Data Lake Storage Gen2 account, you must create and configure a storage account. Here are the requirements for Power Platform Dataflows:
1.	The storage account must be created in the same Azure Active Directory tenant as your Power Apps tenant.
2.	We recommend that the storage account is created in the same region as the Power Apps environment you plan to use it in. To determine where your Power Apps environment is, contact your environment admin.
3.	The storage account must have the Hierarchical Name Space feature enabled.
4.	You must be granted an Owner role on the storage account.

The following sections walk through the steps necessary to configure your Azure Data Lake Storage Gen2 account.

## Create the storage account
Follow the steps in [Create an Azure Data Lake Storage Gen2 storage account](/azure/storage/blobs/data-lake-storage-quickstart-create-account).
1.	Make sure you select the same region as your environment and set your storage as StorageV2 (general purpose v2).
2.	Make sure you enable the hierarchical namespace feature. 
3.	We recommend that you set the replication setting to Read-access geo-redundant storage (RA-GRS).

## Connect your Azure Data Lake Storage Gen2 to Power Apps
Once you've set up your Azure Data Lake Storage Gen2 account in the Azure portal, you are ready to connect it to a specific dataflow or a Power Apps environment. Connecting the lake to an environment allows other makers and admins in the environment to create dataflows that store their data in your organization's lake as well. 

To connect your Azure Data Lake Storage Gen2 account with the dataflow, follow these steps:
1.	Sign in to [Power Apps](https://make.powerapps.com/?utm_source=padocs&utm_medium=linkinadoc&utm_campaign=referralsfromdoc), and verify which environment you're in. The environment switcher is located on the right side of the header. 
2. On the left navigation pane, select the down arrow next to **Data**.

   ![Power Apps maker portal Data tab.](media/powerapps-portal-data.png)

3. In the list that appears, select **Dataflows** and then on the command bar select **New dataflow**.

   ![Create a new dataflow.](media/create-a-dataflow.png) 

4. Select the analytical tables you want. These tables indicate what data you want to store in your organization's Azure Data Lake Store Gen2 account. 

   ![Select analytical tables.](media/select-analytical-entities.png)

## Select the storage account to use for dataflow storage
If a storage account has not yet been associated with the environment, a **Link to data lake** dialog box appears. You'll need to sign in and find the data lake you created in the previous steps. In this example, no data lake is associated with the environment and so a prompt occurs to add one. 


1. Select storage account.

    The **Select Storage Account** screen appears.
    
    ![Select storage account.](media/select-storage-account.png)
    
2. Select the **Subscription ID** of the storage account.
3. Select the **Resource group name** in which the storage account was created.
4. Enter the **Storage account name**.
5. Select **Save**.

Once these steps are successfully completed, your Azure Data Lake Storage Gen2 account is connected to Power Platform Dataflows and you can continue to create a dataflow.

## Considerations and limitations
There are a few considerations and limitations to keep in mind when working with your dataflow storage:
- Linking an Azure Data Lake Store Gen2 account for dataflow storage is not supported in the default environment.
- Once a dataflow storage location is configured for a dataflow, it can't be changed.
- By default, any member of the environment can access dataflow data using the Power Platform Dataflows Connector. However, only the owners of a dataflow can access its files directly in Azure Data Lake Storage Gen2. To authorize additional people to access the dataflows data directly in the lake, you must authorize them to the dataflow’s **CDM Folder** in the data lake or the data lake itself.
- When a dataflow is deleted, its **CDM Folder** in the lake will also be deleted. 

> [!IMPORTANT]
> You shouldn't change files created by dataflows in your organization’s lake or add files to a dataflow’s **CDM Folder**. Changing files might damage dataflows or alter their behavior and is not supported. Power Platform Dataflows only grants read access to files it creates in the lake. If you authorize other people or services to the filesystem used by Power Platform Dataflows, only grant them read access to files or folders in that filesystem.

## Privacy notice
By enabling the creation of dataflows with Analytical tables in your organization, via the Azure Synapse Link for Dataverse service, details about the Azure Data Lake storage account, such as the name of the storage account, will be sent to and stored in the Azure Synapse Link for Dataverse service, which is currently located outside the PowerApps compliance boundary and may employ lesser or different privacy and security measures than those typically in PowerApps. Note that you may remove the data lake association at any time to discontinue use of this functionality and your Azure Data Lake storage account details will be removed from the Azure Synapse Link for Dataverse service.
Further information about Azure Synapse Link for Dataverse is available in [this article.](https://go.microsoft.com/fwlink/?linkid=2109088)


## Frequently asked questions
*What if I had previously created dataflows in my organization’s Azure Data Lake Storage Gen2 and would like to change their storage location?*

   You can't change the storage location of a dataflow after it was created.

*When can I change the dataflow storage location of an environment?*

   Changing the environment's dataflow storage location is not currently supported. 

## Next steps
This article provided guidance about how to connect an Azure Data Lake Storage Gen2 account for dataflow storage. 

For more information about dataflows, the Common Data Model, and Azure Data Lake Storage Gen2, see these articles:
- [Self-service data prep with dataflows](./self-service-data-prep-with-dataflows.md)
- [Creating and using dataflows in Power Apps](./create-and-use-dataflows.md)
- [Connect Azure Data Lake Storage Gen2 for dataflow storage]()
- [Add data to a table in Microsoft Dataverse](./add-data-power-query.md)

For more information about Azure storage, see this article:
- [Azure Storage security guide](/azure/storage/common/storage-security-guide)

For more information about the Common Data Model, see these articles:
- [Common Data Model - overview](/common-data-model/) 
- [Common Data Model folders](/common-data-model/data-lake)
- [CDM model file definition](/common-data-model/model-json)

You can ask questions in the [Power Apps Community](https://go.microsoft.com/fwlink/?linkid=2099971).


[!INCLUDE[footer-include](../../includes/footer-banner.md)]