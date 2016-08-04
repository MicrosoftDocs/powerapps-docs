<properties
	pageTitle="Delete a custom entity and clear data | Microsoft Common Data Model"
	description="Delete a custom entity from the Common Data Model and clear all data"
	services="powerapps"
	documentationCenter="na"
	authors="karthik-1"
	manager="erikre"
	editor=""
	tags=""/>

<tags
   ms.service="powerapps"
   ms.devlang="na"
   ms.topic="article"
   ms.tgt_pltfrm="na"
   ms.workload="na"
   ms.date="08/04/2016"
   ms.author="karthikb"/>

# Delete a custom entity from the Common Data Model #
You can delete custom entities but not standard entities.

1. On [powerapps.com](https://web.powerapps.com), click or tap **Manage** in the left navigation pane, and then click or tap **Entities**.

	You can filter the list of entities by typing one or more characters in the search bar above the list.

1. In the list of entities, click or tap the entity that you want to delete, and then click or tap the trash-can icon in the upper-right corner.

1. In the dialog box that appears, click or tap **Delete** to delete the entity.

## Notes ##
- When you delete an entity, you delete both its definition and all data in the entity.
- You might break an app if you delete an entity that's used in that app.
- If entity A has [lookup fields](data-platform-entity-lookup.md) to entity B, you might need to delete entity B before you can delete entity A.
