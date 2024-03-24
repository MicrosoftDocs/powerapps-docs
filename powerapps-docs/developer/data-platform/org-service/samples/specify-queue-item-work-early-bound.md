---
title: "Sample: Specify a queue item to work on (Microsoft Dataverse) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "This sample shows how to specify a user who will work on a queue item" # 115-145 characters including spaces. This abstract displays in the search result.
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

# Sample: Specify a queue item to work on

This sample shows how to use [PickFromQueueRequest](/dotnet/api/microsoft.crm.sdk.messages.pickfromqueuerequest) to specify a user who will work on a queue item.

> [!div class="nextstepaction"]
> [SDK for .NET: Specify a queue item to work on sample code](https://github.com/microsoft/PowerApps-Samples/tree/master/dataverse/orgsvc/C%23/SpecifyQueueItem)

## How to run this sample

[!include[cc-how-to-run-samples](../../includes/cc-how-to-run-samples.md)]

## What this sample does

The `PickFromQueueRequest` message is intended to be used in a scenario where it contains data that is needed to assign a queue item to a user and optionally remove the queue item from the queue.

## How this sample works

In order to simulate the scenario described in [What this sample does](#what-this-sample-does), the sample will do the following:

### Setup

1. Checks for the current version of the org.
2. The `Queue` method creates a private queue instance and set its property values.
3. The `QueueItem` method creates a new instance of queueitem and initialize its properties.

### Demonstrate

1. The `WhoAmIRequest` method retrieves the current user information.
1. The `PickFromQueueRequest` method creates an instance of an existing queueitem in order to specify the user that will be working on it.

### Clean up

Display an option to delete the sample data that is created in [Setup](#setup). The deletion is optional in case you want to examine the tables and data created by the sample. You can manually delete the records to achieve the same result.

[!INCLUDE[footer-include](../../../../includes/footer-banner.md)]
