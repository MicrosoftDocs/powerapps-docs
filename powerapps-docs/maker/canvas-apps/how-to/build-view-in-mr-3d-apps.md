---
title: Create an app with 3D and mixed reality controls
description: Learn about how to use 3D and mixed reality controls.
author: Joel-lindstrom

ms.topic: how-to
ms.custom: canvas
ms.reviewer: mkaur
ms.date: 12/09/2021
ms.author: anuitz
search.audienceType:
  - maker
contributors:
    - joel-lindstrom
    - mduelae
    - anuitz
---

# Create an app with 3D and mixed reality controls

You can use the [3D object](../mixed-reality-component-view-3d.md) and [View in MR](../mixed-reality-component-view-mr.md) controls to view items in 3D, or to see how a particular item might fit within a specified space.

In this article, you'll learn how to use the 3D and mixed reality controls in Power Apps.

Watch this video to learn how to build mobile apps with View in MR control:
> [!VIDEO https://learn-video.azurefd.net/vod/player?id=7651a5f3-4886-4910-97b0-290116a9fa89]

## Prerequisites

See [prerequisites for mixed-reality capable devices](../mixed-reality-overview.md#prerequisites).

## Create an app with View in MR control

The **View in MR** control creates a button in your app. When app users selects the button, it overlays a selected 3D model (in the .glb file format) or image (in .jpg or .png file formats) onto the live camera feed of the device.

> [!TIP]
> You can also take photos and [upload them to OneDrive](../mixed-reality-take-upload-photos.md).

In this section, we will build a screen in an app that will allow a user to view the selected item in mixed reality using the **View in MR** control.

1. Open an app in [Power Apps Studio](https://create.powerapps.com/).

1. Select the **OnStart** property of the app, copy and paste the following:

    ```power-fx
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

    :::image type="content" source="media/build-view-in-mr-3d-apps/app-onstart.png" alt-text="App OnStart property with the formula updated as mentioned in the above sample code.":::

    This formula will create a collection containing the names and links of the 3D objects to be viewed in mixed reality.

1. Add a **Text label** to the screen by dragging and dropping it from the **Insert** tab.

1. Position the added text label at the top-left corner of the screen, and modify the following properties in the **Properties** tab:

    | Property       | Value               |
    |----------------|---------------------|
    | Text           | "View In MR"        |
    | Font size      | 24                  |
    | Font weight    | `FontWeight.Semibold` |
    | Text alignment | `Align.Center`        |
    | Width          | 640        |

1. In the Advanced tab, modify the following properties for the text label:

    | Property       | Value                      |
    |----------------|----------------------------|
    | Color          | `RGBA(255, 255, 255, 1)`     |
    | Fill           | `RGBA(56, 96, 178, 1)`       |

    This change provides a header for the screen.

1. Insert a **Blank vertical gallery** from the **Layout** section of the **Insert** tab.

1. Position the gallery below the "View in MR" header you added earlier and expand it to use rest of the screen.

1. Change the following properties of the gallery:

    | Property      | Value        |
    |---------------|--------------|
    | Data source   | `col3dObjects` |
    | Template size | 80           |
    | X | 0 |
    | Y | 92 |
    | Width | 640 |
    | Height | 1044 |

1. Select **Edit gallery** to edit the gallery.

    :::image type="content" source="media/build-view-in-mr-3d-apps/edit-gallery.png" alt-text="Edit gallery for MR.":::

1. Insert a **Text label** into the gallery.

1. Change the following properties of the added text label:

    | Property | Value               |
    |----------|---------------------|
    | Text     | `ThisItem.ObjectName` |
    | X        | 10                  |
    | Y        | 5                   |
    | Width    | 540                 |

1. Edit the gallery again.

1. From the **Mixed Reality** section of the **Insert** tab, drag and drop the **View in MR** control into the gallery.

1. Change the following properties of the **View in MR** control.

| Property     | Value                                 |
|--------------|---------------------------------------|
| Text         | "View In MR"                          |
| Display type | Icon                                  |
| Source       | `ThisItem.ObjectURL`                    |
| X            | `Parent.TemplateWidth - Self.Width - 5` |
| Y            | 5                                     |
| Width        | 70                                    |

This change will provide a gallery that has a list of 3D objects and a button to press for the user to view those objects in mixed reality.

### Test the mixed reality control

Now that all the controls have been added, [save and publish](../save-publish-app.md) the app. On a mixed-reality capable device, open the app, and press the button that corresponds with the object you would like to view. This will open the **View in MR** experience.

:::image type="content" source="media/build-view-in-mr-3d-apps/view-mr-app.png" alt-text="View in MR.":::

Follow the on-screen instructions to calibrate the device by slowly moving it left and right while pointing the camera at a surface to be measured. Once the calibration is complete, you'll see an array of dots on the surface as well as a circle near the center of the screen. This circle shows where the 3D object can be placed initially. Once the cube has been placed it can be moved or rotated by using touch controls.

To move the object, press on it and slide it to where you would like it to be placed. To rotate the object, press one finger to the screen then swipe with another finger right or left.

Use the back button in the top left corner to return to the app screen and select another object. Repeat this process as desired to view each of the objects.

## Create an app with 3D object control

The **3D object** control allows you to view an item in 3D inside Power Apps. When app loads, it shows the 3D models (in the .glb file format) or image (in .jpg or .png file formats) inside the app through the control. You can select the 3D model to rotate, zoom in or out.

In this section, we will build a screen in an app that will allow a user to view the selected items in 3D using the **3D object** control.

1. Follow the steps 1 and 2 from the [Create an app with View in MR control](#create-an-app-with-view-in-mr-control) section to create an app with the collection of 3D objects for the app.

1. Add a **Text label** to the screen by dragging and dropping it from the **Insert** tab.

1. Position the added text label at the top-left corner of the screen, and modify the following properties in the **Properties** tab:

    | Property       | Value               |
    |----------------|---------------------|
    | Text           | "3D object"        |
    | Font size      | 24                  |
    | Font weight    | `FontWeight.Semibold` |
    | Text alignment | `Align.Center`        |
    | Width          | 640        |

1. In the Advanced tab, modify the following properties for the text label:

    | Property       | Value                      |
    |----------------|----------------------------|
    | Color          | `RGBA(255, 255, 255, 1)`     |
    | Fill           | `RGBA(56, 96, 178, 1)`       |

    This change provides a header for the screen.

1. Insert a **Blank vertical gallery** from the **Layout** section of the **Insert** tab.

1. Position the gallery below the "View in MR" header you added earlier and expand it to use rest of the screen.

1. Change the following properties of the gallery:

    | Property      | Value        |
    |---------------|--------------|
    | Data source   | `col3dObjects` |
    | Template size | 80           |
    | X | 0 |
    | Y | 92 |
    | Width | 640 |
    | Height | 1044 |

1. Select **Edit gallery** to edit the gallery.

    :::image type="content" source="media/build-view-in-mr-3d-apps/edit-gallery-3d.png" alt-text="Edit gallery for 3D.":::

1. Insert a **Text label** into the gallery.

1. Change the following properties of the added text label:

    | Property | Value               |
    |----------|---------------------|
    | Text     | `ThisItem.ObjectName` |
    | Width    | 640                 |

1. Edit the gallery again.

1. From the **Media** section of the **Insert** tab, drag and drop the **3D object** control into the gallery.

1. Change the following properties of the **View in MR** control.

| Property     | Value                                 |
|--------------|---------------------------------------|
| Source       | `ThisItem.ObjectURL`                    |
| X            | 18 |
| Y            | 138                                    |
| Width        | 600                                    |
| Height | 550 |

This change will provide a gallery that has a list of 3D objects that you can view in 3D.

### Test the 3D control

Now that all the controls have been added, [save and publish](../save-publish-app.md) the app. On a mixed-reality capable device, open the app, touch the screen to zoom in, zoom out, or turn the object being viewed in 3D.

:::image type="content" source="media/build-view-in-mr-3d-apps/view-in-3d.png" alt-text="3D object.":::

Since the gallery contains several objects in 3D, swipe down on the screen to see other objects and use the zoom or turn capabilities to work with the objects in 3D.

### See also

- [3D object control](../mixed-reality-component-view-3d.md)
- [Measuring Camera control](../mixed-reality-component-measure-distance.md)
- [View shape in MR control](../mixed-reality-component-view-shape.md) 

[!INCLUDE[footer-include](../../../includes/footer-banner.md)]
