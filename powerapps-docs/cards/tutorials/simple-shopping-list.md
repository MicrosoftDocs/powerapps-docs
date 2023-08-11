---
title: Create a shopping list card
description: Learn about the basic elements of a card by creating a shopping list card.
ms.date: 09/20/2022
ms.topic: how-to
author: iaanw
ms.author: iawilt
ms.reviewer: 
ms.custom: 
ms.collection: 
---

# Create a shopping list card

In this tutorial, you'll create a card that displays a shopping list and lets you add items. You'll use the [card designer](../make-a-card/designer-overview.md), [variables](../make-a-card/variables/variables.md), and [Power Fx](../make-a-card/power-fx/intro-to-pfx.md).

At the end of the tutorial, your shopping list card should look like the following example:

:::image type="content" source="../media/tutorial-simple-shopping-list/shopping-list-card.png" alt-text="Screenshot of a finished shopping list card.":::

## Prerequisites

- A [Power Apps](https://powerapps.microsoft.com/) account

## Create a card

1. Sign in to [Power Apps](https://make.powerapps.com) and select your environment.

1. In the left pane, select **Cards**. [!INCLUDE [left-navigation-pane](../../includes/left-navigation-pane.md)]

1. Select **+ Create a card**.

1. Under **Card name**, type *SimpleShoppingCard*, and then select **Create**.

1. Select the text **Your card title goes here**. In the text label properties pane, set **Text** to *Shopping List*.

1. Select the text **Add and remove element to customize your new card.** In the text label properties pane, set **Text** to *Use the box below to add items to the list*.

## Add a variable

The shopping list will hold individual items in separate lines of text. It looks like a table with a single column, with one grocery item in each row. That suggests you'll need to create a table variable to store your list.

1. In the left pane, select **Variables**.
1. Select **+ New variable**.
1. In the **New variable** window, enter *MyGroceryList* under **Name**. Set **Type** to **Table**.
1. Select the curly brackets to the right of **Default value** and enter *""* between the brackets. This indicates that our table holds text values in a column implicitly called **Value**
1. Select **Save**.

   :::image type="content" source="../media/tutorial-simple-shopping-list/setup-grocery-array-var.png" alt-text="Screenshot of the MyGroceryList variable properties pane.":::

## Add a list to the card

1. In the left pane, select **Insert**.
1. In the tool pane, select **Display** to expand the category, and then select **Text label**.
1. In the text label properties pane, select the **Advanced** tab.
1. Set **Repeat for every** to *MyGroceryList*.

   :::image type="content" source="../media/tutorial-simple-shopping-list/advanced-pane-setup.png" alt-text="Screenshot of a text label's advanced properties pane, with MyGroceryList in the Repeat for every property.":::

   Setting a text label's **Repeat for every** property repeats the text label for every item in the specified table. In this example, the table, `MyGroceryList`, is the variable you created. In other words, a separate text label is created in the card for every item in the grocery list.

1. Select the **Properties** tab. Set **Text** to *ThisItem.Value*.

   Assigning the system-defined variable `ThisItem.Value` to the text label displays the value of the current item in the `MyGroceryList` array as the label text. *Array* is another term for a table variable. You can enter the variable name in the formula bar or the properties pane.

    :::image type="content" source="../media/tutorial-simple-shopping-list/set-thisitem-value.png" alt-text="Screenshot of a variable name entered in the text label's Text property.":::

## Add an input box

The list you created is empty, so in the final step, you'll give the user the ability to add items.

1. In the left pane, select **Insert**.
1. In the tool pane, select **Input** to expand the category, and then select **Text input**.
1. In the text input properties pane, set **Name** to *NewItem* and set **Label** to *New Item:*.

   :::image type="content" source="../media/tutorial-simple-shopping-list/added-input-text-names.png" alt-text="Screenshot of variable names entered in the Name and Label properties of an input text box.":::

   The **Name** property lets you refer to the control in a Power Fx expression. It has to be one word, with no spaces or special characters. The **Label** property is displayed in the card. The name and label of a control don't have to be similar, as they are here, but using similar names makes it easier to keep track of controls.

### Add a Power Fx button

1. In the left pane, select **Insert**.
1. In the tool pane, select **Input** to expand the category, and then select **Button**.
1. In the button properties pane, set **Title** to *Add Item*.
1. In the properties pane, select **PowerFx** to place your cursor in the formula bar.
1. Type the following Power Fx expression in the formula bar: *Collect(MyGroceryList, {Value: NewItem})*

    This expression uses the Power Fx function **Collect** to append the value of the user's input, `NewItem`, to the `MyGroceryList` table variable in the implicit **Value** column. Since the expression is bound to the button's **OnSelect** property, it runs when the user selects the button.

    :::image type="content" source="../media/tutorial-simple-shopping-list/pfx-in-button.png" alt-text="Screenshot of the Power Fx expression in the formula bar, assigned to the button's OnSelect property.":::

## Test the card

You should always save your changes before you play a card. Select **Save**, and then select **Play**.

Test your card by adding a few items to the grocery list.

## Next steps

Learn how to make a more complex card with [Microsoft Dataverse connectors](dataverse-card.md).
