---
title: "Sample: Work with activity party records (Microsoft Dataverse) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "This sample shows how to work with activity party records" # 115-145 characters including spaces. This abstract displays in the search result.
ms.date: 04/06/2022
author: mayadumesh
ms.author: mayadu
ms.reviewer: pehecke
ms.topic: sample
search.audienceType:
  - developer
contributors:
  - JimDaly
  - phecke
---

# Sample: Work with activity party records

This sample code shows how to work with activity party records.

> [!div class="nextstepaction"]
> [SDK for .NET: Work with activity party records sample code](https://github.com/microsoft/PowerApps-Samples/tree/master/dataverse/orgsvc/C%23/ActivityPartyRecords)

## How to run this sample

[!include[cc-how-to-run-samples](../../includes/cc-how-to-run-samples.md)]

## What this sample does

This sample creates some sample data, to work with activity party records.

## How this sample works

In order to simulate the scenario described in [What this sample does](#what-this-sample-does), the sample will do the following:

### Setup

1. Checks for the current version of the org.
1. Creates three contact records which are required for this sample.

### Demonstrate

1. Retrieves the contact records that are created in the [Setup](#setup).
2. Creates the activity party records for each contact.
3. Also creates Letter activity and set **From** and **To** columns to the respective Activity Party tables.

### Clean up

Display an option to delete the records created during [Setup](#setup). The deletion is optional in case you want to examine the tables and data created by the sample. You can manually delete the records to achieve the same result.

[!INCLUDE[footer-include](../../../../includes/footer-banner.md)]
