---
title: "Work with Quick Find's search item limit"
description: "Learn about the record limit of a Quick Search and how to avoid hitting the limit."
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

# Work with Quick Find's search item limit

Model-driven apps provide experiences to quickly find records using [quick find search](../../user/quick-find.md) or [Grid search](../../user/grid-filters.md#grid-search). With these experiences, users have a single text input that might be applied to multiple columns in a table.

Today, these experiences use [Dataverse search APIs](search/overview.md) by default. With search, the results can include results from multiple tables for a more comprehensive search capability. Historically, quick find  experiences depended on the capability to perform Dataverse data queries optimized for quick retrieval on a single table. This capability remains and you can use it in your applications, but you should consider whether the Dataverse search APIs are a better fit for your requirement.

Because these queries support specific user experiences in applications, they must return results or fail quickly. The user won't wait a long time for results and these queries can use a lot of system resources because they may have conditions on multiple columns of the table. For these reason, quick find queries return an error when the number results exceeds 10,000 rows. The error returned is:

> Name: `QuickFindQueryRecordLimitExceeded`<br />
> Code: `0x8004E024`<br />
> Number: `-2147164124`<br />
> Message: `The number of records for this search exceeds the Quick Search record limit. Please refine your query and try again.`

You don't need to display this error in your application, but you should expect that it can occur. You can mitigate this by:

- Limiting the number of fields searched by your query
- Include limiting conditions in your query.


This article will explain how the 10,000 search item limit is calculated and includes best practices to avoid hitting this limit.

> [!NOTE]
> A Quick Find is a FetchXML query that contains one of these filter columns: `isquickfindquery`, `isquickfindfields`.

## How the search item limit is calculated

Quick Find queries use a two-stage execution. The first stage uses the Quick
Find filters and the provided search string to gather the records before applying
additional filters. The query engine enforces the 10,000 record limit during this stage.

The second stage uses the result set from the first stage and runs any remaining
filters, for example: related record or security filters.

Consider the following FetchXML Quick Find query:

```xml
<fetch version='1.0' output-format='xml-platform' mapping='logical'>
  <entity name='account'>
    <attribute name='name' />
    <filter type='or' isquickfindfields='1' overridequickfindrecordlimitenabled='1'>
      <condition attribute='name' operator='like' value='%A%' />
    </filter>
    <filter type='and'>
      <condition attribute='statecode' operator='eq' value='0'/>
    </filter>
  </entity>
</fetch>
```

The query engine will execute the condition on "name" first. Since the search is
using wild cards with a short search string, the query will hit the 10k limit
before running any other filters. It is important to note that even if the
result set after the second stage (when applying a state code value) would have
filtered down to less than 10k records, the query engine will hit the exception
in the first stage and not progress to stage two.

## When the search limit does not apply to Quick Find queries

The query engine treats Quick Find queries with 1 or zero search columns as a
standard query and not a Quick Find. Such queries are not subject to the 10,000 record
limit. The reason being Quick Find queries with 1 or less conditions perform
better as a standard query than a Quick Find.

## Avoiding the search limit exception

When writing and executing Quick Find queries in Dynamics 365 Customer Engagement or Dataverse, use the following tips to avoid the 10k search limit:

### Best practices when querying

The following best practices should be observed when querying data.

- Avoid adding unnecessary fields into the Quick Find query view
- Keep queries as precise as possible avoiding generic queries and unnecessary wild cards

### Specific exception querying

If you have a specific need to have a query exceed this limit on a temporary basis, edit the FetchXML query to include setting the `overridequickfindrecordlimitenabled` column equal to 0 within the filter XML element. Use of this column will disable the 10k limit for the specific Quick Find query.

### Organizational override

In extreme cases where a business organization query regularly returns more than 10k search items, an administrator can contact Microsoft Support to request the 10k item limit be disabled. Disabling the limit is not recommended and can result in over consumption of resources and environment wide outages if misused.

### See Also

[Use FetchXML to construct a query](use-fetchxml-construct-query.md)

[!INCLUDE[footer-include](../../includes/footer-banner.md)]
