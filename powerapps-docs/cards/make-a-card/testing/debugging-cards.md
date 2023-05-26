---
title: Test and debug cards
description: Learn how to test and debug your cards for Microsoft Power Apps.
ms.date: 09/20/2022
ms.topic: how-to
author: iaanw
ms.author: iawilt
ms.reviewer: 
ms.custom: 
ms.collection: 
---

# Test and debug cards

Use the **Play** page to preview your cards before sending them out to users. The **Play** page has tools to test your card and help you debug any issues. Get to the **Play** page in the [card designer](../designer-overview.md).

Card instances that you preview in the **Play** page expire 48 hours after you create the preview. After 48 hours, select **Play** in the card designer to create a fresh instance of the card.

## Prerequisites

- A [Power Apps](https://powerapps.microsoft.com/) account
- [A card](../../tutorials/hello-world-card.md)

## Preview a card in the Play page

1. Sign in to [Power Apps](https://powerapps.microsoft.com/). Select **Cards**, and then select a card. If the **Cards** tab is not visible, select **More** and pin the **Cards** tab.
1. Select **Play** at the top of the card designer window. The **Play** page opens in a new browser tab.

   :::image type="content" source="../../media/debugging-cards/play-button-in-designer.png" alt-text="Screenshot of the Play button in the card designer.":::

The **Play** page is made up of the following components:

   :::image type="content" source="../../media/debugging-cards/play-page-elements.png" alt-text="Screenshot of the Play page in the card designer with components called out.":::

Legend:

1. The card title
1. Preview the card in light or dark mode
1. View and interact with the card
1. Send a link to the card to Microsoft Teams
1. [Open debugging information and tools](#debug-your-card)

## Test your card

The example used in this section is from the [simple card tutorial](../../tutorials/hello-world-card.md).

Test your card by interacting with all the controls in it. In the example below, the **Say Hello** button stores the user's text input in a variable, and then uses the value of the variable in the card title. If you're testing this card, you'll enter your name and select **Say Hello**, and then make sure the card title changes to reflect your input.

Before you interact with the card, its title is **Hello No Name**:

:::image type="content" source="../../media/debugging-cards/card-before-interaction.png" alt-text="Screenshot of a card before interacting with it.":::

After you interact with the card, the card title changes to **Hello \<whatever you entered\>**:

:::image type="content" source="../../media/debugging-cards/card-after-interaction.png" alt-text="Screenshot of the card after interacting with it.":::

You should also change the **View** from light to dark mode and make sure the card looks good in both.

:::image type="content" source="../../media/debugging-cards/dark-mode-card.png" alt-text="Screenshot of the card in dark mode.":::

## Debug your card

If you encounter issues while testing your card, open the debug pane to troubleshoot and get suggestions for fixing them.

There are four tabs in the debug pane: **Memory**, **JSON**, **Output**, and **Info**.

### Memory

The **Memory** tab displays the variables that the card has stored and how your card is assigning and using them. If you're encountering issues with memory, check your variable names and any related Power Fx formulas that are used in your card.

The example below shows that the user input that's stored in `UserAnswer` has the same value as the variable `UserName`, and that both are used in the **main** screen.

:::image type="content" source="../../media/debugging-cards/memory-example.png" alt-text="Screenshot of the Memory tab in the debug pane.":::

### JSON

The **JSON** tab displays the JSON representation of your card. A direct view of the card's underlying code can be helpful for developers who prefer a code-first approach.

### Output

The **Output** tab displays any output from your card. This tab is available only when a card has output elements.

### Info

The **Info** tab displays the card's **Environment ID**, **Card ID**, and **User**.
