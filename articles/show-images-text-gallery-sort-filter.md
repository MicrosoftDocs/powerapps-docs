<properties
	pageTitle="Show images and text in a gallery; Sort and filter the gallery in KratosApps | Microsoft Azure"
	description=""
	services=""
	documentationCenter=""
	authors="MandiOhlinger"
	manager="dwrede"
	editor=""/>

<tags
   ms.service="na"
   ms.devlang="na"
   ms.topic="article"
   ms.tgt_pltfrm="na"
   ms.workload="na"
   ms.date="10/13/2015"
   ms.author="mandia"/>


# Show images and text in a gallery, including gallery selection, sort, and filter
Create a gallery to show images and text about several products, and sort and filter that information.

In KratosApps, use a gallery to show several related items, as in a catalog. Galleries are great for showing information about products, such as names and prices. In this topic, we create a gallery and sort and filter the information using Excel-like functions. Also, when an item is selected, a border is placed around the item.


### Prerequisites
- Install KratosApps. Create an app or open an existing app in KratosApps.
- To familiarize yourself with configuring controls in KratosApps, step through the [configure a control](get-started-test-drive.md#configure-a-control).
- Download this [sample data](https://gallery.technet.microsoft.com/Sample-data-for-Create-c77790e7), or import your own data. The download includes .jpg images in a zip file.

## Add a gallery to show images and text

1. Create a collection named **Inventory** based on the sample data. Steps include:  
	a) Open an app in KratosApps. On the **Insert** tab, select **Controls**, and then select **Import**:  
	![][1]  
	b) Set the **OnSelect** property of the import control to the following expression:  
	```Collect(Inventory, Import1!Data)```  
		![][12]  
	c) Select the **Import Data** button to open Windows Explorer. Select *CreateFirstApp.zip*, and select **Open**.  
	d) In the **File** menu, select **Collections**. The Inventory collection is listed with the data you imported:  
	![][3]  

	You've just created the Inventory collection, which contains information about five products, including a design image, the name of the product, and the number of units in stock. 

2. Select the back arrow or press the Esc key to return to the designer.
3. On the **Insert** tab, select **Gallery**, and then select the horizontal **With Text** image gallery:  
![][4]  
3. Set the **Items** property of the gallery to **Inventory**:  
![][5]  
4. Rename the gallery to **ProductGallery**, and move the gallery so it doesn't block the other controls. Widen it to show three products:  
![][6]  
5. In the first item of the gallery, select the bottom label:  
![][7]  
	> [AZURE.NOTE] When you change the first item in any gallery, you automatically change all other items in the gallery.  
 
6. Set the **Text** property of the label to the following expression:  
```ThisItem!UnitsInStock``` <br/>

	When you do this, the label shows the units in stock for each product:  
![][8]  

> [AZURE.NOTE] By default, the **Text** property of the top label is set to ```ThisItem!ProductName```. You can change it to any other item in your collection. For example, if your collection has *ProductDescription* or *Quantity* fields, you can set the label to ```ThisItem!ProductDescription``` or ```ThisItem!Quantity```.

Using these steps, you imported data that includes .jpg images into a collection. You then added a gallery that displays the data and configured a label to show the units in stock for each product.

## Highlight the gallery item you select

1. Select any item in the gallery *except* the first one. The edit icon displays (upper left corner). Select the edit icon:  
![][9]  
2. On the **Insert** tab, select **Shapes**, and then select the rectangle. A blue solid rectangle appears in each gallery item.
3. On the **Home** tab, select **Fill**, and then select **No Fill**.
4. Select **Border**, select **Border Style**, and then select the solid line.
5. Select **Border** again, and set the thickness to 3. Resize the rectangle so that it surrounds each gallery item. The items in your gallery now have a blue border and should looks similar to the following:  
![][10]  
6. On the **Shape** tab, select **Visible**, and then enter the following expression in the Function Bar:  
```If(ThisItem!IsSelected, true)```

	A blue rectangle surrounds the current selection in a gallery. Click a few gallery items to confirm that the rectangle appears around each item that you select. Remember, you can also open **Preview** ![][2] to see and test what you're creating.

> [AZURE.TIP] Click the rectangle, click **Reorder** on the **Home** tab, and then click **Send to Back**. Using this step, you can click a gallery label to select it without the rectangle getting in the way.

Using these steps, you added a border around the current selection in the gallery.


## Sort and filter items in the gallery

#### Sort in ascending or descending order

1. Select any item in the gallery *except* the first one.
2. The **Items** property is currently set to Inventory (the name of your collection). Change it to the following:  
```Sort(Inventory, ProductName)```

	When you do this, the items in the gallery are sorted by the product name in ascending order:
	![][11]  

	Try descending order. Set the **Items** property of the gallery to the following expression:  
```Sort(Inventory, ProductName, Descending)```  

#### Add a slider control and filter items in the gallery


1. Add a slider control, name it **StockFilter**, and move it near the gallery.
2. Configure the slider so that users can't set it to a value outside the range of units in stock:  
	a) On the **Data** tab, click **Min**, and then enter the following expression:  
	```Min(Inventory, UnitsinStock)```  
	b) On the **Data** tab, click **Max**, and then enter the following expression:  
	```Max(Inventory, UnitsinStock)```
3. Set the **Items** property of the gallery to the following expression:  
```Filter(Inventory, UnitsinStock<=StockFilter!Value)```
4. In **Preview**, adjust the slider to a value that's between the highest and the lowest price in the gallery. As you adjust the slider, the gallery shows only those products that cost less than the value you choose:  
![][13]  
5. On the **Insert** tab, select **Text**, select **Input Text**, and rename the new control to **NameFilter**.
6. Set the **Items** property of the gallery to the following expression:  
```Filter(Inventory, UnitsinStock<=StockFilter!Value && NameFilter!Text in ProductName)```
7. In **Preview**, set the slider to *30*, and type the letter *g* in the input text box. The gallery shows the only product with fewer than 30 units in stock *and* has a name with the letter "g":  
![][14]  


## What you learned
In this topic, you:

- Created a collection, imported data that includes .jpg images into that collection, and showed the data in a gallery.
- Under each image in the gallery, configured a label that lists the units in stock for that item.
- Added a border around the item that you select.
- Sorted the items by product name in ascending and descending order.
- Added a slider and an input text control to filter the products by units in stock and product name.


[1]: ./media/show-images-text-gallery-sort-filter/import.png
[2]: ./media/show-images-text-gallery-sort-filter/preview.png
[3]: ./media/show-images-text-gallery-sort-filter/inventorycollection.png
[4]: ./media/show-images-text-gallery-sort-filter/withtext.png
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
