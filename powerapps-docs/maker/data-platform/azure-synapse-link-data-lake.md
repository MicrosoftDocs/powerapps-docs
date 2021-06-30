---
title: "Configure Azure Synapse Link for Dataverse with Azure Data Lake | MicrosoftDocs"
description: "Learn how to export table data to Azure Data Lake Storage Gen2 in Power Apps"
ms.custom: ""
ms.date: 02/10/2021
ms.reviewer: "Mattp123"
ms.service: powerapps
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "how-to"
applies_to: 
  - "powerapps"
author: "sabinn-msft"
ms.assetid: 
ms.author: "matp"
manager: "kvivek"
search.audienceType: 
  - maker
search.app: 
  - PowerApps
  - D365CE
contributors:
  - sama-zaki
---

# Configure Azure Synapse Link for Dataverse with Azure Data Lake

[!INCLUDE[cc-data-platform-banner](../../includes/cc-data-platform-banner.md)]

You can use the Azure Synapse Link to connect your Microsoft Dataverse data to Azure Data Lake Storage Gen2 to enable various analytics scenarios. This article shows you how to connect your Dataverse data to your Azure Data Lake Storage Gen2 account.

> [!NOTE]
> Azure Synapse Link for Dataverse was formerly known as Export to data lake. The service was renamed effective May 2021 and will continue to export data to Azure Data Lake as well as Azure Synapse Analytics.

## Prerequisites

### Azure Data Lake Storage Gen2

Follow the steps in the [Create an Azure Storage account](/azure/storage/blobs/data-lake-storage-quickstart-create-account) article, and note these requirements:

- You must be granted an **Owner** and **Storage Blob Data Contributor** role on the storage account.
- The storage account must have the **Hierarchical namespace** feature enabled. By enabling the hierarchical namespace, you are automatically setting the storage account to be a **Data Lake Storage Gen2** account.

Additionally, we recommend that you set replication to **read-access geo-redundant storage (RA-GRS)**. More information: [Read-access geo-redundant storage](/azure/storage/common/storage-redundancy-grs#read-access-geo-redundant-storage).

![Storage account properties](media/storage-account-properties.png "Storage account properties")

> [!NOTE]
> - The storage account must be created in the same Azure Active Directory (Azure AD) tenant as your Power Apps tenant.
> - The storage account must be created in the same region as the Power Apps environment you will use the feature in.
> - You must have **Reader** role access to the resource group with the storage account.  
> - To link the Dataverse environment to Azure Data Lake Storage Gen2, you must be a Dataverse administrator.
> - Only tables that have change tracking enabled can be exported.

## Select and export Dataverse table data to Azure Data Lake Storage Gen2

1. Sign in to [Power Apps](https://make.powerapps.com/?utm_source=padocs&utm_medium=linkinadoc&utm_campaign=referralsfromdoc) and select your preferred environment.

2. Select **Data** > **Azure Synapse Link** from the left sidebar and select **+ New link to data lake** from the top.

    ![Navigate to Power Apps](media/navigate-to-powerapps.png "Navigate to Power Apps")

3. Select each of the following settings, and then select **Next**:
   - **Subscription**. Select your Azure subscription.
   - **Resource group**. Select the resource group that contains the Azure Data Lake Storage Gen2 account.
   - **Storage account**. Select the Azure Data Lake Storage Gen2 account to use for the export.

    > [!NOTE]
    > As part of linking the Dataverse environment to a data lake, you grant the Azure Synapse Link service access to your storage account. Ensure that you followed the [prerequisites](#prerequisites) of creating and configuring the Azure data lake storage account, and granting yourself an owner role on the storage account. Additionally, you grant the Power Platform Dataflows service access to your storage account. More information: [Self-service data prep with dataflows](self-service-data-prep-with-dataflows.md).  

4. Select the tables that you want to export to the data lake, and then select **Save**. Only tables with change tracking enabled can be exported. More information: [Enable change tracking](/dynamics365/customer-engagement/admin/enable-change-tracking-control-data-synchronization).

   ![Select tables for export](media/export-data-lake-select-entity.png "Select tables for export")

Your Dataverse environment is linked to the Azure Data Lake Storage Gen2 account. The file system in the Azure storage account is created with a folder for each table selected to be replicated to the data lake.

You can follow the steps above to create a link from one Dataverse environment to multiple Azure data lakes in your Azure subscription. Similarly, you could create a link from multiple Dataverse environments to the same Azure Data Lake, all within the same tenant.

> [!NOTE]
> The data exported by Azure Synapse Link service is encrypted at rest in Azure Data Lake Storage Gen2. Additionally, transient data in the blob storage is also encrypted at rest. Encryption in Azure Data Lake Storage Gen2 helps you protect your data, implement enterprise security policies, and meet regulatory compliance requirements. More information: [Azure Data Encryption-at-Rest]( /azure/security/fundamentals/encryption-atrest)
>
> Currently, you can't provide public IPs for the Azure Synapse Link for Dataverse service that can be used in **Azure Data Lake firewall settings**. Public IP network rules have no effect on requests originating from the same Azure region as the storage account. Services deployed in the same region as the storage account use private Azure IP addresses for communication. Thus, you can't restrict access to specific Azure services based on their public outbound IP address range.
More information: [Configure Azure Storage firewalls and virtual networks]( /azure/storage/common/storage-network-security)

## Manage table data to the data lake

After you have set up the Azure Synapse Link, you can manage the tables that are exported in one of two ways:

- On the Power Apps maker portal **Azure Synapse Link** area, select **Manage tables** on the command bar to add or remove one or more linked tables.
- On the Power Apps maker portal **Tables** area, select **…** next to a table, and then select the linked data lake where you want to export table data.

   ![Select a table for export](media/select-entity-export.png "Select a table for export")

To unlink all linked tables, on the Power Apps maker portal **Azure Synapse Link** area, select **Unlink data lake**.

## View your data in Azure Data Lake Storage Gen2

1. Sign in to [Azure](https://portal.azure.com), select the storage account, and then in the leftmost navigation pane, select **Storage Explorer**.
2. Expand **File Systems**, and then select Dataverse-*environmentName*-org-*Id*.

The model.json file, along with its name and version, provides a list of tables that have been exported to the data lake. The model.json file also includes the initial sync status and sync completion time.

A folder that includes snapshot comma-delimited (CSV format) files is displayed for each table exported to the data lake.
   ![Table data in the data lake](media/entity-data-in-lake.png "Table data in the data lake")

### What's next?
After successfully using the Azure Synapse Link for Dataverse service, discover how you can analyze and consume your data with **Discover Hub**. To access **Discover Hub**, go to **Power Apps** > **Azure Synapse Link**. Select your linked service and then select the **Discover Hub** tab. Here you can find recommended tools and curated documentation to help you get the most value out of your data.
![Discover Hub](media/discover-hub.png "Discover Hub")

### See also

[Analyze Dataverse data in the data lake with Power BI](./export-to-data-lake-data-powerbi.md)

[Ingest Dataverse data in the data lake with Azure Data Factory](./export-to-data-lake-data-adf.md)

[Azure Synapse Link for Dataverse Advanced Configuration](./azure-synapse-link-advanced-configuration.md)

[Azure Synapse Link FAQ](export-data-lake-faq.yml)

[!INCLUDE[footer-include](../../includes/footer-banner.md)]
