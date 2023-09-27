---
title: "Sample: Use optimistic concurrency with update and delete operations (Microsoft Dataverse) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "This sample shows how to use optimistic concurrency for update and delete operations." # 115-145 characters including spaces. This abstract displays in the search result.
ms.date: 04/03/2022
author: divkamath
ms.author: dikamath
ms.reviewer: pehecke
ms.topic: sample
search.audienceType:
  - developer
contributors:
  - JimDaly
  - phecke
---

# Sample: Use optimistic concurrency with update and delete operations

This sample shows how to use optimistic concurrency for update and delete operations.

> [!div class="nextstepaction"]
> [SDK for .NET: Use optimistic concurrency with update and delete operations sample code](https://github.com/microsoft/PowerApps-Samples/tree/master/dataverse/orgsvc/C%23/OptimisticConcurrency)

## How to run this sample

[!include[cc-how-to-run-samples](../../includes/cc-how-to-run-samples.md)]

## What this sample does

The `UpdateRequest` class is intended to be used in a scenario where it contains data that is needed to update an existing record.

## How this sample works

In order to simulate the scenario described in [What this sample does](#what-this-sample-does), the sample will do the following:

### Setup

1. Checks for the current version of the org.
1. The `Account` method creates an account record.

### Demonstrate

1. Retrieves the account record that is created in the [Setup](#setup).
1. Updates the account record by increasing the `creditlimit` column.
1. The `UpdateRequest` method sets the request's concurrency behavior to check for a row version match.

### Clean up

Displays an option to delete all the data created in the sample. The deletion is optional in case you want to examine the data created by the sample. You can manually delete the data to achieve same results.

[!INCLUDE[footer-include](../../../../includes/footer-banner.md)]
