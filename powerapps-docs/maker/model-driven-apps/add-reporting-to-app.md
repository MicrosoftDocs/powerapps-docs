---
title: "Add reporting features to your model-driven app" 
description: Learn how to add reporting to your model-driven app in Power Apps.
ms.custom: ""
ms.date: 09/17/2024
ms.reviewer: ""
ms.topic: "how-to"
author: "Mattp123"
ms.assetid: b4098c96-bce1-4f57-804f-8694e6254e81
ms.subservice: mda-maker
ms.author: "matp"
search.audienceType: 
  - maker
---
# Add reporting features to your model-driven app

Power Apps apps can include paginated style reports that provide useful business information to the user. These reports are based on SQL Server Reporting Services and provide the same set of features that are available for typical SQL Server Reporting Services reports.

:::image type="content" source="media/progress-against-goals-report.png" alt-text="Progress against goals standard report" lightbox="media/progress-against-goals-report.png":::

System reports are available to all users. Individuals who create or otherwise own reports can share them with specific colleagues or teams, or can make the reports available to the organization, so that all users can run them. These reports use FetchXML queries that are proprietary to Microsoft Dataverse and retrieve data to build the report. Reports that you create in a Power Apps app are Fetch-based reports.

> [!NOTE]
> Report features don't work with canvas apps or model-driven apps running on mobile devices, such as tablets and phones.

## Add reporting to a model-drive app

You can add fetch-based reporting functionality to your app so that users can run, share, create, and edit reports. To do this, you add the report table to your app.

1. Sign in to [Power Apps](https://make.powerapps.com/?utm_source=padocs&utm_medium=linkinadoc&utm_campaign=referralsfromdoc) select **Solutions**, open the solution you want, and then open the model-driven app where you want to add reporting for editing.
2. In the app designer, select **New** > **Dataverse table**. 
3. In the **Select a table** list, select the **Report** table, and then select **Add**.
4. Select **Save**, and then select **Publish**.

Now the app displays a **Reports** page where users can view, run, assign, share, and edit the reports they have permission to as well as create new reports using the report wizard.

:::image type="content" source="media/report-feature-in-app.png" alt-text="Model-driven app with reporting added" lightbox="media/report-feature-in-app.png":::

## Options for creating new reports

You can create a new report in one of two ways:

- Use the Report Wizard. Open a model-driven app that is enabled for reporting, select the **Reports** page, and then select **New** to open the Report Wizard to create a new report. The Report Wizard can create table and chart reports, including drill-through reports and top N reports. More information: [Create a report using the Report Wizard](../../user/create-report-with-wizard.md) 
- Use the Report Authoring Extension. You can write new or customize existing fetch-based Reporting Services reports with Visual Studio, SQL Server Data Tools, and the Report Authoring Extension. More information: [Create a new report using SQL Server Data Tools](/dynamics365/customer-engagement/analytics/create-a-new-report-using-sql-server-data-tools)

## Report visibility

Standard table reports, such as the Accounts Summary report for the account table, are available to all app users. Users who own reports can share them with specific colleagues or teams. System administrators and system customizers can make reports available with organization-wide visibility, so that all users can use them. For information about how to share a report, see [Share a report with other users and teams](../../user/work-with-reports.md#share-a-report-with-other-users-or-teams). 

## Reports in solutions

Reports are solution aware. Adding a report as a component to a solution makes it become a single unit of software that extends Power Apps functionality and the user interface. Only reports that are visible to the organization can be added to solutions.

To find if a report is viewable to the organization: In the list of reports, open a model-driven app, select a report, and then select **Edit**. On the **Administration** tab, determine whether **Viewable By** is set to **Organization**.

> [!div class="mx-imgBorder"] 
> ![Organization level report visibility.](media/report-scope.png "Organization level report visibility")

You can add, import, or export snapshots of reports as part of a solution. In model-driven apps, reports, sub reports, report category, report display area, and report-related row type are considered as components of a report set. When you import a solution update in non-overwrite mode, any updates by the solution to a report will be ignored if any component of the report set has been customized.

## Related articles

[Work with reports](../../user/work-with-reports.md)<br/>
[Create a report using the Report Wizard](../../user/create-report-with-wizard.md)<br/>
[Add a report from outside Power Apps](../../user/add-existing-report.md)<br/>
[Edit the default filter of a report](../../user/edit-report-filter.md)<br/>


[!INCLUDE[footer-include](../../includes/footer-banner.md)]
