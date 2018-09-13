---
title: "Sample: Bulk delete records in bulk that match common criteria (Common Data Service for Apps) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "This sample shows how to delete records in bulk that match common criteria" # 115-145 characters including spaces. This abstract displays in the search result.
ms.custom: ""
ms.date: 08/01/2018
ms.reviewer: ""
ms.service: "powerapps"
ms.topic: "article"
author: "brandonsimons" # GitHub ID
ms.author: "jdaly" # MSFT alias of Microsoft employees only
manager: "ryjones" # MSFT alias of manager or PM counterpart
---
# Sample: Bulk delete records that match common criteria

<!-- https://docs.microsoft.com/en-us/dynamics365/customer-engagement/developer/sample-bulk-delete-records-match-common-criteria -->

This sample shows how to delete records, in bulk, that match common criteria.

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
3. The `BulkDeleteRequest` creates the bulk delete process and set the request properties.
4. The `InspectBulkDeleteOperation` method inspects and display the information abou the created `BulkDeleteOperation`.
5. The `RetrieveBulkDeleteOperation` method retrieves the `BulkDeleteOperation`.

### Demonstrate
1. Checks whether the standard email templates are present.
1. The `PerformBulkDelete` method performs the main bulk delete operation.

### Clean up

1. Display an option to delete the sample data that is creatd in [Setup](#setup).

    The deletion is optional in case you want to examine the entities and data created by the sample. You can manually delete the records to achieve the same result.
