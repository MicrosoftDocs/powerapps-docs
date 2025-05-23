---
title: "Sample: Task Parallel Library with CrmServiceClient (Microsoft Dataverse)| Microsoft Docs"
description: "Task Parallel Library (TPL) makes developers more productive by simplifying the process of adding parallelism and concurrency to applications. This sample demonstrates using this with CrmServiceClient"
ms.date: 01/31/2023
author: MattB-msft
ms.author: mbarbour
ms.reviewer: pehecke
ms.topic: sample
applies_to:
  - "Dynamics 365 (online)"
search.audienceType:
  - developer
contributors:
  - JimDaly
  - phecke
---

# Sample: Task Parallel Library with CrmServiceClient

[!INCLUDE[cc-terminology](../includes/cc-terminology.md)]

This C# .NET sample shows how to use the <xref:Microsoft.Xrm.Tooling.Connector.CrmServiceClient> class with the Task Parallel Library (TPL).

> [!NOTE]
> You could also use the <xref:Microsoft.PowerPlatform.Dataverse.Client.ServiceClient> instead of the <xref:Microsoft.Xrm.Tooling.Connector.CrmServiceClient> class in this sample.

The Task Parallel Library enables developers to be more productive by simplifying the process of adding parallelism and concurrency to applications. Adding parallelism and concurrency can significantly improve the total throughput for applications that need to perform a large number of Dataverse operations in a short period of time.

## Requirements

- Visual Studio 2019 or later
- Dataverse test environment and valid user logon credentials

## How to run the sample

1. Clone the [PowerApps-Samples](https://github.com/microsoft/PowerApps-Samples) repository so that you have a copy locally.
2. Open the `dataverse\Xrm Tooling\TPLCrmServiceClient\TPLCrmServiceClient.sln` file in Visual Studio.
3. Press **F5** to compile and run the program.

## Demonstrates

Because the <xref:Microsoft.Xrm.Tooling.Connector.CrmServiceClient> class includes handling for the transient errors thrown by the Dataverse service protection limits, the combination of TPL and `CrmServiceClient` is valuable to create applications that can optimize throughput while being resilient to the service protection limit errors by re-trying requests that are rejected due to these limits. The <xref:Microsoft.Xrm.Tooling.Connector.CrmServiceClient.Clone?displayProperty=nameWithType> method enables TPL to use the client with multiple threads.

More information: [Service Protection API Limits](../api-limits.md)

> [!NOTE]
> You could also use the <xref:Microsoft.PowerPlatform.Dataverse.Client.ServiceClient.Clone%2A?displayProperty=nameWithType> method in this sample code instead of <xref:Microsoft.Xrm.Tooling.Connector.CrmServiceClient.Clone?displayProperty=nameWithType> with the same results.

This sample will generate a number of account table rows using the <xref:System.Threading.Tasks.Parallel.ForEach%2A?displayProperty=nameWithType> method, then it will use that technique again to delete the tables created. By default, this sample will create only 10 rows, which is not enough to hit the service protection API limit errors. If you raise the `numberOfRecords` variable value to 10000, you can use Fiddler to observe how some of the requests will be rejected and re-tried.

### See also

[Task Parallel Library (TPL)](/dotnet/standard/parallel-programming/task-parallel-library-tpl)

[!INCLUDE[footer-include](../../../includes/footer-banner.md)]
