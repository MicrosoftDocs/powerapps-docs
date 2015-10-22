<properties
	pageTitle="Create and update a collection in PowerApps Studio | Microsoft Azure"
	description="Create collections and add columns to existing collections in PowerApps Studio"
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
   ms.date="10/22/2015"
   ms.author="mandia"/>


# Create and update a collection in your app
Use a collection to store data that can be used in your app. A collection is a group of items that are similar. For example, you create a MyImages collection that stores all the product images your company sells. Within PowerApps, you can add your MyImages collection and create an app that displays all the pictures of these products. In another example, you can create a PriceList collection that lists the products and the price of each product.

You can create and use collections within PowerApps. Let's get started.

### Prerequisites
- Install [PowerApps Studio](http://aka.ms/powerappsinstall). Create a new app or open an existing app in PowerApps Studio. 
- To familiarize yourself with configuring controls in PowerApps, step through the [configure a control](get-started-test-drive.md#configure-a-control).


## Create a collection that has one column
The following steps show you how to create a collection within your app using the Collect function, and how to add items to your collection.

1. Open your app in PowerApps Studio.
2. On the **Insert** tab, select **Text**, and then select **Input Text**:  
![][1]  
3. In the top left corner, select **Text1**, and rename the control to **Destination**:  
![][2]  
4. On the **Insert** tab, select **Button** to add a button control to your designer. From the drop-down list, the **OnSelect** property is listed. Set it to the following function:  
```Collect(Destinations, Destination!Text)```  
It should look like the following:  
![][3]  

5. Click the button text, and enter **Add**:  
![][5]  
6. Select the Add button, and move it under your text control. You can move it anywhere:  
![][6]  


In these steps, you used the Collect function to create a collection named **Destinations**. You also added a button control and when clicked, adds new items to your collection. Now, see what you created:

1. Select Preview:  
![][7]    
2. Type a city name into the box, and then select the **Add** button.
3. Enter some additional city names and select the **Add** button each time.
4. Press the **Esc** key to close the Preview window.
5. To see the Destinations collection and the text values you entered, select the **File** tab, and then select **Collections**. The text you entered is listed under **Preview**:  
![][8]


#### Extra Credit 
Now, let's bind the Destinations collection to a listbox:

1. On the **Insert** tab, select **Controls**, and then select **ListBox**:  
![][22]  
2. Move the listbox so you can easily see it. Set its **Items** property to the following expression:  
```Destinations!Value```  <br/>

	When you do this, the listbox is automatically populated with the items you previously entered in the Destinations collection:  
![][4]  

Preview your changes: ![][7]. In the listbox, you can select the different cities. In the Input Text box, enter a new city and select the **Add** button. The listbox is automatically updated to include the new city you entered. 



## Create a collection that has more than one column
The following steps show you how to create a collection within your app using the Collect function, and how to add multiple rows to your collection.

1. Open your app in PowerApps Studio.
2. On the **Insert** tab, select **Text**, and then select **Input Text**.
3. In the top left corner, select **Text1**, and rename the control to **City**:  
![][9]  
4. Add another input text control, and rename it **State**.
5. Move the City and State text controls so they are side-by-side:  
![][10]  
	**Note**: You can replace 'Input Text' with something like 'Enter the City' or 'Enter the State', which was done in the screen shot.
6. On the **Insert** tab, select **Button**. Set its **OnSelect** property to the following function:  
```Collect(Destinations, {Cities:City!Text, States:State!Text})```  
It should look like the following:
![][11]  
	**Note**: You can use this same function to add additional columns to this collection. For example, you can add another input text for Country to add a Countries column: `Collect(Destinations, {Cities:City!Text, States:State!Text}, {Countries:Country!Text})`

7. Rename the button control **AddCityStateButton**, and set its **Text** property to **Add City and State**:  
![][12]  


In these steps, you added a **Cities** column and a **States** column to the **Destinations** collection. The button control adds these new text items to your collection. Now, see what you created:

1. Select Preview:  
![][7]  
2. Type some text into the City and State boxes, and then select the **Add City and State** button.
3. Add a few more cities and states.
4. Press the **Esc** key to close the Preview window.
5. To see the items you added to the Destinations collection, select the **File** tab, and then select **Collections**:  
![][13]


## Add more columns to an existing collection
There are a few sections in this walk-through. When complete, you'll know how to import data into your app, create a gallery that shows data in a price list, and use a slider control that determines the quantity of a product.

### Import the price list
1. Download the [PriceList](https://gallery.technet.microsoft.com/Sample-data-for-Show-a-set-5933d4c7) zip file.
2. Within your app, select the **Insert** tab, select **Controls**, and then select **Import**:  
![][14]  
3. On the **Behavior** tab, select **OnSelect**. Enter the following function:  
```Collect(PriceList, Import1!Data)```  
4. Preview your app, select **Import Data** button, select the PriceList.zip file, and select **Open**.
5. Close the Preview window.
6. Select the **File** tab, and select **Collections**. The items you imported are listed:  
![][15]


### Add the gallery
1. On the **Insert** tab, select **Gallery**, scroll down to **Custom Galleries**, and then select **Portrait**:    
![][16]  
2. Rename the gallery to **PriceGallery** and set the Items property to **PriceList**:  
![][18]  
3. Move the PriceList gallery to the right side of the **Import Data** control.
4. Select the gallery, click the first square in the gallery, and add three labels (**Insert** tab > **Label**). Set the **Text** property of each label to one of the following expressions:  
	``ThisItem!Name``  
``Text(ThisItem!Price, "$#")``  
``ThisItem!Maker``   
5. Resize and arrange the labels in a row near the top of the gallery. You an also adjust the size of the gallery template by selecting it, and then moving the borders. When complete, your gallery looks similar to the following:  
![][19]


### Add the controls and update the collection
1. On the **Insert** menu, select **Controls**, and select **Slider**. Name the slider **OrderQty**, and move it under the gallery.
2. Add a button, set its **Text** property to **Add**, and move it under the **OrderQty** slider. Your app looks similar to the following:  
![A gallery (with two columns), a slider, and an Add button][20]
3. Set the **OnSelect** property of the **Add** button to the following expression:  
```Collect(OrderList, {Name:PriceGallery!Selected!Name, Qty:OrderQty!Value, Cost:OrderQty!Value*LookUp(PriceList, PriceGallery!Selected!Name in Name, Price)});SaveData(OrderList, "orderfile")```  
**Note** When you click this button later in this procedure, you'll create and save a collection named **OrderList**. The collection will contain the name of a product that you enter in the gallery, a quantity that you choose with the slider, and the total cost calculated by multiplying the quantity by the price of the product.
4. Select the **Screen** tab and set the **OnVisible** property to the following expression:  
```If(IsEmpty(PriceList), LoadData(PriceList, "pricefile"));If(IsEmpty(OrderList), LoadData(OrderList, "orderfile"))```

Now, see what you created:

1. Open **Preview**.
2. Select a product in the gallery, move the slider to your desired quantity, and then select the **Add** button.  
> [AZURE.IMPORTANT] When you select a product, that product is not highlighted to indicate you selected it. When we created the gallery, we didn't add this functionality. Know that clicking the product does select it.
3. Repeat these steps to add a couple more products. Press **Esc** to close the Preview window.
4. On the **File** tab, select **Collections** to display a preview of the **OrderList** collection you created:  
![Preview the OrderList collection][21]


> [AZURE.TIP] To remove all items from the order list, add a button, set its **Text** property to **Clear**, and set its **OnSelect** property to the following expression:  
```Clear(OrderList);SaveData(OrderList, "orderfile")```  
To remove one item at a time, show the **OrderList** collection in a gallery, and then set the **OnSelect** property of a label in that gallery to the following expression:  
```Remove(OrderList, ThisItem);SaveData(OrderList, "orderfile")```



[1]: ./media/create-update-collection/insertmenu-inputtext.png
[2]: ./media/create-update-collection/renametext.png
[3]: ./media/create-update-collection/buttononselect.png
[4]: ./media/create-update-collection/listboxpreview.png
[5]: ./media/create-update-collection/buttontext.png
[6]: ./media/create-update-collection/buttonundertext.png
[7]: ./media/create-update-collection/preview.png
[8]: ./media/create-update-collection/existingcollections.png
[9]: ./media/create-update-collection/renametext-city.png
[10]: ./media/create-update-collection/citystate.png
[11]: ./media/create-update-collection/buttononselectcitystate.png
[12]: ./media/create-update-collection/buttononcitystate.png
[13]: ./media/create-update-collection/existingcollectionscitystate.png
[14]: ./media/create-update-collection/import.png
[15]: ./media/create-update-collection/pricelistcollection.png
[16]: ./media/create-update-collection/portrait.png
[18]: ./media/create-update-collection/galleryitems.png
[19]: ./media/create-update-collection/gallerylabels.png
[20]: ./media/create-update-collection/slider.png
[21]: ./media/create-update-collection/existingcollectionsorderlist.png
[22]: ./media/create-update-collection/listbox.png