---
title: "Sample: Detect Multiple duplicate records(Common Data Service for Apps) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "This sample shows how to detect and log multiple duplicate records for a specified entity type." # 115-145 characters including spaces. This abstract displays in the search result.
ms.custom: ""
ms.date: 08/01/2018
ms.reviewer: ""
ms.service: "powerapps"
ms.topic: "samples"
author: "brandonsimons" # GitHub ID
ms.author: "jdaly" # MSFT alias of Microsoft employees only
manager: "ryjones" # MSFT alias of manager or PM counterpart
---
# Sample: Detect multiple duplicate records

This sample shows how to detect and log multiple duplicate records for a specified entity type.

## How to run this sample

[!include[cc-how-to-run-samples](../../includes/cc-how-to-run-samples.md)]

## What this sample does

The `BulkDetectDuplicatesRequest` message is intended to be used in a scenario that contains data that is needed to submit an asynchronous system job that detects and logs multiple duplicate records. You can download the sample from [here](https://github.com/Microsoft/PowerApps-Samples/tree/master/cds/orgsvc/C%23/DetectMultipleDuplicateRecords).

## How this sample works

In order to simulate the scenario described in [What this sample does](#what-this-sample-does), the sample will do the following:

### Setup

1. Checks for the current version of the org.
1. The `CreateRequiredRecords` class creates some duplicate entity records for the sample.
1. The `DuplicateRule` method creates a duplicate detection rule.
1. The  `DuplicateRuleCondition` method creates a duplicate detection rule condition for detecting duplicate records.
1. The `PublishDuplicateRuleRequest` method publishes the duplicate detection rule.
1. The `PublishDuplicateRuleRequest` returns before the publish is completed, so we keep retrieving the async job state until it is `Completed`

### Demonstrate

1. The `BulkDetectDuplicatesRequest` method creates the BulkDetectDuplicatesRequest object

### Clean up

1. Display an option to delete the records created in the [Setup](#setup).

    The deletion is optional in case you want to examine the entities and data created by the sample. You can manually delete the records to achieve the same result.

