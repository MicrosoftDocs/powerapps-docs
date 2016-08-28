<properties
    pageTitle="Scan a barcode | Microsoft PowerApps"
    description="Scan a variety of barcode types, such as UPC and Codabar"
    services=""
    suite="powerapps"
    documentationCenter="na"
    authors="aftowen"
    manager="erikre"
    editor=""
    tags=""/>

<tags
   ms.service="powerapps"
   ms.devlang="na"
   ms.topic="article"
   ms.tgt_pltfrm="na"
   ms.workload="na"
   ms.date="08/26/2016"
   ms.author="anneta"/>

# Scan a barcode in Microsoft PowerApps #
Scan several types of barcodes by creating an app and running it on a device, such as a phone, that has a camera. The numerical equivalent of the barcode appears in a **Text box** control, and you can upload that data to a variety of [data sources](connections-list.md).

If you're unfamiliar with PowerApps, see [Get started](getting-started.md).

## Known limitations ##
- Barcodes should be at least 1" (2.5cm) high and 1.5" (4cm) wide.
- To scan barcodes by using a phone, hold it in portrait orientation, and slowly move it from 7" (18cm) to 10" (25cm) away from the barcode.
- Long barcode types (such as I2of5, which can have 15 or more characters) can give truncated or otherwise incorrect results, especially if the barcode isn't printed clearly.
- For iPhones and Android devices, you can specify the **Height** property of the **Barcode** control, but a fixed aspect ratio determines its width.
- To delay running out of memory on devices that are running iOS, set the **Height** property of the **Barcode** control to **700** (or lower) and the **Scanrate** property to **35** (or lower).
- If the device runs out of memory and the app freezes, restart the app.

## Create a blank app ##
1. [Sign up for PowerApps](signup-for-powerapps.md), and then do *either* of the following:

	- [Open PowerApps](https://create.powerapps.com/api/start) in a browser on a device that has a camera.
	- [Install PowerApps](http://aka.ms/powerappsinstall) from the Windows Store on a device that has a camera. Open PowerApps, sign in, and then click or tap **New** on the **File** menu (along the left edge).

1. Under **Create an app**, click or tap **Phone layout** in the **Blank app** tile.

	![Create an app from scratch](./media/scan-barcode/create-from-blank.png)

1. If you haven't used PowerApps before, get familiar with key areas of the app by taking the intro tour (or click or tap **Skip**).

	![Opening screen of the quick tour](./media/scan-barcode/quick-tour.png)

	**Note**: You can always take the tour later by clicking or tapping the question-mark icon near the upper-right corner and then clicking or tapping **Take the intro tour**.

## Add a Barcode control ##
1. On the **Insert** tab, click or tap **Media**, and then click or tap **Barcode**.

	![Add barcode scanner](./media/scan-barcode/add-scanner.png)

1. Ensure that the **Barcode** control is selected by confirming that a selection box (with handles to resize the control) surrounds it.

	![Selection box](./media/scan-barcode/selection-box.png)

1. On the **Home** tab, click or tap **Barcode1**, and then type or paste **MyScanner** under **Rename**.

	**Tip**: The first **Barcode** control that you add is named **Barcode1** by default. If you delete that control and add another **Barcode** control, it will be named **Barcode2** by default. By manually renaming a control, you ensure that formulas will refer to the control by its correct name.

	![Rename the barcode control](./media/scan-barcode/rename-barcode.png)

1. (optional) To change the type of barcode that you expect to scan from **UPC** to another type:

	1. With **MyScanner** selected, ensure that the properties list shows **BarcodeType**.

		![BarcodeType in properties list](./media/scan-barcode/barcodetype-property.png)

	1. Click or tap in the formula bar, and then remove **UPC** but not the period.

		![Select barcode type](./media/scan-barcode/select-type.png)

	1. In the list of barcode types, click or tap the type of barcode that you expect to scan.

## Add a Text box ##
1. On the **Insert** tab, click or tap **Text box**.

	If the **Insert** tab doesn't appear, maximize your PowerApps window.

	![Text box on the Insert tab](./media/scan-barcode/insert-textbox.png)

1. Drag the selection box (not the resize handles) around the **Text box** control down until it appears below **MyScanner**.

	![Text box with selection box](./media/scan-barcode/move-textbox.png)

1. With the **Text box** control still selected, ensure that **Text** appears in the properties list, and then type or paste **MyScanner.Text** in the formula bar.

	![Text property of the Text box control](./media/scan-barcode/text-property.png)

## Test the app ##
1. Open Preview mode by pressing F5 (or by clicking or tapping the play button near the upper-right corner).

	![Open Preview mode](./media/scan-barcode/open-preview.png)

1. Hold a barcode up to the camera on the device until the numerical component of the barcode appears in the **Text box** control.

## Next steps ##
- [Connect the app to a data source](add-data-connection.md) and configure the **[Patch](function-patch.md)** function so that users can save results.
- Add a **[Drop down](control-drop-down.md)** control, and configure it so that users can choose which type of barcode they want to scan.
- Add a **[Slider](control-slider.md)** control, and configure it so that users can adjust the scan rate or the height of the **Barcode** control.
