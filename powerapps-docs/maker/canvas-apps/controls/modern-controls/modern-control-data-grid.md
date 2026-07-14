---
title: Data Grid modern control in canvas apps - Power Apps
description: Learn about the details, properties, and examples of the Data Grid modern control in Power Apps.
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

# Data Grid modern control in canvas apps (preview)

[This article is pre-release document and is subject to change.]

Display records from a data source in a scrollable, sortable, and searchable grid.

## Description

The **Data Grid** modern control displays records in a column-and-row layout built on Fluent UI. It supports optional search filtering, sortable columns, and selectable rows. The control supports **row virtualization**, enabling smooth scrolling through large datasets with more than 2,000 records. Columns are configured as sub-controls and support multiple types including text, number, phone, email, URL, and button. Use it when you need a high-performance, data-dense view of tabular data with built-in interaction. Key properties for this control are **Items**, **Searchable**, **Sortable**, and **SelectMultiple**.

> [!NOTE]
> The **Data Grid** control is a new control separate from the existing **Table** control. It is not a replacement for the **Table** control.

> [!NOTE]
> If text wrapping is enabled at the column level, row virtualization is disabled. To take advantage of virtualization for large datasets, keep text wrapping turned off on your columns.

## Limitations

- **Attachment column not supported**: Attachment-type columns from Dataverse are not currently supported and do not render in the grid.

## General

**Items** – The data source for the grid. Accepts a Dataverse table, collection, or inline table expression.

**Visible** – Whether the control appears or is hidden.

## Behavior

**Searchable** – Whether a search bar appears above the grid. When **true**, users can type to filter visible rows; the current search string is exposed via the **SearchText** output property. Default is **false**.

**Sortable** – Whether users can sort by a column by selecting its header. Default is **false**.

**SelectMultiple** – Whether users can select more than one row at a time. Default is **false**.

**ShowHeaders** – Whether column header labels appear at the top of the grid. Default is **true**.

**ShowSelector** – Whether a checkbox appears at the start of each row for row selection. Default is **false**.

**Required** – Whether the user must select at least one row.

**DisplayMode** – Whether the control allows user input (**Edit**), only displays data (**View**), or is disabled (**Disabled**).

## Size and position

**[X](../properties-size-location.md)** – Distance between the left edge of the control and the left edge of its parent container (screen if no parent container).

**[Y](../properties-size-location.md)** – Distance between the top edge of the control and the top edge of its parent container (screen if no parent container).

**Width** – Distance between the control's left and right edges. Default is **792**.

**Height** – Distance between the control's top and bottom edges. Default is **475**.

## Style and theme

**BasePaletteColor** – The base color used by the theme to generate the control's color palette.

**Font** – The font family used for the grid text.

**Size** – The font size of the grid text, in points. Default is **14**.

**Color** – The color of the grid text.

## Output properties

**Selected** – The most recently selected row, returned as a record.

**SelectedItems** – All currently selected rows, returned as a table. Use this when **SelectMultiple** is **true**.

**SearchText** – The current value the user has typed in the search bar. Only available when **Searchable** is **true**.

## Configuring columns

The Data Grid uses **Data Grid Column** sub-controls to define how each column appears and what data it shows. Columns are added when you connect a data source and configure fields in the authoring panel. Column properties are locked by default — select a column and choose **Unlock** to customize it.

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