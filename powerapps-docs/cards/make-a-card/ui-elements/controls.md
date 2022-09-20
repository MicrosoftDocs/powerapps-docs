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
- **Input**: Controls that ask for information from users, such as text, numbers, and dates, or that allow the user to interact with the card, such as buttons and lists
- **Layout**: Controls that modify the layout and appearance of card elements

## Prerequisites

- A [Power Apps](https://powerapps.microsoft.com/) account
- [A card](../../tutorials/hello-world-card.md)

## Insert a control

1. Sign in to [Power Apps](https://powerapps.microsoft.com/). Select **Cards (preview)** > **Cards**, and then select a card.

1. In the left pane of the card designer, select **Insert**.

1. In the tool pane, select a category to expand it, and then select a control from the list to place it on the card. You can also drag a control from the list and drop it on the card.

   :::image type="content" source="../../media/make-a-card/insert-menu.png" alt-text="Screenshot of the Insert menu in the Power Apps card designer.":::

1. With the control selected, use the properties pane to modify it.

## Controls reference

The following tables describe the card controls.

### Display

| Item | Description |
| --- | --- |
| Text label | Standard text block; accepts strings and Power Fx formulas |
| Image | Accepts image URLs |
| Media | Accepts other media URLs |

### Input

| Item | Description |
| --- | --- |
| Text input | Allows the user to enter text. The value is stored as a string. |
| Number input | Allows the user to enter a number. The value is stored as a string. |
| Button | Allows the user to select a button. Use a Power Fx formula to control what happens when the button is selected. |
| Date picker | Allows the user to enter a date in mm/dd/yyyy format or select a date on the calendar. The value is stored as a date. |
| Time picker | Allows the user to enter a time in HH:MM AM/PM format or select a time from a list of hours and minutes. The value is stored as a time. |
| Drop down | Allows the user to select an option from a list. The default is two choices, but more can be added. |
| Check box | Allows the user to select a check box. The default is "not selected." |

### Layout

| Item | Description |
| --- | --- |
| Container | A standard container, useable with any element<br>A container takes on the properties of the first element placed inside it. Only elements of the same type can be added to a container. |
| Button set | A container for a group of buttons |
| Image set | A container for a group of images |
| Fact set | A table of property-value pairs |
| Column set | A container for columns |
| Column  | Add to a column set to create dividers on the page<br>Empty columns aren't visible. You'll need to put another element (like a text input control) into a column to make it visible. |
