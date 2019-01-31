---
title: SaveData and LoadData functions | Microsoft Docs
description: Reference information, including syntax, for the SaveData and LoadData functions in PowerApps
author: gregli-msft
manager: kvivek
ms.service: powerapps
ms.topic: reference
ms.custom: canvas
ms.reviewer: anneta
ms.date: 01/31/2019
ms.author: gregli
search.audienceType: 
  - maker
search.app: 
  - PowerApps
---
# SaveData and LoadData functions in PowerApps
Saves and re-loads a [collection](../working-with-data-sources.md#collections).

## Description
The **SaveData** function stores a collection for later use under a name.  

The **LoadData** function re-loads a collection by name that was previously saved with **SaveData**. You can't use this function to load a collection from another source.  

Use these functions to improve app-startup performance by caching data in the **[App.OnStart](../controls/control-screen.md#additional-properties)** formula on a first run and then re-loading the local cache on subsequent runs. You can also use these functions to add [simple offline capabilities](../offline-apps.md) to your app.

You can't use these functions inside a browser, either when authoring the app in PowerApps Studio or when running the app in the web player. To test your app, run it in PowerApps Mobile on an iPhone or Android device.

These functions are limited by the amount of available app memory because they operate on an in-memory collection. Available memory can vary depending on the device and operating system, the memory that the PowerApps player uses, and the complexity of the app in terms of screens and controls. If you store more than a few megabytes of data, test your app with expected scenarios on the devices on which you expect the app to run. You should generally expect to have between 30 and 70 megabytes of available memory.  

**LoadData** doesn't create the collection; the function only fills an existing collection. You must first create the collection with the correct [columns](../working-with-tables.md#columns) by using **[Collect](function-clear-collect-clearcollect.md)**. The loaded data will be appended to the collection; use the **[Clear](function-clear-collect-clearcollect.md)** function first if you want to start with an empty collection.

Storage is encrypted and in a private location on the local device, isolated from other users and other apps.

## Syntax
**SaveData**( *Collection*, *Name* )<br>**LoadData**( *Collection*, *Name* [, *IgnoreNonexistentFile* ])

* *Collection* - Required.  Collection to be stored or loaded.
* *Name* - Required.  Name of the storage. You must use the same name to save and load the same set of data. The name space isn't shared with other apps or users.
* *IgnoreNonexistentFile* - Optional. Boolean (**true**/**false**) value that indicates whether **LoadData** function should display or ignore errors when it can't locate a matching file. If you specify **false**, errors will be displayed. If you specify **true**, errors will be ignored, which is useful for offline scenarios. **SaveData** may create a file if the device is offline (that is, if the **Connection.Connected** status is **false**).

## Examples

| Formula | Description | Result |
| --- | --- | --- |
| **If(Connection.Connected, ClearCollect(LocalTweets, Twitter.SearchTweet("PowerApps", {maxResults: 100})),LoadData(LocalTweets, "Tweets", true))** |If the device is connected, load the LocalTweets collection from the Twitter service; otherwise, load the collection from the local file cache. |The content is rendered whether the device is online or offline. |
| **SaveData(LocalTweets, "Tweets")** |Save the LocalTweets collection as a local file cache on the device. |Data is saved locally so that **LoadData** can load it into a collection. |

