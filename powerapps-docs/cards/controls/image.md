---
title: Image control for cards in Power Apps
description: Learn about the details, properties and examples of the image control for cards in Power Apps.
author: anuitz
ms.topic: reference
ms.custom: 
ms.reviewer: mkaur
ms.date: 03/01/2023
ms.author: anuitz
search.audienceType:
  - maker
search.app:
  - PowerApps
contributors:
  - mduelae
  - anuitz
---

# Image control for cards in Power Apps

An image with properties to control what the image looks like.

## Description


## Properties

**[Name](../control-reference.md#n)** – A unique identifier associated with the item.

**[Url](../control-reference.md#n)** – The URL to the image. Supports data URI in version 1.2+.

**[Initially visible](../control-reference.md#i)** – If false, this item will be removed from the visual tree.

**[Alt text](../control-reference.md#a)** – Alternate text describing the image.

**[Spacing](../control-reference.md#s)** – Controls the amount of spacing between this control and the preceding control.

**[Divider](../control-reference.md#d)** – When true, draw a separating line at the top of the control.

**[Horizontal alignment](../control-reference.md#h)** – Controls how this control is horizontally positioned within its parent.

**[Size](../control-reference.md#s)** – Controls the approximate size of the image. The physical dimensions will vary per host.

**[Height](../control-reference.md#h)** –The desired height of the image. If specified as a pixel value, ending in 'px', E.g., "50px", the image will distort to fit that exact height. This overrides the size property.

**[Width](../control-reference.md#w)** – The desired on-screen width of the image, ending in 'px'. E.g., "50px". This overrides the size property.

**[Style](../control-reference.md#s)** – Controls how this image is displayed.

**[Background color](../control-reference.md#b)** – Applies a background to a transparent image. This property will respect the image style.

**[Repeat for every](../control-reference.md#r)** – Data context expression.

**[SelectAction](../control-reference.md#s)** – An Action that will be invoked when the column set is tapped or selected. Action.ShowCard is not supported.

**[Requires](../control-reference.md#r)** – A series of key/value pairs indicating features that the item requires with corresponding minimum version. When a feature is missing or of insufficient version, fallback is triggered.



