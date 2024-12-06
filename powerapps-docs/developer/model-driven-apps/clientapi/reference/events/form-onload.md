---
title: "Form OnLoad event (Client API reference) in model-driven apps"
description: Includes description and supported parameters for the OnLoad event.
author: MitiJ
ms.author: mijosh
ms.date: 01/16/2024
ms.reviewer: jdaly
ms.topic: reference
applies_to: "Dynamics 365 (online)"
search.audienceType: 
  - developer
contributors:
  - JimDaly
---
# Form OnLoad event

This event occurs whenever the form is loaded, specifically:

- On initial page load
- After a new record is first saved (created)
 
Use the formContext.ui.[addOnLoad](../formContext-ui/addOnLoad.md) and formContext.ui.[removeOnLoad](../formContext-ui/removeOnLoad.md) methods to manage event handlers for this event. 

> [!NOTE] 
> Controls in a form may not be ready when a form's `OnLoad` event occurs. Use the `OnLoad` event of the control to wait for it to be ready. More information: [Add or remove event handler function to event using UI](../../events-forms-grids.md#add-or-remove-event-handler-function-to-event-using-ui)

## Asynchronous OnLoad event handler support

The `OnLoad` event handler has the ability to wait for promises returned by event handlers to settle before loading a form that allows for an `OnLoad` event to be asynchronous ("async"). The `OnLoad` event becomes async when the event handler returns a promise.

The form loads when each promise returned by the event handler is resolved. For any promises that are returned, there's a 10-second limit for each promise. After that, the platform considers promises to be timed out. This timeout is applied per promise. For example, if you have five promises returned, the total wait time is 50 seconds.
Suppose the promise is rejected or timed out. In that case, the form load operation behaves similarly to the current script errors.

The `OnLoad` event will wait for one promise returned per handler. If multiple promises are required, it's recommended to wrap all the promises in the `Promise.all()` method and return the single resulting promise. For multiple handlers that return a promise, we recommend that you create one handler that calls all the events and return a single promise that wraps all required promises. This is to minimize wait times caused by the timeout.

### Enable Async OnLoad using app setting

To use async onLoad handlers, you'll need to enable it through the app setting.
An app setting is a platform component that allows you to turn supported features on or off for your app.
To enable the async Onload event handlers for a specific app:

1. Go to https://make.powerapps.com.
1. Make sure you select the correct environment.
1. Select **Apps** from the left navigation pane.
1. Select the app and then select **...** (ellipses). Select **Edit**.
1. Select **Settings** in the command bar.
1. When the dialog opens, select **Features**.
1. Turn on **Async onload handler**.
1. Select **Save**.

    ![Async OnLoad app setting](../../../media/async_onLoad_app_settings.png "Async OnLoad app setting")
    
### Async OnLoad timeouts

When using an async handler, a form load waits for the promise to be fulfilled, but only up to 10 seconds. This limit ensures that the form loads within a reasonable amount of time.

### Related articles

[Events (Client API reference)](../events.md)   
[Events in forms and grids in model-driven apps](../../events-forms-grids.md)

[!INCLUDE[footer-include](../../../../../includes/footer-banner.md)]
