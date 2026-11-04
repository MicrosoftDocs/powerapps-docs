---
title: Card Gallery modern control in canvas apps (preview) - Power Apps
description: Learn about the properties, data mappings, and examples of the Card Gallery modern control in Power Apps.
author: yogeshgupta698
ms.topic: reference
ms.custom: canvas
ms.date: 11/02/2026
ai-usage: ai-generated
ms.subservice: canvas-maker
ms.author: yogupt
ms.reviewer: joshuapa
search.audienceType:
  - maker
---

# Card Gallery modern control in canvas apps (preview)

Display records as responsive cards with optional grouping and selection.

[!INCLUDE [preview-note](~/../shared-content/shared/preview-includes/preview-note.md)]

## Description

Use **Card Gallery** to show a table of records as cards. Map each record's fields to a title, subtitle, description, and optional images with `ThisItem`.

The gallery adjusts its column count to the available width and supports single or multiple selection. You can organize cards into collapsible groups. Cards have a fixed height, and the gallery virtualizes rows as users scroll.

Unlike a classic gallery, Card Gallery uses a predefined card layout rather than a template of child controls. You configure its content and appearance through properties.

## General

Use these properties to supply records and map their content.

| Property | Description |
| --- | --- |
| **Items** | Table of records to display. Use a data source, collection, or inline `Table()` expression. |
| **Title** | Title evaluated for each record. Default is `ThisItem.Title`. |
| **Subtitle** | Subtitle evaluated for each record. Default is `ThisItem.Subtitle`. |
| **Description** | Body text evaluated for each record. Default is `ThisItem.Body`. |
| **Image** | Main image evaluated for each record. Default is `ThisItem.Image`. Set it to `Blank()` for cards without a main image. |
| **HeaderImage** | Small image beside the title and subtitle. Default is `ThisItem.HeaderImage`. Set it to `Blank()` to omit it. |
| **GroupBy** | Text expression evaluated for each record, such as `ThisItem.Team`. Default is `""`, which displays an ungrouped gallery. |
| **Visible** | Whether the gallery appears. |

Your table doesn't need these exact column names if you change the mappings. For example, set **Title** to `ThisItem.ProductName` when your table contains a **ProductName** column.

The content mappings use per-record expressions. Don't use a column-name string such as `"ProductName"` where you intend to show a field value; use `ThisItem.ProductName`.

## Behavior

Use these properties to control selection and the gallery's state.

**Default** – Record to select initially or when the control resets. Use a record from **Items**, not a table of records. The gallery allows an empty initial selection; it doesn't automatically select the first record when you leave **Default** blank.

**Selectable** – Whether users can select cards. Default is `true`. Turning it off prevents user selection; it doesn't remove the **Default** or selection outputs.

**SelectMultiple** – Whether users can select more than one card. Default is `false`. When `true` and **ShowSelector** is `true`, activating a card toggles its selection. Activating an already selected card removes it from **SelectedItems**.

**ShowSelector** – Whether cards show selection indicators. Default is `true`. Hiding the indicators doesn't turn off selection; use **Selectable** for that. With **SelectMultiple** set to `true` and **ShowSelector** set to `false`, a plain click replaces the selection. Ctrl+click on Windows, Command+click on macOS, or keyboard activation toggles an individual card without replacing the other selected records.

**OnSelect** – Action that runs when a user activates a selectable card.

**OnChange** – Action that runs when a user interaction changes the selection. The control updates **Selected** and **SelectedItems** first, then runs **OnChange**, followed by **OnSelect**. Selecting the same card again in single-selection mode doesn't change the selection, but still runs **OnSelect**.

**DisplayMode** – `DisplayMode.Edit` allows selection. `DisplayMode.View` allows navigation without changing selection. `DisplayMode.Disabled` disables interaction.

**LoadingStateText** – Message displayed while **Items** hasn't resolved.

**EmptyStateText** – Message displayed after **Items** resolves to an empty table.

**ShowScrollbar** – Whether the vertical scrollbar appears. Default is `true`.

Use `Reset(ProjectCards)` to reset a gallery named **ProjectCards** to its default selection. The control exposes **Default**, not **DefaultSelectedItems**.

## Size and position

Configure the gallery's size and responsive layout with these properties.

| Property | Description |
| --- | --- |
| **X**, **Y** | Position relative to the parent. |
| **Width**, **Height** | Gallery dimensions. Defaults are `680` by `600`; phone defaults are `320` by `560`. |
| **MinCardWidth** | Minimum target card width used to calculate the number of columns. Default is `240`, or `280` for phone layouts. Minimum accepted value is `100`. A gallery narrower than this target still uses one column. |
| **MaxColumns** | Maximum number of columns. Default is `0`, which lets available width determine the column count without a cap. |
| **Gap** | Space between rows and between columns. Default is `16`. |
| **CardHeight** | Height shared by all cards. Default is `200`; minimum is `50`. |
| **PaddingTop**, **PaddingRight**, **PaddingBottom**, **PaddingLeft** | Padding inside the gallery. Blank values use `8` pixels at runtime. An explicit `0` removes padding on that side. |

The gallery uses the width inside its padding to determine how many cards fit. **MaxColumns** limits that result; it doesn't force a column count that can't fit.

## Style and theme

Use these properties to style the gallery and its cards.

| Property | Description |
| --- | --- |
| **Fill** | Background color of the gallery. |
| **CardFill** | Background color of each card. |
| **CardLayoutDirection** | Layout within each card: `LayoutDirection.Vertical` or `LayoutDirection.Horizontal`. Default is `LayoutDirection.Vertical`. This property doesn't change the gallery into a horizontally scrolling list. |
| **CardImagePlacement** | Whether the main image appears before or after the header: `ImagePlacement.BeforeHeader` or `ImagePlacement.AfterHeader`. Default is `ImagePlacement.BeforeHeader`. |
| **CardImagePosition** | How the main image fits its area: `ImagePosition.Fill`, `.Fit`, `.Stretch`, `.Tile`, or `.Center`. Default is `ImagePosition.Fill`. |
| **CardImageRatio** | Share of the card reserved for the main image, from `0` to `1`. Applies to height in vertical cards and width in horizontal cards. `0` hides the main image. Leave it blank to use the card's automatic image layout. This property isn't an image aspect ratio. |
| **CardBorderRadius** | Corner radius of the cards. Default is `16`. |
| **CardDropShadow** | Card shadow: `DropShadow.None`, `.Light`, `.Semilight`, `.Regular`, `.Semibold`, `.Bold`, or `.ExtraBold`. Default is `DropShadow.Regular`. |
| **TitleColor**, **SubtitleColor**, **DescriptionColor** | Text colors for each content slot. |
| **TitleSize**, **SubtitleSize**, **DescriptionSize** | Text sizes in pixels. Defaults are `16`, `14`, and `12`, respectively. |
| **SelectedCardFill** | Background color of selected cards. When unset, selected cards retain **CardFill**. |
| **SelectedCardBorderColor** | Color of the selected-card outline. |
| **SelectedCardBorderThickness** | Width of the selected-card outline. Default is `2`. |

## Output properties

Read these properties to respond to selection and loading.

**Selected** – The last record in the current selection, or blank when nothing is selected. In multiple-selection mode, deselecting a record can change this output to another record that remains selected. It isn't always the record most recently activated.

**SelectedItems** – Table containing the currently selected records. Records retain their original fields, not just the fields mapped to visible card content.

**IsLoading** – Read-only Boolean output that indicates **Items** hasn't resolved yet. An empty table is an empty state, not a loading state. This isn't an input for showing a custom spinner while another operation runs.

For example, use `ProjectCards.Selected.Title` in another control to show the selected project's title. Use `CountRows(ProjectCards.SelectedItems)` to count the selected records.

## Group cards

Set **GroupBy** to a text-valued field expression, such as `ThisItem.Team`. The gallery creates a heading for each group. Groups start expanded, and users can collapse or expand them independently.

Group matching is case-insensitive. For example, `"Engineering"` and `"engineering"` form one group, using the first spelling encountered for its heading. Groups appear in the order they first occur in **Items**, and records keep their relative order within each group.

When every group value is blank, the gallery remains ungrouped. Don't mix blank group values with named groups; mixed blank and named values produce an invalid-grouping state. Supply a nonempty text value for every record when grouping.

**GroupBy** doesn't require the Power Fx `GroupBy()` function or a nested table schema. Selection outputs still return the original records, not group headings.

## Accessibility

Provide accessible descriptions for the gallery and its content.

**AccessibleLabel** – Accessible description of the gallery.

**ItemAccessibleLabel** – Accessible description evaluated for each card. For example, use `ThisItem.Title`.

**ImageAccessibleLabel** – Alternative text evaluated for each main image.

**HeaderImageAccessibleLabel** – Alternative text evaluated for each header image.

**TabIndex** – Position in keyboard navigation. Default is `0`.

**Tooltip** – Additional information for the gallery.

**ContentLanguage** – Language of the content.

Users can navigate cards with the arrow keys, Home, and End. Provide meaningful item labels and image alternative text, and test keyboard navigation in both grouped and ungrouped layouts.

## Example

This example displays three local records without grouping. The records have text fields named **Title**, **Subtitle**, **Body**, and **Team**. It doesn't require a connector, collection, or external image. The image properties are explicitly blank, so the table doesn't need image columns.

```yaml
- ProjectCards:
    Control: ModernCardGallery@1.1.0
    Properties:
      Items: |-
        =Table(
          {Title: "Website refresh", Subtitle: "In progress", Body: "Update the customer website.", Team: "Marketing"},
          {Title: "Customer research", Subtitle: "Planned", Body: "Interview customers about onboarding.", Team: "Marketing"},
          {Title: "Service dashboard", Subtitle: "In progress", Body: "Track response times and open requests.", Team: "Support"}
        )
      Title: =ThisItem.Title
      Subtitle: =ThisItem.Subtitle
      Description: =ThisItem.Body
      Image: =Blank()
      HeaderImage: =Blank()
      ItemAccessibleLabel: =ThisItem.Title
      AccessibleLabel: ="Projects"
      Selectable: =true
      SelectMultiple: =false
      ShowSelector: =true
      MinCardWidth: =240
      MaxColumns: =2
      CardHeight: =200
      Gap: =16
      Width: =680
      Height: =560
      X: =40
      Y: =40
```

To let users select several projects, set **SelectMultiple** to `true` and read **SelectedItems**. To group these records, set **GroupBy** to `ThisItem.Team`. Test selection with both values of **ShowSelector**, including keyboard activation when indicators are hidden.

If you add images, check both **Image** and **HeaderImage** in Studio and in the published app.

## Limitations

Consider these constraints when you design and test your app:

- Cards use a predefined layout. You can't add arbitrary child controls as you can with a classic gallery template.
- All cards share **CardHeight**. Per-record automatic height isn't available.
- The control doesn't expose built-in search and sorting properties. Prepare the table supplied to **Items** with appropriate Power Fx formulas.
- Virtualization reduces the number of rendered cards; it doesn't guarantee that a data-source formula delegates or retrieves every record. Check the delegation behavior of your data source and formulas.
- Group values must be consistently nonempty text when grouping is active. The control doesn't support a mix of blank and named groups.

## See also

- [Modern controls overview](overview-modern-controls.md)
- [Card modern control](modern-control-card.md)
- [Data Grid modern control](modern-control-data-grid.md)
- [Understand delegation in a canvas app](../../delegation-overview.md)
