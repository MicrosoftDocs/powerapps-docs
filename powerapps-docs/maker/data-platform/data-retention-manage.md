---
title: Manage data retention policies in Microsoft Dataverse
description: This article explains how you can view and managed existing data retention policies in Microsoft Dataverse. 
author: Mattp123
ms.author: matp
ms.service: powerapps
ms.topic: how-to 
ms.date: 03/23/2023
ms.custom: template-how-to 
---
# Manage data retention policies

Use the retention policies dashboard to view and manage retention policies. From the dashboard, view the policy run history, update policy details, deactivate, and delete a policy.

## View and manage retention policies

1. Sign into [Power Apps](https://make.powerapps.com/?utm_source=padocs&utm_medium=linkinadoc&utm_campaign=referralsfromdoc), and then on the left navigation pane select **Retention policies**. [!INCLUDE [left-navigation-pane](../../includes/left-navigation-pane.md)]
1. Select a retention policy from the list, and then on the command bar select **Policy details**.
1. The following retention policy actions are available:
  - **History**. Displays the retention [policy run status](#policy-run-status), run start, run end and tables included in the last run.
  - **Policy details**.
  - **Deactivate**. Stops the retention policy from running by disabling the policy schedule. To activate the policy, select **Policy details**, set the policy **Schedule**, and then select **Update**.
  - **Delete**. Removes the policy.

### Policy run status

|Status  |Description  |
|---------|---------|
|Scheduled     |  The policy has been scheduled to run.       |
|In progress - Retention     | The process of moving and changing the data state from active to non-active (retained) for the records in the parent root table and all child tables.        |
|In progress - Pending Reconciliation     |  Waiting to reconcile the retained records in Dataverse managed data lake.      |
|In progress – Reconciling     | During this stage, ensures no data loss by reconciling the retained records with the original records before delete from active.     |
|In progress – Pending Delete     |  Waiting to delete all retained records.       |
|In progress – Delete     |  Delete of retained records from applications       |
|Succeeded     |  Retention process completed successfully.       |
|Failed     |  Retention process failed       |

## View retained data

There are a few ways you can view retained data.

> [!NOTE]
> To view retained data in an environment requires the system administrator security role.

### View retained data using advanced find

1. Play a model-driven app, and then open advanced find. 
1. At the top of the advanced find pane, select **Change to retained data**.
   :::image type="content" source="media/data-retention-advanced-find.png" alt-text="Select change to retained data on the advanced find pane.":::
1. Select tables and search filters you want, and then select **Apply**. More information: [Advanced find in model-driven apps](../../user/advanced-find.md)

### View retained data using a flow

Use the Power Automate cloud flow template to generate and retrieve retained data in Excel is available. <!-- Continue here-->