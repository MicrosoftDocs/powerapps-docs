---
title: "Sample: Enable duplicate detection and retrieve duplicates (Common Data Service for Apps) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "This sample shows how to enable duplicate detection and retrieve duplicate records." # 115-145 characters including spaces. This abstract displays in the search result.
ms.custom: ""
ms.date: 08/01/2018
ms.reviewer: ""
ms.service: "powerapps"
ms.topic: "samples"
author: "brandonsimons" # GitHub ID
ms.author: "jdaly" # MSFT alias of Microsoft employees only
manager: "ryjones" # MSFT alias of manager or PM counterpart
---
# Sample: Enable duplicate detection and retrieve duplicates

<!-- https://docs.microsoft.com/en-us/dynamics365/customer-engagement/developer/org-service/sample-enable-duplicate-detection-and-retrieve-duplicates -->

This sample shows how to enable duplicate detection and retrieve duplicate records. You can download the sample from [here](https://github.com/Microsoft/PowerApps-Samples/tree/master/cds/orgsvc/C%23/EnableDuplicateDetection).

## How to run this sample

[!include[cc-how-to-run-samples](../../includes/cc-how-to-run-samples.md)]

## What this sample does

The `IsDuplicateDetectionEnabled` property is intended to be used in a scenario to enable duplicate detection rule for an organization and also for an entity.

## How this sample works

In order to simulate the scenario described in [What this sample does](#what-this-sample-does), the sample will do the following:

### Setup

1. Checks for the current version of the org.
1. The `Account` method creates some account records to retrieve duplicates.
1. The `RetrieveDuplicateRequest` method retrieves the duplicate records. 
1. The `EnableDupkicateDetectionForOrg` class enables duplicate detection for an organization. 
1. To enable duplicate detection set `IsDuplicateDetectionEnabled = true`.
1. The `RetrieveEntityRequest` method retrieves the netity metadata. 
1. Set `IsDuplicateDetectionEnabled = true` to update the duplicate detection flag.
1. The `UpdateEntityRequest` updates the entity with duplicate detection set to `true`.

### Clean up

1. Display an option to delete the records created in the [Setup](#setup).

    The deletion is optional in case you want to examine the entities and data created by the sample. You can manually delete the records to achieve the same result.
