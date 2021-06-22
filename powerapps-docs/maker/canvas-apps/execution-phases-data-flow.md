---
title: Understand canvas app execution phases and data call flow
description: Learn about the execution phases of canvas apps while starting-up, and the flow of data calls.
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
contributors:
  - JinManAhn-MSFT
  - lancedMicrosoft
  - yingchin
---

# Understand canvas app execution phases and data call flow

When a user opens a canvas app, the app goes through several phases of execution before showing any user interface. While the app loads, it connects to different [data sources](./connections-list.md#popular-connectors)&mdash;such as SharePoint, Microsoft Dataverse, SQL Server (on-premises), Azure SQL Database (online), Excel, and Oracle.

In this article, you'll learn about these different phases of execution and how an app connects to data sources.

## Execution phases in canvas apps

A canvas app goes through the following phases of execution before showing the interface to a user:

1. **Authenticate the user**: Prompts the first-time user to sign in with credentials for whatever connections the app needs. If that user opens the app again, that person might be prompted again, depending on the organization's security policies.

1. **Get metadata**: Retrieves metadata, such as the version of the Power Apps platform on which the app runs and the sources from which it must retrieve data.

1. **Initialize the app**: Performs any tasks specified in the [OnStart](functions/object-app.md#onstart-property) property.

1. **Render the screens**: Renders the first screen with controls that the app has populated with data. If the user opens other screens, the app renders them by using the same process.  

## Data call flow in canvas apps

Data calls from canvas apps send data sources by using connectors over the OData protocol. OData requests flow to back-end layers to reach out to the target data source and retrieve data for the client, or commit data to the data source.

Understanding how OData requests travel in canvas apps can help you to optimize your canvas app performance and your back-end data sources.

In this section, you'll learn about how the data call flows in canvas apps with different data source types.

### Data call flow with online data sources

The following diagram shows how a typical data request in a canvas app (on the left side) travels server-side layers, reaches out to the target data source (on the right side), and then returns the data to the client.

![Typical data call flow for all connectors except the connector for Dataverse](media\execution-phases-data-flow\all-connectors-general.png "Typical data call flow for all connectors except the connector for Dataverse")

Each layer in the preceding diagram can perform quickly or encounter some overhead while processing the request. In many apps, two particular spots commonly present noticeable overhead:

- **Back-end data source** while processing the request.

- **Client** while sending the request&mdash;or while manipulating the received data on the heap memory and executing the associated JavaScript functions to process data to show in screens.

### Data call flow with on-premises data gateway

If a canvas app connects to an on-premises data source like SQL Server, you need to have another layer called an [*on-premises data gateway*](gateway-reference.md). This gateway is mandatory for accessing on-premises data sources. It takes charge of converting OData protocol requests to SQL Data Manipulation Language (DML) statements.

The following diagram shows where and how the on-premises data gateway is put in place to process data requests.

![Data call flow for an on-premises data gateway](media\execution-phases-data-flow\on-premiess-connectors.png "Data call flow for an on-premises data gateway")

If the app uses a data source on-premises, the location and the specification of the data gateway also affect the performance of data calls.

### Data call flow with Microsoft Dataverse

When you use Microsoft Dataverse as the data source, data requests go to the environment instance directly&mdash;without passing through Azure API Management. Because of this, the performance of data calls is much faster compared to the rest of the data sources. The app is by default connected to Microsoft Dataverse when you create a new canvas app.

![Data call flow with Microsoft Dataverse](media\execution-phases-data-flow\dataverse-connector.png "Data call flow with Microsoft Dataverse")

With the understanding of this high-level concept of how data calls travel, you can get into the details of reviewing the performance of your app. In summary, performance overhead can happen at any of the layers&mdash;from client, API Management, connector, on-premises data gateway, or back-end data sources.

## Next steps

[Common sources of slow performance for a canvas app](slow-performance-sources.md)

### See also

[Common canvas app performance issues and resolutions](common-performance-issue-resolutions.md) <br>
[Tips and best practices to improve canvas app performance](performance-tips.md) <br>
[Common issues and resolutions for Power Apps](common-issues-and-resolutions.md) <br>
[Troubleshooting startup issues for Power Apps](../../troubleshooting-startup-issues.md)


[!INCLUDE[footer-include](../../includes/footer-banner.md)]