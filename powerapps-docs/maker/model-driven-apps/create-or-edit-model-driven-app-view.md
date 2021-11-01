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
# Create and edit public model-driven app views

Model-driven apps can contain a range of views, so that app users can see the most suitably presented and filtered version of the table that they are investigating.  Views can be **Personal**, **System** or **Public**.

> [!NOTE]
   >   Views are tied a given table however we can select this during the process of creating a model driven app.  By default ALL views will be made available.

:::image type="content" source="media/create-or-edit-model-driven-app-view/switch-views.gif" alt-text="Configure views in model-driven apps":::

> [!TIP]
> For a general introduction into views please read [Understand views in model-driven apps](create-edit-views.md)

## Create a public view in Power Apps
Public views are available to users as when reviewing a table.  App makers can create and configure these using Power Apps.

> [!NOTE]
> Public views created in Power Apps that include **Contains data** or **Does not contain data** filters will not appear in the list of saved views in Advanced Find.

1. Sign in to [Power Apps](https://make.powerapps.com/?utm_source=padocs&utm_medium=linkinadoc&utm_campaign=referralsfromdoc).
1. Select **Solutions** in the left navigation.

1. Create a new solution by selecting **New solution** or select **edit** in the ellipses (**...**) menu of an existing solution. For more  information on creating a model-driven app see:
   - [Create a model driven app](create-model-driven-app.md)
   - [Add a table to a solution](../data-platform/data-platform-create-entity)

From within the solution there are two ways to edit views. *App Designer* and Tables

## Edit public views through tables

In the solution that we opened earlier create a new table or find an existing table that where the public views need to be edited.

1. Expand **Data**, select **Tables**, select the table required, and then select the **Views** tab.
1. On the toolbar, select **Add view**.
:::image type="content" source="media/add-view.png" alt-text="Add view to table":::
1. On the **Create a view** dialog box, enter a name and, optionally, a description, and then select **Create**.
:::image type="content" source="media/create-a-view-dialog.png" alt-text="Create a view":::
1. In the view designer, select **+ View column** to add additional columns needed within the view. Or alternatively, select Table columns in the left navigation and drag the table columns into your view.

   ![Add column.](../data-platform/media/add-column-to-view.png)

   > [!TIP]
   > The **Default** view in the **Add column** pane displays all columns. If preferred, select **Standard** or **Custom** to display a subset of columns.
   > :::image type="content" source="media/display-all-columns.png" alt-text="Select All to display all columns":::
1. In the view designer, the following tasks can be performed:

   - To change the column filtering select the header of the column where the filter is required, and then in the dropdown select **Filter by**.
   - To change the column sorting select the header of the column where sorting is needed then select **Sort A-Z** or **Sort Z-A** or **Sort descending** or **Sort ascending**.  
   - Configure column width by clicking and dragging the column to the desired position.
   - Reorder columns by dragging a column to the desired position.
    > [!NOTE]
    > Depending on the data type of the column the term **Sort A-Z**/**Sort Z-A** or **Sort ascending**/**Sort descending** is used

    > [!TIP]
    > It is also possible to change column order by clicking on the column header and selecting **Move Right** or **Move Left**.
2. Select **Publish** to save the view and make it available for other users in your organization.

## Next steps

[Configure columns in model-driven app views](choose-and-configure-columns.md)<br />
[Creating and editing view filters](create-edit-view-filters.md)<br/>
[Sorting records within views](configure-sorting.md)


