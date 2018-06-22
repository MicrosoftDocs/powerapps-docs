---
title: "Form data OnLoad Event (Client API reference) in model-driven apps| MicrosoftDocs"
ms.date: 10/31/2017
ms.service: "crm-online"
ms.topic: "reference"
applies_to: "Dynamics 365 (online)"
ms.assetid: fb13c0a1-0e00-4592-8e58-3c2412141fbd
author: "KumarVivek"
ms.author: "kvivek"
manager: "amyla"
---
# Form data OnLoad Event (Client API reference)



This event occurs whenever form data is loaded, specifically:

- On initial page load
- When the page data is explicitly refreshed using formContext.data.[refresh](../formContext-data/refresh.md) method.
- When the data is refreshed on a page on saving a record, if there are any changes.
 
Use the formContext.data.[addOnLoad](../formContext-data/addOnLoad.md) and formContext.data.[removeOnLoad](../formContext-data/removeOnLoad.md) methods to manage event handlers for this event. 



