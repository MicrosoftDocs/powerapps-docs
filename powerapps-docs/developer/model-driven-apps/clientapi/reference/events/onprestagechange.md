---
title: "OnPreStageChange event (Client API reference) in model-driven apps in Power Apps"
description: This event occurs before the stage of a business process flow control changes.
author: MitiJ
ms.author: mijosh
ms.date: 03/12/2022
ms.reviewer: jdaly
ms.topic: reference
search.audienceType: 
  - developer
contributors:
  - JimDaly
---
# OnPreStageChange event (Client API reference)

This event occurs **Before** the stage of a business process flow control changes. This event occurs after the user selects the **Next Stage**, **Move to previous stage** or **Set Active Stage** buttons in the user interface or when a developer uses the `formContext.data.process.moveNext`, `formContext.data.process.movePrevious`, or `formContext.data.process.setActiveStage` methods.

> [!NOTE]
> The OnPreStageChange event is supported only on Unified Interface.

From within a web resource script registered to the onPreStageChange event, a developer can invoke the following on the executionContext object passed into the web resource script: 

`executionContext.getEventArgs().preventDefault();` 

When you invoke `preventDefault`:

- The stage navigation will not be processed. The process instance will remain on the original stage.
- In a cross-table navigation, the form of the table of the destination stage will not open.
- The save of the main form will not be processed. If the main form was in a dirty state, it would remain in a dirty state.
- Any web resources that registered onStageChange will not be invoked.


An execution context object is passed to event handlers for this event. You can use the [getEventArgs](../executioncontext/getEventArgs.md) method to retrieve an object that has the following methods:

- **getDirection**: Returns a string that is either `Next` or `Previous` to show the direction of the stage change.
- **getStage**: Returns a stage object. Except when the navigation moves to a new table, the stage returned represents the destination stage object—that is, the next active stage. When the navigation moves to a new table, the stage is the stage being navigated from—that is, the previous active stage object. More information: [Stage methods](../formContext-data-process.md#stage-methods).

[!INCLUDE[cc-terminology](../../../../data-platform/includes/cc-terminology.md)]

## Methods supported for this event

- **formContext.data.process**.[addOnPreStageChange](../formcontext-data-process/eventhandlers/addOnPreStageChange.md) method to add event handlers for this event.
- **formContext.data.process**.[removeOnPreStageChange](../formcontext-data-process/eventhandlers/removeOnPreStageChange.md) method to remove event handlers for this event. 

### Related articles

[Events (Client API reference)](../events.md)   
[Events in forms and grids in model-driven apps](../../events-forms-grids.md)

[!INCLUDE[footer-include](../../../../../includes/footer-banner.md)]
