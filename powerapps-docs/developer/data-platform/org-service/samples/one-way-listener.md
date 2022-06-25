---
title: "Sample: One-way listener (Microsoft Dataverse) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "This sample shows how the application registers a remote service plugin that executes whenever  a message is posted to one-way endpoint." # 115-145 characters including spaces. This abstract displays in the search result.
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
# Sample: One-way listener

This sample shows how to write a `Azure Service Bus` listener for a one-way endpoint contract. You can download the sample from [here](https://github.com/Microsoft/PowerApps-Samples/tree/master/cds/orgsvc/C%23/OneWayListeners).

This sample listener application registers a remote service plug-in that executes whenever a message is posted to a one-way endpoint on the `Azure Service Bus`. When the plug-in executes, it outputs to the console the contents of the execution context contained in the message. 


[!INCLUDE[footer-include](../../../../includes/footer-banner.md)]
