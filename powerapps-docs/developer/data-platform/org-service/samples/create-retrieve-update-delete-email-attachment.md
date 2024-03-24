---
title: "Sample: Create, retrieve, update, and delete an email attachment (Microsoft Dataverse) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "This sample shows how to perform CRUD operations on email atachments" # 115-145 characters including spaces. This abstract displays in the search result.
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

# Sample: Create, retrieve, update, and delete an email attachment

This sample shows how to create, retrieve, update, and delete email attachments using the following methods:

- [IOrganizationService.Create](/dotnet/api/microsoft.xrm.sdk.iorganizationservice.create)
- [IOrganizationService.Retrieve](/dotnet/api/microsoft.xrm.sdk.iorganizationservice.retrieve)
- [IOrganizationService.Update](/dotnet/api/microsoft.xrm.sdk.iorganizationservice.update)
- [IOrganizationService.Delete](/dotnet/api/microsoft.xrm.sdk.iorganizationservice.delete)

> [!div class="nextstepaction"]
> [SDK for .NET: Create, retrieve, update, and delete an email attachment sample code](https://github.com/microsoft/PowerApps-Samples/tree/master/dataverse/orgsvc/C%23/CRUDEmailAttachments)

## How to run this sample

[!include[cc-how-to-run-samples](../../includes/cc-how-to-run-samples.md)]

## What this sample does

The `IOrganizationService` message is intended to be used in a scenario that provides programmatic access to the metadata and data for an organization.

## How this sample works

In order to simulate the scenario described in [What this sample does](#what-this-sample-does), the sample will do the following:

### Setup

1. Checks for the current version of the org.
1. The `Email` method creates email activity that is required for the sample.

### Demonstrate

1. The `ActivityMimeAttachment` method creates three email attachments.
1. The `Retrieve` method retrieves an attachment including its id, subject, filename and body.
1. The `Update` method updates the filename of the existing attachment.

### Clean up

Display an option to delete the records created in the [Setup](#setup). The deletion is optional in case you want to examine the tables and data created by the sample. You can manually delete the records to achieve the same result.

[!INCLUDE[footer-include](../../../../includes/footer-banner.md)]
