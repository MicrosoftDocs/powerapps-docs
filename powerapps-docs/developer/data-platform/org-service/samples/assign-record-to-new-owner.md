---
title: " Assign a record to a new owner (Microsoft Dataverse) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "This sample showcases how to assign records to a new owner." # 115-145 characters including spaces. This abstract displays in the search result.
ms.date: 04/03/2022
author: divkamath
ms.author: dikamath
ms.reviewer: pehecke
ms.topic: sample
search.audienceType:
  - developer
contributors:
  - JimDaly
  - phecke
---

# Assign a record to a new owner

This sample shows how to assign an account to another user by using the [IOrganizationService.Update](/dotnet/api/microsoft.xrm.sdk.iorganizationservice.update) message.

This sample uses the `IOrganization.Update` method rather than the [AssignRequest](/dotnet/api/microsoft.crm.sdk.messages.assignrequest) because there is an effort to remove specialized messages. More information: [Perform specialized operations using update](../../special-update-operation-behavior.md)

> [!div class="nextstepaction"]
> [SDK for .NET: Assign a record to a new owner sample code](https://github.com/microsoft/PowerApps-Samples/tree/master/dataverse/orgsvc/C%23/AssignRecordToNewOwner)

## How to run this sample

[!include[cc-how-to-run-samples](../../includes/cc-how-to-run-samples.md)]

## What this sample does

The [IOrganizationService.Update](/dotnet/api/microsoft.xrm.sdk.iorganizationservice.update) message is intended to be used in a scenario where it contains the data that is needed to update existing record.

## How this sample works

In order to simulate the scenario described in [What this sample does](#what-this-sample-does), the sample will do the following:

### Setup

1. Checks for the current version of the org.
1. Creates required data that this sample requires.

### Demonstrate

1. The `Retrieve` method retrieves the account records created in the setup(#setup).
1. The `Update` message updates the `ownerid` column to the user who you want to own the record.

### Clean up

Displays an option to delete all the data created in the sample. The deletion is optional in case you want to examine the data created by the sample. You can manually delete the data to achieve same results.

[!INCLUDE[footer-include](../../../../includes/footer-banner.md)]
