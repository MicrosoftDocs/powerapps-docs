---
title: "Design forms for performance in model-driven apps | MicrosoftDocs"
description: Learn how to customize forms for performance for your model-driven apps.
ms.custom: ""
ms.date: 08/27/2021
ms.reviewer: "Mattp123"
ms.service: powerapps
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "conceptual"
applies_to: 
  - "PowerApps"
author: "mspilde"
ms.subservice: mda-maker
ms.author: "mspilde"
manager: "kvivek"
search.audienceType: 
  - maker
search.app: 
  - "PowerApps"
  - D365CE
---
# Design forms for performance in model-driven apps

Building experiences where tasks can be completed quickly and efficiently is crucial to user satisfaction. Model-driven apps can be highly customized to create experiences that meet the needs of your users, but it is important to know how to effectively code, build, and run model-driven apps that load quickly when a user opens and navigates in your app while working on daily tasks. Performance has been shown to be a key driver of dissatisfaction of an app when it is not optimized for performance.

Intelligent customizations and performant forms are important aspects to building highly efficient and productive forms. It's also important to make sure you're building highly productive forms with the best practices in user interface design and layout. For information about designing forms for efficiency and productivity, see [Design productive main forms in model-driven apps](design-productive-forms.md). 

It is also important to ensure users are on recommended and supported devices and minimum required specifications. More information: [Supported web browsers and mobile devices](/power-platform/admin/supported-web-browsers-and-mobile-devices)

## Working with data and tabs

This section covers how controls that display data and tabs impact form performance.

### Significance of the default tab

The default tab is the first expanded tab on a form. It plays a special role in the loading of a form page. By design, the controls of the default tab are always rendered when opening a record. Specifically, the control initialization logic, such as data retrieval, is invoked for every control on the tab. In contrast, a secondary tab does not perform this initialization on its controls when the form is initially loaded. Instead, the control initialization occurs at the time the secondary tab is opened either through user interaction or calling the `setFocus` client API method. This provides an opportunity to shelter the initial form load from excessive control processing by placing certain controls in secondary tabs instead of the default tab. Thus, the control placement strategy can have a significant effect on the responsiveness of the initial form load. A more responsive default tab provides a better overall experience for modifying important fields, interacting with the command bar, and exploring other tabs and sections.

Always put controls that are used the most often at the top of your default tab.  Layout and information architecure is not only important for performance but also to improve productivity when users interact with data on the form.  More information [Design productive main forms in model-driven apps](design-productive-forms.md)

### Data driven controls

Controls that require extra data beyond the primary record produce the most strain on form responsiveness and loading speed. These controls fetch data over the network and often involve a waiting period (seen as progress indicators) as it can take time to transmit the data.

Some of the data driven controls include:

- Quick view form
- Subgrid
- Timeline
- Assistant

Keep only the most frequently used of these controls on the default tab. The remaining data driven controls should be distributed into secondary tabs to allow the default tab to load quickly. Furthermore, this layout strategy reduces the chance of fetching data that ends up being unused.

There are other controls that are less impactful than the data driven controls but can still participate in the above layout strategy in order to achieve the best performance. These controls include:

- Lookup
- iFrame
- Web Resource

## Web browser

This section covers good practices to use with web browsers.

### Don't open new windows

The `openForm` client API method allows a parameter option to display a form in a new window, don't use this parameter (or set it to false).  Setting it to false will ensure the   `openForm` method performs the default behavior of displaying the form using the existing window. It is also possible to directly call the `window.open` JavaScript function from a custom script or another application; however, this should also be avoided. Opening a new window means that all of the page resources need to be fetched and loaded from scratch since the page is unable to leverage most of the client caching capabilities between a previously loaded form and the form in a new window. As an alternative to opening new windows, consider using the multi-session experience that allows records to be opened in multiple tabs while still maximizing the performance benefits of client caching.

### Use modern browsers

Using the most up-to-date web browser is key to ensuring your model-driven app runs as fast as possible.  The reason for this is that many of the performance improvements can only be used in the newer modern browsers.

For example, if your organization older versions of Firefox, non-Chromium-based browsers, and so on, many of the performance gains that are built into a model-driven app will not be available in the older browser versions because they don't support features that the app depends on to run quickly and smoothly. Internet Explorer is no longer supported, please move to Edge or a modern browser.

In most cases, you can expect to see page load improvements by just switching to Microsoft Edge, updating to the latest current browser version from an older version, or moving to a modern Chromium-based browser.

## JavaScript customization

This section covers how to make intelligent customizations when you use JavaScript that help you build performant forms and pages in a model driven app.

### Using JavaScript with forms

The ability for forms to be customized by JavaScript provides professional developers great flexibility over how a form looks and behaves. The improper use of this flexibility can negatively impact form performance. Developers should use the following strategies to maximize form performance when implementing JavaScript customizations.

#### Use asynchronous network requests when requesting data

Request data asynchronously rather than synchronously when extra data is necessary for customizations. For events that support waiting for asynchronous code like the form `OnLoad` and form `OnSave` events, event handlers should return a `Promise` in order for the platform to wait until the `Promise` is settled. The platform will show an appropriate UI while the user waits for the event to complete.

For events that do not support waiting for asynchronous code, like the form `OnChange` event, you can use a workaround to stop interaction with a form while the code is doing an asynchronous request by using `showProgressIndicator`. This is better than using synchronous requests as users will still be able to interact with other parts of the application and see a progress indicator.

Here's an example using asynchronous code in synchronous extension points.

```javascript
//Only do this if an extension point does not yet support asynchronous code
Xrm.Utility.showProgressIndicator("Checking settings...")
Xrm.WebApi.retrieveRecord("settings_entity", "7333e80e-9b0f-49b5-92c8-9b48d621c37c").then(
	(data) => {
Xrm.Utility.closeProgressIndicator(); 
//do other logic with data here
	}, (error) => {
Xrm.Utility.closeProgressIndicator(); 
//do other logic with error here
});
```

Using asynchronous code is not recommended. Find other options to achieve the result. Asynchronous code can cause issues if the resolution handler expects the application context to remain the same as it was when the asynchronous code was started. Your code should check that the user is in the same context after each asynchronous continuation point. 

For example, there may be code in an event handler to make a network request and change a control to be disabled based on the response data. Before the response from the request is received, the user may have interacted with the control or navigated to a different page. Because the user is on a different page, the form context may not be available, which might lead to errors, or there might be other undesired behavior.

#### Async support in form Onload and form OnSave events

Starting in 2021 release wave 2, the form `OnLoad` and `OnSave` events support handlers returning promises. The events will wait for any promises returned by a handler to resolve, up to a timeout period.

More information:
- [Form OnLoad](/powerapps/developer/model-driven-apps/clientapi/reference/events/form-onload)
- [Form OnSave](/powerapps/developer/model-driven-apps/clientapi/reference/events/form-onsave)
- [Interact with HTTP and HTTPS resources asynchronously](/powerapps/developer/model-driven-apps/best-practices/business-logic/interact-http-https-resources-asynchronously)

#### Limit the amount of data requested during form load

Only request the minimum amount of data that is necessary to perform business logic on a form. Cache the data that is requested as much as possible, especially for data that doesn’t change often or doesn’t need to be fresh. For example, imagine there is a form that requests data from a *setting* table. Based on data in the setting table, the form might choose to hide a section of the form. In this case, the JavaScript can cache data in `sessionStorage` so that data is only requested once per session. A stale-while-revalidate strategy might also be used where the JavaScript uses the data from `sessionStorage` while requesting data for the next navigation to the form.


```javascript
const SETTING_ENTITY_NAME = "settings_entity";
const SETTING_FIELD_NAME = "settingField1";
const SETTING_VALUE_SESSION_STORAGE_KEY = `${SETTING_ENTITY_NAME}_${SETTING_FIELD_NAME}`;

// Retrieve setting value once per session
async function onLoad1(executionContext) {
    let settingValue = sessionStorage.getItem(SETTING_VALUE_SESSION_STORAGE_KEY);

    // Ensure there is a stored setting value to use
    if (settingValue === null || settingValue === undefined) {
        settingValue = await requestSettingValue();
    }

    // Do logic with setting value here
}

// Retrieve setting value with stale-while-revalidate strategy
async function onLoad2(executionContext) {
    let requestPromise;
    let settingValue = sessionStorage.getItem(SETTING_VALUE_SESSION_STORAGE_KEY);
    let settingValueRequested = false;

    // Ensure there is a stored setting value to use the first time in a session
    if (settingValue === null || settingValue === undefined) {
        settingValueRequested = true;
        settingValue = await requestSettingValue();
    }

    // Do logic with setting value here

    // Request setting value again but don't wait on it
    // In case there is a fast navigation to another page, don’t make the same request again if it is already in flight
    // Additional logic can be added so that this is done less than once per page
    if (!settingValueRequested && !requestPromise) {
        settingValueRequested = true;
        requestPromise = requestSettingValue().then(() => {
            requestPromise = undefined;
        });
    }
}

function requestSettingValue() {
    return Xrm.WebApi.retrieveRecord(
        SETTING_ENTITY_NAME,
        "7333e80e-9b0f-49b5-92c8-9b48d621c37c",
        `?$select=${SETTING_FIELD_NAME}`
    ).then(
        (data) => {
            try {
                sessionStorage.setItem(SETTING_VALUE_SESSION_STORAGE_KEY, data[SETTING_FIELD_NAME]);
            } catch (e) {
                // Handle  error
            } finally {
                return data[SETTING_FIELD_NAME];
            }
        },
        (error) => {
            // Handle error
        }
    );
}
```

Use information available in the client API rather than make requests. For example, rather than request a user’s security roles on form load, you can use [getGlobalContext.userSettings.roles](/powerapps/developer/model-driven-apps/clientapi/reference/xrm-utility/getglobalcontext/usersettings#securityroleprivileges).

#### Load code only when it’s needed

Load as much code as needed for events for a particular form. If you have code that is only for *form A* and *form B*, it shouldn't be included in a library that is loaded for *form C*. It should be in its own library.

Avoid loading libraries in the `OnLoad` event if they are only used for the `OnChange` or `OnSave` events. Instead, load them in those events. This way the platform can defer loading them until after the form loads. More information: [Optimize form performance](/dynamics365/customerengagement/on-premises/customize/optimize-form-performance)

## Tools you can use to help make apps performant

This section describes the tools that can help you understand performance issues and offer recommendations about how to optimize your customizations in model-driven apps.

### Performance insights

Performance insights is a self-service tool for enterprise app makers that analyzes runtime telemetry data and provides a prioritized list of recommendations to help improve the performance of model-driven apps. This feature provides a daily set of analytic insights related to the performance of a Power Apps model-driven or customer engagement app, such as Dynamics 365 Sales or Dynamics 365 Service, with recommendations and actionable items. Enterprise app makers can view detailed performance insights at an app-level in Power Apps. More information: [What are performance insights? (preview)](../common/performance-insights-overview.md)

### Solution Checker

Solution Checker is a powerful tool that can analyze client and server customizations for performance or reliability issues.  It can parse client-side JavaScript, form XML, and .NET server-side plugins and give targeted insights into what may slow end users down.  We recommend that you run Solution Checker each time you publish changes in a development environment, so that any performance concerns are surfaced before reaching end users. More information: [Use solution checker to validate your model-driven apps in Power Apps](../data-platform/use-powerapps-checker.md)

Some examples of performance-related issues found with solution checker:

- [il-specify-column](/powerapps/developer/data-platform/best-practices/work-with-metadata/retrieve-specific-columns-entity-via-query-apis?client=PAChecker&error=il-specify-column&source=featuredocs). Avoid selecting all columns via Dataverse query APIs.
- [web-use-async](/powerapps/developer/model-driven-apps/best-practices/business-logic/interact-http-https-resources-asynchronously?client=PAChecker&error=web-use-async&source=featuredocs). Interact with HTTP and HTTPS resources asynchronously.
- [web-avoid-ui-refreshribbon](https://go.microsoft.com/fwlink/?linkid=2157641&error=web-remove-console&client=PAChecker) Avoid using `refreshRibbon` in form `onload` and `EnableRule`.
More info here: Use solution checker to validate your apps in Power Apps - Power Apps | Microsoft Docs

### Object checker

Object checker runs real-time diagnostics on component objects within your solution. If issues are detected, a recommendation is returned that describes how to fix the issue. More information: [Use object checker to diagnose a solution component (preview)](../data-platform/object-checker.md)

### See also

[Design productive main forms in model-driven apps](design-productive-forms.md)
