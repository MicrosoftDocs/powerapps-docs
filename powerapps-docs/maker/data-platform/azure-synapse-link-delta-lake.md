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

Delta Lake is an open-source project that enables building a lakehouse architecture on top of data lakes. Delta Lake provides ACID (atomicity, consistency, isolation, and durability) transactions, scalable metadata handling, and unifies streaming and batch data processing on top of existing data lakes. Azure Synapse Analytics is compatible with Linux Foundation Delta Lake. The current version of Delta Lake included with Azure Synapse has language support for Scala, PySpark, and .NET. More information:
https://docs.microsoft.com/azure/synapse-analytics/spark/apache-spark-what-is-delta-lake

Apache Parquet is the baseline format for Delta Lake, enabling you to leverage the efficient compression and encoding schemes that are native to the format. Parquet file format uses column-wise compression. It is efficient and saves storage space. Queries that fetch specific column values need not read the entire row data thus improving performance. Therefore, Serverless SQL pool needs less time and fewer storage requests to read the data.

## Prerequisites



## [Section 1 heading]

## Next steps
