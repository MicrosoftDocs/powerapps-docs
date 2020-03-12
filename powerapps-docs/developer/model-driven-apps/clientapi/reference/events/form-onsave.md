---
title: "Form OnSave Event (Client API reference) in model-driven apps| MicrosoftDocs"
ms.date: 10/31/2018
ms.service: powerapps
ms.topic: "reference"
applies_to: "Dynamics 365 (online)"
ms.assetid: 89123cde-7c66-4c7d-94e4-e287285019f8
author: "KumarVivek"
ms.author: "kvivek"
manager: "annbe"
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---
# Form OnSave Event (Client API reference) in model-driven apps



The `OnSave` event occurs when:
- The user clicks the **Save** icon in the lower right corner of the form, even when there is no changed data to be saved.
- Code executes the [formContext.data.entity.save](../formContext-data-entity/save.md) method, even when there is no changed data to be saved.
- The user navigates away from the form and there is unsaved data in the form.
- The auto-save option is enabled, 30 seconds after data has changed and there is unsaved data in the form.
- Code executes the [formContext.data.save](../formContext-data/save.md) method and there is unsaved data in the form.
- Code executes the [formContext.data.refresh](../formContext-data/refresh.md) method passing a true value as the first parameter and there is unsaved data in the form.

To determine which button was clicked to perform the save, use the getSaveMode method.

You can cancel the save action by using the preventDefault method within the event arguments object. The preventDefault method which is accessible by using the getEventArgs method that is part of the execution context. Execution context is automatically passed to the form event handler.

> [!NOTE]
> OnSave events are synchronous, and it isn't recommended to use asynchronous code in an OnSave event handler that needs an action to be taken or handled on the response. This causes issues if the response handler expects the app context to remain the same as it was when the asynchronous code was started.
> 
> For example, there may be code in an OnSave event handler to make a network request, stop the form save (using the preventDefault method), and then close the form if the request is successful. Before the response from the request is receieved, the user may have navigated to a different page. In this case, the user may see an unexpected unsaved changes dialog from the page they are on when the response is received.

### Related topic
[Grid OnSave Event](grid-onsave.md)  



