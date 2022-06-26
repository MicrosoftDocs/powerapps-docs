---
title: "Sample: Delete a queue (early bound)(Microsoft Dataverse) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "This sample showcases how to delete queue" # 115-145 characters including spaces. This abstract displays in the search result.
ms.date: 04/03/2022
author: JimDaly #TODO: No Owner
ms.author: jdaly
manager: kvivek
ms.reviewer: pehecke
ms.topic: sample
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---

# Sample: Delete a queue (early bound)



This sample shows how to delete a simple queue using the [IOrganizationService.Delete](/dotnet/api/microsoft.xrm.sdk.iorganizationservice.delete) message.

You can download the sample from [here](https://github.com/microsoft/PowerApps-Samples/tree/master/cds/orgsvc/C%23/DeleteQueue).

## How to run this sample

[!include[cc-how-to-run-samples](../../includes/cc-how-to-run-samples.md)]

## What this sample does

The `IOrganizationService` message is intended to be used in a scenario where it contains data that provides programmatic access to the metadata and data for an organization.

## How this sample works

In order to simulate the scenario described in [What this sample does](#what-this-sample-does), the sample will do the following:

### Setup

1. Checks for the current version of the org.
2. The `CreateRequiredRecords` method creates records that are required for the sample.

### Demonstrate

The `newQueue` method creates a queue instance and set its property values. 

### Clean up

Display an option to delete the records created in the [Setup](#setup). The deletion is optional in case you want to examine the tables and data created by the sample. You can manually delete the records to achieve the same result.



[!INCLUDE[footer-include](../../../../includes/footer-banner.md)]
