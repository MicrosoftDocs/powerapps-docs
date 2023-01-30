---
title: "Web API  Data operations  Samples (C#) (Microsoft Dataverse)| Microsoft Docs"
description: "This topic provides a description of various Web API samples that are implemented using C#"
ms.date: 09/03/2022
author: divkamath
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

# Web API Data operations Samples (C#)

This topic provides information about the Web API samples implemented with C# using .NET 6.0. While each sample focuses on a different aspect of the Microsoft Dataverse Web API, they share similar characteristics and structure.

<a name="bkmk_prerequisites"></a>

## Prerequisites

The following is required to build and run the Dataverse Web API C# samples :

- A version of Microsoft Visual Studio 2022 or later. A free version, [Visual Studio Community](https://visualstudio.microsoft.com/vs/community/), is available for download [here](https://visualstudio.microsoft.com/downloads/).

- Access to Dataverse with an account that has the System Administrator security role.

## WebApiService class library

These samples use the [WebAPIService class library (C#)](samples/webapiservice.md) to provide re-usable common code that handles re-triable service protection limit errors. More information: [Service protection API limits](../api-limits.md)

<a name="bkmk_webApiSamplesListing"></a>

## Web API samples listing (C#)

The following table lists the samples implemented in C#. Each sample is described in a more general manner in a corresponding sample group topic that focuses on the HTTP request and response messages, as detailed in the topic [Web API Samples](web-api-samples.md).

|Sample|Sample Group|Description|
|------|-----------|------------|
|[Web API Basic Operations Sample (C#)](samples/webapiservice-basic-operations.md)| [Web API Basic Operations Sample](web-api-basic-operations-sample.md)|Demonstrates how to create, retrieve, update, delete, associate and disassociate Dataverse entity records.|
|[Web API Query Data sample (C#)](samples/webapiservice-query-data.md)| [Web API Query Data Sample](web-api-query-data-sample.md)| Demonstrates how to use OData v4 query syntax and functions as well as Dataverse query functions. Includes examples of working with pre-defined queries and using FetchXML to perform queries. |
|[Web API Conditional Operations sample (C#)](samples/webapiservice-conditional-operations.md)| [Web API Conditional Operations Sample](web-api-conditional-operations-sample.md) | Demonstrates how to perform conditional operations you specify with ETag criteria.|
|[Web API Functions and Actions Sample (C#)](samples/webapiservice-functions-and-actions.md)|[Web API Functions and Actions Sample](web-api-functions-actions-sample.md)| Demonstrates how to use bound and unbound functions and actions, including custom actions.|
|[Web API Metadata Operations Sample (C#)](samples/webapiservice-metadata-operations.md)|[Web API Metadata Operations Sample](web-api-metadata-operations-sample.md)|Demonstrates how to perform selected operations that modify the Dataverse schema, or metadata.|

The following samples demonstrate methods to add parallelism and concurrency to applications. These capabilities are an important part of maximizing throughput when performing operations that will add or update data within Dataverse.

- [Web API WebApiService Parallel Operations Sample (C#)](samples/webapiservice-parallel-operations.md)
- [Web API Parallel Operations with TPL Dataflow components Sample (C#)](samples/webapiservice-tpl-dataflow-parallel-operations.md)

<a name="bkmk_howDownloadRun"></a>

## How to download and run the samples

The source code for each sample is available on GitHub at: [PowerApps-Samples/dataverse/webapi/C#-NETx/](https://github.com/microsoft/PowerApps-Samples/tree/master/dataverse/webapi/C%23-NETx). You can download the repository as a zip file which contains the solution files for the samples. For more information, see the **How to run this sample** section in each sample topic.

### See also

[Use the Dataverse Web API](overview.md)<br />
[Web API Samples](web-api-samples.md)<br />
[Web API Samples (Client-side JavaScript)](web-api-samples-client-side-javascript.md)<br />
[WebAPIService class library (C#)](samples/webapiservice.md)<br />

[!INCLUDE[footer-include](../../../includes/footer-banner.md)]
