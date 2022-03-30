---
title: "Form OnLoad event (Client API reference) in model-driven apps| MicrosoftDocs"
description: Includes description and supported parameters for the OnLoad event.
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
# Form OnLoad event

This event occurs whenever form data is loaded, specifically:

- On initial page load.
- When the page data is explicitly refreshed using formContext.data.[refresh](../formContext-data/refresh.md) method.
- When the data is refreshed on a page on saving a record, if there are any changes.
 
Use the formContext.data.[addOnLoad](../formContext-data/addOnLoad.md) and formContext.data.[removeOnLoad](../formContext-data/removeOnLoad.md) methods to manage event handlers for this event. 

> [!NOTE] 
> Controls in a form may not be ready when a form's `OnLoad` event occurs. Use the `OnLoad` of the control to wait for it to be ready. More information: [Add or remove event handler function to event using UI](../../events-forms-grids.md#add-or-remove-event-handler-function-to-event-using-ui)

## Asynchronous OnLoad event handler support

The `OnLoad` event handler has the ability to wait for promises returned by event handlers to settle before loading a form which allows for an OnLoad event to be asynchronous ("async").  The `OnLoad` event becomes async when the event handler returns a promise.

The form loads when each promise returned by the event handler is resolved. For any promises that are returned, there is a 10 second limit for each promise. After that, the platform considers promises to be timed out. This timeout is applied per promise. For example, if you have five promises returned, the total wait time is 50 seconds.
Suppose the promise is rejected or timed out. In that case, the form load operation behaves similarly to the current script errors.

The `OnLoad` event will only wait for one promise returned per handler. If multiple promises are required, it is recommended to wrap all the promises in the `Promise.all()` method and return the single resulting promise. For multiple handlers that return a promise, we recommend that you create one handler that calls all the events and return a single promise that wraps all required promises. This is to minimize wait times caused by the timeout.

### Enable Async OnLoad using app setting

To use async onLoad handlers, you will need to enable it through the app setting.
An app setting is a platform component that allows you to turn supported features on or off for your app.
To enable the async Onload event handlers for a specific app:

1. Go to https://make.powerapps.com.
2. Make sure you select the correct environment.
3. Select **Apps** from the left navigation pane.
4. Select the app and then select **...** (ellipses). Select **Open in preview**.
5. Select **Settings** in the command bar.
6. When the dialog opens, select **Features**.
7. Turn on **Async onload handler**.
8. Select **Save**.

    ![Async OnLoad app setting](../../../media/async_onLoad_app_settings.png "Async OnLoad app setting")
    
### Async OnLoad timeouts

When using an async handler, a form load will wait for the promise to be fulfilled. To ensure that a load completes on time, the handler throws a timeout exception after 10 seconds to let you know to tune the async OnLoad event for better performance.

There may be scenarios where you want to halt the OnLoad execution, and the timeout will stop the operation from occurring.  An example is opening a dialog in the async OnLoad and waiting for the user’s input before saving. To make sure the async operation will wait you can provide the event argument **disableAsyncTimeout**(executioncontext.getEventArgs().disableAsyncTimeout()).
 When the **disableAsyncTimeout is set, the timeout for that handler will not be applied. It will continue to wait for that handler's promise to be fulfilled.

This should be used with caution as it might affect the performance of the form load.

[!INCLUDE[footer-include](../../../../../includes/footer-banner.md)]
