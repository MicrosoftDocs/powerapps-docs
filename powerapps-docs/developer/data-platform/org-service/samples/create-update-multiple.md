---
title: "Sample: Use CreateMultiple and UpdateMultiple (Microsoft Dataverse) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "This sample shows how to execute multiple organization messages requests by using a single web service method call." # 115-145 characters including spaces. This abstract displays in the search result.
ms.date: 12/12/2022
author: divka78
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

This sample shows how to perform bulk create and update operations by using a single web service method call, passing [CreateMultipleRequest](/dotnet/api/microsoft.xrm.sdk.messages.createmultiplerequest) and [UpdateMultipleRequest](/dotnet/api/microsoft.xrm.sdk.messages.updatemultiplerequest) and as parameters.

These messages are optimized to provide the most performant way to create or update records with Dataverse.

This sample is a Visual Studio .NET 6.0 solution that contains 4 different projects that perform the same operations in different ways so that you can compare the performance of each method.

<!-- TODO: add link -->
You can download the sample from [here](https://github.com/microsoft/PowerApps-Samples/tree/master/dataverse/orgsvc/C%23/ExecutemultipleRequests).

[!INCLUDE[cc-terminology](../../includes/cc-terminology.md)]

## Prerequisites

- Microsoft Visual Studio 2022
- Access to Dataverse with system administrator or system customizer privileges.

## How to run this sample

1. Clone or download the [PowerApps-Samples](https://github.com/microsoft/PowerApps-Samples) repository.
1. Open the [PowerApps-Samples/dataverse/orgsvc/C#-NETCore/CreateUpdateMultiple/CreateUpdateMultiple.sln](TODO) file using Visual Studio 2022.
1. Edit the appsettings.json file. Set the connection string `Url` and `Username` parameters as appropriate for your test environment.
1. The environment Url can be found in the Power Platform admin center. It has the form `https://<environment-name>.crm.dynamics.com`.
1. Build the solution, and then run the desired project.

When the sample runs, you will be prompted in the default browser to select an environment user account and enter a password. To avoid having to do this every time you run a sample, insert a `Password` parameter into the connection string in the appsettings.json file. For example:

```json
{
"ConnectionStrings": {
    "default": "AuthType=OAuth;Url=https://myorg.crm.dynamics.com;Username=someone@myorg.onmicrosoft.com;Password=mypassword;RedirectUri=http://localhost;AppId=51f81489-12ee-4a9e-aaae-a2591f45987d;LoginPrompt=Auto"
  }
}
```
> [!TIP]
> You can set a user environment variable named `DATAVERSE_APPSETTINGS` to the file path of the appsettings.json file stored anywhere on your computer. The samples will use that appsettings file if the environment variable exists and is not null. Be sure to log out and back in again after you define the variable for it to take affect. To set an environment variable, go to **Settings** > **System** > **About**, select **Advanced system settings**, and then choose **Environment variables**.

## What this sample does

This sample is a Visual Studio 2022 solution that contains 4 projects that perform the same operations:

1. Create a new custom table named `sample_example` if it doesn't already exist.
1. Prepare a configurable set of entities for the custom table representing records to create.
1. Create the records. Each project uses a different method.
1. Update the set of entities that were created by appending text to the name.
1. Update the records using the same method they were created
1. Use the the `BulkDeleteRequest` to delete the records created and report on the success of this request.
1. Delete the custom `sample_example` table created in the first step.

Each project uses a shared set of settings in the `Settings.cs` file that allow you to control:

- `NumberOfRecords`: The number of records to create. The default value is 100 but you can raise it to 1000 or higher.
- `BypassCustomPluginExecution`: Whether custom plug-in logic should be bypassed. This is useful to observe the performance impact of plug-ins registered on events for the table.
- `DeleteTable`: Whether to delete the custom `sample_example` table at the end of the sample. If you want to test plug-ins that use events on this table, this will preserve the table so you can run the samples multiple times while testing plug-ins.

These settings are in the Settings.cs file that is included in each project. Apply the change in one project and they will be set for all of them.

The `ExecuteMultipleRequest` message is intended to be used in a scenario where it contains data that is needed to execute one or more messages requests as a single batch operation, and optionally return a collection of results.

## How this sample works

By default the **CreateUpdateMultiple** project should be set as the startup project for the solution. To try any of the other samples, select the project in Solution Explorer and choose Set as startup project.

### Demonstrate

As mentioned in [What this sample does](#what-this-sample-does) above, this sample demonstrates how to create and update records in bulk for a custom table created by the sample. To do this, it must create a custom table and clean up when you finish running the sample.

The shared `Utility.cs` class contains static methods to perform operations that are common in each sample. These are not the primary focus of the sample, but might be of interest:

|Method  |Description  |
|---------|---------|
|`TableExists`|Detects whether a table with the specified schema name exists.|
|`BulkDeleteRecordsByIds`|Asynchronously deletes a group of records for a specified table by id.|
|`IsMessageAvailable`|Detect whether a specified message is supported for the specified table.|
|`CreateExampleTable`|Creates the table used by projects in this solution if it doesn't already exist.|
|`DeleteExampleTable`|Deletes the table used by projects in this solution, unless the `DeleteTable` setting is false.|

Details about each project and the default output are described below:

#### CreateUpdateMultiple
<!-- TODO -->
#### ExecuteMultiple
<!-- TODO -->
#### ParallelCreateUpdate
<!-- TODO -->
#### SimpleLoop
<!-- TODO -->

### Clean up

By default, when each project in the solution completes successfully, all the records created in the custom `sample_example` table will be deleted and the `sample_example` table will also be deleted. But it is expected that you will change the `DeleteTable` setting to preserve the table when running each of the samples. Make sure to set it to `true` the last time you run one of the projects so that the table will be deleted.


### See Also

[Use CreateMultiple and UpdateMultiple (Preview)](../use-createmultiple-updatemultiple.md)<br />

[!INCLUDE[footer-include](../../../../includes/footer-banner.md)]
