---
title: Explore data on a grid page
description: Explore data on a grid page in model-driven apps.
author: mduelae
manager: kvivek
ms.component: pa-user
ms.topic: conceptual
ms.date: 02/25/2022
ms.subservice: end-user
ms.author: mkaur
ms.reviewer: ""
ms.assetid: 
search.audienceType: 
  - enduser
search.app: 
  - PowerApps
  - D365CE
---

# Explore data on a grid page (preview)

[!INCLUDE [cc-beta-prerelease-disclaimer](../includes/cc-beta-prerelease-disclaimer.md)]

In model-driven apps, the read-only grid is the default control that's used to show data in tabular form. When there's a table in a subarea, the subarea's default layout in the app sitemap is called *the grid page*.

:::image type="content" source="./media/grid-page-1.png" alt-text="A screenshot of a grid page in a model-driven app.":::

Legend:

1. **Command bar**: Shows the commands available for the page.
2. **View selector**: Select to change views.
3. **Edit columns**: Select to add, remove, or reorder columns.
4. **Edit filters**: Select to filter the view with advanced queries.
5. [**Search this view** or **Quick find**](#grid-search): Enter text to show only the rows in the current view that contain your text.

## Navigation

To navigate to a record from the grid page, select the link in the primary column. In the example below, the primary column is *Account Name*. The grid page keeps your filters, sort order, and the state the page was in, when you navigate away and come back. The grid page works the same way when you filter data through search, column filtering, or pagination.

:::image type="content" source="./media/grid-remember-state-on-back-navigate.gif" alt-text="An animated screenshot that shows that navigating back to a grid page opens it in the state it was left in.":::

On a grid page with records that are in a hierarchy relationship, select the hierarchy icon to open the hierarchy view.

:::image type="content" source="./media/grid-row-hierarchy-icon.png" alt-text="A screenshot of a table column in a model-driven app, showing the row hierarchy icon.":::

To open a record in a new tab or a new window, right-click the link in the column and select **Open link in new tab** or **Open link in new window**.

## View selector
  
The view selector lists all the table views that you can use. By default, the list is grouped into **My Views**, personal views that you created, and **System Views**, views that your administrator created and shared with you.

:::image type="content" source="./media/view-selector.png" alt-text="A screenshot of the view selector on a grid page.":::

If your administrator has turned on the [modern advanced find experience](/power-platform/admin/settings-features), the list of views isn't divided into personal and system groups. To easily tell which kind of view you're looking at, personal views have a user icon ![Persona view icon.](./media/user-icon.png "Personal view icon"). You can also hover over the information icon ![Information button.](media/info-icon.png "Information icon") to see the view type.

By default, personal views are listed before system views. Both views are sorted alphabetically. You can [change the order](./grid-filters-advanced.md#change-sort-order) the views are listed in.

 To quickly find a view in a long list, use the search box at the top of the view selector.

:::image type="content" source="./media/search-view.png" alt-text="A screenshot of the view selector on a grid page, showing the search box and personal view icons.":::

Every table in your app has a [default view](./grid-filters-advanced.md#set-default-view) that's set by your administrator. The  **Default** label in the view selector identifies the default view.

## Column editor

Use the [column editor](./grid-filters-advanced.md#column-editor) to add, remove, or reorder columns.

:::image type="content" source="./media/colum-editor.gif" alt-text="An animated screenshot that shows the column editor on a grid page.":::

## Filter editor

Use the [filter editor](./grid-filters-advanced.md#filter-editor) to see the query that underlies the current view. You can also add or remove conditions to change the data that's shown in the view.

:::image type="content" source="./media/edit-filters.gif" alt-text="An animated screenshot that shows the filter editor on a grid page.":::

## Grid search

The search box on a grid page can offer two different experiences, depending on how your administrator has configured it.

### Option 1: Search this view

**Search this view** is the default experience. When you enter text in the **Search this view** box, the system searches the current view. It displays the results in the same columns that are used in the current view.

### Option 2: Quick find

If your administrator has turned on quick find, then the search box shows **Quick find** instead of **Search this view**. When you enter text in the **Quick find** box, the system searches the table's quick find view. It displays the results in the columns of the quick find view rather than the current view.

## Column filters
  
You can choose from many filter options for a column in a grid. The type of data in the column determines the options that are available. For example, the **Full Name** column in the **Contacts** grid page has different filter options from the **Activity Type** column in the **Activities** grid page.

>[!IMPORTANT]
>In Unified Interface, grids don't pre-populate column filters based on the current view definition.

:::image type="content" source="./media/filter-options.png" alt-text="A screenshot of the filtering options available for columns that contain different kinds of data.":::

### Filtering on a lookup column

When you filter data on a lookup column, you can select from a list of values rather than typing. For example, to filter a view by **Primary Contact**, you can select a name from the list that appears when you select the filter text box.

If you start typing, the filter suggests matching results to help you complete the search. The results include all rows that aren't otherwise filtered out.

:::image type="content" source="./media/lookup-filter.png" alt-text="A screenshot of the Primary Contact column filter that shows search completion.":::

### Filtering on a date column

When you filter on a date column, you can select from many different ways to search. For example, you can search **On or after** an exact date, **Next fiscal year**, or **Last week**.

:::image type="content" source="./media/date-filter.png" alt-text="A screenshot of a date column filter that shows the date search options.":::
  
### Filtering activities

Use the activity type filter to show only the activities you're interested in. You can filter activities by type, such as email, task, and phone call.

:::image type="content" source="./media/activity_filter.png" alt-text="A screenshot of the activity type filter that shows several types of activities selected.":::

## Jump bar

The jump bar on a grid page gives you quick access to records that start with a particular letter. The jump bar acts on the first sorted column in the view. If the sort order hasn't changed, the jump bar uses the primary column.

:::image type="content" source="./media/jumpbar-filter-on-sorted-column.gif" alt-text="An animated screenshot that shows the jump bar used to navigate to records that start with the letter S.":::

[!INCLUDE[footer-include](../includes/footer-banner.md)]
