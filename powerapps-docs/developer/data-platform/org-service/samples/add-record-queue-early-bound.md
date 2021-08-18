---
title: "Sample: Add a record to queue (Microsoft Dataverse) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "This sample shows how to add a record to a queue." # 115-145 characters including spaces. This abstract displays in the search result.
ms.custom: ""
ms.date: 06/17/2021
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
# Sample: Add a record to a queue

[!INCLUDE[cc-data-platform-banner](../../../../includes/cc-data-platform-banner.md)]

This sample shows how to add a record to a queue. It creates source and destination queues. It adds a letter activity to the source queue and then moves it to the destination queue. You can download the sample from [here](https://github.com/Microsoft/PowerApps-Samples/tree/master/cds/orgsvc/C%23/RecordToQueue).

[!INCLUDE[cc-terminology](../../includes/cc-terminology.md)]

This sample requires additional users that are not in your system. Create the users manually in **Microsoft 365** in order to run the sample without any errors. For this sample, create a user profile **as is** shown below. 

**First Name**: Kevin<br/>
**Last Name**: Cook<br/>
**Security Role**: Sales Manager<br/>
**UserName**: kcook@yourorg.onmicrosoft.com<br/>

## How to run this sample

[!include[cc-how-to-run-samples](../../includes/cc-how-to-run-samples.md)]

## What this sample does

The `AddToQueueRequest` message is intended to be used in a scenario where it contains data that is needed to move a table record from a source queue to destination queue.

## How this sample works

In order to simulate the scenario described in [What this sample does](#what-this-sample-does), the sample will do the following:

### Setup

1. Checks for the current version of the org.
2. The `Queue` method creates source and destination queues and store their returned GUIDs in variable.
3. Creates a Letter table.
4. The `AddToQueueRequest` method adds a table record into a queue, in this sample it associates the letter with first queue.
5. Retrieves the user created manually in **Microsoft 365** for assigning the queue items to the user's queue.

### Demonstrate

1. The `RetrieveUserQueueRequest` message retrieves the known private queues for the user.
2. The `AddToQueueRequest` message adds the record from a source queue to destination queue.

### Clean up

Display an option to delete the sample data that is created in [Setup](#setup). The deletion is optional in case you want to examine the tables and data created by the sample. You can manually delete the records to achieve the same result.


[!INCLUDE[footer-include](../../../../includes/footer-banner.md)]