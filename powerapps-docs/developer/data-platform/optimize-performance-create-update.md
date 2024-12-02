---
title: Optimize performance for bulk operations
description: Choose the best approach when building client applications that create or update large numbers records.
author: apurvghai
ms.topic: article
ms.date: 07/01/2024
ms.subservice: dataverse-developer
ms.author: apurvgh
ms.reviewer: jdaly
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
contributors:
  - JimDaly
  - MicroSri
---
# Optimize performance for bulk operations

When you need to create or update thousands or millions of records in Dataverse, the choices you make can save hours of time for the bulk operation project to complete. This article describes the factors that affect performance and the options you have to build client applications that optimize performance for bulk operations. Consideration should also be given to other factors, such as the number of records, record size, network latency, and data complexity.

## Table type

The type of table you choose to store your data has the greatest impact on how much throughput you can expect with bulk operations. Dataverse offers two types of tables: *standard* and *elastic*. 

- A **standard** table stores data using Azure SQL. Standard tables provide transaction support and greater capabilities for modeling relationships.
- An **elastic** table stores data using Azure Cosmos DB. Elastic tables automatically scale horizontally to handle large amounts of data and high levels of throughput with low latency. Elastic tables are suitable for applications that have unpredictable, spiky, or rapidly growing workloads.

If data load times are your primary concern, elastic tables provide the best performance. [Learn about when to use elastic tables](elastic-tables.md#when-to-use-elastic-tables)

## Business logic

Dataverse provides the capability to add extra business logic when records are created or updated by using *plug-ins*. [Plug-ins](plug-ins.md) can be registered to run *synchronously* before or within the transaction of a standard table operation. Elastic tables support plug-ins that can execute before an operation starts because there's no transaction. Any error that occurs in the plug-in code during a synchronous step for a standard table, or before the operation in an elastic table, cancels the operation. A plug-in developer can deliberately throw an exception to cancel the operation to ensure data validation logic is applied.

Any plug-in that is registered to run synchronously increases the time for the operation to complete. To preserve performance:

- **Limit the number of synchronous plug-ins that are registered for the operations.** Add logic to run asynchronously using an asynchronous plug-in or Power Automate flow unless it's essential the logic be applied synchronously.
- **Ensure the plug-ins you have are limited in the logic that they attempt to perform.** While plug-ins must complete within a generous 2-minute time limit, synchronous plug-ins that exceed two seconds to run seriously degrade performance.
- **Ensure plug-ins only run when necessary.** Plug-ins for update operations can be filtered to run only when specific columns are updated.
- **Make sure that plug-ins are optimized to perform logic as efficiently as possible.** For standard tables, you need to consider the impact that transactions and record locks may have on performance. [Learn about scalable customization design](scalable-customization-design/overview.md) and other [best practices for writing plug-ins](best-practices/business-logic/index.md)
- **Choose which API to register your plug-in on.** You can apply synchronous logic to run on the more efficient `CreateMultiple` and `UpdateMultiple` bulk operation APIs. [Learn how to write plug-ins for CreateMultiple and UpdateMultiple](write-plugin-multiple-operation.md).


### Bypass business logic

To expedite the bulk operation project, you can disable plug-ins registered for the create or update operations to improve performance. If the business logic isn't essential, or if you plan other steps to ensure eventual data consistency, you can manually disable the plug-in steps and re-enable them when the bulk operation project is complete. However, disabling plug-ins disables the logic from being applied from *any* client. Any user or other process adding data to Dataverse during this period won't have any of the business logic applied.

As a developer of a client application performing the bulk operation, you can apply an [optional parameter](optional-parameters.md) to the requests you send to by-pass logic. Only a system administrator, or users who have been granted a specific privilege can use this header. [Learn more about how to bypass custom Dataverse logic](bypass-custom-business-logic.md).

## Bulk operation APIs

Dataverse provides [bulk operation APIs](bulk-operations.md) that enable the highest possible throughput for create and update operations. These APIs include `CreateMultiple`, `UpdateMultiple`, and `UpsertMultiple`. For elastic tables only, you can use `DeleteMultiple`.

While these APIs provide the highest throughput, they have the following limitations for standard tables:

- **Not currently available for all tables.** Any custom table should support them, but not all the core Dataverse tables support them, such as Account or Contact. You can run a query provided in the documentation to determine whether a table can use these APIs.
- **Not forgiving of data errors.** You need to make sure that the data you're changing is carefully scrubbed and validated. Any error that occurs within one operation in these APIs causes the entire operation to fail.
- **Not supported to use in plug-ins.** Currently, these APIs should only be used by external client applications.


Bulk operations are available for all elastic tables and elastic tables can return information about individual operations that fail. [Learn more about bulk operations with elastic tables](use-elastic-tables.md#bulk-operations-with-elastic-tables).

## Batch APIs

If you aren't able to use bulk operation APIs, with the SDK for .NET you can use [ExecuteMultiple](org-service/execute-multiple-requests.md), and with Web API you can use [OData $batch](webapi/execute-batch-operations-using-web-api.md).

Use these APIs to group a set of operations in a single request and achieve greater efficiency primarily due to fewer, larger requests reducing the total payload sent and received over the wire for each operation. A client application doesn't need to wait for an operation to finish before sending the next request.

Each operation within the request is applied sequentially on the server, so there's no improved efficiency per operation. However, because the operations are done individually, you can get information about which operations failed, or stop the batch when an error occurs. You can send up to 1,000 operations per request, but for best results we recommend you start with a smaller number and experiment to determine what size batch works best for your case.

> [!NOTE]
> Both bulk operation and batch APIs see significant performance gains when used in parallel. See [Parallel requests](#parallel-requests).

## Client architecture

Dataverse is designed as a data source to support multiple applications with large numbers of concurrent users. To optimize throughput, design your client to use Dataverse's strengths.

Bottlenecks in client-side code are the primary cause of performance issues. Developers frequently fail to fully use the capabilities of the code, which can affect performance. It's crucial to optimize how the client application utilizes the infrastructure's cores or compute, as failure to optimize can significantly affect performance. For example, when using Azure Functions, there are several steps that can be taken to optimize performance, such as implementing autoscaling, using warm-up instances, adjusting CPU usage, utilizing multiple cores, and allowing concurrency.
### Service protection limits

To ensure consistent availability and performance for everyone, Dataverse applies some limits to how APIs are used. These limits are designed to detect when client applications are making extraordinary demands on server resources. Bulk operation projects always make extraordinary demands, so you need to be prepared to manage the errors that service protection limits return. If you aren't getting some service protection limit errors, you haven't maximized the capability of your application.

Service protection limit errors are just another kind of transient error that your client should be prepared to handle, like a temporary loss of network connectivity. A resilient client application must respond to the error by waiting and retrying. The only difference is that service protection limits tell you how long you need to wait before retrying.

Read these articles to learn more:

- [How to retry Dataverse requests](api-limits.md#how-to-retry)
- [Dataverse service protection limits](api-limits.md)
- [Azure best practices: Transient fault handling](/azure/architecture/best-practices/transient-faults)

### Parallel requests

You can see a significant improvement in throughput by [sending requests in parallel](send-parallel-requests.md), but you need to understand how to send them correctly.

### Not all environments are the same

Not every Dataverse environment has the same number of web server resources allocated to it. Dataverse scales to the need of the environment by adding more web server resources to support it. A production environment supporting thousands of active users requires more web servers than a trial environment. When your environment has a lot of web servers, sending requests in parallel can make a dramatic difference in the total throughput your client application can achieve.

### Recommended degree of parallelization (DOP)

Dataverse returns data in a response header that tells you a [recommended degree of parallelization (DOP) for your environment](send-parallel-requests.md#optimum-degree-of-parallelism-dop). Performance worsens if you send more parallel requests than the response header recommends. The client hardware you use to run your application may need more CPU cores to send this many requests in parallel. You may need to use more clients to get maximum throughput. For example, you may use a scaled-out app service or Azure function.

Depending on your client-side architecture, you may need to split recommended degree of parallelism. For example, when you have two clients, and your recommended DOP is 50; configure each client to use 25.

### Disable Azure affinity

When appropriate, you can see best results when you configure your client to use all the available web servers by [removing the Azure affinity cookie](send-parallel-requests.md#server-affinity) that tries to associate your application to a single web server. Disabling Azure affinity isn't appropriate for interactive applications that use cached data from the server to optimize the user experience.

### Optimize your connection

When using .NET, you should [apply configuration changes like the following](send-parallel-requests.md#optimize-your-connection) to optimize your connection so your requests aren't limited by default settings.

```csharp
// Bump up the min threads reserved for this app to ramp connections faster - minWorkerThreads defaults to 4, minIOCP defaults to 4 
ThreadPool.SetMinThreads(100, 100);
// Change max connections from .NET to a remote service default: 2
System.Net.ServicePointManager.DefaultConnectionLimit = 65000;
// Turn off the Expect 100 to continue message - 'true' will cause the caller to wait until it round-trip confirms a connection to the server 
System.Net.ServicePointManager.Expect100Continue = false;
// Can decrease overall transmission overhead but can cause delay in data packet arrival
System.Net.ServicePointManager.UseNagleAlgorithm = false;
```

## Recommendation summary

Based on the factors previously described, follow these recommendations to optimize throughput for bulk operation projects:

- Choose a table type that fits your requirements. Elastic tables have much greater capacity for bulk operations.
- Minimize, disable, or bypass custom business logic on the tables you're using. Configure your client application to bypass custom logic when appropriate.
- Use Dataverse bulk operation APIs when you can, otherwise use batch APIs.
- Design your client application to manage transient errors, including those errors returned by service protection limits.
- Send requests in parallel. Use the response header to guide you to the recommended degree of parallelism (DOP). Disable the affinity cookie when appropriate.
- Validate the data to ensure it meets the table column schema. This can helps prevent errors and reduces the number of failed operations.

### See also

[Elastic tables](elastic-tables.md)   
[Use plug-ins to extend business processes](plug-ins.md)   
[Bypass custom Dataverse logic](bypass-custom-business-logic.md)   
[Bulk Operation messages](bulk-operations.md)   
[Write plug-ins for CreateMultiple and UpdateMultiple](write-plugin-multiple-operation.md)   
[Send parallel requests](send-parallel-requests.md)

[!INCLUDE[footer-include](../../includes/footer-banner.md)]
