---
title: "Sample: Insert or update record using Upsert (Common Data Service for Apps) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "This sample shows how to insert or update records using the Upsert message." # 115-145 characters including spaces. This abstract displays in the search result.
ms.custom: ""
ms.date: 08/01/2018
ms.reviewer: ""
ms.service: "powerapps"
ms.topic: "samples"
author: "brandonsimons" # GitHub ID
ms.author: "jdaly" # MSFT alias of Microsoft employees only
manager: "ryjones" # MSFT alias of manager or PM counterpart
---
# Sample: Insert or update a record using Upsert

<!-- https://docs.microsoft.com/en-us/dynamics365/customer-engagement/developer/sample-insert-update-record-upsert -->

This sample code shows how to insert or update records by using the [UpsertRequest](https://docs.microsoft.com/en-us/dotnet/api/microsoft.xrm.sdk.messages.upsertrequest?view=dynamics-general-ce-9) message.

## How to run this sample

[!include[cc-how-to-run-samples](../../includes/cc-how-to-run-samples.md)]

## What this sample does

The `UpsertRequest` message is intended to be used in a scenario where it contains data that is needed to update or insert a record.

## How this sample works

In order to simulate the scenario described in [What this sample does](#what-this-sample-does), the sample will do the following:

### Setup

1. Checks the current version of the org.
1. 

### Demonstrate

1. Creates the appointment instance using the [BookRequest](https://docs.microsoft.com/en-us/dotnet/api/microsoft.crm.sdk.messages.bookrequest?view=dynamics-general-ce-9) message and verifies that the appointment has been scheduled or not.

### Clean up

1. Display an option to delete the records created in the [Setup](#setup).

    The deletion is optional in case you want to examine the entities and data created by the sample. You can manually delete the records to achieve the same result.
