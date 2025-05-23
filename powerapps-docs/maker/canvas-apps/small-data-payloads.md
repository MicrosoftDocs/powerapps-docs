---
title: Small data payloads in Power Apps  
description: Small data payloads in Power Apps.
author: lancedMicrosoft
ms.subservice: canvas-developer
ms.topic: article
ms.date: 12/01/2023
ms.author: lanced
ms.reviewer: mkaur
search.audienceType:
  - maker
contributors:
  - lancedMicrosoft
  - mduelae
  
---

# Small data payloads - limit the amount of data you get
One of the most important patterns for enterprise data apps is to limit the size of the data you fetch into Power Apps. If the data payloads are small, nearly everything else gets easier. The Gallery and Table controls do this for you automatically when you connect directly to the data source in the Items property. For instance, when connected directly to a remote data source, a Gallery control pages in data in small increments, for example, 100 records. This default leverages the fact that an end user rarely really needs more than a hundred records for a user task.

## Use delegation
One key way to keep data payloads small is to rely on the data source to do work for you before it gets to Power Apps. **[Delegation](delegation-overview.md)** is when Power Fx can translate a Power Fx expression into a query expression that a data source such as Dataverse, SQL Server, SharePoint, and Excel can handle on its own. And, then Power Fx delegates that query, or gives the responsibility of doing the query work, the data mashup, to the data source. The data source produces the correct data and returns it to Power Apps. 

When the data source is bound directly to a gallery or table, then the data is paged or handed back the data to Power Apps in small performant increments of 100 records. Different data sources have different capabilities. Dataverse, for example, has many more capabilities to filter data on the server than Excel. A good example is CountRows and CountIf. Dataverse supports CountRows in a limited way. Dataverse calculates the size of the table periodically and keep that value around. When CountRows is called, you're given that value. That way it doesn't have to perform a full table scan to get the exact number for every CountRows call. But Dataverse also supports an exact count with CountIf up to 50,000 rows. It supplies these two different capabilities as a way to help preserve good performance of Dataverse server. In contrast, SharePoint doesn't support this function. So, a Power Fx expression with CountRows or CountIf for SharePoint isn't delegated. Instead, Power Apps downloads a limited number of rows, 500 – 2000. Power Fx works on the 500/2000 records locally and returns a result. If your data is always less than 500/2000 records this approach can work. But if it's greater than 500/2000 records you might get incorrect results. 

### Avoid too many columns
By default, Power Apps computes the actual columns you need for a given query using a feature call **Explicit Column Selection**.  This feature is on by default for all new apps. To turn on the explicit column selection feature on the canvas app, go to **Settings** > **Upcoming features** > **Preview**> turn on **Explicit column selection** toggle.


## Suggestions
To achieve the goal of a small data payload, consider the following questions and suggestions:
1. Aim for the default query for a gallery or table to only return approximately 100 – 200 records. If you use a delegable query, this happens automatically. If you're querying an API, or other source that doesn't support delegation, use parameters to refine the results. 

    - Consider using a data source based view that automatically filters the data.  Most enterprise-grade apps make heavy use of views on the data source.
    - Consider using default lookup or filter values to scope the data.  
    -	Consider requiring search arguments in the UI before you show data.
    - Consider these questions about your app:
        - What is necessary on a given screen by default? 
        - What data does the end user really need to take a given business action? 
        - Users generally don’t need thousands of records on an initial screen to accomplish a task.  
    
2. Start building your query for a gallery or table by using the [delegation tables](delegation-overview.md) for your data source. Only choose the functions supported for your query. If your query isn't delegable, what can you do to make it delegable? 



