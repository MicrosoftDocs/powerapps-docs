<properties
    pageTitle="Scan a barcode | Microsoft PowerApps"
    description="Scan a variety of barcode types, such as Codabar and UPC"
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

1. [Sign up for PowerApps](signup-for-powerapps.md), and then do *either* of the following:

	- [Open PowerApps](https://create.powerapps.com/api/start) in a browser.
	- [Install PowerApps](http://aka.ms/powerappsinstall) from the Windows Store. Open PowerApps, sign in, and then click or tap **New** on the **File** menu (along the left edge).

1. Under **Create an app**, click or tap **Phone layout** in the **Blank app** tile.

	![Create an app from scratch](./media/scan-barcode/create-from-blank.png)

1. On the **Insert** tab, click or tap **Media**, and then click or tap **Barcode**.

	![Add barcode scanner](./media/scan-barcode/add-scanner.png)

1. (optional) If you don't expect to scan a UPC barcode, change the type of barcode that you expect to scan.

	1. Ensure that the **Barcode** control is selected by confirming that a selection box (with handles to resize the control) surrounds it.

	![Selection box](./media/scan-barcode/selection-box.png)

	1. Ensure that the properties list shows **BarcodeType**.

	![BarcodeType in properties list](./media/scan-barcode/barcodetype-property.png)

	1. Click or tap in the formula bar, and then press Backspace three times to remove **UPC** but not the period.

	![Select barcode type](./media/scan-barcode/select-type.png)

	1. In the list of barcode types, click or tap the type of barcode that you expect to scan.

1.
