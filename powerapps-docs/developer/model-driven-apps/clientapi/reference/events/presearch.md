---
title: "Lookup Control PreSearch event (Client API reference) in model-driven apps| MicrosoftDocs"
description: Includes description and supported parameters for the PreSearch event.
ms.date: 04/19/2021
ms.service: powerapps
ms.topic: "reference"
applies_to: "Dynamics 365 (online)"
ms.assetid: 89123cde-7c66-4c7d-94e4-e287285019f8
author: "Nkrb"
ms.author: "nabuthuk"
manager: "kvivek"
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---
# Lookup Control PreSearch event (Client API reference)



This event occurs just before the lookup control launches a dialog to search for records. There is no UI to set event handlers for this event. You must use the [addPreSearch](../controls/addpresearch.md) and [removePreSearch](../controls/removepresearch.md) methods on the lookup control to add or remove event handlers for this event.

Use this event with other lookup control methods to change the results displayed in a lookup based on the form data just before the lookup control shows search results for a user to choose from. 

## Related topics

[addCustomFilter](../controls/addCustomFilter.md)





[!INCLUDE[footer-include](../../../../../includes/footer-banner.md)]