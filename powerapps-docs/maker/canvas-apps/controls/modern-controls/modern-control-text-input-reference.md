---
title: Text Input modern control in canvas apps - Power Apps
description: Learn about the details, properties, and examples of the Text Input modern control in Power Apps.
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

# Text Input modern control in canvas apps

A text input field for capturing single-line or multi-line text, with support for password masking and search modes.

## Description

Use the **Text Input** control to capture text input from users with flexible formatting options. The control supports single-line text, multi-line text areas, password fields with masking, and search input with appropriate styling. Key properties for this control are **Text**, **Placeholder**, **Type**, and **TriggerOutput**.

> [!NOTE]
> This article describes the Text Input modern control. For information about migrating from the previous version, see [Migrate to the Text Input modern control](text-input-migration.md).

## General

**Default** – The initial text displayed when the control first loads. Use this to set a default value before user interaction.

**Text** – The current text value in the control (output property). This is what you reference in formulas to get the user's entered text.

**Placeholder** – Hint text displayed in the input field when it's empty. Use this to guide users on what to enter. Default is **"Enter text"**.

**Visible** – Whether the control appears or is hidden. Use a Power Fx formula to show or hide the control based on app state.

## Behavior

**OnChange** – How the app responds when the user changes the text. This event fires when the user moves focus away from the control (on blur), not on every keystroke. This improves performance and prevents issues with rapid formula execution.

**OnSelect** – How the app responds when the user clicks or taps inside the control.

**Type** – The input mode for the text field. Accepts `TextInputType` enum values:

| Value | Description |
|-------|-------------|
| `TextInputType.Text` | Standard single-line text input (default) |
| `TextInputType.Multiline` | Multi-line text area that allows line breaks |
| `TextInputType.Password` | Password field that masks characters as *** |
| `TextInputType.Search` | Search input with appropriate styling |

**TriggerOutput** – Controls when the **Text** output property updates. Accepts `TriggerOutput` enum values:

| Value | Description |
|-------|-------------|
| `TriggerOutput.OnKeypress` | Updates on every keystroke (default) |
| `TriggerOutput.OnBlur` | Updates only when focus leaves the control |
| `TriggerOutput.Delayed` | Updates after a short delay (used in forms) |

> [!NOTE]
> When added to a form, **TriggerOutput** automatically defaults to **Delayed** for better form performance.

**MaxLength** – The maximum number of characters allowed in the input field. Users cannot type beyond this limit.

**Required** – Whether the user must enter text before submitting a form. When `true`, the control shows validation styling if left empty.

**ValidationState** – The visual validation state of the control. Accepts `ValidationState` enum values:

| Value | Description |
|-------|-------------|
| `ValidationState.None` | No validation styling (default) |
| `ValidationState.Error` | Shows error styling (red border) |

**DisplayMode** – Whether the control allows user input (**Edit**), only displays data (**View**), or is disabled (**Disabled**). In **View** mode, the text is shown but cannot be edited (truly read-only).

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

**BasePaletteColor** – The base color used by the theme to generate the control's color palette. Changes this property to apply a different theme color to the control.

**Font** – The name of the font family in which text appears.

**Size** – The font size of the text, in points.

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

**AccessibleLabel** – A label for screen readers to announce what the input field is for. Should describe the type of text expected (e.g., "Customer name" or "Feedback comments").

**ContentLanguage** – The language used for the input text. Inherits from app settings if not specified.

## Example

The following YAML example shows text input controls with various input types:

```yaml
- NameInput:
    Control: ModernTextInput@1.0.0
    Properties:
      Placeholder: ="Enter your full name"
      Type: =TextInputType.Text
      TriggerOutput: =TriggerOutput.OnKeypress
      Required: =true
      Appearance: =Appearance.FilledDarker
      AccessibleLabel: ="Full name, required field"
      X: =40
      Y: =100
      Width: =300
      Height: =32

- EmailInput:
    Control: ModernTextInput@1.0.0
    Properties:
      Placeholder: ="you@company.com"
      Type: =TextInputType.Text
      TriggerOutput: =TriggerOutput.OnKeypress
      MaxLength: =100
      Required: =true
      AccessibleLabel: ="Email address, required field"
      X: =40
      Y: =150
      Width: =300
      Height: =32

- PasswordInput:
    Control: ModernTextInput@1.0.0
    Properties:
      Placeholder: ="At least 8 characters"
      Type: =TextInputType.Password
      TriggerOutput: =TriggerOutput.OnKeypress
      MaxLength: =50
      Required: =true
      AccessibleLabel: ="Password, must be at least 8 characters"
      X: =40
      Y: =200
      Width: =300
      Height: =32

- CommentsInput:
    Control: ModernTextInput@1.0.0
    Properties:
      Default: =""
      Placeholder: ="Tell us more about your inquiry..."
      Type: =TextInputType.Multiline
      TriggerOutput: =TriggerOutput.OnBlur
      MaxLength: =500
      Align: =Align.Left
      AccessibleLabel: ="Additional comments, optional, maximum 500 characters"
      X: =40
      Y: =250
      Width: =300
      Height: =120

- SearchInput:
    Control: ModernTextInput@1.0.0
    Properties:
      Placeholder: ="Search..."
      Type: =TextInputType.Search
      TriggerOutput: =TriggerOutput.Delayed
      Appearance: =Appearance.Outline
      AccessibleLabel: ="Search by name or description"
      X: =40
      Y: =390
      Width: =300
      Height: =32
```

## What's new in this version

This new Text Input modern control includes the following improvements:

- **OnChange optimization**: The **OnChange** event now fires only when the user leaves the field (on blur), not on every keystroke. This dramatically improves performance and prevents issues with rapid formula execution.
- **TriggerOutput flexibility**: The **TriggerOutput** property now defaults to **OnKeypress** for immediate updates, with **Delayed** used automatically in forms for better performance.
- **Default property**: New **Default** property allows you to set an initial value when the control loads.
- **Password preview**: Password fields now show masked characters (***) even in preview mode, making it easier to design secure forms.
- **DisplayMode.View fixed**: When set to **View** mode, the control is now truly read-only. Previously, users could still edit the text.
- **Null handling improved**: Blank or null values now properly return empty strings instead of null, preventing formula errors.
- **Multiline overflow fixed**: Multi-line text areas no longer have overflow issues when users press Enter to create new lines.
- **OnChange tabbing fixed**: **OnChange** no longer fires when users tab through fields without making changes.
- **Border rendering fixed**: Borders now render correctly even when control height is less than 32 pixels.
- **Color palette override**: The **BasePaletteColor** property in the property panel now properly overrides the global theme.

## Best practices

- **Clear placeholders**: Use **Placeholder** to show example text or formatting hints (e.g., "MM/DD/YYYY" for dates).
- **Appropriate type**: Use **Type** appropriately - **Password** for sensitive data, **Multiline** for long text, **Search** for search boxes.
- **MaxLength validation**: Set **MaxLength** to prevent users from entering too much text, especially for database fields with character limits.
- **TriggerOutput consideration**: Use **OnKeypress** for immediate feedback (search, filters), **OnBlur** for validation, **Delayed** for expensive operations.
- **Required fields**: Mark required fields clearly with **Required** and provide visual feedback with **ValidationState**.
- **Accessible labels**: Always provide descriptive **AccessibleLabel** text that explains what text to enter.
- **OnChange efficiency**: Since **OnChange** fires on blur (not every keystroke), it's safe to use for data updates and validations without performance concerns.
- **Character counters**: For fields with **MaxLength**, consider showing a character count to help users stay within limits.

## Limitations

- The control border may be cut off or render incorrectly when height is set below 32 pixels.
- MaxLength property may not be available in all scenarios (implementation in progress).

## See also

- [Migrate to the Text Input modern control](text-input-migration.md)
- [Modern controls overview](overview-modern-controls.md)
- [Size and location properties](../properties-size-location.md)
