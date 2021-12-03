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

## Asynchronous event handler support

The OnSave event has ability to wait for promises returned by event handlers to settle before saving, allowing the `OnSave` event to be asynchronous ("async").

The `OnSave` event becomes async when a promise is returned by an `OnSave` event handler, async OnSave events are enabled by default, if you wish to disable async operations for your `OnSave` handlers, go to [PowerApps](https://powerapps.microsoft.com), select **Solutions** tab , select the solution that has the app and then select **Settings**, and look for “Async onsave handler”, make sure the check box is unchecked.  After disabling the option make sure you publish customizations.

Saving of the record happens when each promise returned by a handler is resolved. For any promises that are returned, there is a 10-second limit for each promise, after that the platform considers promises to be timed out. This timeout is applied per promise. For example, if we have five promises returned, the total wait time is 50 seconds.  

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

### Disable Async OnSave using app setting 

An app setting is a platform component that allows you to override a setting on an app. App setting should have a unique name and must be in the format `solutionpublisherprefix_appname_settingname`.

To disable the async `OnSave` event handlers for a specific app:

- Create a new unmanaged solution. 
- Open the newly created solution. Select **Add existing** > **App** > **Model-driven app**.
- From the list of existing model-driven apps, select the app where you want to see this feature. 
- Publish all customizations. 
- Again from the list of solutions in the solution explorer, select the solution where you have added the model-driven app and then select **Export**. A zip file is downloaded to your local machine.
- Extract the downloaded  zip file. Open the **Customizations.xml** file in your preferred editing tool. 
- Add the following code `AppModule` node in the `customization.xml` file. Setting the `<value>false</value>` to disable async `OnSave` event handler support for that specific app. Any form within this app will be able to get access to the async OnSave functionality.

   ```XML
   <appsettings>
   <appsetting uniquename="MyAppName_AsyncOnSave">
      <iscustomizable>1</iscustomizable>
      <settingdefinitionid>
         <uniquename>AsyncOnSave</uniquename>
      </settingdefinitionid>
      <value>true</value>
   </appsetting>
  </appsettings>
   ```

- You can verify whether the configuration has been successfully installed using the following request: 

  ```http
  GET https://org00000000.crm.dynamics.com/api/data/v9.2/appsettings?$filter=(uniquename eq 'MyAppName_AsyncOnSave')
  Accept: application/json
  Authorization: Bearer ey...
  ```

### Related article

[Grid OnSave Event](grid-onsave.md)  


[!INCLUDE[footer-include](../../../../../includes/footer-banner.md)]
