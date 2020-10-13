---
title: Run apps in a web browser | Microsoft Docs
description: In this topic, you learn how to run apps in a web browser
author: mduelae
ms.service: powerapps
ms.component: pa-user
ms.topic: quickstart
ms.date: 10/11/2020
ms.author: mkaur
manager: "kvivek"
ms.custom: ""
ms.reviewer: ""
ms.assetid: 
search.audienceType: 
  - enduser
search.app: 
  - PowerApps
  - D365CE
---

# Run an app in a web browser
When you create an app, or someone shares an app with you, you can run that app on the Dynamics 365 mobile app or in a web browser on a tablet. In this topic, you'll learn how to run a canvas or model-driven app in a web browser on a tablet from the [Dynamics 365 Home page](https://home.dynamics.com).

For full functionality and optimized experience, we strongly recommend that you use the Dynamics 365 for phones and tablets mobile app. If you don't have the Dynamics 365 for phones and tablets app installed, you can still use the web browser on your tablet, as long as your device has sufficiently high screen resolution. For more information: [What's supported](https://docs.microsoft.com/dynamics365/mobile-app/support-phones-tablets#supported-devices-for-the-mobile-app).

> [!NOTE]
> Using the web browser on your phone to run your model-driven apps isn't supported; you must use the Dynamics 365 for phones app.

To follow this quickstart, you need:
- A Power Apps license. This is available with a Power Apps plan, such as the Power Apps per user plan, or [Power Apps trial](https://docs.microsoft.com/powerapps/maker/signup-for-powerapps), or any of the [Microsoft Office 365](https://signup.microsoft.com/Signup?OfferId=467eab54-127b-42d3-b046-3844b860bebf&dl=O365_BUSINESS_PREMIUM&ali=1) or [Dynamics 365](https://dynamics.microsoft.com/pricing/) plans that include Power Apps.
- Access to an app that you built or that someone else built and shared with you.
- Access to a supported web browser and operating system.
   - For canvas apps, see: [System requirements, limits, and configuration values](../maker/canvas-apps/limits-and-config.md)
   - For model-driven apps, see: [Requirements/supported configurations](https://docs.microsoft.com/power-platform/admin/online-requirements)


## Sign in to Dynamics 365
Sign in to Dynamics 365 at [https://home.dynamics.com](https://home.dynamics.com).

## Find an app on the Home page
The Home page may show several types of business apps, but you can find a specific app by typing part of its name in the search box. You can also filter the list to show only apps created by a specific source, such as Power Apps. To do this, select **Filter** and then select the source.

If you've recently installed the app, it might not immediately appear in the list of apps. Select **Sync** to show all your apps. This process may take up to a minute.

![](./media/run-app-browser/dynamics-365-home.png)


## Run an app from a URL
You can save an app's URL as a bookmark in your tablet's browser and run it by selecting the bookmark, or you can send a URL as a link through email. If someone else created an app and shared it with you in an email, you can run the app by selecting the link in the email. When running an app using a URL, you may be prompted to sign in using your Azure Active Directory credentials.

![](./media/run-app-browser/web-login.png)

## Connect to data
If an app requires a connection to a data source or permission to use the device's capabilities (such as the camera or location services), you must give consent before you can use the app. Typically, you're prompted only the first time.

![Connection](./media/run-app-browser/app-connection.png)

## Close an app
To close an app, sign out of the Dynamics 365 Home page, or open another app.

## Next steps
In this topic, you learned how to run a canvas or model-driven app in a web browser. To learn how to:
- run a canvas app on a mobile device, see [Run a canvas app on a mobile device](run-app-client.md)
- run a model-driven app on a mobile device, see [Run a model-driven app on a mobile device](run-app-client-model-driven.md)
- use a model-driven app, see [Use model-driven apps](use-model-driven-apps.md)

