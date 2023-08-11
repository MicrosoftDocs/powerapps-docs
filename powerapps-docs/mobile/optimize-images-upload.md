---
title: Optimize images for upload
description: The Power Apps mobile app can optimize images before they get uploaded to Dataverse. 
author: trdehove
ms.component: pa-user
ms.topic: quickstart
ms.date: 08/08/2023
ms.subservice: mobile
ms.author: trdehove
ms.custom: ""
ms.reviewer: sericks
ms.assetid: 
search.audienceType: 
  - enduser
---

# Optimize images for upload

The Power Apps mobile app can optimize images before they get uploaded to Dataverse. This means reducing the file size while preserving the visual quality of the image, as much as possible.

This is very useful for performance and cost savings. When this feature is enabled, the user experience is smoother both when uploading images to Dataverse and when downloading images that were uploaded with optimization.

> [!Important]
> -	This feature is available for both canvas apps and model-driven apps. However, for model-driven apps, it’s only available with version 3.23081.0 or higher.
> -	This feature is not supported on Power Apps for Windows.

## Turn on the feature

1. Open the Power Apps mobile app.
1. From the **Home**, **All apps**, or **More** page, select your profile image. Your user profile page appears.
1. Turn on the **Optimize images for upload** setting.

    :::image type="content" source="media/optimize-images-setting.png" alt-text="Optimize images for upload.":::
    
If enabled, the image optimization is applied when using:
-	An out-of-the-box control.
-	A PCF control using PCF APIs to deal with images.
-	For model-driven apps, any customization that uses client APIs to deal with images. More information: [Xrm.Device (Client API reference)](/power-apps/developer/model-driven-apps/clientapi/reference/xrm-device)

Images uploaded with other mechanisms don't benefit from this feature. 

## Turn off the feature
1. Open the Power Apps mobile app.
1. From the **Home**, **All apps**, or **More** page, select your profile image. Your user profile page appears.
1. Turn off the **Optimize images for upload** setting.
