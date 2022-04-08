---
title: "Create or edit a model-driven app system chart in Power Apps | MicrosoftDocs"
description: "Learn how to create a system chart for a model-driven app"
ms.custom: ""
ms.date: 07/08/2021

ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "how-to"
applies_to: 
  - "Dynamics 365 (online)"
  - "Dynamics 365 Version 9.x"
  - "PowerApps"
author: "joel-lindstrom"
ms.subservice: mda-maker
ms.author: "matp"
manager: "kvivek"
ms.reviewer: matp
search.audienceType: 
  - maker
search.app: 
  - "PowerApps"
  - D365CE
---
# Create a model-driven app system chart



In this article you learn how to create a system chart. System charts are organization-owned charts, which makes them available to anyone with access to read the data running the app. System charts can't be assigned or shared with specific app users.

> [!Note]
> Model-driven apps not configured to display **All** charts for a table will need newly created charts selected for the table within the app designer. More information: [Add table assets](add-edit-app-components.md#add-table-assets)

## Create a new chart

1. Sign in to [Power Apps](https://make.powerapps.com/?utm_source=padocs&utm_medium=linkinadoc&utm_campaign=referralsfromdoc).
1. On the left navigation pane, select **Dataverse** and then the table which requires a chart.

1. Select **Charts** from the menu, and then select **Add Chart**.

   :::image type="content" source="media/create-table-chart.png" alt-text="Steps to introducing a chart into a table.":::

   A new window opens where you can create a chart.

2. Specify the type of chart, and how the data is displayed in the chart.

   - Enter the chart name, such as *Number of employees by account*.
   - In the **Select Column** dropdowns:
      -  In the **Legend Entries (Series)** dropdown list select a column, such as **Number of Employees**.
      - In the **Horizonal (Category) Axis** dropdown list select a column, such as **Account Name**.

   -   Add a description to identify the purpose of the chart, such as *This column chart displays the number of employees by account name*.

   :::image type="content" source="media/add-and-customize-visualizations-in-model-driven apps/add-and-customize-visualizations-in-model-driven-apps-3.png" alt-text="Description to identify the purpose of the system chart you create.":::

3. Select **Save and Close**.

The **Number of employees by account** chart is now displayed in the app designer list of charts available for the account table.

## View your visualization in a model-driven app

Now that the chart has been created, it can be used to visualize table data in the model-driven app. Follow these steps to view the chart:

1. Open a model-driven app that contains your table via a solution or open the app directly from the **Apps** area.
2. Select **...** next to the app, and then select **Play**. The model-driven app opens in a separate browser tab.

4. On the left navigation pane, select a table such as **Accounts**.

5. On the command bar, select **Show Chart**.

   The chart pane opens.

   :::image type="content" source="media/add-and-customize-visualizations-in-model-driven apps/view-your-visualization-in-your-model-driven-app-3.png" alt-text="Chart selector.":::

6. By selecting the dropdown chart list, any of the system charts in the app will be available to select.

   The chart appears in-line with the data view.

   :::image type="content" source="media/add-and-customize-visualizations-in-model-driven apps/view-your-visualization-in-your-model-driven-app-2.png" alt-text="Your system chart named Number of employees by account is displayed.":::

Use your chart:
- Select a bar on the chart to filter the data in the view.
- Refresh the chart to display other data by changing the view.
- Add the chart to a model-driven app dashboard. More information: [Create or edit model-driven app dashboards](create-edit-dashboards.md)

> [!NOTE] 
> If the chart is not visible in the dropdown chart list then the model-driven app has been created with specific charts associated with it. To resolve this, open the model-driven app in design mode, select charts, and then select your newly created chart. 
> :::image type="content" source="media/add-and-customize-visualizations-in-model-driven apps/add-and-customize-visualizations-in-model-driven-apps-1.png" alt-text="Select Chart from within app":::
> Then save and publish your app.

## Known chart creation issues

In the chart designer, adding an order by on certain calculated columns is not supported and will cause an error. The calculated columns causing this are using another calculated column, a related table column, or a local column on the table.

## Next steps

[Create or edit dashboards](create-edit-dashboards.md)

[!INCLUDE[footer-include](../../includes/footer-banner.md)]
