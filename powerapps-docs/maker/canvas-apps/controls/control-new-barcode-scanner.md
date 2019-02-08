---
title: 'Barcode-scanner control: reference | Microsoft Docs'
description: Information, including properties and examples, about the barcode-scanner control
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
# Barcode-scanner control for canvas apps

Scans barcodes, QR codes, and data-matrix codes on an Android or iOS device. Not supported in a web browser.

## Description

The control opens a native scanner on an Android or iOS device. The scanner automatically detects a barcode, a QR code, or a data-matrix code when in view. The control doesn't support scanning in a web browser.

The control supports QR codes, data-matrix codes, and these types of barcodes:

- UPC A
- UPC E
- EAN 8
- EAN 13
- CODE 39
- CODE 128
- ITF
- PDF 417

## Key properties

**Value** – Output property that contains the text value of the code that was scanned most recently.

**Text** - Text that appears on the button that activates the scanner.

**OnScan** – How an app responds when a barcode is successfully scanned.

## Additional properties

**[BorderColor](properties-color-border.md)** – The color of a control's border.

**[BorderStyle](properties-color-border.md)** – Whether a control's border is **Solid**, **Dashed**, **Dotted**, or **None**.

**[BorderThickness](properties-color-border.md)** – The thickness of a control's border.

**[DisplayMode](properties-core.md)** – Whether the control allows user input (**Edit**), only displays data (**View**), or is disabled (**Disabled**).

**FlashlightEnabled** - Whether the flashlight is enabled automatically when the scanner is opened.

**[Height](properties-size-location.md)** – The height of the button that activates the scanner.

**[Tooltip](properties-core.md)** – Explanatory text that appears when the user hovers over a control.

**Type** - The type of code that was detected in the scan that succeeded most recently.

**[Visible](properties-core.md)** – Whether a control appears or is hidden.

**[Width](properties-size-location.md)** – The width of the button that activates the scanner.

**[X](properties-size-location.md)** – The distance between the left edge of a control and the left edge of its parent container (screen if no parent container).

**[Y](properties-size-location.md)** – The distance between the top edge of a control and the top edge of the parent container (screen if no parent container).
