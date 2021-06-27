---
title: How to create a Power App with the barcode scanner control
description: Learn how to make a canvas Power App that uses the barcode scanner control.
author: joel-lindstrom
ms.service: powerapps
ms.topic: conceptual
ms.custom: canvas
ms.reviewer: tapanm
ms.date: 06/27/2021
ms.author: v-ljoel
search.audienceType: 
  - maker
search.app: 
  - PowerApps
---
# Example: How to create a Power App with the barcode scanner control
The barcode scanner control in Power Apps lets you use your phone or mobile device to scan barcodes of various formats, including UPC-style barcodes and QR codes. This can be very useful. Here are some common  scenarios:

-   Build an app to check in items like books into a collection

-   Create an inventory management app and use barcodes to quickly identify
    items

-   Make an employee check-in app and scan badges for security

In this topic we will create a simple canvas app with barcode scanner and display scanned items in a gallery.

## Prerequisites

-  Power Apps License ([About Microsoft 365](https://www.microsoft.com/licensing/product-licensing/microsoft-365-enterprise?activetab=m365enterprise%3aprimaryr5)

-  Before you create an app from scratch, familiarize yourself with Power Apps basics by generating an app and then customizing that app's gallery, forms, and cards.

-  To create an app, you must be assigned to the **Environment Maker** security role.

## Open a blank app 

1.  Sign in to [Power Apps](https://make.powerapps.com).

2.  Under **Make your own app**, select **Canvas app from blank**.

3.  Specify a name for your app, select **Phone**, and then select **Create**.

![](media/how-to-create-an-app-with-the-barcode-scanner/open-a-blank-app-1.png)

## Add barcode scanner

1.  In the left navigation bar, select **Screen1.**

2.  On the **Insert tab**, select the down-arrow next to **Media** to open a list of media types and media controls, and then select **Barcode scanner**.

![ Select barcode scanner](media/how-to-create-an-app-with-the-barcode-scanner/add-barcode-scanner-1.png "Select barcode scanner")

3.  On the **Advanced** tab of the right-hand pane, select **OnScan**.

![](media/how-to-create-an-app-with-the-barcode-scanner/add-barcode-scanner-2.png "")

4.  Set the **OnScan** property of the Barcode scanner control to this expression by typing or pasting it in the formula bar: 

```
Collect(
    colScannedItems,
    {ScannedItem: BarcodeScanner1.Value, ScannedTime: Now()}
)
```

![OnScan property of the Barcode scanner control](media/how-to-create-an-app-with-the-barcode-scanner/add-barcode-scanner-3.png "OnScan property of the Barcode scanner control")

5.  On the **Properties** tab of the right-hand pane, set **X** property to 180 and the **Y** property to 1005.

![](media/how-to-create-an-app-with-the-barcode-scanner/add-barcode-scanner-4.png "")

## Add gallery

1.  On the **Insert tab**, select the down-arrow next to **Gallery** to open a list of gallery types, and then select **Vertical**.

![Gallery types select Vertical](media/how-to-create-an-app-with-the-barcode-scanner/add-gallery-1.png "Gallery types select Vertical")

2.  On the **Properties** tab of the right-hand pane, select the down arrow for the **Layout** menu.

3.  Select **Title and subtitle**.

![Select Title and subtitle](media/how-to-create-an-app-with-the-barcode-scanner/add-gallery-2.png "Select Title and subtitle")

4.  On the **Properties** tab of the right-hand pane, select **Data source**.

![Properties tab of the right-hand pane select Data source](media/how-to-create-an-app-with-the-barcode-scanner/add-gallery-3.png "Properties tab of the right-hand pane select Data source")

5.  Set the **Items** property of the Gallery control to this expression by typing or pasting it in the formula bar:

```
colScannedItems
```

![Items property of the Gallery control to this expression](media/how-to-create-an-app-with-the-barcode-scanner/add-gallery-4.png "")

6.  In the left navigation bar, select **Title2**.

![Left navigation bar select Title2](media/how-to-create-an-app-with-the-barcode-scanner/add-gallery-5.png "Left navigation bar select Title2")

7.  On the **Properties** tab of the right-hand pane, select **Text**.

![Properties tab of the right-hand pane, select Text](media/how-to-create-an-app-with-the-barcode-scanner/add-gallery-6.png "Properties tab of the right-hand pane, select Text")

8.  Set the **Text** property of the Label control to this expression by typing or pasting it in the formula bar:

```
ThisItem.ScannedItem
```

![Text property of the Label control](media/how-to-create-an-app-with-the-barcode-scanner/add-gallery-7.png "Text property of the Label control")

9.  In the left navigation bar, select **Subtitle2**.

![Left navigation bar select Subtitle2](media/how-to-create-an-app-with-the-barcode-scanner/add-gallery-8.png "Left navigation bar select Subtitle2")

10. On the **Properties** tab of the right-hand pane, select **Text**.

![Properties tab of the right-hand pane select Text](media/how-to-create-an-app-with-the-barcode-scanner/add-gallery-9.png "Properties tab of the right-hand pane select Text]")

11. Set the **Text** property of the Label control to this expression by typing or pasting it in the formula bar:

```
ThisItem.ScannedTime
```

![Set the Text property of the Label control](media/how-to-create-an-app-with-the-barcode-scanner/add-gallery-10.png "Set the Text property of the Label control")

## Test the app

1.  In the left navigation bar, select **Screen1**, and then open Preview by pressing F5 (or by selecting the play icon near the upper-right corner).

2.  Exit Preview by pressing F5 (or by selecting the play icon near the upper-right corner).

3.  **Save** & **Publish** by pressing the keyboard shortcut: **Ctrl+Shift+P**.

4.  Select **Publish this version**.

![Save and Publish](media/how-to-create-an-app-with-the-barcode-scanner/test-the-app-1.png "Save and Publish")

5.  Download the **Power Apps** app on your mobile device.

6.  Open the **Power Apps** app, Log in, and launch your Barcode Scanner application.

![Launch your Barcode Scanner application](media/how-to-create-an-app-with-the-barcode-scanner/test-the-app-2.png "Launch your Barcode Scanner application")

7.  Select **Scan** and scan any barcode label (example: book barcode label).

## Final Results

![Final Results](media/how-to-create-an-app-with-the-barcode-scanner/final-results-1.png "Final Results")