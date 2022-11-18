---
title: Optimize performance for Create and Update operations | Microsoft Docs
description: Choose the best approach when creating or updating large numbers records.
author: divka78
ms.topic: article
ms.date: 11/28/2022
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

This topic introduces two new messages: `CreateMultiple` and `UpdateMultiple`. At this time, these messages are only available for custom tables which have been created recently or for tables used by Microsoft products, such as Dynamics 365 Project Operations. These operations are currently only available when using the Dataverse SDK for .NET. In the coming months we are deploying changes that will make these messages available to all tables that support create or update operations and enable using them with the Dataverse Web API. More information: [CreateMultiple and UpdateMultiple](#createmultiple-and-updatemultiple)

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

- There is a 2 minute time limit for plug-ins to execute. This is extremely generous considering the impact that a plug-in can have on the performance of an application. Most synchronous plug-ins should aim to complete in less than 2 seconds.
- You should not use `ExecuteMultiple` or `ExecuteTransaction` operations within plug-ins. These are only intended to be used by client applications and they disrupt the transaction behavior required for plug-ins. More information: [Do not use batch request types in plug-ins and workflow activities](best-practices/business-logic/avoid-batch-requests-plugin.md)
- You should not try to use techniques that involve performing operations in parallel. You must develop your plug-ins knowing that the calls will be performed sequentially and may need to be rolled back. More information: [Do not use parallel execution within plug-ins and workflow activities](best-practices/business-logic/do-not-use-parallel-execution-in-plug-ins.md)

> [!NOTE]
> At this time, we do not support using `CreateMultiple` and `UpdateMultiple` calls within plug-ins, but we plan to support this in the coming months.


## CreateMultiple and UpdateMultiple

Use `CreateMultiple` and `UpdateMultiple` to perform create or update operations on a collection of records of the same type. These messages are more efficient because:

 - Changes to all records are applied to the database in a single operation rather than as individual row inserts or updates.
 - Plug-ins for these messages need only be invoked once to apply logic to all the records in this operation.

`CreateMultiple` and `UpdateMultiple` are exactly like `Create` and `Update`, except that they accept a collection of entities in the `Targets` parameter rather than a single one in the `Target` parameter. In other words, if you pass a collection with one item to `CreateMultiple`, it is exactly like `Create`. With a single item in the collection, there is no performance benefit and all the same custom logic expected for `Create` will occur with `CreateMultiple`. The same is true for `Update` and `UpdateMultiple`.

The performance benefit comes as you add more items to the collection parameter. The larger the number of items in the `Targets` collection, the greater the efficiency that can be achieved. So, these messages are the best choice if you need to perform operations on large numbers of record. But there are limits. See [Limitations](#limitations).

If you are a plug-in developer, you may be thinking *"Does this mean I must maintain the same business logic in plug-ins for two different messages?"*. The answer is *No*. The reason is that the message processing for the multiple version of these operations is merged with the single version.

The plug-in steps for `Create` will be applied to every entity passed in the `Targets` collection to `CreateMultiple`, and the same is true for `Update` and `UpdateMultiple`. Also, when any plug-ins are registered for `CreateMultiple` steps, they will also be applied to `Create`, and the same is true for `UpdateMultiple` and `Update`.

This means that you are not required to manage your business logic for the the operations in two different places. Your logic on the single versions of these messages will continue to work when client applications use the multiple version of the operation. This is different from how `Retrieve` and `RetrieveMultiple` work. `Retrieve` and `RetrieveMultiple` will continue to be separate for backward compatibility.

However, to achieve optimum efficiency and performance, you should consider migrating any logic in plug-ins for `Create` or `Update` to `CreateMultiple` and `UpdateMultiple`. More information: [Write plug-ins for CreateMultiple and UpdateMultiple](write-plugin-multiple-operation.md)

### Limitations

This section explains the limitations for `CreateMultiple` and `UpdateMuliple` operations.

#### Not currently available in Web API

Today you can only use the Dataverse SDK for .NET [CreateMultipleRequest](xref:Microsoft.Xrm.Sdk.Messages.CreateMultipleRequest) and [UpdateMultipleRequest](xref:Microsoft.Xrm.Sdk.Messages.UpdateMultipleRequest) classes with the [IOrganizationService.Execute](xref:Microsoft.Xrm.Sdk.IOrganizationService.Execute%2A) method.

We are working to enable this for Web API as well and expect to release this in the coming months.

#### No continue on error behavior

Unlike the `ExecuteMultiple` message, there is no capabilty to continue processing if an error occurs in any of the respective operations using `CreateMultiple` or `UpdateMultiple`. When an error occurs, the entire request will be rolled back. In a plug-in, this means that the entire operation will roll back. With a client performing bulk operations, there are strategies you can apply to manage this. More information: [Managing errors](#managing-errors).

#### Number of entities to send in each request is limited

Because the efficiency per operation increases with the number of entities passed to the `Targets` parameter for `CreateMultiple` and `UpdateMultiple`, there is reason to try and send the largest posssible number of entities in each request. There is no set limit to the number of entities you can send, but if you send too many you can encounter an [OutOfMemoryException](xref:System.OutOfMemoryException). As a general rule, we don't recommend sending more than 1000 entities in a single request. You may need to send less.

Contributing factors to encountering an `OutOfMemoryException` are:

- The amount of data included in each entity, that is, the number of columns that have values and the kind of data included.
- Whether plug-in steps include entity images. An entity image is a 'snapshot' or copy of the record being processed with values that can be referenced by a plug-in rather than retrieved from the database. The data in any entity images requires data that can increase the likelihood of an `OutOfMemoryException`.

### Managing errors

### Guidelines for using CreateMultiple and UpdateMultiple

## Other Options

There are other options that you can use separately or together with `CreateMultiple` or `UpdateMultiple' to optimize performance.

### ExecuteMultiple

ExecuteMultiple was introduced to address performance issues caused by network latentcy. By bundling multiple requests together in a single request, the total size of the payload is reduced and performance is improved compared to sending individiual operations over the internet.

All the requests are sent as a group and are then processed sequentially on the server. If an error occurs, the request can be configured to continue and return information about the requests that failed. The number of requests that can be included is limited to 1000.

The requests can be any type of request except `ExecuteMultiple`. However, you can send requests for `CreateMultiple` and `UpdateMultiple` with `ExecuteMultiple`.

### ExecuteTransaction

ExecuteTransaction also provides the ability to send a set of requests as a group, but in this case, all the requests will be included in a single transaction that must all succeed together or they will all fail together.

### Web API $batch

### Sending requests in Parallel

## Frequently Asked Questions

### Will there be an UpsertMultiple?

### Will there be a DeleteMultiple?

### Why isn't the logic for Retrieve and RetrieveMultiple merged?




