---
title: Migrate to the Text modern control - Power Apps
description: Learn about the differences between the earlier earlier Text modern control and the updated updated Text modern control, and how to update your formulas.
author: yogeshgupta698
ms.topic: reference
ms.custom: canvas
ms.date: 02/17/2026
ms.subservice: canvas-maker
ms.author: yogupt
ms.reviewer: mkaur
search.audienceType:
  - maker
---

# Migrate to the Text modern control

This article describes the breaking changes, property renames, and behavioral differences between the earlier earlier Text modern control and the updated updated Text modern control. Use this guide to update your apps when adopting the new control.

> [!IMPORTANT]
> Apps using the earlier version of the Text modern control require formula updates if they reference any of the renamed or removed properties listed below. Formulas that reference old property names will produce errors after migration.

## Summary of changes

| Change type | Count |
|-------------|-------|
| Properties renamed | 9 |
| Properties with no effect (not removed) | 2 |
| Value format changed to enum | 3 |
| Properties moved between sections | Most design properties |
| New properties added | 1 (OnSelect) |

## Breaking changes

### Property renames

The following properties have been renamed. Any formula in your app that reads from or writes to these properties must be updated.

| Old name (Previous) | New name (New) | Impact |
|----------------|-------------------|--------|
| `FontColor` | `Color` | Formula references need update |
| `FontItalic` | `Italic` | Formula references need update |
| `FontStrikethrough` | `Strikethrough` | Formula references need update |
| `FontUnderline` | `Underline` | Formula references need update |
| `Weight` | `FontWeight` | Formula references need update + value format changed |
| `BorderRadiusTopLeft` | `RadiusTopLeft` | Formula references need update |
| `BorderRadiusTopRight` | `RadiusTopRight` | Formula references need update |
| `BorderRadiusBottomLeft` | `RadiusBottomLeft` | Formula references need update |
| `BorderRadiusBottomRight` | `RadiusBottomRight` | Formula references need update |

### Enum format changes

Three properties that previously accepted string values now require enum syntax. Update any hardcoded string values in your formulas.

| Property | Old format (Previous) | New format (New) |
|----------|-----------------|---------------------|
| `Align` | `"Start"` | `Align.Left` |
| `VerticalAlign` | `""` (empty string) | `VerticalAlign.Middle` |
| `FontWeight` (was `Weight`) | `"Regular"` | `FontWeight.Normal` |

**Additional `Align` enum values:**

| Old string | New enum |
|------------|----------|
| `"Start"` | `Align.Left` |
| `"Center"` | `Align.Center` |
| `"End"` | `Align.Right` |
| `"Justify"` | `Align.Justify` |

**Additional `VerticalAlign` enum values:**

| Old string | New enum |
|------------|----------|
| `"Top"` | `VerticalAlign.Top` |
| `""` or `"Middle"` | `VerticalAlign.Middle` |
| `"Bottom"` | `VerticalAlign.Bottom` |

**Additional `FontWeight` enum values:**

| Old string | New enum |
|------------|----------|
| `"Regular"` | `FontWeight.Normal` |
| `"Bold"` | `FontWeight.Bold` |
| `"Semibold"` | `FontWeight.Semibold` |
| `"Medium"` | `FontWeight.Normal` (Medium maps to Normal in updated version) |
| `"Lighter"` | `FontWeight.Lighter` |

### Properties with no effect

The following properties are no longer visible in the property panel and have no effect in the new control. They remain available programmatically for backward compatibility, so existing formulas won't break.

| Property | Was in Previous | Notes |
|----------|------------|-------|
| `DisplayMode` | Advanced > Design | Not shown in property panel. Has no effect in the new control. The Text control is display-only; interactive behavior is handled via the new **OnSelect** event. |
| `ContentLanguage` | Advanced > Data | Not shown in property panel. Has no effect in the new control. Language is inherited from the app settings. |

Existing formulas that reference these properties will continue to work without errors, but the properties have no impact on the control's behavior.

## Default value changes

The following default values have changed between the Previous and updated versions.

| Property | Previous default | New default | Impact |
|----------|-------------|----------------|--------|
| `Width` | 96 | 150 | Controls may appear wider |
| `VerticalAlign` | `""` (undefined) | `VerticalAlign.Middle` | Text vertical position changes |
| `Align` | `"Start"` | `Align.Left` | Functionally equivalent |
| `FontWeight` (was `Weight`) | `"Regular"` | `FontWeight.Normal` | Functionally equivalent |
| `Size` (font size) | 14 | 15 | Slightly larger text |
| `PaddingTop/Bottom/Left/Right` | 5 | 5 | No change |

## Property section reorganization

In the Previous version, properties were split between **Data** and **Design** sections in the Advanced panel. In the updated version, almost all properties have moved to the **Design** section.

| Section | Previous | New |
|---------|-----|--------|
| **Data** | 21 properties (Text, Align, BorderRadius\*, BorderColor, BorderStyle, BorderThickness, Fill, Font, FontColor, FontItalic, FontStrikethrough, FontUnderline, Padding\*, Size, VerticalAlign, Weight, Wrap, ContentLanguage) | 1 property (Text only) |
| **Design** | 6 properties (DisplayMode, Height, Visible, Width, X, Y) | 26 properties (all styling and layout) |

This reorganization does not affect runtime behavior or formulas, but changes where you find properties in the authoring panel.

## New capabilities

The updated version of the Text control introduces the following new functionality:

### OnSelect event

The new **OnSelect** event allows you to trigger actions when a user clicks or taps the text. This enables use of the Text control as a lightweight interactive element without needing a separate Button control.

The event is fully accessible:
- Keyboard users can trigger it with **Enter** or **Space** when the control has focus.
- Screen readers announce the control as interactive when **OnSelect** is set.

Example:
```
// Navigate when text is selected
OnSelect = Navigate(DetailScreen, ScreenTransition.Fade)
```

## Migration checklist

Use this checklist when migrating an app from the Previous Text control to the updated version:

1. **Search for renamed properties** in the formula bar and replace them:
   - `FontColor` → `Color`
   - `FontItalic` → `Italic`
   - `FontStrikethrough` → `Strikethrough`
   - `FontUnderline` → `Underline`
   - `Weight` → `FontWeight`
   - `BorderRadiusTopLeft` → `RadiusTopLeft`
   - `BorderRadiusTopRight` → `RadiusTopRight`
   - `BorderRadiusBottomLeft` → `RadiusBottomLeft`
   - `BorderRadiusBottomRight` → `RadiusBottomRight`

2. **Update enum string values:**
   - Replace `"Start"` with `Align.Left` in `Align` formulas
   - Replace `""` or `"Top"` with `VerticalAlign.Middle` or `VerticalAlign.Top` in `VerticalAlign` formulas
   - Replace `"Regular"` with `FontWeight.Normal` in `FontWeight` formulas

3. **Review properties with no effect:**
   - `DisplayMode` and `ContentLanguage` still exist programmatically but have no effect in the new control
   - Existing formulas won't break, but these properties don't impact the control's behavior
   - Not visible in property panel

4. **Review layout:**
   - Default `Width` changed from 96 to 150 — check controls that relied on the narrower default
   - Default `VerticalAlign` is now `Middle` — review text vertical positioning in your UI

5. **Test screen readers:** The **OnSelect** event makes the control focusable. Verify screen reader announcements if you've added **OnSelect**.

## See also

- [Text modern control reference](text-reference.md)
- [Modern controls overview](overview-modern-controls.md)
- [New enum patterns in modern controls](../new-enums-reference.md)
