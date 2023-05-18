---
title: Preview your canvas apps
description: Preview your app in Power Apps Studio to see how the app will look for your app users.
author: tashaev

ms.topic: conceptual
ms.custom: canvas
ms.reviewer: mkaur
ms.date: 05/18/2023
ms.subservice: canvas-maker
ms.author: tashas
search.audienceType: 
  - maker
contributors:
  - mduelae
  - tashas
---
# Preview an app

When building an app, it's helpful to preview it and see how it will look for your users. When you preview an app, you can also preview how the app will appear on various devices and at different sizes, this is especially beneficial when you're building a responsive app.

To preview how the app will look like for your app users, open the app for editing in [Power Apps Studio](https://create.powerapps.com) and in the app actions menu, select ![Preview button.](media/studio/preview-button.png)
to **Preview the app**.

You can preview the app to see how it will look on different devices using the device picker. 

> [!div class="mx-imgBorder"] 
> ![Preview your app.](media/studio/preview-app.png)

Legend: 
1. **Tablet Devices**: Allows you to select from common tablet devices from several manufacturers, along with the ability to select a custom size based on your needs. This option shows a device frame and device safe zone, shown as the black area either on the top and bottom or sides depending upon the orientation. It also shows a black area with the home bar at the bottom.  
2. **Mobile devices**: Lets you select from common phones from several manufacturers, along with the ability to select a custom size based on your needs. This option shows a device frame and device safe zone, shown as the black area either on the top and bottom or sides depending upon the orientation. It also shows a black area with the home bar at the bottom. 
3. **Web view**: Lets you preview what the app looks like on a web browser. You can select Window size to fill the browser window, or you can specify a custom size to emulate your app embedded at a certain size. This option does not include a device frame.  
4. **Orientation Switcher**: Switch between vertical and horizontal orientation. The **Orientation Switcher** option is disabled if the Lock Orientation setting is set to **On**. 

## Display settings

The way your app behaves with each preview option is determined by app type and your display settings. For instance, if you're developing a responsive app, the content within it adjusts to fit the screen size of the device being used. 

Watch this video to learn how the device picker can help you confirm that the content is adjusting correctly.

VIDEO LINK

The way the preview appears can differ based on the app settings and whether you selected a phone or tablet layout during the app creation process.

- Apps created using the phone setting can still be viewed in the preview while selecting a tablet type device from the device picker, but if the app wasn't built using responsive app creation techniques, the app appears in a phone shape on tablet devices. You get a message explaining why the preview is narrow. If you’d like the app to be responsive to phone, tablet, and web sizes then we recommend selecting the tablet option when you create your app. You can use responsive auto-layout containers to determine the flow of the content for different screen sizes including phones. More information: [Building responsive canvas apps](build-responsive-apps.md)  

- Under Display settings:
   - **Scale To Fit**: When set to **On** your entire app is scaled to fit the available space. If a smaller space is available to the app, you may notice empty space on the sides to accommodate the scaling. This empty space will also appear for your app users when they play apps.
  - **Lock Orientation**: When set to **On**, the **Switch Orientation** button in the device picker is disabled.  

## Known Issues 

- If **Scale To Fit** setting is on and **Lock Aspect Ratio** is off, your preview won't accurate. This configuration isn't recommended. More information: [Change screen size and orientation of canvas apps](set-aspect-ratio-portrait-landscape.md)  

- If **Scale to Fit** is off and you resize your browser window while in preview mode, the preview won't be accurate. To address the issue, close and reopen the preview once your browser window is in the desired size. 

