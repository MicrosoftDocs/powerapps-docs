---
title: Migrate to the Text Input modern control - Power Apps
description: Learn about the differences between the previous Text Input modern control and the new Text Input modern control, and how to update your formulas.
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

# Migrate to the Text Input modern control

This article describes the breaking changes, property renames, and behavioral differences between the previous Text Input modern control and the new Text Input modern control. Use this guide to update your apps when adopting the new control.

> [!IMPORTANT]
> Apps using the previous version of the Text Input modern control require formula updates if they reference any of the renamed or removed properties listed below. Formulas that reference old property names will produce errors after migration.

## Summary of changes

| Change type | Count |
|-------------|-------|
| Properties renamed | 6 |
| Properties added | 2 |
| Value format changed to enum | 4 |
| Properties moved between sections | Most design properties |
| Bug fixes and behavioral changes | 8 major improvements |

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
| `Default` | Text | The initial text displayed when the control first loads |
| `OnSelect` | Action | Event that fires when the user clicks or taps in the control |

### Enum format changes

Four properties that previously accepted string values now require enum syntax. Update any hardcoded string values in your formulas.

| Property | Old format (Previous) | New format (New) |
|----------|----------------------|------------------|
| `Appearance` | `"FilledDarker"` | `Appearance.FilledDarker` |
| `Align` | `""` (empty string) | `Align.Left` |
| `Type` | `"Text"` | `TextInputType.Text` |
| `ValidationState` | `"None"` | `ValidationState.None` |

**Appearance enum values:**

| Old string | New enum |
|------------|----------|
| `"Filled"` | `Appearance.Filled` |
| `"FilledDarker"` | `Appearance.FilledDarker` |
| `"Outline"` | `Appearance.Outline` |

**Align enum values:**

| Old string | New enum |
|------------|----------|
| `""` or `"Left"` | `Align.Left` |
| `"Center"` | `Align.Center` |
| `"Right"` | `Align.Right` |

**TextInputType enum values:**

| Old string | New enum |
|------------|----------|
| `"Text"` | `TextInputType.Text` |
| `"Multiline"` | `TextInputType.Multiline` |
| `"Password"` | `TextInputType.Password` |
| `"Search"` | `TextInputType.Search` |

**ValidationState enum values:**

| Old string | New enum |
|------------|----------|
| `"None"` | `ValidationState.None` |
| `"Error"` | `ValidationState.Error` |

## Behavioral changes and improvements

The new version includes significant behavioral changes and bug fixes:

### 1. OnChange fires on focus out only (CRITICAL CHANGE)

**Previous behavior:** The **OnChange** event fired on every keystroke as the user typed, which could cause performance issues with complex formulas.

**New behavior:** The **OnChange** event fires only when the user moves focus away from the control (on blur/focus out).

**Migration:**
- **Action required:** Review all **OnChange** formulas
- This change dramatically improves performance and prevents issues with rapid formula execution
- If you need per-keystroke updates, use **TriggerOutput** set to **OnKeypress** and reference the **Text** property directly
- Most apps will benefit from this change without modifications

**Example:**
```
// This formula now runs on blur, not every keystroke
OnChange = Patch(
    Customers,
    LookUp(Customers, ID = varCustomerID),
    {Name: NameInput.Text}
)

// If you need immediate updates, use the Text property directly
SearchResults = Filter(Products, TextInput1.Text in ProductName)
```

### 2. TriggerOutput default changed (IMPORTANT)

**Previous behavior:** **TriggerOutput** defaulted to **FocusOut**, meaning the **Text** output property updated only when focus left the control.

**New behavior:** **TriggerOutput** now defaults to **OnKeypress** for immediate updates. When the control is added to a form, it automatically changes to **Delayed** for better form performance.

**Migration:**
- **Action required if you relied on FocusOut behavior:** Explicitly set `TriggerOutput = TriggerOutput.OnBlur`
- Test formulas that reference the **Text** property to ensure timing is correct
- Forms will automatically use **Delayed** mode

**Example:**
```
// If you need the old FocusOut behavior explicitly
TextInput1.TriggerOutput = TriggerOutput.OnBlur

// Default is now OnKeypress (immediate updates)
// No setting needed for immediate updates
```

### 3. TriggerOutput no longer fires OnChange

**Previous behavior:** Calling or setting **TriggerOutput** would also trigger the **OnChange** event.

**New behavior:** **TriggerOutput** controls when the **Text** output updates but does not trigger **OnChange**.

**Migration:**
- **OnChange** and **TriggerOutput** are now independent
- If you relied on **TriggerOutput** triggering **OnChange**, update your logic to call OnChange actions explicitly

### 4. DisplayMode.View is now truly read-only

**Previous behavior (bug):** Setting `DisplayMode = DisplayMode.View` did not prevent editing. Users could still type and modify the text.

**New behavior (fixed):** When `DisplayMode = DisplayMode.View`, the control is truly read-only. Text is displayed but cannot be edited.

**Migration:** No action needed. This is a bug fix. Verify that read-only forms work as expected.

### 5. Null values return empty string

**Previous behavior (bug):** Null or blank values in the **Text** property would return `null`, causing errors in formulas.

**New behavior (fixed):** Blank or null values now properly return an empty string `""`.

**Migration:** Remove workarounds for null handling:

```
// Old workaround - no longer needed
If(IsBlank(TextInput1.Text) || TextInput1.Text = null, "", TextInput1.Text)

// New - Text property never returns null
TextInput1.Text
```

### 6. Password preview works correctly

**Previous behavior (bug):** Password fields showed actual characters in preview/edit mode, making it hard to design secure forms.

**New behavior (fixed):** Password fields show masked characters (***) even in preview mode.

**Migration:** No action needed. This is a visual improvement for designing password fields.

### 7. Multiline overflow fixed

**Previous behavior (bug):** Multi-line text areas had overflow issues when users pressed Enter to create new lines. Text could disappear or display incorrectly.

**New behavior (fixed):** Multi-line text now handles line breaks correctly without overflow.

**Migration:** No action needed. This is a bug fix.

### 8. OnChange doesn't fire on tab-through

**Previous behavior (bug):** **OnChange** would fire when users tabbed through fields without making changes, causing unnecessary formula execution.

**New behavior (fixed):** **OnChange** only fires when the text actually changes.

**Migration:** No action needed. This improves performance and prevents false-positive triggers.

### 9. Border rendering improved

**Previous behavior (bug):** Borders were cut off or rendered incorrectly when control height was less than 32 pixels.

**New behavior (fixed):** Borders now render correctly at small heights (though minimum 32px is still recommended).

**Migration:** No action needed. This is a bug fix.

### 10. Color palette override works

**Previous behavior (bug):** Setting **BasePaletteColor** in the property panel didn't override the global theme color.

**New behavior (fixed):** **BasePaletteColor** now properly overrides global theme settings.

**Migration:** No action needed. Verify that theme colors display as expected.

## Default value changes

The following default values have changed between versions.

| Property | Previous default | New default | Impact |
|----------|------------------|-------------|--------|
| `Placeholder` | Varies | "Enter text" | May show different hint text |
| `TriggerOutput` | FocusOut | OnKeypress | Text updates immediately on keystroke (Delayed in forms) |
| `Width` | 320 | 320 | No change |
| `Height` | 32 | 32 | No change |

## Property section reorganization

In the previous version, most properties were in the **Data** section under the Advanced tab. In the new version, properties are logically split between **Action**, **Data**, and **Design** sections.

### Previous property organization (Advanced tab)

- **Action section:** OnChange
- **Data section:** AccessibleLabel, Align, Appearance, BasePaletteColor, BorderColor, BorderRadius, BorderStyle, BorderThickness, ContentLanguage, Fill, Font, FontColor, FontItalic, FontSize, FontStrikethrough, FontUnderline, FontWeight, MaxLength, Mode, Padding properties, Placeholder, Required, TriggerOutput, Type, ValidationState, Value
- **Design section:** DisplayMode, Height, Visible, Width, X, Y

### New property organization (Advanced tab)

- **Action section:** OnChange, OnSelect
- **Data section:** AccessibleLabel, ContentLanguage, Default, MaxLength, Placeholder, Required, TriggerOutput, Type, ValidationState
- **Design section:** Align, Appearance, BasePaletteColor, BorderColor, BorderStyle, BorderThickness, Color, DisplayMode, Fill, Font, FontWeight, Height, Italic, Padding properties, Radius properties, Size, Strikethrough, Underline, Visible, Width, X, Y

This reorganization does not affect runtime behavior but makes properties easier to find in the authoring panel.

## Migration checklist

Use this checklist when migrating an app from the previous Text Input control to the new version:

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
- `Align = ""` → `Align = Align.Left`
- `Type = "Text"` → `Type = TextInputType.Text`
- `ValidationState = "None"` → `ValidationState = ValidationState.None`

### 3. Review OnChange logic (CRITICAL)

**OnChange** now fires on blur, not every keystroke:

- Review all **OnChange** formulas to ensure this timing works for your app
- For immediate per-keystroke updates, use **Text** property directly in other formulas
- Test that validations and calculations work correctly with the new timing

```
// OnChange runs on blur
OnChange = Patch(...)

// For immediate updates, reference Text directly
FilteredList = Filter(Data, TextInput1.Text in Title)
```

### 4. Adjust TriggerOutput if needed

If you relied on **FocusOut** behavior:

```
// Explicitly set to OnBlur for old FocusOut behavior
TextInput1.TriggerOutput = TriggerOutput.OnBlur

// Default is now OnKeypress (immediate)
// Forms automatically use Delayed
```

### 5. Remove null handling workarounds

Text property never returns null anymore:

```
// Remove this type of workaround
If(IsBlank(TextInput1.Text) || TextInput1.Text = null, "", TextInput1.Text)

// Just use the Text property directly
TextInput1.Text
```

### 6. Use Default property

Set initial values with **Default** instead of **OnVisible**:

```
// Better approach with Default property
TextInput1.Default = varInitialValue

// Old approach (still works, but Default is cleaner)
Screen1.OnVisible = Set(varInitialValue, "Default text")
```

### 7. Test DisplayMode.View

Verify that read-only forms work correctly:
- **View** mode is now truly read-only (bug fixed)
- Confirm users cannot edit text in View mode

### 8. Test multiline inputs

If you use **TextInputType.Multiline**:
- Test that line breaks work correctly
- Verify no overflow issues when pressing Enter

### 9. Verify theme colors

Check that **BasePaletteColor** applies correctly (bug was fixed).

## Examples

### Example 1: Update font properties

**Previous version:**
```
TextInput1.FontColor = Color.Black
TextInput1.FontSize = 14
TextInput1.FontItalic = false
```

**New version:**
```
TextInput1.Color = Color.Black
TextInput1.Size = 14
TextInput1.Italic = false
```

### Example 2: OnChange behavior change

**Previous version (fired on every keystroke):**
```
// This caused performance issues
OnChange = Patch(
    Customers,
    LookUp(Customers, ID = varCustomerID),
    {
        Email: EmailInput.Text,
        LastModified: Now()
    }
)
```

**New version (fires on blur):**
```
// This now runs only when user leaves field - much better performance
OnChange = Patch(
    Customers,
    LookUp(Customers, ID = varCustomerID),
    {
        Email: EmailInput.Text,
        LastModified: Now()
    }
)

// For immediate filtering, reference Text directly
FilteredCustomers = Filter(Customers, SearchInput.Text in CustomerName)
```

### Example 3: TriggerOutput default change

**Previous version (default was FocusOut):**
```
// Default behavior - Text updated on focus out
// No TriggerOutput setting needed
```

**New version (default is OnKeypress):**
```
// Default is now OnKeypress - immediate updates
// If you want the old FocusOut behavior:
TextInput1.TriggerOutput = TriggerOutput.OnBlur
```

### Example 4: Remove null handling

**Previous version (workaround for null bug):**
```
// Had to handle null values
If(IsBlank(TextInput1.Text) || TextInput1.Text = null,
    "",
    TextInput1.Text
)
```

**New version (bug fixed):**
```
// Text property never returns null
TextInput1.Text
```

### Example 5: Use Default property

**Previous version:**
```
// Set initial value in screen's OnVisible
Screen1.OnVisible = Set(varCustomerName, "John Doe")
TextInput1.Value = varCustomerName
```

**New version:**
```
// Use Default property directly
TextInput1.Default = "John Doe"
```

### Example 6: Type with enum

**Previous version:**
```
// String-based type
TextInput1.Type = "Password"
```

**New version:**
```
// Enum-based type
TextInput1.Type = TextInputType.Password
```

## See also

- [Text Input modern control reference](text-input-reference.md)
- [Modern controls overview](overview-modern-controls.md)
- [New enum patterns in modern controls](../new-enums-reference.md)
