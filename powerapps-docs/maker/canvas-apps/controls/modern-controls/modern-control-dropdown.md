---
title: Dropdown modern control in canvas apps - Power Apps
description: Learn about the details, properties, and examples of the Dropdown modern control in Power Apps.
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

# Dropdown modern control in canvas apps

Let users pick a single value from a collapsible list.

## Description

The **Dropdown** modern control presents a list of choices in a compact, collapsible format. Users select one item and the list collapses back to a single line. Use the **Dropdown** control when you need users to choose one option from a list of more than seven items, for required fields with a fixed set of choices, or for forms where screen space is limited. For fewer options (two to seven), consider using a [Radio group](modern-controls-radio-group.md) instead. If users need to select multiple items, use a [Combo box](modern-control-combobox.md).

Key properties for this control are **Items**, **Default**, **ValidationState**, and **OnChange**.

> [!NOTE]
> This article describes the updated Dropdown modern control. For information about what changed from the previous version, see [Recent updates](#recent-updates).

On desktop, the updated control opens a **Fluent-themed flyout** that matches the app's visual theme. The previous version opened the browser's HTML `<select>` element, which couldn't be themed. 

## General

**Items** – The source of data that contains the items that appear in the control. Accepts a table, a collection, or an inline array (for example, `["Option A", "Option B", "Option C"]`).

**ItemDisplayText** – A Power Fx formula evaluated for each item in **Items** to determine the text shown in the list. Use `ThisItem` to reference the current item. Defaults to `ThisItem.Value` for string arrays and `ThisItem.Value1` for table data sources. Change this when your data source has a specific column to display (for example, `ThisItem.Name`).

**Default** – The initial selected value before the user makes a change. Set this to a value that exists in **Items** (for example, `="Option A"`). Leave blank for no default selection.

**AccessibleLabel** – Label read by screen readers. Describe the purpose of the dropdown (for example, `"Select a country"`).

**Visible** – Whether the control appears or is hidden.

## Behavior

**OnChange** – Actions to perform when the user changes the selection. Use `Self.Selected.Value` inside the formula to read the newly selected item. For example, `Notify("You selected " & Self.Selected.Value)` displays a message each time the selection changes.

**Required** – Whether the user must make a selection. When **true**, an indicator appears beside the dropdown. Default is **false**.

**DisplayMode** – Whether the control allows user input (**Edit**), only displays data (**View**), or is disabled (**Disabled**).

**ValidationState** – Applies validation styling to the control. Accepts `ValidationState` enum values:

| Value | Description |
|-------|-------------|
| `ValidationState.None` | No validation styling. Default. |
| `ValidationState.Error` | Highlights the control border in red to indicate an error. |

## Size and position

**[X](../properties-size-location.md)** – Distance between the left edge of the control and the left edge of its parent container (screen if no parent container).

**[Y](../properties-size-location.md)** – Distance between the top edge of the control and the top edge of its parent container (screen if no parent container).

**Width** – Distance between the control's left and right edges. Default is **320**.

**Height** – Distance between the control's top and bottom edges. Default is **32**.

**PaddingTop** – Distance between the control content and the top edge of the control.

**PaddingBottom** – Distance between the control content and the bottom edge of the control.

**PaddingLeft** – Distance between the control content and the left edge of the control.

**PaddingRight** – Distance between the control content and the right edge of the control.

## Style and theme

**Appearance** – The visual style of the dropdown field. Accepts `Appearance` enum values:

| Value | Description |
|-------|-------------|
| `Appearance.FilledDarker` | Filled with a slightly darker background. Default. |
| `Appearance.Filled` | Filled with a standard background. |
| `Appearance.Outline` | Outlined border with a transparent background. |

**BasePaletteColor** – The base color used by the theme to generate the control's color palette. Use this value to apply a different theme color to the control.

**Font** – The font family used for the dropdown text.

**Size** – The font size of the dropdown text, in points. Default is **14**.

**Color** – The color of the dropdown text.

**FontWeight** – The weight (thickness) of the dropdown text. Accepts `FontWeight` enum values: `FontWeight.Bold`, `FontWeight.Semibold`, `FontWeight.Normal` (default), `FontWeight.Lighter`.

**Italic** – Whether the dropdown text appears in italic style.

**Underline** – Whether a line appears under the dropdown text.

**Strikethrough** – Whether a line appears through the middle of the dropdown text.

**Fill** – The background fill color of the control.

**BorderColor** – The color of the control's border.

**BorderStyle** – The style of the control's border. Accepts `BorderStyle` enum values: `BorderStyle.Solid`, `BorderStyle.Dashed`, `BorderStyle.Dotted`, or `BorderStyle.None`.

**BorderThickness** – The thickness of the control's border in pixels.

**RadiusTopLeft** – The corner radius for the top-left corner of the control.

**RadiusTopRight** – The corner radius for the top-right corner of the control.

**RadiusBottomLeft** – The corner radius for the bottom-left corner of the control.

**RadiusBottomRight** – The corner radius for the bottom-right corner of the control.

## Additional properties

**ContentLanguage** – The display language for the control content, if different from the app language.

## Output properties

**Selected** – The currently selected item, returned as a record. For a string array, use `Dropdown1.Selected.Value` to read the selected text. For a table data source, use `Dropdown1.Selected.<ColumnName>`.

> [!NOTE]
> **Selected** is an output property. You can reference it in other controls and formulas, but you can't set it directly.

## Examples

### Basic dropdown with inline options

This example creates a required country dropdown with inline validation. When the user hasn't selected a value, the control shows an error state.

```yaml
- CountryDropdown:
    Control: ModernDropdown@1.0.0
    Properties:
      AccessibleLabel: ="Select your country"
      Default: ={Value:"United States"}
      ItemDisplayText: =ThisItem.Value
      Items: =["Australia", "Canada", "United Kingdom", "United States"]
      Required: =true
      ValidationState: =If(IsBlank(CountryDropdown.Selected.Value), ValidationState.Error, ValidationState.None)
      Width: =240   
```

### Dropdown bound to a data source

This example binds the dropdown to a table data source and displays the **Name** column. The **OnChange** action stores the selected record in a variable.

```yaml
- DepartmentDropdown:
    Control: ModernDropdown@1.0.0
    Properties:
      AccessibleLabel: ="Select a department"
      Appearance: =Appearance.Outline
      ItemDisplayText: =ThisItem.Name
      Items: =Departments
      OnChange: =Set(varSelectedDept, Self.Selected)
      Width: =320
```

## Recent updates

The updated version of the **Dropdown** modern control includes the following improvements and behavior changes.

### Property renames

| Previous property | New property | Notes |
|---|---|---|
| `DefaultSelectedItems` | `Default` | Set the initial selection through `Default`. Change any formula referencing `Dropdown1.DefaultSelectedItems` to `Dropdown1.Default`. |
| `FontSize` | `Size` | Renamed to match other modern controls. Default changed from **0** (inherits from theme) to **14**. |
| `BorderRadius` | `RadiusTopLeft`, `RadiusTopRight`, `RadiusBottomLeft`, `RadiusBottomRight` | Split into four independent corner radius properties for greater styling flexibility. |

### Enum format changes

| Property | Previous value | New value |
|---|---|---|
| `Appearance` | `"FilledDarker"` | `Appearance.FilledDarker` |
| `Appearance` | `"Filled"` | `Appearance.Filled` |
| `Appearance` | `"Outline"` | `Appearance.Outline` |
| `ValidationState` | `"None"` | `ValidationState.None` |
| `ValidationState` | `"Error"` | `ValidationState.Error` |

### Bug fixes and improvements

- **Fluent-themed flyout**: On desktop, the dropdown list now opens as a Fluent-themed flyout that matches the app's visual design. The previous version used the browser's HTML `<select>` element, which couldn't be themed. On mobile, both versions use the device-native picker and it remains unchanged.
- **ItemDisplayText**: New property that controls which field of a data source record to show in the list. For string arrays, this property defaults automatically. For table data sources, set this property to the column you want to display (for example, `ThisItem.Name`).
- **Full font control**: New `Font`, `Color`, `FontWeight`, `Italic`, `Underline`, and `Strikethrough` properties give full text styling control, consistent with other modern controls.
- **Updated enums**: `Appearance` and `ValidationState` now use typed Power Fx enums, improving IntelliSense and reducing formula errors.

## Accessibility

**AccessibleLabel** – Set this property to a meaningful description so screen readers can announce the purpose of the dropdown (for example, `"Select your country"`).

**Required** – When set to **true**, screen readers announce the field as required.

Keyboard users can press **Enter** or **Space** to open the dropdown, use **Arrow** keys to move between items, and press **Enter** to confirm a selection.

## Limitations

- The Fluent-themed flyout is available on desktop only. On mobile, the control uses the device-native picker.
- Very large data sources may cause the dropdown list to load slowly. Filter or limit the data where possible.

## See also

- [Modern controls overview](overview-modern-controls.md)
- [Size and location properties](../properties-size-location.md)
