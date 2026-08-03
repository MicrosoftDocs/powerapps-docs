---
title: Toggle modern control in Power Apps
description: Learn about the details, properties, and examples of the toggle modern control in Power Apps.
author: noazarur-microsoft

ms.topic: reference
ms.component: canvas
ms.date: 08/03/2026
ms.subservice: canvas-maker
ms.author: yogupt


ms.reviewer: mkaur
search.audienceType: 
  - maker
contributors:
  - mduelae
  - noazarur-microsoft
  - yogeshgupta698
  
---
# Toggle modern control in Power Apps

A control that the user can turn on or off by moving the handle.

## Description

A toggle is a user interface element built for modern graphical user interfaces (GUIs) that functions in the same way as a checkbox. Use a toggle when you want an on/off switch metaphor - for example, to enable or disable a setting. The key properties for this control are **Checked**, **Label**, **OnCheck**, **OnSelect**, and **OnUncheck**.
 
## General

**Label** – The text shown next to the toggle. 

**AccessibleLabel** – Label for screen readers. 

**Visible** - Whether a control appears or is hidden. 

## Behavior

**Checked** - The initial value of a control before it's changed by the user. 

**DisplayMode** – Whether the control allows user input (Edit), only displays data (View), or is disabled (Disabled). 

## Size and position 

**LabelPosition** – Where the label appears relative to the toggle. This property uses the typed enum values `LabelPosition.Before` and `LabelPosition.After`. The default is `LabelPosition.After`. 

**[X](../properties-size-location.md)** – The distance between the left edge of a control and the left edge of its parent container (screen if no parent container).

**[Y](../properties-size-location.md)** – The distance between the top edge of a control and the top edge of the parent container (screen if no parent container).

**Width** - The distance between a control's left and right edges. 

**Height** - The distance between a control's top and bottom edges. 

## Style and theme

**BasePaletteColor** - The color palette applied to a control. This color impacts all surfaces of the control that render a theme color. 

**Font** - The name of the family of fonts in which text appears. 

**Size** - The font size of the text that appears on a control. If the value is null or zero, the selected Fluent theme drives the font size. 

**Color** - The color of text in a control. 

**FontWeight** - The weight of the text in a control: **Bold**, **Lighter**, **Normal**, or **Semibold**. 

**FontItalic** - Whether the text in a control is italic. 

**FontUnderline** - Whether a line appears under the text that appears on a control. 

**FontStrikethrough** - Whether a line appears through the text that appears on a control. 

## Additional properties

**Tooltip** – Explanatory text that appears when the user hovers over the control. 

**OnCheck** – Actions to perform when the value of the toggle changes to **true**. 

**OnSelect** – Actions to perform when the user selects a control. 

**OnUncheck** – Actions to perform when the value of the toggle changes to **false**. 

## Recent updates

The updated version of the **Toggle** modern control includes the following improvements and behavior changes.

### Property renames

| Previous property | New property | Notes |
|---|---|---|
| `FontColor` | `Color` | Renamed for consistency across modern controls. |
| `FontSize` | `Size` | Renamed for consistency across modern controls. |

### Enum format changes

Properties that previously accepted plain text strings now use typed Power Fx enums. Typed enums give you IntelliSense autocomplete and compile-time validation, and they help avoid formula errors from misspelled values.

| Property | Previous value | New value |
|---|---|---|
| `LabelPosition` | `"Before"` | `LabelPosition.Before` |
| `LabelPosition` | `"After"` | `LabelPosition.After` |

### Improvements

- **Tooltip support**: A new `Tooltip` property shows explanatory text when the user hovers over the toggle.
- **Improved sizing**: The toggle now fills the full width and height of the control's bounds, so it sizes predictably when you resize the control or place it in a responsive container.
- **Read-only View mode**: When `DisplayMode` is `View`, the toggle now renders as read-only rather than looking disabled, so users can clearly tell the difference between a value they can't change and a control that's unavailable.

## See also

- [Modern controls overview](overview-modern-controls.md)
- [Recent updates to modern controls](modern-control-updates.md)
- [Checkbox modern control](modern-control-checkbox.md)
