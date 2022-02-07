---
title: Use mixed reality controls in Power Apps
description: Use augmented reality features in Power Apps to view and manipulate 3D models in the real world, take measurements, and create and view 3D shapes.
author: anuitz
ms.service: powerapps
ms.topic: overview
ms.custom: canvas
ms.reviewer: tapanm
ms.date: 02/02/2022
ms.subservice: canvas-maker
ms.author: anuitz
search.audienceType: 
  - maker
search.app: 
  - PowerApps
contributors:
  - tapanm-msft
  - anuitz
---
# Add mixed reality controls to your canvas app

Add mixed reality (MR) controls to your canvas apps to interact with the real world in 3D.

You can use MR controls to:

- View and manipulate 3D content
- Overlay 3D content and 2D images on the camera feed
- Measure distance, area, and volume
- Identify spaces and locations

:::image type="content" source="./media/augmented-overview/mixed-reality-overview.png" alt-text="A screenshot of a phone app with a 3D control under construction in Microsoft Power Apps Studio, alongside a photo that shows the app in use.":::

[Build your own controls](../../developer/component-framework/custom-controls-overview.md) or use prebuilt controls for MR applications:

- [View in 3D](mixed-reality-component-view-3d.md)
- [View in mixed reality](mixed-reality-component-view-mr.md)
- [Measure in mixed reality](mixed-reality-component-measure-distance.md)
- [View shape in mixed reality](mixed-reality-component-view-shape.md)

You'll find the controls on the **Insert** pane, under **Media** and **Mixed Reality**:

:::image type="content" source="./media/augmented-overview/augmented-overview-insert-all.png" alt-text="A screenshot of the Insert pane in Microsoft Power Apps Studio.":::
  
> [!TIP]
> The MR controls in Power Apps use Babylon and Babylon React Native. Mixed reality content that works in the [Babylon sandbox](https://sandbox.babylonjs.com/) should work in Power Apps through this shared MR platform. If your content works in Babylon but not in Power Apps, ask a question in the [Power Apps community forum](https://powerusers.microsoft.com/t5/Get-Help-with-Power-Apps/ct-p/PA_General).
>  
> [Read more about our integration with Babylon](https://babylonjs.medium.com/babylon-react-native-bringing-3d-and-xr-to-react-native-applications-7928b55acc85).

## Prerequisites

The device you use to create an app with MR controls, such as your PC, doesn't need to be MR-capable. Mobile devices that run the app must have specific hardware and software to use MR controls.

### Android devices

Android devices need to have Google Play Services for AR (known more commonly as ARCore) installed. ARCore should be installed automatically on MR-capable devices. If necessary, download [Google Play Services for AR from the Google Play Store](https://play.google.com/store/apps/details?id=com.google.ar.core).

For more information about ARCore and devices that support it, see the [list of supported devices on the Google ARCore support site](https://developers.google.com/ar/discover/supported-devices#android_play).

The experience is a little different for devices in China, which don't ship with the Google Play Store. [ARCore must be downloaded from specific app stores in China](https://developers.google.com/ar/discover/supported-devices#android_china).

### iOS (Apple) devices

iPhones and iPads with specific hardware can run MR apps using the ARKit framework. For more information about MR and iOS devices that support it, see the [list of supported devices on the Apple augmented reality website](https://www.apple.com/augmented-reality/). (Scroll to the bottom of the page to see the list.)

## Mixed reality controls

Start installing the controls in your apps:

- View 3D content with the **[View in 3D](mixed-reality-component-view-3d.md)** control.
- View images and 3D content in the real world with the **[View in mixed reality](mixed-reality-component-view-mr.md)** control.
- Measure distance, area, and volume with the **[Measure in mixed reality](mixed-reality-component-measure-distance.md)** control.
- Create and view 3D shapes with the **[View shape in mixed reality](mixed-reality-component-view-shape.md)** control.

### See also

[Microsoft Learn: Build a 3D mobile app with Power Apps in mixed reality](/learn/modules/power-apps-tutorial/)

[!INCLUDE[footer-include](../../includes/footer-banner.md)]
