---
title: "OnStageChange Event (Client API reference) in model-driven apps| MicrosoftDocs"
description: This event occurs when the stage of a business process flow control changes.
ms.date: 04/15/2021
ms.service: powerapps
ms.topic: "reference"
applies_to: "Dynamics 365 (online)"
ms.assetid: 0c85fe34-1368-4d0d-87eb-4109206ce4f7
author: "Nkrb"
ms.author: "nabuthuk"
manager: "kvivek"
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---
# OnStageChange Event (Client API reference)



This event occurs when the stage of a business process flow control changes. This event occurs when the user clicks the **Next Stage** or **Move to previous stage** buttons in the user interface or when a developer uses the `formContext.data.process.moveNext` or `formContext.data.process.movePrevious` methods. You can’t cancel the stage change using code in a handler for this event.

An execution context object is passed to event handlers for this event. You can use the [getEventArgs](../executioncontext/getEventArgs.md) method to retrieve an object that has the following methods:

- **getDirection**: Returns a string that is either “next” or “previous” to show the direction of the stage change.
- **getStage**: Returns a stage object. Except when the navigation moves to a new table, the stage returned represents the destination stage object,that is, the next active stage. When the navigation moves to a new table, the stage is the stage being navigated from, that is, the previous active stage object. More information: [Stage methods](../formContext-data-process.md#stage-methods).

[!INCLUDE[cc-terminology](../../../../data-platform/includes/cc-terminology.md)]

## Methods supported for this event
- **formContext.data.process**.[addOnStageChange](../formcontext-data-process/eventhandlers/addOnStageChange.md) method to add event handlers for this event.
- **formContext.data.process**.[removeOnStageChange](../formcontext-data-process/eventhandlers/removeOnStageChange.md) method to remove event handlers for this event. 





[!INCLUDE[footer-include](../../../../../includes/footer-banner.md)]