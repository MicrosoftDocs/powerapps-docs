<properties
	pageTitle="PowerApps: SaveData and LoadData functions"
	description="Reference information for the SaveData and LoadData functions in PowerApps, including syntax and examples"
	services=""
	suite="powerapps"
	documentationCenter="na"
	authors="gregli-msft"
	manager="dwrede"
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

Saves and re-loads a [collection](working-with-data-sources.md#collections).

## Description ##

The **SaveData** function stores a collection for later use under a name.  

The **LoadData** function re-loads a collection by name that was previously saved with **SaveData**.  This function cannot be used to load a collection from another source.  

**LoadData** does not create the collection, it only fills it.  You must first create the collection with the correct [columns](working-with-tables.md#columns) using **[Collect](function-clear-collect-clearcollect.md)**.

Storage is encrypted and in a private location on the device, isolated from other users and other apps.  
 
## Syntax ##

**SaveData**( *Collection*, *Name* )<br>**LoadData**( *Collection*, *Name* )

- *Collection* - Required.  Collection to be stored or loaded.
- *Name* - Required.  Name of the storage.  This name must match between **SaveData** and **LoadData** calls.  The name space is not shared with other apps or users.



