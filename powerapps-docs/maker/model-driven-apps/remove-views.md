---
title: "Delete or turn off a model-driven app view in Power Apps"
description: "Learn how to delete or deactivate a view"
ms.custom: ""
ms.date: 10/08/2024
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
search.audienceType: 
  - maker
---
# Delete or turn off a model-driven app view

Views allow the data in Microsoft Dataverse tables to be presented in a way that meets a business need at a given time.

The views that are required in an organization might change over time. It's good practice to maintain views in order to keep your model-driven apps as simple as possible to use and maintain.

## System views versus public views

Depending on the type of view, you can either turn it off or delete it. Turned off views can be turned on again, while the deletion of a view is permanent.

- Custom table public views can both be deleted and turned off/on. Public views that are standard with Dataverse, such as the active accounts and inactive accounts standard public views can be turned off/on.
- [System views](create-edit-views.md#system-views) can't be  deleted or turned off/on. This includes public views created by the system.

## Turn on or turn off views

Custom public views can be turned off and these turned off views can be turned on. While a view is turned off, the view isn't available in the associated model-driven apps for users to select. Public views set as the default view for the table can't be turned off.

1. Sign in to [Power Apps](https://make.powerapps.com/?utm_source=padocs&utm_medium=linkinadoc&utm_campaign=referralsfromdoc), open the environment you want, select **Solutions** on the left navigation pane, and then open the unmanaged solution you want.  
1. Open the table you want, and then select the **Views** area under **Data experiences**.
1. Select the view you want to turn on or off, and then select either **Turn off** or **Turn on** on the command bar.

## Delete a view

Deleting a view permanently removes it from the environment.

1. Sign in to [Power Apps](https://make.powerapps.com/?utm_source=padocs&utm_medium=linkinadoc&utm_campaign=referralsfromdoc), open the environment you want, select **Solutions** on the left navigation pane, and then open the unmanaged solution you want.  
1. Open the table you want, and then select the **Views** area under **Data experiences**.
1. Select the view you want to remove, and then select **Remove** > **Delete from this environment** on the command bar.

> [!NOTE]
>
> - Where a model-driven app specifies a view this creates a dependency between the app and the view.  If this is the case the view will need to first be removed from the app using the app designer.
> - If the view has been added to more than one solution, you can select **Remove** > **Remove from this solution** to remove from the solution but keep available in the environment.

## Delete or activate and deactivate views in classic solution explorer

### Delete a view in classic solution explorer  

You can delete any custom public view. Use the steps in [Access view definitions](accessing-view-definitions.md) to find the view you want to delete and use the ![Delete button.](media/delete.gif "Delete button")**Delete** command. Once you verify that you really want to delete it, the view is permanently deleted.  
  
### Deactivate or activate views in classic solution explorer

1. Navigate to **System Views** as described in [Access view definitions](accessing-view-definitions.md).  
  
2. Select a public view. To see inactive views, use the **Inactive Public Views** view.  
  
3. On the menu bar, select **More Actions**, and then select either **Deactivate** or **Activate**.  
  
4. Select **Publish All Customizations**.

## Next steps

[Views overview](create-edit-views.md)

[!INCLUDE[footer-include](../../includes/footer-banner.md)]
