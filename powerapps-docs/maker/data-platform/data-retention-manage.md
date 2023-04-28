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

[!INCLUDE [cc-beta-prerelease-disclaimer](../../includes/cc-beta-prerelease-disclaimer.md)]

Use the retention policies dashboard to view and manage retention policies. From the dashboard, view the policy run history, update policy details, deactivate, and delete a policy.

> [!IMPORTANT]
> - This is a preview feature.
> - [!INCLUDE [cc-preview-features-definition](../../includes/cc-preview-features-definition.md)]
> - For public preview, only non-production environments are allowed for previewing the long-term data retention feature.

## View and manage retention policies

1. Sign into [Power Apps](https://make.powerapps.com/?utm_source=padocs&utm_medium=linkinadoc&utm_campaign=referralsfromdoc), and then on the left navigation pane select **Retention policies**. [!INCLUDE [left-navigation-pane](../../includes/left-navigation-pane.md)]
1. Select a retention policy from the list, and then on the command bar select **Policy details**.
1. The following retention policy actions are available:
  - **History**. Displays the retention [policy run status](#policy-run-status), run start, run end and tables included in the last run.
  - **Policy details**. Displays the properties for the policy where you can view and edit.
  - **Deactivate**. Stops the retention policy from running by disabling the policy schedule. To activate a deactivated policy, select **Policy details**, set the policy **Schedule**, and then select **Update**.
  - **Delete**. Removes the policy.

### Policy run status

|Status  |Description  |
|---------|---------|
|Scheduled     |  The policy has been scheduled to run.       |
|In progress - Retention     | The process of moving and changing the data state from active to non-active (retained) for the rows in the parent root table and all child tables.        |
|Pending Reconciliation     |  Waiting to reconcile the retained rows in Dataverse managed data lake.      |
|In progress – Reconciliation     | During this stage, ensures no data loss by reconciling the retained rows with the original rows before delete from active.     |
|Pending Delete     |  Waiting to delete all retained rows.       |
|In progress – Delete     |  Delete of retained rows from applications.       |
|Succeeded     |  Retention process completed successfully.       |
|Failed     |  The retention process failed  .     |

## View long term retained data

You can view retained data from an Advanced Find query or by creating a Power Automate flow. 

> [!NOTE]
> To view retained data in an environment requires the system administrator security role or other security role membership that includes organization scope read privileges to the table.

### Grant privileges to view retained data

Imagine an auditor requires access to long term data retained for the accounts table. To provide the auditor access, a Power Plaform admin creates a new role, for example a role named *LTRAccounts Access Role* and grants organization scope read privilege to the accounts table. Then add the auditor's Power Platform user account to the security role. When the auditor's job is complete, it's a best practice to remove the auditor from the security role. For more information about creating and editing Dataverse security roles, go to [Create or edit a security role to manage access](/power-platform/admin/create-edit-security-role). <!--I don't think this would be enough. Probably have to start with the App access user role and add this privilege. Also, how to access advanced find for the auditor? I believe they can go to maker portal > Settings > Advanced Settings > and then select the Advanced Find (filter icon)-->

### View retained data using advanced find

> [!NOTE]
> Advanced Find doesn't retrieve table row attachments. To view attachment data, create a flow. More information: [Create a cloud flow to view Dataverse long term retained data](data-retention-flow.md)

1. Sign into [Power Apps](https://make.powerapps.com/?utm_source=padocs&utm_medium=linkinadoc&utm_campaign=referralsfromdoc), and then select **Settings** > **Advanced settings**.
1. On the **Dynamics 365 Settings** page, select **Advanced Find** (filter icon) on the command bar.
1. At the top of the advanced find pane, select **Change to retained data**.
   :::image type="content" source="media/data-retention-advanced-find.png" alt-text="Select change to retained data on the advanced find pane.":::
1. Select the tables and search filters you want, and then select **Apply**. More information: [Advanced find in model-driven apps](../../user/advanced-find.md)

If you need to retrieve long term data from multiple related tables, such as the account table, which has an associated retained case, first use Advanced Find retrieve the retained case row. Then use the **Casenumber** column and use Advanced Find to retrieve the account row. <!-- Need more detail on how to do this -->

### View retained data using a flow

Use the Power Automate cloud flow template to generate and retrieve retained data in Excel. More information: [Create a cloud flow to view Dataverse long term retained data](data-retention-flow.md)

### Limitations for retrieval of retained data

This restrictions are enforced by Dataverse for each environment:

- Up to five users can query and retrieve retained data at the same time.
- Up to 30 queries per day are allowed for each environment.
- Any single request from Advanced Find, Power Automate cloud flow, or Dataverse OData public API is considered as one query.
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