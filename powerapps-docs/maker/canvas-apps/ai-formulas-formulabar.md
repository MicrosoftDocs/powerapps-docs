---
title: Create and edit formulas with Copilot
description: How to interact with formulas in the formula bar using AI.
author: warrenbryant-msft
ms.topic: conceptual
ms.custom: canvas
ms.reviewer: mkaur
ms.date: 7/22/2024
ms.subservice: canvas-maker
ms.author: warrenbryant
search.audienceType: 
  - maker
ms.collection: 
    - bap-ai-copilot
    - get started
contributors:
  - warrenbryant-msft
  - mduelae
---

# Create Power Fx formulas with Copilot

 Use Copilot in Power Apps to create and modify Power Fx formulas quickly. You can use Copilot in the formula bar to help explain Power Fx formulas in natural language, or create Power Fx formulas from natural language.

## Prerequisites
- To use this feature, Power Fx formula bar must be turned on.
- Copilot must be enabled for your environment and tenant. For more information, see [Enable or disable Copilot (preview) in Power Apps](ai-overview.md#enable-or-disable-copilot-preview-in-power-apps).
> [!NOTE]
> AI generated content may be inaccurate and should be checked for accuracy.


## Explain a formula

Use Copilot in the formula bar to understand what a formula is doing.

1. Select a control and its corresponding property.
1. On the formula bar, select the **Copilot functionality menu** > **Explain This Formula**.
:::image type="content" source="media/copilot/ufb-explain-copilot.png" alt-text="Explain this formula":::

    When Copilot provides an explanation of the formula, you can copy and insert it as a code comment or share it with other makers who are working on the same app.
:::image type="content" source="media/copilot/ufb-explanation-copilot.png" alt-text="Formula explanation":::


### Known Limitations
- There's a 5,000 character limit for formula explanations.
- Copilot in Power Apps is only aware of default properties.
- User defined functions aren't supported.

## Copilot comment generated formulas

When you add a comment in the formula bar, Copilot will attempt to provide a suggested formula. You have the option to accept the suggestion or manually type the formula. These comments can serve as documentation in the formula bar, just like regular code comments.

1. With your canvas app open for editing, type a code comment using **//** or **/*** in the formula bar.
:::image type="content" source="media/copilot/ufb-comment-copilot.png" alt-text="Typed comment":::

    Wait few seconds for Copilot to generate a formula recommendation or press enter to generate immediately.

1. Use the **Tab key** on the keyboard to select and use the recommended formula. You can also type through the recommendation.
:::image type="content" source="media/copilot/ufb-commentfx-copilot.png" alt-text="Typed comment with recommended formula":::

    The suggested formula remains until you select elsewhere or type a character that doesn't align with the recommendation. You can keep comments used for generating Power Fx formulas in the formula bar as documentation, similar to traditional code comments.
    
> [!NOTE]
> - If Copilot doesn't provide a suggestion, it couldn't generate a formula based on your comment. Try rephrasing or modifying the comment.
> - We recommend, enclosing the element you want to incorporate in your formula within quotes such as **"Button1.text"**.


### Known Limitations
- Copilot in Power Apps only recognizes the default properties within the app.
- Code comments only work with general Power Fx functions, and not Power Apps specific functions such as **Navigate()**.
- The advanced panel doesn't trigger suggestions.
- Existing formulas for that property aren't included in the recommendation.
- User defined functions aren't supported.


### Enable or disable Copilot comment generated formulas


 Copilot comment generated formulas are enabled by default for new apps, and disabled by default for existing apps, but can be enabled or disabled for any app from app settings.

- Go to **Settings** > **Upcoming features** > **New**. Set the toggle to **On** or **Off** for **Copilot comment-generated formulas**.

> [!NOTE]
> When **Copilot comment generated formulas** is fully integrated into the platform, it will be enabled for all apps and it will not be possible to disable it.

## Responsible AI

Review the Microsoft Documentation on [FAQ about using AI responsibly in Power Apps](../common/responsible-ai-overview.md) to understand the choices a user has when working with AI. Additionally, review the [Power Fx Copilot FAQ](../common/faqs-copilot-powerfx.md) for questions regarding this functionality specifically.

## Language Support

The following table lists the languages available for the formula bar copilot features, which is based on the settings in your Power Platform environment and browser.

| **Name**                           | **Language Code** | **Functionality Supported**                   |
|------------------------------------|-------------------|-----------------------------------------------|
| English                            | en-US             | Explain a formula, Comment generated formulas |
| Chinese (simplified) - China       | zh-Hans           | Explain a formula                             |
| Czech - Czech Republic             | cs-CZ             | Explain a formula                             |
| Danish - Denmark                   | da-DK             | Explain a formula                             |
| Dutch - Netherlands                | nl-NL             | Explain a formula                             |
| Finnish - Finland                  | fi-FI             | Explain a formula                             |
| French - France                    | fr-FR             | Explain a formula                             |
| German - Germany                   | de-DE             | Explain a formula                             |
| Greek - Greece                     | el-GR             | Explain a formula                             |
| Italian - Italy                    | it-IT             | Explain a formula                             |
| Japanese - Japan                   | ja-JP             | Explain a formula                             |
| Korean - Korea                     | ko-KR             | Explain a formula                             |
| Norwegian (Bokmål) - Norway        | nb-NO             | Explain a formula                             |
| Polish - Poland                    | pl-PL             | Explain a formula                             |
| Portuguese - Brazil                | pt-BR             | Explain a formula                             |
| Russian - Russia                   | ru-RU             | Explain a formula                             |
| Spanish (Traditional Sort) - Spain | es-ES             | Explain a formula                             |
| Swedish - Sweden                   | sv-SE             | Explain a formula                             |
| Thai - Thailand                    | th-TH             | Explain a formula                             |
| Turkish - Türkiye                  | tr-TR             | Explain a formula                             |
