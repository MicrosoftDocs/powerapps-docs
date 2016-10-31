<properties
	pageTitle="Create a custom entity | Microsoft PowerApps"
	description="Create a custom entity that is based on another entity, or from scratch."
	services="powerapps"
	documentationCenter="na"
	authors="robinarh"
	manager="robinr"
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

# Create a custom entity
You can create a custom entity to store data that is specific to your organization. You can then show that data by developing an app that refers to the entity.

There are two ways to create an entity:

- Create the entity from scratch. By default, the entity contains only [four system fields and a record title field](data-platform-create-entity.md#system-and-record-title-fields).
- Create an entity that is based on another entity, by copying the fields and settings of that entity, but not its data.

In both cases, Microsoft PowerApps automatically stores and helps secure the data. After you create an entity, you can [create or modify one or more of its fields](data-platform-manage-fields.md), and [build relationships between entities](data-platform-entity-lookup.md).

**Note:** Before you create an entity, see the [list of standard entities](data-platform-intro.md#standard-entities). These entities cover typical scenarios, such as accounts and contacts. If one of these entities will meet your requirements out of the box or after only minor changes, you can save yourself some time by starting with that entity.

## Create an entity
1. 1. On [powerapps.com](https://web.powerapps.com), expand the **Common Data Service** section and click or tap **Entities** in the left navigation pane.
1. If you haven't created a database, you need to create one. For more information, see [Create a Common Data Service database](create-database.md).
1. Near the upper-right corner, click or tap **New entity**.
1. In the **Entity name** field, enter a name for the entity. Make sure that the name is clear and meaningful, because you can't change it after you create the entity. When you develop an app, you will reference the entity by this name in a formula.
1. Specify a display name and, optionally, a description for the entity, and then click or tap **Next**.
1. Optional: Change the value in the **Title** field to something that is more meaningful for your data.
1. Click or tap **Create** to create the entity.

Your entity appears in the list of entities in your database. To show your entity at the top of the list, click or tap the **Type** column header. The entities will be sorted by type, and all custom entities will appear above all standard entities.

## System fields and the record title field
All entities have five system fields. These fields are read-only. Therefore, you can't change or delete these fields, and you don't assign values to them.

Display name         | System field name    | Data type    | Description
-------------------- | -------------------- | ------------ | -----------
Id                   | System field name    | Big Integer  | The unique identifier for the record.
Created By           | CreatedByUser        | Text         | The user who created a record.
Created Record Date  | CreatedOnDateTime    | DateTime     | The date and time when a record was created.
Last modified By     | LastModifiedByUser   | Text         | The user who most recently modified the record.
Modified Record Date | LastModifiedDateTime | DateTime     | The date and time when a record was most recently modified.

If you create an entity from scratch, it also contains a custom field that is named **Title**. This field is set as the record's **Title** field. The **Title** field value is the user-friendly identifier of a record whenever you use that record in an app. You can change which field is the **Title** field, but every entity must have a **Title** field.

## Next steps
- [Manage fields in an entity](data-platform-manage-fields.md)
- [Define relationships between entities](data-platform-entity-lookup.md)
- [Generate an app by using a Common Data Service database](data-platform-create-app.md)
- [Create an app from scratch using a Common Data Service database](data-platform-create-app-scratch.md)
