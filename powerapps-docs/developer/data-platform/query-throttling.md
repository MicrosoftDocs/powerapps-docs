---
title: "Query throttling (Microsoft Dataverse)| Microsoft Docs"
description: "Read about how the server can throttle a query to reduce system performance impact and what you can do about it."
ms.custom: ""
ms.date: 04/29/2021
ms.service: powerapps
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
applies_to: 
  - "Dynamics 365 (online)"
ms.assetid: fc3ade34-9c4e-4c33-88a4-aa3842c5eee1
caps.latest.revision: 78
author: "pnghub"
ms.author: "gned"
ms.reviewer: "pehecke"
manager: "mayadumesh"
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---

# Query throttling

If a specific query creates a disproportional load on the database storing
Microsoft Dataverse data, it can starve the database of resources and negatively impact
performance of all data operations. When this happens Dataverse can start
throttling that particular query which would allow all other scenarios to
perform normally.

The primary way in which *query throttling* is different from 
[Service protection API limits](api-limits.md) is
query throttling targets a specific query that causes a performance degradation while
leaving the rest of the traffic unaffected. If the throttled query
originates from a non-interactive application, throttling is likely to not be
noticeable for end-users. If the query originates from an interactive
application it will affect users that exercise that particular scenario.

## Query throttling behavior

Throttling can manifest in two ways:

- A delay is introduced before each execution of the query, making the
    scenario that uses it slower

- Some fraction of attempts to execute the query are failing with a dedicated
    error:

| **Error code** | **Hex code** | **Message**                                                                                                                    |
|----------------|--------------|--------------------------------------------------------------------------------------------------------------------------------|
| \-2147187388   | 0x80048544   | This query cannot be executed because it conflicts with query throttling. Please refer to [Query throttling](query-throttling.md) |

## Common causes

Most of the situations when query throttling is necessary fall into one of the
two broad categories:

- Some query in a common interactive scenario, for example a saved query used
    in a grid or a query executed by a plug-in, is inefficient and requires a lot
    of database resources for each execution

- An automated operation, for example data integration involving moving a
    large amount of data into or out of Dataverse, executes a query at a very
    high rate which consumes a lot of database resources in aggregate even if
    each execution is cheap

## How to avoid query throttling

Query throttling depends on the query and the scenario where it is executed but there are some common guidelines:

- For slow low-frequency queries, typically used in interactive
    applications, the query structure needs to be changed to make it more
    efficient

    - Some common guidelines for improving the query performance can be found
        in [Improve FetchXML request performance](fetchxml-performance.md)

- For non-interactive applications the common ways to reduce the database load
    are:

    - If [ExecuteMultiple](xref:Microsoft.Xrm.Sdk.Messages.ExecuteMultipleRequest) (or another batching mechanism) is used, the batch
        size can be reduced

    - If the application uses concurrency, the number of threads can be reduced

    - A delay between requests can be introduced to reduce the request rate
        when neither batching nor concurrency are used

