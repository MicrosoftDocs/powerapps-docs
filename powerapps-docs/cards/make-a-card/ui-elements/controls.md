---
title: Add controls to a card (Preview)
description: Learn about controls you can add to your Microsoft Power Apps cards.
ms.date: 09/20/2022
ms.topic: how-to
author: iaanw
ms.author: iawilt
manager: shellyha
ms.reviewer: 
ms.custom: 
ms.collection: 
---

# Add controls to a card (Preview)

[!INCLUDE[cards_preview_notice](../../includes/preview-include.md)]

Controls are the building blocks of your card's interface and functionality. They add text, images, and other elements to create a rich cards experience. Insert, modify, and remove them in the [card designer](../designer-overview.md).

There are three categories of controls that you can add to your card:

- **Display**: Controls that display elements, including text, images, and other media
- **Input**: Controls that ask for information from users, such as text, numbers, and dates, or that allow the user to interact with the card, such as buttons and drop-down lists
- **Layout**: Controls that modify the layout and physical appearance of card elements

## Prerequisites

- A [Power Apps](https://powerapps.microsoft.com/) account
- [A card](../../tutorials/hello-world-card.md)

## Insert a control

1. Sign in to [Power Apps](https://powerapps.microsoft.com/). Select **Cards (preview)** > **Cards**, and then select a card.

1. In the left pane of the card designer, select **Insert**.

   :::image type="content" source="../../media/make-a-card/insert-menu.png" alt-text="Screenshot of the Insert menu in the Power Apps card designer.":::

1. In the tool pane, select a category to expand it, and then select a control from the list to place it on the card.

    You can also drag a control from the list and drop it on the card.

1. With the control selected, use the **Properties** pane to modify it.

## Controls reference

The following tables describe the card controls.

### Display

| Item | Description |
| --- | --- |
| Text label | Standard text block; enter strings and Power Fx formulas |
| Image | Enter an image file URL |
| Media | Supports adding other forms of media to the card using the file URL |

### Input

Use an input element when you want the end user of the card to specify information.

| Item        | Description                                                                                                           |
|-----------------|---------------------------------------------------------------------------------------------------------------------------|
| Text input     | Allow the user to input text. The value is stored as a string.                          |
| Number input    | Allow the user to input a number. The value is stored as a string. |
| Button       | Allow the user to select a button. Use a Power Fx formula to control what happens when the button is selected.                                                                       |
| Date picker      | Allow the user to input a date (in mm/dd/yyyy format) or choose a date from the dropdown calendar. The value is stored as a Date.                                  |
| Time picker     | Enter a time (in HH:MM AM/PM format) or select a time from the dropdown clock. The variable is stored as a Time.                                                      |
| Drop down | User selects a choice from the dropdown; default is two choices, but more can be added.                                   |
| Checkbox    | Checkbox for the user to select, if applicable; default is unchecked.                                                      |

### Layout

Just like with the **Button** group, use layout controls when you want to group elements together, either for ease of reference or design purposes.

| Item  | Description                                                                                                                                                                                                      |
|-----------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Container | A standard container, useable with any element; takes on the properties of the first element placed inside. Doesn't support multiple element types at once.                                                          |
| Button set | Container for a set of buttons.                                                          |
| Image set  | Container for images; provides an easy UI method to add more images.                                                                                                                                                 |
| Fact set   | Creates a table of property-value pairs.                                                                                                                                                                             |
| Column set | Container for columns; provides an easy UI method to add more columns. Required when using columns.                                                                                                                  |
| Column    | Add to a column set to create dividers on the page. Empty columns aren't inherently visible in the final card, so you'll need to put another element (like a text input control) into a column to make it visible. |

## Data binding

Data binding is used to repeat controls for a table variable using the **Repeat for every** advanced property.

For example, if you have a table named `fruits` bound to the array `["apples", "oranges", "pears"]`, you can add a text label control and set its **Repeat for every** property to `fruits` and the **Text** property to `ThisItem`. When played, the card will show three text labels with each of the strings in the table.

   :::image type="content" source="../../media/make-a-card/cards-data-binding.png" alt-text="Screenshot of tree view in Card Designer.":::
