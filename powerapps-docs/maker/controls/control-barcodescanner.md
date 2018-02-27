---
title: 'Barcode scanner control: reference | Microsoft Docs'
description: Information, including properties and examples, about the barcode scanner control
services: ''
suite: powerapps
documentationcenter: na
author: fikaradz
manager: anneta
editor: ''
tags: ''

ms.service: powerapps
ms.devlang: na
ms.topic: article
ms.tgt_pltfrm: na
ms.workload: na
ms.date: 10/25/2016
ms.author: fikaradz

---
# Barcode scanner control in PowerApps
A control with which the user can take photos by using the barcode scanner on the device.

## Description
If you add this control, the user can update a data source with one or more photos from wherever the app is running.

## Key properties
**barcode scanner** – On a device that has more than one barcode scanner, the numeric ID of the barcode scanner that the app uses.

## Additional properties
**[BorderColor](properties-color-border.md)** – The color of a control's border.

**[BorderStyle](properties-color-border.md)** – Whether a control's border is **Solid**, **Dashed**, **Dotted**, or **None**.

**[BorderThickness](properties-color-border.md)** – The thickness of a control's border.

**Brightness** – How much light the user is likely to perceive in an image.

**Contrast** – How easily the user can distinguish between similar colors in an image.

**[DisplayMode](properties-core.md)** – Whether the control allows user input (**Edit**), only displays data (**View**), or is disabled (**Disabled**).

**[Height](properties-size-location.md)** – The distance between a control's top and bottom edges.

**[OnSelect](properties-core.md)** – How the app responds when the user taps or clicks a control.

**OnStream** – How the app responds when the **Stream** property is updated.

**Photo** – The image captured  when the user takes a picture.

**Stream** – Automatically updated image based on the **StreamRate** property.

**StreamRate** – How often to update the image on the **Stream** property, in milliseconds.  This value can range from 100 (1/10th of a second) to 3,600,000 (1 hour).

**[Tooltip](properties-core.md)** – Explanatory text that appears when the user hovers over a control.

**[Visible](properties-core.md)** – Whether a control appears or is hidden.

**[Width](properties-size-location.md)** – The distance between a control's left and right edges.

**[X](properties-size-location.md)** – The distance between the left edge of a control and the left edge of its parent container (screen if no parent container).

**[Y](properties-size-location.md)** – The distance between the top edge of a control and the top edge of the parent container (screen if no parent container).

**Zoom** – The percentage by which an image from a barcode scanner is magnified or the view of a file in a PDF viewer.

## Related functions
[**Patch**( *DataSource*, *BaseRecord*, *ChangeRecord* )](../../functions/function-patch.md)

## Example
### Add photos to an Image gallery control
1. Add a **barcode scanner** control, name it **Mybarcode scanner**
   
    Don't know how to [add, name, and configure a control](../add-configure-controls.md)?
2. Add a **Label** control and set its output to the Barcode's value.  
3. Scan a barcode of the type set under BarcodeType property.
4. The label is going to display the scanned barcode.

