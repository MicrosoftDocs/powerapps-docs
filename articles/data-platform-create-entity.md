<properties
	pageTitle="Create a custom entity | Microsoft Common Data Model"
	description="Create a custom entity based on another entity or from scratch."
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
   ms.date="08/01/2016"
   ms.author="karthikb"/>

# Create a custom entity in the Common Data Model
Create a custom entity to store data that's specific to your organization, and show that data by developing an app that refers to the entity.

Create an entity:

- from scratch so that it contains only [four system fields and a record title field](data-platform-create-entity.md#system-and-record-title-fields) by default
- based on another entity by copying its fields and settings but not its data

Either way, PowerApps automatically stores and helps secure the data. After you create an entity, you can [create or modify one or more of its fields](data-platform-manage-fields.md) and [build relationships between entities](data-platform-entity-lookup.md).

**Note**: Before you create an entity, see the [list of standard entities](data-platform-intro.md#standard-entities), which cover common scenarios such as accounts and contacts. Save yourself some time by starting with one of these entities if it meets your needs out of the box or with only minor changes.

## Create an entity ##
1. On [powerapps.com](https://web.powerapps.com), click or tap **Manage** in the left navigation pane, and then click or tap **Entities**.

1. If prompted, click or tap **Create my database**.

	A list of entities appears.

1. Perform either of these steps:

	- To duplicate an entity, click or tap the elllipsis (...) for the entity that you want to duplicate, and then click or tap **Duplicate entity**.

	The entity is created, and a list of its fields appears so that you can customize your new entity.
	- To create an entity from scratch, go to the next step.

1. Near the upper-right corner, click or tap **New Entity**.

1. Specify an **Entity name** that's clear and meaningful because you can't change it after you create the entity.

	You'll reference the entity by this name in a formula when you develop an app.

1. Specify a **Display name** and (optionally) a **Description** for your entity, and then click or tap **Next**.

1. (optional) Rename the **Title** field to something more meaningful for your data.

1. Click or tap **Create** to create the entity.

Your entity appears in the list of entities in your database. To display your entity at the top of the list, click or tap the **Type** column header. The entities will be sorted by type with all custom entities above all standard entities.

## System and record-title fields ##
All entities contain five system fields. These fields are read-only, so you can't change or delete them, and you don't assign values to them.

| System field name    | Display name     | Data type | Description |
|----------------------|------------------|-----------|-------------|
| CreatedOnDateTime    | Created Record Date        | DateTime  | The date and time when a record was created. |
| CreatedByUser        | Created By       | User      | The user who created a record.		         |
| LastModifiedDateTime | Modified Record Date | DateTime  | The date and time when a record was  most recently modified. |
| LastModifiedByUser   | Last modified By | User      | The user who most recently modified the record.        |
| RecordId | Id | Big Integer      | The unique identifier for the record.        |

If you create an entity from scratch, it also contains a custom field that's named **Title** and set as the record-title field. A record-title field is the user-friendly identifier of a record whenever you use it in an app. You can change which field is the record-title field, but every entity must have one.

## Next steps ##
- [Manage fields in an entity](data-platform-manage-fields.md)
- [Define relationships between entities](data-platform-entity-lookup.md)
- [Create an app using the Common Data Model](data-platform-create-app.md)
