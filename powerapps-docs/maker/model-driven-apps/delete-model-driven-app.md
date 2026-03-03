---
title: "Delete a model-driven app in Power Apps"
description: "Learn how to delete or remove a model-driven app from your Power Platform environment."
keywords: ""
ms.date: 03/03/2026
ms.custom: 
ms.topic: how-to
applies_to: 
  - "Dynamics 365 (online)"
  - "Dynamics 365 Version 9.x"
  - "powerapps"
ms.assetid: e82e7f64-37ad-41e5-acd7-16309881c6a2
author: "Mattp123"
ms.subservice: mda-maker
ms.author: "matp"
ms.reviewer: 
ms.suite: 
ms.tgt_pltfrm: 
topic-status: Drafting
search.audienceType: 
  - maker
---
# Delete a model-driven app

Apps might need to be deleted for a variety of reasons. An app might have been prepared purely as a development training exercise, might no longer be used in the organization, or could have been superseded in some way.

The process for removing an app is straightforward. However, dependencies can be encountered when you delete objects in Microsoft Dataverse.  While you can delete apps at any time in an unmanaged solution, you can't delete tables that are used in the apps until such time as the app has been removed. The same is true for other app objects, such as table views.

> [!IMPORTANT]
>
> - If a model-driven app or site map is installed as part of a managed solution, see [Delete a model-driven app that was installed as part of a managed solution](#delete-a-model-driven-app-that-was-installed-as-part-of-a-managed-solution) for information about how to delete it.
> - Model-driven apps from Microsoft, such as Dynamics 365 Sales, Dynamics 365 Customer Service, and Dynamics 365 Field Service can’t be deleted. You can hide these apps from users by removing the security roles that are assigned to the app. Notice that these apps are visible to users with environment maker, system administrator, and system customizer security roles or any user with create privileges on the Model-driven App table.

## Delete or remove an unmanaged app in your environment

1. Sign in to [Power Apps](https://make.powerapps.com/?utm_source=padocs&utm_medium=linkinadoc&utm_campaign=referralsfromdoc).
2. On the left navigation, select **Solutions**, and then open the solution that has the app you want to delete. If the app isn't in a custom solution, select **Apps**.
3. Select the unmanaged model-driven app that you want to delete, and then select **Delete** on the command bar.
4. In the confirmation message choose from two options:
   - **Remove solution** removes the app from the solution, but retains it within the environment.
   - **Delete from this environment** deletes it from both the solution and the environment.

   If the component has dependencies, such as relationships, these must be removed before the app can be deleted. To see the dependencies of an app, select the app and then select **Show Dependencies** on the command bar.

5. When an app is deleted, you should also delete the associated site map. If you don't delete the site map, the site map designer displays an error the first time there is an attempt to create another app with the same name. However, it is possible to ignore the error, and the error doesn't appear when you try to create the app again.
   1. On the left navigation pane, select **Solutions**. [!INCLUDE [left-navigation-pane](../../includes/left-navigation-pane.md)]
   1. Open the **Default Solution**.
   1. On the left navigation pane, select **Site maps**, select the site map that has the same name of the app that you deleted earlier, and then select **Delete from this environment**.
   1. Select **Delete** to confirm.

## Delete a model-driven app that you installed as part of a managed solution

You can't delete a model-driven app or site map that you installed in the environment as part of a managed solution. Instead, delete the managed solution.

### Delete a managed solution

All the components of a managed solution are deleted by deleting the solution.

> [!CAUTION]
> Be careful when you delete a managed solution. The solution might contain components that are used for production purposes, such as a line of business application. When you delete the solution, you delete all solution components and any data associated with the managed solution.

1. Sign in to [Power Apps](https://make.powerapps.com/?utm_source=padocs&utm_medium=linkinadoc&utm_campaign=referralsfromdoc). 
1. Select **Solutions** in the left navigation.
1. In the **Solutions** list, select the managed solution you want to delete. On the toolbar, select **Delete**.


[!INCLUDE[footer-include](../../includes/footer-banner.md)]
