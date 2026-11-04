---
title: Data Grid modern control in canvas apps - Power Apps
description: Learn about the properties, pagination, and YAML examples of the Data Grid modern control in Power Apps.
author: yogeshgupta698
ms.topic: reference
ms.custom: canvas
ms.date: 11/02/2026
ai-usage: ai-assisted
ms.subservice: canvas-maker
ms.author: yogupt
ms.reviewer: joshuapa
search.audienceType:
  - maker
reviewer: joshuapartlow
ms.collection: bap-ai-copilot
---

# Data Grid modern control in canvas apps

Display records from a data source in a scrollable, sortable, and searchable grid.

## Description

The **Data Grid** modern control displays records in a column-and-row layout built on Fluent UI. It supports optional search filtering, sortable columns, and selectable rows. The control supports **row virtualization**, enabling smooth scrolling through large datasets with more than 2,000 records. You configure columns as subcontrols, and they support multiple types including text, number, phone, email, URL, and button. Use this control when you need a high-performance, data-dense view of tabular data with built-in interaction. Key properties for this control are **Items**, **Searchable**, **Sortable**, and **SelectMultiple**.

> [!NOTE]
> The **Data Grid** control is the recommended control for displaying tabular data in canvas apps, instead of the [Table control](modern-control-table.md). It provides improved performance and usability for data-dense scenarios.

Row virtualization turns on automatically for large datasets. Rows have a consistent height whether or not virtualization is active.

> [!NOTE]
> If you enable text wrapping on a column, row virtualization is disabled. The app checker flags columns with text wrapping enabled. Keep text wrapping turned off to use virtualization for large datasets.

## General

**Items** – The data source for the grid. Accepts a Dataverse table, collection, or inline table expression. Switching the data source refreshes the columns.

**Visible** – Whether the control appears or is hidden.

## Behavior

**Searchable** – Whether a search bar appears above the grid. When **true**, users can type to filter loaded records. The **SearchText** output property exposes the current search string. The default value is **false**. Turning off **Searchable** clears the search filter. To handle filtering in the **Items** formula instead, see [Search and sorting](#search-and-sorting).

**Sortable** – Whether users can sort by a column by selecting its header. Default is **true**. Whether sorting can run at the data source depends on the source and column.

**SelectMultiple** – Whether users can select more than one row at a time. Default is **false**.

**ShowHeaders** – Whether column header labels appear at the top of the grid. Default is **true**.

**ShowSelector** – Whether a checkbox appears at the start of each row for row selection. Default is **false**.

**ShowAIRowSummary** - Whether eligible Dataverse rows offer an AI-generated summary. Default is **false**. Setting this property to **true** doesn't configure a summary for the table or override administrator settings. See [AI row summaries](#ai-row-summaries).

**Required** – Whether the user must select at least one row.

**DisplayMode** – Whether the control allows user input (**Edit**), only displays data (**View**), or is disabled (**Disabled**).

To reset the control, including its current selection, use the [Reset function](/power-platform/power-fx/reference/function-reset). For example, set a button's **OnSelect** property to `Reset(DataGrid1)`, where `DataGrid1` is the name of your grid.

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

**SearchText** – The current value the user types in the search bar. Use it in **Items** when **DelegateSearch** is **true**.

**CurrentPage** – The current 1-based page number. In numbered mode, it follows the pager. In automatic mode, it follows the visible row range.

**ItemsCount** – The number of records currently loaded by the grid, not the total record count in the remote data source and not just the number of rows on the visible page.

**AllItemsLoaded** – With pagination enabled, indicates that all records available through the current paging source have loaded. With `Pagination.None`, becomes **true** when the single fetch finishes, even if the app's data row limit truncated the results.

> [!IMPORTANT]
> Don't use **AllItemsLoaded** with `Pagination.None` as proof that every record in a remote table is present. Similarly, **ItemsCount** isn't a server-side total. Any separate count formula is subject to the connector's delegation and counting limits.

## Pagination

Use pagination to load records as users scroll or display records one page at a time. Set **Pagination** to choose how the grid loads and displays records, and **PageSize** to set the number of records per fetch or numbered page. A connected data source can supply records incrementally; a collection or inline table already contains the records available to the control.

Pagination and row virtualization serve different purposes. Pagination controls data loading and page boundaries. Virtualization controls how many rows the grid renders at once. Turning on pagination doesn't make a nondelegable **Items** formula delegable or retrieve records that aren't in a collection.

### Pagination properties

Use these properties with **Items**, **Searchable**, and **Sortable** to configure paging and search.

| Property | Description |
| --- | --- |
| **Pagination** | The paging mode. Accepts `Pagination.None`, `Pagination.Auto`, or `Pagination.Number`. The default is `Pagination.None`. |
| **PageSize** | The number of records requested per page, and the size of a numbered page. Use a positive whole number. A blank, zero, negative, or invalid value falls back to 100. A fractional value is rounded down. Use **Pagination**, not a blank **PageSize**, to turn paging off. |
| **DelegateSearch** | When `false`, the grid searches the records it has loaded. When `true`, the grid exposes **SearchText** without applying its own search filter; use that output in the **Items** formula. The default is `false`. |

### Paging modes

Choose a mode that matches the way users review records.

| Value | Behavior |
| --- | --- |
| `Pagination.None` | Makes one nonpageable fetch, subject to the app's data row limit. Doesn't show a pager or fetch more records as users scroll. **PageSize** doesn't enable paging in this mode. |
| `Pagination.Auto` | Loads more records from a pageable source as users scroll. For an in-memory table or collection, displays the available records without simulating incremental server loading. |
| `Pagination.Number` | Shows one page of records with first-page, previous-page, and next-page actions. Fetches additional pages from a pageable source as needed. For a materialized source, pages through the available records. |

For a self-contained example, see [Numbered pages](#numbered-pages).

### Search and sorting

When **DelegateSearch** is `false`, search checks the grid's loaded records. If a pageable source has more records, the grid offers a load-more action during a search. A search with no matches among loaded records doesn't prove that the remote table has no matches.

To handle search in Power Fx:

1. Set **Searchable** to `true`.
2. Set **DelegateSearch** to `true`.
3. Use the grid's **SearchText** output in **Items** with a filter that your connector can delegate.

For example, for a connected table named `Products` with a text column named `Name` and a grid named `PagedDataGrid`, set **Items** to:

```power-fx
Filter(Products, StartsWith(Name, PagedDataGrid.SearchText))
```

This formula requires that table and column in your app. Check delegation support for your connector before using it with a large table. **DelegateSearch** doesn't automatically delegate a formula; it transfers responsibility for filtering to the formula you write.

For a source that supports server-side sorting, sorting a supported column re-queries the source with the new order. For a materialized table in numbered mode, the grid sorts the available records before selecting the page. Neither behavior can sort records excluded by an upstream, nondelegable formula.

### Change the paging configuration

Changing **Pagination** or **PageSize** returns the grid to the first page, clears its search text, and clears the active sort. Apply any required search or sort again after changing the configuration.

When the **Items** formula changes, the grid rebuilds its paging source rather than replaying previously completed results. For example, when you change a filter over a SharePoint list, the grid uses the new results even when the previous query had finished loading. This behavior is different from changing only the page size or paging mode.

### Pagination considerations

Keep the source's data-loading and delegation limits in mind:

- Pagination doesn't bypass delegation limits in **Items**, connector limits, or the scope of an already populated collection.
- **CurrentPage**, **ItemsCount**, and **AllItemsLoaded** are outputs. Don't assign formulas to them to implement custom paging.
- Built-in search over a partly loaded source can return incomplete results. Use a delegable **Items** formula when you need source-wide search.
- Changing the paging configuration rebuilds the paging view. Don't depend on a page number remaining unchanged after changing **Items**, **Pagination**, or **PageSize**.

The control's other [limitations](#limitations), including the relationship between text wrapping and virtualization, still apply.

## Configure columns

The Data Grid uses **Data Grid Column** sub-controls to define how each column appears and what data it shows. You add columns when you connect a data source and configure fields in the authoring panel. Column properties are locked by default. Select a column and choose **Unlock** to customize it.

You can also configure column variants for data sources that aren't directly connected, such as collections. Column formulas can use `ThisItem` to access the current row. Columns bound to multiple-selection choice fields display the selected values. Copying and pasting the grid preserves its column variants.

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

The following YAML examples demonstrate a searchable grid and numbered pages. Both examples use inline data, so you don't need a connection or collection.

### Searchable grid

The following YAML example shows a searchable grid with two text columns:

```yaml
- DataGrid2:
    Control: ModernDataGrid@1.8.0
    Properties:
      Items: |-
        =Table({Name: "Darius Franklin", Department: "Sales"}, {Name: "Elizabeth Moore", Department: "Engineering"}, {Name: "Hannah Jarvis", Department: "Marketing"})
      Searchable: =true
      X: =40
      Y: =40
    Children:
      - Department_Column1:
          Control: ModernDataGridColumn@1.2.0
          Variant: Textual
          IsLocked: true
          Properties:
            FieldDisplayName: ="Department"
            Text: =ThisItem.Department
      - Name_Column1:
          Control: ModernDataGridColumn@1.2.0
          Variant: Textual
          IsLocked: true
          Properties:
            FieldDisplayName: ="Name"
            Text: =ThisItem.Name
```

### Numbered pages

This self-contained YAML example displays five records in pages of two. It doesn't require a connection or collection. The first page contains Darius and Elizabeth, the second contains Hannah and Henry, and the third contains Malik.

```yaml
- PagedDataGrid:
    Control: ModernDataGrid@1.8.0
    Properties:
      Items: |-
        =Table(
            {Name: "Darius", Department: "Sales"},
            {Name: "Elizabeth", Department: "Engineering"},
            {Name: "Hannah", Department: "Marketing"},
            {Name: "Henry", Department: "Sales"},
            {Name: "Malik", Department: "Engineering"}
        )
      Pagination: =Pagination.Number
      PageSize: =2
      Searchable: =true
      DelegateSearch: =false
      Width: =600
      Height: =400
      X: =40
      Y: =40
    Children:
      - NameColumn:
          Control: ModernDataGridColumn@1.2.0
          Variant: Textual
          IsLocked: true
          Properties:
            FieldDisplayName: ="Name"
            Text: =ThisItem.Name
      - DepartmentColumn:
          Control: ModernDataGridColumn@1.2.0
          Variant: Textual
          IsLocked: true
          Properties:
            FieldDisplayName: ="Department"
            Text: =ThisItem.Department
```

Preview the app and use the pager to move between pages. Enter `Engineering` in the search box to show Elizabeth and Erin. Searching returns to the first page of matching records.

For automatic loading, connect **Items** directly to a supported pageable data source, set **Pagination** to `Pagination.Auto`, and set **PageSize** to a suitable value such as `100`. An inline table demonstrates page layout, but it doesn't demonstrate remote fetching.

## AI row summaries

AI row summaries help users understand a Dataverse record without opening a separate form. For example, a user reviewing accounts can read a short summary of the account information selected by the maker's prompt.

### Prerequisites

The grid needs both a configured Dataverse summary and permission to show it:

- Connect **Items** to a Dataverse table that has a row summary configured. The grid's support for collections and inline tables doesn't extend to AI row summaries.
- Ask your Power Platform administrator to allow **Summary in canvas data grid** for the environment. See [Administrator settings](#administrator-settings).
- [Create and test a row summary](../../../data-platform/configure-form-row-summary.md#create-a-row-summary) for the table. The canvas grid uses the same table-level summary configuration described in the model-driven app article; you don't author a separate prompt on each grid. For column selection, formatting, and language instructions, see [Write a good prompt for the row summary](../../../data-platform/configure-form-row-summary.md#write-a-good-prompt-for-the-row-summary).

### Administrator settings

The **Summary in canvas data grid** feature control governs access to summaries in canvas grids. It is separate from **ShowAIRowSummary**, which a maker sets on each grid.

To review the feature's configuration, sign in to the [Power Platform admin center](https://admin.powerplatform.microsoft.com/) and select **Copilot** > **Settings**. Under **Power Apps**, locate **Summary in canvas data grid**, select the environment, and select **Edit setting**. Allow the feature for that environment and save your changes. For details about this settings experience, see [Copilot settings](/power-platform/admin/copilot/copilot-hub#settings).

The canvas grid also checks the shared **AI insight cards** (`EnableFormInsights`) setting and whether AI prompts are enabled. Allowing the canvas-specific feature doesn't override these settings or license and capacity eligibility checks. The shared row-summary controls are moving from the environment's **Settings** > **Product** > **Features** page to the Copilot settings experience. See [AI insight cards](/power-platform/admin/settings-features#ai-insight-cards) for that transition.

### Enable and use summaries

Follow these steps after the table's summary is configured:

1. Open your canvas app in Power Apps Studio and select the **Data Grid** control.
2. Set **Items** to the configured Dataverse table. For example, use `Accounts` if you configured a summary for that table. Don't use the inline sample table in this article to test AI summaries.
3. Set **ShowAIRowSummary** to `true`.
4. Preview the app. Point to a row and select the summary icon in its first cell to open the AI-generated summary.
5. Compare the summary with the record's data. Test more than one record, including records with missing values, before sharing the app.

To hide summaries on a particular grid, set **ShowAIRowSummary** to `false`. This action doesn't delete the table's summary configuration.

> [!NOTE]
> AI-generated summaries can be incomplete or incorrect. Review important details in the source record before acting on them.

### Troubleshoot missing summaries

If the summary icon doesn't appear, check the following:

| Check | Action |
| --- | --- |
| Control setting. | Confirm that [ShowAIRowSummary](#behavior) is `true` on this grid. |
| Data source. | Bind [Items](#general) directly to the configured Dataverse table to isolate data-source issues. A collection or inline table isn't a substitute. |
| Table configuration. | Confirm that the table contains records and has a [tested, applied row summary](../../../data-platform/configure-form-row-summary.md#create-a-row-summary). Review the table exclusions in that article. |
| Administrator settings. | Ask your administrator to check [Summary in canvas data grid and the shared settings](#administrator-settings) for the environment. The control property doesn't bypass administrator policies or eligibility checks. |

If a summary fails to load, don't interpret the failure as a statement about the record. Review the underlying record and retry when the service is available.

## Limitations

The Data Grid control has the following limitations:

- **Attachment columns aren't supported**: The grid doesn't render attachment-type columns from Microsoft Dataverse.
- **Per-column text styling isn't available**: You can't set the font size or font color for an individual column.
- **Alternating row colors aren't available**: The grid doesn't support zebra striping.
- **Variable row height isn't available**: All rows use the same height. You can't set a custom or per-row height.
- **Search hint text isn't customizable**: You can't change the placeholder text in the search bar.
- **Search delegation**: Search might not be delegable on all data sources, and a delegation warning might not appear. For large data sources, verify that search returns the results you expect.
- **DefaultSelectedItems**: Changes to the default selected items aren't reflected after the grid first loads.
- **AI row summaries**: Summaries require a configured Dataverse table and are subject to the table summary's [known limitations](../../../data-platform/configure-form-row-summary.md#known-limitations).

## See also

- [Modern controls overview](overview-modern-controls.md)
- [Table modern control](modern-control-table.md)
- [Size and location properties](../properties-size-location.md)
- [Configure a row summary](../../../data-platform/configure-form-row-summary.md)
- [Delegation overview](../../delegation-overview.md)