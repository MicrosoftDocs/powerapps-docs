---
title: Concat and Concatenate functions in Power Apps
description: Reference information including syntax and examples for the Concat and Concatenate functions in Power Apps.
author: gregli-msft
manager: kvivek
ms.service: powerapps
ms.topic: reference
ms.custom: canvas
ms.reviewer: nabuthuk
ms.date: 05/23/2019
ms.author: gregli
search.audienceType: 
  - maker
search.app: 
  - PowerApps
---
# Concat and Concatenate functions in Power Apps

Concatenates individual strings of text and strings in [tables](../working-with-tables.md).

## Description

The **Concatenate** function concatenates a mix of individual strings and a single-column table of strings. When you use this function with individual strings, it's equivalent to using the **&** [operator](operators.md).

The **Concat** function concatenates the result of a formula applied across all the [records](../working-with-tables.md#records) of a table, resulting in a single string. Use this function to summarize the strings of a table, just as the **[Sum](function-aggregates.md)** function does for numbers.

[!INCLUDE [record-scope](../../../includes/record-scope.md)]

Use the [**Split**](function-split.md) or [**MatchAll**](function-ismatch.md) function to split a string into a table of substrings.

## Syntax

**Concat**( *Table*, *Formula* )

- *Table* - Required.  Table to operate on.
- *Formula* - Required.  Formula to apply across the records of the table.

**Concatenate**( *String1* [, *String2*, ...] )

- *String(s)* - Required.  Mix of individual strings or a single-column table of strings.

## Examples

The examples in this section use these global variables:

- **FirstName** = "Jane"
- **LastName** = "Doe"
- **Products** = ![Table with two columns and four rows.](media/function-concatenate/products.png)

To create these global variables in an app, insert a [**Button**](../controls/control-button.md) control, and set its **OnSelect** property to this formula:

```powerapps-dot
Set( FirstName, "Jane" ); Set( LastName, "Doe" );
Set( Products,
    Table(
        { Name: "Violin", Type: "String" },
        { Name: "Cello", Type: "String" },
        { Name: "Trumpet", Type: "Wind" }
    )
)
```

Select the button (by clicking it while you hold down the Alt key).

### Concatenate function and the & operator

For these examples, set the **Text** property of a [**Label**](../controls/control-text-box.md) control to a formula from the first column of the next table.

| Formula | Description | Result |
|---------|-------------|--------|
| **Concatenate(&nbsp;LastName,&nbsp;",&nbsp;",&nbsp;FirstName&nbsp;)** | Concatenates the value in **LastName**, the string **", "** (a comma followed by a space), and the value in **FirstName**. | "Doe,&nbsp;Jane" |
| **LastName&nbsp;&&nbsp;",&nbsp;"&nbsp;&&nbsp;FirstName** | Same as the previous example except using the **&** operator instead of the function. | "Doe,&nbsp;Jane" |
| **Concatenate(&nbsp;FirstName,&nbsp;"&nbsp;",&nbsp;LastName&nbsp;)** | Concatenates the value in **FirstName**, the string **" "** (a single space), and the value in **LastName**. | "Jane&nbsp;Doe" |
| **FirstName&nbsp;&&nbsp;"&nbsp;"&nbsp;&&nbsp;LastName** | Same as the previous example, using the **&** operator instead of the function. | "Jane&nbsp;Doe" |

### Concatenate with a single-column table

For this example, add a blank, vertical [**Gallery**](../controls/control-gallery.md) control, set its **Items** property to the formula in the next table, and then add a label in the gallery template.

| Formula | Description | Result |
|---------|-------------|--------|
| **Concatenate( "Name:&nbsp;",&nbsp;Products.Name, ",&nbsp;Type:&nbsp;",&nbsp;Products.Type )** | For each record in the **Products** table, concatenates the string **"Name: "**, the name of the product, the string **", Type: "** and the type of the product.  | ![Table of products.](media/function-concatenate/single-column.png) |

### Concat function

For these examples, set the **Text** property of a label to a formula from the first column of the next table.

| Formula | Description | Result |
|---------|-------------|--------|
| **Concat( Products, Name & ", " )** | Evaluates the expression **Name & ", "** for each record of **Products** and concatenates the results together into a single text string.  | "Violin,&nbsp;Cello,&nbsp;Trumpet,&nbsp;" |
| **Concat( Filter(&nbsp;Products,&nbsp;Type&nbsp;=&nbsp;"String"&nbsp;), Name & ", " )** | Evaluates the formula **Name & ", "** for each record of **Products** that satisfies the filter **Type = "String"**, and concatenates the results into a single text string.   | "Violin,&nbsp;Cello,&nbsp;" |

### Trimming the end

The last two examples include an extra ", " at the end of the result. The function appends a comma and a space to the **Name** value of every record in the table, including the last record.

In some cases, these extra characters don't matter. For example, a single-space separator doesn't appear if you show the result in a label. If you want to remove these extra characters, use the [**Left**](function-left-mid-right.md) or [**Match**](function-ismatch.md) function.

For these examples, set the **Text** property of a label to a formula from the first column of the next table.

| Formula | Description | Result |
|---------|-------------|--------|
| **Left( Concat(&nbsp;Products,&nbsp;Name&nbsp;&&nbsp;",&nbsp;"&nbsp;), Len(&nbsp;Concat(&nbsp;Products,&nbsp;Name&nbsp;&&nbsp;",&nbsp;"&nbsp;)&nbsp;)&nbsp;-&nbsp;2 )** | Returns the result of **Concat** but removes the last two characters, which form the extraneous separator. | "Violin,&nbsp;Cello,&nbsp;Trumpet" |
| **Match( Concat(&nbsp;Products,&nbsp;Name&nbsp;&&nbsp;",&nbsp;"&nbsp;), "^(?&lt;trim&gt;.*),&nbsp;$" ).trim** | Returns the characters of **Concat** from the beginning of the text string (^) to the end ($) but doesn't include the unwanted comma and space at the end. | "Violin,&nbsp;Cello,&nbsp;Trumpet" |

### Split and MatchAll

If you used **Concat** with a separator, you can reverse the operation by combining the **Split** and **MatchAll** functions.

For these examples, add a blank, vertical gallery, set its **Items** property to a formula in the next table, and then add a label in the gallery template.

| Formula | Description | Result |
|---------|-------------|--------|
| **Split( Concat(&nbsp;Products,&nbsp;Name&nbsp;&&nbsp;",&nbsp;"&nbsp;), ", " )** | Splits the text string with the separator **", "**. The string ends with a comma and space, so the last row in the result is an empty string.  | ![Table with last row empty.](media/function-concatenate/split.png) |
| **MatchAll( Concat(&nbsp;Products,&nbsp;Name&nbsp;&&nbsp;",&nbsp;"&nbsp;), "[^\s,]+" ).FullMatch** | Splits the text string based on characters that aren't spaces or commas. This formula removes the extra comma and space at the end of the string. | ![Table with only 3 rows.](media/function-concatenate/matchall.png)

[!INCLUDE[footer-include](../../../includes/footer-banner.md)]