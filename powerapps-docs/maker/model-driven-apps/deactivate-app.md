---
title: Hide a model-driven app  | MicrosoftDocs
description: Find out how to hide a model-driven app from users with Power Apps
Keywords: 
author: matp
ms.subservice: mda-maker
ms.author: ansja
ms.reviewer: matp
manager: kvivek
ms.date: 01/05/2021
ms.service: powerapps
ms.topic: how-to
applies_to: 
  - "powerapps"
search.audienceType: 
  - maker
search.app: 
  - PowerApps
---
# Hide a model-driven app from users

Deactivate a model-driven app to hide it from users who otherwise would be able to find and run it. When a model-driven app is deactivated, it no longer appears in the common places where apps are found, such as the list of model-driven apps displayed in Power Apps Mobile or [Office apps](https://www.office.com/apps).

## Deactivate a model-driven app

1. Sign in to [Power Apps](https://make.powerapps.com/?utm_source=padocs&utm_medium=linkinadoc&utm_campaign=referralsfromdoc).
1. Select the environment in which the app is located
1. Select **Solutions**
1. Select the model-driven app to be hidden from all users, select **...** to the right of the app or in the top menu, and then select **Deactivate** on the command bar or app context menu.

   :::image type="content" source="media/deactivate-app.png" alt-text="Deactivate command for a model-driven app.":::

The **Status** of the app appears as **Off** from the solution's **Objects** view.

> [!NOTE]
> - Deactivated apps are still visible to other users from the **Apps** area of Power Apps.
> - While a model-driven app is in a deactivated state, it can't be played or shared.

## Reactive a model-driven app

A deactivated app can be reactivated by following the same process and then selecting **Activate**.

### See also

[Privileges required to view and access apps](app-visibility-privileges.md)


[!INCLUDE[footer-include](../../includes/footer-banner.md)]