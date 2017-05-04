<properties
	pageTitle="SaveData and LoadData functions | Microsoft PowerApps"
	description="Reference information, including syntax, for the SaveData and LoadData functions in PowerApps"
	services=""
	suite="powerapps"
	documentationCenter="na"
	authors="gregli-msft"
	manager="anneta"
	editor=""
	tags=""/>

<tags
   ms.service="powerapps"
   ms.devlang="na"
   ms.topic="article"
   ms.tgt_pltfrm="na"
   ms.workload="na"
   ms.date="11/07/2015"
   ms.author="gregli"/>

# SaveData and LoadData functions in PowerApps #

Saves and re-loads a [collection](../working-with-data-sources.md#collections).

## Description ##

The **SaveData** function stores a collection for later use under a name.  

The **LoadData** function re-loads a collection by name that was previously saved with **SaveData**. You can't use this function to load a collection from another source.  

**LoadData** doesn't create the collection; the function only fills an existing collection. You must first create the collection with the correct [columns](../working-with-tables.md#columns) by using **[Collect](function-clear-collect-clearcollect.md)**.

Storage is encrypted and in a private location on the local device, isolated from other users and other apps.  

## Syntax ##

**SaveData**( *Collection*, *Name* )<br>**LoadData**( *Collection*, *Name* [, *Ignore_non_existent_file* ])

- *Collection* - Required.  Collection to be stored or loaded.
- *Name* - Required.  Name of the storage. You must use the same name to save and load the same set of data. The name space isn't shared with other apps or users.
- *Ignore_non_existent_file* - Optional. Indicates whether **LoadData** function should ignore errors when it is unable to locate a matching file. Errors will be displayed when set to false. Setting this parameter to true is useful for Offline scenarios where **SaveData** may create a file if the **Connection.Connected** status is false.

## Examples ##
| Formula | Description | Result |
|---------|-------------|--------|
| **  If(Connection.Connected, ClearCollect(LocalTweets, Twitter.SearchTweet("PowerApps", {maxResults: 100})),LoadData(LocalTweets, "Tweets", true))** | If the device is connected, load the Collection LocalTweets from the Twitter service else **LoadData** to LocalTweets from the local file cache. | The content is rendered regardless of the connection status of the device. |
| **  SaveData(LocalTweets, "Tweets")** | Save the LocalTweets collection as local file cache on the device | Data that can be loaded into a Collection using **LoadData**. |
