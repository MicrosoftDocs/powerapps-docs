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
|In progress - Retention     | The process of moving and changing the data state from active to non-active (retained) for the rows in the parent root table and all child tables.        |
|In progress - Pending Reconciliation     |  Waiting to reconcile the retained rows in Dataverse managed data lake.      |
|In progress – Reconciling     | During this stage, ensures no data loss by reconciling the retained rows with the original rows before delete from active.     |
|In progress – Pending Delete     |  Waiting to delete all retained rows.       |
|In progress – Delete     |  Delete of retained rows from applications       |
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

Use the Power Automate cloud flow template to generate and retrieve retained data in Excel is available. <!-- Need a demo of this or more specific steps how to do it.-->

### Limitations for retrieval of retained data

This restrictions are enforced by Dataverse for each environment:

- Up to five users can query and retrieve retained data at the same time.
- ‘Admin’ role or ‘global entity access’ role on table required to retrieve retained data <!-- Do you mean global read access to the Entity privilege? -->
- Up to 30 queries per day are allowed for each environment.
- Any single request from advanced find, Power Automate cloud flow, or Dataverse OData public API is considered as one query.
- Queries are allowed on one table at a time. Joins and aggregation functions aren't allowed.
- Retained data includes lookup data and doesn't require joins. 
- Lookup values in a table are denormalized with ID and name value.

## Storage capacity reports

When data is retained long term in Dataverse, it is a switch from a live (active) state to a retained cold (non-active) state for rows.

The existing Power Platform admin reports display the total consumed storage for each storage type with the details for each table. The total consumed storage for Database, file, and log is the sum of the live and retained data.
 
## Solution aware retention policies

Dataverse retention policies are solution aware. Dataverse retention policies added to a solution are known as solution-aware retention policies. You can add multiple retention policies to a single solution. Retention policies are added to an unmanaged solution. This helps makers follow application lifecycle management (ALM) best practices when working with Dataverse retention policies.

When you include your retention policies in a solution, their definitions become portable, making it easier to move them from one environment to another, saving time required to create the retention policy. For example, you first develop a solution containing a retention policy in a development or sandbox environment. You then move that retention policy to a pre-production environment to test and validate that the solution works well and is ready for production. After testing is completed, the admin imports the solution into the production environment.

> [!NOTE]
> - The data retained by retention policies isn't portable as part of solutions, only the retention policy definitions are. You must run the retention policy in an environment to retain the data in Dataverse long term storage.
> - Only retention policies created in Power Platform environments can be solution-aware.

You create a solution before you add a retention policy to it. Exporting and importing solutions containing retention policies is the same as with other solution components.

For more information about solutions and solution components, go to [Solutions overview](solutions-overview.md).

<!-- Brief intro and link to dev article for Enterprise governance - GDPR Bulk Delete-->