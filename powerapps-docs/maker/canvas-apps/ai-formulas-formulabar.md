---
title: Use Copilot to create and edit Power Fx formulas in Power Apps
description: Learn how to use Copilot, an AI feature in Power Apps, to create and edit Power Fx formulas in the formula bar from natural language or code comments.
author: warrenbryant-msft
ms.author: warrenbryant
ms.date: 11/13/2024
ms.topic: conceptual
ms.reviewer: mkaur
ms.subservice: canvas-maker
ms.collection:
  - bap-ai-copilot
  - get started
search.audienceType:
  - maker
contributors:
  - warrenbryant-msft
  - mduelae
ai-usage: ai-assisted
ms.custom: 
  - ai-gen-diyeditor
  - canvas
---

# Use Copilot to create and edit Power Fx formulas

Copilot is an AI feature in Power Apps Studio that helps you create and modify Power Fx formulas quickly. You can use Copilot in the formula bar to explain Power Fx formulas in natural language or generate Power Fx formulas from natural language or code comments.


## Prerequisites

Copilot must be enabled for your environment and tenant. For more information, see [Enable or disable Copilot (preview) in Power Apps](ai-overview.md#disable-copilot-in-power-apps).

 
> [!NOTE]
> By default, the new formula bar is enabled. If the **Copilot functionality menu** isn't visible, check the following app settings in Power Apps Studio:
> 1. On the command bar, select **Settings** > **Updates**.
> 1. From the **Retired** tab, turn off the **Legacy formula bar** toggle.


## Explain a formula

Use Copilot in the formula bar to understand what a formula is doing in plain language.

1. Select a control and its corresponding property.

1. On the formula bar, select the **Copilot functionality menu** > **Explain this formula**, or select a subset of a formula and then select the **Copilot functionality menu** > **Explain this Selection** to explain only that part.

    :::image type="content" source="media/copilot/ufb-copilot-dropdown.png" alt-text="Screenshot of the Copilot functionality menu showing the Explain this formula item.":::

    Copilot provides an explanation of the formula that you can copy and insert as a code comment or share with other makers who are working on the same app. When explaining a selection, Copilot may also provide additional context if it is important for the explanation.

    :::image type="content" source="media/copilot/ufb-explanation-copilot.png" alt-text="Screenshot of Copilot's explanation of a formula.":::

### Known limitations of explaining formulas

- The maximum length for a formula explanation is 5,000 characters. If the formula exceeds this limit, use a partial explanation to ensure it works.
- Copilot only recognizes default properties in Power Apps.
- Copilot doesn't recognize user-defined functions.

> [!NOTE]
> AI generated content may be inaccurate and should be checked for accuracy.

## Generate formulas from code comments 

Copilot can generate Power Fx formulas from code comments in the formula bar. You can accept the suggestion or type the formula yourself. Formula code comments can also serve as documentation for your formulas, just like regular code comments.

1. With your canvas app open for editing, type a code comment using `//` or `/*` in the formula bar.

    :::image type="content" source="media/copilot/ufb-comment-copilot.png" alt-text="Screenshot of a comment typed in the Copilot formula bar." lightbox="media/copilot/ufb-comment-copilot.png":::

    Wait a few seconds for Copilot to generate a formula suggestion or press Enter to generate it immediately.

1. Press Tab on the keyboard to accept and use the suggested formula. You can also type through the suggestion.

    :::image type="content" source="media/copilot/ufb-commentfx-copilot.png" alt-text="Screenshot of a comment with a suggested formula." lightbox="media/copilot/ufb-commentfx-copilot.png":::

The suggestion remains until you select elsewhere or type a character that doesn't match the suggestion.

You can keep the comments used for generating Power Fx formulas in the formula bar as documentation, similar to traditional code comments.

> [!NOTE]
>
> - If Copilot doesn't provide a suggestion, then it couldn't generate a formula based on your comment. Try rephrasing the comment.
> - We recommend enclosing in quotes the elements that you want to include in your formula, such as `"Button1.text"`.

### Known limitations of generating formulas from code comments

- Copilot works on that singular control and property, and it won't make changes to other controls or properties to achieve the desired outcome.
- Copilot doesn't take existing formula text into account.
- Copilot only recognizes default properties in Power Apps.
- Copilot doesn't recognize user-defined functions.
- Code comments only work with general Power Fx functions, and not Power Apps-specific functions such as `Navigate()`.
- The advanced panel doesn't trigger suggestions.
- Existing formulas for the property aren't included in the suggestion.


## Create a formula (preview)

[This section is prerelease documentation and is subject to change.]

From the Copilot button in the formula bar, you can now generate a formula from natural language from a discrete request.

### Prerequisites

Before you can use Copilot to create a formula from a discrete request in your canvas app, you need to turn on **Copilot for formula** in the app settings in [Power Apps](https://make.powerapps.com/).

1. Open your [canvas app for editing](edit-app.md) in Power Apps Studio. On the command bar, select **Settings** > **Updates**.
1. On the **Preview** tab, find and turn on the **Copilot for formulas** setting.

### Use Copilot to create a formula from a discrete request

1. Select a control and its corresponding property.

1. On the formula bar, select the **Copilot functionality menu** > **Create a formula**.

    :::image type="content" source="media/copilot/ufb-copilot-dropdown.png" alt-text="Screenshot of the Copilot functionality menu showing the Create a formula item.":::

    The Copilot menu opens inline when the formula bar is expanded, or below the formula bar if it's collapsed.

1. In the Copilot text box, type your request, such as *show today's day of the week*.

    :::image type="content" source="media/copilot/ufb-create-input.png" alt-text="Screenshot of the Ceate a Formula functionality showing a sample input.":::

1. Copilot will attempt to create a formula. Select **Accept** to insert the formula in the same position as the Copilot interface, or update and resumbit your request.

    :::image type="content" source="media/copilot/ufb-create-formula.png" alt-text="Screenshot of the Ceate a Formula functionality showing recommended formula.":::

  > [!NOTE]
  > The same limitations apply for creating a formulas from a discrete request as [generating formulas from code comments](ai-formulas-formulabar.md#known-limitations-of-generating-formulas-from-code-comments).



## Responsible AI

Understand the choices you have when working with AI. Learn more in [FAQ about using AI responsibly in Power Apps](../common/responsible-ai-overview.md). Review the [Power Fx Copilot FAQ](../common/faqs-copilot-powerfx.md) for questions about this feature specifically.

## Language Support

The following table lists the languages available for the formula bar copilot features, which is based on the settings in your Power Platform environment and browser.

| **Name** | **Language Code** | **Functionality Supported** |
|----------|-------------------|-----------------------------|
| English | en-US | Explain a formula, Comment generated formulas, Create a formula|
| Chinese (simplified) - China | zh-Hans | Explain a formula, Comment generated formulas |
| Czech - Czech Republic | cs-CZ | Explain a formula, Comment generated formulas |
| Danish - Denmark | da-DK | Explain a formula, Comment generated formulas |
| Dutch - Netherlands | nl-NL | Explain a formula, Comment generated formulas |
| Finnish - Finland | fi-FI | Explain a formula, Comment generated formulas |
| French - France | fr-FR | Explain a formula, Comment generated formulas |
| German - Germany | de-DE | Explain a formula, Comment generated formulas |
| Greek - Greece | el-GR | Explain a formula, Comment generated formulas |
| Italian - Italy | it-IT | Explain a formula, Comment generated formulas |
| Japanese - Japan | ja-JP | Explain a formula, Comment generated formulas |
| Korean - Korea | ko-KR | Explain a formula, Comment generated formulas |
| Norwegian (Bokmål) - Norway | nb-NO | Explain a formula, Comment generated formulas |
| Polish - Poland | pl-PL | Explain a formula, Comment generated formulas |
| Portuguese - Brazil | pt-BR | Explain a formula, Comment generated formulas |
| Russian - Russia | ru-RU | Explain a formula, Comment generated formulas |
| Spanish (Traditional Sort) - Spain | es-ES | Explain a formula, Comment generated formulas |
| Swedish - Sweden | sv-SE | Explain a formula, Comment generated formulas |
| Thai - Thailand | th-TH | Explain a formula, Comment generated formulas |
| Turkish - Türkiye | tr-TR | Explain a formula, Comment generated formulas |



## Related information

[Copilot comment generated formulas (video)](https://youtu.be/kV60VZoPoWw?feature=shared)
