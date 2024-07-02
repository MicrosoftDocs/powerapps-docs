---
title: "Form Loaded event (Client API reference) in model-driven apps| MicrosoftDocs"
description: Includes description and supported parameters for the Loaded event.
author: aorth
ms.author: aorth
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

This event occurs after the form load completes. It's recommended to run app logic that isn't immediately needed during the form load process. For example, moving extra APIs calls after form load completes can significiantly improve the loading experience and reduce time to first use.
 
Use the formContext.ui.[addLoaded](../formContext-ui/addLoaded.md) and formContext.ui.[removeLoaded](../formContext-ui/removeLoaded.md) methods to manage event handlers for this event. 

[!INCLUDE[footer-include](../../../../../includes/footer-banner.md)]
