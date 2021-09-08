---
title: "Troubleshoot form issues in model-driven apps (model-driven apps) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "Learn about how to resolve the common issues on model-driven apps forms." # 115-145 characters including spaces. This abstract displays in the search result.
ms.custom: ""
ms.date: 09/07/2021
ms.reviewer: ""
ms.service: powerapps
ms.subservice: troubleshoot
ms.topic: "article"
author: "Nkrb" # GitHub ID
ms.author: "nabuthuk" # MSFT alias of Microsoft employees only
manager: "kvivek" # MSFT alias of manager or PM counterpart
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---

# Troubleshoot form issues in model-driven apps

Troubleshooting issues in Unified Interface is essential when you're working with forms that occur when loading a form, running a script, working with events, or saving data.

This article helps you fix some of the common issues you might encounter while working with model-driven app forms.

> [!IMPORTANT]
> - The tools described in this article are designed for troubleshooting purposes; they aren't meant to be used in day-to-day production scenarios, even though you can use them for troubleshooting issues in production environments. 
> - These troubleshooting tools only affect the current user session unless otherwise noted (for example, when a browser tab accesses the model-driven app). They don't change system customizations or affect any other users or sessions. After the current session is closed, the effect is no longer applied.
> - Most of the tools are available in all the production environments. Some of them mentioned in the article might not have been deployed to your organization yet; new tools are added periodically.
> - Tools listed in this article are written in a scenario-driven way. You can use them independently to troubleshoot different types of issues. 
> - [Use URL parameters to disable various form components](#use-url-parameters-to-disable-various-form-components) and [View registered form event handlers and libraries in Monitor](#view-registered-form-event-handlers-and-libraries-in-monitor) are critical and fundamental tools you'll frequently use to troubleshoot many scenarios. 

## Use URL parameters to disable various form components

When you're troubleshooting issues with forms, you need to use the URL parameters to disable components as you work to isolate the specific component that caused the issue. We recommend that you use the flags one at a time to narrow down the cause of the issue. You can use the following URL parameters:

- **DisableFormCommandbar**  

   Disables the command bar on the form. It only disables the command bar on form pages and not supports list (grid), dashboard, etc.  

   ```http
   https://myorg.crm.dynamics.crm/main.aspx?appid=00000000-0000-0000-0000-000000000000&pagetype=entityrecord&id=00000000-0000-0000-0000-000000000000**&flags=DisableCommandbar=true
  ```

- **DisableFormHandlers**  

   Disables all the form handlers. If you use the **DisableFormHandlers=true** flag, it disables the following event handlers: [OnLoad](./clientapi/reference/events/form-onload.md), [OnSave](./clientapi/reference/events/form-onsave.md), business rule, [OnChange](./clientapi/reference/events/attribute-onchange.md), and [TabStateChange](./clientapi/reference/events/tabstatechange.md). 
 
   To learn more about obtaining event or library indices for granular controls, see [View registered form event handlers and libraries in monitor](#view-registered-form-event-handlers-and-libraries-in-monitor). 

   ```http
   https://myorg.crm.dynamics.crm/main.aspx?appid=00000000-0000-0000-0000-000000000000&pagetype=entityrecord&id=00000000-0000-0000-0000-000000000000**&flags=DisableFormHandlers=true
   ```

    - **&flags=DisableFormHandlers=*eventName***  

       Disables the form handler by specifying the event name, for example, ****DisableFormHandlers=onload**.

       ```http
       https://myorg.crm.dynamics.crm/main.aspx?appid=00000000-0000-0000-0000-000000000000&pagetype=entityrecord&id=00000000-0000-0000-0000-000000000000**&flags=DisableFormHandlers=true
       ```

    - **&flags=DisableFormHandlers=*eventName_index***

      Disables the event handler at the specified index for any supported event name. For example, `DisableFormHandlers=true_0` disables all the event handlers at index 0. `DisableFormHandlers=onload_2` disables the [OnLoad](./clientapi/reference/events/form-onload.md) event handler at index 2.

    - **&flags=DisableFormHandlers=*eventName_startIndex_endIndex***

      Disables all the event handlers within the given range by specifying `startIndex` and `endIndex` values (both are included). For example, `DisableFormHandlers=true_0_2` disables all the event handlers of index 0, 1, and 2. `DisableFormHandlers=onload_2_5` disables the [OnLoad](./clientapi/reference/events/form-onload.md) event handler of index 2, 3, 4, and 5. If you have more event handlers, you can use this approach to narrow down problematic handlers quickly.  
  
    > [!NOTE]
    > Business rules are authored in the business rule designer, compiled into the client-side script, and registered in multiple form events, such as `OnLoad`, `OnSave`, and `OnChange`. The way to disable business rules are very similar to other form events. However, there're a few key differences:  
    > - When you use `DisableFormHandlers=true`, `businessrule`, `businessrule_*index*`, or `businessrule_*startIndex_endIndex*`, you're disabling the business rule(s) in all the form events they're registered to.  
    > - For example, the image below shows instructions on refreshing business rule(s) in the backend. You only need to do it once in your organization, and you can revert your changes after troubleshooting.  
      > [!div class="mx-imgBorder"]
      > ![Refresh business rules](media/businessrule-need-refresh.png "Refresh business rules")
      > After you perform the above action and refresh the form, you'll see different message with additional information, as shown in below:  
      > [!div class="mx-imgBorder"]
      > ![Business rules individual control](media/businessrule-individual-control.png "Business rules individual control")

  
- **DisableFormLibraries**  

   Disables form libraries and prevents the libraries from being loaded. To learn more about obtaining event or library indices for granular controls, see [View registered form event handlers and libraries in monitor](#view-registered-form-event-handlers-and-libraries-in-monitor) . The usage is similar to `DisableFormHandlers`, except it does not take an event name as the value.
 
    - **&flags=DisableFormLibraries=true**: Disable all the form libraries. 
    - **&flags=DisableFormLibraries=*index***: Disable form libraries at the specified index. 
    - **&flags=DisableFormLibraries=*startIndex_endIndex***: Disable form libraries in the range of startIndex and endIndex (both included). 

- **DisableWebResourceControls**  

   Disables all the web resource controls on the form.  

  ```http
  https://myorg.crm.dynamics.crm/main.aspx?appid=00000000-0000-0000-0000-000000000000&pagetype=entityrecord&id=00000000-0000-0000-0000-000000000000**&flags=DisableWebResourceControls=true
  ```

  > [!div class="mx-imgBorder"]
  > ![Disable web resource](media/disable-web-resource-control.png "Disable web resource")
    
- **DisableFormControl**  
    
  Disables a form control. Specify the control name to disable the control. If you see that the issue goes away with **&flags=DisableWebResourceControls=true**, and there is more than one web resource control on the form, you can use this flag to further identify the control that's causing the issue.   

  ```http
  https://myorg.crm.dynamics.crm/main.aspx?appid=00000000-0000-0000-0000-000000000000&pagetype=entityrecord&id=00000000-0000-0000-0000-000000000000**&flags=DisableFormControl=controlname
  ```

- **DisableBusinessProcessFlow**  

  Disables all the business process flows on the form.  

  ```http
  https://myorg.crm.dynamics.crm/main.aspx?appid=00000000-0000-0000-0000-000000000000&pagetype=entityrecord&id=00000000-0000-0000-0000-000000000000**&flags=DisableBusinessProcessFlow=true
  ```
   
- **navbar** 
  This isn't a **flag** parameter; instead, use **navbar=off** in the URL.

You can also add multiple URL parameters separated with a comma (**,**).

```Http
https://myorg.crm.dynamics.crm/main.aspx?appid=00000000-0000-0000-0000-000000000000&pagetype=entityrecord&id=00000000-0000-0000-0000-000000000000**&flags=DisableFormHandlers=true,DisableWebResourceControls=true,DisableFormCommandbar=true,DisableBusinessProcessFlow=true&navbar=off
```

> [!NOTE]
> The difference between **DisableFormHandlers** and **DisableFormLibraries** are:
> - The **DisableFormHandlers** flag disables form handlers regardless of the containing form libraries. In contrast, the **DisableFormLibraries** flag disables the form libraries (web resources) regardless of the functions (event handlers) included in the libraries. Simply put, **DisableFormLibraries** makes sure the specified JavaScript web resource files are not loaded.
> - The **DisableFormHandlers** flag doesn't prevent the containing form library from being loaded. Thus it doesn't stop the JavaScript code present in the library but not registered as an event handler from being executed. For example, if a form library `new_myscript.js` is written in the following way (not recommended practice):  
> - You should start with **DisableFormHandlers** to see if the issue goes away, and if not, you can try **DisableFormLibraries**. Disabling any script always involves some risks of potentially breaking your form scenarios. However, the latter tend to have more side effects because of the disablement of the entire JavaScript files.
> [!div class="mx-imgBorder"]
> ![Difference between DisableFormHandlers and DisableFormLibraries](media/difference-between-disableformhandlers-disableformlibraries.png "Difference between DisableFormHandlers and DisableFormLibraries")
> Assuming the `myOnloadHandler` is registered as an `OnLoad` event handler, the `DisableFormHandlers=true` flag only prevents the second alert, whereas the `DisableFormLibraries=true` flag prevents both alerts.


## View registered form event handlers and libraries in monitor

To view registered form event handles and libraries, you can view the `FormEvents` operation in [Monitor](../../maker/model-driven-apps/monitor-form-checker.md).

> [!div class="mx-imgBorder"]
> ![Form events](media/registered-form-events.png "Form events")

You'll need the `eventIndex` and `libraryIndex` parameter values when using the **DisableFormHandlers** or **DisableFormLibraries** URL flags. After an event or library is disabled, you'll see the event enabled state in both **FormEvents** operation (an overall view of all registered event handlers of all events), and **FormEvents.*eventName*** operation (details logged when a specific event happens).

> [!div class="mx-imgBorder"]
> ![Form events OnLoad](media/form-events-onload.png "Form events OnLoad")


## Unexpected behaviors when loading a form

### Issue  

Some common issues that can cause unexpected behavior when a model-driven app form is loaded are:

- Columns or controls don't have the values you expect.

- Controls aren't disabled or aren't enabled.

- Controls aren't shown or aren't hidden.

### How to troubleshoot

There are multiple reasons why unexpected behaviors occur when a form opens. One of the most common is the [OnLoad](./clientapi/reference/events/form-onload.md) scripts that run synchronously or asynchronously to change the column or control behavior. To determine whether your script is causing the issue, you can disable the form handlers by appending **&flags=DisableFormHandlers=true** at the end of your app URL.

If the unexpected behavior stops occurring after you disabled the form handler, it is a strong indication that the specific form handler is causing this behavior. If you have identified the problematic script that's causing this behavior, follow up with the script owner to further troubleshoot this issue.  

## Saving in progress error message

### Issue

Sometimes when you save a form, you see a **Saving in Progress** error message. 

This error occurs when the form [OnSave](./clientapi/reference/events/form-onsave.md) event is triggered before the previous [OnSave](./clientapi/reference/events/form-onsave.md) event has been completed. This behavior isn't supported, and the error appears by design because calling the `OnSave` event before the previous `OnSave` event is complete will cause recursive save loops with unintended consequences.

A typical cause for this error is the script that calls the `save()` method in the [OnSave](./clientapi/reference/events/form-onsave.md) event handler. Another possible cause might be concurrent `save()` calls in the `setTimeout()` method, which might cause the error to intermittently show up, depending on whether the prior `save()` call was completed before another `save()` call was made.

### How to troubleshoot

In [Monitor](../../maker/model-driven-apps/monitor-form-checker.md) the `FormEvents.onsave` operation provides all the details that are causing the error (the call stack has been modified for demonstration purpose). The call stack tells what exact web resource, function, line, and row number causing this error. The form checker cannot detect the error if the issue can't be reproduced.

> [!div class="mx-imgBorder"]
> ![Save in progress error](media/save-in-progress-error.png "Save in progress error")


Follow up with the script owner to further troubleshoot the issue.

## Intermittent form errors 

### Issue

The most common cause of intermittent or random form errors is using unsupported [client API](./clientapi/reference.md) methods. These errors have the following characteristics:

- They occur only for specific records, users, regions, or browsers, or only during periods when the network or service load is high.

- They rarely occur in support instances.

- They might occur once on a computer, and the same error might occur again after you clear the browser cache.

- [formContext.getControl](./clientapi/reference/controls/getcontrol.md) or [formContext.getControl(arg).getAttribute()](./clientapi/reference/controls/getattribute.md) randomly returns null for a valid control or column.

There are many ways to write unsupported client API methods, and they all share a common pattern: they cause a race condition in the form load pipeline. Because they introduce a race condition, the issue only occurs when the custom script executes before the form is fully ready to be accessed via the client API. This can depend on many factors:

- In the JavaScript web resource, code is put into a global scope that's executed immediately when the web resource file is loaded, without waiting for the form to be accessible. Make sure the code is executed inside a valid form handler, such as an [OnLoad](./clientapi/reference/events/form-onload.md) handler.  

  > [!div class="mx-imgBorder"]  
  > ![Unsupported Client API method](media/unsupported-clientapi-globalcode.png "Unsupported Client API method")  

- In the Power Apps component framework component script file, client API methods are accessed inside the [init](../component-framework/reference/control/init.md) or [updateView](../component-framework/reference/control/updateview.md) function. The `init()` and `updateView()` functions are executed immediately when the component is loaded, without waiting for the form to be readily accessible. You can't use unsupported Client API methods in Power Apps component framework components.

Client API is accessed inside a `window.setTimeout()` function in the web resource file. The page state is unpredictable when the `setTimeout()` method executes the wrapped function. Due to the nature of the timer function, when the execution occurs, the page might be in a transitional state (during page load or save) that's not readily accessible by the Client API.

### How to troubleshoot

Using [Monitor](../../maker/model-driven-apps/monitor-form-checker.md), you can access information that helps you determine when the unsupported client access occurred and when the access occurred at the wrong time due to a race condition. However, Form Checker will not report such unsupported client access when the unsupported code happens to execute at the right time that does not cause an issue.

> [!div class="mx-imgBorder"]
> ![Unsupported Client API](media/unsupported-client-api-method.png "Unsupported Client API")

> [!NOTE]
> The call stack has been modified for illustration purposes. The call stack shows details like web resource, function, and the line causing the error.

Follow up with the script owner to further troubleshoot the issue.

## The form or record isn't saved when you try to save the form

### Issue

A common cause is an [OnSave](./clientapi/reference/events/form-onsave.md) event handler that calls the [executionContext.getEventArgs().preventDefault()](./clientapi/reference/save-event-arguments/preventDefault.md) method to cancel the save operation.

### How to troubleshoot

In [Monitor](../../maker/model-driven-apps/monitor-form-checker.md), the `FormEvents.onsave` operation provides all the details of why the save event is canceled details than that are available from the form UI itself.

> [!div class="mx-imgBorder"]
> ![Record isn't saved error](media/record-not-saved-error.png "Record isn't saved error")

Follow up with the script owner to further troubleshoot the issue.

## Form freezes, loads slowly, or throws unexplained errors

### Issue

There are many possible reasons for a form to freeze, load slowly, or throw a "Web resource method does not exist" script error or an error that isn't a common script error. Some of the possible reasons include:

- Bad `OnLoad` scripts.

- Web resource controls.

- Ribbon button scripts and rules.

- Synchronous network requests.

- Custom plug-ins.

- Business process flow errors.

### How to troubleshoot

Determine if the issue reproduces without involving forms. If it does, then there is a broader issue that should be investigated out of the form's context. Actual ownership of the problem depends on the particular details case by case. 

- If you believe this issue only occurs on forms, see [Use URL parameters to disable various form components](#use-url-parameters-to-disable-various-form-components) to narrow down the component that's causing the issue.
- If you identified that the issue is caused by certain form libraries/script files, follow up with the owner who made these customizations further to find out the root cause of the issue.
- If you have identified that web resource controls cause the issue with the **DisableWebResourceControls** flag, then you can use the `DisableFormControl` flag to disable each one-by-one until the problem is longer reproduced. The last disabled control that doesn't reproduce the issue is the one that is causing the issue. Follow up with the owner of the control to further troubleshoot the issue.
- If you have identified that the issue is caused by the command bar/ribbon with the **DisableFormCommandbar** flag, this means this is not an issue with the form but an issue with the command bar. Use [Command Checker](https://powerapps.microsoft.com/blog/introducing-command-checker-for-model-app-ribbons/) to troubleshoot individual commands and identify which one is causing the issue.


## A business rule or custom script isn't working

### Issue

This issue occurs if a business rule or custom script that used to work in the legacy web client stopped working in Unified Interface. One of the main reasons for this error to occur is when a business rule or script in Unified Interface references a control that isn't available in Unified Interface.

### How to troubleshoot

One of the reasons that the business rule or script is not working in Unified Interface is that the controls that are part of them do not exist in Unified Interface.
Composite controls exist in the web client, but in Unified Interface composite control is broken down into parts and is stored differently. For example, if the column `fullname` is part of the business rule or custom script, columns `firstname`, `middlename`, or `lastname` should be used instead.

Once you launch form checker, you'll be able to see more details in the `CompositeControl` operation including the composite control that is causing the problem, the columns that can be used in the business rule or custom script instead and a full call stack (the call stack has been modified for demonstration purpose).

> [!div class="mx-imgBorder"]
> ![Custom script not working](media/custom-script-error.png "Custom script not working")

Follow up with the corresponding owner of the business rule or custom script to change the control suggested by the form checker.


## Related menu/Related tab

### Issue

There are many reasons why a related menu item doesn't appear on the **Related** tab or has an incorrect label.

### How to troubleshoot

In the following example, a related table `role` (security role) doesn't appear in the `team` form because the `role` table isn't available in Unified Interface.

> [!div class="mx-imgBorder"]
> ![Related menu](media/related-menu-error.png "Related menu")

In [Monitor](../../maker/model-driven-apps/monitor-form-checker.md), the `RelatedMenu` operation provides all the details that are causing the issue.

There are also a few sources where a record can be included as an option for the **Related** menu tab. The following example contains details that indicate that the label `Activities` in the **Related** menu on an account form comes from the plural display name of the related table.

> [!div class="mx-imgBorder"]
> ![Related menu details](media/related-menu-error-details.png "Related menu details")

Follow up with the corresponding owner of the related menu item.


## Why a control is disabled/enabled or visible/hidden

### Issue

There are many possible reasons why a control might be disabled or hidden when the form is loaded. 

### How to troubleshoot

You can use [Monitor](../../maker/model-driven-apps/monitor-form-checker.md) to view the `FormControls` operation that includes all the details about the initial control state when the form loads.

> [!div class="mx-imgBorder"]
> ![Forms controls check](media/form-controls-check.png "Form controls check")

Another place to check is the `ControlStateChange.visible` or `ControlStateChange.disabled` operation that explains why the control disable or visible state is changed at any time on the form. This operation explains the control state before the change, intended state change that may or may not succeed, and the state after the change. Not all control state change attempts are successful. For a control disabled by form XML, you can enable it through client API in an `OnLoad` event handler. However, if control is disabled for security reasons, it's highly unlikely an attempt to enable it through client API would successfully change the state.

> [!div class="mx-imgBorder"]
> ![Control state changed](media/control-state-changed.png "Control state changed")

A control can be disabled by using the following list of rules in order. If a rule is met, then the following rules are ignored. If you want to change whether a control is disabled, you must change the input to the rule used for the result or to a rule earlier in the list.

- If the flags `DisableWebResourceControls=true` or `DisableFormControl=<control name>` are passed and the control is affected by these flags, the control will be disabled.
- If the owning table is read-only in Unified Interface in table definitions, the control is disabled.
- If the table isn't available in offline mode, the control is disabled.
- If the current user doesn't have write permissions on the record, the control is disabled.
- If the column definition has `IsValidforCreate` set to false, the control is disabled.
- If the column definition has `IsValidforUpdate` set to false, the control is disabled.
- If the current user doesn't have `Assign to` privilege, the owner column is disabled.
- If the user doesn't have write permissions on the column defined by field-level security, the control is disabled.
- If the control is disabled or enabled by the Client API script, the control disabled state will honor that setting.
- If the control is disabled in the form designer, the control is disabled.
- If the user doesn't have `Assign To` privilege for the lookup control's table, or `Assign` privilege on the current record's table, the lookup control is disabled

Finally, if the control passes all the above checks, the record state determines whether the control is disabled. The control is enabled by default on active records and disabled on inactive records.

> [!NOTE]
> The difference between `FormControls` and `ControlStateChange` is that the `FormControls` operation reflects the initial control state when the form is loaded, while the `ControlStateChange`operation reflects the state change at any time on the form, whether it's during form load, in OnChange or OnSave events after the form is loaded.


## Why a control has a certain value on form load

### Issue
A control may or may not have a specific value on form load as the user expected. 

### How to troubleshoot

There are many possible reasons why control can have a value when a form loads. The `ControlDefaultValue` operation in [Monitor](../../maker/model-driven-apps/monitor-form-checker.md) explains the source of the default values. 

> [!div class="mx-imgBorder"]
> ![Default control value](media/control-default-value.png "Default control value")

If multiple updates are happening to a control's value, an `Update Sequence` will indicate the final value. For example, here is a control with a default value and then overridden with a value passed with a client API script. There is a call stack provided.

> [!div class="mx-imgBorder"]
> ![Control value before](media/control-default-value-after.png "Control value before")

There are scenarios where columns are populated based on a relationship column mapping, in which case the event will show that.

> [!div class="mx-imgBorder"]
> ![Control value after](media/control-default-value-update-sequence.png "Control value after")

Verify where the value is coming from and take action based on the below table:

| Source | How to fix |
|--|--|
| Client API script | Contact the script owner. |
| Default value | Check the control's configuration. |
| Relationship column mapping | Check the relationship configuration and update the column mapping. |
| Value passed by page input data passed via URL | Check the API that opens the specific form with the issue, it is passing the value. |


## Why a tab or section is visible or hidden

### Issue
There are many possible reasons why a tab or section might be hidden or visible.

### How to troubleshoot

The `TabStateChange` or `SectionStateChange` operations in [Monitor](../../maker/model-driven-apps/monitor-form-checker.md) explain the visible state change, as shown in the following image. If a script causes it, then the call stack would reveal the web resource file, line number, and function name that caused this behavior.

> [!div class="mx-imgBorder"]
> ![Tab section](media/tab-section-visible.png "Tab section")

Follow up according to the suggestion in the state reason or the owner of the web resource/business rules to change or fix the behavior.


## Unexpected dialogs or navigation

### Issue

There are many possible reasons why a dialog appears, or navigation happens unexpectedly. One of the common causes is the [Xrm.Navigation](./clientapi/reference/xrm-navigation.md) API methods are called to open a record or a form by a custom script. For example, when you open a form, an alert appears, as shown in the following image.

> [!div class="mx-imgBorder"]
> ![Alert dialog box](media/unexpected-alert-dialogs.png "Alert dialog box")

### How to troubleshoot

The `XrmNavigation` operation in [Monitor](../../maker/model-driven-apps/monitor-form-checker.md) contains call stack that helps you identify the script that's causing unexpected behavior.

> [!div class="mx-imgBorder"]
> ![XrmNavigation operation in monitor](media/form-checker-navigation.png "XrmNavigation operation in monitor")

Follow up with the owner of the web resource to change or fix the behavior.

## Opening another form instead of a quick create form

### Issue
When opening a quick create form from a lookup or a grid, another form may open (edit or main form) instead of a quick create form. There are few reasons why this can happen:

- The main form dialog force flag is being set.
- Quick create form is not available.

### How to troubleshoot

You can use [Monitor](../../maker/model-driven-apps/monitor-form-checker.md) to view the `FormType` operation that includes all the reasons why a quick create form is not opened.

> [!div class="mx-imgBorder"]
> ![Table not enabled for quick create](media/troubleshoot-forms-entity-not-eabled-for-quick-create.png "Table not enabled for quick create")

You'll need to follow up with the table owner who has disabled quick create through table definitions (metadata).


## Table doesn't appear in the quick create menu flyout

### Issue

When opening the global quick create menu flyout, not all tables are available. There are few reasons why the tables are filtered in this list:

- There is no quick create form available for the table.
- Table is not enabled for quick create form.
- Table is not enabled for the new Unified Interface.
- Table is read-only in Unified Interface.
- Table's mobile client visibility cannot be modified.
- Table is not part of the app module.
- User does not have a create privilege on the table.
- The create privilege is not supported for the table.

### How to troubleshoot

You can use [Monitor](../../maker/model-driven-apps/monitor-form-checker.md) to view the `QuickCreateMenu` operation, which includes all the tables and reasons why they are filtered from the quick create menu flyout.

See the examples below to understand the reasons for filtering. Based on the explanations, contact the responsible party or make changes accordingly.

> [!div class="mx-imgBorder"]
> ![Table not enabled for Unified Interface](media/troubleshoot-forms-entity-unified-client.png "Table not enabled for Unified Interface")

> [!div class="mx-imgBorder"]
> ![Table not available for quick create](media/troubleshoot-forms-entity-not-available-for-quick-create.png "Table not available for quick create")

> [!div class="mx-imgBorder"]
> ![Table not part of app module](media/troubleshoot-forms-entity-not-part-of-app.png "Table not part of app module")

## Unexpected unsaved changes message

### Issue
When working on forms, you get the *unsaved changes* message on the form footer when you navigate from the current form or save the form without any changes. 

### How to troubleshoot

The *unsaved changes* error appears when you change the form and when the changes are not saved. If you haven't made any changes manually, they could come from a JavaScript, plug-in, or business rule. You can use [Monitor](../../maker/model-driven-apps/monitor-form-checker.md) to view the `UnsavedChanges` operation that helps find the source of the changes. You can filter by OperationType `UnsavedChanges`.

The `all attributes modified` section includes a quick summary of the columns causing the unsaved changes error and their values. The `unsaved changes` section shows what happened to the columns in detail. For every column, a list of controls are provided that could be causing a change. The value change is also displayed (previousValue, newValue), and a call stack.

The screenshot below shows the root cause of the issue. You can see that the change has come from the `OnLoad` script.

> [!div class="mx-imgBorder"]
> ![Unsaved changes error](media/unsaved-changes-error.png "Unsaved changes error")

> [!NOTE]
> If the user has manually made the changes on the form, a call stack will not be provided.

Verify where the change is coming from and if it's expected behavior or not. If a script causes the change, the original web resource can be traced back in the call stack. In most cases, it will either be a script. Make a call based on the web resource itself.


## Business required column validation does not behave as expected

### Issue
Business required columns by default block the form save operation if the value is empty. However, in many by-design scenarios, a business-required column may not block the save operation when the value is empty or block the save when you don't believe it should.

### How to troubleshoot

The `RequiredFieldValidation` operation is logged when a save is attempted, regardless of whether save is successful or not. This operation explains why each business-required column blocks or doesn't block the save operation.

Below is an example of this operation. The message explains how to read the detailed reports of each required column. In this example, `fax` column is bound to one control, and the control of the same name is read-only hence will not trigger required column validation.

> [!div class="mx-imgBorder"]
> ![Column validation](media/required-field-validation.png "Column validation")

Below is another example that `jobtitle` is a business-required column on the business process flow but not on the form, and the column is not modified. Thus it does not block the save operation even when it's empty.

> [!div class="mx-imgBorder"]
> ![Required column validation](media/required-field-validation-bpf-only-field.png "Required column validation")

### Follow up

Most times, the behavior is by design, and the `RequiredFieldValidation` operation explains why this column behaves in a certain way in form save operation. If the required column validation is skipped on a column because the control is disabled or hidden, as the first example illustrated, see the form checker suggestions for further analysis. 

This may lead to another troubleshooting scenario such as [Why a control is disabled/enabled or visible/hidden](#why-a-control-is-disabledenabled-or-visiblehidden).


## Some columns are not displayed on the merge dialog

### Issue

The merge dialog uses the default main form definition for the table and selectively renders most, but not all the columns in the dialog. This Form Checker operation explains why some of the columns are not displayed on the merge dialog, even that they may be displayed on the main form.

### How to troubleshoot

The `MergeDialog.load` operation below explains the reason why some columns are not displayed.  

In this example, `parentcustomerid` column on the contact form is not supported in the merge dialog. The business card column is not displayed because the containing section is hidden in the main form XML definition. Even though showing the owning section in the main form via client API is possible, the merge dialog honors the form XML configuration as event handlers are not supported on the merge dialog.

> [!div class="mx-imgBorder"]
> ![Merge dialog load](media/merge-dialog-load.png "Merge dialog load")


[!INCLUDE[footer-include](../../includes/footer-banner.md)]