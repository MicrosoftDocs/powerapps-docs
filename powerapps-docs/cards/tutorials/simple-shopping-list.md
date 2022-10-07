---
title: Create a shopping list card (preview)
description: Learn about card basics while creating a simple shopping list card.
ms.date: 09/20/2022
ms.topic: article
author: iaanw
ms.author: iawilt
manager: shellyha
ms.reviewer: 
ms.custom: 
ms.collection: 
---

# Create a shopping list card (preview)

[!INCLUDE[cards_preview_notice](../includes/preview-include.md)]

This tutorial shows you how to build a simple card that displays a shopping list and lets you add new items. At the end of this tutorial, your shopping list card will look like the example below:

:::image type="content" source="../media/tutorial-simple-shopping-list/shopping-list-card.png" alt-text="Screenshot of a finished simple shopping list card." border="true":::

## Prerequisites

- A [Power Apps](https://powerapps.microsoft.com/) account.
- Familiarity with the [Card Designer](../make-a-card/designer-overview.md), [variables](../make-a-card/variables/variables.md), and [Power Fx](../make-a-card/power-fx/intro-to-pfx.md).

## Create a card

1. Go to [Power Apps](https://make.powerapps.com) and select **Cards (preview)** on the left.

1. Select **+ Create a card**.

1. Enter "SimpleShoppingCard" under **Card name** and then select **Create**. The default card will appear, shown below.

   :::image type="content" source="../media/tutorial-simple-shopping-list/default-blank-card.png" alt-text="Screenshot of a blank card." border="true":::

1. Select the top **Text label** and enter `Shopping List`. Then select the **Text label** and enter `Use the field below to add items to the list.`.

## Add a new variable

The shopping list will hold several individual lines of text, so you'll need to create a variable to hold these.

1. Select **Variables** then **New variable** to create a new variable.

1. The **New variable** box will appear. Under name **Name** enter "myGroceryList".

1. Set the variable **Type** to *Table*. Keep the **Value Persistance** set to **Temporary**.

   :::image type="content" source="../media/tutorial-simple-shopping-list/setup-grocery-array-var.png" alt-text="Screenshot of the my grocery list variable setup." border="true":::

1. Select **Save** to create the `MyGroceryList` table variable.

1. You should now see that your variable list contains one variable whose name is `MyGroceryList` and type is *Table*.

   :::image type="content" source="../media/tutorial-simple-shopping-list/my-grocery-list-array-var.png" alt-text="Screenshot of the fully set up my grocery list array variable." border="true":::

## Add and configure the list

Now that you have a table variable for your list, you need to add it to the card and configure it.

1. Select **Insert** from the menu. Select **Display** then **Text label**.

   :::image type="content" source="../media/tutorial-simple-shopping-list/add-text-label.png" alt-text="Screenshot of where to find the Text label in the Insert>Display menu." border="true":::

    A **Text label** will appear on the card underneath the Text labels you edited previously.

1. With the empty Text label still selected, select the **Advanced** tab on the right. Select the **Repeat for every** field and enter `MyGroceryList`.

   :::image type="content" source="../media/tutorial-simple-shopping-list/advanced-pane-setup.png" alt-text="Screenshot of how to setup Advanced pane" border="true":::

   This will repeat the Text label for every element in a given table. In this example, the table you're providing - `myGroceryList` - is the variable you created previously. This means that for every element in the grocery list, a separate text label is created in the card.

1. Switch back to the **Properties** tab. In the **Text** field, enter `ThisItem`.

   Assigning the `ThisItem` variable to the text label lets you view and display the current element of the `myGroceryList` array in the visible text of the Text label.

## Add the input field and button

The list you've created is currently empty, so the final step is to give the card the ability to add items to the list.

1. Select **Insert** from the menu. Then select **Input** then **Text input**. A text input box will appear on the screen.

1. Select the **Text input** control to display its properties.

   - Set **Name** to `TheNewItem`.
   - Set **Label** to `New Item:`.

   :::image type="content" source="../media/tutorial-simple-shopping-list/added-input-text-names.png" alt-text="Screenshot of added variable names to an input text box." border="true":::

   > [!NOTE]
   > The **Name** property lets you refer to the field from Power Fx and has to be one word. The **Label** property is displayed above the field; you can see it on the card to the left. These don't have to be similar as they are here (i.e. *TheNewItem* and "New Item:"), but it makes it easier to keep track of things.

1. Select **Insert** then **Input** then **Button** to add a button to the card.

   :::image type="content" source="../media/tutorial-simple-shopping-list/add-a-button.png" alt-text="Screenshot of adding a button to the card." border="true":::

1. Select the button to see its properties. Set its **Title** to `Add a new item`.

    > [!TIP]
    > The **Type** property is set to **Run Power Fx**. Buttons can be used for other kinds of actions, but using a Power Fx expression is the most common.

1. Select **Save**.

### Add the Power Fx expression

1. With the button selected, add in the following line of code into the Power Fx editor at the top: `Collect(myGroceryList, theNewItem)`

This PowerFX expression will append the contents of the `theNewItem` field to the `myGroceryList` table.

   | Variable          | Function in Power Fx                                                             |
   | ----------------- | -------------------------------------------------------------------------------------- |
   | `Collect`         | A built-in function that takes a table and an item and adds the item to the table. |
   | `MyGroceryList`   | The first variable you created; an initially empty table.                              |
   | `TheNewItem`      | The text input field above the button.                                                 |

## Test the card

1. Save all of your changes by selecting **Save** at the top. Always save your changes before testing your card.

1. Select the **Play** button in the upper right corner. This will launch your card in a new web page.

    :::image type="content" source="../media/tutorial-simple-shopping-list/play-button-in-cards.png" alt-text="Screenshot showing where the play button is." border="true":::

## Next Steps

Learn how to make a more complex card with the [Dataverse](dataverse-card.md).

