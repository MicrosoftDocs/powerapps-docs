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
# Use filters on a grid

Grids in Unified Interface have been improved to increase the amount of data that can be seen on your screen. There are many different filtering options that are avilable. The type of data in the column determines which filter options are available. For example, the **Full Name** column in the **Contacts** grid will have different filter options than the **Activity Type** column in the **Activites** Gird.


   > [!div class="mx-imgBorder"]
   > ![Grids filtering](media/filter-options.png "Grids filtering")
   
   
## Lookup field column

When you filter on a lookup column, you can select from a list of records to filter by rather manually typing in data. For example, on a **Account** lookup column select the acccout names from the list of records to filter by.

   > [!div class="mx-imgBorder"]
   > ![Lookup filtering](media/lookup-filter.png "Lookup filtering")


## Date filter

The **Date** filter on grids is a very powerful filter. There are many different filters to choose from, such as **On** to seach by exact date or select filter such as **Next X fiscal year** or **In fiscal period** to search by year.

   > [!div class="mx-imgBorder"]
   > ![Date filtering](media/date-filter.png "Date filtering")


## Grid and filter navigation 

When you filter data on a grid the page remembers the filter, sort, and the page state when you navigate away and then come back to the page. This includes quick find, column filtering, page number, and more. The navigation outside the page opens with the initial state.


   > [!div class="mx-imgBorder"]
   > ![Grids remember state](media/grid-remember-state-on-back-navigate.gif "Grids remember state")


The jump bar uses the first sorted field. If no sort change has been made, the jump bar uses the primary field. 

   > [!div class="mx-imgBorder"]
   > ![Grids remember state](media/jumpbar-filter-on-sorted-column.gif "Grids remember state")
  
   
When you select the hierarchy icon, it will navigate to the hierarchy form.

   > [!div class="mx-imgBorder"]
   > ![Hierarchy icon](media/grid-row-hierarchy-icon.png "Hierarchy icon")
   
You can also open primary field and lookup fields in new tab or window.

   > [!div class="mx-imgBorder"]
   > ![Open in a new window](media/newtab.png "[Open in a new window")


## Search a view on a grid

When you use the **Search this view** option on a grid, the system searchs for data in the view that you are in. 

1. Go to the **Contacts** grid and from the list of view selct **My Active Contacts**.

    > [!div class="mx-imgBorder"]
    > ![My active contact view](media/myactive-contacts-view.png "My active contact view")
    
2. Select **Search this view** to search for data in the current view that you are in.

    > [!div class="mx-imgBorder"]
    > ![Search view](media/search-view.png "Search view")

The system will search for data in the **My Active Contacts** view and when search data is displayed, it will show the same set of columns that is in your current view.

   > [!div class="mx-imgBorder"]
   > ![Search view](media/search-view2.png "Search view")



 
