---
title: "Form OnLoad event (Client API reference) in model-driven apps| MicrosoftDocs"
description: Learn how to set the form OnLoad event.
ms.date: 04/15/2021
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
# Form OnLoad event (Client API reference)

The form `OnLoad` event occurs after the form has loaded. It also occurs after a record is saved on create or update, and on refresh. For example by selecting the **Save** or the **Refresh** button on the main form.  Use the `OnLoad` event to apply logic about how the form should be displayed, to set properties on columns, and interact with other page elements.

You can determine in what context the `OnLoad` event occurs by using [getEventArgs](../executioncontext/getEventArgs.md). By doing so, you can apply logic conditional on the context. 

Data for related tables on a form, such as data for subgrids and quick view forms are not guaranteed to be available when the `OnLoad` event handler is executed. Logic that depends on related data should use the [Subgrid OnLoad](./subgrid-onload.md) event, quick view form should use the [isLoaded](../formcontext-ui-quickforms/isloaded.md) function, or the appropriate function for determining when the data should be loaded for the particular related data.

[!INCLUDE[cc-terminology](../../../../data-platform/includes/cc-terminology.md)]

Controls and other UI of the form are not guaranteed to be rendered and in the DOM when the `OnLoad` event occurs. Logic in the `OnLoad` event handler cannot prevent the form from loading.

The form `OnLoad` event is synchronous by default. However, you should **not** make synchronous network requests in an `OnLoad` event handler. This can cause a slow save experience and an unresponsive app. Instead, you should [asynchronous network requests](../../../best-practices/business-logic/interact-http-https-resources-asynchronously.md). Using asynchronous requests will [dramatically improve the performance of form loads](https://powerapps.microsoft.com/blog/turbocharge-your-model-driven-apps-by-transitioning-away-from-synchronous-requests/) compared to using synchronous requests. If a promise is returned by an event handler, the event becomes asynchronous and the form runtime will wait until the promise is settled before allowing the user to interact with the form.

You should be careful when using asynchronous code in an `OnLoad` event handler that needs an action to be taken or handled on the resolution of the async code. Asynchronous code can cause issues if the resolution handler expects the app context to remain the same as it was when the asynchronous code has started. For example, there may be code in an `OnLoad` event handler to make a network request and change a control to be disabled based on the response data. Before the response from the request is received, the user may have interacted with the control or navigated to a different page, so there may be undesired behavior. If you need to not show data or UI before the asynchronous requests complete, your code can hide or disable the relevant UI until the requests are complete. Your code should also check that the user is in the same context after each asynchronous continuation point.





[!INCLUDE[footer-include](../../../../../includes/footer-banner.md)]
