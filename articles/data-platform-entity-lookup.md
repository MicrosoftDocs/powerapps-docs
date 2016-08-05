<properties
	pageTitle="Entity relationships via lookup field | Microsoft Common Data Model"
	description="Build a relationship between entities by using a lookup field."
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
   ms.date="07/21/2016"
   ms.author="karthikb"/>

# Build a relationship between entities in the Common Data Model #
Data in one entity often relates to data in another entity. For example, you might have a **Customers** entity and an **Orders** entity, and the **Orders** entity might have a field to show which customer placed the order. You can use a lookup field to show data from the **Customers** entity based on which orders they placed.

If you're unfamiliar with the Common Data Model, see [Understand entities](data-platform-intro.md).

## Define a relationship ##
You can create several types of relationships from one entity to another (or between an entity and itself). Each entity can have a relationship with more than one other entity, and each entity can have more than one relationship to another entity. Some common relationship types are:

- **Normal**: This type of relationship exists between two entities.

- **Self**: This type of relationship exists between an entity and itself.

- **One-to-one**: In this type of relationship, each record in entity A can match only one record in entity B, and vice versa.

- **One-to-many**: In this type of relationship, each record in entity A can match more than one record in entity B, but each record in entity B can match only one record in entity A.

- **Many-to-many**: In this type of relationship, each record in entity A can match more than one record in entity B, and vice versa. The current release of the Common Data Model doesn't support this type of relationship.

## Add a lookup field ##
To add a lookup field to an entity, specify the field's data type as **Lookup**, and specify the entity with which you want to create a relationship.

1. On [powerapps.com](https://web.powerapps.com), click or tap **Manage** in the left navigation pane, and then click or tap **Entities**.

1. In the list of entities, click or tap an entity to display its fields.

	You can filter the list by typing one or more characters in the search bar above the list.

1. Near the top of the screen, click or tap **Add field**.

	A blank row appears at the bottom of the list of fields.

1. Specify the display name and the name of the field, and then specify **Lookup** as the data type of the field.

1. In the **Lookup entity** list, specify the entity with which you want to create a relationship.

1. Click or tap **Save** to commit the changes.

## Use a lookup field in an app ##
If you use PowerApps to [create an app automatically](data-platform-create-app.md) from an entity that contains a lookup field, it appears as a **Drop down** control that contains data from the **Title** field of the referred entity.

## Delete a record with lookup field ##
If entity A has a lookup field to entity B:

- You can delete any record in entity A without restriction.
- If a record in entity B matches one or more records in entity A, you must delete all matching records in entity A before you can delete the record in entity B.

**Note**: If entity B is a standard entity with a lookup relationship to entity A and you delete a record from entity B, all matched records in entity A are also deleted.

For information about how to delete a field, see [Manage fields](data-platform-manage-fields.md).

## Next steps ##
- [Create an app](data-platform-create-app.md)
