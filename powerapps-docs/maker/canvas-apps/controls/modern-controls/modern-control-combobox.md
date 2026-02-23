---
title: Combo box modern control in canvas apps - Power Apps
description: Learn about the details, properties, and examples of the Combo box modern control in Power Apps.
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

# Combo box modern control in canvas apps

A searchable, multi-select dropdown control for selecting one or more items from a list.

## Description

Use the **Combo box** control to let users search and select items from a large list of options. The control supports single or multiple selection, type-ahead search, and custom item display formulas. Key properties for this control are **Items**, **DefaultSelectedItems**, and **SelectMultiple**.

## General

**Items** – The data source that contains the items shown in the combo box. Can be a collection, table, or Power Fx formula that returns a table.

**ItemDisplayText** – A formula that determines what text to display for each item in the dropdown list. Use `ThisItem` to reference the current item. Example: `ThisItem.DisplayName` or `ThisItem.Value1`.

**DefaultSelectedItems** – The initial item(s) selected in the control before the user makes a change. Must be a table of records from the **Items** data source.

**InputTextPlaceholder** – Hint text that appears in the input field when no items are selected. Default is **"Find items"**.

**Visible** – Whether the control appears or is hidden. Use a Power Fx formula to show or hide the control based on app state.

## Behavior

**SelectMultiple** – Whether users can select multiple items. When `true`, users can select multiple items and each selected item can be toggled on or off by clicking it again. When `false`, only one item can be selected at a time. Default is **true**.

**IsSearchable** – Whether the search box is enabled. When `true`, users can type to filter the list. When `false`, the control acts as a simple dropdown without search. Default is **true**.

**OnChange** – How the app responds when the user selects or deselects an item. This event fires immediately on every selection or deselection, making it ideal for real-time filtering or dependent dropdowns.

**AllowMultipleSelection** – (Display property) A toggle that controls whether users can select multiple items. Maps to the **SelectMultiple** property.

**AllowSearching** – (Display property) A toggle that controls whether search is enabled. Maps to the **IsSearchable** property.

**DisplayMode** – Whether the control allows user input (**Edit**), only displays data (**View**), or is disabled (**Disabled**). In **View** mode, the selection is shown but cannot be changed.

**DelayOutput** – When set to `true`, delays the **OnChange** event until the user clicks outside the control or presses Enter. When `false`, **OnChange** fires immediately on each selection. Default is **false**.

## Data

**SelectedItems** – (Output) A table of records representing the items currently selected by the user. Use this property to reference the user's selections in formulas.

**Selected** – (Output) When **SelectMultiple** is `false`, returns the single selected item as a record. When **SelectMultiple** is `true`, returns the first selected item.

**SearchText** – (Output) The current text typed by the user in the search box. Use this to create custom filtering logic or to track search behavior.

**MultiValueDelimiter** – The separator character used when displaying multiple selected items in the input field. Default is **", "** (comma and space).

## Validation

**Required** – Whether the control must have at least one item selected before the form can be submitted. When `true`, the control shows a validation error if empty.

**ValidationState** – The current validation state of the control. Accepts `ValidationState` enum values:

| Value | Description |
|-------|-------------|
| `ValidationState.Error` | The control value has an error |
| `ValidationState.None` | No validation applied (default) |

## Size and position

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
| `Appearance.FilledDarker` | Filled with darker background |
| `Appearance.Outline` | Outline style with border |

Default is `Appearance.FilledDarker`.

**BasePaletteColor** – The base color used by the theme to generate the control's color palette. Changes this property to apply a different theme color to the control.

**Font** – The name of the font family in which text appears.

**Size** – The font size of the text, in points. Default is **14**.

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

## Example

The following YAML example shows combo box controls with single and multi-select modes:

```yaml
- DepartmentComboBox:
    Control: ModernCombobox@1.0.0
    Properties:
      Items: =["Engineering", "Sales", "Marketing", "Support"]
      InputTextPlaceholder: ="Select a department..."
      SelectMultiple: =false
      IsSearchable: =true
      Required: =true
      X: =40
      Y: =100
      Width: =320
      Height: =32

- TeamMemberComboBox:
    Control: ModernCombobox@1.0.0
    Properties:
      Items: =["Alice Smith", "Bob Johnson", "Carol Williams", "David Brown"]
      InputTextPlaceholder: ="Select team members..."
      SelectMultiple: =true
      IsSearchable: =true
      MultiValueDelimiter: ="; "
      X: =40
      Y: =150
      Width: =320
      Height: =32
```

## Accessibility

**AccessibleLabel** – A label for screen readers to announce what the control is for. Should describe the purpose of the combo box, not the current selection.

**TabIndex** – The tab order of the control relative to other controls. Controls with lower **TabIndex** values receive focus before controls with higher values.

## Updates to Combo box starting Feb 2026

This updated version of the Combo box modern control includes the following improvements and changes.

### Property renames

The following properties have been renamed. Update any formulas in your app that reference the old names.

| Previous property | New property |
|-------------------|--------------|
| `FontColor` | `Color` |
| `FontSize` | `Size` |
| `FontItalic` | `Italic` |
| `FontStrikethrough` | `Strikethrough` |
| `FontUnderline` | `Underline` |
| `BorderRadius` | `RadiusTopLeft`, `RadiusTopRight`, `RadiusBottomLeft`, `RadiusBottomRight` |

### Enum format changes

The following properties now require typed enum syntax instead of plain string values:

| Property | Previous format | New format |
|----------|----------------|------------|
| `Appearance` | `"FilledDarker"` | `Appearance.FilledDarker` |
| `ValidationState` | `"None"` | `ValidationState.None` |

### Behavioral changes

- **SelectMultiple defaults to true**: The **SelectMultiple** property now defaults to `true`. If your app requires single selection, explicitly set `SelectMultiple = false`.
- **Toggle selection behavior**: Clicking a selected item now unselects it, making it easier to remove selections without clearing the entire list.
- **Immediate OnChange firing**: The **OnChange** event now fires immediately on every selection or deselection, enabling real-time filtering and dependent dropdowns. Set `DelayOutput = true` if you need the previous delayed behavior.
- **Search text clears on selection**: When an item is selected, the search text automatically clears.
- **Reset() includes SearchText**: The `Reset()` function now clears both the selection and the search text.

### Removed and replaced properties

| Removed property | Replacement | Notes |
|------------------|-------------|-------|
| `TriggerOutput` | `DelayOutput` | `TriggerOutput = "Keypress"` → `DelayOutput = false`. `TriggerOutput = "FocusOut"` → `DelayOutput = true`. |
| `Fields` | `ItemDisplayText` | Replace `Fields = ["FieldName"]` with `ItemDisplayText = ThisItem.FieldName`. |

### Other improvements

- **Improved data handling**: Better support for Dataverse Many-to-One relationships and increased item limit handling (previously limited to ~800 items).
- **Mobile-optimized defaults**: When adding the control in a mobile layout, defaults are automatically adjusted (font size 24, width 560, height 64).

## Limitations

- The control is optimized for lists with up to several thousand items. For very large datasets (10,000+ items), consider using server-side filtering with the **SearchText** output property.
- Chevron and checkbox icons do not scale with font size in the current version.

## See also

- [Modern controls overview](overview-modern-controls.md)
- [Size and location properties](../properties-size-location.md)
