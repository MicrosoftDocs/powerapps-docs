---
title: Accessibility limitations in canvas apps
description: Learn about the accessibility limitations in canvas apps.
author: tahoon-ms
ms.service: powerapps
ms.topic: article
ms.custom: canvas
ms.date: 02/26/2021
ms.author: tahoon
ms.reviewer: tapanm
search.audienceType: 
  - maker
search.app: 
  - PowerApps
contributors:
  - chmoncay
  - tahoon-ms
  - tapanm-msft
---

# Accessibility limitations in canvas apps

You can [design and build accessible canvas apps](accessible-apps.md) with built-in controls. Sometimes, the combination of app design, use of various controls, and the configured control properties may result in an app to have an inaccessible user interface.

In this article, you'll learn about these accessibility limitations in canvas apps, and how can you improve the app interface to make it more accessible.

## Dialogs and overlays

Dialogs and user interfaces that appear on top of other content are not supported. These overlays require focus management, hiding background content from screen readers, and appropriate control roles.

Consider the following:

- Use separate screens for each “dialog”.
- Use the **[Notify](functions/function-showerror.md)** function.
- [Create a code component](../../developer/component-framework/overview.md) that implements an accessible dialog.

## Tabbed interfaces

Tabbed interfaces are not supported. A tabbed interface is made up of a list of tabs and a panel that shows content associated with the selected tab. The list of tabs should be navigable with arrow keys. Appropriate control roles and states are required.

Consider the following:

- Put each tab panel on a separate screen. Append the role and state of a tab to its **[AccessibleLabel](controls/properties-accessibility.md)**. For example, if an **[Icon](controls/control-shapes-icons.md)** is used as a tab, its label could be “Documents. Tab. 3 of 5. Selected.”.
- [Create a code component](../../developer/component-framework/overview.md) that implements an accessible tabbed interface.

## Custom tables

The only built-in control that supports two-dimensional data is the **[Data Table](controls/control-data-table.md)**. Avoid using **[Galleries](controls/control-gallery.md)** to present data in rows and columns. Rows and columns have to be annotated so that screen reader users can understand their structure and navigate cells.

Consider the following:

- Use the built-in **[Data Table](controls/control-data-table.md)**.
- Present data in one direction only with a **[Gallery](controls/control-gallery.md)**.
- [Create a code component](../../developer/component-framework/overview.md) that implements an accessible table.

## Custom combo boxes

It is possible to emulate a combo box by combining a **[Text Input](controls/control-text-input.md)** and a **[Gallery](controls/control-gallery.md)**. However, combo boxes assembled from built-in controls are not accessible. Combo boxes must handle arrow keys and set appropriate roles and states on its components.

Consider the following:

- Use the built-in **[Combo box](controls/control-combo-box.md)** or **[Drop down](controls/control-drop-down.md)**.
- [Create a code component](../../developer/component-framework/overview.md) that implements an accessible combo box.

## Scrollable content 

Keyboard users can't scroll **[Forms](controls/control-form-detail.md)**, **[Scrollable screens](add-scrolling-screen.md)**, and **[Containers](controls/control-container.md)** if there are no interactive controls inside them.

For **[Galleries](controls/control-gallery.md)** with no interactive content, you can set **[TabIndex](controls/properties-accessibility.md)** on the **Gallery** itself so that keyboard users can focus on it and use arrow keys to scroll it.

For **[Labels](controls/control-text-box.md)**, setting **TabIndex** will make them focusable for keyboard scrolling. However, it will also [turn them into buttons](controls/control-text-box.md#accessibility-guidelines). Don't making labels scrollable if they're not meant to be buttons. Ensure the **Label** is large enough to fit text. The **AutoHeight** property can be used to automatically adjust the control's size when it is inside a **Form**, **Scrollable screen**, or **Gallery**.

## Expandable sections

Expandable sections, also known as disclosures, contain content that is hidden until the user presses a button. There is no built-in support for these elements but there is a workaround.

Mention the expanded state in the **[AccessibleLabel](controls/properties-accessibility.md)** of the button. For example, “Show more details. Collapsed.”.

Update the **AccessibleLabel** when the expanded state changes. Position the expanded content immediately after the button so that screen reader users can logically navigate to it. Push other content down when the section expands.

## Landmarks

You can create headings with **[Label](controls/control-text-box.md)** controls. Navigation, banner, and other landmarks are not supported. Power Apps automatically sets the main landmark to the app screen.

For other landmarks, use a heading as a workaround.

## Custom roles and states

There is no built-in support for custom roles and states. Hence, it's not recommended to create composite check boxes, sliders, and toggles from built-in controls.

Consider the following:

- Mention the control's role and state in its **[AccessibleLabel](controls/properties-accessibility.md)**. For example, if an **[Icon](controls/control-shapes-icons.md)** is used as a check box, its label could be “Enable notifications. Check box. Checked.”.
- [Create a code component](../../developer/component-framework/overview.md) that sets WAI-ARIA [roles](https://www.w3.org/TR/wai-aria-1.1/#usage_intro) and [states](https://www.w3.org/TR/wai-aria-1.1/#introstates) as appropriate.

## Custom keyboard handling

It is not possible to react to specific key presses. For example, you can't have custom behavior for arrow keys or the Escape key. Hence, it is not possible to compose list-like controls like radio buttons from built-in controls. Nor can you create overlays that can be dismissed with the Escape key.

Enter or Space key handling is supported with **[OnSelect](controls/properties-core.md)**. However, this property is also triggered by other input methods like mouse clicks. There is no way to distinguish the source of the event.

## Focus management

**SetFocus** function can be used to change focus but it only works in [limited scenarios](functions/function-setfocus.md#limitations).

It is not possible to detect when controls receive or lose focus.

## Hide content from screen reader users only

There is no [aria-hidden](https://www.w3.org/TR/wai-aria-1.1/#aria-hidden) equivalent to show content to sighted users but hide it for screen reader users. Only [a few scenarios](accessible-apps-content-visibility.md) are supported.

## Next steps

[Accessibility properties](controls/properties-accessibility.md)

### See also

- [Create accessible apps](accessible-apps.md)
- [Accessible app structure](accessible-apps-structure.md)
- [Accessible colors in Power Apps](accessible-apps-color.md)
- [Show or hide content from assistive technologies for canvas apps](accessible-apps-content-visibility.md)
- [Announce dynamic changes with live regions for canvas apps](accessible-apps-live-regions.md)
- [Use the Accessibility checker](accessibility-checker.md)
