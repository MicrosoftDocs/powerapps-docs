---
title: Understand delegation in a canvas app
description: Learn about how to use delegation to process large data sets efficiently in a canvas app.
author: lancedMicrosoft

ms.topic: overview
ms.custom: canvas
ms.reviewer: mkaur
ms.date: 5/22/2025
ms.subservice: canvas-maker
ms.author: lanced
search.audienceType: 
  - maker
contributors:
  - mduelae
  - lanced-microsoft
  - gregli-msft
  
---
# Query limitations: Delegation and query limits

## Understanding delegation
Power Apps works best with a back-end data source when a Power Fx query fully translates into an equivalent query that runs on the data source. Power Apps sends a query the data source understands, the data source runs the query, and Power Apps gets the results. For example, the data source filters the data and only returns the rows that meet the filter criteria. When this works, the query is **delegated** to the data source.

But Power Fx queries can't always translate into equivalent queries on every data source. For example, Dataverse supports more query features than Excel. Dataverse supports the 'in' (membership) query operator, but Excel doesn't. A query is **non-delegable** if it uses a feature the data source doesn't support. If any part of a query expression is nondelegable, Power Apps doesn't delegate any part of the query.

When a query is nondelegable, Power Apps gets the first 500 records from the data source and then runs the actions in the query. You can increase this limit to 2,000 records. [Changing the limit](#changing-the-limit) **Power Apps limits the result size to 500 records to keep your app performing well.** Larger result sets can cause performance issues for your app and Power Apps.

But this limitation can be a problem because the query might return incorrect results if the data source has more than 500 or 2,000 records. For example, if your data source has 10 million records and your query needs to work on the last part of the data, like family names that start with 'Z', and your query uses a nondelegable operator like distinct, you only get the first 500 or 2,000 records. This means you get incorrect results.

**Create your Power Fx queries by using the delegable tables for your data source.** Only use query functions that can be delegated. It's the only way to keep your app performing well and to make sure users can get all the information they need.

Pay attention to delegation warnings that show where delegation isn't possible. If you work with small data sets (fewer than 500 records), you can use any data source and formula because the app processes data locally if the formula can't be delegated.

> [!NOTE]
> Delegation warnings help you manage your app so it returns correct results. If the data in your data source exceeds 500 records and a function can't be delegated, Power Fx marks the formula with a blue underline. 

## Delegable data sources
Delegation works with certain tabular data sources only. If a data source supports delegation, its [connector documentation](/connectors/) explains that support. For example, these popular tabular data sources support delegation:

- [Power Apps delegable functions and operations for Microsoft Dataverse](connections/connection-common-data-service.md#power-apps-delegable-functions-and-operations-for-dataverse) 
- [Power Apps delegable functions and operations for SharePoint](connections/connection-sharepoint-online.md#power-apps-delegable-functions-and-operations-for-sharepoint) 
- [Power Apps delegable functions and operations for SQL Server](connections/sql-connection-overview.md#power-apps-functions-and-operations-delegable-to-sql-server) 
- [Power Apps delegable functions and operations for Salesforce](/connectors/salesforce/#power-apps-delegable-functions-and-operations-for-salesforce) 


Imported Excel workbooks (using the **Add static data to your app** data source), collections, and tables stored in context variables don't need delegation. All this data is already in memory, so you can use the full Power Apps language.

## Delegable functions
Use only formulas that can be delegated. This article lists formula elements that can be delegated. Every data source is different, and not all support all these elements. Check for delegation warnings in your formula.

### Filter functions
**[Filter](functions/function-filter-lookup.md)**, **[Search](functions/function-filter-lookup.md)**, **[First](functions/function-first-last.md)**, and **[LookUp](functions/function-filter-lookup.md)** can be delegated.

Within the **Filter** and **LookUp** functions, use these with columns of the table to select the appropriate records:

* **[And](functions/function-logicals.md)** (including **[&&](functions/operators.md)**), **[Or](functions/function-logicals.md)** (including **[||](functions/operators.md)**), **[Not](functions/function-logicals.md)** (including **[!](functions/operators.md)**)
* **[In](functions/operators.md)** 
        > [!NOTE]
    > [In](functions/operators.md) is only delegated for columns on the base data source. For example, if the data source is the **Accounts** table, `Filter(Accounts, Name in ["name1", "name2"])` delegates to the data source for evaluation. But `Filter(Accounts, PrimaryContact.Fullname in ["name1", "name2"])` isn't delegated because the **Full name** column is on a different table (**PrimaryContact**) than **Accounts**. The expression is evaluated locally.
* **[=](functions/operators.md)**, **[<>](functions/operators.md)**, **[>=](functions/operators.md)**, **[<=](functions/operators.md)**, **[>](functions/operators.md)**, **[<](functions/operators.md)**
* **[+](functions/operators.md)**, **[-](functions/operators.md)**
* **[TrimEnds](functions/function-trim.md)**
* **[IsBlank](functions/function-isblank-isempty.md)**
* **[StartsWith](functions/function-startswith.md)**, **[EndsWith](functions/function-startswith.md)**
* Constant values that are the same across all records, such as control properties and [global and context variables](working-with-variables.md).

You can also use parts of your formula that evaluate to a constant value for all records. For example, **Left( Language(), 2 )**, **Date( 2019, 3, 31 )**, and **Today()** don't depend on any columns of the record, so they return the same value for all records. These values are sent to the data source as a constant and don't block delegation.

The previous list doesn't include these notable items.

* **[If](functions/function-if.md)**
* **[*](functions/operators.md)**, **[/](functions/operators.md)**, **[Mod](functions/function-mod.md)**
*  Column casting operations **[Text](/power-platform/power-fx/reference/function-text)**, **[Value](/power-platform/power-fx/reference/function-value)**
* **[Concatenate](functions/function-concatenate.md)** (including **[&](functions/operators.md)**)
* **[ExactIn](functions/operators.md)**
* String manipulation functions: **[Lower](functions/function-lower-upper-proper.md)**, **[Upper](functions/function-lower-upper-proper.md)**, **[Left](functions/function-left-mid-right.md)**, **[Mid](functions/function-left-mid-right.md)**, **[Len](functions/function-left-mid-right.md)**, ...
* Signals: **[Location](functions/signals.md)**, **[Acceleration](functions/signals.md)**, **[Compass](functions/signals.md)**, ...
* Volatiles: **[Rand](functions/function-rand.md)**, ...
* [Collections](working-with-variables.md)

## Delegation and collections
When you use `With`, `UpdateContext`, or `Set`, they internally create collections. Collections are a static in-memory list of records and don't participate in delegation. You don't see a delegation warning. 

## Query limitations

### Lookup and expand levels
Power Apps lets you use up to two lookup levels. A Power Fx query expression can include a maximum of two lookup functions to maintain performance. When a query expression includes a lookup, Power Apps first queries the base table, then runs a second query to expand the first table with the lookup information. One additional level beyond this is supported as the maximum. But for offline scenarios, only one level of lookup expand is supported.

Expand or join up to 20 entities in a single query. If you need to join more than 20 tables in one query, try creating a view on the data server if possible.

### Expression evaluation - property of entity must be on left side 'LHS' of equality operator
Put the property of an entity to be compared on the left hand side (LHS) of an equation. For example, in the following expression, the entity property **'Business unit ID'.Name** is on the LHS and the expression works:

```power-fx
Filter(
        Budgets,
        'Business unit ID'.Name = LookUp(
            Users,
            'Primary Email' = User().Email,
            'Business Unit'
        ).Name,
        DataCardValue37.Selected.'Date Range String'='Date Range String'
    )
```
But this expression doesn't work:

```power-fx
 Filter(
        Budgets,
        LookUp(
            Users,
            'Primary Email' = User().Email,
            'Business Unit'
        ).Name = 'Business unit ID'.Name,
        'Date Range String'=DataCardValue37.Selected.'Date Range String'
    )
```

### Sorting functions
**[Sort](functions/function-sort.md)** and **[SortByColumns](functions/function-sort.md)** can be delegated.

In **Sort**, the formula can only be the name of a single column and doesn't include other operators or functions.

### Aggregate functions
Some aggregate functions can be delegated based on back-end support. Functions like **[Sum](functions/function-aggregates.md)**, **[Average](functions/function-aggregates.md)**, **[Min](functions/function-aggregates.md)**, and **[Max](functions/function-aggregates.md)** can be delegated. Counting functions, like **[CountRows](functions/function-table-counts.md)** and **[Count](functions/function-table-counts.md)**, can also be delegated. But **[RemoveIf](functions/function-remove-removeif.md)** and **[UpdateIf](functions/function-update-updateif.md)** have delegation restrictions. Only a limited number of data sources support delegation for these functions. For more information, see the [Delegation list](#delegable-data-sources).



## Nondelegable functions
All other functions can't delegate, including these notable functions:

* **[FirstN](functions/function-first-last.md)**, **[Last](functions/function-first-last.md)**, **[LastN](functions/function-first-last.md)**
* **[Choices](functions/function-choices.md)**
* **[Concat](functions/function-concatenate.md)**
* **[Collect](functions/function-clear-collect-clearcollect.md)**, **[ClearCollect](functions/function-clear-collect-clearcollect.md)**
* **[GroupBy](functions/function-groupby.md)**, **[Ungroup](functions/function-groupby.md)**

## Nondelegable limits
Formulas that can't be delegated are processed locally. Local processing lets you use the full Power Apps formula language. But there's a tradeoff: all the data must be brought to the device first, which can mean retrieving a large amount of data over the network. This process can take time and make your app seem slow or unresponsive.

To avoid this, Power Apps limits the amount of data that can be processed locally to 500 records by default. This limit lets you use small data sets completely and refine your use of large data sets by seeing partial results.

Be careful when using this feature because it can confuse users. For example, if you use the **Filter** function with a selection formula that can't be delegated over a data source with a million records, only the first 500 records are scanned. If the record you want is record 501 or 500,001, **Filter** doesn't consider or return it.

Aggregate functions can also be confusing. For example, if you use **Average** over a column in that same million-record data source, **Average** can't be delegated because the expression isn't delegated (see the [earlier note](#aggregate-functions)). Only the first 500 records are averaged. If you're not careful, a user might think a partial answer is complete.

## Changing the limit
The default number of records is 500, but you can change this number for an entire app:

1. Select **Settings**.
1. Under **General**, change the **Data row limit** setting from 1 to 2,000.

In some cases, 2,000 (or 1,000 or 1,500) records is enough for your scenario. You can increase this number to fit your needs, but as you do, your app's performance can degrade, especially for wide tables with many columns. It's still best to delegate as much as possible.

To make sure your app can scale to large data sets, set this value to 1. Anything that can't be delegated returns a single record, which is easy to detect when testing your app. This helps you avoid surprises when moving a proof-of-concept app to production.

## Delegation warnings
Power Apps shows a warning (yellow triangle) when you create a formula that can't be delegated. This makes it easier to know what is and isn't delegated.

Delegation warnings show only on formulas that use delegable data sources. If you don't see a warning but think your formula isn't delegated, check your data source type against the list of [delegable data sources](delegation-overview.md#delegable-data-sources) earlier in this article.

## Examples
In this example, you automatically generate a three-screen app based on a SQL Server table named **[dbo].[Fruit]**. To learn how to generate the app, apply similar principles from the [article about Dataverse](data-platform-create-app.md) to SQL Server.

![Three-screen app.](./media/delegation-overview/products-afd.png)

The gallery's **Items** property uses a formula with the **SortByColumns** and **Search** functions, both of which can be delegated.

In the search box, enter **"Apple"**.

Marching dots briefly appear near the top of the screen as the app communicates with SQL Server to process the search request. All records that match the search criteria appear, even if the data source has millions of records.

![Search text-input control.](./media/delegation-overview/products-apple.png)

The search results include **"Apples"** and **"Pineapple"** because the **Search** function looks everywhere in a text column. To find only records that contain the search term at the start of the fruit's name, use another delegable function, **Filter**, with a more specific search term. For simplicity, remove the **SortByColumns** call.

![Remove SortByColumns call.](./media/delegation-overview/products-apple-delegationwarning.png)

The new results include **"Apples"** but not **"Pineapple"**. A yellow triangle appears next to the gallery and in the screen thumbnail if the left navigation bar shows thumbnails. A blue, wavy line appears under part of the formula. Each of these elements indicates a warning. When you hover over the yellow triangle next to the gallery, this message appears:

![Hover over delegation warning.](./media/delegation-overview/products-apple-yellowwarning.png)

SQL Server is a delegable data source, and **Filter** is a delegable function. However, **Mid** and **Len** can't be delegated to any data source.

But it works, doesn't it? Kind of. That's why this is a warning and not a red, wavy squiggle.

- If the table has fewer than 500 records, the formula works perfectly. All records are brought to the device, and **Filter** is applied locally.
- If the table has more than 500 records, the formula doesn't return record 501 or higher, even if it matches the criteria.

### See also

- [Troubleshoot Power Apps canvas app performance issues](/troubleshoot/power-platform/power-apps/canvas-app-performance/troubleshoot-perf-table) <br>
[Performance tips and best practice to use delegation](performance-tips.md#use-delegation)


[!INCLUDE[footer-include](../../includes/footer-banner.md)]
