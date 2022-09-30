---
title: "Work with repeating controls"
description: "Learn about to make controls repeat for a table"
keywords: "Card Designer, Power Apps, cards, controls"
ms.date: 09/20/2022
ms.topic: article
author: iaanw
ms.author: iawilt
manager: shellyha
ms.reviewer: 
ms.custom: 
ms.collection: 
---

# Data binding

Data binding is used to repeat controls for a table variable using the **Repeat for every** advanced property.

For example, if you have a table named `fruits` with `["apples", "oranges", "pears"]`, you can add a **Text label** control and set the **Repeat for every** property to `fruits` and the **Text** property to `ThisItem`. When played, the card will show three text labels with each of the strings in the table.

   :::image type="content" source="../../media/make-a-card/cards-data-binding.png" alt-text="Screenshot of tree view in Card Designer." border="false":::

This same data binding pattern for tables can be used with other controls and within column sets and containers. 