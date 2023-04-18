---
title: Troubleshoot issues in the Power Apps mobile app
description: Troubleshooting and known issues for the Power Apps mobile app 
author: sericks007

ms.component: pa-user
ms.topic: conceptual
ms.date: 03/15/2023
ms.subservice: mobile
ms.author: sericks
search.audienceType: 
  - enduser
---

# Troubleshoot issues in the Power Apps mobile app

This troubleshooting article helps fix common issues for the [Power Apps mobile app](../mobile/run-powerapps-on-mobile.md).

> [!NOTE]
> If you are having an issue with Power Apps for iOS or Android and you don't find a solution on this page, please send a description of your issue with a screenshot and session ID to [pamobsup@microsoft.com](mailto:pamobsup@microsoft.com?subject=Power%20Mobile%20issues). Comments on this page are not received by the support team.

## Error: A major update is available. Upgrade your app to the latest version to keep your app working. If you are unable to upgrade, contact your administrator.

A major update to the Power Apps offline sync engine has been made. To keep your app working, [upgrade to the latest version of the Power Apps mobile app](run-powerapps-on-mobile.md). You must be running one of the following versions or later:

-   Android: 3.23031.18
-   iOS: 13.23031.18
-   Windows: 3.23024.21

If you are unable to upgrade, contact your administrator.

## Diagnose mobile apps with Monitor

Monitor is a tool that offers makers a deep view of what an app does and how it does it by logging all key activities that occur in the app as it runs. You can [connect a mobile app session to Monitor](../maker/monitor-canvasapps.md#for-apps-running-on-power-apps-mobile-preview) to better diagnose and troubleshoot issues faster.

## Debug JavaScript web resources in mobile apps

While developing JavaScript web resources for mobile scenarios, you can use your Android device to debug your mobile-specific code and ensure it works as expected. More information: [Debug JavaScript in mobile apps on Android](../developer/model-driven-apps/clientapi/debug-JavaScript-code.md#debug-javascript-in-mobile-apps-on-android).

## Error: There was a problem signing you in

You are unable to sign in due to issues with the Microsoft Authenticator app.

If you don't have the Microsoft Authenticator app, download the app from the App Store or Play Store and then sign in to Power Apps mobile again.

If you already have the Microsoft Authenticator app installed and you're having sign in issues, then try these steps:

1. Back up your Microsoft Authenticator account. For more information, see [Back up and recover account credentials using the Microsoft Authenticator app](/azure/active-directory/user-help/user-help-auth-app-backup-recovery)
2. Uninstall the Microsoft Authenticator app.
3. Uninstall Power Apps mobile.
4. Reinstall the Microsoft Authenticator app and add your back up account.
5. Reinstall [Power Apps mobile](../mobile/run-powerapps-on-mobile.md).
6. Open Power Apps mobile and then sign in.

## Error: Your device configuration is preventing sign in

If you get this error messages, it means your company's IT department requires Microsoft Intune or an authentication app to sign in securely. However, your device setup is blocking Power Apps mobile from launching the authentication app that's installed on your device.

Microsoft authentication apps are Authenticator and Company Portal. Your company may use a third-party authentication app. If you're not sure, ask your IT department or help desk which authentication app to use. Once you have the correct authentication app, then follow the steps below.

 > [!NOTE]
 > Power Apps requires a valid license to sign in. For more information, see [Licensing overview](/power-platform/admin/pricing-billing-skus).

Sometimes, updating and manually opening the authentication app on your device before signing in to Power Apps mobile can fix the problem. If this doesn't fix the issue, then follow the next steps depending on your device manufacturer and authentication app.

### Huawei or Honor device

1. Go to **Settings** > **Battery** > **App launch**.

    > [!NOTE]
    > The **App launch** menu can have different names depending on the model and the operating version of your mobile device. If you   don't see the **App launch** menu option, then look for one of the following menu options:
    > - **Close apps after screen lock** 
    > - **Applications**
    > - **Background applications**

2. Under **Manage automatically**, on the authenticator app set the toggle switch to **OFF**.
3. On the **Manage manually** screen ensure that **Secondary launch / Can be launched by other apps** is enabled. To allow the Power Apps mobile app to launch the app.

### Vivo device

1. Go to **Settings** > **More Settings** > **Applications** > **Autostart**.
2. Set the toggle switch to **ON** for the authenticator app.

If the issue is still not fixed, then try these steps:

1. Back up your Microsoft Authenticator accounts. For more info, see [Back up and recover account credentials using the Microsoft Authenticator app](/azure/active-directory/user-help/user-help-auth-app-backup-recovery) 
2. Uninstall the Microsoft Authenticator app.
3. Uninstall Power Apps mobile.
4. Install Microsoft Authenticator again and add your back up accounts again.
5. Install [Power Apps mobile](../mobile/run-powerapps-on-mobile.md).
6. Open Power Apps mobile and sign in.

If you still can't sign in, then email us at pamobsup@microsoft.com and include your device make and model, session ID, and provide the exact error message that you get.

## App list is empty

The app list in the Power Apps mobile app may appear empty when you lose internet connection before the app list has completely downloaded. This can happen in any of the following scenarios:

- It's the first time you're signing in to the mobile app.
- When you pull down to refresh the app list.
- When you come back online after a period of being offline. The app list is automatically refreshed.

To resolve connection related issues, ensure you remain connected to the internet while the app list is fully downloaded.

## Pin to Home does not work on iOS 14

**iOS device running iOS 14**: The Safari browser no longer supports the **Pin to Home** functionality for Power Apps mobile. You need to use the Siri Shortcuts app to pin an app to the Home screen. For more information, see [Use Siri Shortcuts (iOS 14 or later)](../mobile/run-powerapps-on-mobile.md#use-siri-shortcuts-to-add-a-shortcut-to-the-home-screen-ios-14-or-later).

**iOS 13**: You can still use the Safari browser to pin an app to the Home screen. For more information, see [Pin an app to the home screen](../mobile/run-powerapps-on-mobile.md#use-safari-to-add-a-shortcut-ios-13-or-earlier)

## App resets when running it on Power Apps mobile

When you run a canvas or model-driven app on Power Apps mobile, it can reset if the app is using too many resources. If the app uses more resources than are available on your device, the app will reset. This is similar to when you visit a large, complex webpage and the web browser suspends the page because it is consuming too much power.

On Android devices, this app restart can look like a crash because the app is completely closed and the user is taken to the home screen of the device.

If you experience a reset while using a canvas app, contact your app developer, and see [Prevent canvas app restarts](../mobile/power-apps-mobile-canvas-app-restarts.md).

## Unable to download SharePoint attachment in the mobile app

The Power Apps platform does not support accessing authenticated URLs, including SharePoint attachments. If you run a Power Apps application in a web browser and it tries to access a SharePoint attachment, it may work if you are signed-in to SharePoint in another tab. This is because web browsers support multiple signed-in users, and sign-ins are valid across browser tabs. However, the Power Apps mobile app is not a web browser, so does not benefit from this browser-based behavior.

## Power Automate Flow menu opens a blank Login to Flow screen on iOS 14

If you encounter a blank **Login to Flow** page when using the Power Automate Flow menu in a Power Apps on mobile, enable **Allow Cross-Website Tracking** in **iOS Settings** > **Power Apps** and open the app again.

## Flows created in a solution are not supported on Power Apps mobile

The Flow action menu in Power Apps mobile doesn't support flows created in a solution.

## Network requests fail when Power Apps mobile app is running in the background

When Power Apps mobile app is running in the background and a canvas or model driven app makes a network request, a mobile operating system could deprioritize or cancel this network request. This can cause an error toast to appear in the mobile the app when it returns from the background. 

If you experience a failed network request when the Power Apps mobile app is running in the background, contact your app developer.

### See also  

[Power Pages known issues](/power-pages/known-issues)

[Power Automate known issues](/power-automate/process-advisor-issues)

[!INCLUDE[footer-include](../includes/footer-banner.md)]
