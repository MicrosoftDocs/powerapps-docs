---
title: Button control in cards for Power Apps
description: Learn about the properties of the button control in cards for Power Apps.
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

# Button control in cards

[!INCLUDE[cards-deprecation-banner](~/includes/cards-deprecation-notice.md)]

A button control that executes Power Fx, opens a URL, shows a screen, or toggles visibility on select. Learn more about [how to use the button control](../make-a-card/ui-elements/use-buttons.md).

Buttons are added under the **actions** section of the tree view at the bottom of the card by default. This button can be placed elsewhere in the card and grouped with other buttons using a [button set control](button-set.md).

## Properties

**[Type](control-reference.md#t)** – What action the button should take on select - can be Show Screen, Run Power Fx, Open Url, or Toggle Visibility.

**[OnSelect](control-reference.md#o)** - The Power Fx that executes when a user taps or clicks on the button of type 'Run Power Fx'.

**[Screen](control-reference.md#s)** - The screen that is shown below the current card when a user taps or clicks on a button of type 'Show Screen'.

**[Url](control-reference.md#u)** - The url to open when a user taps or clicks on a button of type 'Open Url'.

**[Target Elements](control-reference.md#t)** - The elements to change the visibility of when a user taps or clicks on a button of type 'Toggle Visibility'.

**[Title](control-reference.md#t)** - Label for button or link that represents this button.

**[Style](control-reference.md#s)** - Controls the style of a button, which influences how the button is displayed, spoken, etc.

**[Tooltip](control-reference.md#t)** - Defines text that should be displayed to the end user as they hover the mouse over the action, and read when using narration software.

**[Mode](control-reference.md#m)** – Determines whether the action should be displayed as a primary button or in the overflow menu that's secondary.

**[IconUrl](control-reference.md#i)** - Optional icon to be shown on the button beside the title. Supports data URI in version 1.2+.

**[Associated inputs](control-reference.md#a)** - Controls which inputs are associated with the action.

**[Repeat for every](control-reference.md#r)** - The source of data that is used to show multiple instances of this control. Learn how to use [repeat for every](control-reference.md#r).

**[Show when](control-reference.md#s)** - Conditional layout expression.
