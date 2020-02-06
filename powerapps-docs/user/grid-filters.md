---
title: "Filter data on grids | MicrosoftDocs"
author: mduelae
manager: kvivek
ms.service: powerapps
ms.component: pa-user
ms.topic: conceptual
ms.date: 02/03/2019
ms.author: mkaur
ms.reviewer: ""
ms.assetid: 
search.audienceType: 
  - enduser
search.app: 
  - PowerApps
  - D365CE
---
# Use grid filters 

Grids in the Unified Interface have been improved to increase the amount of data you can see on your screen. Now you can choose from many different filtering options for a column; the type of data in the column determines which filter options are available. For example, the **Full Name** column in the **Contacts** grid has different filter options than the **Activity Type** column in the **Activities** grid.


   > [!div class="mx-imgBorder"]
   > ![Grid filtering](media/filter-options.png "Grid filtering")
   

## Grid and filter navigation

When you filter data on a grid, the main grid page remembers the filter, sort order, and the page state when you navigate away and then return to the page. This works the same when data is filtered on quick find, column filtering, page number, and more. 

   > [!div class="mx-imgBorder"]
   > ![Navigating back to the page opens it in the same state](media/grid-remember-state-on-back-navigate.gif "Navigating back to the page opens it in the same state")

The page jump bar uses the first sorted field. If no change has been made to the sort order, the jump bar uses the primary field.

   > [!div class="mx-imgBorder"]
   > ![Select a filter on the jump bar](media/jumpbar-filter-on-sorted-column.gif "Select a filter on the jump bar")
  
When you select the hierarchy icon, you navigate to the hierarchy view.

   > [!div class="mx-imgBorder"]
   > ![Hierarchy icon](media/grid-row-hierarchy-icon.png "Hierarchy icon")

You can also open primary field and lookup fields in a new tab or window.

   > [!div class="mx-imgBorder"]
   > ![Open in a new window](media/newtab.png "[Open in a new window")


## Early-access features

This section is for early-access features. You can opt in early to enable these features in your environment. This will allow you to test these features and then adopt them across your environments. For information on how to enable these features, see [Opt in to 2020 release wave 1 updates](https://docs.microsoft.com/power-platform/admin/opt-in-early-access-updates).


   > [!NOTE]
   > Do not change the default display format for time, number, currency, time, or date as this causes an issue. For more information, see [Known issue](https://docs.microsoft.com/powerapps/user/grid-filters#known-issue).

### Lookup field column

When you filter on a lookup column, you can select from a list of records to filter by rather than manually typing in the data. For example, on a **Primary Contact** lookup column, you can select the contact name from the list of records to filter by.

   > [!div class="mx-imgBorder"]
   > ![Lookup filtering](media/lookup-filter.png "Lookup filtering")

### Date filter

The robust **Date** filter includes many different values to choose from, such as **On** to search by an exact date, or **Next X fiscal year** or **In fiscal period** to search by year or quarter.

   > [!div class="mx-imgBorder"]
   > ![Date filtering](media/date-filter.png "Date filtering")

### Filter the list of activities

You can filter the list of activities to see only the ones you’re interested in. For example, you can further limit the activities you are seeing in a view by using the activity type filter. The activity type filter allows you to filter activities based on the type, such as email, task, phone call, and so on.


   > [!div class="mx-imgBorder"]
   > ![Activities filter](media/activity_filter.png "Activities filter")


#### Known issue

If you change the default display format for number, currency, time, or date and then filter data on a grid, the filter will not show your selected display format. The filters will still display in the system default format and in some cases filtering may not work at all. 

To fix the issue, set the display format for number, currency, time, and date back to the default setting. 

1. In the upper-right corner, select the gear icon ![Gear icon](media/selection-rule-gear-button.png), and then select **Personalization Settings**.

2. On the **Formats** tab change the number, currency, time, and date value back to the default setting.

    > [!div class="mx-imgBorder"] 
    > ![Format settings](media/default-format.png "format settings")
    
    
We are working on the issue, please check back for availability. 
  
### Use search on a grid

When you use the **Search this view** option on a grid page, the system searches for data in the view that you're currently in. In the following example, you perform a search on the **Contacts** grid.

1. Go to the **Contacts** grid, and then select **My Active Contacts** from the list of views.

    > [!div class="mx-imgBorder"]
    > ![My active contact view](media/myactive-contacts-view.png "My Active Contacts view")

2. Select **Search this view** to search for data in the view you're in.

    > [!div class="mx-imgBorder"]
    > ![Search view](media/search-view.png "Search this view")

The system searches for data in the **My Active Contacts** view and displays search results by using the same set of columns that are used in your current view.

   > [!div class="mx-imgBorder"]
   > ![Search view](media/search-view2.png "Search results from the Search this view command")


#### Use the quick-find search experience

To switch back to the old quick-find search experience that uses an entity's quick-find view definition to perform searches, you'll need admin permissions.

1. In the upper-right corner, select the gear icon ![Gear icon](media/selection-rule-gear-button.png), and then select **Advanced Settings**.

2. Go to **Settings** > **Administration** > **System Settings**.

3. On the **General** tab, under **Set up Quick Find**, select **Yes** for **Use quick find view of an entity for searching on grids and sub-grids**.




