---
title: View long term retained data in Microsoft Dataverse
description: Learn how to access ready only data that is in long term storage. 
author: Mattp123
ms.author: matp
ms.service: powerapps
ms.topic: how-to
ms.date: 05/05/2023
ms.custom: template-how-to 
---
# View long term retained data

You can view retained data from an Advanced Find query or by creating a Power Automate flow. 

> [!NOTE]
> To view retained data in an environment requires the system administrator security role or other security role membership that includes organization scope read privileges to the table.

## Grant privileges to view retained data

Imagine an auditor requires access to long term data retained for the accounts table. To provide the auditor access, a Power Plaform admin creates a new role, for example a role named *LTRAccounts Access Role* and grants organization scope read privilege to the accounts table. Then add the auditor's Power Platform user account to the security role. When the auditor's job is complete, it's a best practice to remove the auditor from the security role. For more information about creating and editing Dataverse security roles, go to [Create or edit a security role to manage access](/power-platform/admin/create-edit-security-role). <!--I don't think this would be enough. Probably have to start with the App access user role and add this privilege. Also, how to access advanced find for the auditor? I believe they can go to maker portal > Settings > Advanced Settings > and then select the Advanced Find (filter icon)-->

## View retained data using Advanced Find

> [!NOTE]
> - You can't save or export the Advanced Find find query results of the retained data for sharing with others. To share retained data, [create a cloud flow to view Dataverse long term retained data](/power-automate/dataverse/data-retention-flow).
> - Advanced Find doesn't retrieve table row attachments. To view attachment data, create a flow. More information: [Create a cloud flow to view Dataverse long term retained data](/power-automate/dataverse/data-retention-flow)

1. Sign into [Power Apps](https://make.powerapps.com/?utm_source=padocs&utm_medium=linkinadoc&utm_campaign=referralsfromdoc), and then select **Settings** > **Advanced settings**.
1. On the **Dynamics 365 Settings** page, select **Advanced Find** (filter icon) on the command bar.
1. At the top of the Advanced Find pane, select **Change to retained data**.
   :::image type="content" source="media/data-retention-advanced-find.png" alt-text="Select change to retained data on the advanced find pane.":::
1. Select the tables and search filters you want, and then select **Apply**. More information: [Advanced find in model-driven apps](../../user/advanced-find.md)

If you need to retrieve long term data from multiple related tables, such as the account table, which has an associated retained case, first use Advanced Find retrieve the retained case row. Then use the **Casenumber** column and use Advanced Find to retrieve the account row that contains the case number. 

## View retained data using a flow

Create a Power Automate cloud flow to create an Excel file of the retained data from a FetchXML query and send as an email attachment. More information: [Create a cloud flow to view Dataverse long term retained data](/power-automate/dataverse/data-retention-flow)

## Limitations for retrieval of retained data

This restrictions are enforced by Dataverse for each environment:

- Up to five users can query and retrieve retained data at the same time.
- Up to 30 queries per day are allowed for each environment.
- Any single request from Advanced Find, Power Automate cloud flow, or Dataverse OData public API is considered as one query.
- Queries are allowed on one table at a time. Joins and aggregation functions aren't allowed.
- Retained data includes lookup data and doesn't require joins.
- Lookup values in a table are denormalized with ID and name value.

## See also

[Dataverse long term data retention overview (preview)](data-retention-overview.md)