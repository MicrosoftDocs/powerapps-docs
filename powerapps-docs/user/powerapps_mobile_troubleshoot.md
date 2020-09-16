---
title: "Troubleshoot issues for the Power Apps mobile app | MicrosoftDocs"
author: mduelae
manager: kvivek
ms.service: powerapps
ms.component: pa-user
ms.topic: conceptual
ms.date: 09/16/2020
ms.author: mduelae
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

**Common errors**

- **Your device configuration is preventing sign-in**
- **There was a problem signing you in**

**Resolution**

If you receive one of these messages it means that your IT administrator is using Microsoft Intune or requires you to sign-in securely using an authenticator app, but your device configuration is blocking the Power Apps mobile app from launching the authenticator app installed on your device. Microsoft authenticator apps are Authenticator and Company Portal. Your company may also use a third-party authenticator app. If you are unsure, ask your IT administrator which authenticator app you should be using and then follow the instructions below.

 > [!NOTE]
 > Power Apps requires a valid license to sign-in. For more information, see [Licensing overview](https://docs.microsoft.com/power-platform/admin/pricing-billing-skus).

Sometimes, updating and manually opening your authenticator app on your device before retrying to sign-in from the Power Apps mobile app is enough to fix the issue.
 
If the suggestion above did not work, the steps to resolve the issue are device manufacturer-specific and depend which authenticator app you have installed.

For **Huawei** and **Honor** device, do the following:

1. Go to **Settings** > **Battery** > **App launch**. 

    > [!NOTE]
    > The **App launch** menu can have different names depending on the model and the operating version of your mobile device. If you   don’t see the **App launch** menu option, then look for one of the following menu options:
    > - **Close apps after screen lock** 
    > - **Applications** 
    > - **Background applications**

2. Under **Manage automatically** for the authenticator app set the toggle switch to **OFF**.
3. On the **Manage manually** screen ensure that **Secondary launch / Can be launched by other apps** is enabled. This will allow the Power Apps mobile app to launch the app.

For **Vivo** device, do the following:

1. Go to **Settings** > **More Settings** > **Applications** > **Autostart**.
2. Set the toggle switch to **ON** for the authenticator app.

If the above does not resolve the issue, try this:

1. Back up your Microsoft Authenticator accounts. For more info, see [Back up and recover account credentials using the Microsoft Authenticator app](https://docs.microsoft.com/azure/active-directory/user-help/user-help-auth-app-backup-recovery)
2. Uninstall the Microsoft Authenticator app.
3. Uninstall the Power Apps mobile app.
4. Install Microsoft Authenticator again and add your back up accounts again.
5. Install the Power Apps mobile app.
6. Open the Power Apps mobile app and sign-in.

If you still can't sign-in please email us at pamobsup@microsoft.com and include your device make and model, session ID and quote the error message that you got on your screen.

## Pin to Home functionality is not supported using Safari for iOS 14

Safari for iOS 14 no longer supports the Power Apps mobile app **Pin to Home** functionality. This still works on on iOS 13 or ealier. 




## App icons are blank on iOS 14 or later

If your using an older version of Power Apps mobile on iOS 14 then app list icons are blank. To fix the issue, update your Power Apps mobile app to the latest version.

