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

The Power Apps mobile app can optimize images before they get uploaded to Dataverse. This means reducing the file size while preserving the visual quality of the image as much as possible.
This is very useful for performance and cost savings. When this feature is enabled, user experience is smoother both when uploading images from Dataverse and when downloading images that were uploaded with optimization.

> [!Important]
> -	This feature is available on both canvas apps and model-driven apps. However, for model-driven apps it’s only available starting with version 3.2308.1
> -	This feature is not supported on Power Apps for Windows

If enabled, the image optimization is applied when using:
-	An out-of-the-box control.
-	A PCF control using PCF APIs to deal with images.
-	For model-driven apps: any customization that uses client APIs to deal with images. More information: [Xrm.Device (Client API reference)](/power-apps/developer/model-driven-apps/clientapi/reference/xrm-device)

Images uploaded with other mechanisms will not benefit from this feature. 


Should you want to opt out from this feature, you can do so by switching the toggle “optimize images for upload” off:
