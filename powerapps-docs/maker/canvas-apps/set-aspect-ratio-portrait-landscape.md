---
title: Change screen size and orientation of a canvas app | Microsoft Docs
description: Step-by-step instructions for changing settings such as the screen size and the orientation of a canvas app in PowerApps
author: evchaki
manager: kvivek
ms.service: powerapps
ms.topic: conceptual
ms.custom: canvas
ms.reviewer: anneta
ms.date: 11/07/2018
ms.author: evchaki
search.audienceType: 
  - maker
search.app: 
  - PowerApps
---
# Change screen size and orientation of a canvas app in PowerApps
Customize a canvas app by changing its screen size and orientation.

## Prerequisites

Create an app or open one for editing, and then select **App settings** on the **File** menu.

## Change screen size and orientation
1. Under **App settings**, select **Screen size + orientation**.

    ![Option to change the screen size and orientation of an app](./media/set-aspect-ratio-portrait-landscape/size-orientation.png)

1. In the **Orientation** list, select **Portrait** or **Landscape**.

1. (Tablet apps only) Under **Aspect ratio**, perform either of these steps:

    - Select the ratio that matches the target device for this app.
    - Select **Custom** to set your own size, and then specify a width between 50 - 3840 and a height between 50 - 2160.

    ![Change the aspect ratio of a tablet app](./media/set-aspect-ratio-portrait-landscape/aspect-tablet.png)
    
1. Under **Scale to fit**, specify either **On** or **Off**.

    This setting is on by default so that app screens resize to fit the available space on the device. When this setting is on, the app's **Width** property matches its **DesignWidth**, and the app's **Height** matches its **DesignHeight**.

    If you turn this setting off, the app adjusts to the aspect ratio of the device on which it's running and takes up all of the available space. The app doesn't scale and, as a result, screens can show more information.

    When this setting is turned off, **Lock aspect ratio** is automatically turned off and disabled. In addition, the **Width** property of all screens is set to `Max(App.Width, App.DesignWidth)`, and their **Height** property is set to `Max(App.Height, App.DesignHeight)` so that they track the dimensions of the window in which the app is playing instead. With this change, you can create apps that respond to different devices and window dimensions. More information: [Create responsive layout](create-responsive-layout.md)

1. Under **Lock aspect ratio**, specify either **On** or **Off**.

    If you lock the aspect ratio, the app will retain the appropriate aspect ratio for the selections made in the screen orientation and aspect ratio in steps 1 and 2, no matter the device. For example, if a phone app is running on another kind of device like a web browser, the app may display incorrectly by retaining its phone aspect ratio, not filling the window and having dark bars to fill in the aspect ratio mismatch. If you unlock the aspect ratio, the app will adjust to the aspect ratio of the device on which it's running. This may cause unintended or unwanted distortion of the controls on the screen.

1. Under **Lock orientation**, specify either **On** or **Off**.

    If you lock the app's orientation, the app will retain the orientation that you specify. If the app is running on a device for which the screen is in a different orientation, the app will display incorrectly and may show unwanted results. If you unlock the app's orientation, it will adjust to the screen orientation of the device on which it's running.

    You can also modify the app's orientation by enabling **Enable app embedding user experience** in **Advanced settings**. This feature top-left aligns the app when it's embedded and changes the background color of the hosting canvas to white.

1. Select **Apply** to save your changes.

## Next step
On the **File** menu, select **Save** to republish your app with the new settings.
