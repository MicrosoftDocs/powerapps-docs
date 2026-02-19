---
title: Migrate to the Link modern control - Power Apps
description: Learn about the differences between the previous Link modern control and the new Link modern control, and how to update your formulas.
author: yogeshgupta698
ms.topic: reference
ms.custom: canvas
ms.date: 02/18/2026
ms.subservice: canvas-maker
ms.author: yogupt
ms.reviewer: mkaur
search.audienceType:
  - maker
---

# Migrate to the Link modern control

This article describes the breaking changes, property renames, and behavioral differences between the previous Link modern control and the new Link modern control. Use this guide to update your apps when adopting the new control.

> [!IMPORTANT]
> Apps using the previous version of the Link modern control require formula updates if they reference any of the renamed or removed properties listed below. Formulas that reference old property names will produce errors after migration.

## Summary of changes

| Change type | Count |
|-------------|-------|
| Properties renamed | 10 |
| Properties removed | 1 |
| Value format changed to enum | 4 |
| Properties moved between sections | Most design properties |
| Bug fixes and security | 5 major improvements |

## Breaking changes

### Property renames

The following properties have been renamed. Any formula in your app that reads from or writes to these properties must be updated.

| Old name (Previous) | New name (New) | Impact |
|---------------------|----------------|--------|
| `FontColor` | `Color` | Formula references need update |
| `FontSize` | `Size` | Formula references need update |
| `FontItalic` | `Italic` | Formula references need update |
| `FontStrikethrough` | `Strikethrough` | Formula references need update |
| `FontUnderline` | `Underline` | Formula references need update |
| `URL` | `Url` | Formula references need update (case change) |
| `Appearance` | `Type` | Formula references need update + value format changed |
| `BorderRadius` | `RadiusTopLeft`, `RadiusTopRight`, `RadiusBottomLeft`, `RadiusBottomRight` | Single property split into four corner-specific properties |
| `BorderRadiusTopLeft` | `RadiusTopLeft` | Prefix "Border" removed |
| `BorderRadiusTopRight` | `RadiusTopRight` | Prefix "Border" removed |
| `BorderRadiusBottomLeft` | `RadiusBottomLeft` | Prefix "Border" removed |
| `BorderRadiusBottomRight` | `RadiusBottomRight` | Prefix "Border" removed |

> [!NOTE]
> **FontWeight** enum value change: If your previous control used `FontWeight.Medium`, it will automatically map to `FontWeight.Normal` in the new version. The `Medium` value is not available in the new control.

### Enum format changes

Four properties that previously accepted string values now require enum syntax. Update any hardcoded string values in your formulas.

| Property | Old format (Previous) | New format (New) |
|----------|----------------------|------------------|
| `Appearance` / `Type` | `"Default"` | `LinkAppearance.Default` |
| `Align` | `""` (empty string) | `Align.Left` |
| `VerticalAlign` | `""` (empty string) | `VerticalAlign.Middle` |

**LinkAppearance enum values (Type property):**

| Old string | New enum |
|------------|----------|
| `"Default"` | `LinkAppearance.Default` |
| `"Subtle"` | `LinkAppearance.Subtle` |

**Align enum values:**

| Old string | New enum |
|------------|----------|
| `"Start"` or `""` | `Align.Left` |
| `"Center"` | `Align.Center` |
| `"End"` | `Align.Right` |
| `"Justify"` | `Align.Justify` |

**VerticalAlign enum values:**

| Old string | New enum |
|------------|----------|
| `"Top"` | `VerticalAlign.Top` |
| `""` or `"Middle"` | `VerticalAlign.Middle` |
| `"Bottom"` | `VerticalAlign.Bottom` |

### Removed properties

The following property has been removed from the control and is no longer available.

| Property | Was in Previous | Notes |
|----------|-----------------|-------|
| `AcceptsFocus` | Advanced > Data | Removed. The control now automatically manages focus behavior for accessibility. This property is no longer needed. |

If your app references `AcceptsFocus` in formulas, remove those references.

## Behavioral changes and improvements

The new version includes significant bug fixes and security enhancements:

### 1. URL security validation (CRITICAL SECURITY FIX)

**Previous behavior (security vulnerability):** The **URL** property did not validate or sanitize URLs, allowing potentially malicious `javascript:` URIs and other unsafe protocols that could execute code or create XSS vulnerabilities.

**New behavior (security fix):** The **Url** property now validates and sanitizes URLs to prevent XSS injection attacks. URLs using `javascript:` or other unsafe protocols are blocked and will not navigate.

**Migration:**
- **Action required:** Review all **Url** formulas in your app
- Ensure URLs use standard `https://` or `http://` protocols
- Remove any `javascript:` URIs (these are security risks and will no longer work)
- Test all links after migration

**Example of blocked URL:**
```
// This will NOT work in new version (security risk)
Url = "javascript:alert('XSS')"

// Use standard URLs instead
Url = "https://company.com/page"
```

### 2. Font weight now applies correctly

**Previous behavior (bug):** Changes to the **FontWeight** property were not reflected visually. Links appeared with the default font weight regardless of the property value.

**New behavior (fixed):** The **FontWeight** property now correctly applies bold, semibold, normal, and lighter weights to link text.

**Migration:** No action needed. This is a bug fix. If you previously used workarounds or avoided using **FontWeight**, you can now use it normally.

### 3. Wrap property works correctly

**Previous behavior (bug):** The **Wrap** property did not correctly change text wrapping behavior. Text might wrap or not wrap regardless of the property setting.

**New behavior (fixed):** The **Wrap** property now correctly controls whether text wraps to multiple lines (`true`) or stays on a single line (`false`).

**Migration:** No action needed. This is a bug fix. Verify that your links display as expected with current **Wrap** settings.

### 4. URL preview in edit mode

**Previous behavior (bug):** When placing the cursor on a link control in edit mode, the URL was not displayed, making it difficult to verify link destinations.

**New behavior (fixed):** The URL now displays when you hover over or focus on the link control in edit mode.

**Migration:** No action needed. This is a usability improvement.

### 5. Alt+Click to open links in editor

**Previous behavior:** Alt+Click on a link in edit mode did not open the URL in a browser.

**New behavior (new feature):** Alt+Click on a link in edit mode now opens the URL in your default browser, allowing you to test links without leaving the editor.

**Migration:** No action needed. This is a new convenience feature for app development.

## Default value changes

The following default values have changed between versions.

| Property | Previous default | New default | Impact |
|----------|------------------|-------------|--------|
| `Width` | 320 | 150 | Links may appear narrower |
| `Padding` (all sides) | varies | 5 | Consistent padding around text |
| `Align` | `""` (undefined) | `Align.Left` | Explicitly left-aligned |
| `VerticalAlign` | `""` (undefined) | `VerticalAlign.Middle` | Centered vertically |

## Property section reorganization

In the previous version, most properties were in the **Data** section under the Advanced tab. In the new version, properties are logically split between **Data** and **Design** sections.

### Previous property organization (Advanced tab)

- **Data section:** AcceptsFocus, AccessibleLabel, Align, Appearance, AutoHeight, BasePaletteColor, BorderColor, BorderRadius properties, BorderStyle, BorderThickness, ContentLanguage, Fill, Font, FontColor, FontItalic, FontSize, FontStrikethrough, FontUnderline, FontWeight, Padding properties, Text, URL, VerticalAlign, Wrap
- **Design section:** DisplayMode, Height, Visible, Width, X, Y

### New property organization (Advanced tab)

- **Data section:** AccessibleLabel, ContentLanguage, Text, Url
- **Design section:** Align, AutoHeight, BasePaletteColor, BorderColor, BorderStyle, BorderThickness, Color, DisplayMode, Fill, Font, FontWeight, Height, Italic, Padding properties, Radius properties, Size, Strikethrough, Type, Underline, VerticalAlign, Visible, Width, Wrap, X, Y

This reorganization does not affect runtime behavior but makes properties easier to find in the authoring panel.

## Migration checklist

Use this checklist when migrating an app from the previous Link control to the new version:

### 1. **CRITICAL: Review URL security**

Check all **URL** / **Url** property formulas:
- Ensure URLs use `https://` or `http://` protocols
- Remove any `javascript:` URIs (security risks)
- Remove any data URIs or other unsafe protocols
- Test all links after migration

### 2. Update property names

Search for and replace these property names in formulas:

- `FontColor` → `Color`
- `FontSize` → `Size`
- `FontItalic` → `Italic`
- `FontStrikethrough` → `Strikethrough`
- `FontUnderline` → `Underline`
- `URL` → `Url` (case change)
- `Appearance` → `Type`
- `BorderRadius` → Use `RadiusTopLeft`, `RadiusTopRight`, `RadiusBottomLeft`, `RadiusBottomRight` instead
- `BorderRadiusTopLeft` → `RadiusTopLeft`
- `BorderRadiusTopRight` → `RadiusTopRight`
- `BorderRadiusBottomLeft` → `RadiusBottomLeft`
- `BorderRadiusBottomRight` → `RadiusBottomRight`

### 3. Update enum values

Replace string values with enum syntax:

- `Appearance = "Default"` → `Type = LinkAppearance.Default`
- `Appearance = "Subtle"` → `Type = LinkAppearance.Subtle`
- `Align = ""` → `Align = Align.Left`
- `VerticalAlign = ""` → `VerticalAlign = VerticalAlign.Middle`

### 4. Remove AcceptsFocus references

Remove any formulas that reference the **AcceptsFocus** property:

```
// Remove this type of code
If(Link1.AcceptsFocus, ...)
```

### 5. Review layout

- Default **Width** changed from 320 to 150 — adjust if links appear too narrow
- All **Padding** properties now default to 5 — verify spacing looks correct

### 6. Test font weight and wrap

- Test that **FontWeight** settings display correctly (bug was fixed)
- Verify **Wrap** behavior matches expectations (bug was fixed)

### 7. Test all links

- Click every link to verify navigation works correctly
- Ensure no `javascript:` URIs were used (these are blocked)
- Test Alt+Click in edit mode to verify URL preview

## Examples

### Example 1: Update appearance and URL

**Previous version:**
```
Link1.Appearance = "Default"
Link1.URL = "https://example.com"
Link1.FontColor = Color.Blue
Link1.FontSize = 16
```

**New version:**
```
Link1.Type = LinkAppearance.Default
Link1.Url = "https://example.com"
Link1.Color = Color.Blue
Link1.Size = 16
```

### Example 2: Security fix - remove javascript: URI

**Previous version (SECURITY RISK):**
```
// DO NOT USE - Security vulnerability!
Link1.URL = "javascript:void(0)"
```

**New version (secure approach):**
```
// Use OnSelect for custom behavior instead of javascript: URIs
Link1.Url = ""  // Leave blank if no navigation needed
Link1.OnSelect = Set(varCustomAction, true)

// Or use a standard URL
Link1.Url = "https://company.com/action"
```

### Example 3: Dynamic link with enum

**Previous version:**
```
Link1.Appearance = If(varPremium, "Default", "Subtle")
Link1.Align = If(varRTL, "End", "Start")
```

**New version:**
```
Link1.Type = If(varPremium, LinkAppearance.Default, LinkAppearance.Subtle)
Link1.Align = If(varRTL, Align.Right, Align.Left)
```

### Example 4: Remove AcceptsFocus logic

**Previous version:**
```
If(Link1.AcceptsFocus,
    Set(varLinkFocusable, true),
    Set(varLinkFocusable, false)
)
```

**New version:**
```
// AcceptsFocus removed - control manages focus automatically
// Remove this logic entirely or use OnSelect for interaction tracking
Link1.OnSelect = Set(varLinkClicked, true)
```

## See also

- [Link modern control reference](link-reference.md)
- [Modern controls overview](overview-modern-controls.md)
- [New enum patterns in modern controls](../new-enums-reference.md)
