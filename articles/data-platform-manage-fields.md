<properties
	pageTitle="Manage fields in a table"
	description="Create, read, update and delete fields in a table."
	services="powerapps"
	documentationCenter="na"
	authors="guangyang"
	manager="dwrede"
	editor=""
	tags=""/>

<tags
   ms.service="powerapps"
   ms.devlang="na"
   ms.topic="article"
   ms.tgt_pltfrm="na"
   ms.workload="na"
   ms.date="04/07/2016"
   ms.author="guayan"/>

# Manage fields in a table

In PowerApps, each table has a set of fields. The table definition and field definitions together define the schema of the table. This article describes how to manage fields in a table.

## Fields overview

Each field has the following properties that you can specify.

| Property | Description |
|----------|-------------|
| Field name | The name of the field. It's unique within a table. It serves as the identifier of the field, and you can use it to reference the field in PowerApps formula. |
| Display name | The display name of field. It will be used when a field appears in any PowerApps UI. |
| Data type | The type of data this field stores. For each data type, there might be additional properties to configure. For a full list of supported data types, see [Understand Tables in PowerApps](data-platform-intro.md). |
| Required | Whether this field is required. |
| Unique | Whether the value of this field needs to be unique across all records. |

There are three kinds of fields: system, standard, an custom.

### System fields

All tables have a set of read-only fields provided by the system. These fields cannot be changed or deleted. The value will also be assigned by the system automatically. The following is a list of the most important system fields:

- CreatedDateTime: the date and time when a record was created.
- ModifiedDateTime: the date and time when a record was last modified.

For a full list of system fields, please go [Create a Table in PowerApps](data-platform-create-table).

### Standard fields

These are fields in the standard tables provided by the system. These fields cannot be changed or deleted. For a full list of standard tables and corresponding standard fields, see [Standard tables and enumeration types](data-platform-standard-tables.md).

### Custom fields

These are the fields you've created. You can create custom fields in both standard and custom tables. In addition to the name and display name, all fields must be defined as a particular data type. The most important data types that PowerApps supports are:

- Number Sequence: A system generated read-only sequence number. Usually used as the record unique ID.
- Text: Text of various lengths.
- Number: A number.
- Boolean: True or false.
- DateTime: A date and time.
- Enumeration: One value from a list of values.
- Currency: A numeric value representing money.
- Email: A text value representing an email address.
- Phone: A text value representing a phone number.
- URL: A text value representing a URL.
- Location: A location, as defined by its latitude and longitude.

For a full list of supported data types, see [Understand Tables in PowerApps](data-platform-intro.md).

## Browse the fields of a table

To browse all the fields in a table:

1. Sign in to [PowerApps portal]() with your organization's account.
2. Click the **Manage** tab in the left navigation pane. Click **Tables** to navigate to the table management page.
3. Find the table. You can search for it in the search bar at the top.
4. Click the table to navigate to the fields page.

## Create a field

To create a field:

1. Navigate to the fields page.
2. Click the **Add field** button. This will add a new row to the bottom of the fields grid where you can enter the field information.
3. Provide the following information for the new field:
	* Field name: This name serves as the identifier of the field in the platform. You will use it to reference the field in PowerApps formulas.
	* Display name: The display name is used as the label of the filed in the app UI by default.
	* Type: The data type of the field. Depending on the type you choose, there may be additional information you need to provide.
	* Unique value: Specify whether the value of this field needs to be unique for a record. The default value is No.
	* Required: Specify whether the value of this field needs to be required for a record. The default value is No.

## Update a field

To update a field:

1. Navigate to the fields page.
2. In the fields grid, choose the field you want to update and click anywhere in that row. The row expands so that you can update the field information.
3. Update the field information in the expanded editor.
4. If you want to undo the change, click the **Undo** button on the right side of the row. This will undo all the changes you have made to this field.

## Delete a field

To delete a field:

1. Navigate to the fields page.
2. In the fields grid, choose the field you want to update and click the **Delete** button on the right side of the row.
3. This will dim the field to indicate that you've chosen to delete it from the table.

## Save your changes

After you have made all the changes, click the **Save** button to commit them. This will submit all the changes you've made. Before you do this, all the changes are kept in the browser and are not propagated to the data platform.

A progress indicator will show the progress of the operation. Do not navigate to other parts of the portal or close the browser at this point. After the operation is finished, it will either return a successful result or fail with detailed error messages indicating the issues and how you can fix them.

## Restrictions and best practices

Managing fields in a meaningful way can be a challenging task. The following are some restrictions and best practices to keep in mind.

### Standard table vs. custom table

You cannot make any breaking changes to any standard table, including:

1. Changing or deleting any system and standard fields.
2. Adding any new field that is required.

This is because standard tables serve as a baseline so that every organization and user has a common understanding of how these standard tables work.

You have much more flexibility with custom tables, because these are only for your own organization. But it's also a good idea not to make breaking changes to custom tables once they are used in some apps. Otherwise, the apps that use them might break.

### Important field settings

A few of field settings are important to get right at the beginning. This is because either you cannot change them later or changing them later might require significant updates to your app.

* **Field name**: You cannot change the field name after the field is created.
* **Type**: You can change it after the field is created, with these restrictions:
    * If you don't have any data stored in the table yet, you can change the type freely.
    * If you have some data stored in the table already, changing the type might affect the data. For example, changing from **Text** to **Number** might fail, because the data in the table might not be in the correct format for **Number**. However, changing from **Text** to **Number** will work.
    * Regardless of whether you have data stored in the table, changing the type might affect or even break apps that are using the table.
* **Unique value**: You can change the setting after the field is created, with these restrictions:
    * If you don't have any data stored in the table yet, you can change it from **true** to **false** or **false** to **true**.
    * If you have some data stored in the table already, you can change it from **true** to **false** but cannot always change it from false to true. It depends on whether the value of this field is already unique for all records.
    * Regardless of whether you have data stored in the table, the change might affect or even break apps that are using the table, especially when you change it from **false** to **true**.
* **Required**: You can change the setting after the field is created, with these restrictions:
    * If you don't have any data stored in the table yet, you can change it from **true** to **false** or **false** to **true**.
    * If you have some data stored in the table already, you can change it from **true** to false, but cannot always change it from **false** to **true**. If all the records in the table have a value for this field, changing from **false** to **true** is fine. Otherwise, you cannot do it.
    * Regardless of whether you have data stored in the table, the change might affect or even break apps that are using the table, especially when you change it from **false** to **true**.

## Next steps

You've now learned how to manage fields in a table. Next, you'll learn how to build relationships between two tables.
