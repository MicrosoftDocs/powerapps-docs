---
title: Card controls (Preview)
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

# Controls (Preview)

[!INCLUDE[cards_preview_notice](../../includes/preview-include.md)]

These table details the basic building blocks of a card, and the ones you're most likely to use.

## Display

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

## Layout

Just like with the Button Group, use Layout when you want to group elements together, either for ease of reference or design purposes.

| **Item**  | **Description**                                                                                                                                                                                                      |
|-----------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Container | A standard container, useable with any element; takes on the properties of the first element placed inside. Doesn't support multiple element types at once.                                                          |
| Button set | Container for a set of buttons.                                                          |
| Image set  | Container for images; provides an easy UI method to add more images.                                                                                                                                                 |
| Fact set   | Creates a table of property/value pairs.                                                                                                                                                                             |
| Column set | Container for columns; provides an easy UI method to add more columns. Required when using columns.                                                                                                                  |
| Column    | Add to a Column set to create dividers on the page. Empty columns aren't inherently visible in the final card, so you'll need to put another element (like Text input) into a column to make it visible. |
