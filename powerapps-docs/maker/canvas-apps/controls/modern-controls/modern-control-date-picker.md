---
title: Date picker modern control in canvas apps - Power Apps
description: Learn about the details, properties, and examples of the Date picker modern control in Power Apps.
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

# Date picker modern control in canvas apps

The **Date picker** modern control provides an intuitive calendar interface for date selection in canvas apps. This control combines visual calendar navigation with flexible formatting options to create a seamless date input experience for users.

## Description

Use this control when you need users to select specific dates, such as appointment scheduling, event planning, or filtering data by date ranges. The control supports customizable date formats, timezone handling, and date range restrictions to meet diverse application requirements.

Key capabilities include:

- Visual calendar interface with month and year navigation
- Flexible date formatting using predefined formats or custom patterns
- Date range validation to restrict selectable dates
- Timezone support for local or UTC display
- Accessibility features for screen readers and keyboard navigation

The control outputs the selected date through the SelectedDate property, which you can use in formulas throughout your app.


Key properties for this control are **SelectedDate**, **Format**, and **DateTimeZone**.

## General

**Placeholder** – Hint text that appears when no date is selected. Default is **"Select a date"**.

**DefaultDate** – The initial date selected in the control before the user makes a change. Use this property to set a default date when the picker first loads.

**Format** – The display format for the selected date. Accepts `DatePickerFormat` enum values or a custom format string:

**Enum values:**

| Value | Description | Example |
|-------|-------------|---------|
| `DatePickerFormat.LongAbbreviated` | Abbreviated month with full year (default) | Jan 15, 2024 |
| `DatePickerFormat.Short` | Short numeric format | 1/15/2024 |
| `DatePickerFormat.Long` | Full month name with year | January 15, 2024 |

**Custom format strings:**

You can also use custom date format patterns as strings to create specific date representations:

| Format string | Example output |
|---------------|----------------|
| `"dd-mm-yyyy"` | 15-01-2024 |
| `"dd-mm"` | 15-01 |
| `"yyyy-mm-dd"` | 2024-01-15 |
| `"dd/mm/yyyy"` | 15/01/2024 |
| `"mm/dd/yyyy"` | 01/15/2024 |

Use custom format strings when you need a specific date representation not available in the enum values. Example: `Format = "dd-mm-yyyy"`.

**DateTimeZone** – The timezone used for date display and storage. Accepts `DateTimeZone` enum values:

| Value | Description |
|-------|-------------|
| `DateTimeZone.Local` | User's local timezone (default) |
| `DateTimeZone.UTC` | Coordinated Universal Time |

**Visible** – Whether the control appears or is hidden. Use a Power Fx formula to show or hide the control based on app state.

## Behavior

**OnChange** – How the app responds when the user selects a different date. This event fires when the date selection changes.

**DisplayMode** – Whether the control allows user input (**Edit**), only displays data (**View**), or is disabled (**Disabled**). In **View** mode, the selected date is shown but the calendar can't be opened.

**IsEditable** – Whether the user can type a date directly into the input field or must use the calendar picker. When `false`, users must select the calendar icon to choose a date. Default is **false**.

## Date range

**StartDate** – The earliest date that can be selected in the calendar. Dates before this date are disabled. Default is **Date(1900, 1, 1)**.

**EndDate** – The latest date that can be selected in the calendar. Dates after this date are disabled. Default is **Date(Year(Today())+100, 12, 31)**.

**StartOfWeek** – The day that appears as the first column in the calendar view. Accepts `StartOfWeek` enum values:

| Value | Description |
|-------|-------------|
| `StartOfWeek.Sunday` | Week starts on Sunday (default) |
| `StartOfWeek.Monday` | Week starts on Monday |
| `StartOfWeek.Tuesday` | Week starts on Tuesday |
| `StartOfWeek.Wednesday` | Week starts on Wednesday |
| `StartOfWeek.Thursday` | Week starts on Thursday |
| `StartOfWeek.Friday` | Week starts on Friday |
| `StartOfWeek.Saturday` | Week starts on Saturday |

## Data

**SelectedDate** – (Output) The date currently selected by the user. Returns a date value that you can use in formulas. Returns `Blank()` if no date is selected.

## Validation

**ValidationState** – The current validation state of the control. Accepts `ValidationState` enum values:

| Value | Description |
|-------|-------------|
| `ValidationState.Error` | The control value has an error |
| `ValidationState.None` | No validation applied (default) |

## Size and position

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
| `Appearance.FilledDarker` | Filled with darker background (default) |
| `Appearance.Outline` | Outline style with border |

**BasePaletteColor** – The base color used by the theme to generate the control's color palette. Change this property to apply a different theme color to the control.

**Font** – The name of the font family in which text appears.

**Size** – The font size of the text, in points. Default is **0** (uses theme default).

**Color** – The color of the text in the control.

**FontWeight** – The weight (thickness) of the text. Accepts `FontWeight` enum values:

| Value | Description |
|-------|-------------|
| `FontWeight.Bold` | Bold text |
| `FontWeight.Semibold` | Semibold text |
| `FontWeight.Normal` | Normal weight (default) |
| `FontWeight.Lighter` | Lighter weight |

**Italic** – Whether the text appears in italic style.

**Underline** – Whether a line appears under the text.

**Strikethrough** – Whether a line appears through the middle of the text.

**Fill** – The background fill color of the control.

**BorderColor** – The color of the control's border.

**BorderStyle** – The style of the control's border. Accepts `BorderStyle` enum values: `BorderStyle.Solid`, `BorderStyle.Dashed`, `BorderStyle.Dotted`, or `BorderStyle.None`.

**BorderThickness** – The thickness of the control's border in pixels.

**RadiusTopLeft** – The corner radius for the top-left corner of the control.

**RadiusTopRight** – The corner radius for the top-right corner of the control.

**RadiusBottomLeft** – The corner radius for the bottom-left corner of the control.

**RadiusBottomRight** – The corner radius for the bottom-right corner of the control.

## Accessibility

**AccessibleLabel** – A label for screen readers to announce what the control is for. It should describe the purpose of the date picker, not the current selection.

**ContentLanguage** – The language used for formatting dates and calendar display. The app settings provide the value if you don't specify it.

## Example

The following YAML example shows date picker controls for selecting dates:

```yaml
- StartDatePicker:
    Control: ModernDatePicker@1.0.0
    Properties:
      Placeholder: ="Select start date"
      DefaultDate: =Today()
      StartDate: =Today()
      EndDate: =Today() + 365
      StartOfWeek: =StartOfWeek.Monday
      X: =40
      Y: =100
      Width: =280
      Height: =32

- EndDatePicker:
    Control: ModernDatePicker@1.0.0
    Properties:
      Placeholder: ="Select end date"
      Format: =DatePickerFormat.Short
      DefaultDate: =Today() + 7
      StartOfWeek: =StartOfWeek.Monday
      X: =340
      Y: =100
      Width: =280
      Height: =32
```

## Recent updates

The updated version of the **Date picker** modern control includes improvements and behavior change.

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
| `Required` | Use `ValidationState` instead to control validation styling. |

### Bug fixes and improvements

- **DisplayMode.View properly enforced**: In **View** mode, the control is now properly read-only and the calendar can't be opened. Previously, the picker was still editable in View mode.
- **Format property fully honored**: All format values are now properly applied. Previously, certain format values were ignored until another change was made.
- **DateTimeZone respected**: The **DateTimeZone** property now correctly applies to date display and storage. Previously, this property value was sometimes ignored.
- **Blank value handling**: When the control is in **View** mode with a blank value, it no longer incorrectly shows a previous value.
- **Mobile calendar improvements**: Calendar flyout is now properly sized for mobile devices, with optimized defaults (width 560, height 64, font size 24).
- **Month/Year flyout positioning**: Fixed issue where the month/year selector went off-screen on smaller displays.
- **Gallery and data card stability**: Resolved crashes that occurred when adding the date picker to galleries or data cards.
- **Color palette inheritance**: The calendar flyout now properly respects the **BasePaletteColor** override.
- **Command bar integration**: The authoring command bar and right-click menu now show Font, Font Size, Font color, and Background color for quick access.
- **DefaultDate property**: New property allows setting an initial date when the picker first loads.

## Limitations

- The calendar icon doesn't scale with font size in the current version.
- On mobile devices, the control shows the Fluent calendar view instead of the native mobile date picker.

## See also

- [Modern controls overview](overview-modern-controls.md)
- [Size and location properties](../properties-size-location.md)
