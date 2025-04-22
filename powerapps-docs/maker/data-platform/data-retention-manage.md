---
title: Manage data retention policies in Microsoft Dataverse
description: This article explains how you can view and managed existing data retention policies in Microsoft Dataverse. 
author: pnghub
ms.author: gned
ms.reviewer: matp
ms.service: powerapps
ms.subservice: dataverse-maker
ms.topic: how-to 
ms.date: 02/29/2024
ms.custom: template-how-to 
---
# Manage data retention policies

Use the retention policies dashboard to view and manage retention policies. From the dashboard, view the policy run history, update policy details, deactivate, and delete a policy.

## View and manage retention policies

1. Sign into [Power Apps](https://make.powerapps.com/?utm_source=padocs&utm_medium=linkinadoc&utm_campaign=referralsfromdoc), and then on the left navigation pane select **Retention policies**. [!INCLUDE [left-navigation-pane](../../includes/left-navigation-pane.md)]
1. Select a retention policy from the list, and then on the command bar select **Policy details**.
1. The following retention policy actions are available:
  - **History**. Displays the retention [policy run status](#policy-run-status), run start, run end and table. For every run, you can view all tables (root and child tables) and the number of rows retained in the run.
  - **Policy details**. Displays the properties for the policy where you can view and edit the policy name, criteria, and frequency.
  - **Deactivate**. Stops the retention policy from running by disabling the policy schedule. To activate a deactivated policy, select **Policy details**, set the policy **Schedule**, and then select **Update**.
  - **Delete**. Removes the policy.

:::image type="content" source="media/data-retention-policy-details.png" alt-text="Policy run details":::

### Policy run status

|Status  |Description  |
|---------|---------|
|Scheduled     |  The policy has been scheduled to run.       |
|In progress - Retention     | The process of moving and changing the data state from active to non-active (retained) for the rows in the parent root table and all child tables.        |
|Pending Reconciliation     |  Waiting to reconcile the retained rows in Dataverse long term retention.      |
|In progress – Reconciliation     | During this stage, ensures no data loss by reconciling the retained rows with the original rows before delete from active.     |
|Pending Delete     |  Waiting to delete all retained rows.       |
|In progress – Delete     |  Delete of retained rows from applications.       |
|Completed     |  Retention process completed successfully.       |
|Failed     |  The retention process failed.     |

### View details on failed records

Query the Dataverse table `Retentionfailuredetails` for error details.

|Column name  |Description  |
|---------|---------|
|`Operationid`     |  The policy `runid` visible in the long term retention dashboard for a specific policy run.       |
|`entitylogicalname`     | Name of the table containing the record.      |
|`recordid`     | Unique identifier of every record in the table.    |
|`message`     | Detailed error message.        |

### Bulk delete long term retained data

Dataverse bulk delete with the Dataverse SDK supports deletion of long term retained data. [More information](/power-apps/developer/data-platform/delete-data-bulk#:~:text=Bulk%20delete%20is%20also%20available,DataSource%20field%20to%20%22retained%22). 

## See also

[View long term retained data](data-retention-view.md) <br />
[Share your ideas](https://experience.dynamics.com/ideas/categories/list/?category=55f731de-11f3-ed11-8848-00224827ed7b&forum=eef9aef6-0ff3-ed11-8848-00224827e88b)
