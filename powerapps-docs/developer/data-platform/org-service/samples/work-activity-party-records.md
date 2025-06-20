---
title: "Sample: Work with activity party records (Microsoft Dataverse) | Microsoft Docs" 
description: "This sample shows how to work with activity party records" 
ms.date: 12/17/2024
author: phecke
ms.author: pehecke
ms.reviewer: jdaly
ms.topic: sample
search.audienceType:
  - developer
contributors:
  - JimDaly
  - phecke
---

# Sample: Work with activity party records

This sample code shows how to work with activity party records. Learn how to create a letter activity addressed to multiple contacts.

> [!div class="nextstepaction"]
> [SDK for .NET: Work with activity party records sample code](https://github.com/microsoft/PowerApps-Samples/tree/master/dataverse/orgsvc/CSharp-NETCore/Activities/ActivityParty)

Related article: [Activity tables](../../activity-entities.md)

## About the sample code

|Sample|Description|Build target|
|---|---|---|
|ActivityParty|Demonstrates creating a letter activity.|.NET 9|

The code sample demonstrates how to create a letter activity. Specifically, the samples demonstrate how to:

1. Connect to Dataverse using a [connection string](../../xrm-tooling/use-connection-strings-xrm-tooling-connect.md) that defines required connection information
1. Create a [letter activity](../../reference/entities/letter.md) to send to multiple [contacts](../../reference/entities/contact.md)
1. Use the Dataverse [organization service context](../organizationservicecontext.md) to process the data changes
1. Use [early-bound](../early-bound-programming.md#early-bound) entity types

The code being demonstrated can be found in the `Program.CreateLetter()` method invoked by `Program.Run()`.

The early-bound entity files in the *DataModel* project were generated using the following PAC CLI command:
`pac modelbuilder build`. More information: [pac modelbuilder](/power-platform/developer/cli/reference/modelbuilder)

More general information can be found in [README-code-design](https://github.com/microsoft/PowerApps-Samples/tree/master/dataverse/orgsvc/CSharp-NETCore/README-code-design.md) file.

## How to build and run the code sample

1. Clone the [PowerApps-Samples](https://github.com/microsoft/PowerApps-Samples) repository.
1. Locate the sample folder.
1. Open the solution file (*.sln) in Visual Studio.
1. Edit the project's appsettings.json file and set the `Url`value as appropriate for your Dataverse test environment.
1. Build and run the project [F5].
1. You are prompted in a browser window for account sign-in credentials to the target environment.

## Expected program output

For a successful run, the program's console output should look similar to the following example.
Otherwise, any errors or exceptions are displayed.

```console
CreateLetter(): letter activity created with ID < >
Press any key to undo environment data changes.
```

[!INCLUDE[footer-include](../../../../includes/footer-banner.md)]
