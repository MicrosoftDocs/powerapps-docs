---
title: Connect 3D models to Power Apps
description: Load 3D models into Power Apps from attachments, media content, direct URLs, or Base64-encoded URIs.
author: anuitz
ms.topic: how-to
ms.custom: canvas
ms.reviewer: mkaur
ms.date: 3/4/2022
ms.subservice: canvas-maker
ms.author: anuitz
search.audienceType: 
  - maker
contributors:
  - mduelae
  - anuitz
---

# Load 3D models in canvas apps

Load a 3D model in your canvas apps from a variety of sources. You can get models from attachments or media content, a direct URL, or a Base64-encoded URI (uniform resource identifier).

Make sure your 3D models are [optimized for use with Power Apps](/dynamics365/mixed-reality/guides/3d-content-guidelines/optimize-models) to minimize load times.

## Loading 3D models from common connectors

Loading 3D models from attachments or media content depends on how a data connector is supported. To check if a data connector will work the mixed reality controls, add a label control to the canvas app and set the **Text** property to the data source. If the label text starts with `appres://`,then that data connector should work with the **3D object control**.

> [!TIP]
> You can rename a .glb file extension to .jpg and directly upload it to the app through the Media tab.


### Load 3D models from Microsoft Lists

First, create a list in SharePoint and add an entry for each 3D model that you want to have in your app.

1. [Create a list using Microsoft Lists](https://go.microsoft.com/fwlink/?linkid=2186009).
2. Select the **+ Add column** column heading and then select **Show/hide columns**.
3. Select **Attachments** and then select **Apply**.
4. Add an entry to the list. In the entry form, select **Add attachments** and select your 3D model file.
5. Repeat for each model you want to include in your app.

Then, add a gallery to your app, set its source to the list, add a **3D object** control, and set its source to the gallery.

1. [Add a gallery](./add-gallery.md) in Power Apps Studio.
2. Set the gallery data source to the list.
3. [Add the **3D object** control](./mixed-reality-component-view-3d.md).
4. In the **Advanced** properties tab, set **Source** to **First(Gallery1.Selected.Attachments).Value**.

### Load 3D models from an Excel workbook

First, create an Excel workbook in OneDrive in the same folder that contains your model files. Add a table with rows for each model that you want to have in your app.

1. Create an Excel workbook and save it in the OneDrive folder that contains your model files.

    :::image type="content" source="./media/augmented-3d/augmented-3d-onedrive-list.png" alt-text="A screenshot of OneDrive that shows the Excel workbook ModelGallery and its accompanying 3D model files.":::

2. In the workbook, create a table with columns named **3DModel [image]** and **Name**.
3. Add a row for each model you want to show in the app gallery. Enter a label for the model in the **Name** column and the relative file path to the model file in the **3DModel [image]** column.

    :::image type="content" source="./media/augmented-3d/augmented-3d-excel-list.png" alt-text="{A screenshot of an Excel table with columns for the name of a 3D model and the path to the object file.}":::

4. Close the workbook.

Then, add a gallery to your app, set its source to the Excel workbook, add a **3D object** control, and set its source to the gallery.
  
1. [Add a gallery](./add-gallery.md) in Power Apps Studio.
2. Use the OneDrive connector to set the gallery data source to the Excel workbook.
3. [Add the **3D object** control](./mixed-reality-component-view-3d.md).
4. In the **Advanced** properties tab, set **Source** to **Gallery1.Selected.'3DModel'**.

### Load 3D models from a URL

The **Source** property of the **3D object** control can be the URL of a 3D model file.

The 3D model file must be on a server that doesn't have restrictive cross-origin resource sharing (CORS) settings. The hosting server must permit cross-origin requests from *powerapps.com*. You can use Dropbox or GitHub to host your files and get a CORS-compliant URL.

#### Host your 3D model files in Dropbox

1. Upload a 3D model file to Dropbox and select **Share**.
1. Generate a public download link. For example, *<https://www.dropbox.com/s/rANdoMGeneR4tedLink/my-file.glb?dl=0>*.
1. Modify the URL like this: replace **www** with **dl**, and remove **?dl=0** at the end.

You now have a direct-access URL (in our example, *<https://dl.dropbox.com/s/rANdoMGeneR4tedLink/my-file.glb>*), that you can use as the source of your 3D control.

#### Host your 3D model files in GitHub

1. Make sure the 3D model file is stored in a public repo.
2. Get the URL of the file. For example, *<https://github.com/microsoft/experimental-pcf-control-assets/blob/master/robot_arm.glb>*.
3. Modify the URL like this: remove **/blob/**, and replace **<https://github.com>** with **<https://raw.githubusercontent.com>**.

You now have a CORS-compliant URL (in our example, *<https://raw.githubusercontent.com/microsoft/experimental-pcf-control-assets/master/robot_arm.glb>*), that you can use as the source of your 3D control.

### Load Base64-encoded 3D models

The **Source** property of the **3D object** control can be a Base64-encoded 3D model data URI that is in the format *data:base64,\<Base64-encoded content\>*.

> [!IMPORTANT]
> Your app may take longer to load if you use Base64-encoded models.

You can create a Base64-encoded URI of your model using Microsoft Power Automate or Microsoft Dataverse.

#### Create a Base64-encoded 3D model with Microsoft Power Automate

Power Automate can convert 3D model files stored in a SharePoint document library to Base64 using the **dataUri(base64(*file content*))** expression.

In the following example, a document library named *3DModelBase64Library* and a list named *3DModelBase64* exist in the same SharePoint site. The list must include a column of type **multiple-line text**.

1. In the document library, [create a flow](/power-automate/sharepoint-overview) based on the **When a new file is added in SharePoint, complete a custom action** template.
2. Set **Library Name** to *3DModelBase64Library* (the name of the document library in this example).
3. Add a step, **Get file content from SharePoint**.
4. Set **File Identifier** to **Identifier**.
5. Add a step, **Create item from SharePoint**.
6. Set **List Name** to *3DModelBase64* (the name of the list in this example) and **Title** to **File Name with extension**.
7. Set **dataUri** to the following expression:

    ```concat('data:model/gltf-binary;base64,', Last(split(dataUri(base64(body('Get_file_content'))), ',')))```

    :::image type="content" source="./media/augmented-3d/augmented-3d-convert-flow.png" alt-text="A screenshot of a Power Automate workflow that shows the steps to convert 3D model files in a SharePoint document library to Base64.":::

The flow runs when a file is added to the document library, converting the file to a Base64-encoded data URI.

In Power Apps Studio, connect the **3D object** control to the list using the SharePoint data connector. Set the control's **Source** property to the Base64-encoded data URI.

#### Create a Base64-encoded 3D model with Microsoft Dataverse

The [Note (Annotation) table](../../developer/data-platform/reference/entities/annotation.md) in Microsoft Dataverse converts any file attached in the **Document** field to Base64.

## Known constraints when loading 3D models from URLs in canvas apps

- The security architecture of Power Apps requires HTTPS links, not HTTP.
- The server that hosts the model files must not require authentication and must be CORS-compliant.

[!INCLUDE[footer-include](../../includes/footer-banner.md)]
