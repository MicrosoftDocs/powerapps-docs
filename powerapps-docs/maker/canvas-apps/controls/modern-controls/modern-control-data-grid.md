---
title: Data Grid modern control in canvas apps - Power Apps
description: Learn about the details, properties, and examples of the Data Grid modern control in Power Apps.
author: yogeshgupta698
ms.topic: reference
ms.custom: canvas
ms.date: 07/20/2026
ms.subservice: canvas-maker
ms.author: yogupt
ms.reviewer: mkaur
search.audienceType:
  - maker
---

# Data Grid modern control in canvas apps

Display records from a data source in a scrollable, sortable, and searchable grid.

## Description

The **Data Grid** modern control displays records in a column-and-row layout built on Fluent UI. It supports optional search filtering, sortable columns, and selectable rows. The control supports **row virtualization**, enabling smooth scrolling through large datasets with more than 2,000 records. You configure columns as subcontrols, and they support multiple types including text, number, phone, email, URL, and button. Use this control when you need a high-performance, data-dense view of tabular data with built-in interaction. Key properties for this control are **Items**, **Searchable**, **Sortable**, and **SelectMultiple**.

> [!NOTE]
> The **Data Grid** control is the recommended control for displaying tabular data in canvas apps, instead of the [Table control](modern-control-table.md). It provides improved performance and usability for data-dense scenarios.

> [!NOTE]
> If you enable text wrapping at the column level, row virtualization is disabled. To take advantage of virtualization for large datasets, keep text wrapping turned off on your columns.

## Recent improvements

The Data Grid control includes the following improvements for general availability:

- **Automatic virtualization for large datasets**: Row virtualization turns on automatically so you can scroll smoothly through large datasets. Virtualization is disabled only when you enable text wrapping on a column. The app checker flags columns that have text wrapping enabled so you can keep virtualization on.
- **Consistent row heights**: Rows render at a consistent height whether or not virtualization is active.
- **Resettable control**: The **Reset** function now resets the control, including the current selection.
- **Multiple-selection choice columns**: Columns bound to multiple-selection choice fields now display their values.
- **More reliable search**: Fixed an issue that could cause the control to stop responding when you use the search bar, and improved the search bar's padding and alignment.
- **Email columns**: Selecting a value in an email column no longer affects your browser session.
- **Copy and paste**: Copying and pasting the control no longer changes its columns into custom variants.
- **Column configuration**: You can configure column variants for data sources that aren't directly connected, and column property formulas can use `ThisItem`.
- **Data source changes**: Switching the data source refreshes the columns, and the search filter clears when you turn off **Searchable**.

## Limitations

The Data Grid control has the following limitations:

- **Attachment columns aren't supported**: The grid doesn't render attachment-type columns from Microsoft Dataverse.
- **Per-column text styling isn't available**: You can't set the font size or font color for an individual column.
- **Alternating row colors aren't available**: The grid doesn't support zebra striping.
- **Variable row height isn't available**: All rows use the same height. You can't set a custom or per-row height.
- **Search hint text isn't customizable**: You can't change the placeholder text in the search bar.
- **Search delegation**: Search might not be delegable on all data sources, and a delegation warning might not appear. For large data sources, verify that search returns the results you expect.
- **DefaultSelectedItems**: Changes to the default selected items aren't reflected after the grid first loads.

## General

**Items** – The data source for the grid. Accepts a Dataverse table, collection, or inline table expression.

**Visible** – Whether the control appears or is hidden.

## Behavior

**Searchable** – Whether a search bar appears above the grid. When **true**, users can type to filter visible rows. The current search string is exposed through the **SearchText** output property. The default value is **false**.

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

**BasePaletteColor** – The base color that the theme uses to generate the control's color palette.

**Font** – The font family used for the grid text.

**Size** – The font size of the grid text, in points. Default is **14**.

**Color** – The color of the grid text.

## Output properties

**Selected** – The most recently selected row, returned as a record.

**SelectedItems** – All currently selected rows, returned as a table. Use this property when **SelectMultiple** is **true**.

**SearchText** – The current value the user types in the search bar. This property is only available when **Searchable** is **true**.

## Configuring columns

The Data Grid uses **Data Grid Column** sub-controls to define how each column appears and what data it shows. You add columns when you connect a data source and configure fields in the authoring panel. Column properties are locked by default. Select a column and choose **Unlock** to customize it.

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