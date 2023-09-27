---
title: "Sample: Bulk delete records in bulk that match common criteria (Microsoft Dataverse) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "This sample shows how to delete records in bulk that match common criteria" # 115-145 characters including spaces. This abstract displays in the search result.
ms.date: 04/03/2022
author: JimDaly
ms.author: jdaly
ms.reviewer: pehecke
ms.topic: sample
search.audienceType:
  - developer
contributors:
  - JimDaly
  - phecke
---

# Sample: Bulk delete records that match common criteria

This sample shows how to delete records, in bulk, that match common criteria.

> [!div class="nextstepaction"]
> [SDK for .NET: Bulk delete records that match common criteria sample code](https://github.com/microsoft/PowerApps-Samples/tree/master/dataverse/orgsvc/C%23/BulkDeleteMatchCriteria)

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
