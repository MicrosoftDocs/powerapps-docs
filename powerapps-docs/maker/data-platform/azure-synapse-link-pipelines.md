---
title: "Copy Dataverse data into Azure SQL | MicrosoftDocs"
description: "Learn how to run Azure Synapse pipelines with your exported Dataverse table data"
ms.custom: ""
ms.date: 02/07/2023
ms.reviewer: "Mattp123"
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "how-to"
applies_to: 
  - "powerapps"
author: "JasonHQX"
ms.subservice: dataverse-maker
ms.author: "matp"
search.audienceType: 
  - maker
contributors: "sama-zaki"
---
# Copy Dataverse data into Azure SQL

[!INCLUDE[cc-data-platform-banner](../../includes/cc-data-platform-banner.md)]

Use the Azure Synapse Link to connect your Microsoft Dataverse data to Azure Synapse Analytics to explore your data and accelerate time to insight. This article shows you how to run Azure Synapse pipelines or Azure Data Factory to copy data from Azure Data Lake Storage Gen2 to an Azure SQL Database with incremental updates feature enabled in Azure Synapse Link.

> [!NOTE]
> Azure Synapse Link for Microsoft Dataverse was formerly known as Export to data lake. The service was renamed effective May 2021 and will continue to export data to Azure Data Lake as well as Azure Synapse Analytics.
> This template is a code sample. We encourage you to use this template as guidance to test out the functionality of retrieving data from Azure Data Lake Storage Gen2 to Azure SQL Database using the pipeline provided.

## Prerequisites

1. Azure Synapse Link for Dataverse. This guide assumes that you've already met the prerequisites to create an Azure Synapse Link with Azure Data Lake. More information: [Prerequisites for an Azure Synapse Link for Dataverse with your Azure Data Lake](azure-synapse-link-data-lake.md#prerequisites)
2. Create an Azure Synapse Workspace or Azure Data Factory under the same Microsoft Entra tenant as your Power Apps tenant.
3. Create an Azure Synapse Link for Dataverse with the **incremental folder update enabled** to set the time interval. More information: [Query and analyze the incremental updates](azure-synapse-incremental-updates.md)
4. Microsoft.EventGrid provider needs to be registered for trigger. More information: [Azure portal](/azure/azure-resource-manager/management/resource-providers-and-types#azure-portal). Note: If you are using this feature in Azure Synapse Analytics, ensure that your subscription is also registered with Data Factory resource provider, otherwise you'll get an error stating that the creation of an "Event Subscription" failed.
5. Create an Azure SQL database with the **Allow Azure services and resources to access this server** property enabled. More information: [What should I know when setting up my Azure SQL Database (PaaS)?](/archive/blogs/azureedu/what-should-i-know-when-setting-up-my-azure-sql-database-paas#firewall)
6. Create and configure an Azure integration runtime. More information: [Create Azure integration runtime - Azure Data Factory & Azure Synapse](/azure/data-factory/create-azure-integration-runtime?tabs=data-factory)

> [!IMPORTANT]
> Using this template might incur additional costs. These costs are related to the usage of Azure Data Factory or Synapse workspace pipeline and are billed on a monthly basis. The cost of using pipelines mainly depends on the time interval for incremental update and the data volumes. To plan and manage the cost of using this feature, go to: [Monitor costs at pipeline level with cost analysis](/azure/data-factory/plan-manage-costs#monitor-costs-at-pipeline-level-with-cost-analysis)
>
> It's important to take these additional costs into consideration when deciding to use this template as they are not optional and must be paid in order to continue using this feature.

## Use the solution template

# [Synapse Analytics](#tab/synapse-analytics)
1. Go to the [Azure portal](https://portal.azure.com) and open Azure Synapse workspace.
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
   :::image type="content" source="media/ADLSG2-use-this-template.png" alt-text="Use this template" lightbox="media/ADLSG2-use-this-template.png":::

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
   :::image type="content" source="media/ADLSG2-add-trigger-pipeline.png" alt-text="Create a trigger for the pipeline." lightbox="media/ADLSG2-add-trigger-pipeline.png":::
1. Select the trigger in the earlier step, and then select **Continue** to proceed to the next screen where the trigger validates the matching files.
1. Select **Continue** to proceed to the next screen.
1. In the **Trigger Run Parameter** section, enter the below parameters, and then select **OK**.
   - **Container**: `@split(triggerBody().folderPath,'/')[0]`
   - **Folder**: `@split(triggerBody().folderPath,'/')[1]`  
1. After associating the trigger with the pipeline, select **Validate all**. 
1. Once validation succeeds, select **Publish All**.
   :::image type="content" source="media/ADLSG2-publish-all.png" alt-text="Select Publish all" lightbox="media/ADLSG2-publish-all.png":::

1. Select **Publish** to publish all the changes.

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

### Adding Alerting Functionality for the "Else" Condition in the Existing ADF Pipeline

In the current ADF pipeline, we distinguish between two successful scenarios: one where the data ingestion proceeds as expected and one where it doesn't. Though the pipeline succeeds in both cases, the latter scenario is a concern that requires immediate attention.

To address this, we'll add an alerting step after the "IF" condition. If this condition is not met, the user will be notified via email. Here's how to add this functionality using Azure Logic Apps:

1. **Connect** to the Existing Logic App (or **Create** One if Necessary).

1. **Open** the Logic App designer.

1. Configuring Logic App:
   - **Create** a Blank Logic App in Logic App Designer
   ![image](https://github.com/MicrosoftDocs/powerapps-docs/assets/69673173/e8fcf937-bd2f-473b-9411-1c2b4edac0ff)
   - **Search** "Request" to create an HTTP Request based trigger.
   ![image](https://github.com/MicrosoftDocs/powerapps-docs/assets/69673173/d6c78784-2c5d-471c-a290-f341d800418c)
   - Then **select** "When a HTTP request is received"
   ![image](https://github.com/MicrosoftDocs/powerapps-docs/assets/69673173/57ac6474-f611-4ff3-bde8-ed21b2d4cfd6)
   - **Copy** the following sample JSON into the textbox and select **Done**.
    ```json
    {
        "ErrorMessage": "<Error>",
        "ResourceName": "<ResourceName>",
        "Pipeline": "<name>",
        "RunID": "<RunID>",
        "Email": "<email-address>"
    }
    ```
   - **Click** "Add new parameter" and **Select** POST as the "Method".
   ![image](https://github.com/MicrosoftDocs/powerapps-docs/assets/69673173/31086305-b919-448e-b290-7f9e78e63b30)
   - **Click** "Next Step".
   - **Type** in and **select** the name of your preferred email provider. E.g. Outlook
   - **Click** "Actions"
   ![image](https://github.com/MicrosoftDocs/powerapps-docs/assets/69673173/dd429a21-ed3b-4fbf-9f4a-f5cc86ca4b3d)
   - **Select** "Send an email".
   - Sign in to create a connection to Outlook.
   - **Create** email using "Dynamic content" (These are received through the Put Request)
   - **Copy** "HTTP POST URL" and go to your ADF pipeline.

1. Adding and Configuring Web Activity in ADF:
   - **Add** a "Web Activity" to the canvas and connect it as shown below.
    ![image](https://github.com/MicrosoftDocs/powerapps-docs/assets/69673173/ea6609dd-49da-4460-a558-10596e83baf0)
   - **Click** on the Web Activity and navigate to "Settings".
   - **Set** the URL as the "HTTP POST URL" we copied.
   - **Set** "Method" as POST.
   - **Set** "Headers" as shown below.
    ![image](https://github.com/MicrosoftDocs/powerapps-docs/assets/69673173/bb12e4a2-285f-412f-819e-389573a0d5be)
   - **Set** "Body" dynamic content as (make sure to change the value pairs to the appropriate values)
   ```json
    @{
        "ErrorMessage": "@{<Error>}",
        "ResourceName": "@{<ResourceName>}",
        "Pipeline": "@{<name>}",
        "RunID": "@{<RunID>}",
        "Email": "@{<email-address>}"
    }
    ```
   
1. Save and Test:
   - Click "Save."
   - Run a test on the ADF pipeline with the scenario that triggers the "else" condition to verify that the email alert is working correctly.

With this added step in your ADF pipeline, you can ensure prompt notification if the "IF" condition is not met, even when the pipeline technically succeeds. This functionality enhances monitoring and helps maintain the data integrity and timely response needed for your business operations.

### See also

[Blog: Announcing Azure Synapse Link for Dataverse](https://aka.ms/synapse-dataverse)

[!INCLUDE[footer-include](../../includes/footer-banner.md)]