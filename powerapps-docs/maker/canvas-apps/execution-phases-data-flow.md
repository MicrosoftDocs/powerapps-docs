---
title: Understand canvas apps execution phases and data flow | Microsoft Docs
description: Learn about the execution phases of canvas apps while starting-up, and the flow of data.
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

# Understand canvas apps execution phases and data flow

When a user opens a canvas app, it goes through several phases of execution before showing any user interface. While the app loads, it connects to different [data sources](https://docs.microsoft.com/powerapps/maker/canvas-apps/connections-list#popular-connectors)&mdash;such as SharePoint, Microsoft Dataverse, SQL Server (on-premises), Azure SQL Database (online), Excel, and Oracle.

In this article, you'll learn about the different phases of execution before the app shows the user interface, and how the app connects to the data sources.

## Execution phases in canvas apps

A canvas app goes through the following phases of execution before showing the interface to the user:
 
1. **User authentication**

    Prompts the user, if that person has never opened the app before, to sign-in with credentials for whatever connections the app needs. If the same user opens the app again, that person might be prompted again, depending on the organization’s security policies.

1. **Get metadata**

    Retrieves metadata such as the version of the Power Apps platform on which the app runs and the sources from which it must retrieve data. 

1. **Initialize the app**

    Performs any tasks specified in the [OnStart](https://docs.microsoft.com/powerapps/maker/canvas-apps/reference-properties) property.

1. **Render the screens**

    Renders the first screen with controls that the app has populated with data. If the user opens other screens, the app renders them by using the same process.  

## Data flow in canvas apps

Data calls from Power Apps canvas apps send data sources using the connectors over the OData protocol. OData requests flow to backend layers to reach out the target data source(s), and retrieve data for the client, or commit data to the data source.

Understanding how OData requests travel in the server-side could help you to
optimize your canvas app performance, and your backend data sources.

In this section, you'll learn about how the data flows in canvas apps with different data source types.

### Data flow with online data sources

The following diagram, in Figure1, shows how a typical data request in a canvas
app (left side) is travelling server-side layers and reaching out a target data
source (right side) and then returns the retrieved data back to the client. This
is the typical journey of a data request over various connectors, except the
Microsoft Dataverse connector.  Figure3 visualizes how requests are passed in
the Microsoft Dataverse connector.

![](media/706002e78c4830e1e415ac1dd65089a9.png)

Figure 1. How OData calls travel in Power Apps via connectors, except for the
Microsoft Dataverse connector.

 

Each layer in Figure1 could perform fast or have some overheads while processing
the request.

In many apps, two spots commonly present noticeable overheads:

-   First in a backend data source while processing the request.

-   Second in the client while sending a request or while manipulating received
    data on the heap memory and executing associated JavaScript functions to
    process data to show in screens.


### Data flow with on-premises data gateway

If a canvas app connects to an on-premises data source like SQL server, you need
to have another layer, called on-premises Data Gateway. The on-premises data
gateway is a mandatory part to access on-premises data sources. It takes charge
of converting protocol from OData requests to SQL DML (data manipulation
language) statement. Figure2 illustrates where and how the on-premises data
gateway would be put in place and process data requests.

![](media/9d8b37c195e050da9a8fe9812becb9fb.png)

Figure 2 How OData calls travel to on-premises SQL data source via an
on-premises Data Gateway

 

If the app uses a data source on-premises, the location and specification of
data gateway would also affect the performance of data calls.

### Data flow with Microsoft Dataverse connector

When you use the Microsoft Dataverse connector to access a Microsoft Dataverse
environment, data requests would go to the environment instance directly,
without passing through API management.  Hence, the performance of data calls is
much faster.  By default,  the Microsoft Dataverse connector is created when you
create a new canvas app.

![](media/fda4d09c0075bd19124cc4daf1bbf7cb.png)

Figure 3 How to OData requests travel to the Microsoft Dataverse

With understanding this high-level concept of how data calls travel, let us get
into the detail of performance. Concisely, performance overhead could be
happening at any of the layers from client, APIM, connector, on-premises data
gateway and backend data sources.

## Understand possible sources of slow performance for a canvas app

In many enterprises, the slow performance of Power Apps has statistically been
related to:

1.  The way of implementing the app

2.  the bottleneck in data sources

3.  usage patterns like browser types

4.  geographical location of on-prem data gateway and environment

5.  throttling in a gigantic volume of requests onto a backend within a brief
    period

 

1.  The way of implementing an app: this means many things. When the maker makes
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

2.  The bottleneck in data sources: there are many scenarios making backend data
    source to be bottlenecked. Usually tables in the data source fall into a
    hotspot when many transactional/non-transactional queries are directed to
    the same table or record from different users. In other cases, OData calls
    get slow down if the backend machine hosting the data source is low-end
    machine, if the backend SQL instance has blockings and deadlocks and if it
    suffers from resource contention. Plus, if you have on-premises data gateway
    and it is unhealthy, OData calls could be slow by the bottleneck from the
    data gateway too. In these cases, it must tune the backend data source.

3.  Usage patterns: apps you publish will be used by many users on different
    devices, on different browsers and at different locations having various
    network conditions. As the Power Apps client executes, it is strongly
    recommended to use modern browsers like [new Microsoft
    Edge](https://www.microsoft.com/en-us/edge). If some users are on using
    legacy browsers like Internet Explorer, their experience could be affected.
    Makers are suggested to publish the app regularly. As the Power Apps
    platform is continuously optimized and deployed, your app is regenerated
    within the latest platform optimizations when you republish it.

4.  Geographical location of the environment and on-premises data gateway: users
    can access the app globally. However, it would be better to have the data
    source near most of the end users. When your app access your on-premises
    data source (for example), the location of on-premises data gateway should
    be close to the data source to minimize any extra overhead between the
    gateway and data source.

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