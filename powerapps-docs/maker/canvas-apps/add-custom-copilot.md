---
title: Add a custom Copilot to a canvas app
description: "Add a custom Copilot to a canvas app in Power Apps."
author: mduelae
ms.topic: conceptual
ms.custom: canvas
ms.reviewer: 
ms.date: 10/10/2024
ms.subservice: canvas-maker
ms.author: mkaur
search.audienceType: 
  - maker
contributors:
  - mduelae
---

# Add a custom Copilot to a canvas app (preview)

[This article is prerelease documentation and is subject to change.]

Microsoft Copilot Studio lets makers develop custom Copilots using AI. With just a few steps, you can integrate your custom Copilot across all canvas app screens without altering the app's design. This feature is available both on the web and in the Power Apps mobile app.

> [!IMPORTANT]
>
> - This is a preview feature.
> - Preview features aren't meant for production use and might have restricted functionality. These features are subject to [supplemental terms of use](https://go.microsoft.com/fwlink/?linkid=2189520), and are available before an official release so that customers can get early access and provide feedback.

> [!NOTE]
>
> App Copilot for canvas apps is currently rolling out and might not yet be available in your region. App Copilot may be available on [Power Apps mobile](../../mobile/run-powerapps-on-mobile.md) for mobile devices before it becomes available on the web browser during rollout.

## Availability

- App Copilot for canvas apps is currently being rolled out and might not be available in your region yet. During the rollout, capability might be accessible on [Power Apps mobile](../../mobile/run-powerapps-on-mobile.md) for mobile devices before it becomes available on web browsers.
- To use copilots in Power Apps, you must enable data movement across regions for generative AI features. This is crucial if your organization and environment are located in different regions. For more information, see [Enable copilots and generative AI features](/power-platform/admin/geographical-availability-copilot\#enable-data-movement-across-regions).

## Prerequisites

- Allow data movement across regions for generative AI features. This step is important if your organization and your environment are in different regions. Learn more in [Enable copilots and generative AI features](/power-platform/admin/geographical-availability-copilot\#enable-data-movement-across-regions).
- Create a custom Copilot in [Copilot Studio](/microsoft-copilot-studio/fundamentals-get-started?tabs=web) and publish it in the same environment as the app.

- Configure the custom Copilot with [user authentication in Microsoft Entra ID](/microsoft-copilot-studio/configuration-authentication-azure-ad).

- [Give makers and users access](/microsoft-copilot-studio/admin-share-bots?tabs=web) to the custom Copilot within the environment.

## Connect a custom Copilot to a canvas app

Open your [canvas app open for editing](edit-app.md) in Power Apps Studio:

1. On the command bar, select the **Settings** > **Updates** > **Preview** tab and enable **App Copilot**.

   :::image type="content" source="media/add-custom-copilot/enable-app-copilot.png" alt-text="Screenshot of the loction of the App Copilot toggle in Seattings.":::

   You see a **Copilot** tab appear in **Settings**.

1. Select the **Copilot** tab. In the drop-down list under **Connect a copilot**, select a custom copilot published and shared in the same environment as your canvas app.

   :::image type="content" source="media/add-custom-copilot/copilot-tab.png" alt-text="Screenshot that shows the Copilot tab in Settings and where you can select an app that was shared with you." lightbox="media/add-custom-copilot/copilot-tab.png":::

1. Once you select a Copilot, close the settings dialog box and publish the app. App users can now use the App Copilot within the app.

Copilot isn't visible when previewing an app in Power Apps Studio. To view Copilot in action, save and publish your app, then open it in Power Apps mobile or a web browser.

> [!TIP]
> Removing the custom Copilot from the app will disable its functionality.

## Use App Copilot

- Open your canvas app in a web browser. On the command bar, select **Copilot**.

   :::image type="content" source="media/add-custom-copilot/copilot-chat-in-app.png" alt-text="Screenshot that shows the Copilot chat in the app." lightbox="media/add-custom-copilot/copilot-chat-in-app.png":::

- In the Power Apps mobile app on iOS or Android devices, select the floating button to access App Copilot. You can reposition the button or dismiss it. To use App Copilot again after dismissing it, close and reopen the app.

## Difference between App Copilot and Copilot control

**Copilot Control**: This feature requires makers to update their canvas app layout to accommodate the control and is only available on the web. It supports asking questions about your data or connecting to a new custom Copilot from Copilot Studio.

**App Copilot**: This feature doesn't require any changes to your canvas app layout. It's available both on the web and natively on mobile devices, and it can connect to pre-existing custom Copilots created in Copilot Studio.

### See Also

[FAQ for Copilot](/microsoft-copilot-studio/faqs-copilot)
