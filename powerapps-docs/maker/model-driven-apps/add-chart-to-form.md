---
title: Add a chart to a model-driven app main form in Power Apps | MicrosoftDocs
description: Learn how to add a chart to a main form
Keywords: 
author: Mattp123
applies_to: 
  - "Dynamics 365 (online)"
  - "Dynamics 365 Version 9.x"
  - "powerapps"
ms.author: matp
manager: kvivek
ms.reviewer: matp
ms.date: 07/27/2020
ms.service: powerapps
ms.topic: how-to
ms.assetid: 
search.audienceType: 
  - maker
search.app: 
  - PowerApps
  - D365CE
---
# Add a chart to a form

[!INCLUDE [cc-data-platform-banner](../../includes/cc-data-platform-banner.md)]

You can add a chart to a form or change an existing list to a chart. For example, you can change the Child Accounts filtered sub-grid to display a chart instead of a list on the account main form.

> [!div class="mx-imgBorder"] 
> ![Account main form child accounts grid.](media/main-form-child-accts-chart.png)

1. Sign into Power Apps, select **Solutions**, open the solution with the table you want, and then select the **Forms** tab. 
2. Open the form where you want to add a chart or change a list to a chart, on the form designer command bar, and then select **Switch to classic**. 
3. Add a sub-grid to the form, or to change an existing list in a sub-grid, double-click a sub-grid on the form. 
4.  On the **Set Properties** page for the sub-grid, select the **Show Chart Only** option. When enabled, this option displays the view in a chart format. 
      > [!div class="mx-imgBorder"] 
      > ![Show chart only.](media/form-show-chart-only.png)

5. On the **Set Properties** page for the sub-grid, consider from the following options that affect how the chart is displayed, and then select **OK**. For more information about these properties, see [Set properties for a model-driven app chart or list included in a dashboard](set-properties-chart-list-included-dashboard.md).  
    - **Records**: 
         - **Only Related Records**: Shows the rows based on the selected view, but only with rows related to the table row.  
         - **All Row Types**: Shows all the rows based on the selected view. 
    - **View Selector**: When enabled, users can change to a different view, which displays the chart with different data and filtering that are associated with the view:
         -  **Off**. Don’t display the view selector. You or other users won’t be able to change views at runtime.
         - **Show All Views**. Provide a full list of views associated with the value set in the **Table** property.
         - **Show Selected Views**. Select this setting to limit the list of views available at runtime. To select the specific views to be displayed, hold down the Ctrl key and tap or select each view you want to include.
     - **Display Chart Selection**: When enabled, users can change the type of chart (column, bar, pie, etc.) on the form. If the user changes the type of chart, the settings aren’t saved. The chart type reverts to the **Default Chart** setting when the form is closed.

5. Publish your customization. More information: [Publish changes](../data-platform/create-solution.md#publish-changes)

### See also
[Create a model-driven app system chart](create-edit-system-chart.md)

[!INCLUDE[footer-include](../../includes/footer-banner.md)]