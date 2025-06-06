---
title: "Create an Azure Synapse Link for Dataverse with Azure Data Lake in Power Apps"
description: "Learn how to export table data to Azure Data Lake Storage Gen2 in Power Apps."
ms.date: 04/29/2025
ms.reviewer: "Mattp123"
ms.topic: "how-to"
applies_to: 
  - "powerapps"
author: MilindaV2
ms.subservice: dataverse-maker
ms.author: "milindav"
search.audienceType: 
  - maker
contributors:
  - sama-zaki
---
# Create an Azure Synapse Link for Dataverse with Azure Data Lake

You can use the Azure Synapse Link to connect your Microsoft Dataverse data to Azure Data Lake Storage Gen2 to enable various analytics scenarios. This article shows you how to perform the following tasks:

1. Connect your Dataverse data to your Azure Data Lake Storage Gen2 account with the Azure Synapse Link service.
2. Manage Dataverse tables included in the Azure Synapse Link.
3. Monitor your Azure Synapse Link.
4. Unlink your Azure Synapse Link.
5. Relink your Azure Synapse Link.
6. View your data in Azure Data Lake and understand the file structure.

> [!NOTE]
> Azure Synapse Link for Dataverse was formerly known as Export to data lake. The service was renamed effective May 2021 and will continue to export data to Azure Data Lake as well as Azure Synapse Analytics.

## Prerequisites

- Azure Data Lake Storage Gen2: You must have an Azure Data Lake Storage Gen2 account and **Owner** and **Storage Blob Data Contributor** role access. Your storage account must enable **Hierarchical namespace** for both initial setup and delta sync. **Allow storage account key access** is required only for the initial setup.

> [!NOTE]
>
> - The storage account must be created in the same Microsoft Entra tenant as your Power Apps tenant.
> - To set **Enabled from selected virtual networks and IP addresses** for linked storage account to grant access from selected IP addresses, you must create an Azure Synapse Link with managed identities.[Use managed identities for Azure with your Azure data lake storage](./azure-synapse-link-msi.md) (without managed identities set up, you must enable public network access for Azure resources for both initial setup and delta sync.)
> - We strongly recommend that you enable the [soft delete feature](/azure/storage/blobs/soft-delete-container-enable?tabs=azure-portal) on the storage account selected for this purpose. Enabling soft delete enables you to recover from accidental data deletes faster.
> - You must have **Reader** role access to the resource group with the storage account.  
> - To link the environment to Azure Data Lake Storage Gen2, you must have the Dataverse system administrator security role.
> - Only tables that have change tracking enabled can be exported.
> - The creation of Azure Synapse Link profiles under a single Dataverse environment is limited to a maximum of 10.

## Connect Dataverse to Azure Data Lake Storage Gen2

1. Sign in to [Power Apps](https://make.powerapps.com/?utm_source=padocs&utm_medium=linkinadoc&utm_campaign=referralsfromdoc) and select your preferred environment.
1. On the left navigation pane, select **Azure Synapse Link**. If **Azure Synapse Link** isn't visible in the side panel pane, select **…More** and select **Discover all**. **Azure Synapse Link** is in the **Data Management** section.
1. On the command bar, select **+ New link to data lake**.
1. Select the **Subscription**, **Resource group**, and **Storage account**. Ensure that storage account meets the requirements specified in the [Prerequisites](#prerequisites) section. Select **Next**.

    > [!NOTE]
    > As part of linking the environment to a data lake, you grant the Azure Synapse Link service access to your storage account. Ensure that you followed the [prerequisites](#prerequisites) of creating and configuring the Azure data lake storage account, and granting yourself an owner role on the storage account. Additionally, you grant the Power Platform Dataflows service access to your storage account. More information: [Self-service data prep with dataflows](self-service-data-prep-with-dataflows.md).  

1. Choose the tables you want to export either by selecting them one by one or by entering a comma separated list of tables in the search box, and then select **Save**. Only tables with the **Track changes** property can be exported. More information: [Advanced options for tables](/power-apps/maker/data-platform/create-edit-entities-portal?tabs=excel#advanced-options).

   ![Select tables for export.](media/export-data-lake-select-entity.png "Select tables for export")

You can follow the steps in this article to create a link from one environment to multiple Azure data lakes in your Azure subscription. Similarly, you could create a link from multiple environments to the same Azure Data Lake, all within the same tenant.

> [!NOTE]
> The Azure Synapse Link for Dataverse service is seamlessly integrated into the Power Platform as an out-of-the-box feature. It meets the security and governance standards set for the Power Platform data storage and governance. More information: [Data storage and governance](/power-platform/admin/security/data-storage)
> 
> The data exported by Azure Synapse Link service is encrypted at transit using Transport Layer Security(TLS) 1.2 or higher and encrypted at rest in Azure Data Lake Storage Gen2. Additionally, transient data in the blob storage is also encrypted at rest. Encryption in Azure Data Lake Storage Gen2 helps you protect your data, implement enterprise security policies, and meet regulatory compliance requirements. More information: [Azure Data Encryption-at-Rest]( /azure/security/fundamentals/encryption-atrest)
>

## Manage table data to the data lake

After you set up the Azure Synapse Link, you can manage the tables that are exported in one of two ways:

- On the Power Apps maker portal **Azure Synapse Link** area, select **Manage tables** on the command bar to add or remove one or more linked tables.
- On the Power Apps maker portal **Tables** area, select **…** next to a table, and then select the linked data lake where you want to export table data.

   ![Select a table for export.](media/select-entity-export.png "Select a table for export")

## Monitor your Azure Synapse Link

After you set up the Azure Synapse Link, you can monitor the Azure Synapse Link under the **Tables** tab.

   ![Azure Synapse Link monitoring](media/monitoring.png "Azure Synapse Link monitoring")

- There will be a list of tables that are a part of the selected Azure Synapse Link.
- There are different stages the sync status circulates through. **NotStarted** indicates that the table is waiting to be synced. Once the table initial sync is **Completed**, there's a post processing stage where incremental updates won't take place. This might take several hours depending on the size of your data. As the incremental updates start taking place, the date for the last sync will be regularly updated.
- The **Count** column shows the number rows written. When **Append only** is set to **No**, this is the total number of records. When **Append Only** is set to **Yes**, this is the total number of changes.
- The  **Append only** and **Partition strategy** columns show the usage of different advanced configurations.

## Unlinking an Azure Synapse Link

1. Select the desired Azure Synapse Link to unlink.

2. Select **Unlink data lake** from the command bar.

3. To delete both the data lake file system, select **Delete data lake file system**.

4. Select **Yes**, and allow a few minutes for everything to be unlinked and deleted.

## Relinking an Azure Synapse Link

If you deleted the file system when unlinking, follow the steps above to relink the same data lake. If you didn't delete the file system when unlinking, you must clear the data to relink:

1. Go to the Azure Data Lake.

2. Delete the Dataverse container.

3. Go to Power Apps, and relink the data lake.

## View your data in Azure Data Lake Storage Gen2

1. Select the desired Azure Synapse Link, and then select **Go to Azure data lake** from the top panel.

2. Expand **File Systems**, and then select dataverse-*environmentName*-*organizationUniqueName*.

The model.json file, along with its name and version, provides a list of tables that have been exported to the data lake. The model.json file also includes the initial sync status and sync completion time.

A folder that includes snapshot comma-delimited (CSV format) files is displayed for each table exported to the data lake.
   ![Table data in the data lake.](media/entity-data-in-lake.png "Table data in the data lake")
   
## Link a Synapse workspace to an existing Azure Synapse Link profile with data lake only

1. In web browsers address bar, append `?athena.updateLake=true` to the web address that ends with **exporttodatalake**.

2. Select an existing profile from the Azure Synapse Link area, and then select extended option.

3. Select **Link to Azure Synapse Analytics Workspace** and allow a few minutes for everything to be linked.


### Continuous snapshot updates

Microsoft Dataverse data can continuously change through create, update, and delete transactions. Snapshots provide a read-only copy of data that's updated at regular intervals, in this case every hour. This ensures that at any given point, a data analytics consumer can reliably consume data in the lake.

![Continuous snapshot updates.](media/snapshot-updates.png "Continuous snapshot updates")

When tables are added as part of the initial export, the table data is written to the table.csv files under the corresponding folders in the data lake. This is the T1 interval, where a snapshot read-only file named *table*-T1.csv&mdash;for example, Account-T1.csv or Contacts-T1.csv&mdash;is created. Additionally, the model.json file is updated to point to these snapshot files. Opening model.json, you can view the snapshot details.

Here's an example of an Account.csv partitioned file and snapshot folder in the data lake.

![Accounts table snapshot.](media/export-data-lake-account-snapshots.png "Accounts table snapshot")

Changes in Dataverse are continuously pushed to the corresponding CSV files by using the trickle feed engine. This is the T2 interval, where another snapshot is taken. *table*-T2.csv&mdash;for example, Accounts-T2.csv or Contacts-T2.csv (assuming there are changes for the table) &mdash;and model.json are updated to the new snapshot files. Any new person who views snapshot data from T2 onward is directed to the newer snapshot files. This way, the original snapshot viewer can continue to work on the older snapshot T1 files while newer viewers can read the latest updates. This is useful in scenarios that have longer-running downstream processes.

> [!NOTE]
> A new snapshot file is created only if there's a data update.
> Only the latest five snapshot files are retained. Stagnant data is automatically removed from your Azure Data Lake Storage Gen 2 account.

Here's an example of the model.json file, which always points to the latest time-stamped account snapshot file.

![Sample snapshot model.json file.](media/sample-snapshot-json.png "Sample snapshot model.json file")

### What's next?

After successfully using the Azure Synapse Link for Dataverse service, discover how you can analyze and consume your data with **Discover Hub**. To access **Discover Hub**, go to **Power Apps** > **Azure Synapse Link**. Select your linked service and then select the **Discover Hub** tab. Here you can find recommended tools and curated documentation to help you get the most value out of your data.
![Discover Hub.](media/discover-hub.png "Discover Hub")

### See also

[Analyze Dataverse data in the data lake with Power BI](./export-to-data-lake-data-powerbi.md)

[Ingest Dataverse data in the data lake with Azure Data Factory](./export-to-data-lake-data-adf.md)

[Azure Synapse Link for Dataverse Advanced Configuration](./azure-synapse-link-advanced-configuration.md)

[Azure Synapse Link FAQ](export-data-lake-faq.yml)

[!INCLUDE[footer-include](../../includes/footer-banner.md)]
