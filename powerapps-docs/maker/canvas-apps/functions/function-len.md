---
title: Len function in Power Apps
description: Reference information including syntax and examples for the Len function in Power Apps.
author: gregli-msft
manager: kvivek
ms.service: powerapps
ms.topic: reference
ms.custom: canvas
ms.reviewer: nabuthuk
ms.date: 11/07/2015
ms.subservice: canvas-maker
ms.author: gregli
search.audienceType: 
  - maker
search.app: 
  - PowerApps
---
# Len function in Power Apps
Returns the length of a string of text.

## Description
If you specify a single string as the argument, the return value is the length as a number.  If you specify a single-column [table](../working-with-tables.md) that contains strings, the return value is a single-column table that contains the length of each string. If you have a multi-column table, you can shape it into a single-column table, as [working with tables](../working-with-tables.md) describes.

If you specify a [blank](function-isblank-isempty.md) string, **Len** returns 0.

## Syntax
**Len**( *String* )

* *String* - Required. The string to measure.

**Len**( *SingleColumnTable* )

* *SingleColumnTable* - Required. A single-column table of strings to measure.

## Examples
### Single string
For the examples in this section, the [data source](../working-with-data-sources.md) is a text-input control that's named **Author** and that contains the string "E. E. Cummings".

| Formula | Description | Result |
| --- | --- | --- |
| **Len( Author.Text )** |Measures the length of the string in the **Author** control. |14 |
| **Len( "" )** |Measures the length of an empty string. |0 |

### Single-column table
For the first example in this section, the data source is named **People** and contains this data:

![People table.](media/function-len/people-table.png)

| Formula | Description | Result |
| --- | --- | --- |
| **Len( ShowColumns(&nbsp;People,&nbsp;"Address"&nbsp;) )** |In the **Address** [column](../working-with-tables.md#columns) of the **People** table:<br><ul><li>Measures the length of each string.</li><li>Returns a single-column table that contains the length of each string.</li> | ![Len with ShowColumns.](media/function-len/people-table-len.png) |
| **Len( [ "Hello", "to the", "World", "" ] )** |In the **[Value](function-value.md)** column of the inline table:<br><ul><li>Measures the length of each string.</li><li>Returns a single-column table that contains the length of each string.</li> |![Len with text values.](media/function-len/people-table-len-inline.png) |



[!INCLUDE[footer-include](../../../includes/footer-banner.md)]