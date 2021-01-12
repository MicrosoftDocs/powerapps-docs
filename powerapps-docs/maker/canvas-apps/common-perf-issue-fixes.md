---
title: Common canvas app performance issues and resolutions | Microsoft Docs
description: Learn about the common performance issues and resolutions for canvas apps.
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

# Common canvas app performance issues and resolutions

You can build canvas apps with diverse options of data sources. Choose the right data source and a connector depending on the business needs and scenarios that the app is designed for. For enterprise apps, Microsoft Dataverse is the recommended data source since it comes with a lot of performance benefits. For apps with small amount of transactions, you can go with any other available data sources in your environment.

Think about the number of users who will use the app when it has published, the volume of CRUD (Create/Update/Delete) transactions, type of data interactions, geographical access, and user’s devices.

Common issues can make your canvas app to run slowly. In this article, you'll learn about some of the most common performance issues, and resolutions for general scenarios, popular events such as OnStart, and data sources such as SQL Server (on-premises), Azure SQL Database, SharePoint, Microsoft Dataverse, and Excel. This information will help you to choose the right data source with your business plan, and growth in mind.

## General performance

Some of the performance issues impact canvas apps regardless of the data source type, or the connector you choose. Let's take a look at the general performance problems and guidelines that apply to all apps and clients running those apps.

### Large data sets loading slowly on different platforms

An app performance may vary when loading large sets of data on different platform like iOS or Android. This variation happens because of different network request limitations for each platform.

Furthermore, the number of concurrent network requests allowed may be different on different platforms. This difference can have a major impact on the data load time for large data sets.

Hence, as a recommendation, restrict loading of data that you need to display on the screen immediately. For additional data, paginate, and cache your data. Refer to the [performance tips and best practices](performance-tips.md) for additional ways to improve the app performance.

### Too many columns retrieved

It's recommended to select only the necessary columns for the app. Adding more, or all columns from the data source downloads all column data. This action results in network overheads, and high memory usage in client devices. And this problem can impact users with mobile devices even more if the network bandwidth is limited, or a device with limited memory, or a legacy processor.

For example, if you use Microsoft Dataverse as the data source for your app, make sure you have enabled the [Explicit Column Selection](use-native-cds-connector.md) feature. This feature allows Power Apps to restrict the data retrieval for only the columns used in the app.

### Unsupported or legacy browsers

Users using unsupported, or legacy browsers such as Internet Explorer may experience performance issues. Ensure the users only use the [supported browsers for running canvas apps](limits-and-config.md#supported-browsers-for-running-canvas-apps).

### Slow performance because of geographical distance

Geographical location of the Dataverse environment, and the proximity of the data source to the end-users impacts performance.

Having an environment close to users is recommended. Though Power Apps uses Content Delivery Network (CDN) for content, data calls still get the data from the data source. Data source located in another geographical location may adversely impact the performance of the app.

Geographical location distances impact performance in different forms, such as latency, reduced throughput, lower bandwidth, and packet loss.

### Allow list not configured

Ensure that you don't block the required service URLs, or add them to your firewall's allow list. For a complete list of all service URLs required to be allowed for Power Apps, go to [Required services](limits-and-config.md#required-services).

## OnStart event

The OnStart event runs when the application is loading. Calling a lot of data in the OnStart event will slow down the load of the app. A screen with heavy dependency of controls and values defined on another screen will be affected with slow screen navigation.

Some of the most common problems experienced in many such situations are:

### High number of calls in OnStart event causing app to start slow

In an enterprise, volume of data calls to a central data source can drive server bottleneck, or resource contention.

Leverage cache mechanism, and optimize data calls. A single app may be used by many users. Hence, a number of data calls per user reach at the server’s endpoints, which could be a spot where the bottleneck, or throttling can happen.

### Latency on OnStart because of heavy scripts

This is one of the most common mistake while designing canvas apps. Makers should only get the necessary data required for the app to start.

Optimize formula in an OnStart event. You can move some formulas to OnVisible event instead. This way, you can let the app start fast, and other steps can continue while the app launches.

## Memory pressure

A check on memory consumption of a canvas app becomes very important as most of the times, the apps run on mobile devices. Memory exceptions in the heap is the most likely cause behind a canvas app that crashes or freezes (hangs) on certain devices.

JavaScript (JS) heap may hit the memory heap celing because to heavy scripts running at client side for adding columns, joining, filtering, sorting, and grouping.

In most cases, out-of-memory exception at the heap in client may trigger the app to crash, or hang.

Profile the app performance using a browser such as [developer tools for Microsoft Edge](https://docs.microsoft.com/microsoft-edge/devtools-guide-chromium/). Check the scenarios that hit the ceiling of JS heap.

When using data from the sources such as Microsoft Dataverse, or SQL Server (online/on-premises), you can use a **View** object to ensure joining/filtering/grouping/sorting occurs on server-side instead of client-side. This approach reduces client overhead of scripting for such actions.

Developer tools for most browsers allow you to profile memory. It would visualize heap size, document, nodes, and listeners.

![An example of memory pressure for an app as seen from the developer tools of a browser](media/common-perf-issue-fixes/memory-pressure.png "An example of memory pressure for an app as seen from the developer tools of a browser")

If client-heavy operations like JOIN, or Group By happened at client with a data set having 2000 records or more, the objects in heap would be increasing resulting in hitting the ceiling.

## SQL Server (online and on-premises)

You can use [SQL Server connector for Power Apps](https://docs.microsoft.com/connectors/sql/) to connect to SQL Server on-premises, or Azure SQL Database.
In this section, you'll learn about common performance related problems with SQL Server as the connector for a canvas app, and resolutions. More information: [Connect to SQL Server from Power Apps](connections/connection-azure-sqldatabase.md), [Create a canvas app from Azure SQL Database](app-from-azure-sql-database.md).

> [!NOTE]
> Though this section references SQL Server connector with performance issues, resolutions for online and on-premises SQL data sources, most of the recommendations also apply when using in general any database type as the data source&mdash;such as MySQL, or PostgreSQL.

The following are the common performance problems that you may encounter with SQL Server connector for canvas apps. Later sections&mdash;[SQL Server on-premises](#sql-server-on-premises), and [Azure SQL Database](#azure-sql-database), list performance problems more relevant to the respective type of data sources.

### N+1 query

Galleries generating too many requests to servers caused N+1 query problem. **N+1** query problem is one of the most commonly experienced problem when using the [gallery](add-gallery.md) control.

Use View objects in SQL backend to avoid the N+1 query problem. Or, change the UI (user interface) scenarios to avoid the problem.

### Table SCAN instead of Index SEEK (SQL)

Queries in database ran table scans instead of index seek. More information: [Hints](https://docs.microsoft.com/sql/t-sql/queries/hints-transact-sql-table?view=sql-server-ver15)

Use [StartsWith](functions/function-startswith.md) instead of [IN](functions/operators#in-and-exactin-operators.md) in formula. For example, when using a SQL data source, the `StartWith` operator results in an index seek; whereas the `IN` operator results in an index or table scan.

### Slow queries

Profile slow queries in a SQL database, and tune if any slow queries are found. This includes index, and query tuning.

For instance, if there was a formula getting certain data with descending (DESC) order on a certain column, that sorting column should have an index with descending order. Be aware that an index key would be creating an ascending (ASC) order by default unless specified otherwise.

You can can also check the URL address of data requests. For example, following data request snippet (partial OData call) asks SQL to return 500 records matching column to *Value* and order by *ID* in descending order.

`Items? \$filter=Column eq ‘Value’ & Orderby = ID desc & top 500`

This helps ascertain index requirements to cover such request conditions. In this situation for example, the ID column should have an index with descending order to perform the query fast.

Check the execution plan of slow queries to see if any table or index scan exists. Check if any excessive cost of Key Lookup in the execution plan of slow queries observed or not. For more information, read [monitor and tune for performance](https://docs.microsoft.com/sql/relational-databases/performance/monitor-and-tune-for-performance).

Additional resources:

- [Monitor and tune for performance](https://docs.microsoft.com/sql/relational-databases/performance/monitor-and-tune-for-performance)
- [Monitor Query Store performance](https://docs.microsoft.com/sql/relational-databases/performance/monitoring-performance-by-using-the-query-store)
- [Use Extended Events to identify, or troubleshoot performance problems](https://docs.microsoft.com/sql/relational-databases/extended-events/extended-events)

### Database resource contention

Enure the data source&mdash;SQL database has no resource contentions such as processor bottleneck, I/O contention, memory pressure, *tempDB* contention. Also check for Locks & Waits, Deadlock, and timeout of queries.

> [!TIP]
> Use [automatic tuning](https://docs.microsoft.com/sql/relational-databases/automatic-tuning/automatic-tuning) for insights into potential query performance problems, recommend solutions, and automatically fix identified problems.

### Thick client or excessive requests

An app running Group By, Filter By, JOIN operations client-side uses processor, and memory resources from the client devices. Depending on the data size, these operations may take more scripting time on client-side, increasing JS heap size on the client.

Since each lookup data call travels to the data source through the data gateway, the total number of data calls becomes more important.

In such situations, use the **View** object in SQL database for Group By, Filter By, or JOIN operations instead of doing such operations at Power Apps client-side. View can select columns and remove some big data type like NVARCHAR(MAX), VARCHAR(MAX), and VARBINARY(MAX) unless necessary.

You can create view(s) with only necessary columns which require for canvas app. Then, use the view entity in canvas app.

> [!TIP]
> This approach also addresses [N+1 query problem](#n1-query).

### Data size transferred to the client

By default, a canvas app shows data using the tables, or views from the available database objects. Retrieving all columns from a table may result in a slow response, especially when using big data types such as NVARCHAR(MAX).

Transferring large amounts of data to clients take time. In addition, this also results in more scripting time with large amounts of data in the JS heap on the client-side.

### SQL Server on-premises

Performance of a canvas apps using SQL Server connector with an on-premises data gateway may get affected in various ways. This section lists the common performance issues, and resolutions when using an on-premises database source.

#### Unhealthy on-premises data gateway

As oOrganizations can define multiple nodes of on-premises data gateway. All such configured nodes should be healthy, on-premises data gateway service should be up and running.

If one of nodes is unreachable, data requests onto the unhealthy node won't not return the result within a decent time resulting in `unreachable` error message after waiting for a while.

Ensure all on-premises data gateway nodes are healthy, and configured at with a decent network latency between the nodes and the SQL instance.

#### Location of on-premises data gateway

Data gateway requires some network calls to on-premises data sources to interpret the OData requests. For instance, data gateway needs to understand the data entity schema to translate OData requests into SQL DML (data manipulation language) statement. However, when the data gateway configured at the other continent with **high network latency** between the data gateway and the SQL instance, it adds extra overhead.

In an enterprise environment, having a scalable data gateway cluster is recommended when heavy data requests are expected. Check how many connections are established between data gateway nodes and the SQL instance.

By checking concurrent connections in an on-premises data gateway or in a SQL server, your organization can decide the point when the data gateway needs to scale out, and with how many nodes.

#### Data gateway scalability

If a large volume of data is expected to be accessed from the on-premises data gateway, just a single node of the on-premises data gateway can become a bottleneck to cover such large volume of requests.

A single node of the on-premises data gateway may be sufficient to deal with 200 or less concurrent connections. Furthermore, if all these concurrent connections are executing queries actively, other requests end up waiting for an available connection.

To ensure on-premises data gateway scales as per the volume of data and requests, [monitor and optimize on-prem data gateway performance](https://docs.microsoft.com/data-integration/gateway/service-gateway-performance).

### Azure SQL Database

Canvas apps can Azure SQL Database using the SQL Server connector. A common performance problem can be introduced when using Azure SQL Database is the selection of an incorrect tier depending on the business requirement.

Azure SQL Database is available in different service tiers, with varied capabilities for matching business requirements. For more information, read the service tiers information in [Azure SQL Database documentation](https://docs.microsoft.com/azure/azure-sql/database/sql-database-paas-overview).

Under heavy data requests, the resources on the tier you select may get throttled once the threshold value is hit. The performance of queries thereafter are compromised.

Check the service tier of Azure SQL Database&mdash;if it is on DTU-Based purchase model. Lower tier would have some limitations and constraints. From a performance perspective, CPU, IO throughput, and latency are important. Hence, check the performance of the SQL database periodically, and check if resource usage exceeds the threshold. For example, on-premises SQL Server normally sets the threshold of CPU usage on around 75%.

## SharePoint

SharePoint connector pipelines to SharePoint list(s). In addition, you can also create canvas apps directly from the SharePoint list. Let's take a look at the common performance problems and resolutions when using a SharePoint data source type.

### Delegation and data size

The size of the data transmitting to the client matters, especially when the SharePoint data source is remote. If formula in the events at canvas app has [non-delegable](delegation-overview.md) functions inside, Power Apps platform retrieves records upto the defined Data Row Limits (500, by default) that can be increased to 2000. If Data Row Limits is set to 2000, and the SharePoint list has many columns, data size transmitting to client can be huge leading to the slowness of the app.

SharePoint provides many [delegable functions](https://docs.microsoft.com/connectors/sharepointonline/#power-apps-delegable-functions-and-operations-for-sharepoint). Check your formula to see if it's delegable. If not, Power Apps retrieves a number of records to the client, set as Data Row Limits (Default 500). And then, applies the formula on this retrieved data set at the client side.

A reduced Data Row Limit inside SharePoint, and use of delegable functions in the Power Apps formula are important for the app to perform.

For a delegable function example, consider an ID column defined as Number data type in the SharePoint list. Both formulas below will return the results as expected. However, the former is non-delegable while the latter is delegable.

| Formula                                           | Delegable? |
|---------------------------------------------------|------------|
| `Filter (‘SharePoint list data source’, ID = 123 )` | Yes        |
| `Filter(‘SharePoint list data source’, ID ="123")`  | No         |

As we assume that the ID column in SharePoint is defined with the data type as Number, the right-hand side value should be numeric variable instead of string variable. Otherwise, such mismatch may trigger the formula to be non-delegable.

### Too many dynamic lookup columns

SharePoint supports various data types&mdash;including dynamic lookups such as *Person*, *Group*, and *Calculated*. If a SharePoint list defines too many dynamics columns, it takes more time to manipulate these dynamic columns within SharePoint before returning data to the client running the canvas app.

Don't overuse dynamic lookup columns, and Person or Group type in SharePoint. This overuse may result in avoidable but additional overhead on the SharePoint side for manipulation of data. For example, you can use static column to keep email aliases, or names of people instead.

### Picture column and Attachment

Size of an image, and attached file can attribute to a slow response while retrieving to the client unless specific columns are specified.

Review your SharePoint list, and ensure only the necessary columns have been defined. The number of columns in the list affects performance of the data requests. This effect is because of the matched records, or the records up to the defined Data Low Limits is retrieved, and transmitted back to client with all columns defined in the list&mdash;whether the app uses all of them, or not.

Enable the **Explicit Column Selection** feature on the canvas app (**File** -> **Settings** -> **Advanced Settings** -> Turn **Explicit column selection** feature *On*) is highly recommended to only query the columns used by the app.

### Large lists

If you have a large list with hundreds of thousands of records, consider partitioning the list, or split the list into several lists based on parameters such as the categories, or date and time.

For instance, your data could be stored on different lists on a yearly, or monthly basis. Then, you can implement the app to let a user select a time window to retrieve the data within that range.

Within a controlled environment, the performance benchmark has proved that the
performance of OData requests against a SharePoint list are highly related to the number of columns in the list and the number of rows retrieving limited by Data row Limits. The lower number of columns, and the lower data row limits setting perform better.

However, in the real-world apps designed for business requirements, it may not be quick or simple to reduce the data rows limits, and columns. Hence,it's recommended to monitor the OData requests at the client side, and
tune Data Row Limits, and the number of columns in a SharePoint list.

## Microsoft Dataverse

When you use the Common Data Service connector to access a Microsoft Dataverse environment, data requests go to the environment instance directly—without passing through API management. More information: [Data call flow with Common Data Service connector](execution-phases-data-flow.md#data-call-flow-with-common-data-service-connector-for-microsoft-dataverse-environment) Microsoft Dataverse has enabled by default so that when you create a
new canvas app connecting to your Microsoft Dataverse instance, data requests
from your app will execute through Microsoft Dataverse onto your
Microsoft Dataverse instance.

Microsoft Dataverse connector performs much faster than the old connector. If
you have existing canvas apps using an old connector, we highly recommend
migrating the app to the Microsoft Dataverse connector.

**Common issues**

1.  Too much data transmitted to a client also made requests be slow. For
    instance, if your app has set Data Row Limits to 2000, instead of default
    500, it adds up extra overhead on transferring data and manipulating
    received data to JS Heap at client side.

2.  The app did run client-heavy scripting such as Filter By/Join at client side
    instead of doing such operation at server side.

3.  Canvas app had used old commondataservice connectors. Firstly, the old
    commondatasource connectors got some overheads. Hence, OData requests via
    the connector were slower than that via Microsoft Dataverse connector.

Recommendations

1.  **Enable Explicit Column Selection (ECS)** which would select only used
    columns in your app instead of retrieving all columns of the entity you used
    in your app.

2.  **Leverage Microsoft Dataverse View.  **Microsoft Dataverse View makes a
    logical view out of entities with joining/ filtering entities. For instance,
    if you should join entities and filter their data, you can define a view via
    Microsoft Dataverse View designer by joining them and define only necessary
    columns. Then, use this view in your app which put load to server by avoid
    the app from joining overhead at client side. This would reduce not only
    extra operations but also data transmission.

3.  **Migrate your app to use Microsoft Dataverse **connector in case your app
    is still using the old connectors such as commondataservice or
    dynamicscrmonline.

4.  Reduce Data Row Limits to 500 at least. Please think about your app really
    requires retrieving more than 500 records or not. As your app might be
    running at mobile/tablet devices, having light-weight data at clients would
    perform better. In many cases, delegable functions cover your business
    logic.

Note: Microsoft Dataverse View only support sorting and filtering as of today.
Group By would be in the future.

| **Note**: By default, out-of-box entities set minimum privileges as Figure4. You can configure many privileges. If you defined custom entities, however, you must set privileges for your custom entities from the Custom Entities tab. Otherwise, app users might not be able to see data from the app you published when users are under Microsoft Dataverse User role. Microsoft Dataverse comes with the built-in [security model](https://docs.microsoft.com/en-us/power-platform/admin/wp-security-cds) which administrators can configure or edit security role privileges and access level for out-of-box entities and custom entities. From PowerApps portal, select a gear icon positioned at the right top, then select Advanced settings. The page would be redirected to Dynamics 365 settings page.  Within the page, click the Settings menu at the top. Find and click Security under System. If you click Security Roles among many menus, it will list up defined Security roles. Find Common Data Service User from the list. When you click the role, you would be landing at Security Role privilege editor [Figure 4], where you can configure security privileges per security role and entities. |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|


![](media/f8391683e9b7c1e97d9b31af8584a47f.png)

Figure 4 Security Role privilege editor

 

## Excel

People in the business world use Excel sheets to manage their business data. The
Excel connector in PowerApps provides connectivity from a canvas app to the data
in Excel data table. By following steps here, you can define a data table(s)
within an Excel file and retrieve such data onto a canvas app.

Although a maker knows a little about other data sources, Excel would be enough
to store your business data based on your format.

However, please be aware that the Excel connector has limitations compared to
other data sources. As it provides little delegable functions, PowerApps loads
data from data table up to 2000 records, nothing more than that. If you really
want to load more than 2000 records, you should do partition your data onto a
different data table and then load both data tables.

Apart from this limitation, there are some cases when slow performance happens.
Let us see what common issues are there.

**Common issues**

1.  Too many data tables are defined, and each data table has an immense size of
    data over many columns. As Excel is not a relational database nor data
    source providing some delegable functions, PowerApps should load data from
    defined data tables and then you can use functions that PowerApps provides
    such as Filter, Sort, JOIN, Group By and Search. If you have defined too
    many data tables and each contains many columns and stores many records,
    obviously launching App would be affected by because each data table should
    be manipulated within JS heap in Browser and the app would also consume
    certain amount of memory for the data(refer to a section how to check memory
    usage of your app using developer tool.)

    1.  Heavy transactions from many users get slow down the app too. We know
        Excel is a product dealing with data in its spread sheets. It is not a
        system nor a relational database. Which means that any data changes from
        your app would be managed by Excel in the same way that Excel does for
        data in spread sheets.  
        If the app mainly reads data from the excel file but rarely triggers
        transactions like Create/Update/Delete, the app will perform well
        although hundreds of thousands of users use the app. However, if heavy
        transactions happen from a small group of users, it would be a big
        offender of slow performance.  
        There is no simple number saying what is the threshold of transactions
        because it is also related to data itself and the size of the data table
        and others like network footprint and user’s devices.

>   The location and size of the excel file. If all data tables are defined
>   within a single file and the file size is big, then extra overheads for
>   downloading the file and reading data to load are expected.  
>   Meanwhile, you can select various storage to store the excel file(s): Azure
>   Blob storage, One Drive for business and so on. Please be aware that the
>   Excel file should be downloaded to the client before loading data out of the
>   data tables defined within the file. You can naturally imagine the
>   downloading time of the file would be adding up on overall performance of
>   your app start.

 

Recommendations

1.  It is better to keep the file near your end-users so that the file can be
    downloaded quickly instead of putting it in a remote location.

2.  Leverage other data sources like Microsoft Dataverse, SQL, or SharePoint
    instead, especially for the Enterprise scale app.

3.  If you have Read-only data, you can import such data into the app itself
    instead of loading it whenever the Power Apps app start.

4.  Split to multiple Excel files with minimum data tables(sheets) and load a
    file when it really requires so that transmitting a file and loading data
    from data table would be scattered.

5.  Define only the necessary columns on the data table at Excel. Loading
    unnecessary columns hurts the performance, obviously.

The Excel connector and Excel file will be a good fit for small transactions and
data. However, it might not be good enough on the enterprise scale.

