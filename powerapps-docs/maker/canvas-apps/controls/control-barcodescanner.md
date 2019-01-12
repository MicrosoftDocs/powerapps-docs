---
title: 'Web barcode-scanner control: reference | Microsoft Docs'
description: Information, including properties and examples, about the barcode-scanner control
author: fikaradz
manager: kvivek
ms.service: powerapps
ms.topic: reference
ms.custom: canvas
ms.date: 10/25/2016
ms.author: fikaradz
ms.reviewer: anneta
search.audienceType:
  - maker
search.app:
  - PowerApps
---
# Web barcode-scanner control (experimental) in PowerApps

The legacy barcode-scanning control, which is obsolete but might be useful for scanning codes in a web browser.

## Description

The control shows the camera feed in the app so that users can scan barcodes on all devices. The control is obsolete due to poor performance, and the mobile **[Barcode scanner](control-new-barcode-scanner.md)** control replaces this control.

## Key properties

**barcode scanner** – On a device that has more than one barcode scanner, the numeric ID of the barcode scanner that the app uses.

## Additional properties

**[AccessibleLabel](properties-accessibility.md)** – Label for screen readers.

**[BorderColor](properties-color-border.md)** – The color of a control's border.

**[BorderStyle](properties-color-border.md)** – Whether a control's border is **Solid**, **Dashed**, **Dotted**, or **None**.

**[BorderThickness](properties-color-border.md)** – The thickness of a control's border.

**[DisplayMode](properties-core.md)** – Whether the control allows user input (**Edit**), only displays data (**View**), or is disabled (**Disabled**).

**[Height](properties-size-location.md)** – The distance between a control's top and bottom edges.

**ShowLiveBarcodeDetection** – Whether visual cues are shown to indicate the status of barcode detection. Yellow rectangles represent areas that are being examined. A green line across a rectangle indicates successful barcode identification.

**Stream** – Automatically updated image based on the **StreamRate** property.

**StreamRate** – How often to update the image on the **Stream** property, in milliseconds.  This value can range from 100 (1/10th of a second) to 3,600,000 (1 hour).

**Text** – Value of barcode that was last identified by the scanner.

**[Tooltip](properties-core.md)** – Explanatory text that appears when the user hovers over a control.

**[Visible](properties-core.md)** – Whether a control appears or is hidden.

**[Width](properties-size-location.md)** – The distance between a control's left and right edges.

**[X](properties-size-location.md)** – The distance between the left edge of a control and the left edge of its parent container (screen if no parent container).

**[Y](properties-size-location.md)** – The distance between the top edge of a control and the top edge of the parent container (screen if no parent container).

## Related functions

[**Patch**( *DataSource*, *BaseRecord*, *ChangeRecord* )](../functions/function-patch.md)

## Example

### Add photos to an Image gallery control

1. Add a **barcode scanner** control, name it **Mybarcode scanner**

    Don't know how to [add, name, and configure a control](../add-configure-controls.md)?

1. Add a **Label** control, and set its output to the barcode scanner's **Text** property.

1. Scan a barcode of the type set under **BarcodeType** property.

    The label displays the scanned barcode.

## Accessibility guidelines

### Video alternatives

* Consider adding a **[Label](control-text-box.md)** with its **[Text](properties-core.md)** set to the barcode scanner's **Text**. Since the barcode scanner does not display the identified barcode value, doing the above makes the scanner accessible to everyone, not just those with visual disabilities.

### Screen reader support

* **[AccessibleLabel](properties-accessibility.md)** must be present.

    > [!NOTE]
  > Screen readers will announce when a new barcode has been found. The value won't be announced. As long as the barcode is in view, screen readers will remind the user every five seconds that the same barcode is still being identified.
