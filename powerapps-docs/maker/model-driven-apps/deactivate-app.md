---
title: Hide a model-driven app  | MicrosoftDocs
description: Find out how to hide a model-driven app from users with Power Apps
Keywords: 
author: matp
ms.subservice: mda-maker
ms.author: ansja
ms.reviewer: matp
ms.date: 08/17/2022
ms.topic: how-to
applies_to: 
  - "powerapps"
search.audienceType: 
  - maker
---
# Hide a model-driven app from users

Turn off a model-driven app to hide it from users who otherwise would be able to find and run it. When a model-driven app is turned off, it no longer appears in the common places where apps are found, such as the list of model-driven apps displayed in Power Apps Mobile or [Office apps](https://www.office.com/apps).

## Turn off a model-driven app

1. Sign in to [Power Apps](https://make.powerapps.com/?utm_source=padocs&utm_medium=linkinadoc&utm_campaign=referralsfromdoc).
1. Select the environment where the app is located.
1. Select **Solutions** on the left navigation pane, and then open the solution you want. [!INCLUDE [left-navigation-pane](../../includes/left-navigation-pane.md)]
1. Select the model-driven app to be hidden from all users, and then on the command bar select **...** > **Turn off**.

   :::image type="content" source="media/deactivate-app.png" alt-text="Turn off command for a model-driven app.":::

The **Status** of the app appears as **Off** from the solution's **Objects** view.

> [!NOTE]
>
> - Apps that are turned off are still visible to other users from the **Apps** area of Power Apps.
> - While a model-driven app is in a turned off state, it can't be played or shared from make.powerapps.com, however direct links to the app will continue to work.
> - Managed model-driven apps can't be turned off.

## Turn on a model-driven app

An app that is turned off can be turned on by following the same steps described earlier and then selecting **Turn on**.

### See also

[Privileges required to view and access apps](app-visibility-privileges.md)


[!INCLUDE[footer-include](../../includes/footer-banner.md)]
