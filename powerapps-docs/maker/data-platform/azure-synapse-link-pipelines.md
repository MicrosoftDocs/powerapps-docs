---
title: "Copy Dataverse data into Azure SQL | MicrosoftDocs"
description: "Learn how to run Azure Synapse pipelines with your exported Dataverse table data"
ms.custom: ""
ms.date: 08/18/2022
ms.reviewer: "Mattp123"
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "how-to"
applies_to: 
  - "powerapps"
author: "JasonHQX"
ms.subservice: dataverse-maker
ms.author: "matp"
manager: "kvivek"
search.audienceType: 
  - maker
search.app: 
  - PowerApps
  - D365CE
contributors: "sama-zaki"
---
# Copy Dataverse data into Azure SQL

[!INCLUDE[cc-data-platform-banner](../../includes/cc-data-platform-banner.md)]

Use the Azure Synapse Link to connect your Microsoft Dataverse data to Azure Synapse Analytics to explore your data and accelerate time to insight. This article shows you how to run Azure Synapse pipelines or Azure Data Factory to copy data from Azure Data Lake Storage Gen2 to an Azure SQL Database with incremental updates feature enabled in Azure Synapse Link.

> [!NOTE]
> Azure Synapse Link for Microsoft Dataverse was formerly known as Export to data lake. The service was renamed effective May 2021 and will continue to export data to Azure Data Lake as well as Azure Synapse Analytics.

## Prerequisites

1. Azure Synapse Link for Dataverse. This guide assumes that you've already met the prerequisites to create an Azure Synapse Link with a Synapse workspace. More information: [Prerequisites for an Azure Synapse Link for Dataverse with your Azure Synapse Workspace](azure-synapse-link-synapse.md#prerequisites)
2. Create an Azure Synapse Workspace or Azure Data Factory under the same Azure Active Directory (Azure AD) tenant as your Power Apps tenant.
3. Create an Azure Synapse Link for Dataverse with the incremental folder update enabled. More information: [Query and analyze the incremental updates](azure-synapse-incremental-updates.md)
4. Microsoft.EventGrid provider needs to be registered for trigger. More information: [Azure portal](/azure/azure-resource-manager/management/resource-providers-and-types#azure-portal)
5. Create an Azure SQL database with the **Allow Azure services and resources to access this server** property enabled. More information: [What should I know when setting up my Azure SQL Database (PaaS)?](/archive/blogs/azureedu/what-should-i-know-when-setting-up-my-azure-sql-database-paas#firewall)
6. Create and configure an Azure integration runtime. More information: [Create Azure integration runtime - Azure Data Factory & Azure Synapse](/azure/data-factory/create-azure-integration-runtime?tabs=data-factory)

## Use the solution template
# [Synapse Analytics](#tab/synapse-analytics)
1. In [Power Apps](https://make.powerapps.com/?utm_source=padocs&utm_medium=linkinadoc&utm_campaign=referralsfromdoc), go to **Data** > **Azure Synapse Link**, select your desired Azure Synapse Link from the list, and then select **Go to Azure Synapse workspace**.
   :::image type="content" source="media/go-to-workspace.png" alt-text="Go to Azure Synapse Workspace":::

1. Select **Integrate** > **Browse gallery**.
1. Select **Copy Dataverse data into Azure SQL using Synapse Link** from the integration gallery.

# [Azure Data Factory](#tab/data-factory)
1. Go to the Azure portal and open Azure Data Factory Studio.
1. Select **Add new resource** > **Pipeline** > **Template gallery**.
1. Select **Copy Dataverse data into Azure SQL using Synapse Link** from the template gallery.

---

## Configure the solution template

1. Create a linked service to Azure Data Lake Storage Gen2, which is connected to Dataverse using the appropriate authentication type. To do this, select **Test connection to validate the connectivity,** and then select **Create**.
1. Similar to the previous steps, create a linked service to Azure SQL Database where Dataverse data will be synced.
1. Once **Inputs** are configured, select **Use this template**.
   :::image type="content" source="media/ADLSG2-use-this-template.png" alt-text="Use this template":::

1. Now a trigger can be added to automate this pipeline, so that the pipeline can always process files when incremental updates are completed periodically. Go to **Manage** > **Trigger**, and create a trigger using the following properties:
   - **Name**: Enter a name for the trigger, such as *triggerModelJson*.
   - **Type**: **Storage events**.
   - **Azure subscription**: Select the subscription that has Azure Data Lake Storage Gen2.
   - **Storage account name**: Select the storage that has Dataverse data.
   - **Container name**: Select the container created by Azure Synapse Link.
   - **Blob path ends with**: */model.json*
   - **Event**: **Blob created**.
   - **Ignore empty blobs**: **Yes**.
   - **Start trigger**: Enable **Start trigger on creation**.

   :::image type="content" source="media/ADLSG2-create-trigger.png" alt-text="Create a trigger":::
1. Select **Continue** to proceed to the next screen.
1. On the next screen, the trigger validates the matching files. Select **OK** to create the trigger.
1. Associate the trigger with a pipeline. Go to the pipeline imported earlier, and then select **Add trigger** > **New/Edit**.
   :::image type="content" source="media/ADLSG2-add-trigger-pipeline.png" alt-text="Create a trigger for the pipeline.":::
1. Select the trigger in the earlier step, and then select **Continue** to proceed to the next screen where the trigger validates the matching files.
1. Select **Continue** to proceed to the next screen.
1. In the **Trigger Run Parameter** section, enter the below parameters, and then select **OK**.
   - **Container**: `@split(triggerBody().folderPath,'/')[0]`
   - **Folder**: `@split(triggerBody().folderPath,'/')[1]`  
1. After associating the trigger with the pipeline, select **Validate all**. 
1. Once validation succeeds, select **Publish All**.
   :::image type="content" source="media/ADLSG2-publish-all.png" alt-text="Select Publish all":::

1. Select **Publish** to publish all the changes.
   :::image type="content" source="media/ADLSG2-publish2.png" alt-text="Select Publish to complete the publishing":::

### Add an event subscription filter

To ensure that the trigger fires only when model.json creation is complete, advanced filters need to be updated for the trigger’s event subscription. An event is registered against the storage account the first time the trigger runs.
  
1. Once a trigger run completes, go to storage account > **Events** > **Event Subscriptions**.
1. Select the event that was registered for the model.json trigger.
   :::image type="content" source="media/ADLSG2-event-subscription.png" alt-text="Event subscription":::

1. Select the **Filters** tab, and then select **Add new filter**.
   :::image type="content" source="media/ADLSG2-add-new-filter.png" alt-text="Add new filter":::

1. Create the filter:
   - **Key**: **subject**
   - **Operator**: **String does not end with**
   - **Value**: */blobs/model.json*

1. Remove the **CopyBlob** parameter from **data.api** **Value** array.

1. Select **Save** to deploy the additional filter.
   :::image type="content" source="media/ADLSG2-save-filter.png" alt-text="Save added filter":::

### See also

[Blog: Announcing Azure Synapse Link for Dataverse](https://aka.ms/synapse-dataverse)

[!INCLUDE[footer-include](../../includes/footer-banner.md)]
