---
title: Show, sort, and filter data in a canvas app gallery
description: Learn about how to use a gallery to display images and text, and how to sort and filter the images in canvas apps.
author: adrianorth
ms.service: powerapps
ms.topic: conceptual
ms.custom: canvas
ms.reviewer: tapanm
ms.date: 06/02/2015
ms.subservice: canvas-maker
ms.author: aorth
search.audienceType: 
  - maker
search.app: 
  - PowerApps
contributors:
  - tapanm-msft
  - adrianorth
---
# Show, sort, and filter data in a canvas app gallery
Create a gallery to show images and text about several products, and sort and filter that information.

In Power Apps, you can use a gallery to show several related items, just as you see in a catalog. Galleries are great for showing information about products, such as names and prices. In this topic, we create a gallery and sort and filter the information using Excel-like functions. Also, when an item is selected, a border is placed around the item.

> [!NOTE]
> This topic uses a tablet app. You can use a phone app but you will need to resize some of the controls.

### Prerequisites
* [Sign up](../signup-for-powerapps.md) for Power Apps, and then [sign in](https://make.powerapps.com?utm_source=padocs&utm_medium=linkinadoc&utm_campaign=referralsfromdoc) using the same credentials that you used to sign up.
* Create a tablet app from a [template](get-started-test-drive.md), from [data](get-started-create-from-data.md), or from [scratch](get-started-create-from-blank.md).
* Learn how to [configure a control](add-configure-controls.md).
* These steps use the [CreateFirstApp](https://pwrappssamples.blob.core.windows.net/samples/CreateFirstApp.zip) as sample input data, which includes .jpg images. The zip file includes an XML file that can be converted to Excel. Otherwise, Power Apps automatically reads the files in the .zip files and imports it successfully. You can download and use this sample data, or import your own.

## Show data in a gallery
1. Create a collection named **Inventory** using the sample data. Steps include:  
   
   1. On the **Insert** tab, select **Controls**, and then select **Import**:
      
      ![Insert control][1]  
   2. Set the **[OnSelect](controls/properties-core.md)** property of the import control to the following formula:  
      **Collect(Inventory, Import1.Data)**
      
      ![OnSelect property][12]  
   3. Select the **Import Data** button to open Windows Explorer. Select *CreateFirstApp.zip*, and select **Open**.
   4. In the **File** menu, select **Collections**. The Inventory collection is listed with the data you imported:
      
      ![File - collections][3]  
      
      You've just created the Inventory collection, which contains information about five products, including a design image, the name of the product, and the number of units in stock.
      
      > [!NOTE]
      > The import control is used to import Excel-like data and create the collection. The import control imports data when you are creating your app, and previewing your app. Currently, the import control does not import data when you publish your app.
      > 
      > 
2. Select the back arrow to return to the designer.
3. On the **Insert** tab, click or tap **Gallery**, and then click or tap the **Horizontal** gallery.
   
    ![Gallery - horizontal][4]
4. In the right-hand pane, click or tap the option in which the title and the subtitle overlay the graphic:
   
    ![Layout][15]
5. Set the **[Items](controls/properties-core.md)** property of the gallery to **Inventory**:
   
    ![Gallery layout][5]
6. Rename the gallery to **ProductGallery**, and move the gallery so it doesn't block the other controls. Resize the gallery so it shows three products:
   
    ![Rename gallery][6]
7. In the first item of the gallery, select the bottom label:  
   
    ![App with gallery][7]  
   
   > [!NOTE]
   > When you change the first item in any gallery, you automatically change all other items in the gallery.  
   > 
   > 
8. Set the **[Text](controls/properties-core.md)** property of the label to the following expression:  
    **ThisItem.UnitsInStock** <br/>
   
    When you do this, the label shows the units in stock for each product:

![Stock of each product][8]  

> [!NOTE]
> By default, the **[Text](controls/properties-core.md)** property of the top label is set to ```ThisItem.ProductName```. You can change it to any other item in your collection. For example, if your collection has *ProductDescription* or *Price* fields, you can set the label to ```ThisItem.ProductDescription``` or ```ThisItem.Price```.
> 
> 

Using these steps, you imported data that includes .jpg images into a collection. You then added a gallery that displays the data and configured a label to show the units in stock for each product.

## Highlight the gallery item you select
1. Select any item in the gallery *except* the first one. The edit icon displays (upper left corner). Select the edit icon:  
   ![Edit][9]  
2. On the **Insert** tab, select **Shapes**, and then select the rectangle. A blue solid rectangle appears in each gallery item.
3. On the **Home** tab, select **Fill**, and then select **No Fill**.
4. Select **Border**, select **Border Style**, and then select the solid line.
5. Select **Border** again, and set the thickness to 3. Resize the rectangle so that it surrounds the gallery item. The items in your gallery now have a blue border and should look similar to the following:  
   ![Select border][10]  
6. On the **Shape** tab, select **Visible**, and then enter the following formula in the Formula Bar:  
   
    **If(ThisItem.IsSelected, true)**
   
    A blue rectangle surrounds the current selection in a gallery. Select a few gallery items to confirm that the rectangle appears around each item that you select. Remember, you can also open **Preview** ![Preview button][2] to see and test what you're creating.

> [!TIP]
> Select the rectangle, select **Reorder** on the **Home** tab, and then select **Send to Back**. Using this feature, you can select a gallery item without the border blocking anything.
> 
> 

Using these steps, you added a border around the current selection in the gallery.

## Sort and filter items in the gallery
In these steps, we are going to sort the gallery items in ascending and descending order. Also, we'll add a slider control to 'filter' gallery items by the units in stock that you choose.

#### Sort in ascending or descending order
1. Select any item in the gallery *except* the first one.
2. The **[Items](controls/properties-core.md)** property is currently set to Inventory (the name of your collection). Change it to the following:  
   
    **Sort(Inventory, ProductName)**
   
    When you do this, the items in the gallery are sorted by the product name in ascending order:
    ![Gallery sorted][11]  
   
    Try descending order. Set the **[Items](controls/properties-core.md)** property of the gallery to the following formula:  
   
    Sort(Inventory, ProductName, Descending)  

#### Add a slider control and filter items in the gallery
1. Add a Slider control (**Insert** tab > **Controls**), rename it to **StockFilter**, and move it under the gallery.
2. Configure the slider so that users can't set it to a value outside the range of units in stock:  
   
   1. On the **Content** tab, select **Min**, and then enter the following expression:  
      ```Min(Inventory, UnitsInStock)```  
   2. On the **Content** tab, select **Max**, and then enter the following expression:  
      ```Max(Inventory, UnitsInStock)```
3. Select any item in the gallery *except* the first one. Set the **[Items](controls/properties-core.md)** property of the gallery to the following expression:  
   ```Filter(Inventory, UnitsInStock<=StockFilter.Value)```
4. In **Preview**, adjust the slider to a value that's between the highest and the lowest quantity in the gallery. As you adjust the slider, the gallery shows only those products that are less than the value you choose:  
   ![Preview gallery with slider value][13]  

Now, let's add to our filter:

1. Go back to the designer.
2. On the **Insert** tab, select **Text**, select **Input Text**, and rename the new control to **NameFilter**. Move the text control below the slider.
3. Set the **[Items](controls/properties-core.md)** property of the gallery to the following expression:  
   ```Filter(Inventory, UnitsInStock<=StockFilter.Value && NameFilter.Text in ProductName)```
4. In **Preview**, set the slider to *30*, and type the letter *g* in the text-input control. The gallery shows the only product with less than 30 units in stock *and* has a name with the letter "g":  
   ![Preview slider with 30][14]  

## Tips and Tricks
* At anytime, you can select the preview button (![Preview button image][2]) to see what you created and test it.
* When designing your app, you can re-size the controls and move them around using click-and-drag.
* Press **ESC** or select the **X** to close the preview window.
* When using a gallery, select the first item in the gallery to change all items in the gallery. For example, select the first item to add a border to all items in the gallery.
* To update the properties of the gallery, select any item in the gallery *except* the first one. For example, select the second item to update the *Items*, *ShowScrollbar*, and other properties that apply to the gallery (not the items in the gallery).  

## What you learned
In this topic, you:

* Created a collection, imported data that includes .jpg images into that collection, and showed the data in a gallery.
* Under each image in the gallery, configured a label that lists the units in stock for that item.
* Added a border around the item that you select.
* Sorted the items by product name in ascending and descending order.
* Added a slider and an input text control to filter the products by units in stock and product name.

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