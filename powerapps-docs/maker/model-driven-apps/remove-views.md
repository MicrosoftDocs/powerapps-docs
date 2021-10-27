---
title: "Delete or deactivate a model-driven app view in Power Apps | MicrosoftDocs"
description: "Learn how to delete or deactivate a view"
ms.custom: ""
ms.date: 03/30/2020
ms.reviewer: ""
ms.service: powerapps
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "how-to"
applies_to: 
  - "Dynamics 365 (online)"
  - "Dynamics 365 Version 9.x"
  - "powerapps"
author: "Mattp123"
ms.assetid: 60865f78-7482-42da-8960-adbd3c155028
caps.latest.revision: 25
ms.subservice: mda-maker
ms.author: "matp"
manager: "kvivek"
search.audienceType: 
  - maker
search.app: 
  - PowerApps
  - D365CE
---
# Delete or deactivate a model-driven app view 

[!INCLUDE [cc-data-platform-banner](../../includes/cc-data-platform-banner.md)]

<a name="BKMK_RemoveViews"></a>   

 You may have a view that you don't want people to see. Depending on the type of view, you can either delete it or deactivate it. If you don't want to delete the view permanently, you can deactivate it instead.
 
  * You can delete any custom public view. Once you verify that you really want to delete it, the view will be permanently deleted.

  * You cannot delete or deactivate any [system views](create-edit-views.md#system-views), including public views the system created. You can deactivate any public view, including public views the system created.

## Delete a view

1.  Sign in to [Power Apps](https://make.powerapps.com/?utm_source=padocs&utm_medium=linkinadoc&utm_campaign=referralsfromdoc).  

2.  Expand **Dataverse**, select **Tables**, select the table you want, and then select the **Views** tab.

3.  Select **More commands** ![More Commands button.](media/more-commands.gif "More Commands button for Forms") next to the view you want, and then select **Delete view**. You can also select **Delete view** on the menu bar.

## Deactivate or activate views  

1.  Sign in to [Power Apps](https://make.powerapps.com/?utm_source=padocs&utm_medium=linkinadoc&utm_campaign=referralsfromdoc).  

2.  Expand **Dataverse**, select **Tables**, select the table you want, and then select the **Views** tab.

3.  Select **More commands** ![More Commands button.](media/more-commands.gif "More Commands button for Forms") next to the view you want, and then select either **Deactivate** or **Activate**. You can also select **Deactivate** or **Activate** on the menu bar.

## Delete a view in solution explorer  

You can delete any custom public view. Use the steps in [Access view definitions](accessing-view-definitions.md#open-a-view-for-editing-in-solution-explorer) to find the view you want to delete and use the ![Delete button.](media/delete.gif "Delete button")**Delete** command. Once you verify that you really want to delete it, the view will be permanently deleted.  
  
## Deactivate or activate views in solution explorer 

1.  Navigate to **System Views** as described in [Access view definitions](accessing-view-definitions.md#open-a-view-for-editing-in-solution-explorer).  
  
2.  Select a public view. To see inactive views, use the **Inactive Public Views** view.  
  
3.  On the menu bar, select **More Actions**, and then select either **Deactivate** or **Activate**.  
  
4.  Select **Publish All Customizations**. 

## Next steps
[Create or edit a view](./create-edit-views-app-designer.md)


[!INCLUDE[footer-include](../../includes/footer-banner.md)]