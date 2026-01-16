---
title: Export Microsoft Dataverse data in Delta Lake format
description: Use Azure Synapse Link to export your Microsoft Dataverse data to Azure Synapse Analytics in Delta Lake format to explore your data and accelerate time to insight.
author: JasonHQX
ms.author: jasonhuang
ms.reviewer: matp
ms.service: powerapps
ms.topic: how-to
ms.subservice: dataverse-maker
ms.date: 05/13/2025
ms.custom: template-how-to
---
# Export Dataverse data in Delta Lake format

Use Azure Synapse Link for Dataverse to export your Microsoft Dataverse data in Delta Lake format. Delta Lake is the native format for Microsoft Fabric as well as many other tools like Azure Databricks. Exporting data in Delta lake format directly from Dataverse eliminates the need to have a separate Delta Lake conversion processes on your own and accelerates time to insight. This article provides information about this feature and shows you how to perform the following tasks:

- Explains Delta Lake and Parquet and why you should export data in this format.
- Export your Dataverse data to your Azure Synapse Analytics workspace in Delta Lake format with the Azure Synapse Link.
- Monitor your Azure Synapse Link and data conversion.
- View your data from Azure Data Lake Storage Gen2.
- View your data from Synapse Workspace.
- View your data in Microsoft Fabric.

## What is Delta Lake?

Delta Lake is an open-source project that enables building a lakehouse architecture on top of data lakes. Delta Lake provides ACID (atomicity, consistency, isolation, and durability) transactions, scalable metadata handling, and unifies streaming and batch data processing on top of existing data lakes. Azure Synapse Analytics is compatible with Linux Foundation Delta Lake. The current version of Delta Lake included with Azure Synapse has language support for Scala, PySpark, and .NET. More information: [What is Delta Lake?](/azure/synapse-analytics/spark/apache-spark-what-is-delta-lake). You can also learn more from the [Introduction to Delta Tables video](https://www.youtube.com/watch?v=B_wyRXlLKok).

Apache Parquet is the baseline format for Delta Lake, enabling you to leverage the efficient compression and encoding schemes that are native to the format. Parquet file format uses column-wise compression. It's efficient and saves storage space. Queries that fetch specific column values need not read the entire row data thus improving performance. Therefore, serverless SQL pool needs less time and fewer storage requests to read the data.

## Why use Delta Lake?

- **Scalability**: Delta Lake is built on top of Open-source Apache license, which is designed to meet industry standards for handling large-scale data processing workloads.
- **Reliability**: Delta Lake provides ACID transactions, ensuring data consistency and reliability even in the face of failures or concurrent access.
- **Performance**: Delta Lake leverages the columnar storage format of Parquet, providing better compression and encoding techniques, which can lead to improved query performance compared to query CSV files.
- **Cost-effective**: The Delta Lake file format is a highly compressed data storage technology that offers significant potential storage savings for businesses. This format is specifically designed to optimize data processing and potentially reduce the total amount of data processed or running time required for on-demand computing.
- **Data protection compliance**: Delta Lake with Azure Synapse Link provides tools and features including soft-delete and hard-delete to comply various data privacy regulations, including General Data Protection Regulation (GDPR).

## How Delta Lake works with Azure Synapse Link for Dataverse?

When setting up an Azure Synapse Link for Dataverse, you can enable the **export to Delta Lake** feature and connect with a Synapse workspace and Spark pool. Azure Synapse Link exports the selected Dataverse tables in CSV format at designated time intervals, processing them through a Delta Lake conversion Spark job. Upon the completion of this conversion process, CSV data is cleaned up for storage saving. Additionally, a series of maintenance jobs are scheduled to run on a daily basis, automatically performing compaction and vacuuming processes to merge and clean up data files to further optimize storage and improve query performance.

> [!IMPORTANT]
>
> - If you're upgrading from CSV to Delta Lake with existing custom views, we recommend updating the script to replace all **partitioned** tables to **non_partitioned.** Do this by looking for instances of `_partitioned` and replace them with an empty string.
> - For the Dataverse configuration, append-only is enabled by default to export CSV data in `appendonly` mode. The Delta Lake table will have an in-place update structure because the Delta Lake conversion comes with a periodic merge process.
> - You need to provision a Spark pool (compute resources) in your own Azure subscription for Delta conversion. This Spark pool is used to perform periodic Delta conversions based on the time interval chosen by you. 
> - There are no costs incurred with the creation of Spark pools. Charges are only incurred once a Spark job is executed on the target Spark pool and the Spark instance is instantiated on demand. These costs are related to the usage of Azure Synapse workspace Spark and are billed monthly. The cost of conducting Spark computing mainly depends on the time interval for incremental update and the data volumes. More information: [Azure Synapse Analytics pricing](https://azure.microsoft.com/pricing/details/synapse-analytics/)
> - You need to create a Spark pool with the current version (see the version table in [In-place upgrade from previous versions](#in-place-upgrade-from-previous-versions)). If you're using a previous Spark version, perform an in-place upgrade for your existing profiles. More information: [In-place upgrade from previous versions](#in-place-upgrade-from-previous-versions)

> [!NOTE]
> The Azure Synapse Link status in Power Apps (make.powerapps.com) reflects the Delta Lake conversion state:
> - `Count` shows the number of records in the Delta Lake table.
> - `Last synchronized on` Datetime represents the last successful conversion timestamp.
> - `Sync status` is shown as **active** once the data sync and Delta Lake conversion completes, indicating that the data is ready for consumption.

## Prerequisites

- Dataverse: You must have the Dataverse **system administrator** security role. Additionally, tables you want to export via Azure Synapse Link must have the **Track changes** property enabled. More information: [Advanced options](create-edit-entities-portal.md#advanced-options)
- Azure Data Lake Storage Gen2: You must have an Azure Data Lake Storage Gen2 account and **Owner** and **Storage Blob Data Contributor** role access. Your storage account must enable **Hierarchical namespace** and **public network access** for both initial setup and delta sync. **Allow storage account key access** is required only for the initial setup.  
- Synapse workspace: You must have a Synapse workspace and **Owner** role in access control(IAM) and the **Synapse Administrator** role access within the Synapse Studio. The Synapse workspace must be in the same region as your Azure Data Lake Storage Gen2 account. The storage account must be added as a linked service within the Synapse Studio. To create a Synapse workspace, go to [Creating a Synapse workspace](/azure/synapse-analytics/get-started-create-workspace).
- An Apache Spark pool in the connected Azure Synapse workspace with the current Apache Spark version (see [version requirements](#current-versions-and-requirements)) using this [recommended Spark Pool configuration](#recommended-spark-pool-configuration). For information about how to create a Spark Pool, go to [Create new Apache Spark pool](/azure/synapse-analytics/quickstart-create-apache-spark-pool-portal#create-new-apache-spark-pool).
- The Microsoft Dynamics 365 minimum version requirement to use this feature is 9.2.22082. More information: [Opt in to early access updates](/power-platform/admin/opt-in-early-access-updates#how-to-enableearly-access-updates)

### Recommended Spark Pool configuration

This configuration can be considered a bootstrap step for average use cases.

- Node size: small (4 vCores / 32 GB)
- Autoscale: Enabled
- Number of nodes: 3 to 10 (or 20 if needed. <sup>1</sup>More information below.)  
- Automatic pausing: Enabled
- Number of minutes idle: 5
- Apache Spark: 3.5 (see [version requirements](#current-versions-and-requirements) for latest)
- Dynamically allocate executors: Enabled
- Default number of executors: 1 to 9

> [!IMPORTANT]
>
> - Use the Spark pool exclusively for Delta Lake conversation operation with Synapse Link for Dataverse. For optimal reliability and performance, avoid running other Spark jobs using the same Spark pool.
> - You might need to increase the number of nodes of the Spark pool if you expect a large number of rows to be processed. If the size of the Spark pool is insufficient, Delta conversion jobs might fail
> - The same Spark pool is used by the system to run a nightly job that compacts Delta files in the lake between 11 PM and 6 AM local time. The system determines the night time to run this job based on the location of your Dataverse environment. You can't provide a specific time window. This option reduces the size of Delta files by merging files known as "compaction." In rare cases, this job might interfere with the incremental conversion job. You can increase the number of nodes to 20 in case you notice these failures.
> - You're only charged for the spark pool nodes actually utilized. Increasing the number of nodes might not result in higher charges.

## Connect Dataverse to Synapse workspace and export data in Delta Lake format

1. Sign into [Power Apps](https://make.powerapps.com/?utm_source=padocs&utm_medium=linkinadoc&utm_campaign=referralsfromdoc) and select the environment you want.
1. On the left navigation pane, select **Azure Synapse Link**. [!INCLUDE [left-navigation-pane](../../includes/left-navigation-pane.md)]
1. On the command bar, select **+ New link**
1. Select **Connect to your Azure Synapse Analytics workspace**, and then select the **Subscription**, **Resource group**, and **Workspace name**.
1. Select **Use Spark pool for processing**, and then select the precreated **Spark pool** and **Storage account**.
   :::image type="content" source="media/synapse-link-usesparkpool.png" alt-text="Azure Synapse Link for Dataverse configuration that includes spark pool.":::

1. Select **Next**.
1. Add the tables you want to export, and then select **Advanced**.
1. Optionally, select **Show advanced configuration settings** and enter the time interval, in minutes, for how often the incremental updates should be captured.
1. Select **Save**.

## Monitor your Azure Synapse Link and data conversion

1. Select the Azure Synapse Link you want, and then select **Go to Azure Synapse Analytics workspace** on the command bar.
1. Select **Monitor** > **Apache Spark applications**. More information: [Use Synapse Studio to monitor your Apache Spark applications](/azure/synapse-analytics/monitoring/apache-spark-applications)

## View your data from Synapse workspace

1. Select the Azure Synapse Link you want, and then select **Go to Azure Synapse Analytics workspace** on the command bar.
1. Expand **Lake Databases** on the left pane, select **dataverse-***environmentNameorganizationUniqueName*,
and then expand **Tables**. All Parquet tables are listed and available for analysis with the naming convention
*DataverseTableName.* **(Non_partitioned Table)**.

> [!NOTE]
> Don't use tables with the naming convention *_partitioned*. When you choose Delta parquet as the format, tables with the *_partition* naming convention are used as staging tables and removed after they're used by the system.
>  

## View your data from Azure Data Lake Storage Gen2

1. Select the Azure Synapse Link you want, and then select **Go to Azure data lake** on the command
bar.
1. Select the **Containers** under **Data Storage**.
1. Select **dataverse-* **environmentName-organizationUniqueName*. All parquet files are stored in the
**deltalake** folder.

## In-place upgrade from previous versions

### Current versions and requirements

The following table shows the current and previous versions for Azure Synapse Link with Delta Lake. When upgrading or creating a new configuration, use the current versions listed below.

| Component | Current Version | Previous Version | Status | Reference Link |
|-----------|----------------|------------------|--------|----------------|
| Apache Spark | 3.5 | 3.4 | 3.4 retired | [Apache Spark 3.4 runtime](https://learn.microsoft.com/en-us/azure/synapse-analytics/spark/apache-spark-34-runtime) |
| Delta Lake | 3.0 | 2.4 | - | [Delta Lake compatibility](https://docs.delta.io/releases/) |

> [!IMPORTANT]
> Update this table when new versions are released. All version references in this document should use the current versions listed above.

### Upgrade from Apache Spark 3.4 to 3.5

In accordance with the Synapse runtime for Apache Spark lifecycle policy, Azure Synapse runtime for Apache Spark 3.4 is retired. After the end of support date, the retired runtimes are unavailable for new Spark pools and existing workflows with Spark 3.4 pools won't be executed while metadata will temporarily remain in the Synapse workspace. More information: [Azure Synapse Runtime for Apache Spark 3.4](https://learn.microsoft.com/en-us/azure/synapse-analytics/spark/apache-spark-34-runtime).

To ensure that your existing Synapse Link profiles continue to process data, upgrade your Synapse Link profiles using the in-place upgrade process below.

#### Prerequisites

- You must have an existing Azure Synapse Link for Dataverse Delta lake profile running with a previous Apache Spark version.
- You must create a new Synapse Spark pool with the current Spark version (see table above), **using the same or higher nodes hardware configuration within the same Synapse workspace**. For information about how to create a Spark pool, go to [Create new Apache Spark pool](/azure/synapse-analytics/quickstart-create-apache-spark-pool-portal#create-new-apache-spark-pool). This Spark pool should be created independent of your existing pool - **do not delete your current Spark pool or create the new pool with the same name**.

#### Upgrade steps

1. Sign in to Power Apps and select your preferred environment.
2. On the left navigation pane, select **Azure Synapse Link**. If the item isn't in the left navigation pane, select **…More** and then select the item you want.
3. If you're using a retired Spark version, you'll see an error message indicating that support has ended. Select the upgrade button in the ribbon to begin the upgrade process.

   :::image type="content" source="media/synapse-link-spark-34-eol-message.jpg" alt-text="Error message showing Apache Spark end of support with upgrade button in ribbon.":::

4. In the upgrade dialog, select the available Spark pool with the current version from the dropdown list.

   :::image type="content" source="media/synapse-link-spark-35-pool-selection.png.jpg" alt-text="Dropdown menu showing available Apache Spark pools for upgrade.":::

5. Select **Update** to complete the upgrade.

> [!NOTE]
>
> - The Spark pool upgrade occurs only when a new Delta lake conversion Spark job is triggered. Ensure you have at least one data change after selecting **Update**.
> - You can delete the older Spark pool after verifying that Delta conversion jobs use the new pool.

## Related articles

[What is Azure Synapse Link for Dataverse?](export-to-data-lake.md)
