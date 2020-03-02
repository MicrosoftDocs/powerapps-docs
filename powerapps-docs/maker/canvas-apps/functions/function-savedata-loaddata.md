---
title: SaveData and LoadData functions | Microsoft Docs
description: Reference information, including syntax, for the SaveData and LoadData functions in Power Apps
author: gregli-msft
manager: kvivek
ms.service: powerapps
ms.topic: reference
ms.custom: canvas
ms.reviewer: tapanm
ms.date: 01/31/2019
ms.author: gregli
search.audienceType: 
  - maker
search.app: 
  - PowerApps
---
# SaveData and LoadData functions in Power Apps
Saves and re-loads a [collection](../working-with-data-sources.md#collections) from a local device.

## Description
The **SaveData** function stores a collection for later use under a name.  

The **LoadData** function re-loads a collection by name that was previously saved with **SaveData**. You can't use this function to load a collection from another source.  

Use these functions to improve app-startup performance by caching data in the **[App.OnStart](../controls/control-screen.md#additional-properties)** formula on a first run and then re-loading the local cache on subsequent runs. You can also use these functions to add [simple offline capabilities](../offline-apps.md) to your app.

You can't use these functions inside a browser, either when authoring the app in Power Apps Studio or when running the app in the web player. To test your app, run it in Power Apps Mobile on an iPhone or Android device.

These functions are limited by the amount of available app memory because they operate on an in-memory collection. Available memory can vary depending on the device and operating system, the memory that the Power Apps player uses, and the complexity of the app in terms of screens and controls. If you store more than a few megabytes of data, test your app with expected scenarios on the devices on which you expect the app to run. You should generally expect to have between 30 and 70 megabytes of available memory.  

These functions depend on the collection being implicitly defined with the presence of a **[Collect](function-clear-collect-clearcollect.md)** or **[ClearCollect](function-clear-collect-clearcollect.md)** function call in any formula within your app.  You do not actually need to call **Collect** or **ClearCollect** to load data into the collection in order to define it, which is the common case when using **LoadData** after a previous **SaveData**.  All that is needed is the presence of these functions in a formula to implicitly define the structure of the collection.  For more information see [creating and removing variables](../working-with-variables.md#create-and-remove-variables).

The loaded data will be appended to the collection. Use the **[Clear](function-clear-collect-clearcollect.md)** function before calling **LoadData** if you want to start with an empty collection.

The device's built in app sandbox facilities are used to isolate saved data from other apps.  The device may also encrypt the data or use a mobile device management tool such as [Microsoft Intune](https://www.microsoft.com/en-us/microsoft-365/enterprise-mobility-security/microsoft-intune) to encrypt.

## Syntax
**SaveData**( *Collection*, *Name* )<br>**LoadData**( *Collection*, *Name* [, *IgnoreNonexistentFile* ])

* *Collection* - Required.  Collection to be stored or loaded.
* *Name* - Required.  Name of the storage. You must use the same name to save and load the same set of data. The name space isn't shared with other apps or users.
* *IgnoreNonexistentFile* - Optional. A Boolean value indicating what to do if the file does not already exist.  Use *false* (default) to return an error and *true* to suppress the error.   

## Examples

| Formula | Description | Result |
| --- | --- | --- |
| **SaveData( LocalCache, "MyCache" )** | Save the **LocalCache** collection to the user's device under the name "MyCache", suitable for **LoadData** to retrieve later. | Data is saved to the local device. |
| **LoadData( LocalCache, "MyCache" )** | Loads the **LocalCache** collection from the user's device under the name "MyCache", previously stored with a call to **SaveData**.  | Data is loaded from the local device. |   

### Simple offline example

This very simple example captures and stores the names and pictures of everyday items while offline.  It stores the information in the device's local storage for later use, allowing the app to be closed or the device to restart without losing data.  

You must have a device to work through this example as it uses the **LoadData** and **SaveData** functions that do not operate when in a web browser.

1. Create a blank canvas app with a tablet layout.  For more details read [creating an app from a template](../get-started-test-drive.md) and select **Tablet layout** under **Blank app**.  

1. Add a [**Text input**](../controls/control-text-input.md) control and a [**Camera**](../controls/control-camera.md) control and arrange them roughly as shown:
    > [!div class="mx-imgBorder"]  
    > ![A text input and camera control added to a blank screen](media/function-savedata-loaddata/simple-text-camera.png)

1. Add a [**Button**](../controls/control-button.md) control.

2. Double click the button control to change the button text to **Add Item** (or modify the **Text** property).

3. Set the **OnSeelct** property of the button control to this formula which will add an item to our collection:
    ```powerapps-dot
    Collect( MyItems, { Item: TextInput1.Text, Picture: Camera1.Photo } )
    ```
    > [!div class="mx-imgBorder"] 
    > ![A button control added with the text "Add Item" and the OnSelect property set](media/function-savedata-loaddata/simple-additem.png)

1. Add another **Button** control.

2. Double click the button control to change the button text to **Save Data** (or modify the **Text** property).

3. Set the **OnSeelct** property of the button control to this formula in order to save our collection to the local device:
    ```powerapps-dot
    SaveData( MyItems, "LocalSavedItems" )
    ```
    > [!div class="mx-imgBorder"] 
    > ![A button control added with the text "Save Data" and the OnSelect property set](media/function-savedata-loaddata/simple-savedata.png)

	It is tempting to test the button, and it won't hurt anything if you want to try, but you will only see an error as we are authoring in a web browser.  You must first save the app and open on a device before we can test this formula which we will do in the steps to follow.

1. Add a third **Button** control.

2. Double click the button control to change the button text to **Load Data** (or modify the **Text** property).

3. Set the **OnSeelct** property of the button control to this formula in order to load our collection from the local device:
    ```powerapps-dot
    LoadData( MyItems, "LocalSavedItems" )
    ``` 
    > [!div class="mx-imgBorder"] 
    > ![A button control added with the text "Load Data" and the OnSelect property set](media/function-savedata-loaddata/simple-loaddata.png)

1. Add a [**Gallery**](../controls/control-gallery.md) control with a Vertical layout that includes a picture and text areas: 
    > [!div class="mx-imgBorder"] 
    > ![Gallery variety selection, "Vertical" selected with image and text areas](media/function-savedata-loaddata/simple-gallery-add.png)

1. When prompted, select the **MyItems** collection as the data source for this gallery.  This will set the **Items** property of the **Gallery** control: 
    > [!div class="mx-imgBorder"] 
    > ![Gallery selection of data source](media/function-savedata-loaddata/simple-gallery-collection.png)
    The image control in the gallery template should default its **Image** property to **ThisItem.Picture** and the label controls should both default their **Text** properties to **ThisItem.Item**.  Check these formulas if after adding items in the following steps you don't see anything in the gallery. 

1. Position the control to the right of the other controls: 
    > [!div class="mx-imgBorder"] 
    > ![Gallery re-positioned to the right of the screen](media/function-savedata-loaddata/simple-gallery-placed.png)

1. Save your app.  If it is the first time it has been saved, there is no need to publish it; if not, also publish the app.

1. Open your app on a device such as a phone or tablet.  **SaveData** and **LoadData** cannot be used in Studio or in a web browser.  Refresh your app list if you don't see your app immediately, it can take a few seconds for the app to appear on your device.  Signing out and back in to your account can help too.
    > [!div class="mx-imgBorder"] 
    > ![App running with no items added](media/function-savedata-loaddata/simple-mobile.png) 
    Once your app has been downloaded, you can disconnect from the network and run the app offline.

1. Enter the name and take a picture of an item.

2. Select the **Add Item** button.  Repeat adding items a couple of times to load up your collection.
    > [!div class="mx-imgBorder"] 
    > ![App running with three items added](media/function-savedata-loaddata/simple-mobile-with3.png) 

1. Select the **Save Data** button.  This will save the data in your collection to your local device.

1. Close the app.  You collection in memory will be lost including all item names and pictures, but they will still be there in the device's storage.

1. Launch the app again.  The collection in memory will again show as empty in the gallery.
    > [!div class="mx-imgBorder"] 
    > ![App again running with no items added](media/function-savedata-loaddata/simple-mobile.png) 

1. Select the **Load Data** button.  The collection will be repopulated from the stored data on your device and your items will be back in the gallery.  Note that the collection was empty before this button calls the **LoadData** function; there was no need to call **Collect** or **ClearCollect** before loading the data from storage.
    > [!div class="mx-imgBorder"] 
    > ![App running with three items restored after calling the LoadData function](media/function-savedata-loaddata/simple-mobile-load1.png) 

1. Select the **Load Data** button again.  The stored data will be appended to the end of the collection and a scroll bar will appear on the gallery.  If you would like to replace rather than append, use the **Clear** function first to clear out the collection before calling the **LoadData** function.
    > [!div class="mx-imgBorder"] 
    > ![App running with six items restored after calling the LoadData function twice](media/function-savedata-loaddata/simple-mobile-load2.png) 
 
### More advanced offline example

For a detailed example, see the article on [simple offline capabilities](../offline-apps.md).







