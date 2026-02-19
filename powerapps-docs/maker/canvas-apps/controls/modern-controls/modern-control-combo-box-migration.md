---
title: Migrate to the Combo box modern control - Power Apps
description: Learn about the differences between the earlier earlier Combo box modern control and the updated updated Combo box modern control, and how to update your formulas.
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

# Migrate to the Combo box modern control

This article describes the breaking changes, property renames, and behavioral differences between the earlier earlier Combo box modern control and the updated updated Combo box modern control. Use this guide to update your apps when adopting the new control.

> [!IMPORTANT]
> Apps using the earlier version of the Combo box modern control require formula updates if they reference any of the renamed or removed properties listed below. Formulas that reference old property names will produce errors after migration.

## Summary of changes

| Change type | Count |
|-------------|-------|
| Properties renamed | 6 |
| Properties removed | 2 |
| Value format changed to enum | 2 |
| Properties moved between sections | Most design properties |
| New properties added | 3 (DelayOutput, ItemDisplayText, TabIndex) |
| Default value changes | 1 critical (SelectMultiple) |
| Behavioral changes | 5 major |

## Breaking changes

### Property renames

The following properties have been renamed. Any formula in your app that reads from or writes to these properties must be updated.

| Old name (Previous) | New name (New) | Impact |
|----------------|-------------------|--------|
| `FontColor` | `Color` | Formula references need update |
| `FontSize` | `Size` | Formula references need update |
| `FontItalic` | `Italic` | Formula references need update |
| `FontStrikethrough` | `Strikethrough` | Formula references need update |
| `FontUnderline` | `Underline` | Formula references need update |
| `BorderRadius` | `RadiusTopLeft`, `RadiusTopRight`, `RadiusBottomLeft`, `RadiusBottomRight` | Single property split into four corner-specific properties |

> [!NOTE]
> **FontWeight** enum value change: If your Previous control used `FontWeight.Medium`, it will automatically map to `FontWeight.Normal` in the updated version. The `Medium` value is not available in the updated control.

### Enum format changes

Two properties that previously accepted string values now require enum syntax. Update any hardcoded string values in your formulas.

| Property | Old format (Previous) | New format (New) |
|----------|-----------------|---------------------|
| `Appearance` | `"FilledDarker"` | `Appearance.FilledDarker` |
| `ValidationState` | `"None"` | `ValidationState.None` |

**Appearance enum values:**

| Old string | New enum |
|------------|----------|
| `"Filled"` | `Appearance.Filled` |
| `"FilledDarker"` | `Appearance.FilledDarker` |
| `"Outline"` | `Appearance.Outline` |

**ValidationState enum values:**

| Old string | New enum |
|------------|----------|
| `"None"` | `ValidationState.None` |
| `"Error"` | `ValidationState.Error` |

### Removed properties

The following properties have been removed from the control and are no longer available.

| Property | Was in Previous | Notes |
|----------|------------|-------|
| `TriggerOutput` | Advanced > Data | Removed. Use the new **DelayOutput** property instead. `TriggerOutput = "Keypress"` is equivalent to `DelayOutput = false`. |
| `Fields` | Advanced > Data | Removed. Use the **ItemDisplayText** formula property instead for more flexibility. Example: `ItemDisplayText = ThisItem.DisplayName`. |

If your app references `TriggerOutput` or `Fields` in formulas, you must update them using the new properties.

### New properties

The updated version introduces new properties that were not available in the Previous version:

| Property | Type | Description |
|----------|------|-------------|
| `DelayOutput` | Boolean | When `true`, delays the **OnChange** event until focus leaves the control. When `false`, fires immediately on each selection (default). Replaces **TriggerOutput**. |
| `ItemDisplayText` | Formula | A formula that determines what text to display for each item. Use `ThisItem` to reference fields. Replaces the **Fields** property. |
| `TabIndex` | Number | Controls the tab order for keyboard navigation. |

## Critical default value change

### SelectMultiple default changed from false to true

**This is the most significant breaking change.**

| Property | Previous default | New default | Impact |
|----------|-------------|----------------|--------|
| `SelectMultiple` | `false` | `true` | **CRITICAL**: Users can now select multiple items by default. If your app logic expects single selection only, you must explicitly set `SelectMultiple = false`. |

**Action required:** Review all combo box controls in your app. If you need single-selection behavior, explicitly set:

```
SelectMultiple = false
```

### Other default changes

| Property | Previous default | New default | Impact |
|----------|-------------|----------------|--------|
| `Width` | 320 | 320 | No change |
| `Height` | 32 | 32 | No change |
| `Size` (was `FontSize`) | 14 | 14 | No change (property renamed but value unchanged) |

## Behavioral changes

The updated version includes several significant behavioral changes that affect how the control works:

### 1. OnChange fires immediately

**Previous behavior:** The **OnChange** event timing was controlled by the **TriggerOutput** property. Setting it to `"Keypress"` fired on every keystroke, while other options delayed the event.

**New behavior:** By default, **OnChange** now fires immediately on every selection or deselection. This enables real-time dependent dropdowns and filtering.

**Migration:** If you need the previous delayed behavior, set `DelayOutput = true`.

### 2. Toggle selection behavior

**Previous behavior:** Clicking an already-selected item did nothing. Users had to clear the selection using the X button or by selecting a different item.

**New behavior:** Clicking a selected item now unselects it (toggle behavior). This makes it easier to remove selections, especially in multi-select scenarios.

**Migration:** No action needed. This is a usability improvement that shouldn't break existing logic, but be aware that users can now toggle selections by clicking.

### 3. Search text clears on selection

**Previous behavior:** Search text remained in the input field after selecting an item, requiring manual clearing.

**New behavior:** When an item is selected, the search text automatically clears, showing the selected item(s) instead.

**Migration:** If your app logic depends on retaining the search text after selection, you may need to adjust your formulas.

### 4. Reset() includes SearchText

**Previous behavior:** The `Reset()` function cleared the selection but did not clear the search text.

**New behavior:** The `Reset()` function now clears both the selection **and** the search text.

**Migration:** No action needed unless your app logic specifically relied on `Reset()` leaving the search text intact.

### 5. TriggerOutput removed

**Previous behavior:** The **TriggerOutput** property controlled when output properties updated and when **OnChange** fired. Options included `"Keypress"`, `"FocusOut"`, and others.

**New behavior:** **TriggerOutput** is removed. The new **DelayOutput** boolean property controls output timing:
- `DelayOutput = false` (default) → Fires immediately (like `TriggerOutput = "Keypress"`)
- `DelayOutput = true` → Fires on focus out (like `TriggerOutput = "FocusOut"`)

**Migration:** Replace `TriggerOutput` references:

| Old Previous formula | New New formula |
|----------------|-------------------|
| `TriggerOutput = "Keypress"` | `DelayOutput = false` |
| `TriggerOutput = "FocusOut"` | `DelayOutput = true` |

## Property section reorganization

In the Previous version, most properties were in the **Data** section under the Advanced tab. In the updated version, properties are split between **Data** and **Design** sections.

### Previous property organization (Advanced tab)

- **Data section:** Most properties including styling (Font, FontColor, Fill, Border properties, Padding, etc.)
- **Design section:** DisplayMode, Height, Visible, Width, X, Y

### New property organization (Advanced tab)

- **Data section:** OnChange, AccessibleLabel, ContentLanguage, DefaultSelectedItems, DelayOutput, InputTextPlaceholder, IsSearchable, ItemDisplayText, Items, MultiValueDelimiter, Required, SelectMultiple, ValidationState
- **Design section:** Appearance, BasePaletteColor, BorderColor, BorderStyle, BorderThickness, Color, DisplayMode, Fill, Font, FontWeight, Height, Italic, Padding properties, Radius properties, Size, Strikethrough, TabIndex, Underline, ValidationState (also appears here), Visible, Width, X, Y

This reorganization does not affect runtime behavior but changes where you find properties in the authoring panel.

## ItemDisplayText replaces Fields

### Previous: Fields property

The **Fields** property was a simple way to specify which field to display:

```
Fields = ["DisplayName"]
```

### New: ItemDisplayText formula

The **ItemDisplayText** property accepts a Power Fx formula for more flexibility:

```
ItemDisplayText = ThisItem.DisplayName
```

Or combine multiple fields:

```
ItemDisplayText = ThisItem.FirstName & " " & ThisItem.LastName
```

**Migration:** Replace `Fields = ["FieldName"]` with `ItemDisplayText = ThisItem.FieldName`.

## Known issues and limitations

The updated version resolves many issues from the Previous version but has some known limitations:

### Resolved in updated version
- ✅ 800-item limit significantly improved
- ✅ Many-to-One Dataverse relationships now work correctly
- ✅ Hidden combo boxes no longer lose values on `SubmitForm()`
- ✅ Search works correctly with dynamic `Filter()` patterns
- ✅ Input field updates immediately after selecting a searched item
- ✅ Text properly respects control dimensions (no clipping)
- ✅ SearchField visibility in data panel fixed

### Still open in updated version
- ⚠️ Chevron and checkbox icons don't scale with font size
- ⚠️ Dropdown may appear at top of page in custom pages (z-index issue)
- ⚠️ SharePoint Person columns may not work correctly in some scenarios

## Migration checklist

Use this checklist when migrating an app from the Previous Combo box control to the updated version:

### 1. Update property names

Search for and replace these property names in formulas:

- `FontColor` → `Color`
- `FontSize` → `Size`
- `FontItalic` → `Italic`
- `FontStrikethrough` → `Strikethrough`
- `FontUnderline` → `Underline`
- `BorderRadius` → Use `RadiusTopLeft`, `RadiusTopRight`, `RadiusBottomLeft`, `RadiusBottomRight` instead

### 2. Update enum values

Replace string values with enum syntax:

- `Appearance = "FilledDarker"` → `Appearance = Appearance.FilledDarker`
- `ValidationState = "None"` → `ValidationState = ValidationState.None`

### 3. Replace removed properties

- Replace `TriggerOutput = "Keypress"` with `DelayOutput = false`
- Replace `TriggerOutput = "FocusOut"` with `DelayOutput = true`
- Replace `Fields = ["FieldName"]` with `ItemDisplayText = ThisItem.FieldName`

### 4. **CRITICAL: Set SelectMultiple if needed**

For every combo box that should only allow single selection:

```
SelectMultiple = false
```

**Do not skip this step!** The default changed from `false` to `true`.

### 5. Review OnChange logic

- If your **OnChange** logic expects delayed firing, add `DelayOutput = true`
- If your logic expects only single-selection, ensure `SelectMultiple = false`
- Test that the immediate firing of **OnChange** doesn't cause performance issues with large datasets

### 6. Test toggle behavior

Verify that users clicking selected items to unselect them doesn't break your app logic.

### 7. Review Reset() calls

If your app uses `Reset()`, verify that clearing the search text along with the selection doesn't cause issues.

### 8. Test with your data

- Test with your actual data sources, especially Dataverse tables
- Verify performance with large lists (1000+ items)
- Test search functionality with various filter patterns

### 9. Accessibility testing

The new **TabIndex** property improves keyboard navigation. Test that the tab order works correctly with your form layout.

## Examples

### Example 1: Single-selection combo box (most common migration)

**Previous version:**
```
// Properties
SelectMultiple = false  // Explicitly set (but was default)
TriggerOutput = "FocusOut"
Fields = ["Title"]
```

**New version:**
```
// Properties
SelectMultiple = false  // MUST explicitly set (no longer default)
DelayOutput = true      // Replaces TriggerOutput = "FocusOut"
ItemDisplayText = ThisItem.Title  // Replaces Fields
```

### Example 2: Multi-select with immediate firing

**Previous version:**
```
// Properties
SelectMultiple = true
TriggerOutput = "Keypress"
OnChange = Filter(DetailItems, Category in ComboBox1.SelectedItems.Category)
```

**New version:**
```
// Properties
SelectMultiple = true  // Now the default, but explicit is better
DelayOutput = false    // Now the default (immediate firing)
OnChange = Filter(DetailItems, Category in ComboBox1.SelectedItems.Category)
```

### Example 3: Custom display text

**Previous version:**
```
Fields = ["DisplayName"]
```

**New version:**
```
ItemDisplayText = ThisItem.DisplayName & " (" & ThisItem.Code & ")"
```

## See also

- [Combo box modern control reference](combo-box-reference.md)
- [Modern controls overview](overview-modern-controls.md)
- [New enum patterns in modern controls](../new-enums-reference.md)
