---
title: "Do not use parallel execution within plug-ins and workflow activities | MicrosoftDocs"
description: "Multi or parallel threading within plug-ins or custom workflow activities is not supported."
services: ''
suite: powerapps
documentationcenter: na
author: JimDaly
manager: ryjones
editor: ''
tags: ''
ms.service: powerapps
ms.devlang: na
ms.topic: article
ms.tgt_pltfrm: na
ms.workload: na
ms.date:  08/14/2019
ms.subservice: dataverse-developer
ms.author: pehecke
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---
# Do not use parallel execution within plug-ins and workflow activities

[!INCLUDE[cc-data-platform-banner](../../../../includes/cc-data-platform-banner.md)]

**Category**: Design, Performance, Security, Supportability

**Impact potential**: High

<a name='symptoms'></a>

## Symptoms

Multi-threading or parallel calls within plug-ins or custom workflow activities can cause corruption of those the connections.  As an example, executing parallel threads can log exceptions such as:

`Generic SQL error.`
`The transaction active in this session has been committed or aborted by another session.`

Also, non-thread safe objects such as items in the [System.Collections Namespace](/dotnet/api/system.collections) can become corrupted by parallel threads.

<a name='guidance'></a>

## Guidance

The sandbox service has been designed to execute calls in a specific order as part of a transaction.  Developing plug-ins or custom workflow activities to make parallel or multi-threaded calls is not supported.  Develop your plug-ins and custom workflow activities knowing that the calls will be performed sequentially and may need to be rolled back.

> [!NOTE]
> Using parallel execution from a client program is a supported practice to optimize performance as needed. This guidance is specific to code written to be executed within a plug-in or custom workflow activity.

<a name='problem'></a>

## Problematic patterns

Plug-ins and custom workflow activities run within a single transaction and multiple threads introduced by parallel execution can corrupt the transaction. The following are examples of patterns and practices that should not be used within plug-ins and custom workflow activities:

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