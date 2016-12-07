<properties
	pageTitle="Entity relationships via lookup field | Microsoft PowerApps"
	description="Build a relationship between entities by using a lookup field."
	services="powerapps"
	documentationCenter="na"
	authors="kfend"
	manager="kfend"
	editor=""
	tags=""/>

<tags
   ms.service="powerapps"
   ms.devlang="na"
   ms.topic="article"
   ms.tgt_pltfrm="na"
   ms.workload="na"
   ms.date="12/06/2016"
   ms.author="kfend"/>

# Build a relationship between entities
Data in one entity often relates to data in another entity. For example, you might have a **Customers** entity and an **Orders** entity, and the **Orders** entity might have a field to show which customer placed the order. You can use a lookup field to show data from the **Customers** entity based on which orders they placed. For more information, see [Entity relationships and lookup fields](https://docs.microsoft.com/en-us/common-data-service/entity-reference/relationships).

## Define a relationship ##
You can create several types of relationships from one entity to another (or between an entity and itself). Each entity can have a relationship with more than one entity, and each entity can have more than one relationship to another entity. Some common relationship types are:

- **Normal** - This type of relationship exists between two entities.

- **Self** - This type of relationship exists between an entity and itself.

- **One-to-one** - In this type of relationship, each record in entity A can match only one record in entity B, and vice versa.

- **One-to-many** - In this type of relationship, each record in entity A can match more than one record in entity B, but each record in entity B can match only one record in entity A.

- **Many-to-many** - In this type of relationship, each record in entity A can match more than one record in entity B, and vice versa. The current release of the Common Data Service doesn't support this type of relationship.

## Add a lookup field
To add a lookup field to an entity, specify the field's data type as **Lookup**, and specify the entity with which you want to create a relationship.

1. On [powerapps.com](https://web.powerapps.com), expand the **Common Data Service** section and click or tap **Entities** in the left navigation pane.
1. In the list of entities, click or tap an entity to display its fields. You can filter the list by typing one or more characters in the search bar above the list.
1. Near the top of the screen, click or tap **Add field**. A blank row appears at the bottom of the list of fields.
1. Specify the display name and the name of the field, and then specify **Lookup** as the data type of the field.
1. In the **Lookup entity** list, specify the entity with which you want to create a relationship.
1. Click or tap **Save** to commit the changes.

## Use a lookup field in an app
If you [create an app automatically](data-platform-create-app.md) from an entity that contains a lookup field, it appears as a **Drop down** control that contains data from the **Title** field of the referred entity.

## Delete a record with a lookup field
If entity A has a lookup field to entity B:

- You can delete any record in entity A without restriction.
- If a record in entity B matches one or more records in entity A, you must delete all matching records in entity A before you can delete the record in entity B.

**Note**: If entity B is a standard entity with a lookup relationship to entity A and you delete a record from entity B, all matched records in entity A are also deleted.

For information about how to delete a field, see [Manage fields](data-platform-manage-fields.md).

## Next steps ##
- [Generate an app by using a Common Data Service database](data-platform-create-app.md)
- [Create an app from scratch using a Common Data Service database](data-platform-create-app-scratch.md)
