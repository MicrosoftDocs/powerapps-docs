---
title: "Sample: Insert or update record using Upsert (Microsoft Dataverse) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "This sample shows how to insert or update records using the Upsert message." # 115-145 characters including spaces. This abstract displays in the search result.
ms.custom: ""
ms.date: 10/31/2018
ms.reviewer: "pehecke"
ms.service: powerapps
ms.topic: "samples"
author: "JimDaly" # GitHub ID
ms.author: "jdaly" # MSFT alias of Microsoft employees only
manager: "ryjones" # MSFT alias of manager or PM counterpart
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---
# Sample: Insert or update a record using Upsert

[!INCLUDE[cc-data-platform-banner](../../../../includes/cc-data-platform-banner.md)]

This sample code shows how to insert or update records by using the [UpsertRequest](/dotnet/api/microsoft.xrm.sdk.messages.upsertrequest?view=dynamics-general-ce-9) message. You can download the sample from [here](https://github.com/Microsoft/PowerApps-Samples/tree/master/cds/orgsvc/C%23/InsertRecordUsingUpsert).

## How to run this sample

[!include[cc-how-to-run-samples](../../includes/cc-how-to-run-samples.md)]

## What this sample does

The `UpsertRequest` message is intended to be used in a scenario where it contains data that is needed to update or insert a record.

## How this sample works

In order to simulate the scenario described in [What this sample does](#what-this-sample-does), the sample will do the following:

### Setup

1. Checks the current version of the org.
1. Import a managed solution (UpsertSample_1_0_0_0_managed.zip) that creates a `sample_product` table that has an alternate key named `sample_productcode`. Verify that the indexes to support the alternate key are active.

### Demonstrate

1. The `ProcessUpsert` method processes data in the `newsampleproduct.xml` to represent new products and creates 13 new records.
1. The second time when the `ProcessUpsert` method is called, it processes data in `updatedsampleproduct.xml` to represent updates to products previously created. 
1. The `UpsertRequest` method creates 6 updated records. 

### Clean up

Display an option to delete the managed solution created in the [Setup](#setup). The deletion is optional in case you want to examine the tables and data created by the sample. You can manually delete the records to achieve the same result.


[!INCLUDE[footer-include](../../../../includes/footer-banner.md)]