---
title: "Query throttling (Microsoft Dataverse)"
description: "Read about how the server can throttle a query that reduces system performance and what you can do about it."
ms.date: 01/08/2025
ms.topic: article
applies_to: 
  - "Dynamics 365 (online)"
author: MsSQLGirl
ms.subservice: dataverse-developer
ms.author: jukoesma
ms.reviewer: pehecke
search.audienceType: 
  - developer
---

# Query throttling

If a query creates a disproportional load on the database storing Microsoft Dataverse data, it can starve the database of resources and negatively impact performance of all data operations. When this happens, Dataverse starts throttling that query to allow all other scenarios to perform normally.

The primary way in which *query throttling* is different from [Service protection API limits](api-limits.md) is
query throttling targets a query that causes a performance degradation while leaving the rest of the traffic unaffected. If the throttled query originates from a non-interactive application, throttling is likely to not be noticeable for end-users. If the query originates from an interactive application, it affects users that exercise that particular scenario.

## Query throttling behavior

Throttling can manifest in three ways:

- A delay is introduced before each execution of the query, making the scenario that uses it slower
- Some fraction of attempts to execute the query are failing with any of the following errors:

|Error code<br />Hex code|Name|Message|
|---|---|---|
|`-2147187388`<br />`0x80048544`|`DataEngineQueryThrottling`|`This query cannot be executed because it conflicts with query throttling.` <br />or <br /> `This query is throttled as it negatively impacts the database health.`|
|`-2147187132`<br />`0x80048644`|`DataEngineLeadingWildcardQueryThrottling`|`This query cannot be executed because it conflicts with Query Throttling; the query uses a leading wildcard value in a filter condition, which will cause the query to be throttled more aggressively.`<br />or <br /> `This query is throttled as it negatively impacts the database health; the query uses a leading wildcard value in a filter condition, which will cause the query to be throttled more aggressively.`|
|`-2147186876`<br />`0x80048744`|`DataEngineComputedColumnQueryThrottling`|`This query cannot be executed because it conflicts with Query Throttling; the query uses a computed column in a filter condition, which will cause the query to be throttled more aggressively.` <br />or <br /> `This query is throttled as it negatively impacts the database health; the query uses a computed column in a filter condition, which will cause the query to be throttled more aggressively.`|
|`-2147186875`<br />`0x80048745`|`DataEnginePerformanceValidationIssuesQueryThrottling`|`This query cannot be executed because it conflicts with Query Throttling; the query has performance validation issues ({0}), which will cause the query to be throttled more aggressively.` <br />or <br /> `This query is throttled as it negatively impacts the database health; the query has performance validation issues ({0}), which will cause the query to be throttled more aggressively.`|

## <a name="DataEnginePerformanceValidationIssuesQueryThrottling"></a> Dataverse error for query throttling caused by anti-patterns

Dataverse heavily throttles queries that use [known query anti-patterns](query-antipatterns.md) when they're identified as a risk to the health of the environment to help prevent outages.

When a query fails due to throttling and the query is using one of the anti-patterns, Dataverse returns the following unique error to help identify which anti-patterns the query is using:

> Name: `DataEnginePerformanceValidationIssuesQueryThrottling`<br />
> Code: `0x80048745`<br />
> Number: `-2147186875`<br />
> Message: `This query cannot be executed because it conflicts with Query Throttling; the query has performance validation issues ({0}), which will cause the query to be throttled more aggressively. Please refer to this document: https://go.microsoft.com/fwlink/?linkid=2162952` 
<br />or <br /> 
`This query is throttled as it negatively impacts the database health; the query has performance validation issues ({0}), which will cause the query to be throttled more aggressively. Please refer to this document: https://go.microsoft.com/fwlink/?linkid=2162952`

[!INCLUDE [cc-query-antipattern-enum-table](includes/cc-query-antipattern-enum-table.md)]

> [!NOTE]
> If a query contains either the `PerformanceLeadingWildCard` or the `FilteringOnCalculatedColumns` anti-pattern, a different Dataverse error is thrown. Queries that use the `PerformanceLeadingWildCard` anti-pattern throw the `DataEngineLeadingWildcardQueryThrottling` error mentioned on this page, and queries that use the `FilteringOnCalculatedColumns` anti-pattern throw the `DataEngineComputedColumnQueryThrottling` error mentioned on this page. 
> 
> The `DataEngineLeadingWildcardQueryThrottling` and `DataEngineComputedColumnQueryThrottling` errors predate the `DataEnginePerformanceValidationIssuesQueryThrottling` error; `DataEngineLeadingWildcardQueryThrottling` and `DataEngineComputedColumnQueryThrottling` continue to be thrown to maintain backward compatibility.  

## Common causes

Most of the situations when query throttling is necessary fall into one of these two broad categories:

- Some query in a common interactive scenario is inefficient and requires a lot of database resources for each execution
  - Common examples are a saved query used in a grid or a query executed by a plug-in

- An automated operation executes a query at a high rate that consumes a lot of database resources in aggregate even if each execution is less expensive
  - A common example is data integration that moves a large amount of data into or out of Dataverse

## How to avoid query throttling

Query throttling depends on the query and the scenario where it runs but there are some common guidelines:

- For slow low-frequency queries, typically used in interactive applications, the query structure needs to be changed to make it more efficient

  - Some common guidelines for improving the query performance can be found in [Optimize performance using FetchXml](fetchxml/optimize-performance.md)

- For non-interactive applications the common ways to reduce the database load are:

  - When using [ExecuteMultiple](xref:Microsoft.Xrm.Sdk.Messages.ExecuteMultipleRequest) (or another batching mechanism), reduce the size of the batch
  - If the application is multi-threaded, reduce the number of concurrent threads
  - If you aren't using batching or concurrent requests, add a delay between requests to reduce the request rate
 
### See also
[Query anti-patterns](query-antipatterns.md)  
[Optimize performance using FetchXml](fetchxml/optimize-performance.md)  
[Optimize performance using QueryExpression](org-service/queryexpression//optimize-performance.md)  
[Service protection API limits](api-limits.md)
