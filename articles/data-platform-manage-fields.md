<properties
	pageTitle="Manage custom fields in an entity | Microsoft Common Data Model"
	description="Create, read, update and delete custom fields in an entity."
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

# Manage custom fields in the Common Data Model #
In the Common Data Model, you can create and update one or more custom fields in any entity. When you create a custom field, you specify a set of properties, such as the field's name, its display name, and the type of data that it will contain.

If you're unfamiliar with the Common Data Model, see [Understand entities](data-platform-intro.md).

**Note:** Every entity contains [system fields](data-platform-create-entity.md#system-and-record-title-fields) (such as when a record was updated most recently and by whom). In addition, [standard entities](data-platform-intro.md#standard-entities) contain standard (default) fields. You can't modify or delete system or standard fields. If you create a custom field, it should provide functionality on top of these built-in fields.

## Create a field ##
1. On [powerapps.com](https://web.powerapps.com), click or tap **Manage** in the left navigation pane, and then click or tap **Entities**.

	A list of entities appears. You can show custom entities at the top of the list if you click or tap the **Type** column header. You can also filter the list by typing one or more characters in the search bar.

1. Click or tap an entity, and then click or tap **Add field** near the top of the screen.

1. Under **Display name**, specify the string of text that will identify the field to users, as [Create an app](data-platform-create-app.md) describes.

1. Under **Name**, specify the string of text by which you'll refer to the field, for example, in a formula when you build an app.

	**Important**: Specify a name that's unique, clear, and meaningful because you can't change it after you create the field.

1. Under **Type**, specify the type of data, such as **Text** or **Number**, that the field will contain.

	**Important**: Specify this property carefully because you might not be able to change it after the field contains data. For information about the types of data that you can specify, see [Understand entities](data-platform-intro.md#custom-fields).

1. If prompted, specify additional information for the data type that you specified.

1. Under **Unique**, select the check box if every record should have a unique value in this field.

1. Under **Required**, select the check box if every record should have a value in this field.

	**Important**: You can't require a custom field in a standard entity to contain data. This restriction prevents you from breaking any apps that rely on that entity.

1. Click or tap **Save** to submit your changes.

	**Important**: Your changes will be lost if you haven't saved them before you open another page in the browser or close the browser.

	When the operation finishes, you're notified that it succeeded, or an error message indicates what issues prevented success and how you can fix them.

## Update or delete a field ##
1. On [powerapps.com](https://web.powerapps.com), click or tap **Manage**, click or tap **Entities**, and then click or tap an entity.

1. In the list of fields for the entity that you selected, click or tap a field, and then follow either of these steps:

	- Change one or more properties of the field, keeping in mind these [best practices and restrictions](data-platform-manage-fields.md#best-practices-and-restrictions).

		To select the next property, press Tab. To undo all changes to a field, click or tap the ellipsis (...) for the field, and then click or tap **Undo**.

	- Delete the field by clicking or tapping its ellipsis (...) near the right edge and then clicking or tapping **Delete**.

1. Click or tap **Save** to submit your changes.

	**Important**: Your changes will be lost if you haven't saved them before you open another page in the browser or close the browser.

	When the operation finishes, you're notified that it succeeded, or an error message indicates what issues prevented success and how you can fix them.

## Best practices and restrictions ##
As you create and modify fields, keep these points in mind:

- You can't modify or delete system fields or their values.
- In a standard entity, you can't modify or delete a standard (default) field, add a field that requires data, or make any other change that could break an app that relies on that entity.
- In a custom entity, you should ensure that any changes that you make won't break any app that relies on that entity.
- You must give each custom field a name that's unique within the entity, and you can't rename a field after you create it.
- You can change the data type of any field if it doesn't yet contain data or all data in that field meets the requirements of the new data type. For example, you can change the data type of a field from **Number** to **String**, but you can't change the data type of a field from **String** to **Number** if it contains non-numerical data
- You might break an app that uses an entity if you modify a field in that entity in one or more of these ways:
	- Change the field's data type.
	- Require values if one or more records doesn't contain a value in that field.
	- Require unique values if two or more records contain the same value in that field.

## Next steps ##
- [Define relationships between entities](data-platform-entity-lookup.md)
- [Create an app using entities](data-platform-create-app.md)
