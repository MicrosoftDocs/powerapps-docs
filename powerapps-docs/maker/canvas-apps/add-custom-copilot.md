---
title: Add a custom Copilot to a canvas app
description: "Add a custom Copilot to a canvas app in Microsoft Power Apps."
author: mduelae
ms.topic: conceptual
ms.custom: canvas
ms.reviewer: 
ms.date: 7/8/2024
ms.subservice: canvas-maker
ms.author: mkaur
search.audienceType: 
  - maker
contributors:
  - mduelae
---

# Add a custom Copilot to a canvas app (preview)

[This article is prerelease documentation and is subject to change.]

Microsoft Copilot Studio empowers makers to create their own custom Copilots with AI. In a few steps, you can add your custom Copilot across all your canvas app screens without modifying your app's design. You can use this feature both on the web and through the Power Apps mobile app.

> [!IMPORTANT]
> - App Copilot for canvas apps is currently rolling out and might not yet be available in your region.
> - You must allow data movement across regions, for generative AI features, as a prerequisite to use copilots in Power Apps. This step is important if your organization and your environment are in different regions. For more information, see [Enable copilots and generative AI features](/power-platform/admin/geographical-availability-copilot\#enable-data-movement-across-regions).
> - Preview features aren't meant for production use and might have restricted functionality. These features are available before an official release so that customers can get early access and provide feedback.
> - For more information, go to our [preview terms](https://go.microsoft.com/fwlink/?linkid=2189520).

## What is the difference between App Copilot in canvas apps and the Copilot control?

**Copilot control** requires makers to update their canvas app to make space for the control and is only available on the web. The control feature supports asking questions about your data or connecting to a new (not existing) custom copilot from Copilot Studio.

**App Copilot** doesn't require updating the canvas app layout. App Copilot is available across web and natively on mobile devices and can connect to pre-existing custom Copilots created in Copilot Studio.

## How to enable App Copilot

### Prerequisites

- Create a custom Copilot in [Copilot Studio](/microsoft-copilot-studio/fundamentals-get-started?tabs=web) and publish it in the same environment as the app.

- Configure the custom Copilot with [user authentication in Microsoft Entra ID](/microsoft-copilot-studio/configuration-authentication-azure-ad).

- [Give makers and users access](/microsoft-copilot-studio/admin-share-bots?tabs=web) to the custom Copilot within the environment.

## Connect your custom Copilot to your canvas app


Open your [canvas app open for editing](edit-app.md) in Power Apps Studio:

1. On the command bar, select **Settings** > **Updates** > **Preview** tab and enable **Copilot from app settings**.

1. You'll see a **Copilot** tab appear in **Settings**. From the drop-down list, select a custom Copilot that's published and shared in the same environment as your canvas app.

   :::image type="content" source="media/add-custom-copilot/copilot-tab.png" alt-text="Screenshot that shows the Copilot tab in Settings and where you can select an app that was shared with you." lightbox="media/add-custom-copilot/copilot-tab.png":::

1. When your select a copilot close the settings and publish the app. This lets users to App Copilot in the canvas app.

> [!TIP]
> Removing the custom Copilot from the app disables the functionality.

## Use App Copilot 

- Open your canvas app in a web broswer. On the command bar, select **Copilot**.

   :::image type="content" source="media/add-custom-copilot/copilot-chat-in-app.png" alt-text="Screenshot that shows the Copilot chat in the app." lightbox="media/add-custom-copilot/copilot-chat-in-app.png":::

- In Power Apps mobile running on iOS or Android devices, select the floating button to access App Copilot. You can move the button around or dismiss it. To use App Copilot after dismissing it, close and reopen the app. 
