---
title: View long term retained data in Microsoft Dataverse
description: Learn how to access ready only data that is in long term storage. 
author: pnghub
ms.author: matp
ms.reviewer: matp
contributors: manasdalai
ms.service: powerapps
ms.subservice: dataverse-maker
ms.topic: how-to
ms.date: 06/27/2024
ms.custom: template-how-to
---
# View long term retained data

You can view retained data from an advanced find query or by creating a Power Automate flow. 

To view retained data in an environment requires the system administrator security role or other security role membership that includes organization scope read privileges to the table.

## Grant privileges to view retained data

Imagine an auditor requires access to long term data retained for the accounts table. To provide the auditor access, a Power Platform admin creates a new role, for example a role named *LTRAccounts Access Role* and grants organization scope read privilege to the accounts table. Then add the auditor's Power Platform user account to the security role. When the auditor's job is complete, it's a best practice to remove the auditor from the security role.

:::image type="content" source="media/data-retention-grant-privileges.png" alt-text="Privileges for viewing retained data" lightbox="media/data-retention-grant-privileges.png":::

For more information about creating and editing Dataverse security roles, go to [Create or edit a security role to manage access](/power-platform/admin/create-edit-security-role).

## View retained data using edit filters from a model-driven app

> [!NOTE]
> - You can't save or export the the view query results of the retained data for sharing with others. To share retained data, [create a cloud flow to view Dataverse long term retained data](/power-automate/dataverse/data-retention-flow).
> - Edit filters doesn't retrieve table row attachments. To view attachment data, create a flow. More information: [Create a cloud flow to view Dataverse long term retained data](/power-automate/dataverse/data-retention-flow)

1. Sign into [Power Apps](https://make.powerapps.com/?utm_source=padocs&utm_medium=linkinadoc&utm_campaign=referralsfromdoc), play an app that includes a table that has retained data.
1. Open the view you want. From the view, select **Edit filters**.
1. Select **Change to retained data**.
   :::image type="content" source="media/data-retention-advanced-find.png" alt-text="Select change to retained data on the edit filter pane.":::
   
   > [!NOTE]
   > This changes the [fetch element](../../developer/data-platform/fetchxml/reference/fetch.md) `datasource` attribute value to `"retained"`.

1. Select the tables and search filters you want, and then select **Apply**. The retained data is displayed in the read-only grid.
   :::image type="content" source="media/data-retention-advanced-find-results.png" alt-text="Advanced find query results displaying retained case records":::
If you need to retrieve long term data from multiple related tables, such as the account table, which has an associated retained case table, first use advanced find retrieve the retained case row. Then use the `Casenumber` column and use advanced find to retrieve the account row that contains the case number.

More information: [Advanced find in model-driven apps](../../user/advanced-find.md)

## View retained data using a flow

Create a Power Automate cloud flow to create an Excel file of the retained data from a FetchXML query and send as an email attachment. More information: [Create a cloud flow to view Dataverse long term retained data](/power-automate/dataverse/data-retention-flow)

> [!NOTE]
> If the retained data includes attachments from the annotation table, the returned value is a base64 representation of the file. Large files might cause the cloud flow action to [time-out](/power-automate/limits-and-config#timeout) or to exceed its output [message size limit](/power-automate/limits-and-config#message-size).
>
> To workaround this behavior, use the `ExportRetainedData` message Web API to [ExportRetainedData action](/power-apps/developer/data-platform/webapi/reference/exportretaineddata) or SDK for .NET using Azure Functions or other custom development options.

## Limitations for retrieval of retained data

These restrictions are enforced by Dataverse for each environment:

- Up to five users can query and retrieve retained data at the same time.
- Up to 100 queries per day are allowed for each environment.
- Any single request from advanced find, Power Automate cloud flow, or Dataverse OData public API is considered as one query.
- Queries are allowed on one table at a time. Joins and aggregation functions aren't allowed. Consider options with Microsoft Fabric for complex queries and Power BI options. More information: [View retained data with Microsoft Fabric](#view-retained-data-with-microsoft-fabric)
- Retained data includes lookup data. Lookup values in the table are denormalized with ID and name value.

## View retained data with Microsoft Fabric 

You can view the active (live) and inactive (long term retained) application data in Dataverse using Microsoft Fabric.
To do this, link your Dataverse environment to Fabric. More information: [Link your Dataverse environment to Microsoft Fabric and unlock deep insights](azure-synapse-link-view-in-fabric.md).

When your long term retention policy is run successfully, you can access the active and inactive Dataverse data. The [limitations applied to retrieval of retained data](#limitations-for-retrieval-of-retained-data) don't apply to this mode of access.

You can explore the data with SQL endpoint and query Dataverse data with SQL and generate views in Fabric. You can also create Power BI reports. More information: [Work with Dataverse data and generate Power BI reports](fabric-work-data-and-power-bi.md)

The Dataverse table column `msft_datastate` can be used to filter the data with the SQL `WHERE` clause:

- Inactive application data: `WHERE msft_datastate=1`
- Active (live) application data: `WHERE msft_datastate=0 or msft_datastate=NULL'

## Known issues

### Personal views of retained data

Saving the query results of the retained data as a personal view isn't supported. Although users can save the query results of the retained data as a personal view, the view doesn't return results.

## See also

[Dataverse long term data retention overview](data-retention-overview.md) <br />
[Share your ideas](https://experience.dynamics.com/ideas/categories/list/?category=55f731de-11f3-ed11-8848-00224827ed7b&forum=eef9aef6-0ff3-ed11-8848-00224827e88b)
