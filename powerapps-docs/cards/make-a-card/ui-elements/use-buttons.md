---
title: Add buttons
description: Learn how to build a card with buttons.
ms.date: 09/20/2022
ms.topic: article
author: iaanw
ms.author: iawilt
manager: shellyha
ms.reviewer: 
ms.custom: 
ms.collection: 
---

# Add buttons

Buttons are a type of control that let users perform actions in cards. They're a visual interface that makes it easy for users to do things with cards without entering any input aside from a click.

Buttons can do one of four things:

1. Run Power Fx - when selected, the button will run a [Power Fx formula](../power-fx/intro-to-pfx.md)
1. Show Screen - when selected, the button will go to the specified screen
1. Open Url - when selected, the button will launch the given url in an external or embedded web browser
1. Toggle Visibility - when selected, the button will show or hide other controls in the card

## Prerequisites

- A [Power Apps](https://powerapps.microsoft.com/) account.
- A card. For an example, see the [simple card tutorial](../../tutorials/hello-world-card.md).
- Familiarity with the [Card Designer](../../make-a-card/designer-overview.md).

## Add a button to a card

1. Go to [Power Apps](https://powerapps.microsoft.com/). Select **Cards (Preview)** and then the card you want add a button to.
1. Select **+ Insert** on the left. Then select **Button** to add a button to your card.

    :::image type="content" source="../../media/use-buttons/add-button.png" alt-text="Screenshot of Button in Insert menu":::
1. Now that the button is on your card, you can edit its properties. At a minimum, choose a button **Type** and add a button **Title** to display on the card, as shown below.

    :::image type="content" source="../../media/use-buttons/button-title.png" alt-text="Screenshot of Button in Insert menu":::

### Button type

There are four types of buttons you can add to your card:

- Run PowerFx
- Show Screen
- Open Url
- Toggle Visibility

#### Run PowerFX

The **Run PowerFX** button type lets you use buttons to run Power Fx formulas. These formulas can be simple or complex, and when combined with buttons make it easy for users to navigate card logic.

Set the **Type** to **Run PowerFX**. Then select the **Power Fx** link to add a formula to the Formula bar.

When you test the button, the actions expressed by the Power Fx formula should happen.

#### Show Screen

The **Show Screen** button lets users select a button and then display a screen. For more information about screens, see the [screens](../screens/use-screens.md) article.

Set the **Type** to **Show Screen** and then select a **Screen** to switch to. If you don't have any screens, only *main** will appear in the list. When the user selects the button, the new screen will appear under the card.

#### Open Url

The **Open Url** button lets users select a button that opens a URL.

Set the **Type** to **Open Url** and then enter a **Url**. When the user selects the button, the URL entered previously will open.

#### Toggle Visibility

The **Toggle Visibility** button shows or hides other controls in the card.

Set the **Type** to **Toggle Visibility**. Then select the **Target Elements** pane and select **+ Add new**. Enter the **ElementID** and toggle the **Visibility** property to make the element visible or invisible. Add as many elements as you want to toggle the visibility of.

