---
title: Use Copilot to create and edit Power Fx formulas in Power Apps
description: Learn how to use Copilot, an AI feature in Power Apps, to create and edit Power Fx formulas in the formula bar from natural language or code comments.
author: warrenbryant-msft
ms.author: warrenbryant
ms.date: 01/12/2026
ms.update-cycle: 180-days
ms.topic: how-to
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

Copilot is an AI feature in Power Apps Studio that helps you create and change Power Fx formulas quickly. Use Copilot in the formula bar to explain Power Fx formulas in everyday language or generate Power Fx formulas from natural language or code comments.

## Prerequisites

An admin must enable Copilot for your environment and tenant. For more information, see [Copilot in Power Apps overview](ai-overview.md).

## Explain a formula

Use Copilot in the formula bar to learn what a formula does in plain language.

1. Select a control and its property. For example, select a label control with its **Text** property.

1. On the formula bar, select the dropdown near the **fx** field label, and then select **Explain this formula**.

   :::image type="content" source="media/copilot/ufb-copilot-dropdown.png" alt-text="Screenshot of the Copilot functionality menu showing the Explain this formula item.":::

   Alternatively, select part of a formula, select the dropdown near the **fx** field label, and then select **Explain this selection** to explain only that part.

   :::image type="content" source="media/copilot/copilot-explain-section.png" alt-text="Screenshot of Copilot's option to Explain this section, showing part of the formula highlighted by the user." lightbox="media/copilot/copilot-explain-section.png":::

    Copilot gives you an explanation of the formula that you can copy and insert as a code comment, or share with other makers working on the same app. When Copilot explains a selection, it can add context if that's important for the explanation.

    :::image type="content" source="media/copilot/copilot-explanation.png" alt-text="Screenshot of Copilot's explanation of a formula.":::

### Known limitations of explaining formulas

- The maximum length for a formula explanation is 5,000 characters. If the formula is longer, use a partial explanation to make sure it works.
- Copilot recognizes only default properties in Power Apps.
- Copilot doesn't recognize user-defined functions.

> [!NOTE]
> AI-generated content can be inaccurate, so check it for accuracy.

## Generate formulas from code comments

Copilot can generate Power Fx formulas from code comments in the formula bar. You can accept the suggestion or type the formula yourself. Formula code comments can also serve as documentation for your formulas, just like regular code comments.

1. With your canvas app open for editing, type a code comment using `//` or `/*` in the formula bar.

    :::image type="content" source="media/copilot/ufb-comment-copilot.png" alt-text="Screenshot of a comment typed in the Copilot formula bar." lightbox="media/copilot/ufb-comment-copilot.png":::

    Wait a few seconds for Copilot to generate a formula suggestion or press `Enter` to generate it immediately.

1. Press `Tab` on the keyboard to accept and use the suggested formula. You can also type through the suggestion.

    :::image type="content" source="media/copilot/ufb-commentfx-copilot.png" alt-text="Screenshot of a comment with a suggested formula." lightbox="media/copilot/ufb-commentfx-copilot.png":::

The suggestion remains until you select elsewhere or type a character that doesn't match the suggestion.

You can keep the comments used for generating Power Fx formulas in the formula bar as documentation, similar to traditional code comments.

> [!NOTE]
>
> - If Copilot doesn't provide a suggestion, then it couldn't generate a formula based on your comment. Try rephrasing the comment.
> - We recommend enclosing in quotes the elements that you want to include in your formula, such as `"Button1.text"`.

### Known limitations of generating formulas from code comments

- Copilot works on a singular control and property, and it doesn't make changes to other controls or properties to achieve the desired outcome.
- Copilot doesn't take existing formula text into account.
- Copilot only recognizes default properties in Power Apps.
- Copilot doesn't recognize user-defined functions.
- Code comments only work with general Power Fx functions, and not Power Apps-specific functions such as `Navigate()`.
- The advanced panel doesn't trigger suggestions.
- Existing formulas for the property aren't included in the suggestion.

## Create a formula (preview)

[This section is prerelease documentation and is subject to change.]

From the Copilot dropdown menu in the formula bar, you can now generate a formula by using natural language to make a discrete request.

> [!NOTE]
> The **Copilot for formulas** feature is on by default. To turn it off, open your app, go to **Settings** > **Updates** > **Preview**, and find the **Copilot for formulas** toggle. If you turn off the setting, the **Create a formula (preview)** menu option disappears from the Copilot dropdown menu in the formula bar.

### Use Copilot to create a formula from a discrete request

1. Select a control, like a **Text label**, and its corresponding property, such as **Text**.

1. On the formula bar, select the **Copilot functionality menu** > **Create a formula**.

    :::image type="content" source="media/copilot/ufb-create-input.png" alt-text="Screenshot of the Create a Formula functionality showing a sample input." lightbox="media/copilot/ufb-create-input.png":::
1. In the Copilot text box, type your request, such as *show today's day of the week*.
1. Select the **Create** arrow to submit your request.
1. Copilot attempts to create a formula. Select **Apply** to insert the formula in the same position as the Copilot interface, or update and resubmit your request.

    :::image type="content" source="media/copilot/ufb-create-formula.png" alt-text="Screenshot of the Create a Formula functionality showing recommended formula." lightbox="media/copilot/ufb-create-formula.png":::

    You see the result after you apply the formula.

    :::image type="content" source="media/copilot/copilot-request-result.png" alt-text="Screenshot that shows the day of the week in a text label.":::

  > [!NOTE]
  > The same limitations apply for creating formulas from a discrete request as [generating formulas from code comments](ai-formulas-formulabar.md#known-limitations-of-generating-formulas-from-code-comments).

## Responsible AI

Understand the choices you have when working with AI. Learn more in [FAQ about using AI responsibly in Power Apps](../common/responsible-ai-overview.md). Review the [Power Fx Copilot FAQ](../common/faqs-copilot-powerfx.md) for questions about this feature specifically.

## Language support

The following table lists the languages available for the formula bar copilot features. The list is based on the settings in your Power Platform environment and browser.

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
