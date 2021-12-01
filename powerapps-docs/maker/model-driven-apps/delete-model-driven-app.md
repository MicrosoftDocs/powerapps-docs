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
Delete or remove apps that are obsolete in your environment.

> [!IMPORTANT]
> - If a model-driven app or site map was installed in the default solution as part of a managed solution, see [Delete a model-driven app that was installed as part of a managed solution](#delete-a-model-driven-app-that-was-installed-as-part-of-a-managed-solution).
> - First party model-driven apps, such as Dynamics 365 Sales, Dynamics 365 Customer Service, and Dynamics 365 Field Service can’t be deleted. You can hide these apps from users by removing the security roles that are assigned to the app. Notice that these apps will still be visible to users with environment maker, system administrator, and system customizer roles or any user with create privileges on the Model-driven App table. 

1. Sign in to [Power Apps](https://make.powerapps.com/?utm_source=padocs&utm_medium=linkinadoc&utm_campaign=referralsfromdoc).
2. On the left navigation, select **Apps**. 
3. Select the app that you want to delete, and then select **Delete** on the command bar.
4. In the confirmation message that appears, select **Delete**.

   The app is deleted from your environment.
  
If the component has dependencies, such as relationships, you must remove the dependencies before you can delete the app. To see the dependencies of an app, select the app and then select **Show Dependencies** on the command bar.

> [!NOTE]
> When you delete the app, we recommend that you delete its associated site map. If you do not delete the associated site map, the site map designer displays an error the first time you try to create another app with the same name. However, you can ignore the error, and the error will not appear when you try to create the app again.

## Delete a model-driven app that was installed as part of a managed solution

To delete a model-driven app or site map that was installed in the environment as part of a managed solution, delete the managed solution. 

### Delete a managed solution

All the components of a managed solution are deleted by deleting the solution.
1.	Sign in to [Power Apps](https://make.powerapps.com/?utm_source=padocs&utm_medium=linkinadoc&utm_campaign=referralsfromdoc). 
2.	On the left navigation, select **Solutions**.
3.	In the **Solutions** list, select the managed solution you want to delete and then on the toolbar select **Delete**.

[!INCLUDE[footer-include](../../includes/footer-banner.md)]