---
title: Performance considerations for Power Apps  
description: Other performance considerations for Power Apps  
author: lancedMicrosoft
ms.subservice: canvas-developer
ms.topic: article
ms.date: 12/10/2024
ms.author: lanced
ms.reviewer: mkaur
search.audienceType:
  - maker
contributors:
  - lancedMicrosoft
  - mduelae
  
---
# Other performance considerations
In addition to the [four key performance principles](create-performant-apps-overview.md), there are several other possible reasons for poor performance typically due to external factors. 

## Consider the differences in Client browsers, devices, and locations
Canvas apps can be used on different devices, browsers, and locations with varying network conditions. As the Power Apps client is executed, be sure to use modern, updated, and supported browsers. The performance of an app might vary when loading large sets of data on different platforms like iOS or Android. This variation happens because of different network request limitations on each platform. For example, the number of concurrent network requests allowed differs by platform. These differences can have a major impact act on the data load time for large datasets.

## Consider the differences in Geographic location of the on-premises data gateway and environment
Users can access canvas apps globally. However, we recommend that you locate the data source near most of your users. For example, when your app accesses your on-premises data gateway, it’s best to place the gateway near the users who is accessing the app most frequently.

## General Server-side issues
Poor performance might be caused by problems at the server source of the data. This can happen for various reasons. You can use the monitoring tool to assess the specific issue by measuring the data call timings.

### Possible bottlenecks issues in the data source
There are many possible causes of bottlenecks in the data source. Usually, a few tables in the data source are at the center of activity for many queries. Queries might be slow if:

* The data source is missing or has incorrect indexes.
* The query is joining extra-ordinary large amounts of data on the server.
* The query requires a table SCAN, for example, **In** operator instead of using an index like **StartsWith**.
* The back-end machine hosting the data source is low on resources.
* The back-end SQL instance has blockings, deadlocks, or resource contention.
* The on-premises data gateway is unhealthy.
* The on-premises data gateway should be scaled out.

When these problems occur, tune the back-end data source to avoid slowing the app’s performance.

## Specific data sources

### Azure SQL Database
It's important to select the right tier for your business requirements. For more information, see [Azure SQL Database documentation](/azure/azure-sql/database/sql-database-paas-overview). A lower tier has some limitations and constraints. From a performance perspective, CPU, I/O throughput, and latency are important. Therefore, we recommend that you check the performance of the SQL database periodically, and check whether resource usage exceeds the threshold. For example, on-premises SQL Server normally sets the threshold of CPU usage to around 75 percent.

### SharePoint

The SharePoint connector can be used to create apps that use data from SharePoint Lists. Here are some common performance problems and resolutions for SharePoint:

**Avoid too many dynamic lookup columns**: SharePoint supports various data types, including dynamic lookups such as Person, Group, and Calculated. If a list defines too many dynamic columns, it takes more time to manipulate these dynamic columns within SharePoint before returning data to the client running the canvas app. To avoid this, don’t overuse the dynamic lookup columns in SharePoint. For example, use static columns to keep email aliases or people’s names.

**Carefully use the picture column and attachment**: The size of an image and an attached file can contribute to a slow response while retrieving to the client. Review your list, and ensure that only necessary columns have been defined. The number of columns in the list affects the performance of the data requests. This is because the matched records, or the records up to the defined data row limits, are retrieved and transmitted back to the client with all the columns defined in the list—even if the app doesn’t use all of them.

**Consider breaking up large lists**: If you have a large list with hundreds of thousands of records, consider partitioning the list or splitting it into several lists based on parameters such as categories, or date and time. For instance, your data might be stored in different lists on a yearly or monthly basis. In such a case, you can design the app to let a user select a time window and retrieve the data within that range.

### Dataverse
When you use Microsoft Dataverse as the data source, data requests go directly to the environment instance without passing through Azure API Management. So, it tends to be faster than other data sources.  For more information, see [Data call flow when connecting to Microsoft Dataverse.](execution-phases-data-flow.md#data-call-flow-with-microsoft-dataverse)

**Check custom table configurations**: If custom tables are used in Dataverse, additional security configuration might be required for users to view the records with canvas apps. For more information, see [Security concepts in Dataverse](/power-platform/admin/wp-security-cds), [Configure user security to resources in an environment](/power-platform/admin/database-security), and [Security roles and privileges.](/power-platform/admin/security-roles-privileges)

### Excel

The Excel connector allows a canvas app to connect to a table in an Excel file. However, this connector has limitations compared to other data sources. For example, it restricts the canvas app to loading data from the table only up to 2,000 records due to limited delegable functions. To load more than 2,000 records, partition your data in different data tables as other data sources.

**Use the new Excel connector**: Be sure to use the new Excel connector - Excel business online. It allows for multi-user access and handles contention issues better. 

**Only use the columns you need from large data lists in Excel**: An app can perform slowly if the Excel file that has too many data tables or data tables that contain an immense amount of data over several columns. To ensure that your app isn’t affected by this problem, define only the columns you need on the data table in an Excel file.

**Note the limitations of Excel as a database.**  Excel isn’t a relational database system : Any changes from an app are managed by Excel in the same way as if a user were changing data in an Excel file directly. If the app has a high number of reads, but fewer update operations, it might perform well. However, if the app requires heavy transactions, it can adversely affect the performance of the app. There’s no specific threshold value for the number of transactions. It also depends on the data being manipulated. Several other aspects also affect the app’s performance, such as network overhead or the user’s device.

**Consider the differences in geographic location**: The geographic location of the data and its distance from customer locations can be a performance issue. This issue can be amplified if a mobile client has limited bandwidth.

## Enable Preload app for enhanced performance

You can optionally preload your app to increase performance.

1. Sign in to [Power Apps](https://make.powerapps.com).

2. On the left navigation pane, select **Apps**.

3. Select the app and then select **Settings** on the command bar.

4. In the **App settings** pance, set the **Preload app for enhanced performance** to **Yes**. The app will then pre-load.
 
5. For the changes to take effect for apps embedded in Teams, remove and add your app into Teams again.

    > [!NOTE]
    > This makes the compiled app assets accessible via unauthenticated endpoints to enable loading them before authentication. However, users can still only use your app to access data via connectors only after authentication and authorization completes. This behavior ensures that the data an app retrieves from data sources won’t be available to unauthorized users. Compiled app assets include a collection of JavaScript files containing text authored in app controls (such as PCF controls), media assets (such as images), the app name, and the environment URL the app resides in.
    > 
    > In general, apps should retrieve media and information from data sources, through connections. If media and information must be added to the app, without coming from a connection, and it is considered sensitive you may want to disable this setting. Note, disabling this setting will result in users waiting a bit longer to access an app.
