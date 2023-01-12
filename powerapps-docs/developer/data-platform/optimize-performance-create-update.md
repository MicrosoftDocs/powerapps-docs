---
title: Optimize performance for Create and Update operations | Microsoft Docs
description: Choose the best approach when creating or updating large numbers records.
author: divkamath
ms.topic: article
ms.date: 12/12/2022
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

When your application works with large numbers of records you must consider how to achieve the best possible performance. Dataverse offers several options you can use to maximize total throughput when performing create and update operations with large numbers of records. Learn about the available options and choose the one that is the best for your application.

This topic introduces two new messages: `CreateMultiple` and `UpdateMultiple`. At this time, these messages are only available for custom tables which have been created recently or for tables used by Microsoft products, such as Dynamics 365 Project Operations. These operations are currently only available when using the Dataverse SDK for .NET. In the coming months we are deploying changes that will make these messages available to all tables that support create or update operations and enable using them with the Dataverse Web API. More information: [Use CreateMultiple and UpdateMultiple (Preview)](org-service/use-createmultiple-updatemultiple.md)

## Scenarios

Performance is important for all applications, but it is critical for certain scenarios. In this topic we will look at bulk data load and plug-ins.

### Bulk data operations

When you must create or update large numbers of records in a limited amount of time, the choice you make as a developer can save hours of time to complete a task. Applications that perform operations in bulk typically make the most extreme requests for shared resources and will encounter [Service protection API limits](api-limits.md). This topic will provide options you may use to achieve maximum throughput for the level of resources allocated to your Dataverse environment.

A key point to appreciate in this scenario is that your code runs in a client application making individual calls to Dataverse APIs and you manage any errors that occur. The situation is different with plug-ins.

### Plug-ins

Plug-ins provide the ability to extend the behavior of existing Dataverse messages on the server or to implement the operations to support a custom action. All plug-ins are triggered by requests that originate from external calls to Dataverse APIs.

Plug-in run in a sandbox, which is a virtual computer isolated from the Dataverse server. Your plug-in code is a client application that is invoked by Dataverse whenever an API call to Dataverse requires the logic your plug-in contains. When registered as part of a synchronous step, the time to perform the plug-in logic contributes to the total time of the operation it extends or implements. Plug-ins can have a significant impact on the total performance of any Dataverse API used by a client application.  

When the synchronous step is part of the transaction, any error that occurs in your plug-in code MUST force the entire operation to roll back in order to maintain data integrity.

Because of the way plug-ins run, there are the following constraints.

- There is a 2 minute time limit for plug-ins to execute. This is extremely generous considering the impact that a plug-in can have on the performance of an application. Most synchronous plug-ins should complete in less than 2 seconds.
- You should not use `ExecuteMultiple` or `ExecuteTransaction` operations within plug-ins. These are only intended to be used by client applications and they disrupt the transaction behavior required for plug-ins. More information: [Do not use batch request types in plug-ins and workflow activities](best-practices/business-logic/avoid-batch-requests-plugin.md)
- You should not try to use techniques that involve performing operations in parallel. You must develop your plug-ins knowing that the calls will be performed sequentially and may need to be rolled back. More information: [Do not use parallel execution within plug-ins and workflow activities](best-practices/business-logic/do-not-use-parallel-execution-in-plug-ins.md)

> [!NOTE]
> At this time, we do not support using `CreateMultiple` and `UpdateMultiple` calls within plug-ins, but we plan to support this in the coming months.


## Other Options

There are other options that you can use separately or together with `CreateMultiple` or `UpdateMultiple' to optimize performance.

### ExecuteMultiple

ExecuteMultiple was introduced to address performance issues caused by network latentcy. By bundling multiple requests together in a single request, the total size of the payload is reduced and performance is improved compared to sending individiual operations over the internet.

All the requests are sent as a group and are then processed sequentially on the server. If an error occurs, the request can be configured to continue and return information about the requests that failed. The number of requests that can be included is limited to 1000.

The requests can be any type of request except `ExecuteMultiple`. However, you can send requests for `CreateMultiple` and `UpdateMultiple` with `ExecuteMultiple`.

### ExecuteTransaction

ExecuteTransaction also provides the ability to send a set of requests as a group, but in this case, all the requests will be included in a single transaction that must all succeed together or they will all fail together.

### Web API $batch

### Sending requests in parallel

[Send parallel requests](send-parallel-requests.md)

## Frequently Asked Questions




### See also

[Send parallel requests](send-parallel-requests.md)