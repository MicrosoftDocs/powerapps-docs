---
title: Show, sort, and filter data in a canvas app gallery
description: Learn how to use a gallery to display data, and how to sort and filter data in a canvas app gallery.
author: yogeshgupta698

ms.topic: how-to
ms.custom: canvas
ms.reviewer: mkaur
ms.date: 05/12/2025
ms.subservice: canvas-maker
ms.author: yogupt
search.audienceType: 
  - maker
contributors:
  - mduelae
---
# Show, sort, and filter data in a canvas app gallery

Create a gallery to show data about several products, and sort and filter that information.

In Power Apps, use a gallery to show several related items, much like a product catalog. Galleries are great for displaying product names, prices, and unit counts. In this article, you create a gallery and sort and filter the information using Power Fx functions. When an item is selected, a border highlights it.

> [!NOTE]
> This article uses a tablet app layout. You can follow the same steps in a phone app, but you might need to resize some controls to fit the screen.

## Prerequisites

- [Sign up](../signup-for-powerapps.md) for Power Apps, and then [sign in](https://make.powerapps.com?utm_source=padocs&utm_medium=linkinadoc&utm_campaign=referralsfromdoc) using the same credentials that you used to sign up.
- Create a tablet app from a [template](get-started-test-drive.md) or [from scratch](get-started-create-from-blank.md).
- Learn how to [configure a control](add-configure-controls.md).

## Show data in a gallery

1. Create a collection named **Inventory** by adding a **Button** control and setting its **OnSelect** property to the following formula:

   ```powerapps-dot
   ClearCollect(
       Inventory,
       { ProductName: "Europa",    UnitsInStock: 25 },
       { ProductName: "Ganymede",  UnitsInStock: 32 },
       { ProductName: "Callisto",  UnitsInStock: 12 },
       { ProductName: "Io",        UnitsInStock: 47 },
       { ProductName: "Titan",     UnitsInStock: 18 }
   )
   ```

1. Select the button while holding the **Alt** key (or select **Preview** and then the button) to populate the **Inventory** collection with five products, each with a product name and a unit count.

   > [!NOTE]
   > This article uses a small inline collection so you can follow along without external data. For production scenarios, connect to a real data source such as [SharePoint](connections/connection-sharepoint-online.md) or [Microsoft Dataverse](connections/connection-common-data-service.md).

1. On the **Insert** tab, select **Layout** > **Horizontal gallery**.

1. In the right-hand pane, select a layout that shows a title and subtitle.

1. Set the **Items** property of the gallery to **Inventory**.

1. Rename the gallery to **ProductGallery** and resize it to show three products at once.

1. Select the bottom label in the first gallery item.

   > [!NOTE]
   > When you change the first item in a gallery, the same change automatically applies to all other items.

1. Set the **Text** property of the label to:

   ```powerapps-dot
   ThisItem.UnitsInStock
   ```
   
The label now shows the number of units in stock for each product.

   > [!TIP]
   > You can bind any label to any field in your collection. For example, use `ThisItem.ProductName` or `ThisItem.Price` if those fields exist in your data source.

## Highlight the selected gallery item

1. Select any gallery item *except* the first one, then select the edit (pencil) icon in the upper-left corner to enter template editing mode.

1. On the **Insert** tab, select **Shapes** > **Rectangle**. A solid rectangle appears in each gallery item.

1. On the **Properties** pane, set **Color** to **No fill** (transparent).

1. Under **Border**, set the style dropdown to **Solid** and the thickness value to **3**.

1. Resize the rectangle to surround the gallery item contents.

1. Set the **Visible** property of the rectangle to:

   ```powerapps-dot
   ThisItem.IsSelected
   ```
   
The blue border now appears only around the selected item.

   > [!TIP]
   > If the border overlaps content, select the rectangle and choose **Reorder** > **Send to Back** to move it behind other controls.

## Sort and filter items in the gallery

### Sort in ascending or descending order

1. Select any gallery item *except* the first one to update the gallery's **Items** property.

1. Change the **Items** property to sort by product name in ascending order:

   ```powerapps-dot
   Sort(Inventory, ProductName)
   ```

1. To sort in descending order, change the **Items** property to:

   ```powerapps-dot
   Sort(Inventory, ProductName, SortOrder.Descending)
   ```

### Filter items with a slider and text input

1. On the **Insert** tab, select **Input** > **Slider**. Rename the slider to **StockFilter** and position it below the gallery.

1. Set the slider's range to match the data:
   - Set **Min** to: `Min(Inventory, UnitsInStock)`
   - Set **Max** to: `Max(Inventory, UnitsInStock)`

1. Select any gallery item *except* the first one and set the **Items** property to:

   ```powerapps-dot
   Filter(Inventory, UnitsInStock <= StockFilter.Value)
   ```

1. Select **Preview** (F5) and adjust the slider to see the gallery filter products by stock quantity.

1. To also filter by product name, add a **Text input** control (on the **Insert** tab, select **Input** > **Text input**), rename it **NameFilter**, and place it below the slider.

1. Update the **Items** property to combine both filters:

   ```powerapps-dot
   Filter(Inventory, UnitsInStock <= StockFilter.Value && NameFilter.Text in ProductName)
   ```

1. In **Preview**, set the slider to **30** and type **g** in the text input. The gallery shows only products with 30 or fewer units in stock *and* a product name containing the letter "g".

## Tips and tricks

- Select the preview button (F5) at any time to test what you've built.
- You can resize and reposition controls using drag-and-drop.
- Press **Esc** or select **X** to close the preview window.
- To change all items in a gallery at once, select the *first* item in the gallery.
- To update gallery-level properties (such as **Items** or **ShowScrollbar**), select any item *except* the first one.

## Summary

In this article, you:

- Created a collection with sample product data.
- Displayed collection data in a horizontal gallery.
- Configured labels to show field values from each record.
- Added a selection border around the active gallery item.
- Sorted gallery items by product name in ascending and descending order.
- Used a slider and text input to filter products by stock quantity and name.

[!INCLUDE[footer-include](../../includes/footer-banner.md)]