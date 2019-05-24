---
title: Concat and Concatenate functions | Microsoft Docs
description: Reference information, including syntax and examples, for the Concat and Concatenate functions in PowerApps
author: gregli-msft
manager: kvivek
ms.service: powerapps
ms.topic: reference
ms.custom: canvas
ms.reviewer: anneta
ms.date: 05/23/2019
ms.author: gregli
search.audienceType: 
  - maker
search.app: 
  - PowerApps
---
# Concat and Concatenate functions in PowerApps
Concatenates individual strings of text and strings in [tables](../working-with-tables.md).

## Description
The **Concat** function concatenates the result of a formula applied across all the [records](../working-with-tables.md#records) of a table, resulting in a single string. Use this function to summarize the strings of a table, just as the **[Sum](function-aggregates.md)** function does for numbers.

[!INCLUDE [record-scope](../../../includes/record-scope.md)]

Use the [**Split** function](function-split.md) or [**MatchAll** function](function-ismatch.md) to split a string into a table of substrings.

The **Concatenate** function concatenates a mix of individual strings and a single-column table of strings. Used with individual strings, this function is equivalent to using the **&** [operator](operators.md). 

## Syntax
**Concat**( *Table*, *Formula* )

* *Table* - Required.  Table to operate on.
* *Formula* - Required.  Formula to apply across the records of the table.

**Concatenate**( *String1* [, *String2*, ...] )

* *String(s)* - Required.  Mix of individual strings or a single-column table of strings.

## Examples

The examples in this section use the following global variables:

- **FirstName** = "Jane"   
- **LastName** = "Doe" 
- **Products** = ![](media/function-concatenate/products.png) 

To create these global variables in an app, insert a button control and set its **OnSelect** property to
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
Select the button (hold down the Alt key while clicking the button).

### Concatenante function and & operator

| Formula | Description | Result | 
|---------|-------------|--------|
| **Concatenate(&nbsp;LastName,&nbsp;",&nbsp;",&nbsp;FirstName&nbsp;)** | Concatenates the value in **LastName**, the string **", "** (a comma followed by a space), and the value in **FirstName**. | "Doe,&nbsp;Jane" |
| **LastName&nbsp;&&nbsp;",&nbsp;"&nbsp;&&nbsp;FirstName** | Same as the previous example, using the **&** operator instead of the function. | "Doe,&nbsp;Jane" |
| **Concatenate(&nbsp;FirstName,&nbsp;"&nbsp;",&nbsp;LastName&nbsp;)** | Concatenates the value in **FirstName**, the string **" "** (a single space), and the value in **LastName**. | "Jane&nbsp;Doe" |
| **FirstName&nbsp;&&nbsp;"&nbsp;"&nbsp;&&nbsp;LastName** | Same as the previous example, using the **&** operator instead of the function. | "Jane&nbsp;Doe" |

### Concatenate with single column table

| Formula | Description | Result | 
|---------|-------------|--------|
| **Concatenate( "Name:&nbsp;",&nbsp;Products.Name, ",&nbsp;Type:&nbsp;",&nbsp;Products.Type )** | For each record in the **Products** table, concatenates the string **"Name: "**, the name of the product, the string **", Type: "** and the type of the product.  | ![](media/function-concatenate/single-column.png) |

### Concat function

| Formula | Description | Result | 
|---------|-------------|--------|
| **Concat( Products, Name & ", " )** | Evaluates the formula **Name & ", "** for each record of **Products** and concatenates the results together into a single text string.  | "Violin, Cello, Trumpet, " |
| **Concat( Filter(&nbsp;Products,&nbsp;Type&nbsp;=&nbsp;"String"&nbsp;), Name & ", " )** | Evaluates the formula **Name & ", "** for each record of **Products** that satifies the filter **Type = "String"** and concatenates the results together into a single text string.   | "Violin, Cello, " |

### Trimming the end

Note that in the last two example an extra ", " is included at the end of the result.  This is because for each record of the table the function extracts the **Name** and adds a ", " to the end, no matter if it is the first record or the last. 

In some cases these extra characters won't matter, for example if a single space separator is used and the result is displayed in a label.  For situations where these extra characters needs to be removed, you can use the [**Left** function](function-left-mid-right.md) or the [**Match** function](function-ismatch.md):

| Formula | Description | Result | 
|---------|-------------|--------|
| **Left( Concat(&nbsp;Products,&nbsp;Name&nbsp;&&nbsp;",&nbsp;"&nbsp;), Len(&nbsp;Concat(&nbsp;Products,&nbsp;Name&nbsp;&&nbsp;",&nbsp;"&nbsp;)&nbsp;)&nbsp;-&nbsp;2 )** | Returns the result of **Concat** but removes the last two characters, the extra separator that is not desired. | "Violin, Cello, Trumpet" |
| **Match( Concat(&nbsp;Products,&nbsp;Name&nbsp;&&nbsp;",&nbsp;"&nbsp;), "^(?&lt;trim&gt;.*),&nbsp;$" ).trim** | Returns the characters of **Concat** from the beginning of the text string (^) to the end ($) but does not include the unwanted comma and space at the end. | "Violin, Cello, Trumpet" |

### Split and MatchAll

The **Split** and **MatchAll** functions can be used to reverse **Concat** when used with a separator.

| Formula | Description | Result | 
|---------|-------------|--------|
| **Split( Concat(&nbsp;Products,&nbsp;Name&nbsp;&&nbsp;",&nbsp;"&nbsp;), ", " )** | Splits the text string with the separator **", "**.  Since there is a comma and space at the end of the string, this becomes an extra row in the result with an empty string.  | ![](media/function-concatenate/split.png) |
| **MatchAll( Concat(&nbsp;Products,&nbsp;Name&nbsp;&&nbsp;",&nbsp;"&nbsp;), "[^\s,]+" ).FullMatch** | Splits the text string based on characters that are not a space or a comma. In this case, the extra comma and space at the end of the string is automatically removed. | ![](media/function-concatenate/matchall.png)







