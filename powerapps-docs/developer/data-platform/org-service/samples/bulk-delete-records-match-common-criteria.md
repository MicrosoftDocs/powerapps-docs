---
title: "Sample: Bulk delete records in bulk that match common criteria (Microsoft Dataverse) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "This sample shows how to delete records in bulk that match common criteria" # 115-145 characters including spaces. This abstract displays in the search result.
ms.custom: ""
ms.date: 10/31/2018
ms.reviewer: "pehecke"
ms.service: powerapps
ms.topic: "article"
author: "JimDaly" # GitHub ID
ms.author: "jdaly" # MSFT alias of Microsoft employees only
manager: "ryjones" # MSFT alias of manager or PM counterpart
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---
# Sample: Bulk delete records that match common criteria

[!INCLUDE[cc-data-platform-banner](../../../../includes/cc-data-platform-banner.md)]

This sample shows how to delete records, in bulk, that match common criteria. You can download the sample from [here](https://github.com/Microsoft/PowerApps-Samples/tree/master/cds/orgsvc/C%23/BulkDeleteMatchCriteria).

[!INCLUDE[cc-terminology](../../includes/cc-terminology.md)]

## How to run this sample

[!include[cc-how-to-run-samples](../../includes/cc-how-to-run-samples.md)]

## What this sample does

The `BulkDeleteRequest` message is intended to be used in a scenario where it contains data that is needed to create the bulk delete request.

## How this sample works

In order to simulate the scenario described in [What this sample does](#what-this-sample-does), the sample will do the following:

### Setup

1. Checks for the current version of the org.
2. Creates an sample account record.
3. Queries for a system user to send an email to, after the bulk delete operation completes.
4. The `BulkDeleteRequest` creates the bulk delete process and set the request properties.
5. The `InspectBulkDeleteOperation` method inspects and display the information about the created `BulkDeleteOperation`.
6. The `RetrieveBulkDeleteOperation` method retrieves the `BulkDeleteOperation`.

### Demonstrate

1. Checks whether the standard email templates are present.
1. The `PerformBulkDelete` method performs the main bulk delete operation.

### Clean up

Display an option to delete the sample data that is created in [Setup](#setup). The deletion is optional in case you want to examine the tables and data created by the sample. You can manually delete the records to achieve the same result.


[!INCLUDE[footer-include](../../../../includes/footer-banner.md)]