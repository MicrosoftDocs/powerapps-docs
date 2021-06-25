---
title: Build mobile apps using the Measure in MR component
description: Learn how use the Measure in MR component in your Power Apps..
author: joel-lindstrom
ms.service: powerapps
ms.topic: conceptual
ms.custom: canvas
ms.reviewer: tapanm
ms.date: 06/25/2021
ms.author: v-ljoel
search.audienceType: 
  - maker
search.app: 
  - PowerApps
contributors:
  - tapanm-msft

---

# Build mobile apps using the Measure in MR component

You can use the **Measure in MR component** in your app to let users measure distance, area, and volume. During measurement, you create two-dimensional and three-dimensional polygons that can be used to confirm how a certain-sized object would fit within a space.

The component creates a button in your app. When app users select the button, it shows a live camera feed of the device. App users can then specify a starting point, and one or multiple sequential endpoints to measure between. The instances of measured segments are shown directly on the live camera feed.

When the user exits the component, the measurements that were taken are captured in the **Measurements** property so they can be saved or stored.

Screenshots taken during the mixed reality experience are stored in the **Photos** property for viewing within the app.

In this topic, we will create a simple screen in an app to use the **Measure in MR** component to measure the area of a user-defined space as well as view a photo of the space that was measured.

## Prerequisites

### Mixed-reality capable devices

To use the component in an app created with Power Apps, the device that runs the app (such as a phone or tablet) needs to have specific hardware and software. The device you use to create the app in the Power Apps studio (such as your PC) does not need to be MR-capable.

### For Android devices

For Android devices, this means you'll need to have the ARCore services installed. ARCore is usually installed automatically as part of the default set of apps and services on your device if it supports MR. The services are referred to as Google Play Services for AR. If necessary, you can download [Google Play Services for AR from the Google Play Store](https://play.google.com/store/apps/details?id=com.google.ar.core).

For more details on ARCore and supported devices, see the [list of supported devices on the Google ARCore support site](https://developers.google.com/ar/discover/supported-devices#android_play).

For devices in China, the experience is a little different as you'll need to [download ARCore from specific, supported app stores in China](https://developers.google.com/ar/discover/supported-devices#android_china).

### For iOS (Apple) devices

For iOS devices, MR is supported on specific hardware with ARKit. See the [list of iOS devices supported for MR at the bottom of the Apple augmented reality website](https://www.apple.com/augmented-reality/).

## Add the Measure in MR component 

Insert the component into your app as you normally would for any other button component.

With an app open for editing in [Power Apps Studio](https://create.powerapps.com/):

1.  Open the **Insert** tab.

2.  Expand **Mixed Reality**.

3.  Select the component **Measure in MR** to place it in the center of the app
    screen, or drag and drop it to position it anywhere on the screen.

Once the component is in the app, position it near the bottom of the screen. Then, with the component still selected, use the Properties tab on the right to change the following properties:

| Property            | Value        |
|---------------------|--------------|
| Text                | Measure Area |
| Unit of measurement | Feet         |
| Measurement type    | Area         |

Then select the Advanced tab to change the **OnMixedRealitySelect** property to this code:

```
ClearCollect(colMRMeasurements, Self.Measurements);  
ClearCollect(colMRPhotos, Self.Photos)  
```

This will allow the user to define areas to be measured in square feet and store the most recent results of the measurements in a collection named colMRMeasurements and the most recent photos in a collection named colMRPhotos.

## Add a header and an image and label to view the measurement results

### Header label

Add a text label to the screen. Position it at the top left corner of the screen and modify the following properties in the Properties tab:

| Property       | Value        |
|----------------|--------------|
| Text           | Measure Area |
| Font size      | 24           |
| Font weight    | Semibold     |
| Text alignment | Center       |
| Width          | Parent.Width |

Then in the Advanced tab, modify the following properties:

| Property | Value                  |
|----------|------------------------|
| Color    | RGBA(255, 255, 255, 1) |
| Fill     | RGBA(56, 96, 178, 1)   |

This will provide a header for the screen.

### Image and label to display results

Add an image control, position it just below the header label, and set the following properties:

| Property         | Value                       |
|------------------|-----------------------------|
| Image            | First(colMRPhotos).ImageURI |
| Border Thickness | 2                           |

This will display the first image taken from the **Measure in MR** component.

Add another label to the screen, positioning it below the image. Change the **Text** property in the Properties tab to this code:

```
"Area: " & If(IsEmpty(colMRMeasurements), "no area measured", First(colMRMeasurements).Area & " sq. " & First(colMRMeasurements).Unit)
```

This will display the first area measurement and unit type that is collected from the **Measure in MR** component. If there is no measurement to be returned, the text will show **Area: no area measured** to let the user know that no value is present.

## Test the app

Now that all the controls have been added, save and publish the app. On a mixed-reality capable device (as defined in the Prerequisites section), open the app, and press the **Measure Area** button. This will open the **Measure in MR** experience, allowing the user to define an area to be measured.

Follow the on-screen instructions to calibrate the device by slowly moving it left and right while pointing the camera at a surface to be measured. Once the calibration is complete, you will see an array of dots on the surface as well as a circle and dot reticle in the center of the screen. This reticle is used to define lengths, areas, and volumes by using the + button to add points and line segments.

Photos can be captured using the camera button. These photos will show the lengths, areas, and volumes defined by the user.

There is an undo button to undo any placed points.

Begin by placing a point using the + button. You will notice that an orange line and measurement now appear connected to the point you just placed. Place a second point and notice how a line with measurement appears between the two points you place. Continue placing points until the desired shape has been fully defined. To close a shape, place the reticle on the first point made and use the \+ button. You will notice that the center point of the reticle changes color from white to green, indicating that the shape can be closed. If two of the sides of the shape intersect, or you try to close a shape using any other point than the first one, you will notice that the center point of the reticle changes from white to red, indicating that a point cannot be placed there.

Once an area has been fully defined, position the device so that a picture can be taken of the area you just defined and use the camera button to do so. The select the **Submit** button. A confirmation dialog will appear, asking if you have finished with your measurements. If you have more measurements to enter, select **Cancel** to return to the MR environment. If you are finished, select **Submit** to be taken back to the app screen.

You will see the first picture taken as well as the calculated area of the shape you defined as well as the units, in this case sq. feet.

The measurement and photo can then be used like any other photo or text field in Power Apps, for instance to be sent in an email or stored in a table in Dataverse.