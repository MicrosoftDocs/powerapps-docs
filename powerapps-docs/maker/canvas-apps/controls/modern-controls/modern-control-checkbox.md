---
title: Checkbox modern control in Power Apps
description: Learn about the details, properties, and examples of the checkbox modern control in Power Apps.
author: yogeshgupta698

ms.topic: reference
ms.component: canvas
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
# Checkbox modern control in Power Apps

A control that the user can select or clear to set its value to **true** or **false**.

## Description
The user can specify a Boolean value by using this familiar control that's been used in graphical user interfaces (GUIs) for decades. The key properties for this control are **Checked**, **Label**, **OnCheck**, and **OnUncheck**.

## General

**Label** – The checkbox's label.

**AccessibleLabel** – Label for screen readers.

**Visible** - Whether a control appears or is hidden. 

## Behavior 

**Checked** – The controlled value for the checkbox.

**DisplayMode** – Whether the control allows user input (Edit), only displays data (View), or is disabled (Disabled).

## Size and position 

**[X](../properties-size-location.md)** – The distance between the left edge of a control and the left edge of its parent container (screen if no parent container).

**[Y](../properties-size-location.md)** – The distance between the top edge of a control and the top edge of the parent container (screen if no parent container).

**Width** - The distance between a control's left and right edges. 

**Height** - The distance between a control's top and bottom edges. 

## Style and theme

**BasePaletteColor** - The color palette applied to a control. This color impacts all surfaces of the control that render a theme color. 

**Font** - The name of the family of fonts in which text appears. 

**Size** - The font size of the text that appears on a control. If the value is null or zero, the selected Fluent theme drives the font size. 

**Color** - The color of text in a control. 

**FontWeight** - The weight of the text in a control: Bold, Lighter, Normal, or Semibold. 

**FontItalic** - Whether the text in a control is italic. 

**FontUnderline** - Whether a line appears under the text that appears on a control. 

**FontStrikethrough** - Whether a line appears through the text that appears on a control. 


## Additional properties

**Tooltip** - Explanatory text that appears when the user hovers over the control. 

**OnCheck** - Actions to perform when the user checks the control. 

**OnSelect** - Actions to perform when the user selects a control. 

**OnUncheck** - Actions to perform when the user unchecks the control. 

## Example

The following YAML example shows a checkbox that the user must select to accept terms before continuing:

```yaml
- TermsCheckbox:
    Control: ModernCheckbox@1.0.0
    Properties:
      Label: ="I accept the terms and conditions"
      Checked: =false
      OnCheck: =Set(varTermsAccepted, true)
      OnUncheck: =Set(varTermsAccepted, false)
      Tooltip: ="You must accept the terms to continue"
```

You can reference the checkbox's **Checked** property elsewhere in your app. For example, set a submit button's **DisplayMode** to `=If(TermsCheckbox.Checked, DisplayMode.Edit, DisplayMode.Disabled)` so users can continue only after they select the checkbox.

## Recent updates

The updated version of the **Checkbox** modern control includes the following improvements and behavior changes.

### Property renames

| Previous property | New property | Notes |
|---|---|---|
| `FontColor` | `Color` | Renamed for consistency across modern controls. |
| `FontSize` | `Size` | Renamed for consistency across modern controls. |

### Improvements

- **Tooltip support**: A new `Tooltip` property shows explanatory text when the user hovers over the checkbox.
- **Read-only View mode**: When `DisplayMode` is `View`, the checkbox now renders as read-only rather than looking disabled, so users can clearly tell the difference between a value they can't change and a control that's unavailable.
- **More reliable Checked behavior**: The control now honors a `Checked` default of **true** when the app loads, and the `OnCheck` and `OnUncheck` events fire consistently, including when the checkbox is used inside a gallery.

## See also

- [Modern controls overview](overview-modern-controls.md)
- [Recent updates to modern controls](modern-control-updates.md)
- [Toggle modern control](modern-control-toggle.md)




