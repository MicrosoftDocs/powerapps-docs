---
title: Common sources of slow performance for a canvas app | Microsoft Docs
description: Learn about the common sources of slow performance for a canvas app.
author: JinManAhn-MSFT
ms.service: powerapps
ms.topic: conceptual
ms.custom: canvas
ms.reviewer: tapanm
ms.date: 01/22/2021
ms.author: jiahn
search.audienceType: 
  - maker
search.app: 
  - PowerApps
---

# Common sources of slow performance for a canvas app

Slow performance of a canvas app can be because of several different possibilities. In this article, you'll learn about the most common possible sources of slow performance for a canvas app.

Before you begin, ensure you understand the [execution phases and flow of data calls](execution-phases-data-flow.md) in canvas apps.

## App design

Depending on how a particular canvas app is designed, the app may have many different aspects to consider for performance.

Some of the aspects to consider in the app design that may result in slow performance are:

- **App is client-heavy** - The app gets large sets of data into data collections at the initial moment. And then, uses such data within multiple screens over client-heavy operations like JOIN, Sort, AddColumn, and GroupBy.
- **App has long formula in OnStart** - The app triggers many unnecessary data calls in screens, and such data calls return large data records.

To review the app design as a possible source of slow app performance, monitor the app by using [Monitor](../monitor-overview.md). Check which data calls are taking a long time, and how many data calls trigger such behaviors in the app.

Also, balance the workload between the client, and the server. Delegating the workload to the server is recommended. From the client memory consumption perspective, it's important to make the client app lightweight.

## Bottleneck in the data source

There are many possibilities that can result in the bottleneck of the data source. Usually, tables in the data source are at the center of activity when many transactional/non-transactional queries are directed to the same table or record from different users.

OData calls may slow down if:

- The backend machine hosting the data source is low on resources.
- The backend SQL instance has blockings, deadlocks, or resource contention.
- On-premises data gateway is unhealthy, resulting in the OData calls to slow down.

Tune the backend data source when these problems occur to avoid slow performance of the app.

## Client browsers, devices, and locations

Canvas apps can be used by users on different devices, browsers, and locations with varying network conditions. As the Power Apps client executes, ensure to use modern, updated, and [supported browsers](limits-and-config.md#supported-browsers-for-running-canvas-apps).

If some users are using legacy, unsupported, or deprecated browsers like Internet Explorer 11, their experience could be affected.

## Geographical location of the on-premises data gateway and environment

Users can access canvas apps globally. However, it's recommended to have the data source near most of the end users.

For example, when your app accesses your on-premises data source, the location of on-premises data gateway should be close to the data source to minimize any extra overhead between the data gateway, and the data source.

## Temporary throttling of high-volume requests at the backend

Depending on how you design a canvas app, it may generate many data calls within a small amount of time. For example, an app connecting to a Microsoft Dataverse environment is subject to the [Dataverse service protection API limits](https://docs.microsoft.com/powerapps/developer/data-platform/api-limits). Such app may get throttled when the data calls exceed the supported limits.

If an app exceeds the connector's throttling limits, the app is subject to a temporary throttle. Profiling the app using [Monitor](../monitor-overview.md) would help you to investigate this problem. In addition, apps generating many avoidable data calls may not give the best user experience, whether the calls get throttled, or not.

Makers can select from several data sources available for Power Apps using different [connectors](connections-list.md). Although there are many options to choose a data source from, it's important to choose the
right data source and connector from many perspectives&mdash;architecture,
performance, maintenance, scalability, and so on.

Connector-specific limits are available in [Power Apps connectors](https://docs.microsoft.com/connectors/connector-reference/connector-reference-powerapps-connectors) documentation, and may vary in comparison to other connectors.

## Next steps

[Common performance issues and resolutions](common-performance-issue-resolutions.md)

### See also

[Understand canvas apps execution phases and data call flow](execution-phases-data-flow.md) <br>
[Tips and best practices to improve canvas apps performance](performance-tips.md) <br>
[Common issues and resolutions](common-issues-and-resolutions.md) <br>
[Troubleshooting startup issues for Power Apps](../../troubleshooting-startup-issues.md)
