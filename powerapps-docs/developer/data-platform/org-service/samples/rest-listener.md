---
title: "Sample: Rest listener (Microsoft Dataverse) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "This sample shows how to write a Azure Service Bus Listener for a REST endpoint contract." # 115-145 characters including spaces. This abstract displays in the search result.
ms.date: 04/03/2022
author: jaredha
ms.author: jaredha
ms.reviewer: jdaly
ms.topic: sample
search.audienceType:
  - developer
---

# Sample: REST listener

This sample shows how to write a `Azure Service Bus` Listener for a `REST` endpoint contract.

> [!div class="nextstepaction"]
> [SDK for .NET: REST listener sample code](https://github.com/microsoft/PowerApps-Samples/tree/master/dataverse/orgsvc/C%23/RESTListener)

This sample registers a remote service plug-in that executes whenever a message is posted to a `REST` endpoint on the service bus. When the plug-in executes, it prints to the console the contents of the execution context contained in the message.

[!INCLUDE[footer-include](../../../../includes/footer-banner.md)]
