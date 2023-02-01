---
title: "Debug JavaScript code for model-driven apps| MicrosoftDocs"
description: "Explains how to debug JavaScript code for model-driven apps"
ms.topic: "conceptual"
applies_to: 
  - "Dynamics 365 (online)"
author: adrianorth
ms.author: aorth
ms.date: 01/31/2023
ms.reviewer: jdaly
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
contributors: 
  - JimDaly
  - caburk
---
# Debug JavaScript code for model-driven apps

Custom logic using JavaScript in model-driven apps are contained within JavaScript web resources. The JavaScript web resources provide the libraries that define functions that developers register to handle events.

In a model-driven app viewed within a web browser, you can use developer tools that all modern browsers provide. With these tools you can locate the JavaScript libraries loaded in the model-driven application, set break points and debug your code using common methods.

> [!NOTE]
> With model-driven apps, because of the way that the libraries are added to the page, you may not easily find the library representing the JavaScript Web resource. These libraries may not be listed in the file list or in the hierarchy of source files.
> 
> If you know the name of the JavaScript web resource you want to debug, for Microsoft Edge or Google Chrome sources you can use the `Ctrl+P` **Open file** command to locate the file by name and start debugging. If you have a function that is causing an error, but you don't know the name of the file, see [Identify JavaScript web resource causing error](#identify-javascript-web-resource-causing-error).

More information:

- [mdn web docs: What are browser developer tools?](https://developer.mozilla.org/docs/Learn/Common_questions/What_are_browser_developer_tools).
- [Microsoft Edge Sources](https://learn.microsoft.com/microsoft-edge/devtools-guide-chromium/sources/)
- [Google Chrome Sources](https://developer.chrome.com/docs/devtools/sources/)
- [Mozilla Firefox JavaScript Debugger](https://firefox-source-docs.mozilla.org/devtools-user/debugger/index.html)
- [Apple Safari Debugger tab](https://support.apple.com/guide/safari-developer/debugger-tab-devfce7d9aed/mac)

## Identify JavaScript web resource causing error

When a JavaScript library causes a script error in a model-driven app, the following dialog appears:

:::image type="content" source="media/script-error-dialog.png" alt-text="Script error dialog":::

If you click the **Show Details** link, more details will be displayed similar to the following:

```
Xrm.Navigation.openalertDialog is not a function
Session Id: 53febd7c-3388-4ea5-a195-d84cf5883c30
Correlation Id: d154420e-5999-4250-b140-081f04a8e264
Event Name: onsave
Function Name: Example.formOnSave
Web Resource Name: example_example-form-script
Solution Name: Active
Publisher Name: DefaultPublisherYourOrg
Time: Tue Jan 31 2023 13:36:34 GMT-0800 (Pacific Standard Time)
```

In this case, the name of the function was incorrect, `openalertDialog` should be `openAlertDialog`

> [!NOTE]
> You can also get the same details on errors using Monitor. See [Custom script errors](../../../maker/monitor-modelapps.md#custom-script-errors)

## Debug JavaScript in Mobile apps

While developing JavaScript web resources for mobile scenarios, you can use your Android device to debug your mobile-specific code and ensure it works as expected.

> [!NOTE]
> It is not currently possible to debug devices using iOS.

### Configure your device

- Refer to the Android documentation to enable Developer options and USB debugging on your device. More information: [Android Developers: Configure on-device developer options](https://developer.android.com/studio/debug/dev-options)
- In the Microsoft Edge or Chrome browser, discover your Android device. More information: [Chrome Developers: Remote debug Android devices](https://developer.chrome.com/docs/devtools/remote-debugging/)

   - On Microsoft Edge: `edge://inspect/#devices`
   - On Chrome: `chrome://inspect/#devices`

> [!NOTE]
> Make sure that **Discover USB devices** is enabled.

### Configure the mobile application

1. In the mobile app, go to the list of Power Apps and select on the menu button.
1. Make sure that the toggle **Enable remote debugging for model-driven apps** is on.

   :::image type="content" source="media/field-service-mobile-app-settings.png" alt-text="Field service mobile app settings":::

1. When enabling this option, you'll have a confirmation dialog. Select **Confirm**.

   :::image type="content" source="media/field-service-mobile-app-settings-confirm-remote-debugging.png" alt-text="Confirm remote debugging dialog":::

### Debug from your development machine

1. Plug your computer to your Android device.
1. Open any model-driven app from Power Apps or the Field Service Mobile application
1. In the `edge://inspect/#devices` page in your browser, you'll be able to see the page available from the **Remote Target** section.

   :::image type="content" source="media/edge-inspect-devices.png" alt-text="Edge DevTools Devices screen":::

1. Click on **inspect**.


### See also

[JavaScript web resources](../script-jscript-web-resources.md)<br />
[Debug a model-driven app with Monitor](../../../maker/monitor-modelapps.md)<br />

[!INCLUDE[footer-include](../../../includes/footer-banner.md)]