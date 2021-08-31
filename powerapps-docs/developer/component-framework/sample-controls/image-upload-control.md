---
title: " Image Upload component| Microsoft Docs"
description: "This sample component renders as an `Upload` button to upload the image and a default image when the component loads for the first time."
ms.custom: ""
manager: kvivek
ms.date: 6/08/2021
ms.service: "powerapps"
ms.topic: "article"
ms.author: "nabuthuk"
author: nkrb
---

# Implementing an image upload component

This sample component renders as an `Upload` button to upload the image and a default image when the component loads for the first time. When you click on the `Upload`, a file explorer pops up to pick an image.

[!INCLUDE[cc-terminology](../../data-platform/includes/cc-terminology.md)]

The selected image renders within the component. Meanwhile, the `Remove` button is shown if we need to reset. When you click on the `Remove` button, the default image is displayed.

> [!div class="mx-imgBorder"] > ![Image Upload component](../media/image-upload-control.png "Image Upload component")

## Available for

Model-driven apps

## Code

You can download the complete sample component from [here](https://github.com/microsoft/PowerApps-Samples/tree/master/component-framework/ImageUploadControl).

This sample shows how to create an image picker and showcases the device API and resources API to load the image defined in manifest. Image content is stored in base64 encoding and could be saved and revisited.

The `resources.getResource` method takes the input as the web resource name defined in the component manifest and loads that web resource. The component renders an `Upload` button and the default image for initial rendering. Images are defined in the manifest’s [resource](../reference/resources.md) node.

```xml
    <resources>
      <code path="index.ts" order="1" />
	    <css path="css/TS_ImageUploadControl.css" order="1" />
      <img path="img/default.png" />
      <resx path="strings/TSImageUploadControl.1033.resx" version="1.0.0" />
    </resources>
```

The `successCallback` will be triggered and the resource content injects in the `successCallback`. Then you use the image element 'src' points to the content and the default image loads.

The `device.pickFile` method opens a dialog box to select files for the upload. For desktop, it opens the file explorer, for the mobile client, it opens the library of the photo. When you click on the `upload` button, the device API `pickFile` triggers and the user picks up the file. Once the file is successfully picked, the file's filename, file content will be injected in the `successCallback`.

> [!NOTE]
> If the same form or table is used on the legacy web client, then the field will show out-of-box text component on legacy web client, where there might have UX issues.  To make it hidden on the legacy web client, we could uncheck the **Visibility** checkbox and check **Hide Default Control** checkbox together.

### Related topics

[Download sample components](https://github.com/microsoft/PowerApps-Samples/tree/master/component-framework)<br/>
[How to use the sample components](../use-sample-components.md)<br/>
[Power Apps component framework API reference](../reference/index.md)<br/>
[Power Apps component framework manifest schema reference](../manifest-schema-reference/index.md)

[!INCLUDE[footer-include](../../../includes/footer-banner.md)]
