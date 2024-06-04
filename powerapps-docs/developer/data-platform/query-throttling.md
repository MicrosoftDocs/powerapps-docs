---
title: "Query throttling (Microsoft Dataverse)"
description: "Read about how the server can throttle a query to reduce system performance impact and what you can do about it."
ms.date: 06/04/2024
ms.topic: article
applies_to: 
  - "Dynamics 365 (online)"
author: pnghub
ms.subservice: dataverse-developer
ms.author: gned
ms.reviewer: pehecke
search.audienceType: 
  - developer
---

# Query throttling

If a specific query creates a disproportional load on the database storing Microsoft Dataverse data, it can starve the database of resources and negatively impact performance of all data operations. When this happens, Dataverse starts throttling that particular query to allow all other scenarios to perform normally.

The primary way in which *query throttling* is different from [Service protection API limits](api-limits.md) is
query throttling targets a specific query that causes a performance degradation while leaving the rest of the traffic unaffected. If the throttled query originates from a non-interactive application, throttling is likely to not be noticeable for end-users. If the query originates from an interactive application, it affects users that exercise that particular scenario.

## Query throttling behavior

Throttling can manifest in three ways:

- A delay is introduced before each execution of the query, making the scenario that uses it slower
- Some fraction of attempts to execute the query are failing with any of the following errors:

|Error code|Hex code|Message|
|---|---|---|
|`-2147187388`|`0x80048544`| `This query cannot be executed because it conflicts with query throttling.`|
|`-2147187132`|`0x80048644`| `This query cannot be executed because it conflicts with Query Throttling; the query uses a leading wildcard value in a filter condition, which will cause the query to be throttled more aggressively.`|
|`-2147186876`|`0x80048744`| `This query cannot be executed because it conflicts with Query Throttling; the query uses a computed column in a filter condition, which will cause the query to be throttled more aggressively.` |

For more information about more aggressively throttled query patterns like leading wild cards can be found in [Optimize performance using FetchXml](fetchxml/optimize-performance.md) and [Optimize performance using QueryExpression](org-service/queryexpression/optimize-performance.md)

## Common causes

Most of the situations when query throttling is necessary fall into one of these two broad categories:

- Some query in a common interactive scenario, for example a saved query used in a grid or a query executed by a plug-in, is inefficient and requires a lot of database resources for each execution

- An automated operation, for example data integration involving moving a large amount of data into or out of Dataverse, executes a query at a high rate that consumes a lot of database resources in aggregate even if each execution is less expensive

## How to avoid query throttling

Query throttling depends on the query and the scenario where it's executed but there are some common guidelines:

- For slow low-frequency queries, typically used in interactive applications, the query structure needs to be changed to make it more efficient

  - Some common guidelines for improving the query performance can be found in [Optimize performance using FetchXml](fetchxml/optimize-performance.md)

- For non-interactive applications the common ways to reduce the database load are:

  - When using [ExecuteMultiple](xref:Microsoft.Xrm.Sdk.Messages.ExecuteMultipleRequest) (or another batching mechanism), reduce the size of the batch
  - If the application is multi-threaded, reduce the number of concurrent threads
  - If you aren't using batching or concurrent requests, add a delay between requests to reduce the request rate