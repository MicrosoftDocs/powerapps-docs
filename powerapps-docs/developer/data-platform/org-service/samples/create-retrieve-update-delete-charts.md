---
title: "Sample: Create, retrieve, update, and delete charts ( Microsoft Dataverse) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "This sample showcases how to create, retrieve, update, and delete an user-owned visualizations." # 115-145 characters including spaces. This abstract displays in the search result.
ms.date: 04/03/2022
author: mspilde
ms.author: mspilde
ms.reviewer: jdaly
ms.topic: sample
search.audienceType:
  - developer
contributors:
  - JimDaly
  - phecke
---

# Sample: Create, retrieve, update, and delete a chart

This sample shows how to create, retrieve, update, and delete an user-owned visualization using the following methods:

- [IOrganizationService.Create](/dotnet/api/microsoft.xrm.sdk.iorganizationservice.create)
- [IOrganizationService.Retrieve](/dotnet/api/microsoft.xrm.sdk.iorganizationservice.retrieve)
- [IOrganizationService.Update](/dotnet/api/microsoft.xrm.sdk.iorganizationservice.update)
- [IOrganizationService.Delete](/dotnet/api/microsoft.xrm.sdk.iorganizationservice.delete)

> [!div class="nextstepaction"]
> [SDK for .NET: Create, retrieve, update, and delete a chart sample code](https://github.com/microsoft/PowerApps-Samples/tree/master/dataverse/orgsvc/C%23/CRUDOperationsChart)

[!INCLUDE[cc-terminology](../../includes/cc-terminology.md)]

## How to run this sample

[!include[cc-how-to-run-samples](../../includes/cc-how-to-run-samples.md)]

## What this sample does

The `IOrganizationService` message is intended to be used in a scenario where it contains data that provides programmatic access to the metadata and data for an organization.

## How this sample works

In order to simulate the scenario described in [What this sample does](#what-this-sample-does), the sample will do the following:

### Setup

1. Checks for the current version of the org.
1. The `CreateRequiredRecords` method creates records that is required for the sample.

### Demonstrate

1. The `presentationXml` method sets the presentation XML string.
2. The `dataXml` method sets the data XML string.
3. The `newUserOwnedVisualization` method creates the visualization record.
4. The `retrievedOrgOwnedVisualization` method retrieves the visualization.
5. The `newDataXml` method updates the name and the data description string.

### Clean up

Display an option to delete the records created in the [Setup](#setup). The deletion is optional in case you want to examine the tables and data created by the sample. You can manually delete the records to achieve the same result.

[!INCLUDE[footer-include](../../../../includes/footer-banner.md)]
