---
title: "Sample: Persistent queue listener (Microsoft Dataverse) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "This sample shows how to write a Azure Service Bus listener application for a persistent queue endpoint contract." # 115-145 characters including spaces. This abstract displays in the search result.
ms.date: 04/03/2022
author: jaredha
ms.author: jaredha
manager: sunilg
ms.reviewer: jdaly
ms.topic: sample
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
contributors:
 - JimDaly
 - phecke
---
# Sample: Persistent queue listener

This sample shows how to write a Azure Service Bus listener application for a persistent queue endpoint contract. You can download the sample from [here](https://github.com/Microsoft/PowerApps-Samples/tree/master/cds/orgsvc/C%23/PersistentQueueListener).

The listener waits for a message to be posted to the service bus and to be available in the endpoint queue. When a message is available in the queue, the listener reads the message, prints the execution context contained in the message to the console, and deletes the message from the queue.


[!INCLUDE[footer-include](../../../../includes/footer-banner.md)]
