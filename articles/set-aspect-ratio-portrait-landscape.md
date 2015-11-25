<properties
	pageTitle="Set the landscape or portrait aspect ratio within PowerApps | Microsoft PowerApps"
	description="Configure the aspect ratio for landscape and portrait orientation in PowerApps"
	services=""
	suite="powerapps"
	documentationCenter=""
	authors="MandiOhlinger"
	manager="dwrede"
	editor=""/>

<tags
   ms.service="powerapps"
   ms.devlang="na"
   ms.topic="article"
   ms.tgt_pltfrm="na"
   ms.workload="na"
   ms.date="11/24/2015"
   ms.author="mandia"/>

# Use the landscape or portrait view

When you create an app, you can use the Landscape or Portrait view. You can also lock the aspect ratio. This topic provides more information on these options.

### Prerequisites
- Install [PowerApps](http://aka.ms/powerappsinstall) and sign-in with your work or organization account.
- Create a new PowerApp or open an existing PowerApp.
- To familiarize yourself with configuring controls in PowerApps, step through the [configure a control](get-started-test-drive.md#configure-a-control).

## Set landscape or portrait for a phone app
1. On the **File** tab, select **App Settings**.
2. Select **Screen size + orientation**.
3. Select **Landscape** or **Portrait**:  
![][5]  

You can also enable or disable **Lock aspect ratio** and **Lock orientation**:  
![][6]  

## Set landscape or portrait for a tablet
1. On the **File** tab, select **App Settings**.
2. Select **Screen size + orientation**.
3. In the drop-down list, select **Landscape** or **Portrait**:  
![][4]  

You can also enable or disable **Lock aspect ratio** and **Lock orientation**:  
![][6]  

## What is Lock aspect ratio
Put simply, not enabling this feature allows your app to run everywhere. When you enable this setting, you lock your app to the aspect ratio you choose. For example:

You create a tablet app and set the aspect ratio to 4:3 (iPad). You enable the **Lock aspect ratio** setting. When you do this, it locks in this ratio and the app *always* renders to the 4:3 aspect ratio. When your apps runs on Surface Pro or other mobile devices with different aspect ratios, the app displays incorrectly and may even show some undesirable results.

The same applies for phone apps. When this setting is enabled, the app *always* renders to the default iPhone aspect ratio. When your app runs on other mobile phones with different aspect ratios, the app displays incorrectly and may even show some undesirable results. When **Lock aspect ratio** is not checked, the same app automatically scales to Windows Phone, Android, and so on, with no additional settings.

To summarize, if you don't enable the **Lock aspect ratio** setting, PowerApps automatically scales to the mobile device using the app.

## What is Lock orientation
When enabled, the PowerApp stays in Landscape or Portrait, even when the mobile device is rotated. When not enabled, PowerApps automatically adjusts the orientation when the mobile device is rotated. 

## Tips and Tricks
- At anytime, you can select the Preview button (![][3]) to see how your app looks with the options you choose.
- When designing your app, you can re-size the controls and move them around using click-and-drag.


[1]: ./media/set-aspect-ratio-portrait-landscape/phoneratio.png
[2]: ./media/set-aspect-ratio-portrait-landscape/tabletratio.png
[3]: ./media/set-aspect-ratio-portrait-landscape/preview.png
[4]: ./media/set-aspect-ratio-portrait-landscape/tabletorientation.png
[5]: ./media/set-aspect-ratio-portrait-landscape/phoneorientation.png
[6]: ./media/set-aspect-ratio-portrait-landscape/advancedsettings.png
