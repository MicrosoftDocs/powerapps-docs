---
title: "Simple shopping list"
description: "Create a simple shopping list card, learning about the basics of creating a card"
keywords: "Power Cards, Power Cards Designer, Power Apps, Cards, tutorial"
ms.date: 03/18/2022
ms.topic: article
author: eberhardts
ms.author: v-eberhardts
manager: shellyha
ms.reviewer: 
ms.custom: 
ms.collection: 
---

# Simple Shopping List

This tutorial will show you how to build a simple card that displays a shopping list and lets you add new items. You'll learn about:

- Variables
- Calling PowerFX from a button
- Repeating UI elements
- Reading data from input fields
- A basic tour of the user interface

The result will look like the example below:

:::image type="content" source="../../media/tutorial-simple-shopping-list/shopping-list-card.png" alt-text="Screenshot of a finished simple shopping list card." border="false":::

This tutorial will only let you add items in this card. For a more complex shopping list tutorial, see [Compound Shopping List](compound-shopping-list.md).

## Create a card and give it a name

1. Create your card as described in the [Setup instructions](../../get-started-designer/setup-designer.md). You'll be asked for a name for your card – use something you'll remember later when you go looking for it, like "shopping list tutorial".

   :::image type="content" source="../../media/tutorial-simple-shopping-list/create-card.png" alt-text="Screenshot of where to go to create a card." border="false":::

2. You'll see the default "empty" card:

   :::image type="content" source="../../media/tutorial-simple-shopping-list/default-blank-card.png" alt-text="Screenshot of a blank card." border="false":::

3. Select the first heading and enter "Shopping List".

4. Select the second heading and enter "Use the field below to add items to the list".

5. Save your card. Cards don't autosave, so it's good to save as you go.

## Create a variable to hold your list

This shopping list will hold several individual lines of text (or strings), so you'll need to create a variable to hold these strings.

1. Select Variables from the Navigation bar

   :::image type="content" source="../../media/tutorial-simple-shopping-list/go-to-variables.png" alt-text="Screenshot of the variables location in Cards." border="false":::

1. Select the New variable button. This will open the variable editor.

   :::image type="content" source="../../media/tutorial-simple-shopping-list/add-new-variable.png" alt-text="Screenshot of how to add a new variable." border="false":::

1. Give your variable a name. In this example, we use `my_grocery_list`.

1. Set the type of variable to **array**. This will be an array of strings.

   :::image type="content" source="../../media/tutorial-simple-shopping-list/setup-grocery-array-var.png" alt-text="Screenshot of the my grocery list variable setup." border="false":::

1. Save the card.

1. Now you should see that your variable list contains one variable whose name is `my_grocery_list` and type is array.

   :::image type="content" source="../../media/tutorial-simple-shopping-list/my-grocery-list-array-var.png" alt-text="Screenshot of the fully set up my grocery list array variable." border="false":::

1. Save the card.

## Add and configure the list

Time to build the card UI.

1. Open the Tool Panel

   :::image type="content" source="../../media/tutorial-simple-shopping-list/find-tool-panel.png" alt-text="Screenshot of where to find the cards tool panel." border="false":::

1. First, add the list. Drag and drop a Text Block from the Elements pane onto the card underneath the text blocks you previously added. The Text Block will snap into place, so you don't have to be precise with positioning.

   :::image type="content" source="../../media/tutorial-simple-shopping-list/add-text-block-to-card.png" alt-text="Screenshot of another text block added to the card." border="false":::

1. With the empty Text Block still selected, go to the Advanced tab in the Property pane

   :::image type="content" source="../../media/tutorial-simple-shopping-list/go-to-advanced-pane.png" alt-text="Screenshot of how to find the advanced properties for the selected text block." border="false":::

1. Select the "Repeat for every" field and enter `= my_grocery_list`.

   This will repeat the TextBlock for every element in a given array. In this example, the array you're providing&mdash;`my_grocery_list`&mdash;is the variable you created previously. This means that for every element in the grocery list, a separate text block is created in the card.

   :::image type="content" source="../../media/tutorial-simple-shopping-list/add-array-to-advanced.png" alt-text="Screenshot showing how to add the my grocery list variable to the advanced pane under repeat for every." border="false":::

1. Select Properties (visible in the picture above for reference)

1. In the "Text" field of the Properties tab, enter `=$data`.

   Assigning the `$data` variable to the text block lets you view and display the current element of the `my_grocery_list` array in the visible text of the Text Block.

   :::image type="content" source="../../media/tutorial-simple-shopping-list/add-data-var-to-text-block.png" alt-text="Screenshot showing how to add the data variable to the text field in the properties tab." border="false":::

1. Save the card. Now you're done creating the list.

## Add the input field and button

The list you've created is currently empty, so the final step is to give the card the ability to add items to the list.

1. Add an Input.Text onto the card underneath all of the previously created text boxes.

1. Select the Input.Text and go to its Properties to update the following properties:

   - **Name:** the_new_item (this has an automatically assigned value of *inputText1*, but you'll want to give it a more meaningful name to reuse in a PowerFx script later.)
   - **Label:** New Item:

   Result:

   :::image type="content" source="../../media/tutorial-simple-shopping-list/added-input-text-names.png" alt-text="Screenshot of added variable names to an input text box." border="false":::

   > [!NOTE]
   > The Name property lets you refer to the field from PowerFX – it needs to be one word. The Label property is displayed above the field – you can see it on the card to the left. These don't have to be similar as they are here (i.e., *the_new_item* and "New Item:"), but it makes it easier to keep track of things.

1. Add a button to the card. Drop it anywhere below the New Item field.

   :::image type="content" source="../../media/tutorial-simple-shopping-list/add-a-button.png" alt-text="Screenshot of adding a button to the card." border="false":::

1. In the Button Properties, set the Title property to "Add the New Item". Note that the Type property is "Run PowerFx"&mdash;buttons can be used for other kinds of actions, but using a PowerFX expression is the most common.

   :::image type="content" source="../../media/tutorial-simple-shopping-list/run-pfx-in-button.png" alt-text="Screenshot showing the button type." border="false":::

1. Click **Save**.

## One line of PowerFX to tie it all together

1. With the button selected, add in the following line of code into the PowerFX editor: `AppendItem(my_grocery_list, the_new_item)`

   This PowerFX expression reads the text from the input field and adds it to the array variable.

   | Variable | Function in PowerFX script |
   | - | - |
   | `AppendItem` | A built-in function that takes an array and an item and appends the item to the array. |
   | `my_grocery_list` | The first variable you created; an initially empty array |
   | `the_new_item` | The text input field above the button |

1. Save the card.

## Test the card

Save first (always save before testing) and then select the Play button in the upper right corner. This will launch your card in a new web page.

:::image type="content" source="../../media/tutorial-simple-shopping-list/play-button-in-cards.png" alt-text="Screenshot showing where the play button is." border="false":::

### Bonus things to try

- Try making the items on the shopping list have a different color than the rest of the text.
- Use a PowerFX expression to add "please" to every item on the shopping list
- Advanced: make it so every item in the shopping list has two text blocks instead of one. For more information on this, see the [Compound List tutorial](compound-shopping-list.md).
