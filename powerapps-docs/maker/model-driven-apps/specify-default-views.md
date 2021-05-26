---
title: "Specify a model-driven app default view in Power Apps | MicrosoftDocs"
description: "Learn how to specify a default view"
ms.custom: ""
ms.date: 03/30/2020
ms.reviewer: ""
ms.service: powerapps
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
applies_to: 
  - "Dynamics 365 (online)"
  - "Dynamics 365 Version 9.x"
  - "powerapps"
author: "Mattp123"
ms.assetid: 1a9d27e1-4dd7-4063-87a5-3d7565fc6194
caps.latest.revision: 25
ms.author: "matp"
manager: "kvivek"
search.audienceType: 
  - maker
search.app: 
  - PowerApps
  - D365CE
---
# Specify a model-driven app default view

[!INCLUDE [cc-data-platform-banner](../../includes/cc-data-platform-banner.md)]

<a name="BKMK_SetDefaultView"></a>   

Unless someone has 'pinned' a different view in your app as their personal default, they will see the default view that you specify as the app maker. You can set any of the public views as the default view for a table.  
  
1.  Sign in to [Power Apps](https://make.powerapps.com/?utm_source=padocs&utm_medium=linkinadoc&utm_campaign=referralsfromdoc).  

2.  Expand **Data**, select **Tables**, select the table you want, and then select the **Views** tab.

3.  Select **More commands** ![More Commands button](media/more-commands.gif "More Commands button for Forms") next to the view you want, and then select **Set as default view**. You can also select **Set as default view** on the menu bar.

    > [!div class="mx-imgBorder"] 
    > ![Set as default view](media/set-as-default-menu-maker.png)

## Set the default view for a table in solution explorer 
  
1.  Open [solution explorer](advanced-navigation.md#solution-explorer), expand **Entities**, select the table that you want, and then select **Views**.    
  
2.  Select a public view.  
  
3.  On the menu bar, select **More Actions** > **Set Default**.  

    > [!div class="mx-imgBorder"] 
    > ![Set as default](media/set-as-default-menu.png)
  
4.  On the solution explorer toolbar, select **Publish All Customizations**.  

## Next steps
[Understand views](create-edit-views.md)


[!INCLUDE[footer-include](../../includes/footer-banner.md)]