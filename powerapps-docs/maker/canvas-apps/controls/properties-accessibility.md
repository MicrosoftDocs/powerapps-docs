---
title: Accessibility properties for canvas apps | Microsoft Docs
description: Reference information about properties such as TabIndex and Tooltip
author: fikaradz
manager: kvivek
ms.service: powerapps
ms.topic: reference
ms.custom: canvas
ms.reviewer: tapanm
ms.date: 01/26/2017
ms.author: fikaradz
search.audienceType: 
  - maker
search.app: 
  - PowerApps
---
# Accessibility properties for canvas apps

Configuration of properties that aid alternative ways of interacting with controls suitable for users with disabilities.

## Properties

**AccessibleLabel** – Label for screen readers. An empty value for Image, Icon and Shape controls will make the controls invisible to the screen reader and treated as decorations.

**Live** – How screen readers should announce changes to content. Available only in the **[Label](control-text-box.md)** control.

* When set to **Off**, the screen reader doesn't announce changes.
* When set to **Polite**, the screen reader finishes speaking before announcing any changes that occurred while the screen reader was speaking.
* When set to **Assertive**, the screen reader interrupts itself to announce any changes that occurred while the screen reader was speaking.

Learn how to [announce dynamic changes with live regions](../accessible-apps-live-regions.md).

**TabIndex** – Determines if the control participates in keyboard navigation.

Keyboard navigation is an important aspect of any app.  For many the keyboard is more efficient than using touch or a mouse and it enables screen readers for the visually impaired.  The navigation order should:
- Mirror what is seen visually.
- Only have a tab stop at controls that are interactive.
- Follow either an intuitive across and then down "Z" order or a down and then across "reverse-N" order.

The above requirements will be met with the default **TabIndex** values and we recommend that you do not change them.  The default is what most users expect visually and it will work well with a screen reader.  But there may be cases in which you will want to override the default.  Use the **TabIndex** property and the [**Enhanced group** control](https://powerapps.microsoft.com/en-us/blog/enhanced-group-experimental-control-with-layout-control-and-nesting/) (experimental) to make adjustments to the navigation order.  

The **TabIndex** property has two recommended values:

| TabIndex value | Behavior | Default for |
|----------------|----------|-------------|
| 0 | Control participates in keyboard navigation. | [**Button**](control-button.md), [**Text input**](control-text-input.md), [**Combo box**](control-combo-box.md), and other typically interactive controls. |
| &minus;1 | Control does not participate in keyboard navigation. | [**Label**](control-text-box.md), [**Image**](control-image.md), [**Icon**](control-shapes-icons.md), and other typically non-interactive controls. |

Navigation order generally goes from left-to-right, then top-to-bottom, in a "Z" pattern. The order is based on the **X** and **Y** property values of the controls. If controls are dynamically moved on the screen, for example by having a formula for **X** or **Y** based on a timer or other control, the navigation order will change dynamically too.

Use the [**Enhanced group** control](https://powerapps.microsoft.com/en-us/blog/enhanced-group-experimental-control-with-layout-control-and-nesting/) (experimental) to bundle controls that should be navigated together or to create columns in a "reverse-N" pattern.  At the top of the following example, the name fields are contained within an enhanced group control which causes navigation to proceed down before moving across.  At the bottom of the example, no group controls are used, and navigation proceeds across and then down as normal which is not intuitive given the control groupings. 

![Animation showing enhanced group control causing navigation to proceed down within a group before moving across](media/properties-accessibility/enhanced-group.gif)

Similarly, tabbing through containers such as [**Form**](control-form-detail.md) and [**Gallery**](control-gallery.md) controls will navigate through all elements of the container before proceeding to the next control outside of the container.  

Controls which have a **Visible** property value of *false* or a **DisplayMode** property value of **Disabled** are not included in the navigation.  

When using a browser, navigating from the last control of the screen will move to the browser's built-in controls, such as the URL address.  

> [!WARNING]
> Avoid **TabIndex** values that are greater than 0. Ultimately controls are rendered in HTML where even the [W3C has warned](https://www.w3.org/TR/wai-aria-practices/#kbd_general_between) "Authors are strongly advised NOT to use these values." Many HTML tools warn for values greater than 0 as does the [App Checker](../accessibility-checker.md) when it reports "Check the order of the screen items."  All for good reason: using **TabIndex** in this manner can be very difficult to get right and can make assistive technologies such as screen readers unusable.
> 
> When controls exist with **TabIndex** greater than 0, users will navigate to controls with increasing **TabIndex** values (1, then 2, etc). When users have navigated all controls with positive **TabIndex** values, they will finally navigate to controls with **TabIndex** of 0 including the browser's built-in controls. When there are multiple controls with the same **TabIndex**, their **X** and **Y** position determines their relative order.





