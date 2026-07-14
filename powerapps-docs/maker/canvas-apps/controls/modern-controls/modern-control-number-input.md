---
title: Number Input modern control in canvas apps - Power Apps
description: Learn about the details, properties, and examples of the Number Input modern control in Power Apps.
author: yogeshgupta698
ms.topic: reference
ms.custom: canvas
ms.date: 02/23/2026
ms.subservice: canvas-maker
ms.author: yogupt
ms.reviewer: mkaur
search.audienceType:
  - maker
---

# Number Input modern control in canvas apps

A numeric input field with increment and decrement buttons, validation, and decimal precision control.

## Description

The **Number Input** control is a modern control in Power Apps that lets users enter numeric values with built-in validation, increment/decrement buttons, and configurable precision settings. This control provides a user-friendly interface for numeric data entry while automatically enforcing data integrity through minimum and maximum value constraints.

Use this control when you need to collect numbers from users, such as quantities, prices, percentages, or measurements. The control includes step buttons for easy value adjustment, supports decimal precision control, and provides visual validation feedback to ensure data quality.

Key capabilities:

- Input validation with customizable min/max boundaries
- Increment and decrement buttons with configurable step values
- Decimal precision control from integers to three decimal places
- Built-in accessibility features and screen reader support
- Responsive design that adapts to different screen sizes


Key properties for this control are **Value**, **Min**, **Max**, **Step**, and **Precision**.

## General

**Default** – The initial value displayed when the control first loads. Use this value to set a default numeric value before user interaction.

**Value** – The current numeric value in the control. This value is the output property you reference in formulas to get the user's entered number.

**HintText** – Placeholder text displayed in the input field when it's empty. Use this text to guide users on what value to enter.

**Visible** – Whether the control appears or is hidden. Use a Power Fx formula to show or hide the control based on app state.

## Behavior

**OnChange** – How the app responds when the user changes the value. This event fires when the user moves focus away from the control (on blur) or clicks the increment or decrement step buttons, not on every keystroke.

**Min** – The minimum allowed value. Users can't enter or step below this number. The control shows a validation error if the user attempts to enter a value below the minimum.

**Max** – The maximum allowed value. Users can't enter or step above this number. The control shows a validation error if the user attempts to enter a value above the maximum.

**Step** – The increment or decrement amount when users click the step up or down buttons. Default is **1**.

**Precision** – The number of decimal places to display and allow. Accepts `DecimalPrecision` enum values:

| Value | Description |
|-------|-------------|
| `DecimalPrecision.Auto` | Automatically determines decimal places based on input (default) |
| `DecimalPrecision.'0'` | No decimal places (integers only) |
| `DecimalPrecision.'1'` | One decimal place (e.g., 12.3) |
| `DecimalPrecision.'2'` | Two decimal places (e.g., 12.34) |
| `DecimalPrecision.'3'` | Three decimal places (e.g., 12.345) |

**ValidationState** – The visual validation state of the control. Accepts `ValidationState` enum values:

| Value | Description |
|-------|-------------|
| `ValidationState.None` | No validation styling (default) |
| `ValidationState.Error` | Shows error styling (red border) |

**DisplayMode** – Whether the control allows user input (**Edit**), only displays data (**View**), or is disabled (**Disabled**). In **View** mode, the value is shown but can't be edited.

## Size and position

**Align** – The horizontal alignment of text within the control. Accepts `Align` enum values:

| Value | Description |
|-------|-------------|
| `Align.Left` | Aligns text to the left edge (default) |
| `Align.Center` | Centers text horizontally |
| `Align.Right` | Aligns text to the right edge |

**X** – Distance between the left edge of the control and the left edge of its parent container (screen if no parent container).

**Y** – Distance between the top edge of the control and the top edge of its parent container (screen if no parent container).

**Width** – Distance between the control's left and right edges. Default is **320**.

**Height** – Distance between the control's top and bottom edges. Default is **32**.

**PaddingTop** – Distance between the text and the top edge of the control.

**PaddingBottom** – Distance between the text and the bottom edge of the control.

**PaddingLeft** – Distance between the text and the left edge of the control.

**PaddingRight** – Distance between the text and the right edge of the control.

## Style and theme

**Appearance** – The visual style of the control. Accepts `Appearance` enum values:

| Value | Description |
|-------|-------------|
| `Appearance.Filled` | Filled background style |
| `Appearance.FilledDarker` | Darker filled background (default) |
| `Appearance.Outline` | Outlined border with transparent background |

**BasePaletteColor** – The base color that the theme uses to generate the control's color palette. Change this property to apply a different theme color to the control.

**Font** – The name of the font family for the text.

**Size** – The font size of the text, in points.

**Color** – The color of the text in the control.

**Fill** – The background fill color of the control.

**BorderColor** – The color of the control's border.

**BorderStyle** – The style of the control's border. Accepts `BorderStyle` enum values: `BorderStyle.Solid`, `BorderStyle.Dashed`, `BorderStyle.Dotted`, or `BorderStyle.None`.

**BorderThickness** – The thickness of the control's border in pixels.

**RadiusTopLeft** – The corner radius for the top-left corner of the control.

**RadiusTopRight** – The corner radius for the top-right corner of the control.

**RadiusBottomLeft** – The corner radius for the bottom-left corner of the control.

**RadiusBottomRight** – The corner radius for the bottom-right corner of the control.

## Accessibility

**AccessibleLabel** – A label for screen readers to announce what the input field is for. Describe the type of numeric data expected, such as "Product quantity" or "Age in years".

**ContentLanguage** – The language used for the input text. If you don't specify this property, the app settings provide the value.

## Example

The following YAML example shows a product quantity selector with inventory validation and a currency amount input with dynamic formatting:

```yaml
- QuantityInput:
    Control: ModernNumberInput@1.0.0
    Properties:
      Default: =1
      Min: =1
      Max: =100
      Step: =1
      Precision: =DecimalPrecision.'0'
      HintText: ="Enter quantity"
      AccessibleLabel: ="Product quantity"
      X: =40
      Y: =100
      Width: =200
      Height: =32

- PriceInput:
    Control: ModernNumberInput@1.0.0
    Properties:
      Default: =0
      Min: =0
      Max: =10000
      Step: =0.01
      Precision: =DecimalPrecision.'2'
      HintText: ="0.00"
      Align: =Align.Right
      Appearance: =Appearance.FilledDarker
      AccessibleLabel: ="Purchase amount in dollars"
      X: =40
      Y: =150
      Width: =200
      Height: =32

- DiscountInput:
    Control: ModernNumberInput@1.0.0
    Properties:
      Default: =0
      Min: =0
      Max: =100
      Step: =5
      Precision: =DecimalPrecision.'1'
      HintText: ="0.0"
      AccessibleLabel: ="Discount percentage"
      X: =40
      Y: =200
      Width: =200
      Height: =32
```

## Recent updates

The updated version of the **Number input** modern control includes improvements and behavior change.

### Property renames

The following properties are renamed. Update any formulas in your app that reference the old property names.

| Previous property | New property |
|-------------------|--------------|
| `FontColor` | `Color` |
| `FontSize` | `Size` |
| `FontItalic` | `Italic` |
| `FontStrikethrough` | `Strikethrough` |
| `FontUnderline` | `Underline` |
| `BorderRadius` | `RadiusTopLeft`, `RadiusTopRight`, `RadiusBottomLeft`, `RadiusBottomRight` |

### Removed properties

| Removed property | Notes |
|------------------|-------|
| `TriggerOutput` | Removed entirely. **OnChange** now fires on focus out and step button clicks. |

### Bug fixes and improvements

- **OnChange optimization**: The **OnChange** event now fires on focus out (when the user leaves the field) and when clicking step buttons, not on every keystroke. This change improves performance and reduces unnecessary formula evaluations.
- **Default value**: The **Default** property allows you to set an initial value when the control loads, separate from the **Value** property.
- **HintText support**: New **HintText** property provides placeholder text to guide users.
- **Color property added**: The **Color** property for text color is now available. This property was missing in the previous version.
- **Fill property added**: The **Fill** property for background color is now available for better styling control.
- **Font property added**: The **Font** property allows you to change the font family.
- **Race condition fixed**: Resolved an issue where entering a new value and immediately submitting a form recorded the previous value instead of the new one.
- **Value overflow fixed**: Numbers no longer overflow or display incorrectly at high values.
- **Min/Max validation improved**: The control now properly validates that Min can't exceed Max.
- **Simplified properties**: Properties are now logically organized into **Data** and **Design** sections for better discoverability.

## Best practices

- **Set reasonable boundaries**: Always define **Min** and **Max** values to prevent invalid data entry.
- **Match precision to data**: Use **Precision** to match your data requirements (integers for quantities, two decimals for currency, and so on).
- **Appropriate step values**: Set **Step** to meaningful increments (for example, 5 for ages, 0.01 for currency, 10 for large numbers).
- **Clear hints**: Use **HintText** to show the expected format or example values (for example, "0.00" for currency).
- **Validate input**: Use **ValidationState** to provide visual feedback when values are out of acceptable ranges.
- **Accessible labels**: Always provide descriptive **AccessibleLabel** text that explains what numeric value is expected.
- **OnChange efficiency**: Since **OnChange** fires on blur and step clicks (not every keystroke), it's safe to use for calculations or data updates without performance concerns.

## Limitations

- The control doesn't directly support currency symbols. Use separate Text controls to display currency formatting.
- Step buttons might not scale proportionally with control size in all scenarios.

## See also

- [Modern controls overview](overview-modern-controls.md)
- [Size and location properties](../properties-size-location.md)
