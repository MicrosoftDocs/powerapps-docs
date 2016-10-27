<properties
	pageTitle="Understand delegation | Microsoft PowerApps"
	description="Use delegation to process large data sets efficiently."
	services=""
	suite="powerapps"
	documentationCenter="na"
	authors="gregli-msft"
	manager="anneta"
	editor=""
	tags=""/>

<tags
   ms.service="powerapps"
   ms.devlang="na"
   ms.topic="article"
   ms.tgt_pltfrm="na"
   ms.workload="na"
   ms.date="10/25/2016"
   ms.author="gregli"/>

# Understand delegation #

PowerApps includes a powerful set of functions for filtering, sorting, and shaping data:  **[Filter](functions/function-filter-lookup.md)**, **[Lookup](functions/function-filter-lookup.md)**, **[Sort](functions/function-sort.md)**, **[Search](functions/function-sort.md)**, and **[AddColumns](functions/function-table-shaping.md)** functions to name just a few.  With these functions, you can provide your users with focused access to the information they need.  For those with a database background, this is how you create the equivalent of SQL queries.  

The key to building efficient apps is to minimize the amount of data that needs to be brought to your device.  This could be only a handful of records from a sea of millions, or a single aggregate value based on thousands of records.  Or perhaps only the first set of records can be retrieved, and the rest brought in as the user gestures that they want more.  Being focused can dramatically reduces the processing power, memory, and network bandwidth needed by your app, resulting in snappier response times for your users, even on phones connected via a wireless network.  

*Delegation* is where the expressiveness of PowerApps formulas meets the need to minimize data moving over the network.  In short it means that PowerApps will delegate the processing of data to the data source, rather than moving the data to the app for processing locally.  

Where this becomes complicated, and the reason this article exists, is because not everything that can be expressed in a PowerApps' formula can be delegated to every data source.  The PowerApps language mimics Excel's formula language, designed with complete and instant access to a complete workbook in memory.  As a result, the PowerApps language is far richer than most data sources can support, including powerful database engines such as SQL Server.

**When working with data, you want to only use data sources and formulas that can be delegated.**  It is the best way to keep your app performing well and ensure users can access all the information they expect to.

Without delegation, it is only possible to access the first 500 records of a data source.  This may be fine for small tables of information, but care must be taken if the table is already or may grow to be larger than this limit.

## Delegatable data sources ##

At this time, these data sources support delegation: 

- Common Data Service
- Salesforce
- Microsoft SQL Server

We are continuing to add delegation support to existing data sources, as well as more data sources.

## Delegatable functions ##

The next step is to only use formulas that can be delegated.  Included here are the items in a function that could be delegated.  However, every data source is different, and not all of these are supported by every data source.  Check for blue dot suggestions in your particular formula. 

### Filter functions ###

**Filter** and **LookUp** can be delegated.  Within these functions, the following can be used with columns of the table to select the appropriate records:

* **[And](functions/function-logicals.md)** (including **[&&](functions/operators.md)**), **[Or](functions/function-logicals.md)** (including **[||](functions/operators.md)**), **[Not](functions/function-logicals.md)** (including **[!](functions/operators.md)**)
* **[+](functions/operators.md)**, **[-](functions/operators.md)**
* **[In](functions/operators.md)**
* **[=](functions/operators.md)**, **[<>](functions/operators.md)**, **[>=](functions/operators.md)**, **[<=](functions/operators.md)**, **[>](functions/operators.md)**, **[<](functions/operators.md)**
* **[TrimEnds](functions/function-trim.md)**
* **[IsBlank](functions/function-isblank-isempty.md)**
* Constant values, which do not include context variables or collections

Portions of your formula that evaluate to a constant value for all records can also be used.  For example, **Left( Language(), 2 )** does not depend on any columns of the record and therefore returns the same value for all records.  It is effectively a constant.  Use of context variables, collections, and signals may not be constant and therefore will prevent **Filter** and **LookUp** from being delegated.  

Some notable items missing from the above list:

* **[If](functions/function-if.md)**
* **[*](functions/operators.md)**, **[/](functions/operators.md)**, **[Mod](functions/function-mod.md)**
* **[Concatenate](functions/function-concatenate.md)** (including **[&](functions/operators.md)**)
* **[ExactIn](functions/operators.md)**
* String manipulation functions: **[Lower](functions/function-lower-upper-proper.md)**, **[Upper](functions/function-lower-upper-proper.md)**, **[Left](functions/function-left-mid-right.md)**, **[Mid](functions/function-left-mid-right.md)**, **[Len](functions/function-left-mid-right.md)**, ...
* Signals: **[Location](functions/signals.md)**, **[Acceleration](functions/signals.md)**, **[Compass](functions/signals.md)**, ...
* Volatiles: **[Now](functions/function-now-today-istoday.md)**, **[Rand](functions/function-rand.md)**
* [Context variables and collections](working-with-variables.md)

### Sorting functions ###

**Sort**, **SortByColumns**, and **Search** can be delegated.  

In **Sort**, the formula can only be the name of a single column and can't include other operators or functions.

### Other functions ### 

All other functions do not support delegation, including these notable functions:

* Table shaping: **[AddColumns](functions/function-table-shaping.md)**, **[DropColumns](functions/function-table-shaping.md)**, **[ShowColumns](functions/function-table-shaping.md)**, ... 
* Aggregates: **[Sum](functions/function-aggregates.md)**, **[Average](functions/function-aggregates.md)**, **[Min](functions/function-aggregates.md)**, ... 
* **[First](functions/function-first-last.md)**, **[FirstN](functions/function-first-last.md)**, **[Last](functions/function-first-last.md)**, **[LastN](functions/function-first-last.md)**
* **[CountRows](functions/function-table-counts.md)**, **[CountA](functions/function-table-counts.md)**, **[Count](functions/function-table-counts.md)**
* **[Concat](functions/function-concatenate.md)**
* **[Collect](functions/function-clear-collect-clearcollect.md)**, **[ClearCollect](functions/function-clear-collect-clearcollect.md)**
* **[CountIf](functions/function-table-counts.md)**, **[RemoveIf](functions/function-remove-removeif.md)**, **[UpdateIf](functions/function-update-updateif.md)**

## Non-delegatable limits ##

Formulas that cannot be delegated will be processed locally.  This allows for the full breadth of the PowerApps formula language to be used.  But at a price: all the data must be brought to the device first, which could involve retrieving a large amount of data over the network.  That can take time, giving the impression to users that your app is slow or hung.

To avoid this, PowerApps imposes a limit on the amount of data that can be processed locally from a data source.  The limit is 500 records.  We chose this number so that you would still have complete access to small data sets and you would be able to refine your use of large data sets by seeing partial results.

Obviously care must be taken when using this facility as it can be confusing for users.  For example, consider a **Filter** function with a selection formula that cannot be delegated, over a million record data source.  Since the filtering will be done locally, only the first 500 records of the million records will be scanned.  If the desired record is record 501, or 500,001, it will not be considered or returned by **Filter**.

Another place where this can be a problem is aggregate functions.  Take **Average** over a column of that same million record data source.  Since **Average** cannot be delegated, only the first 500 records will be averaged.  Care must be taken or a partial answer could be misconstrued by a user as a complete answer.

## Blue dot suggestions ##

To make it easier to know what is and is not being delegated, the authoring experience provides blue dot suggestions when a formula contains something that cannot be delegated.  

For example:
 
Obviously, working with non-delegatable formulas could be a problem.  For this reason, the authoring experience will mark non-delegatable formulas with a blue dot:






    



