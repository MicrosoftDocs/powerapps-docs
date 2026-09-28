---
title: "Badge Modern Control in Canvas Apps: Properties and Examples"
description: "Discover how to use the Badge modern control in Power Apps canvas apps. Learn its semantic intents, icons, styling options, accessibility behavior, and examples."
author: yogeshgupta698
ms.topic: reference
ms.custom: canvas
ms.date: 09/24/2026
ms.subservice: canvas-maker
ms.author: yogupt
ms.reviewer: joshuapa
search.audienceType:
  - maker
contributors:
  - mduelae
  - yogeshgupta698
  - noazarur-microsoft
---

# Badge modern control in canvas apps

The **Badge** modern control displays compact status information, labels, counts, or categories in a canvas app.

## Description

Use the **Badge** control to highlight short information such as an unread count, item status, or category. The updated native control supports semantic intent colors, appearance and shape options, an optional icon, and an optional **OnSelect** action. Key properties are **Content**, **Intent**, **Appearance**, **Shape**, **Icon**, and **IconPosition**.

> [!NOTE]
> This article describes the updated Badge modern control. For information about what changed from the previous version, see [Recent updates](#recent-updates).

## General

**Content** – The text or number displayed in the badge. The default is `"AB"`. Keep the value short, such as `"5"`, `"New"`, or `"Active"`.

**Icon** – The Fluent icon name displayed alongside the content. The default is blank. If **Content** is blank, the badge can display only the icon.

**IconPosition** – The position of **Icon** relative to **Content**. Accepts `BadgeIconPosition.Before` (default) or `BadgeIconPosition.After`.

**Visible** – Whether the control appears or is hidden.

## Behavior

**OnSelect** – Actions to perform when the user selects the badge. When this property contains an active formula, the badge becomes interactive and responds to Enter or Space while it has keyboard focus. When the property is blank, the badge is display-only.

**DisplayMode** – Whether the control allows interaction (**Edit**), only displays content (**View**), or is disabled (**Disabled**). When the control isn't interactive, **OnSelect** doesn't fire.

## Size and position

**[X](../properties-size-location.md)** – Distance between the left edge of the control and the left edge of its parent container (screen if no parent container).

**[Y](../properties-size-location.md)** – Distance between the top edge of the control and the top edge of its parent container (screen if no parent container).

**Width** – Distance between the control's left and right edges. The default is **64** on desktop layouts and **88** on phone layouts.

**Height** – Distance between the control's top and bottom edges. The default is **32** on desktop layouts and **44** on phone layouts.

**Align** – The horizontal alignment of the badge content. Accepts `Align.Left`, `Align.Center` (default), `Align.Right`, or `Align.Justify`.

**VerticalAlign** – The vertical alignment of the badge content. Accepts `VerticalAlign.Top`, `VerticalAlign.Middle` (default), or `VerticalAlign.Bottom`.

**PaddingTop**, **PaddingRight**, **PaddingBottom**, **PaddingLeft** – The distance between the badge content and each edge of the control.

## Style and theme

**Appearance** – The visual treatment of the badge. Accepts `BadgeAppearance` enum values:

| Value | Description |
|---|---|
| `BadgeAppearance.Filled` | Solid background with contrasting content. |
| `BadgeAppearance.Ghost` | Transparent background with colored content. |
| `BadgeAppearance.Outline` | Transparent background with a colored border and content. |
| `BadgeAppearance.Tint` | Lightly tinted background with colored content. Default. |

**Shape** – The corner style of the badge. Accepts `BadgeShape` enum values:

| Value | Description |
|---|---|
| `BadgeShape.Circular` | Fully rounded or pill-shaped badge. Default. |
| `BadgeShape.Rounded` | Badge with rounded corners. |
| `BadgeShape.Square` | Badge with square corners. |

**Intent** – The semantic meaning that determines the badge's Fluent color treatment. Accepts `BadgeIntent` enum values:

| Value | Description |
|---|---|
| `BadgeIntent.Neutral` | Low-emphasis or subtle information. |
| `BadgeIntent.Highlight` | Brand-colored information that should stand out. |
| `BadgeIntent.Informative` | Informational or neutral context. |
| `BadgeIntent.Positive` | Successful or positive status. Default. |
| `BadgeIntent.Attention` | Important information that needs attention. |
| `BadgeIntent.Caution` | Warning or caution state. |
| `BadgeIntent.Urgent` | Severe or urgent state. |
| `BadgeIntent.Critical` | Critical error or destructive state. |

**BasePaletteColor** – The base color used to derive the badge's brand palette when **Intent** is `BadgeIntent.Highlight`.

**Font** – The font family used for the badge content.

**Size** – The font size of the badge content. When blank, the control inherits the app's default font size.

**Color** – The color of the badge content. When blank, **Intent** and **Appearance** determine the content color.

**FontWeight** – The weight of the badge content. Accepts `FontWeight.Bold`, `FontWeight.Semibold`, `FontWeight.Normal`, or `FontWeight.Lighter`.

**Italic** – Whether the badge content appears in italic style.

**Underline** – Whether a line appears under the badge content.

**Strikethrough** – Whether a line appears through the badge content.

**Fill** – The background color of the control. When blank, **Intent** and **Appearance** determine the background.

**BorderColor** – The color of the control's border.

**BorderStyle** – The style of the control's border.

**BorderThickness** – The thickness of the control's border.

**RadiusTopLeft**, **RadiusTopRight**, **RadiusBottomLeft**, **RadiusBottomRight** – The radius of each corner of the control.

## Additional properties

**AccessibleLabel** – A label read by screen readers. Provide a label that communicates the badge's meaning, such as `"5 unread notifications"`. An accessible label is especially important for an icon-only badge and for a badge with an **OnSelect** formula.

**Tooltip** – Explanatory text that appears when the user hovers over or focuses the control.

**ContentLanguage** – The display language for the badge content, if different from the app language.

## Accessibility

When **OnSelect** contains a formula, the badge uses button semantics and supports Enter and Space. When **OnSelect** is blank, the badge remains display-only.

Set **AccessibleLabel** so assistive technologies receive the badge's meaning, not only its short visual content. For an icon-only badge, the accessible label should describe the icon.

## Example

The following self-contained YAML example shows an interactive critical-alert badge:

```yaml
- CriticalAlertsBadge:
    Control: ModernBadge@1.0.0
    Properties:
      Content: ="3"
      Icon: ="Alert"
      IconPosition: =BadgeIconPosition.Before
      Intent: =BadgeIntent.Critical
      Appearance: =BadgeAppearance.Filled
      Shape: =BadgeShape.Circular
      AccessibleLabel: ="3 critical alerts"
      Tooltip: ="Show critical alerts"
      OnSelect: =Notify("3 critical alerts", NotificationType.Warning)
```

## Limitations

- The control doesn't retrieve presence, status, or notification data. Set **Content** and **Intent** with formulas based on your app's data.
- The control doesn't automatically shorten large counts. Use a Power Fx formula in **Content** to display a value such as `"99+"`.
- Studio doesn't conditionally require **AccessibleLabel** when **Content** is blank and **Icon** is set. Add the label explicitly so an icon-only badge has an accessible name.

## Recent updates

The updated version of the **Badge** modern control includes the following improvements and behavior changes.

### Property renames

| Previous property | New property |
|---|---|
| `FontColor` | `Color` |
| `FontSize` | `Size` |
| `FontItalic` | `Italic` |
| `FontStrikethrough` | `Strikethrough` |
| `FontUnderline` | `Underline` |
| `ThemeColor` | `Intent` |

### Theme color to semantic intent

The **ThemeColor** property is renamed to **Intent**, and the enum names now describe what the badge communicates rather than a raw color.

| Previous value | New value |
|---|---|
| `"Brand"` | `BadgeIntent.Highlight` |
| `"Danger"` | `BadgeIntent.Critical` |
| `"Important"` | `BadgeIntent.Attention` |
| `"Informative"` | `BadgeIntent.Informative` |
| `"Severe"` | `BadgeIntent.Urgent` |
| `"Subtle"` | `BadgeIntent.Neutral` |
| `"Success"` | `BadgeIntent.Positive` |
| `"Warning"` | `BadgeIntent.Caution` |

> [!NOTE]
> An empty previous **ThemeColor** maps to `BadgeIntent.Highlight` to preserve the earlier control's brand-color default. A newly inserted updated Badge uses `BadgeIntent.Positive` by default.

### Bug fixes and improvements

- **Updated enums**: `Appearance`, `Shape`, and `Intent` use the typed `BadgeAppearance`, `BadgeShape`, and `BadgeIntent` enums. Alignment and font weight values also use typed enums.
- **Icon support**: New **Icon** and **IconPosition** properties display a Fluent icon before or after the badge content.
- **OnSelect support**: The badge can trigger actions when selected and supports keyboard activation.
- **Tooltip support**: New **Tooltip** property shows explanatory text on hover or focus.
- **Native implementation**: The Badge is now a native control based on Fluent UI v9.

## See also

- [Modern controls overview](overview-modern-controls.md)
- [Recent updates to modern controls](modern-control-updates.md)
- [Size and location properties](../properties-size-location.md)
