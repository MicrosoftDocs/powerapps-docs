---
title: Text modern control in canvas apps - Power Apps
description: Learn about the details, properties, and examples of the Text modern control in Power Apps.
author: yogeshgupta698
ms.topic: reference
ms.custom: canvas
ms.date: 02/17/2026
ms.subservice: canvas-maker
ms.author: yogupt
ms.reviewer: mkaur
search.audienceType:
  - maker
---

# Text modern control in canvas apps

Display text and labels on your app screen.

## Description

Use the **Text** control to display static content, dynamic values, messages, and labels in your canvas app. The control supports rich formatting options including font styling, alignment, and auto-sizing to fit content. Key properties for this control are **Text**, **Size**, and **Color**.

## General

**Text** – The text string to display on the canvas. Supports any text or Power Fx formula that evaluates to a string.

**Visible** – Whether the control appears or is hidden. Use a Power Fx formula to show or hide the control based on app state.

## Behavior

**OnSelect** – How the app responds when the user selects (clicks or taps) the Text control. The control is accessible: **OnSelect** also triggers when the user presses Enter or Space while the control has keyboard focus.

**Wrap** – Whether the text wraps to the next line when it exceeds the control width. When set to `false`, text is clipped at the control boundary.

## Size and position

**[X](../properties-size-location)** – Distance between the left edge of the control and the left edge of its parent container (screen if no parent container).

**[Y](../properties-size-location)** – Distance between the top edge of the control and the top edge of its parent container (screen if no parent container).

**Width** – Distance between the control's left and right edges.

**Height** – Distance between the control's top and bottom edges.

**AutoHeight** – Whether the control automatically increases its height when the text content exceeds the visible area. When **Visible** is `false`, the **Height** output property does not update as text changes.

**Align** – The horizontal alignment of text within the control. Accepts `Align` enum values:

| Value | Description |
|-------|-------------|
| `Align.Left` | Aligns text to the left edge |
| `Align.Center` | Centers text horizontally |
| `Align.Right` | Aligns text to the right edge |
| `Align.Justify` | Stretches text to fill the full width |

**VerticalAlign** – The vertical alignment of text within the control. Accepts `VerticalAlign` enum values:

| Value | Description |
|-------|-------------|
| `VerticalAlign.Top` | Aligns text to the top |
| `VerticalAlign.Middle` | Centers text vertically (default) |
| `VerticalAlign.Bottom` | Aligns text to the bottom |

## Style and theme

**Font** – The name of the font family in which text appears.

**Size** – The font size of the text, in points. Default is **15**.

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

**PaddingTop** – Distance between the text and the top edge of the control.

**PaddingBottom** – Distance between the text and the bottom edge of the control.

**PaddingLeft** – Distance between the text and the left edge of the control.

**PaddingRight** – Distance between the text and the right edge of the control.

**RadiusTopLeft** – The corner radius for the top-left corner of the control.

**RadiusTopRight** – The corner radius for the top-right corner of the control.

**RadiusBottomLeft** – The corner radius for the bottom-left corner of the control.

**RadiusBottomRight** – The corner radius for the bottom-right corner of the control.

## Example

The following YAML example shows a clickable label with styling that can be used for headings or interactive text elements:

```yaml
- TitleLabel:
    Control: ModernText@1.0.0
    Properties:
      Text: ="Welcome to Power Apps"
      X: =40
      Y: =40
      Width: =300
      Height: =50
      Size: =24
      FontWeight: =FontWeight.Bold
      Color: =RGBA(0, 120, 212, 1)
      Align: =Align.Center
      VerticalAlign: =VerticalAlign.Middle

- StatusLabel:
    Control: ModernText@1.0.0
    Properties:
      Text: ="Status: Active"
      X: =40
      Y: =120
      Width: =200
      Height: =40
      Size: =16
      FontWeight: =FontWeight.Semibold
      Color: =Color.Green
      Fill: =RGBA(0, 255, 0, 0.1)
      BorderColor: =Color.Green
      BorderThickness: =2
      RadiusTopLeft: =8
      RadiusTopRight: =8
      RadiusBottomLeft: =8
      RadiusBottomRight: =8
      OnSelect: =Set(varLabelClicked, true)
```

## Updates to Text starting Feb 2026

This updated version of the Text modern control includes the following improvements and changes.

### Property renames

The following properties have been renamed. Update any formulas in your app that reference the old names.

| Previous property | New property |
|-------------------|--------------|
| `FontColor` | `Color` |
| `FontSize` | `Size` |
| `FontItalic` | `Italic` |
| `FontStrikethrough` | `Strikethrough` |
| `FontUnderline` | `Underline` |
| `Weight` | `FontWeight` |
| `BorderRadius` | `RadiusTopLeft`, `RadiusTopRight`, `RadiusBottomLeft`, `RadiusBottomRight` |

### Removed properties

| Removed property | Notes |
|------------------|-------|
| `DisplayMode` | Removed from the property panel. The property still exists for backward compatibility but has no effect. The Text control is display-only; use the **OnSelect** event for interactive behavior. |

### Bug fixes and improvements

- **OnSelect event**: The control now supports an **OnSelect** event, making it possible to trigger actions when a user clicks or taps the text. This event is fully accessible and also responds to keyboard input (Enter or Space).
- **Vertical alignment default**: The default **VerticalAlign** is now `VerticalAlign.Middle` for better visual balance.
- **Auto height improvements**: Fixed scroll bar appearing in portrait mode and auto height not recalculating when the control is hidden.
- **Text scaling**: Fixed an issue where the text control did not scale correctly within containers.
- **Updated command bar**: The authoring command bar and right-click menu now show Font, Font size, Alignment, Font color, and Background color for quick access.
- **Mobile-optimized defaults**: When adding the control in a mobile layout, defaults are automatically adjusted (font size 15, padding 5, width 150, height 32).

## See also

- [Modern controls overview](overview-modern-controls.md)
- [Size and location properties](../properties-size-location.md)
