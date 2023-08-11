---
title: Install the Power Apps mobile app
description: Learn how to install and run a canvas or model-driven app on a mobile device.
author: trdehove

ms.component: pa-user
ms.topic: quickstart
ms.date: 03/16/2023
ms.subservice: mobile
ms.author: trdehove
ms.reviewer: sericks
ms.assetid: 
search.audienceType: 
  - enduser
searchScope:
  - "Power Apps"
ms.collection: get-started
contributors:
- makolomi
---

#  Install the Power Apps mobile app

If you're not signed up for Power Apps, [sign up for free](https://make.powerapps.com/signup?redirect=marketing&email=). Then choose the download link or scan a QR code to download Power Apps mobile.


| iOS | Android | Windows |
| :---:         |     :---:      |          :---: |
| [![Download Power Apps from the Apple App Store.](media/app-store-icon.png "Download Power Apps from the Apple App Store")](https://itunes.apple.com/app/powerapps/id1047318566?mt=8)   | [![Download Power Apps from Google Play.](media/play-store-android-icon.png "Download Power Apps from Google Play")](https://play.google.com/store/apps/details?id=com.microsoft.msapps)     | [![Download Power Apps from Windows Store.](media/windows-store-icon.png "Download Power Apps from Windows Store")](https://www.microsoft.com/store/apps/9MVC8P1Q3B29)   |
| ![Download Power Apps from the Apple App Store using the QR code.](media/qr-code-ios.png "Download Power Apps from the Apple App Store using the QR code")    |  ![Download Power Apps from Google Play using the QR code.](media/qr-code-android.png "Download Power Apps from Google Play using the QR code")      | ![Download Power Apps from Windows Store using QR the code.](media/qr-code-windows.png "Download Power Apps from Windows Store using the QR code")    |

> [!NOTE]
>  For more information on Power Apps for Windows, see [Power Apps for Windows](windows-app-install.md).

## Required privileges and supported devices

Review the following privileges and supported devices to run Power Apps Mobile app:

- [Required privileges](/dynamics365/mobile-app/set-up-dynamics-365-for-phones-and-dynamics-365-for-tablets#required-privileges)
- [Supported platforms for running apps using the Power Apps mobile app](../limits-and-config.md#supported-platforms-for-running-apps-using-the-power-apps-mobile-app)

## Sign in

Open Power Apps on your mobile device, and sign in by using your Azure Active Directory credentials.

If you have the Microsoft Authenticator app installed on your mobile device, enter your username when prompted, and then approve the notification sent to your device. If you run into issues signing in, see [Troubleshoot issues for Power Apps mobile app](powerapps-mobile-troubleshoot.md).

![Sign in to Power Apps.](media/powerapps_mobile_app_signin_screen.png "Sign in to Power Apps")
    
## Find the app
  
When you create an app, or someone shares an app with you&mdash;either a [canvas app](../maker/index.md#canvas-apps) or [model-driven](../maker/index.md#model-driven-apps) app&mdash;you can run that app on Power Apps mobile. 
   
> [!NOTE]
> To see a model-driven app in the list of apps on Power Apps mobile, you need to have a [predefined security role](/power-platform/admin/database-security#predefined-security-roles) in the environment that the app is in. If a predefined security role is assigned to a user using a Dataverse team, you need to use an Azure Active Directory (AAD) group team. Users will not see model-driven apps if a predefined security role is assigned using a Dataverse owner team.
  
![Power Apps mobile user interface with model-driven and canvas apps.](media/powerappsmobile-1.png "Power Apps mobile user interface with model-driven and canvas apps")

Legend:

1. **Model-driven apps**
2. **Canvas apps**  


The apps that you used recently will show on the default screen when you sign in to Power Apps mobile.
  
The **Home** is the default screen when you sign in. It shows the apps that you used recently and the apps that have marked as favorites. 

![Default Home screen.](media/default-home-screen.png "Default Home screen")

## Filter apps 

If you don't have any apps, then when you sign in, you will land on the **All apps** screen. The list of apps is organized in alphabetical order. Type in an app name in the search bar to find an app.

![Filter and find apps.](media/app-list-2.png "Filter and find apps")  

1. **Settings**: Access app settings and sign out.
2. **Search**: Use the search to search for apps. When you run a search, it will only search for apps that are on the screen you're on.
3. **Favorites** (canvas apps only): Displays canvas apps that you have pinned to favorites.
4. **Recent apps**: Displays both model-driven and canvas apps that you have recently used.
5. **Home**: Displays favorite apps and recently accessed apps sorted by open date.
6. **All apps**: Displays all canvas apps and model-driven apps to which you have access, including apps you created and apps that others shared with you.
7. **More** (canvas apps only): Displays featured and sample apps.
8. **Details**: View information about the app including run the app, add a shortcut for the app, and add the app to favorites.
9. **Sort apps**: You can short by the app name or modified date. </li> 
  
## Add to favorites

You can only add canvas apps to your list of favorite apps.

- Swipe left and then select **Favorite**. A yellow star will appear next to app name when it's added to favorites. You can also select **Details** ![Details button.](media/detailsbutton.png) and then add the app to favorites.

   > [!div class="mx-imgBorder"]
   > ![Add to list of favorites.](media/add-to-favs-1-1.png "Add to list of favorites")     

- To remove the app from the list, swipe left again and then select **Unfavorite**.

   > [!div class="mx-imgBorder"]
   > ![Remove the app from the list.](media/add-to-favs-1-2.png "Remove the app from the list")     

## Sort apps

You can sort both canvas apps and model-driven apps. 
You can sort apps alphabetically by name or by modified date. The sort option is available on **Home**, **All apps**, **Featured apps**, and **Sample apps** screen.

![Sort menu.](media/sort-apps-iphone.png "Sort menu")

## Search apps

If you know the name of the app that you want to run, then use search to quickly find the app. You can search for both canvas apps and model-driven apps.

To find an app, enter the app name in the search field. The app will only search for apps that are on the screen you're on.

![Search for your app.](media/search_apps-1.png "Search for your app")

## Refresh the list of apps

On the **Home**, **All apps** or any other screen with a list of apps, swipe down to refresh the app list.

   > [!div class="mx-imgBorder"]
   >![Refresh the app list.](media/refesh-apps-iphone.png)

## Add shortcuts

You can add a shortcut for both canvas apps and model-driven apps to the home screen of your device for quick access.

### Use Safari to add a shortcut (iOS 13 or earlier)

1. On the app that you want to create a shortcut for, swipe to the right and select **Shortcut**.

     > [!div class="mx-imgBorder"]
     > ![Select shortcut.](media/add-shortcut-iphone.png "Select shortcut") 

2. Select ![Pin an app on iPhone button.](media/add-to-home-button.png "Pin an app on iPhone button").
 
   > [!div class="mx-imgBorder"]
   > ![Pin an app on iPhone.](media/pin_to_home_1.png "Pin an app on iPhone") 
   
3. Scroll down and select **Add to Home Screen**   

   > [!div class="mx-imgBorder"]
   > ![Add to Home Screen.](media/pin_to_home_2.png "Add to Home Screen") 
   
4. Select **Add**.   

   > [!div class="mx-imgBorder"]
   > ![Select Add to add to Home screen.](media/pin_to_home_3.png "Select Add to add to Home screen") 
   
> [!NOTE]
> For iOS devices that have multiple browsers installed, use Safari when pinning an app to home. 

### Use Siri shortcuts to add a shortcut to the Home screen (iOS 14 or later) 

The Power Apps mobile app is now integrated with Siri shortcuts, which gives you the ability to add a shortcut to the Home screen, launch apps with Siri, and create new workflows. For more information on how shortcuts work on iOS, see [Shortcuts User Guide](https://support.apple.com/guide/shortcuts/welcome/ios). This feature requires Power Apps mobile version 3.20092.x or later.

Users on iOS 14 or later can use Siri Shortcuts to pin an app to the home screen. The new experience works for both model-driven and canvas apps. When you add a Siri shortcut, the app is added to the iOS **Shortcuts** app and from there you can add the app to your home screen.

1. On the app that you want add a shortcut for, swipe to the right and select **Shortcut**.

    > [!div class="mx-imgBorder"]
    > ![Select shortcut.](media/add-shortcut-iphone.png "Select shortcut") 
   
3. Add a custom phrase to open the app using voice commands and then select **Add to Siri**.

   > [!div class="mx-imgBorder"]
   >![Select Add to Siri.](media/add-shortcut-1.png "Select Add to Siri")
   
4. The app is added to the **Shortcuts** app on your mobile device. Open the **Shortcuts** app and select the ellipsis (...) above the app name.

   > [!div class="mx-imgBorder"]
   > ![Select the ellipsis to add a shortcut.](media/add-short-2.png "Select the ellipsis] to add shortcut")

5. Select **Add to Home Screen**.

   > [!div class="mx-imgBorder"]
   > ![Select Add to Home Screen.](media/add-to-homescreen.png "Select Add to Home Screen")
   
6. On the upper right corner, select **Add** and then select **Done**. 

   > [!div class="mx-imgBorder"]
   >![Select Add.](media/add-shortcut-3.png "Select Add")
   
7. Go to your home screen to find the pinned app.   
  
   > [!div class="mx-imgBorder"]
   > ![App shortcut on home screen.](media/add-shortcut-4.png "App shortcut on home screen")

You can customize the shortcut icon but it is limited to the customization options in iOS. For more information, go to [Modify shortcut icons](https://support.apple.com/guide/shortcuts/modify-shortcut-icons-apd5ad5a2128/ios).

### Pin to home on Android 

Select the ellipsis (...) on the app tile, select **Pin to Home**, and then follow the instructions that appear.

![Pin an app.](media/pin_to_home.png "Pin an app")  

## See non-production apps

By default, only production model-driven apps are shown in the list of apps.

To see model-driven apps from non-production environments, select the **Settings** menu ![Settings button](media/settings_icon-1.png), and then turn on **Show non-production apps**. Follow the instructions that appear.

![Non-production apps toggle.](media/non_prod_toggle.png "Non-production apps toggle")

## Run an app

To run an app on a mobile device, select the app tile. If someone else created an app and shared it with you in an email, you can run the app by selecting the link in the email.

### Run a canvas app

If this is the first time you're running a canvas app by using Power Apps mobile, a screen shows the swipe gestures.

#### Close a canvas app

Use your finger to swipe from the left edge of the app to the right to close an app. On Android devices, you can also press the Back button and then confirm that you intended to close the app.

![Close an app.](media/swipe.gif "Close an app")

#### Pinch and zoom in on a canvas app

![Pinch to zoom.](media/pinchtozoom.jpg "Pinch to zoom")

#### Give consent to a canvas app

If an app requires a connection to a data source or permission to use the device's capabilities (such as the camera or location services), you must give consent before you can use the app. Typically, you're prompted only the first time you run the app.

![Give consent to a canvas app.](media/give_consent_canvas.jpg "Give consent to canvas app")

### Use a model-driven app 

The following image shows an example of a model-driven app screen after you've signed in. To learn how to use model-driven apps running on Power Apps mobile, go to [Use model-driven apps on Power Apps mobile](use-custom-model-driven-app-on-mobile.md). 

![Model-driven app home page.](media/model-driven-app-opened.png "Model-driven app home page")

#### Give consent to a model-driven app

If an app requires a connection to a data source or permission to use the device's capabilities (such as the camera or location services), you must give consent before you can use the app. Typically, you're prompted only the first time you use the app.

![Give consent.](media/give_consent.png "Give consent")

#### Close a model-drive app

Select the site map ![Site map icon.](media/pa_mobile_sitemap_icon.png "Site map icon"), and then select **Apps**.

![Close a model-driven app.](media/pa_mobile_close_app.png "Close a model-driven app")

>[!Note]
> An app maker can customize the navigation bar and show or hide the **Home**, **Recent**, **Pinned** buttons in the site map. An app maker can also make groups collapsible. For more information, see [Hide or show the Home, Pinned, Recent, and collapsible groups](../user/navigation.md#hide-or-show-the-home-pinned-recent-and-collapsible-groups).

## Other mobile apps

The table below outlines which other mobile apps you can use to run your app.

| **Mobile App** | **Apps you can run** |
|-------------------------|-------------------------|
| [Power Apps mobile](run-powerapps-on-mobile.md) (covered in this topic) | <ul><li>[Model-driven apps](../maker/index.md#model-driven-apps)</li><li>[Canvas apps](../maker/index.md#canvas-apps)</li><li>[Dynamics 365 Marketing](/dynamics365/marketing/help-hub)</li><li>[Dynamics 365 Customer Service](/dynamics365/customer-service/help-hub)</li></ul> |
| [Power Apps for Windows](windows-app-install.md) | <ul><li>[Model-driven apps](../maker/index.md#model-driven-apps)</li><li>[Canvas apps](../maker/index.md#canvas-apps)</li></ul> |
| [Dynamics 365 for phone and tablets](/dynamics365/mobile-app/overview) | <ul><li>[Microsoft Dynamics 365 Customer Engagement (on-premises)](/dynamics365/customerengagement/on-premises/overview)</li> <b>Note</b>: Dynamics 365 for Tablets is deprecated, and won't be supported in 2023. |
| [Dynamics 365 Sales Mobile](/dynamics365/sales/sales-mobile/dynamics-365-sales-mobile-app) | <ul><li>[Dynamics 365 Sales](/dynamics365/sales/help-hub)</li></ul> |
| [Field Service Mobile](/dynamics365/field-service/mobile-power-app-overview) | <ul><li>[Field Service (Dynamics 365) ](/dynamics365/field-service/overview)</li></ul> |
  
## Regional availability of Power Apps mobile app
 
Power Apps mobile app is available to users in Azure global cloud and also in the following regions:
- [US Department of Defense (US DoD)](/azure/azure-government/documentation-government-overview-dod)
- [US Government Community Cloud (GCC) High](/power-platform/admin/microsoft-dynamics-365-government#about-dynamics-365-us-government-environments-and-products)
- [US Government Community Cloud (GCC)](/power-platform/admin/microsoft-dynamics-365-government#about-dynamics-365-us-government-environments-and-products)
- [China Sovereign Cloud](/power-platform/admin/about-microsoft-cloud-china)
  
Mobile users have an option to select their region on Power Apps mobile app sign in screen.

:::image type="content" source="media/Select_user_region_mobile_app.jpg" alt-text="Choose a region when signing in to Power Apps mobile app":::
 
 More information:
 - [Azure Government documentation](/azure/azure-government/)
 - [Dynamics 365 US Government](/power-platform/admin/microsoft-dynamics-365-government#about-dynamics-365-us-government-environments-and-products)
 - [Power Platform and Dynamics 365 apps in China](/power-platform/admin/about-microsoft-cloud-china)
  
## Privacy notice
Power Apps mobile app for Android registers for a system event that is broadcasted when the device is finished booting. Power Apps mobile app for Android registers for this event to support push notifications sent to the app. 
  
Power Apps mobile app and [wrapped native mobile apps](../maker/common/wrap/overview.md) may use device sensors, such as the device accelerometer, to respond to user actions. For example, [wrapped native mobile apps](../maker/common/wrap/overview.md) would automatically show the app menu when the user shakes the device. 
    
## See also

[Use model-driven apps on Power Apps mobile](use-custom-model-driven-app-on-mobile.md) <br/>
[Troubleshoot issues for Power Apps mobile](/powerapps/user/powerapps_mobile_troubleshoot)




[!INCLUDE[footer-include](../includes/footer-banner.md)]
