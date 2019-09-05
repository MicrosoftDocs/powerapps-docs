---
title: "Connect Azure Data Lake Storage Gen2 for dataflow storage | MicrosoftDocs"
description: "Learn how connect Azure Data Lake Storage Gen2 for dataflow storage"
ms.custom: ""
ms.date: 09/05/2019
ms.reviewer: ""
ms.service: powerapps
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
applies_to: 
  - "Dynamics 365 (online)"
  - "Dynamics 365 Version 9.x"
  - "powerapps"
author: "Mattp123"
ms.assetid: 
caps.latest.revision: 
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

[!INCLUDE [cc-beta-prerelease-disclaimer](../../includes/cc-beta-prerelease-disclaimer.md)]

You can configure dataflows to store their data in your organization’s Azure Data Lake Storage Gen2 account. This article describes the general steps necessary to do so, and provides guidance and best practices along the way. There are some advantages to configuring dataflows to store their definitions and datafiles in your data lake, including the following:

- Azure Data Lake Storage Gen2 provides an enormously scalable storage facility for data
- Dataflow data and definition files can be leveraged by your IT department's developers to leverage Azure Data and artificial intelligence (AI) services as demonstrated in the GitHub samples from Azure Data Services
- Enables developers in your organization to integrate dataflow data into internal applications, and line-of-business solutions, using developer resources for dataflows and Azure

> [!IMPORTANT]
> You should not change files created by dataflows in your organization’s lake or add files to a dataflow’s CDM Folder. Changing files might damage dataflows or alter their behavior and is not supported. Power Platform Dataflows only grants read access to files it creates in the lake. If you authorize other people or services to the filesystem used by Power Platform Dataflows, only grant them read access to files or folders in that filesystem.

## Requirements
To use Azure Data Lake Storage Gen2 for dataflows, you need the following:
- A PowerApps environment – any PowerApps plan will allow you to create dataflows with Azure Data Lake Storage Gen2 as a destination, you will need to be authorized the environment as a maker. 
- An Azure subscription - you need an Azure subscription to use Azure Data Lake Storage Gen2
- Resource group - use a resource group you already have, or you can create a new one
- An Azure Storage account with Data Lake Storage Gen2 feature enabled

> [!TIP]
> If you don't have an Azure subscription, create a free account before you begin.

## Prepare your Azure Data Lake Storage Gen2 for Power Platform Dataflows
Before you can configure Power BI with an Azure Data Lake Storage Gen2 account, you must create and configure a storage account. Let's take a look at the requirements for Power Platform Dataflows:
1.	The storage account must be created in the same AAD tenant as your PowerApps tenant.
2.	It is recommended that the storage account is created in the same region as the PowerApps environment you plan to use it in. To determine where you PowerApps environment is contact your environment admin.
3.	The storage account must have the Hierarchical Name Space feature enabled.
4.	You must must be granted an Owner role on the storage account.
The following sections walk through the steps necessary to configure your Azure Data Lake Storage Gen2 account in detail.

## Create the storage account
Follow the steps in the Create an Azure Data Lake Storage Gen2 storage account article.
1.	Make sure you select the same location as your Power BI tenant, and set your storage as StorageV2 (general purpose v2)
2.	Make sure you enable the hierarchical namespace feature
3.	It is recommended to set replication setting to Read-access geo-redundant storage (RA-GRS)

## Create a Cross-Origin Resource Sharing (CORS) rule for the Athena service

> [!NOTE]
> Power Platform Dataflows leveraged the Athena service to connect a Data Lake to a PowerApps environment. In this section, you are required to grant the Athena service a role to the storage account, so it can be configured for Dataflow use

Next, you need to enable the Athena service access the storage account via web browser and the PowerApps portal. Web browsers implement a security restriction known as same-origin policy that prevents a web page from calling APIs in a different domain; CORS provides a secure way to allow one domain (the origin domain) to call APIs in another domain. See the CORS specification for details on CORS.

Follow the steps in the storage account, you just created, settings page in the Azure Portal. In the CORS menu item, select the Blob service section and enter these details. 

|Setting  |Value  |
|---------|---------|
|Allowed origins   | https://athena-ui-prod.trafficmanager.net     |
|Allowed methods   |  DELETE, GET, HEAD, MERGE, POST, OPTIONS, PUT, PATCH   |
|Allowed headers   | *        |
|Exposed headers   | *        |
|Max age |         *|


The following image shows the CORS Rule configured for the Athena Service.
![CORS rule](media/dataflows-cores-rule.png)

## Connect your Azure Data Lake Storage Gen2 to PowerApps
Once you've set up your Azure Data Lake Storage Gen2 account in the Azure portal, you are ready to connect it to a specific dataflow or a PowerApps environment from the PowerApps portal. Connecting the lake to an environment will allow other makers and admins in the environment to create dataflows that store their data in your organizations lake as well. 

You connect your Azure Data Lake Storage Gen2 account with the following steps:
1.	Sign in to [PowerApps](https://web.powerapps.com/?utm_source=padocs&utm_medium=linkinadoc&utm_campaign=referralsfromdoc), and verify which environment you're in, find the environment switcher near the right side of the header. 
2. Click or tap the down arrow for Data near the left edge.

   ![PowerApps maker portal Data tab](media/powerapps-portal-data.png)

3. In the list that appears, click or tap Dataflows, and then click or tap New Dataflow near the upper-right corner of the window.

   ![Create a new dataflow](media/new-dataflow.png) 

4. From there, you select analytical entities only to indicate you would like to store data in your organizations Azure Data Lake Store Gen2 account. 

   ![Select analytical entities](media/select-analytical-entities.png)

## Select the Storage Account to use for Dataflow storage
If a storage account has not yet been associated with the environment, Link to data lake dialog will appear. You will need to sign in, and find the Data Lake you created in previous steps. In this example there is no lake associated with the environment so we will be prompted to add a lake. 

1. Select storage account
    The following screen will appear:
    ![Select storage account](media/select-storage-account.png)
2. Select the Subscription ID of the Storage Account.
3. Select the Resource Group name in which the storage account was created.
4. Provide the Storage Account name.
5. Select **Save**.

Once those steps are successfully completed, your Azure Data Lake Storage Gen2 is connected to Power Platform Dataflows and you can continue to create a dataflow.

## Considerations and limitations
This feature is a preview feature, and its behavior may change as it approaches release. There are a few considerations and limitations to keep in mind when working with your dataflow storage:
- Linking an Azure Data Lake Store Gen2 account for dataflow storage is not supported in the default environment.
- Once a dataflow storage location is configured for a dataflow, it cannot be changed.
- By default member of the environment can access dataflow data using the Power Platform Dataflows Connector. However, only the owners of a dataflow can access its files directly in Azure Data Lake Storage Gen2. To authorize additional people to access the dataflows data directly in the lake, you must authorize them to the dataflow’s CDM folder in the lake or the lake itself.
- When a Dataflow is deleted, its CDM Folder in the lake will be deleted. It is not recommended to modify or add files to a dataflow’s CDM Folder.

## Frequently asked questions
*What if I had previously created dataflows in my organization’s Azure Data Lake Storage Gen2 and would like to change their storage location?*

You cannot change the storage location of a dataflow after it was created.

*When can I change the dataflow storage location of an environment?*

Changing the environments dataflow storage location is not yet allowed 

## Next steps
This article provided guidance on how to connect an Azure Data Lake Gen2 for dataflow storage. For additional information, take a look at the following articles:
For more information about dataflows, CDM, and Azure Data Lake Storage Gen2, take a look at the following articles:

- [Self-service data prep in PowerApps](https://go.microsoft.com/fwlink/?linkid=2099972)
- [Creating and using dataflows in PowerApps](https://go.microsoft.com/fwlink/?linkid=2100076)
- [Connect Azure Data Lake Storage Gen2 for dataflow storage](https://go.microsoft.com/fwlink/?linkid=2099973)
- [Add data to an entity in Common Data Service](https://go.microsoft.com/fwlink/?linkid=2100075)

For more information about Azure storage, you can read these articles:
- [Azure Storage security guide](https://docs.microsoft.com/azure/storage/common/storage-security-guide)
For more information about the Common Data Model, you can read its overview article:
- [Common Data Model - overview](https://docs.microsoft.com/powerapps/common-data-model/overview) 
- [CDM folders](https://go.microsoft.com/fwlink/?linkid=2045304)
- [CDM model file definition](https://go.microsoft.com/fwlink/?linkid=2045521)

And you can always try asking questions of the [PowerApps Community](https://go.microsoft.com/fwlink/?linkid=2099971).
