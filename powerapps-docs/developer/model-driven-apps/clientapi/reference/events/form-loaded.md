---
title: "Form Loaded event (Client API reference) in model-driven apps "
description: Includes description and supported parameters for the Loaded event.
author: MitiJ
ms.author: mijosh
ms.date: 07/02/2024
ms.reviewer: jdaly
ms.topic: reference
applies_to: "Dynamics 365 (online)"
search.audienceType: 
  - developer
contributors:
  - JimDaly
---
# Form Loaded event

This event occurs after the form load completes. App logic that isn't immediately needed during the form load process should be run after load completes. For example, moving extra APIs calls after form load completes can significantly improve the loading experience and reduce time to first use.
 
Use the formContext.ui.[addLoaded](../formContext-ui/addLoaded.md) and formContext.ui.[removeLoaded](../formContext-ui/removeLoaded.md) methods to manage event handlers for this event. 

## Related articles

[Events (Client API reference)](../events.md)   
[Events in forms and grids in model-driven apps](../../events-forms-grids.md)

[!INCLUDE[footer-include](../../../../../includes/footer-banner.md)]
