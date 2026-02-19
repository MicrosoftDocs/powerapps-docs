---
title: Migrate to the Date picker modern control - Power Apps
description: Learn about the differences between the earlier earlier Date picker modern control and the updated updated Date picker modern control, and how to update your formulas.
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

# Migrate to the Date picker modern control

This article describes the breaking changes, property renames, and behavioral differences between the earlier earlier Date picker modern control and the updated updated Date picker modern control. Use this guide to update your apps when adopting the new control.

> [!IMPORTANT]
> Apps using the earlier version of the Date picker modern control require formula updates if they reference any of the renamed or removed properties listed below. Formulas that reference old property names will produce errors after migration.

## Summary of changes

| Change type | Count |
|-------------|-------|
| Properties renamed | 5 |
| Properties removed | 1 |
| Value format changed to enum | 5 |
| Properties moved between sections | Most design properties |
| New properties added | 1 (DefaultDate) |
| Bug fixes | 8 major behavioral fixes |

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

Five properties that previously accepted string values now require enum syntax. Update any hardcoded string values in your formulas.

| Property | Old format (Previous) | New format (New) |
|----------|-----------------|---------------------|
| `Appearance` | `"FilledDarker"` | `Appearance.FilledDarker` |
| `DateTimeZone` | `"Local"` | `DateTimeZone.Local` |
| `Format` | `"Long Abbreviated"` | `DatePickerFormat.LongAbbreviated` |
| `StartOfWeek` | `"Sunday"` | `StartOfWeek.Sunday` |
| `ValidationState` | `"None"` | `ValidationState.None` |

**Appearance enum values:**

| Old string | New enum |
|------------|----------|
| `"Filled"` | `Appearance.Filled` |
| `"FilledDarker"` | `Appearance.FilledDarker` |
| `"Outline"` | `Appearance.Outline` |

**DateTimeZone enum values:**

| Old string | New enum |
|------------|----------|
| `"Local"` | `DateTimeZone.Local` |
| `"UTC"` | `DateTimeZone.UTC` |

**Format enum values:**

| Old string | New enum |
|------------|----------|
| `"Long Abbreviated"` | `DatePickerFormat.LongAbbreviated` |
| `"Short"` | `DatePickerFormat.Short` |
| `"Long"` | `DatePickerFormat.Long` |

**StartOfWeek enum values:**

| Old string | New enum |
|------------|----------|
| `"Sunday"` | `StartOfWeek.Sunday` |
| `"Monday"` | `StartOfWeek.Monday` |
| `"Tuesday"` | `StartOfWeek.Tuesday` |
| `"Wednesday"` | `StartOfWeek.Wednesday` |
| `"Thursday"` | `StartOfWeek.Thursday` |
| `"Friday"` | `StartOfWeek.Friday` |
| `"Saturday"` | `StartOfWeek.Saturday` |

**ValidationState enum values:**

| Old string | New enum |
|------------|----------|
| `"None"` | `ValidationState.None` |
| `"Error"` | `ValidationState.Error` |

### Removed properties

The following property has been removed from the control and is no longer available.

| Property | Was in Previous | Notes |
|----------|------------|-------|
| `Required` | Output property | Removed from updated version. Use custom validation with **ValidationState** property instead to implement required field logic. |

If your app references `Required` in formulas, you must implement custom validation logic.

### New properties

The updated version introduces a new property that was not available in the Previous version:

| Property | Type | Description |
|----------|------|-------------|
| `DefaultDate` | Date | The initial date selected when the control first loads. Use this to set a default value before user interaction. |

## Behavioral changes

The updated version includes several significant bug fixes that change how the control behaves:

### 1. DisplayMode.View now properly enforced

**Previous behavior (bug):** Setting `DisplayMode = DisplayMode.View` did not properly disable the control. Users could still open the calendar and select dates.

**New behavior (fixed):** When `DisplayMode = DisplayMode.View`, the control is properly read-only. The selected date is displayed, but the calendar cannot be opened.

**Migration:** This is a bug fix, not a breaking change. However, if your app relied on the buggy behavior, you may need to adjust your logic. Use `DisplayMode.Edit` if you want users to be able to select dates.

### 2. Format property fully honored

**Previous behavior (bug):** Certain **Format** property values were ignored until another property changed. Format changes sometimes did not reflect immediately.

**New behavior (fixed):** All **Format** values are immediately applied when changed.

**Migration:** No action needed. This is a bug fix that improves user experience.

### 3. DateTimeZone respected

**Previous behavior (bug):** The **DateTimeZone** property value was sometimes ignored, causing dates to display in an unexpected timezone.

**New behavior (fixed):** The **DateTimeZone** property now consistently applies the correct timezone for date display and storage.

**Migration:** Verify that your date calculations account for the timezone setting. If your app previously worked around this bug, you may need to remove workarounds.

### 4. Blank value in View mode

**Previous behavior (bug):** When the control was in **View** mode with a blank value, it sometimes showed a previous value instead of remaining blank.

**New behavior (fixed):** Blank values display correctly in **View** mode.

**Migration:** No action needed. This is a bug fix.

### 5. Selected date persistence

**Previous behavior (bug):** Selected date label sometimes disappeared when navigating away from the screen and returning.

**New behavior (fixed):** Selected date persists correctly across navigation.

**Migration:** No action needed. This is a bug fix.

### 6. Gallery and data card stability

**Previous behavior (bug):** Adding the date picker to a gallery or data card sometimes caused crashes.

**New behavior (fixed):** Date picker works reliably in galleries and data cards.

**Migration:** No action needed. This is a bug fix.

### 7. Calendar positioning

**Previous behavior (bug):** Month/Year selector flyout could go off-screen on smaller displays.

**New behavior (fixed):** Flyout positioning is improved to stay within screen boundaries.

**Migration:** No action needed. This is a bug fix.

### 8. Color palette inheritance

**Previous behavior (bug):** Setting **BasePaletteColor** did not properly apply to the calendar flyout.

**New behavior (fixed):** Calendar flyout now properly inherits the color palette.

**Migration:** No action needed. This is a bug fix.

## Property section reorganization

In the Previous version, most properties were in the **Data** section under the Advanced tab. In the updated version, properties are split between **Data** and **Design** sections.

### Previous property organization (Advanced tab)

- **Data section:** AccessibleLabel, Appearance, BasePaletteColor, BorderColor, BorderRadius, BorderStyle, BorderThickness, ContentLanguage, DateTimeZone, EndDate, Fill, Font, FontColor, FontItalic, FontSize, FontStrikethrough, FontUnderline, FontWeight, Format, IsEditable, Padding properties, Placeholder, SelectedDate, StartDate, StartOfWeek, ValidationState
- **Design section:** DisplayMode, Height, Visible, Width, X, Y

### New property organization (Advanced tab)

- **Data section:** OnChange, AccessibleLabel, ContentLanguage, DateTimeZone, DefaultDate, EndDate, Format, IsEditable, Placeholder, StartDate, StartOfWeek, ValidationState
- **Design section:** Appearance, BasePaletteColor, BorderColor, BorderStyle, BorderThickness, Color, DisplayMode, Fill, Font, FontWeight, Height, Italic, Padding properties, Radius properties, Size, Strikethrough, Underline, Visible, Width, X, Y

This reorganization does not affect runtime behavior but changes where you find properties in the authoring panel.

## Implementing Required field validation

Since the **Required** property is removed in the updated version, use the **ValidationState** property to implement required field validation.

### Previous approach (no longer available):

```
// Required property was an output
If(DatePicker1.Required And IsBlank(DatePicker1.SelectedDate),
    Notify("Date is required", NotificationType.Error)
)
```

### New approach (use ValidationState):

```
// Set ValidationState property on the control
DatePicker1.ValidationState = If(
    IsBlank(DatePicker1.SelectedDate),
    ValidationState.Error,
    ValidationState.None
)

// In form submission logic
If(DatePicker1.ValidationState = ValidationState.Error,
    Notify("Please select a date", NotificationType.Error),
    // Submit form
    SubmitForm(Form1)
)
```

## Default value changes

The following default values have changed between the Previous and updated versions.

| Property | Previous default | New default | Impact |
|----------|-------------|----------------|--------|
| `Width` | 320 | 320 | No change |
| `Height` | 32 | 32 | No change |
| `Size` (was `FontSize`) | 0 | 0 | No change |
| `Placeholder` | "Select a date..." | "Select a date" | Minor text difference |

## Migration checklist

Use this checklist when migrating an app from the Previous Date picker control to the updated version:

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
- `DateTimeZone = "Local"` → `DateTimeZone = DateTimeZone.Local`
- `Format = "Long Abbreviated"` → `Format = DatePickerFormat.LongAbbreviated`
- `StartOfWeek = "Sunday"` → `StartOfWeek = StartOfWeek.Sunday`
- `ValidationState = "None"` → `ValidationState = ValidationState.None`

### 3. Replace Required property logic

Replace any references to the **Required** property with custom validation using **ValidationState**:

```
// Old Previous code
If(DatePicker1.Required And IsBlank(DatePicker1.SelectedDate), ...)

// New New code
DatePicker1.ValidationState = If(IsBlank(DatePicker1.SelectedDate), ValidationState.Error, ValidationState.None)
```

### 4. Review DisplayMode usage

Verify that controls using `DisplayMode = DisplayMode.View` should truly be read-only. In Previous, this mode was buggy and still allowed editing. In updated, it properly prevents editing.

### 5. Test DateTimeZone behavior

If your app uses **DateTimeZone** property:
- Test that dates display in the correct timezone
- Remove any workarounds for the Previous timezone bug
- Verify date calculations work with the correct timezone

### 6. Test in galleries and data cards

If you previously avoided using date pickers in galleries or data cards due to crashes, test that they now work reliably.

### 7. Verify format changes

Test that **Format** property changes reflect immediately. Remove any workarounds that forced format updates.

### 8. Use DefaultDate for initial values

If you need to set an initial date, use the new **DefaultDate** property instead of setting **SelectedDate** in OnVisible:

```
// Better approach with DefaultDate
DatePicker1.DefaultDate = Today()

// Old approach (still works, but DefaultDate is cleaner)
Screen1.OnVisible = Set(varInitialDate, Today()); Patch(...)
```

### 9. Mobile testing

Test the control on mobile devices to verify the calendar flyout is properly sized and positioned.

## Examples

### Example 1: Date range with validation

**Previous version:**
```
// Date picker properties
DateTimeZone = "Local"
Format = "Long Abbreviated"
```

**New version:**
```
// Date picker properties
DateTimeZone = DateTimeZone.Local
Format = DatePickerFormat.LongAbbreviated
DefaultDate = Today()
ValidationState = If(IsBlank(SelectedDate), ValidationState.Error, ValidationState.None)
```

### Example 2: Required field validation

**Previous version (using Required output):**
```
// Form submission
If(DatePicker1.Required And IsBlank(DatePicker1.SelectedDate),
    Notify("Date is required"),
    SubmitForm(Form1)
)
```

**New version (using ValidationState):**
```
// Set on DatePicker control
ValidationState = If(IsBlank(SelectedDate), ValidationState.Error, ValidationState.None)

// Form submission
If(DatePicker1.ValidationState = ValidationState.Error,
    Notify("Date is required"),
    SubmitForm(Form1)
)
```

## See also

- [Date picker modern control reference](date-picker-reference.md)
- [Modern controls overview](overview-modern-controls.md)
- [New enum patterns in modern controls](../new-enums-reference.md)
