---
title: Slider modern control in canvas apps - Power Apps
description: Learn about the details, properties, and examples of the Slider modern control in Power Apps.
author: yogeshgupta698
ms.topic: reference
ms.custom: canvas
ms.date: 04/16/2026
ms.subservice: canvas-maker
ms.author: yogupt
ms.reviewer: mkaur
search.audienceType:
  - maker
---

# Slider modern control in canvas apps

Let users select a numeric value by dragging a handle along a track.

## Description

The **Slider** modern control lets users set a value between a minimum and maximum by dragging a handle along a track. The control supports horizontal and vertical orientation.

Use this control when you want users to pick a value from a continuous range, such as:

- Volume or brightness controls
- Budget or price range selectors
- Quantity pickers
- Rating or satisfaction scales

Key properties for this control are **Default**, **Min**, **Max**, **Value** (output), and **OnChange**.

> [!NOTE]
> This article describes the updated Slider modern control. For information about what changed from the previous version, see [Recent updates](#recent-updates).

## General

**Default** – The initial value of the slider before the user makes a change. Resets to this value when `Reset` is triggered. Default is **50**.

**Min** – The minimum value the user can set. Default is **0**.

**Max** – The maximum value the user can set. Default is **100**.

**Visible** – Whether the control appears or is hidden.

## Behavior

**OnChange** – Actions to perform when the user changes the slider value. Use `Self.Value` to read the current value.

**DisplayMode** – Whether the control allows user input (**Edit**), only displays data (**View**), or is disabled (**Disabled**).

**LayoutDirection** – The orientation of the slider track. Accepts `LayoutDirection` enum values:

| Value | Description |
|-------|-------------|
| `LayoutDirection.Horizontal` | Handle moves left to right. Default. |
| `LayoutDirection.Vertical` | Handle moves bottom to top. |

## Size and position

**[X](../properties-size-location.md)** – Distance between the left edge of the control and the left edge of its parent container (screen if no parent container).

**[Y](../properties-size-location.md)** – Distance between the top edge of the control and the top edge of its parent container (screen if no parent container).

**Width** – Distance between the control's left and right edges. Default is **200**.

**Height** – Distance between the control's top and bottom edges. Default is **35**.

## Style and theme

**BasePaletteColor** – The base color that the theme uses to generate the control's color palette. Change this value to apply a different theme color to the slider track and handle.

**Size** – The visual size of the slider handle and track. Accepts `SliderSize` enum values:

| Value | Description |
|-------|-------------|
| `SliderSize.Small` | Smaller handle and track. |
| `SliderSize.Medium` | Standard size. Default. |
| `SliderSize.Large` | Larger handle and track. |

## Accessibility

**AccessibleLabel** – Label that screen readers read. Describe the purpose of the slider (for example, `"Volume"`). Always set this property so assistive technologies can identify the control.

**ContentLanguage** – The display language for the control content, if different from the app language.

**Tooltip** – Explanatory text that appears when the user hovers over the control. Helpful for sighted users who need additional context about the slider's purpose.

## Output properties

**Value** – The current value of the slider, updated as the user drags the handle. Use this value in formulas to read the slider's current position (for example, `Slider1.Value`).

## Examples

### Budget selector with a label

This example shows a horizontal slider that lets users set a monthly budget. A label updates in real time as the user drags the handle.

```yaml
- BudgetSlider:
    Control: ModernSlider@1.0.0
    Properties:
      Default: =500
      Min: =0
      Max: =10000
      LayoutDirection: =LayoutDirection.Horizontal
      Size: =SliderSize.Medium
      AccessibleLabel: ="Monthly budget"
      Tooltip: ="Drag to set your monthly budget"
      Width: =300
      Height: =35

- BudgetLabel:
    Control: ModernText@1.0.0
    Properties:
      Size: =14
      Text: |-
        ="Budget: $" & BudgetSlider.Value
```

### Vertical volume slider

This example uses a vertical slider for a volume control and writes the selected value to a variable.

```yaml
- VolumeSlider:
    Control: ModernSlider@1.0.0
    Properties:
      Default: =30
      Min: =0
      Max: =100
      LayoutDirection: =LayoutDirection.Vertical
      Size: =SliderSize.Small
      AccessibleLabel: ="Volume"
      Width: =35
      Height: =200
```

## Recent updates

The updated version of the **Slider** modern control includes the following improvements and behavior changes.

### Property renames

| Previous property | New property | Notes |
|---|---|---|
| `Value` (input) | `Default` | The input property that sets the initial value is now `Default`. `Value` is now a read-only output property. |
| `Layout` | `LayoutDirection` | Renamed for clarity and changed from string to typed enum. |

### Enum format changes

| Property | Previous value | New value |
|---|---|---|
| `LayoutDirection` | `"Horizontal"` | `LayoutDirection.Horizontal` |
| `LayoutDirection` | `"Vertical"` | `LayoutDirection.Vertical` |
| `Size` | `"Small"` | `SliderSize.Small` |
| `Size` | `"Medium"` | `SliderSize.Medium` |
| `Size` | `"Large"` | `SliderSize.Large` |

### Bug fixes and improvements

- **Separate Default and Value**: `Default` sets the initial value; `Value` is now a dedicated read-only output property. This change matches the pattern used by Number Input and other modern controls, making formulas more predictable.
- **Tooltip support**: New `Tooltip` property shows explanatory text on hover.
- **Updated enums**: `LayoutDirection` and `Size` now use typed Power Fx enums, improving IntelliSense and reducing formula errors.

## Best practices

- **Set meaningful Min and Max values.** A slider from 0 to 100 works well for percentages, but for dollar amounts or quantities, use a range that matches the expected input so each drag movement feels responsive.
- **Always provide an AccessibleLabel.** Screen readers rely on this property to describe the slider's purpose to users with visual impairments.
- **Pair the slider with a label** that displays the current value (for example, `"Budget: $" & Slider1.Value`). Users can see the exact number without guessing from the handle position.
- **Use vertical orientation sparingly.** Horizontal sliders are more familiar to most users. Reserve vertical sliders for cases where the metaphor matches, such as volume faders.

## See also

- [Modern controls overview](overview-modern-controls.md)
- [Size and location properties](../properties-size-location.md)
