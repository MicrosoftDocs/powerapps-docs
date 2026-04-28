---
title: Data Grid modern control in canvas apps - Power Apps
description: Learn how to use the Data Grid modern control in canvas apps to display, search, sort, and select records efficiently. Start building today.
author: yogeshgupta698
ms.topic: reference
ms.custom: canvas
ms.date: 04/28/2026
ms.subservice: canvas-maker
ms.author: yogupt
ms.reviewer: mkaur
search.audienceType:
  - maker
---

# Data Grid modern control in canvas apps

Display records from a data source in a scrollable, sortable, and searchable grid.

## Description

The **Data Grid** modern control displays records in a column-and-row layout built on Fluent UI. It supports virtual scrolling for large datasets, optional search filtering, sortable columns, and selectable rows. You configure columns as subcontrols, and they support multiple types including text, number, phone, email, URL, and button. Use this control when you need a high-performance, data-dense view of tabular data with built-in interaction. Key properties for this control are **Items**, **Searchable**, **Sortable**, and **SelectMultiple**.

> [!NOTE]
> The **Data Grid** control is a new control separate from the existing **Table** control. It's not a replacement for the **Table** control.

## General

**Items** – The data source for the grid. Accepts a Dataverse table, collection, or inline table expression.

**Visible** – Whether the control appears or is hidden.

## Behavior

**Searchable** – Whether a search bar appears above the grid. When **true**, users can type to filter visible rows. The current search string is exposed through the **SearchText** output property. The default value is **false**.

**Sortable** – Whether users can sort by a column by selecting its header. The default value is **false**.

**SelectMultiple** – Whether users can select more than one row at a time. The default value is **false**.

**ShowHeaders** – Whether column header labels appear at the top of the grid. The default value is **true**.

**ShowSelector** – Whether a checkbox appears at the start of each row for row selection. The default value is **false**.

**Required** – Whether the user must select at least one row.

**DisplayMode** – Whether the control allows user input (**Edit**), only displays data (**View**), or is disabled (**Disabled**).

## Size and position

**[X](../properties-size-location.md)** – Distance between the left edge of the control and the left edge of its parent container (screen if no parent container).

**[Y](../properties-size-location.md)** – Distance between the top edge of the control and the top edge of its parent container (screen if no parent container).

**Width** – Distance between the control's left and right edges. The default value is **792**.

**Height** – Distance between the control's top and bottom edges. The default value is **475**.

## Style and theme

**BasePaletteColor** – The base color that the theme uses to generate the control's color palette.

**Font** – The font family used for the grid text.

**Size** – The font size of the grid text, in points. The default is **14**.

**Color** – The color of the grid text.

## Output properties

**Selected** – The most recently selected row, returned as a record.

**SelectedItems** – All currently selected rows, returned as a table. Use this property when **SelectMultiple** is **true**.

**SearchText** – The current value the user types in the search bar. This property is only available when **Searchable** is **true**.

## Configuring columns

The Data Grid uses **Data Grid Column** sub-controls to define how each column appears and what data it shows. You add columns when you connect a data source and configure fields in the authoring panel. Columns are locked by default. Select a column and choose **Unlock** to customize it.

### Column properties

**Header Text** – The label shown in the column header.

**Visible** – Whether the column appears in the grid.

**Width** – The width of the column in pixels. Default is **150**.

**Text** – (Text, Phone, Email, URL, Button columns) A Power Fx formula evaluated per row that returns the value to display. Evaluated in the context of `ThisItem` (for example, `ThisItem.'Full Name'`).

**Image** – (Image column) A Power Fx formula evaluated per row that returns an image value or URL.

**Icon** – The Fluent icon shown in the column cell.

**AccessibleLabel** – (Image column) The accessible label for the image, read by screen readers.

### Column types

| Column type | Description |
|-------------|-------------|
| Text column | Displays a text value. |
| Number column | Displays a numeric value. |
| Phone column | Displays a phone number. |
| Email column | Displays an email address as a link. |
| URL column | Displays a URL as a hyperlink. |
| Button column | Displays a button in each row cell. |

## Example

The following YAML example shows a searchable grid with two text columns:

```yaml
- DataGrid2:
    Control: ModernDataGrid@1.1.0
    Properties:
      Items: |-
        =Table({Name: "Alice Contoso", Department: "Sales"}, {Name: "Bob Fabrikam", Department: "Engineering"}, {Name: "Carol Northwind", Department: "Marketing"})
      Searchable: =true
      X: =40
      Y: =40
    Children:
      - Department_Column1:
          Control: ModernDataGridColumn@1.1.0
          Variant: Textual
          IsLocked: true
          Properties:
            FieldDisplayName: ="Department"
            Text: =ThisItem.Department
      - Name_Column1:
          Control: ModernDataGridColumn@1.1.0
          Variant: Textual
          IsLocked: true
          Properties:
            FieldDisplayName: ="Name"
            Text: =ThisItem.Name
```

## See also

- [Modern controls overview](overview-modern-controls.md)
- [Table modern control](modern-control-table.md)
- [Size and location properties](../properties-size-location.md)
