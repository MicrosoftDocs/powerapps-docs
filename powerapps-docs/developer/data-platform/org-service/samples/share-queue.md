---
title: " Share a queue (Microsoft Dataverse) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "This sample showcases how to share a queue." # 115-145 characters including spaces. This abstract displays in the search result.
ms.custom: ""
ms.date: 12/20/2019
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

# Share a queue

[!INCLUDE[cc-data-platform-banner](../../../../includes/cc-data-platform-banner.md)]

This sample shows how to give a user or team access to a queue. The [AddPrincipalToQueueRequest](/dotnet/api/microsoft.crm.sdk.messages.addprincipaltoqueuerequest?view=dynamics-general-ce-9) adds the specified principal to the list of queue members. If the passed-in security principal is a team each member of the team is added to the queue.

You can download the sample from [here](https://github.com/microsoft/PowerApps-Samples/tree/master/cds/orgsvc/C%23/ShareQueue).

## How to run this sample

See [How to run this sample](https://github.com/microsoft/PowerApps-Samples/blob/master/cds/README.md) for information about how to run this sample.

## What this sample does

The [AddPrincipalToQueueRequest](/dotnet/api/microsoft.crm.sdk.messages.addprincipaltoqueuerequest?view=dynamics-general-ce-9) message is intended to be used in a scenario where it contains the data to add the specified principal to the list of queue members. If the principal is a team, add each team member to the queue.

## How this sample works

In order to simulate the scenario described in [What this sample does](#what-this-sample-does), the sample will do the following:

### Setup

1. Checks for the current version of the org. 
1. Creates required data that this sample requires.

### Demonstrate

The `AddPrincipalToQueueRequest` message shares a queue to a team.

### Clean up

Displays an option to delete all the data created in the sample. The deletion is optional in case you want to examine the data created by the sample. You can manually delete the data to achieve same results.


[!INCLUDE[footer-include](../../../../includes/footer-banner.md)]