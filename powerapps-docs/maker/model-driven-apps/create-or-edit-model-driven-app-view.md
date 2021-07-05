---
title: "Create and edit public or system model-driven app views | MicrosoftDocs"
description: "Learn how to create or edit public or system model-driven app views."
ms.date: 07/04/2021
ms.service: powerapps
ms.topic: how-to
author: Joel-Lindstrom
ms.author: v-ljoel
ms.reviewer: matp
---
# Create and edit public or system model-driven app views

In Power Apps, views define how rows for a specific table are displayed. A view defines the following:

-   The columns (attributes) to display

-   The width of the columns

-   How the rows are sorted by default

-   Which filters are applied to determine which rows appear in the list by
    default

Typically, views are classified into three types:

-   **Personal:** Individual users can create personal views according to their personal requirements. These views are visible only to the user who created them and anyone they choose to share them with.
    
-   **Public:** As an app maker, you can create and edit public views to fit your organizational requirements. These views are available in the view selector, and you can use them in sub-grids in a form or as a list in a dashboard.
    
-   **System:** As an app maker, you can also modify system views to meet the requirements of your organization. These are special views that the application depends on: they exist for system tables or are automatically created when you create custom tables. These views are available to some or all users, depending on their permissions.

More information: [Understand views](https://docs.microsoft.com/powerapps/maker/model-driven-apps/create-edit-views)

A drop-down list of views is frequently displayed in the application so that people have options for different views of table data.

The rows that are visible in individual views are displayed in a list, sometimes called a grid, which frequently provides options so that people can change the default sorting, column widths, and filters to more easily see the data that's important to them. Views also define the data source for charts that are used in the application.

## Creating or editing system model-driven apps

In this lesson, we will perform several tasks required to work with views, such as create a public view, add an existing view to an app, and change columns, filters, and sort order for a view.

## Create a public view in Power Apps

In this exercise we will create a view in the Account entity. We will add this view to the app we created in the create model driven app video (insert link)

1.  Sign in to [Power Apps](https://make.powerapps.com/?utm_source=padocs&utm_medium=linkinadoc&utm_campaign=referralsfromdoc).
    
2.  Expand **Data**, select **Tables**, select the **Account** table, and then select the **Views** tab.
    
3.  On the toolbar, select **Add view**.

4.  On the **Create a view** dialog box, enter a name and, optionally, a description, and then select **Create**.
    
5.  In the view designer, select **+ View column** to add additional columns you want to display in the view.

![Add column](media/create-or-edit-model-driven-app-view/create-a-public-view-in-power-apps-1.png "Add column")

  **Tip**: The **Default** view in the **Add column** pane displays the commonly used columns. If the column you want isn’t listed, select **All** to display additional columns.
    
![Select All to display all columns](media/create-or-edit-model-driven-app-view/create-a-public-view-in-power-apps-2.png "Select All to display all columns")

6.  In the view designer, you can perform the follow tasks:

-   To change the column filtering select the header of the column you want to filter, and then in the dropdown select **Filter by**.
-   To change the column sorting select the header of the column you want to filter and then select **Sort A-Z** or **Sort Z-A**.
    
-   Configure column width by selecting and dragging the column to the desired position.

-   Reorder columns by dragging a column to the position you want to move it to.
    
    **Note**: You can also change column order by selecting on the column header and selecting **Move Right** or **Move Left**.

7. Select **Publish** to save the view and make it available for other users in your organization.

## Work with views in app designer

The following sections describe how to create and edit views in app designer.

### Open and add a view in the app designer

The following steps explain how to open and add a view in the app designer.

1.  In Power Apps select **Apps** from the left navigation pane, select **...** next to the **Manage Customers** app, and then select **Edit**.
    
2.  In the app designer **Table View** section, select **Views**.

![Table View section select Views](media/create-or-edit-model-driven-app-view/open-and-add-a-view-in-the-app-designer-1.png "Table View section select Views")

3.  By default, all views will be selected. To select specific views to display in the app, uncheck the **All** checkbox

![select specific views to display in the app](media/create-or-edit-model-driven-app-view/open-and-add-a-view-in-the-app-designer-2.png "select specific views to display in the app")
    
4.  To add an existing view to your app, select it from the list of views.

5.  To create a new view from App Designer, select **Create new**

    **Note**

    Views are displayed based on the table that you have selected. For example, when you select **Account**, views that are related to the Account table are displayed.

More information about the app designer: [Design custom business apps by using the app designer](https://docs.microsoft.com/powerapps/maker/model-driven-apps/design-custom-business-apps-using-app-designer)

### Add a column to your view in app designer

Views display rows in a table that contains rows and columns. Each row is a row, and the columns you display from the row are determined by the columns you add to the view.

1.  In app designer, select the table view that you want and then on the right pane next to the view, select **edit** (pencil button).
    
2.  On the **Components** tab, select the **Column Attributes** list for either the **Primary Table** or **Related Table**.

![Add a column](media/create-or-edit-model-driven-app-view/open-and-add-a-view-in-the-app-designer-3.png "Add a column")
    
3.  From the list, select the attribute you want and drag it to the column heading. You can also add the attribute by double-selecting it.
    
4. Repeat step 3 until you've added all the attributes you want to display in your view.

As you add attributes, you can drag them to any position among existing column headings. You can also move columns around after you add them to your view.

### Define filter criteria in app designer

You can set filter criteria so that only a subset of the rows is displayed in a view. When a user opens the view, only the rows that meet the defined filter criteria are displayed. You can select columns from both the primary and related tables to filter on.

1.  In the app designer, expand the **Filter Criteria** section.

![Set Filter Criteria](media/create-or-edit-model-driven-app-view/define-filter-criteria-in-app-designer-1.png "Set Filter Criteria")

2.  Select **Add Filter**.

3.  Select an attribute from the drop-down list in the first column.

4.  Select an operator from the drop-down list in the second column.

![Set Filter Criteria Operator](media/create-or-edit-model-driven-app-view/define-filter-criteria-in-app-designer-2.png "Set Filter Criteria Operator")

5.  Enter a value to filter by in the third column.

You can filter data based on the attributes of related tables in addition to the
primary table.

1.  On the **Components** tab, select the **Column Attributes** list for **Related Table**, select the **Choose a Table** down arrow in the topmost column, and then choose the table you want. This will add a separate section.
    
2.  Repeat steps 2 through 5 from the previous procedure.

More information: [Create and edit relationships between tables](https://docs.microsoft.com/powerapps/maker/data-platform/create-edit-entity-relationships)

#### Group multiple filters in app designer

You can add multiple filters to your view if you want to filter rows by using more than one column.

1.  Select the filters that you want to group. ![Set Group Filter](media/create-or-edit-model-driven-app-view/group-multiple-filters-in-app-designer-1.png "Set Group Filter")

2.  Select Group And or Group Or to group the filters. ![Group Filter Selection](media/create-or-edit-model-driven-app-view/group-multiple-filters-in-app-designer-2.png "Group Filter Selection") When you select **Group And**, only rows that meet both criteria are displayed in the view. When you select **Group Or**, rows that meet any of the filter criteria are displayed. For example, to show only rows that have priority of High or Normal, and status of Active, select **Group And**.

To remove the filter from a group, select the group, and then select **Ungroup**.

### Set primary and secondary sort order for columns in app designer

When a view is opened, the rows it displays are sorted in the order you set when you created the view. By default, rows will be sorted according to the first column in a view when no sort order is selected. You can choose to sort on a single column, or you can choose two columns—one primary and one secondary—to sort by. When the view is opened, the rows will first be sorted by the column you want to use for primary sort order, and then by the column you want to use for secondary sort order.

**Note**

You can only set primary and secondary sort order for column attributes you added from the primary table.

1.  Select the column you want to use for sorting.

2.  Select the down arrow, and then choose **Primary Sort** or **Secondary Sort**.

![Sort Record](media/create-or-edit-model-driven-app-view/set-primary-and-secondary-sort-order-for-columns-in-app-designer-1.png "Sort Record")

If you remove the column you chose for the primary sort order, the column you chose for the secondary sort order becomes the primary.

### Edit a public or system view in app designer

You can change the way a public or system view is displayed by adding, configuring, or removing columns.

![change the way a public or system view is displayed](media/create-or-edit-model-driven-app-view/edit-a-public-or-system-view-in-app-designer-1.png "change the way a public or system view is displayed")

1.  In the **Views** list for a table, select the **Show list of references** down arrow ![Drop Down](media/create-or-edit-model-driven-app-view/edit-a-public-or-system-view-in-app-designer-2.png "Drop Down").
    
2.  Next to the view you want to edit, select **Open the View Designer**.  The view opens in the view designer. ![Open view Designer](media/create-or-edit-model-driven-app-view/edit-a-public-or-system-view-in-app-designer-3.png "Open view Designer")

When you edit a public or system view, you must save and publish your changes before they will be visible in the application.
