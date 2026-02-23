---
title: Info button modern control in canvas apps - Power Apps
description: Learn about the details, properties, and examples of the Info button modern control in Power Apps.
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

# Info button modern control in canvas apps

An interactive information icon that displays detailed content in a flyout when clicked or hovered.

## Description

The **Info button** control provides contextual help and additional information in your canvas apps. When users select or hover over this interactive information icon, it displays detailed content in a flyout panel without disrupting their workflow.

Use this control to:

- Provide contextual help for form fields and complex features
- Display tooltips with additional guidance
- Offer explanatory content without cluttering your app interface
- Enhance user experience with on-demand information

The **Info button** appears as a standard information icon and supports rich text content, customizable styling, and accessibility features.This modern control integrates seamlessly with your app's design system through theme-based colors and flexible positioning options.

Key properties for this control are **Content**, **IconColor**, and **OnSelect**.

## General

**Content** – The information text displayed in the flyout when the user clicks or hovers over the info button icon. Supports plain text and formatted content.

**Visible** – Whether the control appears or is hidden. Use a Power Fx formula to show or hide the control based on app state.

## Behavior

**OnSelect** – How the app responds when the user clicks the info button. Use this property to trigger extra actions beyond showing the flyout, such as logging analytics or updating variables.

**DisplayMode** – Whether the control allows user input (**Edit**), only displays data (**View**), or is disabled (**Disabled**). In **View** mode, the icon is shown but the flyout can't be opened.

## Size and position

**X** – Distance between the left edge of the control and the left edge of its parent container. If there's no parent container, the screen acts as the parent.

**Y** – Distance between the top edge of the control and the top edge of its parent container. If there's no parent container, the screen acts as the parent.

**Width** – Distance between the control's left and right edges. The default value is **32**.

**Height** – Distance between the control's top and bottom edges. The default value is **32**.

**PaddingTop** – Distance between the icon and the top edge of the control.

**PaddingBottom** – Distance between the icon and the bottom edge of the control.

**PaddingLeft** – Distance between the icon and the left edge of the control.

**PaddingRight** – Distance between the icon and the right edge of the control.

## Style and theme

**BasePaletteColor** – The base color that the theme uses to generate the control's color palette. Change this property to apply a different theme color to the control.

**Font** – The name of the font family used for text in the flyout content.

**Size** – The font size of text in the flyout, in points. The default is **15**.

**Color** – The color of text in the flyout content.

**FontWeight** – The weight (thickness) of text in the flyout. Accepts `FontWeight` enum values:

| Value | Description |
|-------|-------------|
| `FontWeight.Bold` | Bold text |
| `FontWeight.Semibold` | Semibold text |
| `FontWeight.Normal` | Normal weight (default) |
| `FontWeight.Lighter` | Lighter weight |

**Italic** – Whether the text in the flyout appears in italic style.

**Underline** – Whether a line appears under the text in the flyout.

**Strikethrough** – Whether a line appears through the middle of the text in the flyout.

**IconColor** – The color of the information icon button itself. Use this value to match your app's theme or draw attention to important information.

## Accessibility

**AccessibleLabel** – A label for screen readers to announce what the info button provides information about. It should describe the purpose or topic of the information, not just "info button".

**ContentLanguage** – The language used for the flyout content. If you don't specify this property, the app settings provide the language.

## Example

The following YAML example shows contextual help buttons for form fields with conditional styling and tooltip content:

```yaml
- EmailInfoButton:
    Control: ModernInformationButton@1.0.0
    Properties:
      Content: ="We'll use this email to send you order confirmations and account notifications. Your email is never shared with third parties."
      IconColor: =Color.Blue
      AccessibleLabel: ="Email address information"
      X: =200
      Y: =100
      Width: =28
      Height: =28

- PasswordInfoButton:
    Control: ModernInformationButton@1.0.0
    Properties:
      Content: '="Password requirements: At least 8 characters, one uppercase letter, one number, and one special character (!@#$%)"'
      IconColor: =Color.Orange
      AccessibleLabel: ="Password requirements"
      X: =200
      Y: =150
      Width: =28
      Height: =28

- GeneralInfoButton:
    Control: ModernInformationButton@1.0.0
    Properties:
      Content: ="Click the info icon to view additional details and helpful tips."
      IconColor: =Color.Gray
      Size: =14
      X: =200
      Y: =200
      Width: =28
      Height: =28
```

## Updates to Info button starting Feb 2026

This updated version of the Info button modern control includes the following improvements and changes.

### Property renames

The following properties are renamed. Update any formulas in your app that reference the old names.

| Previous property | New property |
|-------------------|--------------|
| `FontColor` | `Color` |
| `FontSize` | `Size` |
| `FontItalic` | `Italic` |
| `FontStrikethrough` | `Strikethrough` |
| `FontUnderline` | `Underline` |

### Removed properties

| Removed property | Notes |
|------------------|-------|
| `AcceptsFocus` | Removed. The control now automatically manages focus behavior for accessibility. |

### Bug fixes and improvements

- **Content expansion fixed**: The information flyout background now properly expands to fit all content. Previously, long text could be clipped or overflow the flyout.
- **Improved reliability**: Resolved intermittent crashes that occurred when you clicked the info button in certain scenarios.
- **Simplified properties**: Streamlined property organization with most styling properties now in the **Design** section for better discoverability.
- **Consistent styling**: Font and color properties now consistently apply to both the icon and flyout content.

## Best practices

- **Keep content concise**: While the flyout can display lengthy text, aim for two to three short sentences for better user experience.
- **Use accessible labels**: Always provide descriptive **AccessibleLabel** text that explains what information the button provides.
- **Strategic placement**: Position info buttons next to form fields, labels, or unfamiliar terms where users might need clarification.
- **Consistent iconcolor**: Use consistent colors across your app to help users recognize info buttons quickly.
- **Mobile considerations**: Ensure info buttons are large enough to tap easily on mobile devices (minimum 32x32 pixels).

## See also

- [Modern controls overview](overview-modern-controls.md)
- [Size and location properties](../properties-size-location.md)
