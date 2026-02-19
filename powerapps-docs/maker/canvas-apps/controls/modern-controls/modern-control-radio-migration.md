---
title: Migrate to the Radio modern control - Power Apps
description: Learn about the differences between the previous Radio modern control and the new Radio modern control, and how to update your formulas.
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

# Migrate to the Radio modern control

This article describes the breaking changes, property renames, and behavioral differences between the previous Radio modern control and the new Radio modern control. Use this guide to update your apps when adopting the new control.

> [!IMPORTANT]
> Apps using the previous version of the Radio modern control require formula updates if they reference any of the renamed or removed properties listed below. Formulas that reference old property names will produce errors after migration.

## Summary of changes

| Change type | Count |
|-------------|-------|
| Properties renamed | 6 |
| Properties added | 8 |
| Properties moved between sections | Most design properties |
| Bug fixes and behavioral improvements | 10 major fixes |

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
| `BorderRadius` | `RadiusTopLeft`, `RadiusTopRight`, `RadiusBottomLeft`, `RadiusBottomRight` | Single property split into four corner-specific properties |

> [!NOTE]
> **FontWeight** enum value change: If your previous control used `FontWeight.Medium`, it will automatically map to `FontWeight.Normal` in the new version. The `Medium` value is not available in the new control.

### New properties

The new version introduces properties that were not available in the previous version:

| Property | Type | Description |
|----------|------|-------------|
| `Default` | Item | The item selected by default when the control loads |
| `HoverColor` | Color | Text color when user hovers over an option |
| `PressedColor` | Color | Text color when user clicks an option |
| `DisabledColor` | Color | Text color when control is disabled |
| `RadioSize` | Number | Size of the radio button circles in pixels |
| `RadioBackgroundFill` | Color | Background fill color of radio button circles |
| `RadioBorderColor` | Color | Border color of radio button circles |
| `RadioSelectionFill` | Color | Fill color when a radio button is selected |
| `LineHeight` | Number | Spacing between radio button options |

## Behavioral changes and improvements

The new version includes significant bug fixes and behavioral improvements:

### 1. Item order now preserved (IMPORTANT)

**Previous behavior (bug):** The order of items in the **Items** property was sometimes ignored or reordered unexpectedly, making it difficult to control the display sequence of options.

**New behavior (fixed):** The **Items** property now preserves the order of items exactly as specified in your formula. Options display in the same sequence as the data source.

**Migration:**
- Verify that your item order is correct in the **Items** source
- If you previously worked around this bug by reordering data or using sort formulas, you can remove those workarounds
- Test that options appear in the expected sequence

**Example:**
```
// This now displays in exact order: Small, Medium, Large, Extra Large
Items = ["Small", "Medium", "Large", "Extra Large"]

// No need for workarounds like this anymore:
// Items = SortByColumns(["Small", "Medium", "Large"], "Value", Ascending)
```

### 2. View mode appearance improved

**Previous behavior (bug):** When `DisplayMode = DisplayMode.View`, the control appeared disabled or grayed out, making it hard to read the selected value.

**New behavior (fixed):** In **View** mode, the control now displays with a proper read-only appearance that clearly shows the selected option without looking disabled.

**Migration:** No action needed. This is a visual improvement that makes read-only forms easier to read.

### 3. OnChange fires reliably

**Previous behavior (bug):** The **OnChange** event sometimes failed to fire or fired inconsistently when selections changed.

**New behavior (fixed):** **OnChange** now fires immediately and reliably every time the user selects a different option.

**Migration:** No action needed. This is a reliability fix. If you had workarounds for missed OnChange events, you can remove them.

### 4. Gallery selection fixed

**Previous behavior (bug):** Radio buttons inside galleries sometimes required a double-click to register a selection. Single clicks didn't work reliably.

**New behavior (fixed):** Radio buttons in galleries now respond correctly to single clicks.

**Migration:** No action needed. This is a bug fix that improves usability.

### 5. Scrolling works correctly

**Previous behavior (bug):** Long lists of radio options were cut off and didn't scroll, making some options inaccessible.

**New behavior (fixed):** Lists of options now scroll properly when they exceed the control's height.

**Migration:** No action needed. This is a bug fix. You may be able to remove height constraints you added to work around this issue.

### 6. Theme color respected

**Previous behavior (bug):** Setting **BasePaletteColor** didn't always apply correctly. Default colors would override the theme color.

**New behavior (fixed):** The **BasePaletteColor** property now consistently applies the chosen theme color to the control.

**Migration:** No action needed. This is a bug fix. Verify that your theme colors display as expected.

### 7. Default value matching improved

**Previous behavior (bug):** The **Default** property sometimes failed to match items from **Items**, causing errors or unexpected selections.

**New behavior (fixed):** **Default** now reliably matches items from the **Items** data source.

**Migration:** No action needed. This is a bug fix.

### 8. No extra options displayed

**Previous behavior (bug):** Changing the **Items** data source without updating **Default** could cause extra, unexpected options to appear in the list.

**New behavior (fixed):** Only the items from **Items** are displayed, with no spurious options.

**Migration:** No action needed. This is a bug fix.

### 9. Vertical spacing fixed

**Previous behavior (bug):** Vertical spacing between radio button options was inconsistent or too tight.

**New behavior (fixed):** Options are spaced consistently. Use the new **LineHeight** property to adjust spacing if needed.

**Migration:** No action needed. If spacing looks different, adjust the **LineHeight** property to your preference.

## Default value changes

The following default values have changed between versions.

| Property | Previous default | New default | Impact |
|----------|------------------|-------------|--------|
| `Width` | Varies | 360 (mobile) | May need adjustment |
| `Height` | Varies | 150 (mobile) | May need adjustment |
| `Size` (was `FontSize`) | Varies | 24 (mobile) | Font may appear larger |

## Property section reorganization

In the previous version, most properties were in the **Data** section under the Advanced tab. In the new version, properties are logically split between **Action**, **Data**, and **Design** sections.

### Previous property organization (Advanced tab)

- **Action section:** OnChange
- **Data section:** AccessibleLabel, BasePaletteColor, ContentLanguage, Font, FontColor, FontItalic, FontSize, FontStrikethrough, FontUnderline, FontWeight, Items, ItemDisplayText, Required, TriggerOutput, ValidationState
- **Design section:** DisplayMode, Height, Visible, Width, X, Y

### New property organization (Advanced tab)

- **Action section:** OnChange, OnSelect
- **Data section:** AccessibleLabel, ContentLanguage, Default, ItemDisplayText, Items, Layout, Required, TriggerOutput, ValidationState
- **Design section:** BasePaletteColor, BorderColor, BorderStyle, BorderThickness, Color, DisabledColor, DisplayMode, Fill, Font, FontWeight, Height, HoverColor, Italic, LineHeight, PaddingBottom, PaddingLeft, PaddingRight, PaddingTop, PressedColor, RadioBackgroundFill, RadioBorderColor, RadioSelectionFill, RadioSize, RadiusBottomLeft, RadiusBottomRight, RadiusTopLeft, RadiusTopRight, Size, Strikethrough, Underline, Visible, Width, X, Y

This reorganization does not affect runtime behavior but makes properties easier to find in the authoring panel.

## Migration checklist

Use this checklist when migrating an app from the previous Radio control to the new version:

### 1. Update property names

Search for and replace these property names in formulas:

- `FontColor` → `Color`
- `FontSize` → `Size`
- `FontItalic` → `Italic`
- `FontStrikethrough` → `Strikethrough`
- `FontUnderline` → `Underline`
- `BorderRadius` → Use `RadiusTopLeft`, `RadiusTopRight`, `RadiusBottomLeft`, `RadiusBottomRight` instead

### 2. Verify item order

Check that radio options display in the correct order:
- The **Items** property now preserves order exactly
- Remove any workarounds for item ordering bugs
- Test that options appear in the expected sequence

### 3. Set Default property

Use the new **Default** property to specify the initial selection:

```
// Set default selection
Radio1.Default = LookUp(Radio1.Items, ID = 1)

// Or for simple lists
Radio1.Default = "Option 1"
```

### 4. Test in View mode

Verify that read-only forms display correctly:
- **View** mode now shows selected value clearly (not grayed out)
- Confirm selections are readable in forms

### 5. Test in galleries

If you have radio buttons inside galleries:
- Verify single-click selection works (no longer requires double-click)
- Test that selections register correctly

### 6. Review OnChange logic

Verify that **OnChange** formulas work correctly:
- OnChange now fires reliably on every selection change
- Remove any workarounds for missed OnChange events

### 7. Adjust scrolling and spacing

- Remove height constraints added to work around scrolling bugs
- Use **LineHeight** property to adjust vertical spacing if needed

### 8. Add interactive colors

Take advantage of new color properties for better UX:

```
Radio1.HoverColor = Color.Blue
Radio1.PressedColor = Color.DarkBlue
Radio1.DisabledColor = Color.Gray
```

### 9. Customize radio button appearance

Use new radio styling properties:

```
Radio1.RadioSize = 20
Radio1.RadioSelectionFill = Color.Green
Radio1.RadioBorderColor = Color.DarkGreen
```

## Examples

### Example 1: Update font properties

**Previous version:**
```
Radio1.FontColor = Color.Black
Radio1.FontSize = 14
Radio1.FontItalic = false
```

**New version:**
```
Radio1.Color = Color.Black
Radio1.Size = 14
Radio1.Italic = false
```

### Example 2: Fix item ordering

**Previous version (workaround for bug):**
```
// Had to use SortByColumns to control order
Items = SortByColumns(
    Table(
        {Order: 1, Size: "Small"},
        {Order: 2, Size: "Medium"},
        {Order: 3, Size: "Large"}
    ),
    "Order"
)
```

**New version (bug fixed):**
```
// Order is now preserved automatically
Items = ["Small", "Medium", "Large"]

// Or with table
Items = Table(
    {Size: "Small"},
    {Size: "Medium"},
    {Size: "Large"}
)
```

### Example 3: Set default selection

**Previous version:**
```
// Had to use OnVisible workaround
Screen1.OnVisible = Set(varDefaultShipping, "Standard")
Radio1.Selected = LookUp(Radio1.Items, Value = varDefaultShipping)
```

**New version:**
```
// Use Default property directly
Radio1.Default = LookUp(Radio1.Items, ShippingType = "Standard")
```

### Example 4: Add hover and pressed colors

**Previous version (not available):**
```
// These properties didn't exist
```

**New version:**
```
// Add interactive colors
Radio1.HoverColor = RGBA(0, 120, 212, 1)
Radio1.PressedColor = RGBA(0, 90, 158, 1)
Radio1.RadioSelectionFill = RGBA(0, 120, 212, 1)
```

### Example 5: Adjust spacing

**Previous version (no control over spacing):**
```
// Could not control vertical spacing
```

**New version:**
```
// Use LineHeight to adjust spacing
Radio1.LineHeight = 40  // Increases space between options
```

## See also

- [Radio modern control reference](radio-reference.md)
- [Modern controls overview](overview-modern-controls.md)
- [New enum patterns in modern controls](../new-enums-reference.md)
