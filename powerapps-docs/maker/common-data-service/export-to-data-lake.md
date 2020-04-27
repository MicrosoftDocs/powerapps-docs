---
title: "Export to data lake | MicrosoftDocs"
description: "Learn how to export entity data to an Azure data lake in Power Apps"
ms.custom: ""
ms.date: 04/27/2020
ms.reviewer: "Mattp123"
ms.service: powerapps
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
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
---

# Export entity data to Azure Data Lake Storage Gen2

The Export to Data Lake service is a pipeline to continuously export data from Common Data Service to Azure Data Lake Storage Gen2. The Export to Data Lake service is designed for enterprise big data analytics by delivering scalable high availability with disaster recovery capabilities. Data is stored in the Common Data Model format, which provides semantic consistency across apps and deployments. 

![Export to data lake overview](media/export-data-lake-overview.png "Export to Data Lake overview")

Export to Data Lake provides these features: 

- Linking or unlinking the Common Data Service environment to Data Lake Storage Gen2 in your Azure subscription. 
- Continuous replication of entities to Data Lake Storage Gen2.
- Initial write, followed by incremental writes for data and metadata. 
- Replication of both standard and custom entities. 
- Replication of create, update, and delete (CrUD) transactions. 
- Continuous snapshot updates for large analytics scenarios. 
- Facilitated metadata discovery and interoperability between data producers and consumers such as Power BI, Azure Data Factory, Azure Databricks, and Azure Machine Learning.

## How data and metadata are exported

The Export to Data Lake service supports initial and incremental writes for entity data and metadata. Any data or metadata changes in Common Data Service are automatically pushed to the data lake without any additional action. This is a push, rather than pull, operation. Changes are pushed to the destination without you needing to set up refresh intervals. 

Both standard and custom entities can be exported. Notice that the change tracking entity attribute in Common Data Service is used to keep the data synchronized in an efficient manner by detecting what data has changed since it was initially extracted or last synchronized. 

All create, update, delete operations are exported from Common Data Service to the data lake. For example, when a user deletes an Account entity record in Common Data Service, the transaction is replicated to the destination data lake.

## Prerequisites

Before you can export Common Data Service data to a data lake, you must create and configure an Azure Storage v2 (general-purpose v2) storage account. 

Follow the steps in the [Create an Azure Storage account](/azure/storage/blobs/data-lake-storage-quickstart-create-account) article, and note these requirements: 

- You must be granted an owner role on the storage account. 
- Set your storage type as **Storagev2 (general purpose v2)**. 
- The storage account must have the **Hierarchical namespace** feature enabled. 

 We recommend that you set replication to read-access geo-redundant storage (RA-GRS). More information: [Read-access geo-redundant storage](/azure/storage/common/storage-redundancy-grs#read-access-geo-redundant-storage)

>   ![Storage account properties](media/storage-account-properties.png "Storage account properties")

> [!NOTE]
> - The storage account must be created in the same Azure Active Directory (Azure AD) tenant as your Power Apps tenant.  
> - The storage account must be created in the same region as the Power Apps environment you'll use the feature in.  
> - To link the Common Data Service environment to Azure Data Lake Storage Gen2, you must be a Common Data Service administrator. 
> - Only entities that have change tracking enabled can be exported. 

## Select and export Common Data Service entity data to Azure Data Lake Storage Gen2

1. Sign in to [Power Apps](https://make.powerapps.com/?utm_source=padocs&utm_medium=linkinadoc&utm_campaign=referralsfromdoc), expand **Data**, and then select **Entities**. 
2. On the command bar, select **Export to data lake**, and then on the **Export to data lake** page, select **New link to data lake**. 
3. Select each of the following settings, and then select **Next**: 
   - **Subscription**. Select your Azure subscription. 
   - **Resource group**. Select the resource group that contains the Storage v2 (general-purpose v2) storage account.
   - **Storage account**. Select the Storage v2 (general-purpose v2) storage account to use for the export. 

    > [!NOTE]
    > As part of linking the Common Data Service environment to a data lake, you grant the Export to Data Lake service access to your storage account. Ensure that you followed the [prerequisites](#prerequisites) of creating and configuring the Azure data lake storage account, and granting yourself an owner role on the storage account. Additionally, you grant the Power Platform Dataflows service access to your storage account. More information: [Self-service data prep with dataflows](self-service-data-prep-with-dataflows.md).  

4. Select the entities that you want to export to the data lake, and then select **Save**. Only entities with change tracking enabled can be exported. More information: [Enable change tracking](/dynamics365/customer-engagement/admin/enable-change-tracking-control-data-synchronization)

   > [!div class="mx-imgBorder"] 
   > ![Select entities for export](media/export-data-lake-select-entity.png "Select entities for export")

Your Common Data Service environment is linked to the Azure Data Lake Storage Gen2 account. The file system in the Azure storage account is created with a folder for each entity selected to be replicated to the data lake. 

> [!NOTE]
> The data exported by Export to data lake service is encrypted at rest in Azure Data Lake Storage Gen2. Additionally, transient data in the blob storage is also encrypted at rest. Encryption in Azure Data Lake Storage Gen2 helps you protect your data, implement enterprise security policies, and meet regulatory compliance requirements. More information: [Azure Data Encryption-at-Rest]( /azure/security/fundamentals/encryption-atrest)

## Manage entity data to the data lake

After you've set up data export to Azure Data Lake Storage Gen2 in your subscription, you can manage the export of entity data to the data lake in one of two ways: 

- On the Power Apps maker portal **Export to data lake** area, select **Manage entities** on the command bar to add or remove one or more linked entities.
- On the Power Apps maker portal **Entities** area, select **…** next to an entity, and then select the linked data lake where you want to export entity data. 

   ![Select an entity for export](media/select-entity-export.png "Select an entity for export")

To unlink all linked entities, on the Power Apps maker portal **Export to data lake** area, select **Unlink data lake**.

## View your data in Azure Data Lake Storage Gen2

1. Sign in to [Azure](https://portal.azure.com), select the storage account, and then in the leftmost navigation pane, select **Storage Explorer**. 
2. Expand **File Systems**, and then select commondataservice-*environmentName*-org-*Id*. 

The model.json file, along with its name and version, provides a list of entities that have been exported to the data lake. The model.json file also includes the initial sync status and sync completion time. 

A folder that includes snapshot comma-delimited (CSV format) files is displayed for each entity exported to the data lake.
   > [!div class="mx-imgBorder"] 
   > ![Entity data in the data lake](media/entity-data-in-lake.png "Entity data in the data lake") 

### Continuous snapshot updates

Common Data Service data can continuously change through create, update, and delete transactions. Snapshots provide a read-only copy of data that's updated at regular intervals, in this case every hour. This ensures that at any given point, a data analytics consumer can reliably consume data in the lake.

![Continuous snapshot updates](media/snapshot-updates.png "Continuous snapshot updates")

When entities are added as part of the initial export, the entity data is written to the entity.csv files under the corresponding folders in the data lake. This is the T1 interval, where a snapshot read-only file named *entity*-T1.csv&mdash;for example, Account-T1.csv or Contacts-T1.csv&mdash;is created. Additionally, the model.json file is updated to point to these snapshot files. Opening model.json, you can view the snapshot details. 

Here's an example of an Account.csv partitioned file and snapshot folder in the data lake.

![Accounts entity snapshot](media/export-data-lake-account-snapshots.png "Accounts entity snapshot") 

Changes in Common Data Service are continuously pushed to the corresponding CSV files by using the trickle feed engine. This is the T2 interval, where another snapshot is taken. *Entity*-T2.csv&mdash;for example, Accounts-T2.csv or Contacts-T2.csv (assuming there are changes for the entity) &mdash;and model.json are updated to the new snapshot files. Any new person who views snapshot data from T2 onward is directed to the newer snapshot files. This way, the original snapshot viewer can continue to work on the older snapshot T1 files while newer viewers can read the latest updates. This is useful in scenarios that have longer-running downstream processes. 

Here's an example of the model.json file, which always points to the latest time-stamped account snapshot file. 

![Sample snapshot model.json file](media/sample-snapshot-json.png "Sample snapshot model.json file") 

## Transporting an Export to Data Lake configuration across environments

In Power Apps, solutions are used to transport apps and components from one environment to another, or to apply a set of customizations to existing apps. To make the Export to Data Lake configurations solution-aware, import the Export to Data Lake Core solution into the environment. This enables basic application lifecycle management (ALM) abilities such as distribution, and backup and restore of the Export to Data Lake configuration. 

### Import the Export to Data Lake Core solution

1.	From the Power Apps maker portal, select the environment where you want to distribute the Export to Data Lake configuration.
2.	On the leftmost navigation pane, select **Solutions**, select **Open AppSource**, search for the solution named **Export to Data Lake Core**, and then import the solution.

### Add an Export to Data Lake configuration to a solution

> [!IMPORTANT]
> Before you can add an Export to Data Lake configuration, you must install the Export to Data Lake Core solution described earlier. 

1.	From the Power Apps maker portal, select the environment where you want to distribute the Export to Data Lake configuration, and then on the leftmost navigation pane, select **Solutions**. 
2.	Select **New solution**, provide a name, select a publisher, and then specify a version number.  
3.	Open the solution you created in the previous step, select **Add existing** > **Other** > **Export to data lake config**. 
4.	Select the linked data lake configurations that you want, and then select **Add**. 
5.	In the **Solutions** area, select the solution, and then on the command bar, select **Export**. 
6.	In the **Before you export** pane, select **Publish** to publish all changes before you export, and then select **Next**. 

### Import the solution that contains the Export to Data Lake configuration

In the environment where you want to import your solution, in the Power Apps maker portal **Solutions** area, import the solution. 

#### Verify the Export to Data Lake configuration

From the Power Apps maker portal in the environment where you imported the Export to Data Lake configuration, verify that you can see your linked data lake in addition to the entities that you transported from your other environment.

> [!div class="mx-imgBorder"] 
> ![Imported Export to Data Lake entities](media/imported-export-entities.png "Imported Export to Data Lake entities") 

### See also

[Blog: Exporting CDS data to Azure Data Lake](https://powerapps.microsoft.com/blog/exporting-cds-data-to-azure-data-lake-preview/)
