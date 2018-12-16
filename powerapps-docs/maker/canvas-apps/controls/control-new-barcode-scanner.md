---
title: 'Barcode scanner control: reference | Microsoft Docs'
description: Information, including properties and examples, about the barcode scanner control
author: fikaradz
manager: kvivek
ms.service: powerapps
ms.topic: reference
ms.custom: canvas
ms.date: 11/25/2018
ms.author: fikaradz
ms.reviewer: anneta
search.audienceType:
  - maker
search.app:
  - PowerApps
---
# Barcode scanner control in PowerApps
Scans barcodes, QR codes, and data matrix codes with an Android or iOS device.  Not supported in a web browser.

## Description
The control opens a native scanner on Android and iOS devices. The scanner will automatically detect  a barcode, QR code or a data matrix code when in view.  The control does not support scanning in a web browser.

In addition to QR codes and data matrix codes, the following barcodes types are supported: UPC A, UPC E, EAN 8, EAN 13, CODE 39, CODE 128, ITF, PDF 417.

## Key properties
**Value** – Output property containing the text value of the last code that was scanned.

**Text** - Text shown inside the button that activates the scanner.

## Additional properties
**[BorderColor](properties-color-border.md)** – The color of a control's border.

**[BorderStyle](properties-color-border.md)** – Whether a control's border is **Solid**, **Dashed**, **Dotted**, or **None**.

**[BorderThickness](properties-color-border.md)** – The thickness of a control's border.

**[DisplayMode](properties-core.md)** – Whether the control allows user input (**Edit**), only displays data (**View**), or is disabled (**Disabled**).

**FlashlightEnabled** - Whether the flashlight is enabled automatically when the scanner is opened.

**[Height](properties-size-location.md)** – The height of the button that activates the scanner.

**[Tooltip](properties-core.md)** – Explanatory text that appears when the user hovers over a control.

**Type** - The type of code that was detected in the last successful scan.

**[Visible](properties-core.md)** – Whether a control appears or is hidden.

**[Width](properties-size-location.md)** – The width of the button that activates the scanner.

**[X](properties-size-location.md)** – The distance between the left edge of a control and the left edge of its parent container (screen if no parent container).

**[Y](properties-size-location.md)** – The distance between the top edge of a control and the top edge of the parent container (screen if no parent container).
