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

## How to use this solution template in Synapse Workspace

1. In [Power Apps](https://make.powerapps.com/?utm_source=padocs&utm_medium=linkinadoc&utm_campaign=referralsfromdoc), go to **Data** > **Azure Synapse Link**, select your desired Azure Synapse Link from the list, and then select **Go to Azure Synapse workspace**.
   :::image type="content" source="media/go-to-workspace.png" alt-text="Go to Azure Synapse Workspace":::

1. Select on **Integrate** > **Browse gallery**. Select **Copy Dataverse data into Azure SQL using Synapse Link** from the gallery.



### See also

[Blog: Announcing Azure Synapse Link for Dataverse](https://aka.ms/synapse-dataverse)

[!INCLUDE[footer-include](../../includes/footer-banner.md)]
