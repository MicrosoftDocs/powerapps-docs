---
title: Building mobile apps with View in 3D and Mixed Reality components
description: Learn about how to use 3D and MR components.
author: Joel-lindstrom
ms.service: powerapps
ms.topic: conceptual
ms.custom: canvas
ms.reviewer: tapanm
ms.date: 05/24/2021
ms.author: v-ljoel
search.audienceType:
  - maker
search.app:
  - PowerApps
---
# Build mobile apps with View in 3D & Mixed Reality components

You can use the **View in MR** component in your app to let users see how a particular item might fit within a specified space.

The component creates a button in your app. When app users click the button, it overlays a selected 3D model (in the .glb file format) or image (in .jpg or .png file formats) onto the live camera feed of the device.

You can also take photos and [upload them to OneDrive](https://docs.microsoft.com/powerapps/maker/canvas-apps/mixed-reality-take-upload-photos).

In this topic, we will build a screen in an app that will allow a user to select 3D models from a gallery and view them using the **View in MR** component.

## Prerequisites

### Mixed-reality capable devices

To use the component in an app created with Power Apps, the device that runs the app (such as a phone or tablet) needs to have specific hardware and software. The device you use to create the app in the Power Apps studio (such as your PC) does not need to be MR-capable.

### For Android devices

For Android devices, this means you'll need to have the ARCore services installed. ARCore is usually installed automatically as part of the default set of apps and services on your device if it supports MR. The services are referred to as Google Play Services for AR. If necessary, you can download [Google Play Services for AR from the Google Play Store](https://play.google.com/store/apps/details?id=com.google.ar.core).

For more details on ARCore and supported devices, see the [list of supported devices on the Google ARCore support site](https://developers.google.com/ar/discover/supported-devices#android_play).

For devices in China, the experience is a little different as you'll need to [download ARCore from specific, supported app stores in China (https://developers.google.com/ar/discover/supported-devices#android_china).

### For iOS (Apple) devices

For iOS devices, MR is supported on specific hardware with ARKit. See the [list of iOS devices supported for MR at the bottom of the Apple augmented reality website](https://www.apple.com/augmented-reality/).

## Initialize a collection, insert a header and gallery of 3D items to view

### Initialize a collection

In the **OnVisible** property of the screen, copy and paste the following:

```
ClearCollect(
    col3dObjects,
    {
        ObjectName: "Forklift",
        ObjectURL: "https://raw.githubusercontent.com/microsoft/experimental-pcf-control-assets/master/forklift.glb"
    },
    {
        ObjectName: "HVAC",
        ObjectURL: "https://raw.githubusercontent.com/microsoft/experimental-pcf-control-assets/master/hvac.glb"
    },
    {
        ObjectName: "Machine",
        ObjectURL: "https://raw.githubusercontent.com/microsoft/experimental-pcf-control-assets/master/machine.glb"
    },
    {
        ObjectName: "Pallet w/ Boxes",
        ObjectURL: "https://raw.githubusercontent.com/microsoft/experimental-pcf-control-assets/master/pallet_with_boxes.glb"
    },
    {
        ObjectName: "Robot Arm",
        ObjectURL: "https://raw.githubusercontent.com/microsoft/experimental-pcf-control-assets/master/robot_arm.glb"
    }
)
```

This will create a collection containing the names of 3D objects to be viewed, as well as providing URLs for the **View in MR** component to reference.

### Header label

With an app open for editing in [Power Apps Studio](https://create.powerapps.com/), add a **Text label** to the screen by dragging and dropping it from the **Insert** tab. Position it at the top left corner of the screen and modify the following properties in the Properties tab:

| Property       | Value               |
|----------------|---------------------|
| Text           | "View In MR"        |
| Font size      | 24                  |
| Font weight    | FontWeight.Semibold |
| Text alignment | Align.Center        |
| Width          | Parent.Width        |

Then in the Advanced tab, modify the following properties:

| Property       | Value                      |
|----------------|----------------------------|
| Color          | RGBA(255, 255, 255, 1)     |
| Fill           | RGBA(56, 96, 178, 1)       |

This will provide a header for the screen.

### Gallery of 3D items to view

Insert a **Blank vertical gallery** from the **Layout** section of the **Insert** tab, positioning it below the header you just added. Change the following properties of the gallery:

| Property      | Value        |
|---------------|--------------|
| Data source   | col3dObjects |
| Template size | 80           |

Also from the **Insert** tab, drag and drop a **Text label** into the gallery. Change the following properties of the text label:

| Property | Value               |
|----------|---------------------|
| Text     | ThisItem.ObjectName |
| X        | 10                  |
| Y        | 5                   |
| Width    | 540                 |

From the **Mixed Reality** section of the **Insert** tab, drag and drop the **View in MR** component into the gallery. Then change the following properties:

| Property     | Value                                 |
|--------------|---------------------------------------|
| Text         | "View In MR"                          |
| Display type | Icon                                  |
| Source       | ThisItem.ObjectURL                    |
| X            | Parent.TemplateWidth - Self.Width - 5 |
| Y            | 5                                     |
| Width        | 70                                    |

This will provide a gallery that has a list of 3D objects and a button to press for the user to view those objects in mixed reality.

## Test the app

Now that all the controls have been added, save and publish the app. On a mixed-reality capable device (as defined in the Prerequisites section), open the app, and press the button that corresponds with the object you would like to view. This will open the **View in MR** experience.

Follow the on-screen instructions to calibrate the device by slowly moving it left and right while pointing the camera at a surface to be measured. Once the calibration is complete, you will see an array of dots on the surface as well as a circle near the center of the screen. This circle shows where the 3D object can be placed initially. Once the cube has been placed it can be moved or rotated by using touch controls.

To move the object, press on it and slide it to where you would like it to be placed. To rotate the object, press one finger to the screen then swipe with another finger right or left.

Use the back button in the top left corner to return to the app screen and select another object. Repeat this process as desired to view each of the objects.