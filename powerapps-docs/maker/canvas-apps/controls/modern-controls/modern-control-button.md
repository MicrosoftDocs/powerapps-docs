---
title: "Button Modern Control in Canvas Apps: Properties and Examples"
description: "Discover how to use the Button modern control in Power Apps canvas apps. Learn key properties, styling options, and implementation examples to trigger actions effectively."
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

# Button modern control in canvas apps

The **Button** modern control provides a clickable element that triggers actions in a canvas app, offering flexible styling and comprehensive interaction capabilities.

## Description

The **Button** modern control provides a clickable element that triggers app logic when selected. Use it for form submissions, navigation, confirmations, and any interaction that requires user input. The control supports icon and text combinations, full font styling, and multiple appearance styles through Fluent theming. Key properties for this control are **Text**, **Appearance**, and **OnSelect**.

> [!NOTE]
> This article describes the updated Button modern control. For information about what changed from the previous version, see [Recent updates](#recent-updates).

## General

**Text** – The label displayed on the button. Supports any text or Power Fx formula that evaluates to a string. Use this property to set or change the button text.

**Visible** – Whether the control appears or is hidden. Use a Power Fx formula to show or hide the button based on app state.

## Behavior

**OnSelect** – Use the **OnSelect** property to define what happens when the button is selected. It's how the app responds when the user selects the button. The control is accessible: **OnSelect** also triggers when the user presses Enter or Space while the control has keyboard focus.

> [!TIP]
> Common OnSelect actions include:
 > - `Navigate(Screen2)` - Navigate to another screen
 > - `SubmitForm(Form1)` - Submit a form
 > - `Set(varName, value)` - Set a variable
 > - `Notify("Message", NotificationType.Success)` - Show a notification
 > - `Patch(DataSource, Record, Updates)` - Update data

**DisplayMode** – Whether the control allows user input (**Edit**), only displays data (**View**), or is disabled (**Disabled**). When **Disabled**, the button is visually dimmed and **OnSelect** doesn't fire.

## Getting started

The **Button** modern control is one of the most commonly used controls in Power Apps. At its core, a button has two essential elements: the text that users see (the **Text** property) and the action that happens when selected (the **OnSelect** property). Once you understand these basics, you can create interactive apps that respond to user input.

### Set button text

To change what text appears on your button, set the **Text** property:

- **In the Properties pane**: Enter text directly in the **Text** field
- **Using a formula**: `Text = "Click Me"` or `Text = "Save " & TextInput1.Text`

### Make buttons interactive

Define what happens when users selects the button using the **OnSelect** property:

1. Select the button in your app.
1. In the Properties pane, find the **OnSelect** property.
1. Enter your Power Fx formula, such as `Navigate(NextScreen)`.

### Configure button properties

Power Apps uses a streamlined approach for editing controls.

- Select the button on the canvas:
  - **Use the Properties pane** on the right to modify basic properties.
  - **Use the formula bar** at the top for advanced formulas.
  - **Switch to Advanced properties** for detailed customization.

## Size and position

**[X](../properties-size-location.md)** – Distance between the left edge of the control and the left edge of its parent container (screen if no parent container).

**[Y](../properties-size-location.md)** – Distance between the top edge of the control and the top edge of its parent container (screen if no parent container).

**Width** – Distance between the control's left and right edges. Default is **96**.

**Height** – Distance between the control's top and bottom edges. Default is **32**.

**Align** – The horizontal alignment of the button content within the control. Accepts `Align` enum values: `Align.Left`, `Align.Center`, `Align.Right`, `Align.Justify`.

**VerticalAlign** – The vertical alignment of the button content. Accepts `VerticalAlign` enum values: `VerticalAlign.Top`, `VerticalAlign.Middle`, `VerticalAlign.Bottom`.

**PaddingTop** – Distance between the button content and the top edge of the control.

**PaddingBottom** – Distance between the button content and the bottom edge of the control.

**PaddingLeft** – Distance between the button content and the left edge of the control.

**PaddingRight** – Distance between the button content and the right edge of the control.

## Style and theme

**Appearance** – The visual style of the button. Accepts `ButtonAppearance` enum values:

| Value | Description |
|-------|-------------|
| `ButtonAppearance.Primary` | Filled button using the brand color. Default. |
| `ButtonAppearance.Secondary` | Subtle filled style, secondary emphasis. |
| `ButtonAppearance.Outline` | Outlined button with no background fill. |
| `ButtonAppearance.Subtle` | Minimal styling, no border or fill. |
| `ButtonAppearance.Transparent` | No visible styling; blends with the background. |

**BasePaletteColor** – The base color used by the theme to generate the control's color palette. Change this property to apply a different theme color to the button.

**Icon** – The Fluent icon name to display alongside the button text (for example, `"Add"`, `"Save"`, `"Delete"`). Leave blank for a text-only button.

**IconStyle** – Whether the icon renders in outline or filled style. Accepts `IconStyle` enum values: `IconStyle.Outline` (default) or `IconStyle.Filled`.

**IconRotation** – Rotation in degrees applied to the icon. Default is **0**.

**Layout** – The position of the icon relative to the button text. Accepts `ButtonLayout` enum values:

| Value | Description |
|-------|-------------|
| `ButtonLayout.IconBefore` | Icon appears to the left of the text. Default. |
| `ButtonLayout.IconAfter` | Icon appears to the right of the text. |
| `ButtonLayout.IconOnly` | Only the icon is shown; no text label. |

**Font** – The font family used for the button label.

**Size** – The font size of the button label, in points.

**Color** – The color of the button label text.

**FontWeight** – The weight (thickness) of the button label. Accepts `FontWeight` enum values: `FontWeight.Bold`, `FontWeight.Semibold`, `FontWeight.Normal` (default), `FontWeight.Lighter`.

**Italic** – Whether the button label appears in italic style.

**Underline** – Whether a line appears under the button label text.

**Strikethrough** – Whether a line appears through the middle of the button label text.

**BorderColor** – The color of the control's border.

**BorderStyle** – The style of the control's border. Accepts `BorderStyle` enum values: `BorderStyle.Solid`, `BorderStyle.Dashed`, `BorderStyle.Dotted`, or `BorderStyle.None`.

**BorderThickness** – The thickness of the control's border in pixels.

**RadiusTopLeft** – The corner radius for the top-left corner of the control.

**RadiusTopRight** – The corner radius for the top-right corner of the control.

**RadiusBottomLeft** – The corner radius for the bottom-left corner of the control.

**RadiusBottomRight** – The corner radius for the bottom-right corner of the control.

## Additional properties

**AccessibleLabel** – Label read by screen readers. Provide a meaningful description when the button label alone isn't sufficient (for example, when using an icon-only button).

**Tooltip** – Explanatory text that appears when the user hovers over the button.

**ContentLanguage** – The display language for the control content, if different from the app language.

## Example

The following YAML example shows a submit button and a cancel button with OnSelect actions:

```yaml
- SubmitButton:
    Control: ModernButton@1.0.0
    Properties:
      Text: ="Submit"
      OnSelect: |
        SubmitForm(DataForm1);
        Navigate(SuccessScreen)
      Appearance: =ButtonAppearance.Primary
      Icon: ="Checkmark"
      IconStyle: =IconStyle.Outline
      Layout: =ButtonLayout.IconBefore
      AccessibleLabel: ="Submit the form"
      Tooltip: ="Submit your response"
      Width: =120
      Height: =36

- CancelButton:
    Control: ModernButton@1.0.0
    Properties:
      Text: ="Cancel"
      OnSelect: =Navigate(HomeScreen)
      Appearance: =ButtonAppearance.Outline
      Width: =120
      Height: =36
```

### Common button patterns

Here are typical button implementations:

**Navigation button:**
```powerfx
OnSelect = Navigate(DetailsScreen, ScreenTransition.Fade)
```

**Data submission:**
```powerfx
OnSelect = SubmitForm(Form1); Notify("Data saved!", NotificationType.Success)
```

**Variable update:**
```powerfx
OnSelect = Set(IsVisible, !IsVisible)
```

**Confirmation dialog:**
```powerfx
OnSelect = If(
    Confirm("Are you sure you want to delete this item?"),
    Remove(Collection1, ThisItem)
)
```

## Recent updates

The updated version of the **Button** modern control includes the following improvements and behavior changes.

### Property renames

The following properties are renamed. Update any formulas in your app that reference the old property names.

| Previous property | New property |
|---|---|
| `FontSize` | `Size` |
| `FontColor` | `Color` |
| `FontItalic` | `Italic` |
| `FontUnderline` | `Underline` |
| `FontStrikethrough` | `Strikethrough` |
| `BorderRadius` | `RadiusTopLeft`, `RadiusTopRight`, `RadiusBottomLeft`, `RadiusBottomRight` |

### Removed properties

| Removed property | Notes |
|---|---|
| `AcceptsFocus` | Removed. The modern Button control always accepts keyboard focus. No replacement needed. |

### Bug fixes and improvements

- **Updated enums**: `Appearance`, `Layout`, and `IconStyle` now use typed Power Fx enums (`ButtonAppearance`, `ButtonLayout`, `IconStyle`) instead of string values, improving IntelliSense and reducing formula errors.
- **Tooltip support**: New `Tooltip` property shows explanatory text on hover.
- **Border improvements**: Added `BorderStyle` and `BorderThickness` for more precise border control. Four corner-specific properties replace `BorderRadius` for independent corner control.
- **Full font control**: Font properties are now consistent with other modern controls. Use `Font`, `Size`, `Color`, `Italic`, `Underline`, and `Strikethrough`.

## See also

- [Modern controls overview](overview-modern-controls.md)
- [Size and location properties](../properties-size-location.md)
