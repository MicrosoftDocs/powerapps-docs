---
title: Run canvas and model-driven apps on a mobile device | Microsoft Docs
description: Learn how to run a canvas app or a custom model-driven app on a mobile device.
author: mduelae
ms.service: powerapps
ms.component: pa-user
ms.topic: quickstart
ms.date: 03/12/2020
ms.author: mkaur
ms.custom: ""
ms.reviewer: ""
ms.assetid: 
search.audienceType: 
  - enduser
search.app: 
  - PowerApps
  - D365CE
---

# Run canvas apps and model-driven apps on a mobile device

[!INCLUDE [cc-beta-prerelease-disclaimer](../includes/cc-beta-prerelease-disclaimer.md)]

When you create an app, or someone shares an app with you&mdash;either a canvas app or model-driven app&dash;you can run that app on iOS and Android devices by using the Power Apps mobile app. If you're on a Windows device, you can only run canvas apps; model-driven apps aren't supported on the Power App mobile app for Windows devices. In this topic, you'll learn how to get started and run a canvas app and a model-driven app on your mobile device. 

To learn how to use model-driven apps running on the Power Apps mobile app, see [User Guide for model-driven apps running on the Power Apps mobile app](use-custom-model-driven-app-on-mobile.md).

> [!IMPORTANT]
> Model-driven apps for Dynamics 365 Sales, Dynamics 365 Customer Service, Dynamics 365 Field Service, Dynamics 365 Marketing, and Dynamics 365 Project Service Automation<!--Via Dynamics Style Guide. If this sentence doesn't apply to all these products, maybe only mention Sales, Customer Service, and Field Service as you do in use-custom-model-driven-app-on-mobile.md? "Dynamics verticals" is out of brand.--> don't run in the Power Apps mobile app. Instead, you use the Dynamics 365 for phones and tablets app. More information: [User Guide for Dynamics 365 for phones and tablets](https://docs.microsoft.com/dynamics365/mobile-app/dynamics-365-phones-tablets-users-guide)

![Power Apps mobile](media/powerappsmobile.png "Power Apps mobile user interface")

Legend:

1. **Model-driven apps**
2. **Canvas apps**

**To sign up for the Power Apps mobile preview**

1. [Install Power Apps for iOS](https://go.microsoft.com/fwlink/?linkid=2125171) or [install Power Apps for Android](https://go.microsoft.com/fwlink/?linkid=2125172).
2. If you've already installed the app, the app you installed will be replaced by the preview version of the app.
3. Make sure to manually update to the latest version available, to benefit from the latest improvements. 
3. After you've installed the app, you can start testing. For any feedback, please reach out to us at [pamobsup@microsoft.com](mailto:pamobsup@microsoft.com). 

## Open Power Apps, and sign in

Open Power Apps on your mobile device, and sign in by using your Azure Active Directory credentials.

![Sign in to Power Apps](media/powerapps_mobile_app_signin_screen.png "Sign in to Power Apps")

If you have the Microsoft Authenticator app installed on your mobile device, simply enter your username when prompted, and then approve the notification sent to your device.


## Find the app

When you sign in to the app, the **My apps** filter is set by default. If you don't find the app you're looking for, you can open the **Power Apps** menu, and then select a different filter. 


![App filters](media/filter-menu.png "App filters")

The following filters are available:

* **All apps** : Displays all canvas apps and model-driven apps to which you have access, including apps you created and apps that others shared with you.

* **My apps**: For canvas apps, this displays canvas apps that you've opened, apps that you're the owner of, and apps that you can edit. For model-driven apps, this displays all model-driven apps that you have access to. 

* **Sample apps** (canvas apps only): Displays sample canvas apps from Microsoft that showcase real application scenarios with fictitious data to help you explore design possibilities.

* **Favorites** (canvas apps only): Displays canvas apps that you've marked by selecting the ellipsis (...) on the app tile, and then selecting **Favorite**. To remove an app from this list, select the ellipsis (...) on the app tile, and then select **Unfavorite**.

    ![Mark as Favorite](media/add_favorite_app.png "Mark as Favorite")

* **Featured apps** (canvas apps only): Displays canvas apps that your admin has marked as featured apps.

### Sort apps

After you filter your apps, you can sort the filtered list by the date the apps were most recently opened or modified, or alphabetically by name. These preferences are retained when you close and reopen apps. You can sort both canvas apps and model-driven apps.

![Sort menu](media/sort_apps.png "Sort menu")

### Search apps

If you know the name of the app you want to run, you can select the search icon at the top, and then type part of its name in the search box. You can search for both canvas apps and model-driven apps.

![Search for apps](media/search_apps.png "Search for apps")

If you filtered your apps, the filtered list will be searched.

### Refresh the list of apps

Select the refresh icon ![Refresh icon](media/refresh_icon.png) to refresh the list of apps. This will refresh the lists of both the canvas apps and model-driven apps. 

## Pin an app to the home screen

You can pin both canvas apps and model-driven apps to the home screen of your device for quick access. Select the ellipsis (...) on the app tile, select **Pin to Home**, and then follow the instructions that appear.

![Pin an app](media/pin_to_home.png "Pin an app")

## See non-production apps

By default, only production model-driven apps are shown in the list of apps.

To see model-driven apps from non-production environments, select the **Settings** menu ![Settings icon](media/settings_icon.png), and then turn on **Show non-production apps**. Follow the instructions that appear.

![Non-production apps toggle](media/non_prod_toggle.png "Non-production apps toggle")

## Run an app

To run an app on a mobile device, select the app tile. If someone else created an app and shared it with you in an email, you can run the app by selecting the link in the email.

### Run a canvas app

If this is the first time you're running canvas app by using the Power Apps mobile app, a screen shows the swipe gestures.

#### Close a canvas app

Use your finger to swipe from the left edge of the app to the right to close an app. On Android devices, you can also press the Back button and then confirm that you intended to close the app.

![Close an app](media/swipe.gif "Close an app")

#### Pinch and zoom in on a canvas app

![Pinch to zoom](media/pinchtozoom.jpg "Pinch to zoom")

#### Give consent to a canvas app

If an app requires a connection to a data source or permission to use the device's capabilities (such as the camera or location services), you must give consent before you can use the app. Typically, you're prompted only the first time you run the app.

![Give consent](media/give_consent_canvas.jpg "Give consent")

### Run a model-driven app 

The following image shows an example of a mode-driven app screen after you've signed in. To learn how to use model-driven apps running on the Power Apps mobile app, see [User Guide for model-driven apps running on the Power Apps mobile app](use-custom-model-driven-app-on-mobile.md). 

![Model-driven app home page](media/model-driven-app-opened.png "Model-driven app home page")

#### Give consent to a model-driven app

If an app requires a connection to a data source or permission to use the device's capabilities (such as the camera or location services), you must give consent before you can use the app. Typically, you're prompted only the first time you use the app.

![Give consent](media/give_consent.png "Give consent")

#### Close a model-drive app

Select the site map ![Site map icon](media/pa_mobile_sitemap_icon.png "Site map icon"), and then select **Apps**.

![Close a model-driven app](media/pa_mobile_close_app.png "Close a model-driven app")

## Known issues

We're still working through some known issues and will release fixes for them over time. Make sure to manually update to the latest preview build as soon as it's available. 

Some known issues include:

- No apps are displayed in the app list when you open the Power Apps app in offline mode
- Icons inside model-driven apps sometimes disappear.

