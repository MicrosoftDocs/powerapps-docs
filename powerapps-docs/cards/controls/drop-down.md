---
title: Drop down control in cards for Power Apps
description: Learn about the properties of the drop-down control in cards for Power Apps.
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

# Drop down control in cards

[!INCLUDE[cards-deprecation-banner](~/includes/cards-deprecation-notice.md)]

A menu that lets users choose one item from an expandable list of items. The default is two choices, but more can be added.

## Properties

**[Value](control-reference.md#v)** – The initial item (or set of items) that should be selected. For multi-select, specify a comma-separated string of values.

**[Choices](control-reference.md#c)** - The list of items the user can select from.

**[Placeholder](control-reference.md#p)** – Description of the input desired. Only visible when no selection has been made, the style is compact and isMultiSelect is false.

**[Label](control-reference.md#l)** – Label for this input.

**[Wrap](control-reference.md#w)** – If true, allow text to wrap. Otherwise, text is clipped.

**[Multiple selection](control-reference.md#m)** – Allow multiple items to be selected.

**[Initially visible](control-reference.md#i)** – If false, this item will be removed from the visual tree.

**[Spacing](control-reference.md#s)** – Controls the amount of spacing between this control and the preceding control.

**[Divider](control-reference.md#d)** – When true, draw a separating line at the top of the control.

**[Height](control-reference.md#h)** – Specifies the height of the control.

**[Error message](control-reference.md#e)** – Error message to display when entered input is invalid.

**[Required field](control-reference.md#r)** – Whether or not this input is required.

**[Repeat for every](control-reference.md#r)** – The source of data that is used to show multiple instances of this control. Learn how to use [repeat for every](control-reference.md#r).

**[Show when](control-reference.md#s)** – Conditional layout expression.
