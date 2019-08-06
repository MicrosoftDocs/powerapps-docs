---
title: "OnPreProcessStatusChange Event (Client API reference) in Dynamics 365 for Customer Engagement| MicrosoftDocs"
ms.date: 06/30/2019
ms.service: crm-online
ms.topic: reference
applies_to: Dynamics 365 for Customer Engagement (online)
ms.assetid: 
author: MSFTMan
ms.author: Deonhe
manager: KVivek
search.audienceType: 
  - developer
search.app: 
  - D365CE
---
# OnPreProcessStatusChange Event (Client API reference)

[!INCLUDE[](../../../../../includes/cc_applies_to_update_9_0_0.md)]

This event occurs **before** the status of a process instance changes. 

Use the **formContext.data.process**.[addOnPreProcessStatusChange](../formContext-data-process/eventhandlers/addOnPreProcessStatusChange.md) method to add event handlers for this event and the **formContext.data.process**.[removeOnPreProcessStatusChange](../formContext-data-process/eventhandlers/removeOnPreProcessStatusChange.md) method to remove them. 

From within a web resource script registered to the onPreStageChange event, a developer can invoke the following on the executionContext object passed into the web resource script: 

`executionContext.getEventArgs().preventDefault();` 
