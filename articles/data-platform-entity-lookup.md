<properties
	pageTitle="Entity relationships via lookup field | Microsoft Common Data Model"
	description="Build relationships between entities using lookup field."
	services="powerapps"
	documentationCenter="na"
	authors="karthikb"
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

# Entity relationships via a lookup field

In many cases, entities need to have relationships with each other. For example, a record in *Account* entity represents an organization that might do business with your organization, and a record in the *Contact* represents a person. There is a relationship between *Account* and *Contact*, because an account needs to have a contact so that we know who to contact regarding to a particular account. A relationship like this is modeled as a lookup field in the Microsoft Common Data Model.

## Understanding relationships

A relationship is used to describe the case where you need to connect records from multiple entities together to enable your scenarios. A single relationship is set up between two entities. You can have multiple relationships to the same or different entities, which might have other relationships for themselves.

Some common relationship types are:

* **Normal**: This is a relationship from one entity to another entity.

* **Self**: This is a relationship from one entity to itself.

* **One-to-one**: This is a relationship where one record in an entity A can have no more than one matching record in entity B, and one record in entity B can have no more than one matching record in entity A.

* **One-to-many**: This is a relationship where one record in entity A can have many matching records in entity B, but a record in entity B can have only one matching record in entity A.

* **Many-to-many**: This is a relationship where one record in entity A can have many matching records in entity B, and one record in entity B can have many matching records in entity A. This will be supported by Common Data Model in the future.

## Lookup field

Microsoft Common Data Model supports entity relationships via a lookup field. A lookup field is a field in an entity with the data type specified as **Lookup**. It points to another entity which you need the relationship with.

To create a lookup field:

1. Sign in to [PowerApps portal](https://web.powerapps.com) with your organization's account.
2. Click the **Manage** tab in the left navigation pane. Click **Entities** to navigate to the entity management page.
3. Find the entity you need. You can search for it in the search bar at the top.
4. Click the entity to navigate to the fields page, which will show all the fields of the entity.
5. Click the **Add field** button. This will add a new row to the bottom of the fields grid where you can enter the field information.
6. Specify the display name and the field name.
7. For the type, choose **Lookup**.
8. In the **Lookup entity** list, select the entity you want this field to serve as a lookup to.
9. Click **Save** to commit the changes.

## Using a lookup field in PowerApps

You can use a lookup field when building an app in PowerApps.
1. Create an [app using Common Data Model](data-platform-create-app.md)
1. The lookup relationship will be modeled as a dropdown with the results populated from the Title field of the referred entity.

## Deleting a record with lookup field

If entity A has a lookup field to entity B, it affects the record delete behavior in the following ways:

* You can delete any record in entity A without restriction.
* When you a delete a record in entity B, if this record matches one or multiple records in entity A, you need to delete all the matched records in entity A first.

**Note** If entity B is a standard entity with lookup relationship, when you a delete a record in entity B all matched records in entity A are also deleted if entity A.

## Next steps
- [Create an app using Common Data Model](data-platform-create-app.md)
