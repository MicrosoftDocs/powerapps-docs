---
title: "Troubleshoot issues for the Power Apps mobile app | MicrosoftDocs"
description: Troubleshooting and known issues for the Power Apps mobile app 
author: mduelae
manager: kvivek
ms.service: powerapps
ms.component: pa-user
ms.topic: conceptual
ms.date: 2/9/2021
ms.author: mkaur
ms.custom: ""
ms.reviewer: ""
ms.assetid: 
search.audienceType: 
  - enduser
search.app: 
  - PowerApps
---

# Troubleshoot issues for the Power Apps mobile app

This troubleshooting article helps fix common issues for the [Power Apps mobile app](run-canvas-and-model-apps-on-mobile.md).

## Sign in issues

### Unable to sign in due to issues with the Microsoft Authenticator app 

If you don’t have the Microsoft Authenticator app, download the app from the App Store or Play Store and then sign in to the Power Apps mobile again.

If you already have the Microsoft Authenticator app installed and you're having sign in issues, then try these steps:

1. Back up your Microsoft Authenticator account. For more information, see [Back up and recover account credentials using the Microsoft Authenticator app](https://docs.microsoft.com/azure/active-directory/user-help/user-help-auth-app-backup-recovery)
2. Uninstall the Microsoft Authenticator app.
3. Uninstall the Power Apps mobile app.
4. Reinstall the Microsoft Authenticator app and add your back up account.
5. Reinstall the [Power Apps mobile](https://docs.microsoft.com/powerapps/mobile/run-powerapps-on-mobile#install-power-apps-mobile-app).
6. Open Power Apps mobile and then sign in.


### Other sign in errors 

Sign in errors: 
- **Your device configuration is preventing sign in**
- **There was a problem signing you in**


If you receive one of these messages it means that your IT administrator is using Microsoft Intune or requires you to sign in securely using an authenticator app, but your device configuration is blocking the Power Apps mobile app from launching the authenticator app that's installed on your device. Microsoft authenticator apps are Authenticator and Company Portal. Your company may also use a third-party authenticator app. If you're not sure, ask your IT administrator which authenticator app you should be using and then follow the instructions below.

 > [!NOTE]
 > Power Apps requires a valid license to sign in. For more information, see [Licensing overview](https://docs.microsoft.com/power-platform/admin/pricing-billing-skus).

Sometimes, updating and manually opening your authenticator app on your device before trying to sign in on the Power Apps mobile app can fix the issue.
 
If the suggestion above did not work, the steps to resolve the issue are device and manufacturer-specific and also depends on which authenticator app you have installed.

**Huawei or Honor device**

1. Go to **Settings** > **Battery** > **App launch**. 

    > [!NOTE]
    > The **App launch** menu can have different names depending on the model and the operating version of your mobile device. If you   don’t see the **App launch** menu option, then look for one of the following menu options:
    > - **Close apps after screen lock** 
    > - **Applications** 
    > - **Background applications**

2. Under **Manage automatically**, on the authenticator app set the toggle switch to **OFF**.
3. On the **Manage manually** screen ensure that **Secondary launch / Can be launched by other apps** is enabled. To allow the Power Apps mobile app to launch the app.

**Vivo device**

1. Go to **Settings** > **More Settings** > **Applications** > **Autostart**.
2. Set the toggle switch to **ON** for the authenticator app.

If the above does not resolve the issue, try these steps:

1. Back up your Microsoft Authenticator accounts. For more info, see [Back up and recover account credentials using the Microsoft Authenticator app](https://docs.microsoft.com/azure/active-directory/user-help/user-help-auth-app-backup-recovery)
2. Uninstall the Microsoft Authenticator app.
3. Uninstall the Power Apps mobile app.
4. Install Microsoft Authenticator again and add your back up accounts again.
5. Install the Power Apps mobile app.
6. Open the Power Apps mobile app and sign in.

If you still can't sign in, then email us at pamobsup@microsoft.com and include your device make and model, session ID, and provide the exact error message that you get.

## Pin to Home does not work on iOS 14

If you're on an iOS device running iOS 14, the Safari browser no longer supports the **Pin to Home** functionality from the Power Apps mobile app. You will need to use the Siri Shortcuts app to pin an app to the home screen. For more information, see [Use Siri Shortcuts (iOS 14 or later)](https://docs.microsoft.com/powerapps/user/run-canvas-and-model-apps-on-mobile#use-siri-shortcuts-to-pin-home-ios-14-or-later).

If you're still on iOS 13, you can continue to use the Safari browser to pin an app to the Home screen. For more information, see [Pin an app to the home screen](https://docs.microsoft.com/powerapps/user/run-canvas-and-model-apps-on-mobile#use-safari-to-pin-to-home-ios-13-or-earlier)

## App list appears blank on the Power Apps mobile app

Common scenarios the list of apps on the Power Apps mobile app appears blank when you disconnect or lose internet connection. 

-	First time signing in to Power Apps mobile and the list of apps is loading.
-	You’re signed in and see your apps and then swipe down on the list of apps to refresh the app list.
-	You’re coming back online from working in offline mode.

In all of these scenarios, the download is interrupted when internet connection is lost and the apps don't fully download. This is why the list of apps appear blank.

To work around this issue, don’t disconnect from the internet and let the app list fully download before disconnecting from the internet.




