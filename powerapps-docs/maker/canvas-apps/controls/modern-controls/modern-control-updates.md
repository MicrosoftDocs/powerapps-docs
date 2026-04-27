---
title: Recent modern control updates in canvas apps - Power Apps
description: Learn about recent updates to modern controls in Power Apps canvas apps, what changed, and how to update your existing apps.
author: yogeshgupta698
ms.topic: overview
ms.custom: canvas
ms.date: 04/20/2026
ms.subservice: canvas-maker
ms.author: yogupt
ms.reviewer: mkaur
search.audienceType:
  - maker
---

# Recent updates to modern controls in canvas apps

Starting February 2026, modern controls in canvas apps have updated versions with new property names, enum-based values, and behavior changes. This article explains what changed and how to update your existing apps.

> [!IMPORTANT]
> These updates might require you to update formulas in your existing apps. Before you update any control, review the update guide for that control and fix any affected formulas.

## Why update?

- **Better performance** — Events like OnChange fire less often, reducing unnecessary recalculations.
- **Better mobile experience** — Controls use touch-friendly sizes and font defaults on mobile layouts.
- **More styling options** — Separate corner radius properties and new border styles give you more design control.
- **IntelliSense and validation** — Enum-based values replace plain strings, so you get autocomplete and compile-time checks in your formulas.


## Find and update controls in your app

When you open an app that uses an older version of a modern control, you see a notification on the control. The notification tells you that an update is available, and includes a **Learn more** link and an **Update** button.
 
:::image type="content" source="media/modern-controls-updates-1.png" alt-text="Screenshot of a modern control showing an update notification with Learn more and Update options.":::

### Steps to update a control

1. Select **Learn more** to open the update guide for that control.
1. Review property renames, enum changes, and behavior differences listed in the guide.
1. Find formulas in your app that use renamed or removed properties, and update them.
1. Select **Update** to upgrade the control to the new version.
1. Test your app to make sure everything works as expected.

> [!TIP]
> The **Update** button might not appear for all controls right away. Check back if you don't see it yet.

## Controls with available updates

The following table lists each control that has an updated version, with a link to its specific update guide and a summary of what changed.

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
| Button | [Updates to Button](modern-control-button.md#recent-updates) | Six property renames, enum values for Appearance/Layout/IconStyle, new Tooltip and border properties, AcceptsFocus removed |
| Dropdown | [Updates to Dropdown control](modern-control-dropdown.md#recent-updates) | Fluent-themed flyout on desktop, DefaultSelectedItems renamed to Default, FontSize renamed to Size, enum format changes |
| Icon | [Updates to Icon control](modern-control-icon.md#recent-updates) | OnSelect support, TabIndex removed, Style renamed to IconStyle, new border and padding properties |
| Slider | [Updates to Slider](modern-control-slider.md#recent-updates) | Value renamed to Default, Layout renamed to LayoutDirection, enum values for Size and LayoutDirection, new Tooltip property |

## Property changes across modern controls

This section covers changes that affect multiple controls. If you only need to update one control, use the update guide linked in the [table above](#controls-with-available-updates).

### Property renames

Many properties were renamed for consistency across controls. If your formulas reference the old names, you need to update them to the new names:

| Old name (Previous) | New name (New) | Affected controls |
|---------------------|----------------|-------------------|
| `FontColor` | `Color` | Text, Link, Info Button, Radio, Text Input, Tab List, Number Input, Date Picker, Combo Box, Button |
| `FontSize` | `Size` | Text, Link, Info Button, Radio, Text Input, Tab List, Number Input, Date Picker, Combo Box, Button, Dropdown |
| `FontItalic` | `Italic` | Text, Link, Info Button, Radio, Text Input, Tab List, Date Picker, Combo Box, Button |
| `FontStrikethrough` | `Strikethrough` | Text, Link, Info Button, Radio, Text Input, Date Picker, Combo Box, Button |
| `FontUnderline` | `Underline` | Text, Link, Info Button, Radio, Text Input, Date Picker, Combo Box, Button |
| `Weight` | `FontWeight` | Text only |
| `BorderRadius` | `RadiusTopLeft`, `RadiusTopRight`, `RadiusBottomLeft`, `RadiusBottomRight` | All controls with borders |

### New enum patterns

Properties that previously accepted plain text strings (like `"Bold"` or `"Start"`) now require typed enum values (like `FontWeight.Bold` or `Align.Left`). If your formulas hardcode the old string values, you need to update them.

Using enums gives you IntelliSense autocomplete, compile-time validation, and localization safety in your Power Fx formulas. Each control's update guide lists the specific enum changes for that control.

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

**Used by:** Date Picker, Text Input, Number Input, Combo Box, Dropdown, Radio

| Enum value | Description |
|------------|-------------|
| `ValidationState.None` | No validation styling (default) |
| `ValidationState.Error` | Shows error styling (red border) |

> [!NOTE]
> Only two values are available: `None` and `Error`. There's no `Valid` or `Success` state.

#### Appearance

**Used by:** Date Picker, Text Input, Number Input, Combo Box, Dropdown

| Enum value | Description |
|------------|-------------|
| `Appearance.Filled` | Filled background style |
| `Appearance.FilledDarker` | Darker filled background (default for most controls) |
| `Appearance.Outline` | Outlined border with transparent background |


#### BorderStyle

**Used by:** Text, Text Input, Number Input, Date Picker, Combo Box, Tab List, Link, Radio, Icon, Dropdown

| Enum value | Description |
|------------|-------------|
| `BorderStyle.Solid` | Solid line border (default) |
| `BorderStyle.Dashed` | Dashed line border |
| `BorderStyle.Dotted` | Dotted line border |
| `BorderStyle.None` | No border |


#### IconStyle

**Used by:** Icon, Button

| Enum value | Description |
|------------|-------------|
| `IconStyle.Outline` | Renders the icon in outline (unfilled) style (default) |
| `IconStyle.Filled` | Renders the icon in filled style |

Replace the previous string values `"Outline"` and `"Filled"` with `IconStyle.Outline` and `IconStyle.Filled`.

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

Several controls changed *when* the **OnChange** event fires. This is one of the most impactful changes — if your app logic depends on OnChange, review this table:

| Control | Previous OnChange | New OnChange | Impact |
|---------|------------------|--------------|--------|
| Text Input | Every keystroke | Focus out (blur) only | **CRITICAL** - Major performance improvement, might require formula updates |
| Number Input | Every keystroke | Focus out + step button clicks | Major performance improvement |
| Combo Box | Delayed/Focus out | Every selection/deselection | More responsive interaction |
| Radio | Sometimes inconsistent | Every selection reliably | Improved reliability |

> [!TIP]
> If you need per-keystroke updates (for example, live search), reference the control's output property (such as `TextInput1.Text`) directly in your formulas instead of relying on OnChange.

### TriggerOutput changes

The **TriggerOutput** property controls when a control pushes its value to dependent formulas. Here's what changed:

| Control | Change | Impact |
|---------|--------|--------|
| Text Input | Default changed from **FocusOut** to **Keypress** | Text updates immediately on keystroke (Delayed in forms) |
| Number Input | **TriggerOutput** property removed entirely | No longer available |
| Combo Box | No longer fires OnChange | TriggerOutput and OnChange are now independent |
| Text Input | No longer fires OnChange | TriggerOutput and OnChange are now independent |


### Improved mobile defaults

When you add an updated control to a mobile layout canvas, it automatically uses touch-friendly defaults:

- Larger widths and heights for easier tapping
- Larger font sizes (typically 24 pt)
- Appropriate padding and spacing

You don't need to do anything extra — these defaults apply automatically for new controls on mobile layouts.

### Updated command bar and right-click menus

Updated controls include refreshed command bar and right-click menus in the Studio authoring experience, giving you quick access to common style properties like font, color, fill, alignment, and borders.

## See also

- [Modern controls overview](overview-modern-controls.md)
- Individual control update guides (see table in the section above)
