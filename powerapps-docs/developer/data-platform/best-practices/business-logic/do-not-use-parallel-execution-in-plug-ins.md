---
title: "Don't use parallel execution within plug-ins and workflow activities | MicrosoftDocs"
description: "Multi or parallel threading within plug-ins or custom workflow activities isn't supported."
ms.date: 06/20/2025
author: MsSQLGirl
ms.author: jukoesma
ms.reviewer: pehecke
ms.topic: article
ms.subservice: dataverse-developer
search.audienceType: 
  - developer
contributors:
 - JimDaly
 - phecke
---
# Don't use parallel execution within plug-ins and workflow activities

**Category**: Design, Performance, Security, Supportability

**Impact potential**: High

<a name='symptoms'></a>

## Symptoms

Multi-threading or parallel calls within plug-ins or custom workflow activities can cause corruption of those the connections. As an example, executing parallel threads can log exceptions such as:

`Generic SQL error.`
`The transaction active in this session has been committed or aborted by another session.`

Also, nonthread safe objects such as items in the [System.Collections Namespace](/dotnet/api/system.collections) can become corrupted by parallel threads.

<a name='guidance'></a>

## Guidance

The sandbox service is designed to execute calls in a specific order as part of a transaction. Developing plug-ins or custom workflow activities to make parallel or multi-threaded calls isn't supported. Develop your plug-ins and custom workflow activities knowing that the calls are performed sequentially and might need to be rolled back.

> [!NOTE]
> Using parallel execution from a client program is a supported practice to optimize performance as needed. This guidance is specific to code written to be executed within a plug-in or custom workflow activity.

<a name='problem'></a>

## Problematic patterns

Plug-ins and custom workflow activities run within a single transaction and multiple threads introduced by parallel execution can corrupt the transaction. The following are examples of patterns and practices that shouldn't be used within plug-ins and custom workflow activities:

- Using [Task-based asynchronous pattern (TAP)](/dotnet/standard/asynchronous-programming-patterns/task-based-asynchronous-pattern-tap)
- Using [Task Parallel Library (TPL)](/dotnet/standard/parallel-programming/task-parallel-library-tpl)
- Using [Managed Threading](/dotnet/standard/threading/index)


<a name='additional'></a>

## Additional information

Using and updating shared pipeline context objects could cause these objects to contain unexpected results or become corrupted. The affect of this would be a failure in the plug-in or custom workflow activity. 

<a name='seealso'></a>

### See also

[Parallel Processing, Concurrency, and Async Programming in .NET](/dotnet/standard/parallel-processing-and-concurrency)<br />

[!INCLUDE[footer-include](../../../../includes/footer-banner.md)]
