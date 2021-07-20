---
title: "Create and edit public model-driven app views | MicrosoftDocs"
description: "Learn how to create or edit public or system model-driven app views."
ms.date: 07/04/2021
ms.service: powerapps
ms.subservice: mda-maker
ms.topic: tutorial
author: Joel-Lindstrom
ms.author: v-ljoel
ms.reviewer: matp
---
# Create and edit public model-driven app views

In Power Apps, views define how records for a specific table are displayed. A view defines the following behavior:
- The columns, also known as attributes, to display.
- The width of the columns in the view.
- How the records are sorted by default.
- Which filters are applied to determine the records that appear in the list by default.

Typically, views are classified into three types:
- **Personal**: Individual users can create personal views according to their unique requirements. These views are visible only to the user who created them and anyone they choose to share them with.  
- **Public**: As an app maker, you can create and edit public views to fit your organizational requirements. These views are available in the view selector, and you can use them in subgrids in a form or as a list in a dashboard.
- **System**: As an app maker, you can also modify system views to meet the requirements of your organization. These are special views that the application depends on: they exist for system tables or are automatically created when you create custom tables. These views are available to some or all users, depending on their privileges.

More information: [Understand model-driven app views](create-edit-views.md)

A drop-down list of views is commonly displayed in an app so that people have options for different views of table data, such as the Donations table in the Fundraiser sample app.
:::image type="content" source="media/create-or-edit-model-driven-app-view/system-views-picker.png" alt-text="Select a system view from the view picker.":::

The records that are visible in individual views are displayed in a list, sometimes called a grid, which frequently provides options so that people can change the default sorting, column widths, and filters to more easily see the data that's important to them. Views also define the data source for charts that are used in the application.

In this tutorial, we perform several tasks required to work with views, such as create a public view, add an existing view to an app, and change columns, filters, and sort order for a view.

## Create a public view in Power Apps

In this exercise, you create a public view for the account entity. You then add this view to an app.

1. Sign in to [Power Apps](https://make.powerapps.com/?utm_source=padocs&utm_medium=linkinadoc&utm_campaign=referralsfromdoc).
    
1. Expand **Data**, select **Tables**, select the **Account** table, and then select the **Views** tab.
    
1. On the toolbar, select **Add view**.

1. On the **Create a view** dialog box, enter *Accounts with revenue more than 50 K* as the **Name**. Optionally, enter a description, and then select **Create**.
    
1. In the view designer, select **+ View column** and add the **Address1: City** column to the view.

   > [!TIP]
   > The **Default** view in the **Add column** pane displays the commonly used columns. If the column you want isn’t listed, select **All** to display additional columns.

   ![Select All to display all columns](media/create-or-edit-model-driven-app-view/create-a-public-view-in-power-apps-2.png "Select All to display all columns")

1. Repeat the previous step by selecting **Add column** and add the following additional columns to the view: 
   - **Address 1: Country/Region**
   - **Address 1: Primary Contact**
   - **Annual Revenue**

1. Change the column filtering for the **Annual Revenue** field by selecting the header of the column, and then in the dropdown select **Filter by**. Select **Greater than** for the operator and then enter *50000* for the value. Select **Apply**. 
   :::image type="content" source="media/create-or-edit-model-driven-app-view/accounts-more-50k-rev.png" alt-text="Add a filter for accounts with more than 50,000 revenue.":::
   Notice the view in the designer reacts to the filter.
1. Change the column sorting to sort by the most to least revenue. To do this, select the header of the **Annual Revenue** column, and then select **Larger to smaller**. Notice for text-based columns the sort options are **Sort A to Z** and **Sort Z to A**.

1. Explore additional changes you can make to the view.
   - Increase a column width by selecting just to the right of the column heading you want to increase and drag the column to the right.
   - Reposition columns by dragging a column to the position you want to move it to. For example, select the **Primary Contact** column header and drag it between the **Account Name** and **Address 1: City** columns.

   > [!NOTE]
   >    You can also change column order by selecting the column header and then select **Move Right** or **Move Left**.

1. Select **Save**, and then select **Publish** to make the view available for other users in the environment.

## Add the view in the app designer

1. In Power Apps, select **Apps** from the left navigation pane, select **...** next to the unmanaged app you want, and then select **Edit** > **Edit in preview**. If you don't have an app to use, [Build your first model-driven app](build-first-model-driven-app.md).

1. In the **Pages** section of app designer, select **Account view**.
1. In the right **Properties** pane, select **Manage views**, select the following views, and then select **Save**.
   - **Active Accounts**
   - **Inactive Accounts**
   - **Accounts with revenue more than 50K**
   :::image type="content" source="media/create-or-edit-model-driven-app-view/select-view-for-app.png" alt-text="Select the views you want to display":::
1. Select **Publish** to save and publish the app.

### Display the view in an app

To see your view in the app, on the app designer command bar, select **Play**. Notice that the view is displayed and the additional **Active Accounts** and **Inactive Accounts** views are also available by selecting the view selector.
:::image type="content" source="media/create-or-edit-model-driven-app-view/view-displayed-in-app.png" alt-text="Views available from an app":::

## Open and add the view in the classic app designer

1. In Power Apps, select **Apps** from the left navigation pane, select **...** next to the unmanaged app you want, and then select **Edit** . If you don't have an app to use, [Build your first model-driven app](build-first-model-driven-app.md).
    
1. In the app designer **Entity View** section, select **Views**.

   ![Table View section select Views](media/create-or-edit-model-driven-app-view/open-and-add-a-view-in-the-app-designer-1.png "Table View section select Views")

1. On the right **Components** tab, by default, all views are selected. To select specific views to display in the app, clear the **All** checkbox.

   ![select specific views to display in the app](media/create-or-edit-model-driven-app-view/open-and-add-a-view-in-the-app-designer-2.png "select specific views to display in the app")
    
1. To add an existing view to your app, select it from the list of views, or to create a new view from the app designer, select **Create New**.

   > [!NOTE]
   > Views are displayed based on the table that you have selected. For example, when you select **Account**, views that are related to the account table are displayed.

### Add a column to your view in the classic app designer

Views display records from a table that contains rows and columns. Each record is a row, and the columns that are displayed from the record are determined by the columns you add to the view.

1. In app designer, select **Views**, then on the right **Components** pane place your mouse cursor over the view, and then select **edit** (pencil button).
    :::image type="content" source="media/create-or-edit-model-driven-app-view/edit-view.png" alt-text="Edit a view":::
1. On the **Components** tab in the view designer, select the **Column Attributes** list for the **Primary Entity**.

   ![Add a column](media/create-or-edit-model-driven-app-view/open-and-add-a-view-in-the-app-designer-3.png "Add a column")
    
1. From the list of columns, select the column you want, such as the **Address 1: State/Province** column,and drag it to the view heading. You can also add the column by double-clicking it.
    :::image type="content" source="media/create-or-edit-model-driven-app-view/add-address1-state-column.png" alt-text="Add the Address 1: State/Province column to the view":::
1. Repeat step 3 until you've added all the columns you want to display in your view. As you add columns, you can drag them to any position among existing column headings. You can also move columns around after you add them to your view by dragging the column heading to the column heading where you want to move it.
1. Select **Save and Close** on the command bar, to save the view and return to the app designer.

### Define filter criteria in the classic app designer

You can set filter criteria so that only a subset of the records is displayed in a view. When a user opens the view, only the records that meet the defined filter criteria are displayed. You can select columns from both the primary and related tables to filter on.

1. In app designer, select **Views**, then on the right **Components** pane place your mouse cursor over the view, and then select edit (pencil button).
    :::image type="content" source="media/create-or-edit-model-driven-app-view/edit-view.png" alt-text="Edit a view":::
1. In the view designer, expand the **Filter Criteria** section, and then select **Add Filter**.

   ![Set Filter Criteria](media/create-or-edit-model-driven-app-view/define-filter-criteria-in-app-designer-1.png "Set Filter Criteria")

1. Select the **Address1: State/Province** column from the drop-down list in the first column.

1. Select the **Equals** operator from the drop-down list in the second column.

1. Enter *TX* as the value to filter by in the third column.

   ![Set Filter Criteria Operator](media/create-or-edit-model-driven-app-view/define-filter-criteria-in-app-designer-2.png "Set Filter Criteria Operator")
   
   Notice how the view now shows accounts with annual revenue greater than $50,000 in the state of Texas (TX).
1. Select **Save and Close** on the command bar, to save the view and return to the app designer.
<!-- You can also filter data based on the attributes of related tables in addition to the
primary table.

1. On the **Components** tab, select the **Column Attributes** list for **Related Table**, select a related table from the drop down list, and then choose the table you want. This will add a separate section.
    
2.  Repeat steps 2 through 5 from the previous procedure.

More information: [Create and edit relationships between tables](https://docs.microsoft.com/powerapps/maker/data-platform/create-edit-entity-relationships)  -->

#### Group multiple filters in the classic app designer

You can add multiple filters to your view if you want to filter records by using more than one column.

1. Select the filters that you want to group. 
   ![Set Group Filter](media/create-or-edit-model-driven-app-view/group-multiple-filters-in-app-designer-1.png "Set Group Filter")

1. Select **Group And** or **Group Or** to group the filters. 
   ![Group Filter Selection](media/create-or-edit-model-driven-app-view/group-multiple-filters-in-app-designer-2.png "Group Filter Selection") 
   
   When you select **Group And**, only records that meet both criteria are displayed in the view. When you select **Group Or**, records that meet any of the filter criteria are displayed. For example, to show only records that have priority of **High** or **Normal**, and a status of **Active**, select **Group And**.

To remove the filter from a group, select the group, and then select **Ungroup**.

### Set primary and secondary sort order for columns in the classic app designer

When a view is opened, the records displayed are sorted in the order you set when you created the view. By default, records will be sorted according to the first column in a view when no sort order is selected. You can choose to sort on a single column, or you can choose two columns—one primary and one secondary—to sort by. When the view is opened, the records are first sorted by the column you want to use for primary sort order, and then by the column you want to use for the secondary sort order.

> [!NOTE]
> You can only set primary and secondary sort order for column attributes you added from the primary table.

1. In app designer, select **Views**, then on the right **Components** pane place your mouse cursor over the view, and then select edit (pencil button).
    :::image type="content" source="media/create-or-edit-model-driven-app-view/edit-view.png" alt-text="Edit a view":::
1. In the **Columns** area of the view designer, select the column heading you want to use for sorting, such as **Business Phone**, select the down arrow, and then choose **Primary Sort** or **Secondary Sort**.

   ![Sort Record](media/create-or-edit-model-driven-app-view/set-primary-and-secondary-sort-order-for-columns-in-app-designer-1.png "Sort Record")

If you remove the column you chose for the primary sort order, the column you chose for the secondary sort order becomes the primary.

### Edit a public or system view in app designer

You can change the way a public or system view is displayed by adding, configuring, or removing columns.

1. In the **Views** list for a table, select the **Show list of references** down arrow 
 ![Drop Down](media/create-or-edit-model-driven-app-view/edit-a-public-or-system-view-in-app-designer-2.png "Drop Down").
   > [!NOTE]
   > The down arrow is only displayed when the table views are not configured to use **All** views.

1. Place your mouse cursor over the ![Open view Designer pencil icon](media/create-or-edit-model-driven-app-view/edit-a-public-or-system-view-in-app-designer-3.png "Open view Designer"), and select it, to **Open the View Designer**. 

   ![change the way a public or system view is displayed](media/create-or-edit-model-driven-app-view/edit-a-public-or-system-view-in-app-designer-1.png "change the way a public or system view is displayed")

When you edit a public or system view, you must save and publish your changes before they will be visible in the application.

### See also

[Create a model-driven app with the app designer](create-model-driven-app.md) <br />
[Design custom business apps by using the app designer](design-custom-business-apps-using-app-designer.md)
