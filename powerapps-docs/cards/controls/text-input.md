---
title: Text input control in cards for Power Apps
description: Learn about the properties of the text input control in cards for Power Apps.
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

# Text input control in cards

[!INCLUDE[cards-deprecation-banner](~/includes/cards-deprecation-notice.md)]

A field for users to type text.

## Properties

**[Default value](control-reference.md#d)** – The initial value for this field.

**[Placeholder](control-reference.md#p)** – Description of the input desired. Displayed when no selection has been made.

**[Label](control-reference.md#l)** – Label for this input.

**[Multiline](control-reference.md#m)** – If true, allow multiple lines of input.

**[Style](control-reference.md#s)** – Determines the input type of the text input control, allowed values: text, tel, url, email, password.

**[Max length](control-reference.md#m)** – Hint of maximum length characters to collect (may be ignored by some clients).

**[InlineAction](control-reference.md#i)** – The inline action for the input. Typically displayed to the right of the input. It is strongly recommended to provide an icon on the action (which will be displayed instead of the title of the action).

**[Initially visible](control-reference.md#i)** – If false, this item will be removed from the visual tree.

**[Spacing](control-reference.md#s)** – Controls the amount of spacing between this control and the preceding control.

**[Divider](control-reference.md#d)** – When true, draw a separating line at the top of the control.

**[Height](control-reference.md#h)** – Specifies the height of the control.

**[Required field](control-reference.md#r)** – Whether or not this input is required.

**[Error message](control-reference.md#e)** – Error message to display when entered input is invalid.

**[Regex](control-reference.md#r)** – Regular expression indicating the required format of this text input.

**[Repeat for every](control-reference.md#r)** – The source of data that is used to show multiple instances of this control. Learn how to use [repeat for every](control-reference.md#r).

**[Show when](control-reference.md#s)** – Conditional layout expression.
