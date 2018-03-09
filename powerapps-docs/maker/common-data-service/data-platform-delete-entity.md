---
title: Delete a custom entity and clear data | Microsoft Docs
description: Delete a custom entity, and clear all data.
services: powerapps
documentationcenter: na
author: kfend
manager: kfend
editor: ''
tags: ''

ms.service: powerapps
ms.devlang: na
ms.topic: article
ms.tgt_pltfrm: na
ms.workload: na
ms.date: 12/06/2016
ms.author: kfend

---
# Delete a custom entity
You can delete custom entities, but you can't delete standard entities.

1. On [powerapps.com](https://web.powerapps.com), expand the **Common Data Service** section and click or tap **Entities** in the left navigation pane. You can filter the list of entities by typing one or more characters in the search bar above the list.
2. In the list of entities, click or tap the entity to delete, and then click or tap the trash bin button in the upper-right corner.
3. In the dialog box that appears, click or tap **Delete** to delete the entity.

>[!NOTE]
>When you delete an entity, you delete both the entity definition and all data that the entity contains.

>[!NOTE]
>You might break an app if you delete an entity that is used in that app.

>[!NOTE]
>If entity A has [lookup fields](data-platform-entity-lookup.md) to entity B, you might have to delete entity B before you can delete entity A.

