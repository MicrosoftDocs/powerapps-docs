---
title: "Sample: Add a record to queue (Common Data Service for Apps) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "This sample shows how to add a record to a queue." # 115-145 characters including spaces. This abstract displays in the search result.
ms.custom: ""
ms.date: 08/01/2018
ms.reviewer: ""
ms.service: "powerapps"
ms.topic: "samples"
author: "brandonsimons" # GitHub ID
ms.author: "jdaly" # MSFT alias of Microsoft employees only
manager: "ryjones" # MSFT alias of manager or PM counterpart
---
# Sample: Add a record to a queue

<!-- https://docs.microsoft.com/en-us/dynamics365/customer-engagement/developer/sample-add-record-queue-early-bound 
-->

This sample shows how to add a record to a queue. It creates source and destination queues. It adds a letter activity to the source queue and then moves it to the destination queue.

This sample requires additional users that are not in your system. Create the users manually in **Office 365** in order to run the sample without any errors. For this sample create a user profile **as is** shown below. 

**First Name**: Kevin<br/>
**Last Name**: Cook<br/>
**Security Role**: Sales Manager<br/>
**UserName**: kcook@yourorg.onmicrosoft.com<br/>

## How to run this sample

[!include[cc-how-to-run-samples](../../includes/cc-how-to-run-samples.md)]

## What this sample does

The `AddToQueueRequest` message is intended to be used in a scenario where it contains data that is needed to move an entity record from a source queue to destination queue.

## How this sample works

In order to simulate the scenario described in [What this sample does](#what-this-sample-does), the sample will do the following:

### Setup

1. Checks for the current version of the org.
2. The `Queue` method creates source and destination queues and store their returned GUIDs in vatiable.
3. Creates a Letter entity.
4. The `AddToQueueRequest` method adds an entiy record into a queue, in this sample it associates the letter with first queue.
5. Retrieves the user created manually in **Office 365** for assigning the queue items to the user's queue.

### Demonstrate

1. The `RetrieveUserQueueRequest` message retrieves the known private queues for the user.
2. The `AddToQueueRequest` message adds the record from a source queue to destination queue.
### Clean up

1. Display an option to delete the sample data that is created in [Setup](#setup).

    The deletion is optional in case you want to examine the entities and data created by the sample. You can manually delete the records to achieve the same result.
