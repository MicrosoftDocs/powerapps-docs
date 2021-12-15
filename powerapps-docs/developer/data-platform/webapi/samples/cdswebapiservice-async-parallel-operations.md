---
title: "Web API CDSWebApiService Async Parallel Operations Sample (C#) (Microsoft Dataverse)| Microsoft Docs"
description: "This sample demonstrates using Task Parallel Library (TPL) dataflow components with asynchronous requests."
ms.custom: ""
ms.date: 07/15/2021
ms.service: powerapps
applies_to: 
  - "Dynamics 365 (online)"
author: "JimDaly"
ms.author: "pehecke"
ms.reviewer: "pehecke"
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---

# Web API CDSWebApiService Async Parallel Operations Sample (C#)

[!INCLUDE[cc-terminology](../../includes/cc-terminology.md)]

This sample demonstrates using Task Parallel Library (TPL) dataflow components [Dataflow (Task Parallel Library)](/dotnet/standard/parallel-programming/dataflow-task-parallel-library) with asynchronous requests.

TPL provides capabilities to add parallelism and concurrency to applications. These capabilities are an important part of maximizing throughput when performing operations that will add or update data within Dataverse.

This sample uses the CDSWebApiService class asynchronous methods within asynchronous operations. Because the CDSWebApiService class can manage Service Protection API limits, this code can be resilient to the transient 429 errors that clients should expect. It will retry a configurable number of times. More information: [Service Protection API Limits](../../api-limits.md)

This sample simply creates a configurable number of account rows (records) to create, which it will in turn delete. This sample uses dataflow components to process the rows and transform the results of the create operation into the next phase that deletes these rows. Because of the nature of this data flow, delete operations for previously created rows will start before all the rows to create are finished.

## Prerequisites

The following is required to build and run the CDSWebApiService C# samples :

- Microsoft Visual Studio 2019. 
- Access to Microsoft Dataverse with privileges to perform CRUD operations.
  
<a name="bkmk_runSample"></a>
  
## How to run this sample

1. Go to the [PowerApps-Samples](https://github.com/microsoft/PowerApps-Samples) GitHub repository, clone or download the samples repository, and extract its contents into a local folder.

1. Navigate to the repository folder cds/webapi/C#/AsyncParallelOperations, and then open the AsyncParallelOperations.sln file in Visual Studio.

1. In **Solution Explorer**, under the **AsyncParallelOperations** project, open the App.config file. This is a shared application configuration file used by all the Web API C# samples. Once you edit this file, you do not have to edit it again unless you're changing the environment or logon used to run the samples.

1. You must edit the `Url`, `UserPrincipalName`, and `Password` values to set the Dataverse instance and credentials you want to connect to.

    ```xml
        <add name="Connect"
            connectionString="Url=https://yourorg.api.crm.dynamics.com;
            Authority=null;
            ClientId=51f81489-12ee-4a9e-aaae-a2591f45987d;
            RedirectUrl=app://58145B91-0C36-4500-8554-080854F2AC97;
            UserPrincipalName=you@yourorg.onmicrosoft.com;
            Password=y0urp455w0rd;
            CallerObjectId=null;
            Version=9.1;
            MaxRetries=3;
            TimeoutInSeconds=180;
            "/>
    ```

1. Make sure that the **AsyncParallelOperations** project is set as the startup project. The name of the project should be bold to indicate it is the startup project. If the name is not bold, right-click it in the solution explorer and select **Set as Startup Project**.

1. Press F5 to run the program in debug mode.

## Code listing

This sample depends on the assembly included in the CDSWebAPIService project. For information on the methods this class provides see: [Web API CDSWebApiService class Sample (C#)](cdswebapiservice.md).

The following is the code from the Program.cs file:

```csharp
using Newtonsoft.Json.Linq;
using System;
using System.Collections.Generic;
using System.Configuration;
using System.Threading.Tasks;
using System.Threading.Tasks.Dataflow;

namespace PowerApps.Samples
{
    internal class Program
    {
        //Get configuration data from App.config connectionStrings
        private static readonly string connectionString = ConfigurationManager.ConnectionStrings["Connect"].ConnectionString;

        private static readonly ServiceConfig serviceConfig = new ServiceConfig(connectionString);

        //Controls the max degree of parallelism
        private static readonly int maxDegreeOfParallelism = 10;

        //How many records to create with this sample.
        private static readonly int numberOfRecords = 100;

        private static async Task Main()
        {
            #region Optimize Connection

            //Change max connections from .NET to a remote service default: 2
            System.Net.ServicePointManager.DefaultConnectionLimit = 65000;
            //Bump up the min threads reserved for this app to ramp connections faster - minWorkerThreads defaults to 4, minIOCP defaults to 4
            System.Threading.ThreadPool.SetMinThreads(100, 100);
            //Turn off the Expect 100 to continue message - 'true' will cause the caller to wait until it round-trip confirms a connection to the server
            System.Net.ServicePointManager.Expect100Continue = false;
            //Can decrease overall transmission overhead but can cause delay in data packet arrival
            System.Net.ServicePointManager.UseNagleAlgorithm = false;

            #endregion Optimize Connection

            var executionDataflowBlockOptions = new ExecutionDataflowBlockOptions
            {
                MaxDegreeOfParallelism = maxDegreeOfParallelism
            };

            var count = 0;
            double secondsToComplete;

            //Will be populated with account records to import
            List<JObject> accountsToImport = new List<JObject>();

            Console.WriteLine($"Preparing to create {numberOfRecords} acccount records using Web API.");

            //Add account records to the list to import
            while (count < numberOfRecords)
            {
                var account = new JObject
                {
                    ["name"] = $"Account {count}"
                };
                accountsToImport.Add(account);
                count++;
            }

            using (var svc = new CDSWebApiService(serviceConfig))
            {
                secondsToComplete = await ProcessData(svc, accountsToImport, executionDataflowBlockOptions);
            }

            Console.WriteLine($"Created and deleted {accountsToImport.Count} accounts in  {Math.Round(secondsToComplete)} seconds.");

            Console.WriteLine("Sample completed. Press any key to exit.");
            Console.ReadLine();
        }

        private static async Task<double> ProcessData(CDSWebApiService svc, List<JObject> accountsToImport,
            ExecutionDataflowBlockOptions executionDataflowBlockOptions)
        {
            var createAccounts = new TransformBlock<JObject, Uri>(
                async a =>
                {
                    return await svc.PostCreateAsync("accounts", a);
                },
                    executionDataflowBlockOptions
                );

            var deleteAccounts = new ActionBlock<Uri>(
                async u =>
                {
                    await svc.DeleteAsync(u);
                },
                executionDataflowBlockOptions
              );

            createAccounts.LinkTo(deleteAccounts, new DataflowLinkOptions { PropagateCompletion = true });

            var start = DateTime.Now;

            accountsToImport.ForEach(a => createAccounts.SendAsync(a));
            createAccounts.Complete();
            await deleteAccounts.Completion;

            //Calculate the duration to complete
            return (DateTime.Now - start).TotalSeconds;
        }
    }
}
```

### See also

[Use the Dataverse Web API](../overview.md)<br />
[Web API CDSWebApiService class Sample (C#)](cdswebapiservice.md)<br />
[Web API CDSWebApiService Basic Operations Sample (C#)](cdswebapiservice-basic-operations.md)<br />
[Web API CDSWebApiService Parallel Operations Sample (C#)](cdswebapiservice-parallel-operations.md)<br />
[Create a table using the Web API](../create-entity-web-api.md)<br />
[Update and delete table rows using the Web API](../update-delete-entities-using-web-api.md)

[!INCLUDE[footer-include](../../../../includes/footer-banner.md)]
