<properties
	pageTitle="Manage fields in an entity | Microsoft Common Data Model"
	description="Create, read, update and delete fields in an entity."
	services="powerapps"
	documentationCenter="na"
	authors="karthikb"
	manager="dwrede"
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

# Manage fields in an entity

In the Common Data Model, each entity has a set of fields. The entity definition and field definitions together define the schema of the entity. This article describes how to manage fields in an entity.

## Fields overview

Each field has the following properties that you can specify.

| Property | Description |
|----------|-------------|
| Name | The name of the field. It's unique within an entity. It serves as the identifier of the field, and you can use it to reference the field in PowerApps formulas. |
| Display name | The display name of field. It will be used when a field appears in the app. |
| Type | The type of data this field stores. For each data type, there might be additional properties to configure. For a full list of supported data types, see [Understand entities in PowerApps](data-platform-intro.md). |
| Unique | Whether the value of this field needs to be unique across all records. |
| Required | Whether this field is required whenever records are added. |

There are three kinds of fields: system, standard, and custom.

### System fields

All entities have a set of read-only fields provided by the system. These fields cannot be changed or deleted. The value will also be assigned by the system automatically. The following is a list of the most important system fields:

- CreatedOnDateTime: the date and time when a record was created.
- LastModifiedDateTime: the date and time when a record was last modified.

For a full list of system fields, see [Create an entity in Microsoft Common Data Model](data-platform-create-entity).

### Standard fields

These are fields in the standard entities provided by the system. These fields cannot be changed or deleted. For a full list of standard entities and corresponding standard fields, see [Standard entities and enumeration types](data-platform-standard-entities.md).

### Custom fields

These are the fields you've created. You can create custom fields in both standard and custom entities. In addition to the name and display name, all fields must be defined as a particular data type. The most important data types that PowerApps supports are:

- Text: Text of 128 characters in length.
- Number: A number.
- Boolean: True or false.
- DateTime: A date and time.
- Enumeration: One value from a list of values.
- Image: An image.

For a full list of supported data types, see [Understand entities in PowerApps](data-platform-intro.md).

## Browse the fields of an entity

To browse all the fields in an entity:

1. Sign in to [PowerApps portal](https://web.powerapps.com) with your organization's account.
2. Click the **Manage** tab in the left navigation pane. Click **Entities** to navigate to the entity management page.
3. Find the entity. You can search for it in the search bar at the top.
4. Click the entity to navigate to the fields page.

## Create a field

To create a field:

1. Navigate to the fields page.
2. Click the **Add field** button. This will add a new row to the bottom of the fields grid where you can enter the field information.
3. Provide the following information for the new field:
	* Display name: The display name is used as the label of the field in the app when using app from data flow. See [creating an app using Common Data Model](data-platform-create-app.md)
	* Name: This name serves as the identifier of the field in the platform. You will use it to reference the field in PowerApps formulas.
	* Type: The data type of the field. Depending on the type you choose, there may be additional information you need to provide.
	* Unique value: Specify whether the value of this field needs to be unique for a record. The default value is No.
	* Required: Specify whether the value of this field needs to be required for a record. The default value is No.

## Update a field

To update a field:

1. Navigate to the fields page.
1. In the fields grid, choose the field you want to update and click on that column.
1. Update the field information in the column selected. You can tab into next column, if required.
1. If you want to undo the change, click on the ... menu on the right side of the row and choose the **Undo** from the menu. This will undo all the changes you have made to this field.

## Delete a field

To delete a field:

1. Navigate to the fields page.
2. In the fields grid, click on the ... menu on the right side of the field you wish to delete and choose the **Delete** action.

## Save your changes

After you have made all the changes, click the **Save** button to commit them. This will submit all the changes you've made. Before you do this, all the changes are kept in the browser and are not propagated to the Common Data Model.

Do not navigate to other parts of the portal or close the browser at this point. After the operation is finished, it will either return a successful result or fail with detailed error messages indicating the issues and how you can fix them.

## Restrictions and best practices

Managing fields in a meaningful way can be a challenging task. The following are some restrictions and best practices to keep in mind.

### Standard entity vs. custom entity

You cannot make any breaking changes to any standard entity, including:

1. Changing or deleting any system and standard fields.
2. Adding any new field that is required.

This is because standard entities serve as a baseline so that every organization and user has a common understanding of how these standard entities work.

You have much more flexibility with custom entities, because these are only for your own organization. But it's also a good idea not to make breaking changes to custom entities once they are used in some apps. Otherwise, the apps that use them might not work.

### Important field settings

A few of field settings are important to get right at the beginning. This is because either you cannot change them later or changing them later might require significant updates to your app.

* **Field name**: You cannot change the field name after the field is created.
* **Type**: You can change it after the field is created, with these restrictions:
    * If you don't have any data stored in the entity yet, you can change the type freely.
    * If you have some data stored in the entity already, changing the type might affect the data. For example, changing from *Text* to *Number* might fail, because the data in the entity might not be in the correct format for *Number*. However, changing from *Text* to *Number* will work.
    * Regardless of whether you have data stored in the entity, changing the type might affect or even break apps that are using the entity.
* **Unique value**: You can change the setting after the field is created, with these restrictions:
    * If you don't have any data stored in the entity yet, you can change it from *true* to *false* or vice-versa.
    * If you have some data stored in the entity already, you can change it from *true* to *false* but cannot always change it from *false* to *true*. This depends on whether the value of this field is already unique for all records.
    * Regardless of whether you have data stored in the entity, the change might affect or even break apps that are using the entity, especially when you change it from *false* to *true*.
* **Required**: You can change the setting after the field is created, with these restrictions:
    * If you don't have any data stored in the entity yet, you can change it from *true* to *false* or vice-versa.
    * If you have some data stored in the entity already, you can change it from *true* to *false*, but cannot always change it from *false* to *true*. This depends on whether the value of this field is present for all records.
    * Regardless of whether you have data stored in the entity, the change might affect or even break apps that are using the entity, especially when you change it from *false* to *true*.

## Next steps

- [Define relationships between entities](data-platform-entity-lookup.md)
- [Create an app using entities](data-platform-create-app.md)
