---
title: "Sort rows in a model-driven app view in Power Apps"
description: Learn how to sort rows in a model-driven app with Power Apps.
ms.custom: ""
ms.date: 11/11/2024
ms.reviewer: ""
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "how-to"
applies_to: 
  - "Dynamics 365 (online)"
  - "Dynamics 365 Version 9.x"
  - "powerapps"
author: "Mattp123"
ms.assetid: 25f5aa52-56dc-4be5-884e-9346616f665f
caps.latest.revision: 25
ms.subservice: mda-maker
ms.author: "matp"
search.audienceType: 
  - maker
---
# Sort rows in a model-driven app view

When you create or edit a view, you can configure the sort order for either ascending or descending.

To change the sort order in the view designer, go to [Create a public view in Power Apps](create-edit-views-app-designer.md#create-a-public-view-in-power-apps).

## Change the sort order of a view

1. Sign in to [Power Apps](https://make.powerapps.com/?utm_source=padocs&utm_medium=linkinadoc&utm_campaign=referralsfromdoc).  
1. Select **Solutions**, and then open the solution you want. [!INCLUDE [left-navigation-pane](../../includes/left-navigation-pane.md)]
1. Select **Tables**, open the table you want, and then select the **Views** area.
1. Select a view to open it in the view designer.
1. Select the leftmost column head, such as **Account Name** in the example here, and from the column menu, select **Sort A to Z** or **Sort Z to A**. The sort order is indicated in the column head with an up arrow or a down arrow.
   > [!div class="mx-imgBorder"] 
   > ![Edit filters.](media/view-column-menu.png "Edit filters")
1. If a sort order hasn't been set for the view, select **Sort by**, and then select the primary sort by column.

1. To sort the view by additional columns, select **Then sort by** on the view properties pane on the right, and then select a sort by column for the view.

   :::image type="content" source="media/create-or-edit-model-driven-app-view/sort-view-by-multiple-columns.png" alt-text="Sorting a table view for column Account Name":::

1. To remove a filter expression, under **Filter by** in the view properties pane, select **X**  next to the filter expression you want to remove.
1. Select **Save and publish** to save the view and make it available to apps that include the table.

## Next steps

[Table views overview](create-edit-views.md)

[Setting managed properties for views](managed-properties-views.md)

[!INCLUDE[footer-include](../../includes/footer-banner.md)]
