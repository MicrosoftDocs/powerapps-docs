---
title: "Create and edit public model-driven app views | MicrosoftDocs"
description: "Learn how to create or edit public or system model-driven app views."
ms.date: 07/04/2021
ms.service: powerapps
ms.subservice: mda-maker
ms.topic: tutorial
author: Joel-Lindstrom
ms.author: matp
ms.reviewer: matp
---
# Create and edit public or system views

Model-driven apps can contain a range of views, so that app users can open the most suitably presented and filtered version of the table.  Views can be **Personal**, **System** or **Public**.

> [!NOTE]
   >   Views are tied to a given table. However, you can select views during the process of creating a model driven app. By default, ALL views are made available in an app.

:::image type="content" source="media/create-or-edit-model-driven-app-view/switch-views.gif" alt-text="Configure views in model-driven apps":::

> [!TIP]
> For a general introduction into views, go to [Understand views in model-driven apps](create-edit-views.md)

## Create a public view in Power Apps

Public views are available for users to display table records. App makers can create and configure public views using Power Apps.

> [!NOTE]
> Public views created in Power Apps that include **Contains data** or **Does not contain data** filters will not appear in the list of saved views in Advanced Find.

## Edit public views from a table

In the solution that we opened earlier, create a new table or find an existing table where the public views need to be edited.

1. Sign in to [Power Apps](https://make.powerapps.com/?utm_source=padocs&utm_medium=linkinadoc&utm_campaign=referralsfromdoc).
1. Select an [environment](model-driven-app-glossary.md#environment)

   > [!NOTE]
   > It is best practice to create tables inside a custom solution. More information: [Solution (glossary)](model-driven-app-glossary.md#solution)

1. Expand **Data**, select **Tables**, select the table you want, and then select the **Views** tab.  If using a custom solution, open the solution, open then table, and then select the **Views** tab.
1. On the toolbar, select **Add view**.
   :::image type="content" source="media/add-view.png" alt-text="Add view to table":::
1. On the **Create a view** dialog, enter a name and, optionally, a description, and then select **Create**.
   :::image type="content" source="media/create-a-view-dialog.png" alt-text="Create a view":::
1. In the view designer, select **+ View column** to add additional columns needed within the view. Or, select **Table columns** in the left navigation and drag the table columns into your view.

   ![Add column.](../data-platform/media/add-column-to-view.png)

   > [!TIP]
   > The **Default** view in the **Add column** pane displays all columns. If preferred, select **Standard** or **Custom** to display a subset of columns.
   > :::image type="content" source="media/display-all-columns.png" alt-text="Select All to display all columns":::
1. In the view designer, the following tasks can be performed:

   - To change the column filtering select the header of the column where the filter is required, and then in the dropdown list select **Filter by**.
   - To change the column sorting select the header of the column where sorting is needed then select **Sort A-Z**, **Sort Z-A**, **Sort descending**, or **Sort ascending**.  
   - Configure column width by selecting and dragging the column to the desired position.
   - Reorder columns by dragging a column to the desired position.
    > [!NOTE]
    > Depending on the data type of the column the term **Sort A-Z**/**Sort Z-A** or **Sort ascending**/**Sort descending** is used

    > [!TIP]
    > It is also possible to change column order by selecting the column header and then selecting **Move Right** or **Move Left**.
2. Select **Publish** to save the view and make it available for other users in your organization.

### Next steps

[How to configure view columns](choose-and-configure-columns.md)

[Learn about sorting within views](configure-sorting.md)

[Learn about filtering views](create-edit-view-filters.md)

[Make views editable using sub-grids](make-grids-lists-editable-custom-control.md)

[!INCLUDE[footer-include](../../includes/footer-banner.md)]