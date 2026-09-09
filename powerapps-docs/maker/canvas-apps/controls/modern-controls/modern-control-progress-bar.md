---
title: "Progress Bar Modern Control in Canvas Apps: Properties and Examples"
description: "Discover how to use the Progress bar modern control in Power Apps canvas apps. Learn its properties, styling options, accessibility behavior, and examples."
author: yogeshgupta698
ms.topic: reference
ms.custom: canvas
ms.date: 09/08/2026
ms.subservice: canvas-maker
ms.author: yogupt
ms.reviewer: joshuapa
search.audienceType:
  - maker
contributors:
  - mduelae
  - yogeshgupta698
  - noazarur-microsoft
---

# Progress bar modern control in canvas apps

The **Progress bar** modern control shows the progress of an operation in a canvas app.

## Description

Use the **Progress bar** control to show measurable progress, such as completed steps or uploaded records. When progress can't be measured, use the indeterminate state to show that an operation is still running. The control is display-only and doesn't accept user input. Key properties are **Value**, **Max**, and **Indeterminate**.

> [!NOTE]
> This article describes the updated Progress bar modern control. For information about what changed from the previous version, see [Recent updates](#recent-updates).

## General

**Value** – The current progress value. The control displays this value relative to **Max**. Values below zero display as zero, and values above **Max** display as complete. The default is **50**.

**Max** – The value that represents completion. The default is **100**.

**AccessibleLabel** – A label read by screen readers. Describes the operation whose progress is displayed, such as `"Uploading invoices"`.

**Visible** – Whether the control appears or is hidden.

## Behavior

**Indeterminate** – Whether the control shows an animated indeterminate state instead of measurable progress. When this property is `true`, **Value** and **Max** aren't used to determine the displayed progress. The default is `false`.

**DisplayMode** – Whether the control uses the **Edit**, **View**, or **Disabled** visual state. The Progress bar is display-only in every mode and doesn't accept user input.

## Size and position

**[X](../properties-size-location.md)** – Distance between the left edge of the control and the left edge of its parent container (screen if no parent container).

**[Y](../properties-size-location.md)** – Distance between the top edge of the control and the top edge of its parent container (screen if no parent container).

**Width** – Distance between the control's left and right edges. The default is **200**.

**Height** – Distance between the control's top and bottom edges. The default is **8**.

## Style and theme

**ProgressColor** – The semantic color of the progress indicator. Accepts `ProgressColor` enum values:

| Value | Description |
|---|---|
| `ProgressColor.Brand` | Uses the app's brand color. Default. |
| `ProgressColor.Success` | Indicates successful or positive progress. |
| `ProgressColor.Warning` | Indicates a warning state. |
| `ProgressColor.Error` | Indicates an error or critical state. |

**Thickness** – The thickness of the progress indicator. Accepts `ProgressThickness` enum values:

| Value | Description |
|---|---|
| `ProgressThickness.Medium` | Medium thickness. Default. |
| `ProgressThickness.Large` | Large thickness. |

**Shape** – The corner style of the progress indicator. Accepts `ProgressShape` enum values:

| Value | Description |
|---|---|
| `ProgressShape.Rounded` | Rounded ends. Default. |
| `ProgressShape.Square` | Square corners. |

## Additional properties

**Tooltip** – Explanatory text that appears when a user hovers over the control.

**ContentLanguage** – The display language for the control's accessible content, if different from the app language.

## Accessibility

The control exposes progress-bar semantics to assistive technologies. In the determinate state, screen readers receive the current value, minimum value, and maximum value. In the indeterminate state, the current value isn't announced.

Set **AccessibleLabel** to identify the operation whose progress is shown. The control isn't keyboard interactive because it doesn't accept user input.

## Example

The following self-contained YAML example shows 65 percent completion:

```yaml
- CompletionProgress:
    Control: ModernProgressBar@1.0.0
    Properties:
      Value: =65
      Max: =100
      Indeterminate: =false
      ProgressColor: =ProgressColor.Brand
      Thickness: =ProgressThickness.Large
      Shape: =ProgressShape.Rounded
      AccessibleLabel: ="65 percent complete"
      Tooltip: ="Progress: 65 percent"
```

## Limitations

- The control is horizontal only.
- The control doesn't display a label or percentage. Use a separate Text control when visible text is needed.
- The control is display-only and doesn't expose behavior events.

## Recent updates

The updated version of the **Progress bar** modern control includes the following improvements and behavior changes.

### Removed properties

| Removed property | Notes |
|---|---|
| `OnChange` | Not available in the updated control. The Progress bar is display-only and its value is driven by a formula. |

### Bug fixes and improvements

- **Updated enums**: `ProgressColor`, `Thickness`, and `Shape` now use the typed `ProgressColor`, `ProgressThickness`, and `ProgressShape` enums instead of string values, improving IntelliSense and reducing formula errors.
- **Tooltip support**: New `Tooltip` property shows explanatory text on hover.
- **Native implementation**: The control is now a native control based on Fluent UI, with progress-bar semantics for assistive technologies.

## See also

- [Modern controls overview](overview-modern-controls.md)
- [Recent updates to modern controls](modern-control-updates.md)
- [Size and location properties](../properties-size-location.md)
