---
title: "Form OnLoad Event (Client API reference) in model-driven apps| MicrosoftDocs"
ms.date: 12/14/2020
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



The form `OnLoad` event occurs after the form has loaded. It also occurs after a record is created, for example by selecting the **Save** button on the main form.   Use the `OnLoad` event to apply logic about how the form should be displayed, to set properties on fields, and interact with other page elements.

You can determine in what context the `OnLoad` event occurs by using [getEventArgs](../executioncontext/getEventArgs.md). By doing so, you can apply logic conditional on the context. 

Data for related entities on a form, such as data for subgrids and quick view forms, are not guaranteed to be available when an `OnLoad` event handler is executed. Logic that depends on related data should use the subgrid onload event, the quick view form isLoaded function, or the appropriate manner for determining when related data is loaded for the particular related data.

Controls and other UI of the form are not guaranteed to be rendered and in the DOM when the `OnLoad` event occurs.

Logic in an `OnLoad` event handler cannot prevent the form from loading.

The form `OnLoad` events are synchronous. However, you should **not** make synchronous network requests in an `OnLoad` event handler. This can cause a slow save experience and an unresponsive app. Instead, you can make asynchronous network requests. 

You should be careful when using asynchronous code in an `OnLoad` event handler that needs an action to be taken or handled on the resolution of the async code. Asynchronous code can cause issues if the resolution handler expects the app context to remain the same as it was when the asynchronous code has started. For example, there may be code in an `OnLoad` event handler to make a network request and change a control to be disabled based on the response data. Before the response from the request is receieved, the user may have interacted with the control or navigated to a different page, so there may be undesired behavior. 



