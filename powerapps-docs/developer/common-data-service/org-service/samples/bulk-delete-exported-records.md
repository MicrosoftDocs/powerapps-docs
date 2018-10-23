---
title: "Sample: Bulk delete exported records (Common Data Service for Apps) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "This sample shows how to perform a bulk deletion of records" # 115-145 characters including spaces. This abstract displays in the search result.
ms.custom: ""
ms.date: 08/01/2018
ms.reviewer: ""
ms.service: "powerapps"
ms.topic: "article"
author: "brandonsimons" # GitHub ID
ms.author: "jdaly" # MSFT alias of Microsoft employees only
manager: "ryjones" # MSFT alias of manager or PM counterpart
---
# Sample: Bulk delete exported records

This sample shows how to perform a bulk deletion of records that were previously exported from Common Data Service for Apps by using the **Export to Excel** option.

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

1. The `PerformBulkDeleteBackup` method performs the main bulk delete operation on inactive opportunities and activities to remove them from the system.

### Clean up

1. Display an option to delete the sample data that is created in [Setup](#setup).

    The deletion is optional in case you want to examine the entities and data created by the sample. You can manually delete the records to achieve the same result.
