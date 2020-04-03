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

<!--comment: There are four GIFs in this topic. GIFs on docs are problematic for several reasons. Here is the MS guidance on use of GIFs:
>
- Animated GIFs require the same steps be written out in text. You can’t rely only on the action in the images. At minimum, the alt text must explain well. Use an alt text that says something along the lines of "This image demonstrates adding a user. The step by step instructions follow in text." You can never have an animated gif file unless you have text that describes the thing in the gif.
>
- Animated GIFs must not loop. If there is no way to provide a Pause or Stop button (which on Docs, there isn’t), then you have to build the GIF so that it doesn’t loop. Then users have to refresh the page if they want to see the animation again.
>
- Animated GIFs must also use only approved fictitious content, such as people and company names, phone numbers, etc. 
>
Based on the above, you should replace the GIFs with still images. If the GIFs don't loop (which they seem to do), you would still need to make sure there are sufficient written steps for readers who can't see the action in the GIFs. (Also, be sure all names in the GIFs are from an approved fictitious names list.)
-->


# Edit or create personal views using advanced grid filters 

Easily create a personal view for yourself to see the records that are important to you. The advanced filters allow you to create a wide range of views from simple to complex that you can also add group and nested conditions to.


<!--question: what does "English organizations" mean? Does it mean it's available only in English language versions? -->


> [!NOTE]
> The advanced filter option is available only to English organizations.

When you create and save a personal view, it appears in your list of personal views under **My Views**.

> [!div class="mx-imgBorder"]
> ![Personal views](media/my_peronsal_view.png "Personal views")


## See the current view definition

To see which filters were applied to the current view, select a view and then select **Filter** ![Filter icon](media/commandbar_filter_icon.png "Filter icon"). This opens expression builder and displays the default view definition.

> [!div class="mx-imgBorder"] 
> ![Current view definition](media/current_view_def.gif "Current view definition")

## Add conditions to filters

1. To edit the current view and add more filters, select a view and then select **Filter** ![Filter icon](media/commandbar_filter_icon.png "Filter icon").
2. On the **Advanced filters** screen, use the expression builder to add conditions to filters. For more information on how to add conditions, see [Add conditions to a filter](https://docs.microsoft.com/powerapps/maker/model-driven-apps/create-edit-view-filters#add-conditions-to-a-filter).
3. When you're done, select **Apply**. 

   > [!div class="mx-imgBorder"] 
   > ![Add filters](media/add_filters.gif "Add filters")

### Add a group or nested condition 

To drill down further into your data, add a group or nested condition to the filters. For more information, see [Add a group condition to a filter](https://docs.microsoft.com/powerapps/maker/model-driven-apps/create-edit-view-filters#add-a-group-condition-to-a-filter).

   > [!div class="mx-imgBorder"] 
   > ![Add a group or nested condition](media/group_condition.gif "Add a group or nested condition")

### Clear filters

To clear filters that were applied and reset the view back to the original definition, select **Clear filter** ![Clear filter icon](media/clear_filter_icon.png "Clear filter icon").

### Save your personal view

An asterisk next to a view name indicates the view has not been saved. 

   > [!div class="mx-imgBorder"] 
   > ![Unsaved view](media/unsaved_view.png "Unsaved view")

1. To save a personal view, on the command bar select **More** ![More icon](media/commandbar_more_icon.png "More icon"). 
2. Select **Create view** > **Save filter as new view**.
3. On the **Save as new view** dialog box, type in a name and description for the view and then select **Save**.
4. Go to your list of view to see the new personal view that you created.
 
   > [!div class="mx-imgBorder"] 
   > ![Save a personal view](media/save_personal_view.gif "Save a personal view")


   
