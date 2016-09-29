<properties
	pageTitle="ForAll function | Microsoft PowerApps"
	description="Reference information, including syntax and examples, for the ForEach function in PowerApps"
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
   ms.date="04/26/2016"
   ms.author="gregli"/>

# ForAll function in PowerApps #

Calculated values and performs actions for all [records](../working-with-tables.md#records) of a [table](../working-with-tables.md).

## Description ##

The **ForAll** function evaluates a formula for all records of a table.

The result of each formula evaluation is returned in a table.  Each result record corresponds, in order, with each of the records in the source table.  If the result of the formula is a single value, the resulting table will be a single column table.  If the result of the formula is a record, the resulting table will contain records with the same columns as the result record.  

The formula can include functions that modify the records of a data source, such as the **[Patch](function-patch.md)** and **[Collect](function-clear-collect-clearcollect.md)** functions.  The formula can also call methods on connections.  Multiple actions can be performed per record by using the [**;** operator](operators.md).  Modifying the table that is the subject of the **ForAll** is not allowed.

Many functions in PowerApps can process more than one value at a time through use of a single column table.  For example, the **Len** function can process a table of text values, returning a table of lengths, in the same manner that **ForAll** could.  This can eliminate the need to use **ForAll** in many cases, can be more efficient, and is easier to read.

When writing your formula, keep in mind that records can be processed in any order and where possible in parallel.  The first record of the table may be processed after the last record.  Functions with side effects must be used with care to avoid ordering dependencies.  For this reason, as they could easily be used to hold a variable that would be susceptible to this effect, the **[UpdateContext](function-updatecontext.md)**, **[Clear](function-clear-collect-clearcollect.md)**, and **[ClearCollect](function-clear-collect-clearcollect.md)** functions cannot be used within a **ForAll**.  **[Collect](function-clear-collect-clearcollect.md)** can be used, but the order in which records are added is undefined.

[AZURE.INCLUDE [record-scope](../../includes/record-scope.md)] 

The **ForAll** function cannot be delegated.   

## Syntax ##

**ForAll**( *Table*, *Formula* )

- *Table* - Required. Table to be acted upon.
- *Formula* - Required.  The formula to evaluate for all records of the *Table*.

## Examples ##

### Calculations ###

The following examples use the **Squares** [data source](../working-with-data-sources.md):

![](media/function-forall/squares.png)

To create this data source as a collection, use this formula as the OnSelect property of a Button control: 
**ClearCollect( Squares, [ "1", "4", "9" ] )**

| Formula | Description | Result |
|---------|-------------|--------|
| **ForAll(&nbsp;Squares,&nbsp;Sqrt(&nbsp;Value&nbsp;)&nbsp;)**<br><br>**Sqrt(&nbsp;Squares&nbsp;)** | For all the records of the input table, calculates the square root of the **Value** column.  The **Sqrt** function can also be used with a single column table, making it possible perform this example without using **ForAll**. | <style> img { max-width: none } </style> ![](media/function-forall/sqrt.png) | 
| **ForAll(&nbsp;Squares,&nbsp;Power(&nbsp;Value,&nbsp;3&nbsp;)&nbsp;)** | For all the records of the input table, raises the **Value** column to the third power.  The **Power** function does not support single column tables and therefore **ForAll** must be used in this case. | <style> img { max-width: none } </style> ![](media/function-forall/power3.png) | 

### Using a Connection ###

The following examples use the **Expressions** [data source](../working-with-data-sources.md):

![](media/function-forall/translate.png)

To create this data source as a collection, use this formula as the OnSelect property of a Button control: 
**ClearCollect( Expressions, [ "Hello", "Good morning", "Thank you", "Goodbye" ] )**

This example also uses a [Microsoft Translator](../connections/connection-microsoft-translator.md) connection.  To add this to your app, see the article on [managing connections](../add-manage-connections.md).

| Formula | Description | Result |
|---------|-------------|--------|
| **ForAll( Expressions, MicrosoftTranslator.Translate( Value, "es" ) )** | For all the records in the Expressions table, translate the contents of the **Value** column into Spanish (abbreviated "es") | <style> img { max-width: none } </style> ![](media/function-forall/translate-es.png) |
| **ForAll( Expressions, MicrosoftTranslator.Translate( Value, "fr" ) )** | For all the records in the Expressions table, translate the contents of the **Value** column into French (abbreviated "fr") | <style> img { max-width: none } </style> ![](media/function-forall/translate-fr.png) |

