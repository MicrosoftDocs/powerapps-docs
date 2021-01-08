---
title: Possible sources of slow performance for a canvas app | Microsoft Docs
description: Learn about the possible sources of slow performance for a canvas app.
author: lancedMicrosoft
ms.service: powerapps
ms.topic: conceptual
ms.custom: canvas
ms.reviewer: tapanm
ms.date: 01/07/2021
ms.author: lanced
search.audienceType: 
  - maker
search.app: 
  - PowerApps
---

# Possible sources of slow performance for a canvas app

Slow performance of a canvas app can be because of several different possibilities. In this article, you'll learn about the most common possible sources of slow performance for a canvas app.

In many enterprises, the slow performance of Power Apps has statistically been
related to the following factors.

Before you begin, ensure you understand the [execution phases and flow of data calls](execution-phases-data-flow.md) in canvas apps.

## App implementation method

App implementation method can include any things. When the maker makes
    the client-heavy app by getting large sets of data into data collections at
    the very initial moment and use such data within multiple screens over
    client-heavy operations like JOIN, Sort, AddColumn and GroupBy, when the app
    has long formula in OnStart, when the app triggers many unnecessary data
    calls in screens and when each data calls returns large data records, then
    the app would perform slow. Monitor the app’s behavior by using the [Power
    Apps
    Monitor](https://powerapps.microsoft.com/en-us/blog/introducing-monitor-to-debug-apps-and-improve-performance/) and
    check what data calls are taking a long time and how many data calls trigger
    scenarios in the app.  The other suggestion is to balance the workload
    between client and server.  Delegating the workload to the server would be
    recommended too. From client memory consumption perspective, it is also
    important to make client app lightweight.

## Bottleneck in the data source(s)

The bottleneck in data sources: there are many scenarios making backend data
    source to be bottlenecked. Usually tables in the data source fall into a
    hotspot when many transactional/non-transactional queries are directed to
    the same table or record from different users. In other cases, OData calls
    get slow down if the backend machine hosting the data source is low-end
    machine, if the backend SQL instance has blockings and deadlocks and if it
    suffers from resource contention. Plus, if you have on-premises data gateway
    and it is unhealthy, OData calls could be slow by the bottleneck from the
    data gateway too. In these cases, it must tune the backend data source.

## Usage patterns - such as browser types

Usage patterns: apps you publish will be used by many users on different
    devices, on different browsers and at different locations having various
    network conditions. As the Power Apps client executes, it is strongly
    recommended to use modern browsers like [new Microsoft
    Edge](https://www.microsoft.com/en-us/edge). If some users are on using
    legacy browsers like Internet Explorer, their experience could be affected.
    Makers are suggested to publish the app regularly. As the Power Apps
    platform is continuously optimized and deployed, your app is regenerated
    within the latest platform optimizations when you republish it.

## Geographical location of the on-premises data gateway and environment

Geographical location of the environment and on-premises data gateway: users
    can access the app globally. However, it would be better to have the data
    source near most of the end users. When your app access your on-premises
    data source (for example), the location of on-premises data gateway should
    be close to the data source to minimize any extra overhead between the
    gateway and data source.



## Ephemeral throttling of high volume requests at the backend



5.  Throttling: In most cases, you might not experience throttling limits unless
    you built your app generates lots of data calls within a small period
    intentionally. Please check [this
    article](https://docs.microsoft.com/en-us/connectors/conversionservice/) 
    and [this
    one](https://docs.microsoft.com/en-us/powerapps/developer/common-data-service/api-limits) .
    For instance, calls per connection per user would be limited to 600 over
    1-minute sliding time window. If your app is built to generate many data
    calls, whether calls get throttled or not, your users might not experience
    the best experience, profiling the app using Power Apps Monitor would help
    you to avoid this problem.

I briefly touched on several points. In the real world, makers can select any
number of data sources
via [connectors](https://docs.microsoft.com/en-us/powerapps/maker/canvas-apps/connections-list) for
Power Apps.  Although there are many options, it is important to choose the
right data source and connector from many perspectives: architecture,
performance, maintenance, scalability and so on. Let us check the details about
what potential performance issues might exist per data source: SQL
(on-premises), Azure SQL online, SharePoint, Microsoft Dataverse, Dynamics, and
Excel. This information will help you to choose the right data source with your
business plan and growth in mind.