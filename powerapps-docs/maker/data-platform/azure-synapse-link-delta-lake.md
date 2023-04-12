---
title: Export Microsoft Dataverse data in Delta Lake format
description: Use Azure Synapse Link to export your Microsoft Dataverse data to Azure Synapse
Analytics in Delta Lake format to explore your data and accelerate time to insight.
author: JasonHQX
ms.author: jasonhuang
ms.reviewer: matp
ms.service: powerapps
ms.topic: how-to
ms.date: 04/11/2023
ms.custom: template-how-to
---
# Export Dataverse data in Delta Lake format (preview)

[!INCLUDE [cc-beta-prerelease-disclaimer](../../../../../../repos/powerapps-docs-pr/powerapps-docs/includes/cc-beta-prerelease-disclaimer.md)]

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
> - For the Dataverse configuration, append-only is enabled by default to export CSV data in `appendonly`
mode. But the delta lake table will have an in-place update structure because the delta lake conversion comes with a periodic merge process.
> - There are no costs incurred to the creation of Spark pools. Charges are only incurred once a Spark job
is executed on the target Spark pool and the Spark instance is instantiated on demand. These costs
are related to the usage of Azure Synapse workspace Spark and are billed monthly. The cost of
conducting Spark computing mainly depends on the time interval for incremental update and the
data volumes. More information: https://azure.microsoft.com/en-us/pricing/details/synapseanalytics/
> - It's important to take these additional costs into consideration when deciding to use this feature as
they are not optional and must be paid in order to continue using this feature.
> - The [recommended Spark Pool configuration](#recommended-spark-pool-configuration) will be just as a bootstrap step for average use cases. If you see issues during the sync, we'll reach out to you to change the configuration.

Delta Lake is an open-source project that enables building a lakehouse architecture on top of data lakes. Delta Lake provides ACID (atomicity, consistency, isolation, and durability) transactions, scalable metadata handling, and unifies streaming and batch data processing on top of existing data lakes. Azure Synapse Analytics is compatible with Linux Foundation Delta Lake. The current version of Delta Lake included with Azure Synapse has language support for Scala, PySpark, and .NET. More information: [What is Delta Lake?](/azure/synapse-analytics/spark/apache-spark-what-is-delta-lake)

Apache Parquet is the baseline format for Delta Lake, enabling you to leverage the efficient compression and encoding schemes that are native to the format. Parquet file format uses column-wise compression. It is efficient and saves storage space. Queries that fetch specific column values need not read the entire row data thus improving performance. Therefore, serverless SQL pool needs less time and fewer storage requests to read the data.

## Prerequisites

- Azure Synapse Link for Dataverse. This guide assumes that you have already met the
prerequisites to create an Azure Synapse Link with a Synapse workspace. More information: [Prerequisites](azure-synapse-link-synapse.md#prerequisites)
- An Azure Synapse workspace under the same Azure Active Directory (Azure AD) tenant as your Power Apps tenant. For information about how to create the workspace, go to: [Creating a Synapse workspace](/azure/synapse-analytics/get-started-create-workspace)
- A Spark Pool in the connect Azure Synapse workspace with Apache Spark Version 3.1 using this [recommended Spark Pool configuration](#recommended-spark-pool-configuration). For information about how to create a Spark Pool, go to [Create new Apache Spark pool](/azure/synapse-analytics/quickstart-create-apache-spark-pool-portal#create-new-apache-spark-pool).
- Microsoft Dynamics 365 minimum version requirement is 9.2.22082. More information: [Opt in to early access updates](/power-platform/admin/opt-in-early-access-updates#how-to-enableearly-access-updates)

### Recommended Spark Pool configuration

- Node size: small (4 vCores / 32 GB)
- Autoscale: Enabled
- Number of nodes: 5 to 10
- Automatic pausing: Enabled
- Number of minutes idle: 5
- Apache Spark: 3.1

## [Section 1 heading]

## Next steps
