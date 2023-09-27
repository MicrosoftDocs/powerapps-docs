---
title: "Sample: Bulk delete exported records (Microsoft Dataverse) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "This sample shows how to perform a bulk deletion of records" # 115-145 characters including spaces. This abstract displays in the search result.
ms.date: 04/03/2022
author: JimDaly #TODO: NoOwner
ms.author: jdaly
ms.reviewer: pehecke
ms.topic: sample
search.audienceType:
  - developer
---

# Sample: Bulk delete exported records

This sample shows how to perform a bulk deletion of records that were previously exported from Microsoft Dataverse by using the **Export to Excel** option.

> [!div class="nextstepaction"]
> [SDK for .NET: Bulk delete exported records sample code](https://github.com/microsoft/PowerApps-Samples/tree/master/dataverse/orgsvc/C%23/BulkDeleteExported)

[!INCLUDE[cc-terminology](../../includes/cc-terminology.md)]

## How to run this sample

[!include[cc-how-to-run-samples](../../includes/cc-how-to-run-samples.md)]

## What this sample does

The `BulkDeleteRequest` message is intended to be used in a scenario where it contains data that is needed to create the bulk delete request.

## How this sample works

In order to simulate the scenario described in [What this sample does](#what-this-sample-does), the sample will do the following:

### Setup

1. Checks for the current version of the org.
2. Query for a system user to send an email after bulk delete request operation completes.
3. The `BulkDeleteRequest` creates the bulk delete process and set the request properties.
4. The `CheckSuccess` method queries for the `BulkDeleteOperation` until it has been completed or until the designated time runs out. It then checks to see if the operation is complete.

### Demonstrate

The `PerformBulkDeleteBackup` method performs the main bulk delete operation on inactive opportunities and activities to remove them from the system.

### Clean up

Display an option to delete the sample data that is created in [Setup](#setup). The deletion is optional in case you want to examine the tables and data created by the sample. You can manually delete the records to achieve the same result.

[!INCLUDE[footer-include](../../../../includes/footer-banner.md)]
