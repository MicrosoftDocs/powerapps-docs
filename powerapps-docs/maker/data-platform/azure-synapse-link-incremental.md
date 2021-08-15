---
title: "Read the Incremental Updates of Dataverse data | MicrosoftDocs"
description: "Learn how to read the incremental updates of your Dataverse data."
ms.custom: ""
ms.date: 08/06/2021
ms.reviewer: "Mattp123"
ms.service: powerapps
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "conceptual"
applies_to: 
  - "powerapps"
author: "sama-zaki"
ms.assetid: 
ms.subservice: dataverse-maker
ms.author: "matp"
manager: "kvivek"
search.audienceType: 
  - maker
search.app: 
  - PowerApps
  - D365CE
contributors: ""
---

# Read the Incremental Updates of Dataverse data

[!INCLUDE[cc-data-platform-banner](../../includes/cc-data-platform-banner.md)]

> [!NOTE]
> Azure Synapse Link for Dataverse was formerly known as Export to data lake. The service was renamed effective May 2021 and will continue to export data to Azure Data Lake as well as Azure Synapse Analytics.

After creating a continuous pipeline of data from Dataverse to your Synapse workspace with Azure Synapse Link for Dataverse, you can read the incremental updates of a specified time interval.

> [!NOTE]
> Azure Synapse Link for Dataverse was formerly known as Export to data lake. The service was renamed effective May 2021 and will continue to export data to Azure Data Lake as well as Azure Synapse Analytics.

## Prerequisites

This section describes the prerequisites necessary to ingest exported Dataverse data with Data Factory.

### Azure Synapse Link for Dataverse

This guide assumes that you've already exported Dataverse data by using [Azure Synapse Link for Dataverse](export-to-data-lake.md). All tables must be exported with the append-only option.

## Read the Incremental Updates of your Dataverse data

1. Every Dataverse table exported with Azure Synapse Link for Dataverse contains a *SinkModifiedOn* column.

2. Maintain a pointer to the *SinkModifiedOn* column to specify the time interval in which the read the data updates.

### See also

[Azure Synapse Link for Dataverse](./export-to-data-lake.md)

[!INCLUDE[footer-include](../../includes/footer-banner.md)]
