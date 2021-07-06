---
title: "Sample: Enable duplicate detection and retrieve duplicates (Microsoft Dataverse) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "This sample shows how to enable duplicate detection and retrieve duplicate records." # 115-145 characters including spaces. This abstract displays in the search result.
ms.custom: ""
ms.date: 10/31/2018
ms.reviewer: "pehecke"
ms.service: powerapps
ms.topic: "samples"
author: "JimDaly" # GitHub ID
ms.author: "jdaly" # MSFT alias of Microsoft employees only
manager: "ryjones" # MSFT alias of manager or PM counterpart
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---
# Sample: Enable duplicate detection and retrieve duplicates

[!INCLUDE[cc-data-platform-banner](../../../../includes/cc-data-platform-banner.md)]

This sample shows how to enable duplicate detection and retrieve duplicate records. You can download the sample from [here](https://github.com/Microsoft/PowerApps-Samples/tree/master/cds/orgsvc/C%23/EnableDuplicateDetection).

[!INCLUDE[cc-terminology](../../includes/cc-terminology.md)]

## How to run this sample

[!include[cc-how-to-run-samples](../../includes/cc-how-to-run-samples.md)]

## What this sample does

The `IsDuplicateDetectionEnabled` property is intended to be used in a scenario to enable duplicate detection rule for an organization and also for a table.

## How this sample works

In order to simulate the scenario described in [What this sample does](#what-this-sample-does), the sample will do the following:

### Setup

1. Checks for the current version of the org.
1. The `Account` method creates some account records to retrieve duplicates.
1. The `RetrieveDuplicateRequest` method retrieves the duplicate records. 
1. The `EnableDuplicateDetectionForOrg` class enables duplicate detection for an organization. 
1. To enable duplicate detection set `IsDuplicateDetectionEnabled = true`.
1. The `RetrieveEntityRequest` method retrieves the entity metadata. 
1. Set `IsDuplicateDetectionEnabled = true` to update the duplicate detection flag.
1. The `UpdateEntityRequest` updates the entity with duplicate detection set to `true`.

### Clean up

Display an option to delete the records created in the [Setup](#setup). The deletion is optional in case you want to examine the tables and data created by the sample. You can manually delete the records to achieve the same result.


[!INCLUDE[footer-include](../../../../includes/footer-banner.md)]