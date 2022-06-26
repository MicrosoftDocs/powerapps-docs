---
title: "Sample: Retrieve all charts attached to a table (Microsoft Dataverse) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "This sample showcases how to retrieve charts attached to a table " # 115-145 characters including spaces. This abstract displays in the search result.
ms.date: 04/03/2022
author: mspilde
ms.author: mspilde
manager: lwelicki
ms.reviewer: jdaly
ms.topic: sample
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---

# Sample: Retrieve all charts attached to a table

This sample shows how to retrieve all the organization-owned visualizations attached to a table by using the [IOrganizationService.RetrieveMultiple](//dotnet/api/microsoft.xrm.sdk.iorganizationservice.retrievemultiple) method.

You can download the sample from [here](https://github.com/microsoft/PowerApps-Samples/tree/master/cds/orgsvc/C%23/RetrieveChartsAttachedToEntity).

[!INCLUDE[cc-terminology](../../includes/cc-terminology.md)]

## How to run this sample

[!include[cc-how-to-run-samples](../../includes/cc-how-to-run-samples.md)]


## What this sample does

The `IOrganizationService` message is intended to be used in a scenario where it contains data that provides programmatic access to the metadata and data for an organization.

## How this sample works

In order to simulate the scenario described in [What this sample does](#what-this-sample-does), the sample will do the following:

### Setup

Checks for the current version of the org.

### Demonstrate

The `newSavedQuery` method creates a query for retrieving all organization-owned visualizations that are attached to the account table.


### Clean up

This sample creates no records. No cleanup is required.


[!INCLUDE[footer-include](../../../../includes/footer-banner.md)]
