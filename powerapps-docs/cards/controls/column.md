---
title: Column control in cards for Power Apps
description: Learn about the properties of the column control in cards for Power Apps.
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

# Column control in cards

[!INCLUDE[cards-deprecation-banner](~/includes/cards-deprecation-notice.md)]

An individual column which acts as a container for other elements. This column can be arranged side-by-side with other columns using the [column set control](column-set.md).

Add to a column set to create dividers on the page. Empty columns aren't visible. You'll need to put another control (like a text input control) into a column to make it visible. You can drag and drop controls into a column within the card canvas.

## Properties

**[Initially visible](control-reference.md#i)** – If false, this item will be removed from the visual tree.

**[Spacing](control-reference.md#s)** – Controls the amount of spacing between this control and the preceding control.

**[Divider](control-reference.md#d)** – When true, draw a separating line at the top of the control.

**[Minimum height](control-reference.md#m)** – Specifies the minimum height of the column set in pixels, like "80px".

**[Content alignment](control-reference.md#c)** – Defines how the content should be aligned vertically within the column.

**[Width](control-reference.md#w)** – Auto, stretch, a number representing relative width of the column in the column group, or in version 1.1 and higher, a specific pixel width, like "50px".

**[Style](control-reference.md#s)** – Style hint for this control, allowed values: default, emphasis, good, attention, warning, accent.

**[Background image](control-reference.md#b)** – Specifies a background image. Acceptable formats are PNG, JPEG, and GIF.

**[Bleed](control-reference.md#b)** – Determines whether the control should bleed through its parent's padding.

**[Repeat for every](control-reference.md#r)** – The source of data that is used to show multiple instances of this control. Learn how to use [repeat for every](control-reference.md#r).

**[Show when](control-reference.md#s)** – Conditional layout expression.
