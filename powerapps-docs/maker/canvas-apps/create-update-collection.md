---
title: Create and update a collection in a canvas app
description: Create a collection, add items to the collection, and remove one or all items from a collection in a canvas app.
author: mduelae

ms.topic: how-to
ms.custom: canvas
ms.reviewer: mkaur
ms.date: 02/6/2025
ms.subservice: canvas-maker
ms.author: tapanm
search.audienceType:
  - maker
contributors:
  - gregli-msft
  - mduelae
---

# Create and update a collection in a canvas app

Use a collection to store data that users can manage in your app. A collection is a group of items that are similar, such as products in a product list. For more information about different types of variables such as collections: [Understand canvas-app variables](working-with-variables.md).

## Prerequisites

- [Sign up](../signup-for-powerapps.md) for Power Apps, and then [sign in](https://make.powerapps.com?utm_source=padocs&utm_medium=linkinadoc&utm_campaign=referralsfromdoc) by providing the same credentials that you used to sign up.
- Create an app or open an existing app in Power Apps.
- Learn how to [configure a control](add-configure-controls.md) in Power Apps.

Watch this video to learn how to create and update a collection:
> [!VIDEO https://learn-video.azurefd.net/vod/player?id=b709db8a-7d9c-4869-b2f7-76027df3bee0]

## Create a multicolumn collection

1. In Power Apps Studio, add a **Text input** control.

1. Rename the control by selecting its ellipsis in the left navigation pane, selecting **Rename**, and then typing **ProductName**.

   :::image type="content" source="./media/create-update-collection/rename-textbox.png" alt-text="Screenshot that shows you how to rename a control.":::

1. Add a **Drop down** control.

   :::image type="content" source="./media/create-update-collection/add-dropdown.png" alt-text="Screenshot that shows how to add a dropdown list.":::

1. Rename the **Drop down** control **Colors**, and make sure that the **Items** property is selected in the property list.

   :::image type="content" source="./media/create-update-collection/items-property.png" alt-text="Screenshot that shows the Items property next to the formula bar.":::

1. In the formula bar, replace **DropDownSample** with this expression:

    `["Red","Green","Blue"]`

1. Add a **Button** control, set its **Text** property to **"Add"**, and set its **OnSelect** property to this formula:

    ```power-fx
    Collect(
        ProductList,
        {
            Product: "ProductName.Text",
            Color: "Colors.Selected.Value"
        }
    )
    ```

1. To preview the app, press `F5` or select the play button. Type some text into **ProductName**, select an option in **Colors**, and then select **Add**.

1. Repeat the previous step at least two more times, and then press `Esc`.

1. Select the **Variables** pane and then select **Collections** to see the collections that you created.

   :::image type="content" source="./media/create-update-collection/collections.png" alt-text="Screenshot that shows the Collections section of the Variables list.":::

## Show a collection

1. Select **Insert** > **Vertical gallery** control.

1. Set the gallery's **Items** property to **ProductList**.

1. Select the gallery in the tree view and then select **Fields**.

1. Set the subtitle field to **Color**, and set the title field to **Product**.

1. Select **Layout** > **Title and subtitle**.

   :::image type="content" source="./media/create-update-collection/change-layout.png" alt-text="Screenshot that shows the Layout tab with Title and subtitle tile selected.":::

## Remove one or all items

1. Select the gallery and add a **Trash** icon to the gallery template.

1. Set the icon's **OnSelect** property to this formula:

    `Remove(ProductList, ThisItem)`

1. Outside the gallery, add a button, set its **Text** property to **"Clear"**, and set its **OnSelect** property to this formula:

    `Clear(ProductList)`

1. While holding down the Alt key, select the **Trash** icon for an item to remove that item from the collection, or select the **Clear** button to remove all items from the collection.

## Put a list into a collection

1. [Create a connection to a list created using Microsoft Lists](connections/connection-sharepoint-online.md#create-a-sharepoint-connection).

1. Add a button, and set its **[OnSelect](controls/properties-core.md)** property to this function, replacing *ListName* with the name of your list:

    `Collect(MySPCollection, ListName)`

    This function creates a collection named **MySPCollection** and that contains the same data as your list.

1. While holding down the `Alt` key, select the button.

For information about how to show data in a form (with drop-down lists, date pickers, and people pickers): [Edit form and Display form controls](controls/control-form-detail.md).

## Next steps

- Review the [reference article](functions/function-clear-collect-clearcollect.md) for the **Collect** function.
- Learn how to shape data in a collection by using the [AddColumns, DropColumns, RenameColumns, and ShowColumns](functions/function-table-shaping.md) functions.

[!INCLUDE[footer-include](../../includes/footer-banner.md)]
