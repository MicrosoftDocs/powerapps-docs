---
title: "Sample: Rollup records related to a specific record (Microsoft Dataverse) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "This sample showcases how to rollup records related to specified record." # 115-145 characters including spaces. This abstract displays in the search result.
ms.date: 04/03/2022
author: JimDaly #TODO: No Owner
ms.author: jdaly
ms.reviewer: pehecke
ms.topic: sample
search.audienceType:
  - developer
contributors:
  - JimDaly
  - phecke
---

# Sample: Rollup records related to a specific record

This sample shows how to roll up opportunities by the parent account.

> [!div class="nextstepaction"]
> [SDK for .NET: Rollup records related to a specific record sample code](https://github.com/microsoft/PowerApps-Samples/tree/master/dataverse/orgsvc/CSharp/RollupSpecificRecords)

## How to run this sample

[!include[cc-how-to-run-samples](../../includes/cc-how-to-run-samples.md)]

## What this sample does

The `RollupRequest` message is intended to be used in a scenario where it contains data that is needed to create a roll up request.

## How this sample works

In order to simulate the scenario described in [What this sample does](#what-this-sample-does), the sample will do the following:

### Setup

1. Checks for the current version of the org.
2. Creates sample account and opportunity records.

### Demonstrate

1. The `QueryExpression` queries the opportunities by parent account.
2. The `RollupRequest` creates the roll up request.

### Clean up

Display an option to delete the records in [Setup](#setup). The deletion is optional in case you want to examine the table and data created by the sample. You can manually delete the records to achieve the same result.

[!INCLUDE[footer-include](../../../../includes/footer-banner.md)]
