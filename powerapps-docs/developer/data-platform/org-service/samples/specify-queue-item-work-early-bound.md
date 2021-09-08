---
title: "Sample: Specify a queue item to work on(Microsoft Dataverse) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "This sample shows how to specify a user who will work on a queue item" # 115-145 characters including spaces. This abstract displays in the search result.
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
# Sample: Specify a queue item to work on

[!INCLUDE[cc-data-platform-banner](../../../../includes/cc-data-platform-banner.md)]

<!-- https://docs.microsoft.com/dynamics365/customer-engagement/developer/sample-specify-queue-item-work-early-bound -->

This sample shows how to use [PickFromQueueRequest](/dotnet/api/microsoft.crm.sdk.messages.pickfromqueuerequest?view=dynamics-general-ce-9) to specify a user who will work on a queue item. You can download the sample from [here](https://github.com/Microsoft/PowerApps-Samples/tree/master/cds/orgsvc/C%23/SpecifyQueueItem).

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