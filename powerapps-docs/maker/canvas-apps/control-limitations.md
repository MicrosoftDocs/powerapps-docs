---
title: Control limitations for Power Apps | Microsoft Docs
description: Learn about limitations of controls in Power Apps.
author: navjotm
ms.service: powerapps
ms.topic: conceptual
ms.custom: canvas
ms.reviewer: tapanm
ms.date: 01/07/2021
ms.author: namarwah
search.audienceType: 
  - maker
search.app: 
  - PowerApps
---

# Limitations of controls in Power Apps

In this article, learn about the limitations of the controls used in canvas apps inside Microsoft Dataverse environments, and apps made with Power Apps inside Microsoft Teams (Microsoft Dataverse for Teams environments). For more information about environments, go to [Types of environments](https://docs.microsoft.com/power-platform/admin/environments-overview#types-of-environments).

## Limitations of controls in Dataverse environments

This section lists limitations of controls used inside the canvas apps created using Power Apps Studio for Dataverse environments.

- [Attachments control](controls//control-attachments.md) - see [Attachments control limitations](controls//control-attachments.md#limitations).

- [Audio, and video controls](controls/control-audio-video.md) - see [Audio and video alternatives](controls/control-audio-video.md#audio-and-video-alternatives).

- [Barcode control](controls/control-new-barcode-scanner.md), [Camera control](controls/control-camera.md)
    - On iOS, the camera control is supported in the Power Apps for mobile app. It's not supported within the browser or Teams Mobile.
   - On Android, the camera control isn't supported in Teams Mobile.
   - When using Internet Explorer, the camera control isn't supported. Microsoft Edge is recommended.
   - When using desktop browsers, the barcode scanner isn't supported. Use the Power Apps for mobile app.

- [Container control (experimental)](controls/control-container.md) - see [Container control (experimental) limitations](controls/control-container.md#known-limitations).

- [Export and import controls](controls/control-export-import.md) - see [Export and import control limitations](controls/control-export-import.md#limitations).

- [Gallery control](controls/control-gallery.md) - see [Gallery control limitations](controls/control-gallery.md#limitations).

- [Image control](controls/control-image.md) - only supports external media URLs using HTTPS.

- [Power BI tile control](controls/control-power-bi-tile.md) - see [Power BI tile control limitations for passing a parameter](controls/control-power-bi-tile.md#pass-a-parameter).

- [PDF viewer control (experimental)](controls/control-pdf-viewer.md) - see [PDF viewer control (experimental) limitations](controls/control-pdf-viewer.md#limitations).

- [Stream Video control](controls/control-stream-video.md) - see [Stream Video control limitations](controls/control-stream-video.md#limitations).

## Limitations of controls in Dataverse for Teams environments

This section lists limitations of controls used by apps created inside Dataverse for Teams environments (Microsoft Teams integrated Power Apps):

### General limitations

Apps made with Power Apps in a Dataverse for Teams environment can't be opened outside of Teams. To use controls like *Camera*, upgrade your Power Apps license so that the app can be opened outside of Teams&mdash;for example&mdash;in the Power Apps mobile app.

### Limitations of specific controls

- [Barcode control](controls/control-new-barcode-scanner.md) - the barcode scanner control isn't supported in Teams Mobile.

- [Camera control](controls/control-camera.md) - the Camera control isn't supported in Teams Mobile. If you're creating a Power Apps app for use inside Teams, use the [Add picture](controls/control-add-picture.md) control instead.

- [Microphone control](controls/control-microphone.md) - the following conditions apply when using the Microphone control in apps created using Power Apps on Teams Mobile:

    - The audio format for microphone recordings in Teams will always be *AAC* with a file extension of .MP4.
    - Teams has its own recording experience. The microphone control inside apps created using Power Apps will be disabled during the recording period.
    - Microphone recordings are limited to a maximum duration of 10 minutes.

- [Mixed Reality](mixed-reality-overview.md) - within Teams, the Mixed Reality controls aren't supported:
    - View in MR
    - View Shape in MR
    - Measure in MR

### Unsupported controls

The following controls aren't supported by apps made with Power Apps created inside Dataverse for Teams environments:

- [Address Input](geospatial-component-input-address.md)
- [Camera](controls/control-camera.md) (in Teams Mobile)
- [Map](geospatial-component-map.md)
- [Mixed reality](mixed-reality-overview.md) (View in MR, View shape in MR, Measure in MR)

## Next steps

[Controls and properties reference](reference-properties.md)
