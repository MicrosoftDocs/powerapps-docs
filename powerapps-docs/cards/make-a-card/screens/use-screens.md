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

Cards can have multiple screens that see with a **Show Screen** button or navigate between formulas. Screens can be used to show a different user interface for specific scenarios. For example, a polling card might have a screen to collect user responses and a screen to show the current aggregated poll results.

## Tree view

You can view the screens in your card and change properties of each screen using the tree view in the Card Designer.

   :::image type="content" source="../../media/make-a-card/cards-tree-view.png" alt-text="Screenshot of tree view in Card Designer." border="false":::

## Make a new screen

1. Open the **Tree View** for your card and select **+ New screen**.
1. Enter a name for your new screen and select **Create** to make it.
1. Add any controls, data, and variables you want to this screen. After you've added everything you wanted, you can use buttons to call your screen from a card.

## Use buttons with Show Screen

To show screens from other cards, use the **Show Screen** button.

1. Select **Insert** from the left. Then select **Input**>**Button** to create a new button.
1. Go to **Type** in the Properties pane on the right. Select the drop-down and change the **Type** to **Show Screen**.
1. **ShowCard** will appear on the right. Select the **Screen** you want to show and the **Name** of your button.

   :::image type="content" source="../../media/make-a-card/show-card-properties.png" alt-text="Screenshot of ShowCard options." border="false":::

    In the example above this button will show the `NameScreen` on a button that has the text "Say Goodbye".

    Now when you test your card the screen will appear after selecting the button. The example below shows how the screen appears after adding the button above to the [simple card tutorial](../../tutorials/hello-world-card.md) card.

   :::image type="content" source="../../media/make-a-card/screen-example.png" alt-text="Screenshot of an example screen in a card." border="false":::

Repeat this process as many times as needed to create more screens.
