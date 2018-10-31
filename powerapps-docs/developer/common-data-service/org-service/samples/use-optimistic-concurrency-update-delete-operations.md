---
title: "Sample: Use optimistic concurrency with update and delete operations (Common Data Service for Apps) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "This sample shows how to use optimistic concurrency for update and delete operations." # 115-145 characters including spaces. This abstract displays in the search result.
ms.custom: ""
ms.date: 10/31/2018
ms.reviewer: ""
ms.service: "powerapps"
ms.topic: "samples"
author: "brandonsimons" # GitHub ID
ms.author: "jdaly" # MSFT alias of Microsoft employees only
manager: "ryjones" # MSFT alias of manager or PM counterpart
---
# Sample: Use optimistic concurrency with update and delete operations

<!-- https://docs.microsoft.com/en-us/dynamics365/customer-engagement/developer/org-service/sample-use-optimistic-concurrency-update-delete-operations -->

This sample shows how to use optimistic concurrency for update and delete operations. You can download the sample from [here](https://github.com/Microsoft/PowerApps-Samples/tree/master/cds/orgsvc/C%23/OptimisticConcurrency).

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
1. Updates the account record by increasing the `creditlimit` attribute.
1. The `UpdateRequest` method sets the request's concurrency behaviour to check for a row version match.

### Clean up

1. Displays an option to delete all the data created in the sample.

The deletion is optional in case you want to examine the data created by the sample. You can manually delete the data to achieve same results.
