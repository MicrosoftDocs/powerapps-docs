---
title: "onPreProcessStatusChange event (Client API reference) in model-driven apps"
description: Includes description and supported parameters for the onPreProcessStatusChange event.
author: matthidinger
ms.author: mahiding
ms.date: 03/12/2022
ms.reviewer: jdaly
ms.topic: reference
search.audienceType: 
  - developer
contributors:
  - JimDaly
---
# onPreProcessStatusChange event (Client API reference)

[!INCLUDE[](../../../../../includes/cc_applies_to_update_9_0_0.md)]

This event occurs **before** the status of a process instance changes. 

Use the **formContext.data.process**.[addOnPreProcessStatusChange](../formContext-data-process/eventhandlers/addOnPreProcessStatusChange.md) method to add event handlers for this event and the **formContext.data.process**.[removeOnPreProcessStatusChange](../formContext-data-process/eventhandlers/removeOnPreProcessStatusChange.md) method to remove them. 

From within a web resource script registered to the `onPreProcessStatusChange` event, a developer can invoke the following method on the `executionContext` object passed into the web resource script: 

`executionContext.getEventArgs().preventDefault();` 

When you invoke `preventDefault`:

- The state change isn't processed. The process instance remains on the original stage in the original state.
- The save of the main form isn't processed. If the main form was in a dirty state, it would remain in a dirty state.
- Any web resources that registered onProcessStatusChange isn't invoked.

This client API is only supported on the unified client. The legacy web client doesn't support this client API.

## Methods supported for this event

- **`formContext.data.process`**.[addOnPreProcessStatusChange](../formcontext-data-process/eventhandlers/addOnPreProcessStatusChange.md) method to add event handlers for this event.
- **`formContext.data.process`**.[removeOnPreProcessStatusChange](../formcontext-data-process/eventhandlers/removeOnPreProcessStatusChange.md) method to remove event handlers for this event. 

### Related articles

[Events (Client API reference)](../events.md)   
[Events in forms and grids in model-driven apps](../../events-forms-grids.md)

[!INCLUDE[footer-include](../../../../../includes/footer-banner.md)]
