---
title: "Azure Synapse Link | MicrosoftDocs"
description: "Learn how to export table data to an Azure Synapse Analytics and Azure Data Lake in Power Apps"
ms.custom: ""
ms.date: 02/10/2021
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
contributors:
  - sama-zaki
---

# Export table data to Azure Synapse Analytics and Azure Data Lake Storage Gen2

[!INCLUDE[cc-data-platform-banner](../../includes/cc-data-platform-banner.md)]

> [!NOTE]
> Azure Synapse Link for Dataverse was formerly known as Export to data lake. The service was renamed effective June 2021 and will continue to export to data to the data lake as well as Azure Synapse Analytics.

The Azure Synapse Link for Dataverse is a pipeline to continuously export data from

-	Microsoft Dataverse to Azure Synapse Analytics
- Microsoft Dataverse to Azure Data Lake Storage Gen2

The Azure Synapse Link for Dataverse is a service designed for enterprise big data analytics by delivering scalable high availability with disaster recovery capabilities. Data is stored in the Common Data Model format, which provides semantic consistency across apps and deployments.

![Azure Synapse Link overview](media/azure-synapse-link-overview.png "Azure Synapse Link overview")

The Azure Synapse Link for Dataverse provides these features:

- Linking or unlinking the Dataverse environment to Azure Synapse Analytics and/or Azure Data Lake Storage Gen2 in your Azure Subscription.
- Continuous replication of tables to Azure Synapse Analytics and/or Azure Data Lake Storage Gen2 in your Azure Subscription.
- Initial write, followed by incremental writes for data and metadata.
- Replication of both standard and custom tables.
- Replication of create, update, and delete (CUD) transactions.
- Continuous snapshot updates for large analytics scenarios.
- Facilitated metadata discovery and interoperability between data producers and consumers such as Azure Synapse Analytics, Power BI, Azure Data Factory, Azure Databricks, and Azure Machine Learning.

## How data and metadata are exported

The Azure Synapse Link for Dataverse service supports initial and incremental writes for table data and metadata. Any data or metadata changes in Dataverse are automatically pushed to the Azure Synapse metastore and Azure Data Lake, depending on the configuration, without any additional action. This is a push, rather than pull, operation. Changes are pushed to the destination without you needing to set up refresh intervals.

Both standard and custom tables can be exported. Notice that the change tracking table attribute in Dataverse is used to keep the data synchronized in an efficient manner by detecting what data has changed since it was initially extracted or last synchronized.

All create, update, and delete operations are exported from Dataverse to the data lake. For example, when a user deletes an Account table row in Dataverse, the transaction is replicated in the destination location.

## When to use Azure Synapse Analytics as the Destination for Dataverse Data

Azure Synapse Analytics is a limitless analytics service that brings together data integration, enterprise data warehousing, and big data analytics. It gives you the freedom to query data on your terms, using either serverless or dedicated resources—at scale. It also allows you to build analytics solutions on top of the Apache Spark engine. With Azure Synapse you can ingest, explore, prepare, manage, and serve data for immediate business intelligence and machine learning needs all from a single service.

## When to use Azure Data Lake Storage Gen2 as the Destination for Dataverse Data

Azure Data Lake is a storage solution that allows you to process data on demand, scale instantly, and only pay per job. It provides enterprise-grade security, auditing and support. Azure Data Lake is a great landing page for your Dataverse data before being utilized in another service or application. It gives you the flexibility to utilize your data in various forms and ways.

### See also

[Analyze exported data with Power BI](./export-to-data-lake-data-powerbi.md)

[Ingest exported data with Azure Data Factory](./export-to-data-lake-data-adf.md)

[Export to data lake FAQ](export-data-lake-faq.yml)

[Blog: Exporting CDS data to Azure Data Lake](https://powerapps.microsoft.com/blog/exporting-cds-data-to-azure-data-lake-preview/)

[!INCLUDE[footer-include](../../includes/footer-banner.md)]
