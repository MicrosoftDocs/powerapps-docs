---
title: "Access Copy Dataverse data to Azure SQL | MicrosoftDocs"
description: "Learn how to copy Dataverse data to Azure SQL with a Pipeline Template."
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

# Copy Dataverse data to Azure SQL with a Pipeline Template

[!INCLUDE[cc-data-platform-banner](../../includes/cc-data-platform-banner.md)]

After exporting data from Dataverse to Azure Data Lake Storage Gen2 with Azure Synapse Link for Dataverse, you can use Azure Data Factory to create a pipeline that copies data from the data lake to Azure SQL.

> [!NOTE]
> Azure Synapse Link for Dataverse was formerly known as Export to data lake. The service was renamed effective May 2021 and will continue to export data to Azure Data Lake as well as Azure Synapse Analytics.

This article shows you how to perform the following tasks:

1. Create a pipeline from an official Microsoft template.

2. Configure the template.

3. Run the pipeline.

## Prerequisites

This section describes the prerequisites necessary to copy exported Dataverse data to Azure SQL.

- **Azure roles.** The user account that's used to sign in to Azure must be a member of the
*contributor* or *owner* role, or an *administrator* of the Azure subscription. To view the permissions that you have in the subscription, go to the [Azure portal](https://portal.azure.com/), select your username in the upper-right corner, select **...**, and then select **My permissions**. If you have access to multiple subscriptions, select the appropriate one. To create and manage child resources for Data Factory in the Azure portal&mdash;including datasets, linked services, pipelines, triggers, and integration runtimes&mdash;you must belong to the *Data Factory Contributor* role at the resource group level or above.

- **Azure Synapse Link for Dataverse.**This guide assumes that you've already exported Dataverse data by using [Azure Synapse Link for Dataverse](export-to-data-lake.md). In this example, the account table data is exported to the data lake.

- **Azure Data Factory.** This guide assumes that you've already created a data factory under the same subscription and resource group as the storage account containing the exported Dataverse data.

- **Azure SQL.** This guide assumes that you've already created an Azure SQL database under the same subscription and resource group as the storage account containing the exported Dataverse data.

## Copy Dataverse data to Azure SQL with a Pipeline Template

1. Open [Azure Data Factory](https://ms-adf.azure.com/en-us/datafactories) and select the data factory that is on the same subscription and resource group as the storage account containing your exported Dataverse data. Then select **Author** from the left panel.

2. Select **+** and add a **Pipeline from template**.

3. Search for and select the **Copy Dataverse data from Azure Data Lake to Azure SQL** template created by Microsoft.

    ![Pipeline Template SQL](media/sql-template.png "Pipeline Template SQL")

4. Input the Azure SQL database in the first entry and the Azure Data Lake Storage Gen2 account in the second entry and select **Use this template**.

    ![Configure Template SQL](media/configure-template.png "Configure Template SQL")

5. Open the data flow and select **ADLS** > **Source options**. Replace the container in the **Root location** with your container containing the exported Dataverse data. Replace the **entity** with the Dataverse table name you wish to copy to Azure SQL database.

    ![Configure Source Options](media/source-options-template.png "Configure Source Options")

6. Navigate to the pipeline and run it. Optionally, **Add trigger** to copy the data at specific time intervals.

### See also

[Azure Synapse Link for Dataverse](./export-to-data-lake.md)

[!INCLUDE[footer-include](../../includes/footer-banner.md)]
