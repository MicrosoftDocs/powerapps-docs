---
title: "Lookup Control PreSearch Event (Client API reference) in Dynamics 365 Customer Engagement| MicrosoftDocs"
ms.date: 10/31/2017
ms.service: "crm-online"
ms.topic: "reference"
applies_to: "Dynamics 365 (online)"
ms.assetid: 89123cde-7c66-4c7d-94e4-e287285019f8
author: "KumarVivek"
ms.author: "kvivek"
manager: "amyla"
---
# Lookup Control PreSearch Event (Client API reference)



This event occurs just before the Lookup control launches a dialog to search for records. There is no UI to set event handlers for this event. You must use the [addPreSearch](../controls/addpresearch.md) and [removePreSearch](../controls/removepresearch.md) methods on the lookup control to add or remove event handlers for this event.

Use this event with other Lookup control methods to change the results displayed in a lookup based on the form data just before the lookup control shows search results for a user to choose from. 

## Related topics

[addCustomFilter](../controls/addCustomFilter.md)



