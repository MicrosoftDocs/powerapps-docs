---
title: "Form OnLoad Event (Client API reference) in model-driven apps| MicrosoftDocs"
ms.date: 10/31/2018
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
# Form OnLoad Event (Client API reference)



The form `OnLoad` event occurs after the form has loaded. It also occurs after a record is created by selecting the **Save** button on the main form.  It cannot prevent the window from loading. Use the `OnLoad` event to apply logic about how the form should be displayed, to set properties on fields, and interact with other page elements.

The form `OnLoad` events are synchronous. However, you should **not** make synchronous network requests in an `OnLoad` event handler. This can cause a slow save experience and an unresponsive app. Instead, you can make asynchronous network requests. 

You should be careful when using asynchronous code in an OnLoad event handler that needs an action to be taken or handled on the resolution of the async code. Asynchronous code can cause issues if the resolution handler expects the app context to remain the same as it was when the asynchronous code has started. For example, there may be code in an `OnLoad` event handler to make a network request and change a control to be disabled based on the response data. Before the response from the request is receieved, the user may have interacted with the control or navigated to a different page, so there may be undesired behavior. 



