<properties
	pageTitle="IsBlank and IsEmpty functions | Microsoft PowerApps"
	description="Reference information, including syntax and examples, for the IsBlank and IsEmpty functions in PowerApps"
	services=""
	suite="powerapps"
	documentationCenter="na"
	authors="gregli-msft"
	manager="dwrede"
	editor=""
	tags=""/>

<tags
   ms.service="powerapps"
   ms.devlang="na"
   ms.topic="article"
   ms.tgt_pltfrm="na"
   ms.workload="na"
   ms.date="11/01/2015"
   ms.author="gregli"/>

# IsBlank and IsEmpty functions in PowerApps #

Tests whether a value is blank or a [table](working-with-tables.md) contains no [records](working-with-tables.md#records).

## Overview ##

*Blank* is a placeholder for "no value" or "unknown value." An input-text box is *blank* if the user hasn't typed any characters in it. The same control is no longer *blank* as soon as the user types a character in it.  

Any property or calculated value can be *blank*.  For example, a Boolean value normally has one of two values: **true** or **false**.  But in addition to these two, it can also be *blank*.  This is similar to Microsoft Excel, where a worksheet cell starts out as blank but can hold the values **TRUE** or **FALSE**, among others. At any time, the contents of the cell can be removed, and it would return to a *blank* state.

*Empty* is specific to tables that contain no records. The table structure may be intact, complete with [column](working-with-tables.md#columns) names, but no data is in the table.  A table may start as empty, take on records and no longer be empty, and then have the records removed and again be empty.

## Description ##

The **IsBlank** function tests for a *blank* value. *Blank* values are found in situations such as these:

- A control property has no formula set for it.
- No value is typed into an input-text control, or no selection is made in a listbox.  You can use **IsBlank** to provide feedback that a field is required.
- A string that contains no characters has a **[Len](function-len.md)** of 0.
- An error occurred in a function. Often, one of the arguments to the function wasn't valid. Many functions return *blank* if the value of an argument is *blank*.
- Connected [data sources](working-with-data-sources.md), such as SQL Server, may use "null" values.  These values appear as *blank* in PowerApps.
- The *else* portion of an **[If](function-if.md)** function wasn't specified, and all conditions were **false**.
- You used the **[Update](function-update-updateif.md)** function but didn't specify a value for all columns. As a result, no values were placed in the columns you didn't specify.

The **IsEmpty** function tests whether a table contains any records. It's equivalent to using the **[CountRows](function-table-counts.md)** function and checking for zero. You can use **IsEmpty** to check for data-source errors by combining it with the **[Errors](function-errors.md)** function.

The return value for both functions is a Boolean **true** or **false**.

## Syntax ##

**IsBlank**( *Value* )

- *Value* – Required. Value to test.

**IsEmpty**( *Table* )

- *Table* - Required. Table to test for records.

## Examples ##

### IsBlank ###

1. Create an app from scratch, add an input-text control, and name it **FirstName**.

1. Add a label, and set its **Text** property to this formula:

	**If( IsBlank( FirstName!Text ), "First Name is a required field." )**

	By default, the **Text** property of an input-text control is set to **"Input Text"**. Because the control contains a value, it isn't blank, and the label control doesn't display any message.

1. Remove all the characters from the input-text control, including any spaces.

	Because the control no longer contains any characters, its **Text** property will be *blank*, and **IsBlank( FirstName!Text )** will be **true**. The required field message is displayed.

You can perform validation by using other tools. See the **[Validate](function-validate.md)** function and [working with data sources](working-with-data-sources.md).  

Other examples:

| Formula | Description | Result |
|---------|-------------|--------|
| **IsBlank( "" )** | A string that contains no characters. | **true** |
| **IsBlank( "Hello" )** | A string that contains one or more characters. | **false** |
| **IsBlank( *AnyCollection* )** | Because the [collection](working-with-data-sources.md#collections) exists, it isn't blank, even if it doesn't contain any records. To check for an empty collection, use **IsEmpty** instead. | **false** |
| **IsBlank( Mid( "Hello", 17, 2 ) )** | The starting character for **[Mid](function-left-mid-right.md)** is beyond the end of the string.  The result is an empty string.  | **true** |
| **IsBlank( If( false, false ) )** | An **[If](function-if.md)** function with no *ElseResult*.  Because the condition is always **false**, this **[If](function-if.md)** always returns *blank*.  | **true** |

### IsEmpty ###

1. Create a collection named **IceCream** by setting the **OnSelect** property of a button to this formula and then pressing the button:

	**Collect( IceCream, { Flavor: "Strawberry", Quantity: 300 }, { Flavor: "Chocolate", Quantity: 100 } )**

	The collection contains this data:

	![](media/function-isblank-isempty/icecream-strawberry-chocolate.png)

	This collection has two records and isn't empty. **IsEmpty( IceCream )** returns **false**, and **CountRows( IceCream )** returns **2**.

2. Empty the collection by changing the **OnSelect** property of the button to this formula and then pressing the button:

	**Clear( IceCream )**

	The collection is now empty:

	![](media/function-isblank-isempty/icecream-clear.png)

	The **[Clear](function-clear-collect-clearcollect.md)** function removes all the records from a collection, resulting in an empty collection. **IsEmpty( IceCream )** returns **true**, and **CountRows( IceCream )** returns **0**.

You can also use **IsEmpty** to test whether a calculated table is empty, as these examples show:

| Formula | Description | Result |
|---------|-------------|--------|
| **IsEmpty( [&nbsp;1,&nbsp;2,&nbsp;3 ] )** | The single-column table contains three records and, therefore, isn't empty.  | **false** |
| **IsEmpty( [&nbsp;] )** | The single-column table contains no records and is empty. | **true** |
| **IsEmpty( Filter( [&nbsp;1,&nbsp;2,&nbsp;3&nbsp;], Value > 5 ) )** | The single-column table contains no values that are greater than 5.  The result from the filter doesn't contain any records and is empty. | **true** |
