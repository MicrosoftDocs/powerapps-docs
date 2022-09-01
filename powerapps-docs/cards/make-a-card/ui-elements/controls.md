---
title: "Card controls"
description: "Learn about the different controls available for cards"
keywords: "Cards Designer, Power Apps, Cards, controls"
ms.date: 09/20/2022
ms.topic: article
author: iaanw
ms.author: iawilt
manager: shellyha
ms.reviewer: 
ms.custom: 
ms.collection: 
---

# Controls

These are the basic building blocks of a card, and the ones you're most likely to use.

| **Item**     | **Description**                                                                                                                                                                                               |
|--------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| TextBlock    | Standard text block; supports strings and PowerFX formulas.                                                                                                                                                   |
| Button       | Specify an action to occur when the button is pressed with PowerFX formula.                                                                                                                                   |
| Image        | Supports addition of images to card via URL.                                                                                                                                                                  |
| Media        | Supports addition of other forms of media to card via URL.                                                                                                                                                    |
| Button Group | If you have multiple buttons in one location on the card, use a Button Group to manage the buttons under one parent element (visible on the Structure page). Provides an easy UI method to add more buttons.  |

#### Inputs

Use an input element when you want the end user of the card to specify information.

| **Item**        | **Description**                                                                                                           |
|-----------------|---------------------------------------------------------------------------------------------------------------------------|
| Input.Text      | Allow the user to input a text response; parses as a string.                                                              |
| Input.Number    | Allow the user to input a numerical response by typing a number or selecting from the up/down arrows; parses as a string. |
| Input.Date      | Allow the user to input a date (mm/dd/yyyy) or choose a date from the dropdown calendar.                                  |
| Input.Time      | Enter a time (HH:MM AM/PM) or select a time from the dropdown clock.                                                      |
| Input.ChoiceSet | User selects a choice from the dropdown; default is two choices, but more can be added.                                   |
| Input.Toggle    | Checkbox for the user to select if applicable; default is unchecked.                                                      |

#### Containers

Just like with the Button Group in the Elements section, use a container when you want to group elements together, either for ease of reference or design purposes.

| **Item**  | **Description**                                                                                                                                                                                                      |
|-----------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Container | A standard container, useable with any element; takes on the properties of the first element placed inside. Doesn't support multiple element types at once.                                                          |
| ImageSet  | Container for images; provides an easy UI method to add more images.                                                                                                                                                 |
| FactSet   | Creates a table of property/value pairs.                                                                                                                                                                             |
| ColumnSet | Container for columns; provides an easy UI method to add more columns. Required when using columns.                                                                                                                  |
| Column    | Add to a ColumnSet to create dividers on the page. Empty columns aren't inherently visible in the final card, so you'll need to put another element (e.g., TextBlock, Input, etc.) into a column to make it visible. |
