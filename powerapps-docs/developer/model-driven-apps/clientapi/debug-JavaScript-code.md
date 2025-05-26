---
title: "Debug JavaScript code for model-driven apps"
description: "Explains how to debug JavaScript code for model-driven apps"
ms.topic: how-to
applies_to: 
  - "Dynamics 365 (online)"
author: sriharibs-msft
ms.author: srihas
ms.date: 01/31/2025
ms.reviewer: jdaly
search.audienceType: 
  - developer
contributors: 
  - JimDaly
  - caburk
---
# Debug JavaScript code for model-driven apps

Custom logic using JavaScript in model-driven apps is contained within JavaScript web resources. JavaScript web resources provide the libraries that define functions developers register as event handlers.

In a model-driven app viewed within a web browser, you can use developer tools that all modern browsers provide. With these tools you can locate the JavaScript libraries loaded in the model-driven application, set break points, and debug your code using common methods.

Model-driven apps viewed using mobile apps on Android, or the Windows desktop app require some more steps. See:

- [Debug JavaScript in mobile apps on Android](#debug-javascript-in-mobile-apps-on-android)
- [Debug JavaScript in mobile apps on iOS](#debug-javascript-in-mobile-apps-on-ios)
- [Debug JavaScript in the Windows desktop app](#debug-javascript-in-the-windows-desktop-app)

> [!NOTE]
> Because of the way that the libraries are added to the page, you may not easily find the library representing the JavaScript Web resource. These libraries may not be listed in the file list or in the hierarchy of source files.
> 
> If you know the name of the JavaScript web resource you want to debug, for Microsoft Edge or Google Chrome sources you can use the `Ctrl+P` **Open file** command to locate the file by name and start debugging. If you have an event handler that is causing an error, but you don't know the name of the file, see [Identify JavaScript web resource causing error](#identify-javascript-web-resource-causing-error).

More information:

- [Mdn web docs: What are browser developer tools?](https://developer.mozilla.org/docs/Learn/Common_questions/What_are_browser_developer_tools).

   - [Microsoft Edge Sources](/microsoft-edge/devtools-guide-chromium/sources/)
   - [Google Chrome Sources](https://developer.chrome.com/docs/devtools/sources/)
   - [Mozilla Firefox JavaScript Debugger](https://firefox-source-docs.mozilla.org/devtools-user/debugger/index.html)
   - [Apple Safari Debugger tab](https://support.apple.com/guide/safari-developer/debugger-tab-devfce7d9aed/mac)

## Identify JavaScript web resource causing error

When an event handler causes a script error in a model-driven app, the following dialog appears:

:::image type="content" source="media/script-error-dialog.png" alt-text="Script error dialog":::

If you select the **Show Details** link, you can find the details that include: event name, function name, web resource name, solution name, and publisher name.

```
Xrm.Navigation.openalertDialog is not a function
Session Id: 53febd7c-3388-4ea5-a195-d84cf5883c30
Correlation Id: aaaa0000-bb11-2222-33cc-444444dddddd
Event Name: onsave
Function Name: Example.formOnSave
Web Resource Name: example_example-form-script
Solution Name: Active
Publisher Name: DefaultPublisherYourOrg
Time: Tue Jan 31 2023 13:36:34 GMT-0800 (Pacific Standard Time)
```

In this case, the name of the function was incorrect, `openalertDialog` should be `openAlertDialog`

> [!NOTE]
> You can get the same details on errors using Monitor. More information: [Custom script errors](../../../maker/monitor-modelapps.md#custom-script-errors).

## Debug JavaScript in mobile apps on Android

While using JavaScript web resources for mobile scenarios, you can use your Android device to debug your mobile-specific code and ensure it works as expected.

To debug JavaScript in mobile apps on Android, you must complete the following three steps:

### 1. Configure your device

- Refer to the Android documentation to enable Developer options and USB debugging on your device. More information: [Android Developers: Configure on-device developer options](https://developer.android.com/studio/debug/dev-options)
- In the Microsoft Edge or Chrome browser, discover your Android device. More information: [Chrome Developers: Remote debug Android devices](https://developer.chrome.com/docs/devtools/remote-debugging/)

   - On Microsoft Edge: `edge://inspect/#devices`
   - On Chrome: `chrome://inspect/#devices`

> [!NOTE]
> Make sure that **Discover USB devices** is enabled.

### 2. Configure the mobile application

1. In the mobile app, go to the list of Power Apps and select on the menu button.
1. Make sure that the toggle **Enable remote debugging for model-driven apps** is on.
1. There's a confirmation dialog when you enable this option. Select **Confirm**.

### 3. Debug from your development machine

1. Plug your computer to your Android device.
1. Open any model-driven app from Power Apps or the Field Service Mobile application
1. In the `edge://inspect/#devices` page in your browser, find your organization URL in the **Remote Target** section.

   :::image type="content" source="media/edge-inspect-devices.png" alt-text="Edge DevTools Devices screen":::

1. Select on **inspect**.

More information: [Microsoft Edge: Remotely debug Android devices](/microsoft-edge/devtools-guide-chromium/remote-debugging/)

## Debug JavaScript in mobile apps on iOS

You can use Safari on a Mac to debug JavaScript web resources on iOS.

To debug JavaScript in mobile apps on iOS, you must complete the following two steps:

### 1. Configure the mobile application

1. In the mobile app, go to the list of Power Apps and select on the menu button.
1. Make sure that the toggle **Enable remote debugging for model-driven apps** is on.

### 2. Debug from your Mac
   
1. Connect your iPhone or iPad to your Mac.
1. Launch Safari on your Mac.
1. In the **Develop** menu, find your connected iPhone or iPad, and then look for **Power Apps** or **Field Service**.

More information: [Inspecting iOS and iPadOS | Apple Developer Documentation](https://developer.apple.com/documentation/safari-developer-tools/inspecting-ios)

## Debug JavaScript in the Windows desktop app

To debug JavaScript on Windows, you must first install the prerequisite applications.

- You must have a WebView2 runtime installed on your machine with a minimum version of 111. [Download the WebView2 Runtime](https://developer.microsoft.com/microsoft-edge/webview2/#download-section)
- You must install the Remote Tools for Microsoft Edge from the Microsoft Store: [Remote Tools for Microsoft Edge - Microsoft Store Apps](https://apps.microsoft.com/store/detail/remote-tools-for-microsoft-edge/9P6CMFV44ZLT)

### 1. Configure your Windows device

1. Enable Developer Mode.

   1. Open **Windows Settings** > **Privacy & security** > **For developers**.
   1. Enable **Developer Mode**.

1. Enable Device Portal.

   1. Open **Windows Settings** > **Privacy & security** > **For developers**.
   1. Enable **Device Portal**.
   1. Select **Yes** to install Windows Developer Mode package when prompted.
   1. Once Device Portal is enabled, **note the URL you will use to connect using localhost**. On most devices, it's `https://localhost:50080`  
   1. For debugging Power Apps / Field Service Mobile locally, you can continue with **Restrict to loopback connections only** enabled and **Authentication** disabled (otherwise you need to set a user password)

   Here's a screenshot summary of the recommended developer settings:

   :::image type="content" source="media/security-privacy-for-developers.png" alt-text="Enable device portal screen":::

### 2. Configure the Windows application

Configure the Power Apps or Field Service Windows desktop app for remote debugging.

Use the **Run command** (shortcut is `Windows + R`) and use the following deep link to launch the Windows app with special arguments.

- Power Apps: `ms-apps://?addWebView2AdditionalBrowserArgument=--enable-features=msEdgeDevToolsWdpRemoteDebugging`
- Field Service Mobile: `ms-apps-fs://?addWebView2AdditionalBrowserArgument=--enable-features=msEdgeDevToolsWdpRemoteDebugging`

### 3. Debug from Windows

1. Launch Power Apps or Field Service for Windows.
1. Open the Microsoft Edge browser and navigate to `edge://inspect`.
1. Use the **Connect to a remote Windows device** section and connect to `http://localhost:50080`. It takes a few seconds to connect, but you should see the organization URL.

   :::image type="content" source="media/devtools-configuration-for-windows.png" alt-text="Inspect in the DevTools screen":::

1. Select **inspect** and the DevTools opens.

### Related articles

[JavaScript web resources](../script-jscript-web-resources.md)   
[Debug a model-driven app with Monitor](../../../maker/monitor-modelapps.md)   
[Troubleshoot issues in the Power Apps mobile app](../../../mobile/powerapps-mobile-troubleshoot.md)

[!INCLUDE[footer-include](../../../includes/footer-banner.md)]
