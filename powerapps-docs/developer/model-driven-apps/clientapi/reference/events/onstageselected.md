---
title: "OnStageSelected event (Client API reference) in model-driven apps| MicrosoftDocs"
description: Includes description and supported parameters for the OnStageSelected event.
ms.date: 04/19/2021
ms.service: powerapps
ms.topic: "reference"
applies_to: "Dynamics 365 (online)"
ms.assetid: 1ef0f11c-6188-4492-ae61-260a402223b8
author: "Nkrb"
ms.author: "nabuthuk"
manager: "kvivek"
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---
# OnStageSelected event (Client API reference)

This event occurs when a stage of a business process flow control is selected. You can’t cancel the stage selection using code in a handler for this event.

> [!NOTE]
> The chevron arrow buttons in the business process flow bar can be used to move through and view all the stages. However, these forward and backward chevron buttons do not select the stage and do not change the active stage. Therefore, OnStageSelected event does not occur while navigating and viewing stages when using the chevron arrow buttons.

You can use the [getEventArgs](../executioncontext/getEventArgs.md) method to retrieve an object that has the following method:

**getStage**: Returns a stage object representing the selected stage. More information: [Stage methods](../formContext-data-process.md#stage-methods).

## Methods supported for this event

- **formContext.data.process**.[addOnStageSelected](../formcontext-data-process/eventhandlers/addOnStageSelected.md) method to add event handlers for this event.
- **formContext.data.process**.[removeOnStageSelected](../formcontext-data-process/eventhandlers/addOnStageSelected.md) method to remove event handlers for this event. 





[!INCLUDE[footer-include](../../../../../includes/footer-banner.md)]