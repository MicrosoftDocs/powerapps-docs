---
title: "OnStageSelected Event (Client API reference) in model-driven apps| MicrosoftDocs"
ms.date: 10/31/2018
ms.service: "crm-online"
ms.topic: "reference"
applies_to: "Dynamics 365 (online)"
ms.assetid: 1ef0f11c-6188-4492-ae61-260a402223b8
author: "KumarVivek"
ms.author: "kvivek"
manager: "amyla"
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---
# OnStageSelected Event (Client API reference)



This event occurs when a stage of a business process flow control is selected. You can’t cancel the stage selection using code in a handler for this event.

You can use the [getEventArgs](../executioncontext/getEventArgs.md) method to retrieve an object that has the following method:

**getStage**: Returns a stage object representing the selected stage. More information: [Stage methods](../formContext-data-process.md#stage-methods).

## Methods supported for this event
- **formContext.data.process**.[addOnStageSelected](../formcontext-data-process/eventhandlers/addOnStageSelected.md) method to add event handlers for this event.
- **formContext.data.process**.[removeOnStageSelected](../formcontext-data-process/eventhandlers/addOnStageSelected.md) method to remove event handlers for this event. 



