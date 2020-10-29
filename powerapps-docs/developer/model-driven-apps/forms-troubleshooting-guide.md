---
title: "Forms troubleshooting guide  (model-driven apps) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "Learn about how to resolve the common issues on model-driven apps forms." # 115-145 characters including spaces. This abstract displays in the search result.
ms.custom: ""
ms.date: 11/10/2020
ms.reviewer: ""
ms.service: powerapps
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

# Overview

Troubleshooting issues and problems in the Unified Interface is very important when you are working with forms and trying to fix issues that happen when loading a form, running a script, working with events or saving data. The following will help you troubleshoot common problems that can occur and help you better understand how to mitigate or resolve issues when working with forms in the Unified Interface.

Please be sure you have read through and understand how to use the [Monitoring Tool](https://docs.microsoft.com/powerapps/maker/model-driven-apps/monitor-form-checker)
and how to open up form events.

> [!IMPORTANT]

- The tools mentioned below are only designed for troubleshooting purposes and are not intended to be used in day-to-day normal production scenarios. For example, the URL flags that disables some form components should only be used to help narrow down the source of the issue, and should not be leveraged to permanently disable these form components when using the app in your daily operations.

- The tools will affect the current user session unless otherwise called out (such as the browser tab that's accessing the model-driven app). They do not change system customizations or affect any other users or sessions. Once the current session is closed, the effect is no longer applied.

- Most of the tools are available in production environments. Some of the tools mentioned in the guide may not have been deployed to your organization yet as new tools are added periodically.

- The tools listed below can be used independently to troubleshoot a certain category of issues.

The following sections include information on what you will need to complete the
troubleshooting scenarios included in this guide.

### Utilizing URL parameters to disable various form components.

In many of the examples and scenarios that you may run into it will require the use of a URL parameter to troubleshoot the issue. The following is a list of URL parameters that can be used to disable various form components when troubleshooting that will help narrow down many issues to a specific component.

It is recommended that you use the flags one-by-one to narrow down the cause of the issue.

- DisableFormCommandbar

- DisableFormHandlers

- DisableFormLibraries

- DisableWebResourceControls

- DisableFormControl

- DisableBusinessProcessFlow

- navbar (this is not a "flag" parameter, instead use "&navbar=off" in the
    URL)

Below are examples of how to use each of the flags listed above.

https://myorg.crm.dynamics.crm/main.aspx?appid=00000000-0000-0000-0000-000000000000&pagetype=entityrecord&id=00000000-0000-0000-0000-000000000000**&flags=DisableFormHandlers=true**

You can also add multiple URL parameters separated with comma ",":  
https://myorg.crm.dynamics.crm/main.aspx?appid=00000000-0000-0000-0000-000000000000&pagetype=entityrecord&id=00000000-0000-0000-0000-000000000000**&flags=DisableFormHandlers=true,DisableWebResourceControls=true,DisableFormCommandbar=true,DisableBusinessProcessFlow=true&navbar=off**

https://myorg.crm.dynamics.crm/main.aspx?appid=00000000-0000-0000-0000-000000000000&pagetype=entityrecord&id=00000000-0000-0000-0000-000000000000**&flags=DisableFormCommandbar=true**

### View registered form event handlers and libraries

To see registered form event handles and libraries you can view the "FormEvents" operation.

![](media/1bd222527f6947d09561cf4ea21c43fc.png)

You'll need the "eventIndex" and "libraryIndex" when using **DisableFormHandlers** or **DisableFormLibraries** URL flags.  Once an event or library is disabled the "disabledByConfigFlag" will be true, and you'll also see such events in the actual event handling.

![](media/08112c46fd04c7ae7b3d9a49ae36b7be.png)

### Disabling form handlers

The following disables form handlers but does not prevent the containing web resource files from being loaded.

- **&flags=DisableFormHandlers=\<event name\>**: You can specify any supported event name, such as DisableFormHandlers=onload. If you use DisableFormHandlers=true, it'll be a shortcut to disable these event handlers: onload, onsave, businessrule, onchange and ontabstatechange.

- **&flags=DisableFormHandlers=\<event name\>_\<event index\>**: This value disables the handler at index 0 in the event handler list of any given supported event name. For example, DisableFormHandlers=true_0 will disable handler at index 0 of the event names included by "true" value. DisableFormHandlers=onload_2 will disable handler at index 2 of the onload
event.

- **&flags=DisableFormHandlers=\<event name\>\<starting index\>\<end index\>**: This value disables all handlers for a given event name within the given index range. For example, DisableFormHandlers=true_0_2 will disable handlers of index from 0 to 2 (0 and 2 are included) of the event names included by "true" value. DisableFormHandlers=onload_2_5 will disable onload handlers of index from 2 to 5.

### Disabling form libraries

To help troubleshoot issues you may have to disable form libraries. The below covers how to use URL Parameters to disable libraries from running in your event handlers.

- **&flags=DisableFormLibraries=true**  Disables all form libraries.

- **&flags=DisableFormLibraries=\<library index\>**  This value disables the form library at index handler at the given index. For example, DisableFormLibraries=0 disables form library at index 0.

- **&flags=DisableFormLibraries=\<starting index\>_\<ending index\>**  This value disables the form library within the given index range. For example, DisableFormLibraries=0_2 will disable form libraries of index from 0 to 2 (0 and 2 are included).

### Differences between DisableFormHandlers and DisableFormLibraries

The main difference between disabling form libraries and form handlers are:

- DisableFormHandlers disables handlers regardless the containing form libraries, while DisableFormLibaries disables form libraries (web resources) regardless the functions (event handlers) included in the libraries.

- DisableFormHandlers does not prevent the containing form library from being loaded, thus does not prevent the javascript code that is in a library but not registered as any event handler from being executed.  For example, if a form library "new_myscript.js" is written in the following way:

  - Assuming myOnloadHandler is registered as an onload handler.
  - DisableFormHandlers=true will only prevent the second alert dialog, while
  - DisableFormLibraries=true will prevent both alert dialogs.

### Disabling web resource controls

To help troubleshoot issues you may have to disable web resource controls. The below covers how to use URL Parameters to disable any web resource from running in your event handlers.

**&flags=DisableWebResourceControls=true** Here is a screen shot of what it will look like in your application.

![](media/0f342d7d828dc443cedca216c50dcaba.png)

### Disabling controls on a form

To help troubleshoot issues you may have to disable controls are a form. The below covers how to use URL Parameters to disable a control to help further
troubleshoot issues.

**&flags=DisableFormControl=new_mycontrol**

> [!NOTE]
> This flag disables a form control given the control name. If the issue goes away when &flags=DisableWebResourceControls=true, there may be more than one web
resource control on the form and you can use this flag to further help pinpoint the control that is causing the issue.

### Disable the business process flow

To help troubleshoot issues you may have to disable a business process flow. To disable business process flows use add to
**&flags=DisableBusinessProcessFlow=true** the end of your app URL. This will disable a business process flow to help further troubleshoot issues.

## Unexpected behaviors when loading a form

Please read through the overview section if you have not already done so to help familiarize you with the various tools and options to help troubleshoot your
issue.

You may see unexpected behaviors when you open a form. Some common issues include but are not limited to:

- Fields or controls do not have an expected value

- Controls are not disabled/enabled as expected

- Controls are not shown/hidden as expected

- Any of the above behaviors appear shortly after the form is opened, e.g., you see a value or a control for a split second, and then the value changes, or the control disappears

There are many possible causes of unexpected behaviors when a form opens. One of the most common is an OnLoad script that runs synchronously or asynchronously to change the field / control behavior. To determine if your script is causing the issue you can easily turn your script on or off using URL parameters by appending **&flags=DisableFormHandlers=true** to the end of your app url.

If the form loads normally after turning off your form handler it will be an indicator that there is an issue with your script that is blocking or causing an
error when a form is loading.

## Intermittent form errors

Please read through the overview section if you have not already done so to help familiarize you with the various tools and options to help troubleshoot your
issue.

There are many possible causes for intermittent or random form errors. Using unsupported Client API could be the main reason why you see errors and usually share some of following characteristics:

- Intermittent or random

- Occurs on some records, users, regions, browsers, or only during a certain period when network or service load is high.

- Occurs rarely on support instances.

- The repro may only occur once on a computer, and it may occur again after
    clearing browser cache.

- [formContext.getControl](https://docs.microsoft.com/powerapps/developer/model-driven-apps/clientapi/reference/controls/getcontrol)  or [formContext.getControl(arg).getAttribute()](https://docs.microsoft.com/powerapps/developer/model-driven-apps/clientapi/reference/controls/getattribute)  randomly returns null for a valid control or attribute.

There are many ways to write unsupported Client API code and all share one common pattern that they are not written in a supported pipeline and they cause
a race condition in the form load pipeline. Because they introduce a race condition, the issue only occurs when the custom script is executed before the form is fully ready to be accessed via Client API depending on many factors.

- In a JavaScript web resource, code is put into a global scope that is executed immediately when the web resource file is loaded without waiting for the form to be accessible. You should make sure the code is executed inside a valid form handler, such as an OnLoad handler.

- In a PCF control script file, Client API is accessed inside the init() or updateView() function. init() and updateView() are executed immediately when the control is loaded without waiting for the form to be readily accessible. Client API should not be used in PCF controls.

- In a web resource file, Client API is accessed inside a window.setTimeout() function. The page state is unpredictable when setTimeout() executes the wrapped function due to the nature of the timer function, so when the execution happens the page may be in a transitional state (during page load, or save) that's not readily accessible by Client API.

Using the [Monitoring Tool](https://docs.microsoft.com/powerapps/maker/model-driven-apps/monitor-form-checker), you can access information that will help determine when unsupported Client access occurs and when the access happens at the wrong time due to race condition.

The below sample event shows the callstack of the unsupported script (the callstack has been modified for demonstration purpose). The callstack tells what exact web resource, function and line and row number is causing this error.

![](media/2a1ae405c7bd93fbbb8799207e66dc0f.png)

This is caused by unsupported scripting. Follow up with the script owner to fix the problematic script code.

 ## "Save in Progress" error dialog

Please read through the overview section if you have not already done so to help familiarize you with the various tools and options to help troubleshoot your
issue.

### Symptom

When the form saves, you see this "Save in Progress" error dialog:

### Root Cause

The nature of this error is that another form save action is triggered before the previous save action is complete. This is not supported scripting and the error dialog is by design because calling save before save is complete would cause recursive save loops with unintended behaviors.

A typical (but not only) cause of this error is a script that calls save() in OnSave handler. Another possible cause is concurrent save() calls in setTimeout(), and which could cause the error dialog to intermittently show up, depending on whether the prior save() call is complete when another save() call
is made.

### How to troubleshoot

Below is a sample Form Checker monitor event (the callstack has been modified for demonstration purpose). The callstack tells what exact web resource,
function and line and row number is causing this error. Form Checker will NOT be able to detect this error when this issue is not reproducing.

![](media/0b55b3313b8735c64312f8eca34b9dbf.png)

This is caused by unsupported scripting. Please follow-up with the script owner to fix the problematic script code.

## The form / record is not saved when you try to save the form

Please read through the overview section if you have not already done so to help familiarize you with the various tools and options to help troubleshoot your
issue.

### Root Cause

A very common cause is an OnSave handler that has called executionContext.getEventArgs().preventDefault()  to cancel the save
operation.

### How to troubleshoot

Below is a sample Form Checker monitor event to explain why the save is canceled that's not explicit enough from the form UI itself:

![](media/d46e1fb8fccc5ea31719b6f1c90afd80.png)

Please follow-up with the script owner to fix or change the OnSave handler script.

## Form script errors

Please read through the overview section if you have not already done so to help familiarize you with the various tools and options to help troubleshoot your issue.

### Root Cause

If you see a form script error during form OnLoad, OnSave, OnChange, business rule execution, or other events, the error dialog itself may not contain
sufficient information to help troubleshooting.

### How to troubleshoot

For example, customer has onload handler, say "onload(controlName)", and they checked "Pass execution context as first parameter" option in the event handler editor in form designer. In their code:

```javascript
function onload(controlName)
{
  Xrm.Page.getControl(controlName);

}
```

This causes a problem because the first parameter for onload function is actually executionContext, however the script incorrectly uses it as control name for getControl(). Client API code thus throw this error:

![](media/dcf2e7127702a253e47ded5d8a3b2d51.png)

Once you launch Form Checker, you'll be able to see more details including the full callstack (the callstack has been modified for demonstration purpose) because callstack may be truncated if you're not in a monitor session which discloses the exact web resource and code location that causes this error.

![](media/c9564f8fd456df581bd310047908937a.png)

Please follow up with the owner of the problematic script to further root cause the issue.

## Form freezes or is very slow or throws unexplained errors

Please read through the overview section if you have not already done so to help familiarize you with the various tools and options to help troubleshoot your
issue.

### Symptoms

- Form is very slow

- Form throws unexplainable errors

- Form throws "Web resource method does not exist" script error

### Root Cause

There are many possible reasons a form freezes or is slow, or throws an error that is not a typical script error dialog. Some of the many possible reasons are:

1. It's not only slow or freezes on forms, it also occurs in other places such as sitemap / navigation pane, grids, or dashboards

2. Bad onload scripts

3. Web resource controls

4. Command button scripts and rules

5. Synchronous network requests

6. Custom plugins

7. Business Process Flow errors

This troubleshooting guide details these reasons which would help narrow down the troubleshooting scope.

### How to troubleshoot

Determine if the issue reproduces without involving forms. If it does, then there is a broader issue that should not be investigated by the forms team. Actual ownership of the issue depends on the particular details case by case.

If you believe this issue only occurs on forms, please refer to [Utilizing URL parameters to disable various form components](https://dynamicscrm.visualstudio.com/OneCRM/_wiki/wikis/OneCRM.wiki/9351/Form-Checker?anchor=utilizing-url-parameters-to-disable-various-form-components#utilizing-url-parameters-to-disable-various-form-components)"
to help narrow down the component that's causing the issue.

Also check for and fix synchronous network requests as described here:

- <https://powerapps.microsoft.com/blog/turbocharge-your-model-driven-apps-by-transitioning-away-from-synchronous-requests/> 

- <https://docs.microsoft.com//powerapps/developer/model-driven-apps/best-practices/business-logic/interact-http-https-resources-asynchronously> 

Please follow-up with the owner of the control to further troubleshoot the issue.

## Save in Progress error dialog

Please read through the overview section if you have not already done so to help familiarize you with the various tools and options to help troubleshoot your
issue.

When the form saves, and you see the "Save in Progress" informational dialog.

![](media/434bff84e7cb8fbe6cf42fa8e58003ec.png)

The nature of this dialog is that another form save action is triggered before the previous save action is complete. This is not supported, and is by design because calling save before save is complete would cause recursive save loops with unintended behaviors.

A typical (but not only) cause of this error is a script that calls save() in an OnSave handler. Another possible reason this can occur is if there are concurrent save() calls in setTimeout(). which could cause the error dialog to, intermittently show up, depending on whether the prior save() call is complete when another save() call is made.

Below is a sample from the [Monitoring Tool](https://docs.microsoft.com/powerapps/maker/model-driven-apps/monitor-form-checker)
for a form onSave event (the callstack has been modified for demonstration purpose). The callstack will include the web resource, function, and the line and row number when the error occurs.

![](media/0b55b3313b8735c64312f8eca34b9dbf.png)

This is caused by unsupported scripting. You will need to follow up with the script owner to fix the problematic script code.

## A record does not save

Please read through the overview section if you have not already done so to help familiarize you with the various tools and options to help troubleshoot your
issue.

A very common cause is an OnSave handler that has called *executionContext.getEventArgs().preventDefault()*  to cancel the save operation.

Below is a sample from the [Monitoring Tool](https://docs.microsoft.com/powerapps/maker/model-driven-apps/monitor-form-checker)
for the form onSave event that can help determine why the save is canceled when the error is not explicit enough from the UI.

![](media/d46e1fb8fccc5ea31719b6f1c90afd80.png)

You will need to follow up with the script owner to fix or change the OnSave handler script.

## Form script errors

Please read through the overview section if you have not already done so to help familiarize you with the various tools and options to help troubleshoot your
issue.

If you see a form script error during a form OnLoad, OnSave, OnChange, business rule execution, or other events, the error dialog itself may not have enough
information to help troubleshooting the issue.

For example, you have an onload handler, "onload(controName)", and have checked "Pass execution context as first parameter" option in the event handler editor
in form designer. In their code:

```javascript
function onload(controlName)
{
  Xrm.Page.getControl(controlName);
}
```

This causes a problem because the first parameter for onload function is actually executionContext, however the script incorrectly uses it as control
name for getControl().

The Client API code will throw this error:

![](media/dcf2e7127702a253e47ded5d8a3b2d51.png)

Once you launch the [Monitoring Tool](https://docs.microsoft.com/powerapps/maker/model-driven-apps/monitor-form-checker), you will be able to see more details including the full callstack. The monitoring tool will provide you more details that can help find the web resource and code location that caused the error.

![](media/c9564f8fd456df581bd310047908937a.png)

You will need to follow up with the script owner to further troubleshoot and resolve any issues identified in the call stack from the monitoring tool.

## Business rule or custom script is not working

Please read through the overview section if you have not already done so to help familiarize you with the various tools and options to help troubleshoot your
issue.

This can happen if a business rule/custom script used to work in web client, stopped working in Unified Client. One of the main reasons this can occur is when a business rule or script Unified Client is referencing a control that is not available in the Unified Interface.

An example of a common issue where this can happen is when a composite control is included in a script that exists in web client, but in the Unified Interface the composite control is broken down into parts and is stored this way. For example, if a field "fullname" is part of the business rule or custom script, the fields "firstname", "middlename" or "lastname" should be used instead.

Once you launch the [Monitoring Tool](https://docs.microsoft.com/powerapps/maker/model-driven-apps/monitor-form-checker), you'll be able to see more details including the composite control that is causing the problem, the fields that can be used in the business rule or custom script instead and a full callstack (the callstack has been modified for
demonstration purpose).

![](media/b3a9360f0b190d3f415515f3a2fa29e2.png)

You will need to follow up with the owner of the business rule or custom script to make the change to use controls suggested in the monitoring tool.

## Related Menu / Related tab

Please read through the overview section if you have not already done so to help familiarize you with the various tools and options to help troubleshoot your
issue.

There are many reasons why a related menu item doesn't show in the tab or have incorrect labels. Below is an example where you can use the [Monitoring Tool](https://docs.microsoft.com/powerapps/maker/model-driven-apps/monitor-form-checker)to check the RelatedMenu event.

In this example, it shows the reasons why a related entity "role" (Security Role) does not show in the "team" form is because "role" is not available in
Unified Client.

![](media/1d26002c9580f85cfd3e076d872a9c62.png)

There are also a few sources where a record can be included as an option the related menu tab. The following example includes details the indicate the label "Activities" in account form related menu comes from the related entity's plural display name.

![](media/9cb9236185c19789c4a3dd83b28a7ce0.png)

You will need to follow up with the owner of the related menu item indicated in the Related Menu event in the monitoring tool.

## Why a control is disabled / enabled / visible / hidden

There're many possible reasons why a control is disabled or hidden when the form loads. In the example below you can use the [Monitoring Tool](https://docs.microsoft.com/powerapps/maker/model-driven-apps/monitor-form-checker) to view the "FormControls" event will include details on the initial control
state as demonstrated below

![](media/7b467af8c691178678a2f122baeab225.png)

Another example is a "ControlStateChange" operation that explains why a control's disabled / visible state is changed by client Api or Business Rules. This can occur during a form load or triggered after the form is loaded using an onchange handler (the callstack has been modified for demonstration purpose). The details in the callstack will include the web resource, function and line and row number causing the control state change.

![](media/aa5b96b0f5bcb7883ed1a23274ccd088.png)

> [!NOTE]
> The difference between "FormControls" and "ControlStateChange" is that the former reflects the initial control state when the form loads, while the latter reflects the state change at any time on the form. For example, if a control is disabled for security reasons, it's very unlikely to be enabled after the form is loaded, so the initial state can be found in "FormControls" and not likely found in "ControlStateChange". Even if a Client API function tries to enable the control, it will not be effective, and you'll see "ControlStateChange" event of the disabled state change intention by the script without success, and you'll be able to find out why the intention is unsuccessful in "FormControls".

You will need to follow up with the owner of the web resource / business rules indicated in the state reason to change or fix the behavior.

## Why a tab or section is visible or hidden

There are many possible reasons why a tab or section hidden or visible. "TabStateChange" or "SectionStateChange" explains the visible state change as demonstrated below (the callstack has been modified for demonstration purpose). The callstack tells what exact web resource, function and line and row number is
causing the control state change.

![](media/64de8f308707b4e4045c930ac1e3a842.png)

You will need to follow up with the owner of the web resource / business rules indicated in the state reason to change or fix the behavior.

## Unexpected dialogs or navigation

There are many possible reasons why an expected dialog or navigation happens. One of the common causes is when you use the XrmNavigation Client API to open
another record or form. For example, when you open a form, an expected dialog as below is shown:

![](media/bc211907c97a0debf8e64e8f3f9b76b2.png)

The "XrmNavigation" event in the [Monitoring Tool](https://docs.microsoft.com/powerapps/maker/model-driven-apps/monitor-form-checker) will help you identify the script causing the unexpected behavior (the callstack has been modified for demonstration purpose). The callstack in the details of the event will include the web resource, function, line and row number causing the issue.

![](media/c0f67c573efc2b97d5dfa32b010bd916.png)

You will need to follow up with the owner of the web resource to change or fix the behavior.

## Example on how to troubleshoot a form

Below is an example of how you can use the tools outlined above to help troubleshoot an issue and solve problems using these troubleshooting tools.

### Issue: A form freezes when you try to open it

There're many reasons a form can be frozen, to narrow it down we'll try to leverage some of the URL flags to disable individual components and see if the
issue goes away.

- First use the **DisableFormCommandbar** flag. When you refresh or reload the page, notice the command bar / ribbon disappears. If the issue goes away, the problem is caused by some command customization. Next step is to further analyze individual commands to root cause the problem which is out of range of this document.

- If the issue still persists, use **DisableFormHandlers=true** flag. If the issue goes away, we'll further pinpoint the exact event handler function that's causing the problem.

- Assuming the form has 10 libraries, and 20 onload handlers, we can use binary search approach to narrow down the handler index range.

    - Open the [Monitoring Tool](https://docs.microsoft.com/en-us/powerapps/maker/model-driven-apps/monitor-form-checker) to view the registered form event handlers and libraries to get the list of onload handlers of indices ranging from 0 to 19 and form libraries of indices ranging from 0 to 9.

    - Use DisableFormHandlers=onload_0_9 which is more precise (or true_0_9 which might be a bit over killing but should also work for form load scenario) to see if the issue goes away. If it does, it proves the issue is caused by some handlers between index 0 and 9 (both included); otherwise, the issue is caused by handlers between index 10 and 19.

    - Assuming the issue is caused by handlers of index 0 to 9, use DisableFormHandlers=onload_0_4 (or true_0_4) to disable handlers of index between 0 and 4. Keep doing that until the range is small enough to loop through each one individually. Assuming the range is narrowed down to 3 to 4, use the DisableFormHandlers=onload_3, then onload_4 until you pinpoint the exact handler that's causing this problem.

    - Assuming the issue is caused by handler of index 3, read the event handler details obtained using the monitoring tool. If the handler is sampleOnloadHandler() in web resource foo.js in solution X by publisher Y. Follow up with the owner of the event handler to further analyze this issue.

- If the issue still persists, use **DisableFormLibraries=true** flag to disable all form libraries, and follow similar binary search approach if the amount of libraries is large, or just disable them one-by-one in a similar way we leverage DisableFormHandlers flag above.

- If the issue still persists, use **DisableWebResourceControls=true** flag to disable all web resource controls. If the issue goes away, use the **DisableFormControl** flag to further pinpoint the exact web resource control. Assuming the issue goes away with DisableFormControl=foo, and follow up with the control owner to do deeper troubleshooting.

- Continue turning off form components one-by-one with the appropriate URL parameters. The component that is disabled and makes the issue go away will be the component causing the problem. You should follow up with the owner of the component for further analysis.
