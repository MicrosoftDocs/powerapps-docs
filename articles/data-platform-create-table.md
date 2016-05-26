<properties
	pageTitle="Create a table | Microsoft PowerApps"
	description="Create a table based on another table or from scratch."
	services="powerapps"
	documentationCenter="na"
	authors="guangyang"
	manager="erikre"
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

# Create a table in PowerApps
You can store data that's specific to your organization in a custom table, and show that data by referring to the table when you develop an app. You can create a table:

- Based on another table, by copying its fields and settings but not its data
- From scratch, so that, by default, it contains only [four system fields and a record-title field](data-platform-create-table.md#system-and-record-title-fields)

Either way, PowerApps stores and helps secure the data automatically. After you create a table, you can create or modify one or more of its fields and build relationships between tables.

**Note**: Before you create a table, see [Standard tables and enumeratio types](data-platform-standard-tables.md). These tables cover common scenarios, such as accounts and contacts. Save yourself some time by starting with one of these tables if any of them meets your needs out of the box or with only minor changes.

## Create a table
1. On [powerapps.com](http://powerapps.com), select **Manage** > **Tables** in the left navigation pane.
1. Near the upper-right corner, select **New Table**, and then specify a name, a display name, and (optionally) a description for your table.

	**Important**: Be sure to specify a clear and meaningful name for your table because you can't change it later. You'll reference this name in formulas when you develop an app. The display name and the description should also be meaningful, but you can change them later.

1. In the list, perform either of these steps:
	- Select the name of a table to create a table based on that table.
	- Select **blank** to create a table from scratch.
1. Click **Save** to create the table.

## System and record-title fields ##
All tables, including any that you create from scratch, contain four system fields. These fields are read-only, so you can't change or delete them, and you don't assign values to them.

| System-field name | Display name | Data type | Description |
|------------|--------------|-----------|-------------|
| CreatedOnDateTime | Created on | DateTime | The date and time when a record was created. |
| CreatedByUser | Created by | User | The user who created a record. |
| LastModifiedDateTime | Last modified on | DateTime | The date and time when a record was  most recently modified. |
| LastModifiedByUser | Last modified by | User | The user who most recently modified the record . |

If you create a table from scratch, it also contains a custom field that's named **Title** and set as the [record-title field](). A record-title field is the user-friendly identifier of a record whenever a record is used in any app UI. You can change which field is used, but every table must have a record title field.

## Next steps
- [Manage fields in a table](data-platform-manage-fields.md)
- [Define relationships between tables](data-platform=table-lookup.md)
- [Create an app using tables](data-platform-create-app.md)
