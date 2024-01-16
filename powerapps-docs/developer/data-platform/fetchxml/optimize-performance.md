---
title: Optimize performance using FetchXml
description: Learn how to optimize performance when you retrieve data from Microsoft Dataverse using FetchXml.
ms.date: 08/31/2023
ms.reviewer: jdaly
ms.topic: how-to
author: pnghub
ms.subservice: dataverse-developer
ms.author: gned
search.audienceType: 
  - developer
---
# Optimize performance using FetchXml

This article describes ways you can optimize preformance when retrieving data using FetchXml.

## Late Materialize query

If you're experiencing performance issues with an existing long-running query you can try setting a `latematerialize = 'true'` attribute to the [fetch element](reference/fetch.md). Behind the scenes, this setting will break the query up into smaller parts and re-assemble the results before returning them to you.

Using the `latematerialize` attribute might not always provide a performance benefit. It may make simple queries run more slowly. It is most beneficial when your query:

- Has many joins
- Contains many columns
- Contains lookup columns

## Query Hints

> [!IMPORTANT]
> Only apply these options when recommended by Microsoft technical support. Incorrect use of these options can damage the performance of a query.

Microsoft SQL Server supports a number of query hints to optimize queries. FetchXML
supports query hints and can pass these query options to SQL Server using the [fetch element](reference/fetch.md) `[options](reference/fetch.md#options)` attribute.

[!INCLUDE [fetch-options-table](reference/includes/fetch-options-table.md)]


## No lock

In earlier versions, the `no-lock` attribute used to prevent shared locks on records. It is no longer necessary to include this.

<!-- TODO: Include other sections for more performance optimization capabilities and best practices. -->

### See also

[Query data using FetchXml](overview.md)  
[Select columns using FetchXml](select-columns.md)  
[Join tables using FetchXml](join-tables.md)  
[Order rows using FetchXml](order-rows.md)  
[Filter rows using FetchXml](filter-rows.md)  
[Page results using FetchXml](page-results.md)  
[Count rows using FetchXml](count-rows.md)

[!INCLUDE [footer-banner](../../../includes/footer-banner.md)]
