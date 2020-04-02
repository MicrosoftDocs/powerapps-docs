---
title: "Create a personal view using advanced grid filters  | MicrosoftDocs"
author: mduelae
manager: kvivek
ms.service: powerapps
ms.component: pa-user
ms.topic: conceptual
ms.date: 04/02/2020
ms.author: mkaur
ms.reviewer: ""
ms.assetid: 
search.audienceType: 
  - enduser
search.app: 
  - PowerApps
  - D365CE
---
# Edit or create personal views using advanced grid filters 

Easily create a personal view for a set of records using advanced grid filters and expression builder. The advanced filters allows you to create a wide range of views from simple to complex that you can also add grouped and nested conditions to.

When you create and save a personal view, it will appear in your list of view under **My Views**.

![Personal views](media/my_peronsal_view.png "Personal views")

> [!NOTE]
> Advanced filtering is only avilable to English orgs. 

## See the current view definition

To see which filters were applied to the current view, select a view and then select the filter icon to open expression builder. This displays the current view definition by default.

![Current view definition](media/current_view_def.gif "Current view definition")

## Add conditions to filters

1. To edit the current view and add more filters, select a view and then select the filter icon.
2. On the **Advanced filters** screen use the expression builder to add conditions to filters. For more information on how to add conditions, see [Add conditions to a filter](https://docs.microsoft.com/powerapps/maker/model-driven-apps/create-edit-view-filters#add-conditions-to-a-filter).
3. When you're done, select **Apply**. 

![Add filters](media/add_filters.gif "Add filters")

### Add a group or nested condition 

To drill down further into your data, can add a group or nested condition to a filter. For more information, see [Add a group condition to a filter](https://docs.microsoft.com/powerapps/maker/model-driven-apps/create-edit-view-filters#add-a-group-condition-to-a-filter).


![Add a group or nested condition](media/group_condition.gif "Add a group or nested condition")

### Clear filters

Once the filters are applied, to clear them and reset the view back to the original definition, select the clear filter icon ![Clear filter icon](media/clear_filter_icon.png "Clear filter icon").

### Save your personal view

The asterisk next to a view name indicates the view has not been saved. 

![Unsaved view](media/unsaved_view.png "Unsaved view")

1. To save a personal view, on the command bar select the more icon ![More icon](media/commandbar_more_icon.png "More icon"). 
2. Select **Create view** > **Save filter as new view**.
3. On the **Save as new view** dialog box, type in a name and description for the view and then select **Save**.
4. Go to your list of view to see the new personal view that you created.
 
![Save a personal view](media/save_personal_view.gif "Save a personal view")


   
