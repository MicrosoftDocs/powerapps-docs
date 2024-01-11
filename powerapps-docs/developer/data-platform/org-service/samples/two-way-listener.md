---
title: "Sample: Two-way listener (Microsoft Dataverse) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "This sample shows how to write a Azure Service Bus Listener for a two-way endpoint contract." # 115-145 characters including spaces. This abstract displays in the search result.
ms.date: 04/03/2022
author: jaredha
ms.author: jaredha
ms.reviewer: jdaly
ms.topic: sample
search.audienceType:
  - developer
contributors:
  - JimDaly
  - phecke
---

# Sample: Two-way listener

This sample shows how to write a `Azure Service Bus` Listener for a two-way endpoint contract.

> [!div class="nextstepaction"]
> [SDK for .NET: Two-way listener sample code](https://github.com/microsoft/PowerApps-Samples/tree/master/dataverse/orgsvc/C%23/TwoWayListener)

This sample registers a remote service plug-in that executes whenever a message is posted to a two-way endpoint on the `Azure Service Bus`. When the plug-in executes, it prints to the console the contents of the execution context contained in the message.

[!INCLUDE[footer-include](../../../../includes/footer-banner.md)]
