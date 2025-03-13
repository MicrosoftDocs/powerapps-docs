---
title: Table card elements in Cards for Power Apps
description: Learn about the card elements and properties surrounding Tables
author: sch
ms.topic: reference
ms.custom:
ms.reviewer:
ms.date: 08/23/2023
ms.author: aschaedle
search.audienceType:
  - maker
contributors:
  - sch
---

# Table control in cards

[!INCLUDE[cards-deprecation-banner](~/includes/cards-deprecation-notice.md)]

Use the Table control to present tabular data or any structured information that is best laid out in rows and columns. Tables are made up of three separate card elements:
- Tables
- Table Rows
- Table Cells


## Table

Tables are the top-level container for Table Rows. For this reason, they have many properties that apply to the appearance and layout of all Table Cells and Rows contained within.

### Element Properties

**[Show grid lines](control-reference.md#s)** – Specifies whether grid lines should be displayed.

**[Visible](control-reference.md#i)** – Show or hide the table. Can be **true** or **false**.

**[Spacing](control-reference.md#s)** – Controls the amount of spacing between this control and the preceding control.

**[Divider](control-reference.md#d)** – When true, draw a separating line at the top of the control.

**[Vertical alignment](control-reference.md#c)** – Defines how the content should be aligned vertically for all children of the Table.

**[Horizontal alignment](control-reference.md#c)** – Defines how the content should be aligned horizontally for all children of the Table.

**[Height](control-reference.md#m)** – Specifies whether the table should grow with the size of the data (auto) or grow to fill the height of a container (stretch).

**[Grid style](control-reference.md#s)** – Style hint for all Table Cells within the Table. Allowed values: default, emphasis, good, attention, warning, accent.

**[Repeat for every](control-reference.md#r)** – The source of data that is used to show multiple instances of this control. Learn how to use [repeat for every](control-reference.md#r).

### Column Properties

The number of columns are defined on the Table itself. Columns can be added and removed from the "Columns" tab, where each column has the following properties:

**[Width](control-reference.md#w)** – Specifies the width of the column. If expressed as a number, width represents the weight a the column relative to the other columns in the Table. If expressed as a string, width must by in the format "{{number}}px" (for instance, "50px") and represents an explicit number of pixels.

**[Horizontal alignment](control-reference.md#c)** – Controls how the content of all Cells in the column is horizontally aligned by default. When specified, this value overrides the setting at the Table level. When not specified, horizontal alignment is defined at the Table, row or Cell level.

**[Vertical alignment](control-reference.md#c)** – Controls how the content of all Cells in the column is vertically aligned by default. When specified, this value overrides the setting at the Table level. When not specified, vertical alignment is defined at the Table, row or Cell level.


## Table Row

The immediate child of a Table card element is a Table Row. It groups several Table Cells together horizontally and has some properties that apply to all items in that Row:

**[Visible](control-reference.md#i)** – Show or hide an element. Can be **true** or **false**.

**[Spacing](control-reference.md#s)** – Controls the amount of spacing between this control and the preceding control.

**[Divider](control-reference.md#d)** – When true, draw a separating line at the top of the control.

**[Vertical alignment](control-reference.md#c)** – Defines how the content should be aligned vertically for all Cells in the Row.

**[Horizontal alignment](control-reference.md#c)** – Defines how the content should be aligned horizontally for all Cells in the Row.

**[Height](control-reference.md#m)** – Specifies whether the Table Row should grow with the size of the data (auto) or grow to fill the height of a container (stretch).

**[Style](control-reference.md#s)** – Style hint for all Table Cells within the Row. Allowed values: default, emphasis, good, attention, warning, accent.

**[Repeat for every](control-reference.md#r)** – The source of data that is used to show multiple instances of child Cells. Learn how to use [repeat for every](control-reference.md#r).


## Table Cell

Represents a cell within a row of a Table element. It can contain any standalone card element as a child, and the following properties:

**[Bleed](control-reference.md#b)** – Determines whether the control should bleed through its parent's padding.

**[Background image](control-reference.md#b)** – Specifies a background image. Acceptable formats are PNG, JPEG, and GIF.

**[Minimum height](control-reference.md#m)** – Specifies the minimum height of the Table Cell in pixels, like "80px".

**[Spacing](control-reference.md#s)** – Controls the amount of spacing between this control and the preceding control.

**[Divider](control-reference.md#d)** – When true, draw a separating line at the top of the control.

**[Horizontal alignment](control-reference.md#c)** – Defines how the content should be aligned horizontally for all children of the Table.

**[Vertical alignment](control-reference.md#c)** – Defines how the content should be aligned for child card elements of the Cell.

**[Present right-to-left](control-reference.md#p)** – When enabled, content in the Table Cell should be presented right to left.

**[Height](control-reference.md#m)** – Specifies whether the Table Cell should grow with the size of the data ("auto") or grow to fill the height of a container ("stretch").

**[Style](control-reference.md#s)** – Style hint for the Table Cell background. Allowed values: default, emphasis, good, attention, warning, accent.
