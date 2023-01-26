---
title: "Web API WebApiService Parallel Operations Sample (C#) (Microsoft Dataverse)| Microsoft Docs"
description: "This sample demonstrates sending requests in parallel using the .NET Task Parallel Library (TPL)."
ms.date: 09/02/2022
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

# Web API WebApiService Parallel Operations Sample (C#)

[!INCLUDE[cc-terminology](../../includes/cc-terminology.md)]

This .NET 6.0 sample demonstrates how to perform parallel data operations using the Dataverse Web API.

This sample uses the common helper code in the [WebAPIService class library (C#)](webapiservice.md).

## Prerequisites

The following is required to build and run this sample:

- Microsoft Visual Studio 2022.
- Access to Dataverse with privileges to perform data operations.
  
<a name="bkmk_runSample"></a>
  
## How to run this sample

1. Clone or download the [PowerApps-Samples](https://github.com/microsoft/PowerApps-Samples) repository.
1. Locate the [/dataverse/webapi/C#-NETx/ParallelOperations/](https://github.com/microsoft/PowerApps-Samples/tree/master/dataverse/webapi/C%23-NETx/ParallelOperations) folder.
1. Open the `ParallelOperations.sln` file using Visual Studio 2022
1. Edit the `appsettings.json` file to set the following property values:

   |Property|Instructions  |
   |---------|---------|
   |`Url`|The Url for your environment. Replace the placeholder `https://yourorg.api.crm.dynamics.com` value with the value for your environment. See [View developer resources](../../view-download-developer-resources.md) to find this. |
   |`UserPrincipalName`|Replace the placeholder `you@yourorg.onmicrosoft.com` value with the UPN value you use to access the environment.|
   |`Password`|Replace the placeholder `yourPassword` value with the password you use.|

1. Save the `appsettings.json` file
1. Press F5 to run the sample.

## Code

The code for this sample is here: [PowerApps-Samples/dataverse/webapi/C#-NETx/ParallelOperations/Program.cs](https://github.com/microsoft/PowerApps-Samples/blob/master/dataverse/webapi/C%23-NETx/ParallelOperations/Program.cs)

## Demonstrates

This sample includes settings you can apply to optimize your connection.

This sample first sends a request simply to access the value of the `x-ms-dop-hint` response header to determine the recommended degrees of parallelism for this environment. When the maximum degree of parallelism is set equal to the value of the `x-ms-dop-hint` response header you should achieve a steady state where throughput is optimized with a minimum of `429 TooManyRequests` service protection limit errors returned.

To encounter service protection limits with this sample you should raise the `numberOfRecords` variable to over 10,000 or whatever is needed for the sample to run for more than 5 minutes. You should also change the code to set the `maxDegreeOfParallelism` to be significantly greater than `x-ms-dop-hint` response header value. Then, using Fiddler you should be able to observe how WebAPIService retries the requests that return this error.

This example uses the [Parallel.ForEachAsync Method](/dotnet/api/system.threading.tasks.parallel.foreachasync) introduced with .NET 6.0.

This sample processes a list of requests to create account records, sending the requests in parallel and then uses the data returned to add requests to delete the created accounts to a [ConcurrentBag](/dotnet/api/system.collections.concurrent.concurrentbag-1?view=net-6.0&preserve-view=true). After the records are created, the number of seconds to create the records is displayed.

Then, the delete requests in the `ConcurrentBag` are processed and the time spent deleting the records is displayed.

You may want to compare this sample to the [Web API Parallel Operations with TPL Dataflow components Sample (C#)](webapiservice-tpl-dataflow-parallel-operations.md).

## Clean up

By default this sample will delete all the records created in it. If you want to view created records after the sample is completed, change the `deleteCreatedRecords` variable to `false` and you will be prompted to decide if you want to delete the records.

### See also

[Use the Dataverse Web API](../overview.md)<br />
[WebAPIService class library (C#)](webapiservice.md)<br />
[Create a table row using the Web API](../create-entity-web-api.md)<br />
[Update and delete table rows using the Web API](../update-delete-entities-using-web-api.md)<br />
[Service protection API limits](../../api-limits.md)<br />
[Web API Samples](../web-api-samples.md)<br />
[Web API Basic Operations Sample (C#)](webapiservice-basic-operations.md)<br />
[Web API Query Data sample (C#)](webapiservice-query-data.md)<br />
[Web API Conditional Operations sample (C#)](webapiservice-conditional-operations.md)<br />
[Web API Functions and Actions Sample (C#)](webapiservice-functions-and-actions.md)<br />
[Web API Metadata Operations Sample (C#)](webapiservice-metadata-operations.md)<br />
[Web API Parallel Operations with TPL Dataflow components Sample (C#)](webapiservice-tpl-dataflow-parallel-operations.md)<br />

[!INCLUDE[footer-include](../../../../includes/footer-banner.md)]
