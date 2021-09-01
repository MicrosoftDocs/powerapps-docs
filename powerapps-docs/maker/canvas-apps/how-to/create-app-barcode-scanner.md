---
title: Create a canvas app with the barcode scanner control
description: Learn how to make a canvas app that uses the barcode scanner control.
author: joel-lindstrom
ms.service: powerapps
ms.topic: article
ms.custom: canvas
ms.reviewer:
ms.date: 09/01/2021
ms.subservice: canvas-maker
ms.author: tapanm
search.audienceType: 
  - maker
search.app: 
  - PowerApps
contributors:
    - joel-lindstrom
    - tapanm-msft
---

# Create a canvas app with the barcode scanner control

The barcode scanner control in Power Apps lets you use your phone or mobile device to scan barcode from [various formats](../controls/control-new-barcode-scanner.md#barcode-availability-by-device).

Some of the common uses of barcode scanner control in a canvas app are:

- An app to check in items like books into a collection
- An inventory management app that uses barcode to identify items
- An employee app to check in and badge scanning for security

In this article, we'll create a canvas app with barcode scanner and display scanned items in a gallery.

## Prerequisites

- [Power Apps license](/power-platform/admin/pricing-billing-skus)
- Before you create an app from scratch, familiarize yourself with Power Apps basics by [generating an app](../get-started-test-drive.md) and then customizing that app's [controls](../add-configure-controls.md), [gallery](../add-gallery.md), [forms](../working-with-forms.md), and [cards](../working-with-cards.md).
- To create an app, you must be assigned to the [Environment Maker](/power-platform/admin/database-security) security role.

## Open a blank app

1. Sign in to [Power Apps](https://make.powerapps.com).

1. Under **Make your own app**, select **Canvas app from blank**.

1. Enter a name for your app, select **Phone**, and then select **Create**.

    ![Name the app](media/ceate-app-barcode-scanner/open-a-blank-app-1.png)

## Add barcode scanner

1. From the left-pane, select **Screen1**.

1. From the left-pane, select **+ Insert** > expand **Media** > select **Barcode scanner** control.

    ![ Select barcode scanner](media/ceate-app-barcode-scanner/select-barcode-scanner.png "Select barcode scanner")

1. From the properties list on the right-side of the screen, select **Advanced** tab, and then select the **OnScan** property.

    ![OnScan property](media/ceate-app-barcode-scanner/select-advanced-onscan.png "OnScan property")

1. Set the **OnScan** property of the Barcode scanner control to this expression by typing or pasting it in the formula bar.

    ```powerapps-dot
    Collect(
        colScannedItems,
        {ScannedItem: BarcodeScanner1.Value, ScannedTime: Now()}
    )
    ```

    ![OnScan property of the Barcode scanner control](media/ceate-app-barcode-scanner/add-barcode-scanner-3.png "OnScan property of the Barcode scanner control")

1. From the **Properties** pane, set **X** property to "180" and the **Y** property to "1005".

    ![X and y properties](media/ceate-app-barcode-scanner/add-barcode-scanner-4.png "X and y properties")

## Add gallery

1. Select **+ Insert** > expand **Layout** > select **Vertical gallery** control.

    ![Gallery types select Vertical](media/ceate-app-barcode-scanner/insert-vertical-gallery.png "Gallery types select Vertical")

1. From the properties pane, select the layout for the gallery as **Title and subtitle**.

    ![Select Title and subtitle](media/ceate-app-barcode-scanner/gallery-title-subtitle.png "Select Title and subtitle")

1. Select the gallery control on canvas.

1. Set the **Items** property of the gallery control to this expression by typing or pasting it in the formula bar.

    ```powerapps-dot
    colScannedItems
    ```

    ![Items property of the Gallery control](media/ceate-app-barcode-scanner/add-gallery-4.png "Items property of the Gallery control")

1. In the left-pane, expand the **Gallery1**, and select **Title2**.

    ![Left navigation bar select Title2](media/ceate-app-barcode-scanner/add-gallery-5.png "Left navigation bar select Title2")

1. Set the **Text** property of **Title2** to the following expression.

    ```powerapps-dot
    ThisItem.ScannedItem
    ```

    ![Text property of the Label control](media/ceate-app-barcode-scanner/add-gallery-7.png "Text property of the Label control")

1. Select **Subtitle2** label, and set it's **Text** property to this expression.

    ```powerapps-dot
    ThisItem.ScannedTime
    ```

    ![Set the Text property of the Label control](media/ceate-app-barcode-scanner/add-gallery-10.png "Set the Text property of the Label control")

## Try the app

1. To test the app, select **Screen1**, and then press **F5** on the keyboard.

1. After testing, [save and publish](../save-publish-app.md) the app.

1. Download [Power Apps Mobile](https://powerapps.microsoft.com/downloads/) on your phone.

1. Open the **Power Apps** app, and sign in.

1. Select and open the barcode scanner app.

    ![Launch your Barcode Scanner application](media/ceate-app-barcode-scanner/test-the-app-2.png "Launch your Barcode Scanner application")

1. Select **Scan**, and scan any barcode label (for example, barcode label on a book).

## Final Results

You'll see the scanned barcode information is saved inside the app.

![Final Results](media/ceate-app-barcode-scanner/final-results-1.png "Final Results")

### See also

[Barcode scanner control in Power Apps](../controls/control-new-barcode-scanner.md)
