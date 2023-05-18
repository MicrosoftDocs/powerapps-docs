---
title: Preview your canvas apps
description: Preview your app in Power Apps Studio to see how the app will look for your app users.
author: amchern

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
# Preview your app

While building your canvas app, it can be beneficial to preview it periodically to get a sense of how it will appear to your users. With this feature, you can also preview how your app will appear on various devices and at different sizes, which can be especially helpful if you are constructing a responsive application.

To see how your app will look for your app users, open the app for editing in [Power Apps Studio](https://create.powerapps.com), in the app actions menu, select ![Preview button.](media/studio/preview-button.png)
to **Preview the app**.

You can preview your app to see how it will look on different devices using the device picker.  


> [!div class="mx-imgBorder"] 
> ![Preview your app.](media/studio/preview-app.png)

Legend: 
1. **Tablet Devices**: Allows you to select from common tablet devices from several manufacturers, along with the ability to select a custom size based on your needs. This option shows a device frame and device safe zone, shown as the black area either on the top and bottom or sides depending upon the orientation. It also shows a black area with the home bar at the bottom.  
2. **Mobile devices**: Lets you to select from common phones from several manufacturers, along with the ability to select a custom size based on your needs. This option shows a device frame and device safe zone, shown as the black area either on the top and bottom or sides depending upon the orientation. It also shows a black area with the home bar at the bottom. 
3. **Web view**: Lets you to preview what the app will look like on a web browser. You can select Window size to fill the browser window, or you can specify a custom size to emulate your app embedded at a certain size. This option does not include a device frame.  
4. **Orientation Switcher**: Switch between vertical and horizontal orientation. This button will be disabled if the Lock Orientation setting is set to **On**. 

## Display settings

The way in which your app behaves with each preview option is determined by the app type and the display settings that have been selected.

For instance, if you're developing a responsive app, the content within it will adjust to fit the screen size of the device being used. The device picker feature allows you to confirm that the content is adjusting correctly.

VIDEO LINK

The way the preview appears can differ based on the app settings and whether you selected a phone or tablet layout during the app creation process.

- Apps created using the Phone setting can still be viewed in the preview while selecting a tablet type device from the device picker, but if the app was not built using responsive app creation techniques, the app will still appear in in a phone shape on tablet devices. You will see a message explaining why the preview is narrow. If you’d like your app to be responsive to phone, tablet, and web sizes we recommend selecting the Tablet option to create your app. You can use responsive auto-layout containers to determine the flow of the content for different screen sizes including phones. Learn more.  

- Under Display settings:
   - **Scale To Fit**: When set to **On** this results in your entire app being scaled to fit the available space. If a smaller space is available to the app, you may notice empty space on the sides to accommodate the scaling. This empty space will also appear for your app users when they play apps.
  - **Lock Orientation**: When set to **On**, the **Switch Orientation** button in the device picker will be disabled.  

## Known Issues 

- If **Scale To Fit** setting is on and **Lock Aspect Ratio** is off, your preview may not be accurate. This configuration is not recommended. Learn more.  
- If **Scale to Fit** is off and you resize your browser window while in preview mode, the preview may not be accurate. To address this, close and reopen the preview once your browser window is in the desired size. 

