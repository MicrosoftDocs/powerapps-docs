---
title: Prevent canvas app restarts on Power Apps mobile
description: Learn how to prevent canvas app restarts on Power Apps mobile
author: anuitz
manager: tapanm-MSFT
ms.component: pa-user
ms.topic: conceptual
ms.date: 12/14/2022
ms.subservice: mobile
ms.author: sericks
ms.custom: ""
ms.reviewer: ""
ms.assetid: 
search.audienceType: 
  - enduser
search.app: 
  - PowerApps
---

# Prevent canvas app restarts

When you run a canvas app on Power Apps mobile, it can be restarted for the following reasons:

- The app is using too much total memory
- The app is using too much memory or processing at once
- The app is moved to background – either your specific app when a native control (like Add Picture or Barcode Scanner) is used or the Power Apps mobile app is put in background by the user

This memory and processing limitation, which is especially strict in background, is imposed by the operating system (Android or iOS). If the app uses more resources than are available on your device, the app will reset. This is similar to when you visit a large complex webpage, the web browser suspends the page if it is consuming too much power.

On Android, this app restart can look like a crash because the app is completely closed and the user is taken to the home screen of the device.

When creating an app, remember to optimize the app to run on the lowest-specification device that your end-users will use and follow best practices around resource usage.

> [!NOTE]
> Since app restarts are caused by the operating system restricting the amount of memory and processing an app can do, it might take a combination of the mitigations suggested below to minimize app restarts. The more memory and processing can be reduced - both in total and at once - the less likely an app restart will be.

> [!TIP]
> You can [connect a mobile app session to Monitor](../maker/monitor-canvasapps.md#for-apps-running-on-power-apps-mobile-preview) to see where your app is doing heavy processing or memory-intensive operations. Monitor is a tool that offers makers a deep view of what an app does and how it does it by logging all key activities that occur in the app as it runs.

| Problem | Root Cause | Mitigation |
|---------|---------|---------|
| App restarts when loading a specific screen | If a specific screen is running too many formulas at once, the app can have too much processing and be restarted by the operating system. | Limit the number of controls on a screen and the number of formulas being run when the screen is loaded - which might require splitting up screens. <br><br> Avoid control dependency between screens. <br><br> Prevent the user from taking action during high-processing moments (e.g. when a large gallery with multiple filters / lookups is loading). <br><br> Consider using named formulas. <br><br> Consider using the 'Delayed Load' app setting. |
| App restarts after multiple screen navigations | There are memory leaks happening on the screens, resulting in memory usage building up as the user navigates around the app. | Turn on the ‘Keep recently visited screens in memory’ app setting – while this increases total memory usage in the short term as the screen is preserved in memory, across multiple screen navigates, it will prevent memory leaks. |
| App restarts when doing **SaveData**/**LoadData** or using data connections | **SaveData** and data connections both increase the total memory being used by the app. **SaveData** is also a processing-heavy operation. Bringing in large amounts of data into the app and saving that data for offline usage (especially media content and files) can cause the app to go above its allotted memory, causing the OS to restart the app. | Optimize the amount of data brought into the app via data connections and saved via **SaveData**. <br><br> Reduce the number of **SaveData** calls where possible. <br><br> Turning on the ‘Explicit column selection’ app setting and turning off ‘Record scope one-to-many and many-to-many relationships’ app setting can also help reduce the data being brought into the app. |
| App restarts when using the Camera control | The camera control saves the captured image to memory. This can increase the memory usage of the app, especially if the captured image is saved into variables or **SaveData** using the **OnStream** property. | Do not save any images beyond the most recently captured one. <br><br> Use **Photo** instead of **Stream** to only capture images when the user taps on the camera. <br><br> If you need to use **Stream**, set the **StreamRate** property as high as possible to reduce the number of updates. |
| App restarts when using the Add Picture control | The Add Picture control saves the selected media content into memory. Due to the size of media content, this can result in significant memory pressure. | Consider changing improved media capture, which changes where the media content is captured. <br><br> Consider turning off the **UseMobileCamera** property so users can only select media from gallery/photo library. <br><br> Consider using the attachment control (as part of a form) to only select files instead of capturing them using the camera. <br><br> Consider switching to the Camera control. |
| App restarts when using native controls like Add Picture, Barcode scanner/reader, View in MR, Measuring camera, etc | Native controls can put the app in background where the OS has stricter limitations on memory before restarting the app. | Make sure all memory and processing intensive operations are completed before using these controls, e.g. disable the Add Picture control until any SaveData operations are completed. <br><br> Consider switching to a different control like Camera instead of Add Picture. |
| App restarts happens for a subset of devices | Devices have different amounts of memory and processing available. As an example, older devices are more prone to app restarts due to their lower available processing. <br><br> Having other apps running can also reduce the amount of processing available. Similarly, other apps installed and lots of photos/media saved to the device can take up memory, reducing what is available for the app. | In the Power Apps Mobile menu, Clear Cache to remove saved data. Note that this should only be done when the user has data as clearing the cache will remove any SaveData or app caches. <br><br> On Android, set battery to unrestricted for the Power Apps Mobile app. <br><br> Close any running apps other than Power Apps and remove any unneeded data from the device (unused apps, images, etc). <br><br> Consider investing in devices that meet the performance needs of your app. |
| App restarts continue to happen | Memory usage is impacted by how the canvas app is authored. Making sure your app follows best practices can help ensure performance, reducing memory usage and processing. | Optimize your app following the best practices below. <br><br> While it is cumbersome, consider using the app slower – pause a little bit between screen navigations or after taking pictures or saving/loading data. |

## Best practices for building performant apps

- [Build large and complex apps](../maker/canvas-apps/working-with-large-apps.md)
- [Common performance issues and resolutions](../maker/canvas-apps/common-performance-issue-resolutions.md)
- [Tips and best practices to improve performance of canvas apps](../maker/canvas-apps/performance-tips.md)
- [PowerApps coding standards and guidelines](https://powerapps.microsoft.com/blog/powerapps-canvas-app-coding-standards-and-guidelines/)
- [PowerApps canvas app coding standards and guidelines whitepaper](https://pahandsonlab.blob.core.windows.net/documents/PowerApps%20canvas%20app%20coding%20standards%20and%20guidelines.pdf) (Note, review the section titled, Optimizing for performance)
