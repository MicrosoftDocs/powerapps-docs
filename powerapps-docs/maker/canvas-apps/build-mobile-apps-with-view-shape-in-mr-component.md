---
title: Build mobile apps with View Shape in MR component
description: Learn how to use the view shape in MR component in your Power Apps.
author: joel-lindstrom
ms.service: powerapps
ms.topic: conceptual
ms.custom: 
ms.date: 06/25/2021
ms.author: v-ljoel
ms.reviewer: tapanm
contributors:
    - tapanm-msft
  
---

# Build mobile apps with View Shape in MR component

You can use the **View Shape in MR** component in your app to let users see if a simple cube might fit within a specified space. They might want to do this to see how a certain object that you provide would fit in their space. If you have a 3D model or head-on picture for the object you would like to fit test consider using [the View in MR component](https://docs.microsoft.com/en-us/powerapps/maker/canvas-apps/mixed-reality-component-view-mr) instead.

The component creates a button in your app. When app users click the button, it overlays a cube onto the live camera feed of the device. You set up the dimensions of the cube when you edit the component in Power Apps.

In this topic, we will create a screen in an app that will allow users to create a custom cube shape by inputting unit to be used (centimeters, feet, inches, or meters) as well as defining the height, width, and depth of the cube.

## Prerequisites

### Mixed-reality capable devices

To use the component in an app created with Power Apps, the device that runs the app (such as a phone or tablet) needs to have specific hardware and software. The device you use to create the app in the Power Apps studio (such as your PC) does not need to be MR-capable.

### For Android devices

For Android devices, this means you'll need to have the ARCore services installed. ARCore is usually installed automatically as part of the default set of apps and services on your device if it supports MR. The services are referred to as Google Play Services for AR. If necessary, you can download [Google Play Services for AR from the Google Play Store](https://play.google.com/store/apps/details?id=com.google.ar.core).

For more details on ARCore and supported devices, see the [list of supported devices on the Google ARCore support site](https://developers.google.com/ar/discover/supported-devices#android_play).

For devices in China, the experience is a little different as you'll need to [download ARCore from specific, supported app stores in China](https://developers.google.com/ar/discover/supported-devices#android_china).

### For iOS (Apple) devices

For iOS devices, MR is supported on specific hardware with ARKit. See the [list of iOS devices supported for MR at the bottom of the Apple augmented reality website](https://www.apple.com/augmented-reality/).

## Insert a header and labels and controls to specify the cube’s dimensions and units

### Header label

With an app open for editing in [Power Apps Studio](https://create.powerapps.com/), add a text label to the screen. Position it at the top left corner of the screen and modify the following properties in the Properties tab:

| Property       | Value               |
|----------------|---------------------|
| Text           | "Place A Cube"      |
| Font size      | 24                  |
| Font weight    | FontWeight.Semibold |
| Text alignment | Align.Center        |
| Width          | Parent.Width        |

Then in the Advanced tab, modify the following properties:

| Property | Value                  |
|----------|------------------------|
| Color    | RGBA(255, 255, 255, 1) |
| Fill     | RGBA(56, 96, 178, 1)   |


This will provide a header for the screen.

### Labels and controls to specify cube properties

Add four text labels to the screen. These will be the labels to identify the
controls we will add later. For each label, modify the **Text** property to one of the following:

-   “Unit Type”

-   “Width”

-   “Height”

-   “Depth”

Set the **Width** property of these labels to 160 and position them so they are stacked vertically in the order described above, near the top of the screen and to the left side.

Add a dropdown control and three text entry controls. The dropdown will be used to select a unit type for the cube dimensions and the three text entry controls will be used to enter the width, height, and depth of the cube.

Select the drop down, rename it to *drpUnitType*, and change the following properties:

| Property | Value                                       |
|----------|---------------------------------------------|
| Items    | ["Centimeters", "Feet", "Inches", "Meters"] |
| Default  | "Feet"                                      |
| Width    | 280                                         |

Position the control to the right of the Unit Type label.

Add three text input controls, renaming each *txtShapeHeight*, *txtShapeWidth*, and *txtShapeDepth*. Change the following properties for all three controls:

| Property | Value             |
|----------|-------------------|
| Default  | 2                 |
| Format   | TextFormat.Number |
| Width    | 144               |

Position the text input control named *txtShapeWidth* to the right of the Width label. Likewise, position the controls named *txtShapeHeight* and *txtShapeDepth* to the right of the Height and Depth labels, respectively.

Next, you will add the View Shape in MR component and configure it to use the controls that were just created to provide dynamic dimensions to the MR cube it will generate.

## Insert the View Shape in MR component

Insert the component into your app as you normally would for any other button control or component.

1.  Open the **Insert** tab.

2.  Expand **Mixed Reality**.

3.  Select the component **View Shape in MR** to place it in the center of the
    app screen, or drag and drop it to position it anywhere on the screen.

Once the component has been added, position in near the bottom of the screen and change the following properties:

| Property    | Value                      |
|-------------|----------------------------|
| Text        | "Place a cube"             |
| ShapeWidth  | txtShapeWidth.Text         |
| ShapeHeight | txtShapeHeight.Text        |
| ShapeDepth  | txtShapeDepth.Text         |
| Units       | drpUnitType.Selected.Value |
| Width       | 280                        |

![A picture containing graphical user interface Description automatically generated](media/build-mobile-apps-with-view-shape-in-mr-component/insert-the-view-shape-in-mr-component-1.jpg)

## Test the app

Now that all the controls have been added, save and publish the app. On a mixed-reality capable device (as defined in the Prerequisites section), open the app, and press the **Place a cube** button. This will open the **View Shape in MR** experience, allowing the user to define an area to be measured.

Follow the on-screen instructions to calibrate the device by slowly moving it left and right while pointing the camera at a surface to be measured. Once the calibration is complete, you will see an array of dots on the surface as well as a circle near the center of the screen. This circle shows where the cube can be placed initially. Once the cube has been placed it can be moved or rotated by using touch controls.

To move the cube, press on it and slide it to where you would like it to be placed. To rotate the cube, press one finger to the screen then swipe with another finger right or left.

Use the back button in the top left corner to return to the app screen and change one or more of the width, height, depth, or unit type settings. Select the **Place a cube** button and place the new cube.