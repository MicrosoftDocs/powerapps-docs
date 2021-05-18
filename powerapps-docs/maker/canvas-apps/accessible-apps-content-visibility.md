---
title: Show or hide content from assistive technologies for canvas apps
description: Techniques to show content only to sighted users or only to screen-reader users only for canvas apps
author: tahoon-ms
ms.service: powerapps
ms.topic: article
ms.custom: canvas
ms.date: 02/18/2021
ms.author: tahoon
search.audienceType:
  - maker
search.app:
  - PowerApps
contributors:
  - tahoon-ms
  - tapanm-msft
  - chmoncay
---

# Show or hide content from assistive technologies for canvas apps

In most cases, all users should be able to access all content, but you might occasionally want to show content only to sighted users or only to screen-reader users. For example, you might want only screen-reader users to access descriptions of chart trends that are obvious to sighted users. You might also want to hide an icon from screen-reader users if an adjacent label describes it. Another description on the icon would be unnecessarily verbose.

## Hide content from all users

* Set **[Visible](controls/properties-core.md)** to false.

## Hide content from sighted users and show it to screen-reader users

Use any of these techniques:

* Set **[Size](controls/properties-text.md)** to 0.
* Set **[Width](controls/properties-size-location.md)** and **[Height](controls/properties-size-location.md)** to 1.
* Set **[X](controls/properties-size-location.md)**, **[Y](controls/properties-size-location.md)**, or both properties such that the control is outside the screen.
* Set **[Color](controls/properties-color-border.md)** and related properties to transparent.
* Position a rectangle **[Shape](controls/control-shapes-icons.md)** above the content, and set **[Fill](controls/properties-color-border.md)** to the same color as the background color of the screen.

> [!NOTE]
> Users can still use a keyboard to access an interactive control, such as a **[Button](controls/control-button.md)**, even if you hide it by using one of the techniques in the previous list. Set **[TabIndex](controls/properties-accessibility.md)** to -1 if you want to prevent users from accessing the control by pressing the Tab key.

## Hide content from screen-reader users and show it to sighted users

* For **[Image](controls/control-image.md)**, **[Icon](controls/control-shapes-icons.md)**, and **[Shape](controls/control-shapes-icons.md)** controls, set **[AccessibleLabel](controls/properties-accessibility.md)** to the empty string "".

## Next steps

[Announce dynamic changes with live regions for canvas apps](accessible-apps-live-regions.md)

### See also

- [Create accessible apps](accessible-apps.md)
- [Accessible app structure](accessible-apps-structure.md)
- [Accessible colors in Power Apps](accessible-apps-color.md)
- [Use the Accessibility checker](accessibility-checker.md)
- [Accessibility limitations in canvas apps](accessible-apps-limitations.md)
- [Accessibility properties](controls/properties-accessibility.md)
