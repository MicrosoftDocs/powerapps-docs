---
title: Show or hide content from assistive technologies in canvas apps | Microsoft Docs
description: Techniques to show content to sighted users only or to screen reader users only for canvas apps
author: tahoon
ms.service: powerapps
ms.topic: article
ms.custom: canvas
ms.date: 10/22/2018
ms.author: tahoon
search.audienceType:
  - maker
search.app:
  - PowerApps
---
# Show or hide content from assistive technologies for canvas apps in PowerApps
Typically, content should be accessible to all users. However, in a minority of cases, it might be useful to show content to sighted users only or to screen reader users only. For example, descriptions of chart trends that are obvious visually should be hidden from sighted users. Yet another example is when an icon is described by an adjacent visible label. The icon can be hidden from screen reader users because having another description on the icon would be unnecessarily verbose.

## Hide content for all users
* Set **[Visible](controls/properties-core.md)** to false.

## Hide content for sighted users and show it to screen reader users
Use any of the following techniques
* Set **[Size](controls/properties-text.md)** to 0.
* Set **[Width](controls/properties-size-location.md)** and **[Height](controls/properties-size-location.md)** to 1.
* Set **[X](controls/properties-size-location.md)** and/or **[Y](controls/properties-size-location.md)** such that the control is outside the screen.
* Set **[Color](controls/properties-color-border.md)** and related properties to transparent.
* Position a rectangle **[Shape](controls/control-shapes-icons.md)** above the content. Set **[Fill](controls/properties-color-border.md)** to the same color as the background color of the screen.

> [!NOTE]
> Interactive controls like **[Buttons](controls/control-button.md)** that are hidden with one of the techniques above are still keyboard accessible. Set **[TabIndex](controls/properties-accessibility.md)** to -1 if you want to prevent the control from being reached by the TAB key.

## Hide content for screen reader users and show it to sighted users
* For **[Image](controls/control-image.md)**, **[Icon](controls/control-shapes-icons.md)**, and **[Shape](controls/control-shapes-icons.md)** controls, set **[AccessibleLabel](controls/properties-accessibility.md)** to the empty string "".

## Next steps
Learn about [accessibility properties](controls/properties-accessibility.md) in PowerApps controls.
