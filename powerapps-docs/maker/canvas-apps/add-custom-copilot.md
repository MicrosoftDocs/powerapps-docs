---
title: Enable a custom Copilot to a canvas app
description: "Add a custom Copilot created in Microsoft Copilot Studio and enabled it for your canvas app."
author: mduelae
ms.topic: how-to
ms.custom: canvas
ms.reviewer: 
ms.date: 4/10/2025
ms.subservice: canvas-maker
ms.author: mkaur
search.audienceType: 
  - maker
contributors:
  - mduelae
---
# Add a custom Copilot to a canvas app (preview)

[This article is prerelease documentation and is subject to change.]

You can integrate a custom Copilot created in Microsoft Copilot Studio and enable it for your canvas app. This lets users interact with Copilot to ask questions about the data in your app. With just a few simple steps, you can embed a custom Copilot across all your canvas app screens without changing the app's design.

> [!IMPORTANT]
> - This is a preview feature.
> - Preview features aren't meant for production use and might have restricted functionality. These features are subject to [supplemental terms of use](https://go.microsoft.com/fwlink/?linkid=2189520), and are available before an official release so that customers can get early access and provide feedback.
> - Starting February 2, 2026, this feature will be removed. Makers will no longer be able to add a custom copilot to new Canvas apps. Existing apps that already use this will continue to function for now, but will be fully deprecated in the future.

> [!NOTE]
>
> App Copilot for canvas apps is currently rolling out and might not yet be available in your region. App Copilot may be available on [Power Apps mobile](../../mobile/run-powerapps-on-mobile.md) for mobile devices before it becomes available on the web browser during rollout.

## Availability

- This capability might not be available in your region yet. Learn more in [Explore Copilot features by geography and languages](https://releaseplans.microsoft.com/en-US/availability-reports/?report=copilotfeaturereport).
- During the rollout, this capability might be accessible on the [Power Apps mobile app](../../mobile/run-powerapps-on-mobile.md) before it becomes available on web browsers.
- To use copilots in Power Apps, you must enable data movement across regions for generative AI features. This is crucial if your organization and environment are located in different regions. For more information, see [Enable copilots and generative AI features](/power-platform/admin/geographical-availability-copilot\#enable-data-movement-across-regions).

## Prerequisites

Before using this feature, make sure the following prerequisites are met:

- Create a custom Copilot in [Copilot Studio](/microsoft-copilot-studio/fundamentals-get-started?tabs=web) and publish it in the same environment as your canvas app.

- Configure the custom Copilot with [user authentication in Microsoft Entra ID](/microsoft-copilot-studio/configuration-authentication-azure-ad).

- [Give makers and users access](/microsoft-copilot-studio/admin-share-bots?tabs=web) to the Copilot within the environment.


## Connect Copilot to your app

Open your [canvas app for editing](edit-app.md) in Power Apps Studio:

1. In the command bar, go to **Settings** > **Updates** > **Preview** tab, and set the toggle for **App Copilot** to **On**.

   You see a **Copilot** tab appear in **Settings**.

1. Select the **Copilot** tab. In the drop-down list under **Connect a copilot**, select a custom copilot published and shared in the same environment as your canvas app.

   :::image type="content" source="media/add-custom-copilot/copilot-tab.png" alt-text="Screenshot that shows the copilot tab in Settings and where you can select an app that was shared with you." lightbox="media/add-custom-copilot/copilot-tab.png":::

1. Once you select a Copilot, close the settings dialog box and publish the app. Once the app is published, users are able to use Copilot within it.

Copilot isn't visible when previewing an app in Power Apps Studio. To see Copilot in action, save and publish your app, and then open it using the Power Apps mobile app or a web browser.

> [!TIP]
> Removing the custom Copilot from the app will disable its functionality.

## Use Copilot in your app

- Open your canvas app in a web browser. On the command bar, select **Copilot**.

   :::image type="content" source="media/add-custom-copilot/copilot-chat-in-app.png" alt-text="Screenshot that shows the copilot chat in the app." lightbox="media/add-custom-copilot/copilot-chat-in-app.png":::

- In the Power Apps mobile app on iOS or Android devices, select the floating button to access Copilot. You can reposition the button or dismiss it. To use Copilot again after dismissing it, close and reopen the app.

## Difference between this feature and the Copilot control

This feature lets you add a custom Copilot created in Microsoft Copilot Studio to a canvas app. It doesn't require any changes to the app's layout. It's available both on the web and natively on mobile devices, and it can connect to existing custom Copilots created in Copilot Studio.

When you add a [Copilot control to a canvas app](add-ai-copilot.md), makers need to update the app's layout to accommodate the control, which is only available on the web. This control supports asking questions about your data or connecting to a new  [custom copilot from Copilot Studio](add-ai-copilot.md#customize-the-copilot-using-copilot-studio).

### See Also

[FAQ for Copilot](/microsoft-copilot-studio/faqs-copilot)
