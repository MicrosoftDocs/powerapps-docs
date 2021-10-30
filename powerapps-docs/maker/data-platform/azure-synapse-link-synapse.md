---
title: "Create an Azure Synapse Link for Dataverse with your Azure Synapse Workspace | MicrosoftDocs"
description: "Learn how to export table data to Azure Synapse Analytics in Power Apps"
ms.custom: ""
ms.date: 08/17/2021
ms.reviewer: "Mattp123"
ms.service: powerapps
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
contributors:
  - sama-zaki
---

# Create an Azure Synapse Link for Dataverse with your Azure Synapse Workspace (Preview)

[!INCLUDE[cc-data-platform-banner](../../includes/cc-data-platform-banner.md)]

You can use the Azure Synapse Link to connect your Microsoft Dataverse data to Azure Synapse Analytics to explore your data and accelerate time to insight. This article shows you how to perform the following tasks:

1. Connect your Dataverse data to your Azure Synapse Analytics workspace with the Azure Synapse Link service.
2. Manage Dataverse tables included in the Azure Synapse Link.
3. Monitor your Azure Synapse Link.
4. Unlink your Azure Synapse Link.
5. Relink your Azure Synapse Link.
6. View your data in Azure Synapse Analytics.

> [!NOTE]
>
> - Azure Synapse Link for Microsoft Dataverse was formerly known as Export to data lake. The service was renamed effective May 2021 and will continue to export data to Azure Data Lake as well as Azure Synapse Analytics.

## Prerequisites

- Azure Data Lake Storage Gen2: You must have an Azure Data Lake Storage Gen2 account and **Owner** and **Storage Blob Data Contributor** role access. Your storage account must enable **Hierarchical namespace** and it is recommended that replication is set to **read-access geo-redundant storage (RA-GRS)**. 

- Synapse workspace: You must have a Synapse workspace and the **Synapse Administrator** role access within the Synapse Studio. The Synapse workspace must be in the same region as your Azure Data Lake Storage Gen2 account. The storage account must be added as a linked service within the Synapse Studio. To create a Synapse workspace, go to [Creating a Synapse workspace](/azure/synapse-analytics/get-started-create-workspace).

> [!NOTE]
>
> - The storage account and Synapse workspace must be created in the same Azure Active Directory (Azure AD) tenant as your Power Apps tenant.
> - The storage account and Synapse workspace must be created in the same region as the Power Apps environment you will use the feature in.
> - You must have **Reader** role access to the resource group with the storage account and Synapse workspace.  
> - To link the Dataverse environment to Azure Data Lake Storage Gen2, you must have the Dataverse system administrator security role.
> - Only tables that have change tracking enabled can be exported.
> - When you add multiple users to the synapse workspace, they must have the **Synapse Administrator** role access within the Synapse Studio and the **Storage Blob Data Contributor** role on the Azure Data Lake Storage Gen2 account.

## Connect Dataverse to Synapse workspace

1. Sign in to [Power Apps](https://make.powerapps.com/?utm_source=padocs&utm_medium=linkinadoc&utm_campaign=referralsfromdoc) and select your preferred environment.

2. On the left navigation pane, select **Data**, select **Azure Synapse Link**, and then on the command bar, select **+ New link to data lake**.

    ![Navigate to Power Apps.](media/navigate-to-powerapps.png "Navigate to Power Apps")

3. Select the the **Connect to your Azure Synapse workspace (Preview)** option.

4. Select the **Subscription**, **Resource group**, **Workspace name**, and **Storage account**. Ensure that the Synapse workspace and storage account meet the requirements specified in the [Prerequisites](#prerequisites) section. Select **Next**.

    ![Connect to your workspace.](media/connect-to-workspace.png "Connect to your workspace")

    > [!NOTE]
    > As part of linking the Dataverse environment to a data lake, you grant the Azure Synapse Link service access to your storage account. Ensure that you followed the [prerequisites](#prerequisites) of creating and configuring the Azure data lake storage account, and granting yourself an owner role on the storage account. Additionally, you grant the Power Platform Dataflows service access to your storage account. More information: [Self-service data prep with dataflows](self-service-data-prep-with-dataflows.md).  

5. Add the tables you want to export, and then select **Save**. Only tables with change tracking enabled can be exported. More information: [Enable change tracking](/dynamics365/customer-engagement/admin/enable-change-tracking-control-data-synchronization).

    ![Add tables.](media/add-tables.png "Add tables")

You can follow the steps above to create a link from one Dataverse environment to multiple Azure Synapse Analytics workspaces and Azure data lakes in your Azure subscription by adding an Azure data lake as a linked service on a Synapse workspace. Similarly, you could create a link from multiple Dataverse environments to the same Azure Synapse Analytics workspace and Azure data lake, all within the same tenant.

> [!NOTE]
> The data exported by Azure Synapse Link service is encrypted at rest in Azure Data Lake Storage Gen2. Additionally, transient data in the blob storage is also encrypted at rest. Encryption in Azure Data Lake Storage Gen2 helps you protect your data, implement enterprise security policies, and meet regulatory compliance requirements. More information: [Azure Data Encryption-at-Rest]( /azure/security/fundamentals/encryption-atrest)
>
> Currently, you can't provide public IPs for the Azure Synapse Link for Dataverse service that can be used in **Azure Data Lake firewall settings**. Public IP network rules have no effect on requests originating from the same Azure region as the storage account. Services deployed in the same region as the storage account use private Azure IP addresses for communication. Thus, you can't restrict access to specific Azure services based on their public outbound IP address range.
More information: [Configure Azure Storage firewalls and virtual networks]( /azure/storage/common/storage-network-security)

## Manage table data to the Synapse workspace

After you have set up the Azure Synapse Link, you can manage the tables that are exported in one of two ways:

- On the Power Apps maker portal **Azure Synapse Link** area, select **Manage tables** on the command bar to add or remove one or more linked tables.
- On the Power Apps maker portal **Tables** area, select **…** next to a table, and then select the linked data lake where you want to export table data.

   ![Select a table for export.](media/select-entity-export.png "Select a table for export")

## Monitor your Azure Synapse Link

After you have set up the Azure Synapse Link, you can monitor the Azure Synapse Link under the **Tables** tab.

- There will be a list of tables that are a part of the selected Azure Synapse Link.
- There are different stages the sync status will circulate through. **NotStarted** indicates that the table is waiting to be synced. Once the table initial sync has been **Completed**, there will be a post processing stage where incremental updates will not take place. This may take several hours depending on the size of your data. As the incremental updates start taking place, the date for the last sync will be regularly updated.
- The **Count** column shows the number of changes to the data. It does not show the total number of rows to the data.
- The  **Append only** and **Partition strategy** columns show the usage of difference advanced configurations.

## Unlinking an Azure Synapse Link

1. Select the desired Azure Synapse Link to unlink.

2. Select **Unlink data lake** from the command bar.

3. To delete both the data lake file system as well as the Synapse Database, select **Delete data lake file system**.

4. Select **Yes**, and allow a few minutes for everything to be unlinked and deleted.

## Relinking an Azure Synapse Link

If you deleted the file system when unlinking, follow the steps above to relink the same Synapse workspace and data lake. If you did not delete the file system when unlinking, you must clear the data to relink:

1. Navigate the Azure Synapse Analytics.

2. Select the **...** for the unlinked database and select **New notebook** > **Empty notebook**.

3. Attach the notebook to an Apache Spark pool by selecting a pool from the drop down menu. If you do not have an Apache Spark pool, select **Manage pools** to create one.

4. Enter the following script, replace **\<DATABASE_NAME\>** with the name of the database to unlink, and run the notebook.

```SQL
    %%sqls
    DROP DATABASE <DATABASE_NAME> CASCADE
```

5. After running the notebook, refresh the database list from the left panel. If the database still exists, try right clicking on the database and selecting **Delete**.

6. Navigate to Power Apps, and relink the Synapse workspace and data lake.

## View your data in Azure Synapse Analytics

1. Select the desired Azure Synapse Link and select the **Go to Azure Synapse Analytics workspace** from the top panel.

2. Expand **Databases**, and then select dataverse-*environmentName*-*organizationUniqueName* and expand **Tables**.

All of the exported Dataverse tables will be listed and available for analysis.

### What's next?

After successfully using the Azure Synapse Link for Dataverse service, discover how you can analyze and consume your data with **Discover Hub**. To access **Discover Hub**, go to **Power Apps** > **Azure Synapse Link**. Select your linked service and then select the **Discover Hub** tab. Here you can find recommended tools and curated documentation to help you get the most value out of your data.
![Discover Hub.](media/discover-hub.png "Discover Hub")

### See also

[Configure Azure Synapse Link for Dataverse with your Azure Data Lake](./azure-synapse-link-data-lake.md)

[Azure Synapse Link for Dataverse Advanced Configuration](./azure-synapse-link-advanced-configuration.md)

[Azure Synapse Link FAQ](export-data-lake-faq.yml)

[Blog: Announcing Azure Synapse Link for Dataverse](https://aka.ms/synapse-dataverse)

[!INCLUDE[footer-include](../../includes/footer-banner.md)]
