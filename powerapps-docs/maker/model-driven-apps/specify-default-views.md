---
title: "Specify a default view for a table in Power Apps | MicrosoftDocs"
description: "Learn how to specify a default view"
ms.custom: ""
ms.date: 03/30/2020
ms.reviewer: ""
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "how-to"
applies_to: 
  - "Dynamics 365 (online)"
  - "Dynamics 365 Version 9.x"
  - "powerapps"
author: "Mattp123"
ms.assetid: 1a9d27e1-4dd7-4063-87a5-3d7565fc6194
caps.latest.revision: 25
ms.subservice: mda-maker
ms.author: "matp"
search.audienceType: 
  - maker
---
# Specify a default view for a table

<a name="BKMK_SetDefaultView"></a>   

Unless someone has 'pinned' a different view in your app as their personal default, they will see the default view specified by the app maker. Any of the public views can be set as the default view for a table.  
  
1. Sign in to [Power Apps](https://make.powerapps.com/?utm_source=padocs&utm_medium=linkinadoc&utm_campaign=referralsfromdoc).  

1. Select **Solutions** on the left navigation pane. [!INCLUDE [left-navigation-pane](../../includes/left-navigation-pane.md)]
1. Open the solution where the table is located.
1. Open the table, and then select the **Views** area.
1. Select **More commands** ![More Commands button.](media/more-commands.gif "More Commands button for forms") next to the view, and then select **Set as default view**. This can also be set on the command bar.

    > [!div class="mx-imgBorder"] 
    > ![Set as default view.](media/set-as-default-menu-maker.png)

> [!NOTE]
> You can also specify the views that can be displayed in a model-driven app using the model-driven app designer. More information: [Manage views and charts](create-add-remove-forms-views-dashboards.md#manage-views-and-charts)

## Set the default view for a table in solution explorer
  
1.  Open [solution explorer](advanced-navigation.md#solution-explorer), expand **Entities**, select the table that you want, and then select **Views**.
  
2.  Select one of the public views.  
  
3.  On the menu bar, select **More Actions** > **Set Default**.  

    > [!div class="mx-imgBorder"] 
    > ![Set as default.](media/set-as-default-menu.png)
  
4.  On the solution explorer toolbar, select **Publish All Customizations**.  

## Next steps

[Delete or deactivate a view](remove-views.md)

[!INCLUDE[footer-include](../../includes/footer-banner.md)]
