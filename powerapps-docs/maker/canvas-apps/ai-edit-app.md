---
title: Use natural language to edit an app using the Copilot panel
description: Edit your app through conversation with AI Copilot in Power Apps Studio.
author: mduelae
ms.topic: conceptual
ms.custom: canvas
ms.collection: get-started
ms.reviewer: 
ms.date: 6/5/2022
ms.subservice: canvas-maker
ms.author: mkaur
search.audienceType: 
  - maker
contributors:
  - mduelae
---

# Use natural language to edit an app (preview)

[This article is prerelease documentation and is subject to change.]

Edit and build your app with the power of AI and Copilot. Tell AI what changes you want to make to your app in simple language, and let AI do the work for you.

The Copilot panel is available when you edit an app in Power Apps Studio. Use AI to build your app by telling the AI assistant what kind of changes you want to make such as add a screen or add a text label.

> [!div class="mx-imgBorder"]
> ![Copilot panel.](media/artificial-intelligence/copilot-pane.png)

> [!IMPORTANT]
> - To use this capability you must have a [Microsoft Dataverse database](/power-platform/admin/create-database) in your environment.
> - Preview features aren’t meant for production use and may have restricted functionality. These features are available before an official release so that customers can get early access and provide feedback.
> - For more information, go to our [preview terms](https://go.microsoft.com/fwlink/?linkid=2189520).
> - This capability is powered by [ Azure OpenAI Service](/azure/cognitive-services/openai/overview).
> - This capability is in process of rolling out, and may not be available in your region yet.
> - This capability may be subject to usage limits or capacity throttling.


## Prerequisites

Prerequisites for AI features: [AI Copilot overview (preview)](ai-overview.md)

## What's supported

AI Copilot supports the following commands:

- [Use a screen template](add-screen-context-variables.md) to add a new screen.
- Modify the properties of various controls. Supported controls: 
    - Screen
    - Container
    - Gallery
    - From
    - Button
    - Label
    - Text input
    - Containers 
    > [!NOTE]
    > [Modern controls](controls/modern-controls/overview-modern-controls.md) are not supported.
- Make bulk updates to controls within a single screen and utilize formula templates.

## Use Copilot to edit your app

1. Open your app for editing in [Power Apps Studio](https://create.powerapps.com).
1. On the app actions menu, select **Copilot**.
1. In the **Copilot** panel, describe what changes you want to make such as **Add a  new screen**.

   > [!div class="mx-imgBorder"]
   > ![Add a screen.](media/artificial-intelligence/copilot-pane-add-screen.png)


[!INCLUDE[footer-include](../../includes/footer-banner.md)]
