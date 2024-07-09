---
title: Add a custom Copilot to a canvas app
description: "Add a custom Copilot to a canvas app in Microsoft Power Apps."
author: mduelae
ms.topic: conceptual
ms.custom: canvas
ms.reviewer: 
ms.date: 7/8/2024
ms.subservice: canvas-maker
ms.author: tapanm
search.audienceType: 
  - maker
contributors:
  - mduelae
---

# Add a custom Copilot to a canvas app

\[This article is prerelease documentation and is subject to change.\]

Microsoft Copilot Studio empowers makers to create their own custom Copilots with AI. In a few steps, you can add your custom Copilot across all your Canvas app screens without modifying your app's design. This feature is available on the web and natively on mobile devices.

> [!NOTE]
> App Copilot on Canvas is currently rolling out and might not yet be available in your region.

> [!IMPORTANT]
>
> - You must allow data movement across regions, for generative AI features, as a prerequisite to use copilots in Power Apps. This step is important if your organization and your environment are in different regions. For more information, see [Enable copilots and generative AI features](/power-platform/admin/geographical-availability-copilot\#enable-data-movement-across-regions).
> - Preview features aren't meant for production use and might have restricted functionality. These features are available before an official release so that customers can get early access and provide feedback.
> - For more information, go to our [preview terms](https://go.microsoft.com/fwlink/?linkid=2189520).

## What is the difference between App Copilot on Canvas apps and the Copilot control?

**Copilot control** requires makers to update their application to make space for the control and is only available on the web. The control feature supports asking questions about your data or connecting to a new (not existing) custom copilot from Copilot Studio.

**App Copilot** doesn't require updating the canvas app layout. App Copilot is available across web and natively on mobile devices and can connect to pre-existing custom Copilots created in Copilot Studio.

## How to enable App Copilot

### Prerequisites

- Create a custom Copilot in [Copilot Studio](/microsoft-copilot-studio/fundamentals-get-started?tabs=web) and publish it in the same environment as the app.

- Configure the custom Copilot with [user authentication in Microsoft Entra ID](/microsoft-copilot-studio/configuration-authentication-azure-ad).

- [Give makers and users access](/microsoft-copilot-studio/admin-share-bots?tabs=web) to the custom Copilot within the environment.

## Connect your custom Copilot to your Canvas app

In your Power Apps settings:

1. Go to **Settings** > **Updates** > **Preview** and enable **Copilot from app settings**.

   :::image type="content" source="media/add-custom-copilot/enable-copilot-setting.png" alt-text="Screenshot that shows where you can enable Copilot settings." lightbox="media/add-custom-copilot/enable-copilot-setting.png":::

1. You see a new Copilot tab appear in **Settings**. Here, you can select a custom Copilot published and shared with you within the same environment as the app.

   :::image type="content" source="media/add-custom-copilot/copilot-tab.png" alt-text="Screenshot that shows the Copilot tab in Settings and where you can select an app that was shared with you." lightbox="media/add-custom-copilot/copilot-tab.png":::

1. Select the Copilot you want to connect then close the settings and publish the app for users to access App Copilot in the Canvas app.

> [!TIP]
> Removing the custom Copilot from the app disables the functionality.

## Use App Copilot in Canvas apps

### On the web

1. Open your app in Power Apps.

   :::image type="content" source="media/add-custom-copilot/open-copilot-web.png" alt-text="Screenshot that shows an open Copilot app.":::

1. Open your custom Copilot with the Copilot icon in the top navigation bar.
   :::image type="content" source="media/add-custom-copilot/copilot-chat-in-app.png" alt-text="Screenshot that shows the Copilot chat in the app." lightbox="media/add-custom-copilot/copilot-chat-in-app.png":::

### On iOS and Android devices

A floating button enables users to access App Copilot. Users can move the button around or dismiss it. Once dismissed, the button returns after closing then reopening the app.
