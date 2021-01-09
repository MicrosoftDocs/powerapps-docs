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

Regardless of data sources you pick, there are common issues making your canvas app slow in the playing of your app. In this article, you'll learn about some of the most common performance issues, and resolutions for popular events such as OnStart, and data sources such as SQL Server (on-premises), Azure SQL Database, SharePoint, Microsoft Dataverse, and Excel.

This information will help you to choose the right data source with your
business plan and growth in mind.

## General performance guidelines

### Unsupported or legacy browsers

Users using unsupported, or legacy browsers such as Internet Explorer may experience performance issues. Ensure the users only use the [supported browsers for running canvas apps](limits-and-config.md#supported-browsers-for-running-canvas-apps).

### User location

Geographical location of the Dataverse environment, and the proximity of the data source to the end-users impacts performance.

Having an environment close to users is recommended. Though Power Apps uses Content Delivery Network (CDN) for content, data calls still get the data from the data source. Data source located in another geographical location may adversely impact the performance of the app.

Geographical location distances impact performance in different forms, such as latency, reduced throughput, lower bandwidth, and packet loss.

### Allow list

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

![](media/47a38d822105608e02dda54b6c206ca4.png)

If client-heavy operations like JOIN, or Group By happened at client with a data set having 2000 records or more, the objects in heap would be increasing resulting in hitting the ceiling.



## SQL Server (online and on-premises)

> [!NOTE]
> Though this section references SQL Server connector with performance issues, resolutions for online and on-premises SQL data sources, most of the recommendations also apply when using in general any database type as the data source&mdash;such as MySQL, or PostgreSQL.

### N+1 query

Galleries generating too many requests to servers caused N+1 query problem. **N+1** query problem is one of the most commonly experienced problem when using the [gallery](add-gallery.md) control.

Use View objects in SQL backend to avoid the N+1 query problem. Or, change the UI (user interface) scenarios to avoid the problem.

### Table SCAN instead of Index SEEK (SQL)

Queries in database ran table scans instead of index seek. More information: [Hints](https://docs.microsoft.com/sql/t-sql/queries/hints-transact-sql-table?view=sql-server-ver15)

Use [StartsWith](functions/function-startswith.md) instead of [IN](functions/operators#in-and-exactin-operators.md) in formula. For example, when using a SQL data source, the `StartWith` operator results in an index seek; whereas the `IN` operator results in an index or table scan.

### SQL Server on-premises data source

Performance of a canvas apps using SQL Server connector with an on-premises data gateway may get affected in various ways. This section lists the common performance issues, and resolutions when using an on-premises database source.

Common causes

1.  **Thick client or excessive requests:** some canvas app formed formula to do
    Group By, Filter By, JOIN operations client-side. Although canvas app can do
    such operations, they would need CPU and memory resources from client
    devices. Depending on data size, these operations make extra scripting time
    at the client side on top of increasing JS heap size of the client. Be aware
    of each lookup data call also travel to data source via data gateway. In
    this case, the number of data calls is really a matter.

2.  **Unhealthy on-premises data gateway: **As organizations can define multiple
    nodes of on-premises data gateway, all configured nodes should be healthy,
    on-premises data gateway service should be up and running. If one of nodes
    was unreachable, data requests onto the unhealthy node would not return the
    result within a decent time but ‘unreachable’ error message after waiting
    for a while.

3.  **The location of on-premises data gateway: **data gateway requires some
    network calls to on-premises data sources to interpret OData requests. For
    instance, data gateway needs to understand the data entity schema so that
    she could translate OData requests into SQL DML (data manipulation language)
    statement. However, when the data gateway configured at the other continent
    with high** network latency **between the data gateway and SQL instance, it
    would spawn extra overhead.

4.  **Scalability:** In some enterprises, a high volume of data access onto the
    on-premises data gateway would be expected. In this case, just one node of
    the on-premises data gateway could be a bottleneck to cover a large volume
    of requests. A single node of the on-premises data gateway can deal with
    concurrent connections up to 200. If all these concurrent connections are
    executing queries actively, other requests would be waiting for an available
    connection.

Recommendations

1.  Do **use the View object in** SQL database for Group By, Filter By, JOIN
    operations instead of doing such operations at PowerApps client-side. Maker
    or DBA (Database administrator) can create view(s) with only necessary
    columns which require for canvas app. Then, use the view entity in canvas
    app. This approach would also address N+1 query problem.

2.  Make sure all on-premises data gateway nodes are healthy and configured at
    decent network latency between the nodes and SQL instance.

3.  In enterprises, having a scalable data gateway cluster would be recommended
    in case heavy data requests are expected. DBA (Database administrator) can
    check how many connections get set up between data gateway nodes and the SQL
    instance. By checking concurrent connections in an on-premises data gateway
    or in a SQL server, your organization can decide the point when the data
    gateway should be scaled out how many nodes are.

4.  Please do [monitor and optimize on-prem data gateway
    performance](https://docs.microsoft.com/en-us/data-integration/gateway/service-gateway-performance) by
    following instructions in the link. As an on-premises data gateway is in
    organization’s network, Microsoft could not check its performance nor
    health, but organizations should do.

5.  Do profile slow queries in a SQL database and tune if any slow queries are
    found. That is, tune indexes and queries. For instance, if there was a
    formula getting certain data with descending (DESC) order on a certain
    column, that sorting column should have an index with descending order. Be
    aware that an index key would be creating an ascending (ASC) order by
    default unless specified. Makers can also check the URL address of data
    requests. For example, following data request snippet asks SQL to return 500
    records matching Column to Value and order by ID descending. Hence, makers
    can imagine what index requires to cover the request condition.In the
    example below which shows a partial part of an OData call, the ID column
    should have an index with descending order to perform the query
    fast.**Items? \$filter=Column eq ‘Value’ & Orderby = ID desc & top
    500 **Check the execution plan of slow queries to see if any table or index
    scan exists. Check if any excessive cost of Key Lookup in the execution plan
    of slow queries observed or not. When it comes to tune SQL queries, refer to
    this doc, [monitor and tune for
    performance](https://docs.microsoft.com/en-us/sql/relational-databases/performance/monitor-and-tune-for-performance?view=sql-server-ver15).

6.  Make sure your SQL database has no resource contentions such as CPU
    bottleneck, IO contention, Memory pressure and/or tempDB contention, apart
    from checking Locks & Waits, Deadlock and timeout of queries.

**Note**: Azure SQL provides a feature called [Automatic
tuning](https://docs.microsoft.com/en-us/sql/relational-databases/automatic-tuning/automatic-tuning?view=sql-server-ver15).
As it is named, it would create missing indexes automatically and fix the
execution plan performance problems. Consider turning on this feature on SQL
instance.

### Azure SQL Database data source

Organizations can connect to Azure SQL Online via SQL connector. In this case,
slow requests were caused by slow queries in the database and/or the huge volume
of data had to be transmitted to the client. There were the main concerns. In
some case, Service tier of a SQL server was also attributed to slow response.

Common issues

1.  **Data size** **transfer **to client: by default, PowerApps canvas app shows
    data entities which would be either tables or views from database objects.
    All columns of entities would be retrieving, which prompts slow response of
    data requests in case entities have many columns and define many big data
    types like NVARCHAR(MAX). Simply, total data size of transferring data to
    client requires transferring time and scripting time to keep that amount
    data in the JS heap at client side.

2.  **Slow queries**: depending on filtering conditions of data requests, the
    SQL statement which was converted to could be executed with a certain
    execution plan. If the query executed with heavy IO operation by table scan
    or index scan, it means data entities might not have proper indexes covering
    the query. Although the execution plan of queries uses indexes, it could be
    slow too in case Key Lookup costs high. Refer to item\#3,5 and 6 from
    on-premises SQL section above.

3.  [Service
    tier](https://docs.microsoft.com/en-us/azure/sql-database/sql-database-service-tiers-dtu):
    Three Azure SQL Database service tiers—Basic, Standard, and Premium—are
    available. Each tier has a bit different CPU, IO Throughput and
    IO(Input/output) latency. Under heavy data requests, these resources could
    be throttled once the threshold hits. Then, query performance would be
    compromised.

Recommendations

1.  **Monitor and turn slow queries**. check this article: [Monitor and Tune for
    Performance](https://docs.microsoft.com/en-us/sql/relational-databases/performance/monitor-and-tune-for-performance?view=sql-server-ver15).  
    [Query
    Store](https://docs.microsoft.com/en-us/sql/relational-databases/performance/monitoring-performance-by-using-the-query-store?view=sql-server-ver15) would
    also provide the necessary information to find slow queries. You can
    use [Extended
    Events](https://docs.microsoft.com/en-us/sql/relational-databases/extended-events/extended-events?view=sql-server-ver15) to
    trace SQL. If you need more details, please refer to [Quick Start: Extended
    events in SQL
    Server ](https://docs.microsoft.com/en-us/sql/relational-databases/extended-events/quick-start-extended-events-in-sql-server?view=sql-server-ver15)and SSMS
    XEvent Profiler.

2.  **Do use View** object in Azure SQL online for Group By, Filter By, JOIN
    operations instead of doing such operations at PowerApps client-side. In
    addition, View can define only necessary columns. View can select columns
    and remove some big data type like NVARCHAR(MAX), VARCHAR(MAX) and
    VARBINARY(MAX) unless necessary.  Maker or DBA (Database administrator) can
    create view(s) with only necessary columns which require for canvas app.
    Then, use the view entity in canvas app. This approach would also address
    N+1 query problem.

3.  **Check the service tier of Azure SQL online if it is on DTU-Based purchase
    model**. Lower tier would have some limitations and constraints. From a
    performance perspective, CPU, IO throughput and latency would be matter.
    Hence, check the performance of the SQL database and check if resource usage
    exceeds the threshold or not. on-premises SQL normally sets the threshold of
    CPU usage on around 75%, for example.

 

## SharePoint online

SharePoint connector pipelines to SharePoint list(s). From SharePoint list
itself, maker can see Power App menu which wizard would create a canvas app
quickly.

Common issues

1.  **Data size **transmitting back to client is matter, especially when the
    SharePoint data source is remote. If formula in events at canvas app has
    nondelegable functions inside, Power Apps platform would retrieve records up
    to Data Row Limits, default 500 but maker can change it up to 2000. If Data
    Row Limits were set to 2000 and the SharePoint list has many columns, data
    size transmitting to client could be huge and it could lead to slowness.

2.  **Too many dynamic lookup columns: **SharePoint supports various data types
    including dynamic lookup, Person or Group and Calculated. If a SharePoint
    list defines too many dynamics columns, it would take time to manipulate
    these dynamic columns within SharePoint itself before serving asked data
    requests. This would depend on the volume of data rows on the SharePoint
    list.

3.  Picture column and Attachment: size of image and attached file will
    attribute to slow response if they are all retrieving to client unless
    specific columns specified.

Recommendations

1.  As SharePoint provides many [delegable
    functions](https://docs.microsoft.com/en-us/powerapps/maker/canvas-apps/delegation-overview),it
    is worthy checking your formula to see if it would be delegable or not. 
    Otherwise, PowerApps would retrieve the number of records to client, which
    defined within Data Row Limits (Default 500), and then apply formula on a
    retrieved data set at client side. **Not only reducing Data Row Limits to a
    low value or at least staying at the default but also forming the formula to
    be delegable are important to make the app performant**.  
    For instance, let say you have an ID column defined Number data type in the
    list. Both formulas below will return the results as expected. However, the
    former is nondelegable and the latter delegable.

| Formula                                           | Delegable? |   |
|---------------------------------------------------|------------|---|
| Filter (‘SharePoint list data source’, ID = 123 ) | Yes        |   |
| Filter(‘SharePoint list data source’, ID =”123”)  | No         |   |

2.  As we assume that the ID column in SharePoint defined data type as Number,
    right-hand side value should be numeric variable instead of string variable.
    Otherwise, this type of mismatch would trigger the formula to be
    nondelegable.

3.  Review your SharePoint list and make sure only the necessary columns have
    been defined. As number of columns in the list would affect performance of
    data requests because either matched records or records up to data low
    limits would be retrieving and transmitting back to client with all columns
    defined in the list whether the app uses some or not.  
    Enabling Explicit Column Selection (ECS) is highly recommended so that data
    requests would ask only used columns on the app.

4.  Do not overuse dynamic Lookup columns and Person or Group type in
    SharePoint. Otherwise, extra overheads would be seen on the SharePoint side
    to manipulate data before applying any filter or search on.  You can use a
    static column to keep email aliases or names of people instead.

5.  If you have a gigantic list having hundreds of thousands of records,
    consider partitioning the list to split into several ones per category or
    datetime. For instance, your data could be stored on different lists on a
    yearly or monthly base. Then, you can implement the app to let a user select
    a time window to retrieve data within that range.

Within a controlled environment, the performance benchmark has proved that the
performance of OData requests against SharePoint list were highly related to the
number of columns in the list and the number of rows retrieving limited by Data
Low Limits. The lower column and the lower data row limits setting perform the
better. In the real world, however, it is quite hard to simply reduce data rows
limits and columns because the app needs a certain amount of data to cover
business scenarios.  Hence, please monitor OData requests at the client side and
tune these two knobs.

 

## Microsoft Dataverse

### Too many columns retrieved

It's recommended to select only the necessary columns for the app. Adding more, or all columns from the data source downloads all column data. This action results in network overheads, and high memory usage in client devices. And this problem can impact users with mobile devices even more if the network bandwidth is limited, or a device with limited memory, or a legacy processor.

If you use Microsoft Dataverse, make sure you have enabled the [Explicit Column Selection](use-native-cds-connector.md) feature. This feature allows Power Apps to restrict the data retrieval for only the columns used in the app.

As you can check this article ‘[What is
Microsoft Dataverse](https://docs.microsoft.com/en-us/powerapps/maker/common-data-service/data-platform-intro)’,
Microsoft Dataverse provides a handy way to define custom entities with built-in
security model where you can securely store your business data in.

Canvas app can access a Microsoft Dataverse data source which directly connect
to Microsoft Dataverse instance without through API management layer (Refer to
Figure 3.) Microsoft Dataverse has enabled by default so that when you create a
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

 



 

## Conclusion


Makers can build Power Apps applications with diverse options of data sources.
In this article, we walked through many options you could choose with
considerations per data source and connector. While selecting the data sources,
each way has pros and cons.

Depending on the app covering different business needs and scenarios, makers
would be suggested to pick the right data source and a connector.

In the enterprise level of applications, picking up the Microsoft Dataverse data
source and Microsoft Dataverse connector would be the recommended choice as it
comes with lots of benefits and this combination performs well above.

If your application would have small amount of transactions, you can go with
whatever available data sources in your environment.

Plus, the maker should think about the number of users who will use the app when
it has published, the volume of Create/Update/Delete transactions, type of data
interactions, geographical access, and user’s devices as well.
