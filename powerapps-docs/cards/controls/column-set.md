---
title: Column set control in cards for Power Apps
description: Learn about the properties of the column set control in cards for Power Apps.
author: anuitz
ms.topic: reference
ms.custom: 
ms.reviewer: mkaur
ms.date: 03/01/2023
ms.author: anuitz
search.audienceType:
  - maker
contributors:
  - mduelae
  - anuitz
---

# Column set control in cards

[!INCLUDE[cards-deprecation-banner](~/includes/cards-deprecation-notice.md)]

A collection of columns, each column is a container. These columns allow controls to sit side-by-side.

Column set is useful for showing a row of data. You can add a column for the different UI elements you want within the column set, then drag and drop those elements into the column within the card canvas. You can also [data bind](../make-a-card/ui-elements/data-binding.md) a column set to a collection or data source to repeat the column set for each row, resulting in a list of data. 

## Properties

**[Style](control-reference.md#s)** – Determines the style of the control, allowed values: default, emphasis, good, attention, warning, accent.

**[Bleed](control-reference.md#b)** – Determines whether the control should bleed through its parent's padding.

**[Minimum height](control-reference.md#m)** – Specifies the minimum height of the column set in pixels, like "80px".

**[Initially visible](control-reference.md#i)** – If false, this item will be removed from the visual tree.

**[Spacing](control-reference.md#s)** – Controls the amount of spacing between this control and the preceding control.

**[Divider](control-reference.md#d)** – When true, draw a separating line at the top of the control.

**[Horizontal alignment](control-reference.md#h)** – Controls the horizontal alignment of the column set.

**[Height](control-reference.md#h)** – Specifies the height of the control.

**[Repeat for every](control-reference.md#r)** – The source of data that is used to show multiple instances of this control. Learn how to use [repeat for every](control-reference.md#r).

**[Show when](control-reference.md#s)** – Conditional layout expression.
