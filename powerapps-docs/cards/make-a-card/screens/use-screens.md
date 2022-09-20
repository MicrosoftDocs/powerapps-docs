---
title: Add screens to a card (Preview)
description: Learn how to add screens to your Microsoft Power Apps cards.
ms.date: 09/20/2022
ms.topic: how-to
author: iaanw
ms.author: iawilt
manager: shellyha
ms.reviewer: 
ms.custom: 
ms.collection: 
---

# Add screens to a card (Preview)

[!INCLUDE[cards_preview_notice](../../includes/preview-include.md)]

Cards can have multiple screens, each presenting a different interface for a specific scenario or purpose. For example, a polling card might have a screen to collect user responses and a screen to show the current aggregated poll results. Use buttons to let users switch between screens or use Power Fx formulas for more complex scenarios. Insert, modify, and remove them in the [card designer](../designer-overview.md).

## Prerequisites

- A [Power Apps](https://powerapps.microsoft.com/) account
- [A card](../../tutorials/hello-world-card.md)

## Tree view

View the screens in your card and the elements you've added to them using the card designer tree view.

   :::image type="content" source="../../media/make-a-card/cards-tree-view.png" alt-text="Screenshot of the tree view in the card designer, showing a card named HelloWorldCard with two screens.":::

## Create a screen

1. Sign in to [Power Apps](https://powerapps.microsoft.com/). Select **Cards (preview)** > **Cards**, and then select a card.
1. In the left pane of the card designer, select **Tree View**.
1. Select **+ New screen**.
1. Enter a name for your screen and select **Create**. Spaces and special characters aren't allowed in screen names.
1. Add controls, data, and variables to the screen as needed.

## Use a Show Screen button to open a screen

1. In the left pane of the card designer, select **Insert**.
1. Select **Input** to expand the category, and then select **Button** to add a button to your card.
1. In the button properties pane, set **Type** to **Show Screen**.
1. Set **Screen** to the screen you want the button to show, and then set **Title** to the label to display on the button.

   :::image type="content" source="../../media/make-a-card/show-card-properties.png" alt-text="Screenshot of a Show Screen button properties pane in the card designer.":::

## Use a Power Fx expression to open a screen

The Power Fx [Back](/power-platform/power-fx/reference/function-navigate#back) and [Navigate](/power-platform/power-fx/reference/function-navigate#navigate) functions also switch between screens.

The Show Screen button opens a screen and nothing more. The Power Fx Back and Navigate functions can be used outside of buttons and are appropriate for more complex screen-switching scenarios.

For more information about Back and Navigate, see the [Power Fx reference documentation syntax](/power-platform/power-fx/reference/function-navigate#syntax), [examples](/power-platform/power-fx/reference/function-navigate#examples), and [step-by-step instructions](/power-platform/power-fx/reference/function-navigate#step-by-step).
