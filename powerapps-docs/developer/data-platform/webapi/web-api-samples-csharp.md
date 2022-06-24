---
title: "Web API  Data operations  Samples (C#) (Microsoft Dataverse)| Microsoft Docs"
description: "This topic provides a description of various Web API samples that are implemented using C#"
ms.date: 06/10/2022
author: divka78
ms.author: dikamath
ms.reviewer: jdaly
manager: sunilg
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
contributors: 
  - JimDaly
---
# Web API Data operations Samples (C#)

This topic provides information about the Web API samples implemented with C#. While each sample focuses on a different aspect of the Microsoft Dataverse Web API, they share similar characteristics and structure.

<a name="bkmk_prerequisites"></a>
   
## Prerequisites

The following is required to build and run the Dataverse Web API C# samples :  
  
- A version of Microsoft Visual Studio 2015 or later.  A free version, [Visual Studio Community](https://www.visualstudio.com/products/visual-studio-community-vs.aspx), is available for download [here](https://www.visualstudio.com/downloads/download-visual-studio-vs.aspx).  

- Access to Dataverse with an account that has the System Administrator security role.

> [!NOTE]
> These samples use version 5.2.9 of the deprecated [Microsoft.IdentityModel.Client.ActiveDirectory](/dotnet/api/microsoft.identitymodel.clients.activedirectory) authentication library. For an example using the recommended [Microsoft.Identity.Client](/dotnet/api/microsoft.identity.client), see [Enhanced quick start](enhanced-quick-start.md).
  
<a name="bkmk_webApiSamplesListing"></a>

## CDSWebApiService class library

These samples use the [CDSWebApiService class library (C#)](samples/cdswebapiservice.md) to provide re-usable common code that handles re-triable service protection limits. More information [Service protection API limits](../api-limits.md)

## Web API samples listing (C#)

The following table lists the samples implemented in C#.  Each sample is described in a more general manner in a corresponding sample group topic that focuses on the HTTP request and response messages, as detailed in the topic [Web API Samples](web-api-samples.md).  
  
|Sample|Sample Group|Description|  
|------------|------------------|-----------------|  
|[Web API Basic Operations Sample (C#)](samples/cdswebapiservice-basic-operations.md)|[Web API Basic Operations Sample](web-api-basic-operations-sample.md)|Demonstrates how to create, retrieve, update, delete, associate and disassociate Dataverse entity records.|  
|[Web API Query Data Sample (C#)](samples/cdswebapiservice-query-data.md)|[Web API Query Data Sample](web-api-query-data-sample.md)|Demonstrates how to use OData v4 query syntax and functions as well as Dataverse query functions. Includes examples of working with pre-defined queries and using FetchXML to perform queries.|  
|[Web API Conditional Operations Sample (C#)](samples/cdswebapiservice-conditional-operations.md)|[Web API Conditional Operations Sample](web-api-conditional-operations-sample.md)|Demonstrates how to perform conditional operations you specify with ETag criteria.|  
|[Web API Functions and Actions Sample (C#)](samples/functions-actions-csharp.md)|[Web API Functions and Actions Sample](web-api-functions-actions-sample.md)|Demonstrates how to use bound and unbound functions and actions, including custom actions.| 

The following samples demonstrate methods to add parallelism and concurrency to applications. These capabilities are an important part of maximizing throughput when performing operations that will add or update data within Dataverse.

- [Web API CDSWebApiService Parallel Operations Sample (C#)](samples/cdswebapiservice-parallel-operations.md)
- [Web API CDSWebApiService Async Parallel Operations Sample (C#)](samples/cdswebapiservice-async-parallel-operations.md)
  
<a name="bkmk_howDownloadRun"></a>

## How to download and run the samples
  
The source code for each sample is available on [GitHub](https://github.com/Microsoft/PowerApps-Samples/tree/master/cds/webapi/C%23). You can download the repository as a zip file which contains the solution files for the samples. For more information, see the **How to run this sample** section in each sample topic.  
  

### See also  

[Use the Dataverse Web API](overview.md)<br />
[Web API Samples](web-api-samples.md)<br />
[Web API Samples (Client-side JavaScript)](web-api-samples-client-side-javascript.md)<br />
[CDSWebApiService class library (C#)](samples/cdswebapiservice.md)<br />
[Web API Basic Operations Sample (C#)](samples/cdswebapiservice-basic-operations.md)<br />
[Web API Query Data Sample (C#)](samples/cdswebapiservice-query-data.md)<br />
[Web API Conditional Operations Sample (C#)](samples/cdswebapiservice-conditional-operations.md)<br />
[Web API Functions and Actions Sample (C#)](samples/functions-actions-csharp.md)


[!INCLUDE[footer-include](../../../includes/footer-banner.md)]