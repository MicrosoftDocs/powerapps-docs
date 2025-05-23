---
title: Image control in cards for Power Apps
description: Learn about the properties of the image control in cards for Power Apps.
author: anuitz
ms.topic: reference
ms.custom: 
ms.reviewer: mkaur
ms.date: 03/01/2023
ms.author: anuitz
search.audienceType:
  - maker
contributors:
  - mduelae
  - anuitz
---

# Image control in cards

[!INCLUDE[cards-deprecation-banner](~/includes/cards-deprecation-notice.md)]

An image with properties to control what the image looks like. Supports publicly accessible and CORS-compliant URLs as well as base64 encoded images.

Use the [media control](media.md) for video and audio files.

## Properties

**[Url](control-reference.md#u)** – The URL to the image. Supports data URI in version 1.2+.

**[Initially visible](control-reference.md#i)** – If false, this item will be removed from the visual tree.

**[Alt text](control-reference.md#a)** – Alternate text describing the image.

**[Spacing](control-reference.md#s)** – Controls the amount of spacing between this control and the preceding control.

**[Divider](control-reference.md#d)** – When true, draw a separating line at the top of the control.

**[Horizontal alignment](control-reference.md#h)** – Controls how this control is horizontally positioned within its parent.

**[Size](control-reference.md#s)** – Controls the approximate size of the image. The physical dimensions will vary per host.

**[Height](control-reference.md#h)** – The desired height of the image. If specified as a pixel value, ending in 'px', E.g., "50px", the image will distort to fit that exact height. This overrides the size property.

**[Width](control-reference.md#w)** – The desired on-screen width of the image, ending in 'px'. E.g., "50px". This overrides the size property.

**[Style](control-reference.md#s)** – Controls how this image is displayed.

**[Background color](control-reference.md#b)** – Applies a background to a transparent image. This property will respect the image style.

**[Repeat for every](control-reference.md#r)** – The source of data that is used to show multiple instances of this control. Learn how to use [repeat for every](control-reference.md#r).
