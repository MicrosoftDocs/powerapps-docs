---
title: Rating modern control in canvas apps - Power Apps
description: Learn about the details, properties, and examples of the Rating modern control in Power Apps.
author: yogeshgupta698
ms.topic: reference
ms.custom: canvas
ms.date: 06/12/2026
ms.subservice: canvas-maker
ms.author: yogupt
ms.reviewer: mkaur
search.audienceType:
  - maker
---

# Rating modern control in canvas apps

Allow users to provide a star-based rating by selecting icons.

## Description

The **Rating** modern control lets users provide a rating by selecting from a row of icons (stars by default). It supports full and half-step precision, customizable icon shapes, and color theming. Use it for feedback forms, product reviews, satisfaction surveys, or any scenario where users need to express a value on a scale.

Key properties for this control are **Default**, **Max**, **Step**, and **Color**.

## General

**Default** – The initial rating value before the user makes a selection. Resets to this value when `Reset` is triggered. Default is **3**.

**Max** – The maximum number of icons (stars) displayed. Must be a whole number greater than 1. Default is **5**.

**Step** – Whether users can select half-step increments or only whole values. Accepts `RatingStep` enum values:

| Value | Description |
|-------|-------------|
| `RatingStep.Full` | Users can only select whole values. Default. |
| `RatingStep.Half` | Users can select half-step increments (for example, 3.5). |

**AccessibleLabel** – Label read by screen readers. Provide a meaningful description such as `"Rate your experience"`.

## Behavior

**OnChange** – Actions to perform when the user changes the rating value. Use `Self.Value` to read the new value.

**DisplayMode** – Whether the control allows user input (**Edit**), only displays data (**View**), or is disabled (**Disabled**).

**Visible** – Whether the control appears or is hidden.

## Output properties

**Value** – The current rating value selected by the user. Read-only.

## Size and position

**[X](../properties-size-location.md)** – Distance between the left edge of the control and the left edge of its parent container (screen if no parent container).

**[Y](../properties-size-location.md)** – Distance between the top edge of the control and the top edge of its parent container (screen if no parent container).

**Width** – Distance between the control's left and right edges. Default is **200**.

**Height** – Distance between the control's top and bottom edges. Default is **40**.

## Style and theme

**Color** – The fill color of the selected (filled) rating icons. Accepts any color value — `RGBA(r, g, b, a)`, named colors like `Color.Gold`, or formula-driven values. Defaults to the app's brand/theme color.

**Icon** – The icon shape used for rating items. Accepts icon names as a string (for example, `"Star"`, `"Heart"`). The control uses the selected icon for filled items and a dimmed variant for unfilled items. Default is **Star**.

## Additional properties

**Tooltip** – Explanatory text that appears when the user hovers over the control.

## Example

The following YAML example shows a 5-star rating control with gold color and an OnChange action:

```yaml
- FeedbackRating:
    Control: ModernRating@1.0.0
    Properties:
      Default: =3
      Max: =5
      Step: =RatingStep.Full
      Icon: ="Star"
      Color: =RGBA(255, 185, 0, 1)
      AccessibleLabel: ="Rate your experience"
      Tooltip: ="Select 1 to 5 stars"
      OnChange: =Set(varRatingValue, Self.Value)

- RatingLabel:
    Control: ModernText@1.0.0
    Properties:
      Text: =If(varRatingValue >= 4, "Thanks for the great rating!", "We appreciate your feedback.")
      Size: =14
```

### Half-star rating with heart icons

```yaml
- HeartRating:
    Control: ModernRating@1.0.0
    Properties:
      Default: =2.5
      Max: =5
      Step: =RatingStep.Half
      Icon: ="Heart"
      Color: =RGBA(220, 38, 38, 1)
      AccessibleLabel: ="Rate this item"
```

## See also

- [Modern controls overview](overview-modern-controls.md)
- [Classic Rating control](../control-rating.md)
- [Size and location properties](../properties-size-location.md)