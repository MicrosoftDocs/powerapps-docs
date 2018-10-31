---
title: "Sample: Clean up history for a queue (Common Data Service for Apps) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "This sample shows how to clean up history for a queue" # 115-145 characters including spaces. This abstract displays in the search result.
ms.custom: ""
ms.date: 08/01/2018
ms.reviewer: ""
ms.service: "powerapps"
ms.topic: "article"
author: "brandonsimons" # GitHub ID
ms.author: "jdaly" # MSFT alias of Microsoft employees only
manager: "ryjones" # MSFT alias of manager or PM counterpart
---
# Sample: Clean up history for a queue

<!-- https://docs.microsoft.com/en-us/dynamics365/customer-engagement/developer/sample-clean-up-history-queue-early-bound -->

 This sample shows how to clean up the history for the queue by using [RemoveFromQueueRequest](https://docs.microsoft.com/en-us/dotnet/api/microsoft.crm.sdk.messages.removefromqueuerequest?view=dynamics-general-ce-9) with inactive items. It finds completed phone calls in the queue and removes the associated queue items. You can download the sample from [here](https://github.com/Microsoft/PowerApps-Samples/tree/master/cds/orgsvc/C%23/CleanHistoryQueue).

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

1. Retrieves the queueitem with inactive phone calls from a queue using the [RemoveFromQueueRequest](https://docs.microsoft.com/en-us/dotnet/api/microsoft.crm.sdk.messages.removefromqueuerequest?view=dynamics-general-ce-9) message.

### Clean up

1. Display an option to delete the records created in [Setup](#setup).

    The deletion is optional in case you want to examine the entities and data created by the sample. You can manually delete the records to achieve the same result.
