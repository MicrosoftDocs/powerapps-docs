---
title: "Form OnSave event (Client API reference) in model-driven apps| MicrosoftDocs"
description: Includes description and supported parameters for the form OnSave event.
ms.date: 05/05/2021
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

## Async OnSave event

Async OnSave event gives the ability to wait for promises to settle down before saving, allowing the `OnSave` event to be asynchronous.

Async OnSave event occurs when the `OnSave` event is triggered and a promise is returned by the `OnSave` event handler. Enable the `Async OnSave` event by updating the `customization.xml` file for the app you want. More information: [Enable Async OnSave event](#enable-async-onsave-using-app-setting).

Saving of the record happens when the promise is resolved. For any promises that are returned, there is a 10-second limit for each promise, after that the platform considers promises to be timed out. This timeout is applied per promise. For example, if we have five promises returned, the total wait time is 50 seconds.  

If the promise is rejected or timed out, the save operation continues to behave similarly to the current script errors. Use the [preventDefault](../save-event-arguments/preventDefault.md) method within the event arguments object in that particular handler if you want to prevent the save event to happen if there is a script error/rejected promise or handler times out.

You can also cancel the save operation irrespective of the error in the handler or not using the [preventDefault](../save-event-arguments/preventDefault.md) method within the event arguments object. If this method is called, the Async OnSave event will still wait for all the promises to settle, but the save will not occur. This means the logic within `.then()` & `.catch()` will still execute.

Async OnSave event will only wait for one promise returned per handler. If multiple promises are required, it is recommended to wrap all the promises in the `Promise.all()` method. For multiple handlers that all return a promise, we recommend you to create one handler that calls all the events and return a single promise that wraps all required promises. This is to minimize wait times caused by the timeout.

### Example scenario on when to use Async OnSave event

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

App setting is a platform component that allows you to override a setting on an app. 

To enable the Async OnSave event for a specific app, add the below XML in the `customization.xml`  file. This should be added under the existing AppModule node in your `customization.xml` file.

Setting the `<value>true</value>`, enables the Async OnSave event for that specific app. Any form within this app will be able to get access to the Async OnSave functionality.

```XML
<AppModule>
 <appsettings>
    <appsetting uniquename="MyAppName_AsyncOnSave">
     <value>true</value>
     <settingdefinitionid>
     <uniquename>AsyncOnSave</uniquename>
     </settingdefinitionid>
 </appsetting>
 </AppModule>
 ```

### Related article

[Grid OnSave Event](grid-onsave.md)  


[!INCLUDE[footer-include](../../../../../includes/footer-banner.md)]
