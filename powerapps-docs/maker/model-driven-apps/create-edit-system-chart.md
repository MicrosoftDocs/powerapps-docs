---
title: "Create or edit a model-driven app system chart in Power Apps"
description: "Learn how to create a system chart for a model-driven app."
ms.custom: ""
ms.date: 05/05/2026
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "how-to"
applies_to: 
  - "Dynamics 365 (online)"
  - "Dynamics 365 Version 9.x"
  - "PowerApps"
author: "Hillaryyaory-microsoft"
ms.subservice: mda-maker
ms.author: "hillaryyaor"
ms.reviewer: matp
contributors: anshuman-ms
search.audienceType: 
  - maker
---
# Create or edit a model-driven app system chart

In this article you learn how to create a system chart. System charts are organization-owned charts, which makes them available to anyone with access to read the data running the app. System charts can't be assigned or shared with specific app users.

> [!NOTE]
> Model-driven apps not configured to display **All** charts for a table need newly created charts selected for the table within the app designer. More information: [Add table assets](add-edit-app-components.md#add-table-assets)

## Create a chart

1. Sign in to [Power Apps](make.powerapps.com), and then on the left navigation pane, select **Solutions**. 
1. Open the solution that has the table that requires a chart, open the table, and then select **Charts** under **Data experiences**.
1. Select **New chart**.
1. Specify the type of chart, and how the data is displayed in the chart.
1. The chart designer opens. In the dialog choose from the following legend entries: 
   - In the **Column** dropdown list, select a column, such as *Number of Employees*. The column determines the vertial axis for the chart.
   - In the **Aggregate** dropdown list dialog, select aggregate value type, such as Average. <!--What do the different options do? -->
   - In the **Chart type** dropdown list, select a type of chart to display, such as Column, Bar, Pie, or Donut.
   - Optionally, set minimum and maxium values. <!-- What does this do?-->
1. Select **Next**.
1. Select a column for the category The category determines the horizontal axis for the chart, such as account name in this example. Select **Apply**.
   :::image type="content" source="media/create-edit-system-chart/chart-for-number-employees.png" alt-text="Account number of employees chart":::
1. To save the chart, in the chart designer, select **Save**.
1. Select **Publish** to make the chart available to others.

## Edit a chart

1. Sign in to [Power Apps](make.powerapps.com), and then on the left navigation pane, select **Solutions**. 
1. Open the solution that has the table that includes the chart you want to edit, open the table, and then select **Charts** under **Data experiences**.
1. In the list of charts, open the chart that you want to edit.
1. Make the changes you want for the chart in the chart designer. More information: [Create a chart](#create-a-chart)

## Switch to classic experience

You can open the chart in the classic chart designer.

### Edit a chart using the classic experience

While working in the modern chart designer, select **Switch to Classic** on the command bar.

1. Edit the chart, such as specifying the type of chart, and how the data is displayed in the chart.

   - In the **Select Column** dropdowns:
      - In the **Legend Entries (Series)** dropdown list select a column, such as **Number of Employees**.
      - In the **Horizonal (Category) Axis** dropdown list select a column, such as **Account Name**.

   :::image type="content" source="media/add-and-customize-visualizations-in-model-driven apps/add-and-customize-visualizations-in-model-driven-apps-3.png" alt-text="Description to identify the purpose of the system chart you create.":::

1. Select **Save and Close**.

> [!NOTE]
> When creating a chart, you can preview it with a selected view. The view isn't permanently associated with the chart. The next time you open the chart, the chart displays using the configured default view. You can change the view to display the chart for the data from a different view.

## Maximum number of records displayed in a chart

Charts display views that return up to 50,000 records. Views that exceed 50,000 records display the message: The maximum record limit is exceeded. Reduce the number of records. More information: [Reporting infrastructure](reporting-considerations.md#reporting-infrastructure)

## Known chart issues

In the chart designer, adding an order by on certain calculated columns isn't supported and cause an error. The calculated columns causing the issue are using another calculated column, a related table column, or a local column on the table.

If the chart isn't visible in the dropdown chart list, then the model-driven app has been created with specific charts associated with it. To resolve this, open the model-driven app in design mode, select charts, and then select your newly created chart.
> :::image type="content" source="media/add-and-customize-visualizations-in-model-driven apps/add-and-customize-visualizations-in-model-driven-apps-1.png" alt-text="Select Chart from within app":::
> Then save and publish your app.

## Next steps

[Create or edit dashboards](create-edit-dashboards.md)

[!INCLUDE[footer-include](../../includes/footer-banner.md)]
