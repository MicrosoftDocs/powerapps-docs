---
title: Understand canvas apps execution phases and data call flow | Microsoft Docs
description: Learn about the execution phases of canvas apps while starting-up, and the flow of data calls.
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

# Understand canvas apps execution phases and data call flow

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

## Data call flow in canvas apps

Data calls from Power Apps canvas apps send data sources using the connectors over the OData protocol. OData requests flow to backend layers to reach out the target data source(s), and retrieve data for the client, or commit data to the data source.

Understanding how OData requests travel in the server-side could help you to
optimize your canvas app performance, and your backend data sources.

In this section, you'll learn about how the data call flows in canvas apps with different data source types.

### Data call flow with online data sources

The following diagram shows how a typical data request in a canvas
app (left side) is travels server-side layers, and reaches out to the target data source (right side). And then, returns the data back to the client.

![Typical data call flow for all connectors except the connector for Microsoft Dataverse](media\execution-phases-data-flow\all-connectors-general.png "Typical data call flow for all connectors except the connector for Microsoft Dataverse")

Each layer in the above diagram could perform fast, or have some overheads while processing the request.

In many apps, two spots commonly present noticeable overheads:

1. **Backend data source** - while processing the request.

1. **Client** - while sending the request&mdash;or while manipulating the received data on the heap memory, and executing the associated JavaScript functions to process data to show in screens.

### Data call flow with on-premises data gateway

If a canvas app connects to an on-premises data source like SQL server, you need to have another layer, called on-premises [data gateway](gateway-reference.md).

The on-premises data gateway is a mandatory part to access on-premises data sources. It takes charge of converting protocol from OData requests to SQL DML (Data Manipulation Language) statement.

The following diagram shows where and how the on-premises data
gateway would be put in place and process data requests.

![Data call flow for on-premises connectors](media\execution-phases-data-flow\on-premiess-connectors.png "Data call flow for on-premises connectors")

If the app uses a data source on-premises, the location and the specification of the data gateway would also affect the performance of data calls.

### Data call flow with Common Data Service connector (for Microsoft Dataverse environment)

When you use the Common Data Service connector to access a Microsoft Dataverse
environment, data requests go to the environment instance directly&mdash;without passing through API management. Hence, the performance of data calls is much faster. The Common Data Service connector is created by default when you create a new canvas app.

![Data call flow Common Data Service connector](media\execution-phases-data-flow\on-premiess-connectors.png "Data call flow Common Data Service connector")

With the understanding this high-level concept of how data calls travel, you can get into the details of performance. Concisely, performance overhead can happen at any of the layers&mdash;from client, APIM (API Management), connector, on-premises data gateway, and the backend data sources.

## Next steps

[Possible sources of slow performance for canvas apps](possible-sources-slow-performance.md)
