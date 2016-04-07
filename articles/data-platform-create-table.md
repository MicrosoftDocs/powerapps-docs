<properties
	pageTitle="Create a table"
	description="Create a new table from scratch or based on some existing table."
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

# Create a Table

PowerApps comes with a set of standard tables covering many common scenarios for every organization. It also allows you to create custom tables to store any type of data fitting your organization's needs. Each table will have a set of fields which you can create by yourself. You can also build relationships between two tables. After you create a custom table, you can use it in your apps the same way as standard tables. PowerApps will take care of the data storage and security automatically.

There are two ways to create a table:

- From scratch
- Based on an existing table

Either way, PowerApps will always add the following system fields to the table automatically. They are read-only fields managed by PowerApps itself so you don't need to worry about how to assign values to them in your apps. You cannot change or delete these system fields.

| Field name | Display name | Data type | Description |
|------------|--------------|-----------|-------------|
| CreatedOnDateTime | Created on | DateTime | The date and time when a record was created. |
| CreatedByUser | Created by | User | The user who created a record. |
| LastModifiedDateTime | Last modified on | DateTime | The most recent date and time when a record was modified. |
| LastModifiedByUser | Last modified by | User | The most recent user who modified the record. |

## Create a table from scratch

This will create a table with the system fields and one additional custom field. Following are the steps:

1. Login to [PowerApps portal]() with your organization's account.
2. Click the **Manage** tab on the left hand navigation pane. Then Click **Tables** to navigate to the table management page.
3. Click the **New Table** button on the top right corner of the page.
4. Enter the following information for the new table:
	a. Table name, required.
	b. Display name, required.
    c. Description, optional.
5. Choose **blank** as the table to base on. You can see the fields the new table will include by default.
6. Click the **Save** button to finish the table creation.
7. After the operation finishes, you'll be able to see the fields of the new table and make further changes right away.

The one additional custom field gets added automatically is named **Title** and is set as the table's record title field. This field will be used as the user friendly identifier of a record whenever a record is used in any app UI. Every table needs to have a record title field. You can choose to use another field later. For more information, please go [here]().

## Create a table based on an existing table

This will create a table with all the fields and settings copied from an existing table of your choice. It's very convenient if you need to create a new table which is similar to some existing table. It will only copy the table metadata rather than the data. Following are the steps:

1. Login to [PowerApps portal]() with your organization's account.
2. Click the **Manage** tab on the left hand navigation pane. Then Click **Tables** to navigate to the table management page.
3. Click the **New Table** button on the top right corner of the page.
4. Enter the following information for the new table:
	a. Table name, required.
	b. Display name, required.
    c. Description, optional.
5. Choose a table to base on in the combobox. You can see the fields the new table will include once you've chosen a base table.
6. Click the **Save** button to finish the table creation.
7. After the operation finishes, you'll be able to see the fields of the new table and make further changes right away.

## Restrictions and best practices

It's important to choose a meaningful table name at the very beginning. This is because this table name is the unique identifier of the table itself so that you can reference it in PowerApps formulas. You won't be able to change the table name after the table is created.

It's recommended to choose a meaningful display name, as well as provide useful description for a table. This information will be used in the UI where this table is displayed. You can change them later.

Before creating any new tables, it's recommended to go through the standard tables for two reasons:

1. Check if some standard tables fit your needs already. If so, use them instead of creating a new table.
2. If no standard table fits your needs exactly, see whether some table is similar enough that you can have the new table based on it. This will not only make it easier to create a new table but also help you design the new table by providing some common fields already. You can choose to add, change or delete some fields as needed.

## Next steps

Now you've learned how to create a table, following are some other articles as next steps:

- [Manage fields in a table]()
- [Define relationships between tables]()
- [Create an app using tables]()