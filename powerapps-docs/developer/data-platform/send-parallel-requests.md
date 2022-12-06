---
title: "Send parallel requests (Dataverse)| Microsoft Docs"
description: "When your application needs to send a large number of requests to Dataverse you can achieve much higher total throughput by sending requests in parallel using multiple threads."
ms.date: 12/12/2022
author: divka78
ms.author: dikamath
ms.reviewer: jdaly
ms.topic: get-started-article
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
contributors: 
  - JimDaly
  - phecke
---

# Send parallel requests

When your application needs to send a large number of requests to Dataverse you can achieve much higher total throughput by sending requests in parallel using multiple threads. Dataverse is designed to support multiple concurrent users, so sending requests in parallel leverages this strength.

> [!NOTE]
> In plug-ins, sending parallel requests is not supported. More information: [Do not use parallel execution within plug-ins and workflow activities](best-practices/business-logic/do-not-use-parallel-execution-in-plug-ins.md)

## Optimize your connection

When you are sending requests in parallel, you can apply the following configuration changes so your requests are not limited:

```csharp
// Change max connections from .NET to a remote service default: 2
System.Net.ServicePointManager.DefaultConnectionLimit = 65000;
// Bump up the min threads reserved for this app to ramp connections faster - minWorkerThreads defaults to 4, minIOCP defaults to 4 
ThreadPool.SetMinThreads(100, 100);
// Turn off the Expect 100 to continue message - 'true' will cause the caller to wait until it round-trip confirms a connection to the server 
System.Net.ServicePointManager.Expect100Continue = false;
// Can decrease overall transmission overhead but can cause delay in data packet arrival
System.Net.ServicePointManager.UseNagleAlgorithm = false;
```

More information:
- <xref:System.Net.ServicePointManager.DefaultConnectionLimit?displayProperty=fullName>
- <xref:System.Threading.ThreadPool.SetMinThreads%2A?displayProperty=fullName>
- <xref:System.Net.ServicePointManager.Expect100Continue?displayProperty=fullName>
- <xref:System.Net.ServicePointManager.UseNagleAlgorithm?displayProperty=fullName>

## Optimum degree of parallelism (DOP)

Part of the service that Dataverse provides is managing resource allocation for environments. Production environments that are heavily used by many licenced users will have more resources allocated to them. The number and capabilities of the servers allocatied may vary over time, so there is no fixed number that you should apply to get the optimum degree of parallelism. However, the `x-ms-dop-hint` response header returns an integer value between 1 and 1024 that should provide good results for a given environment.

## Dataverse SDK for .NET

With the Dataverse SDK for .NET, the [Clone](xref:Microsoft.PowerPlatform.Dataverse.Client.ServiceClient.Clone%2A) method available in both [ServiceClient](xref:Microsoft.PowerPlatform.Dataverse.Client.ServiceClient) and [CrmServiceClient](xref:Microsoft.Xrm.Tooling.Connector.CrmServiceClient) allows duplicating an existing connection to Dataverse so that you can leverage the [Task Parallel Library (TPL)](/dotnet/standard/parallel-programming/task-parallel-library-tpl) which simplifies the process of adding parallelism and concurrency to applications.

The `x-ms-dop-hint` response value is available via the [RecommendedDegreesOfParallelism](xref:Microsoft.PowerPlatform.Dataverse.Client.ServiceClient.RecommendedDegreesOfParallelism) property in either `ServiceClient` or  `CrmServiceClient`. You should use this value when setting <xref:System.Threading.Tasks.ParallelOptions.MaxDegreeOfParallelism?displayProperty=fullName> when you use <xref:System.Threading.Tasks.Parallel.ForEach%2A?displayProperty=fullName>.

### Web API

With the Web API, you 