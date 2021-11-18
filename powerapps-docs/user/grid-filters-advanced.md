---
title: "Create a personal view using advanced grid filters  | MicrosoftDocs"
description: Edit or create personal views using advanced grid filters in model-driven Power Apps.
author: mduelae
manager: kvivek
ms.service: powerapps
ms.component: pa-user
ms.topic: conceptual
ms.date: 11/18/2021
ms.subservice: end-user
ms.author: mkaur
ms.reviewer: ""
ms.assetid: 
search.audienceType: 
  - enduser
search.app: 
  - PowerApps
  - D365CE
searchScope:
  - D365-App-msdynce_saleshub
  - D365-Entity-account
  - D365-Entity-contact
  - D365-Entity-actity
  - D365-UI-View
  - Power Platform
  - Power Apps
---


# Edit or create personal views using advanced grid filters 

Use the advanced filter options to create a personal view to see the rows that are important to you. The advanced filter options let you create a wide range of views from simple to complex. It also lets you add grouped and nested conditions to the filters.


> [!NOTE]
> - The advanced filter option is available only in English language versions. We plan to support more languages in future releases.
> - The advanced filter option on the Queues table does not work and displays this error message: We are unable to display the filter conditions for this view.
> - In Unified Interface, grids do not prepopulate column filters based on the current view definition.
> - Public views created in Power Apps that include **Contains data** or **Does not contain data** filters will not appear in the list of saved views in Advanced Find.

When you create and save a personal view, it appears in your list of personal views under **My Views**.

> [!div class="mx-imgBorder"]
> ![Personal views.](media/my_peronsal_view.png "Personal views")


## See the current view definition

To see which filters were applied to the current view, select a view and then select **Filter** ![Filter icon.](media/commandbar_filter_icon.png "Filter icon"). This opens expression builder and displays the default view definition.

> [!div class="mx-imgBorder"] 
> ![Current view definition.](media/current_view_def.gif "This image demonstrates how to see the filters for the view the view")

## Add conditions to filters

1. To edit the current view and add more filters, select a view and then select **Filter** ![Filter icon.](media/commandbar_filter_icon.png "Filter icon").
2. On the **Advanced filters** screen, use the expression builder to add conditions to filters. For more information on how to add conditions, see [Add conditions to a filter](../maker/model-driven-apps/create-edit-view-filters.md#add-conditions-to-a-filter).
3. When you're done, select **Apply**. 

   > [!div class="mx-imgBorder"] 
   > ![Add filters.](media/add_filters.gif "This image demonstrates how to add filters using expression builder")

### Add grouped or nested conditions

To drill down further into your data, you can add grouped or nested conditions to the filters. For more information, see [Add a group condition to a filter](../maker/model-driven-apps/create-edit-view-filters.md#add-a-group-condition-to-a-filter).

   > [!div class="mx-imgBorder"] 
   > ![Add a group or nested condition.](media/group_condition.gif "This image demonstrates how to add a grouped or nested condition to a filter")

### Clear filters

To clear filters that were applied and reset the view back to the original definition, select **Clear filter** ![Clear filter icon.](media/clear_filter_icon.png "Clear filter icon").

### Save your personal view

An asterisk next to a view name indicates the view has not been saved. 

   > [!div class="mx-imgBorder"] 
   > ![Unsaved view.](media/unsaved_view.png "Unsaved view")

1. To save a personal view, on the command bar select **More** ![More icon.](media/commandbar_more_icon.png "More icon"). 
2. Select **Create view** > **Save filter as new view**.
3. On the **Save as new view** dialog box, type in a name and description for the view and then select **Save**.
4. The view will appear in your list of personal views under **My Views**.

   > [!div class="mx-imgBorder"] 
   > ![Save a personal view.](media/save_personal_view.gif "This image demonstrates how to save a personal view")

## Set a default view

You can set a system view or choose one of your views and set it as the default view.

1. Select the table that you want to set the view for, such as Accounts.
2. From the list of views, select the view that you want to set as the default view.
3. Select the view again and then select **Set current view as my default**.

   


[!INCLUDE[footer-include](../includes/footer-banner.md)]
