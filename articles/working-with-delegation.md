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

PowerApps includes a powerful set of functions for filtering, sorting, and shaping data:  **[Filter](functions/function-filter-lookup.md)**, **[Lookup](functions/function-filter-lookup.md)**, **[Sort](functions/function-sort.md)**, **[Search](functions/function-sort.md)**, **[AddColumns](functions/function-table-shaping.md)**, and **[DropColumns](functions/function-table-shaping.md)** functions to name just a few.  With these functions, you can provide your users with focused access to the information they need.  For those with a database background, this is how you create the equivalent of SQL queries.  

The key to building efficient apps is to minimize the amount of data that needs to be brought to your device.  This could be only a handful of records from a sea of millions, or a single aggregate value based on thousands of records.  Or perhaps only the first set of records can be retrieved, and the rest brought in as the user gestures that they want more.  Being focused can dramatically reduces the processing power, memory, and network bandwidth needed by your app, resulting in snappier response times for your users, even on phones connected via a wireless network.  

*Delegation* is where the expressiveness of PowerApps formulas meets the need to minimize the amount of data moving across the network.  In short it means that PowerApps will delegate the processing of data to the data source, rather than moving the data to the app for processing locally.  

Where this becomes complicated, and the reason this article exists, is because not everything that can be expressed in a PowerApps' formula can be delegated to every data source.  The PowerApps language mimics Excel's formula language, designed with complete and instant access to a complete workbook in memory.  As a result, the PowerApps language is far richer than any data source can completely support, including powerful database engines such as SQL Server.

**When working with data, you want to only use functions and operators that can be delegated.**  The authoring experience makes this easy to detect with blue dots on formulas that cannot be delegated.

Besides the improved performance mentioned above, there is another important reasons to seek delegation.  If a formula cannot be delegated, PowerApps will only retrieve the first 500 records of the data.  PowerApps imposes this limit to avoid having apps wait for long periods of time while a large amount of data is retrieved, especially if that was not what the user or author intended.  This can be confusing if a user does not find the data they expect, or the data is used in aggregate functions such as **[Sum](functions/function-aggregated.md)** and **[Average](functions/function-aggregates.md)**.

## Blue dot warnings ##

    

## Delegatable functions ##

The following functions can be delegated:

* Filter
* LookUp (third argument ok)

Within these functions, the following functions and operators can be used in predicates:

* And (including &&), Or (including ||), Not (including !)
* +, -
* In
* =, <>, >=, <=, >, <
* TrimEnds
* IsBlank

Constant formulas.  
Left( Language(), 2 ) Yes
Left( cv, 2 ) NO

Noteable exceltions:
 Concat (including &) P0
*, /, mod P1
ExactIn
* String manupuation functions: Lower, Upper, Left, right, Mid, Len

Column name only:
* Sort
* SortByColumns
* Search

- For **Sort**, the *Formula* argument can only be the name of a single column and can't include other operators or functions. The *SortOrder* argument has no limitations.

All other functions and operators cannot be delegated.  This includes these notable categories:

* Table shaping.  AddColumns, DropColumns, ...  P1
* Aggregates.  Sum, Average, Min, ... P0 
* Count functions: CountRows, CountA, Count P0
* Concatenate

Only names of columns and values that don't vary with the records of the data source can be used.   Context variables and collections not allowed. P0

Signals not supported.  

Blue dot siuggestion.


## Delegatable filter formulas ##  

There are two reasons for this.  The first we have already touched on: the app will result in a better user experience with less resource utilization and less network bandwidth consumed.   


    

It is possible to create a very powerful formula that returns exactly the data that you seek.   

With PowerApps, you can build apps that work with large volumes of data efficiently.  

*Delegation* is how this is accomplished.  


What is desired is the best of both worlds.  All the power of PowerApps formulas with the ability to push the work off the local device.  

For those of you with a database background: delegation is the equivalent of running a SQL query on a SQL server.  PowerApps 

