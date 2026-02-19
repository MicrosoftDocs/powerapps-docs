---
title: Migrate to the Number Input modern control - Power Apps
description: Learn about the differences between the previous Number Input modern control and the new Number Input modern control, and how to update your formulas.
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

# Migrate to the Number Input modern control

This article describes the breaking changes, property renames, and behavioral differences between the previous Number Input modern control and the new Number Input modern control. Use this guide to update your apps when adopting the new control.

> [!IMPORTANT]
> Apps using the previous version of the Number Input modern control require formula updates if they reference any of the renamed or removed properties listed below. Formulas that reference old property names will produce errors after migration.

## Summary of changes

| Change type | Count |
|-------------|-------|
| Properties renamed | 2 |
| Properties removed | 1 |
| Properties added | 4 |
| Value format changed to enum | 4 |
| Properties moved between sections | Most design properties |
| Bug fixes and behavioral changes | 5 major improvements |

## Breaking changes

### Property renames

The following properties have been renamed. Any formula in your app that reads from or writes to these properties must be updated.

| Old name (Previous) | New name (New) | Impact |
|---------------------|----------------|--------|
| `FontSize` | `Size` | Formula references need update |
| `BorderRadius` | `RadiusTopLeft`, `RadiusTopRight`, `RadiusBottomLeft`, `RadiusBottomRight` | Single property split into four corner-specific properties |

### New properties

The new version introduces properties that were not available in the previous version:

| Property | Type | Description |
|----------|------|-------------|
| `Default` | Number | The initial value displayed when the control first loads |
| `HintText` | Text | Placeholder text shown when the input is empty |
| `Color` | Color | Text color (this property was missing in the previous version) |
| `Fill` | Color | Background fill color |
| `Font` | Text | Font family name |

### Enum format changes

Four properties that previously accepted string values now require enum syntax. Update any hardcoded string values in your formulas.

| Property | Old format (Previous) | New format (New) |
|----------|----------------------|------------------|
| `Appearance` | `"FilledDarker"` | `Appearance.FilledDarker` |
| `Align` | `""` (empty string) | `Align.Left` |
| `Precision` | `"Auto"` or numbers | `DecimalPrecision.Auto` |
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

**DecimalPrecision enum values:**

| Old format | New enum |
|------------|----------|
| `"Auto"` or not set | `DecimalPrecision.Auto` |
| `0` | `DecimalPrecision.Zero` |
| `1` | `DecimalPrecision.One` |
| `2` | `DecimalPrecision.Two` |
| `3` | `DecimalPrecision.Three` |

**ValidationState enum values:**

| Old string | New enum |
|------------|----------|
| `"None"` | `ValidationState.None` |
| `"Error"` | `ValidationState.Error` |

### Removed properties

The following property has been removed from the control and is no longer available.

| Property | Was in Previous | Notes |
|----------|-----------------|-------|
| `DelayOutput` | Advanced > Data | Removed. This property was used to control when the value updates. The new **OnChange** behavior (firing on blur and step clicks) makes this property unnecessary. |

If your app references `DelayOutput` in formulas, remove those references and adjust your logic to work with the new **OnChange** timing.

## Behavioral changes and improvements

The new version includes significant behavioral changes and bug fixes:

### 1. OnChange fires on blur and step clicks (CRITICAL CHANGE)

**Previous behavior:** The **OnChange** event fired on every keystroke as the user typed, which could cause performance issues with complex formulas.

**New behavior:** The **OnChange** event fires only when:
- The user moves focus away from the control (on blur/focus out)
- The user clicks the increment or decrement step buttons

**Migration:**
- **Action required:** Review all **OnChange** formulas
- This change improves performance and prevents issues with rapid formula execution
- If you need per-keystroke updates, you'll need to use a different approach or reconsider your design
- Most apps will benefit from this change without modifications

**Example:**
```
// This formula now runs on blur and step clicks, not every keystroke
OnChange = Set(varTotalPrice, NumberInput1.Value * varUnitPrice)
```

### 2. TriggerOutput no longer fires OnChange

**Previous behavior:** Calling `TriggerOutput()` would fire the **OnChange** event.

**New behavior:** `TriggerOutput()` is no longer available and does not trigger **OnChange**.

**Migration:**
- Remove references to `TriggerOutput()` in your formulas
- If you need to manually trigger calculations, call the logic directly using `Set()` or other functions

### 3. Race condition fixed (form submission)

**Previous behavior (bug):** Entering a new value and immediately submitting a form would sometimes record the previous value instead of the new value.

**New behavior (fixed):** The value is correctly captured even when the form is submitted immediately after entering a number.

**Migration:** No action needed. This is a bug fix that improves reliability. You can remove any workarounds you added for this issue.

### 4. Value overflow fixed

**Previous behavior (bug):** Very large numbers could overflow or display incorrectly.

**New behavior (fixed):** Large numbers are now handled correctly without overflow.

**Migration:** No action needed. This is a bug fix.

### 5. Min/Max validation improved

**Previous behavior (bug):** The control did not properly validate that **Min** could not exceed **Max**, leading to confusing behavior.

**New behavior (fixed):** The control now validates that **Min** ≤ **Max** and shows appropriate errors.

**Migration:** No action needed. This is a bug fix. However, review your Min/Max settings to ensure they're logically consistent.

## Default value changes

The following default values have changed between versions.

| Property | Previous default | New default | Impact |
|----------|------------------|-------------|--------|
| `Value` | Not set (blank) | 0 | Control now shows 0 by default instead of blank |
| `Width` | 320 | 320 | No change |
| `Height` | 32 | 32 | No change |

## Property section reorganization

In the previous version, most properties were in the **Data** section under the Advanced tab. In the new version, properties are logically split between **Data** and **Design** sections.

### Previous property organization (Advanced tab)

- **Data section:** OnChange, AccessibleLabel, Align, Appearance, BasePaletteColor, BorderColor, BorderRadius, BorderStyle, BorderThickness, ContentLanguage, DelayOutput, FontSize, Max, Min, Padding properties, Precision, Step, ValidationState, Value
- **Design section:** DisplayMode, Height, Visible, Width, X, Y

### New property organization (Advanced tab)

- **Action section:** OnChange
- **Data section:** AccessibleLabel, ContentLanguage, Default, HintText, Max, Min, Precision, Step
- **Design section:** Align, Appearance, BasePaletteColor, BorderColor, BorderStyle, BorderThickness, Color, DisplayMode, Fill, Font, Height, Padding properties, Radius properties, Size, Visible, Width, X, Y

This reorganization does not affect runtime behavior but makes properties easier to find in the authoring panel.

## Migration checklist

Use this checklist when migrating an app from the previous Number Input control to the new version:

### 1. Update property names

Search for and replace these property names in formulas:

- `FontSize` → `Size`
- `BorderRadius` → Use `RadiusTopLeft`, `RadiusTopRight`, `RadiusBottomLeft`, `RadiusBottomRight` instead

### 2. Update enum values

Replace string values with enum syntax:

- `Appearance = "FilledDarker"` → `Appearance = Appearance.FilledDarker`
- `Align = ""` → `Align = Align.Left`
- `Precision = "Auto"` → `Precision = DecimalPrecision.Auto`
- `ValidationState = "None"` → `ValidationState = ValidationState.None`

### 3. Remove DelayOutput references

Remove any formulas that reference the **DelayOutput** property:

```
// Remove this type of code
NumberInput1.DelayOutput = true
```

### 4. Review OnChange logic (CRITICAL)

**OnChange** now fires on blur and step clicks, not every keystroke:

- Review all **OnChange** formulas to ensure this timing works for your app
- Remove workarounds for performance issues caused by keystroke-level updates
- Test that calculations and validations work correctly with the new timing

```
// This now runs on blur and step clicks
OnChange = UpdateContext({varTotal: NumberInput1.Value * varQuantity})
```

### 5. Remove TriggerOutput calls

Remove any calls to `TriggerOutput()`:

```
// Old code - remove this
TriggerOutput(NumberInput1)

// New approach - trigger logic directly
Set(varTotal, NumberInput1.Value * varQuantity)
```

### 6. Use new Default property

If you set initial values in **OnVisible**, consider using the **Default** property instead:

```
// Better approach with Default property
NumberInput1.Default = 1

// Old approach (still works, but Default is cleaner)
Screen1.OnVisible = Set(varInitialValue, 1)
```

### 7. Add HintText for guidance

Use the new **HintText** property to guide users:

```
NumberInput1.HintText = "Enter quantity"
```

### 8. Test form submission

Test that form submission captures the correct value, especially when users enter a value and immediately submit. The race condition bug is fixed.

### 9. Verify Min/Max boundaries

Ensure **Min** and **Max** values are logically consistent (Min ≤ Max). The control now validates this.

## Examples

### Example 1: Update appearance and precision

**Previous version:**
```
NumberInput1.Appearance = "FilledDarker"
NumberInput1.Precision = 2
NumberInput1.FontSize = 16
```

**New version:**
```
NumberInput1.Appearance = Appearance.FilledDarker
NumberInput1.Precision = DecimalPrecision.Two
NumberInput1.Size = 16
```

### Example 2: OnChange optimization

**Previous version (fired on every keystroke):**
```
// This caused performance issues with complex calculations
OnChange = Patch(
    OrderDetails,
    LookUp(OrderDetails, ID = varOrderID),
    {
        Quantity: NumberInput1.Value,
        Total: NumberInput1.Value * varUnitPrice,
        Tax: (NumberInput1.Value * varUnitPrice) * varTaxRate
    }
)
```

**New version (fires on blur and step clicks):**
```
// This now runs only when user leaves field or clicks step buttons
// Much better performance, no changes needed
OnChange = Patch(
    OrderDetails,
    LookUp(OrderDetails, ID = varOrderID),
    {
        Quantity: NumberInput1.Value,
        Total: NumberInput1.Value * varUnitPrice,
        Tax: (NumberInput1.Value * varUnitPrice) * varTaxRate
    }
)
```

### Example 3: Remove DelayOutput and TriggerOutput

**Previous version:**
```
// Delayed output to reduce updates
NumberInput1.DelayOutput = true

// Button to force output
Button1.OnSelect = TriggerOutput(NumberInput1); SubmitForm(Form1)
```

**New version:**
```
// DelayOutput removed - OnChange timing is optimized by default
// No need to set anything

// Button submits directly
Button1.OnSelect = SubmitForm(Form1)
```

### Example 4: Use Default and HintText

**Previous version:**
```
// Set initial value in screen's OnVisible
Screen1.OnVisible = Set(varQuantity, 1)
NumberInput1.Value = varQuantity
```

**New version:**
```
// Use Default property directly
NumberInput1.Default = 1
NumberInput1.HintText = "Enter quantity (1-100)"
```

### Example 5: Validation with enum

**Previous version:**
```
// String-based validation
NumberInput1.ValidationState = If(
    NumberInput1.Value > 100,
    "Error",
    "None"
)
```

**New version:**
```
// Enum-based validation
NumberInput1.ValidationState = If(
    NumberInput1.Value > 100,
    ValidationState.Error,
    ValidationState.None
)
```

## See also

- [Number Input modern control reference](number-input-reference.md)
- [Modern controls overview](overview-modern-controls.md)
- [New enum patterns in modern controls](../new-enums-reference.md)
