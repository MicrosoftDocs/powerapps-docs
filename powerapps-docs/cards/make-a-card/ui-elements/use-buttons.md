---
title: Add buttons to a card
description: Learn how to add interactive buttons to your cards for Microsoft Power Apps.
ms.date: 09/20/2022
ms.topic: how-to
author: iaanw
ms.author: iawilt
ms.reviewer: 
ms.custom: 
ms.collection: 
---

# Add buttons to a card

Buttons are a type of control that lets users perform actions in cards without entering any input aside from a click. Insert, modify, and remove them in the [card designer](../designer-overview.md).

Buttons can do one of four things:

- [Run a Power Fx expression](../power-fx/intro-to-pfx.md)
- Open a screen
- Open a URL in an external or embedded web browser
- Show or hide other controls in the card

## Prerequisites

- A [Power Apps](https://powerapps.microsoft.com/) account
- [A card](../../tutorials/hello-world-card.md)

## Insert a button

1. Sign in to [Power Apps](https://powerapps.microsoft.com/) and then select **Cards**. [!INCLUDE [left-navigation-pane](../../../includes/left-navigation-pane.md)]

1. In the left pane of the card designer, select **Insert**.

1. In the tool pane, select the **Input** category to expand it, and then select **Button** to add a button to your card.

1. In the properties pane, enter a **Title** to display as the button label. Edit the other properties as needed.

    :::image type="content" source="../../media/use-buttons/button-title.png" alt-text="Screenshot of a button's properties in the card designer, with the button title highlighted.":::

### Button types

You can add four types of buttons to your cards:

- Run PowerFx
- Show Screen
- Open Url
- Toggle Visibility

#### Run Power Fx

Use a **Run PowerFx** button to run Power Fx expressions. [Learn more about Power Fx](../power-fx/intro-to-pfx.md) and the [functions and formulas you can use in an expression](/powerapps/maker/canvas-apps/formula-reference).

Select the **Power Fx** link in the button properties pane to start entering an expression in the formula bar.

:::image type="content" source="../../media/use-buttons/button-powerfx.png" alt-text="Screenshot of a Run PowerFx button properties pane in the card designer.":::

#### Show Screen

Use a **Show Screen** button to display a specific screen beneath the current view. [Learn about screens in Power Apps](../screens/use-screens.md).

In the button properties pane, set the **Type** to **Show Screen**, and then select a **Screen** to open. If you don't have any screens yet, only **main** will appear in the list.

:::image type="content" source="../../media/use-buttons/button-screen.png" alt-text="Screenshot of a Show Screen button properties pane in the card designer.":::

#### Open Url

Use an **Open Url** button to open a web page.

In the button properties pane, set the **Type** to **Open Url** and then enter a **Url**.

:::image type="content" source="../../media/use-buttons/button-url.png" alt-text="Screenshot of an Open Url button properties pane in the card designer.":::

#### Toggle Visibility

Use a **Toggle Visibility** button to show or hide other controls in the card.

1. In the button properties pane, set the **Type** to **Toggle Visibility**.
1. Select the **Target Elements** tab, and then select **+ Add new**.
1. Enter the **ElementID** and toggle the **Visibility** property to make the element visible or invisible.

    :::image type="content" source="../../media/use-buttons/button-visibility.png" alt-text="Screenshot of a Toggle Visibility button properties pane in the card designer, with the Target Elements tab shown.":::

1. Continue to add elements as needed.
