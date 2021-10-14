---
title: "Sample: Task Parallel Library with CrmServiceClient (Microsoft Dataverse)| Microsoft Docs"
description: "Task Parallel Library (TPL) makes developers more productive by simplifying the process of adding parallelism and concurrency to applications. This sample demonstrates using this with CrmServiceClient"
ms.custom: ""
ms.date: 04/12/2021
ms.reviewer: "pehecke"
ms.service: powerapps
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "samples"
applies_to: 
  - "Dynamics 365 (online)"
author: "JimDaly"
ms.author: "nabuthuk"
manager: "kvivek"
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---
# Sample: Task Parallel Library with CrmServiceClient

[!INCLUDE[cc-terminology](../includes/cc-terminology.md)]

Task Parallel Library (TPL) makes developers more productive by simplifying the process of adding parallelism and concurrency to applications.

Adding parallelism and concurrency can significantly improve the total throughput for applications that need to perform a large number of Dataverse operations in a short period of time.

Download the sample: [Task Parallel Library sample with CrmServiceClient](https://github.com/microsoft/PowerApps-Samples/tree/master/cds/Xrm%20Tooling/TPLCrmServiceClient)

## How to run the sample

1. Download and extract the sample so that you have a copy locally.  
2. Open the `TPLCrmServiceClient.sln` file in Visual Studio.  
3. Press **F5** to compile and run the program.  

## Demonstrates

Because the [Microsoft.Xrm.Tooling.Connector.CrmServiceClient Class](/dotnet/api/microsoft.xrm.tooling.connector.crmserviceclient) includes handling for the transient errors thrown by the Dataverse service protection limits, the combination of TPL and CrmServiceClient is valuable to create applications that can optimize throughput while being resilient to the service protection limit errors by re-trying requests that are rejected due to these limits.

More information: [Service Protection API Limits](../api-limits.md)

The [CrmServiceClient.Clone Method](/dotnet/api/microsoft.xrm.tooling.connector.crmserviceclient.clone) enables TPL to use the client with multiple threads.

This simple sample will generate a number of account table records using the [System.Threading.Tasks.Parallel.ForEach Method](/dotnet/api/system.threading.tasks.parallel.foreach).

Then it will use that technique again to delete the tables created.

**NOTE**:
> By default, this sample will create only 10 records, which is not enough to hit the service protection api limit errors. If you raise the `numberOfRecords` variable value to 10000, you can use Fiddler to observe how some of the requests will be rejected and re-tried.

This sample is not configured to disable the Azure Affinity cookies, which is another recommendation to improve throughput. To enable this, add the following to the App.config of your application:

```xml
  <appSettings>
    <add key="PreferConnectionAffinity"
         value="false" />
  </appSettings>
```

## Code listing

Code for this sample is split between two files that define different parts of the same partial class.

SampleProgram.cs contains this code:

```csharp
using Microsoft.Xrm.Sdk;
using Microsoft.Xrm.Tooling.Connector;
using System;
using System.Collections.Generic;
using System.Linq;

namespace PowerApps.Samples
{
    public partial class SampleProgram
    {
        // Limit on the max degree of parallelism
        private static int maxDegreeOfParallelism = 10;

        //How many records to create with this sample.
        private static readonly int numberOfRecords = 10;

        [STAThread] // Added to support UX
        private static void Main()
        {
            CrmServiceClient service = null;

            try
            {
                service = SampleHelpers.Connect("Connect");
                if (service.IsReady)
                {
                    #region Sample Code

                    #region Set up

                    SetUpSample(service);

                    #endregion Set up

                    #region Demonstrate

                    #region Optimize Connection settings

                    //Change max connections from .NET to a remote service default: 2
                    System.Net.ServicePointManager.DefaultConnectionLimit = 65000;
                    //Bump up the min threads reserved for this app to ramp connections faster - minWorkerThreads defaults to 4, minIOCP defaults to 4
                    System.Threading.ThreadPool.SetMinThreads(100, 100);
                    //Turn off the Expect 100 to continue message - 'true' will cause the caller to wait until it round-trip confirms a connection to the server
                    System.Net.ServicePointManager.Expect100Continue = false;
                    //Can decreas overall transmission overhead but can cause delay in data packet arrival
                    System.Net.ServicePointManager.UseNagleAlgorithm = false;

                    #endregion Optimize Connection settings

                    // Generate a list of account entities to create.

                    var accountsToImport = new List<Entity>();
                    var count = 0;
                    Console.WriteLine($"Preparing to create {numberOfRecords} acccount records");
                    while (count < numberOfRecords)
                    {
                        var account = new Entity("account");
                        account["name"] = $"Account {count}";
                        accountsToImport.Add(account);
                        count++;
                    }

                    try
                    {
                        Console.WriteLine($"Creating {accountsToImport.Count} accounts");

                        var startCreate = DateTime.Now;

                        //Import the list of accounts
                        var createdAccounts = CreateEntities(service, accountsToImport);

                        var secondsToCreate = (DateTime.Now - startCreate).TotalSeconds;

                        Console.WriteLine($"Created {accountsToImport.Count} accounts in  {Math.Round(secondsToCreate)} seconds.");

                        Console.WriteLine($"Deleting {createdAccounts.Count} accounts");
                        var startDelete = DateTime.Now;

                        //Delete the list of accounts created
                        DeleteEntities(service, createdAccounts.ToList());

                        var secondsToDelete = (DateTime.Now - startDelete).TotalSeconds;

                        Console.WriteLine($"Deleted {createdAccounts.Count} accounts in {Math.Round(secondsToDelete)} seconds.");
                    }
                    catch (AggregateException)
                    {
                        // Handle exceptions
                    }

                    Console.WriteLine("Done.");
                    Console.ReadLine();
                }

                #endregion Demonstrate

                #endregion Sample Code

                else
                {
                    const string UNABLE_TO_LOGIN_ERROR = "Unable to Login to Microsoft Dataverse";
                    if (service.LastCrmError.Equals(UNABLE_TO_LOGIN_ERROR))
                    {
                        Console.WriteLine("Check the connection string values in cds/App.config.");
                        throw new Exception(service.LastCrmError);
                    }
                    else
                    {
                        throw service.LastCrmException;
                    }
                }
            }
            catch (Exception ex)
            {
                SampleHelpers.HandleException(ex);
            }
            finally
            {
                if (service != null)
                    service.Dispose();

                Console.WriteLine("Press <Enter> to exit.");
                Console.ReadLine();
            }
        }
    }
}
```

SampleMethods.cs contains the definition of two static methods (`CreateEntities` and `DeleteEntities`) used in the code:


```csharp
/// <summary>
/// Creates entities in parallel
/// </summary>
/// <param name="svc">The CrmServiceClient instance to use</param>
/// <param name="entities">A List of entities to create.</param>
/// <returns></returns>
private static ConcurrentBag<EntityReference> CreateEntities(CrmServiceClient svc, List<Entity> entities)
{
    var createdEntityReferences = new ConcurrentBag<EntityReference>();

    Parallel.ForEach(entities,
        new ParallelOptions() { MaxDegreeOfParallelism = maxDegreeOfParallelism },
        () =>
        {
            //Clone the CrmServiceClient for each thread
            return svc.Clone();
        },
        (entity, loopState, index, threadLocalSvc) =>
        {
            // In each thread, create entities and add them to the ConcurrentBag
            // as EntityReferences
            createdEntityReferences.Add(
                new EntityReference(
                    entity.LogicalName,
                    threadLocalSvc.Create(entity)
                    )
                );

            return threadLocalSvc;
        },
        (threadLocalSvc) =>
        {
            //Dispose the cloned CrmServiceClient instance
            if (threadLocalSvc != null)
            {
                threadLocalSvc.Dispose();
            }
        });

    //Return the ConcurrentBag of EntityReferences
    return createdEntityReferences;
}

/// <summary>
/// Deletes a list of entity references
/// </summary>
/// <param name="svc">The CrmServiceClient instance to use</param>
/// <param name="entityReferences">A List of entity references to delete.</param>
private static void DeleteEntities(CrmServiceClient svc, List<EntityReference> entityReferences)
{
    Parallel.ForEach(entityReferences,
        new ParallelOptions() { MaxDegreeOfParallelism = maxDegreeOfParallelism },
        () =>
        {
            //Clone the CrmServiceClient for each thread
            return svc.Clone();
        },
        (er, loopState, index, threadLocalSvc) =>
        {
            // In each thread, delete the entities
            threadLocalSvc.Delete(er.LogicalName, er.Id);

            return threadLocalSvc;
        },
        (threadLocalSvc) =>
        {
            //Dispose the cloned CrmServiceClient instance
            if (threadLocalSvc != null)
            {
                threadLocalSvc.Dispose();
            }
        });
}
```

### More information

[Task Parallel Library (TPL)](/dotnet/standard/parallel-programming/task-parallel-library-tpl)

[!INCLUDE[footer-include](../../../includes/footer-banner.md)]