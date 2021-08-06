---
title: "Visualize Azure Synapse Link for Dataverse data with Power BI | MicrosoftDocs"
description: "Learn how to visualize exported Dataverse table data with Power BI"
ms.custom: ""
ms.date: 08/06/2021
ms.reviewer: "Mattp123"
ms.service: powerapps
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "how-to"
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

# Visualize Azure Synapse Link for Dataverse data with Power BI

[!INCLUDE[cc-data-platform-banner](../../includes/cc-data-platform-banner.md)]

You can use the Azure Synapse Link to connect your Microsoft Dataverse data to Azure Synapse Analytics to explore your data and accelerate time to insight. This article shows you how to generate a Power BI report by connecting to the serverless SQL endpoint from your Azure Synapse Analytics workspace.

> [!NOTE]
>
> - Azure Synapse Link for Microsoft Dataverse was formerly known as Export to data lake. The service was renamed effective May 2021 and will continue to export data to Azure Data Lake as well as Azure Synapse Analytics.
> - This feature is still in preview and preview features are are not complete, but are made available on a “preview” basis so customers can get early access and provide feedback. Preview features may have limited or restricted functionality, are not meant for production use, and may be available only in selected geographic areas.

## Prerequisites

This section describes the prerequisites necessary to access Dataverse choices with Power BI after using the Azure Synapse Link for Dataverse service.

- **Power BI Desktop**. [Get it now](https://powerbi.microsoft.com/downloads/)

- **Azure Synapse Link for Dataverse:** This guide assumes that you have already exported data from Dataverse by using the [Azure Synapse Link for Dataverse](export-to-data-lake.md).

- **Storage Account Access.** You must be granted one of the following roles for the storage account: Storage Blob Data Reader, Storage Blob Data Contributor, or Storage Blob Data Owner.

## Transform your data with an Apache Spark notebook

1. In your Synapse workspace, expand **Databases**, select your Dataverse container. Your exported tables are displayed under the **Tables** directory on the left sidebar.

2. Right-click the desired table and select **New notebook** > **Load to DataFrame**.

    ![Load to DataFrame.](media/load-to-dataframe.png "Load to DataFrame")

3. Attach the notebook to an Apache Spark pool by selecting a pool from the drop down menu. If you do not have an Apache Spark pool, select **Manage pools** to create one.

    ![Attach Spark pool.](media/attach-pool.png "Attach Spark pool")

4. Add code cells to transform your data. Run individual cells by selecting the play button at the left of each cell or run all the cells in succession by selecting **Run all** from the top bar.

    ![Spark notebook.](media/spark-notebook.png "Spark notebook")

### See also

[Blog: Announcing Azure Synapse Link for Dataverse](https://aka.ms/synapse-dataverse)

[!INCLUDE[footer-include](../../includes/footer-banner.md)]
