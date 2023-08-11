---
title: Prevent canvas app restarts in the Power Apps mobile app
description: Learn how to prevent canvas app restarts on Power Apps mobile
author: anuitz
ms.component: pa-user
ms.topic: conceptual
ms.date: 01/05/2023
ms.subservice: mobile
ms.author: anuitz
ms.custom: ""
ms.reviewer: sericks
ms.assetid: 
search.audienceType: 
  - enduser
---

# Prevent canvas app restarts in the Power Apps mobile app

When you run a canvas app in the Power Apps mobile app, it can be restarted for the following reasons:

- The app is using too much total memory.
- The app is using too much memory or processing at one time.
- The app is moved to background – either when your specific app uses a native control (like **Add Picture** or **Barcode Scanner**) or the Power Apps mobile app is put in the background by the user.

This memory and processing limitations, which is especially strict when the Power Apps mobile app runs in the background, is imposed by the operating system (Android or iOS). If the app uses more resources than are available on your device, the app will reset. This is similar to when you visit a large complex webpage, the web browser suspends the page if it is consuming too much power.

On Android devices, this app restart can look like a crash because the app is completely closed and the user is taken to the home screen of the device.

Use this article to learn how to prevent canvas app restarts on Power Apps mobile.

## Prevention tips for end users

While the biggest improvements are usually made by app makers, here are some tips that end users can use to decrease the occurrence of app restarts:

- In the Power Apps mobile app, on the user profile page, select **Clear cache** to remove saved data. Note that this should only be done when the end user has data as clearing the cache will remove any **SaveData** or app caches. 
- On Android devices, ensure the Power Apps mobile app is prioritized. Refer to your device manual to keep the app running through the settings like battery optimization and app sleep configuration.
- Close any running apps, other than the Power Apps mobile app, and remove any unneeded data from the device such as unused apps or images.
- While it is cumbersome, consider using the app slower – pause a little bit between screen navigations or after taking pictures or saving or loading data.

## Prevention tips for app makers

The greatest memory improvements to decrease app restarts can be made by app makers. When creating an app, remember to optimize the app to run on the lowest-specification device that your end users will use and follow best practices around resource usage.

> [!NOTE]
> Since app restarts are caused by the operating system restricting the amount of memory and processing an app can do, it might take a combination of the mitigations suggested below to minimize app restarts. The more memory and processing that can be reduced, both in total and at one time, the less likely an app restart will be.

> [!TIP]
> You can [connect a mobile app session to Monitor](../maker/monitor-canvasapps.md#for-apps-running-on-power-apps-mobile-preview) to see where your app is doing heavy processing or memory-intensive operations. Monitor is a tool that offers makers a deep view of what an app does and how it does it by logging all key activities that occur in the app as it runs.

| Problem | Root Cause | Mitigation |
|---------|---------|---------|
| App restarts when loading a specific screen. | If a specific screen is running too many formulas at one time, the app can have too much processing and be restarted by the operating system. | Limit the number of controls on a screen and the number of formulas being run when the screen is loaded, which might require splitting up screens. <br><br> Avoid control dependency between screens. <br><br> Prevent the user from taking action during high-processing moments. For example, when a large gallery with multiple filters and lookups is loading. <br><br> Consider using named formulas. <br><br> Consider using the **Delayed Load** app setting. |
| App restarts after multiple screen navigations. | There are memory leaks happening on the screens, resulting in memory usage building up as the user navigates around the app. | Turn on the **Keep recently visited screens in memory** app setting. While this increases total memory usage in the short term as the screen is preserved in memory, across multiple screen navigations, it will prevent memory leaks. |
| App restarts when doing **SaveData**/**LoadData** or using data connections. | **SaveData** and data connections both increase the total memory being used by the app. **SaveData** is also a processing-heavy operation. Bringing in large amounts of data into the app and saving that data for offline usage (especially the media content and files) can cause the app to go above its allotted memory, causing the operating system to restart the app. | Optimize the amount of data brought into the app via data connections and saved via **SaveData**. <br><br> Reduce the number of **SaveData** calls where possible. <br><br> Turning on the **Explicit column selection** app setting and turning off the **Record scope one-to-many and many-to-many relationships** app setting can also help reduce the data being brought into the app. |
| App restarts when using the camera control. | The camera control saves the captured image to memory. This can increase the memory usage of the app, especially if the captured image is saved into variables or **SaveData** using the **OnStream** property. | Do not save any images beyond the most recently captured one. <br><br> Use **Photo** instead of **Stream** to only capture images when the user taps on the camera. <br><br> If you need to use **Stream**, set the **StreamRate** property as high as possible to reduce the number of updates. |
| App restarts when using the **Add Picture** control. | The **Add Picture** control saves the selected media content into memory. Due to the size of media content, this can result in significant memory pressure. | Consider changing where the media content is captured. <br><br> Consider turning off the **UseMobileCamera** property so users can only select media from gallery/photo library. <br><br> Consider using the attachment control (as part of a form) to only select files instead of capturing them using the camera. <br><br> Consider switching to the camera control. |
| App restarts when using native controls like **Add Picture**, **Barcode Scanner/Reader**, **View in MR**, **Measuring camera**, and others. | Native controls can put the app in the background where the operating system has stricter limitations on memory before restarting the app. | Make sure all memory and processing intensive operations are completed before using these controls. For example, disable the **Add Picture** control until any **SaveData** operations are completed. <br><br> Consider switching to a different control like **Camera** instead of **Add Picture**. |
| App restarts happen for a subset of devices. | Devices have different amounts of memory and processing available. As an example, older devices are more prone to app restarts due to their lower available processing. <br><br> Having other apps running can also reduce the amount of processing available. Similarly, other apps installed and lots of photos/media saved to the device can take up memory, reducing what is available for the app. | Refer your users to the tips listed above in our [Prevention tips for end users](#prevention-tips-for-end-users) section. <br><br> Consider investing in devices that meet the performance needs of your app. |
| App restarts continue to happen. | Memory usage is impacted by how the canvas app is authored. Make sure your app follows best practices can help ensure performance, reduce memory usage, and processing. | Optimize your app following the [best practices](#best-practices-for-building-performant-apps) below. |

## Best practices for building performant apps

- [Build large and complex apps](../maker/canvas-apps/working-with-large-apps.md)
- [Common canvas app performance issues and resolutions](../maker/canvas-apps/common-performance-issue-resolutions.md)
- [Tips and best practices to improve performance of canvas apps](../maker/canvas-apps/performance-tips.md)
- [Power Apps canvas app coding standards and guidelines](https://powerapps.microsoft.com/blog/powerapps-canvas-app-coding-standards-and-guidelines/)
- [Power Apps canvas app coding standards and guidelines whitepaper](https://pahandsonlab.blob.core.windows.net/documents/PowerApps%20canvas%20app%20coding%20standards%20and%20guidelines.pdf) (Be sure to review the section titled, **Optimizing for performance**.)
