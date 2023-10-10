---
title: Work with repeating controls in cards
description: Learn how to make controls repeat in a table in cards for Microsoft Power Apps.
keywords: "Card Designer, Power Apps, cards, controls"
ms.date: 09/20/2022
ms.topic: conceptual
author: iaanw
ms.author: iawilt
ms.reviewer: 
ms.custom: 
ms.collection: 
---

# Work with repeating controls in cards

Data binding is used to repeat controls for a table variable using the **Repeat for every** advanced property.

For example, if you have a table named `fruits` bound to the array `["apples", "oranges", "pears"]`, you can add a Text label control and set its **Repeat for every** property to `fruits` and its **Text** property to `ThisItem.Value`. When it's opened, the card shows three text labels with each of the strings in the table.

   :::image type="content" source="../../media/make-a-card/cards-data-binding.png" alt-text="Screenshot of a card with a table with the values 'apples,' 'oranges,' and 'pears' in a column.":::

The same data binding pattern for tables can be used with other controls and in column sets and containers.
