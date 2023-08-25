---
title: "Sample: Initialize a record from existing record (Microsoft Dataverse) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "This sample showcases how to create a new record from existing record." # 115-145 characters including spaces. This abstract displays in the search result.
ms.date: 04/03/2022
author: JimDaly #TODO: No Owner
ms.author: jdaly
ms.reviewer: pehecke
ms.topic: sample
search.audienceType:
  - developer
contributors:
  - JimDaly
  - phecke
---

# Sample: Initialize a record from existing record

This sample shows how to use the [IOrganizationService.InitializeFromRequest](/dotnet/api/microsoft.crm.sdk.messages.initializefromrequest) message to create new records from an existing record.

> [!div class="nextstepaction"]
> [SDK for .NET: Initialize a record from existing record sample code](https://github.com/microsoft/PowerApps-Samples/tree/master/dataverse/orgsvc/C%23/InitializeRecordFromExisting)

## How to run this sample

[!include[cc-how-to-run-samples](../../includes/cc-how-to-run-samples.md)]

## What this sample does

The `IOrganizationService.InitializeFromRequest` message is intended to be used in a scenario where it contains the data that is needed to initialize a new record from an existing record.

## How this sample works

In order to simulate the scenario described in [What this sample does](#what-this-sample-does), the sample will do the following:

### Setup

1. Checks for the current version of the org.
2. The `CreateRequiredRecords` method creates any records that this sample requires.

### Demonstrate

1. The `InitializeFromRequest` method creates the request and set properties for the request object.
2. The `InitializeFromResponse` method executes the request.

### Clean up

Display an option to delete the sample data that is created in [Setup](#setup). The deletion is optional in case you want to examine the tables and data created by the sample. You can manually delete the records to achieve the same result.

[!INCLUDE[footer-include](../../../../includes/footer-banner.md)]
