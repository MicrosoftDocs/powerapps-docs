---
title: "Delete or deactivate a model-driven app view in Power Apps | MicrosoftDocs"
description: "Learn how to delete or deactivate a view"
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

Views allow the data in tables to be presented in a way that meets a business need at a given time.

## Why we need to maintain table views

The views that are required in an organization may change over time, and it is good practice to maintain them in order to keep your app as simple as possible to use and maintain.

## System views versus public views

Depending on the type of view, you can either delete it or deactivate it. Deactivated views can be reactivated, while the deletion of a view is permanent.

- Custom public views can both be deleted and deactivated, including public views that the system created.
- [System views](create-edit-views.md#system-views) can't be  deleted or deactivated. This includes public views created by the system.

## Delete a view

1. Sign in to [Power Apps](https://make.powerapps.com/?utm_source=padocs&utm_medium=linkinadoc&utm_campaign=referralsfromdoc).  

2. Select **Tables** on the left navigation pane, select the table you want, and then select the **Views** area. [!INCLUDE [left-navigation-pane](../../includes/left-navigation-pane.md)]

3. Select **More commands** ![More Commands button.](media/more-commands.gif "More Commands button for Forms") next to the view you want, and then select **Delete view**. You can also select **Delete view** on the menu bar.

> [!NOTE]
> Where a model-driven app specifies a view this creates a dependency between the app and the view.  If this is the case the view will need to first be removed from the app using the app designer.

## Deactivate or activate views  

1. Sign in to [Power Apps](https://make.powerapps.com/?utm_source=padocs&utm_medium=linkinadoc&utm_campaign=referralsfromdoc).  

2. Select **Tables** on the left navigation pane, select the table you want, and then select the **Views** area. [!INCLUDE [left-navigation-pane](../../includes/left-navigation-pane.md)]

3. Select **More commands** ![More Commands button.](media/more-commands.gif "More Commands button for Forms") next to the view you want, and then select either **Deactivate** or **Activate**. You can also select **Deactivate** or **Activate** on the menu bar.

## Delete a view in solution explorer  

You can delete any custom public view. Use the steps in [Access view definitions](accessing-view-definitions.md) to find the view you want to delete and use the ![Delete button.](media/delete.gif "Delete button")**Delete** command. Once you verify that you really want to delete it, the view will be permanently deleted.  
  
## Deactivate or activate views in solution explorer

1. Navigate to **System Views** as described in [Access view definitions](accessing-view-definitions.md).  
  
2. Select a public view. To see inactive views, use the **Inactive Public Views** view.  
  
3. On the menu bar, select **More Actions**, and then select either **Deactivate** or **Activate**.  
  
4. Select **Publish All Customizations**.

## Next steps

[Views overview](create-edit-views.md)

[!INCLUDE[footer-include](../../includes/footer-banner.md)]
