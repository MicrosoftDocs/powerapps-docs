---
title: "Sample: Release a queue item to the queue (Common Data Service for Apps) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "This sample shows how to use ReleaseToQueueRequest message" # 115-145 characters including spaces. This abstract displays in the search result.
ms.custom: ""
ms.date: 08/01/2018
ms.reviewer: ""
ms.service: "powerapps"
ms.topic: "samples"
author: "brandonsimons" # GitHub ID
ms.author: "jdaly" # MSFT alias of Microsoft employees only
manager: "ryjones" # MSFT alias of manager or PM counterpart
---
# Sample: Release a queue item to the queue

<!-- https://docs.microsoft.com/en-us/dynamics365/customer-engagement/developer/sample-release-queue-item-queue-early-bound
Couldn't each of the operations in this series of samples be added to just one sample?
 -->
 This sample shows how to use [ReleaseToQueueRequest](https://docs.microsoft.com/en-us/dotnet/api/microsoft.crm.sdk.messages.releasetoqueuerequest?view=dynamics-general-ce-9) to dissociate a user from a queue item that he or she worked on and release a queue item back to the queue.

## How to run this sample

[!include[cc-how-to-run-samples](../../includes/cc-how-to-run-samples.md)]

## What this sample does

The `ReleaseToQueueRequest` message is intended to be used in a scenario where it contains data that is needed to assign a queue item back to the queue owner so others can pick it.

## How this sample works

In order to simulate the scenario described in [What this sample does](#what-this-sample-does), the sample will do the following:

### Setup

1. Checks for the current version of the org.
2. The `Queue` message creates a new queue and store its returned GUIDs in a variable.
3. The `QueueItem` message creates a new instance of a queueitem and initialize its properties.
4. The `WhoAMIRequest` retrieves the current user's information.

### Demonstrate

1. The `ReleaseToQueueRequest` message removes worker from queue item to release queued object from worker's queue.

### Clean up

1. Display an option to delete the sample data created in [Setup](#setup).

    The deletion is optional in case you want to examine the entities and data created by the sample. You can manually delete the records to achieve the same result.
