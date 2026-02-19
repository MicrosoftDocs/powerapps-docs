---
title: Enum reference for modern controls in canvas apps - Power Apps
description: Reference for all enum types used in modern controls in Power Apps canvas apps, including Align, VerticalAlign, FontWeight, ValidationState, and more.
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

# Enum reference for modern controls in canvas apps

Modern controls use typed enum values for many properties, replacing the plain string values used in the previous versions. This article lists all enum types used across modern controls with their accepted values.

Using enum syntax instead of string literals gives you IntelliSense support, compile-time validation, and localization safety in your Power Fx formulas.

## Align

**Used by:** Text, Text Input, Number Input, Link, Tab List, Date Picker, Combo Box

Controls the horizontal alignment of text within a control.

| Enum value | Description |
|------------|-------------|
| `Align.Left` | Aligns text to the left edge |
| `Align.Center` | Centers text horizontally |
| `Align.Right` | Aligns text to the right edge |
| `Align.Justify` | Stretches text to fill the full width (Text, Link only) |

**Migration note:** The previous string value `"Start"` or `""` (empty string) maps to `Align.Left`. The previous value `"End"` maps to `Align.Right`.

**Example:**
```
TextInput1.Align = Align.Center
NumberInput1.Align = Align.Right
```

## VerticalAlign

**Used by:** Text, Link

Controls the vertical alignment of text within a control.

| Enum value | Description |
|------------|-------------|
| `VerticalAlign.Top` | Aligns text to the top of the control |
| `VerticalAlign.Middle` | Centers text vertically (default) |
| `VerticalAlign.Bottom` | Aligns text to the bottom of the control |

**Migration note:** The previous Text control defaulted to `""` (empty/undefined). The new default is `VerticalAlign.Middle`.

**Example:**
```
Text1.VerticalAlign = VerticalAlign.Top
Link1.VerticalAlign = VerticalAlign.Middle
```

## FontWeight

**Used by:** Text, Text Input, Number Input, Link, Tab List, Radio, Combo Box, Date Picker, Info Button

Controls the thickness or weight of the font.

| Enum value | Description |
|------------|-------------|
| `FontWeight.Bold` | Bold weight |
| `FontWeight.Semibold` | Semibold weight |
| `FontWeight.Normal` | Normal/regular weight (default) |
| `FontWeight.Lighter` | Lighter weight |

> [!IMPORTANT]
> **FontWeight.Medium removed**: The `Medium` value is not available in the new controls. If your previous control used `FontWeight.Medium`, it will automatically map to `FontWeight.Normal` during migration.

**Migration note:** The previous Text control property was named `Weight` with string values (`"Regular"`, `"Bold"`, etc.). The new property is `FontWeight` with enum values. Both the property name and the value format changed.

**Example:**
```
Text1.FontWeight = FontWeight.Bold
TextInput1.FontWeight = FontWeight.Semibold
```

## ValidationState

**Used by:** Date Picker, Text Input, Number Input, Combo Box, Radio

Controls the visual validation state of the control.

| Enum value | Description |
|------------|-------------|
| `ValidationState.None` | No validation styling (default) |
| `ValidationState.Error` | Shows error styling (red border) |

> [!NOTE]
> Only two values are available: `None` and `Error`. There is no `Valid` or `Success` state.

**Migration note:** Previous versions may have used string values like `"None"` or `"Error"`. Update to enum syntax.

**Example:**
```
TextInput1.ValidationState = If(
    IsBlank(TextInput1.Text),
    ValidationState.Error,
    ValidationState.None
)

DatePicker1.ValidationState = If(
    IsBlank(DatePicker1.SelectedDate),
    ValidationState.Error,
    ValidationState.None
)
```

## Appearance

**Used by:** Date Picker, Text Input, Number Input, Combo Box

Controls the visual style of input controls.

| Enum value | Description |
|------------|-------------|
| `Appearance.Filled` | Filled background style |
| `Appearance.FilledDarker` | Darker filled background (default for most controls) |
| `Appearance.Outline` | Outlined border with transparent background |

**Migration note:** Previous versions used string values like `"Filled"`, `"FilledDarker"`, `"Outline"`. Update to enum syntax.

**Example:**
```
TextInput1.Appearance = Appearance.Outline
NumberInput1.Appearance = Appearance.FilledDarker
ComboBox1.Appearance = Appearance.Filled
```

## TabListAppearance

**Used by:** Tab List

Controls the visual style of the Tab List control. This is a **new enum** introduced in this release.

| Enum value | Description |
|------------|-------------|
| `TabListAppearance.Transparent` | Transparent background, minimal styling |
| `TabListAppearance.Subtle` | Subtle background fill on active tab |
| `TabListAppearance.Underline` | Underline indicator on active tab (default) |
| `TabListAppearance.Filled` | Filled background on active tab |

**Migration note:** This property is new and did not exist in the previous version.

**Example:**
```
TabList1.Appearance = TabListAppearance.Filled
TabList2.Appearance = TabListAppearance.Underline
```

## TabListAlignment

**Used by:** Tab List

Controls the positioning/alignment of the entire tab list.

| Enum value | Description |
|------------|-------------|
| `TabListAlignment.Start` | Aligns tabs to the left/start edge |
| `TabListAlignment.Center` | Centers the tab list (default) |
| `TabListAlignment.End` | Aligns tabs to the right/end edge |

**Migration note:** Previous versions may have used string values like `"Start"`, `"Center"`, `"End"`. Update to enum syntax.

**Example:**
```
TabList1.Alignment = TabListAlignment.Start
TabList2.Alignment = TabListAlignment.Center
```

## LinkAppearance

**Used by:** Link

Controls the visual style of the Link control.

| Enum value | Description |
|------------|-------------|
| `LinkAppearance.Default` | Standard link appearance with theme color (default) |
| `LinkAppearance.Subtle` | Subtle appearance with lighter styling |

**Migration note:** Previous versions used string values like `"Default"`, `"Subtle"`. Update to enum syntax.

**Example:**
```
Link1.Type = LinkAppearance.Default
Link2.Type = LinkAppearance.Subtle
```

## DatePickerFormat

**Used by:** Date Picker

Controls the date format displayed in the date picker.

| Enum value | Description | Example output |
|------------|-------------|----------------|
| `DatePickerFormat.LongAbbreviated` | Long abbreviated format | Mon, Jan 15, 2024 |
| `DatePickerFormat.Short` | Short format | 1/15/2024 |
| `DatePickerFormat.Long` | Long format | Monday, January 15, 2024 |

**Custom format strings:** You can also use custom format strings like `"dd-mm-yyyy"`, `"yyyy-mm-dd"`, `"dd-mm"` for specific formatting needs.

**Migration note:** Previous versions used string values like `"Long Abbreviated"`. Update to enum syntax or use custom format strings.

**Example:**
```
DatePicker1.Format = DatePickerFormat.LongAbbreviated
DatePicker2.Format = "dd-mm-yyyy"  // Custom format
```

## DateTimeZone

**Used by:** Date Picker

Controls whether dates are treated as local time or UTC.

| Enum value | Description |
|------------|-------------|
| `DateTimeZone.Local` | Local timezone (default) |
| `DateTimeZone.UTC` | UTC timezone |

**Migration note:** Previous versions used string values like `"Local"`, `"UTC"`. Update to enum syntax.

**Example:**
```
DatePicker1.DateTimeZone = DateTimeZone.Local
DatePicker2.DateTimeZone = DateTimeZone.UTC
```

## StartOfWeek

**Used by:** Date Picker

Controls which day is shown as the first day of the week in the calendar.

| Enum value | Description |
|------------|-------------|
| `StartOfWeek.Sunday` | Week starts on Sunday |
| `StartOfWeek.Monday` | Week starts on Monday |
| `StartOfWeek.Tuesday` | Week starts on Tuesday |
| `StartOfWeek.Wednesday` | Week starts on Wednesday |
| `StartOfWeek.Thursday` | Week starts on Thursday |
| `StartOfWeek.Friday` | Week starts on Friday |
| `StartOfWeek.Saturday` | Week starts on Saturday |

**Migration note:** Previous versions used string values like `"Sunday"`, `"Monday"`. Update to enum syntax.

**Example:**
```
DatePicker1.StartOfWeek = StartOfWeek.Monday
DatePicker2.StartOfWeek = StartOfWeek.Sunday
```

## DecimalPrecision

**Used by:** Number Input

Controls the number of decimal places displayed and allowed in number input.

| Enum value | Description | Example |
|------------|-------------|---------|
| `DecimalPrecision.Auto` | Automatically determines decimal places (default) | 12.345 |
| `DecimalPrecision.'0'` | No decimal places (integers only) | 12 |
| `DecimalPrecision.'1'` | One decimal place | 12.3 |
| `DecimalPrecision.'2'` | Two decimal places | 12.34 |
| `DecimalPrecision.'3'` | Three decimal places | 12.345 |

**Migration note:** Previous versions used numeric values (0, 1, 2, 3) or string `"Auto"`. Update to enum syntax: numeric values become `DecimalPrecision.'0'`, `DecimalPrecision.'1'`, etc. (with quotes), and `"Auto"` becomes `DecimalPrecision.Auto`.

**Example:**
```
NumberInput1.Precision = DecimalPrecision.'2'
NumberInput2.Precision = DecimalPrecision.'0'
NumberInput3.Precision = DecimalPrecision.Auto
```

## TextInputType

**Used by:** Text Input

Controls the input mode for the text field.

| Enum value | Description |
|------------|-------------|
| `TextInputType.Text` | Standard single-line text input (default) |
| `TextInputType.Multiline` | Multi-line text area that allows line breaks |
| `TextInputType.Password` | Password field that masks characters as *** |
| `TextInputType.Search` | Search input with appropriate styling |

**Migration note:** Previous versions used string values like `"Text"`, `"Multiline"`, `"Password"`. Update to enum syntax.

**Example:**
```
TextInput1.Type = TextInputType.Text
PasswordField.Type = TextInputType.Password
CommentBox.Type = TextInputType.Multiline
```

## TriggerOutput

**Used by:** Text Input, Combo Box, Radio

Controls when the output property updates.

| Enum value | Description |
|------------|-------------|
| `TriggerOutput.OnKeypress` | Updates on every keystroke (default for Text Input) |
| `TriggerOutput.OnBlur` | Updates only when focus leaves the control |
| `TriggerOutput.Delayed` | Updates after a short delay (automatically used in forms) |

> [!NOTE]
> **Number Input**: The **TriggerOutput** property has been removed from Number Input in the new version.

**Migration note:**
- Text Input: Default changed from **FocusOut** (which maps to OnBlur) to **OnKeypress**
- TriggerOutput no longer fires **OnChange** events

**Example:**
```
TextInput1.TriggerOutput = TriggerOutput.OnKeypress
TextInput2.TriggerOutput = TriggerOutput.OnBlur
```

## Layout

**Used by:** Radio

Controls the arrangement of radio button options.

| Enum value | Description |
|------------|-------------|
| `Layout.Vertical` | Stacks options vertically (default) |
| `Layout.Horizontal` | Arranges options horizontally in a row |

**Migration note:** Previous versions may have used string values. Update to enum syntax.

**Example:**
```
Radio1.Layout = Layout.Vertical
Radio2.Layout = Layout.Horizontal
```

## BorderStyle

**Used by:** Text, Text Input, Number Input, Date Picker, Combo Box, Tab List, Link, Radio

Controls the visual style of a control's border.

| Enum value | Description |
|------------|-------------|
| `BorderStyle.Solid` | Solid line border (default) |
| `BorderStyle.Dashed` | Dashed line border |
| `BorderStyle.Dotted` | Dotted line border |
| `BorderStyle.None` | No border |

**Example:**
```
TextInput1.BorderStyle = BorderStyle.Solid
Text1.BorderStyle = BorderStyle.Dashed
```

## DisplayMode

**Used by:** Date Picker, Text Input, Combo Box, Radio, Tab List, Info Button

> [!NOTE]
> For the **Text** control, `DisplayMode` is not shown in the property panel and has no effect. The property still exists for backward compatibility, so existing formulas won't break. The Text control is display-only; use the new **OnSelect** event for interactive behavior.

Controls whether a control allows user input or shows data as read-only.

| Enum value | Description |
|------------|-------------|
| `DisplayMode.Edit` | User can interact with the control (default) |
| `DisplayMode.View` | Control shows data in read-only state |
| `DisplayMode.Disabled` | Control appears grayed out and cannot be interacted with |

**What's improved:** In this release, `DisplayMode.View` now shows a proper read-only visual state instead of the disabled/grayed-out appearance that was shown in the previous version. This affects Date Picker, Text Input, Radio, and Combo Box controls.

**Example:**
```
TextInput1.DisplayMode = DisplayMode.Edit
DatePicker1.DisplayMode = DisplayMode.View
Radio1.DisplayMode = DisplayMode.Disabled
```

## Migration quick reference

When migrating from previous versions, use this quick reference table:

| Previous string value | New enum value | Property |
|----------------------|----------------|----------|
| `"Start"` or `""` | `Align.Left` | Align |
| `"Center"` | `Align.Center` | Align |
| `"End"` | `Align.Right` | Align |
| `""` | `VerticalAlign.Middle` | VerticalAlign |
| `"Regular"` | `FontWeight.Normal` | FontWeight (was Weight) |
| `"Bold"` | `FontWeight.Bold` | FontWeight (was Weight) |
| `"Medium"` | `FontWeight.Normal` | FontWeight (Medium removed) |
| `"None"` | `ValidationState.None` | ValidationState |
| `"Error"` | `ValidationState.Error` | ValidationState |
| `"Filled"` | `Appearance.Filled` | Appearance |
| `"FilledDarker"` | `Appearance.FilledDarker` | Appearance |
| `"Outline"` | `Appearance.Outline` | Appearance |
| `"Default"` | `LinkAppearance.Default` | Type (Link) |
| `"Subtle"` | `LinkAppearance.Subtle` | Type (Link) |
| `"Long Abbreviated"` | `DatePickerFormat.LongAbbreviated` | Format (Date Picker) |
| `"Local"` | `DateTimeZone.Local` | DateTimeZone |
| `"Sunday"` | `StartOfWeek.Sunday` | StartOfWeek |
| `"Text"` | `TextInputType.Text` | Type (Text Input) |
| `"Multiline"` | `TextInputType.Multiline` | Type (Text Input) |
| `"Password"` | `TextInputType.Password` | Type (Text Input) |
| `0` | `DecimalPrecision.'0'` | Precision (Number Input) |
| `1` | `DecimalPrecision.'1'` | Precision (Number Input) |
| `2` | `DecimalPrecision.'2'` | Precision (Number Input) |
| `3` | `DecimalPrecision.'3'` | Precision (Number Input) |
| `"Auto"` | `DecimalPrecision.Auto` | Precision (Number Input) |

## See also

- [Migration overview for modern controls](migration-overview.md)
- [Modern controls overview](overview-modern-controls.md)
- Individual control reference documentation
