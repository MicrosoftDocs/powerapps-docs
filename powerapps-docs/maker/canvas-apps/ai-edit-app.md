---
title: Use natural language to edit an app using the Copilot panel
description: Edit your app through conversation with Copilot in Power Apps Studio.
author: mduelae
ms.topic: conceptual
ms.custom: canvas
ms.collection: 
    - bap-ai-copilot
    - get started
ms.reviewer: 
ms.date: 5/3/2024
ms.subservice: canvas-maker
ms.author: mkaur
search.audienceType: 
  - maker
contributors:
  - mduelae
---

# Continue editing your app with Copilot (preview)

[This article is prerelease documentation and is subject to change.]

Build and continue editing your app with the help of Copilot powered by AI. Tell Copilot what changes you want to make to your app in simple language, and let AI do the work for you.

The Copilot panel is available when you edit a canvas app in Power Apps Studio. You can edit your app by telling Copilot what kind of changes you want to make such as add a screen, configure navigation, styling a single control, or bulk editing.

> [!div class="mx-imgBorder"]
> ![Copilot panel.](media/artificial-intelligence/copilot-pane-04252024.png)

> [!IMPORTANT]
> - Preview features aren’t meant for production use and may have restricted functionality. These features are available before an official release so that customers can get early access and provide feedback.
> - For more information, go to our [preview terms](https://go.microsoft.com/fwlink/?linkid=2189520).
> - This capability is powered by [ Azure OpenAI Service](/azure/cognitive-services/openai/overview).
> - This capability may be subject to usage limits or capacity throttling.


## Prerequisites

Prerequisites for Copilot in Power Apps features: [Copilot in Power Apps overview (preview)](ai-overview.md)

## What's supported

Copilot in Power Apps supports the following commands:

- [Use a screen template](add-screen-context-variables.md) to add a new screen.
- Modify the properties of various controls. Supported controls: 
    - Screen
    - Horizontal and Vertical containers
    - Gallery
    - Edit form
    - Button
    - Text label
    - Text input

    > [!NOTE]
    > - This feature supports English and its variants.

## Sample commands you can try

When you open the Copilot pane, you can select any of the three cards to explore preset prompts that demonstrate Copilot's capabilities. You can also try the commands listed in the table.

| Scenario      | Commands |
| ----------- | ----------- |
|Add a new screen using template	      |Adding a new email screen|
|             |Adding a new screen|
|             |Add a new screen with header body and footer|
|Add/edit/style a control	|Add a new button|
|             |Change selected button to have width 100|
|             |Add a new icon|
|             |Add a new text label|
|             |Add a submit button and a cancel button for the form|
|Bulk editing	|Change all buttons to gray|
|             |Change all labels in the selected container to be red|
|Working with containers	|Add a button to the selected container|
|Templatized formulas|	When clicking on Button1, show screen 2|
|Modern theming|Change my app to deep forest green|

## Use Copilot to edit your app

1. Sign in to [Power Apps](https://make.powerapps.com) and open a canvas app for editing.
1. In Power Apps Studio, on the top right, select **Copilot**.
1. In the **Copilot** panel, chat with Copilot and describe the changes you want to make such as  **Add a  new screen**.

   > [!div class="mx-imgBorder"]
   > ![Add a screen.](media/artificial-intelligence/copilot-pane-add-screen-04252024.png)


[!INCLUDE[footer-include](../../includes/footer-banner.md)]
