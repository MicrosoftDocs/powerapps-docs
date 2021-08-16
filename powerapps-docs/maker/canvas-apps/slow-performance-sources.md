---
title: Common sources of slow performance for a canvas app
description: Learn about the common sources of slow performance for a canvas app.
author: JinManAhn-MSFT
ms.service: powerapps
ms.topic: conceptual
ms.custom: canvas
ms.reviewer: tapanm
ms.date: 08/16/2021
ms.subservice: canvas-maker
ms.author: jiahn
search.audienceType: 
  - maker
search.app: 
  - PowerApps
contributors:
  - JinManAhn-MSFT
  - lancedMicrosoft
  - wimcoor
---

# Common sources of slow performance for a canvas app

A canvas app can perform slowly for several reasons. In this article, you'll learn about the most common possible sources of slow performance for a canvas app. Before you begin, ensure that you understand the [execution phases and flow of data calls](execution-phases-data-flow.md) in canvas apps.

## App design

Depending on how a particular canvas app is designed, it might have many aspects that affect performance. Some that can result in slow performance are:

- **The app is client-heavy**: The app gets large sets of data into data collections initially, and then uses the data within multiple screens over client-heavy operations like **JOIN**, **Sort**, **Add Column**, and **Group By**.
- **The app has a long formula in OnStart**: The app triggers many unnecessary data calls in screens, and these data calls return large data records.

To review the app design as a possible source of slow app performance, monitor the app by using [Monitor](../monitor-overview.md). Check which data calls are taking a long time, and how many data calls trigger such behavior in the app.

Also, balance the workload between the client and server: delegating the workload to the server is recommended. From the perspective of client memory consumption, it's important to make the client app lightweight.

## Bottleneck in the data source

There are many possible causes of bottlenecks in the data source. Usually, tables in the data source are at the center of activity when many transactional/nontransactional queries are directed to the same table or record from different users.

OData calls might slow down if:

- The back-end machine hosting the data source is low on resources.
- The back-end SQL instance has blockings, deadlocks, or resource contention.
- The on-premises data gateway is unhealthy.

When these problems occur, tune the back-end data source to avoid slowing the app's performance.

## Client browsers, devices, and locations

Canvas apps can be used on different devices, browsers, and locations with varying network conditions. As the Power Apps client is executed, be sure to use modern, updated, and [supported browsers](limits-and-config.md#supported-browsers-for-running-canvas-apps).

If some users are using legacy, unsupported, or deprecated browsers like Internet Explorer 11, their experience might be affected.

## Geographical location of the on-premises data gateway and environment

Users can access canvas apps globally. However, we recommend that you locate the data source near most of your users. For example, when your app accesses your on-premises data source, the location of on-premises data gateway should be close to the data source to minimize any extra overhead between the data gateway and the data source.

## Temporary throttling of high-volume requests at the back end

Depending on how you design a canvas app, it can generate many data calls within a short time. For example, an app connecting to a Microsoft Dataverse environment is subject to the [Dataverse service protection API limits](../../developer/data-platform/api-limits.md). Such an app might get throttled when the data calls exceed supported limits.

If an app exceeds the connector's throttling limits, the app is subject to a temporary throttle. Profiling the app by using Monitor can help you to investigate this problem. Also note that apps that generate many avoidable data calls might not give the best user experience, even if the calls don't get throttled.

Makers can select from several data sources available for Power Apps by using different [connectors](connections-list.md). Although there are many options to choose a data source from, choosing the right data source and connector is important from many perspectives&mdash;architecture, performance, maintenance, and scalability.

Connector-specific limits are available in [Power Apps connectors documentation](/connectors/connector-reference/connector-reference-powerapps-connectors), and might vary in comparison to other connectors.

## Debug published app setting enabled

Apps published with the setting [Debug published app](../monitor-canvasapps.md#setting-debug-published-app) enabled perform significantly slower. Publish your app with this setting disabled as soon as you no longer need to view source expressions when debugging your published app.  

## Next steps

[Common canvas app performance issues and resolutions](common-performance-issue-resolutions.md)

### See also

[Understand canvas app execution phases and data call flow](execution-phases-data-flow.md) <br>
[Tips and best practices to improve canvas app performance](performance-tips.md) <br>
[Common issues and resolutions for Power Apps](common-issues-and-resolutions.md) <br>
[Troubleshooting startup issues for Power Apps](../../troubleshooting-startup-issues.md)


[!INCLUDE[footer-include](../../includes/footer-banner.md)]
