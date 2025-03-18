---
title: Container control in cards for Power Apps
description: Learn about the properties of the container control in cards for Power Apps.
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

# Container control in cards

[!INCLUDE[cards-deprecation-banner](~/includes/cards-deprecation-notice.md)]

A standard container, useable with almost any control.

A container takes on the properties of the first control placed inside it. Only controls of the same type can be added to a container.

## Properties

**[Initially visible](control-reference.md#i)** – If false, this item will be removed from the visual tree.

**[Spacing](control-reference.md#s)** – Controls the amount of spacing between this control and the preceding control.

**[Divider](control-reference.md#d)** – When true, draw a separating line at the top of the control.

**[Horizontal alignment](control-reference.md#h)** – Controls the horizontal alignment of the column set.

**[Content alignment](control-reference.md#c)** – Defines how the content should be aligned vertically within the column.

**[Minimum height](control-reference.md#m)** – Specifies the minimum height of the column set in pixels, like "80px".

**[Height](control-reference.md#h)** – Specifies the height of the control.

**[Style](control-reference.md#s)** – Determines the styling of the container, allowed values: default, emphasis, good, attention, warning, accent.

**[Bleed](control-reference.md#b)** – Determines whether the control should bleed through its parent's padding.

**[Background image](control-reference.md#b)** – Specifies a background image. Acceptable formats are PNG, JPEG, and GIF.

**[Repeat for every](control-reference.md#r)** – The source of data that is used to show multiple instances of this control. Learn how to use [repeat for every](control-reference.md#r).

**[Show when](control-reference.md#s)** – Conditional layout expression.
