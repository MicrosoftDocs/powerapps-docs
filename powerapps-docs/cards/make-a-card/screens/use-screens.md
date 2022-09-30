---
title: Use screens (Preview)
description: Learn how to build with screens.
ms.date: 09/20/2022
ms.topic: article
author: iaanw
ms.author: iawilt
manager: shellyha
ms.reviewer: 
ms.custom: 
ms.collection: 
---

# Use screens (Preview)

[!INCLUDE[cards_preview_notice](../../includes/preview-include.md)]

Cards can have multiple screens. Each screen can show a different user interface for specific scenarios. For example, a polling card might have a screen to collect user responses and a screen to show the current aggregated poll results. Use buttons to let users switch between screens or use Power Fx formulas for more complex scenarios.

## Tree view

You can view the screens in your card and change properties of each screen using the tree view in the Card Designer.

   :::image type="content" source="../../media/make-a-card/cards-tree-view.png" alt-text="Screenshot of tree view in Card Designer." border="true":::

## Make a new screen

1. Open the **Tree View** for your card and select **+ New screen**.
1. Enter a name for your new screen and select **Create** to make it.
1. Add any controls, data, and variables you want to this screen. After you've added everything you wanted, you can use buttons to call your screen from a card.

## Use a button to show a screen

To show screens from other cards, use the **Show Screen** button.

1. Select **Insert** from the left. Then select **Input** then **Button** to create a new button.
1. Go to **Type** in the Properties pane on the right. Select the drop-down and change the **Type** to **Show Screen**.
1. **ShowCard** will appear on the right. Set **Screen** to the screen you want to show and set **Title** to the text to display on your button.

   :::image type="content" source="../../media/make-a-card/show-card-properties.png" alt-text="Screenshot of ShowCard options." border="true":::

    In the example above, this button will show the `NameScreen` screen when a user selects the button titled "Say Goodbye".

    Now, the screen will appear when you test your card and select the button. The example below shows how the screen appears after adding an example button to the [simple card tutorial](../../tutorials/hello-world-card.md) card.

   :::image type="content" source="../../media/make-a-card/screen-example.png" alt-text="Screenshot of an example screen in a card." border="true":::

Repeat this process as many times as needed to create more screens.

## Switch screens with Power Fx formulas

The Power Fx [Back](/power-platform/power-fx/reference/function-navigate#back) and [Navigate](/power-platform/power-fx/reference/function-navigate#navigate) functions let you switch between screens. While **ShowScreen** just shows a screen, these functions can be used outside of buttons and are appropriate for more complex screen-switching scenarios.

For more information about Back and Navigate, see the Power Fx reference documentation [syntax](/power-platform/power-fx/reference/function-navigate#syntax), [examples](/power-platform/power-fx/reference/function-navigate#examples), and [step-by-step instructions](/power-platform/power-fx/reference/function-navigate#step-by-step).
