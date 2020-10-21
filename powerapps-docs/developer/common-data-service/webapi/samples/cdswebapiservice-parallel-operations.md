---
title: "Web API CDSWebApiService  Parallel Operations Sample (C#) (Common Data Service)| Microsoft Docs"
description: "This sample demonstrates using Task Parallel Library (TPL) with synchronous requests."
ms.custom: ""
ms.date: 04/20/2020
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
# Web API CDSWebApiService Parallel Operations Sample (C#)

[!INCLUDE[cc-data-platform-banner](../../../../includes/cc-data-platform-banner.md)]

This example shows how to use a [System.Threading.Tasks.Parallel.ForEach Method](/dotnet/api/system.threading.tasks.parallel.foreach) loop to enable data parallelism over a set of records to create in CDS.

This sample uses the CDSWebApiService class synchronous methods within operations. Because the CDSWebApiService class can manage Service Protection API limits, this code can be resilient to the transient 429 errors that clients should expect. It will retry a configurable number of times. 

More information:

- [Web API CDSWebApiService class Sample (C#)](cdswebapiservice.md)
- [Service Protection API Limits](../../api-limits.md)

This sample is based on the [How to: Write a simple Parallel.ForEach loop](/dotnet/standard/parallel-programming/how-to-write-a-simple-parallel-foreach-loop) example, but modified to perform create and delete operations with CDS entities using the synchronous methods provided by the CDSWebApiService class.

> [!NOTE]
> If you want to use Fiddler to observe the expected service protection API limits, you will need to set the number of records to create to be around 10,000. They will start to appear after 5 minutes. Note how the application retries the failures and completes the flow of all the records.

## Prerequisites

The following is required to build and run the CDSWebApiService C# samples :

- Microsoft Visual Studio 2019. 
- Access to Common Data Service with privileges to perform CRUD operations.
  
<a name="bkmk_runSample"></a>
  
## How to run this sample

1. Go to [Web API CDSWebApiService Sample](https://github.com/microsoft/PowerApps-Samples/tree/master/cds/webapi/C%23/CDSWebApiService), clone or download the samples repository, and extract its contents into a local folder.

1. Open the [CDSWebApiService.sln](https://github.com/microsoft/PowerApps-Samples/blob/master/cds/webapi/C%23/CDSWebApiService/CDSWebApiService.sln).

1. Select the **ParallelOperations** project and open the App.config. This is a common [App.config](https://github.com/microsoft/PowerApps-Samples/blob/master/cds/webapi/C%23/CDSWebApiService/App.config) file used by all the samples in this solution. Once you edit this, you can run any of the samples in this solution.

1. You must edit the `Url`, `UserPrincipalName`, and `Password` values to set the CDS instance and credentials you want to connect to.

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

1. Make sure that the **ParallelOperations** project is set as the startup project. The name of the project should be bold to indicate it is the startup project. If the name is not bold, right-click it in the solution explorer and select **Set as Startup Project**.

1. Press F5 to run the program in debug mode.

## Code listing

This sample depends on the assembly included in the CDSWebAPIService project. For information on the methods this class provides see: [Web API CDSWebApiService class Sample (C#)](cdswebapiservice.md).

The following is the code from the Program.cs file:

```csharp
using Newtonsoft.Json.Linq;
using System;
using System.Collections.Concurrent;
using System.Collections.Generic;
using System.Configuration;
using System.Threading.Tasks;

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

        private static void Main()
        {
            #region Optimize Connection

            //Change max connections from .NET to a remote service default: 2
            System.Net.ServicePointManager.DefaultConnectionLimit = 65000;
            //Bump up the min threads reserved for this app to ramp connections faster - minWorkerThreads defaults to 4, minIOCP defaults to 4
            System.Threading.ThreadPool.SetMinThreads(100, 100);
            //Turn off the Expect 100 to continue message - 'true' will cause the caller to wait until it round-trip confirms a connection to the server
            System.Net.ServicePointManager.Expect100Continue = false;
            //Can decreas overall transmission overhead but can cause delay in data packet arrival
            System.Net.ServicePointManager.UseNagleAlgorithm = false;

            #endregion Optimize Connection

            var parallelOptions = new ParallelOptions() { MaxDegreeOfParallelism = maxDegreeOfParallelism };

            var count = 0;

            //Will be populated with account records to import
            List<JObject> accountsToImport = new List<JObject>();
            //ConcurrentBag is a thread-safe, unordered collection of objects.
            ConcurrentBag<Uri> accountsToDelete = new ConcurrentBag<Uri>();
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

            try
            {
                using (CDSWebApiService svc = new CDSWebApiService(serviceConfig))
                {
                    Console.WriteLine($"Creating {accountsToImport.Count} accounts");
                    var startCreate = DateTime.Now;

                    //Create the accounts in parallel
                    Parallel.ForEach(accountsToImport, parallelOptions, (account) =>

                    {
                        //Add the Uri returned to the ConcurrentBag to delete later
                        accountsToDelete.Add(svc.PostCreate("accounts", account));
                    });

                    //Calculate the duration to complete
                    var secondsToCreate = (DateTime.Now - startCreate).TotalSeconds;

                    Console.WriteLine($"Created {accountsToImport.Count} accounts in  {Math.Round(secondsToCreate)} seconds.");

                    Console.WriteLine($"Deleting {accountsToDelete.Count} accounts");
                    var startDelete = DateTime.Now;

                    //Delete the accounts in parallel
                    Parallel.ForEach(accountsToDelete, parallelOptions, (uri) =>
                    {
                        svc.Delete(uri);
                    });

                    //Calculate the duration to complete
                    var secondsToDelete = (DateTime.Now - startDelete).TotalSeconds;

                    Console.WriteLine($"Deleted {accountsToDelete.Count} accounts in {Math.Round(secondsToDelete)} seconds.");
                    Console.WriteLine("Sample completed. Press any key to exit.");
                    Console.ReadLine();
                }
            }
            catch (Exception)
            {
                throw;
            }
        }
    }
}
```

### See also

[Use the Common Data Service Web API](../overview.md)<br />
[Web API CDSWebApiService class Sample (C#)](cdswebapiservice.md)<br />
[Web API CDSWebApiService Async Parallel Operations Sample (C#)](cdswebapiservice-async-parallel-operations.md)<br />
[Web API CDSWebApiService Basic Operations Sample (C#)](cdswebapiservice-basic-operations.md)<br />
[Create an entity using the Web API](../create-entity-web-api.md)<br />
[Update and delete entities using the Web API](../update-delete-entities-using-web-api.md)