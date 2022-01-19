---
title: "Form OnSave event (Client API reference) in model-driven apps| MicrosoftDocs"
description: Includes description and supported parameters for the form OnSave event.
ms.date: 12/16/2021
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
# Form OnSave event (Client API reference) in model-driven apps

The `OnSave` event occurs when:

- The user selects the **Save** icon in the lower right corner of the form, even when there is no changed data to be saved.
- Code executes the [formContext.data.entity.save](../formContext-data-entity/save.md) method, even when there is no changed data to be saved.
- The user navigates away from the form and there is unsaved data in the form.
- The auto-save option is enabled, 30 seconds after data has changed and there is unsaved data in the form.
- Code executes the [formContext.data.save](../formContext-data/save.md) method and there is unsaved data in the form.
- Code executes the [formContext.data.refresh](../formContext-data/refresh.md) method passing a true value as the first parameter and there is unsaved data in the form.

To determine which button was clicked to perform the save, use the getSaveMode method.

You can cancel the save action by using the preventDefault method within the event arguments object. The preventDefault method is accessible by using the getEventArgs method that is part of the execution context. Execution context is automatically passed to the form event handler.

## Asynchronous event handler support

The OnSave event has ability to wait for promises returned by event handlers to settle before saving, allowing the `OnSave` event to be asynchronous ("async").

The `OnSave` event becomes async when a promise is returned by an `OnSave` event handler. Saving of the record happens when each promise returned by a handler is resolved. For any promises that are returned, there is a 10 second limit for each promise, after that the platform considers promises to be timed out. This timeout is applied per promise. For example, if we have 5 promises returned, the total wait time is 50 seconds.  

If the promise is rejected or timed out, the save operation continues to behave similarly to the current script errors. Use the [preventDefault](../save-event-arguments/preventDefault.md) method within the event arguments object in that particular handler if you want to prevent the save event to happen if there is a script error/rejected promise or handler times out.

You can also cancel the save operation irrespective of the error in the handler or not using the [preventDefault](../save-event-arguments/preventDefault.md) method within the event arguments object. If this method is called, the Async OnSave event will still wait for all the promises to settle, but the save will not occur. This means the logic within `.then()` & `.catch()` will still execute.

The `OnSave` event will only wait for one promise returned per handler. If multiple promises are required, it is recommended to wrap all the promises in the `Promise.all()` method and return the single resulting promise. For multiple handlers that all return a promise, we recommend you to create one handler that calls all the events and return a single promise that wraps all required promises. This is to minimize wait times caused by the timeout.

### Example scenario on when to use async OnSave handlers

Consider creating a Work Order Service Task, you need to validate that the Customer Asset selected has the same account listed in the Work Order. Fetching the account on the Work Order and Customer Asset are both asynchronous processes and need to be completed before the validation can occur. 

In this scenario, since there are multiple async processes and both calls return a single promise by wrapping both in the `Promise.all()` method.

> [!NOTE] 
> The `preventDefault` can only be used synchronously. For example, in the following handler:
   > ```JavaScript
   > function myHandler(context) {
  > return new Promise((resolve) => {
  > setTimeout( () => {
  > context.getEventArgs().preventDefault();
  > }, 1000);
  >  });
  > }
  >```

### Enable Async OnSave using app setting 

To use async onSave handlers you will need to enable it through an app setting:

1. Go to https://make.powerapps.com.
2. Make sure select the correct environment.
3. Select **Apps** from the left navigation pane.
4. Select the app and then select **...** (ellipses). Select **Open in preview**.
5. Select **Settings** from the command bar.
6. When the dialog opens, select **Features**.
7. Turn on **Async onload handler**.
8. Select **Save**.

    ![Async OnSave app setting](../../../media/async_onSave_app_settings.png "Async OnSave app setting")

### Async onSave timeouts

When using an async save the handler will wait for the promise to be fulfilled. To ensure that a save completes in a timely manner the handler throws a timeout exception after 10 seconds to let you know to tune the async `OnSave` event for better performance.

There may be scenarios where you want to halt the `OnSave` execution, and the timeout will stop the operation from occurring.  An example is opening a dialog in the async OnLoad and waiting for the user’s input before saving. To make sure the async operation will wait you can provide the event argument **disableAsyncTimeout**(executioncontext.getEventArgs().disableAsyncTimeout()).

When the **disableAsyncTimeout is set, the timeout for that handler will not be applied. It will continue to wait for that handler's promise to be fulfilled.

This should be used with caution as it might affect the performance of the form save.

### Related article

[Grid OnSave Event](grid-onsave.md)  


[!INCLUDE[footer-include](../../../../../includes/footer-banner.md)]
