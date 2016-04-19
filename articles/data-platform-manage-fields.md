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

# Manage Fields in a Table

In PowerApps, each table has a set of fields. The table definition and field definitions together represents the schema of the table. This article describes how to manage fields in a table.

## Fields overview

Each field has the following properties you can specify.

| Property | Description |
|----------|-------------|
| Field name | The name of the field. It's unique within a table. It serves as the identifier of the field which you can use to reference the field in PowerApps formula. |
| Display name | The display name of field. It will be used when showing a field in any PowerApps UI. |
| Data type | What type of data this field stores. For each data type, there may be additional properties to configure. For a full list of supported data types, please go [here](). To learn how to manage fields in a table, please go [here](). |
| Required | Whether this field is required for a record or not. |
| Unique | Whether the value of this field needs to be unique for a record or not. |

There are three kinds of fields:

### System fields

All tables, standard and custom have a set of read-only fields provided by the system. These fields cannot be changed or deleted. The value will also be assigned by the system automatically. Following is a list of the most important system fields:

- CreatedDateTime: the date and time when a record was created.
- ModifiedDateTime: the date and time when a record was last modified.

For a full list of system fields, please go [here]().

### Standard fields

These are fields in the standard tables provided by the system. These fields cannot be changed or deleted. For a full list of standard tables and corresponding standard fields, please go [here]().

### Custom fields

These are fields created by you. You can create custom fields in both standard and custom tables. In addition to the name and display name, all fields must be defined as a particular data type. Following is a list of the most important data types PowerApps supports today.

- Number Sequence: a system generated read-only sequence number. Usually used as the record unique ID.
- Text: text of various lengths.
- Number: number.
- Boolean: true or false.
- DateTime: date and time.
- Enumeration: one value from a list of values.
- Currency: numeric value representing money.
- Email: text value representing email.
- Phone: text value representing phone number.
- URL: text value representing URL.
- Location: location by latitude and longitude.

For a full list of supported data types, please go [here](). To learn how to manage fields in a table, please go [here]().

## Browse fields of a table

To browse all the fields of a table, following are the steps:

1. Login to [PowerApps portal]() with your organization's account.
2. Click the **Manage** tab on the left hand navigation pane. Then Click **Tables** to navigate to the table management page.
3. Find the table you need. You can search for it in the search bar on the top.
4. Click the table to navigate to the fields page where it will show all the fields of the table.

## Create a field

To create a field, following are the steps:

1. Navigate to the fields page.
2. Click **Add field** button. This will add a new row to the bottom of the fields grid where you can enter the field information.
3. Provide the following information for the new field:
	1. Field name: this is the technical name of the field, serving as the identifier of the field in the platform. You will use it to reference the field in PowerApps formulas.
	2. Display name: this is the display name of the field. When creating an app using this field, it will be used as the label of the filed in the app UI by default.
	3. Type: this is the data type of the field. Depends on the type you choose, there may be additional information you need to provide.
	4. Unique value: specify whether the value of this field needs to be unique for a record. By default no.
	5. Required: specify whether the value of this field needs to be required for a record. By default no.

## Update a field

To update a field, following are the steps:

1. Navigate to the fields page.
2. In the fields grid, choose the field you want to update and click anywhere in that row. This will expand the row for you to update the field information.
3. Update the field information in the expanded editor.
4. If you want to undo the change, click the **Undo** button on the right hand side of the row. This will undo all the changes you have made to this field.

## Delete a field

To delete a field, following are the steps:

1. Navigate to the fields page.
2. In the fields grid, choose the field you want to update and click the **Delete** button on the right hand side of the row.
3. This will gray out the field to indicate that you've chosen to delete it from the table.

## Save changes

Once you have done all the changes, you need to click the **Save** button to commit them. This will submit all the changes you've made. Before you do this, all the changes are kept in the browser which hasn't taken effect yet.

You'll see a modal dialog showing progress of the operation. Please do not navigate to other parts of the portal or close the browser at this point. Once the operation is finished, it will either return successfully or fail with detail error messages indicating the issues and how you can fix them.

## Restrictions and best practices

Managing fields in a meaningful way can be a challenging task. Following are some restrictions and best practices to keep in mind.

### Standard table v.s. custom table

You cannot make any breaking changes to any standard table, including:

1. Changing or deleting any system and standard fields.
2. Adding any new field which is required.

This is because standard tables serve as a baseline so that every organization and user has a common understanding of how these standard tables work.

You have much more flexibility with custom tables since it's only for your own organization. But it's also a good idea to not making breaking changes to them once they are used in some apps. Otherwise, the apps which use them may break.

### Important field settings

A few of field settings are important to get right at the beginning. This is because either you cannot change them later or changing them later may introduce big impacts.

1. Field name: you cannot change it once the field is created.
2. Type: you can change it after the field is created. But there are some nuances
	1. If you don't have any data stored in the table yet, you can change the type freely.
	2. If you have some data stored in the table already, changing type may impact the data. For example, if you are changing from Text to Number, it may fail since the data in the table may not be in the format of Number. However, changing from Number to Text is OK.
	3. Regardless of whether you have data stored in the table or not, such change may impact or even break apps if there are some using the table already.
3. Unique value: you can change it after the field is created. But there are some nuances
	1. If you don't have any data stored in the table yet, you can change it from true to false or false to true.
	2. If you have some data stored in the table already, you can change it from true to false but not always from false to true. It depends on whether the value of this field for all records are already unique or not.
	3. Regardless of whether you have data stored in the table or not, such change may impact or even break apps if there are some using the table already, especially when you change it from false to true.
4. Required: you can change it after the field is created. But there are some nuances
	1. If you don't have any data stored in the table yet, you can change it from true to false or false to true.
	2. If you have some data stored in the table already, you can change it from true to false but not always from false to true. If all the records in the table have value for this field, then changing from false to true is fine. Otherwise, you cannot do that.
	3. Regardless of whether you have data stored in the table or not, such change may impact or even break apps if there are some using the table already, especially when you change it from false to true.

## Next steps

Now you've learned how to manage fields in a table. Next, you'll learn how to build relationships between two tables.