---
title: "Form data OnLoad event (Client API reference) in model-driven apps"
description: Includes description and supported parameters for the form data OnLoad event.
author: MitiJ
ms.author: mijosh
ms.date: 03/12/2022
ms.reviewer: jdaly
ms.topic: reference
applies_to: "Dynamics 365 (online)"
search.audienceType: 
  - developer
contributors:
  - JimDaly
---
# Form data OnLoad event (Client API reference)

This event occurs whenever form data is loaded, specifically:

- On initial page load.
- When the page data is explicitly refreshed using formContext.data.[refresh](../formContext-data/refresh.md) method.
- When the data is refreshed on a page on saving a record, if there are any changes.
 
Use the formContext.data.[addOnLoad](../formContext-data/addOnLoad.md) and formContext.data.[removeOnLoad](../formContext-data/removeOnLoad.md) methods to manage event handlers for this event. 


## Related articles

[Events (Client API reference)](../events.md)   
[Events in forms and grids in model-driven apps](../../events-forms-grids.md)

[!INCLUDE[footer-include](../../../../../includes/footer-banner.md)]
