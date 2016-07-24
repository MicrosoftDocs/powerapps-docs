<properties
	pageTitle="Manage fields in an entity | Microsoft Common Data Model"
	description="Create, read, update and delete fields in an entity."
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

# Manage fields in the Common Data Model#
In the Common Data Model, each entity has a set of fields. The entity definition and field definitions together define the schema of the entity.

## Overview ##
For each field, you can specify these properties.

| Property | Description |
|----------|-------------|
| Name | A string of text that identifies the field when you build a formula in PowerApps. Names of fields must be unique within an entity. |
| Display name | A string of text that you can display in an app to identify a field to users. |
| Data type | The type of data, such as **Text** or **Date**, that this field stores. Some data types have additional properties to configure. For a list of data types, see [Understand entities](data-platform-intro.md). |
| Unique | Whether the value of this field must be unique across all records. |
| Required | Whether this field must contain data. |

Entities can contain system fields, standard fields, custom fields, or a combination of these types of fields.

### System fields ###
You can't change or delete system fields, which all entities contain, or the value of any of those fields. For a full list of system fields, see [Create an entity](data-platform-create-entity), but these are the most important:

- CreatedOnDateTime: the date and time when a record was created.
- LastModifiedDateTime: the date and time when a record was modified most recently.

### Standard fields ###
You can't change or delete standard fields, which standard entities contain. For a list of standard entities and the fields they contain, see [Standard entities and enumeration types](data-platform-standard-entities.md).

### Custom fields ###
You can create a custom field in either a standard entity or a custom entity. For each custom field, you specify a name, a display name, and a data type. For a full list of data types, see [Understand entities](data-platform-intro.md), but these are the most important:

- Text: A string of no more than 128 characters.
- Number: A number.
- Boolean: A value that indicates true or false.
- DateTime: A date and time.
- Enumeration: One value from a list of values.
- Image: An image.

## Display the fields of an entity ##
1. On [powerapps.com](https://web.powerapps.com), click or tap **Manage** in the left navigation pane, and then click or tap **Entities**

1. In the list of entities, click or tap an entity to display its fields.

	You can filter the list of entities by typing one or more characters in the search bar above the list.

## Create a field ##
1. [Display the fields of an entity](data-platform-manage-fields.md#display-the-fields-of-an-entity), and then click or tap **Add field** in the upper-right corner.

	A blank row appears at the bottom of the list of fields.

1. Provide this information for the new field:

	- **Display name**: Specify a string of text that identifies the field to users of an app, as [Creating an app](data-platform-create-app.md) describes.

	- **Name**: Specify a string of text that identifies the field in a formula when you build an app.

	- **Type**: Specify the kind of data that the field will contain. For some data types, you must provide additional information.

	- **Unique value**: Specify whether each record must contain a unique value in this field. By default, values in a field don't need to be unique.

	- **Required**: Specify whether each record must contain a value in this field. By default, fields don't need to contain values.

## Update a field ##
1. [Display the fields of an entity](data-platform-manage-fields.md#display-the-fields-of-an-entity), and then click or tap the field that you want to update.

1. Update the information for the selected field.

	You can select the next property by pressing Tab.

To undo all changes to a field, click or tap the ellipsis (...) for the field, and then click or tap **Undo**.

## Delete a field ##
1. [Display the fields of an entity](data-platform-manage-fields.md#display-the-fields-of-an-entity).

1. Click or tap the ellipsis (...) for the field that you want to delete.

1. Click or tap **Delete**.

## Save your changes ##
When you finish making changes, click or tap **Save** to submit them.

**Important**: Your changes will be lost if you haven't saved them before you open another page in the browser or close the browser.

When the operation finishes, you're notified that it succeeded, or an error message indicates what issues prevented success and how you can fix them.

## Restrictions and best practices ##
For best results in managing fields, keep in mind the restrictions and recommendations in this section.

### Standard entity vs. custom entity ##
You can't make any breaking changes to any standard entity, such as adding a required field or changing or deleting a system or standard field. Standard entities serve as a baseline so that everyone shares an understanding of how they work.

You can make more kinds of changes in custom entities because they serve only your organization. But you should also avoid making breaking changes to custom entities after they're used in one or more apps. Otherwise, those apps might stop working properly.

### Important field settings ###
A few field settings are important to get right at the beginning. This is because either you can't change them later or changing them later might require significant updates to your app.

- **Field name**: You can't change the name of a field after you create the field.
- **Type**: You can change the data type of a field after you create the field, with these restrictions:
	- If the entity that contains the field doesn't contain data, you can change the field's data type freely.
	- If the entity that contains the field contains data, you might affect it if you change the data type of the field. For example, you might not be able to change the data type from **Text** to **Number**, because the data in the entity might not be in the correct format for **Number**. However, you can change the data type of a field from **Number** to **Text**.
	- If the entity that contains the field is used in an app, you might affect or break the app by changing the data type of the field.
- **Unique value**: You can change this property after you create the field, with these restrictions:
	- If the entity that contains the field doesn't contain data, you can change the value of this property from **false** to **true** or vice versa.
	- If the entity that contains the field contains data, you can always change the value of this property from **true** to **false**. You can change the value of this property from **false** to **true** only if the values of this field are already unique in all records.
	- If the entity that contains the field is used in an app, you might affect or break the app by changing the value of this property (especially if you change it from **false** to **true**).
- **Required**: You can change this property after you create the field, with these restrictions:
	- If the entity that contains the field doesn't contain data, you can change the value of this property from **false** to **true** or vice versa.
	- If the entity that contains the field contains data, you can always change the value of this property from **true** to **false**. You can change the value of this property from **false** to **true** only if all records already contain data in this field.
	- If the entity that contains the field is used in an app, you might affect or break the app by changing the value of this property (especially if you change it from **false** to **true**).

## Next steps ##
- [Define relationships between entities](data-platform-entity-lookup.md)
- [Create an app using entities](data-platform-create-app.md)
