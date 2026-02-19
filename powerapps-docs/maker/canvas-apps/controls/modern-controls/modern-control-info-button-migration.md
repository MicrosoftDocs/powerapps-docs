---
title: Migrate to the Info button modern control - Power Apps
description: Learn about the differences between the previous Info button modern control and the new Info button modern control, and how to update your formulas.
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

# Migrate to the Info button modern control

This article describes the breaking changes, property renames, and behavioral differences between the previous Info button modern control and the new Info button modern control. Use this guide to update your apps when adopting the new control.

> [!IMPORTANT]
> Apps using the previous version of the Info button modern control require formula updates if they reference any of the renamed or removed properties listed below. Formulas that reference old property names will produce errors after migration.

## Summary of changes

| Change type | Count |
|-------------|-------|
| Properties renamed | 5 |
| Properties removed | 1 |
| Properties moved between sections | Most design properties |
| Bug fixes | 2 major behavioral fixes |

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

> [!NOTE]
> **FontWeight** enum value change: If your previous control used `FontWeight.Medium`, it will automatically map to `FontWeight.Normal` in the new version. The `Medium` value is not available in the new control.

### Removed properties

The following property has been removed from the control and is no longer available.

| Property | Was in Previous | Notes |
|----------|-----------------|-------|
| `AcceptsFocus` | Advanced > Data | Removed. The control now automatically manages focus behavior for accessibility. This property is no longer needed. |

If your app references `AcceptsFocus` in formulas, remove those references. The control handles focus automatically.

## Behavioral changes

The new version includes significant bug fixes that improve reliability:

### 1. Content flyout properly expands

**Previous behavior (bug):** The information flyout background did not always expand to fit the content. Long text could be clipped or overflow the flyout boundaries.

**New behavior (fixed):** The flyout background now properly expands to accommodate all content, regardless of text length. Multi-line text displays correctly without clipping.

**Migration:** No action needed. This is a bug fix that improves user experience. If you previously limited content length to work around this issue, you can now use longer text if needed.

### 2. Click reliability improved

**Previous behavior (bug):** Clicking the info button sometimes caused intermittent crashes, especially when used in galleries or containers.

**New behavior (fixed):** The control now handles clicks reliably in all scenarios without crashes.

**Migration:** No action needed. This is a bug fix that improves stability.

## Property section reorganization

In the previous version, most properties were in the **Data** section under the Advanced tab. In the new version, properties are logically split between **Data** and **Design** sections.

### Previous property organization (Advanced tab)

- **Data section:** AcceptsFocus, AccessibleLabel, BasePaletteColor, Content, ContentLanguage, Font, FontColor, FontItalic, FontSize, FontStrikethrough, FontUnderline, FontWeight, IconColor, Padding properties
- **Design section:** DisplayMode, Height, Visible, Width, X, Y

### New property organization (Advanced tab)

- **Data section:** OnSelect, AccessibleLabel, Content, ContentLanguage
- **Design section:** BasePaletteColor, Color, DisplayMode, Font, FontWeight, Height, IconColor, Italic, Padding properties, Size, Strikethrough, Underline, Visible, Width, X, Y

This reorganization does not affect runtime behavior but makes properties easier to find in the authoring panel. Design-related properties are now grouped together in the **Design** section.

## Default value changes

The following default values remain unchanged between versions.

| Property | Previous default | New default | Impact |
|----------|------------------|-------------|--------|
| `Width` | 32 | 32 | No change |
| `Height` | 32 | 32 | No change |
| `Size` (was `FontSize`) | 15 | 15 | No change (property renamed but value unchanged) |
| `Padding` (all sides) | 0 | 0 | No change |

## Migration checklist

Use this checklist when migrating an app from the previous Info button control to the new version:

### 1. Update property names

Search for and replace these property names in formulas:

- `FontColor` → `Color`
- `FontSize` → `Size`
- `FontItalic` → `Italic`
- `FontStrikethrough` → `Strikethrough`
- `FontUnderline` → `Underline`

### 2. Remove AcceptsFocus references

If your app references the **AcceptsFocus** property:

```
// Remove this type of code
If(InfoButton1.AcceptsFocus, ...)

// The control now handles focus automatically
```

### 3. Review content length

Since the flyout now properly expands to fit content:
- You can remove workarounds that limited content length
- Consider adding more detailed help text if appropriate
- Test that longer content displays correctly in your app's layout

### 4. Test in galleries and containers

If you previously avoided using info buttons in galleries or containers due to crashes:
- Add info buttons where they provide value
- Test clicking in all scenarios to verify stability

### 5. Verify icon color consistency

Since styling properties have been reorganized:
- Check that **IconColor** displays as expected
- Verify color formulas still work correctly
- Test theme color inheritance with **BasePaletteColor**

## Examples

### Example 1: Update font property references

**Previous version:**
```
InfoButton1.FontColor = Color.Blue
InfoButton1.FontSize = 14
InfoButton1.FontItalic = true
```

**New version:**
```
InfoButton1.Color = Color.Blue
InfoButton1.Size = 14
InfoButton1.Italic = true
```

### Example 2: Remove AcceptsFocus logic

**Previous version:**
```
// Custom focus management
If(InfoButton1.AcceptsFocus,
    Set(varHelpAvailable, true),
    Set(varHelpAvailable, false)
)
```

**New version:**
```
// AcceptsFocus removed - control manages focus automatically
// Remove this logic entirely or use OnSelect instead
InfoButton1.OnSelect = Set(varHelpViewed, true)
```

### Example 3: Expanded content usage

**Previous version (workaround for clipping bug):**
```
// Limited content to prevent clipping
Content = "Email info..."
```

**New version (bug fixed):**
```
// Can now use full content without clipping
Content = "We'll use this email to send you:
• Order confirmations
• Shipping updates
• Account notifications
• Special offers

Your email is never shared with third parties."
```

## See also

- [Info button modern control reference](info-button-reference.md)
- [Modern controls overview](overview-modern-controls.md)
- [New enum patterns in modern controls](../new-enums-reference.md)
