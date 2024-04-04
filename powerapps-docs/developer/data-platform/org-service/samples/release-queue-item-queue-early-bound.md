---
title: "Sample: Release a queue item to the queue (Microsoft Dataverse) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "This sample shows how to use ReleaseToQueueRequest message" # 115-145 characters including spaces. This abstract displays in the search result.
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

# Sample: Release a queue item to the queue

This sample shows how to use [ReleaseToQueueRequest](/dotnet/api/microsoft.crm.sdk.messages.releasetoqueuerequest) to dissociate a user from a queue item that they worked on and release a queue item back to the queue.

> [!div class="nextstepaction"]
> [SDK for .NET: Release a queue item to the queue sample code](https://github.com/microsoft/PowerApps-Samples/tree/master/dataverse/orgsvc/C%23/ReleaseQueueItems)

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

The `ReleaseToQueueRequest` message removes worker from queue item to release queued object from worker's queue.

### Clean up

Display an option to delete the sample data created in [Setup](#setup). The deletion is optional in case you want to examine the tables and data created by the sample. You can manually delete the records to achieve the same result.

[!INCLUDE[footer-include](../../../../includes/footer-banner.md)]
