---
title: "IFRAME OnReadyStateComplete event (Client API reference) in model-driven apps| MicrosoftDocs"
description: Includes description and supported parameters for the OnReadyStateComplete event.
ms.author: jdaly
author: adrianorth
manager: kvivek
ms.date: 03/12/2022
ms.reviewer: jdaly
ms.topic: "reference"
applies_to: "Dynamics 365 (online)"
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
contributors:
  - JimDaly
---
# IFRAME OnReadyStateComplete event (Client API reference)

The `OnReadyStateComplete` event indicates that the content of the IFRAME has loaded and can be accessed in code. Use this event when referencing IFRAME controls within your scripts. 

Use the [control's](/powerapps/developer/model-driven-apps/clientapi/reference/controls/getcontrol) **addOnReadyStateComplete** and **removeOnReadyStateComplete** methods to manage event handlers for this event. Here's an example:

```JavaScript
function onLoad(executionContext)
{
  let formContext = executionContext.getFormContext();
  let webResource = formContext.getControl("webResourceName");
  webResource.addOnReadyStateComplete(context => {
    //do something
  });
}
```

[!INCLUDE[footer-include](../../../../../includes/footer-banner.md)]
