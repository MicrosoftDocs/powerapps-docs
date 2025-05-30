---
title: Edit your app with Copilot in Power Apps Studio (preview)
description: Learn how to use natural language to edit your app with Copilot, an AI assistant that helps you make changes to your app in Power Apps Studio.
author: mduelae
ms.topic: how-to
ms.collection: 
    - bap-ai-copilot
    - get started
ms.reviewer: 
ms.date: 5/27/2025
ms.subservice: canvas-maker
ms.author: mkaur
search.audienceType: 
  - maker
contributors:
  - mduelae
ms.custom:
  - canvas
  - ai-gen-diyeditor
ai-usage: ai-assisted
---

# Edit your app with Copilot in Power Apps Studio (preview)

[!INCLUDE [preview-banner](~/../shared-content/shared/preview-includes/preview-banner.md)]

Edit your apps without writing code or designing screens. With Copilot in Power Apps, you can use natural language to describe the changes you want to make, and AI does the rest.

Copilot is a feature in Power Apps that helps you edit your apps with AI assistance. You can access Copilot from Power Apps Studio when you edit a canvas app. Tell Copilot what kind of changes you want to make in the Copilot conversation pane, such as adding a screen, configuring navigation, styling a control, or editing multiple controls at a time.

:::image type="content" source="media/artificial-intelligence/copilot-pane.png" alt-text="Screenshot of the Power Apps Studio, showing an app open for editing in the center of the screen and the Copilot panel on the right side of the screen.":::

> [!IMPORTANT]
>
> - This is a preview feature.
> - Preview features aren't meant for production use and might have restricted functionality. These features are subject to [supplemental terms of use](https://go.microsoft.com/fwlink/?linkid=2189520), and are available before an official release so that customers can get early access and provide feedback.

> [!NOTE]
>
> This capability:
>
> - Is powered by [Azure OpenAI Service](/azure/cognitive-services/openai/overview)
> - Might be subject to usage limits or capacity throttling

## Prerequisites

Ensure you meet the prerequisites and region availability in [Copilot in Power Apps overview (preview)](ai-overview.md).

## Supported languages

The following table lists the languages that Copilot understands.

You can track future language availability in the [Copilot product report](https://releaseplans.microsoft.com/en-US/availability-reports/?report=copilotproductreport).

| **Name**                           | **Language Code** |
|------------------------------------|-------------------|
| English                            | en-US             |
| Chinese (simplified)               | zh-Hans           |
| Czech                              | cs-CZ             |
| Danish                             | da-DK             |
| Dutch                              | nl-NL             |
| Finnish                            | fi-FI             |
| French                             | fr-FR             |
| German                             | de-DE             |
| Greek                              | el-GR             |
| Italian                            | it-IT             |
| Japanese                           | ja-JP             |
| Korean                             | ko-KR             |
| Norwegian (Bokmål)                 | nb-NO             |
| Polish                             | pl-PL             |
| Portuguese                         | pt-BR             |
| Russian                            | ru-RU             |
| Spanish (Traditional Sort)         | es-ES             |
| Swedish                            | sv-SE             |
| Thai                               | th-TH             |
| Turkish                            | tr-TR             |

## Use Copilot to edit your app

1. Sign in to [Power Apps](https://make.powerapps.com) and open a canvas app for editing.
1. In Power Apps Studio, in the upper-right corner of the page, select **Copilot**.
1. In the Copilot text box, describe a change you want to make, such as  *Add an email screen*.

:::image type="content" source="media/artificial-intelligence/ask-copilot.png" alt-text="Screenshot that shows where to ask Copilot a request.":::

## What you can do with Copilot in Power Apps

Copilot in Power Apps allows you to perform the following tasks:

- Add a new screen using a template. Learn more in [Add a screen](add-screen-context-variables.md).
- Modify the properties of some controls, including:
  - Screen
  - Horizontal and vertical containers
  - Gallery
  - Edit form
  - Button
  - Text label
  - Text input

## Sample commands you can try

When you open the Copilot pane, you can select from three preset prompts that demonstrate Copilot's capabilities: **Create**, **Change**, and **Ask**. You can also try entering the following commands in the Copilot text box.

> [!NOTE]
>
> Some Copilot requests are built into preview features, which only work when **Try the new data experience** toggle is turned on from your Power Apps home page. Learn more in [Build apps with Copilot in Power Apps (preview)](ai-conversations-create-app.md#prerequisites).

### Scenario: Add a new screen using a template

- Add a new screen
- Add a new email screen
- Add a new screen with header, body, and footer

### Scenario: Add/edit/style a control

- Add a new button
- Change the selected button to have width 100
- Add a new icon
- Add a new text label
- Add a submit button and a cancel button to the form

### Scenario: Bulk editing

- Change all buttons to gray
- Change all labels in the selected container to red

### Scenario: Working with containers

- Add a button to the selected container

### Scenario: Templatized formulas

- When the user selects `Button1`, show `Screen2`

### Scenario: Modern theming

- Change my app to deep forest green

[!INCLUDE[footer-include](../../includes/footer-banner.md)]


## Related information

[Editing your app with Copilot in Power Apps (video)](https://youtu.be/g9fFoQ5CETk?feature=shared)
