---
title: Entity relationships via lookup field | Microsoft Docs
description: Build a relationship between entities by using a lookup field.
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
ms.date: 12/09/2016
ms.author: kfend

---
# Build a relationship between entities
Data in one entity often relates to data in another entity. For example, you might have a **Customers** entity and an **Orders** entity, and the **Orders** entity might have a lookup relation to the **Customers** entity to show which customer placed the order. You can use a lookup field to show data from the **Customers** entity for the customer who placed the order. For more information, see [Entity relationships and lookup fields](https://docs.microsoft.com/common-data-service/entity-reference/relationships).

## Define a relationship
You can create several types of relationships from one entity to another (or between an entity and itself). Each entity can have a relationship with more than one entity, and each entity can have more than one relationship to another entity. Some common relationship types are:

* **Normal** - This type of relationship exists between two entities.
* **Self** - This type of relationship exists between an entity and itself.
* **One-to-one** - In this type of relationship, each record in entity A can match only one record in entity B, and vice versa. The current release of the Common Data Service does not support this type of relationship for custom entities.
* **One-to-many** - In this type of relationship, each record in entity A can match more than one record in entity B, but each record in entity B can match only one record in entity A.
* **Many-to-many** - In this type of relationship, each record in entity A can match more than one record in entity B, and vice versa. The current release of the Common Data Service doesn't support this type of relationship.

## Add a lookup relation
To add a lookup relation to an entity, create a relation under the **Relationships** tab and specify the entity with which you want to create a relationship.

1. On [powerapps.com](https://web.powerapps.com), expand the **Common Data Service** section and click or tap **Entities** in the left navigation pane.
2. In the list of entities, click or tap an entity to display its fields. You can filter the list by typing one or more characters in the search bar above the list.
3. Near the top of the screen, click or tap **Relationships**. This tab shows you all of the relationships for the entity. Click **New relationship**.
4. On the **Create relationship** page, specify the related entity with which you want to create a relationship and then, specify the name and display name of the relation.
5. Click or tap **Save** to commit the changes. A lookup field with the same name will be automatically created.

## Use a lookup field in an app
If you [create an app automatically](data-platform-create-app.md) from an entity that contains a lookup field, it appears as a **Drop down** control that contains data from the **primary key** field of the referred entity in a collapsed state. To see two fields in the drop down when it is expanded, you must add the PrimaryId field and a second field of your choice to the **Default Lookup** field group of the related entity of the lookup relation.

## Delete a record with a lookup relation
If entity A has a lookup relation to entity B:

* You can delete any record in entity A without restriction.
* If a record in entity B matches one or more records in entity A, you must delete all matching records in entity A before you can delete the record in entity B.

> [!NOTE]
> If entity B is a standard entity with a parent relationship to entity A and you delete a record from entity A, all matched records in entity B are also deleted.

For information about how to delete a field, see [Manage fields](data-platform-manage-fields.md).

## Next steps
* [Generate an app by using a Common Data Service database](data-platform-create-app.md)
* [Create an app from scratch using a Common Data Service database](maker/data-platform-create-app-scratch.md)

