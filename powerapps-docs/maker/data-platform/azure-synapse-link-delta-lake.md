---
title: Export Microsoft Dataverse data in Delta Lake format
description: Use Azure Synapse Link to export your Microsoft Dataverse data to Azure Synapse Analytics in Delta Lake format to explore your data and accelerate time to insight.
author: JasonHQX
ms.author: jasonhuang
ms.reviewer: matp
ms.service: powerapps
ms.topic: how-to
ms.date: 06/26/2023
ms.custom: template-how-to
---
# Export Dataverse data in Delta Lake format

Use Azure Synapse Link for Dataverse to export your Microsoft Dataverse data to Azure Synapse
Analytics in Delta Lake format. Then explore your data and accelerate time to insight. This article
provides the following information and shows you how to perform the following tasks:

- Explains Delta Lake and Parquet and why you should export data in this format.
- Export your Dataverse data to your Azure Synapse Analytics workspace in Delta Lake format with the Azure Synapse Link.
- Monitor your Azure Synapse Link and data conversion.
- View your data from Azure Data Lake Storage Gen2.
- View your data from Synapse Workspace.

> [!IMPORTANT]
> - For the Dataverse configuration, append-only is enabled by default to export CSV data in `appendonly` mode. But the delta lake table will have an in-place update structure because the delta lake conversion comes with a periodic merge process.
> - There are no costs incurred with the creation of Spark pools. Charges are only incurred once a Spark job is executed on the target Spark pool and the Spark instance is instantiated on demand. These costs are related to the usage of Azure Synapse workspace Spark and are billed monthly. The cost of conducting Spark computing mainly depends on the time interval for incremental update and the data volumes. More information: [Azure Synapse Analytics pricing](https://azure.microsoft.com/pricing/details/synapse-analytics/)
> - It's important to take these additional costs into consideration when deciding to use this feature as they are not optional and must be paid in order to continue using this feature.

## What is Delta Lake?

Delta Lake is an open-source project that enables building a lakehouse architecture on top of data lakes. Delta Lake provides ACID (atomicity, consistency, isolation, and durability) transactions, scalable metadata handling, and unifies streaming and batch data processing on top of existing data lakes. Azure Synapse Analytics is compatible with Linux Foundation Delta Lake. The current version of Delta Lake included with Azure Synapse has language support for Scala, PySpark, and .NET. More information: [What is Delta Lake?](/azure/synapse-analytics/spark/apache-spark-what-is-delta-lake). You can also learn more from the [Introduction to Delta Tables video](https://www.youtube.com/watch?v=B_wyRXlLKok).

Apache Parquet is the baseline format for Delta Lake, enabling you to leverage the efficient compression and encoding schemes that are native to the format. Parquet file format uses column-wise compression. It's efficient and saves storage space. Queries that fetch specific column values need not read the entire row data thus improving performance. Therefore, serverless SQL pool needs less time and fewer storage requests to read the data.

## Why use Delta Lake?

- **Scalability**: Delta Lake is built on top of Open-source Apache license, which is designed to meet industry standards for handling large-scale data processing workloads.
- **Reliability**: Delta Lake provides ACID transactions, ensuring data consistency and reliability even in the face of failures or concurrent access.
- **Performance**: Delta Lake leverages the columnar storage format of Parquet, providing better compression and encoding techniques, which can lead to improved query performance compared to query CSV files.
- **Cost-effective**: The Delta Lake file format is a highly compressed data storage technology that offers significant potential storage savings for businesses. This format is specifically designed to optimize data processing and potentially reduce the total amount of data processed or running time required for on-demand computing.
- **Data protection compliance**: Delta Lake with Synapse Link provides tools and features including soft-delete and hard-delete to comply various data privacy regulations, including General Data Protection Regulation (GDPR).

## How Delta Lake works with Synapse Link for Dataverse?

When setting up an Azure Synapse Link for Dataverse, you can enable the **export to Delta Lake** feature and connect with a Synapse workspace and Spark pool. Synapse Link exports the selected Dataverse tables in CSV format at designated time intervals, processing them through a Delta Lake conversion Spark job. Upon the completion of this conversion process, CSV data is cleaned up for storage saving. Additionally, a series of maintenance jobs are scheduled to run on a daily basis, automatically performing compaction and vacuuming processes to merge and clean up data files to further optimize storage and improve query performance.

## Prerequisites

- Dataverse: You must have the Dataverse **system administrator** security role. Additionally, tables you want to export via Synapse Link must have the **Track changes** property enabled. More information: [Advanced options](create-edit-entities-portal.md#advanced-options)
- Azure Data Lake Storage Gen2: You must have an Azure Data Lake Storage Gen2 account and **Owner** and **Storage Blob Data Contributor** role access. Your storage account must enable **Hierarchical namespace** and **public network access** for both initial setup and delta sync. **Allow storage account key access** is required only for the initial setup.  
- Synapse workspace: You must have a Synapse workspace and **Owner** role in access control(IAM) and the **Synapse Administrator** role access within the Synapse Studio. The Synapse workspace must be in the same region as your Azure Data Lake Storage Gen2 account. The storage account must be added as a linked service within the Synapse Studio. To create a Synapse workspace, go to [Creating a Synapse workspace](/azure/synapse-analytics/get-started-create-workspace).
- A Spark Pool in the connected Azure Synapse workspace with **Apache Spark Version 3.1** using this [recommended Spark Pool configuration](#recommended-spark-pool-configuration). For information about how to create a Spark Pool, go to [Create new Apache Spark pool](/azure/synapse-analytics/quickstart-create-apache-spark-pool-portal#create-new-apache-spark-pool).
- The Microsoft Dynamics 365 minimum version requirement to use this feature is 9.2.22082. More information: [Opt in to early access updates](/power-platform/admin/opt-in-early-access-updates#how-to-enableearly-access-updates)

### Recommended Spark Pool configuration

This configuration can be considered a bootstrap step for average use cases.

- Node size: small (4 vCores / 32 GB)
- Autoscale: Enabled
- Number of nodes: 5 to 10
- Automatic pausing: Enabled
- Number of minutes idle: 5
- Apache Spark: 3.1

## Connect Dataverse to Synapse workspace and export data in Delta Lake format

1. Sign into [Power Apps](https://make.powerapps.com/?utm_source=padocs&utm_medium=linkinadoc&utm_campaign=referralsfromdoc) and select the environment you want.
1. On the left navigation pane, select **Azure Synapse Link**. [!INCLUDE [left-navigation-pane](../../includes/left-navigation-pane.md)]
1. On the command bar select **+ New link**
1. Select **Connect to your Azure Synapse Analytics workspace**, and then select the **Subscription**, **Resource group**, and **Workspace name**.
1. Select **Use Spark pool for processing**, and then select the pre-created **Spark pool** and **Storage account**.
   :::image type="content" source="media/synapse-link-usesparkpool.png" alt-text="Azure Synapse Link for Dataverse configuration that includes spark pool.":::

1. Select **Next**.
1. Add the tables you want to export, and then select **Advanced**.
1. Optionally, select **Show advanced configuration settings** and enter the time interval, in minutes, for how often the incremental updates should be captured.
1. Select **Save**.

## Monitor your Azure Synapse Link and data conversion

1. Select the Azure Synapse Link you want, and then select **Go to Azure Synapse Analytics workspace** on the command bar.
1. Select **Monitor** > **Apache Spark applications**. More information: [Use Synapse Studio to monitor your Apache Spark applications](/azure/synapse-analytics/monitoring/apache-spark-applications)

## View your data from Synapse workspace

1. Select the Azure Synapse link you want, and then select **Go to Azure Synapse Analytics workspace** on the command bar.
1. Expand **Lake Databases** on the left pane, select **dataverse-***environmentNameorganizationUniqueName*,
and then expand **Tables**. All Parquet tables are listed and available for analysis with the naming convention
*DataverseTableName.* **(Non_partitioned Table)**.

## View your data from Azure Data Lake Storage Gen2

1. Select the Azure Synapse link you want, and then select **Go to Azure data lake** on the command
bar.
1. Select the **Containers** under **Data Storage**.
1. Select **dataverse-* **environmentName-organizationUniqueName*. All parquet files are stored in the
**deltalake** folder.

## See also

[What is Azure Synapse Link for Dataverse?](export-to-data-lake.md)
