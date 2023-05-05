---
title: Set a data retention policy for a table
description: Explains how to set a data retention policy for a Microsoft Datverse table. 
author: Mattp123
ms.author: matp
ms.service: powerapps
ms.topic: how-to 
ms.date: 03/23/2023
ms.custom: template-how-to
---
# Set a data retention policy for a table (preview)

[!INCLUDE [cc-beta-prerelease-disclaimer](../../includes/cc-beta-prerelease-disclaimer.md)]

This article explains how to setup a data retention policy for a Microsoft Dataverse table.

> [!IMPORTANT]
> - This is a preview feature.
> - [!INCLUDE [cc-preview-features-definition](../../includes/cc-preview-features-definition.md)]
> - For public preview, only non-production environments are allowed for previewing the long-term data retention feature.

## Prerequisites

The following prerequisites must be completed before you can set a table for long term data retention.

### Verify or enable a table for long term retention

By default, the following tables are enabled for retention. We recommend that before you set up a retention policy, make sure that the parent (root) table you want has been enabled for long term retention.

|Table type  |Tables  |
|---------|---------|
|Standard     | Account, Contact, Case<sup>1</sup>, Opportunity<sup>1</sup>, Lead<sup>1</sup>, Quote<sup>1</sup>, Order<sup>1</sup>, Invoice<sup>1</sup>       |
|Activity  |  Activity Party, Activity Mime Attachment, Appointment, CampaignActivity<sup>1</sup>, CampaignResponse<sup>1</sup>, Chat, Email, Fax, Letter, Phone Call, RecurringAppointmentMaster, ServiceAppointment<sup>1</sup>       |

<sup>1</sup>Requires a Dynamics 365 customer engagement app, such as Dynamics 365 Sales or Dynamics 365 Marketing.

#### Enable a table for long term retention

If a table isn't already enabled for long term data retention, makers can enable it.

> [!NOTE]
> When a parent table is enabled for retention, all the cascade related child tables are automatically enabled. You can't disable retention for a child table when the parent table is already enabled for retention. For example, assume a custom table and notes table are child tables of the case table. These child tables can't be disabled for retention when the parent case table is enabled. A maker can disable the parent table for retention and separately enable the child tables for retention.

1. Sign into [Power Apps](https://make.powerapps.com/?utm_source=padocs&utm_medium=linkinadoc&utm_campaign=referralsfromdoc), go to **Tables**, and then open the table you want. [!INCLUDE [left-navigation-pane](../../includes/left-navigation-pane.md)]
1. Select **Properties** on the command bar, expand **Advanced options**, and then select the **Enable long term retention** property.
   :::image type="content" source="media/data-retention-table-property.png" alt-text="Long term data retention table property":::
1. Select **Save**.

The parent and any child tables will be available for policy setup in about 15-30 minutes after you save the table. The larger the number of child tables, the longer it  takes to complete the process.

> [!NOTE]
> The long term retention property is disabled if the environment isn't enabled for long term retention. More information: [Prerequisite 2: Enable an environment for long term retention](#prerequisite-2-enable-an-environment-for-long-term-retention)

### Determine Dataverse views for policy criteria

Dataverse views are used to determine which table rows are marked for retention using a long-term retention policy. Before setting up a data retention policy, you must set up a Dataverse view as the criteria for retention.

Once you have a Dataverse view for use in a particular long term retention policy, you should test the view result. A good practice is to modify the view query with a `TOP N` statement and test it to ensure that the result set returned is as expected. This is always recommended especially when the number of rows is large. 

For example, consider a Dataverse view created to select all closed cases from the year 2015. The number of cases could be potentially very large. Therefore, you should add a `TOP N`, such as *TOP 10*, to the view and test it to confirm the sample set of the retrieved cases.

During data retention, rows from the parent table and all cascade related child tables are included for data retention as cold data. In the previous example, the parent cases might have associated rows from child cascade tables, for example notes, task, and custom tables. The retention policy ensures that the case record and all its related child rows are marked and retained as cold data in Dataverse. In addition, lookup values in the case table, as an example, are de-normalized with the ID and name values made available as part of the retained cold data. This allows in many scenarios for a single query to retrieve the relevant data.

> [!IMPORTANT]
> We recommend that you create a Dataverse view specific for identifying only the rows you want retained. Then, create and run an app that has the view to verify before using it as the criteria in your policy. For information about how to create a table view, go to [Create and edit public or system views](../model-driven-apps/create-or-edit-model-driven-app-view.md).

### Setup a retention policy

Power Platform administrators setup retention policies.

> [!IMPORTANT]
> - Once data is moved to long term (non-active) data store it can't be moved back to the active data store.
>
> - When a retention policy is run, the process makes API requests in Microsoft Power Platform. These requests are counted towards the existing API requests available with your plan. More information: [Requests limits and allocations](/power-platform/admin/api-request-limits-allocations)
>
> - To complete this task you must have the Power Platform administrator role.

1. [Ensure the table has been enabled for long term retention](#ensure-the-table-has-been-enabled-for-long-term-retention).
1. Sign into [Power Apps](https://make.powerapps.com/?utm_source=padocs&utm_medium=linkinadoc&utm_campaign=referralsfromdoc), and then on the left navigation pane select **Retention policies**. [!INCLUDE [left-navigation-pane](../../includes/left-navigation-pane.md)]
1. On the command bar, select **New retention policy**.
1. Complete the following properties for the retention policy:
   - **Table**. Select the parent root table that will be use to set up a policy to retain historical cold data in long term storage.
   - **Name**. Enter a name for the retention policy.
   - **Criteria**. Select a view from the list. The view should have been previously created and tested to ensure the right historical data was selected. [Determine Dataverse views for policy criteria](#determine-dataverse-views-for-policy-criteria)
   - **Schedule - Start date**. Enter the date you want the policy to run for the first time. The policy runs during the off hours of your environment’s region.
   - **Frequency**. The choices available are **Once**, **Daily**, **Weekly**, **Monthly**, and **Yearly**.
   :::image type="content" source="media/data-retention-policy.png" alt-text="Create a data retention policy" lightbox="media/data-retention-policy.png":::
1. Select **Save**.

Now you can view and manage the policy. More information: [Manage data retention policies](data-retention-manage.md)

About policy runs:

- The parent table and all cascade related records from child tables, of the parent, will be marked and retained as cold data in Dataverse long term storage.
- Logic associated with an existing delete action of any table (parent and children) will always be executed during the policy run.
- A policy run can take from 24-48 hours irrespective of the data volume. Data retention policies are given a low priority by the platform. Dataverse will always run the retention process in the background to avoid any impact on other platform services, such as apps and flows.

## Next steps

[Manage data retention policies](data-retention-manage.md)