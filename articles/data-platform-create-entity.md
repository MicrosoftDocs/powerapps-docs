<properties
	pageTitle="Create an entity | Microsoft Common Data Model"
	description="Create an entity based on another entity or from scratch."
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

# Create an entity in Common Data Model
You can store data that's specific to your organization in a custom entity, and show that data by referring to the entity when you develop an app.

You can create an entity:

- From scratch, so that, by default, it contains only [four system fields and a record title field](data-platform-create-entity.md#system-and-record-title-fields)
- Based on another entity, by copying its fields and settings but not its data

Either way, PowerApps stores and helps secure the data automatically. After you create an entity, you can create or modify one or more of its fields and build relationships between entities.

**Note**: Before you create an entity, see [Standard entities and enumeration types](data-platform-standard-entities.md). These entities cover common scenarios, such as accounts and contacts. Save yourself some time by starting with one of these entities if any of them meets your needs out of the box or with only minor changes.

## Create an entity
1. On [powerapps.com](http://powerapps.com), select **Manage** > **Entities** in the left navigation pane.
1. Near the upper-right corner, select **New Entity**, and then specify a name, a display name, and (optionally) a description for your entity.

	**Important**: Be sure to specify a clear and meaningful name for your entity because this can't be changed later. You'll reference this name in formulas when you develop an app. The display name and the description should also be meaningful, but you can change them later.

1. In the list, perform either of these steps:
	- Select the name of an entity to create an entity with fields copied from that entity.
	- Select **basic entity** to create an entity from scratch.
1. Click **Create** to create the entity.

## System and record-title fields ##
All entities, including any that you create from scratch, contain five system fields. These fields are read-only, so you can't change or delete them, and you don't assign values to them.

| System field name    | Display name     | Data type | Description |
|----------------------|------------------|-----------|-------------|
| CreatedOnDateTime    | Created Record Date        | DateTime  | The date and time when a record was created. |
| CreatedByUser        | Created By       | User      | The user who created a record.		         |
| LastModifiedDateTime | Modified Record Date | DateTime  | The date and time when a record was  most recently modified. |
| LastModifiedByUser   | Last modified By | User      | The user who most recently modified the record.        |
| RecordId | Id | Big Integer      | The unique identifier for the record.        |


If you create an entity from scratch, it also contains a custom field named **Title** and set as the [record title field](). A record title field is the user-friendly identifier of a record whenever a record is used in an app. You can change which field is used as the Title field, but every entity must have one record title field.

## Next steps
- [Manage fields in an entity](data-platform-manage-fields.md)
- [Define relationships between entities](data-platform-entity-lookup.md)
- [Create an app using Common Data Model](data-platform-create-app.md)
