---
title: Delete a custom entity | Microsoft Docs
description: Step-by-step instructions for how to delete a custom entity and clear all data in PowerApps
author: clwesene
manager: kfile
ms.service: powerapps
ms.component: cds
ms.topic: conceptual
ms.date: 03/21/2018
ms.author: clwesene
---

# Delete a custom entity
You can delete custom entities, but you can't delete standard entities.

1. On [powerapps.com](https://web.powerapps.com?utm_source=padocs&utm_medium=linkinadoc&utm_campaign=referralsfromdoc), expand the **Data** section and click or tap **Entities** in the left navigation pane.

    ![Entity Details](./media/data-platform-cds-create-entity/entitylist.png "Entity List")

2. In the list of entities, click or tap the entity to delete, and then click or tap the **Delete entity** option from the command bar.

3. In the dialog box that appears, click or tap **Delete** to delete the entity.

>[!NOTE]
>When you delete an entity, you delete both the entity definition and all data that the entity contains. Entities and the data within them cannot be recovered if deleted.

>[!NOTE]
>You might break an app or flow if you delete an entity that is used in that app.

>[!NOTE]
>If entity A has [lookup fields](data-platform-entity-lookup.md) to entity B, you might have to delete entity B before you can delete entity A.

