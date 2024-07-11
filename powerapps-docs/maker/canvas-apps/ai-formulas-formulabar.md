---
title: Create and edit formulas with Copilot
description: How to interact with formulas in the formula bar using AI.
author: warrenbryant-msft
ms.topic: conceptual
ms.custom: canvas
ms.reviewer: mkaur
ms.date: 7/15/2024
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
    1. Open your [canvas app open for editing](edit-app.md) in Power Apps Studio:
    1. On the command bar, select **Settings** > **Upcoming features**.
    1. From the **Preview** tab, set the toggle for **Power Fx formula bar** to **On**.

- Copilot must be enabled for your environment and tenant. For more information, see [Enable or disable Copilot (preview) in Power Apps](ai-overview.md#enable-or-disable-copilot-preview-in-power-apps).
- Your browser and Power Apps language settings must be set to **English (United States)**.
To use this feature, Power Fx formula bar must be turned on in app settings.
> [!NOTE]
> AI generated content may be inaccurate and should be checked for accuracy.


## Explain a formula

Use Copilot in the formula bar to understand what a formula is doing.

1. Select a control and its corresponding property.
1. On the formula bar, select the **Copilot functionality menu** > **Explain This Formula**.
:::image type="content" source="media/copilot/ufb-explain-copilot.png" alt-text="Explain this formula":::

    When Copilot provides an explanation of the formula, you can copy and insert it as a code comment or share it with other makers who are working on the same app.
:::image type="content" source="media/copilot/ufb-explanation-copilot.png" alt-text="Formula explanation":::

### Language Support

The following table lists the languages available for the Explain a formula feature, which is based on the settings in your Power Platform environment and browser.

| **Name**                           | **Language Code** | 
|------------------------------------|-------------------|
| English                            | en-US             |
| Chinese (simplified) - China       | zh-Hans           | 
| Czech - Czech Republic             | cs-CZ             |
| Danish - Denmark                   | da-DK             |
| Dutch - Netherlands                | nl-NL             |
| Finnish - Finland                  | fi-FI             |
| French - France                    | fr-FR             | 
| German - Germany                   | de-DE             | 
| Greek - Greece                     | el-GR             |
| Italian - Italy                    | it-IT             |
| Japanese - Japan                   | ja-JP             |
| Korean - Korea                     | ko-KR             |
| Norwegian (Bokmål) - Norway        | nb-NO             |
| Polish - Poland                    | pl-PL             |
| Portuguese - Brazil                | pt-BR             |
| Russian - Russia                   | ru-RU             |
| Spanish (Traditional Sort) - Spain | es-ES             |
| Swedish - Sweden                   | sv-SE             |
| Thai - Thailand                    | th-TH             |
| Turkish - Türkiye                  | tr-TR             |


### Known Limitations
- There's a 5,000 character limit for formula explanations.
- Copilot in Power Apps is only aware of default properties.
- User defined functions aren't supported.

## Copilot comment generated formulas (preview)

[This section is prerelease documentation and is subject to change.]

Add a comment in the formula bar and Copilot will suggest a suitable formula. You can accept the suggestion or typing through it. The comments can remain in the formula bar as documentation, similar to regular code comments.


> [!IMPORTANT]
> - Preview features aren’t meant for production use and may have restricted functionality. These features are available before an official release so that customers can get early access and provide feedback. For more information, see [Power Apps preview program](../powerapps-preview-program.md).
> - This capability is in the process of rolling out, and may not be available in your region yet.

1. With your canvas app open for editing, type a code comment using **//** or **/*** in the formula bar.
:::image type="content" source="media/copilot/ufb-comment-copilot.png" alt-text="Typed comment":::

    Wait few seconds for Copilot to generate a formula recommendation.

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
- While Copilot is generating formula suggestions, other activities in the Power Apps Studio might be temporarily unavailable.
- Existing formulas for that property aren't included in the recommendation.
- User defined functions aren't supported.
- This feature isn't available in the Canada region.

### Disable Copilot comment generated formulas

 Copilot comment generated formulas can be disabled from app settings.

- Go to **Settings** > **Upcoming features**. Set the toggle to **Off** for **Copilot comment-generated formulas**.

> [!NOTE]
> You won't be able to disable **Copilot comment generated formulas** when it's generally available.

## Responsible AI

Review the Microsoft Documentation on [FAQ about using AI responsibly in Power Apps](../common/responsible-ai-overview.md) to understand the choices a user has when working with AI. Additionally, review the [Power Fx Copilot FAQ](../common/faqs-copilot-powerfx.md) for questions regarding this functionality specifically.
