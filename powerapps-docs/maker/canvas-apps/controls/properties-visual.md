---
title: Image properties in Power Apps
description: Reference information about image properties in Power Apps.
author: chmoncay
ms.service: powerapps
ms.topic: reference
ms.custom: canvas
ms.reviewer: tapanm
ms.date: 07/06/2021
ms.subservice: canvas-maker
ms.author: gregli
search.audienceType: 
  - maker
search.app: 
  - PowerApps
contributors:
  - tapanm-msft
  - chmoncay
---

# Image properties in Power Apps
Configure graphical elements in your app, including images, photos, and elements of a pen control.

**BackgroundImage** – The name of an image file that appears in the background of a screen.

* Applies to the **[Screen](control-screen.md)** control.

**Image** – The name of the image that appears in an image, audio, or microphone control.

* Applies to **[Audio](control-audio-video.md)**, **[Image](control-image.md)**, **[Microphone](control-microphone.md)**, and **[Video](control-audio-video.md)** controls.

**ImagePosition** – The position (**Fill**, **Fit**, **Stretch**, **Tile**, or **Center**) of an image in a screen or a control if it isn't the same size as the image.
- Fill - Fills the entire specified size with the image. Scales the image proportionally. Crops the image as needed.
- Fit - Fits the entire image into the specified size. Scales the image proportionally. Doesn't crop the image.
- Stretch - Fills the entire specified size with the image. Stretches the image disproportionately as needed. Doesn't crop the image.
- Tile - Repeats the image across the control into the specified size.  Doesn't scale the image. Crops the image as needed.
- Center - Places the image in the center of the control. Doesn't scale the image. Crops the image as needed.

* Applies to **[Audio](control-audio-video.md)**, **[Image](control-image.md)**, **[Microphone](control-microphone.md)**, **[Screen](control-screen.md)**, and **[Video](control-audio-video.md)** controls.



[!INCLUDE[footer-include](../../../includes/footer-banner.md)]
