---
title: Migrate to the Tab List modern control - Power Apps
description: Learn about the differences between the previous Tab List modern control and the new Tab List modern control, and how to update your formulas.
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

# Migrate to the Tab List modern control

This article describes the breaking changes, property renames, and behavioral differences between the previous Tab List modern control and the new Tab List modern control. Use this guide to update your apps when adopting the new control.

> [!IMPORTANT]
> Apps using the previous version of the Tab List modern control require formula updates if they reference any of the renamed or removed properties listed below. Formulas that reference old property names will produce errors after migration.

## Summary of changes

| Change type | Count |
|-------------|-------|
| Properties renamed | 6 |
| Properties added | 2 |
| Value format changed to enum | 2 |
| Properties moved between sections | Most design properties |
| Bug fixes and improvements | 3 major fixes |

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
| `Default` | Item | The tab selected by default when the control loads |
| `Appearance` | Enum | Visual style of tabs (Transparent, Subtle, Underline, Filled) |

### Enum format changes

Two properties that previously accepted string values now require enum syntax. Update any hardcoded string values in your formulas.

| Property | Old format (Previous) | New format (New) |
|----------|----------------------|------------------|
| `Alignment` | `"Center"` | `TabListAlignment.Center` |
| `Appearance` | Not available | `TabListAppearance.Underline` |

**TabListAlignment enum values:**

| Old string | New enum |
|------------|----------|
| `"Start"` or `"Left"` | `TabListAlignment.Start` |
| `"Center"` | `TabListAlignment.Center` |
| `"End"` or `"Right"` | `TabListAlignment.End` |

**TabListAppearance enum values (NEW):**

| Value | Description |
|-------|-------------|
| `TabListAppearance.Transparent` | Transparent background with text only |
| `TabListAppearance.Subtle` | Subtle background with minimal styling |
| `TabListAppearance.Underline` | Tabs with underline indicator for selection (default) |
| `TabListAppearance.Filled` | Filled tab buttons with solid backgrounds |

## Behavioral changes and improvements

The new version includes significant bug fixes and feature additions:

### 1. Item order now preserved (IMPORTANT)

**Previous behavior (bug):** The order of tabs in the **Items** property was sometimes ignored or reordered unexpectedly. Tabs might display in a different sequence than specified.

**New behavior (fixed):** The **Items** property now preserves the order of tabs exactly as specified in your formula. Tabs display in the same sequence as the data source.

**Migration:**
- Verify that your tab order is correct in the **Items** source
- If you previously worked around this bug by reordering data or using sort formulas, you can remove those workarounds
- Test that tabs appear in the expected sequence

**Example:**
```
// This now displays in exact order: Home, Products, About, Contact
Items = ["Home", "Products", "About", "Contact"]

// No need for workarounds like this anymore:
// Items = SortByColumns(TabData, "Order", Ascending)
```

### 2. Items refresh automatically

**Previous behavior (bug):** Updating the **Items** property didn't automatically refresh the tab list. Tabs would show stale data until the screen was refreshed or navigated away and back.

**New behavior (fixed):** Changing the **Items** property now automatically updates the displayed tabs immediately.

**Migration:** No action needed. This is a bug fix. You can remove workarounds that forced screen refreshes.

### 3. Appearance property added (NEW FEATURE)

**Previous behavior:** The Tab List had limited styling options. All tab lists looked similar.

**New behavior:** The **Appearance** property allows you to choose from four visual styles: **Transparent**, **Subtle**, **Underline**, and **Filled**.

**Migration:**
- The default appearance is **Underline**
- Choose an appearance that matches your app's design
- Test that the selected appearance looks good with your color scheme

**Example:**
```
// Choose an appearance style
TabList1.Appearance = TabListAppearance.Filled

// Or make it conditional
TabList1.Appearance = If(
    varDarkMode,
    TabListAppearance.Subtle,
    TabListAppearance.Underline
)
```

## Default value changes

The following default values have changed between versions.

| Property | Previous default | New default | Impact |
|----------|------------------|-------------|--------|
| `Width` | Varies | 300 | May need adjustment |
| `Height` | Varies | 60 | May need adjustment |
| `Size` (was `FontSize`) | Varies | 15 | Font size may differ |
| `Appearance` | Not available | Underline | New visual style |

## Property section reorganization

In the previous version, most properties were in the **Data** section under the Advanced tab. In the new version, properties are logically split between **Action**, **Data**, and **Design** sections.

### Previous property organization (Advanced tab)

- **Action section:** OnChange, OnSelect
- **Data section:** AccessibleLabel, Alignment, BasePaletteColor, ContentLanguage, DefaultSelectedItems, Font, FontColor, FontItalic, FontSize, FontStrikethrough, FontUnderline, FontWeight, Items, Size
- **Design section:** DisplayMode, Height, Visible, Width, X, Y

### New property organization (Advanced tab)

- **Action section:** OnChange, OnSelect
- **Data section:** AccessibleLabel, ContentLanguage, Default, Items
- **Design section:** Align, Alignment, Appearance, BorderColor, BorderStyle, BorderThickness, Color, DisplayMode, Font, FontWeight, Height, Italic, PaddingBottom, PaddingLeft, PaddingRight, PaddingTop, RadiusBottomLeft, RadiusBottomRight, RadiusTopLeft, RadiusTopRight, Size, Strikethrough, Underline, Visible, Width, X, Y

This reorganization does not affect runtime behavior but makes properties easier to find in the authoring panel.

## Migration checklist

Use this checklist when migrating an app from the previous Tab List control to the new version:

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

- `Alignment = "Center"` → `Alignment = TabListAlignment.Center`

### 3. Verify tab order

Check that tabs display in the correct order:
- The **Items** property now preserves order exactly
- Remove any workarounds for tab ordering bugs
- Test that tabs appear in the expected sequence

### 4. Set Default property

Use the new **Default** property to specify the initial tab selection:

```
// Set default tab
TabList1.Default = "Home"

// Or with table data
TabList1.Default = LookUp(TabList1.Items, TabID = 1)
```

### 5. Choose Appearance style

Select an **Appearance** that matches your app's design:

```
// Set appearance
TabList1.Appearance = TabListAppearance.Filled

// Test different styles:
// - Transparent: minimal styling
// - Subtle: light background
// - Underline: indicator line (default)
// - Filled: solid button backgrounds
```

### 6. Test Items refresh

Verify that updating **Items** refreshes the tabs:
- Remove workarounds for refresh bugs
- Test dynamic tab lists that change based on user actions

### 7. Review conditional visibility

If you use **Selected** to control content visibility, verify it works correctly:

```
// Typical pattern
OverviewSection.Visible = TabList1.Selected.Value = "Overview"
SpecsSection.Visible = TabList1.Selected.Value = "Specifications"
```

## Examples

### Example 1: Update font properties

**Previous version:**
```
TabList1.FontColor = Color.DarkBlue
TabList1.FontSize = 16
TabList1.FontItalic = false
```

**New version:**
```
TabList1.Color = Color.DarkBlue
TabList1.Size = 16
TabList1.Italic = false
```

### Example 2: Fix tab ordering

**Previous version (workaround for bug):**
```
// Had to use SortByColumns to control order
Items = SortByColumns(
    Table(
        {Order: 1, Tab: "Home"},
        {Order: 2, Tab: "Products"},
        {Order: 3, Tab: "Contact"}
    ),
    "Order"
)
```

**New version (bug fixed):**
```
// Order is now preserved automatically
Items = ["Home", "Products", "Contact"]

// Or with table
Items = Table(
    {Tab: "Home"},
    {Tab: "Products"},
    {Tab: "Contact"}
)
```

### Example 3: Set default tab

**Previous version:**
```
// Had to use OnVisible workaround
Screen1.OnVisible = Set(varActiveTab, "Home")

// Or relied on first item being selected automatically
```

**New version:**
```
// Use Default property directly
TabList1.Default = "Home"

// Or with table data
TabList1.Default = LookUp(TabList1.Items, TabName = "Home")
```

### Example 4: Use Appearance property (NEW)

**Previous version (not available):**
```
// All tab lists looked similar
// No appearance customization
```

**New version:**
```
// Choose appearance style
TabList1.Appearance = TabListAppearance.Filled

// Conditional styling
TabList1.Appearance = If(
    varUserRole = "Admin",
    TabListAppearance.Filled,
    TabListAppearance.Underline
)
```

### Example 5: Update Alignment enum

**Previous version:**
```
// String-based alignment
TabList1.Alignment = "Center"
```

**New version:**
```
// Enum-based alignment
TabList1.Alignment = TabListAlignment.Center
```

### Example 6: Dynamic tabs with auto-refresh

**Previous version (required workarounds):**
```
// Items didn't refresh automatically
// Had to navigate away and back or use Reset()
Items = colUserTabs

// Workaround to force refresh
OnVisible = Reset(TabList1)
```

**New version (auto-refresh works):**
```
// Items refresh automatically when collection changes
Items = colUserTabs

// No workarounds needed
// Update collection and tabs update immediately
OnSelect = ClearCollect(colUserTabs, Filter(AllTabs, UserRole = varRole))
```

## See also

- [Tab List modern control reference](tab-list-reference.md)
- [Modern controls overview](overview-modern-controls.md)
- [New enum patterns in modern controls](../new-enums-reference.md)
