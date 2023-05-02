---
title: Create a cloud flow to view Dataverse long term retained data
description: This article explains how you can Create a cloud flow to view Microsoft Dataverse long term retained data.
author: Mattp123
ms.author: matp
ms.service: powerapps
ms.topic: how-to 
ms.date: 04/27/2023
ms.custom: template-how-to 
---
# Create a cloud flow to view Dataverse long term retained data

Create a cloud flow to view read-only rows in long term data retention in Microsoft Dataverse. For more information about long term data retention in Dataverse, go to [Dataverse long term data retention overview (preview)](data-retention-overview.md).

The cloud flow generates an email used to retrieve retained data in Excel. If there are retained attachments associated with rows from Dataverse, it's included in Excel.

Creating the flow requires the following high level steps:

1. Pass query parameters in a FetchXML to create an Excel file with retained data.
1. Set a condition to determine if the Excel file has been created. Download the Excel file. Pass the required retrieval criteria parameters (table and FetchXml).
1. Create an Excel file with the retrieved data.
1. Send an email to recipients with the Excel file attached.  

Make sure to check your junk mail folder if you don’t see an email after running a flow successfully.

## Create the query and download FetchXML

1. Sign into [Power Apps](https://make.powerapps.com/?utm_source=padocs&utm_medium=linkinadoc&utm_campaign=referralsfromdoc), and then select **Settings** > **Advanced settings**.
1. On the **Dynamics 365 Settings** page, select **Advanced Find** (filter icon) on the command bar.
1. At the top of the advanced find pane, select **Change to retained data**.
1. Create the query you want to retrieve the retained data. More information: [Advanced find in model-driven apps](../../user/advanced-find.md)
1. In Advanced Find on the **Advanced Find** tab, select **Download Fetch XML**.

## Create the flow

1. On the [Power Apps](https://make.powerapps.com/?utm_source=padocs&utm_medium=linkinadoc&utm_campaign=referralsfromdoc) home page, select **Flows** on the left navigation pane.
1. Select **New flow**, and then select either **Instant cloud flow** or **Scheduled cloud flow**.
1. Enter a name for the flow, and then choose from the following triggers: 
   - For instant cloud flows select **Manually trigger a flow**.
   - For scheduled cloud flows select <!-- WHAT Trigger TO SELECT??? -->
1. Select **Create**.
1. Select **New step**, and then on the **Choose an operation** step, select **Microsoft Dataverse**.
1. For the action, select **Perform a background operation**.
   :::image type="content" source="media/data-retention-flow1.png" alt-text="For the action, select perform background operation.":::

1. Enter the following information: 
   - **Catalog**: **All**
   - **Category**: **All**
   - **Table name**: none <!-- This is required. How can it be none? -->
   - **Action name**: Create ExportedExcel from Retained Data query <!-- Is this typed or selected?-->
   - **FetchXml**: Paste in the FetchXML created earlier.
   :::image type="content" source="media/data-retention-flow2.png" alt-text="Create action that includes your retained data query FetchXML":::
1. Select **New step**.
1. Under **Choose an operation**, select **Condition**, and then select the **Expression** tab.
1. Add the following expression:
   - **outputs**: `('Perform_a_background_operation_(preview)')?['body/backgroundOperationStatusCode’]`
   - **is equal to**: *30*
1. In the **If yes** box, select **Add an action**.
   :::image type="content" source="media/data-retention-flow3.png" alt-text="Add and action for the condition":::
1. On the **Actions** tab, select **Download a file or an image**.
1. 