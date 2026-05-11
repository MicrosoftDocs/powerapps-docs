---
title: Show, sort, and filter data in a canvas app gallery
description: Learn how to use a gallery to display images and text, and how to sort and filter data in a canvas app gallery.
author: lancedmicrosoft

ms.topic: how-to
ms.custom: canvas
ms.reviewer: mkaur
ms.date: 05/11/2025
ms.subservice: canvas-maker
ms.author: lanced
search.audienceType: 
  - maker
contributors:
  - mduelae
  - lancedMicrosoft
---
# Show, sort, and filter data in a canvas app gallery

Create a gallery to show images and text about several products, and sort and filter that information.

In Power Apps, use a gallery to show several related items, much like a product catalog. Galleries are great for displaying product names, prices, and images. In this article, you create a gallery and sort and filter the information using Power Fx functions. When an item is selected, a border highlights it.

> [!NOTE]
> This article uses a tablet app layout. You can follow the same steps in a phone app, but you might need to resize some controls to fit the screen.

## Prerequisites

- [Sign up](../signup-for-powerapps.md) for Power Apps, and then [sign in](https://make.powerapps.com?utm_source=padocs&utm_medium=linkinadoc&utm_campaign=referralsfromdoc) using the same credentials that you used to sign up.
- Create a tablet app from a [template](get-started-test-drive.md) or [from scratch](get-started-create-from-blank.md).
- Learn how to [configure a control](add-configure-controls.md).
- Download the [CreateFirstApp](https://pwrappssamples.blob.core.windows.net/samples/CreateFirstApp.zip) sample data file, which includes product names, unit counts, and .jpg images.

## Show data in a gallery

1. Create a collection named **Inventory** by importing the sample data:

   1. On the **Insert** tab, select **Media** > **Import**.
   2. Set the **OnSelect** property of the Import control to the following formula:
      ```power-fx
      Collect(Inventory, Import1.Data)
      ```
   3. Select the **Import Data** button and open *CreateFirstApp.zip*.

   The **Inventory** collection now contains five products, each with a design image, a product name, and a unit count.

   > [!NOTE]
   > The Import control is intended for use during app authoring and preview only. It doesn't import data when you publish and run the app. For production scenarios, connect to a real data source such as [SharePoint](connections/connection-sharepoint-online.md) or [Microsoft Dataverse](connections/connection-common-data-service.md).

2. Select the back arrow to return to the app canvas.

3. On the **Insert** tab, select **Gallery** > **Horizontal**.

4. In the right-hand pane, select the layout that shows the title and subtitle overlaying the graphic.

5. Set the **Items** property of the gallery to **Inventory**.

6. Rename the gallery to **ProductGallery** and resize it to show three products at once.

7. Select the bottom label in the first gallery item.

   > [!NOTE]
   > When you change the first item in a gallery, the same change automatically applies to all other items.

8. Set the **Text** property of the label to:
   ```power-fx
   ThisItem.UnitsInStock
   ```
   The label now shows the number of units in stock for each product.

   > [!TIP]
   > You can bind any label to any field in your collection. For example, use `ThisItem.ProductName` or `ThisItem.Price` if those fields exist in your data source.

## Highlight the selected gallery item

1. Select any gallery item *except* the first one, then select the edit (pencil) icon in the upper-left corner to enter template editing mode.

2. On the **Insert** tab, select **Shapes** > **Rectangle**. A solid rectangle appears in each gallery item.

3. On the **Properties** pane, set **Fill** to **No fill**.

4. Set the **Border style** to **Solid** and the **Border thickness** to **3**.

5. Resize the rectangle to surround the gallery item contents.

6. Set the **Visible** property of the rectangle to:
   ```power-fx
   ThisItem.IsSelected
   ```
   The blue border now appears only around the selected item.

   > [!TIP]
   > If the border overlaps content, select the rectangle and choose **Reorder** > **Send to Back** to move it behind other controls.

## Sort and filter items in the gallery

### Sort in ascending or descending order

1. Select any gallery item *except* the first one to update the gallery's **Items** property.

2. Change the **Items** property to sort by product name in ascending order:
   ```power-fx
   Sort(Inventory, ProductName)
   ```

3. To sort in descending order, change the **Items** property to:
   ```power-fx
   Sort(Inventory, ProductName, SortOrder.Descending)
   ```

### Filter items with a slider and text input

1. On the **Insert** tab, select **Input** > **Slider**. Rename the slider to **StockFilter** and position it below the gallery.

2. Set the slider's range to match the data:
   - Set **Min** to: `Min(Inventory, UnitsInStock)`
   - Set **Max** to: `Max(Inventory, UnitsInStock)`

3. Select any gallery item *except* the first one and set the **Items** property to:
   ```power-fx
   Filter(Inventory, UnitsInStock <= StockFilter.Value)
   ```

4. Select **Preview** (F5) and adjust the slider to see the gallery filter products by stock quantity.

5. To also filter by product name, add a **Text input** control (on the **Insert** tab, select **Input** > **Text input**), rename it **NameFilter**, and place it below the slider.

6. Update the **Items** property to combine both filters:
   ```power-fx
   Filter(Inventory, UnitsInStock <= StockFilter.Value && NameFilter.Text in ProductName)
   ```

7. In **Preview**, set the slider to **30** and type **g** in the text input. The gallery shows only products with fewer than 30 units in stock *and* a product name containing the letter "g".

## Tips and tricks

- Select the preview button (F5) at any time to test what you've built.
- You can resize and reposition controls using drag-and-drop.
- Press **Esc** or select **X** to close the preview window.
- To change all items in a gallery at once, select the *first* item in the gallery.
- To update gallery-level properties (such as **Items** or **ShowScrollbar**), select any item *except* the first one.

## Summary

In this article, you:

- Created a collection and imported sample data with images.
- Displayed collection data in a horizontal gallery.
- Configured labels to show field values from each record.
- Added a selection border around the active gallery item.
- Sorted gallery items by product name in ascending and descending order.
- Used a slider and text input to filter products by stock quantity and name.

[1]: ./media/show-images-text-gallery-sort-filter/import.png
[2]: ./media/show-images-text-gallery-sort-filter/preview.png
[3]: ./media/show-images-text-gallery-sort-filter/inventorycollection.png
[4]: ./media/show-images-text-gallery-sort-filter/insert-vertical.png
[5]: ./media/show-images-text-gallery-sort-filter/itemsinventory.png
[6]: ./media/show-images-text-gallery-sort-filter/threeimages.png
[7]: ./media/show-images-text-gallery-sort-filter/firstitem.png
[8]: ./media/show-images-text-gallery-sort-filter/bottomlabel.png
[9]: ./media/show-images-text-gallery-sort-filter/editgallery.png
[10]: ./media/show-images-text-gallery-sort-filter/border.png
[11]: ./media/show-images-text-gallery-sort-filter/sort.png
[12]: ./media/show-images-text-gallery-sort-filter/onselect.png
[13]: ./media/show-images-text-gallery-sort-filter/slider.png
[14]: ./media/show-images-text-gallery-sort-filter/inputandslider.png
[15]: ./media/show-images-text-gallery-sort-filter/select-overlay.png


[!INCLUDE[footer-include](../../includes/footer-banner.md)]