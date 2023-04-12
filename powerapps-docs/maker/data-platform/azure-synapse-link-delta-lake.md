---
title: Export Microsoft Dataverse data in Delta Lake format
description: Use Azure Synapse Link to export your Microsoft Dataverse data to Azure Synapse Analytics in Delta Lake format to explore your data and accelerate time to insight.
author: JasonHQX
ms.author: jasonhuang
ms.reviewer: matp
ms.service: powerapps
ms.topic: how-to
ms.date: 04/11/2023
ms.custom: template-how-to
---
# Export Dataverse data in Delta Lake format (preview)

[!INCLUDE [cc-beta-prerelease-disclaimer](../../includes/cc-beta-prerelease-disclaimer.md)]

Use Azure Synapse Link for Dataverse to export your Microsoft Dataverse data to Azure Synapse
Analytics in Delta Lake format. Then explore your data and accelerate time to insight. This article
provides the following information and shows you how to perform the following tasks:

- Explains Delta Lake and Parquet and why you should export data in this format.
- Export your Dataverse data to your Azure Synapse Analytics workspace in Delta Lake format with the Azure Synapse Link.
- Monitor your Azure Synapse Link and data conversion.
- View your data from Azure Data Lake Storage Gen2.
- View your data from Synapse Workspace.

> [!IMPORTANT]
> - This is a preview feature.
> - For the Dataverse configuration, append-only is enabled by default to export CSV data in `appendonly` mode. But the delta lake table will have an in-place update structure because the delta lake conversion comes with a periodic merge process.
> - There are no costs incurred with the creation of Spark pools. Charges are only incurred once a Spark job is executed on the target Spark pool and the Spark instance is instantiated on demand. These costs are related to the usage of Azure Synapse workspace Spark and are billed monthly. The cost of conducting Spark computing mainly depends on the time interval for incremental update and the data volumes. More information: [Azure Synapse Analytics pricing](https://azure.microsoft.com/pricing/details/synapse-analytics/)
> - It's important to take these additional costs into consideration when deciding to use this feature as they are not optional and must be paid in order to continue using this feature.

Delta Lake is an open-source project that enables building a lakehouse architecture on top of data lakes. Delta Lake provides ACID (atomicity, consistency, isolation, and durability) transactions, scalable metadata handling, and unifies streaming and batch data processing on top of existing data lakes. Azure Synapse Analytics is compatible with Linux Foundation Delta Lake. The current version of Delta Lake included with Azure Synapse has language support for Scala, PySpark, and .NET. More information: [What is Delta Lake?](/azure/synapse-analytics/spark/apache-spark-what-is-delta-lake)

Apache Parquet is the baseline format for Delta Lake, enabling you to leverage the efficient compression and encoding schemes that are native to the format. Parquet file format uses column-wise compression. It is efficient and saves storage space. Queries that fetch specific column values need not read the entire row data thus improving performance. Therefore, serverless SQL pool needs less time and fewer storage requests to read the data.

## Prerequisites

- Azure Synapse Link for Dataverse. This guide assumes that you have already met the
prerequisites to create an Azure Synapse Link with a Synapse workspace. More information: [Prerequisites](azure-synapse-link-synapse.md#prerequisites)
- An Azure Synapse workspace under the same Azure Active Directory (Azure AD) tenant as your Power Apps tenant. For information about how to create the workspace, go to: [Creating a Synapse workspace](/azure/synapse-analytics/get-started-create-workspace)
- A Spark Pool in the connect Azure Synapse workspace with Apache Spark Version 3.1 using this [recommended Spark Pool configuration](#recommended-spark-pool-configuration). For information about how to create a Spark Pool, go to [Create new Apache Spark pool](/azure/synapse-analytics/quickstart-create-apache-spark-pool-portal#create-new-apache-spark-pool).
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
1. On the left navigation pane, select **Azure Synapse Link**, and then on the command bar. [!INCLUDE [left-navigation-pane](../../includes/left-navigation-pane.md)]
1. Select **+ New link**, and then in your web browsers address bar, append `?athena.deltaLake=true` to the web address that ends with `exporttodatalake`.
1. Select **Connect to your Azure Synapse Analytics workspace**, and then select the **Subscription**, **Resource group**, and **Workspace name**.
1. Select **Use Spark pool for processing**, and then select the pre-created **Spark pool** and **Storage account**.
   :::image type="content" source="media/synapse-link-usesparkpool.png" alt-text="Azure Synapse Link for Dataverse configuration that includes spark pool.":::

1. Select **Next**.
1. Add the tables you want to export, and then select **Advanced**.
1. Optionally, select **Show advanced configuration settings** and enter the time interval, in minutes, for how often the incremental updates should be captured, 
1. Select **Save**.

## Monitor your Azure Synapse Link and data conversion

1. Select the Azure Synapse Link you want, and then select **Go to Azure Synapse Analytics
workspace** on the command bar.
1. Select **Monitor** > **Apache Spark applications**. More information: [Use Synapse Studio to monitor your Apache Spark applications](/azure/synapse-analytics/monitoring/apache-spark-applications)

## View your data from Synapse workspace

1. Select the Azure Synapse Link you want, and then select **Go to Azure Synapse Analytics workspace** on the command bar.
1. Expand **Lake Databases** on the left pane, select **dataverse-***environmentNameorganizationUniqueName*,
and then expand **Tables**. All Parquet tables are listed and available for analysis with the naming convention
*DataverseTableName.* **(Non_partitioned Table)**.

## View your data from Azure Data Lake Storage Gen2

1. Select the Azure Synapse Link you want, and then select **Go to Azure data lake** on the command
bar.
1. Select the **Containers** under **Data Storage**.
1. Select **dataverse-* **environmentName-organizationUniqueName*. All parquet files are stored in the
**deltalake** folder.

## See also

[What is Azure Synapse Link for Dataverse?](export-to-data-lake.md)