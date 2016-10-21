<properties
	pageTitle="Delete a custom entity and clear data | Microsoft PowerApps"
	description="Delete a custom entity, and clear all data."
	services="powerapps"
	documentationCenter="na"
	authors="robinarh"
	manager="anneta"
	editor=""
	tags=""/>

<tags
   ms.service="powerapps"
   ms.devlang="na"
   ms.topic="article"
   ms.tgt_pltfrm="na"
   ms.workload="na"
   ms.date="10/18/2016"
   ms.author="robinr"/>

# Delete a custom entity
You can delete custom entities, but you can't delete standard entities.

1. On [PowerApps.com](https://web.powerapps.com), in the left navigation pane, click or tap **Entities**. You can filter the list of entities by typing one or more characters in the search bar above the list.
1. In the list of entities, click or tap the entity to delete, and then click or tap the trash bin button in the upper-right corner.
1. In the dialog box that appears, click or tap **Delete** to delete the entity.

## Notes
- When you delete an entity, you delete both the entity definition and all data that the entity contains.
- You might break an app if you delete an entity that is used in that app.
- If entity A has [lookup fields](data-platform-entity-lookup.md) to entity B, you might have to delete entity B before you can delete entity A.
