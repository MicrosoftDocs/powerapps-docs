---
title: Upgrade Fluent UI Controls to Modern Controls
description: Learn how to upgrade the earlier Fluent UI (v8) controls to the latest modern controls in Power Apps canvas apps in Microsoft Teams and in custom pages in model-driven apps.
author: yogeshgupta698
ms.topic: how-to
ms.custom: canvas
ms.date: 07/20/2026
ms.subservice: canvas-maker
ms.author: yogupt
ms.reviewer: mkaur
search.audienceType:
  - maker
---

# Upgrade Fluent UI controls to modern controls

The Fluent UI (v8) controls are the earlier controls that you add to canvas apps in Microsoft Teams and to custom pages in model-driven apps. The updated modern controls are built on the Microsoft Fluent 2 design system and supersede these Fluent UI (v8) controls. You can upgrade the Fluent UI (v8) controls in your app to the latest modern controls.

> [!IMPORTANT]
> The Fluent UI (v8) controls in canvas apps in Microsoft Teams and in custom pages in model-driven apps are deprecated. Modern controls replace them. Upgrade your apps to modern controls to keep getting the latest design, performance, and accessibility improvements.

## Benefits of upgrading

When you upgrade to modern controls, your app gains the improvements that modern controls provide:

- **Microsoft Fluent 2 design**: Controls use the current Fluent 2 design system, so your app matches the latest Microsoft look and feel and stays visually consistent.
- **Theming**: Modern controls respond to the app theme, so you can restyle your app from one place instead of setting colors control by control.
- **Responsive sizing**: Controls use touch-friendly sizes and font defaults, and they adapt to different screen sizes and mobile layouts.
- **Built-in accessibility**: Modern controls improve keyboard navigation and screen reader support, and they use semantic structure for tab order, so you don't set tab numbers manually.
- **Enum-based properties**: Properties that took plain text strings now use typed enum values, so you get IntelliSense, autocomplete, and compile-time validation in your Power Fx formulas.
- **Better performance**: Events such as OnChange fire less often, which reduces unnecessary recalculation in your app.

## Where you can upgrade

Add and upgrade the Fluent UI (v8) controls in these two app surfaces:

- [Canvas apps in Microsoft Teams](../../../../teams/use-the-fluent-ui-controls.md)
- [Custom pages in model-driven apps](../../../model-driven-apps/design-page-for-model-app.md)

These are the only surfaces where the Fluent UI (v8) controls are used.

## Controls you can upgrade

In canvas apps in Microsoft Teams and in custom pages in model-driven apps, upgrade the following Fluent UI (v8) controls to modern controls:

- Button
- Text input (Text box)
- Combo box
- Date picker
- Radio group
- Rating
- Slider

## Upgrade a control

1. Open your canvas app in Microsoft Teams, or your custom page in a model-driven app, in Power Apps Studio.
1. Select the Fluent UI (v8) control that you want to upgrade.
1. Select the **Update** action on the control or in the control's properties.
1. Review the property mapping and the changes that Studio applies.

You can undo and redo the upgrade if you need to.

## Property changes

When you upgrade a control, Studio maps supported properties to modern control properties. Not every property maps one-to-one.

| Earlier property | Modern property |
| --- | --- |
| ButtonType | Appearance |
| Value | Default |
| ColorText | Color |
| Layout | LayoutDirection |
| Font size | Font size changes from points to pixels. Values are scaled. |
| TabIndex | Removed |
| AcceptsFocus | Removed |

## Considerations

- Some earlier styling options, including hover, pressed, disabled state colors, and focus outline, aren't available on modern controls.
- Any property without a modern equivalent isn't carried over.
- Review each control after upgrading to confirm its behavior, layout, and styling.

## See also

- [Overview of modern controls](overview-modern-controls.md)
- [Modern controls reference](modern-controls-reference.md)
