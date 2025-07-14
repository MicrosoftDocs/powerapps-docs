---
title: "Web API Conditional Operation sample (C#) (Microsoft Dataverse)| Microsoft Docs"
description: "This sample shows how to perform conditional message operations when accessing table rows of the Microsoft Dataverse."
ms.date: 09/02/2022
author: MsSQLGirl
ms.author: jukoesma
ms.reviewer: jdaly
search.audienceType:
  - developer
contributors:
  - JimDaly
---

# Web API Conditional Operations sample (C#)

[!INCLUDE[cc-terminology](../../includes/cc-terminology.md)]

This .NET 6.0 sample demonstrates how to perform common data operations using the Dataverse Web API.

This sample uses the common helper code in the [WebAPIService class library (C#)](webapiservice.md).
  
> [!NOTE]
> This sample implements the Dataverse operations and console output detailed in [Web API Conditional Operations Sample](../web-api-conditional-operations-sample.md) and uses the common C# constructs described in [Web API Samples (C#)](../web-api-samples-csharp.md).

## Prerequisites

These are required to build and run this sample:

- Microsoft Visual Studio 2022.
- Access to Dataverse with privileges to perform data operations.
  
<a name="bkmk_runSample"></a>
  
## How to run this sample

1. Clone or download the [PowerApps-Samples](https://github.com/microsoft/PowerApps-Samples) repository.
1. Locate the [/dataverse/webapi/C#-NETx/ConditionalOperations/](https://github.com/microsoft/PowerApps-Samples/tree/master/dataverse/webapi/CSharp-NETx/ConditionalOperations) folder.
1. Open the `ConditionalOperations.sln` file using Visual Studio 2022
1. Edit the `appsettings.json` file to set the following property values:

   |Property|Instructions  |
   |---------|---------|
   |`Url`|The Url for your environment. Replace the placeholder `https://yourorg.api.crm.dynamics.com` value with the value for your environment. See [View developer resources](../../view-download-developer-resources.md) to find the Url for your environment. |
   |`UserPrincipalName`|Replace the placeholder `you@yourorg.onmicrosoft.com` value with the UPN value you use to access the environment.|
   |`Password`|Replace the placeholder `yourPassword` value with the password you use.|

1. Save the `appsettings.json` file
1. Press F5 to run the sample.

## Code

The code for this sample is here: [PowerApps-Samples/dataverse/webapi/C#-NETx/ConditionalOperations/Program.cs](https://github.com/microsoft/PowerApps-Samples/blob/master/dataverse/webapi/CSharp-NETx/ConditionalOperations/Program.cs)

## Demonstrates

This sample has four regions:

### Section 0: Create sample records

Operations:

- Creates a single account record.
- Retrieves the record and stores the ETag value as `initialAcctETagVal`.

### Section 1: Conditional GET

Operations:

1. Attempts to retrieve the record setting the `If-None-Match` header with the `initialAcctETagVal` value.

   Request fails with `304 NotModified` as expected.

1. Update the record `telephone1` column value.
1. Attempt to retrieve the record again setting the `If-None-Match` header with the `initialAcctETagVal` value.

   Request succeeds because the initial ETag value doesn't match anymore.

1. Store the new ETag value as `updatedAcctETagVal`.

### Section 2: Optimistic concurrency on delete and update

Operations:

1. Attempt to delete the original account setting the `If-Match` header with the `initialAcctETagVal` value.

   Request fails with `412 PreconditionFailed` as expected.

1. Attempt to update the original account setting the `If-Match` header with the `initialAcctETagVal` value.

   Request fails with `412 PreconditionFailed` as expected.

1. Attempt to update the original account setting the `If-Match` header with the `updatedAcctETagVal` value.

   Request succeeds because the ETag value matches the current value for the record.

### Section 3: Delete sample records

Operations: A reference to each record created in this sample was added to a list as it was created. This section sends a `$batch` request to delete the record.

## Clean up

By default this sample deletes all the records created in it. If you want to view created records after the sample is completed, change the `deleteCreatedRecords` variable to `false` and you'll be prompted to decide if you want to delete the records.

### See also

[Perform conditional operations using the Web API](../perform-conditional-operations-using-web-api.md)<br />
[Use the Dataverse Web API](../overview.md)<br />
[WebAPIService class library (C#)](webapiservice.md)<br />
[Web API Samples](../web-api-samples.md)<br />
[Web API Basic Operations Sample (C#)](webapiservice-basic-operations.md)<br />
[Web API Query Data sample (C#)](webapiservice-query-data.md)<br />
[Web API Functions and Actions Sample (C#)](webapiservice-functions-and-actions.md)<br />
[Web API table schema operations sample (C#)](webapiservice-metadata-operations.md)<br />
[Web API WebApiService Parallel Operations Sample (C#)](webapiservice-parallel-operations.md)<br />
[Web API Parallel Operations with TPL Dataflow components Sample (C#)](webapiservice-tpl-dataflow-parallel-operations.md)<br />

[!INCLUDE[footer-include](../../../../includes/footer-banner.md)]
