---
title: Show items of different heights in canvas apps gallery
description: Add and configure a flexible height gallery to automatically fit the amount of content in each item of the gallery.
author: fikaradz
ms.service: powerapps
ms.topic: conceptual
ms.custom: canvas
ms.reviewer: tapanm
ms.date: 04/01/2017
ms.subservice: canvas-maker
ms.author: fikaradz
search.audienceType: 
  - maker
search.app: 
  - PowerApps
contributors:
  - tapanm-msft
  - fikaradz
---
# Show items of different heights in canvas apps gallery
If different items in your data set contain different amounts of data in the same field, you can completely show items that contain more data without adding empty space after items that contain less data. Add and configure a **Flexible height** gallery control so that you can:

* Configure **Label** controls to expand or shrink based on their contents.
* Position each control so that it automatically appears just under the control above it.

In this tutorial, you show data about flooring products in a **Flexible height** gallery control. The image of each product appears 5 pixels below the overview, whether the overview contains five lines of text or two lines.

![Dynamic app.](./media/gallery-dynamic-sizing/dynamic-app.png)

**Suggested reading**

If you've never added controls to a gallery, follow the steps in [Show a list of items](add-gallery.md) before you proceed in this topic.

## Add data to a blank app
1. Download [this Excel file](https://az787822.vo.msecnd.net/documentation/get-started-from-data/FlooringEstimates.xlsx), which contains names, overviews, and links to images of flooring products.

    ![Flooring products.](./media/gallery-dynamic-sizing/flooring-products.png)

2. Upload the Excel file to a cloud-storage account such as OneDrive, Dropbox, or Google Drive.

3. In Power Apps Studio, click or tap **New** on the **File** menu.

4. On the **Blank app** tile, click or tap **Phone layout**.

    ![New option on the File menu.](./media/gallery-dynamic-sizing/blank-app.png)

5. Add a connection to the **FlooringEstimates** table in the Excel file.

    For more information, see [Add a connection](add-data-connection.md).

## Add data to a gallery
1. On the **Insert** tab, click or tap **Gallery**, and then click or tap **Flexible height**.

    ![Add gallery.](./media/gallery-dynamic-sizing/add-flexible.png)
2. Resize the gallery to take up the entire screen.

3. Set the gallery's **[Items](controls/properties-core.md)** property to **FlooringEstimates**.

## Show the product names
1. In the upper-left corner of the gallery, click or tap the pencil icon to select the gallery template.

    ![Pencil icon.](./media/gallery-dynamic-sizing/edit-template.png)

2. With the gallery template selected, add a **[Label](controls/control-text-box.md)** control to it.

3. Set the **Text** property of the **Label** control to this expression:<br>
   **ThisItem.Name**

    ![Add label.](./media/gallery-dynamic-sizing/add-text-box.png)

## Show the product overviews
1. With the gallery template selected, add another **Label** control, and move it below the first **Label** control.  

2. Set the **Text** property of the second **Label** control to this expression:<br> **ThisItem.Overview**

3. With the second **Label** control selected, click or tap the name-tag icon on the **Content** tab, and rename the control to **OverviewText**.

    ![Rename label.](./media/gallery-dynamic-sizing/rename-text-box.png)

4. Set the **AutoHeight** property of the **OverviewText** box to **true**.

    This step ensures that the box will grow or shrink to fit its contents.

      ![Text auto height.](./media/gallery-dynamic-sizing/autoheight-text.png)

## Show the product images
1. Resize the template so that it's twice as tall as it was.

    You can add controls to the template more easily as you build the app, and this change won't affect how the app looks when it runs.

2. With the gallery template selected, add an **[Image](controls/control-image.md)** control, and move it below the **OverviewText** box.

3. Ensure that the **Image** property of the **Image** control is set to this expression:<br>
    **ThisItem.Image**

4. Set the **[Y](controls/properties-core.md)** property of the **Image** control based on the position and the size of the **OverviewText** box, as in this expression:
   <br>**OverviewText.Y + OverviewText.Height + 5**

    ![Final app.](./media/gallery-dynamic-sizing/final-app.png)

Apply the same concept if you want to add more controls: set each control's **Y** property based on the **Y** and **Height** properties of the control above it.

## Next steps
Learn more about how to work with a [gallery](working-with-forms.md) control and [formulas](working-with-formulas.md).


[!INCLUDE[footer-include](../../includes/footer-banner.md)]