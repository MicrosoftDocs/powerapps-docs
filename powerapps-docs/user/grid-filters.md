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

[!INCLUDE [cc-beta-prerelease-disclaimer](../includes/cc-beta-prerelease-disclaimer.md)]

<!--note from editor: Renee said the disclaimer you use above is just fine. My edits to this next paragraph are suggested just to make it flow a bit better.-->
Grids in the Unified Interface have been improved to increase the amount of data you can see on your screen. Now you can choose from many different filtering options for a column; the type of data in the column determines which filter options are available. For example, the **Full Name** column in the **Contacts** grid has different filter options than the **Activity Type** column in the **Activities** grid.

   > [!div class="mx-imgBorder"]
   > ![Grid filtering](media/filter-options.png "Grid filtering")

## Lookup field column

When you filter on a lookup column, you can select from a list of records to filter by rather than manually typing in the data. For example, on a **Primary Contact** lookup column, you can select the contact name from the list of records to filter by.

   > [!div class="mx-imgBorder"]
   > ![Lookup filtering](media/lookup-filter.png "Lookup filtering")

## Date filter

The robust **Date** filter includes many different values to choose from, such as **On** to search by an exact date, or **Next X fiscal year** or **In fiscal period** to search by year or quarter.

   > [!div class="mx-imgBorder"]
   > ![Date filtering](media/date-filter.png "Date filtering")

## Grid and filter navigation

When you filter data on a grid, the main grid page remembers the filter, sort order, and the page state when you navigate away and then return to the page. The page state <!--note from editor: Edit okay? I was a bit confused about what "This" referred to.-->includes quick find, column filtering, page number, and more. <!--note from editor: This next sentence seems to contradict the previous point, that when you navigate back to the page it's in the state you left it, not necessarily its "initial state." I guess I don't know what "initial state" means here.-->The navigation outside the page opens with the initial state.<!--note from editor: Can you give this graphic and the next two different alt text strings? I'm not exactly sure what to suggest because I don't clearly see the difference between them. The first seems to be demonstrating that the page state is the same when the user navigates back (so maybe the alt text could be something like "Navigating back to the page opens it in the same state" or something similar?). Remember to describe it well enough for people who aren't looking at the graphics.-->

   > [!div class="mx-imgBorder"]
   > ![Grids remember state](media/grid-remember-state-on-back-navigate.gif "Grid remember state")

The jump bar <!--note from editor: I don't know what a jump bar is, and not sure how it "uses" a field or why it matters.-->uses the first sorted field. If no change has been made to the sort order, the jump bar uses the primary field.<!--note from editor: The alt text for the following graphic will be a good place to reinforce the point of this paragraph. "The remembered page is accessed by the field it was sorted by or by the primary field."?--> 

   > [!div class="mx-imgBorder"]
   > ![Grids remember state](media/jumpbar-filter-on-sorted-column.gif "Grid remember state")
  
When you select the hierarchy icon, you navigate to the hierarchy form.<!--note from editor: Would it be accurate to call this a hierarchy view? I can't quite picture what a hierarchy form is.-->

   > [!div class="mx-imgBorder"]
   > ![Hierarchy icon](media/grid-row-hierarchy-icon.png "Hierarchy icon")

You can also open primary field and lookup fields in a new tab or window.

   > [!div class="mx-imgBorder"]
   > ![Open in a new window](media/newtab.png "[Open in a new window")

## Use search on a grid

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

<!--note from editor: Is there a reason not to have this next section be an H2? It isn't really a subset of the previous H2.-->
## Use the quick-find search experience

To switch back to the old quick-find search experience that uses an entity's quick-find view definition to perform searches, you'll need admin permissions.

1. In the upper-right corner, select the <!--note from editor: I assume there's no tooltip for the gear icon at all? If there is, you'll want to use that and drop the word "icon". So if the tooltip says "Gear", it should be "...select ***Gear** [icon link], and then select...". If it says "Settings", then this should be "...select **Settings** [icon link], and then select..."-->gear icon ![Gear icon](media/selection-rule-gear-button.png), and then select **Advanced Settings**.

2. Go to **Settings** > **Administration** > **System Settings**.

3. On the **General** tab, under **Set up Quick Find**, select **Yes** for **Use quick find view of an entity for searching on grids and sub-grids**.
