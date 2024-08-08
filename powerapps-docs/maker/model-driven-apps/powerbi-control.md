---
title: Use the Power BI report control to add a report to a form with Power Apps
description: The Power BI report control lets you add a report to a model-driven app form. 
author: Mattp123
ms.author: matp
ms.service: powerapps
ms.subservice: mda-maker
ms.topic: how-to
ms.date: 08/08/2024
ms.custom: template-how-to
---
# Use the Power BI report control to add a report (preview)

> [!IMPORTANT]
> The Power BI report control is retired on July 31, 2024. We recommend removing all Power BI report controls from your model-driven apps and use Power BI system dashboard embedding instead. More information: [Create or edit a Power BI embedded system dashboard](create-edit-powerbi-embedded-page.md)

Add a Power BI report to a model-driven app form using the Power BI report control. This unlocks the power to aggregate data across systems, and tailor it down to the context of a single record.

> [!IMPORTANT]
> This is a preview feature. More information: [Model-driven apps and app management](../powerapps-preview-program.md#model-driven-apps-and-app-management)

:::image type="content" source="media/create-edit-powerbi-embedded-page/pbi-report-control-form.jpg" alt-text="Power BI report on a form":::

## Prerequisites

- Microsoft Dataverse environments must have the Power BI Extensions solution installed. More information: [Install an app in the environment view](/power-platform/admin/manage-apps#install-an-app-in-the-environment-view)
- The Power BI report control only works with main form types.

## Add and configure the Power BI control on a form

1. In the form designer, select **Components** on the left navigation pane, expand **Power BI**, and then select **Power BI Report**.
1. Choose from the following properties: 
   - **Report**. Select the Power BI report that you want displayed on the form. More information: [Create Power BI report and dataset components](create-edit-powerbi-report-dataset-components.md).
   - **Show filter pane**. When **True**, displays the filter pane in the Power BI report.
   - **Expand filter pane by default**. When **True**, expands the filter pane by default.
   - **Save filter updates**. When **True** and someone leaves the report, the filter will be saved and reapplied when the person returns.
   - **Show action bar**. When **True**, displays the report’s action bar that contains commands such as File, Export, and Share.
   - **Show bookmarks bar**. When **True**, displays the report’s bookmarks bar.
   - **Show page navigation**. When **True**, displays the report’s page navigation.
   - **Page navigation position**. When **True** determines which position, either left or bottom, to display the page navigation.
   - **Background**.  Set the background to be the default white background or select **Transparent**.
   - **JSON filter string**. The JSON filter string applied on the Power BI report for contextual filtering. More information: [Embed with contextual filtering](embed-powerbi-report-in-system-form.md#embed-with-contextual-filtering)
   - **Show component on**. By default, all client app types **Web**, **Phone**, and **Tablet** are enabled to display the form. Clear the client types where you don’t want the Power BI report displayed.
1. Select **Done**.
1. **Save** and then **Publish** the form.

## Next steps

[Power BI reporting in model-driven apps and Dataverse](reporting-overview.md#power-bi-reporting)
