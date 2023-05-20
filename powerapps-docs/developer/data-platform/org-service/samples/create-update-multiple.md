---
title: "Sample: Use CreateMultiple and UpdateMultiple (Microsoft Dataverse) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "This sample shows how to perform bulk create and update operations by using a single web service method call." # 115-145 characters including spaces. This abstract displays in the search result.
ms.date: 05/20/2023
author: divkamath
ms.author: dikamath
ms.reviewer: jdaly
ms.topic: sample
search.audienceType:
  - developer
search.app:
  - PowerApps
  - D365CE
contributors:
  - JimDaly
  - phecke
---

# Sample: Use CreateMultiple and UpdateMultiple

This sample shows how to perform bulk create and update operations using several different approaches including the use of [CreateMultipleRequest](xref:Microsoft.Xrm.Sdk.Messages.CreateMultipleRequest) and [UpdateMultipleRequest](xref:Microsoft.Xrm.Sdk.Messages.UpdateMultipleRequest) classes. The messages for these request classes are optimized to provide the most performant way to create or update records with Dataverse.

This sample is a Visual Studio .NET 6.0 solution that contains five different projects that perform the same operations in different ways so that you can compare the performance of each method.

You can download the sample from [here](https://github.com/microsoft/PowerApps-Samples/tree/master/dataverse/orgsvc/C%23-NETCore/xMultipleSamples).

[!INCLUDE[cc-terminology](../../includes/cc-terminology.md)]

## Prerequisites

- Microsoft Visual Studio 2022
- Access to Dataverse with system administrator or system customizer privileges.

## How to run this sample

1. Clone or download the [PowerApps-Samples](https://github.com/microsoft/PowerApps-Samples) repository.
1. Open the `PowerApps-Samples/dataverse/orgsvc/C#-NETCore/xMultipleSamples/xMultipleSamples.sln` file using Visual Studio 2022.
1. Edit the `appsettings.json` file. Set the connection string `Url` and `Username` parameters as appropriate for your test environment.
1. The environment Url can be found in the Power Platform admin center. It has the form `https://<environment-name>.crm.dynamics.com`.
1. Build the solution, select the desired project as the startup project and press **F5** to run the console application in debug mode.

When the sample runs, you're prompted in the default browser to select an environment user account and enter a password. To avoid having to enter a password every time you run a sample, insert a `Password` parameter into the connection string in the appsettings.json file. For example:

```json
{
"ConnectionStrings": {
    "default": "AuthType=OAuth;Url=https://myorg.crm.dynamics.com;Username=someone@myorg.onmicrosoft.com;Password=mypassword;RedirectUri=http://localhost;AppId=51f81489-12ee-4a9e-aaae-a2591f45987d;LoginPrompt=Auto"
  }
}
```
> [!TIP]
> You can set a user environment variable named `DATAVERSE_APPSETTINGS` to the file path of the appsettings.json file stored anywhere on your computer. The samples will use that appsettings file if the environment variable exists and is not null. Be sure to log out and back in again after you define the variable for it to take effect. To set an environment variable, go to **Settings** > **System** > **About**, select **Advanced system settings**, and then choose **Environment variables**.

## What this sample does

This sample is a .NET 6.0 Visual Studio 2022 solution that contains five projects that perform the same operations:

1. Create a new custom table named `sample_example` if it doesn't already exist.
1. Prepare a configurable number of `sample_example` entity instances for the custom table representing records to create.

   Each record has the  `sample_name` column value set with an incrementing number. The first value is `sample record 0000001`.

1. Create the `sample_example` records. Each project uses a different method.
1. Update the set of entity instances by appending text to the `sample_name` attribute.
1. Update the `sample_example` records using the same method they were created.
1. Use a [BulkDeleteRequest](xref:Microsoft.Crm.Sdk.Messages.BulkDeleteRequest) to delete the `sample_example` records created and report on the success of this request.
1. Delete the custom `sample_example` table created in the first step, unless configured not to.

Each project uses a shared set of settings in the `Settings.cs` file that allow you to control:

- `NumberOfRecords`: The number of records to create. The default value is 100 but you can raise it to 1000 or higher.
- `BypassCustomPluginExecution`: Whether custom plug-in logic should be bypassed. This setting is useful to observe the performance impact of plug-ins registered on events for the table.
- `DeleteTable`: Whether to delete the custom `sample_example` table at the end of the sample. If you want to test plug-ins that use events on this table, setting this to true preserves the table so you can run the samples multiple times while testing plug-ins.

The `Settings.cs` file is included in each project. Apply the change in one project and they're set for all of them.

### Supporting examples

The shared `Utility.cs` class contains static methods to perform operations that are common in each sample. These methods aren't the primary focus of the sample, but might be of interest:

|Method  |Description  |
|---------|---------|
|`TableExists`|Detects whether a table with the specified schema name exists.|
|`BulkDeleteRecordsByIds`|Asynchronously deletes a group of records for a specified table by ID.|
|`IsMessageAvailable`|Detect whether a specified message is supported for the specified table.|
|`CreateExampleTable`|Creates the table used by projects in this solution if it doesn't already exist.|
|`DeleteExampleTable`|Deletes the table used by projects in this solution, unless the `DeleteTable` setting is false.|

## How this sample works

By default the **CreateUpdateMultiple** project should be set as the startup project for the solution. To try any of the other samples, select the project in Solution Explorer and choose **Set as startup project**.

> [!NOTE]
> [Sample: CreateMultiple and UpdateMultiple plug-ins](createmultiple-updatemultiple-plugin.md) is designed to work together with this sample to demonstrate how plug-ins can be migrated from `Create` and `Update` to `CreateMultiple` and `UpdateMultiple` messages.

### Demonstrate

As mentioned in [What this sample does](#what-this-sample-does) above, this sample demonstrates how to create and update records in bulk for a custom table created by the sample. To demonstrate this, it must create a custom table and clean up when you finish running the sample.

Details about each project and the default output are described below:

#### CreateUpdateMultiple

This project uses [CreateMultipleRequest](xref:Microsoft.Xrm.Sdk.Messages.CreateMultipleRequest) and [UpdateMultipleRequest](xref:Microsoft.Xrm.Sdk.Messages.UpdateMultipleRequest) classes to perform bulk create and update operations.

This project sends two requests, each attempting to complete operations for the total configured number of records.

The output of this project with 100 records includes:

```
Sending CreateMultipleRequest...
        Created 100 records in 1 seconds.
Preparing 100 records to update..
Sending UpdateMultipleRequest...
        Updated 100 records in 3 seconds.
```

#### ExecuteMultiple

This project uses the [ExecuteMultipleRequest class](xref:Microsoft.Xrm.Sdk.Messages.ExecuteMultipleRequest) class to perform bulk create and update operations.

Because `ExecuteMultiple` is limited to 1000 requests and the sample may be configured to create more records than 1000, this project chunks the total number of requests into groups of 1000 and sends as many requests as needed to perform the respective operations.

The output of this project with 100 records includes:

```
Preparing 100 records to create...
Sending 1 ExecuteMultipleRequest to create...
 Sending ExecuteMultipleRequest 1...
        Created 100 records in 4 seconds.
Preparing 100 records to update...
Sending 1 ExecuteMultipleRequest to update...
 Sending ExecuteMultipleRequest 1...
        Updated 100 records in 4 seconds.
```

The output of this project with 2000 records includes:

```
Preparing 2000 records to create...
Sending 2 ExecuteMultipleRequests to create...
 Sending ExecuteMultipleRequest 1...
 Sending ExecuteMultipleRequest 2...
        Created 2000 records in 58 seconds.
Preparing 2000 records to update...
Sending 2 ExecuteMultipleRequests to update...
 Sending ExecuteMultipleRequest 1...
 Sending ExecuteMultipleRequest 2...
        Updated 2000 records in 76 seconds.
```

#### ParallelCreateUpdate

This project uses the <xref:System.Threading.Tasks.Parallel.ForEachAsync%2A?displayProperty=fullName> together with the [Microsoft.PowerPlatform.Dataverse.Client.ServiceClient.ServiceClient.CreateAsync Method](/dotnet/api/microsoft.powerplatform.dataverse.client.serviceclient.createasync) 
and [Microsoft.PowerPlatform.Dataverse.Client.ServiceClient.ServiceClient.UpdateAsync Method](/dotnet/api/microsoft.powerplatform.dataverse.client.serviceclient.updateasync) to perform individual create and update operations using multiple threads.

The number of threads used depends on the [ServiceClient.RecommendedDegreesOfParallelism Property](xref:Microsoft.PowerPlatform.Dataverse.Client.ServiceClient.RecommendedDegreesOfParallelism), which is based on the value of the `x-ms-dop-hint` response header. The `x-ms-dop-hint` response header provides a hint for the Degree Of Parallelism (DOP) that represents a number of threads that should provide good results for a given environment.

The output of this project with 100 records includes:

```
Sending create requests in parallel...
        Created 100 records in 3 seconds.
Preparing 100 records to update..
Sending update requests in parallel...
        Updated 100 records in 3 seconds.
```

#### ParallelCreateUpdateMultiple

This project uses the <xref:System.Threading.Tasks.Parallel.ForEachAsync%2A?displayProperty=fullName> together with the [Microsoft.PowerPlatform.Dataverse.Client.ServiceClient.ServiceClient.ExecuteAsync Method](/dotnet/api/microsoft.powerplatform.dataverse.client.serviceclient.executeasync) to perform multiple create and update operations using multiple threads.

The number of threads used depends on the [ServiceClient.RecommendedDegreesOfParallelism Property](xref:Microsoft.PowerPlatform.Dataverse.Client.ServiceClient.RecommendedDegreesOfParallelism), which is based on the value of the `x-ms-dop-hint` response header. The `x-ms-dop-hint` response header provides a hint for the Degree Of Parallelism (DOP) that represents a number of threads that should provide good results for a given environment.

The output of this project with 100 records includes:

```
Sending create requests in parallel...
        Created 100 records in 1 seconds.
Preparing 100 records to update..
Sending update requests in parallel...
        Updated 100 records in 3 seconds.
```


#### SimpleLoop

This project simply loops through the list of prepared Entity instances to perform individual create and update  operations sequentially using the [CreateRequest](xref:Microsoft.Xrm.Sdk.Messages.CreateRequest) and [UpdateRequest](xref:Microsoft.Xrm.Sdk.Messages.UpdateRequest) classes.

> [!NOTE]
> This sample represents the case where no effort is applied to maximize throughput. It should represent the worst case for performance.

The output of this project with 100 records includes:

```
Sending create requests one at a time...
        Created 100 records in 10 seconds.
Preparing 100 records to update..
Sending update requests one at a time...
        Updated 100 records in 12 seconds.
```

### Clean up

By default, when each project in the solution completes successfully, all the records created in the custom `sample_example` table are deleted and the `sample_example` table is also deleted. But it's expected that you'll change the `DeleteTable` setting to preserve the table when running each of the samples. Make sure to set it to `true` the last time you run one of the projects so that the table will be deleted.


### See Also

[Use CreateMultiple and UpdateMultiple (Preview)](../use-createmultiple-updatemultiple.md)<br />
[Write plug-ins for CreateMultiple and UpdateMultiple (Preview)](../../write-plugin-multiple-operation.md)<br />
[Sample: CreateMultiple and UpdateMultiple plug-ins](createmultiple-updatemultiple-plugin.md)

[!INCLUDE[footer-include](../../../../includes/footer-banner.md)]
