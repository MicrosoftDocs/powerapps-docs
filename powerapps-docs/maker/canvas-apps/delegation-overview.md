---
title: Understand delegation in a canvas app
description: Learn about how to use delegation to process large data sets efficiently in a canvas app.
author: lancedMicrosoft

ms.topic: overview
ms.custom: canvas
ms.reviewer: mkaur
ms.date: 3/24/2025
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
Power Apps works best with a back-end data source when a Power Fx query can be fully translated into an equivalent query that can be run on the data source. Power Apps sends a query the data source understands, the query is performed on the data source, and the query results are returned to Power Apps. For instance, the data source might do the work of filtering the data on the data source and only return the rows that meet the filter criteria. When this works correctly, we say that the query is **delegated** to the data source to do the work of the query.

However, Power Fx queries can't always be translated into equivalent queries on all data sources. For example, Dataverse supports more query features than Excel. Dataverse supports the 'in' (membership) query operator and Excel doesn't. We say the query is **non-delegable** if a query uses a feature that the data source doesn't support. In general, if any part of a query expression is nondelegable we don't delegate any part of the query.

When a query is nondelegable, Power Apps gets the first 500 records from the data source and then performs the actions in the query. This limit can be upped to 2,000 records [Changing the limit](#changing-the-limit) **Power Apps limits the result size to 500 records to preserve good performance of Power Apps.** We found through experimentation that result sets greater than these sizes introduce performance issues for your app and Power Apps in general.

However, this limitation can be a problem as the query may return incorrect results if the data on the data source exceeds 500/2000 records. For instance, consider the example where your data source has 10 Million records and your query needs to operate on the last part of the data. (For example, the family names that start with 'Z') However, your query has a nondelegable operator in it (for example, distinct.) In this case, you only get the first 500/2000 records and you have incorrect results.

**Create your Power Fx queries by using the delegable tables for your data source.** You should only use query functions that can be delegated. It's the only way to keep your app performing well and to ensure users can access all the information they need. 

Take heed of delegation warnings that identify places where delegation isn't possible. If you work with small data sets (fewer than 500 records), you can use any data source and formula because the app can process data locally if the formula can't be delegated.

> [!NOTE]
> Delegation warnings help you manage your app so that it has correct results. If the data in your data source exceeds 500 records and a function can't be delegated, Power Fx will mark the formula with a blue underline. 

## Delegable data sources
Delegation is supported for certain tabular data sources only. If a data source supports delegation, its [connector documentation](/connectors/) outlines that support. For example, these tabular data sources are the most popular, and they support delegation:

- [Power Apps delegable functions and operations for Microsoft Dataverse](connections/connection-common-data-service.md#power-apps-delegable-functions-and-operations-for-dataverse) 
- [Power Apps delegable functions and operations for SharePoint](connections/connection-sharepoint-online.md#power-apps-delegable-functions-and-operations-for-sharepoint) 
- [Power Apps delegable functions and operations for SQL Server](connections/sql-connection-overview.md#power-apps-functions-and-operations-delegable-to-sql-server) 
- [Power Apps delegable functions and operations for Salesforce](/connectors/salesforce/#power-apps-delegable-functions-and-operations-for-salesforce) 


Imported Excel workbooks (using the **Add static data to your app** data source), collections, and tables stored in context variables don't require delegation. All of this data is already in memory, and the full Power Apps language can be applied.

## Delegable functions
The next step is to use only those formulas that can be delegated. Included here are the formula elements that could be delegated. However, every data source is different, and not all of them support all of these elements. Check for delegation warnings in your particular formula.

### Filter functions
**[Filter](functions/function-filter-lookup.md)**, **[Search](functions/function-filter-lookup.md)**, **[First](functions/function-first-last.md)** and **[LookUp](functions/function-filter-lookup.md)** can be delegated.  

Within the **Filter** and **LookUp** functions, you can use these with columns of the table to select the appropriate records:

* **[And](functions/function-logicals.md)** (including **[&&](functions/operators.md)**), **[Or](functions/function-logicals.md)** (including **[||](functions/operators.md)**), **[Not](functions/function-logicals.md)** (including **[!](functions/operators.md)**)
* **[In](functions/operators.md)** 
    > [!NOTE]
    > [In](functions/operators.md) is only delegated for columns on the base data source. For instance, if the data source is **Accounts** table then `Filter(Accounts, Name in ["name1", "name2"])` delegates to the data source for evaluation. However, `Filter(Accounts, PrimaryContact.Fullname in ["name1", "name2"])` doesn't delegate since **Full name** column is on a different table (**PrimaryContact**) than **Accounts**. The expression is evaluated locally.
* **[=](functions/operators.md)**, **[<>](functions/operators.md)**, **[>=](functions/operators.md)**, **[<=](functions/operators.md)**, **[>](functions/operators.md)**, **[<](functions/operators.md)**
* **[+](functions/operators.md)**, **[-](functions/operators.md)**
* **[TrimEnds](functions/function-trim.md)**
* **[IsBlank](functions/function-isblank-isempty.md)**
* **[StartsWith](functions/function-startswith.md)**, **[EndsWith](functions/function-startswith.md)**
* Constant values that are the same across all records, such as control properties and [global and context variables](working-with-variables.md).

You can also use portions of your formula that evaluate to a constant value for all records. For example, **Left( Language(), 2 )**, **Date( 2019, 3, 31 )**, and **Today()** don't depend on any columns of the record and, therefore, return the same value for all records. These values can be sent to the data source as a constant and won't block delegation. 

The previous list doesn't include these notable items:

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
When you use 'With', 'UpdateContext' or 'Set' they internally create collections. Collections are a static in-memory list of records and don't participate in delegation. No delegation warning is shown. 

## Query limitations

### Lookup and expand levels
Power Apps allows for up to two lookup levels. This means a Power Fx query expression can include a maximum of two lookup functions to maintain performance. When a query expression includes a lookup, Power Apps first queries the base table, then performs a second query to expand the first table with the lookup information. We support one additional level beyond this as the maximum. However, for offline scenarios, only one level of lookup expands is supported.

You can expand or join up to 20 entities in a single query. If you need to join more than 20 tables in one query, consider creating a view on the data server, if possible.

### Expression evaluation - property of entity must be on left side 'LHS' of equality operator
It's important to place the property of an entity to be compared in an expression on the left hand side 'LHS' of an equation. To illustrate, in the example below the entity property **'Business unit ID'.Name** is a property value and it must be placed on the LHS of the expression to be evaluated. The following expression succeeds:

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
However, this expression won't: 

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

In **Sort**, the formula can only be the name of a single column and can't include other operators or functions.

### Aggregate functions
Certain aggregate functions can be delegated based on back-end support. Functions like **[Sum](functions/function-aggregates.md)**, **[Average](functions/function-aggregates.md)**, **[Min](functions/function-aggregates.md)**, and **[Max](functions/function-aggregates.md)** can be delegated. Counting functions, such as **[CountRows](functions/function-table-counts.md)** and **[Count](functions/function-table-counts.md)**, can also be delegated. However **[RemoveIf](functions/function-remove-removeif.md)** and **[UpdateIf](functions/function-update-updateif.md)** have delegation restrictions. Currently, only a limited number of data sources support delegation for these functions. For more information, see the [Delegation list](#delegable-data-sources).



## nondelegable functions
All other functions don't support delegation, including these notable functions:

* **[FirstN](functions/function-first-last.md)**, **[Last](functions/function-first-last.md)**, **[LastN](functions/function-first-last.md)**
* **[Choices](functions/function-choices.md)**
* **[Concat](functions/function-concatenate.md)**
* **[Collect](functions/function-clear-collect-clearcollect.md)**, **[ClearCollect](functions/function-clear-collect-clearcollect.md)**
* **[GroupBy](functions/function-groupby.md)**, **[Ungroup](functions/function-groupby.md)**

## nondelegable limits
Formulas that can't be delegated will be processed locally. Local processing allows for the full breadth of the Power Apps formula language to be used. But at a price: all the data must be brought to the device first, which could involve retrieving a large amount of data over the network. That can take time, giving the impression that your app is slow or possibly crashed.

To avoid this, Power Apps imposes a limit on the amount of data that can be processed locally: 500 records by default. We chose this number so that you would still have complete access to small data sets and you would be able to refine your use of large data sets by seeing partial results.

Obviously care must be taken when using this facility because it can confuse users. For example, consider a **Filter** function with a selection formula that can't be delegated, over a data source that contains a million records. Because the filtering is done locally, only the first 500 records are scanned. If the desired record is record 501 or 500,001, it isn't considered or returned by **Filter**.

Aggregate functions can also cause confusion. Take **Average** over a column of that same million-record data source. **Average** can't be delegated in this case since the expression isn't delegated (see the [earlier note](#aggregate-functions)), so only the first 500 records are averaged. If you're not careful, a partial answer could be misconstrued as a complete answer by a user of your app.

## Changing the limit
500 is the default number of records, but you can change this number for an entire app:

1. Select **Settings**.
1. Under **General**, change the **Data row limit** setting from 1 to 2000.

In some cases, you know that 2,000 (or 1,000 or 1,500) will satisfy the needs of your scenario. With care, you can increase this number to fit your scenario. As you increase this number, your app's performance may degrade, especially for wide tables with lots of columns. Still, the best answer is to delegate as much as you can.

To ensure that your app can scale to large data sets, reduce down this setting to 1. Anything that can't be delegated returns a single record, which should be easy to detect when testing your app. This can help avoid surprises when trying to take a proof-of-concept app to production.

## Delegation warnings
To make it easier to know what is and isn't being delegated, Power Apps provides warning (yellow triangle) when you create a formula that contains something that can't be delegated.

Delegation warnings appear only on formulas that operate on delegable data sources. If you don't see a warning and you believe your formula isn't being properly delegated, check the type of data source against the list of [delegable data sources](delegation-overview.md#delegable-data-sources) earlier in this article.

## Examples
For this example, you'll automatically generate a three-screen app based on a SQL Server table named **[dbo].[Fruit]**. For information about how to generate the app, you can apply similar principles in the [article about Dataverse](data-platform-create-app.md) to SQL Server.

![Three-screen app.](./media/delegation-overview/products-afd.png)

The gallery's **Items** property is set to a formula that contains **SortByColumns** and **Search** functions, both of which can be delegated.

In the search box, type **"Apple"**.

Marching dots appear momentarily near the top of the screen as the app communicates with SQL Server to process the search request. All records that meet the search criteria appear, even if the data source contains millions of records.

![Search text-input control.](./media/delegation-overview/products-apple.png)

The search results include **"Apples"** and **"Pineapple"** because the **Search** function looks everywhere in a text column. If you wanted to find only records that contain the search term at the start of the fruit's name, you can use another delegable function, **Filter**, with a more complicated search term. (For simplicity, remove the **SortByColumns** call.)

![Remove SortByColumns call.](./media/delegation-overview/products-apple-delegationwarning.png)

The new results include **"Apples"** but not **"Pineapple"**.  However, a yellow triangle appears next to the gallery (and in the screen thumbnail if the left navigation bar shows thumbnails), and a blue, wavy line appears under a portion of the formula. Each of these elements indicates a warning. If you hover over the yellow triangle next to the gallery, this message appears:

![Hover over delegation warning.](./media/delegation-overview/products-apple-yellowwarning.png)

SQL Server is a delegable data source, and **Filter** is a delegable function, However, **Mid** and **Len** can't be delegated to any data source.

But it worked, didn't it? Well, kind of. And that is why this is a warning and not a red, wavy squiggle.

- If the table contains fewer than 500 records, the formula worked perfectly. All records were brought to the device, and **Filter** was applied locally.
- If the table contains more than 500 records, the formula won't return record 501 or higher, even if it matches the criteria.

### See also

[Impact of using non-delegable functions and inappropriate data row limits on performance](common-performance-issue-resolutions.md#use-of-non-delegable-functions-and-inappropriate-data-row-limits-for-non-delegable-queries) <br>
[Performance tips and best practice to use delegation](performance-tips.md#use-delegation)


[!INCLUDE[footer-include](../../includes/footer-banner.md)]
