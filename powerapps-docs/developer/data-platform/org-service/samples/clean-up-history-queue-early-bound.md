---
title: "Sample: Clean up history for a queue (Microsoft Dataverse) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "This sample shows how to clean up history for a queue" # 115-145 characters including spaces. This abstract displays in the search result.
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

# Sample: Clean up history for a queue

This sample shows how to clean up the history for the queue by using [RemoveFromQueueRequest](/dotnet/api/microsoft.crm.sdk.messages.removefromqueuerequest) with inactive items. It finds completed phone calls in the queue and removes the associated queue items.

> [!div class="nextstepaction"]
> [SDK for .NET: Clean up history for a queue sample code](https://github.com/microsoft/PowerApps-Samples/tree/master/dataverse/orgsvc/C%23/CleanHistoryQueue)

[!INCLUDE[cc-terminology](../../includes/cc-terminology.md)]

## How to run this sample

[!include[cc-how-to-run-samples](../../includes/cc-how-to-run-samples.md)]

## What this sample does

The `RemoveFromQueueRequest` message is intended to be used in a scenario to clean up the queue history with inactive items.

## How this sample works

In order to simulate the scenario described in [What this sample does](#what-this-sample-does), the sample will do the following:

### Setup

1. Checks for the current version of the org.
2. Creates a queue instance and set its property values.
3. Creates a phone call activity instance and also queueitems instance and initializes its properties.
4. Marks the phone call as completed.

### Demonstrate

Retrieves the queueitem with inactive phone calls from a queue using the [RemoveFromQueueRequest](/dotnet/api/microsoft.crm.sdk.messages.removefromqueuerequest) message.

### Clean up

Display an option to delete the records created in [Setup](#setup). The deletion is optional in case you want to examine the tables and data created by the sample. You can manually delete the records to achieve the same result.

[!INCLUDE[footer-include](../../../../includes/footer-banner.md)]
