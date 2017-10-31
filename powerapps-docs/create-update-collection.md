---
title: Create and update a collection | Microsoft Docs
description: Create collections and add columns to existing collections in PowerApps
services: ''
suite: powerapps
documentationcenter: ''
author: lonu
manager: anneta
editor: ''

ms.service: powerapps
ms.devlang: na
ms.topic: article
ms.tgt_pltfrm: na
ms.workload: na
ms.date: 11/30/2015
ms.author: lonu

---
# Create and update a collection in your app
Use a collection to store data that can be used in your app. A collection is a group of items that are similar. For example, you create a MyImages collection that stores all the product images your company sells. Within PowerApps, you can add your MyImages collection and create an app that displays all the pictures of these products. In another example, you can create a PriceList collection that lists the products and the price of each product.

You can create and use collections within PowerApps. Let's get started.

### Prerequisites
* [Sign up](signup-for-powerapps.md) for PowerApps, [install](http://aka.ms/powerappsinstall) it, open it, and then sign in by providing the same credentials that you used to sign up.
* Create an app or open an existing app in PowerApps.
* Learn how to [configure a control](add-configure-controls.md) in PowerApps.
* These steps use the [PriceList.zip](http://pwrappssamples.blob.core.windows.net/samples/PriceList.zip) file as sample input data. The zip file includes an XML file that can be converted to Excel. Otherwise, PowerApps automatically reads the files in the .zip files and imports it successfully. You can download and use this sample data, or import your own.

## Create a single-column collection
The following steps show you how to create a collection within your app using the Collect function, and how to add items to your collection.

1. Open your app.
2. On the **Insert** tab, select **Text**, and then select **Text input**:  
   ![][1]  
3. In the top left corner, select **Text1**, and rename the control to **Destination**:  
   ![][2]  
4. On the **Insert** tab, select **Button** to add a button control to your designer. From the drop-down list, the **[OnSelect](controls/properties-core.md)** property is listed. Set it to the following function:  
   
    ```Collect(Destinations, Destination!Text)```
   
    It should look like the following:  
    ![][3]  
5. Select the button text, and enter **Add**:  
   ![][5]  
6. Select the **Add** button, and move it under your text control. You can move it anywhere:  
   ![][6]  

In these steps, you used the Collect function to create a collection named **Destinations**. You also added a button control and when selected, adds new items to your collection. Now, see what you created:

1. Select Preview:  
   ![][7]  
2. Type a city name into the box, and then select the **Add** button.
3. Enter some additional city names and select the **Add** button each time.
4. Press the **Esc** key to close the Preview window.
5. See the Destinations collection and the text values you entered. On the **File** tab, select **Collections**. The text you entered is listed:  
   ![][8]

#### Extra credit
Now, let's bind the Destinations collection to a listbox:

1. Go back to your designer.
2. On the **Insert** tab, select **Controls**, and then select **ListBox**:  
   ![][22]  
3. Move the listbox so you can easily see it. Set its **[Items](controls/properties-core.md)** property to the following expression:  
   ```Destinations!Value```  <br/>
   
    When you do this, the listbox is automatically populated with the items you previously entered in the Destinations collection:  
   ![][4]  

Preview your changes: ![][7]. In the listbox, you can see the different cities you entered. In the text-input control, enter a new city, and select the **Add** button. The listbox is automatically updated to include the new city you entered.

## Create a multi-column collection
The following steps show you how to create a collection within your app using the Collect function, and how to add multiple rows to your collection.

1. On the **Home** tab, open a new screen.
2. On the **Insert** tab, select **Text**, and then select **Text input**.
3. Rename the text control to **City**:  
   ![][9]  
4. Insert another text-input control, and rename it to **States**.
5. Move the City and States text controls so you can see them both:  
   ![][10]  
   
    > [!NOTE]
> You can replace 'Text Input' with something like 'City' or 'State', which was done in the image.  
6. On the **Insert** tab, select **Button**. Set its **[OnSelect](controls/properties-core.md)** property to the following function:  
   ```Collect(Destinations, {Cities:City!Text, States:States!Text})```  
   
    It should look like the following:  
    ![][11]  
   
    > [!NOTE]
> You can use this same function to add additional columns to this collection. For example, you can add another text-input control for Country to add a Countries column:
   
    `Collect(Destinations, {Cities:City!Text, States:States!Text}, {Countries:Country!Text})`
7. Rename the button control **AddCityStateButton**, and set its **[Text](controls/properties-core.md)** property to **Add City and State**:  
   ![][12]  

In these steps, you added a **Cities** column and a **States** column to the **Destinations** collection. The button control adds these new text items to your collection. Now, see what you created:

1. Select Preview:  
   ![][7]  
2. Type some text into the City and State boxes, and then select the **Add City and State** button.
3. Add a few more cities and states.
4. Press the **Esc** key to close the Preview window.
5. To see the items you added to the Destinations collection, select the **File** tab, and then select **Collections**:  
   ![][13]

## Add columns to a collection
There are a few sections in this walk-through. When complete, you'll know how to import data into your collection, create a gallery that shows data in a price list, and use a slider control that determines the quantity of a product.

### Import the price list and create the collection
1. Download the [PriceList](http://pwrappssamples.blob.core.windows.net/samples/PriceList.zip) zip file.
2. On the **Home** tab, add a new screen.
3. On the **Insert** tab, select **Controls**, and then select **Import**:  
   ![][14]  
4. On the **Action** tab, select **OnSelect**. Enter the following function:  
   
    ```Collect(PriceList, Import1!Data)```  
5. Preview your app. Select the **Import Data** button, select the PriceList.zip file, and select **Open**.
6. Close the Preview window.
7. Select the **File** tab, and select **Collections**. The PriceList items you imported are listed:  
   ![][15]

### Add the gallery to show the collection items
1. Go back to your designer.
2. On the **Insert** tab, select **Gallery**, scroll down to **Custom Galleries**, and then select **Portrait**:    
   ![][16]  
3. Rename the gallery to **PriceGallery** and set the **[Items](controls/properties-core.md)** property to **PriceList**:  
   ![][18]  
4. Move the PriceList gallery below the **Import Data** control. Select the gallery borders and use click-and-drag to resize the gallery so three squares are shown.
5. In the gallery, select the first square, and add three labels (**Insert** tab > **Label**).
6. Resize and arrange the labels in a row near the top of the first square. Your gallery looks similar to the following:  
   ![][19]
7. Set the **[Text](controls/properties-core.md)** property of each label to the following expression:  
   
   | Label | Set Text property to |
   | --- | --- |
   | Label1 |``ThisItem!Name`` |
   | Label2 |``Text(ThisItem!Price, "$#")`` |
   | Label3 |``ThisItem!Maker`` |
   
    When you do this, the labels are automatically updated with the name, price, and maker values within the PriceList collection.
8. Resize the labels and the gallery to remove any extra spaces. Your screen look similar to the following:  
   ![][17]

### Add the quantity slider and update the collection
1. On the **Insert** menu, select **Controls**, and select **Slider**. Rename the slider to **OrderQty**, and move it under the gallery.
2. Add a button, set its **[Text](controls/properties-core.md)** property to **Add**, and move it under the **OrderQty** slider. Your app looks similar to the following:  
   ![][20]
3. Set the **[OnSelect](controls/properties-core.md)** property of the **Add** button to the following expression:  
   
    ```Collect(OrderList, {Name:PriceGallery!Selected!Name, Qty:OrderQty!Value, Cost:OrderQty!Value*LookUp(PriceList, PriceGallery!Selected!Name in Name, Price)});SaveData(OrderList, "orderfile")```  
   
    > [!NOTE]
> When you select this button later in this procedure, you'll create and save a collection named **OrderList**. The collection will contain the name of a product that you enter in the gallery, a quantity that you choose with the slider, and the total cost calculated by multiplying the quantity by the price of the product.
4. Select the **Screen** tab and set the **[OnVisible](controls/control-screen.md)** property to the following expression:  
   
    ```If(IsEmpty(PriceList), LoadData(PriceList, "pricefile"));If(IsEmpty(OrderList), LoadData(OrderList, "orderfile"))```

Now, see what you created:

1. Open **Preview**.
2. Select a product in the gallery, move the slider to your desired quantity, and then select the **Add** button.  
   
   > [!IMPORTANT]
   > When you select a product, that product is not highlighted to indicate you selected it. When we created the gallery, we didn't add this functionality. Know that clicking the product does select it.  
   > 
   > 
3. Repeat these steps to add a couple more products. Press **ESC** to close the Preview window.
4. On the **File** tab, select **Collections** to display a preview of the **OrderList** collection you created:  
   ![][21]

> [!TIP]
> To remove all items from the order list, add a button, set its **[Text](controls/properties-core.md)** property to **Clear**, and set its **[OnSelect](controls/properties-core.md)** property to the following expression:  
> ```Clear(OrderList);SaveData(OrderList, "orderfile")```  
> To remove one item at a time, show the **OrderList** collection in a gallery, and then set the **[OnSelect](controls/properties-core.md)** property of a label in that gallery to the following expression:  
> ```Remove(OrderList, ThisItem);SaveData(OrderList, "orderfile")```
> 
> 

## Tips and Tricks
* At anytime, you can select the Preview button (![][7]) to view your charts, and to see how they look with data.
* When designing your app, you can re-size the controls and move them around using click-and-drag.

## What you learned
In this topic, you:

* Used the Collect() function to create a collection within your app.
* You added a button control and when selected, the button adds new items to your collection.
* Used a listbox to add items to your collection.
* Added a slider control to update items within the collection.

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
[17]: ./media/create-update-collection/resizedgallery.png
[18]: ./media/create-update-collection/galleryitems.png
[19]: ./media/create-update-collection/gallerylabels.png
[20]: ./media/create-update-collection/slider.png
[21]: ./media/create-update-collection/existingcollectionsorderlist.png
[22]: ./media/create-update-collection/listbox.png
