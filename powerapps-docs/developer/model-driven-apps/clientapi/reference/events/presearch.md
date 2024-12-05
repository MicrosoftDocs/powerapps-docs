---
title: "Lookup Control PreSearch event (Client API reference) in model-driven apps"
description: Includes description and supported parameters for the PreSearch event.
author: clromano
ms.author: clromano
ms.date: 03/12/2022
ms.reviewer: jdaly
ms.topic: reference
applies_to: "Dynamics 365 (online)"
search.audienceType: 
  - developer
contributors:
  - JimDaly
---
# Lookup Control PreSearch event (Client API reference)

This event occurs just before the lookup control launches a dialog to search for records. There is no UI to set event handlers for this event. You must use the [addPreSearch](../controls/addpresearch.md) and [removePreSearch](../controls/removepresearch.md) methods on the lookup control to add or remove event handlers for this event.

Use this event with other lookup control methods to change the results displayed in a lookup based on the form data just before the lookup control shows search results for a user to choose from.

### Related articles

[addCustomFilter](../controls/addCustomFilter.md)   
[Events (Client API reference)](../events.md)   
[Events in forms and grids in model-driven apps](../../events-forms-grids.md)

[!INCLUDE[footer-include](../../../../../includes/footer-banner.md)]
