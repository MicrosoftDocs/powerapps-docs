<properties
	pageTitle="Set the landscape or portrait aspect ratio within PowerApps Studio | Microsoft Azure"
	description="Set the aspect ratio for landscape and portrait orientation in PowerApps studio"
	services="powerapps"
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
   ms.date="10/29/2015"
   ms.author="mandia"/>

# Use the landscape or portrait view 

When you create an app, you can use a Landscape or Portrait view. 

### Prerequisites
- Install [PowerApps Studio](http://aka.ms/powerappsinstall). Create a new app or open an existing app in PowerApps. 
- To familiarize yourself with configuring controls in PowerApps, step through the [configure a control](get-started-test-drive.md#configure-a-control).

## Set landscape or portrait for a phone app
1. On the **File** tab, select **App Settings**.
2. Select **Landscape** or **Portrait**:  
![][1]  

You can also enable **Lock aspect ratio**.

## Set landscape or portrait for a tablet
1. On the **File** tab, select **App Settings**.
2. Select **Landscape** or **Portrait**:  
![][2]  

You can also enable **Lock aspect ratio**.

## What is Lock aspect ratio
The **Lock aspect ratio** applies more to tablet apps. When you enable this setting, you lock your app to the aspect ratio you choose. For example:

You create a tablet app and set the aspect ratio to iPad 4:3. You enable the **Lock aspect ratio** setting. When you do this, it always renders to the 4.3 aspect ratio. When your apps runs on Surface Pro 3 or other aspect ratios, it displays incorrectly and may even show some undesirable results. 

If you don't enable the **Lock aspect ratio** settings, it automatically scales to  the other aspect ratios.  

## Tips and Tricks
- At anytime, you can select the Preview button (![][3]) to see how your app looks  with the options you choose.
- When designing your app, you can resize the controls and move them around using click-and-drag.


[1]: ./media/set-aspect-ratio-portrait-landscape/phoneratio.png
[2]: ./media/set-aspect-ratio-portrait-landscape/tabletratio.png
[3]: ./media/set-aspect-ratio-portrait-landscape/preview.png