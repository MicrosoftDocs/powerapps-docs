---
title: Take screenshots of 3D objects in mixed reality
description: Take photos of 3D objects in the real world with augmented reality features in Power Apps.
author: anuitz
ms.topic: how-to
ms.custom: canvas
ms.date: 03/4/2022
ms.reviewer: mduelae
ms.subservice: canvas-maker
ms.author: anuitz
search.audienceType: 
  - maker
contributors:
  - mduelae
  - anuitz
  - CoPrez
---

# Take and upload mixed-reality photos

In this article, we'll create an app that can take photos of a mixed-reality session and upload them to a folder on OneDrive. We'll use the **View in MR** control in this example, but the **View shape in MR** and **Measuring camera** controls would work as well.

We'll cover the following tasks:

- Adding a **3D object** control to view and manipulate a sample 3D object
- Connecting the **3D object** control to a **View in MR** control to view the 3D object in the real world
- Adding a gallery control to view photos taken with the **View in MR** control
- Uploading the photos to OneDrive with a Microsoft Power Automate flow
- Uploading photos captured in mixed-reality to Dataverse

## Prerequisites

- [Create a blank canvas app](./create-blank-app.md).
- Create a folder called **MRPhotos** on OneDrive. You'll use this folder to store your uploaded photos.

>[!TIP]
>The mixed-reality (MR) controls work best in well-lit environments with flat-textured surfaces. Tracking is better on LIDAR-enabled devices.

## Add a button to take a photo of a 3D object in mixed reality

This example has three parts. First, we'll add a button that lets users take a photo of a 3D object in a mixed reality experience.

### Insert a **3D object** control

With your app open for [editing](edit-app.md) in [Power Apps Studio](https://create.powerapps.com):

1. Open the **Insert** tab and expand **Media**.
1. Select **3D object** to place a 3D object on the app screen. Drag the control to the screen to position it more precisely.

    The control comes with a transparent cube shape. If you like, change the control's **Source** property to [load a different 3D model](mixed-reality-component-view-3d-store.md). In this example, we'll use the URL *<https://raw.githubusercontent.com/microsoft/experimental-pcf-control-assets/master/robot_arm.glb>*.

    :::image type="content" source="./media/augmented-upload-photo/augmented-view-3d-shape.png" alt-text="A screenshot of a 3D object control under construction in Microsoft Power Apps Studio, shown with its Source property.":::

### Insert and connect a **View in MR** control

1. Open the **Insert** tab and expand **Mixed Reality**.
1. Select **View in MR** to place the control on the app screen, or drag the control to the screen to position it more precisely.
1. Change the control's **Source** property to **3DObject1.Source**. (*3DObject1* is the name of the **3D object** control we added earlier.) This expression directs the **View in MR** control to overlay the 3D model on the device camera feed.

   :::image type="content" source="./media/augmented-upload-photo/augmented-view-mr.png" alt-text="A screenshot of a View in MR control under construction in Microsoft Power Apps Studio, shown with its Source property.":::

1. [Save and publish the app](save-publish-app.md) and [run it on your mobile device](../../mobile/run-powerapps-on-mobile.md).

1. Select **View in MR** to view the 3D object in mixed reality. Select the camera icon to take a photo of the MR view.

## Insert a gallery control to view photos taken in the app

Next, we'll add a gallery so users can view the photos they've taken.

1. Edit your app again. Open the **Insert** tab and place a **Vertical gallery** control on the screen.
1. Change the control's **Items** property to **ViewInMR1.Photos**. (*ViewInMR1* is the name of the **View in MR** control we added earlier.)
1. Optionally, change the gallery's **Layout** property to **Image and title**.

    :::image type="content" source="./media/augmented-upload-photo/augmented-view-gallery.png" alt-text="A screenshot of a vertical gallery under construction in Microsoft Power Apps Studio, shown with its Items and Layout properties.":::

1. Preview the app and select **View in MR** to generate a sample photo.
    The gallery populates with a sample picture.

    :::image type="content" source="./media/augmented-upload-photo/gallery-example.png" alt-text="A screenshot of a canvas app that shows a 3D model and a photo of the model in a gallery.":::

>[!NOTE]
>If users exit the MR view to see the gallery, then enter the MR view again and take more photos, the new photos will replace the ones they took earlier.

### Add a larger overlay to the thumbnail images in the gallery

To make the photos in the gallery easier to see, you can add a full-size overlay that appears when the user selects a thumbnail image.

1. Edit your app again. Open the **Insert** tab and expand **Media**.
1. Select **Image** to place an image control on the screen. Move and size it according to how you want the larger photo to appear when a thumbnail image is selected.

    :::image type="content" source="./media/augmented-upload-photo/insert-pop-up.png" alt-text="A screenshot of an image control under construction in Microsoft Power Apps Studio.":::

1. Change the image control's properties as follows:
    | Property | Value |
    | - | - |
    | **OnSelect** | **UpdateContext({vVisibleImageZoom:false})** |
    | **Image** | **Gallery1.Selected.Image2** (assuming the gallery control is *Gallery1* and the first thumbnail image is *Image2*)
    | **Visible** | **vVisibleImageZoom**

1. Select the first thumbnail image in the gallery control. Change its **OnSelect** property to **UpdateContext({vVisibleImageZoom:true})**.

    :::image type="content" source="./media/augmented-upload-photo/set-gallery-onselect.png" alt-text="A screenshot of a thumbnail image in a gallery in Microsoft Power Apps Studio, shown with its OnSelect property.":::

1. [Save and publish the app](save-publish-app.md) and [run it on your mobile device](../../mobile/run-powerapps-on-mobile.md).
1. Select **View in MR**, and then select the camera icon to take a photo. Select the back arrow at the top of the screen to exit the MR view.
1. Select the thumbnail in the gallery to show a larger version of the photo. Select the image to hide it.

## Upload photos to OneDrive with a Power Automate flow

Last, we'll create a workflow using the Power Automate pane. The workflow uploads photos from the app to a folder named **MRPhotos** on OneDrive.

### Create a flow in Power Automate

1. Edit your app. On the app authoring menu, select **Power Automate** > **Create new flow**.

1. Search for and select the Power Apps button template.

    :::image type="content" source="./media/augmented-upload-photo/create-power-apps-button.png" alt-text="A screenshot of the Power Automate template page, with the Power Apps button template selected.":::
    
1. In the **Create your flow** window, select **Edit in advanced mode**.    

1. Select **Power Apps button** at the top of the window and enter a new name for your flow. In this example, we'll name the flow *Upload MR Photo*.

    :::image type="content" source="./media/augmented-upload-photo/rename-flow.png" alt-text="A screenshot of the Power Automate edit window, with the workflow name highlighted.":::

1. Select Power Apps button at the top of the window and enter a new name for your flow. In this example, we'll name the flow Upload MR Photo.

    :::image type="content" source="./media/augmented-upload-photo/rename-flow-delete-trigger.png" alt-text="A screenshot of the Power Automate edit window, with the PowerApps step selected for deletion.":::

1. Search for **PowerApps (V2)** and select the PowerApps (V2) trigger.

    :::image type="content" source="./media/augmented-upload-photo/select-powerapps-v2-trigger.png" alt-text="A screenshot of the Power Automate edit window, with the PowerApps (v2) trigger selected.":::

1. Select **Add an input**, and then select **File**.
1. Change the label *File Content* to **Image**.

    :::image type="content" source="./media/augmented-upload-photo/trigger-inputs.png" alt-text="A screenshot of the Power Automate edit window, with the File input label changed to Image.":::

1. Select **New step**. Search for **OneDrive Create file** and select the **Create file** action.

    :::image type="content" source="./media/augmented-upload-photo/onedrive-create-file-action.png" alt-text="A screenshot of the Power Automate edit window, with the OneDrive Create file action selected.":::

1. In **Folder Path**, select the folder icon and navigate to the **MRPhotos** folder you created earlier.
1. In **File Name**, enter **@{triggerBody()?['file']?['name']}** (Your text changes to "file.name.")
1. In **File Content**, enter **@{triggerBody()['file']['contentBytes']}** (Your text changes to "Image.")
1. Save your flow.

The complete flow should look like this:

:::image type="content" source="./media/augmented-upload-photo/flow-complete.png" alt-text="A screenshot of the Power Automate edit window, with the completed workflow shown.":::

### Connect the workflow to a button in your app

1. Return to your app in Power Apps Studio. Your flow is now listed under **Available flows**.

    :::image type="content" source="./media/augmented-upload-photo/flow-data-pane.png" alt-text="A screenshot of the Power Apps Studio Data pane, with the new flow shown.":::

1. Open the **Insert** tab and select **Button**. Place the button control on the screen and resize it as needed.
1. Change the button control's **Text** property to **Upload photos**.
1. In the formula bar at the top of the Power Apps window, select the **OnSelect** property. Select **Action** > **Power Automate** > **Upload MR Photo**.

    :::image type="content" source="./media/augmented-upload-photo/add-flow-to-button.png" alt-text="A screenshot of a button control under construction in Power Apps Studio, with a flow added to the control's OnSelect property.":::

    The button control's **OnSelect** property changes to **UploadMRPhoto.Run(**.

1. To upload the last photo taken, paste the following code after the opening parenthesis: **{file:{name:GUID() & ".png", contentBytes:Last(ViewInMR1.Photos).ImageURI}})**

    :::image type="content" source="./media/augmented-upload-photo/button-upload-code.png" alt-text="A screenshot of a button control's OnSelect property in the Power Apps Studio formula bar, which uploads the last photo taken.":::

    If you placed the button control inside the gallery, paste the following code instead: **{file: {name:GUID() & ".png", contentBytes:ThisItem.ImageURI}})**

    :::image type="content" source="./media/augmented-upload-photo/button-upload-code-gallery.png" alt-text="A screenshot of a button control's OnSelect property in the Power Apps Studio formula bar, when the button is in a gallery.":::

    To make the button upload all the photos taken, delete **UploadMRPhoto.Run(** and paste the following code: **ForAll(ViewInMR1.Photos, UploadMRPhoto.Run({file:{name:GUID() & ".png", contentBytes:ImageURI}}))**

    :::image type="content" source="./media/augmented-upload-photo/button-upload-code-all.png" alt-text="A screenshot of a button control's OnSelect property in the Power Apps Studio formula bar, which uploads all photos taken.":::

1. Preview the app and select **View in MR**, and then select **Upload photos**. Check the **MRPhotos** folder on OneDrive and confirm that the sample photo has been uploaded.

### Add offline capability to your app

You can use your app even when you have limited or no network connectivity using the [**SaveData** and **LoadData** functions](./functions/function-savedata-loaddata.md).

## Upload photos captured in mixed-reality to Dataverse

You can add photos to Dataverse tables through an Image data type column. Image columns in Dataverse have two required fields - Full and Value - which can be set to the ImageURI output of the MR controls.

For example, if you wanted to upload the first photo captured by the Markup in MR control to a Dataverse column called Image:

```power-fx
    Image: {Full: First(MarkupInMR.Photos).ImageURI, Value: First(MarkupInMR.Photos).ImageURI}
```

### See also

- [3D object control](mixed-reality-component-view-3d.md)
- [Measuring Camera control](mixed-reality-component-measure-distance.md)
- [View shape in MR control](mixed-reality-component-view-shape.md)

[!INCLUDE[footer-include](../../includes/footer-banner.md)]
