---
title: "Write queries for quick find"
description: "Learn how to write queries to use Dataverse quick find"
ms.date: 01/25/2024
ms.reviewer: jdaly
ms.topic: article
author: NHelgren
ms.subservice: dataverse-developer
ms.author: nhelgren
search.audienceType: 
  - developer
contributors:
  - JimDaly
---
# Write queries for quick find

Model-driven apps provide experiences to quickly find records using [quick find search](../../user/quick-find.md) or [Grid search](../../user/grid-filters.md#grid-search). With these experiences, users have a single text input that might be applied to multiple columns in a table.

Today, these experiences use [Dataverse search APIs](search/overview.md) by default. With search, the results can include results from multiple tables for a more comprehensive search capability. 

Historically, quick find experiences depended on the capability to perform Dataverse data queries optimized for quick retrieval on a single table. This capability remains and you can use it in your applications, but you should consider whether the Dataverse search APIs are a better fit for your requirement.

TODO: Dataverse Quick find still only way to do Grid Search & Lookup Search (combines quick find view with control filter)

Because these queries support specific user experiences in applications, they must return results or fail quickly. The user won't wait a long time for results and these queries can use a lot of system resources because they can have conditions on multiple columns of the table. For these reason, quick find queries return an error when the number results exceeds 10,000 rows. The error returned is:

> Name: `QuickFindQueryRecordLimitExceeded`<br />
> Code: `0x8004E024`<br />
> Number: `-2147164124`<br />
> Message: `The number of records for this search exceeds the Quick Search record limit. Please refine your query and try again.`

You don't need to display this error in your application, but you should expect that it can occur. You can mitigate this by:

- Limiting the number of fields searched by your query
- Include limiting conditions in your query.


This article will explain how the 10,000 search item limit is calculated and includes best practices to avoid hitting this limit.


TODO: Quick find queries must
 - use 'or'
 - use 'isquickfindfields'
 - use 'Like' operators

This is the common pattern, no reason to use others. Not tested with other.

## Work with Quick Find's search item limit