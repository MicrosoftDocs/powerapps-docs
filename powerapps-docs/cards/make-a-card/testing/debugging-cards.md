---
title: Test and debug cards (Preview)
description: Learn how to test and debug your cards using the Play page
ms.date: 09/20/2022
ms.topic: article
author: iaanw
ms.author: iawilt
manager: shellyha
ms.reviewer: 
ms.custom: 
ms.collection: 
---

# Test and debug cards (Preview)

[!INCLUDE[cards_preview_notice](../../includes/preview-include.md)]

Use the **Play** page to see how finished cards will look and act before sending them out to users. It has the tools to test your card and debug any issues.

> [!NOTE]
> Card instances and their data, which you see on the Play page, will only last 48 hours after being created. Select the **Play** button from the Card Designer to get a new instance of that card.

## Prerequisites

- A [Power Apps](https://powerapps.microsoft.com/) account.
- A card to test. For an example, see the [simple card tutorial](../../tutorials/hello-world-card.md).
- Familiarity with the [Card Designer](../designer-overview.md).

## Access the Play page

To access the Play page:

1. Go to [Power Apps](https://make.test.powerapps.com/) and select **Cards (preview)**.
1. On the left select **Cards** to see all of your cards. Select the card you want to test and debug.
1. Select the **Play** button at the top of the page. A new window will appear with the Play page.

   :::image type="content" source="../../media/debugging-cards/play-button-in-designer.png" alt-text="Screenshot of the Play button in the Card Designer":::

## Play page components

The Play page is made up of the following components:

   :::image type="content" source="../../media/debugging-cards/play-page-elements.png" alt-text="Screenshot of the Play page elements":::

1. Card title - The title of the card
1. View mode - Switch between light and dark modes to see how cards looks in different environments.
1. Card viewer - Interact with and view the card.
1. Send button - Send the card in Teams with a link.
1. Debug pane - Displays important debugging information while testing. For more information, see the [debugging](#debug-your-card) section.

## Test your card

Now that you're on the Play page and understand the different elements of it, you can test your card. The example used in this section is from the [simple card tutorial](../../tutorials/hello-world-card.md).

Try interacting with your card. In the example below, the **Say Hello** button is used to fill a variable with the user's text input. Notice how the bot's title changes to the user input.

Before interacting with the card:

:::image type="content" source="../../media/debugging-cards/card-before-interaction.png" alt-text="Screenshot of the card before interacting with it":::

After interacting with the card:

:::image type="content" source="../../media/debugging-cards/card-after-interaction.png" alt-text="Screenshot of the card after interacting with it":::

You can also change the **View** button on the Play page to switch between light and dark modes. The example below is the same card in dark mode:

:::image type="content" source="../../media/debugging-cards/dark-mode-card.png" alt-text="Screenshot of the card in dark mode":::

If you encounter issues while testing your card, use the [Debug](#debug-your-card) panel to try and fix them.

## Debug your card

The **Debug** panel lets you ascertain issues with your card and gives suggestions when possible for fixes.

To open the **Debug** panel, select the **Debug** button on the right. There are four elements to the debug panel: **Memory**, **JSON**, **Output**, and **Info**.

### Memory

The **Memory** section lets you see variables stored in memory and how your card is assigning and using them.

The example below shows that the user input stored in `UserAnswer` has the same value as the assigned variable `UserName` used in the card.

:::image type="content" source="../../media/debugging-cards/memory-example.png" alt-text="Screenshot of the Memory section in the Debug panel":::

If you're encountering issues with memory, check your variable names and any related Power Fx formulas used in your card.

### JSON

The **JSON** section lets you see the JSON representation of your card. This can be helpful for developers working on cards who prefer a code-first approach.

### Output

The **Output** sections lets you see any output from your card. This is only available for cards where output is set up already.

### Info

The **Info** section lets you see information about the card's **Environment ID**, **Card ID**, and **User**.
