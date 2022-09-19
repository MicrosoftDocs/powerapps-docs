---
title: Add controls (Preview)
description: Learn about the different controls available for cards.
ms.date: 09/20/2022
ms.topic: article
author: iaanw
ms.author: iawilt
manager: shellyha
ms.reviewer: 
ms.custom: 
ms.collection: 
---

# Add card controls (Preview)

[!INCLUDE[cards_preview_notice](../../includes/preview-include.md)]

Controls are the building blocks for designing your card's interface and functionality. They let you add text, visual elements, and other elements that create a rich cards experience.

## Prerequisites

- A [Power Apps](https://powerapps.microsoft.com/) account.
- A card. For an example, see the [simple card tutorial](../../tutorials/hello-world-card.md).
- Familiarity with the [Card Designer](../make-a-card/designer-overview.md).

## Types of controls

To access card controls, go to [Power Apps](https://powerapps.microsoft.com/), select and a card, and then select **Insert**.

   :::image type="content" source="../../media/make-a-card/insert-menu.png" alt-text="Screenshot of the Insert menu Card Designer." border="false":::

There you'll see the following control categories:

- **Display**: controls that display elements, including text, images, and other media
- **Input**: controls that let you ask for different types of user input. These includes options where users can provide custom input (like text and numbers), specific types of input (like dates and time), as well as pre-determined options (like buttons and drop downs).
- **Layout**: controls that let you update the layout and physical appearance of elements on cards.

To add a control to your card, simply select the type you want and it will automatically be added to the card. After adding it you can change the control **Properties** on the right.

For information about all of the control types, see the [controls reference](#controls-reference) section.

## Controls reference

These table detail the available card controls.

### Display

| **Item**     | **Description**                                                                                                                                                                                               |
|--------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Text label    | Standard text block; supports strings and Power Fx formulas.                                                                                                                                                   |
| Image        | Supports addition of images to card via URL.                                                                                                                                                                  |
| Media        | Supports addition of other forms of media to card via URL.                                                                                                                                                    |

### Input

Use an input element when you want the end user of the card to specify information.

| **Item**        | **Description**                                                                                                           |
|-----------------|---------------------------------------------------------------------------------------------------------------------------|
| Text input     | Allow the user to input a text response; parses as a string.                                                              |
| Number input    | Allow the user to input a numerical response by typing a number or selecting from the up/down arrows; parses as a string. |
| Button       | Specify an action to occur when the button is pressed with Power Fx formula.                                                                       |
| Date picker      | Allow the user to input a date (mm/dd/yyyy) or choose a date from the dropdown calendar.                                  |
| Time picker     | Enter a time (HH:MM AM/PM) or select a time from the dropdown clock.                                                      |
| Drop down | User selects a choice from the dropdown; default is two choices, but more can be added.                                   |
| Checkbox    | Checkbox for the user to select if applicable; default is unchecked.                                                      |

### Layout

Just like with the Button Group, use Layout when you want to group elements together, either for ease of reference or design purposes.

| **Item**  | **Description**                                                                                                                                                                                                      |
|-----------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Container | A standard container, useable with any element; takes on the properties of the first element placed inside. Doesn't support multiple element types at once.                                                          |
| Button set | Container for a set of buttons.                                                          |
| Image set  | Container for images; provides an easy UI method to add more images.                                                                                                                                                 |
| Fact set   | Creates a table of property/value pairs.                                                                                                                                                                             |
| Column set | Container for columns; provides an easy UI method to add more columns. Required when using columns.                                                                                                                  |
| Column    | Add to a Column set to create dividers on the page. Empty columns aren't inherently visible in the final card, so you'll need to put another element (like Text input) into a column to make it visible. |

## Data binding

Data binding is used to repeat controls for a table variable using the **Repeat for every** advanced property.

For example, if you have a table named `fruits` with `["apples", "oranges", "pears"]`, you can add a **Text label** control and set the **Repeat for every** property to `fruits` and the **Text** property to `ThisItem`. When played, the card will show three text labels with each of the strings in the table.

   :::image type="content" source="../../media/make-a-card/cards-data-binding.png" alt-text="Screenshot of tree view in Card Designer." border="false":::
