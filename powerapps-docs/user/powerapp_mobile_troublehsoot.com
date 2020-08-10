---
title: "Power Apps Your device configuration is preventing sign-in| MicrosoftDocs"
ms.custom: ""
author: mduelae
manager: kvivek
ms.service: powerapps
ms.component: pa-user
ms.topic: conceptual
ms.date: 08/10/2020
ms.author: mduelae
ms.custom: ""
ms.reviewer: ""
ms.assetid: 
search.audienceType: 
  - enduser
search.app: 
  - PowerApps
  - D365CE
---
# Error message: Your device configuration is preventing sign-in

If you receive this message it means that your IT administrator is using Microsoft Intune and requires you to sign-in securely using an authenticator app, but your device configuration is blocking the Dynamics 365 mobile app from launching the authenticator app installed on your device. Microsoft authenticator apps are Authenticator and Company Portal. Your company may also use a third-party authenticator app. If you are unsure, ask your IT administrator which authenticator app you should be using and then follow the instructions below.

Sometimes, manually opening your authenticator app on your device before retrying to sign-in from the Dynamics 365 mobile app is enough to fix the issue.
 
If the suggestion above did not work, the steps to resolve the issue are device manufacturer-specific and depend which authenticator app you have installed.

For **Huawei** and **Honor** device, do the following:

1. Go to **Settings** > **Battery** > **App launch**. 

    > [!NOTE]
    > The **App launch** menu can have different names depending on the model and the operating version of your mobile device. If you   don’t see the **App launch** menu option, then look for one of the following menu options:
    > - **Close apps after screen lock** 
    > - **Applications** 
    > - **Background applications**

2. Under **Manage automatically** for the authenticator app set the toggle switch to **OFF**.
3. On the **Manage manually** screen ensure that **Secondary launch / Can be launched by other apps** is enabled. This will allow the Dynamics 365 mobile app to launch the app.

For **Vivo** device, do the following:

1. Go to **Settings** > **More Settings** > **Applications** > **Autostart**.
2. Set the toggle switch to **ON** for the authenticator app.

For other device manufacturers, please email Dynamics 365 Mobile Support dynmobisup@microsoft.com and include your device make and model, session ID and quote the error message above.
