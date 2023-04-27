---
title: Barcode reader control in Power Apps
description: Learn about the details, properties and examples of the Barcode reader control in Power Apps.
author: anuitz
ms.topic: reference
ms.custom: canvas
ms.date: 10/18/2022
ms.subservice: canvas-maker
ms.author: anuitz
ms.reviewer: mkaur
search.audienceType:
  - maker
contributors:
  - anuitz
---
# Barcode reader control in Power Apps

Scans barcodes, QR codes, and data-matrix codes on Android, iOS, and Windows devices.

:::image type="content" source="./media/control-barcode-reader/barcode-hero.gif" alt-text="A gif showcasing the different capabilities of the barcode reader control.":::

## Description

The control opens a native scanner on Android, iOS, and Windows devices. On iOS and Android, the scanner supports the following scanning modes:

- **Automatically scan** – A barcode is scanned as soon as it's detected.
- **Select to scan** – The user can determine which of the detected barcodes to scan. The control doesn't support scanning in a web browser.
- **Scan multiple** – The user can scan multiple barcodes during the barcode session.

On Windows devices, the barcode reader will always **automatically scan**.

The barcode reader control supports different zoom levels and turning on/off the device's flashlight from within the scanning experience.

> [!NOTE]
> The barcode scanner control is supported on Android, iOS, and Windows devices. All other platforms will show a warning stating that some features of the app won't work.

:::image type="content" source="./media/control-barcode-reader/barcode-three-screens.PNG" alt-text="A set of three screens side-by-side showing the different capabilities of the barcode reader control.":::

## Key properties

**Barcodes** – Output property that contains a table of the barcodes scanned with two columns: **Value**, and **Type**. **Value** is the text value of the code that was scanned, while **Type** is the type of the code that was scanned.

**OnScan** – Actions to perform when a barcode is successfully scanned.

**OnCancel** – Actions to perform when a barcode scan is canceled by the user.

**OnChange** - Actions to perform when a property on the barcode reader control is changed, including output properties.

**BarcodeType** - The barcode type to scan. You can target multiple barcode types by concatenating them. Ex. `'Microsoft.BarcodeReader.BarcodeType'.Code128 & 'Microsoft.BarcodeReader.BarcodeType'.Code39`.  **Default: Auto**

**Scanning mode** - Whether to `Automatically scan` the first barcode detected in view, to allow the user to `Select to scan` which of the barcodes in view to scan, or to `Scan multiple` barcodes in a single session. On Windows, the barcode reader will always `Automatically scan`.

**Scanning quality** - The image quality the barcode reader scans at. A higher quality is good for small barcodes, but could lead to slow performance. On Windows, the barcode reader will always scan at the device's camera quality. **Default: Automatic**.

**PreferFrontCamera** - If enabled the barcode reader will default to using the front facing camera instead of the rear facing camera.

**BeepOnScan** - If enabled, the barcode reader will play a beep noise when a barcode is scanned.

**VibrateOnScan** - If enabled, the barcode reader will vibrate when a barcode is scanned.

## Additional properties

**Text** - Text that appears on the button that activates the scanner.

**[BorderColor](properties-color-border.md)** – The color of a control's border.

**[BorderStyle](properties-color-border.md)** – Whether a control's border is **Solid**, **Dashed**, **Dotted**, or **None**.

**[BorderThickness](properties-color-border.md)** – The thickness of a control's border.

**[DisplayMode](properties-core.md)** – Whether the control allows user input (**Edit**), only displays data (**View**), or is disabled (**Disabled**).

**[Height](properties-size-location.md)** – The height of the button that activates the scanner.

**[Tooltip](properties-core.md)** – Explanatory text that appears when the user hovers over a control.

**[Visible](properties-core.md)** – Whether a control appears or is hidden.

**[Width](properties-size-location.md)** – The width of the button that activates the scanner.

**[X](properties-size-location.md)** – The distance between the left edge of a control and the left edge of its parent container (screen, if no parent container).

**[Y](properties-size-location.md)** – The distance between the top edge of a control and the top edge of the parent container (screen, if no parent container).

## Accessibility guidelines

The same guidelines for the **[Button](control-button.md)** control apply to the **Barcode reader** control because it's a button that launches the scan.

### Visual alternatives

* The barcode scanner is a button that doesn't display the scan result. Consider showing the scan result with a **[Label](control-text-box.md)** control. Set the label's **[Text](properties-core.md)** property to `First(BarcodeReader.Barcodes).Value` where `BarcodeReader` is the name of the barcode reader control. Set the label's **[Live](properties-accessibility.md)** property to **Polite** so that screen-reader users are notified of changes. This change makes the scanned value accessible to everyone, irrespective of visual ability.

* Users who have visual and motor disabilities might prefer not to point the camera at a barcode. Consider adding another form of input, such as a **[Text input](control-text-input.md)** control, for users to enter barcodes.

## Barcode Availability by Device

| Barcode Type | Supported on iOS and Android | Supported on Windows | Notes |
|--------------|:---:|:---:|:--------:|
| QR_CODE | ✔ | ✔ | |
| DATA_MATRIX | ✔ | ✖ | |
| AZTEC | ✔ | ✖ | |
| CODABAR | ✔ | ✔ | |
| CODE_128 | ✔ | ✔ | |
| CODE_39 | ✔ | ✔ | |
| CODE_93 | ✔ | ✖ | |
| EAN | ✔ | ✔ | Supports EAN_8 and EAN_13 |
| Interleaved 2 of 5 <br> ITF | ✔ | ✖ | |
| PDF_417 | ✔ | ✖ | |
| RSS14 <br> Databar 14 | ✔ | ✖ | Android and iOS support Stacked and Omnidirectional |
| RSS_EXPANDED <br> Databar Expanded | ✔ | ✖ | Android and iOS support Stacked and Omnidirectional |
| UPC | ✔ | ✔ | Supports UPC_A and UPC_E |
| Micro QR Code | ✔ | ✖ | |
| GS1-DWCode | ✖ | ✖ | |
| MSI | ✖ | ✖ | |

## Select() barcode reader control

The barcode reader control doesn't support Select(). As a workaround, set the barcode reader fill color to transparent and put it in front of the control you wanted to select the barcode reader with. This will result in the same experience for the app user where selecting the control launches the barcode reader experience as they will be selecting an invisible barcode reader button instead of the actual control.

### See also

[Limitations of controls in Power Apps](../control-limitations.md)

[!INCLUDE[footer-include](../../../includes/footer-banner.md)]
