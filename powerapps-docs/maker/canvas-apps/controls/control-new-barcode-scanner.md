---
title: Barcode scanner control in Power Apps
description: Learn about the details, properties and examples of the Barcode scanner control in Power Apps.
author: chmoncay
ms.service: powerapps
ms.topic: reference
ms.custom: canvas
ms.date: 07/07/2021
ms.subservice: canvas-maker
ms.author: chmoncay
ms.reviewer: tapanm
search.audienceType:
  - maker
search.app:
  - PowerApps
contributors:
  - tapanm-msft
  - chmoncay
---
# Barcode scanner control in Power Apps

Scans barcodes, QR codes, and data-matrix codes on an Android or iOS device.

## Description

The control opens a native scanner on an Android or iOS device. The scanner automatically detects a barcode, a QR code, or a data-matrix code when in view. The control doesn't support scanning in a web browser.

> [!NOTE]
> The barcode scanner control is only supported on Android and iOS devices. All other platforms will show a warning that some features of the app won't work.

## Key properties

**Value** – Output property that contains the text value of the code that was scanned most recently.

**Type** – Output property that contains the type of the code that was scanned most recently.

**OnScan** – Actions to perform when a barcode is successfully scanned.

**OnCancel** – Actions to perform when a barcode scan is canceled by the user.

**BarcodeType** - The barcode type to scan. You can target multiple barcode types by concatenating them. Ex. BarcodeType.Code128 & BarcodeType.Code39  **Default: Auto**

**PreferFrontCamera** - Whether the front-facing camera, when available, is used for scanning.

**FlashlightEnabled** - Whether the flashlight is enabled automatically when the scanner is opened.

## Additional properties

**Text** - Text that appears on the button that activates the scanner.

**[BorderColor](properties-color-border.md)** – The color of a control's border.

**[BorderStyle](properties-color-border.md)** – Whether a control's border is **Solid**, **Dashed**, **Dotted**, or **None**.

**[BorderThickness](properties-color-border.md)** – The thickness of a control's border.

**[DisplayMode](properties-core.md)** – Whether the control allows user input (**Edit**), only displays data (**View**), or is disabled (**Disabled**).

**[Height](properties-size-location.md)** – The height of the button that activates the scanner.

**[Tooltip](properties-core.md)** – Explanatory text that appears when the user hovers over a control.

**Type** - The type of code that was detected in the scan that succeeded most recently.

**[Visible](properties-core.md)** – Whether a control appears or is hidden.

**[Width](properties-size-location.md)** – The width of the button that activates the scanner.

**[X](properties-size-location.md)** – The distance between the left edge of a control and the left edge of its parent container (screen, if no parent container).

**[Y](properties-size-location.md)** – The distance between the top edge of a control and the top edge of the parent container (screen, if no parent container).

## Accessibility guidelines
The same guidelines for the **[Button](control-button.md)** control apply to the **Barcode scanner** control because it's a button that launches the scan.

### Visual alternatives
* The barcode scanner is a button that doesn't display the scan result. Consider showing the scan result with a **[Label](control-text-box.md)** control. Set the label's **[Text](properties-core.md)** property to the barcode scanner's **Value** property. Set the label's **[Live](properties-accessibility.md)** property to **Polite** so that screen-reader users are notified of changes. This change makes the scanned value accessible to everyone, irrespective of visual ability.

* Users who have visual and motor disabilities might prefer not to point the camera at a barcode. Consider adding another form of input, such as a **[Text input](control-text-input.md)** control, for users to enter barcodes.

## Barcode Availability by Device

| Barcode Type | Android | iOS |
|--------------|:-------:|:---:|
|QR_CODE|✔|✔|
|DATA_MATRIX|✔|✔|
|UPC_A|✔|✔|
|UPC_E|✔|✔|
|EAN_8|✔|✔|
|EAN_13|✔|✔|
|CODE_39|✔|✔|
|CODE_93|✔|✔|
|CODE_128|✔|✔|
|CODABAR|✔|✖|
|ITF|✔|✔|
|RSS14|✔|✖|
|PDF_417|✔|✔|
|RSS_EXPANDED|✔|✖|
|MSI|✖|✖|
|AZTEC|✔|✔|

> [!NOTE]
> PDF_417 and AZTEC aren't supported in Auto mode.

### See also

[Limitations of controls in Power Apps](../control-limitations.md)


[!INCLUDE[footer-include](../../../includes/footer-banner.md)]
