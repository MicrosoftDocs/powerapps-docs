<properties
	pageTitle="Show images and text in a gallery; Sort and filter the gallery in PowerApps | Microsoft Azure"
	description=""
	services="power-apps"
	documentationCenter="" 
	authors="MandiOhlinger"
	manager="dwrede"
	editor=""/>

<tags
   ms.service="power-apps"
   ms.devlang="na"
   ms.topic="article"
   ms.tgt_pltfrm="na"
   ms.workload="" 
   ms.date="09/21/2015"
   ms.author="mandia"/>


# Show images and text in a gallery, including gallery selection, sort, and filter
Create a gallery to show several images, and to sort and filter these images. 

In PowerApps, use a gallery to show several items of something, almost like a catalog. Galleries are great for showing product information, their descriptions, and their prices. In this topic, we create a gallery, and sort and filter the images using Excel-like functions. Also, when an image is selected, a border is placed around the image. 


### Prerequisites 
- Install PowerApps. Create a new app or open an existing app in PowerApps.
- To familiarize yourself with PowerApps and creating apps, step through the [Test Drive](get-started-test-drive.md ). It walks you through performing some key tasks.
- These steps use the [CreateFirstApp](https://gallery.technet.microsoft.com/Sample-data-for-Create-c77790e7) as sample input data, which includes .jpg images. You can use this sample data, or import your own.

## Add a gallery to show images and text

1. Download the [CreateFirstApp](https://gallery.technet.microsoft.com/Sample-data-for-Create-c77790e7) zip file.
2. Create a collection named **Inventory**. Steps include:  
	a) Open your app in PowerApps.  
	b) On the **Insert** tab, select **Controls**, and then select **Import**:  
	![][1]  
	c) Set the **OnSelect** property to the following function:  
	```Collect(Inventory, Import1!Data)```  
		![][12]  
	d) Preview ![][2] your output.  Select the **Import Data** button to open Windows Explorer. Select *CreateFirstApp.zip*, and select **Open**.  
	e) ESC or close the preview window.  
	f) In the **File** menu, select **Collections**. The Inventory collection is listed with the data you imported:  
	![][3]  

	You've just created the Inventory collection, which contains information about five products, including a design image, a product name, and the number of units in stock.

3. Go back to your screen. On the **Insert** tab, select **Gallery**, and then select the **With Text** image gallery:  
![][4]  
4. In the formula bar, set the **Items** property to **Inventory**:  
![][5]  
5. Rename the gallery to **ProductGallery**, and move the gallery so it doesn't block the other controls. Widen it to show three products:  
![][6]  
6. In the first item of the gallery, select the bottom label:  
![][7]  
	> [AZURE.TIP] When you select the the first item in any gallery, you automatically change all other items in the gallery.  

7. Set the **Text** property of the label to the following expression:  
```ThisItem!UnitsInStock``` <br/>

	When you do this, the label shows the units in stock for each product:  
![][8]  

Using these steps, you imported data that includes .jpeg picture images into a collection. You then added a gallery that displays the images and added a label that shows the units in stock for every product. 

## Highlight the gallery item you select

1. In your screen, select any item in the gallery *except* the first one. Select the edit icon in the gallery (upper left corner):  
![][9]  
2. On the Insert tab, select **Shapes**, and then select the rectangle. A blue solid rectangle appears in each gallery item. 
3. On the Home tab, select **Fill**, and then select **No Fill**. 
4. Select **Border**, select **Border Style**, and then select the solid line.
5. Select **Border** again and set the thickness to 3. Resize the rectangle so that it surrounds each gallery item. Your gallery looks similar to the following:  
![][10]  
6. On the Shape tab, select **Visible**, and then enter the following expression in the function bar:  
```If(ThisItem!IsSelected, true)```

	A blue rectangle surrounds the current selection in a gallery. Click a few gallery items to confirm that the rectangle appears around the item that you selected. Remember, you can also preview ![][2] to see and test what you're creating. 

> [AZURE.TIP] Click the rectangle, click **Reorder** on the Home tab, and then click **Send to Back**. Using this step, you can click a gallery label to select it without the rectangle getting in the way.

Using these steps, you added a border around the current selection in the gallery. 


## Sort and filter items in the gallery

#### Sort in ascending or descending order

1. In your screen, select any item in the gallery *except* the first one. 
2. The **Items** property is currently set to Inventory (the name of your collection). Change it to the following:  
```Sort(Inventory, ProductName)```

	When you do this, the items in the gallery are sorted by the product name in ascending order: 
	![][11]  

	Try descending order. Set the **Items** property of the gallery to the following function:  
```Sort(Inventory, ProductName, Descending)```  

#### Add a slider control and filter items in the gallery


1. Add a slider control, name it **StockFilter**, and move it near the gallery.
2. Configure the slider so that users can't set it to a value outside the range of units in stock:  
	a) On the **Data** tab, click **Min**, and then enter the following function:  
	```Min(Inventory, UnitsinStock)```  
	b) On the **Data** tab, click **Max**, and then enter the following function:  
	```Max(Inventory, UnitsinStock)```
3. Set the **Items** property of the gallery to the following expression:  
```Filter(Inventory, UnitsinStock<=StockFilter!Value)```
4. In preview, adjust the slider to a value that's between the highest and the lowest price in the gallery. As you adjust the slider, the gallery shows only those products that are less than the value you choose:  
![][13]  
5. On the **Insert** tab, select **Text**, select **Input Text**, and rename the new control to **MakerFilter**. 
6. Set the **Items** property of the gallery to the following function:  
```Filter(Inventory, UnitsinStock<=StockFilter!Value && MakerFilter!Text in ProductName)```
7. In preview, set the slider to *30*, and type the letter *g* in the input text box. The gallery shows the only product with inventory less than 30 *and* that was made by Ganymede:  
![][14]  


## What you learned
In this topic, you:

- Created a collection and imported data into a gallery that includes .jpg images.
- In the gallery, added a label under each image that lists the units in stock for that item.
- Added a border around the image that you select. 
- Sorted the items by product name in ascending and descending order.
- Added a slider and input text controls to filter the products by units in stock and product name.


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
