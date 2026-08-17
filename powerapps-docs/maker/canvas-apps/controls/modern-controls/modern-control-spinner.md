---
title: "Spinner Modern Control in Canvas Apps: Properties and Examples"
description: "Discover how to use the Spinner modern control in Power Apps canvas apps. Learn key properties, sizes, styling options, and examples to show loading and in-progress states."
author: yogeshgupta698
ms.topic: reference
ms.custom: canvas
ms.date: 08/17/2026
ms.subservice: canvas-maker
ms.author: yogupt
ms.reviewer: mkaur
search.audienceType:
  - maker
contributors:
  - mduelae
  - yogeshgupta698
  - noazarur-microsoft
---

# Spinner modern control in canvas apps

Displays state in motion, such as loading a page or table.

## Description

Use the **Spinner** modern control to display loading scenarios where an action is in progress. The control communicates an indeterminate wait, and you show or hide it based on the loading state of your app. Key properties for this control are **Label**, **Appearance**, and **SpinnerSize**.

The Spinner is a display-only control. For progress that you can measure as a percentage, use the [Progress Bar modern control](modern-control-progress-bar.md).

> [!NOTE]
> This article describes the updated Spinner modern control. For information about what changed from the previous version, see [Recent updates](#recent-updates).

## General

**Label** – The label next to the spinner, such as `"Loading records..."`. The label slot receives the styling related to the text associated with the spinner.

**AccessibleLabel** – Label read by screen readers. When not set, the control uses the **Label** value. Describe the operation in progress, for example `"Loading customer records"`.

**Visible** – Whether the control appears or is hidden. Set this property to a Boolean value that represents the loading state.

## Behavior

**OnChange** – Actions to perform when a property of the spinner changes.

**DisplayMode** – Whether the control allows user input (**Edit**), only displays data (**View**), or is disabled (**Disabled**). The spinner doesn't accept user input, so this property primarily affects the visual appearance.

## Size and position

**LabelPosition** – Where the label is positioned relative to the spinner. Accepts `LabelPosition` enum values: `LabelPosition.Before`, `LabelPosition.After` (default), `LabelPosition.Above`, or `LabelPosition.Below`.

**SpinnerSize** – The size of the spinner. Accepts `SpinnerSize` enum values:

| Value | Description |
|-------|-------------|
| `SpinnerSize.Tiny` | Smallest spinner, for inline use in tight spaces. |
| `SpinnerSize.ExtraSmall` | Extra small spinner. |
| `SpinnerSize.Small` | Small spinner. |
| `SpinnerSize.Medium` | Medium spinner. Default. |
| `SpinnerSize.Large` | Large spinner. |
| `SpinnerSize.ExtraLarge` | Extra large spinner. |
| `SpinnerSize.Huge` | Largest spinner, for full-page loading states. |

**[X](../properties-size-location.md)** – Distance between the left edge of the control and the left edge of its parent container (screen if no parent container).

**[Y](../properties-size-location.md)** – Distance between the top edge of the control and the top edge of its parent container (screen if no parent container).

**Width** – Distance between the control's left and right edges.

**Height** – Distance between the control's top and bottom edges.

## Style and theme

**Appearance** – The appearance of the spinner. Accepts `SpinnerAppearance` enum values: `SpinnerAppearance.Primary` (default) for the app's brand colors, or `SpinnerAppearance.Inverted` for use on dark backgrounds.

**SpinnerColor** – The color of the animated spinner arc. An explicit value overrides the color derived from **BasePaletteColor** and **Appearance**.

**TrackColor** – The color of the stationary track behind the animated arc.

**BasePaletteColor** – The color palette applied to a control. This property impacts all surfaces of the control that render a theme color.

**Font** – The name of the family of fonts in which the label appears.

**Size** – The font size of the label. If the value is null or zero, the selected Fluent theme drives the font size.

**Color** – The color of the label text.

**FontWeight** – The weight of the label text. Accepts `FontWeight` enum values: `FontWeight.Bold`, `FontWeight.Semibold`, `FontWeight.Normal` (default), or `FontWeight.Lighter`.

**Italic** – Whether the label text appears in italic style.

**Underline** – Whether a line appears under the label text.

**Strikethrough** – Whether a line appears through the label text.

## Additional properties

**Tooltip** – Explanatory text that appears when the user hovers over the control.

**ContentLanguage** – The display language for the control content, if different from the app language.

## Example

The following YAML example shows a large loading spinner that appears while `varIsLoading` is `true`:

```yaml
- LoadingSpinner:
    Control: ModernSpinner@1.0.0
    Properties:
      Label: ="Loading customer records..."
      AccessibleLabel: ="Loading customer records"
      Visible: =varIsLoading
      SpinnerSize: =SpinnerSize.Large
      Appearance: =SpinnerAppearance.Primary
      LabelPosition: =LabelPosition.Below
      Size: =14
      FontWeight: =FontWeight.Semibold
```

Set the loading variable before and after a data operation so the spinner shows only while work is in progress:

```powerfx
Set(varIsLoading, true);
ClearCollect(colCustomers, Customers);
Set(varIsLoading, false)
```

## Recent updates

The updated version of the **Spinner** modern control includes the following improvements and behavior changes.

### Property renames

The following properties are renamed. Update any formulas in your app that reference the old property names.

| Previous property | New property |
|---|---|
| `FontSize` | `Size` |
| `FontColor` | `Color` |
| `FontItalic` | `Italic` |
| `FontUnderline` | `Underline` |
| `FontStrikethrough` | `Strikethrough` |

### Bug fixes and improvements

- **Updated enums**: `Appearance`, `SpinnerSize`, and `LabelPosition` now use typed Power Fx enums (`SpinnerAppearance`, `SpinnerSize`, and `LabelPosition`) instead of string values, improving IntelliSense and reducing formula errors. `FontWeight` uses the `FontWeight` enum.
- **Tooltip support**: New `Tooltip` property shows explanatory text on hover.
- **Spinner color control**: New `SpinnerColor` and `TrackColor` properties let you style the animated arc and its track independently of the label text.
- **Full font control**: Font properties are now consistent with other modern controls. Use `Font`, `Size`, `Color`, `Italic`, `Underline`, and `Strikethrough`.

## See also

- [Modern controls overview](overview-modern-controls.md)
- [Recent updates to modern controls](modern-control-updates.md)
- [Progress Bar modern control](modern-control-progress-bar.md)
- [Size and location properties](../properties-size-location.md)
