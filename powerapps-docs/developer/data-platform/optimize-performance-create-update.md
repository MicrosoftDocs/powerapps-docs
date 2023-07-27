---
title: Optimize performance for Create and Update operations | Microsoft Docs
description: Choose the best approach when creating or updating large numbers records.
author: divkamath
ms.topic: article
ms.date: 05/24/2023
ms.subservice: dataverse-developer
ms.author: dikamath
ms.reviewer: jdaly
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
contributors:
  - JimDaly
---
# Optimize performance for Create and Update operations

Dataverse offers several options you can use to maximize total throughput when performing create and update operations with large numbers of records. Learn about the available options and choose the one that is the best for your application.

## Scenarios

Performance is important for all applications, but it's critical for certain scenarios. In this article, we look at bulk data load and plug-ins.

### Elastic tables

Elastic tables are a preview feature at the time of this writing. Elastic tables can provide dramatically improved performance for bulk data operations, but they don't provide strong data consistency or transactions across tables. If performance for bulk operations is most important for your application, consider elastic tables.

More information:

- [Create and edit elastic tables (preview)](../../maker/data-platform/create-edit-elastic-tables.md)
- [Elastic tables (Preview)](elastic-tables.md)
 

### Bulk data operations

When you must create or update large numbers of records, the choice you make as a developer can save hours of time to complete a task. Applications that perform operations in bulk typically make the most extreme requests for shared resources and encounter [Service protection API limits](api-limits.md). This article provides options you may use to achieve maximum throughput for the level of resources allocated to your Dataverse environment.

A key point to recognize in this scenario is: Your code runs in a client application that makes individual calls to Dataverse APIs and you manage any errors that occur. You can retry when an operation fails. The situation is different with plug-ins, especially when they're registered for a synchronous step.

### Plug-ins

Plug-ins extend the behavior of existing Dataverse messages on the server, or to implement the operations to support a custom action. All plug-ins are ultimately, sometimes indirectly, triggered by requests that originate from external calls to Dataverse APIs.

Plug-ins run in a sandbox, which is a virtual computer near, but isolated from the Dataverse server. Your plug-in code is a client application that Dataverse invokes whenever an API call to Dataverse requires the logic your plug-in contains. When registered as part of a synchronous step, the time to perform the plug-in logic contributes to the total time of the operation it extends or implements. Plug-ins registered on synchronous steps can have a significant impact on the total performance of any Dataverse API used by a client application.

Because the synchronous step is part of the transaction, any error that occurs in your plug-in code MUST force the entire operation to roll back in order to maintain data integrity. Unlike bulk data operations from a client application, you can't manage errors except to return the error as an [InvalidPluginExecutionException](xref:Microsoft.Xrm.Sdk.InvalidPluginExecutionException).

Because of the way plug-ins run, there are the following constraints.

- There's a 2-minute time limit for plug-ins to execute. This limit is generous considering the impact that a plug-in registered for a synchronous step can have on the performance of an application. Most synchronous plug-ins should complete in less than 2 seconds.
- You shouldn't use `ExecuteMultiple` or `ExecuteTransaction` operations within plug-ins. These operations are only intended to be used by client applications and they disrupt the transaction behavior required for plug-ins registered for synchronous steps. More information: [Don't use batch request types in plug-ins and workflow activities](best-practices/business-logic/avoid-batch-requests-plugin.md)
- You shouldn't try to use techniques that involve performing operations in parallel. You must develop your plug-ins knowing that the calls are performed sequentially and may need to be rolled back. More information: [Don't use parallel execution within plug-ins and workflow activities](best-practices/business-logic/do-not-use-parallel-execution-in-plug-ins.md)


## Options

The following sections summarize strategies that can be applied for bulk create and update operations

### Simple loop

- Individual requests sent on a single thread.
- Simplest and slowest method.
- Possible to encounter service protection limits using this approach.
- Currently the only recommended approach for code executed in a plug-in.

### Parallel Requests

- With .NET, Task Parallel library (TPL) facilitates sending requests in parallel using multiple threads.
- Aligns with Dataverse strengths to support multiple concurrent requests.
- This approach can be used together with other options and is essential to getting best total throughput possible.
- When the Azure affinity cookie is disabled, requests are sent to all available servers. Each server manages service protection limits independently, reducing likelihood of hitting service protection limits.
- `x-ms-dop-hint` response header value provides recommended degree of parallelism, which varies from environment to environment depending on resources allocated to it.
- Maximum number of threads depends on the number of CPU cores available on the client.
- Client may not have enough CPU cores for maximum throughput, or client default number of threads may send too many. Try to match the recommended degree of parallelism for best results.
- Number of concurrent requests is one of the facets of service protection limits. Typical limit is 52 concurrent requests.
- More information: [Send parallel requests](send-parallel-requests.md)

### ExecuteMultiple and $batch

- Both the Organization Service `ExecuteMultiple` message and Web API `$batch` operation allow you to send multiple data operation requests within a single request.
- These grouped requests can be any kind of request except another nested `ExecuteMultiple` or `$batch` request.
- These requests are performed sequentially in the order provided.
- You can send up to 1000 requests at a time. Depending on the number and nature of requests, the execution time for these requests is higher, which is a facet included in service protection limits. Sending the maximum number of requests doesn't translate into optimum performance.
- You can configure the request to stop if any errors occur, or continue and return the results of the errors for individual operations.
- You can send these requests in parallel.
- The primary performance benefit of using this approach is: Less total data is transferred over the wire in the body of the request compared to sending the requests individually.

   - Rather than looping through each request from the client, you're sending a list of requests to the server and asking the server to loop through them instead
   - The results of each operation don't need to be sent back to the client before the next operation can proceed.

- More information:

    - [Execute multiple requests using the Organization service](org-service/execute-multiple-requests.md)
    - [Execute batch operations using the Web API](webapi/execute-batch-operations-using-web-api.md)

### CreateMultiple and UpdateMultiple (Preview)

These specialized messages optimize performance when the same operation (`Create` or `Update`) is performed on a single table. These messages can provide substantial performance gains, but also a number of constraints you need to be aware of.

- More information:

   - [Bulk Operation messages (preview)](bulk-operations.md)
   - [Write plug-ins for CreateMultiple and UpdateMultiple (Preview)](write-plugin-multiple-operation.md)
   - [Bypass Custom Business Logic](bypass-custom-business-logic.md)

## Guidance

To optimize throughput for create and update operations, we recommend the following.

### Consider elastic tables

If your application doesn't depend on the data modeling and transactional capabilities standard tables provide, consider whether elastic tables would provide a better fit.

### Bulk Data load scenarios

- If you're performing `Create` or `Update` operations on large numbers of records for a single table, we recommend using the `CreateMultiple` and `UpdateMultiple` messages when they become available for the tables you're using. You need to experiment to find the optimum number of items to send in each request.
- You can enable a fall-back strategy to use `ExecuteMultiple` with continue-on-error enabled for any group of operations that fail. This way you can get the benefit of increased throughput most of the time, but still manage to complete the data load when a group of operations fail.
- If you're able, you should send these requests in parallel, with the Azure affinity cookie disabled to minimize the impact of service protection limits.

### Plug-ins

- For tables containing data that may need to be loaded in bulk, you should transfer any synchronous business logic from the individual `Create` and `Update` operation events to the `CreateMultiple` and `UpdateMultiple` events.
- Currently, we don't support `CreateMultiple` and `UpdateMultiple` operations for use in plug-ins. But when we do, and you have logic that creates or updates records of the same table, you can get some performance benefit by using `CreateMultiple` and `UpdateMultiple` rather than by looping through individual operations. We don't expect you'll initiate operations that create thousands of records in plug-ins. But if you're currently able to reliably create or update 10, 50, or 200 records in a loop, or by using `ExecuteMultiple`, you should see better performance by using `CreateMultiple` and `UpdateMultiple`.


### See also

[Bulk Operation messages (preview)](bulk-operations.md)   
[Send parallel requests](send-parallel-requests.md)   
[Write plug-ins for CreateMultiple and UpdateMultiple (Preview)](write-plugin-multiple-operation.md)   
[Elastic tables (Preview)](elastic-tables.md)