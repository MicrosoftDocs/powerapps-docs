---
title: "Delete a model-driven app | MicrosoftDocs"
description: "Learn how to delete or remove a model-driven app from your Power Apps environment."
keywords: ""
ms.date: 02/14/2020
ms.service: powerapps
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
manager: "kvivek"
ms.reviewer: 
ms.suite: 
ms.tgt_pltfrm: 
topic-status: Drafting
search.audienceType: 
  - maker
search.app: 
  - PowerApps
  - D365CE
---

# Delete a model-driven app

## Why apps need to be deleted

Apps may need to be deleted for a variety of reasons.  They may have been prepared purely as a development training exercise, with the intention of removing the application at a later date.  Also, the app may no longer be used in the organization, or may have been superceded in some way.

The process for removing them is extremely straightforward, however it is worth noting that there is a natural order at play when deleting components in Dataverse.  Whilst deleting apps can be done at any time in an unmanaged solution, it is not possible to delete tables that are used in the apps until such time as the app has been removed.  The same is true for table views.

> [!IMPORTANT]
> - If a model-driven app or site map was installed in the default solution as part of a managed solution, see [Delete a model-driven app that was installed as part of a managed solution](#delete-a-model-driven-app-that-was-installed-as-part-of-a-managed-solution).
> - First party model-driven apps, such as Dynamics 365 Sales, Dynamics 365 Customer Service, and Dynamics 365 Field Service can’t be deleted. You can hide these apps from users by removing the security roles that are assigned to the app. Notice that these apps will still be visible to users with environment maker, system administrator, and system customizer roles or any user with create privileges on the Model-driven App table. 

## Delete or remove apps that are obsolete in your environment.

1. Sign in to [Power Apps](https://make.powerapps.com/?utm_source=padocs&utm_medium=linkinadoc&utm_campaign=referralsfromdoc).
2. On the left navigation, select **Apps**.
> [!note]
> Many customisations to a table take place within [solutions](../model-driven-apps/model-driven-app-glossary.md#solution).  To update a model-driven app within a solution first navigate to your **solution**, then select the **app**.
3. Select the app that needs to be deleted want to delete, and then select **Delete** on the command bar.
4. In the confirmation message that appears there are two options.  
   1. **Remove solution** will remove the app from the solution, but retain it within the environment.
   2. **Delete from this environment** will delete it from both the solution and the environment

If the component has dependencies, such as relationships, these must be removed the app can be deleted. To see the dependencies of an app, select the app and then select **Show Dependencies** on the command bar.

5. When an app is deleted, it is best practice to associated site map. If this is not deleted, the site map designer displays an error the first time there is an attempt to create another app with the same name. However, it is possible to ignore the error, and the error will not appear when trying to create the app again.

## Delete a model-driven app that was installed as part of a managed solution

It is not possible to delete a model-driven app or site map that was installed in the environment as part of a managed solution.  Instead, the managed solution must be deleted.

## Delete a managed solution

All the components of a managed solution are deleted by deleting the solution.
1.	Sign in to [Power Apps](https://make.powerapps.com/?utm_source=padocs&utm_medium=linkinadoc&utm_campaign=referralsfromdoc). 
2.	On the left navigation, select **Solutions**.
3.	In the **Solutions** list, select the relevant managed solution then on the toolbar select **Delete**.

> [!note]
> Deleting a managed solution is business critical as it is likely that it is used for production purposes.  All solution components will be deleted and recovery of any data **may** be problematic.  It may be necessary to obtain the correct internal approvals before proceeding with this activity.

[!INCLUDE[footer-include](../../includes/footer-banner.md)]