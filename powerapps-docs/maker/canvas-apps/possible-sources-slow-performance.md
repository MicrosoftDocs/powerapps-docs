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

## App design

Depending on how a particular canvas app is designed, the app may have many different aspects to consider for performance.

Some of the aspects to consider in the app design that may result in slow performance are:

- **App is client-heavy**&mdash;By getting large sets of data into data collections at the very initial moment, and use such data within multiple screens over client-heavy operations like JOIN, Sort, AddColumn and GroupBy.
- **App has long formula in OnStart**&mdash;If the app triggers many unnecessary data calls in screens, and if each data call returns large data records.

To review the app design as a possible source of slow app performance, monitor the app’s behavior by using [Monitor](../monitor-overview.md). Check which data calls are taking a long time, and how many data calls trigger such behaviors in the app.

In addition, balance the workload between the client, and the server. Delegating the workload to the server is recommended. From the client memory consumption perspective, it's important to make the client app lightweight.

## Bottleneck in the data source(s)

There are many possibilities that can result in the bottleneck of the data source(s). Usually, tables in the data source are at the center of activity when many transactional/non-transactional queries are directed to the same table, or record from different users.

OData calls get slow down if:

- The backend machine hosting the data source is a low on resources.
- The backend SQL instance has blockings, deadlocks, and if there's resource contention.
- You have an unhealthy on-premises data gateway, resulting in the OData calls to slow down.

Tune the backend data source(s) when this happens to avoid slow performance of the app.

## Client browsers, devices, and locations

Published canvas apps can be used by users on different devices, browsers, and locations with a varying network conditions. As the Power Apps client executes, ensure to use modern, updated, and [supported browsers](limits-and-config.md#supported-browsers-for-running-canvas-apps).

If some users are using legacy, or unsupported browsers like Internet Explorer 11, their experience could be affected.

Makers are suggested to publish the app regularly. As the Power Apps platform is continuously optimized and deployed, your app is regenerated within the latest platform optimizations when you republish it.

## Geographical location of the on-premises data gateway and environment

Users can access canvas apps globally. However, it's recommended to have the data source near most of the end users. For example, when your app access your on-premises data source, the location of on-premises data gateway should be close to the data source to minimize any extra overhead between the gateway, and the data source.

## Temporary throttling of high volume requests at the backend

Depending on how you design a canvas app, it may generate a lot of data calls within a small period intentionally. For example, an app connecting to a Microsoft Dataverse environment&mdash;subject to the [Dataverse service protection API limits](https://docs.microsoft.com/powerapps/developer/data-platform/api-limits).

Another example is when using [Content Conversation](https://docs.microsoft.com/connectors/conversionservice/) connector. Calls per connection per user are limited to 600 over 60 seconds for this connector.

If an app exceeds the connector's throttling limits, the app is subject to a temporary throttle. When this happens, profiling the app using [Monitor](../monitor-overview.md) would help you to avoid this problem. In addition, if your app is built to generate many such data calls, whether calls get throttled or not, your users may not experience the best experience.

Connector-specific limits are available in [Power Apps connectors](https://docs.microsoft.com/connectors/connector-reference/connector-reference-powerapps-connectors) documentation, and may vary in comparison to other connectors.

Makers can select from a number of data sources available for Power Apps using different [connectors](connections-list.md). Although there are many options to choose a data source from, it's important to choose the
right data source and connector from many perspectives&mdash;architecture,
performance, maintenance, scalability, and so on.

## Next steps

[Common performance issues and resolutions](common-perf-issue-fixes.md)
