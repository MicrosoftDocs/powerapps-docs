---
title: "Sample: Two-way listener (Common Data Service for Apps) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "This sample shows how to write a Azure Service Bus Listener for a two-way endpoint contract." # 115-145 characters including spaces. This abstract displays in the search result.
ms.custom: ""
ms.date: 10/31/2018
ms.reviewer: ""
ms.service: "powerapps"
ms.topic: "samples"
author: "brandonsimons" # GitHub ID
ms.author: "jdaly" # MSFT alias of Microsoft employees only
manager: "ryjones" # MSFT alias of manager or PM counterpart
---
# Sample: Two-way listener

<!-- https://docs.microsoft.com/en-us/dynamics365/customer-engagement/developer/sample-two-way-listener -->

This sample shows how to write a `Azure Service Bus` Listener for a two-way endpoint contract. You can download the sample from [here](https://github.com/Microsoft/PowerApps-Samples/tree/master/cds/orgsvc/C%23/TwoWayListener).

This sample registers a remote service plug-in that executes whenever a message is posted to a two-way endpoint on the `Azure Service Bus`. When the plug-in executes, it prints to the console the contents of the execution context contained in the message.
