---
title: Radio modern control in canvas apps - Power Apps
description: Learn about the details, properties, and examples of the Radio modern control in Power Apps.
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

# Radio modern control in canvas apps

A group of mutually exclusive radio button options that users can use to select one item from a list.

## Description

The **Radio** modern control provides a user-friendly way to present mutually exclusive options in your canvas apps. Users can select exactly one option from a group of choices, making it ideal for scenarios like selecting shipping methods, rating satisfaction, or choosing payment types.

This control automatically manages the selection state—when a user selects one option, any previously selected option is automatically deselected. The Radio control supports both vertical and horizontal layouts, customizable styling, and comprehensive accessibility features to ensure your apps work for all users.

Use the **Radio** control when you need users to make a single choice from 2-7 clearly defined options. For larger option sets, consider using a [Combo Box](modern-control-combobox.md) control instead.

Key properties for this control are **Items**, **ItemDisplayText**, **Default**, and **Selected**.

## General

**Items** – The data source that provides the list of options to display. Can be a table, collection, or list of values. Each item becomes a selectable radio button option.

**ItemDisplayText** – The formula that determines what text displays for each radio button option. Use `ThisItem` to reference the current item from **Items**. For example, `ThisItem.Title` or `ThisItem.OptionName`.

**Default** – The item that the control selects by default when it first loads. Must match an item from the **Items** source.

**Selected** – The currently selected item (output property). Use this in formulas to reference which option the user chooses.

**Visible** – Whether the control appears or is hidden. Use a Power Fx formula to show or hide the control based on app state.

## Behavior

**OnChange** – How the app responds when the user selects a different radio button option. This event fires immediately every time the selection changes.

**Layout** – The arrangement of radio button options. Accepts `Layout` enum values:

| Value | Description |
|-------|-------------|
| `Layout.Vertical` | Stacks options vertically (default) |
| `Layout.Horizontal` | Arranges options horizontally in a row |

**Required** – Whether the user must select an option before submitting a form. When `true`, the control shows validation styling if no selection exists.

**TriggerOutput** – Forces the control to output its current selected value. Use this value when you need to manually trigger value updates.

**DisplayMode** – Whether the control allows user input (**Edit**), only displays data (**View**), or is disabled (**Disabled**). In **View** mode, the selected option appears with a read-only appearance (not grayed out like **Disabled**).

## Size and position

**X** – Distance between the left edge of the control and the left edge of its parent container (screen if no parent container).

**Y** – Distance between the top edge of the control and the top edge of its parent container (screen if no parent container).

**Width** – Distance between the control's left and right edges.

**Height** – Distance between the control's top and bottom edges. The control automatically sizes to fit all radio button options.

**PaddingTop** – Distance between the options and the top edge of the control.

**PaddingBottom** – Distance between the options and the bottom edge of the control.

**PaddingLeft** – Distance between the options and the left edge of the control.

**PaddingRight** – Distance between the options and the right edge of the control.

**LineHeight** – The spacing between radio button options, measured in pixels or points.

## Style and theme

**BasePaletteColor** – The base color that the theme uses to generate the control's color palette. Change this property to apply a different theme color to the control.

**Font** – The name of the font family in which option text appears.

**Size** – The font size of the option text, in points.

**Color** – The color of the option text in the control.

**FontWeight** – The weight (thickness) of the option text. Accepts `FontWeight` enum values:

| Value | Description |
|-------|-------------|
| `FontWeight.Bold` | Bold text |
| `FontWeight.Semibold` | Semibold text |
| `FontWeight.Normal` | Normal weight (default) |
| `FontWeight.Lighter` | Lighter weight |

**Italic** – Whether the option text appears in italic style.

**Underline** – Whether a line appears under the option text.

**Strikethrough** – Whether a line appears through the middle of the option text.

**Fill** – The background fill color of the control.

**HoverColor** – The color of an option's text when the user hovers the mouse over it.

**PressedColor** – The color of an option's text when the user clicks it.

**DisabledColor** – The color of option text when the control is in **Disabled** mode.

**RadioSize** – The size of the radio button circles in pixels.

**RadioBackgroundFill** – The background fill color of the radio button circles.

**RadioBorderColor** – The border color of the radio button circles.

**RadioSelectionFill** – The fill color of the inner circle when a radio button is selected.

**BorderColor** – The color of the control's border.

**BorderStyle** – The style of the control's border. Accepts `BorderStyle` enum values: `BorderStyle.Solid`, `BorderStyle.Dashed`, `BorderStyle.Dotted`, or `BorderStyle.None`.

**BorderThickness** – The thickness of the control's border in pixels.

**RadiusTopLeft** – The corner radius for the top-left corner of the control.

**RadiusTopRight** – The corner radius for the top-right corner of the control.

**RadiusBottomLeft** – The corner radius for the bottom-left corner of the control.

**RadiusBottomRight** – The corner radius for the bottom-right corner of the control.

## Accessibility

**AccessibleLabel** – A label for screen readers to announce what the radio group represents. It should describe the category or question being answered (for example, "Shipping method" or "Payment type").

**ContentLanguage** – The language used for the option text. Inherits from app settings if not specified.

## Example

The following YAML example shows radio button controls with different option sets:

```yaml
- ShippingRadio:
    Control: ModernRadio@1.0.0
    Properties:
      Items: =["Standard (5-7 days)", "Express (2-3 days)", "Overnight"]
      Layout: =Layout.Vertical
      AccessibleLabel: ="Select shipping method"
      X: =40
      Y: =100
      Width: =300

- SatisfactionRadio:
    Control: ModernRadio@1.0.0
    Properties:
      Items: =["Very Satisfied", "Satisfied", "Neutral", "Unsatisfied", "Very Unsatisfied"]
      Required: =true
      Layout: =Layout.Vertical
      AccessibleLabel: ="Service satisfaction rating"
      X: =40
      Y: =200
      Width: =250

- PaymentRadio:
    Control: ModernRadio@1.0.0
    Properties:
      Items: =["Credit Card", "Debit Card", "PayPal", "Bank Transfer"]
      Layout: =Layout.Vertical
      AccessibleLabel: ="Select payment method"
      X: =40
      Y: =350
      Width: =320
```

## Recent updates

The updated version of the **Radio** modern control includes improvements and behavior change.

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

### Bug fixes and improvements

- **Item order preserved**: The control now respects the order of items in the **Items** property and displays them in the same sequence. Previously, the control sometimes reordered items unexpectedly.
- **View mode appearance**: When you set **DisplayMode** to **View**, the control displays a proper read-only appearance instead of appearing disabled or grayed out.
- **OnChange reliability**: The **OnChange** event now fires immediately and reliably on every selection change.
- **Gallery selection fixed**: Radio buttons inside galleries now respond correctly to single clicks. Previously, a double-click was sometimes required.
- **Scrolling support**: Long lists of radio options now scroll properly instead of being cut off.
- **Theme color respected**: The **BasePaletteColor** property is now properly respected and no longer overridden by default colors.
- **Default value matching**: The **Default** property now correctly matches items from the **Items** data source without unexpected errors.
- **Hover and pressed states**: New **HoverColor** and **PressedColor** properties provide visual feedback for user interactions.
- **Radio styling control**: New properties (**RadioSize**, **RadioBackgroundFill**, **RadioBorderColor**, **RadioSelectionFill**) give you fine-grained control over radio button appearance.
- **Disabled state color**: New **DisabledColor** property controls text color when the control is disabled.

## Best practices

- **Clear option text**: Use **ItemDisplayText** to provide clear, descriptive labels for each option. Avoid abbreviations or jargon.
- **Reasonable option count**: Radio buttons work best with 2-7 options. For more options, consider using a Combo Box control instead.
- **Default selection**: Always set a **Default** value to guide users toward the most common or recommended choice.
- **Accessible labels**: Provide descriptive **AccessibleLabel** text that explains what the user is choosing between (for example, "Select your preferred contact method").
- **Visual feedback**: Use **HoverColor** and **PressedColor** to provide clear visual feedback for user interactions.
- **Layout consideration**: Use **Layout.Vertical** for most cases. Only use **Layout.Horizontal** when you have short option labels and limited options (2-4).


## Limitations

- The control height automatically adjusts to fit all options and you can't manually constrain it to a specific height with scrolling (items scroll if needed).
- Very small or very large width and height values might not be fully respected by the control.

## See also

- [Modern controls overview](overview-modern-controls.md)
- [Size and location properties](../properties-size-location.md)
