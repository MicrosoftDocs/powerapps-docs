<properties
	pageTitle="Delete entity and clear data | Microsoft Common Data Model"
	description="Delete an entity from Common Data Model and clear all data"
	services="powerapps"
	documentationCenter="na"
	authors="guangyang"
	manager="erikre"
	editor=""
	tags=""/>

<tags
   ms.service="powerapps"
   ms.devlang="na"
   ms.topic="article"
   ms.tgt_pltfrm="na"
   ms.workload="na"
   ms.date="07/27/2016"
   ms.author="karthikb"/>

# Delete an entity

You can delete custom entities but not standard entities.

To delete an entity:

1. Sign in to [PowerApps portal](https://web.powerapps.com) with your organization's account.
2. Click the **Manage** tab in the left navigation pane. Click **Entities** to navigate to view the list of all entities.
3. Find the entity you need to delete. You can search for it in the search bar at the top.
4. Click the entity to navigate to the *Fields* view, which will show all the fields of the entity.
5. Click the **Delete** icon at the top.
6. Click **Delete** again in the confirmation dialog to delete the entity

**Notes**

* When you delete an entity, both the definition and the data stored in the entity will be deleted.
* Deleting an entity might break any apps using that entity.
* If the entity has lookup fields (relationships to other entities), you might not be able to delete the entity directly. You need to delete other entities it relates to first.
