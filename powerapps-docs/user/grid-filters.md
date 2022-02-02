---
title: "Explore data in a view on a grid page | MicrosoftDocs"
author: mduelae
manager: kvivek
ms.service: powerapps
ms.component: pa-user
ms.topic: conceptual
ms.date: 03/31/2020
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
# Explore data in a view on a grid page

In model-driven apps, the read-only grid is the default control used to represent rows of data in tabular form. 

In the sitemap, when there'a a table in the subarea, the default layout of that subarea is called the grid page. 


   > [!div class="mx-imgBorder"]
   > ![Grid page view.](media/grid-page-1.png "Grid page")

Legend

1. **Command bar**: Shows the commands available for the grid page.
2. **View selector**: Select to change views.
3. **Edit columns**: Select to edit the view by adding, removing, or recording columns in the grid view.
4. **Edit filters**: Select to edit the view with advanced filter queries.
5. **Search this view**: Enter text in the search column above the list to show only those rows in the current view that contain your text.

## Navigation

From the grid page, you can select a cell in the primary column to navigate to the record page.

When you filter data on a grid, the grid page remembers the filter, sort order, and the page state when you navigate away and then return to the page. This works the same way when data is filtered through search, column filtering, or pagination.

   > [!div class="mx-imgBorder"]
   > ![Navigating back to the page opens it in the same state.](media/grid-remember-state-on-back-navigate.gif "Navigating back to the page opens it in the same state")

On grids of tables that support hierarchy relationships, you can select the hierarchy icon to navigate to the hierarchy view.

   > [!div class="mx-imgBorder"]
   > ![Hierarchy icon.](media/grid-row-hierarchy-icon.png "Hierarchy icon")

You can also right-click a cell value in the primary column or a lookup column to open in a new tab or window.

   > [!div class="mx-imgBorder"]
   > ![Open in a new window.](media/newtab.png "Open in a new window")

## View selector
  
The view selector at the top of the page contains all the views of the table you have access to. By default, the list of views is grouped by personal views and system views, with each of the groups listing views ordered alphabetically by view name.

   > [!div class="mx-imgBorder"]
   > ![View selector showing the different views.](media/view-selector.png "View selector")


### Modern advanced find

If your administrator has enabled the modern advanced find experience, you will see a single ungrouped list of views with personal views indicated by the _user_ icon. You can hover over the _info_ icon to understand whether a view is a personal view or a system view. The ordering of views in the list depends on the preset sort order you have chosen, with personal views (ordered alphabetically) over system views (ordered alphabetically) the default. For more information on how you can change the sort order, see https://docs.microsoft.com/en-us/powerapps/user/grid-filters-advanced >> sorting.

You can use the search box at the top of the view selector to quickly search for a view.

The default view for a table is set by the administrator and is indicated by the Default label in the view list. You can choose a view to be the default view or reset the default to the one chosen by the administrator at any time. For more information, see https://docs.microsoft.com/en-us/powerapps/user/grid-filters-advanced >> manage default view.

_GIF of view selector_

## Column editor

Use the column editor to add, remove, or re-order columns. For more information, see [Column editor](grid-filters-advanced.md#column-editor).

   > [!div class="mx-imgBorder"]
   > ![Select the column editor to edit columns.](media/colum-editor.gif "Columns editor")

## Filter editor

Select **Edit filters**  on the grid page, to see the set of conditions in the current view. You can also add more conditions or remove conditions in filter data For more information, see https://docs.microsoft.com/en-us/powerapps/user/grid-filters-advanced >> Filter editor

   > [!div class="mx-imgBorder"]
   > ![Select to edit the filters.](media/edit-filters.gif "Edit filters")

## Grid search

The search box on a grid page may have one of two types of searches as configured by your administrator.

### 1. Search this view (_Default_)

When you use the **Search this view** option on a grid page, the system searches for data in the view that you're currently in. In the following example, you perform a search on the **Contacts** grid.

1. Go to the **Contacts** grid, and then select **My Active Contacts** from the list of views.

    > [!div class="mx-imgBorder"]
    > ![My active contact view.](media/myactive-contacts-view.png "My Active Contacts view")

2. Select **Search this view** to search for data in the view you're in.

    > [!div class="mx-imgBorder"]
    > ![Search view.](media/search-view.png "Search this view")

The system searches for data in the **My Active Contacts** view and displays search results by using the same set of columns that are used in your current view.

   > [!div class="mx-imgBorder"]
   > ![Search view.](media/search-view2.png "Search results from the Search this view command")

### 2. Quick find

If your administrator has enabled the use of quick find view of a table for searching on grids and sub-grids, you will see the **Quick find** search option on the grid page. When you use it, the system searches for data in the quick find view of the table and displays results in the columns of the quick find view and not of the current view. 

## Column filters
  
You can choose from many different filtering options for a column in a grid. The type of data in the column determines what filter options are available. For example, the **Full Name** column in the **Contacts** grid page has different filter options than the **Activity Type** column in the **Activities** grid page.
 
> [!IMPORTANT]
> In Unified Interface, grids don't prepopulate column filters based on the current view definition.

   > [!div class="mx-imgBorder"]
   > ![Grid filtering.](media/filter-options.png "Grid filtering")

### Filtering on a lookup column
 
When you filter on a lookup column, you can select from a list of rows to filter by rather than manually typing in the data. For example, on a **Primary Contact** lookup column, you can select the contact name from the list of rows to filter by.

The filter on a lookup column helps you complete the search by suggesting results inline. These results are based the table being looked up and will include all rows with no filter.

   > [!div class="mx-imgBorder"]
   > ![Lookup filtering.](media/lookup-filter.png "Lookup filtering")

### Filtering on a date column

The robust **Date** filter includes many different values to choose from, such as **On** to search by an exact date, or **Next X fiscal year** or **In fiscal period** to search by year or quarter.

   > [!div class="mx-imgBorder"]
   > ![Date filtering.](media/date-filter.png "Date filtering")
  
### Filtering activities

You can filter the list of activities to see only the ones you're interested in. For example, you can further limit the activities you are seeing in a view by using the activity type filter. The activity type filter allows you to filter activities based on the type, such as email, task, phone call, and so on.


   > [!div class="mx-imgBorder"]
   > ![Activities filter.](media/activity_filter.png "Activities filter")

## Jump bar
The jump bar on a grid page can be used to access rows beginning with a particular character easily. The jump bar acts on the first sorted column in the view. If no change has been made to the sort order, the jump bar uses the primary column.
 
   > [!div class="mx-imgBorder"]
   > ![Select a filter on the jump bar.](media/jumpbar-filter-on-sorted-column.gif "Select a filter on the jump bar")


[!INCLUDE[footer-include](../includes/footer-banner.md)]
