---
title: Accessibility properties for Power Apps
description: Reference information about properties related to accessibility in Power Apps.
author: chmoncay
ms.service: powerapps
ms.topic: reference
ms.custom: canvas
ms.reviewer: tapanm
ms.date: 02/18/2021
ms.subservice: canvas-maker
ms.author: chmoncay
search.audienceType: 
  - maker
search.app: 
  - PowerApps
contributors:
  - chmoncay
  - tahoon-ms
  - tapanm-msft
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

### TabIndex
Determines if the control participates in keyboard navigation.

Keyboard navigation is an important aspect of any app. For many, the keyboard is more efficient than using touch or a mouse. The navigation order should:
- Mirror what is seen visually.
- Only have a tab stop at controls that are interactive.
- Follow either an intuitive across and then down "Z" order or a down and then across "reverse-N" order.

The **TabIndex** property has two recommended values:

| TabIndex value | Behavior | Default for |
|----------------|----------|-------------|
| 0 | Control participates in keyboard navigation. | [**Button**](control-button.md), [**Text input**](control-text-input.md), [**Combo box**](control-combo-box.md), and other typically interactive controls. |
| &minus;1 | Control does not participate in keyboard navigation. | [**Label**](control-text-box.md), [**Image**](control-image.md), [**Icon**](control-shapes-icons.md), and other typically non-interactive controls. |

A logical keyboard navigation sequence can be achieved with just these values, along with the use of the [**Container**](control-container.md) control. We recommend that you do not set **TabIndex** to other values.

When **TabIndex** of all controls are set to either -1 or 0, navigation order goes from left-to-right, then top-to-bottom, in a "Z" pattern. The order is based on the **X** and **Y** property values of the controls. If controls are dynamically moved on the screen, for example, by having its **X** or **Y** value change according to a timer or other control, the navigation order will change dynamically too.

Use the [**Container**](control-container.md) control to bundle controls that should be navigated together or to create columns in a "reverse-N" pattern. Controls in **[Form Cards](control-card.md)** and [**Galleries**](control-gallery.md) are automatically grouped. Tabbing through these containers will navigate through all elements inside the container before proceeding to the next control outside of the container.  

Controls that have a **Visible** property value of *false* or a **DisplayMode** property value of **Disabled** are not included in keyboard navigation.

> [!IMPORTANT]
> **TabIndex** only affects keyboard navigation. A [logical control order](../accessible-apps-structure.md) is still necessary for screen reader users to understand app structure.

> [!WARNING]
> - For rare scenarios where you may not want to follow visual order or logical structure, you can customize the keyboard navigation order by setting **TabIndex** to be greater than zero. If you do this, the accessibility tools will give you a warning about this change. Use caution since it can be difficult to get the order correct and accurate with this manual change that can result in a confusing screen reader experience.
> - When there are controls with **TabIndex** greater than 0, users will first navigate to controls with increasing positive **TabIndex** values (such as, 1, then 2). When users have navigated all controls with positive **TabIndex** values, they will finally navigate to controls with **TabIndex** of 0. When there are multiple controls with the same **TabIndex**, their **X** and **Y** value and the **Containers** they are in will determine their relative order. Inside a **Gallery** or **Form**, **TabIndex** is scoped so that the contained controls will be navigated first before the ones outside.

### See also

- [Create accessible apps](../accessible-apps.md)
- [Accessible app structure](../accessible-apps-structure.md)
- [Accessible colors in Power Apps](../accessible-apps-color.md)
- [Show or hide content from assistive technologies for canvas apps](../accessible-apps-content-visibility.md)
- [Announce dynamic changes with live regions for canvas apps](../accessible-apps-live-regions.md)
- [Use the Accessibility checker](../accessibility-checker.md)
- [Accessibility limitations in canvas apps](../accessible-apps-limitations.md)
