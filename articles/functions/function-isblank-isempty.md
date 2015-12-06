<properties
	pageTitle="PowerApps: IsBlank and IsEmpty functions"
	description="Reference information for the IsBlank and IsEmpty functions in PowerApps, including syntax and examples"
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

Tests if a value is blank or a [table](working-with-tables.md) contains no [records](working-with-tables.md#records).

## Overview ##

*Blank* is a placeholder for "no value" or "unknown value."  An input text box that has had no characters typed into it is *blank* and when it contains characters it is no longer *blank*.  

All properties and calculated values can be *blank*.  For example, normally a Boolean value has one of two values: **true** or **false**.  But in addition to these two, it can also be *blank*.  This is similar to Microsoft Excel, where a workbook cell starts out as blank but can hold the values **TRUE** or **FALSE**, among others. At any time, the contents of the workbook cell can be removed and it again returns to a *blank* state. 

*Empty* is specific to tables that have no records.  The table structure may be intact, complete with [column](working-with-tables.md#columns) names, but there is no data in the table.  A table may start as empty, take on records and no longer be empty, and then have the records removed and again be empty.

## Description ##

The **IsBlank** function tests for a *blank* value.  Among others, *blank* values are found in these situations:

- A control property has no formula set for it.
- There is no value typed into an Input Text control or selection made in a Listbox control.  You can use **IsBlank** to provide feedback that a field is required. 
- A string which contains no characters and has a **[Len](function-len.md)** of 0.
- An error occurred in a function.  Often one of the arguments to the function was invalid.  For many functions, if *blank* is passed in then it is propagated through as the result of the function.
- Connected [data sources](working-with-data-sources.md) such as SQL Server may use "null" values.  These values appear as *blank* in PowerApps.
- The *else* portion of an **[If](function-if.md)** function was not specified, and all  conditions were **false**.
- A column was not included when using the **[Update](function-update-updateif.md)** function, and no value was placed in that column of the record as a result.

The **IsEmpty** function tests if a table has any records in it.  It is equivalent to using the **[CountRows](function-table-counts.md)** function and checking for zero.  You can use **IsEmpty** to check for data source errors with the **[Errors](function-errors.md)** function.

The return value for both functions is a Boolean **true** or **false**.

## Syntax ##

**IsBlank**( *Value* )

- *Value* – Required. Value to test.

**IsEmpty**( *Table* )

- *Table* - Required. Table to test for records.

## Examples ##

### IsBlank ###

1. Create a "Blank App."

2. Insert an input text control.  Rename it **FirstName**.

3. Insert a label control.  Set its **Text** property to:

	- **If( IsBlank( FirstName!Text ), "First Name is a required field." )**

4. The default value for an input text control is **"Input Text"**.  Since the control contains a value, it is not blank, and the label control does not display any message.

5. Remove all the characters from the input text control, including any spaces.  Since the control no longer contains any characters, its **Text** property will be *blank* and **IsBlank( FirstName!Text )** will be **true**.  The required field message is displayed.

There are other tools for performing validation.  See the **[Validate](function-validate.md)** function and working with data sources.  

Other examples:

| Formula | Description | Result |
|---------|-------------|--------|
| **IsBlank( "" )** | A string that contains no characters. | **true** |
| **IsBlank( "Hello" )** | A string that contains one or more characters. | **false** |
| **IsBlank( *AnyCollection* )** | Since the [collection](working-with-data-sources.md#collections) exists, it is not blank, even if it does not contain any records.  To check for an empty collection, use **IsEmpty** instead. | **false** |
| **IsBlank( Mid( "Hello", 17, 2 ) )** | The starting character for **[Mid](function-left-mid-right.md)** is beyond the end of the string.  The result is an empty string.  | **true** |
| **IsBlank( If( false, false ) )** | An **[If](function-if.md)** function with no *ElseResult*.  Since the condition is always **false**, this **[If](function-if.md)** always returns *blank*.  | **true** |

### IsEmpty ###

1. Let's create a new collection named **IceCream**.  Place a button control on a screen, and set the **OnSelect** property to:

	- **Collect( IceCream, { Flavor: "Strawberry", Quantity: 300 }, { Flavor: "Chocolate", Quantity: 100 } )**

	Press the button and the following collection is populated:

	![](media/function-isblank-isempty/icecream-strawberry-chocolate.png)

	This colleciton has two records and is not empty.  **IsEmpty( IceCream )** returns **false** and **CountRows( IceCream )** returns **2**.

2. Let's empty our collection.  Change the **OnSelect** property of our button to this formula:

	- **Clear( IceCream )** 

	Press the button and the colleciton will be emptied:

	![](media/function-isblank-isempty/icecream-clear.png)

	The **[Clear](function-clear-collect-clearcollect.md)** function removes all the records from a collection, resulting in an empty colleciton.  **IsEmpty( IceCream )** returns **true** and **CountRows( IceCream )** returns **0**.

Calculated tables can also be tested for empty.  Here are some examples:

| Formula | Description | Result |
|---------|-------------|--------|
| **IsEmpty( [&nbsp;1,&nbsp;2,&nbsp;3 ] )** | The single-column table contains three records, and is therefore not empty.  | **false** |
| **IsEmpty( [&nbsp;] )** | The single-column table contains no records, and is empty. | **true** | 
| **IsEmpty( Filter( [&nbsp;1,&nbsp;2,&nbsp;3&nbsp;], Value > 5 ) )** | The single-column table contains only values that are less than 5.  The result from filter will not contain any records and will be empty. | **true** | 