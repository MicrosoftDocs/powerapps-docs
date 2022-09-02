---
title: "Compound Shopping List"
description: "Create a compound shopping list card, using more features of power cards"
keywords: "Card Designer, Power Apps, cards, tutorial"
ms.date: 09/20/2022
ms.topic: article
author: iaanw
ms.author: iawilt
manager: shellyha
ms.reviewer: 
ms.custom: 
ms.collection: 
---

# Compound List Item

When you see a list of items in a user interface, it's common for each item to be made up of several UI elements – for example a picture, a title, and a summary.

In this tutorial, you'll learn:

- How to make repeating UI elements
- How to make repeating UI elements that have multiple children (i.e. "compound")
- How to use columns to build a simple list item
- How to create a variable
- How to use fields
- How to use buttons
- How to tie it all together with a little Power Fx

The result will look like the example below:

:::image type="content" source="../media/tutorial-compound-shopping-list/compound-elements-card.png" alt-text="Screenshot of final complex shopping list card":::

Here, the list has Apple and Banana in it. In the UI, for each item in the list, you'll add two different items: a text item ("Apple") and also a checkbox ("Also Apple.")

## Create a card and give it a name

1. Create your card. You'll be asked to name your card - use something unique as you won't be able to create your card if there is an existing card with the same name.  

   :::image type="content" source="../media/tutorial-compound-shopping-list/create-card.png" alt-text="Screenshot of where to go to create a card." border="false":::

1. You'll see the default "empty" card.

   :::image type="content" source="../media/tutorial-compound-shopping-list/default-blank-card.png" alt-text="Screenshot of a blank card." border="false":::

## Create a variable to hold your list

1. Set up your variable per the [instructions in the previous tutorial](simple-shopping-list.md).

## Design the UI

1. Open the Tool pane.

   :::image type="content" source="../media/tutorial-compound-shopping-list/open-tool-panel.png" alt-text="Screenshot of where to go to open the card tool pane." border="false":::

1. Select the first text label and add `Compound List Example`.

1. Select the second text label and add `Use the field below to add items to your list:`

   :::image type="content" source="../media/tutorial-compound-shopping-list/add-items-text-block.png" alt-text="Screenshot adding text blocks to card." border="false":::

1. Now make the list, where each row in the list has:

   1. a text label with the name of the current item
   1. a check box that says `also` and the name of the current item

1. Drag a **Column set** to the card under the text label.

   :::image type="content" source="../media/tutorial-compound-shopping-list/add-column-set.png" alt-text="Screenshot of adding a column set to a card." border="false":::

1. Select the **Add Column** drop down twice to create two columns.

   :::image type="content" source="../media/tutorial-compound-shopping-list/add-two-columns-to-set.png" alt-text="Screenshot showing two added columns to column set in card." border="false":::

   > [!NOTE]
   > The columns will resize automatically when elements are added.

1. Add a text label into the first column.

   :::image type="content" source="../media/tutorial-compound-shopping-list/add-textblock-to-column.png" alt-text="Screenshot of a text block added to the first column in the column set." border="false":::

1. Add an **Check box** to the right-hand column.

   :::image type="content" source="../media/tutorial-compound-shopping-list/add-input-toggle-to-column.png" alt-text="Screenshot adding an input toggle to the second column in the column set." border="false":::

1. Drag and drop a second **Text input** below the column set to give the user the ability to add a new item to the list.

   :::image type="content" source="../media/tutorial-compound-shopping-list/add-input-text-to-card.png" alt-text="Screenshot of a text block added to the second column in the column set." border="false":::

1. In the Properties pane, set the following properties.

   1. **Name**: `itemToAdd`
   1. **Label**: `Add Item`

      :::image type="content" source="../media/tutorial-compound-shopping-list/set-name-and-label.png" alt-text="Screenshot of the name and label updated in the input text box." border="false":::

1. Drag and drop a **Button** below the text box.

   :::image type="content" source="../media/tutorial-compound-shopping-list/add-button-to-card.png" alt-text="Screenshot of adding a button to the card." border="false":::

1. In the Property pane, set the button title to `Add the Item`.

   :::image type="content" source="../media/tutorial-compound-shopping-list/update-button-title.png" alt-text="Screenshot updated button title." border="false":::

1. The card is now complete, and should look something like the following.

   :::image type="content" source="../media/tutorial-compound-shopping-list/card-ui-setup.png" alt-text="Screenshot of the card user interface." border="false":::

### Use the structure pane

Once you've added all the basic elements to a card, use the Tree view pane to select different elements quickly and easily so you can modify their properties. Expand all the triangles and you should see the full card structure.

:::image type="content" source="../media/tutorial-compound-shopping-list/view-card-structure.png" alt-text="Screenshot of the card structure." border="false":::

If you select any element in the card structure pane, it will select the corresponding item in the Card canvas. This will let you set up properties on the items quickly.

For the next step, you'll tweak a few properties to get ready for the one line of Power Fx necessary to make your card work.

1. In the structure pane, select the **Column set** element. This will show you the properties for the Column set on the right.

   :::image type="content" source="../media/tutorial-compound-shopping-list/column-set-properties.png" alt-text="Screenshot of the column set properties pane." border="false":::

   > [!NOTE]
   > The Name property of the Column set here has been set to `repeatingElement`, but this is just for organization. You don't have to change this name.

1. With the **Column set** still selected, in the property pane, select the **Advanced** tab.

   :::image type="content" source="../media/tutorial-compound-shopping-list/advanced-pane-in-properties.png" alt-text="Screenshot where to find the advanced pane for the column set." border="false":::

1. In the **Repeat for every** property, enter the text `myGroceryList`

   :::image type="content" source="../media/tutorial-compound-shopping-list/add-var-to-repeat-for-every.png" alt-text="Screenshot of adding the my grocery list variable to the repeat for every field in advanced properties." border="false":::

1. Save the card.

## Add items to the list

1. Select the button, either via the Card canvas or by selecting it in the Structure pane.

1. In the property pane, select the **Properties** tab.

1. Make sure that the type of the button is set to `Run Power Fx`.

1. Select the Power Fx edit pane at the top of the screen.

   :::image type="content" source="../media/tutorial-compound-shopping-list/select-pfx-bar.png" alt-text="Screenshot of the power fx bar." border="false":::

1. Add the following into the PowerFX edit field: `Collect(myGroceryList, itemToAdd);`

   This Power Fx expression will append the contents of the `itemToAdd` field to the `myGroceryList` table.

1. Save and preview your card.
