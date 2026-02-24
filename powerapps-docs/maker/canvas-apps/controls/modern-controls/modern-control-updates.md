---
title: Recent modern control updates in canvas apps - Power Apps
description: Overview of recent updates to modern controls in Power Apps canvas apps, including property renames, bug fixes, and new features available starting February 2026.
author: yogeshgupta698
ms.topic: overview
ms.custom: canvas
ms.date: 02/23/2026
ms.subservice: canvas-maker
ms.author: yogupt
ms.reviewer: mkaur
search.audienceType:
  - maker
---

# Updates to modern controls in canvas apps

Modern controls in Power Apps canvas apps receive regular quality updates that improve performance, fix bugs, and add new features. Starting February 2026, significant updates are available for modern controls including Text, Number Input, Date Picker, and others.

These updates include property renames, behavioral changes, and new enum patterns that may require formula updates in your existing apps. When you open apps with previous versions of these controls, you'll see update notifications with links to detailed migration guidance.

Key benefits of updating:

- Improved performance and reliability
- Enhanced mobile experience with optimized defaults
- New styling capabilities and flexibility
- Better accessibility and IntelliSense support

**Before you begin**: Before upgrading to the new version, review the article for any controls you’ve used in your app and update any impacted formulas.

## Identifying controls that need updates

When you open an app that uses the previous version of a modern control, you see a notification on the control indicating that an update is available. The notification includes:

- A message indicating this is the previous version of the control
- A **Learn more** link that directs you to the update documentation for that control
- An **Update** button (when available) that upgrades the control to the new version

**Before updating a control:**
1. Select the **Learn more** link to read the update guide for that specific control.
1. Review the enum changes, property renames, and behavioral differences.
1. Identify any formulas in your app that reference renamed or removed properties.
1. Update your formulas according to the update guide.
1. Select the **Update** button to upgrade the control.
1. Test your app thoroughly after updating.

> [!NOTE]
> The **Update** button might not be available for all controls immediately. When available, it appears alongside the **Learn more** link in the control notification.

## Controls with available updates

| Control | Update guide | Key changes |
|---------|----------------|-------------|
| Text | [Updates to Text control](modern-control-text.md#recent-updates) | Nine property renames, enum values, new OnSelect event, DisplayMode removed |
| Number Input | [Updates to Number Input](modern-control-number-input.md#recent-updates) | OnChange on blur plus step clicks, TriggerOutput removed, new styling properties |
| Date Picker | [Updates to Date Picker](modern-control-date-picker.md#recent-updates) | View mode fixed, format honored, DateTimeZone respected, gallery crash fixed |
| Text Input | [Updates to Text Input](modern-control-text-input.md#recent-updates) | OnChange on focus out only, TriggerOutput default = Keypress, View mode truly read-only |
| Tab List | [Updates to Tab List](modern-control-tabs-or-tabs-list.md#recent-updates) | New Appearance property, item order preserved, Items auto-refresh |
| Combo Box | [Updates to Combo Box](modern-control-combobox.md#recent-updates) | SelectMultiple default = true, toggle to unselect, OnChange fires on every selection |
| Radio | [Updates to Radio](modern-controls-radio-group.md#recent-updates) | Item order preserved, View mode read-only (not disabled), new styling properties |
| Link | [Updates to Link](modern-control-link.md#recent-updates) | URL security validation (XSS protection), FontWeight fix, Wrap fix |
| Info Button | [Updates to Info Button](modern-control-info-button.md#recent-updates) | Content flyout expansion fixed, click reliability improved, AcceptsFocus removed |

## Property changes across modern controls

### Property renames

The following property renames apply to most or all controls:

| Old name (Previous) | New name (New) | Affected controls |
|---------------------|----------------|-------------------|
| `FontColor` | `Color` | Text, Link, Info Button, Radio, Text Input, Tab List, Number Input, Date Picker, Combo Box |
| `FontSize` | `Size` | Text, Link, Info Button, Radio, Text Input, Tab List, Number Input, Date Picker, Combo Box |
| `FontItalic` | `Italic` | Text, Link, Info Button, Radio, Text Input, Tab List, Date Picker, Combo Box |
| `FontStrikethrough` | `Strikethrough` | Text, Link, Info Button, Radio, Text Input, Date Picker, Combo Box |
| `FontUnderline` | `Underline` | Text, Link, Info Button, Radio, Text Input, Date Picker, Combo Box |
| `Weight` | `FontWeight` | Text only |
| `BorderRadius` | `RadiusTopLeft`, `RadiusTopRight`, `RadiusBottomLeft`, `RadiusBottomRight` | All controls with borders |

### New enum patterns

Many properties that previously accepted plain string values now use typed enum syntax. This change affects formulas that hardcode these values. Control-specific enum details are covered in each control's update guide.

By using enum syntax instead of string literals, you get IntelliSense support, compile-time validation, and localization safety in your Power Fx formulas.

#### Align

**Used by:** Text, Text Input, Number Input, Link, Tab List, Date Picker, Combo Box

| Enum value | Description |
|------------|-------------|
| `Align.Left` | Aligns text to the left edge |
| `Align.Center` | Centers text horizontally |
| `Align.Right` | Aligns text to the right edge |
| `Align.Justify` | Stretches text to fill the full width (Text, Link only) |

The previous string values `"Start"` or `""` (empty string) map to `Align.Left`. The previous value `"End"` maps to `Align.Right`.

#### VerticalAlign

**Used by:** Text, Link

| Enum value | Description |
|------------|-------------|
| `VerticalAlign.Top` | Aligns text to the top of the control |
| `VerticalAlign.Middle` | Centers text vertically (default) |
| `VerticalAlign.Bottom` | Aligns text to the bottom of the control |

The previous Text control defaulted to `""` (empty/undefined). The new default is `VerticalAlign.Middle`.

#### FontWeight

**Used by:** Text, Text Input, Number Input, Link, Tab List, Radio, Combo Box, Date Picker, Info Button

| Enum value | Description |
|------------|-------------|
| `FontWeight.Bold` | Bold weight |
| `FontWeight.Semibold` | Semibold weight |
| `FontWeight.Normal` | Normal/regular weight (default) |
| `FontWeight.Lighter` | Lighter weight |

> [!IMPORTANT]
> **FontWeight.Medium removed**: The `Medium` value isn't available in the new controls. If your previous control used `FontWeight.Medium`, it automatically maps to `FontWeight.Normal` during the update.

The previous Text control property was named `Weight` with string values (`"Regular"`, `"Bold"`, and so on). The new property is `FontWeight` with enum values. Both the property name and the value format changed.

#### ValidationState

**Used by:** Date Picker, Text Input, Number Input, Combo Box, Radio

| Enum value | Description |
|------------|-------------|
| `ValidationState.None` | No validation styling (default) |
| `ValidationState.Error` | Shows error styling (red border) |

> [!NOTE]
> Only two values are available: `None` and `Error`. There's no `Valid` or `Success` state.

#### Appearance

**Used by:** Date Picker, Text Input, Number Input, Combo Box

| Enum value | Description |
|------------|-------------|
| `Appearance.Filled` | Filled background style |
| `Appearance.FilledDarker` | Darker filled background (default for most controls) |
| `Appearance.Outline` | Outlined border with transparent background |


#### BorderStyle

**Used by:** Text, Text Input, Number Input, Date Picker, Combo Box, Tab List, Link, Radio

| Enum value | Description |
|------------|-------------|
| `BorderStyle.Solid` | Solid line border (default) |
| `BorderStyle.Dashed` | Dashed line border |
| `BorderStyle.Dotted` | Dotted line border |
| `BorderStyle.None` | No border |

### BorderRadius split into corner-specific properties

Controls that previously had a single **BorderRadius** property now have four separate properties for each corner:

```
// Previous version
Control.BorderRadius = 8

// New version
Control.RadiusTopLeft = 8
Control.RadiusTopRight = 8
Control.RadiusBottomLeft = 8
Control.RadiusBottomRight = 8
```

This change gives you more flexibility to create controls with different corner radii, such as rounded top corners only.

### OnChange behavior improvements

Several controls updated the **OnChange** event behavior to fire at more appropriate times:

| Control | Previous OnChange | New OnChange | Impact |
|---------|------------------|--------------|--------|
| Text Input | Every keystroke | Focus out (blur) only | **CRITICAL** - Major performance improvement, might require formula updates |
| Number Input | Every keystroke | Focus out + step button clicks | Major performance improvement |
| Combo Box | Delayed/Focus out | Every selection/deselection | More responsive interaction |
| Radio | Sometimes inconsistent | Every selection reliably | Improved reliability |

**Tip:** For controls where OnChange no longer fires on every keystroke, reference the control's output property (such as `TextInput1.Text`) directly in other formulas if you need immediate per-keystroke updates.

### TriggerOutput changes

For controls with a **TriggerOutput** property:

| Control | Change | Impact |
|---------|--------|--------|
| Text Input | Default changed from **FocusOut** to **Keypress** | Text updates immediately on keystroke (Delayed in forms) |
| Number Input | **TriggerOutput** property removed entirely | No longer available |
| Combo Box | No longer fires OnChange | TriggerOutput and OnChange are now independent |
| Text Input | No longer fires OnChange | TriggerOutput and OnChange are now independent |


### Improved mobile defaults

Updated controls now ship with mobile-optimized defaults when you add them to a mobile layout canvas. These defaults include:

- Larger widths and heights for easier touch interaction
- Larger font sizes (typically 24pt for mobile)
- Appropriate padding and spacing

### Updated command bar and right-click menus

Updated controls have updated command bar menus and right-click floatie menus in the authoring experience. They provide quick access to the most commonly used style properties:

- Font and font size
- Font color
- Background color (Fill)
- Alignment
- Border properties

## See also

- [Modern controls overview](overview-modern-controls.md)
- Individual control update guides (see table in the section above)
