---
title: Accessibility properties for Power Apps
description: Reference information about properties related to accessibility in Power Apps.
author: yogeshgupta698

ms.topic: reference
ms.custom: canvas
ms.reviewer: mkaur
ms.date: 09/06/2022
ms.subservice: canvas-maker
ms.author: yogupt
search.audienceType: 
  - maker
contributors:
  - yogeshgupta698
  - tahoon-ms
  - mduelae
---
# Accessibility properties for Power Apps

Configuration of properties that aid alternative ways of interacting with controls suitable for users with disabilities.

## Properties

### AccessibleLabel
Label for screen readers.

An empty value for Image, Icon, and Shape controls will hide the controls from screen reader users.

### Live
How screen readers should announce changes to content. Available only in the **[Label](control-text-box.md)** control.

* When set to **Off**, the screen reader doesn't announce changes.
* When set to **Polite**, the screen reader finishes speaking before announcing any changes that occurred while the screen reader was speaking.
* When set to **Assertive**, the screen reader interrupts itself to announce any changes that occurred while the screen reader was speaking.

Learn how to [announce dynamic changes with live regions](../accessible-apps-live-regions.md).

### Role
Intended purpose of a control. Available only in the **[Label](control-text-box.md)** control.

This lets screen reader users know whether a **Label** is a heading and allows them to navigate quickly to different parts of the app. There should be exactly one **Heading1** in each screen that serves as the main heading. Use **Heading2** for subheadings. **Heading3** and **Heading4** can be used for finer hierarchies of headings.

Use **Default** for normal text.

### AcceptsFocus and TabIndex
Determines if the control participates in keyboard navigation.

You can use **AcceptsFocus** to configure keyboard navigation for [modern controls](./modern-controls/overview-modern-controls.md). [Classic controls](../reference-properties.md) use **TabIndex**.

| AcceptsFocus | TabIndex | Behavior | Default for |
|--------------|----------|----------|-------------|
| true | 0 or greater | Control participates in keyboard navigation, unless it's hidden or disabled. | [**Button**](control-button.md), [**Text input**](control-text-input.md), [**Combo box**](control-combo-box.md), and other typically interactive controls. |
| false | &minus;1 or less than 0 | Control does not participate in keyboard navigation. | [**Label**](control-text-box.md), [**Image**](control-image.md), [**Icon**](control-shapes-icons.md), and other typically non-interactive controls. |

Any keyboard navigation sequence can be achieved with just these properties, along with the use of the [**Container**](control-container.md) control. For **TabIndex**, we recommend using either 0 or -1 for simplicity.

Controls that have a **Visible** property value of *false* or a **DisplayMode** property value of **Disabled** are not included in keyboard navigation.

> [!IMPORTANT]
> **TabIndex** only affects keyboard navigation. A [logical control order](../accessible-apps-structure.md) is still necessary for screen reader users to understand app structure. Some screen reader users don't even use keyboards.


### See also

- [Create accessible apps](../accessible-apps.md)
- [Accessible app structure](../accessible-apps-structure.md)
- [Accessible colors in Power Apps](../accessible-apps-color.md)
- [Show or hide content from assistive technologies for canvas apps](../accessible-apps-content-visibility.md)
- [Announce dynamic changes with live regions for canvas apps](../accessible-apps-live-regions.md)
- [Use the Accessibility checker](../accessibility-checker.md)
- [Accessibility limitations in canvas apps](../accessible-apps-limitations.md)
